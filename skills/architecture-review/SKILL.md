---
name: architecture-review
description: Reviews architecture and design documents for consistency, scalability, technology choices, and security design; covers DBA/DevOps/SRE aspects. Use when reviewing architecture or design documents, or technical design proposals.
---

# 架构与设计评审

角色边界与意图/需求确认见 `rules/role-boundary-and-intent-confirmation.md`；本角色须特别注意：不猜测通过标准，以约定或确认为准。

## 审查维度

| 维度 | 检查要点 |
|------|----------|
| **一致性** | 与需求、既有架构、接口契约一致；无矛盾 |
| **可扩展性** | 扩展点与边界清晰；容量与性能考虑 |
| **风险与技术债务** | 已知风险与债务已标注；缓解或接受理由 |
| **安全设计** | 威胁建模、认证/授权、数据与访问合规 |
| **DBA/DevOps/SRE** | 数据模型与迁移、流水线与部署、监控与 SLO 是否在设计中体现 |

## 流程

1. **获取设计文档**：架构图、ADR、API 规约、数据模型、安全与运维相关说明。
2. **按维度审查**：逐项对照上表；记录不符合项与建议。
3. **输出结论与风险**：通过/有条件通过/须修订；列出改进建议与优先级。

## 输出要求

审查维度覆盖完整；结论与改进建议明确、可执行；风险与依赖已记录。
