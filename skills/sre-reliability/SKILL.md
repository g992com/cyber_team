---
name: sre-reliability
description: Guides reliability objectives (SLO/SLI), monitoring and alerting, incident review, capacity and cost. Use when the user mentions SRE, reliability, monitoring, alerting, incident, or on-call.
---

# SRE 与可靠性

角色边界与意图/需求确认见 `skills/_common/role-boundary-and-intent-confirmation.md`；本角色仅负责 mapping 规定的本角色产出，不得代做其他角色产出。

## 关键概念

| 概念 | 要点 |
|------|------|
| **SLO/SLI** | 服务级别目标与指标；错误预算与策略 |
| **监控与告警** | 指标、日志、追踪；告警规则与升级 |
| **故障复盘** | 时间线、根因、改进项与跟进 |
| **容量与成本** | 容量规划、弹性与成本优化 |
| **Runbook** | 常见故障与操作步骤；On-call 使用 |

## 流程

1. **定义 SLO/告警**：与业务对齐的 SLO/SLI；告警阈值与升级策略。
2. **On-call 与响应**：值班与升级路径；事件响应与沟通。
3. **复盘与改进**：故障后复盘；结论与改进项跟进；Runbook 更新。

## 产出

- 监控与告警有效、可行动。
- 复盘有结论与跟进；Runbook 与 SLO 报告可维护。
