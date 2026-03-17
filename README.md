# 软件开发团队活动规范

本工程的目的，是为了探索智能化测试在质量体系中的落地路径，尝试通过定义流程、角色职责与工具，固化研发过程，构建多角色智能体协作机制，提升智能体产出的有效性和稳定性。

本目录为**团队活动规范**的根目录，包含流程定义、角色职责、阶段-角色-skill 映射及 skill 清单，供人工阅读与 Agent 解析使用。

**规范根目录位置**：规范库仓（本仓库）的规范母本位于 `.cyber_team/` 下（process、roles、mapping、skills、rules）；人类阅读文档在 **`人类手册/`**（仅供人读，不随规范快照复制）。业务项目以本仓 `.cyber_team/` 为规范根（可从本规范库复制快照并附带 SNAPSHOT.yaml）。路径与逻辑链接约定见 `.cyber_team/CONVENTIONS-paths-and-links.md`。

## 目录结构

- **`.cyber_team/process/`** — 流程与阶段定义；`phases.yaml` 供 Agent 判断当前阶段与顺序；人读的流程说明见 `人类手册/process/process.md`。流程预期产出物规范在此目录：`artifact-metadata-convention.md`、`project-docs/project-docs-index.yaml` 等。文档发现规则模板见 **`.cursor-templates/rules/`** 或 **`.cyber_team/rules/`**，供业务项目复制到 `.cursor/rules/`。
- **`.cyber_team/roles/`** — 角色定义；`roles.yaml` 供 Agent 解析角色与阶段关系；各角色职责说明与 SOP 见 `人类手册/roles/*.sop.md`。
- **`.cyber_team/mapping/`** — `phase-role-skill.yaml` 为核心映射，Agent 据此在给定阶段/角色下加载对应 skill。
- **`.cyber_team/skills/`** — `manifest.yaml` 列出 skill 名称、来源、适用阶段/角色；自建 skill 位于本目录下同名子目录（如 `skills/prd-requirements/`）。
- **state（运行态）** — 本规范仓库提供业务项目初始化模板 `.cyber_team/process/state.yaml` 与更新脚本 `.cyber_team/process/project-docs/status/update_state.py`。业务项目的真实进展应写入**业务项目仓库根目录**的 `state.yaml`，且**更新必须**通过业务项目中的 `scripts/update_state.py`（从规范库复制），不得直接编辑 state.yaml。
- **`人类手册/`** — 本工程（cyber_team）的开发文档与规范说明（如规范建设方案、设计说明、多智能体落地方案等，仅供人读）；不随规范快照复制到业务项目，不存放流程规范中的预期产出物定义。
- **`.cyber_team/rules/`** 与 **`.cursor-templates/rules/`** — 团队协作规范用规则（供业务项目复制到 `.cursor/rules/`）；规范母本见 `.cyber_team/rules/*.md`，模板版见 `.cursor-templates/rules/*.mdc.tpl`。本工程自身的 Cursor 规则（如修改后全工程回顾）在 **`.cursor/rules/`** 下，不随规范复制到业务项目。

## 与 Agent 的接口

1. **阶段与顺序**：读取 `.cyber_team/process/phases.yaml` 的 `phases[].id` 与 `order`。
2. **角色与阶段**：读取 `.cyber_team/roles/roles.yaml` 的 `roles[].phase_ids`。
3. **阶段/角色 → skill**：读取 `.cyber_team/mapping/phase-role-skill.yaml` 的 `mappings`，按 `phase_id`（及可选 `role_id`）得到 `skill_name`。
4. **skill 来源**：根据 `skill_name` 在 `.cyber_team/skills/manifest.yaml` 的 `skills[]` 中查找 `source`（GitHub URL 或本地相对路径）。
5. **进展状态（业务项目）**：**读**取业务项目仓库根目录的 `state.yaml`（可从 `.cyber_team/process/state.yaml` 初始化）；**写**入/更新必须通过业务项目中的 `scripts/update_state.py`（从规范库 `.cyber_team/process/project-docs/status/update_state.py` 复制），不得直接编辑 state.yaml。字段包括 `current_phase`、`completed_phases`、`tailoring_snapshot`（见 `人类手册/process/process.md` 阶段与裁剪）、`current_role`、`updated_at`。
6. **产出物发现（多智能体协作）**：业务项目内维护 `docs/project-docs-index.yaml`（可从本规范仓库 `.cyber_team/process/project-docs/project-docs-index.yaml` 复制到业务项目 docs 目录），按阶段 id 列出各产出物路径；关键文档建议带 YAML frontmatter 元数据（`phase`、`type`、`status`、`owner_role`、`updated_at`），约定见 `.cyber_team/process/artifact-metadata-convention.md`。

阶段转换规则（何时进入下一阶段）见 `人类手册/process/process.md`；出口条件的机器可读定义见 `.cyber_team/process/exit-criteria.yaml`。具体门禁由项目/团队在落地时约定。

7. **角色边界**：各阶段评审结论与评审记录由 mapping 中该阶段对应评审角色（如 requirements-reviewer）产出，项目经理负责派发任务与回收结果，不代写评审文档；各角色仅产出本角色职责内交付物（见 `.cyber_team/mapping/phase-role-skill.yaml`、`.cyber_team/roles/roles.yaml`）。

## 如何询问项目进展（给人类阅读）

当你想了解当前项目进展时，建议直接向“项目经理”角色提问，例如：

- “当前项目进展如何？卡点是什么？下一步计划是什么？”
- “现在处于哪个阶段？哪些产出已经完成并通过评审？”
- “请按角色汇总：谁在做什么、是否阻塞、需要我决策什么？”

**进展回复的输出契约（建议字段）**：

- **当前阶段**：`current_phase`（对应 `.cyber_team/process/phases.yaml` 的阶段 id）
- **已完成阶段**：`completed_phases`
- **进行中（按角色）**：每个角色的 `status/summary/blockers/next` 及关键产出物链接
- **跨角色阻塞/风险**：`project_blockers`、`project_risks`
- **需要你决策**：必须用户确认的待决策项（如有）

## 应用到业务项目：单仓 + 规范快照

推荐方式为**业务项目单仓**：在业务项目根目录建立 `.cyber_team/` 规范快照（从本规范库复制所需子集并附带 SNAPSHOT.yaml），并将 `.cursor-templates/` 中的规则与 skill 入口复制到业务项目的 `.cursor/`，详见 **`.cyber_team/process/templates-index.md`** 与规范库中的初始化脚本/说明。这样 Cursor 只打开业务项目即可，智能体以本仓 `.cyber_team/` 为规范根、以 `.cursor/rules/` 与 `.cursor/skills/` 为入口。

要让智能体在业务项目中**先读 `project-docs-index.yaml` 再按路径读具体文档**，需在业务项目中：

1. **把项目文档索引放到业务项目**  
   将本仓库的 `.cyber_team/process/project-docs/project-docs-index.yaml` 复制到业务项目 **docs 目录**（即 `docs/project-docs-index.yaml`；或团队约定的路径），并按实际产出填写/新增各阶段文档路径。

2. **在业务项目中加入 Cursor 规则**  
   将本仓库 `.cursor-templates/rules/project-docs-discovery.mdc.tpl` 复制到业务项目的 **`.cursor/rules/`** 下并改为 `.mdc` 后缀（或使用 `.cyber_team/rules/project-docs-discovery.md` 复制为 `.mdc`）。  
   该规则约定：在发现或引用阶段产出物（PRD、架构、测试计划等）时，**先读取** 项目 **docs 目录**的 `project-docs-index.yaml`，再按索引中的路径读取具体文档。

**历史方式（多根工作区）**：多根工作区已废弃，不再提供配置模板；请使用单仓 + `人类手册/scripts/setup_business_project.py` 初始化业务项目。

## 多智能体落地参考文档

本规范既支持在 Cursor 中通过多会话模拟多角色协作，也支持在后端以多智能体蜂群方式编排。对应的落地思路已在 `人类手册/` 中给出详细说明：

- **Cursor 多会话协作落地方案**：`人类手册/Cursor-多会话协作落地方案.md`  
  说明如何将本仓库的阶段/角色/skill 规范映射到 Cursor 的多个对话会话中，包括角色与会话的对应关系、各角色 pinned prompt 模板、统一任务卡模板以及一个端到端的协作示例。
- **多智能体蜂群编排落地方案**：`人类手册/多智能体蜂群编排落地方案.md`  
  说明如何以 Orchestrator + Role Agents 的方式，将 `.cyber_team/process/`、`roles/`、`mapping/`、`skills/` 视为多 Agent 系统的“配置中心”，并将**业务项目** `state.yaml` 作为运行态进展状态（阶段驱动快照），给出任务/结果数据模型、阶段驱动逻辑与分阶段落地路线。

在将本规范应用到实际业务项目或多智能体平台时，建议先通读以上两篇文档，再根据团队当前阶段选择“先从 Cursor 多会话实践起步”或“直接在后端搭建多 Agent 编排”。

## 规范来源与改进

本规范依据 `人类手册/role-skills-design.md` 建设方案生成。自建 skill 开发时须遵循 Cursor 的 **create-skill** 技能指引。

- **规范改进方案（精简版）**：`人类手册/plan/norm-improvement-plan.md` — 仅保留智能体协作必要改进项，及「阶段全集 → PM 裁剪 → 业务项目 process」的可行性与有效性评估。
- **规范改进实施计划**：`人类手册/plan/norm-improvement-execution-plan.md` — 按全工程回顾规则拆分的可执行步骤，每步含动作、涉及文件、回顾要点与备忘要求。
- **规范工程进展与待办**：`人类手册/plan/norm-backlog.md` — 本规范工程的最新进展与待办事项，作为后续工作的记忆支持。
