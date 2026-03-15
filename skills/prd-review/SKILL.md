---
name: prd-review
description: Reviews PRD and product requirements documents for function boundary, priorities, scope, and consistency with user stories; supports stakeholder alignment. Checks that 待澄清问题 and 可选澄清 are separate subsections under 干系人对齐, each with a table. Use when reviewing PRD, product requirements document, scope, or priorities.
---

# PRD / 需求文档评审

角色边界与意图/需求确认见 `rules/role-boundary-and-intent-confirmation.md`；本角色须特别注意：不猜测通过标准，以约定或确认为准。

## 评审维度

| 维度 | 检查要点 |
|------|----------|
| **功能边界与范围** | 在/不在范围内是否清晰；与路线图或版本范围一致 |
| **优先级与依赖** | 必须/应该/可以明确；依赖与风险已标注 |
| **验收标准覆盖** | 关键功能有可验证的验收标准；与用户故事可追溯 |
| **与用户故事一致性** | PRD 范围与既有故事无冲突；缺口已识别 |
| **待澄清与可选澄清** | 待澄清问题、可选澄清均在「干系人对齐」下为独立小节且为表格形式（待澄清：序号、问题项、说明、影响范围；可选澄清：引导语+序号、可选澄清问题、说明），二者不混表 |

## 流程

1. **获取评审对象**：待评审的 PRD 或需求文档。
2. **边界与范围**：确认范围表述清晰；与迭代/路线图对齐。
3. **优先级与依赖**：检查优先级标注与依赖关系；标注缺失或冲突。
4. **验收标准**：每条关键范围有对应验收标准；可被测试执行。
5. **与故事对照**：与现有用户故事或 Backlog 对照；列出缺口与重复。
6. **输出结论**：通过/待澄清/须补充；具体改进项与建议优先级。

## 输出要求

结论明确、可执行；干系人可根据结论更新 PRD 或补充需求。
