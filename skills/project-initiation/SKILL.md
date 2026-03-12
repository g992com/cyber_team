---
name: project-initiation
description: Tailors project activities against team activity norms (process/phases/roles/mapping), produces project plan and phase/activity list from user problem or requirements. Use when starting a project, defining project flow, tailoring process, project initiation, 项目启动, 流程裁剪, 项目计划, or when the user asks to determine which phases and activities to run.
---

# 项目启动与流程裁剪

在用户提出问题或需求后，根据团队活动规范（process、phases、roles、mapping）对项目活动进行**裁剪**，确定本项目适用的流程与计划，产出项目计划、流程裁剪说明及阶段与活动清单。依据 PMBOK「按上下文裁剪」及 ISO/IEC/IEEE 16326 项目管理计划实践。

## 输入与前置

- **用户输入**：用户描述的问题、目标或需求（可含业务背景、约束、期望产出）。
- **规范来源**：读取规范根目录下的 `process/phases.yaml`、`roles/roles.yaml`、`mapping/phase-role-skill.yaml` 及可选 `process/process.md`、`stages/*.md`，以了解可裁剪的阶段与活动。

## 执行要点

1. **理解用户输入**：明确问题/目标/需求、范围与优先级；必要时通过提问澄清。
2. **评估项目特征**：结合 `phases.yaml` 与项目实际情况，评估规模、复杂度、约束（时间/资源/合规）及干系人期望。
3. **流程裁剪**：选择保留、简化或跳过的阶段与活动（如小型交付可合并/省略部分评审；合规或高可靠场景保留并强化评审与运维）；记录裁剪理由与适用条件。
4. **输出项目计划**：阶段顺序、每阶段主要产出、参与角色及与规范的对应关系；可选：项目章程摘要（目标、范围概要、关键里程碑、成功标准）。
5. **输出阶段与活动清单**：列出将执行的阶段 id、名称、预期产出、负责角色，与 `state.yaml` 的 `current_phase` / `completed_phases` 设计一致。
6. **确认与交接**：向用户呈现计划与裁剪说明，确认后进入需求阶段或用户指定的下一阶段。

## 产出物约定

| 产出 | 要点 |
|------|------|
| **项目计划** | 阶段顺序、每阶段产出与角色、与规范的对应；可选含项目章程摘要。 |
| **流程裁剪说明** | 保留/简化/跳过的阶段与活动、裁剪理由、适用条件。 |
| **阶段与活动清单** | 阶段 id、名称、预期产出、负责角色，可供 Agent 与人工按计划推进。 |

产出可写入项目根目录或 `docs/` 下，如 `docs/project-plan.md`、`docs/process-tailoring.md`；若项目使用 `docs/project-docs-index.yaml`，可在索引中登记上述文档路径。

## 与 state 的衔接

- 项目启动阶段对应 `state.current_phase: initiation`。
- 完成本阶段并用户确认后，将 `current_phase` 更新为下一阶段（通常为 `requirements`），并将 `initiation` 加入 `completed_phases`。
- 阶段与活动清单中的阶段 id 应与 `process/phases.yaml` 的 `id` 一致，便于 Agent 解析与状态推进。
