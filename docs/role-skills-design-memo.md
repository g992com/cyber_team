# 软件开发团队活动规范与角色 Skills 建设 — 讨论备忘

本文档记录从「各角色 skill 建设」到「团队活动规范 + Agent 驱动」的讨论重点与思路变化，供后续查阅与延续设计时参考。

---

## 设计思路重要转变点（简表）

| 阶段 | 转变点 | 一句话 |
|------|--------|--------|
| **角色范围** | 从「执行角色」到「执行 + 评审」 | 补评审专家，与执行角色区分；安全评审并入架构评审（方案 A）。 |
| **粒度** | 从「一角色一 skill」到「一角色多 skill」 | 产品经理、需求评审专家按文档类型拆成 2～3 个 skill；检索词按子领域分表。 |
| **组织方式** | 从「按角色列」到「按流程驱动」 | 先定流程与阶段，再按阶段定角色职责/活动/SOP/验收，再挂 skill。 |
| **交付形态** | 从「选型文档」到「活动规范 + 选型」 | 目标扩大为团队活动规范；职责说明、SOP、验收要求纳入，并给示例。 |
| **文档定位** | 从「交付物」到「建设方案」 | 本文档是方案；最终规范是一组结构化文件（流程、职责、skills 等）。 |
| **使用者** | 从「人用 skill」到「人 + Agent 双用」 | 产出既要可读也要供 Agent 解析；流程为规范流程以约束 Agent 求稳定输出。 |
| **技能触发** | 从「人工选 skill」到「Agent 自决」 | 期望由 Agent 决定并记录阶段与进展，自动启用对应角色与 skill，无需人工介入。 |
| **产出形态** | 从「无目录约定」到「结构化目录」 | 最终规范为一组文件；设计「最终产出的目录结构」：process/、roles/、stages/、mapping/、skills/ 等，人可读 + Agent 可解析。 |

---

## 一、起点：建设各角色的 skill

**最初目标**：为软件工程各角色建设可复用的 Cursor Agent Skills。

**初步思路**：
1. 设计所需角色和职责；
2. 通过 SkillsMP 从 skillsmp.com 获取与角色匹配的 skills，并做安全检查；
3. 从获取的 skills 中比较、选择最合适的，或自行设计 skills。

**已确认的约束**：
- 选型原则：匹配度优先，安全为硬门槛（无 Critical 才采纳）；
- 交付物：设计文档（本阶段不执行安装）；
- 设计文档路径：工作区根目录 `role-skills-design.md`；
- 检索前先将每个角色扩展为 5～10 条具体职责。

---

## 二、角色与评审专家的补充

**讨论点**：角色中是否要考虑评审专家？

**结论**：增加**评审专家**类角色，与「执行角色」区分：执行角色负责产出，评审专家负责审查与改进建议。

**纳入的角色**：
- 需求评审专家、代码评审专家、设计评审专家、测试评审专家；
- 安全领域评审采用**方案 A**：并入设计评审专家，不单独设安全评审专家；实现层安全由代码评审专家在 PR 中顺带覆盖。

**DBA / SRE / DevOps**：这三个领域的评审统一由**设计评审专家**负责。

---

## 三、SkillsMP 检索与安全扫描的执行

- 配置 API Key 后执行了关键词检索与部分 AI 语义检索；
- 对候选 skill 做了安全扫描，按「无 Critical 才采纳」筛掉一批（如 NeverSight/backend-dev-guides、devops-cicd、LambdaTest/cicd-pipeline-skill、scope-appropriate-architecture、devdocs-requirements 等）；
- 采纳了 frontend-design、backend-development、pytest、user-story、flyway-migration、code-review、technical-writer、review-pr 等，并补充了 **code-review-expert（sanyuan0704）**，经人工确认安全后纳入。

---

## 四、文档类型图与方案的关系

**讨论点**：图中「文档类型 → AI 认知 → 代码生成指导」的产物，对方案有什么帮助？

**结论**：
- 用于**角色/职责与 skill 的对应**：用户故事、PRD、架构设计、API 设计、数据库设计、开发计划等，分别对应产品经理、需求评审、架构师、后端、DBA 等角色及其技能；
- 用于**自建 skill 规格**：自建时可按「输入文档类型 → 期望认知 → 代码生成指导」来写 description 与触发场景；
- **评审专家保障的正是这些产物**：确保文档能产出应有认知，后续代码生成才有依据；
- 可在设计文档中统一采用图中文档类型作为各 role skill 的触发或上下文说明。

---

## 五、检索词优化与产品经理的多 skill

**讨论点**：
1. 各角色检索关键字是否需要优化？
2. 产品经理是否需要多个 skill 支持？

**结论**：
- **检索词**：按职责细分、与文档类型对齐、评审与执行分离，做了一轮优化（如 PRD、acceptance criteria、ADR、schema、SLO、PR review 等）；
- **产品经理**：建议由 **2～3 个 skill** 支持——① 用户故事与验收标准（已采纳 user-story）；② PRD/产品需求文档（检索或自建）；③ 可选 故事地图/路线图/估算；
- **需求评审专家**：同样按 2～3 个 skill 扩展——① 用户故事与验收标准评审；② PRD/需求文档评审；③ 可选 路线图或计划与追溯评审；检索词与自建规格在文档中分表列出。

---

## 六、代码评审 skill：code-review-expert（sanyuan0704）

- 将 **code-review-expert** 纳入代码评审专家候选；因仓库根目录 SKILL.md 导致 SkillsMP 扫描 URL 格式不通过，先标注「建议人工确认」；
- 用户确认该 skill 安全后，文档中统一改为「已人工确认安全，可放心安装」；
- **人工确认**方式：在设计文档附录中增加了「人工确认 skill 安全的步骤与检查清单」（获取代码、确认范围、按检查项排查、做结论、安装与后续），便于在无法自动扫描时使用。

---

## 七、职责说明、SOP 与验收要求

**讨论点**：是否还需要创建各角色对应的职责说明、SOP 及各步骤验收要求？

**结论**：需要。在设计文档中增加「角色职责说明、SOP 与验收要求」一节，提供通用模板，并给出**代码评审专家**、**需求评审专家（用户故事与验收标准）**两个完整示例（职责说明 + SOP 步骤 + 各步骤验收要求表）；其余角色可按模板后续补全或拆为独立文档（如 roles-sop.md）。

---

## 八、组织方式：流程驱动 + 三层结构

**讨论点**：是否按「流程 → 阶段内角色职责/活动/SOP/验收 → 角色-活动-skill」来组织？

**结论**：采用**流程驱动**的三层结构：

1. **定义完整的软件开发流程**：阶段与阶段产出（需求、需求评审、架构/设计、设计/架构评审、开发、代码评审、测试、测试评审、部署/发布、运维/复盘）；
2. **按阶段定义各角色的职责、活动、SOP 与验收标准**：每阶段谁负责什么、做什么、按什么步骤做、怎样算完成；
3. **定义每个角色在活动中需要使用的 skill**：阶段 × 角色 × 活动 对应到具体 skill。

设计文档据此重组：先流程（第 3 节），再各阶段角色与验收（第 4 节），再角色-活动-技能对照（第 5 节），后接角色清单、选型结果、自建规格、SOP 示例与附录。

---

## 九、目标扩大：从「角色 skill」到「团队活动规范」

**讨论点**：原来的目标只是建立各角色的 skill，现在看目标是否应扩大？

**结论**：目标扩大为建立**软件开发团队的活动规范**，并在此基础上定义各角色在活动中使用的 skill。文档标题改为「软件开发团队活动规范与角色 Skills 选型设计」，概述中明确：先定义团队级流程与各阶段角色职责、活动、SOP 及验收标准，再据此确定各角色在活动中使用的 skill，使活动规范与 skill 落地一致。

---

## 十、目标扩大带来的问题与澄清

**讨论点**：这样的目标改变，有什么问题？

**提出的四点与用户澄清**：

| 点 | 提出的顾虑 | 用户澄清 / 结论 |
|----|------------|----------------|
| **范围与维护成本** | 单文档承载「活动规范 + skill 选型」，维护面大。 | 本文档只是**建设方案**；最终规范是**一组结构化的文件**（流程要求、职责、skills 等），不是这一份文档本身。 |
| **受众与使用场景** | 活动规范给人看，skill 给 Agent 用，受众可能不同。 | 最终产出需**既可读、也供 Agent 使用**，要兼顾人与机器。 |
| **流程是参考还是强制** | 流程若写为「参考模型」，团队可能裁剪，与文档脱节。 | 因为最终是**给 Agent 用**（单 Agent 连续或多 Agent 协作），需要**规范流程**才能得到**尽可能稳定的输出**，因此流程按规范定义。 |
| **Skill 触发方式** | 文档写了「阶段 X 用 skill S」，但 Cursor 里 skill 多由用户或上下文触发。 | 期望的最终形态是**不需要人工介入**——应由 **Agent 决定和记录当前阶段与进展**，并据此**决定需要启用的角色及 skill**。 |

---

## 十一、方案定位与最终形态（写入设计文档）

根据上述澄清，在设计文档中固化了以下表述：

- **本文档性质**：建设方案；最终交付的规范是一组**结构化文件**（流程、阶段、角色职责、活动、SOP、验收、skills 等），可多文件、多格式。
- **受众与形态**：最终产出**既可供人阅读，也供 Agent 使用**；流程、职责与技能对照在落地时需**可读 + 可被 Agent 解析**（如结构化描述或机器可读配置）。
- **流程的规范性**：为获得稳定、可复现的输出，流程按**规范流程**定义；阶段、角色与验收共同约束 Agent（单 Agent 或多 Agent 协作）。
- **阶段与 skill 启用的目标形态**：由 **Agent 决定并记录当前阶段与进展**，并**自动决定应启用的角色与 skill**；本方案中的流程与阶段-角色-活动-技能对照为后续实现「Agent 自主判断阶段、切换角色与加载对应 skill」提供规格基础；落地时需将阶段、进展与角色/skill 映射变为 **Agent 可读、可推理、可执行** 的形式（如状态、规则或配置）。

---

## 十二、备忘使用说明

- 本备忘与主设计文档 **role-skills-design.md** 配套使用：主文档承载当前方案与规格，本备忘承载**讨论重点与思路变化**。
- 后续若调整目标、流程或 Agent 驱动形态，可在本备忘末尾按时间或主题追加「十三、十四…」；主文档若有结构性变更，也可在本备忘中记一笔变更原因与对应章节。

---

## 十三、最终产出的目录结构（设计）

**讨论点**：是否可以开始设计最终产出的目录结构？

**结论**：可以。在主设计文档中新增 **第 12 节「最终产出的目录结构（建议）」**，约定规范根目录下：`README.md`、`process/`（phases.yaml + process.md）、`roles/`（roles.yaml + sop/*.md）、`stages/*.md`、`mapping/phase-role-skill.yaml`、`skills/manifest.yaml` 与 `.cursor/skills/`。其中 YAML 与 manifest 供 Agent 解析以判断阶段、角色与加载 skill；Markdown 供人读。附录由原 12 节顺延为 13 节。

**补充**：① 与已有 skill **不合并**，规范单独成结构；用户已修改原 skill 目录名称以区分。② 自建 skill 按**软件开发阶段顺序**落地（需求→需求评审→设计→设计评审→…→运维/复盘），已写入第 12 节与第 10 节。③ 第 12 节补充：**规范根目录放置位置**由项目/团队约定（如 ./team-norms/ 或独立 repo）；**进展/状态**需定义表示与存储（如 state.yaml 含 current_phase、completed_phases、current_role 等），供 Agent 读写；**Agent 用 YAML 约定（草案）**给出 phases.yaml、roles.yaml、phase-role-skill.yaml、manifest.yaml 的建议字段表。

---

## 十四、整体检视与修正

**检视范围**：对 role-skills-design.md 做通篇一致性检查。

**修正项**：① **选型检查单（第 7 节）**：「与目标角色职责直接相关」的引用由「2 中条目」改为「第 6 节职责列表」（第 2 节为文档组织方式，职责在第 6 节）。② **第 12 节目录树**：在规范根目录下补充 **state.yaml（或 .agent/state.yaml）**，与「进展/状态的表示与存储」表述一致。③ **阶段转换规则**：在「进展/状态的表示与存储」后增加一句：何时进入下一阶段**待落地时约定**，约定后可在 process 或 README 中写明。④ **phases.yaml 的 id**：在 Agent 用 YAML 约定表中明确 **phase id 建议与第 3 节「英文标识」一致**（如 requirements, code-review），便于与 mapping、state 统一。

**自建 skill 开发约定**：用户要求开发自建 skill 时须**使用 create-skill 技能**。已在设计文档第 10 节增加「开发自建 skill 时的必遵约定」：实施任一自建 skill 前必须先阅读并遵循 Cursor 的 create-skill（Discovery → Design → Implementation → Verification），按 create-skill 的 SKILL.md 结构、description 规范（WHAT+WHEN、第三人称）、篇幅与引用要求编写。

---

## 十五、本次对话新增：项目经理角色、进展记录与触发式调度闭环

### 15.1 讨论背景与问题

本次对话围绕「多智能体协作解决复杂软件开发项目」补齐了两类缺口：

1. **流程裁剪与计划制定**：当用户提出问题/需求后，需要一个“居中”角色按活动规范裁剪项目活动，确定阶段与计划，避免各角色智能体各自推进导致返工与漂移。
2. **开发期进展对接与问题处置**：用户询问项目进展、或开发中出现跨角色冲突/阻塞/风险时，需要有规范化的记录与触发式调度机制，保证可追溯、可升级、可恢复推进。

### 15.2 关键判断（Why）

- **是否需要类似项目经理的角色**：需要。其价值在多智能体环境更明显（跨阶段对齐、裁剪、统一计划、冲突归因与处置规划）。
- **是否常驻调度**：不建议强依赖常驻调度；采用**触发式介入（Triggered）**更适合，避免项目经理成为单点瓶颈，同时在“系统性问题出现时”仍能形成闭环。
- **进展对接由谁负责**：用户询问项目进展时，由**项目经理**角色智能体对接最合适（跨阶段汇总、风险与下一步计划）。
- **其他角色工作情况如何记录**：需要分层记录：`state.yaml` 存**最新摘要与指针**，角色级明细以日志保留历史，便于追溯与交接。
- **是否累积历史记录**：推荐保留历史（append-only），但要通过“当前有效信息区 + 过期标记 + 可归档 + 敏感信息红线”控制噪声与误导风险。

### 15.3 解决方案（What）

#### 15.3.1 新增阶段与角色：项目启动 + 项目经理

- **新增阶段**：`initiation`（项目启动），位于需求前，用于项目启动、流程裁剪与计划制定（参考 PMBOK tailoring 与 ISO/IEC/IEEE 16326 项目管理计划实践）。
- **新增角色**：`project-manager`（项目经理），主要职责：
  - 根据用户问题/需求按活动规范裁剪阶段与活动
  - 输出项目计划、流程裁剪说明、阶段与活动清单
  - 在执行期以触发式介入处理跨角色冲突/阻塞/风险/计划偏离

#### 15.3.2 触发式项目经理接入（Escalation）闭环

- **触发条件**（任一满足即触发）：跨角色冲突、阻塞升级、风险升级、计划偏离。
- **谁触发**：
  - 默认：发现问题的角色智能体升级（谁发现谁触发）
  - 兜底：用户直接问“卡住/进展/怎么推进”或持续 blocked 时，项目经理主动接入
- **升级信息包（Escalation packet）**：要求提供最小证据包（symptom/evidence/impact/options/decision_needed/recommended_next），降低“口头争议”，提高归因与处置效率。
- **项目经理处置产出**（至少一个）：问题分析与处置计划 / 更新后的阶段与活动清单 / 待澄清与待决策清单。

#### 15.3.3 进展记录：项目级摘要 + 角色级明细（模板化）

- **项目级（摘要）**：扩展 `state.yaml`，新增 `role_updates`（各角色最新 status/summary/artifacts/blockers/next/updated_at）以及 `project_blockers`、`project_risks`。
- **角色级（明细）**：以模板方式提供在 `process/project-docs/status/`，业务项目复制后建议放 `docs/status/{role_id}.md`。
  - per-session 追加记录（append-only）
  - 文件顶部维护“当前有效信息区（Current）”
  - 被推翻结论标注 superseded（或指向替代条目/文档）
  - 可按月/里程碑归档
  - 禁止写入敏感信息（密钥/令牌/口令/敏感数据）

#### 15.3.4 人读与 Agent 用的分层说明

- **项目经理智能体执行口径**写入 `roles/sop/project-manager.md`（读什么、怎么汇总、输出结构）。
- **README 仅面向人类**：补充“如何询问进展 + 输出契约（字段）”，避免把智能体内部读取实现细节写入工程介绍。

#### 15.3.5 修改后全工程回顾（防遗漏/防冲突）

为减少规范演进时的联动遗漏，新增工程级规则：每次完成修改后必须做全工程回顾（id 一致性、mapping/manifest、模板与元数据约定、人读/机读一致性），并在最终输出中说明影响面与已检查项。

### 15.4 已落地到仓库的结构化文件（Where）

> 下列为本次对话中新增/更新的关键文件（以仓库内最终落地为准）：

- `process/phases.yaml`：新增 `initiation` 阶段
- `roles/roles.yaml`：新增 `project-manager` 角色
- `roles/sop/project-manager.md`：项目经理职责/SOP + 触发式介入 + 进展汇总口径
- `stages/initiation.md`：项目启动阶段的人读说明
- `mapping/phase-role-skill.yaml`：`initiation` → `project-manager` → `project-initiation` 映射
- `skills/manifest.yaml` + `skills/project-initiation/SKILL.md`：新增自建 skill（项目启动与流程裁剪）
- `state.yaml`：扩展进展摘要字段（role_updates/project_blockers/project_risks）
- `process/project-docs/status/`：新增角色进展日志模板（含通用模板与项目经理模板）
- `process/project-docs/project-docs-index.yaml`：补齐 `initiation` 阶段产出路径键
- `process/artifact-metadata-convention.md`：补齐 `initiation` 的建议 type
- `README.md`：补充人类可读的“如何询问进展 + 输出契约”；并在 rules 列表中引用新增规则
- `rules/post-change-global-review.md`：新增“修改后全工程回顾”规则（alwaysApply）

---

## 十六、变更备忘（2026-03-10）：多智能体规范落地方案（Cursor 多会话 & 蜂群编排）

### 背景/触发（Context）
- 用户希望基于本仓库规范，在两类场景下落地多智能体协作：
  - 在 Cursor IDE 中，通过多个对话会话（session）扮演不同角色进行协作；
  - 在后端通过拉起多个智能体（orchestrator + role agents）的“蜂群式”编排方式执行规范。
- 需要将这两类落地思路系统化沉淀到 `docs/`，既便于人阅读，也便于未来具体工程实现时直接引用。

### 关键判断（Why）
- **统一规范内核**：将本仓库视为“多智能体编排内核”的配置中心（process/、roles/、mapping/、skills/、state.yaml + 文档索引协议），无论是 Cursor 多会话还是蜂群编排，都应在此基础上工作，而非各自造规范。
- **先易后难**：优先推进 Cursor 多会话方案，原因是：
  - 不依赖额外基础设施，团队只需调整使用方式即可体验“多角色协作”的价值；
  - 可以作为“人工版 orchestrator + role agents”的样板，为后续自动化蜂群实现提供行为参考。
- **显式任务与角色边界**：无论是多会话还是蜂群，都应通过“任务卡 + pinned prompt/SKILL”的方式显式表达：
  - 当前阶段、涉及角色、输入材料、输出要求与验收标准；
  - 角色之间的边界与交接，避免职责模糊。

### 备选方案与取舍（Options）
- 方案 A：仅在 README 中用几段文字简单描述“可以用多会话/多 Agent 来用这套规范”，不另建详细文档。  
  - 未选原因：信息过于粗粒度，无法作为实际实施的操作指引；难以支撑后续工程实现中的细节决策。
- 方案 B（采用）：在 `docs/` 下新增两篇中文方案文档，分别针对 Cursor 多会话协作与多智能体蜂群编排，给出角色映射、数据模型与分阶段落地路线，并在 README 中提供入口说明。  
  - 采用原因：结构清晰、可逐步扩展；既不绑具体技术栈，又能为实际实现提供足够细节。

### 最终方案（What）
- 新增 `docs/Cursor-多会话协作落地方案.md`：
  - 定义推荐会话与角色映射（项目总控/产品/架构/开发/测试/DevOps 等）；
  - 给出统一 pinned prompt 骨架与项目经理/产品角色示例；
  - 设计统一“任务卡”模板与多会话之间的流转方式；
  - 提供从需求→PRD→评审→阶段推进的端到端协作示例，并说明与业务项目 `project-docs-index.yaml` 的对接方式；
  - 给出如何在团队内启动试运行的步骤建议。
- 新增 `docs/多智能体蜂群编排落地方案.md`：
  - 定义 Orchestrator Agent 与各 Role Agent 的职责；
  - 给出 Task/Result 的数据模型（phase_id/role_id/skill_name/inputs/expected_outputs 等）；
  - 描述基于 `process/phases.yaml` + `state.yaml` 的阶段驱动与完成判定逻辑；
  - 说明与 `project-docs-index.yaml` + frontmatter 协议的集成方式；
  - 设计从只自动化 PRD → 加入架构与测试设计 → 串联开发与 CI/CD 的分阶段落地路线；
  - 总结多 Agent 抽象与现有规范文件之间的一一映射关系。
- 更新 `README.md`：
  - 在目录结构中点明 `docs/` 已包含多智能体落地方案文档；
  - 新增「多智能体落地参考文档」小节，链接上述两篇文档，并建议团队在应用规范到业务项目或多 Agent 平台前先阅读这两篇说明。

### 影响范围（Where）
- 变更文件：
  - 新增：`docs/Cursor-多会话协作落地方案.md`、`docs/多智能体蜂群编排落地方案.md`
  - 修改：`README.md`、`docs/role-skills-design-memo.md`
  - 删除/重命名：无
- 受影响的映射/契约/索引（如有）：
  - 概念上强化了 `process/`、`roles/`、`mapping/`、`skills/`、`state.yaml` 与 `project-docs-index.yaml` 的中心地位，但未修改这些文件本身；
  - 明确这些文件共同构成多 Agent 系统的“配置与状态内核”。

### 一致性检查（Check）
- 全工程搜索关键词：
  - `Cursor 多会话协作落地方案`
  - `多智能体蜂群编排落地方案`
- 已检查的清单/索引/映射：
  - `README.md`：确认已新增“多智能体落地参考文档”小节，并正确指向两篇 docs；
  - `docs/role-skills-design-memo.md`：确认新增条目与既有结构一致；
  - `docs/` 目录现有文件：`role-skills-design.md`、`role-skill-consistency-check.md` 与新增两篇文档在定位上互补，无重复或冲突。
- 已运行的诊断：
  - 本轮改动仅涉及 Markdown 文档与 README 文本，无代码与配置 schema 更改，暂未运行额外 lint/类型检查；后续如引入执行层代码，再补充对应诊断。

### 遗留与后续（Next）
- 后续可考虑：
  - 在单独 demo 仓库中，基于本方案实现一个最小可行的多 Agent 例子（例如只覆盖 PRD 阶段的 Orchestrator + Product/QA Agents）；
  - 为多 Agent 实现增加更细粒度的 SKILL 设计（例如专门的 orchestrator skill、task-routing skill 等），并在本仓库 `skills/` 中补充对应 SKILL.md；
  - 根据实际使用 Cursor 多会话协作的反馈，迭代 pinned prompt 模板与任务卡模板，将成熟结论同步更新到 `docs/Cursor-多会话协作落地方案.md`。

---

## 变更备忘（2026-03-10）：process/templates 更名为 process/project-docs

### 背景/触发（Context）
- 用户要求调整工程结构：将 `process/templates` 改名为 `process/project-docs`，并对工程中涉及原目录的引用做统一更新。

### 关键判断（Why）
- **语义更贴切**：`project-docs` 直接表达“项目文档相关模板/索引”的用途，比泛化的 `templates` 更易理解。
- **引用一致性**：所有指向“项目文档索引模板、cursor 规则模板、角色状态模板”的路径需统一改为新目录，避免断链。

### 备选方案与取舍（Options）
- 方案 A：仅重命名目录，不更新文档内路径说明。未选原因：README 与多篇 docs 中明确写了“从本仓库 process/templates/... 复制”，会导致读者按旧路径找不到文件。
- 方案 B（采用）：重命名目录并全工程搜索替换 `process/templates` → `process/project-docs`。采用原因：保证文档与目录一致，复制指引可继续使用。

### 最终方案（What）
- 将 `process/templates` 目录重命名为 `process/project-docs`，原目录下文件迁移至新目录后删除旧目录。
- 新目录结构保持不变：`project-docs-index.yaml`、`cursor-rule-project-docs-discovery.md`、`status/project-manager.md`、`status/role-status-template.md`。
- 全工程内所有 `process/templates` 及 `templates/`（在 process 语境下）的引用改为 `process/project-docs` 或 `project-docs/`。

### 影响范围（Where）
- 变更文件：
  - 新增：`process/project-docs/` 下 4 个文件（从原 templates 迁移）
  - 修改：`README.md`、`docs/role-skills-design-memo.md`、`docs/多智能体蜂群编排落地方案.md`、`docs/Cursor-多会话协作落地方案.md`、`roles/sop/project-manager.md`、`state.yaml`、`process/project-docs/cursor-rule-project-docs-discovery.md`（其内部自引用路径）
  - 删除：`process/templates/` 下全部文件及目录
- 受影响的映射/契约/索引（如有）：无独立 manifest 或索引文件列出 process 子目录；README 与各 docs 中的路径说明已全部更新。

### 一致性检查（Check）
- 全工程搜索关键词：`process/templates`、`templates/project-docs-index`、`templates/cursor-rule`、`templates/status`
- 已检查的清单/索引/映射：README.md、state.yaml、各 docs、roles/sop、process/project-docs 内规则文件。
- 已运行的诊断：未运行 lint（本次仅涉及目录重命名与文本替换）；确认无残留 `process/templates` 引用。

### 遗留与后续（Next）
- 无。若后续有外部文档或脚本硬编码 `process/templates`，需单独更新。

---

## 变更备忘（2026-03-10）：Rules 集中至 rules/ + Cursor 方案文档细化与多根工作区模板

### 背景/触发（Context）
- 用户要求：将规范中的 rules 文件集中到 `rules/` 下；细化《Cursor-多会话协作落地方案》——增加在实际项目中的部署结构图、Rules/Skills 关联说明、各角色 pinned prompt；Skills 按多根工作区实施并生成项目配置模板。
- 目标：规则统一入口、方案文档可落地、多根工作区一键配置。

### 关键判断（Why）
- Rules 集中：`.cursor/rules/` 与 `process/project-docs/` 下规则分散，复制到业务项目时引用易混淆；集中到 `rules/` 后，README 与方案文档统一写“从 rules/ 复制”，业务项目侧只需认 rules/。
- Skills 仅多根：不提供“复制 skills 到业务项目”的替代方案，避免 SKILL.md 内 process/roles/mapping 等路径在单根下失效；多根下规范根即第二根，路径无需改。
- 项目配置模板：提供 `.code-workspace.template` 与 `workspace-setup.md`，用户复制后填 path 即可打开多根工作区，降低落地门槛。

### 备选方案与取舍（Options）
- 方案 A：规则保留在 .cursor/rules 与 process/project-docs，仅在文档中说明两处。未选原因：用户明确要求集中到 rules/ 并调整引用。
- 方案 B（采用）：规则迁移至 rules/，全工程引用替换；方案文档增加 6.0 部署结构、Rules/Skills 关联、多根模板与 pinned prompt 补全。

### 最终方案（What）
- **Rules 集中**：新增 `rules/post-change-project-wide-review.mdc`、`rules/project-docs-discovery.md`（内容来自原 .cursor/rules 与 process/project-docs）；删除 `.cursor/rules/post-change-project-wide-review.mdc`、`process/project-docs/cursor-rule-project-docs-discovery.md`。README、Cursor-多会话协作落地方案 中所有“复制规则”的路径改为 `rules/` 下对应文件名。
- **方案文档**：在「六」前新增「6.0 在实际项目中的部署结构」：Mermaid 图（业务项目根 + 规范仓库）、Rules 与 Skills 的关联方式（Rules 复制到业务项目 .cursor/rules/；Skills 仅多根 + 使用配置模板）。补全 pinned prompt：3.4 架构师、3.5 开发工程师、3.6 测试工程师、3.7 DevOps、3.8 评审类通用（含 role_id/phase_id/skill 表）。
- **多根工作区模板**：新增 `process/project-docs/cursor-multi-root-workspace.code-workspace.template`（两 folders：业务项目、规范仓库）、`process/project-docs/workspace-setup.md`（path 填写说明与使用步骤）。README 增加多会话多根工作区一句，方案文档 6.0 中写明使用该模板打开工作区。

### 影响范围（Where）
- 新增：`rules/post-change-project-wide-review.mdc`、`rules/project-docs-discovery.md`、`process/project-docs/cursor-multi-root-workspace.code-workspace.template`、`process/project-docs/workspace-setup.md`
- 删除：`.cursor/rules/post-change-project-wide-review.mdc`、`process/project-docs/cursor-rule-project-docs-discovery.md`
- 修改：`README.md`、`docs/Cursor-多会话协作落地方案.md`、`docs/role-skills-design-memo.md`（本备忘）
- 受影响的映射/契约：无 manifest 或 mapping 变更；README 目录结构、应用业务项目步骤、方案文档中规则与模板路径已统一。

### 一致性检查（Check）
- 全工程搜索关键词：`cursor-rule-project-docs-discovery`、`process/project-docs/cursor-rule`、`post-change-project-wide-review`、`rules/project-docs-discovery`、`workspace-template`、`workspace-setup`
- 已检查：README、Cursor-多会话协作落地方案、workspace-setup.md、role-skills-design-memo 历史条目（保留不改，仅追加本条）
- 已运行诊断：未运行 lint（以 Markdown/YAML 为主）

### 遗留与后续（Next）
- 规范仓库内若需 Cursor 自动应用 rules，可将 `rules/` 下文件复制到本仓库 `.cursor/rules/` 或配置 Cursor 读取 rules/；未在本次自动配置。
- 多根工作区模板中第二个 folder 的 path 以“模板放在规范仓库根目录”为默认假设；若用户将 .code-workspace 放在业务项目根，需按 workspace-setup.md 自行改两 path。

**补充（同日）**：`post-change-project-wide-review.mdc` 为本工程（cyber_team）自身的开发规则，不属于团队协作规范，已移回 `.cursor/rules/`。README 与方案文档已更新：`rules/` 仅列供业务项目复制的规则（work-execution-standards、project-docs-discovery）；本工程专用规则在 `.cursor/rules/`，不随规范复制到业务项目。

**路径变更（同日）**：多根工作区配置说明与模板已单独放入目录 `process/project-docs/workspace-config/`，内含 `workspace-setup.md` 与 `cursor-multi-root-workspace.code-workspace.template`；README、Cursor-多会话协作落地方案 中相关引用已更新为该目录。

---

## 变更备忘（2026-03-11）：评审角色 pinned prompt 可直接粘贴

### 背景/触发（Context）
- 用户希望在《Cursor-多会话协作落地方案》中，**保留评审类通用骨架**的同时，把需求/设计/代码/测试评审角色的 pinned prompt 都列出来，便于直接复制粘贴到对应会话使用，减少替换占位符的成本与误差。

### 关键判断（Why）
- 通用骨架保留：用于解释“评审类角色共享约定”，也便于后续扩展更多评审角色。
- 直接粘贴实例补齐：将 `<角色名称>/<role_id>/<phase_id>` 固化为四个常用评审角色，降低用户在落地时的操作成本。

### 备选方案与取舍（Options）
- 方案 A：仅保留通用骨架与替换说明。未选原因：仍需要用户手动替换，易漏改、错改。
- 方案 B（采用）：通用骨架保留不动 + 追加 4 份可直接粘贴的 pinned prompt（需求/设计/代码/测试评审）。

### 最终方案（What）
- 在 `docs/Cursor-多会话协作落地方案.md` 的 `3.8` 小节中，在通用骨架之后新增：
  - `3.8.1` 需求评审专家 pinned prompt（role_id: requirements-reviewer, phase_id: requirements-review）
  - `3.8.2` 设计评审专家 pinned prompt（role_id: design-reviewer, phase_id: design-review）
  - `3.8.3` 代码评审专家 pinned prompt（role_id: code-reviewer, phase_id: code-review）
  - `3.8.4` 测试评审专家 pinned prompt（role_id: test-reviewer, phase_id: test-review）

### 影响范围（Where）
- 变更文件：
 - 修改：`docs/Cursor-多会话协作落地方案.md`

### 一致性检查（Check）
- 全工程搜索关键词：`<角色名称>`、`<role_id>`、`<phase_id>`、`##### 3.8.1`、`requirements-reviewer`、`design-reviewer`、`code-reviewer`、`test-reviewer`
- 已检查的清单/索引/映射：`roles/roles.yaml`、`mapping/phase-role-skill.yaml`、`skills/manifest.yaml`（确认 role_id 存在）
- 已运行的诊断：未运行 lint（以 Markdown 为主），人工检查代码块闭合

### 遗留与后续（Next）
- 如后续增加更多评审角色（如安全评审），建议沿用通用骨架并追加“可直接粘贴”的实例块，保持用户操作一致性。

