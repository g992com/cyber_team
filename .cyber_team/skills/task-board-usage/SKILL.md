---
name: task-board-usage
description: 使用 task_board.py 对任务索引与任务卡进行查询、领取、更新与创建；禁止直接编辑 task-index.json 或绕过脚本操作任务卡文件。适用于任何角色在业务项目中进行任务板操作时。
---

# 任务板使用（task_board.py）

本 skill 定义**任务板操作的唯一步骤来源**。凡涉及任务索引/任务卡（创建、查询、领取、更新），先读本 skill 对应小节，再执行。

规则约束见：`.cyber_team/rules/task-board-operations.md`。

## 路径契约（业务项目）

- 脚本：`python3 scripts/task_board.py ...`（若环境无 `python3`，改用 `python`）
- 索引：`docs/status/task-index.json`
- 任务卡目录：`docs/status/task-cards/`
- 任务 payload（JSON，真源）：`docs/status/task-cards/<task_id>.json`

## Python 解释器约定（跨平台）

不同系统对 Python 命令名的约定不同：Windows 常见为 `python`，Linux/macOS 常见为 `python3`。

本规范中所有命令默认以 `python3` 书写；执行时请按以下顺序选择可用解释器：

```bash
python3 --version || python --version
```

若 `python3` 可用则使用 `python3 ...`；否则使用 `python ...`。

## 禁止事项（必须遵守）

- 禁止直接编辑 `docs/status/task-index.json`。
- 禁止绕过脚本手工创建/移动/重命名任务卡文件并假定索引会自动更新。
- 禁止绕过 payload（JSON 真源）直接手改 `docs/status/task-cards/<task_id>.md` 并期望脚本据此校验或渲染一致性；任务卡 Markdown 为渲染视图，需由脚本生成或重渲染。

## 操作一：查询任务（list）

用于找到“属于某角色”的待办/进行中/阻塞任务，或查看全局任务分布。

```bash
# 查看某角色的 todo/doing/blocked
python3 scripts/task_board.py list --role <role_id> --status todo,doing,blocked

# 查看全局任务（不按 role 过滤）
python3 scripts/task_board.py list --status todo,doing,blocked
```

## 操作二：领取任务（claim）

将某个任务从 `todo` 领取为 `doing`（脚本会校验状态机与**任务就绪**：payload 合法且任务卡渲染不陈旧、无占位符）。

```bash
python3 scripts/task_board.py claim --task <task_id> --by <role_id>
```

约束建议（团队约定）：仅领取 `owner_role == <role_id>` 的任务。

## 操作三：更新任务状态与结果（update）

完成任务或产生阻塞时更新状态；完成时建议追加产物路径/链接。

```bash
# 标记阻塞（blocked 必须带 blocker）
python3 scripts/task_board.py update --task <task_id> --status blocked --blocker "<原因>" --by <role_id>

# 标记完成并追加产物路径/链接
python3 scripts/task_board.py update --task <task_id> --status done --add-result "<产物路径或链接>" --by <role_id>
```

约束建议（团队约定）：仅更新 `owner_role == <role_id>` 的任务。

## 操作四：创建新任务（create-task）

创建新任务使用 **create-task**（原子创建，JSON 真源）。

流程：由项目经理/调度者先生成 payload JSON（结构化字段，禁止占位符与空值），再调用 `create-task` 一次性生成任务卡 Markdown 并写入索引。

```bash
# 1) 准备 payload（真源）
# 路径建议：docs/status/task-cards/<task_id>.json
#
# 2) 原子创建：写 payload（规范化）、渲染任务卡、写入索引
python3 scripts/task_board.py create-task --task <task_id> --owner <role_id> --by <role_id>
```

说明：
- `create-task` 默认读取 `docs/status/task-cards/<task_id>.json` 作为 payload 真源，并生成 `docs/status/task-cards/<task_id>.md`。
- 若需要从其他路径读入 payload，可使用 `--payload-file <path>`；如需覆盖已有文件，增加 `--force`。
