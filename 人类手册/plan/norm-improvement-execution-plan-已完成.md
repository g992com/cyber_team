# 规范改进实施计划（已完成）

> **状态**：本计划已实施完成。步骤 1～4 及可选步骤 5 已落地，详见 `人类手册/role-skills-design-memo.md` 中相关变更备忘。本文档保留为实施记录与追溯用。依据的方案见 [规范改进方案（精简版）](norm-improvement-plan.md)。

---

本计划依据 [规范改进方案（精简版）](norm-improvement-plan.md) 与 [修改后全工程回顾](.cursor/rules/post-change-project-wide-review.mdc) 规则编制。执行每步时须遵守**原则**（任何内容都不会出现多个拷贝，使用引用来建立关系），并在该步完成后按规则做**全工程回顾**并将结论**沉淀到备忘**。

---

## 原则（贯穿全程）

- **任何内容都不会出现多个拷贝，使用引用来建立关系**：阶段/角色/映射等仅在规范库一处维护；其他文档通过引用（路径、id、链接）关联，不复制定义。业务项目仅保存 state、tailoring_snapshot、process-tailoring.md、产出物索引等项目特有内容。

---

## 步骤 1：文档化「阶段全集 + 裁剪 → 业务项目 process」与做法 B

**目标**：在规范库内明确约定裁剪结果落点为做法 B（state.tailoring_snapshot + docs/process-tailoring.md），且业务项目不复制阶段定义。

**动作**：
- 在 `人类手册/process/process.md` 或 `README.md` 中增加「阶段与裁剪」小节（或补充现有说明）：规范库维护阶段全集；业务项目通过 state 的 `tailoring_snapshot` 与 `docs/process-tailoring.md` 表达本项目流程，不复制 phases 文件。可引用 `人类手册/plan/norm-improvement-plan.md` 第二节。
- 若 README 已有类似表述，则改为**引用** norm-improvement-plan 的「二、阶段设计」并做一句话概括，避免在 README 中重复大段阶段设计内容（遵守无多拷贝原则）。

**涉及文件**：`人类手册/process/process.md`、`README.md`（二选一或分工：process 写流程与裁剪约定，README 引用）

**本步完成后 — 全工程回顾**：
- 差异与影响面：仅新增/修改上述文档的段落，无删除与重命名。
- 关键词全工程搜索：`tailoring_snapshot`、`process-tailoring`、`做法 B`、`阶段全集`、`裁剪`。
- 契约/文档：确认 README、process.md、norm-improvement-plan 中对「裁剪结果落点」的表述一致，无冲突。
 - 沉淀备忘：在 `人类手册/role-skills-design-memo.md` 追加「变更备忘：文档化阶段裁剪约定（做法 B）」，含背景/判断/方案/影响/一致性检查/遗留。

---

## 步骤 2：落实「阶段定义唯一事实来源」

**目标**：规范库内阶段定义的唯一来源为 `.cyber_team/process/phases.yaml`；其他文档仅引用并说明「与 .cyber_team/process/phases.yaml 一致」，不重复列举阶段 id/order/outputs。

**动作**：
- 检查 `人类手册/role-skills-design.md`：若存在与 phases 完全一致的阶段表格（id/order/产出等），改为「阶段定义见 `.cyber_team/process/phases.yaml`，下表/本节仅作概要或引用说明」，或删除重复表格、改为引用 + 简短说明。
- 检查其他引用阶段的文档（如 `人类手册/Cursor-多会话协作落地方案.md`、`人类手册/多智能体蜂群编排落地方案.md`、`.cyber_team/skills/project-initiation/SKILL.md`）：若有逐条列举阶段列表，改为引用 `.cyber_team/process/phases.yaml` 或「与 .cyber_team/process/phases.yaml 一致」的说明，不保留可与之冲突的副本。
- 确认 `.cyber_team/process/phases.yaml` 为全工程中**唯一**完整列举 phases 的文件。

**涉及文件**：`人类手册/role-skills-design.md`、可能涉及 `人类手册/Cursor-多会话协作落地方案.md`、`人类手册/多智能体蜂群编排落地方案.md`、`.cyber_team/skills/project-initiation/SKILL.md`、以及任何含阶段列表的文档。

**本步完成后 — 全工程回顾**：
- 差异与影响面：修改引用方式，删除或收缩重复的阶段列举。
- 关键词全工程搜索：`phases`、`phase_id`、`initiation`、`requirements`、`order`、阶段表、阶段定义。
- 清单/索引：确认 mapping、state 模板、project-docs-index 等仍使用与 phases.yaml 一致的 phase id，无遗漏。
- 沉淀备忘：在 `人类手册/role-skills-design-memo.md` 追加「变更备忘：阶段定义唯一事实来源（phases.yaml）」，含背景/判断/方案/影响/一致性检查/遗留。

---

## 步骤 3：state 模板增加 tailoring_snapshot，project-initiation 产出要求更新

**目标**：业务项目 state 支持「本项目阶段集合」的存储；project-initiation 明确产出 tailoring_snapshot 与 process-tailoring.md。

**动作**：
- 在 `.cyber_team/process/state.yaml` 中增加 **`tailoring_snapshot`** 字段（建议为列表，如 `tailoring_snapshot: []`），并在文件头注释/schema 说明中注明：本项目要执行的 phase_id 列表，与 `.cyber_team/process/phases.yaml` 的 id 一致；顺序即执行顺序；由项目启动阶段产出。
- 在 `.cyber_team/skills/project-initiation/SKILL.md` 的「产出物约定」或「与 state 的衔接」中明确：须输出 **state.tailoring_snapshot**（写入业务项目 state.yaml）及 **docs/process-tailoring.md**（裁剪理由、保留/省略/简化的阶段与活动、适用条件）。不复制 phases 内容到业务项目。
- 若存在 `.cyber_team/process/state.yaml` 的 schema 说明文档（或 README 中 state 说明），同步补充 tailoring_snapshot 的语义与用法。

**涉及文件**：`.cyber_team/process/state.yaml`、`.cyber_team/skills/project-initiation/SKILL.md`、`README.md`（若含 state 字段说明）。

**本步完成后 — 全工程回顾**：
- 差异与影响面：state 新增字段；project-initiation 产出约定更新。
- 关键词全工程搜索：`tailoring_snapshot`、`state.yaml`、`current_phase`、`completed_phases`、project-initiation、流程裁剪。
- 契约：确认 state 的 schema 说明、project-initiation 产出、norm-improvement-plan 中做法 B 描述一致；若有脚本或编排逻辑读写 state，检查是否需兼容新字段。
- 沉淀备忘：在 `人类手册/role-skills-design-memo.md` 追加「变更备忘：state 增加 tailoring_snapshot 与 project-initiation 产出约定」，含背景/判断/方案/影响/一致性检查/遗留。

---

## 步骤 4：新增阶段出口条件（可机读）与阶段转换规则说明

**目标**：Agent/Orchestrator 可判断当前阶段是否可推进到下一阶段；与 project-docs-index、产出物 status 对齐。

**动作**：
- 在 `.cyber_team/process/` 下新增阶段出口条件描述文件（推荐独立 YAML，如 `.cyber_team/process/exit-criteria.yaml` 或等价名称）：按 phase_id 列出出口条件（如：某阶段对应 project-docs-index 中哪些产出物需存在、关键文档 status 需为 approved 等）。结构需可被 Agent 解析（如 phase_id → 条件列表或检查项）。
- 在 `人类手册/process/process.md` 或 `README.md` 中增加「阶段转换规则」简短说明：何时可进入下一阶段（如：当前阶段出口条件满足、或用户确认）；并引用上述出口条件文件（引用关系，不重复罗列条件细节）。
- 确保出口条件与 `.cyber_team/process/artifact-metadata-convention.md` 的 status、`.cyber_team/process/project-docs/project-docs-index.yaml` 的键一致（phase_id、产出物类型）。

**涉及文件**：新增 `.cyber_team/process/exit-criteria.yaml`（或约定文件名）；修改 `人类手册/process/process.md` 和/或 `README.md`；必要时在 `.cyber_team/process/artifact-metadata-convention.md` 中补充一句「出口条件见 .cyber_team/process/exit-criteria.yaml」。

**本步完成后 — 全工程回顾**：
- 差异与影响面：新增出口条件文件；流程说明中增加转换规则与引用。
- 关键词全工程搜索：`exit_criteria`、`exit-criteria`、阶段转换、出口条件、approved、project-docs-index。
- 契约：确认 exit-criteria 中的 phase_id 与 phases.yaml 完全一致；与 project-docs-index 的 key、artifact 约定的 type/status 对齐。
- 沉淀备忘：在 `人类手册/role-skills-design-memo.md` 追加「变更备忘：阶段出口条件（可机读）与阶段转换规则」，含背景/判断/方案/影响/一致性检查/遗留。

---

## 步骤 5（可选）：process 下增加模板与清单索引

**目标**：便于业务项目初始化时发现需引用的模板及复制目标路径，不复制规范定义本身。

**动作**：
- 在 `.cyber_team/process/` 下新增**模板与清单索引**（如 `.cyber_team/process/README.md` 的固定章节，或独立 `.cyber_team/process/templates-index.md`）：列出「需在业务项目中创建或初始化的资产」及在规范库中的路径、建议在业务项目中的落点（如 state.yaml → 业务项目根目录；project-docs-index.yaml → 业务项目 docs/；process-tailoring.md → 业务项目 docs/；status 模板 → 业务项目 docs/status/）。每项用「规范库路径 → 业务项目目标」表述，避免在索引中重复模板全文（引用关系）。
- 在 README 或 process 说明中增加一句：业务项目初始化时可参考 `process/` 下的模板与清单索引。

**涉及文件**：新增或修改 `.cyber_team/process/README.md` 或 `.cyber_team/process/templates-index.md`；可选在 `README.md` 中增加对模板索引的引用。

**本步完成后 — 全工程回顾**：
- 差异与影响面：新增索引文档或章节，无规范内容拷贝。
- 关键词全工程搜索：`templates-index`、模板索引、复制、初始化、project-docs-index、state.yaml。
- 确认索引中的路径与现有 process 下文件一致，无死链接。
- 沉淀备忘：在 `人类手册/role-skills-design-memo.md` 追加「变更备忘：process 模板与清单索引」，含背景/判断/方案/影响/一致性检查/遗留。

---

## 全程通过标准（与规则一致）

- 全工程搜索后，无已废弃标识/旧字段/旧路径的残留引用（除明确标注的兼容代码）。
- 代码 + 配置 + 文档 + 映射/清单 + 测试（若有）保持一致，无漏改导致的断链。
- 无同名不同义、重复定义、契约不一致、引用悬空、死链接。
- 阶段、角色、映射等规范内容仅在规范库一处定义；业务项目侧仅通过 state、process-tailoring、索引等引用或项目特有内容关联规范库。

---

## 执行与备忘

- 按步骤 1 → 2 → 3 → 4 → 5（可选）顺序执行；每步完成后立即做该步的「全工程回顾」并「沉淀备忘」。
- 若某步发现与原则冲突（如某处存在阶段定义的重复拷贝），应在该步内修正并记入备忘。
- 全部步骤完成后，在 `人类手册/plan/norm-backlog.md` 的「近期进展」中追加一条：规范改进实施计划（步骤 1–4，及可选步骤 5）已完成，并注明日期。
