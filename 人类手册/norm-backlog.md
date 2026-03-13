# 规范工程进展与待办

本文档记录本规范工程（cyber_team）的**最新进展**和**待办事项**，作为后续继续工作的记忆与优先级参考。与智能体协作**强相关**的必要改进见 [规范改进方案（精简版）](norm-improvement-plan.md)；此处主要收纳「有用但非必要」及「可后置」的改进项。

---

## 近期进展（更新时请补充日期与摘要）

- **2025-03-12**：按 [规范改进实施计划](norm-improvement-execution-plan.md) 完成步骤 1–5：① 文档化阶段与裁剪约定（做法 B，process/process.md + README）；② 阶段定义唯一事实来源（role-skills-design 第 3 节改为引用 phases.yaml）；③ state 增加 tailoring_snapshot、project-initiation 产出约定、update_state.py 兼容；④ 新增 process/exit-criteria.yaml 与阶段转换规则说明；⑤ 新增 process/templates-index.md。各步已做全工程回顾并沉淀至 人类手册/role-skills-design-memo.md。
- **2025-03**：明确规范改进策略：仅保留智能体协作必要项；有用项与后置项迁入本待办；确立「阶段全集 → PM 裁剪 → 业务项目 process」的流程设计，并完成可行性与有效性评估（见 [norm-improvement-plan.md](norm-improvement-plan.md)）。

---

## 待办：有用但可简化（按需实施）

以下对智能体协作有助益，但可不作为首轮必做；实施时优先做「裁剪与发现」相关，其余按需。

| 改进项 | 说明 | 优先级 |
|--------|------|--------|
| **裁剪指南 + 裁剪结果持久化** | 在 `process/` 下增加裁剪指南（可裁剪项、按项目类型的建议）；约定业务项目侧「裁剪结果」的落点（如 `docs/project-phases.yaml` 或 state 中的 `tailoring_snapshot`）。 | P1 |
| **state 中 blockers/risks 的语义与结构** | 在 state 或 README 中明确「何时写 project_blockers、谁跟进、何时升级」；可选将 project_risks 细化为结构化字段（id、description、category、mitigation、status）。 | P1 |
| **模板/清单索引** | 在 `process/` 下列出所有可复制到业务项目的资产（state、project-docs-index、status 模板等）及复制目标路径，便于发现与初始化。 | P1 |
| **阶段出口的检查单** | 在阶段出口条件中为关键阶段补充可执行检查单（如 requirements 出口：prd/user_stories 存在且关键 status 为 approved），与出口条件 YAML 一并维护。 | P2 |
| **规范版本与变更约定** | 为 process 增加 `spec_version` 或 changelog 引用；约定规范变更时更新 memo 或 changelog，便于多版本兼容。 | P2 |
| **过程度量定义** | 定义 2～4 个度量目标及对应基元/派生度量、数据来源（state、产出物 frontmatter），供后续看板或分析使用。 | P2 |
| **过程改进说明与改进 backlog** | 过程改进目标、回顾节奏、改进建议的收集与纳入方式；可选 `process/improvement-backlog.md` 跟踪改进项状态。 | P2 |
| **基线及已批准产物变更** | 在 artifact 约定中明确「阶段基线」概念及「已 approved 产物的变更需再评审或版本更新」的轻量规则。 | P2 |
| **需求 ID 与追溯矩阵建议** | PRD/用户故事采用稳定需求 ID；可选在业务项目预留追溯矩阵文档位置（需求 → 设计/测试）。 | P3 |
| **阶段/产出物 RACI 表** | 按阶段或产出物类型列出 R/A/C/I，与现有 owner_role 互补，供人工与评审使用。 | P3 |

---

## 待办：可后置（偏组织/成熟度）

以下对 CMMI/过程成熟度或审计有价值，对智能体协作非前提；可在有明确需求时再做。

| 改进项 | 说明 |
|--------|------|
| **PPQA 客观评价约定** | 在 process 中明确「评审结论由非产出负责人角色给出」等客观性要求。 |
| **完整 RSKM 结构** | 风险类别、概率/影响、缓解计划、评审节奏的完整字段与流程。 |
| **完整 CM 流程** | 基线定义、变更请求/审批流程、配置审计的成文流程。 |
| **MA 数据收集与分析规程** | 度量数据的收集频率、存储、分析及报告规程。 |
| **OPF 评估与部署** | 过程评估节奏、改进项优先级、推广与培训安排。 |

---

## 使用说明

- **更新进展**：完成某项改进或做出重要决策后，在「近期进展」中追加一条（日期 + 摘要）。
- **处理待办**：从待办中选取项实施时，可在该项加「进行中」或移到「近期进展」并注明「已完成：…」。
- **新增待办**：后续讨论产生的新想法、技术债或优化，可按「有用可简化」或「可后置」分类追加到上表。
