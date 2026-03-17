---
description: 任务板（task-index + 任务卡）操作约束：任何角色对任务的创建/查询/领取/更新均须通过脚本化方式，禁止直接读写索引或任务卡文件；具体操作步骤以 task-board-usage skill 为准。
alwaysApply: true
---

# 任务板操作约束（Task Board Operations）

本规则适用于**业务项目**中所有角色：凡涉及任务索引与任务卡（创建、查询、领取、更新），均须遵守本规则。

## 单一定义与执行入口

- **唯一操作入口（步骤定义）**：`[[spec:.cyber_team/skills/task-board-usage/SKILL.md]]`
- 本规则仅定义“必须/禁止”的约束；具体命令与步骤仅在上述 skill 中维护，其他位置只引用，不复制。

## 必须（MUST）

- **必须**通过业务项目脚本 `scripts/task_board.py` 进行任务相关操作（解释器命令名遵循 `task-board-usage` 的跨平台约定：优先 `python3`，无则用 `python`）：
  - 查询：list
  - 领取：claim
  - 更新：update
  - 创建新任务：使用 `create-task`（JSON 真源 + 渲染任务卡 + 写入索引，原子完成）
- 每次执行任务板操作前，**先阅读** `task-board-usage` 中对应操作小节，再执行。

## 禁止（MUST NOT）

- **禁止**直接编辑或手工改写 `docs/status/task-index.json`。
- **禁止**绕过 `task_board.py` 直接创建/移动/重命名任务卡文件并假定索引会自动更新。

## 路径契约（Contract）

- 脚本：业务项目根目录 `scripts/task_board.py`（命令名在 Linux/macOS 常为 `python3`，Windows 常为 `python`）
- 索引：业务项目 `docs/status/task-index.json`
- 任务卡目录：业务项目 `docs/status/task-cards/`

