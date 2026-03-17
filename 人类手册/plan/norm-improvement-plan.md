# 规范改进方案（精简版）

本方案仅保留**智能体协作必要**的改进项；其余「有用但可简化」「可后置」项见 [规范工程进展与待办](norm-backlog.md)。

---

## 一、必要改进项（仅此三项）

| 序号 | 改进项 | 说明 |
|------|--------|------|
| 1 | **阶段定义唯一事实来源** | 规范库内阶段定义的唯一来源为 `.cyber_team/process/phases.yaml`；`人类手册/role-skills-design.md` 等文档仅引用并说明「与 .cyber_team/process/phases.yaml 一致」，不重复列举阶段 id/order/outputs，避免多源不一致。 |
| 2 | **阶段出口条件（可机读）** | 在 `.cyber_team/process/` 下新增阶段出口条件描述（推荐独立 YAML），使 Agent/Orchestrator 能判断「当前阶段是否可推进到下一阶段」。出口条件与 `project-docs-index`、产出物 `status`（如关键文档 approved）及现有 artifact 约定对齐。 |
| 3 | **产出物/模板可发现** | 保持并显化「先读 project-docs-index 再按路径读文档」的约定；可选在 `.cyber_team/process/` 下增加**模板与清单索引**，列出需复制到业务项目的资产及目标路径，便于初始化与发现。 |

以上三项直接支撑：当前阶段 → 该读哪些文档、该谁出手、何时能推进，缺一不可。

---

## 二、阶段设计：全集 + 裁剪 → 业务项目 process

### 2.1 原则：任何内容都不会出现多个拷贝

- **规范库**为阶段、角色、映射等规范内容的**唯一事实来源**；业务项目**不复制**这些定义（不复制 phases.yaml、不复制 roles/mapping 等）。
- 业务项目仅保存**项目特有**内容：进展状态（state）、裁剪结果（本项目执行哪些阶段）、流程裁剪说明、以及本项目实际产出物与文档索引。阶段名称、顺序、产出、角色与 skill 的映射等，一律从规范库读取，通过「裁剪结果」过滤出本项目适用的子集。

### 2.2 思路

- **规范库**：维护**阶段全集**（即当前 `.cyber_team/process/phases.yaml` 的完整生命周期：initiation → … → operations），作为「所有可能阶段」的唯一定义。
- **项目经理**：在项目启动阶段，在充分调查和了解用户需求与问题后，从全集中**裁剪**出适合本业务项目的阶段集合（或说工作流程），形成**该业务项目自己的 process**（以裁剪结果的形式存在，而非复制阶段定义）。
- **业务项目**：通过 **state.yaml 的 `tailoring_snapshot`**（phase_id 列表）表达「本项目要执行的阶段」；配合 **docs/process-tailoring.md** 记录裁剪理由与适用条件。Agent 读取规范库的 phases 后按 tailoring_snapshot 过滤得到「本项目阶段」；角色与 skill 仍从规范库的 `.cyber_team/mapping/`、`.cyber_team/roles/` 按 phase_id 解析。

### 2.3 采用做法 B（裁剪结果落点）

- **已确定采用做法 B**，与「任何内容都不会出现多个拷贝」一致：
  - 业务项目**不**维护 `project-phases.yaml` 或任何 phases 定义的拷贝。
  - 业务项目在 **state.yaml** 中增加 **`tailoring_snapshot`**：本项目要执行的 phase_id 列表（如 `[initiation, requirements, design, development, deployment]`），顺序与执行顺序一致。
  - 业务项目在 **docs/process-tailoring.md** 中记录：裁剪理由、保留/省略/简化的阶段与活动、适用条件（与 project-initiation 产出约定一致）。
- **state.current_phase** 与 **completed_phases** 的取值必须来自 tailoring_snapshot，不能出现本项目未包含的 phase_id。
- project-initiation 的产出要求中须写明：须输出 **state.tailoring_snapshot**（或等效字段）及 **docs/process-tailoring.md**。

**不采用做法 A 的原因**：做法 A 要求在业务项目内维护 `docs/project-phases.yaml`（阶段定义的子集拷贝），会违反「任何内容都不会出现多个拷贝」原则，且规范库阶段若变更时业务项目容易遗漏同步。

### 2.4 可行性与有效性评估

**可行性：高**

- 规范库已具备阶段全集；project-initiation 已包含流程裁剪步骤。做法 B 仅需在 state 中增加 tailoring_snapshot 字段、在业务项目 docs 下产出 process-tailoring.md，无需在业务项目内复制 phases 文件。
- 规范库的 `.cyber_team/mapping/`、`.cyber_team/roles/` 均按 phase_id 索引；Agent 读规范库 phases → 按 tailoring_snapshot 过滤 → 得到本项目阶段列表，与 state.current_phase、出口条件配合即可推进。技术上可行。

**有效性：高**

- **单一事实来源、零拷贝**：阶段定义仅存在于规范库；业务项目只存「哪些阶段」与「为什么这样裁」，不存阶段定义本身，避免多源与同步问题。
- **适配不同项目类型**：同上，小项目少列几个 phase_id，合规项目列全阶段。
- **Agent 行为一致**：Agent 始终读规范库 phases + 业务项目 state.tailoring_snapshot，逻辑统一。

**风险与约束**：规范库 phase_id 集合保持稳定；裁剪 = 全集子集，不引入业务项目自定义 phase_id。

---

**结论**：采用做法 B，在规范库保留阶段全集、业务项目仅保存 tailoring_snapshot + process-tailoring.md，**可行且有效**，且满足「任何内容都不会出现多个拷贝」原则。

---

## 三、与待办文档的关系

- **必要项**：仅上述三项，在本方案中实施即可。
- **有用项与后置项**：均列入 [norm-backlog.md](norm-backlog.md)，作为后续迭代与记忆支持；实施时从待办中按优先级选取，并在该文档中更新进展。

---

## 四、实施顺序建议

1. 明确并文档化「阶段全集 + 裁剪 → 业务项目 process」的约定：裁剪结果落点已确定为**做法 B**（state.tailoring_snapshot + docs/process-tailoring.md），遵守「任何内容都不会出现多个拷贝」原则。
2. 落实「阶段定义唯一事实来源」：检查并修正 role-skills-design 等文档对阶段的引用，统一指向 phases.yaml。
3. 在 .cyber_team/process/state.yaml 模板（及 schema 说明）中增加 **tailoring_snapshot** 字段；在 project-initiation 的产出要求中写明须输出 tailoring_snapshot 与 process-tailoring.md。
4. 新增阶段出口条件（YAML + 与索引/status 的对应），并在 process.md 或 README 中简述阶段转换规则。
5. 可选：在 .cyber_team/process/ 下增加模板与清单索引，便于业务项目初始化。

完成以上后，智能体协作所需的最小必要集即就绪；其余改进按 [norm-backlog.md](norm-backlog.md) 中的待办逐步推进。

**按全工程回顾规则执行的详细步骤**见 [规范改进实施计划](norm-improvement-execution-plan.md)：每步含具体动作、涉及文件、本步完成后的回顾要点与备忘要求。
