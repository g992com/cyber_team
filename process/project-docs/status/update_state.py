#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


DEFAULT_STATE_REL_PATH = "state.yaml"

_TOP_LEVEL_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")


def _utc_now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _write_text_atomic(path: str, content: str) -> None:
    parent = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(parent, exist_ok=True)
    tmp_path = f"{path}.tmp.{os.getpid()}"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)


@dataclass
class _Lock:
    path: str
    fd: Optional[int] = None

    def __enter__(self) -> "_Lock":
        start = time.time()
        while True:
            try:
                self.fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(self.fd, str(os.getpid()).encode("utf-8"))
                return self
            except FileExistsError:
                if time.time() - start > 10.0:
                    raise RuntimeError(f"Lock busy: {self.path}")
                time.sleep(0.2)

    def __exit__(self, exc_type, exc, tb) -> None:
        try:
            if self.fd is not None:
                os.close(self.fd)
        finally:
            self.fd = None
            try:
                os.remove(self.path)
            except FileNotFoundError:
                pass


def _git_root(cwd: str) -> Optional[str]:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=cwd,
            stderr=subprocess.STDOUT,
            text=True,
        ).strip()
        if out:
            return os.path.normpath(out)
    except Exception:
        return None
    return None


def _resolve_state_path(project_root: str, state_rel_path: str) -> str:
    project_root = os.path.abspath(project_root)
    p = os.path.abspath(os.path.join(project_root, state_rel_path))
    # Refuse writing outside the detected project root (prevents multi-root mis-targeting).
    if os.path.commonpath([project_root, p]) != project_root:
        raise RuntimeError(f"Refuse path outside project root: {p} (root={project_root})")
    return p


def _parse_inline_scalar(v: str) -> Any:
    v = v.strip()
    if v in ("", "null", "NULL", "~"):
        return None
    if v in ("{}",):
        return {}
    if v in ("[]",):
        return []
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        parts = [p.strip() for p in inner.split(",")]
        out: List[str] = []
        for p in parts:
            if not p:
                continue
            if (p.startswith('"') and p.endswith('"')) or (p.startswith("'") and p.endswith("'")):
                out.append(p[1:-1])
            else:
                out.append(p)
        return out
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    return v


def _load_state_minimal(path: str) -> Dict[str, Any]:
    """
    Minimal loader for the canonical state.yaml produced by this tool/template.
    It only supports top-level `key: <inline>` pairs and ignores comments/blank lines.
    For safety, if it sees a nested mapping/list block, it refuses to proceed.
    """
    if not os.path.exists(path):
        return {}
    data: Dict[str, Any] = {}
    for raw in _read_text(path).splitlines():
        line = raw.rstrip("\n")
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("- "):
            raise RuntimeError(f"Unsupported YAML block list item in {path}. Use canonical inline values only.")
        m = _TOP_LEVEL_KEY_RE.match(line)
        if not m:
            raise RuntimeError(f"Unsupported YAML line in {path}: {line}")
        k, v = m.group(1), m.group(2)
        if v.strip() == "" and not line.endswith(":"):
            raise RuntimeError(f"Unsupported YAML line in {path}: {line}")
        # Disallow nested block values like:
        # role_updates:
        #   backend:
        # ...
        if v.strip() == "" and line.strip().endswith(":"):
            raise RuntimeError(
                f"Unsupported nested mapping for key={k} in {path}. Keep role_updates as '{{}}' for tool updates."
            )
        data[k] = _parse_inline_scalar(v)
    return data


def _dump_state_canonical(data: Dict[str, Any]) -> str:
    def _dump_inline(x: Any) -> str:
        if x is None:
            return "null"
        if x == {}:
            return "{}"
        if x == []:
            return "[]"
        if isinstance(x, list):
            def q(s: str) -> str:
                return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

            return "[" + ", ".join(q(str(i)) for i in x) + "]"
        if isinstance(x, str):
            # Quote strings that contain spaces or special chars.
            if re.search(r"[^\w\-./:]", x):
                return '"' + x.replace("\\", "\\\\").replace('"', '\\"') + '"'
            return x
        return str(x)

    keys = [
        "current_phase",
        "tailoring_snapshot",
        "completed_phases",
        "current_role",
        "updated_at",
        "role_updates",
        "project_blockers",
        "project_risks",
    ]
    out: List[str] = [
        "# Generated/updated by update_state.py (canonical inline YAML).",
        "# This file is a project runtime snapshot; keep it in the BUSINESS project repo root.",
    ]
    for k in keys:
        if k not in data:
            continue
        out.append(f"{k}: {_dump_inline(data[k])}")
    return "\n".join(out) + "\n"


def cmd_init(args: argparse.Namespace) -> int:
    state_path = args._state_path
    if os.path.exists(state_path) and not args.force:
        raise RuntimeError(f"File exists: {state_path} (use --force to overwrite)")
    data: Dict[str, Any] = {
        "current_phase": "initiation",
        "tailoring_snapshot": [],
        "completed_phases": [],
        "current_role": None,
        "updated_at": _utc_now_iso(),
        "role_updates": {},
        "project_blockers": [],
        "project_risks": [],
    }
    _write_text_atomic(state_path, _dump_state_canonical(data))
    print(f"OK: created {state_path}")
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    data = _load_state_minimal(args._state_path)
    # Keep output stable and grep-friendly.
    print(_dump_state_canonical(data), end="")
    return 0


def cmd_set_phase(args: argparse.Namespace) -> int:
    lock_path = f"{args._state_path}.lock"
    with _Lock(lock_path):
        data = _load_state_minimal(args._state_path)
        data.setdefault("completed_phases", [])
        if not isinstance(data.get("completed_phases"), list):
            raise RuntimeError("completed_phases must be an inline list, e.g. [] or [\"requirements\"]")
        data["current_phase"] = args.phase
        data["updated_at"] = _utc_now_iso()
        _write_text_atomic(args._state_path, _dump_state_canonical(data))
    print(f"OK: current_phase -> {args.phase}")
    return 0


def cmd_add_completed(args: argparse.Namespace) -> int:
    lock_path = f"{args._state_path}.lock"
    with _Lock(lock_path):
        data = _load_state_minimal(args._state_path)
        data.setdefault("completed_phases", [])
        cp = data.get("completed_phases")
        if not isinstance(cp, list):
            raise RuntimeError("completed_phases must be an inline list, e.g. [] or [\"requirements\"]")
        if args.phase not in cp:
            cp.append(args.phase)
        data["completed_phases"] = cp
        data["updated_at"] = _utc_now_iso()
        _write_text_atomic(args._state_path, _dump_state_canonical(data))
    print(f"OK: completed_phases += {args.phase}")
    return 0


def cmd_add_blocker(args: argparse.Namespace) -> int:
    lock_path = f"{args._state_path}.lock"
    with _Lock(lock_path):
        data = _load_state_minimal(args._state_path)
        data.setdefault("project_blockers", [])
        pb = data.get("project_blockers")
        if not isinstance(pb, list):
            raise RuntimeError("project_blockers must be an inline list")
        pb.append(args.text)
        data["project_blockers"] = pb
        data["updated_at"] = _utc_now_iso()
        _write_text_atomic(args._state_path, _dump_state_canonical(data))
    print("OK: blocker added")
    return 0


def cmd_add_risk(args: argparse.Namespace) -> int:
    lock_path = f"{args._state_path}.lock"
    with _Lock(lock_path):
        data = _load_state_minimal(args._state_path)
        data.setdefault("project_risks", [])
        pr = data.get("project_risks")
        if not isinstance(pr, list):
            raise RuntimeError("project_risks must be an inline list")
        pr.append(args.text)
        data["project_risks"] = pr
        data["updated_at"] = _utc_now_iso()
        _write_text_atomic(args._state_path, _dump_state_canonical(data))
    print("OK: risk added")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="update_state.py",
        description="State helper: update project root state.yaml with safety checks to avoid wrong-repo writes.",
    )
    p.add_argument(
        "--project-root",
        required=False,
        help="Project repository root. Default: detect via `git rev-parse --show-toplevel` from cwd.",
    )
    p.add_argument(
        "--state",
        default=DEFAULT_STATE_REL_PATH,
        help=f"State file path relative to project root (default: {DEFAULT_STATE_REL_PATH})",
    )

    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("init", help="Create a canonical state.yaml in project root")
    sp.add_argument("--force", action="store_true", help="Overwrite if exists")
    sp.set_defaults(func=cmd_init)

    sp = sub.add_parser("show", help="Show canonicalized state.yaml")
    sp.set_defaults(func=cmd_show)

    sp = sub.add_parser("set-phase", help="Set current_phase")
    sp.add_argument("--phase", required=True, help="Phase id (must match your phases.yaml ids)")
    sp.set_defaults(func=cmd_set_phase)

    sp = sub.add_parser("add-completed", help="Append phase id to completed_phases (dedup)")
    sp.add_argument("--phase", required=True, help="Phase id to add to completed_phases")
    sp.set_defaults(func=cmd_add_completed)

    sp = sub.add_parser("add-blocker", help="Append a project-level blocker text")
    sp.add_argument("--text", required=True, help="Blocker text (one line)")
    sp.set_defaults(func=cmd_add_blocker)

    sp = sub.add_parser("add-risk", help="Append a project-level risk text")
    sp.add_argument("--text", required=True, help="Risk text (one line)")
    sp.set_defaults(func=cmd_add_risk)

    return p


def main(argv: Optional[List[str]] = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    p = _build_parser()
    args = p.parse_args(argv)

    project_root = args.project_root or _git_root(os.getcwd())
    if not project_root:
        raise RuntimeError("Cannot detect project root (not a git repo?). Use --project-root explicitly.")
    state_path = _resolve_state_path(project_root, args.state)
    args._state_path = state_path

    if hasattr(args, "func"):
        return int(args.func(args))
    p.print_help()
    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        raise SystemExit(1)

