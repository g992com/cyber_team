# 软件开发团队活动规范与角色 Skills 建设 — 讨论备忘

本文档记录从「各角色 skill 建设」到「团队活动规范 + Agent 驱动」的讨论重点与思路变化，供后续查阅与延续设计时参考。

**当前规范根约定**：规范库已采用**单仓模式**，规范根为 **`.cyber_team/`**（其下为 process/、roles/、mapping/、skills/、rules/ 等）。路径与链接约定见仓库 README 与 [.cyber_team/CONVENTIONS-paths-and-links.md](../.cyber_team/CONVENTIONS-paths-and-links.md)。人类手册内凡描述「规范库内」路径的，均已统一为 `.cyber_team/` 前缀；多根工作区已废弃，不提供模板。

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
- 新增 `人类手册/Cursor-多会话协作落地方案.md`（原 docs/ 下）：
  - 定义推荐会话与角色映射（项目总控/产品/架构/开发/测试/DevOps 等）；
  - 给出统一 pinned prompt 骨架与项目经理/产品角色示例；
  - 设计统一“任务卡”模板与多会话之间的流转方式；
  - 提供从需求→PRD→评审→阶段推进的端到端协作示例，并说明与业务项目 `project-docs-index.yaml` 的对接方式；
  - 给出如何在团队内启动试运行的步骤建议。
- 新增 `人类手册/多智能体蜂群编排落地方案.md`：
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
  - 新增：`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/多智能体蜂群编排落地方案.md`
  - 修改：`README.md`、`人类手册/role-skills-design-memo.md`
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
  - `人类手册/role-skills-design-memo.md`：确认新增条目与既有结构一致；
  - `docs/` 目录现有文件：`role-skills-design.md`、`role-skill-consistency-check.md` 与新增两篇文档在定位上互补，无重复或冲突。
- 已运行的诊断：
  - 本轮改动仅涉及 Markdown 文档与 README 文本，无代码与配置 schema 更改，暂未运行额外 lint/类型检查；后续如引入执行层代码，再补充对应诊断。

### 遗留与后续（Next）
- 后续可考虑：
  - 在单独 demo 仓库中，基于本方案实现一个最小可行的多 Agent 例子（例如只覆盖 PRD 阶段的 Orchestrator + Product/QA Agents）；
  - 为多 Agent 实现增加更细粒度的 SKILL 设计（例如专门的 orchestrator skill、task-routing skill 等），并在本仓库 `skills/` 中补充对应 SKILL.md；
  - 根据实际使用 Cursor 多会话协作的反馈，迭代 pinned prompt 模板与任务卡模板，将成熟结论同步更新到 `人类手册/Cursor-多会话协作落地方案.md`。

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
- 新目录结构保持不变：`project-docs-index.yaml`、`cursor-rule-project-docs-discovery.md`、`status/project-manager.md`、`status/role-status.md`。
- 全工程内所有 `process/templates` 及 `templates/`（在 process 语境下）的引用改为 `process/project-docs` 或 `project-docs/`。

### 影响范围（Where）
- 变更文件：
  - 新增：`process/project-docs/` 下 4 个文件（从原 templates 迁移）
  - 修改：`README.md`、`人类手册/role-skills-design-memo.md`、`人类手册/多智能体蜂群编排落地方案.md`、`人类手册/Cursor-多会话协作落地方案.md`、`roles/sop/project-manager.md`、`state.yaml`、`process/project-docs/cursor-rule-project-docs-discovery.md`（其内部自引用路径）
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
- 修改：`README.md`、`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/role-skills-design-memo.md`（本备忘）
- 受影响的映射/契约：无 manifest 或 mapping 变更；README 目录结构、应用业务项目步骤、方案文档中规则与模板路径已统一。

### 一致性检查（Check）
- 全工程搜索关键词：`cursor-rule-project-docs-discovery`、`process/project-docs/cursor-rule`、`post-change-project-wide-review`、`rules/project-docs-discovery`、`workspace-template`、`workspace-setup`
- 已检查：README、Cursor-多会话协作落地方案、workspace-setup.md、role-skills-design-memo 历史条目（保留不改，仅追加本条）
- 已运行诊断：未运行 lint（以 Markdown/YAML 为主）

### 遗留与后续（Next）
- 规范仓库内若需 Cursor 自动应用 rules，可将 `rules/` 下文件复制到本仓库 `.cursor/rules/` 或配置 Cursor 读取 rules/；未在本次自动配置。
- 多根工作区模板中第二个 folder 的 path 以“模板放在规范仓库根目录”为默认假设；若用户将 .code-workspace 放在业务项目根，需按 workspace-setup.md 自行改两 path。

**补充（同日）**：`post-change-project-wide-review.mdc` 为本工程（cyber_team）自身的开发规则，不属于团队协作规范，已移回 `.cursor/rules/`。README 与方案文档已更新：`rules/` 仅列供业务项目复制的规则（work-execution-standards、project-docs-discovery）；本工程专用规则在 `.cursor/rules/`，不随规范复制到业务项目。

**路径变更（同日）**：多根工作区配置说明与模板已单独放入目录（现为 `人类手册/workspace/workspace-config/`），内含 `workspace-setup.md` 与 `cursor-multi-root-workspace.code-workspace.template`；README、Cursor-多会话协作落地方案 中相关引用已更新为该目录。

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
- 在 `人类手册/Cursor-多会话协作落地方案.md` 的 `3.8` 小节中，在通用骨架之后新增：
  - `3.8.1` 需求评审专家 pinned prompt（role_id: requirements-reviewer, phase_id: requirements-review）
  - `3.8.2` 设计评审专家 pinned prompt（role_id: design-reviewer, phase_id: design-review）
  - `3.8.3` 代码评审专家 pinned prompt（role_id: code-reviewer, phase_id: code-review）
  - `3.8.4` 测试评审专家 pinned prompt（role_id: test-reviewer, phase_id: test-review）

### 影响范围（Where）
- 变更文件：
 - 修改：`人类手册/Cursor-多会话协作落地方案.md`

### 一致性检查（Check）
- 全工程搜索关键词：`<角色名称>`、`<role_id>`、`<phase_id>`、`##### 3.8.1`、`requirements-reviewer`、`design-reviewer`、`code-reviewer`、`test-reviewer`
- 已检查的清单/索引/映射：`roles/roles.yaml`、`mapping/phase-role-skill.yaml`、`skills/manifest.yaml`（确认 role_id 存在）
- 已运行的诊断：未运行 lint（以 Markdown 为主），人工检查代码块闭合

### 遗留与后续（Next）
- 如后续增加更多评审角色（如安全评审），建议沿用通用骨架并追加“可直接粘贴”的实例块，保持用户操作一致性。

---

## 变更备忘（2026-03-11）：任务卡索引表 + 脚本化更新（降低单点调度与格式漂移）

### 背景/触发（Context）
- 用户在 Cursor 多会话协作中，期望各角色会话能**自助获取任务并更新状态**，避免项目经理/调度者成为索引更新的单点瓶颈。
- 同时希望通过**脚本约束**读写行为，尽量减小模型漂移导致的“任务格式不一致、索引表被写乱、字段漏写”等问题。

### 关键判断（Why）
- **两层结构更稳**：将“完整任务信息”沉到任务卡文件（Markdown），将“可筛选/可路由字段”沉到索引表（JSON），角色会话先查索引再读卡，既易用也便于自动化。
- **用脚本代替自由文本编辑**：对 status、blocked 必填 blocker、原子写入等做最小校验，可显著降低多人会话对同一索引文件的误改风险。
- **模板放规范仓库、运行在业务项目**：规范仓库提供可复制的模板与脚本，业务项目按约定路径落地，便于跨项目复用。

### 备选方案与取舍（Options）
- 方案 A：单文件时间倒序累积任务卡（append-only）。未选原因：角色会话难以按 role/status 快速筛选；文件膨胀后读取成本上升；状态更新不直观。
- 方案 B（采用）：任务卡文件 + 索引表 + 脚本化更新。采用原因：既保留任务卡的完整上下文，又提供稳定的索引与状态机，并可通过脚本减少漂移与并发破坏。

### 最终方案（What）
- 在规范仓库新增“任务板模板”：
  - `process/project-docs/status/task-board/task_board.py`：提供 `init/list/claim/update/add/new-card` 命令
  - `process/project-docs/status/task-board/task-index.json`：索引表空模板
  - `process/project-docs/status/task-board/task-cards/.gitkeep`：任务卡目录占位
- 在 `人类手册/Cursor-多会话协作落地方案.md` 第 4 章新增 `4.3` 小节，说明复制到业务项目的推荐路径与最短命令流。

### 影响范围（Where）
- 变更文件：
 - 新增：`process/project-docs/status/task-board/task_board.py`、`process/project-docs/status/task-board/task-index.json`、`process/project-docs/status/task-board/task-cards/.gitkeep`
 - 修改：`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/role-skills-design-memo.md`
 - 删除/重命名：无
- 受影响的映射/契约/索引（如有）：无（仅新增可选落地机制，不改变现有 phases/roles/mapping/skills 契约）。

### 一致性检查（Check）
- 全工程搜索关键词：`task-index.json`、`task_board.py`、`task-board`
- 已检查的清单/索引/映射：`人类手册/Cursor-多会话协作落地方案.md`（4.3 代码块闭合）、新增模板目录路径
- 已运行的诊断：`python -m py_compile process/project-docs/status/task-board/task_board.py`（通过）

### 遗留与后续（Next）
- 若未来确实出现多人并发频繁冲突，可考虑：
  - 进一步增强锁策略（更强的文件锁或引入轻量数据库/服务端存储）
  - 或改为“每任务独立 JSON + 总索引生成”的写入模型，进一步降低写冲突面

---

## 变更备忘（2026-03-11）：多会话方案补充「会话丢失与恢复」与记忆持久化说明

### 背景/触发（Context）
- 用户询问：在实际业务项目中实施多会话协作方案时，是否存在**记忆方面的问题**；例如会话丢失后重新建立会话、使用 pinned prompt 后是否能继续之前的工作。

### 关键判断（Why）
- 本方案在设计上已将「可恢复的上下文」放在持久化文件中（state.yaml、task-index + 任务卡、project-docs-index + 文档、规范仓库的 process/roles/mapping/skills），而非依赖对话历史；但文档中未显式说明，易引发“会话丢了是否要重来”的疑虑。
- 明确写出「记忆在文件、不在对话」及恢复步骤，可降低落地时的困惑，并促使团队养成「关键决策写进任务卡/文档」的习惯，减少仅存于对话中的隐性约定。

### 备选方案与取舍（Options）
- 方案 A：仅在 FAQ 或实践建议中简单提一句“会话丢失后可重新粘贴 pinned prompt 并读 state/task”。未选原因：未说清哪些记忆可恢复、哪些不能，以及具体恢复步骤。
- 方案 B（采用）：在落地方案中新增独立章节「七、会话丢失与恢复（记忆与持久化）」，用表格列出记忆类型与持久化位置、恢复方式，并给出 pinned prompt 持久化建议与新会话恢复步骤、明确写出无法通过文件恢复的局限。采用原因：一次性说清设计意图、操作步骤与边界，便于实施与后续迭代。

### 最终方案（What）
- 在 `人类手册/Cursor-多会话协作落地方案.md` 中，在「六、与具体业务项目的对接方式」与「实践步骤建议」之间新增 **第七节「会话丢失与恢复（记忆与持久化）」**，包含：
  - 7.1 设计原则：记忆在文件、不在对话（表格：记忆类型 / 持久化位置 / 新会话如何恢复）；
  - 7.2 Pinned prompt 的持久化与恢复（建议将各角色 pinned prompt 存入规范仓库或业务项目文档，便于新会话复制）；
  - 7.3 新会话恢复的推荐步骤（多根工作区、粘贴 pinned prompt、task_board list/claim、项目经理读 state + 任务分布）；
  - 7.4 无法通过文件恢复的部分（仅存于对话的临时约定、多轮细微上下文；建议关键决策写进任务卡/阶段产出物）。
- 原「七、实践步骤建议」顺延为「八」；在步骤 2「为每个会话配置 pinned prompt」中增加：建议将实际使用的 pinned prompt 保存到仓库（见第七节 7.2），便于会话丢失后快速恢复。

### 影响范围（Where）
- 变更文件：
 - 修改：`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/role-skills-design-memo.md`
 - 新增/删除/重命名：无
- 受影响的映射/契约/索引：无。

### 一致性检查（Check）
- 全工程搜索关键词：`会话`、`state.yaml`、`task_board`、`pinned prompt`、`恢复`
- 已检查的清单/索引/映射：文档内章节编号（六→七→八）、交叉引用（7.2、第八节步骤 2）
- 已运行的诊断：Markdown lint（无报错）

### 遗留与后续（Next）
- 若团队采纳「pinned prompt 清单」建议，可在规范仓库中新增 `process/pinned-prompts/` 或 `docs/cursor-prompts.md` 存放各角色最终版 pinned prompt，便于复制与版本管理。

---

## 变更备忘（2026-03-11）：「做过哪些处理」与「最终切片」的记录策略

### 背景/触发（Context）
- 用户询问：做过哪些处理是否需要记录，还是只需要记录最终工作情况的切片信息？

### 关键判断（Why）
- **会话恢复与接续**只依赖“当前在哪、任务状态、产物在哪”，即切片信息；不需要完整处理历史即可让新会话接上工作。
- **处理记录**（谁何时做了哪一步、决策如何形成）对审计、复盘有用，但会增加维护成本和上下文噪声；本方案当前不依赖其实现恢复，故定为可选。

### 备选方案与取舍（Options）
- 方案 A：要求同时维护「处理历史」与「切片」。未选原因：多会话下由各角色会话自发维护历史成本高，且恢复场景不强制需要。
- 方案 B（采用）：明确「切片信息」为必须且已有设计支撑；「做过哪些处理」为可选，按团队审计/复盘需求再引入（轻量做法：关键决策写进任务卡/文档；显式做法：活动日志或状态变更历史）。采用原因：优先保证恢复与接续，再按需扩展追溯。

### 最终方案（What）
- 在 `人类手册/Cursor-多会话协作落地方案.md` 第七节新增 **7.5 是否需要记录「做过哪些处理」与「最终工作情况切片」**：说明只需切片即可恢复；处理记录为可选，并给出轻量/显式两种可选做法及建议（优先切片，按需历史）。

### 影响范围（Where）
- 变更文件：修改 `人类手册/Cursor-多会话协作落地方案.md`、`人类手册/role-skills-design-memo.md`；无新增/删除/重命名。
- 受影响的映射/契约/索引：无。

### 一致性检查（Check）
- 全工程搜索关键词：`做过哪些处理`、`切片`、`处理记录`、`state.yaml`、`task-index`
- 已检查：第七节与 7.1 表格、task_board 当前能力（仅当前状态）表述一致。

### 遗留与后续（Next）
- 若后续团队需要审计轨迹，可再约定 task_index 的 history 字段或独立活动日志的 schema 与存放位置。

---

## 变更备忘（2026-03-12）：project-docs-index.yaml 由谁、依据什么初始化

### 背景/触发（Context）
- 用户询问：`project-docs-index.yaml` 应该由谁、根据什么依据先初始化？落地方案中仅写“从本仓库复制并填写”，未明确责任人与依据。

### 关键判断（Why）
- 项目启动阶段（initiation）由项目总控/项目经理负责，且 `skills/project-initiation` 已约定“若项目使用 project-docs-index.yaml，可在索引中登记上述文档路径”，故 PM 是索引初始化与 initiation 段登记的自然责任人。
- 索引结构必须与 `process/phases.yaml` 的阶段 id 一致，路径以规范仓库模板为默认，再按实际产出填写或调整。

### 备选方案与取舍（Options）
- 方案 A：不写“由谁”，只写“依据模板与 phases 填写”。未选原因：落地时易出现无人负责或重复初始化。
- 方案 B（采用）：在落地方案「六、与具体业务项目的对接方式」中补充：由项目总控/项目经理在接入或 initiation 时初始化；可由接入实施者先复制模板、PM 再登记核对；依据为模板、phases 阶段 id、实际/计划产出路径。采用原因：与 project-initiation 职责一致，且兼容“先复制后填写”的两种分工。

### 最终方案（What）
- 在 `人类手册/Cursor-多会话协作落地方案.md` 第六节「项目文档索引」下增加「project-docs-index.yaml 由谁、依据什么初始化」说明：由谁（PM/接入实施者）、依据（模板、phases 阶段 id、路径填写规则）。

### 影响范围（Where）
- 变更文件：修改 `人类手册/Cursor-多会话协作落地方案.md`、`人类手册/role-skills-design-memo.md`；无新增/删除/重命名。
- 受影响的映射/契约/索引：无（仅文档澄清，与 process/project-docs/project-docs-index.yaml、phases.yaml、project-initiation 现有约定一致）。

### 一致性检查（Check）
- 全工程搜索关键词：`project-docs-index`、`初始化`、`project-initiation`
- 已检查：落地方案第六节与 project-docs-discovery、workspace-setup 中“复制并填写”表述一致，并与之互补（补充责任与依据）。

### 遗留与后续（Next）
- 若团队希望“各角色产出时自行登记索引”，可在后续在 artifact-metadata-convention 或各角色 pinned prompt 中补充“产出新文档后更新 docs/project-docs-index.yaml 对应条目”的约定。

---

## 变更备忘（2026-03-12）：project-docs-index 路径改为 docs/ 与拷贝责任明确为用户

### 背景/触发（Context）
- 用户要求：（1）从规范库拷贝到业务项目可由用户完成；（2）project-docs-index.yaml 在业务库中不放在根目录，改为放在业务库 docs 目录下，使文档更集中。

### 关键判断（Why）
- 索引放 docs/ 与“路径相对于本文件所在目录”一致：模板内路径改为相对 docs/，去掉 `docs/` 前缀。
- 拷贝责任明确为用户，与“接入实施者/PM”脱钩，简化落地说明。

### 最终方案（What）
- **业务项目中索引路径**：由根目录 `project-docs-index.yaml` 改为 **`docs/project-docs-index.yaml`**；所有引用处统一为“docs 目录下的 project-docs-index.yaml”或“docs/project-docs-index.yaml”。
- **模板** [process/project-docs/project-docs-index.yaml]：头部注释改为“复制到业务项目 docs 目录”；所有条目路径去掉 `docs/` 前缀，改为相对 docs/（如 `requirements/prd.md`）。
- **拷贝责任**：落地方案第六节「由谁」改为：从规范库拷贝到业务项目由**用户**完成（复制到业务项目 docs/）；索引内容的填写与登记可由 PM 或用户完成。

### 影响范围（Where）
- 修改：`process/project-docs/project-docs-index.yaml`、`rules/project-docs-discovery.md`、`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/workspace/workspace-config/workspace-setup.md`、`process/artifact-metadata-convention.md`、`README.md`、`人类手册/多智能体蜂群编排落地方案.md`、`skills/project-initiation/SKILL.md`、`人类手册/role-skills-design-memo.md`。
- 多会话方案内各角色 pinned prompt、部署结构、记忆表、切片信息等凡提及索引路径处均已改为 docs 目录。

### 一致性检查（Check）
- 全工程搜索：`project-docs-index`、`根目录.*project-docs`，确认无遗漏“根目录”与旧路径。
- 模板内路径已全部相对 docs/，与“本文件所在目录”约定一致。

### 遗留与后续（Next）
- 无。已按计划完成路径与责任调整。

---

## 变更备忘（2026-03-12）：进展回复字段引用 README 歧义消除

### 背景/触发（Context）
- 《Cursor-多会话协作落地方案》中项目经理 pinned prompt 第 5 条写「请按 README 中建议的字段结构回复」，未指明是哪个仓库的 README，在多根工作区（规范库 + 业务项目）场景下可能被理解为业务项目 README，造成歧义。

### 关键判断（Why）
- 进展回复的字段结构（current_phase、completed_phases、status/summary/blockers/next、project_blockers/project_risks、需决策项）仅在**本规范仓库根目录 README.md** 的「进展回复的输出契约（建议字段）」中定义；业务项目 README 通常不包含该契约。

### 备选方案与取舍（Options）
- 方案 A：保持「README」不指定；未选原因：多根工作区下存在规范库与业务库两个根，易歧义。
- 方案 B（采用）：显式写「本规范仓库根目录 README.md」并带上小节名「进展回复的输出契约（建议字段）」；采用原因：与文档前文「cyber_team 规范仓库」一致，且便于 Agent/人精确定位。

### 最终方案（What）
- 将「请按 README 中建议的字段结构回复」改为「请按**本规范仓库根目录 README.md**中「进展回复的输出契约（建议字段）」回复」。

### 影响范围（Where）
- 变更文件：修改 `人类手册/Cursor-多会话协作落地方案.md`（项目经理 pinned prompt 第 5 条）；追加 `人类手册/role-skills-design-memo.md`。
- 无新增/删除/重命名；无映射/索引变更。

### 一致性检查（Check）
- 全工程搜索关键词：`README`（在落地方案中仅此一处引用进展字段）；已确认 README.md 第 39–45 行为对应契约。

### 遗留与后续（Next）
- 无。若后续在业务项目侧也希望约定进展回复格式，可在业务项目 README 或规则中引用规范库 README 该小节或复制契约说明。

---

## 变更备忘（2026-03-12）：明确 state.yaml 作用域，避免误写规范库

### 背景/触发（Context）
- 规范库是通用规则/流程内核，`state.yaml` 在这里应当只是 schema 示例/模板；但在多根工作区对接业务项目时，出现了智能体把**业务项目进展**误写回规范库根目录 `state.yaml` 的情况。

### 关键判断（Why）
- `state.yaml` 属于**运行态进展快照**（高频更新、项目特有），应以业务项目为“单一事实源”；规范库只提供 schema 与初始化模板，不能承载任何具体业务项目的真实状态。
- 多根工作区下存在同名文件歧义，若文档/规则写成“读取 state.yaml”而不注明“业务项目”，就会诱发误读/误写。

### 备选方案与取舍（Options）
- 方案 A：删除规范库根目录 `state.yaml` 或强制改名为 `state.template.yaml`；未选原因：会破坏既有文档与既有使用习惯，迁移成本高且容易引入更多引用未更新。
- 方案 B（采用）：保留规范库 `state.yaml` 作为示例，但在关键入口（README/规则/多会话说明）明确“业务项目为准”，并提供 `process/state.yaml` 作为初始化来源；采用原因：改动小、兼容强、能显著降低误写概率。

### 最终方案（What）
- 增加业务项目 `state.yaml` 的初始化模板：`process/state.yaml`。
- 文档与规则统一强调：读取/更新的 `state.yaml` 指**业务项目根目录**的文件；规范库根目录的 `state.yaml` 仅作示例/模板，避免写入业务项目真实进展。

### 影响范围（Where）
- 变更文件：
  - 新增：`process/state.yaml`
  - 修改：`README.md`、`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/workspace/workspace-config/workspace-setup.md`、`rules/project-docs-discovery.md`、`process/artifact-metadata-convention.md`、`process/project-docs/status/project-manager.md`、`process/project-docs/status/role-status.md`、`人类手册/多智能体蜂群编排落地方案.md`

### 一致性检查（Check）
- 全工程搜索关键词：`state.yaml`、`读取 state.yaml`、`读写 state.yaml`、`规范仓库或业务项目中的`
- 已检查的清单/索引/映射：`rules/project-docs-discovery.md`、`人类手册/workspace/workspace-config/workspace-setup.md`、`人类手册/Cursor-多会话协作落地方案.md`、`README.md`
- 已运行的诊断：对变更的 Markdown 运行诊断（无 lint 报错）。

### 遗留与后续（Next）
- 仍存在少量文档段落（如 `人类手册/role-skills-design.md`）从“概念”层面描述 `state.yaml` 可能放在规范根目录或 `.agent/`，如需更严格隔离，可后续统一为“业务项目侧 state + 规范库侧模板”单一路径约定。
- 为进一步降低“更新错仓库”的概率，后续可在业务项目侧引入 `update_state.py`（类似 `task_board.py` 的写入护栏），并在任务卡/总控 prompt 中约定“更新 state 必须通过脚本”。

### 补充（Superseded）
- 该备忘中的“方案 B（保留规范库根目录 `state.yaml` 示例）”已被后续调整替代：规范库已删除根目录 `state.yaml`，统一以 `process/state.yaml` 作为初始化模板，进一步降低多根工作区下同名文件歧义与误写概率。

---

## 变更备忘（2026-03-12）：模板去 template 命名 + 独立 update_state.py 脚本

### 背景/触发（Context）
- 用户希望“复制即用”，减少对接业务项目时的认知成本与操作步骤；同时希望将更新业务项目 `state.yaml` 的脚本从 `task-board/` 中分离，避免被误认为任务卡相关工具。

### 关键判断（Why）
- **template 后缀降低可用性**：实际使用时总需要“复制并改名”，增加摩擦且容易漏改引用。
- **脚本需要语义隔离**：`task-board/` 语义聚焦任务卡；状态更新脚本应放在 `status/` 层级并改名为 `update_state.py`，更符合“项目状态工具”的定位。

### 备选方案与取舍（Options）
- 方案 A：保留 `*-template` 命名，要求使用者复制后自行改名；未选原因：重复操作多、容易出错。
- 方案 B（采用）：规范仓库直接提供最终文件名（`process/state.yaml`、`process/project-docs/status/role-status.md`），业务项目只需复制；同时提供 `process/project-docs/status/update_state.py`，从目录结构上避免混淆。

### 最终方案（What）
- 将状态模板文件从 `process/state-template.yaml` 调整为 `process/state.yaml`。
- 将角色状态日志模板从 `process/project-docs/status/role-status-template.md` 调整为 `process/project-docs/status/role-status.md`。
- 将状态更新脚本从 `process/project-docs/status/task-board/state_board.py` 迁移并更名为 `process/project-docs/status/update_state.py`。

### 影响范围（Where）
- 变更文件：
  - 新增：`process/state.yaml`、`process/project-docs/status/update_state.py`
  - 修改：`README.md`、`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/workspace/workspace-config/workspace-setup.md`、`人类手册/role-skills-design.md`、`人类手册/role-skills-design-memo.md`
  - 删除/重命名：`process/project-docs/status/role-status-template.md` → `process/project-docs/status/role-status.md`；删除 `process/state-template.yaml`；删除 `process/project-docs/status/task-board/state_board.py`

### 一致性检查（Check）
- 全工程搜索关键词：`state-template.yaml`、`role-status-template.md`、`state_board.py`、`task-board/state_board.py`、`update_state.py`
- 已检查的清单/索引/映射：`人类手册/workspace/workspace-config/workspace-setup.md`（复制指引路径）、`README.md`（初始化模板路径）
- 已运行的诊断：对 `process/project-docs/status/update_state.py` 与相关 Markdown 文件运行诊断；并运行 `python process/project-docs/status/update_state.py --help` 验证脚本可用。

### 遗留与后续（Next）
- 如需进一步强约束“只准写业务项目 state”，可在业务项目侧约定：更新 state 必须通过 `scripts/update_state.py`（并在任务卡/总控 prompt 中固化）。

---

## 变更备忘（2025-03-12）：规范改进方案精简 + 阶段全集与裁剪 + 待办文档

### 背景/触发（Context）
- 在流程管理理论与 CMMI 改进讨论基础上，用户要求：仅保留智能体协作必要项；有用项放入统一待办文档作为规范工程进展与后续工作记忆；并希望评估「规范库保留阶段全集、由 PM 裁剪形成业务项目 process」的可行性与有效性。

### 关键判断（Why）
- **必要与有用分离**：智能体协作真正依赖的只有「阶段唯一事实来源」「阶段出口条件可机读」「产出物/模板可发现」；其余（裁剪指南、state 语义、度量、改进、RACI 等）对成熟度或体验有帮助但非协作前提，放入待办便于按需实施。
- **单一进展/待办入口**：规范工程需要一处「最新进展 + 待办」的文档，便于后续会话或人工续接时恢复上下文。
- **阶段裁剪 = 子集**：业务项目 process 由规范库阶段全集的子集构成，不引入自定义 phase_id，可继续使用规范库的 mapping/roles，无需重复维护。

### 备选方案与取舍（Options）
- 方案 A：保留全部流程管理 + CMMI 改进项一并实施；未选原因：对智能体协作并非必要，易过度建设。
- 方案 B（采用）：必要三项单独成方案；有用项与后置项迁入 `人类手册/plan/norm-backlog.md`；阶段设计采用「全集 + PM 裁剪 → 业务项目 process」，并做可行性与有效性评估。

### 最终方案（What）
- 新增 `人类手册/plan/norm-improvement-plan.md`：仅含三项必要改进 +「阶段全集 → 裁剪 → 业务项目 process」的可行性与有效性评估；并约定裁剪结果落点可选「业务项目 project-phases.yaml」或「state.tailoring_snapshot + process-tailoring.md」。
- 新增 `人类手册/plan/norm-backlog.md`：规范工程近期进展、待办（有用可简化 / 可后置）、使用说明；作为后续工作记忆支持。
- 在 README 中增加「规范来源与改进」小节，指向上述两文档。

### 影响范围（Where）
- 新增：`人类手册/plan/norm-improvement-plan.md`、`人类手册/plan/norm-backlog.md`
- 修改：`README.md`（规范来源与改进小节）、`人类手册/role-skills-design-memo.md`（本备忘）

### 一致性检查（Check）
- 全工程搜索关键词：`norm-backlog`、`norm-improvement-plan`
- 已检查：README 链接正确；backlog 与 improvement-plan 互相引用一致。

### 遗留与后续（Next）
- 按 improvement-plan 实施三项必要改进（阶段唯一来源、阶段出口条件、模板索引可选）。
- 在 improvement-plan 或 process 中明确选定「裁剪结果落点」的推荐做法（A：project-phases.yaml / B：tailoring_snapshot + process-tailoring.md），并在 project-initiation 产出要求中写明。

---

## 变更备忘（2025-03-12）：文档化阶段裁剪约定（做法 B）

### 背景/触发（Context）
- 按规范改进实施计划步骤 1：在规范库内明确约定裁剪结果落点为做法 B，业务项目不复制阶段定义。

### 关键判断（Why）
- 做法 B（state.tailoring_snapshot + docs/process-tailoring.md）满足「任何内容都不会出现多个拷贝」原则；process.md 为流程说明的合适落点，README 仅补充 state 字段引用。

### 备选方案与取舍（Options）
- 在 README 中重复大段阶段与裁剪说明；未选原因：违反无多拷贝原则，与规则一致改为引用。
- 采用：在 process/process.md 中新增「阶段与裁剪」小节并引用 norm-improvement-plan；README 在与 Agent 接口中补充 tailoring_snapshot 字段及见 process 阶段与裁剪的引用。

### 最终方案（What）
- process/process.md 新增「阶段与裁剪」：规范库维护阶段全集，业务项目通过 state.tailoring_snapshot 与 docs/process-tailoring.md 表达该业务项目的流程，不复制 phases；详见 人类手册/plan/norm-improvement-plan.md 第二节（做法 B）。
- README 在与 Agent 的接口第 5 条中增加 tailoring_snapshot 字段说明及「见 process/process.md 阶段与裁剪」引用。

### 影响范围（Where）
- 修改：`process/process.md`、`README.md`

### 一致性检查（Check）
- 全工程搜索关键词：`tailoring_snapshot`、`process-tailoring`、`做法 B`、`阶段全集`、`裁剪`
- 已检查：README、process.md、norm-improvement-plan 对裁剪结果落点表述一致，无冲突。

### 遗留与后续（Next）
- 步骤 2：落实阶段定义唯一事实来源（role-skills-design 等改为引用 phases.yaml）。

---

## 变更备忘（2025-03-12）：阶段定义唯一事实来源（phases.yaml）

### 背景/触发（Context）
- 按规范改进实施计划步骤 2：规范库内阶段定义的唯一来源定为 process/phases.yaml，其他文档仅引用不重复列举。

### 关键判断（Why）
- 避免多源不一致与后续 phases 变更时的漏改；role-skills-design 第 3 节原为完整阶段表，与 phases.yaml 重复，故改为引用 + 概要说明。

### 备选方案与取舍（Options）
- 保留 role-skills-design 中的完整阶段表并加注「与 phases.yaml 一致」；未选原因：仍为重复维护，易漂移。
- 采用：删除该表，改为「阶段定义见 process/phases.yaml，本节仅概要说明」，满足无多拷贝原则。

### 最终方案（What）
- 人类手册/role-skills-design.md 第 3 节：删除与 phases.yaml 完全一致的阶段表格，改为「阶段定义（id、name、order、outputs）的唯一定义见 process/phases.yaml；本节不重复列举」+ 对人读的概要说明。第 4、5 节仍使用阶段名称/id，与 phases.yaml 的 id 一致，无需改。
- 其他文档（Cursor-多会话、多智能体蜂群、project-initiation SKILL）已为引用 phases.yaml，未发现重复阶段表，未修改。

### 影响范围（Where）
- 修改：`人类手册/role-skills-design.md`（第 3 节）

### 一致性检查（Check）
- 全工程搜索关键词：`phases`、`phase_id`、`initiation`、`requirements`、阶段表、阶段定义
- 已检查：mapping、state 模板、project-docs-index 使用的 phase id 与 phases.yaml 一致；无遗漏。

### 遗留与后续（Next）
- 步骤 3：state 增加 tailoring_snapshot，project-initiation 产出要求更新。

---

## 变更备忘（2025-03-12）：state 增加 tailoring_snapshot 与 project-initiation 产出约定

### 背景/触发（Context）
- 按规范改进实施计划步骤 3：业务项目 state 支持「本项目阶段集合」存储；project-initiation 明确须产出 tailoring_snapshot 与 process-tailoring.md。

### 关键判断（Why）
- 做法 B 要求裁剪结果落点在 state.tailoring_snapshot + docs/process-tailoring.md；state 模板与 project-initiation 产出须与 norm-improvement-plan 一致。update_state.py 若只序列化固定 key 会丢失新字段，故将 tailoring_snapshot 加入脚本的 keys 与 init 默认值。

### 备选方案与取舍（Options）
- 不在脚本中支持 tailoring_snapshot，由人工或他处维护；未选原因：脚本 init/show 会覆盖或未输出该字段，易丢失。
- 采用：process/state.yaml 与 update_state.py 均增加 tailoring_snapshot；project-initiation SKILL 明确必须产出该字段与 process-tailoring.md。

### 最终方案（What）
- process/state.yaml：Schema 注释增加 tailoring_snapshot 说明；新增字段 tailoring_snapshot: []。
- skills/project-initiation/SKILL.md：产出物约定表与「与 state 的衔接」中明确须输出 state.tailoring_snapshot 与 docs/process-tailoring.md；不复制 phases 到业务项目（做法 B）。
- process/project-docs/status/update_state.py：_dump_state_canonical 的 keys 与 cmd_init 默认 data 中增加 tailoring_snapshot。

### 影响范围（Where）
- 修改：`process/state.yaml`、`skills/project-initiation/SKILL.md`、`process/project-docs/status/update_state.py`

### 一致性检查（Check）
- 全工程搜索关键词：`tailoring_snapshot`、`state.yaml`、`current_phase`、`completed_phases`、project-initiation、流程裁剪
- 已检查：state schema、project-initiation 产出、norm-improvement-plan 做法 B 描述一致；update_state.py 已兼容新字段。

### 遗留与后续（Next）
- 步骤 4：新增阶段出口条件（exit-criteria.yaml）与阶段转换规则说明。

---

## 变更备忘（2025-03-12）：阶段出口条件（可机读）与阶段转换规则

### 背景/触发（Context）
- 按规范改进实施计划步骤 4：Agent/Orchestrator 需可判断当前阶段是否可推进；出口条件与 project-docs-index、产出物 status 对齐。

### 关键判断（Why）
- 出口条件单独 YAML 便于解析；phase_id 与 phases.yaml、project-docs-index 一致；required_artifacts 与 index 的 key 对应，key_status 与 artifact-metadata-convention 的 status 对应。

### 备选方案与取舍（Options）
- 将出口条件写在 process.md 自然语言中；未选原因：不便于 Agent 解析。
- 采用：独立 process/exit-criteria.yaml，process.md 与 README 引用并简述转换规则；artifact-metadata-convention 增加一句「阶段是否可推进见 exit-criteria.yaml」。

### 最终方案（What）
- 新增 process/exit-criteria.yaml：按 phase_id 列出 description、required_artifacts、key_status（与 project-docs-index、artifact 约定对齐）。
- process/process.md「阶段转换规则」：说明出口条件满足或用户确认后可推进，引用 exit-criteria.yaml。
- process/artifact-metadata-convention.md：Agent 使用方式中增加「阶段是否可推进见 process/exit-criteria.yaml」。
- README：阶段转换规则改为引用 process.md 与 exit-criteria.yaml。

### 影响范围（Where）
- 新增：`process/exit-criteria.yaml`
- 修改：`process/process.md`、`process/artifact-metadata-convention.md`、`README.md`

### 一致性检查（Check）
- 全工程搜索关键词：`exit_criteria`、`exit-criteria`、阶段转换、出口条件、approved
- 已检查：exit-criteria 的 phase_id 与 phases.yaml 一致；required_artifacts 与 project-docs-index 的 key 对应。

### 遗留与后续（Next）
- 步骤 5（可选）：process 下增加模板与清单索引。

---

## 变更备忘（2025-03-12）：process 模板与清单索引

### 背景/触发（Context）
- 按规范改进实施计划步骤 5（可选）：便于业务项目初始化时发现需引用的模板及复制目标路径。

### 关键判断（Why）
- 索引仅列「规范库路径 → 业务项目落点」，不复制规范定义全文，符合无多拷贝原则；独立 templates-index.md 便于单独维护与发现。

### 最终方案（What）
- 新增 process/templates-index.md：表格式列出 state.yaml、project-docs-index.yaml、status 模板、process-tailoring、rules 等规范库路径及在业务项目中的落点；并注明阶段/角色/映射不复制、通过引用规范库使用。
- README「应用到业务项目」小节增加一句：业务项目初始化时可参考 process/templates-index.md。

### 影响范围（Where）
- 新增：`process/templates-index.md`
- 修改：`README.md`

### 一致性检查（Check）
- 关键词：templates-index、模板索引、project-docs-index、state.yaml
- 已检查：索引中的规范库路径与现有 process 下文件一致，无死链接。

### 遗留与后续（Next）
- 无。规范改进实施计划步骤 1–5 已完成。

---

## 变更备忘（2026-03-13）：人类手册目录重构与文档迁移

### 背景/触发（Context）
- 将规范库中「仅供人类阅读、智能体不需要直接消费」的文档与机器可读规范分离，集中收纳到统一目录，并通过目录名表达人类导向；目录名采用「人类手册」。
- 业务项目仍沿用 `docs/` 作为项目文档根（如 `docs/project-docs-index.yaml`、`docs/process-tailoring.md`），不随规范库改名。

### 关键判断（Why）
- 仅迁移无机器强依赖的文档，保持 process/phases.yaml、roles、mapping、rules、skills 等 Agent 接口路径稳定。
- 单一事实来源：不复制内容，仅移动 + 全工程更新引用；`.cursor/rules/post-change-project-wide-review.mdc` 中备忘路径同步改为 `人类手册/role-skills-design-memo.md`。
- project-initiation 等 skill 执行仅依赖 YAML 与 manifest，不依赖 `process/process.md`、`stages/*.md`，故可将二者归入人类手册。

### 备选方案与取舍（Options）
- 方案 A：保留 `docs/` 名，仅在其下建 `human/` 子目录。未选原因：用户要求将 docs 改为「人类手册」目录名。
- 方案 B（采用）：规范库根目录下将 `docs/` 物理重命名为 `人类手册/`，并在其下按主题分子目录（stages、roles/sop、process、norm、workspace），全工程更新规范库内部引用。

### 最终方案（What）
- 规范库：`docs/` 重命名为 `人类手册/`；原 `stages/`、`roles/sop/`、`process/process.md`、原 `docs/workspace-config/*` 及原 `docs/` 下规范工程文档迁入 `人类手册/` 对应子目录。
- 全工程引用：凡指向规范库自身人类文档的路径由 `docs/...` 改为 `人类手册/...`；业务项目侧「docs 目录」约定不变。
- 规则：`.cursor/rules/post-change-project-wide-review.mdc` 中备忘写入路径更新为 `人类手册/role-skills-design-memo.md`。

### 影响范围（Where）
- 变更文件：
  - 重命名/移动：`docs/` → `人类手册/`；`stages/` → `人类手册/stages/`；`roles/sop/` → `人类手册/roles/`；`process/process.md` → `人类手册/process/process.md`；原 `docs/workspace-config` → `人类手册/workspace/workspace-config`。
  - 修改：`README.md`、`.cursor/rules/post-change-project-wide-review.mdc`、`人类手册/role-skills-design-memo.md`、`人类手册/plan/norm-improvement-execution-plan.md`、`人类手册/plan/norm-backlog.md`、`人类手册/plan/norm-improvement-plan.md`、`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/process/process.md`、`process/state.yaml`、`skills/project-initiation/SKILL.md`。
- 受影响的映射/契约/索引：无 manifest 或 phase-role-skill 变更；README 目录结构、规则中的备忘路径、各人类手册内交叉引用已统一。

### 一致性检查（Check）
- 全工程搜索关键词：`docs/role-skills-design-memo`、`docs/norm-improvement-plan`、`docs/Cursor-多会话`、`docs/多智能体`、`docs/role-skills-design`、`docs/workspace-config`（规范库语境）；业务项目 `docs/` 路径保留。
- 已检查的清单/索引/映射：README、process/templates-index.md、.cursor/rules、人类手册内互引。
- 已运行的诊断：`update_state.py --help` 通过；未改动脚本逻辑。

### 遗留与后续（Next）
- 若后续需在「向人类解释」时引用人类手册中的阶段/流程说明，可在对应 skill 或规则中按需增加「可选阅读」说明并指向 `人类手册/` 路径。
- 计划文件（如 .cursor/plans 下）中若仍含 `docs/human/` 等旧表述，可在一轮文档整理时统一改为 `人类手册/`。

---

## 变更备忘（2026-03-13）：全工程回顾路径与引用修正

### 背景/触发（Context）
- 按 `.cursor/rules/post-change-project-wide-review.mdc` 对工程做只读检查，发现人类手册重构后仍有若干路径错误或未统一，需修正以避免引用悬空与执行歧义。

### 关键判断（Why）
- 备忘中 `人类手册/workspace/workspace-setup.md` 与真实路径 `人类手册/workspace/workspace-config/workspace-setup.md` 不一致，属引用悬空，必须改。
- 人类手册内文档引用规范库 SOP、流程说明时，应统一使用 `人类手册/roles/`、`人类手册/process/process.md`，与当前目录结构一致；执行计划类文档中「涉及文件」应指向实际位置，便于执行时定位。

### 最终方案（What）
- 将 `人类手册/role-skills-design-memo.md` 中全部 `人类手册/workspace/workspace-setup.md` 改为 `人类手册/workspace/workspace-config/workspace-setup.md`。
- `人类手册/Cursor-多会话协作落地方案.md`：各角色参考文档由 `roles/sop/xxx.md` 改为 `人类手册/roles/` 并注明可待补充，避免指向不存在的文件名。
- `人类手册/多智能体蜂群编排落地方案.md`：`roles/sop/*.md` 改为 `人类手册/roles/*.sop.md`。
- `人类手册/plan/norm-improvement-execution-plan.md`：步骤 1、4 中「涉及文件」及动作中的 `process/process.md` 改为 `人类手册/process/process.md`。

### 影响范围（Where）
- 修改：`人类手册/role-skills-design-memo.md`、`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/多智能体蜂群编排落地方案.md`、`人类手册/plan/norm-improvement-execution-plan.md`；无新增/删除/重命名。

### 一致性检查（Check）
- 全工程搜索：`人类手册/workspace/workspace-setup`、`roles/sop/`（人类手册内）、`process/process.md`（执行计划内）；已确认修正后无悬空路径。
- 已检查：README、templates-index、规则文件未因本轮修改受影响。

### 遗留与后续（Next）
- 无。路径与引用已与当前人类手册结构一致。

---

## 变更备忘（2025-03-14）：阶段转换严格按裁剪顺序自动推进

### 背景/触发（Context）
- 项目实践中项目经理在需求阶段完成后向用户呈现“先需求评审还是直接进设计”两种选项由用户选择，与“严格按裁剪后流程执行”的预期不符。
- 约束：仅修改规范库（cyber_team），不修改业务项目（my_portal）；通过规范统一行为，使下一阶段由 tailoring_snapshot 顺序唯一确定、出口条件满足后直接推进，不提供路径选择。

### 关键判断（Why）
- 下一阶段应由业务项目 state.tailoring_snapshot 顺序唯一确定，避免任务卡或局部表述带来“多路径可选”的歧义；process.md 作为阶段转换规则的唯一定义处，其余文件引用或简短提醒，符合“任何内容只在一处维护”原则。
- “用户确认”保留为出口条件未满足时的例外放行手段，不解释为“每阶段边界让用户在多条路径中择一”。

### 备选方案与取舍（Options）
- 方案 A：在业务库修改任务卡（req-001、req-002）的后续流转建议为唯一下一步，并在业务库 process-tailoring 中写阶段推进策略。未选原因：用户明确要求不修改业务库。
- 方案 B（采用）：仅在规范库中统一阶段转换规则与项目经理约定，使 process.md 为唯一定义、exit-criteria/artifact-metadata-convention/Cursor 落地方案/SOP 引用或补充执行约定；所有采用该规范的项目（含 my_portal）默认严格按裁剪顺序推进。采用原因：满足“只改规范库”约束，且行为由规范唯一决定。

### 最终方案（What）
- **人类手册/process/process.md**：重写「阶段转换规则」— 下一阶段由 tailoring_snapshot 顺序唯一确定；出口条件满足后直接推进并派发任务，不向用户提供路径选择；用户确认仅用于例外推进。
- **process/exit-criteria.yaml**：顶部注释补充“下一阶段由 tailoring_snapshot 顺序唯一确定、条件满足后直接推进”，并引用 process.md。
- **process/artifact-metadata-convention.md**：「阶段是否可推进」改为引用 process.md 阶段转换规则，并保留简短提醒（唯一下一阶段、不提供路径选择、用户确认仅例外）。
- **人类手册/Cursor-多会话协作落地方案.md**：项目经理 pinned prompt 新增第 6 条（确定下一阶段以 tailoring_snapshot 为准、直接推进、不提供路径选择），原 6、7 条顺延为 7、8，并注明与 process.md 一致。
- **人类手册/roles/project-manager.sop.md**：新增「阶段推进」小节，写明下一阶段由 tailoring_snapshot 唯一确定、直接推进、不提供路径选择，并引用 process.md。

### 影响范围（Where）
- 修改：`人类手册/process/process.md`、`process/exit-criteria.yaml`、`process/artifact-metadata-convention.md`、`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/roles/project-manager.sop.md`；无新增/删除/重命名。
- 受影响的引用：README 已引用 process.md 阶段转换规则，无需改；project-initiation SKILL 中“用户确认后”针对 initiation 出口条件，与本次规则不冲突。

### 一致性检查（Check）
- 全工程搜索关键词：`用户确认`、`下一阶段`、`tailoring_snapshot`、`阶段转换`、`路径选择`、`先需求评审还是直接进设计`；确认无遗留“由用户选择先评审还是直接进设计”等旧表述；README、skills/project-initiation/SKILL.md、norm-improvement-execution-plan.md 等引用 process.md 处无需反向修改。
- 已检查：process.md 为阶段转换规则唯一定义处，exit-criteria、artifact-metadata-convention、Cursor 落地方案、project-manager SOP 均为引用或简短提醒，无重复定义冲突。

### 遗留与后续（Next）
- 无。采用本规范的项目在需求阶段完成后将自动进入 requirements-review 并派发评审任务，不再出现路径选择交互。

---

## 变更备忘（2025-03-14）：阶段推进取消“用户确认例外”、未满足时迭代或中止

### 背景/触发（Context）
- 阶段出口条件未满足时，不应存在“经用户确认可例外推进”；应改为：要么持续尝试修改/补齐产出直至满足出口条件，要么在判断无法达成时中止工作并向用户通报；通报时给出推荐方案供用户选择；推荐方案由被阻塞阶段活动的负责人提出，经项目经理再通报用户。

### 关键判断（Why）
- 不设“用户确认放行”的核心理由：阶段门禁若可被用户一句话绕过，则出口条件失去约束力，可追溯性与流程一致性难以保证。
- 推荐方案由阶段负责人提出再经 PM 通报用户：负责人最了解当前阶段阻塞原因与可行选项，由 PM 汇总后通报用户可避免信息失真并保持单一对接入口。

### 备选方案与取舍（Options）
- 方案 A：保留“用户确认可例外推进”，仅明确“不用于路径选择”。未选原因：用户明确要求不存在需用户确认的例外情况。
- 方案 B（采用）：取消例外推进；未满足时仅能迭代满足条件或中止并通报；通报时由阶段负责人提供推荐方案，PM 通报用户供选择。采用原因：满足“无用户确认例外”且保留用户决策点（在推荐方案中选择）。

### 最终方案（What）
- **人类手册/process/process.md**：删除“用户确认仅用于……例外推进”整句；补充“当出口条件未满足时，不得推进”；未满足时应继续尝试满足条件或判断无法达成时中止并通报；推荐方案由被阻塞阶段活动负责人提出并通报 PM，PM 再向用户通报及推荐方案供选择。
- **process/exit-criteria.yaml**：顶部注释改为“未满足时不得推进；应继续满足条件，或判断无法达成时由阶段活动负责人向项目经理通报（含推荐方案），项目经理再通报用户”，并引用 process.md。
- **process/artifact-metadata-convention.md**：「阶段是否可推进」删除“（或用户确认）仅用于例外放行”，改为未满足时不得推进及负责人→PM→用户通报链路。
- **人类手册/Cursor-多会话协作落地方案.md**：项目经理 pinned prompt 第 6 条补充“出口条件未满足时不得推进”及由被阻塞阶段活动负责人向 PM 通报、PM 再向用户通报供选择。
- **人类手册/roles/project-manager.sop.md**：「阶段推进」小节补充出口条件未满足时不得推进、推荐方案由阶段负责人提出经 PM 通报用户。

### 影响范围（Where）
- 变更文件：`人类手册/process/process.md`、`process/exit-criteria.yaml`、`process/artifact-metadata-convention.md`、`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/roles/project-manager.sop.md`；无新增/删除/重命名。
- 受影响的引用：README 仍引用 process.md 阶段转换规则，无需改；initiation 阶段“以用户确认为准”为该阶段出口条件定义，非“例外放行”，未改。

### 一致性检查（Check）
- 全工程搜索关键词：`例外推进`、`例外放行`、`经用户确认可例外`；确认 process.md、exit-criteria、artifact-metadata-convention 中已无上述废弃表述；role-skills-design-memo 中既往备忘为历史记录保留。
- 已检查：process.md 为阶段转换规则唯一定义处，其余文件为引用或简短提醒。

### 遗留与后续（Next）
- 无。出口条件未满足时仅能迭代或中止并通报，推荐方案由阶段负责人→PM→用户链路传递供选择。

---

## 变更备忘（2025-03-14）：规范 plan 文件移动与引用同步、智能体文档解耦及规则沉淀

### 背景/触发（Context）
- 已将 5 个文件（阶段推进无例外规则-已实施.md、norm-backlog.md、norm-improvement-execution-plan-已完成.md、norm-improvement-execution-plan.md、norm-improvement-plan.md）从 `人类手册/` 移动到 `人类手册/plan/`，需同步全工程引用并满足 post-change 全工程回顾规则。
- 要求：智能体依赖的文档（SKILL、state 模板）与人类手册解耦，不引用人类手册路径；文档中不使用「本项目」等模糊指代；将「智能体文档不引用人类手册」「写作约定不用本项目」两条要求沉淀到 post-change-project-wide-review.mdc。

### 关键判断（Why）
- 智能体文档解耦：Agent/Skill 仅能稳定读取规范库中 skills、process 等路径，引用人类手册会导致死链或上下文错位；必要信息应内联或总结在各自文档内。
- 明确指代：「本项目」在规范库与业务项目双语境下易歧义；统一改为「业务项目」「该业务项目」或「规范库」便于执行与追溯。

### 备选方案与取舍（Options）
- 方案 A：仅更新路径，SKILL/state 仍引用人类手册。未选原因：与「智能体文档与人类手册解耦」目标不符。
- 方案 B（采用）：路径更新 + SKILL/state 去掉人类手册引用并自包含说明 + 规则文件新增两条原则 + 备忘按模板完整填写。采用原因：满足解耦、明确指代与规则可延续。

### 最终方案（What）
- **路径更新**：README、人类手册/process/process.md、人类手册/plan/*.md、role-skills-design-memo 中 `人类手册/norm-improvement-plan.md`、`人类手册/norm-improvement-execution-plan.md`、`人类手册/norm-backlog.md` 改为 `人类手册/plan/...`。
- **解耦**：skills/project-initiation/SKILL.md 删除对 `人类手册/norm-improvement-plan.md` 的引用，改为自包含「业务项目不复制规范库 process/phases.yaml，以 state.tailoring_snapshot 与 docs/process-tailoring.md 表达该业务项目的流程」；全文「本项目」改为「业务项目」或「该业务项目」。process/state.yaml 注释删除人类手册引用，「本项目」改为「业务项目」。
- **人类手册/process/process.md**：路径改为 `人类手册/plan/norm-improvement-plan.md`；「本项目」改为「业务项目」「该业务项目」。
- **规则沉淀**：.cursor/rules/post-change-project-wide-review.mdc 的「原则」中新增两条：智能体依赖的文档不得引用人类手册路径；写作约定不使用「本项目」等模糊指代。
- **执行计划已完成文档**：norm-improvement-plan-已完成.md 不存在，引用改为 norm-improvement-plan.md。

### 影响范围（Where）
- 修改：`README.md`、`人类手册/process/process.md`、`人类手册/plan/norm-improvement-execution-plan.md`、`人类手册/plan/norm-improvement-execution-plan-已完成.md`、`人类手册/role-skills-design-memo.md`、`skills/project-initiation/SKILL.md`、`process/state.yaml`、`.cursor/rules/post-change-project-wide-review.mdc`。
- 无新增/删除/重命名文件（移动已在先前完成）。

### 一致性检查（Check）
- 全工程搜索关键词：`人类手册/norm-improvement-plan`、`人类手册/norm-improvement-execution-plan`、`人类手册/norm-backlog`、`人类手册/阶段`、`norm-improvement-plan.md`、`norm-backlog.md`、`本项目`（智能体文档中已消除）。
- 已检查的清单/索引/映射：cyber_team 内无 manifest、mapping、索引引用上述旧路径。
- 已运行的诊断：对修改过的 .md/.yaml/.mdc 做人工检查（链接与表述），无自动化 lint 运行。

### 遗留与后续（Next）
- 无。后续若新增智能体可见文档，须遵守「不引用人类手册」「不用本项目指代」两条原则。

---

## 变更备忘（2025-03-14）：规范库角色边界 — PM 不代做评审与防越界机制

### 背景/触发（Context）
- 项目经理会话在无单独「需求评审专家」会话时代写了 `docs/review/requirements-review.md` 及评审结论，并推进到 design，与「评审结论由评审角色产出」的预期不符。
- 规范库未在 PM 职责与约定中明确「不得亲自撰写评审结论/评审记录」，且「组织评审」表述含糊，易被理解为可代做。需明确角色边界并在各角色 pinned prompt、README、artifact-metadata 等处一致体现，并建立防「角色擅自替代其他角色完成任务」的通用机制。

### 关键判断（Why）
- 单一事实来源：角色边界完整表述在一处（README 或落地方案 §3.1），其余引用或简短复述；供 Agent 使用的文档（README、process/artifact-metadata-convention.md）不得引用 `人类手册/` 路径。
- 各角色 pinned prompt 中显式加入「角色边界」一条，因会话启动时可见性高，能第一时间约束行为。

### 备选方案与取舍（Options）
- 方案 A：仅在 project-manager.md 与 PM pinned prompt 中禁止 PM 代写评审。未选原因：其他角色也可能越界代做，需通用原则。
- 方案 B（采用）：在 README、artifact-metadata、落地方案 §3.1 与各角色 pinned prompt 中统一加入角色边界/不得代做；PM 处额外明确「组织评审」含义及无评审会话时的处理。采用原因：兼顾 PM 与评审边界与全局防越界，且符合 post-change 原则。

### 最终方案（What）
- 人类手册/roles/project-manager.sop.md：新增「角色边界」小节，明确项目经理不负责撰写评审结论/记录，由对应评审角色完成；多会话/单会话时的处理方式。
- 人类手册/Cursor-多会话协作落地方案.md：PM pinned prompt 中将「组织评审」定义为派发评审任务、回收评审产出、不得亲自撰写；增加「角色边界」一条；§4.2 任务流转建议中明确评审结论与文档由评审角色产出、PM 不代写；§3.1 通用约定增加角色边界第 6 条；§3.2–§3.8 各角色 pinned prompt 均增加「不得代其他角色完成其职责内产出；若属其他角色，应交由该角色会话或项目经理派发」。
- README「与 Agent 的接口」：增加第 7 条「角色边界」，引用 mapping/phase-role-skill.yaml、roles/roles.yaml（不引用人类手册路径）。
- process/artifact-metadata-convention.md：责任角色处明确 owner_role 表示负责撰写/维护该文档的角色，其他角色不得代写，应通过派发任务由该角色产出。
- 人类手册/process/process.md：阶段转换规则后增加一句，评审阶段评审结论与评审记录由该阶段对应评审角色产出，项目经理不代写。

### 影响范围（Where）
- 变更文件：
  - 修改：`人类手册/roles/sop/project-manager.sop.md`、`人类手册/Cursor-多会话协作落地方案.md`、`README.md`、`process/artifact-metadata-convention.md`、`人类手册/process/process.md`、`人类手册/role-skills-design-memo.md`。
- 无新增/删除/重命名文件。

### 一致性检查（Check）
- 全工程搜索关键词：`组织评审`、`角色边界`、`不得代写`、`owner_role`；确认「组织评审」仅在落地方案中已定义处出现；README、artifact-metadata 未引用人类手册路径。
- 已检查：README、mapping、落地方案 §3.1–§3.8 与 §4.2、artifact-metadata-convention、project-manager SOP、process.md 表述一致。

### 遗留与后续（Next）
- 可选：新增 `rules/role-boundary.md` 供业务项目复制至 .cursor/rules/，并在 README/模板索引中说明。本次未实施，可按需后续补充。

---

## 变更备忘（2025-03-14）：PM 代做测试用例根因与规范库优化实施

### 背景/触发（Context）
- 项目经理会话在同一会话内直接编写功能测试用例并交付用户，未派发任务给测试工程师（qa）或提示用户创建 qa 会话，构成 PM 越界代做 qa 交付物。用户追问依据何种规则可代做，暴露规范中角色边界与代做条款不完整、智能体实际依赖的规则（project-initiation SKILL）无角色边界表述、且存在「用户可指定是否代做」与「未确认的意图猜测」等漏洞。
- 目标：在规范库中优先修改智能体所依赖的规则（skills、.cursor/rules、YAML），人类手册与改进方向统一；采用单一事实源 + 引用方式（skills/_common/）避免重复维护；实施后按 post-change-project-wide-review 必做清单与沉淀备忘。

### 关键判断（Why）
- 人类手册仅供人读、不驱动智能体，故约束须写入 skills/project-initiation/SKILL.md、skills/_common/*.md、.cursor/rules；人类手册仅作人读一致。
- 通用约定（角色边界 + 意图/需求确认）集中放在 skills/_common/role-boundary-and-intent-confirmation.md，规则与各 SKILL 仅引用该文档，符合「单一定义 + 引用」。
- 用户不指定流程执行方式；禁止未与用户确认即根据对用户意图的猜测做流程或角色决策；PM 不得代做任何其他角色产出，无对应角色会话时仅可派发并提示创建该角色会话。

### 备选方案与取舍（Options）
- 方案 A：仅在人类手册中扩展 PM 不负责清单。未选原因：人类手册不驱动智能体，实际约束缺失。
- 方案 B（采用）：优先改 project-initiation SKILL、新增 skills/_common 通用约定文档、新增 .cursor 规则引用该文档、YAML 注释强化产出归属、人类手册与 process 同步统一；各自建 SKILL 内仅引用 _common + 本角色一句提醒。采用原因：智能体依赖的规则全覆盖，单一定义 + 引用减少重复维护。

### 最终方案（What）
- **A1+A2**：skills/project-initiation/SKILL.md 新增「角色边界」与「禁止未确认的意图猜测」；规范来源改为引用 skills/_common/role-boundary-and-intent-confirmation.md，移除对人类手册路径的引用。
- **A4**：新增 skills/_common/role-boundary-and-intent-confirmation.md（角色边界 + 意图/需求确认，适用所有角色）；新增 rules/role-boundary-and-intent-confirmation.md（引用该文档 + 摘要）；prd-requirements、architecture-design、requirements-review、prd-review、architecture-review、test-plan-review、devops-cicd、sre-reliability 各自建 SKILL 内增加对 _common 文档的引用与本角色一句提醒。
- **A3**：process/phases.yaml、mapping/phase-role-skill.yaml、roles/roles.yaml 顶部注释增加阶段产出与负责角色唯一对应、其他角色不得代做的说明及 _common 文档路径。
- **B1–B3**：人类手册/roles/sop/project-manager.sop.md 扩展「不负责」为评审类+非评审类、删除「用户可指定代做」、明确无对应角色会话时仅派发与提示、流程由 PM 按规范决定用户不指定、增加禁止未确认的意图猜测；人类手册/process/process.md 补充各阶段正式产出由 mapping 规定角色负责、项目经理不代写；人类手册/process/process.md 新增「意图/需求确认（通用约定，人类侧检查清单）」。
- **B4**：意图/需求确认通用约定与各阶段排查要点已写入 process.md 上节。

### 影响范围（Where）
- 新增：`skills/_common/role-boundary-and-intent-confirmation.md`、`rules/role-boundary-and-intent-confirmation.md`
- 修改：`skills/project-initiation/SKILL.md`、`skills/prd-requirements/SKILL.md`、`skills/architecture-design/SKILL.md`、`skills/requirements-review/SKILL.md`、`skills/prd-review/SKILL.md`、`skills/architecture-review/SKILL.md`、`skills/test-plan-review/SKILL.md`、`skills/devops-cicd/SKILL.md`、`skills/sre-reliability/SKILL.md`、`process/phases.yaml`、`mapping/phase-role-skill.yaml`、`roles/roles.yaml`、`人类手册/roles/project-manager.sop.md`、`人类手册/process/process.md`
- 受影响的映射/契约：无；mapping、manifest 未改结构，仅 YAML 注释与 SKILL 引用补充。

### 一致性检查（Check）
- 全工程搜索关键词：`role-boundary`、`意图确认`、`_common`、`phase-role-skill`、`人类手册`（确认智能体依赖文档中已无引用人类手册路径）
- 已检查的清单/索引/映射：mapping、phases、roles 注释与 _common 文档路径一致；各自建 SKILL 引用路径为 skills/_common/role-boundary-and-intent-confirmation.md
- 已运行的诊断：未运行自动化 lint；建议后续执行 post-change 必做清单全项

### 遗留与后续（Next）
- 建议执行一次全工程搜索与 README/索引检查，确认无遗漏引用或断链。若业务项目采用本规范，可复制 rules/role-boundary-and-intent-confirmation.md 或依赖规范库规则在 multi-root 下生效。

---

## 变更备忘（2026-03-14）：角色边界规则从 .cursor/rules 迁至 rules/

### 背景/触发（Context）
- 角色边界与意图/需求确认规则原放在规范库专用目录 `.cursor/rules/`（仅用于本工程开发），但该规则约束的是在业务项目中执行各角色时的行为，属于团队协作规范，应在业务项目中生效。
- 目标：将该规则迁至 `rules/`，与 `project-docs-discovery.md`、`work-execution-standards.md` 一致，作为供业务项目复制到其 `.cursor/rules/` 的规则。

### 关键判断（Why）
- `rules/` 为团队协作规范用规则存放处，供业务项目复制到 `.cursor/rules/`；`.cursor/rules/` 仅用于规范库自身开发的 Cursor 规则，不随规范复制到业务项目（见 README 与 Cursor-多会话协作落地方案）。
- 规则内容与引用（skills/_common/role-boundary-and-intent-confirmation.md）不变，仅存放位置与扩展名（.mdc → .md）变更，单一事实源仍为 skills/_common 文档。

### 备选方案与取舍（Options）
- 方案 A：保留在 .cursor/rules/，仅在文档中说明业务项目可从规范库复制。未选原因：与现有约定（rules/ 供业务项目复制）不一致，易混淆。
- 方案 B（采用）：规则文件迁至 rules/（.md），删除 .cursor/rules/ 下原文件；README、模板索引、方案文档、workspace-setup、setup_business_project.py、role-skills-design-memo 全量更新；实施后按 post-change 做全工程回顾并沉淀完整变更备忘。采用原因：与 project-docs-discovery、work-execution-standards 一致，业务项目通过复制 rules/ 或运行 setup 脚本即可获得该规则。

### 最终方案（What）
- 新增 `rules/role-boundary-and-intent-confirmation.md`（内容与原 .mdc 一致，含 frontmatter 与正文）。
- 删除 `.cursor/rules/role-boundary-and-intent-confirmation.mdc`。
- README、process/templates-index.md、人类手册/Cursor-多会话协作落地方案.md、人类手册/workspace/workspace-config/workspace-setup.md 中「供业务项目复制的规则」列举与复制说明均增加 `role-boundary-and-intent-confirmation.md`。
- setup_business_project.py 在「5) rules」中增加拷贝 `rules/role-boundary-and-intent-confirmation.md` 至业务项目 `.cursor/rules/`。
- role-skills-design-memo 中历史表述由 `.cursor/rules/role-boundary-and-intent-confirmation.mdc` 改为 `rules/role-boundary-and-intent-confirmation.md`。

### 影响范围（Where）
- 新增：`rules/role-boundary-and-intent-confirmation.md`
- 删除：`.cursor/rules/role-boundary-and-intent-confirmation.mdc`
- 修改：`README.md`、`process/templates-index.md`、`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/workspace/workspace-config/workspace-setup.md`、`人类手册/workspace/workspace-config/setup_business_project.py`、`人类手册/role-skills-design-memo.md`
- 受影响的映射/契约/索引：无结构变更；README 与 templates-index 的规则列举、方案文档与 workspace-setup 的复制说明、setup 脚本的拷贝列表已同步。

### 一致性检查（Check）
- 全工程搜索关键词：`role-boundary-and-intent-confirmation`、`.cursor/rules/role-boundary`、`role-boundary-and-intent-confirmation\.mdc`、`rules/role-boundary`
- 已检查的清单/索引/映射：README、process/templates-index.md、人类手册/Cursor-多会话协作落地方案.md、人类手册/workspace/workspace-config/workspace-setup.md、人类手册/role-skills-design-memo.md、setup_business_project.py
- 已运行的诊断：无（仅文档与脚本变更）；可选对修改过的 .md/.py 运行 markdown lint 或 Python lint。

### 遗留与后续（Next）
- 无。若业务项目采用本规范，复制 `rules/role-boundary-and-intent-confirmation.md` 到业务项目 `.cursor/rules/` 或运行 setup_business_project.py 即可获得该规则。

---

## 变更备忘（2026-03-14）：Pinned prompts 增加遵守业务项目 rules 要求

### 背景/触发（Context）
- 项目经理仍会越界、代替测试工程师等工作；仅靠规范库 skills 与业务项目已复制的 `.cursor/rules/` 仍不足，智能体可能未显式「关注」这些规则。
- 目标：在《Cursor-多会话协作落地方案》中为所有角色的 pinned prompt 增加「遵守业务项目 .cursor/rules/ 下已配置规则」的约定，使粘贴到 Cursor 会话的 pinned 内容直接提醒智能体查阅并遵守业务项目侧规则（含角色边界与意图确认）。

### 关键判断（Why）
- 人类手册仅供人读，不直接驱动智能体；但 pinned prompt 是用户粘贴到会话的固定说明，可显式要求智能体「先查阅并遵守业务项目 .cursor/rules/」，作为对 Cursor 已加载规则的补充提醒。
- 写作约定：文档中须使用「业务项目」而非「本项目」；本次修改时已将方案文档第三节内「当本项目」统一改为「当**业务项目**」。

### 备选方案与取舍（Options）
- 方案 A：仅依赖业务项目 .cursor/rules/ 与规范库 skills，不改人类手册。未选原因：智能体可能未主动查阅 rules，pinned prompt 中显式加入「遵守业务项目规则」可强化关注。
- 方案 B（采用）：在《Cursor-多会话协作落地方案》第三节约定的通用骨架与所有角色 pinned prompt（3.1、3.2–3.7、3.8、3.8.1–3.8.4）中增加一条「遵守业务项目 .cursor/rules/」的约定；并将「当本项目」改为「当**业务项目**」；在「其他角色可按上述模式自定义」处补充自定义时须包含该约定；在第三节开头与第七节 7.2 增加一句说明。采用原因：与 post-change 写作约定一致，且覆盖全部 11 处 pinned 块与自定义说明。

### 最终方案（What）
- 3.1 通用骨架：在「请遵守以下约定」后新增「0. **遵守业务项目规则**：…」；通用骨架中「本项目的活动规范」改为「业务项目的活动规范」。
- 3.2 项目经理：新增第 1 条遵守业务项目规则且不得代做、以 mapping 与 rules 为准；原 1–9 顺延为 2–10；（第 7、8 条→第 8、9 条）与 process 一致说明已更新。
- 3.3–3.7、3.8、3.8.1–3.8.4：均在「请遵守以下约定」后增加「1. **遵守业务项目规则**：…」，原条款顺延；各段内「当本项目使用」改为「当**业务项目**使用」。
- 第三节开头增加说明：各角色 pinned prompt 已包含「遵守业务项目 .cursor/rules/」的约定。
- 「其他角色可按上述模式自定义」处增加一条：自定义时须包含「遵守业务项目 .cursor/rules/ 下已配置规则」的约定。
- 第七节 7.2 做法中补充：各模板已包含「遵守业务项目 .cursor/rules/」的约定。

### 影响范围（Where）
- 修改：`人类手册/Cursor-多会话协作落地方案.md`（第三节全部 pinned 块、第三节开头、322 行附近自定义说明、第七节 7.2）
- 受影响的映射/契约/索引：无；仅人类手册内文案变更。

### 一致性检查（Check）
- 全工程搜索关键词：`当本项目`（该文档第三节内已无残留）、`遵守业务项目`、`.cursor/rules`
- 已检查的清单/索引/映射：Cursor-多会话协作落地方案.md 内 3.1、3.2、3.3、3.4、3.5、3.6、3.7、3.8、3.8.1–3.8.4 共 11 处 pinned 块均含「遵守业务项目 .cursor/rules/」或等价表述
- 已运行的诊断：无（仅人类手册 .md 变更）

### 遗留与后续（Next）
- 无。用户将各角色 pinned prompt 从本文档复制到 Cursor 会话并固定后，智能体会在约定中看到「遵守业务项目 .cursor/rules/」的要求，便于主动关注角色边界与意图确认等规则。

---

## 变更备忘（2026-03-14）：意图与规则冲突时先询问 + 规则归 rules、技能归 skills

### 背景/触发（Context）
- 项目经理仍会越界（如代写测试用例）；根因之一是对用户意图的理解（如「在本会话内交付」）若照此执行会与角色边界/流程规则冲突，但智能体未在行动前主动询问用户。
- 目标：将「当发现理解的意图与规则冲突时，应第一时间向用户询问」写为显式、全员适用的规则，并在 PM 场景下补充可操作话术；同时按「规则归 rules、技能归 skills」将角色边界与意图/需求确认的完整约定从 skills/_common 提升到 rules，单一事实源改为 rules/role-boundary-and-intent-confirmation.md，删除 skills/_common/role-boundary-and-intent-confirmation.md。

### 关键判断（Why）
- 角色边界与意图/需求确认为通用规则而非技能，应置于 rules/，供业务项目复制到 .cursor/rules/ 后生效；规范库内 skills 仅保留角色技能，不保留通用规则文档。
- 冲突→询问条款与全文仅在 rules 中维护，各 SKILL、pinned prompt 通过引用 rules 或简短概括建立关联；智能体依赖文档不引用人类手册路径，写作使用「业务项目」「规范库」等明确指代。

### 备选方案与取舍（Options）
- 方案 A：保留 skills/_common 为单一事实源，仅在 _common 中新增冲突→询问条款。未选原因：与「规则归 rules、技能归 skills」一致性原则不符。
- 方案 B（采用）：将 _common 的完整正文迁入 rules/role-boundary-and-intent-confirmation.md，在 rules 中新增冲突→询问条款及可选 PM 示例；删除 skills/_common/role-boundary-and-intent-confirmation.md；所有原引用 _common 的 YAML、SKILL、规则均改为引用 rules；PM SKILL 补充具体问法，PM pinned prompt 中增加对规则与 SKILL 的引用并强调冲突时先询问。采用原因：单一事实源在 rules，引用链清晰，且与 post-change 原则一致。

### 最终方案（What）
- rules/role-boundary-and-intent-confirmation.md：承载原 _common 完整正文（角色边界、意图/需求确认及按角色示例），新增「意图与规则冲突时须先向用户说明并询问」条款及摘要句，并增加项目经理示例问法；frontmatter 更新为本文即完整约定，不再引用外部路径。
- 删除：skills/_common/role-boundary-and-intent-confirmation.md。
- process/phases.yaml、roles/roles.yaml、mapping/phase-role-skill.yaml：注释中「见 skills/_common/...」改为「见 rules/role-boundary-and-intent-confirmation.md」。
- 各 SKILL（project-initiation、prd-requirements、architecture-design、requirements-review、prd-review、architecture-review、test-plan-review、devops-cicd、sre-reliability）：引用由 skills/_common/role-boundary-and-intent-confirmation.md 改为 rules/role-boundary-and-intent-confirmation.md。
- skills/project-initiation/SKILL.md：在角色边界段落增加「意图与规则冲突时先询问」及具体问法（先说明归属与规范要求，再询问「您是否希望我按规范派发给该角色并回收产出？还是因故坚持在本会话内由我代做（将注明越界）？」）。
- 人类手册/Cursor-多会话协作落地方案.md：3.2 项目经理 pinned prompt 第 1 条中增加「意图与规则冲突时须先向用户说明并询问，再执行；具体问法见业务项目 .cursor/rules/ 中角色边界与意图确认规则及规范库 skills/project-initiation/SKILL.md」。

### 影响范围（Where）
- 新增/修改：`rules/role-boundary-and-intent-confirmation.md`（合并全文并新增条款与 PM 示例）
- 删除：`skills/_common/role-boundary-and-intent-confirmation.md`
- 修改：`process/phases.yaml`、`roles/roles.yaml`、`mapping/phase-role-skill.yaml`（注释）；`skills/project-initiation/SKILL.md`（引用 + 具体问法）、`skills/prd-requirements/SKILL.md`、`skills/architecture-design/SKILL.md`、`skills/requirements-review/SKILL.md`、`skills/prd-review/SKILL.md`、`skills/architecture-review/SKILL.md`、`skills/test-plan-review/SKILL.md`、`skills/devops-cicd/SKILL.md`、`skills/sre-reliability/SKILL.md`（引用）；`人类手册/Cursor-多会话协作落地方案.md`（3.2 PM pinned prompt）；`人类手册/role-skills-design-memo.md`（本备忘）
- 受影响的映射/契约/索引：无结构变更；README、process/templates-index.md、workspace-setup.md、setup_business_project.py 已指向 rules/，无需修改。

### 一致性检查（Check）
- 全工程搜索关键词：`意图与规则冲突`、`冲突点并询问`、`role-boundary-and-intent-confirmation`、`理解用户输入`（SKILL 内）；`skills/_common/role-boundary`、`_common/role-boundary`（确认无残留引用）
- 已检查的清单/索引/映射：README、process/templates-index.md、人类手册/workspace/workspace-config/workspace-setup.md、setup_business_project.py（无 _common 引用）；各 SKILL、YAML、Cursor-多会话 3.2 中引用均为 rules
- 已运行的诊断：无（仅 .md/.yaml 文档变更）；可选对修改过的 .md 运行 markdown lint

### 遗留与后续（Next）
- 无。单一事实源现为 rules/role-boundary-and-intent-confirmation.md；业务项目复制该规则到 .cursor/rules/ 后即可获得完整约定（含冲突→询问条款与 PM 示例）。人类手册/过程改进/项目经理-角色边界与测试用例派发流程.md 作为原始文档保留，未修改。

---

## 变更备忘（2026-03-14）：全角色 pinned 补充意图与规则冲突时先询问（批判收敛）

### 背景/触发（Context）
- 在 3.2 项目经理 pinned prompt 已补充「意图与规则冲突时须先向用户说明并询问」及具体问法引用后，需在**所有角色**的 pinned prompt 中补充同类约定，以便与 rules 中「任何角色」条款一致；同时按批判意见控制维护成本、避免人类手册与 rules/SKILL 三处不同步。

### 关键判断（Why）
- 单一事实源在 rules + 各角色 SKILL，人类手册仅做**简短通用句 + 引用**，不写长段角色化说明，避免三处维护易过时。
- 明确**生效前提**（业务项目已复制规则、用户已粘贴 pinned）与**适用范围**（多根/单仓库、规范库路径何时可用），避免误以为人类手册直接驱动智能体。
- 多 SKILL 角色（如开发）：pinned 中「本角色对应 SKILL」改为「本阶段本角色在 mapping 中对应的 skill 及该 skill 的 SKILL.md」，避免歧义。
- 仅 PM 在 rules + SKILL 中已有具体问法；其他角色以 rules 通用条款 + 各自 SKILL 为准，不在人类手册中抄写角色化长段。

### 备选方案与取舍（Options）
- 方案 A：为每个角色在人类手册中写一段差异化说明（如「本角色尤须避免…」）。未选原因：与 rules/SKILL 重复，易过时，违背单一事实源。
- 方案 B（采用）：所有角色共用一句标准句 +「详见业务项目 .cursor/rules/ 及本角色对应 SKILL」；第三节开头增加生效前提与适用范围；3.5 开发单独用 mapping 表述。采用原因：人类手册仅引用、不复制细节，维护成本低，与 post-change 一致。

### 最终方案（What）
- 人类手册/Cursor-多会话协作落地方案.md **第三节开头**：在「以下各角色 pinned prompt 已包含…」段落后增加「生效前提」（业务项目已复制规则、用户已粘贴 pinned；人类手册仅为操作指引）与「适用范围」（规范库 skills 路径在多根或已打开规范库时可用；单仓库仅业务项目时以 .cursor/rules/ 及任务卡为准）。
- **3.1 通用骨架**：第 0 条「并严格遵守。」后追加标准句「**意图与规则冲突时须先向用户说明并询问，再执行**；详见业务项目 `.cursor/rules/` 中角色边界与意图确认规则及本角色对应 SKILL。」
- **3.2 项目经理**：已有长句，保留现状（已含冲突时先询问及具体问法引用）。
- **3.3、3.4、3.6、3.7、3.8、3.8.1～3.8.4**：各段第 1 条「并严格遵守。」后追加上述标准句（本角色对应 SKILL 保持通用表述）。
- **3.5 开发工程师**：第 1 条后追加标准句，但将「本角色对应 SKILL」写为「本阶段本角色在 mapping 中对应的 skill 及该 skill 的 SKILL.md」。

### 影响范围（Where）
- 修改：`人类手册/Cursor-多会话协作落地方案.md`（第三节开头：生效前提与适用范围；3.1、3.3、3.4、3.5、3.6、3.7、3.8、3.8.1、3.8.2、3.8.3、3.8.4 共 10 处 pinned 追加标准句；3.2 已具备故未改）；`人类手册/role-skills-design-memo.md`（本备忘）
- 受影响的映射/契约/索引：无

### 一致性检查（Check）
- 全工程搜索关键词：`意图与规则冲突`、`详见业务项目 .cursor/rules/`、`生效前提`、`适用范围`
- 已检查的清单/索引/映射：Cursor-多会话协作落地方案.md 第三节 3.1～3.8.4 共 11 处（3.2 已有、其余 10 处已补标准句），第三节开头已含生效前提与适用范围
- 已运行的诊断：无（仅人类手册 .md 变更）

### 遗留与后续（Next）
- 无。各角色 SKILL 中若缺「意图与规则冲突时」可操作话术，可按需后续补一句与本角色职责相符的示例，不做强制。

---

## 变更备忘（2026-03-16）：单仓对接方案 — `.cyber_team` 快照 + `.cursor-templates` 模板

### 背景/触发（Context）
- 对接方式从「多根工作区（业务项目 + 规范库）」统一为「业务项目单仓」：规范以 `.cyber_team/` 快照形式存在于业务项目内，规则与 skill 入口从 `.cursor-templates/` 复制到业务项目 `.cursor/`，智能体仅打开业务项目即可工作。
- 目标：单一对接模式、避免多根误读误写、规范版本可追溯（SNAPSHOT.yaml）。

### 关键判断（Why）
- 业务项目内以本仓 `.cyber_team/` 为唯一规范根；禁止在 `.cyber_team/` 外重复维护阶段/角色/映射定义。
- 规范库中模板放在 `.cursor-templates/`，避免被 Cursor 当成本仓规则/技能加载；仅在复制到业务项目 `.cursor/` 后生效。
- 路径与链接统一为 `.cyber_team/` 前缀及 `spec://` / `[[spec:...]]` 逻辑链接，约定见 `.cyber_team/CONVENTIONS-paths-and-links.md`。

### 备选方案与取舍（Options）
- 方案 A：继续支持多根工作区兼容。未选原因：用户明确统一为一种对接模式，简化心智与文档。
- 方案 B（采用）：仅保留单仓 + `.cyber_team` 快照 + `.cursor-templates` 生成 `.cursor`；README/process/templates-index 等以单仓为主、多根为历史方式说明。

### 最终方案（What）
- 新增 `.cyber_team/CONVENTIONS-paths-and-links.md`（路径与逻辑链接约定）、`.cyber_team/SNAPSHOT-STRATEGY.md`（快照与 SNAPSHOT 格式）、`.cyber_team/PILOT-VERIFICATION.md`（试点验证说明）。
- 新增 `.cursor-templates/rules/*.mdc.tpl` 与 `.cursor-templates/skills/<id>/SKILL.md` 薄入口模板，内容指向 `.cyber_team/...`。
- 更新 `.cursor/rules/post-change-project-wide-review.mdc` 第 1 条原则：允许业务项目以 `.cyber_team/` 承载规范快照并禁止其外重复定义；供业务项目复制的规则注明模板位于 `.cursor-templates/rules/`。
- 更新 README、process/templates-index.md、rules/project-docs-discovery.md：规范根与单仓应用方式；去除或弱化多根工作区为主流表述。
- 更新 `人类手册/workspace/workspace-config/setup_business_project.py`：支持将 process/roles/mapping/skills 复制到业务项目 `.cyber_team/`、写入 SNAPSHOT.yaml、从 `.cursor-templates` 生成 `.cursor/rules` 与 `.cursor/skills`（默认开启，可用 `--no-snapshot` 仅做传统初始化）。
- 试点：对 `pilot-business-project/` 执行脚本，验证 `.cyber_team` 与 `.cursor` 结构；`pilot-business-project/` 已加入 `.gitignore`。

### 影响范围（Where）
- 新增：`.cyber_team/CONVENTIONS-paths-and-links.md`、`.cyber_team/SNAPSHOT-STRATEGY.md`、`.cyber_team/PILOT-VERIFICATION.md`，`.cursor-templates/rules/*.mdc.tpl`、`.cursor-templates/skills/*/SKILL.md`
- 修改：`.cursor/rules/post-change-project-wide-review.mdc`，`README.md`，`process/templates-index.md`，`rules/project-docs-discovery.md`，`人类手册/workspace/workspace-config/setup_business_project.py`，`.gitignore`
- 受影响的映射/契约/索引：process/templates-index 中落点表增加 `.cursor-templates` 来源说明

### 一致性检查（Check）
- 全工程搜索关键词：`.cyber_team`、`.cursor-templates`、`多根工作区`、`SNAPSHOT.yaml`
- 已检查的清单/索引/映射：README、process/templates-index.md、post-change-project-wide-review.mdc
- 已运行的诊断：无（脚本已对 pilot-business-project 跑通）

### 遗留与后续（Next）
- 人类手册中仍有多处「多根工作区」表述（如 Cursor-多会话协作落地方案、workspace-setup），保留为历史方式说明，未在本次修改。
- 规范库自身尚未将 process/roles/mapping/skills 迁入 `.cyber_team/` 母本目录，当前复制来源仍为仓库根；若后续迁移，需同步更新 setup 脚本中的复制源路径。

---

## 变更备忘（2026-03-17）：规范母本迁入 `.cyber_team/`

### 背景/触发（Context）
- 按计划将规范库中 process、roles、mapping、skills 迁入 `.cyber_team/`，人类手册保留于仓库根（母本在 `.cyber_team/`，模板在 `.cursor-templates/`）。

### 最终方案（What）
- 将仓库根下 `process/`、`roles/`、`mapping/`、`skills/` 移动至 `.cyber_team/` 下；人类手册保留于仓库根 `人类手册/`。
- 更新 `人类手册/workspace/workspace-config/setup_business_project.py`：复制源改为 `norm/.cyber_team/process` 等，索引与 state 路径改为 `norm/.cyber_team/process/...`。
- 更新 README、`.cyber_team/process/templates-index.md`、`.cursor/rules/post-change-project-wide-review.mdc`、`rules/project-docs-discovery.md`、`rules/role-boundary-and-intent-confirmation.md`、`人类手册/workspace/workspace-config/workspace-setup.md` 中路径为 `.cyber_team/process/`、`人类手册/` 等。
- 对 `pilot-business-project` 重新运行初始化脚本，确认从 `.cyber_team/` 复制与生成 `.cursor` 正常。

### 影响范围（Where）
- 移动：`process/` → `.cyber_team/process/`，`roles/` → `.cyber_team/roles/`，`mapping/` → `.cyber_team/mapping/`，`skills/` → `.cyber_team/skills/`。**人类手册** 保留于仓库根 `人类手册/`，不放入 `.cyber_team/`（仅供人读，非智能体依赖规范）。
- 修改：上述脚本与文档中的路径引用。

### 遗留与后续（Next）
- **补充（同日）**：人类手册已移回仓库根，不置于 `.cyber_team/` 下。`人类手册/` 内部分文档仍含 `process/` 等旧路径表述，可按需改为 `.cyber_team/process/`；人类手册自身路径保持 `人类手册/`。

---

## 变更备忘（2026-03-17）：第八节全工程回顾 + 脚本迁至人类手册/scripts + 试点 tt_test_cases

### 背景/触发（Context）
- 按计划执行第八节「落地时的修改后全工程回顾」整轮；将业务项目初始化脚本由人类执行，从 `人类手册/workspace/workspace-config/` 迁至 `人类手册/scripts/`，仅保留单仓模式（多根工作区模式即将废弃）；对试点项目 `D:\my_ai_project\tt_test_cases` 执行初始化验证。

### 关键判断（Why）
- 脚本由人类在规范库侧执行，放在 `人类手册/scripts/` 更符合「人类手册下给人类用的工具」的定位；单仓为唯一推荐模式，移除 `--no-snapshot` 简化使用。

### 最终方案（What）
- **第八节回顾**：执行差异边界确认、全工程搜索关键词（`.cursor/specs`、`多根工作区`、`.cyber_team/`、`role-boundary-and-intent-confirmation`、`project-docs-discovery`）、清单/索引/映射检查（`.cyber_team/process/templates-index.md`、manifest、mapping、roles、phases、rules）、契约一致性（规范根 `.cyber_team/`、禁止智能体引用 `人类手册/` 路径）。
- **脚本迁移**：新增 `人类手册/scripts/setup_business_project.py`（单仓模式唯一入口，移除 `--no-snapshot`）；删除 `人类手册/workspace/workspace-config/setup_business_project.py`。所有引用更新为 `人类手册/scripts/setup_business_project.py`。
- **templates-index**：修正 process-tailoring 行，规范库无该文件，改为「由项目启动阶段产出，不复制自规范库」。
- **试点**：对 `D:\my_ai_project\tt_test_cases` 执行 `python 人类手册/scripts/setup_business_project.py D:\my_ai_project\tt_test_cases`，确认 `.cyber_team/` 与 `.cursor/` 生成正常。

### 影响范围（Where）
- 新增：`人类手册/scripts/setup_business_project.py`
- 删除：`人类手册/workspace/workspace-config/setup_business_project.py`
- 修改：`.cyber_team/PILOT-VERIFICATION.md`、`人类手册/workspace/workspace-config/workspace-setup.md`、`.cyber_team/process/templates-index.md`（process-tailoring 行）
- 试点目录：`D:\my_ai_project\tt_test_cases`（已生成 `.cyber_team/`、`.cursor/`、docs、scripts、state.yaml）

### 一致性检查（Check）
- 全工程搜索关键词：`.cursor/specs`、`spec://process/`、`多根工作区`、`workspace`、`.cyber_team/`、`role-boundary-and-intent-confirmation`、`project-docs-discovery`
- 已检查的清单/索引/映射：`.cyber_team/process/templates-index.md`、`.cyber_team/skills/manifest.yaml`、`.cyber_team/mapping/phase-role-skill.yaml`、`.cyber_team/roles/roles.yaml`、`.cyber_team/process/phases.yaml`、`.cyber_team/rules/`（路径与引用一致）
- 已运行的诊断：初始化脚本在 tt_test_cases 上执行成功

### 遗留与后续（Next）
- 多根工作区相关文档（如 Cursor-多会话协作落地方案、workspace-setup 中的多根说明）保留为历史参考，不再推荐；新项目一律使用单仓 + `人类手册/scripts/setup_business_project.py`。

---

## 变更备忘（2026-03-16）：人类手册单仓与路径对齐

### 背景/触发（Context）
- 规范库已按 cyber-team-root-spec-layout 计划切换为单仓模式，规范母本在 `.cyber_team/`。人类手册内仍存在「规范库路径」为无前缀的 `process/`、`roles/`、`mapping/`、`skills/` 及多根工作区、workspace 模板的表述，易导致读者按旧路径或多根方式操作。
- 目标：人类手册及全工程中凡描述规范库路径的，统一为 `.cyber_team/` 前缀；对接方式改为单仓优先，多根已废弃；方案 B 已选定：删除 `人类手册/workspace/` 并同步更新引用。

### 关键判断（Why）
- 人类手册仅供人读，但路径统一为 `.cyber_team/` 可与规范库实际结构一致，避免与 Agent 依赖的 .cyber_team 下文件混淆。
- workspace 保留 vs 删除：已选删除（方案 B），因单仓 + `人类手册/scripts/setup_business_project.py` 为唯一推荐方式，多根模板已无维护价值且易造成悬空引用。

### 备选方案与取舍（Options）
- 方案 A：保留 人类手册/workspace/，仅标注废弃；未选原因：计划明确选定方案 B，且删除后 README/方案文档已改写，无悬空操作步骤。
- 方案 B（采用）：删除 `人类手册/workspace/`，README 与 Cursor-多会话 中删除对 workspace-config 的链接，改为「多根已废弃，不提供模板」；人类手册内规范库路径全部加 `.cyber_team/` 前缀。

### 最终方案（What）
- 人类手册内已更新路径与单仓表述的文件：Cursor-多会话协作落地方案.md、多智能体蜂群编排落地方案.md、process/process.md、roles/project-manager.sop.md、过程改进/项目经理-角色边界与测试用例派发流程.md、role-skills-design.md、role-skill-consistency-check.md、role-skills-design-memo.md（增加当前规范根说明）；plan/ 下赛博包工头系列大纲.md、norm-improvement-plan.md、norm-improvement-execution-plan.md、norm-improvement-execution-plan-已完成.md、norm-backlog.md、阶段推进无例外规则-已实施.md。
- 删除：`人类手册/workspace/`（含 workspace-config 及模板）。
- 规范库内 Agent 用文档：`.cyber_team/process/artifact-metadata-convention.md`、`.cyber_team/skills/project-initiation/SKILL.md` 中规范路径统一为 `.cyber_team/...`。

### 影响范围（Where）
- 修改：上述人类手册文件及 README.md、.cyber_team/process/artifact-metadata-convention.md、.cyber_team/skills/project-initiation/SKILL.md。
- 删除：`人类手册/workspace/workspace-config/workspace-setup.md`、`人类手册/workspace/workspace-config/cursor-multi-root-workspace.code-workspace.template`，及目录 `人类手册/workspace/`。
- 受影响的引用：README「历史方式（多根工作区）」段改为「多根已废弃，不提供模板；请使用单仓 + 人类手册/scripts/setup_business_project.py」；Cursor-多会话 第六节部署结构改为单仓、无 workspace 模板引用；role-skills-design-memo 历史条目中出现的 `人类手册/workspace/` 为历史记录，保留不改。

### 一致性检查（Check）
- 全工程搜索关键词：`process/phases.yaml`、`process/state.yaml`、`roles/roles.yaml`、`mapping/phase-role-skill`、`skills/manifest`（不带 `.cyber_team/` 的规范库路径）、`人类手册/workspace/workspace-config`、`多根工作区`、`workspace-setup`。人类手册与 README 中规范库路径已统一为 `.cyber_team/`；README 与 Cursor-多会话 无悬空 workspace 链接；备忘历史条目保留旧路径不改为约定。
- 已检查的清单/索引/映射：README、.cyber_team/process/templates-index.md、人类手册/Cursor-多会话协作落地方案.md、人类手册/plan/ 下各文件、.cyber_team/skills/project-initiation/SKILL.md、.cyber_team/process/artifact-metadata-convention.md。
- 已运行的诊断：无脚本或构建；Markdown 路径与表述一致性已通过 grep 复核。

### 遗留与后续（Next）
- stages/、其他 roles/*.sop 未做逐文件 grep，可按需抽查；历史备忘中 `人类手册/workspace/` 的提及为过去时，无需改为「已删除」以免混淆时间线。

---

## 变更备忘（2026-03-17）：任务板操作单一定义（Rule + Skill），Pinned Prompt 仅引用

### 背景/触发（Context）
- 在实际业务项目中，多会话协作依赖 pinned prompt 提示任务板操作，但多轮对话后易发生“创建任务卡但未更新任务索引”的遗漏。
- 目标是降低 pinned prompt 的上下文开销，并通过“单一定义 + 引用”减少遗忘与三处不同步风险。

### 关键判断（Why）
- **约束与步骤应分层**：任务板的“必须/禁止”属于跨角色通用约束，适合放在业务项目 `.cursor/rules/`；具体命令与步骤适合集中到单一 skill，供规则引用。
- **避免映射膨胀**：不将任务板操作 skill 绑定到 phase-role-skill（否则需要为多阶段、多角色添加映射，维护成本高），而以 rules 驱动“需要时阅读并执行”。
- **人类手册只做引用与说明**：智能体行为的主杠杆在 `.cursor/rules/` 与 `.cyber_team/skills/*/SKILL.md`，人类手册中的 pinned 模板应收敛为引用，避免重复维护命令清单。

### 备选方案与取舍（Options）
- 方案 A：继续在各角色 pinned prompt 中内联 `task_board.py list/claim/update/new-card/add` 命令流。未选原因：上下文噪声大、容易丢失或被压缩，且命令变更会导致多处不同步。
- 方案 B（采用）：新增任务板规则（rule）约束“必须通过脚本”，新增 task-board-usage skill 作为唯一步骤来源，pinned prompt 仅保留一句引用。采用原因：单一定义、跨角色一致、降低遗漏。

### 最终方案（What）
- 新增任务板规则与模板：
  - `.cyber_team/rules/task-board-operations.md`
  - `.cursor-templates/rules/task-board-operations.mdc.tpl`
- 新增任务板使用 skill（唯一步骤来源）并登记：
  - `.cyber_team/skills/task-board-usage/SKILL.md`
  - `.cyber_team/skills/manifest.yaml` 增加 `task-board-usage`（由规则引用驱动，非按阶段/角色自动加载）
- 收敛人类手册中各角色 pinned prompt 的任务板长段命令为单句引用，并更新“任务板与脚本约定”表述：
  - `人类手册/Cursor-多会话协作落地方案.md`

### 影响范围（Where）
- 变更文件：
  - 新增：`.cyber_team/rules/task-board-operations.md`、`.cursor-templates/rules/task-board-operations.mdc.tpl`、`.cyber_team/skills/task-board-usage/SKILL.md`
  - 修改：`.cyber_team/skills/manifest.yaml`、`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/role-skills-design-memo.md`
  - 删除/重命名：无
- 受影响的映射/契约/索引（如有）：无（不修改 `phase-role-skill.yaml`；任务板路径契约延续 `scripts/task_board.py` 与 `docs/status/task-index.json`）。

### 一致性检查（Check）
- 全工程搜索关键词：`task-board-usage`、`task-board-operations`、`task_board.py list/claim/update/new-card/add`、`当**业务项目**使用“任务索引表 + 任务卡 + task_board.py”`、`不要直接编辑 task-index.json`
- 已检查的清单/索引/映射：`.cyber_team/skills/manifest.yaml`、`.cursor-templates/rules/`、`人类手册/Cursor-多会话协作落地方案.md`
- 已运行的诊断：`git diff --stat`（确认变更边界），未新增可执行代码故未跑测试

### 遗留与后续（Next）
- 若后续为 `task_board.py` 增加“创建即写索引”的复合命令（如 `create-task`），需在 `task-board-usage` 的“创建新任务”小节补充并将其作为推荐路径，保留 `new-card + add` 作为等价回退流程。

---

## 变更备忘（2026-03-17）：任务板 create-task（JSON 真源）+ claim 就绪校验（面向多智能体）

### 背景/触发（Context）
- 多会话/多智能体协作下，`new-card` 与 `add` 两步分离会导致“只建卡不入索引”；即使索引存在，也可能出现任务卡仍为占位符模板但被领取执行的风险。
- 目标：把“创建任务”与“可领取前置条件”机制化到脚本层，减少对 pinned prompt/对话记忆/人工自检的依赖。

### 关键判断（Why）
- **原子创建优先**：将“写入任务内容 + 写索引”收敛为单一命令，可从机制上消除漏步。
- **JSON 真源更适合多智能体**：结构化 payload 可做强校验与稳定路由；Markdown 作为渲染视图供人类阅读与跨会话传递上下文，避免双向漂移。
- **就绪校验应在 claim 前强制**：将“占位符未替换/渲染陈旧”等问题拦在领取前，避免任务被错误执行；校验失败仅拒绝 claim，不引入额外写副作用。

### 备选方案与取舍（Options）
- 方案 A：仅通过 rules/skill 强调“new-card 后必须 add”“领取前自检占位符”。未选原因：仍依赖人工/对话记忆，难以保证多智能体一致执行。
- 方案 B（采用）：脚本新增 `create-task`（payload JSON 真源 + 渲染任务卡 + 写索引），并在 `claim` 前强制就绪校验。采用原因：机制化、可验证、可扩展，且与现有锁/原子写入设计一致。

### 最终方案（What）
- `task_board.py` 新增命令：`create-task`，一次性完成：
  - 读取/写入 payload（`docs/status/task-cards/<task_id>.json`，真源，规范化输出）
  - 渲染任务卡（`docs/status/task-cards/<task_id>.md`，渲染视图）
  - 写入索引（记录 `payload_path`，并沿用 lock + 原子替换）
- `claim` 增强：在状态机校验前强制检查任务就绪（payload 合法、任务卡无占位符、任务卡不陈旧），失败则拒绝领取且不改索引。
- 文档同步：
  - `task-board-usage`：创建任务优先 `create-task`，明确 JSON 真源与渲染视图关系。
  - 任务板规则/模板与多会话落地方案：推荐使用 `create-task`，并说明 payload 存放约定。

### 影响范围（Where）
- 变更文件：
  - 修改：`.cyber_team/process/project-docs/status/task-board/task_board.py`、`.cyber_team/skills/task-board-usage/SKILL.md`、`.cyber_team/rules/task-board-operations.md`、`.cursor-templates/rules/task-board-operations.mdc.tpl`、`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/role-skills-design-memo.md`
- 受影响的映射/契约/索引（如有）：
  - 索引任务记录新增可选字段：`payload_path`
  - 新增/固定路径契约：`docs/status/task-cards/<task_id>.json`（真源）与 `docs/status/task-cards/<task_id>.md`（渲染）

### 一致性检查（Check）
- 全工程搜索关键词：`create-task`、`payload_path`、`task-board-usage`、`task_board.py claim`、`docs/status/task-cards/<task_id>.json`
- 已检查的清单/索引/映射：`.cursor-templates/rules/`、`.cyber_team/rules/`、`.cyber_team/skills/task-board-usage/SKILL.md`、`人类手册/Cursor-多会话协作落地方案.md`
- 已运行的诊断：`python -m py_compile` 通过；最小验证覆盖 `create-task` 成功路径、占位符 payload 失败路径、claim 成功路径

### 遗留与后续（Next）
- 可选增强：提供 `rerender-card` 或 `update-payload` 命令，便于 payload 更新后重新渲染 Markdown；并在索引中加入 payload hash/version 以做更强一致性校验。

---

## 变更备忘（2026-03-17）：创建任务卡入口收紧为 create-task（移除 new-card/add）

### 背景/触发（Context）
- 为进一步降低流程歧义与漏步风险，将“创建任务”的路径收敛为单一入口，避免出现不同角色在不同文档中选择不同创建方式（new-card+add vs create-task）导致执行不一致。

### 关键判断（Why）
- 创建任务的核心风险来自“多步可选路径”与“人类/智能体自由选择”，收敛为单一入口能从机制上减少遗漏与理解偏差。
- `create-task` 已覆盖“写 payload（真源）+ 渲染任务卡 + 写索引”的原子能力，保留 `new-card/add` 的收益低于其带来的分歧成本。

### 备选方案与取舍（Options）
- 方案 A：保留 `new-card + add` 作为兼容路径，并在文档中标注推荐 create-task。未选原因：仍保留歧义入口，且用户明确要求只保留唯一方法。
- 方案 B（采用）：文档/规则/skill 仅保留 `create-task`，并在脚本中移除 `new-card` 与 `add` 子命令入口。采用原因：唯一入口、降低歧义、减少漏步。

### 最终方案（What）
- `task_board.py`：移除 `add/new-card` 子命令入口，仅保留 `create-task` 作为创建新任务的方式。
- `task-board-usage` / 任务板规则 / 人类手册：删除 `new-card + add` 的创建说明，表述为“创建新任务仅允许使用 create-task”。\n
### 影响范围（Where）
- 修改：`.cyber_team/process/project-docs/status/task-board/task_board.py`、`.cyber_team/skills/task-board-usage/SKILL.md`、`.cyber_team/rules/task-board-operations.md`、`.cursor-templates/rules/task-board-operations.mdc.tpl`、`人类手册/Cursor-多会话协作落地方案.md`、`人类手册/role-skills-design-memo.md`\n
### 一致性检查（Check）
- 全工程搜索关键词：`new-card`、`add --task`、`new-card + add`、`create-task`
- 已运行的诊断：`python -m py_compile` + 最小验证（确认 `add/new-card` 不再可用，`create-task` 正常）\n
### 遗留与后续（Next）
- 若业务项目历史已存在通过 `add` 写入的索引记录，保持兼容（现有记录仍可 list/update/claim）；后续创建统一走 `create-task`。

