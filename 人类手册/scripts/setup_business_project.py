#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
业务项目初始化脚本（单仓模式）：由人类在规范库侧执行。
按 .cyber_team/SNAPSHOT-STRATEGY.md，从规范仓库（cyber_team）拷贝/创建业务项目所需
文件与目录，采用单仓模式（.cyber_team 快照 + .cursor 从 .cursor-templates 生成）。
多根工作区模式已废弃，仅支持单仓。

用法：在规范仓库根目录执行
  python 人类手册/scripts/setup_business_project.py <业务项目根目录绝对路径>

入参：业务项目根目录的绝对路径。
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def _norm_root(script_dir: str) -> Path:
    """规范仓库根 = 从脚本所在目录向上查找，直到找到包含 .cursor 或 .cyber_team 的目录。"""
    current = Path(script_dir).resolve()
    while current != current.parent:
        if (current / ".cursor").is_dir() or (current / ".cyber_team").is_dir():
            return current
        current = current.parent
    raise RuntimeError("未找到规范仓库根（沿脚本路径上溯未发现包含 .cursor 或 .cyber_team 的目录）")


def _parse_index_first_segments(yaml_path: Path) -> set[str]:
    """从 project-docs-index.yaml 解析各 value 路径的首段，去重返回。仅用标准库。"""
    text = yaml_path.read_text(encoding="utf-8")
    segments: set[str] = set()
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" in line and "/" in line:
            idx = line.find(": ")
            if idx >= 0:
                val = line[idx + 2 :].strip()
                if "#" in val:
                    val = val.split("#")[0].strip()
                if "/" in val:
                    segments.add(val.split("/")[0].strip())
    return segments


def _git_head(rev_path: Path) -> str:
    """返回 rev_path 所在仓库的 HEAD commit sha，失败返回空字符串。"""
    try:
        r = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=rev_path,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if r.returncode == 0 and r.stdout:
            return r.stdout.strip()[:40]
    except Exception:
        pass
    return ""


def _copy_cyber_team_snapshot(norm: Path, target: Path, copy2_fn) -> None:
    """将规范库 .cyber_team/ 下 process/roles/mapping/skills/rules 及约定文档复制到 target/.cyber_team/，并写入 SNAPSHOT.yaml。"""
    dst_root = target / ".cyber_team"
    cyber_team = norm / ".cyber_team"
    dst_root.mkdir(parents=True, exist_ok=True)
    for name in ("process", "roles", "mapping", "skills", "rules"):
        src = cyber_team / name
        if not src.is_dir():
            continue
        dst = dst_root / name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"已复制 .cyber_team/{name}/ → target/.cyber_team/{name}/")
    # 约定文档
    for name in ("CONVENTIONS-paths-and-links.md", "SNAPSHOT-STRATEGY.md"):
        src = cyber_team / name
        if src.exists():
            copy2_fn(src, dst_root / name, name)
    # SNAPSHOT.yaml
    snapshot = {
        "source_repo": "cyber_team",
        "source_commit": _git_head(norm),
        "generated_at": datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "notes": "",
    }
    snapshot_yaml = dst_root / "SNAPSHOT.yaml"
    buf = []
    for k, v in snapshot.items():
        buf.append(f'{k}: "{v}"' if v else f"{k}: ''")
    snapshot_yaml.write_text("\n".join(buf) + "\n", encoding="utf-8")
    print(f"已写入 .cyber_team/SNAPSHOT.yaml")


def _copy_cursor_from_templates(norm: Path, target: Path, copy2_fn) -> None:
    """从 .cursor-templates/rules 和 .cursor-templates/skills 生成 target/.cursor/。"""
    rules_src = norm / ".cursor-templates" / "rules"
    skills_src = norm / ".cursor-templates" / "skills"
    dst_rules = target / ".cursor" / "rules"
    dst_skills = target / ".cursor" / "skills"
    dst_rules.mkdir(parents=True, exist_ok=True)
    dst_skills.mkdir(parents=True, exist_ok=True)
    if rules_src.is_dir():
        for f in rules_src.glob("*.mdc.tpl"):
            dst_name = f.name.replace(".mdc.tpl", ".mdc")
            copy2_fn(f, dst_rules / dst_name, dst_name)
    if skills_src.is_dir():
        for d in skills_src.iterdir():
            if d.is_dir():
                dst_d = dst_skills / d.name
                if dst_d.exists():
                    shutil.rmtree(dst_d)
                shutil.copytree(d, dst_d)
                print(f"已复制 .cursor-templates/skills/{d.name}/ → .cursor/skills/{d.name}/")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="从规范仓库拷贝/创建业务项目所需文件与目录（单仓模式：.cyber_team 快照 + .cursor 从模板生成）",
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=None,
        help="业务项目根目录的绝对路径",
    )
    parser.add_argument(
        "--target",
        dest="target_opt",
        default=None,
        help="业务项目根目录的绝对路径（与位置参数二选一）",
    )
    args = parser.parse_args()
    target_raw = args.target or args.target_opt

    # 入参校验：不能为空
    if not target_raw or not str(target_raw).strip():
        print("ERROR: 入参不能为空，请提供业务项目根目录的绝对路径。", file=sys.stderr)
        return 1

    target = Path(target_raw.strip()).resolve()
    # 业务项目目录必须实际存在且为目录
    if not target.exists():
        print(f"ERROR: 业务项目目录不存在: {target}", file=sys.stderr)
        return 1
    if not target.is_dir():
        print(f"ERROR: 路径不是目录: {target}", file=sys.stderr)
        return 1

    script_dir = os.path.dirname(os.path.abspath(__file__))
    norm = _norm_root(script_dir)
    index_yaml = norm / ".cyber_team" / "process" / "project-docs" / "project-docs-index.yaml"

    # 校验：规范库 .cyber_team 下必须存在 project-docs-index.yaml
    if not index_yaml.exists():
        print(f"ERROR: 规范仓库缺少 .cyber_team/process/project-docs/project-docs-index.yaml，请确认在 cyber_team 根目录下执行。", file=sys.stderr)
        return 1

    task_board_dir = norm / ".cyber_team" / "process" / "project-docs" / "status" / "task-board"

    def copy2(src: Path, dst: Path, label: str = "") -> None:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"已拷贝 {label or src.name} → {dst.relative_to(target)}")

    # 单仓模式：.cyber_team 快照 + .cursor 从 .cursor-templates 生成
    if (norm / ".cursor-templates").is_dir():
        _copy_cyber_team_snapshot(norm, target, copy2)
        _copy_cursor_from_templates(norm, target, copy2)
    else:
        print("WARNING: 未找到 .cursor-templates/，跳过 .cyber_team 与 .cursor 生成。", file=sys.stderr)

    # 1) 拷贝索引
    dst_index = target / "docs" / "project-docs-index.yaml"
    copy2(index_yaml, dst_index, "project-docs-index.yaml")

    # 2) 按索引建 docs 子目录
    segments = _parse_index_first_segments(dst_index)
    segments.add("status")
    for seg in sorted(segments):
        d = target / "docs" / seg
        d.mkdir(parents=True, exist_ok=True)
    print(f"已创建目录 docs/ 及子目录: {', '.join(sorted(segments))}")

    # 3) 任务板
    task_index_src = task_board_dir / "task-index.json"
    if task_index_src.exists():
        copy2(task_index_src, target / "docs" / "status" / "task-index.json")
    (target / "docs" / "status" / "task-cards").mkdir(parents=True, exist_ok=True)
    gitkeep = target / "docs" / "status" / "task-cards" / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.touch()
        print("已创建目录 docs/status/task-cards/ 及 .gitkeep")
    task_board_py = task_board_dir / "task_board.py"
    if task_board_py.exists():
        copy2(task_board_py, target / "scripts" / "task_board.py")

    # 4) state.yaml + update_state.py
    state_src = norm / ".cyber_team" / "process" / "state.yaml"
    if state_src.exists():
        copy2(state_src, target / "state.yaml")
    update_state_src = norm / ".cyber_team" / "process" / "project-docs" / "status" / "update_state.py"
    if update_state_src.exists():
        copy2(update_state_src, target / "scripts" / "update_state.py")

    # 5) rules：若未从 .cursor-templates 生成，则从规范库 .cyber_team/rules/*.md 拷贝到业务项目 .cursor/rules/
    dst_rules = target / ".cursor" / "rules"
    dst_rules.mkdir(parents=True, exist_ok=True)
    if not list(dst_rules.glob("*.mdc")):
        rules_dir = norm / ".cyber_team" / "rules"
        if rules_dir.is_dir():
            for rule_src in rules_dir.glob("*.md"):
                copy2(rule_src, dst_rules / f"{rule_src.stem}.mdc")

    print("完成。单仓模式已配置 .cyber_team 与 .cursor；请按 人类手册/scripts/templates-index.md 在业务项目中继续配置。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
