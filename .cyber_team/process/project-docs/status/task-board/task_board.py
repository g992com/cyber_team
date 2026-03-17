#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple


ALLOWED_STATUSES = {"todo", "doing", "blocked", "done"}
DEFAULT_INDEX_PATH = os.path.join("docs", "status", "task-index.json")
DEFAULT_CARDS_DIR = os.path.join("docs", "status", "task-cards")


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


def _load_index(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        return {"schema_version": 1, "updated_at": "1970-01-01T00:00:00Z", "tasks": []}
    raw = _read_text(path)
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON in index: {path}: {e}") from e
    if not isinstance(data, dict):
        raise RuntimeError(f"Invalid index root type (expect object): {path}")
    data.setdefault("schema_version", 1)
    data.setdefault("updated_at", "1970-01-01T00:00:00Z")
    data.setdefault("tasks", [])
    if not isinstance(data["tasks"], list):
        raise RuntimeError(f"Invalid index.tasks type (expect array): {path}")
    return data


def _save_index(path: str, data: Dict[str, Any]) -> None:
    data["updated_at"] = _utc_now_iso()
    content = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    _write_text_atomic(path, content)


def _find_task(tasks: List[Dict[str, Any]], task_id: str) -> Tuple[int, Dict[str, Any]]:
    for i, t in enumerate(tasks):
        if t.get("task_id") == task_id:
            return i, t
    raise RuntimeError(f"Task not found: {task_id}")


def _validate_status(status: str) -> None:
    if status not in ALLOWED_STATUSES:
        raise RuntimeError(f"Invalid status: {status}. Allowed: {', '.join(sorted(ALLOWED_STATUSES))}")


def _ensure_card_exists(card_path: str) -> None:
    if not os.path.exists(card_path):
        raise RuntimeError(f"Card file not found: {card_path}")


def cmd_init(args: argparse.Namespace) -> int:
    os.makedirs(os.path.dirname(args.index) or ".", exist_ok=True)
    os.makedirs(args.cards_dir, exist_ok=True)
    if not os.path.exists(args.index):
        data = {"schema_version": 1, "updated_at": "1970-01-01T00:00:00Z", "tasks": []}
        _save_index(args.index, data)
    print(f"OK: index={args.index}")
    print(f"OK: cards_dir={args.cards_dir}")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    data = _load_index(args.index)
    role = args.role
    statuses = set(args.status.split(",")) if args.status else None
    if statuses:
        for s in statuses:
            _validate_status(s)
    rows = []
    for t in data["tasks"]:
        if role and t.get("owner_role") != role:
            continue
        if statuses and t.get("status") not in statuses:
            continue
        rows.append(t)
    rows.sort(key=lambda x: (x.get("updated_at") or "", x.get("task_id") or ""), reverse=True)
    out = []
    for t in rows:
        out.append(
            {
                "task_id": t.get("task_id"),
                "status": t.get("status"),
                "owner_role": t.get("owner_role"),
                "card_path": t.get("card_path"),
                "phase_id": t.get("phase_id"),
                "updated_at": t.get("updated_at"),
            }
        )
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


def cmd_claim(args: argparse.Namespace) -> int:
    lock_path = f"{args.index}.lock"
    with _Lock(lock_path):
        data = _load_index(args.index)
        idx, task = _find_task(data["tasks"], args.task)
        if args.by and task.get("owner_role") != args.by:
            raise RuntimeError(f"Cannot claim task owned by {task.get('owner_role')}; you are {args.by}")
        status = task.get("status")
        if status != "todo":
            raise RuntimeError(f"Cannot claim task in status={status}; expect todo")
        task["status"] = "doing"
        task["updated_by"] = args.by
        task["updated_at"] = _utc_now_iso()
        data["tasks"][idx] = task
        _save_index(args.index, data)
    print(f"OK: {args.task} -> doing")
    return 0


def cmd_update(args: argparse.Namespace) -> int:
    _validate_status(args.status)
    lock_path = f"{args.index}.lock"
    with _Lock(lock_path):
        data = _load_index(args.index)
        idx, task = _find_task(data["tasks"], args.task)
        if args.by and task.get("owner_role") != args.by:
            raise RuntimeError(f"Cannot update task owned by {task.get('owner_role')}; you are {args.by}")
        if args.status == "blocked":
            if not args.blocker:
                raise RuntimeError("blocked requires --blocker")
            task["blocker"] = args.blocker
        else:
            if "blocker" in task:
                task.pop("blocker", None)
        task["status"] = args.status
        if args.add_result:
            task.setdefault("result_links", [])
            if not isinstance(task["result_links"], list):
                raise RuntimeError("result_links must be array")
            task["result_links"].append(args.add_result)
        task["updated_by"] = args.by
        task["updated_at"] = _utc_now_iso()
        data["tasks"][idx] = task
        _save_index(args.index, data)
    print(f"OK: {args.task} -> {args.status}")
    return 0


def cmd_add(args: argparse.Namespace) -> int:
    _validate_status(args.status)
    _ensure_card_exists(args.card)
    lock_path = f"{args.index}.lock"
    with _Lock(lock_path):
        data = _load_index(args.index)
        try:
            _find_task(data["tasks"], args.task)
            raise RuntimeError(f"Task already exists: {args.task}")
        except RuntimeError:
            pass
        t: Dict[str, Any] = {
            "task_id": args.task,
            "status": args.status,
            "owner_role": args.owner,
            "card_path": args.card,
            "phase_id": args.phase,
            "updated_by": args.by,
            "updated_at": _utc_now_iso(),
        }
        if args.status == "blocked":
            if not args.blocker:
                raise RuntimeError("blocked requires --blocker")
            t["blocker"] = args.blocker
        data["tasks"].append(t)
        _save_index(args.index, data)
    print(f"OK: added {args.task}")
    return 0


TASK_CARD_TEMPLATE = """【任务类型】<如：PRD 编写 / 架构评审 / 测试计划设计>
【当前阶段】<phase_id，如 prd / architecture / testing>
【目标】<一句话概述期望达成的结果>
【输入材料】
- 用户需求/业务背景：<简要描述或引用链接>
- 相关已有文档：<列出现有 PRD/架构/代码/测试文档路径或链接>
- 约束与前提：<性能/安全/合规/时间等约束>
【输出要求】
- 必须产出：<例如：更新 PRD 某章节、给出评审意见列表、产出测试计划表格等>
- 建议格式：<如 Markdown 标题结构、表格字段等>
【验收标准】
- <该任务被视为“完成”的具体标准，如：覆盖哪些场景、每条需求是否可测试等>
【后续流转建议】
- <完成后建议由哪个角色继续跟进，如“交给架构师评审”“交给测试设计用例”等>

---

## 执行结果

- （完成后补充：结论摘要、产物路径/链接、风险与下一步）
"""


def cmd_new_card(args: argparse.Namespace) -> int:
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    if os.path.exists(args.out) and not args.force:
        raise RuntimeError(f"File exists: {args.out} (use --force to overwrite)")
    content = TASK_CARD_TEMPLATE
    _write_text_atomic(args.out, content)
    print(f"OK: created card {args.out}")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="task_board.py",
        description="Task board helper: manage task-index.json and task cards with stable schema.",
    )
    p.add_argument("--index", default=DEFAULT_INDEX_PATH, help=f"Path to index JSON (default: {DEFAULT_INDEX_PATH})")
    p.add_argument(
        "--cards-dir", default=DEFAULT_CARDS_DIR, help=f"Path to task cards dir (default: {DEFAULT_CARDS_DIR})"
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("init", help="Initialize index and cards directory")
    sp.set_defaults(func=cmd_init)

    sp = sub.add_parser("list", help="List tasks by role/status")
    sp.add_argument("--role", required=False, help="Filter by owner role_id")
    sp.add_argument("--status", required=False, help="Comma-separated statuses, e.g. todo,doing")
    sp.set_defaults(func=cmd_list)

    sp = sub.add_parser("claim", help="Claim a todo task (todo -> doing)")
    sp.add_argument("--task", required=True, help="Task id")
    sp.add_argument("--by", required=False, help="Role id claiming (must match owner_role if provided)")
    sp.set_defaults(func=cmd_claim)

    sp = sub.add_parser("update", help="Update task status and metadata")
    sp.add_argument("--task", required=True, help="Task id")
    sp.add_argument("--status", required=True, help="New status")
    sp.add_argument("--blocker", required=False, help="Blocker reason (required for blocked)")
    sp.add_argument("--add-result", required=False, help="Append a result link/path")
    sp.add_argument("--by", required=False, help="Role id updating (must match owner_role if provided)")
    sp.set_defaults(func=cmd_update)

    sp = sub.add_parser("add", help="Add a new task entry to index (card must exist)")
    sp.add_argument("--task", required=True, help="Task id")
    sp.add_argument("--owner", required=True, help="Owner role id")
    sp.add_argument("--status", required=True, help="Initial status")
    sp.add_argument("--card", required=True, help="Card path (must exist)")
    sp.add_argument("--phase", required=False, help="Phase id")
    sp.add_argument("--blocker", required=False, help="Blocker reason (required for blocked)")
    sp.add_argument("--by", required=False, help="Role id adding")
    sp.set_defaults(func=cmd_add)

    sp = sub.add_parser("new-card", help="Create a new task card file using 4.1 template")
    sp.add_argument("--out", required=True, help="Output path for new card markdown")
    sp.add_argument("--force", action="store_true", help="Overwrite if exists")
    sp.set_defaults(func=cmd_new_card)

    return p


def main(argv: Optional[List[str]] = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    p = _build_parser()
    args = p.parse_args(argv)
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

