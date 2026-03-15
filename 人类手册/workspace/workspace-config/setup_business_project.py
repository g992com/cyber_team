#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
业务项目初始化脚本：按 workspace-setup.md「业务项目侧仍需准备」清单，
从规范仓库（cyber_team）拷贝/创建所需文件与目录。
入参：业务项目根目录的绝对路径。
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


def _norm_root(script_dir: str) -> Path:
    """规范仓库根 = 从脚本所在目录向上查找，直到找到包含 .cursor 子目录的目录（即规范仓库根）。"""
    current = Path(script_dir).resolve()
    while current != current.parent:
        if (current / ".cursor").is_dir():
            return current
        current = current.parent
    raise RuntimeError("未找到规范仓库根（沿脚本路径上溯未发现包含 .cursor 的目录）")


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


def main() -> int:
    parser = argparse.ArgumentParser(
        description="从规范仓库拷贝/创建业务项目所需文件与目录（与 workspace-setup 一致）",
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
    index_yaml = norm / "process" / "project-docs" / "project-docs-index.yaml"

    # 校验：规范根下必须存在 project-docs-index.yaml
    if not index_yaml.exists():
        print(f"ERROR: 规范仓库缺少 {index_yaml.relative_to(norm)}，请确认在 cyber_team 根目录下执行。", file=sys.stderr)
        return 1

    task_board_dir = norm / "process" / "project-docs" / "status" / "task-board"

    def copy2(src: Path, dst: Path, label: str = "") -> None:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"已拷贝 {label or src.name} → {dst.relative_to(target)}")

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
    state_src = norm / "process" / "state.yaml"
    if state_src.exists():
        copy2(state_src, target / "state.yaml")
    update_state_src = norm / "process" / "project-docs" / "status" / "update_state.py"
    if update_state_src.exists():
        copy2(update_state_src, target / "scripts" / "update_state.py")

    # 5) rules：规范库 rules/*.md 全部拷贝到业务项目 .cursor/rules/，目标使用 .mdc 后缀，符合 Cursor 规则约定
    rules_dir = norm / "rules"
    if rules_dir.is_dir():
        for rule_src in rules_dir.glob("*.md"):
            copy2(rule_src, target / ".cursor" / "rules" / f"{rule_src.stem}.mdc")

    print("完成。请按 workspace-setup.md 与多会话方案在业务项目中继续配置。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
