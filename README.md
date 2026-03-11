# 软件开发团队活动规范

本工程的目的，是为了探索智能化测试在质量体系中的落地路径，尝试通过定义流程、角色职责与工具，固化研发过程，构建多角色智能体协作机制，提升智能体产出的有效性和稳定性。

本目录为**团队活动规范**的根目录，包含流程定义、角色职责、阶段-角色-skill 映射及 skill 清单，供人工阅读与 Agent 解析使用。

**规范根目录位置**：当前约定为工作区根目录（即本目录）。Agent 与人工均以此目录为规范根路径读取 process、roles、mapping、skills、state 等文件。

## 目录结构

- **process/** — 流程与阶段定义；`phases.yaml` 供 Agent 判断当前阶段与顺序，`process.md` 供人读；流程预期产出物规范在此目录：`artifact-metadata-convention.md`（产出物元数据约定）、`project-docs/project-docs-index.yaml`（项目文档索引模板，供业务项目复制使用）。文档发现规则见 **rules/** 下 `project-docs-discovery.md`，供业务项目复制到 `.cursor/rules/`。
- **roles/** — 角色定义；`roles.yaml` 供 Agent 解析角色与阶段关系，`sop/*.md` 为各角色职责说明与 SOP。
- **stages/** — 按阶段汇总的职责、活动、验收（人读）。
- **mapping/** — `phase-role-skill.yaml` 为核心映射，Agent 据此在给定阶段/角色下加载对应 skill。
- **skills/** — `manifest.yaml` 列出 skill 名称、来源（GitHub 或本地路径）、适用阶段/角色；自建 skill 位于本目录下同名子目录（如 `skills/prd-requirements/`）。
- **state.yaml** — 当前阶段与进展，供 Agent 读写；字段见下。
- **docs/** — **本工程（cyber_team）的开发文档**（如规范建设方案、设计说明等，人读）；不存放流程规范中的预期产出物定义。已新增多智能体落地方案文档，见下文。
- **rules/** — 团队协作规范用规则（供业务项目复制到 `.cursor/rules/`）：`work-execution-standards.md`、`project-docs-discovery.md`。本工程自身的 Cursor 规则（如修改后全工程回顾）在 **`.cursor/rules/`** 下，不随规范复制到业务项目。

## 与 Agent 的接口

1. **阶段与顺序**：读取 `process/phases.yaml` 的 `phases[].id` 与 `order`。
2. **角色与阶段**：读取 `roles/roles.yaml` 的 `roles[].phase_ids`。
3. **阶段/角色 → skill**：读取 `mapping/phase-role-skill.yaml` 的 `mappings`，按 `phase_id`（及可选 `role_id`）得到 `skill_name`。
4. **skill 来源**：根据 `skill_name` 在 `skills/manifest.yaml` 的 `skills[]` 中查找 `source`（GitHub URL 或本地相对路径）。
5. **进展状态**：读写 `state.yaml`，字段包括 `current_phase`（与 phases.yaml 的 id 一致）、`completed_phases`、`current_role`、`updated_at`。
6. **产出物发现（多智能体协作）**：业务项目内维护 `project-docs-index.yaml`（可从本规范仓库 `process/project-docs/project-docs-index.yaml` 复制），按阶段 id 列出各产出物路径；关键文档建议带 YAML frontmatter 元数据（`phase`、`type`、`status`、`owner_role`、`updated_at`），约定见 `process/artifact-metadata-convention.md`。

阶段转换规则（何时进入下一阶段）由项目/团队在落地时约定，约定后可在 `process/process.md` 或本 README 中写明。

## 如何询问项目进展（给人类阅读）

当你想了解当前项目进展时，建议直接向“项目经理”角色提问，例如：

- “当前项目进展如何？卡点是什么？下一步计划是什么？”
- “现在处于哪个阶段？哪些产出已经完成并通过评审？”
- “请按角色汇总：谁在做什么、是否阻塞、需要我决策什么？”

**进展回复的输出契约（建议字段）**：

- **当前阶段**：`current_phase`（对应 `process/phases.yaml` 的阶段 id）
- **已完成阶段**：`completed_phases`
- **进行中（按角色）**：每个角色的 `status/summary/blockers/next` 及关键产出物链接
- **跨角色阻塞/风险**：`project_blockers`、`project_risks`
- **需要你决策**：必须用户确认的待决策项（如有）

## 应用到业务项目：让智能体读到 project-docs-index.yaml

在实际开发项目中，Cursor 等环境通常只自动加载该项目的 **rules**（`.cursor/rules/`）和 **skills**，不会直接加载本规范仓库的 `process/` 目录。要让智能体在业务项目中**先读 `project-docs-index.yaml` 再按路径读具体文档**，需在业务项目中做两件事：

1. **把项目文档索引放到业务项目**  
   将本仓库的 `process/project-docs/project-docs-index.yaml` 复制到业务项目仓库**根目录**（或团队约定的路径），并按实际产出填写/新增各阶段文档路径。

2. **在业务项目中加入一条 Cursor 规则**  
   将本仓库的 `rules/project-docs-discovery.md` 复制到业务项目的 **`.cursor/rules/`** 下（可保留原名或改为如 `project-docs-discovery.md`）。  
   该规则会随项目被 Cursor 加载，并约定：在发现或引用阶段产出物（PRD、架构、测试计划等）时，**先读取** 项目根目录的 `project-docs-index.yaml`，再按索引中的路径读取具体文档。

这样，智能体在业务项目中只能读到该项目的 rules 和 skills 时，仍会通过这条规则获知「先读 project-docs-index.yaml」，从而正确发现并读写各阶段产出物路径。

**多会话协作（多根工作区）**：若采用《Cursor-多会话协作落地方案》中的多会话方式，需将业务项目与本规范仓库加入同一 Cursor 工作区。本仓库提供多根工作区配置说明与模板：`process/project-docs/workspace-config/` 目录下的 `cursor-multi-root-workspace.code-workspace.template` 与 `workspace-setup.md`，复制模板为 `xxx.code-workspace` 并按说明填写路径后，用 Cursor「打开工作区来自文件」即可。

## 多智能体落地参考文档

本规范既支持在 Cursor 中通过多会话模拟多角色协作，也支持在后端以多智能体蜂群方式编排。对应的落地思路已在 `docs/` 中给出详细说明：

- **Cursor 多会话协作落地方案**：`docs/Cursor-多会话协作落地方案.md`  
  说明如何将本仓库的阶段/角色/skill 规范映射到 Cursor 的多个对话会话中，包括角色与会话的对应关系、各角色 pinned prompt 模板、统一任务卡模板以及一个端到端的协作示例。
- **多智能体蜂群编排落地方案**：`docs/多智能体蜂群编排落地方案.md`  
  说明如何以 Orchestrator + Role Agents 的方式，将 `process/`、`roles/`、`mapping/`、`skills/`、`state.yaml` 视为多 Agent 系统的“配置中心”，并给出任务/结果数据模型、阶段驱动逻辑与分阶段落地路线。

在将本规范应用到实际业务项目或多智能体平台时，建议先通读以上两篇文档，再根据团队当前阶段选择“先从 Cursor 多会话实践起步”或“直接在后端搭建多 Agent 编排”。

## 规范来源

本规范依据 `docs/role-skills-design.md` 建设方案生成。自建 skill 开发时须遵循 Cursor 的 **create-skill** 技能指引。
