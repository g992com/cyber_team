---
name: project-initiation
description: Tailors project activities against team activity norms (process/phases/roles/mapping), produces project plan and phase/activity list from user problem or requirements. Use when starting a project, defining project flow, tailoring process, project initiation, 项目启动, 流程裁剪, 项目计划, or when the user asks to determine which phases and activities to run.
---

# 项目启动与流程裁剪

在用户提出问题或需求后，根据团队活动规范（process、phases、roles、mapping）对项目活动进行**裁剪**，确定业务项目适用的流程与计划，产出项目计划、流程裁剪说明及阶段与活动清单。依据 PMBOK「按上下文裁剪」及 ISO/IEC/IEEE 16326 项目管理计划实践。

## 输入与前置

- **用户输入**：用户描述的问题、目标或需求（可含业务背景、约束、期望产出）。
- **规范来源**：读取规范根目录下的 `process/phases.yaml`、`roles/roles.yaml`、`mapping/phase-role-skill.yaml`（可选阅读 `人类手册/process/process.md`、`人类手册/stages/*.md` 仅作说明参考，非执行依赖）。

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
| **流程裁剪说明** | 保留/简化/跳过的阶段与活动、裁剪理由、适用条件；须写入业务项目 **`docs/process-tailoring.md`**。 |
| **阶段与活动清单** | 阶段 id、名称、预期产出、负责角色，可供 Agent 与人工按计划推进；须同步写入业务项目 **`state.yaml` 的 `tailoring_snapshot`**（业务项目要执行的 phase_id 列表，顺序即执行顺序）。 |

**必须产出**：① 业务项目 **`state.tailoring_snapshot`**（**必须**通过运行业务项目中的 `python scripts/update_state.py set-tailoring --phases "id1,id2,..."` 写入，不得直接编辑 state.yaml）；② 业务项目 **`docs/process-tailoring.md`**（裁剪理由、保留/省略/简化的阶段与活动、适用条件）。业务项目不复制规范库 `process/phases.yaml`，以 `state.tailoring_snapshot` 与 `docs/process-tailoring.md` 表达该业务项目的流程。

产出可写入项目根目录或 `docs/` 下，如 `docs/project-plan.md`、`docs/process-tailoring.md`；若项目使用 `docs/project-docs-index.yaml`，可在索引中登记上述文档路径。

## 与 state 的衔接

- 项目启动阶段对应 `state.current_phase: initiation`。
- **须将裁剪结果写入业务项目 `state.tailoring_snapshot`**：业务项目要执行的 phase_id 列表（与 `process/phases.yaml` 的 id 一致），顺序即执行顺序；**必须**通过 `python scripts/update_state.py` 完成，不得直接编辑 state.yaml。示例：`python scripts/update_state.py set-tailoring --phases "requirements,architecture,design,development,testing"`；若 state 尚未初始化，先运行 `python scripts/update_state.py init`。
- 完成本阶段并用户确认后，通过 `python scripts/update_state.py set-phase --phase requirements` 与 `python scripts/update_state.py add-completed --phase initiation` 更新 `current_phase` 与 `completed_phases`。
- 阶段与活动清单中的阶段 id 应与 `process/phases.yaml` 的 `id` 一致，便于 Agent 解析与状态推进。
