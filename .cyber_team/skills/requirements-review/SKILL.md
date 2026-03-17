---
name: requirements-review
description: Reviews user stories and acceptance criteria for completeness, consistency, and testability (INVEST); identifies gaps and conflicts. Use when reviewing user stories, acceptance criteria, or when the user asks for requirements review.
---

# 用户故事与验收标准评审

角色边界与意图/需求确认见 `.cyber_team/rules/role-boundary-and-intent-confirmation.md`；本角色须特别注意：不猜测通过标准，以约定或确认为准。

## 评审清单

按以下维度检查，输出通过/待澄清/须补充及建议优先级：

| 维度 | 检查要点 |
|------|----------|
| **完整性** | 角色/用户、目标、价值、验收标准、可测试条件是否齐全（INVEST） |
| **一致性** | 与既有需求、PRD、术语是否一致；冲突与重复 |
| **可测性** | 验收标准是否可验证；是否可拆为开发与测试任务 |

## 流程

1. **获取评审对象**：明确待评审的用户故事或验收标准范围。
2. **完整性检查**：按 INVEST 或约定清单逐项检查；标注缺失。
3. **一致性检查**：与相关需求/PRD 对照；列出冲突与重复。
4. **可测性与可执行性**：确认验收标准可验证且开发/测试可执行。
5. **优先级与范围**：与路线图或迭代对齐；标注依赖与优先级。
6. **输出结论**：区分通过/待澄清/须补充；建议具体可执行。

## 输出格式

- **通过**：满足完整性、一致性、可测性，可进入开发/测试。
- **待澄清**：需补充信息或决策后再定。
- **须补充**：必须补充内容方可进入下一阶段；列出具体项。

结论需可被开发与测试直接使用，避免歧义。
