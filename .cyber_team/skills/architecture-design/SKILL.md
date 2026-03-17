---
name: architecture-design
description: Designs system and module structure, technology selection, scalability and consistency; produces ADR and architecture artifacts. Use when designing architecture, making technology choices, or writing ADR.
---

# 架构与 ADR

角色边界与意图/需求确认见 `.cyber_team/rules/role-boundary-and-intent-confirmation.md`；本角色须特别注意：不猜测技术选型前提或业务约束，须以需求或确认为准。

## 产出要点

- **项目分层与边界**：模块划分、接口与契约、依赖方向。
- **技术选型**：选型结论与依据；与需求、约束一致。
- **可扩展性与一致性**：扩展点、数据与接口一致性策略。
- **ADR（架构决策记录）**：关键决策、背景、选项、结论与后果。

## ADR 模板（简要）

```markdown
# ADR-xxx: [标题]

## 状态
提议 / 已接受 / 已废弃

## 背景与问题
[要解决的问题或约束]

## 决策
[采用的方案]

## 后果
[正面与负面影响、后续行动]
```

## 流程

1. **确定边界与约束**：需求、非功能需求、现有系统边界。
2. **选型与分层**：技术选型并记录依据；定义分层与模块边界。
3. **产出 ADR/架构图/数据模型/API 规约**：关键决策写入 ADR；接口与数据模型可被实现与评审使用。
4. **评审准备**：产出完整、可被设计评审专家审查。

## 验收

架构与数据/API 设计文档完整；ADR 覆盖关键决策；技术债务与风险已标注。
