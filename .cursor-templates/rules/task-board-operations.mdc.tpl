---
description: 任务板操作约束：任何角色对任务索引/任务卡的创建/查询/领取/更新必须通过 task_board.py，并按 task-board-usage skill 执行；禁止直接手改索引或绕过脚本操作任务卡文件。
alwaysApply: true
---

# 任务板操作约束

对任务索引与任务卡（创建、查询、领取、更新）的任何操作：

- **必须**遵守 `[[spec:.cyber_team/rules/task-board-operations.md]]`；
- **必须**按 `[[spec:.cyber_team/skills/task-board-usage/SKILL.md]]` 执行（通过 `python3` 或 `python` 运行 `scripts/task_board.py`），不得直接读写 `docs/status/task-index.json` 或绕过脚本操作任务卡文件。
- 创建新任务仅允许使用 `create-task`（JSON 真源 + 渲染任务卡 + 写入索引，原子完成）。

