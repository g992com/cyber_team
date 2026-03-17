# 软件开发团队活动规范与角色 Skills 选型设计

## 1. 概述

**目标**：建立**软件开发团队的活动规范**，并在此基础上定义各角色在活动中使用的 Cursor Agent Skills。  
原目标仅为「为各角色建设可复用的 skill」；随文档演进，范围已扩展为：先定义团队级流程与各阶段角色职责、活动、SOP 及验收标准，再据此确定每个角色在活动中需要使用的 skill，使「活动规范」与「skill 落地」一致。

**本方案交付**：
- **活动规范部分**：软件开发流程（阶段定义）、各阶段角色职责/活动/SOP 要点/验收标准、角色-活动-技能对照；以及角色职责说明与 SOP/验收示例（可扩展为独立 roles-sop）。
- **Skill 选型部分**：角色与职责清单、SkillsMP 检索与安全扫描、选型结果与「推荐采纳 / 自建」建议、自建 skill 规格；采纳的 skill 可安装到项目 `.cursor/skills/`（本阶段不强制执行安装）。

**执行说明**：流程与阶段、各阶段角色与验收、角色-活动-技能对照、选型结果与自建规格均已写入本文档；采纳的 skill 需用 `skillsmp_install_skill` 或从第 8 节推荐安装表 GitHub 地址安装。

**方案定位与最终形态**

- **本文档性质**：本文档为**建设方案**，不是最终交付物本身。最终交付的规范是一组**结构化的文件**，包括但不限于：流程要求、各阶段定义、角色职责、活动与 SOP、验收标准、以及各角色在活动中使用的 skills 等；可由多文件、多格式组成，便于版本与维护。
- **受众与形态**：最终产出需**既可供人阅读**（团队协作、培训、过程改进），也**可供 Agent 使用**（解析流程、阶段、角色与 skill 映射，驱动行为）。因此流程、职责与技能对照等内容在落地时需具备**可读 + 可被 Agent 解析**的形态（如结构化描述、约定格式或机器可读配置）。
- **流程的规范性**：执行方可能是**单个 Agent 连续完成多阶段**，也可能是**多个 Agent 按角色/阶段协作**。为获得**尽可能稳定、可复现的输出**，流程按**规范流程**定义，而非「参考建议」；阶段、角色与验收标准共同约束 Agent 行为，减少随意性与输出漂移。
- **阶段与技能启用的目标形态**：期望的最终形态是**无需人工介入**——由 **Agent 决定并记录当前所处阶段与进展**，并据此**决定应启用的角色与 skill**。本方案中的流程定义、阶段-角色-活动-技能对照等内容，为后续实现「Agent 自主判断阶段、切换角色与加载对应 skill」提供规格基础；落地时需将阶段、进展与角色/skill 映射变为 Agent 可读、可推理与可执行的形式（如状态、规则或配置），以便 Agent 自动选择并启用相应 skill。**最终产出的目录结构建议见第 12 节。**

**选型原则**：
- **匹配度优先**：与角色职责直接相关、description 的 WHEN/WHAT 与典型场景一致。
- **安全为硬门槛**：仅考虑无 Critical 风险的 skill；存在 Critical 一律不采纳。

**安全领域评审**：已采纳方案 A。安全设计/架构评审由**设计评审专家**负责；实现层安全由**代码评审专家**在 PR 中顺带覆盖，或由**安全工程师**执行角色负责。不单独设「安全评审专家」。

---

## 2. 文档组织方式（三层结构）

本方案按**流程驱动**组织，三者顺序为：

1. **定义完整的软件开发流程**：明确阶段与阶段产出（第 3 节）。
2. **按阶段定义各角色的职责、活动、SOP 与验收标准**：每个阶段中谁负责什么、做什么、按什么步骤做、怎样算完成（第 4 节）。
3. **定义每个角色在活动中需要使用的 skill**：阶段 × 角色 × 活动 对应到具体 skill（第 5 节）。

后续第 6 节起为角色清单、选型结果、自建规格、SOP 示例与附录，与上述三层对应使用。

---

## 3. 软件开发流程（阶段定义）

阶段定义（id、name、order、outputs）的**唯一定义**见规范库 **`.cyber_team/process/phases.yaml`**；本节不重复列举，Agent 与人工均以该文件为准。以下为对人读的概要说明。

规范流程按阶段划分，用于约束 Agent 行为、获得稳定输出；在各阶段下挂载角色、活动与 skill。执行可为单 Agent 连续推进或多 Agent 协作，阶段与角色/skill 的映射需在最终结构化产出中可被 Agent 解析并用于自动启用相应 skill。评审阶段可与主阶段并行或在其后（如需求评审在需求阶段末，代码评审在开发 PR 提交时）。

---

## 4. 各阶段角色职责、活动、SOP 与验收标准

按阶段列出参与角色、职责与活动、SOP 要点、验收标准。详细 SOP 与步骤级验收要求见第 11 节示例及后续补全。

| 阶段 | 角色 | 职责/活动 | SOP 要点 | 验收标准 |
|------|------|-----------|----------|----------|
| 项目启动 | 项目经理 | 根据用户问题/需求按活动规范对项目活动裁剪，确定项目流程与计划 | 理解用户输入→评估项目特征→流程裁剪→输出项目计划与阶段/活动清单→确认后进入需求阶段 | 项目计划与裁剪说明已输出；阶段与活动清单与规范一致且可执行；用户已确认 |
| 需求 | 产品经理 | 需求分析、用户故事与验收标准、PRD、路线图/Backlog | 获取输入→分析优先级→编写故事/PRD→与干系人对齐→维护追溯 | 需求文档完整、可测、与路线图对齐；PRD 范围与优先级明确 |
| 需求评审 | 需求评审专家 | 审查需求/用户故事/PRD 的完整、一致、可测性 | 获取评审对象→完整性/一致性/可测性检查→输出评审结论 | 评审结论已分级；待澄清/须补充项已列出；可被开发与测试执行 |
| 架构/设计 | 架构师、DBA、安全工程师 | 架构设计、数据模型、API 设计、安全与合规要点 | 确定边界与选型→产出 ADR/架构图/数据模型/API 规约→评审准备 | 架构与数据/API 设计文档完整；ADR 关键决策已记录 |
| 设计/架构评审 | 设计评审专家 | 审查架构与设计、技术选型、安全设计、DBA/DevOps 方案 | 获取设计文档→按维度审查→输出结论与风险 | 审查维度覆盖；结论与改进建议明确 |
| 开发 | 前端工程师、后端开发工程师、DBA、安全工程师、技术写作 | 实现功能、schema/迁移、安全实现、文档草稿 | 按需求与设计实现→自测→提交 PR→配合评审 | 代码符合规范与设计；PR 可进入代码评审 |
| 代码评审 | 代码评审专家 | 对 PR 做规范/安全/性能/可维护性评审 | 获取变更范围→理解上下文→多维度审查→分级结论→确认后修改 | 结论已分级（P0–P3）；未在未确认前改代码 |
| 测试 | 测试工程师 | 测试策略、用例、执行、质量门禁 | 制定策略→设计用例→执行与回归→报告与门禁 | 测试计划与用例覆盖需求；门禁通过；报告可用 |
| 测试评审 | 测试评审专家 | 审查测试计划/用例的覆盖度与可执行性 | 获取测试产物→覆盖度与边界检查→输出结论 | 评审结论明确；覆盖度与可追溯性满足要求 |
| 部署/发布 | 运维工程师 | 流水线、环境、发布与回滚 | 设计流水线→配置环境→发布与验证→回滚预案 | 流水线可用；发布可回滚；发布说明更新 |
| 运维/复盘 | 可靠性工程师、安全工程师 | 监控告警、故障复盘、安全与合规运维 | 定义 SLO/告警→On-call 与响应→复盘与改进 | 监控与告警有效；复盘有结论与跟进 |

*上表为概要；每角色每阶段的详细 SOP 与步骤级验收可依第 11 节模板扩展并单独维护（如 roles-sop.md）。*

---

## 5. 角色-活动-技能对照

各阶段、角色与活动中**应使用的 skill**（来自本设计文档选型结果与推荐安装表）。同一角色在不同阶段可复用同一 skill 或按子活动选用不同 skill。  
**目标形态**：最终由 Agent 根据当前阶段与进展自动决定启用的角色与上表所列 skill，无需人工选择；本表内容在落地时需转为 Agent 可读的映射（如阶段→角色→skill 列表），以支持自动启用。

| 阶段 | 角色 | 活动/场景 | 使用 skill（名称） | 备注 |
|------|------|-----------|-------------------|------|
| 项目启动 | 项目经理 | 项目启动与流程裁剪 | project-initiation（自建） | 第 10 节自建规格；依据 PMBOK 裁剪与 16326 |
| 需求 | 产品经理 | 用户故事与验收标准 | user-story (razbakov) | 见推荐安装表 |
| 需求 | 产品经理 | PRD/需求文档 | prd-requirements（自建或检索） | 第 10 节自建规格 |
| 需求评审 | 需求评审专家 | 用户故事/验收标准评审 | user-story 兼顾 或 requirements-review（自建） | 多 skill 见第 9 节 |
| 需求评审 | 需求评审专家 | PRD/需求文档评审 | prd-review（自建） | 第 10 节 |
| 架构/设计 | 架构师 | 架构与 ADR | architecture-design（自建） | 第 10 节 |
| 架构/设计 | DBA | 数据模型与迁移 | flyway-migration (martinellich) | 见推荐安装表 |
| 设计/架构评审 | 设计评审专家 | 架构/设计/安全设计评审 | audit-full 可选 或 architecture-review（自建） | 第 9、10 节 |
| 开发 | 前端工程师 | 前端实现 | frontend-design / frontend-style-guide | 二选一或并列 |
| 开发 | 后端开发工程师 | 后端与 API | backend-development (MOODMNKY) | 推荐安装表 |
| 开发 | 技术写作 | 文档 | technical-writer (sjungling) | 推荐安装表 |
| 代码评审 | 代码评审专家 | PR/代码审查 | code-review-expert (sanyuan0704) / review-pr / code-review (folio) | 三选一或并列 |
| 测试 | 测试工程师 | 测试编写与策略 | pytest (the-perfect-developer)；可选 testing-patterns | 推荐安装表 |
| 测试评审 | 测试评审专家 | 测试计划/用例评审 | test-plan-review（自建） | 第 10 节 |
| 部署/发布 | 运维工程师 | CI/CD 与发布 | devops-cicd（自建） | 第 10 节 |
| 运维/复盘 | 可靠性工程师 | 可靠性、监控、复盘 | sre-reliability（自建） | 第 10 节 |
| 多阶段 | 安全工程师 | 安全设计与实现层检查 | code-review (folio) 与设计/架构评审配合 | 方案 A |

*完整 GitHub 链接见第 8 节「推荐直接安装的 skill 链接」；自建 skill 规格见第 10 节。*

---

## 6. 角色与职责（扩展）

### 6.1 开发与交付角色

#### 前端工程师
1. 使用主流前端框架（React / Vue / Angular 等）开发组件与页面
2. 编写与维护 CSS/样式（含响应式、主题、可访问性）
3. 配置构建与打包（Vite/Webpack 等）、优化产出与加载性能
4. 保证可访问性（a11y）与基础 SEO
5. 与后端 API 对接、管理前端状态与路由
6. 编写前端单元/组件测试

#### 后端开发工程师
1. 设计并实现 REST/GraphQL 等 API、版本与兼容策略
2. 实现服务端业务逻辑、领域模型与分层架构
3. 数据库访问（ORM/查询）、事务与一致性
4. 缓存策略（如 Redis）、会话与认证状态
5. 认证与授权（JWT/OAuth、RBAC 等）
6. 日志、监控与错误处理

#### 测试 / QA
1. 编写与维护单元测试、集成测试、E2E 测试
2. 制定测试策略（范围、优先级、自动化比例）
3. 设计测试数据与环境、数据准备与清理
4. 执行与回归测试、缺陷跟踪与复现
5. 质量门禁（覆盖率、通过率、性能基线）
6. 测试报告与质量度量

#### 运维工程师
1. 设计与维护 CI/CD 流水线（构建、测试、部署）
2. 容器化（Docker）与编排（Kubernetes 等）
3. 部署与发布策略（蓝绿、金丝雀、回滚）
4. 基础设施即代码（IaC）、配置管理
5. 流水线与环境的权限与审计
6. 与开发、测试、运维的协作与工具链打通

#### 产品 / 需求
1. 需求 elicitation、分析与优先级排序
2. 编写用户故事、验收标准与用例
3. 路线图与版本规划、依赖与风险识别
4. 与干系人对齐、需求变更与追溯
5. 产品指标与成功标准定义
6. 需求文档与知识库维护

*本角色建议由多个 skill 支持：① 用户故事与验收标准；② PRD/产品需求文档；③ 可选 故事地图/路线图/估算。详见第 8 节检索词表与第 9 节选型结果。*

#### 架构师
1. 系统与子系统设计、模块划分与接口定义
2. 技术选型与选型依据文档
3. 可扩展性、可用性、一致性设计
4. 架构决策记录（ADR）、与团队沟通架构意图
5. 技术债务识别与演进路线
6. 与安全、性能、运维需求的架构级对接

#### DBA
1. 数据建模（概念、逻辑、物理）、表结构与索引设计
2. SQL 与查询优化、执行计划分析
3. 数据迁移与版本管理（schema 变更、回滚）
4. 备份与恢复策略、数据保留与归档
5. 数据质量与一致性校验
6. 容量规划与库性能监控

#### 安全工程师
1. 安全设计与威胁建模、安全需求与合规
2. 漏洞扫描与加固、依赖与供应链安全
3. 认证/授权/密钥管理、敏感数据保护
4. 安全评审（设计/实现/配置）与渗透测试配合
5. 事件响应与安全运维
6. 安全策略与意识培训支持

#### 可靠性工程师
1. 可靠性目标（SLA/SLO/SLI）与错误预算
2. 监控、告警与 On-call、故障发现与升级
3. 容量规划与成本优化
4. 故障复盘与改进、变更与发布风险控制
5. 自动化运维与自愈、混沌工程
6. 文档与 Runbook、与开发/运维协作

#### 技术写作
1. 文档结构设计与信息架构
2. API 文档、用户手册与操作指南
3. 版本说明、发布说明与迁移指南
4. 术语与风格统一、可读性与可维护性
5. 文档版本与发布流程
6. 与开发/产品对接以获取准确信息

---

### 6.2 评审专家角色

#### 需求评审专家
1. 审查需求/用户故事/验收标准的完整性、一致性、可测性
2. 识别遗漏、歧义与冲突，提出澄清与补充建议
3. 优先级与范围把关、与路线图对齐
4. 确保需求可被开发与测试执行
5. 参与需求评审会议并输出评审结论

*本角色建议由多个 skill 支持，与产品经理文档类型对应：① 用户故事与验收标准评审；② PRD/需求文档评审；③ 可选 路线图或计划与需求追溯评审。详见第 8 节检索词与第 9、10 节。*

#### 代码评审专家
1. 审查 PR/代码变更：逻辑正确性、边界与异常处理
2. 规范与最佳实践（命名、结构、可读性）
3. 缺陷与风险（含实现层安全：依赖、密钥、常见漏洞模式）
4. 可维护性、性能与测试覆盖建议
5. 给出明确、可操作的评审意见与优先级

#### 设计评审专家
1. 审查架构与设计文档、技术选型合理性
2. 可扩展性、一致性、风险与技术债务
3. 数据架构与模型、容量与可靠性设计
4. **安全设计/架构评审**：威胁建模、安全架构、数据与访问合规
5. DBA/DevOps/SRE 领域的设计与方案评审（数据模型、流水线、部署、监控）
6. 输出评审结论与改进建议

#### 测试评审专家
1. 审查测试计划/策略的覆盖度与合理性
2. 审查测试用例的边界、等价类与可重复性
3. 测试数据与环境准备、数据依赖
4. 质量门禁与通过标准是否明确
5. 与需求/设计的可追溯性

---

## 7. 选型检查单（模板）

对每个候选 skill 填写：

**安全（硬门槛）**
- [ ] 已用 SkillsMP 安全扫描
- [ ] 无 Critical 风险
- [ ] （可选）Medium/High 风险已记录并说明是否可接受

**匹配度（主要排序依据）**
- [ ] 与目标角色职责直接相关（可引用第 6 节职责列表）
- [ ] description 的 WHEN/WHAT 与角色典型场景一致
- [ ] 匹配程度：高 / 中 / 低 + 一句话理由

**可维护性与生态（次要）**
- [ ] 星星数、最近更新时间（若提供）
- [ ] 与项目技术栈一致性
- [ ] 与同角色其他候选重叠情况；若重叠，取更贴合者

**决策**
- [ ] **采纳**：直接安装 / 需改编
- [ ] **自建**：无合适候选或需合并多个 skill；注明依据
- [ ] **暂缓**：理由

---

## 8. 检索与扫描记录

**执行记录**：已使用 SkillsMP 完成关键词检索及部分 AI 语义检索，并对各角色首选候选执行安全扫描。检索词与扫描结果见下表及第 9 节。

**实际使用的检索词与方式**：

| 角色 | 关键词检索（建议） | AI 语义检索（建议） |
|------|---------------------|----------------------|
| 前端工程师 | `frontend react`, `frontend vue`, `component`, `tailwind`, `accessibility` | "React Vue components, CSS, build, a11y, frontend patterns" |
| 后端开发工程师 | `backend api`, `REST API`, `OpenAPI`, `microservice`, `authentication` | "Backend API design, server logic, database, auth, REST gRPC" |
| 测试工程师 | `testing pytest`, `unit test`, `e2e`, `integration test`, `coverage`, `Jest` | "Unit integration E2E testing, test strategy, coverage, fixtures" |
| 运维工程师 | `devops cicd`, `pipeline`, `docker kubernetes`, `GitHub Actions`, `deploy` | "CI/CD pipeline, Docker K8s, deployment, release, IaC" |
| 产品经理 | 见下方「产品经理：多 skill 支持」 | — |
| 架构师 | `architecture design`, `system design`, `ADR`, `technical decision` | "System architecture, ADR, technical decisions, layering" |
| DBA | `database sql`, `schema`, `migration`, `ORM`, `Flyway`, `Alembic` | "Database schema, SQL optimization, migration, data model" |
| 安全工程师 | `security audit`, `vulnerability`, `OWASP`, `dependency audit` | "Security review, vulnerability, dependency, compliance" |
| 可靠性工程师 | `sre`, `observability`, `SLO`, `monitoring`, `incident`, `runbook` | "SRE reliability, SLO, monitoring, incident, runbook" |
| 技术写作 | `technical writing`, `documentation`, `README`, `API docs`, `changelog` | "Technical docs, API docs, README, changelog, user guide" |
| 需求评审专家 | 见下方「需求评审专家：多 skill 支持」 | — |
| 代码评审专家 | `code review`, `PR review`, `pull request`, `diff review` | "Code review, PR review, pull request, best practices" |
| 设计评审专家 | `architecture review`, `design review`, `technical review` | "Architecture review, design review, security design review" |
| 测试评审专家 | `test plan review`, `test case review`, `test strategy` | "Test plan review, test case review, coverage, test strategy" |

**产品经理：多 skill 支持**

产品经理角色建议由 **2～3 个 skill** 共同支持，对应不同文档类型与职责（用户故事、PRD、路线图/故事地图）。检索时可分主题进行：

| 子领域 | 关键词检索示例 | AI 语义检索示例 |
|--------|----------------|------------------|
| 用户故事与验收标准 | `user story`, `acceptance criteria`, `INVEST` | "User story, acceptance criteria, INVEST, requirements" |
| PRD / 产品需求文档 | `PRD`, `product requirements`, `requirements document`, `scope` | "PRD, product requirements, scope, priorities, acceptance criteria" |
| 路线图 / 故事地图（可选） | `story map`, `backlog`, `roadmap`, `estimation` | "Story map, backlog, roadmap, estimation, development plan" |

**需求评审专家：多 skill 支持**

与产品经理角色对应，需求评审专家建议由 **2～3 个 skill** 支持，按评审对象分主题检索：

| 子领域 | 关键词检索示例 | AI 语义检索示例 |
|--------|----------------|------------------|
| 用户故事与验收标准评审 | `user story review`, `acceptance criteria review`, `requirements review` | "Review user stories, acceptance criteria, completeness, testability" |
| PRD / 需求文档评审 | `PRD review`, `requirements review`, `scope review`, `product requirements review` | "Review PRD, product requirements, scope, priorities, consistency" |
| 路线图或计划与追溯（可选） | `backlog review`, `roadmap review`, `traceability` | "Review backlog, roadmap, requirements traceability, dependencies" |

**安全扫描**：对每个候选 skill 的 GitHub URL 调用 `skillsmp_scan_skill`；仅采纳无 **Critical** 风险的 skill。

**已扫描的候选摘要**（部分）：lightdash/frontend-style-guide（LOW）、poko8nada/frontend-design（SAFE）、MOODMNKY/backend-development（SAFE）、NeverSight/backend-dev-guides（CRITICAL 不采纳）、yonatangross/testing-patterns（HIGH）、the-perfect-developer/pytest（LOW）、NeverSight/devops-cicd（CRITICAL）、LambdaTest/cicd-pipeline-skill（CRITICAL）、yonatangross/review-pr（LOW）、folio-org/code-review（LOW）、**sanyuan0704/code-review-expert**（已人工确认安全）、razbakov/user-story（LOW）、ab300819/devdocs-requirements（CRITICAL）、sjungling/technical-writer（LOW）、yonatangross/scope-appropriate-architecture（CRITICAL）、yonatangross/database-patterns（HIGH）、martinellich/flyway-migration（SAFE）、yonatangross/audit-full（MEDIUM）。

**推荐直接安装的 skill 链接**（无 Critical，采纳决策）：

| 角色 | Skill 名称 | GitHub URL |
|------|------------|------------|
| 前端工程师 | frontend-design | https://github.com/poko8nada/portfolio-v3/tree/main/.github/skills/frontend-design |
| 前端工程师 | frontend-style-guide | https://github.com/lightdash/lightdash/tree/main/.claude/skills/frontend-style-guide |
| 后端开发工程师 | backend-development | https://github.com/MOODMNKY-LLC/mood-mnky-command/tree/main/.cursor/skills/backend-development |
| 测试工程师 | pytest | https://github.com/the-perfect-developer/the-perfect-opencode/tree/main/.opencode/skills/pytest |
| 产品经理（① 用户故事） | user-story | https://github.com/razbakov/skills/tree/main/skills/user-story |
| DBA | flyway-migration | https://github.com/martinellich/aiup-marketplace/tree/main/aiup-vaadin-jooq/skills/flyway-migration |
| 安全（与代码评审共用） | code-review | https://github.com/folio-org/folio-eureka-ai-dev/tree/master/skills/code-review |
| 技术写作 | technical-writer | https://github.com/sjungling/sjungling-claude-plugins/tree/main/plugins/technical-writer/skills/technical-writer |
| 代码评审专家 | review-pr | https://github.com/yonatangross/orchestkit/tree/main/plugins/ork/skills/review-pr |
| 代码评审专家 | code-review | https://github.com/folio-org/folio-eureka-ai-dev/tree/master/skills/code-review |
| 代码评审专家 | code-review-expert（sanyuan0704） | https://github.com/sanyuan0704/code-review-expert（已人工确认安全） |

**code-review-expert（sanyuan0704）简要说明**：基于当前 git 变更做结构化评审，覆盖 SOLID/架构、安全（XSS/注入/SSRF/鉴权/密钥泄露等）、性能（N+1/缓存/内存）、错误处理与边界条件、死代码与移除规划；输出 P0–P3 分级结论，且**仅在用户确认后再实施修改**（review-first）。含 references：solid-checklist、security-checklist、code-quality-checklist、removal-plan。**已人工确认安全，可放心安装。**

---

## 9. 分角色选型结果

| 角色 | 候选 skill（名称 + GitHub） | 安全扫描结果 | 匹配度 | 决策 | 理由 |
|------|-----------------------------|--------------|--------|------|------|
| 前端工程师 | frontend-style-guide (lightdash/lightdash)；frontend-design (poko8nada/portfolio-v3) | LOW；SAFE | 高 | **采纳**（二选一或并列） | lightdash 偏 React/Mantine/TSX；frontend-design 通用前端与设计质量，可按技术栈选 |
| 后端开发工程师 | backend-development (MOODMNKY-LLC/mood-mnky-command) | SAFE | 高 | **采纳** | API/数据库/微服务/ TDD，无 Critical，可直接安装 |
| 测试工程师 | pytest (the-perfect-developer/the-perfect-opencode)；testing-patterns (yonatangross) 为 HIGH | LOW；HIGH | 中～高 | **采纳** pytest；testing-patterns 可选 | pytest 通过安全；testing-patterns 覆盖全类型测试但扫描为 HIGH（子目录未扫），可选需人工复核 |
| 运维工程师 | devops-cicd、ci-cd-pipeline、cicd-pipeline-skill 等扫描均为 CRITICAL | CRITICAL | — | **自建** | 现有候选涉及修改 CI/CD 工作流等被标 Critical，建议自建「DevOps/CICD」skill |
| 产品经理 | user-story (razbakov/skills)；PRD/需求文档类待补充检索 | LOW；— | 高；— | **采纳**（多 skill） | ① 用户故事与验收标准：已采纳 user-story。② PRD/产品需求文档：建议用第 8 节关键词再检索或自建。③ 可选：故事地图/路线图/估算（story map, roadmap, estimation） |
| 架构师 | scope-appropriate-architecture (yonatangross) 为 CRITICAL；audit-full 为 MEDIUM | CRITICAL；MEDIUM | — | **自建**；audit-full 可选 | 架构类候选多含 supply-chain/修改流水线等 Critical；audit-full 为全库审计可作架构/安全评审参考但为 MEDIUM，建议自建「架构设计」skill |
| DBA | flyway-migration (martinellich/aiup-marketplace)；database-patterns (yonatangross) 为 HIGH | SAFE；HIGH | 高（Flyway 偏 Java） | **采纳** flyway-migration；database-patterns 可选 | Flyway 迁移与 schema 版本管理，安全通过；database-patterns 更通用但 HIGH，可选 |
| 安全工程师 | code-review (folio-org/folio-eureka-ai-dev) 含安全维度 | LOW | 中 | **采纳**（与代码评审共用或单独） | 结构化代码/安全/质量评审，可与代码评审专家角色共用 |
| 可靠性工程师 | 未检索到通过安全门槛的专用 skill | — | — | **自建** | 建议自建「SRE/可靠性」skill，覆盖 SLO、监控、故障复盘等 |
| 技术写作 | technical-writer (sjungling/sjungling-claude-plugins) | LOW | 高 | **采纳** | README/API 文档/发布说明等，触发明确，可直接安装 |
| 需求评审专家 | user-story 可部分覆盖用户故事评审；PRD/需求文档评审待检索或自建 | —；CRITICAL；— | — | **采纳**（多 skill） | ① 用户故事与验收标准评审：可用 user-story 兼顾产出与评审，或自建「用户故事/验收标准评审」。② PRD/需求文档评审：用第 8 节关键词检索或自建。③ 可选：路线图/计划与追溯评审 |
| 代码评审专家 | review-pr (yonatangross)；code-review (folio-org)；**code-review-expert (sanyuan0704)** | LOW；LOW；**已人工确认安全** | 高；高；**高** | **采纳**（三选一或并列） | review-pr 多 agent 并行 PR 审查；code-review 结构化 diff 含安全；**code-review-expert** 以 git diff 为输入、SOLID/安全/性能/边界/移除规划，P0–P3 分级与确认后再改，与角色职责高度一致，Stars 高（2k+），已人工确认安全 |
| 设计评审专家 | audit-full (yonatangross) 全库审计含架构/安全 | MEDIUM | 中 | **可选采纳** 或**自建** | audit-full 为 MEDIUM（子目录未扫），可作架构/安全设计评审参考；或自建「设计/架构评审」skill |
| 测试评审专家 | 未检索到专门「测试评审」skill | — | — | **自建** | 建议自建「测试计划/用例评审」skill |

---

## 10. 自建 Skill 规格

以下角色建议自建 skill，供后续按 Cursor **create-skill 技能**的指引编写 SKILL.md。**落地顺序**：按第 3 节软件开发阶段顺序进行（需求 → 需求评审 → 架构/设计 → 设计/架构评审 → … → 运维/复盘），详见第 12 节「自建 skill 落地顺序」。

**开发自建 skill 时的必遵约定**：实施本方案中的任一自建 skill 时，**必须先阅读并遵循 Cursor 的 create-skill 技能**（技能路径：`create-skill` / 对应 SKILL.md）。应按照 create-skill 中的流程执行：Discovery（明确用途、触发场景、产出格式）→ Design（name、description、章节与引用）→ Implementation（目录结构、SKILL.md 含 YAML frontmatter、可选 reference/examples）→ Verification（description 含 WHAT+WHEN、第三人称、SKILL.md 控制在 500 行内、术语一致、引用仅一层）。description 须具体且包含触发词，便于 Agent 发现与选用；自建 skill 的 name、description 要点及触发场景已在下表给出，可作为 Discovery/Design 的输入，具体正文需按 create-skill 的写作原则编写。

| 角色 | 建议 skill name | description 要点 | 主要章节与触发场景 |
|------|-----------------|------------------|--------------------|
| 项目经理 | project-initiation | 根据用户问题/需求按活动规范对项目活动裁剪，产出项目计划与阶段/活动清单。Use when 项目启动、流程裁剪、确定项目流程与计划、项目计划。 | 理解用户输入、评估项目特征、流程裁剪、产出项目计划与阶段/活动清单；触发：项目启动、流程裁剪、项目计划、initiation、tailoring |
| 产品经理（② PRD） | prd-requirements 或 product-requirements | PRD/产品需求文档：功能边界、优先级、验收标准、范围与干系人对齐。Use when 编写或澄清 PRD、产品需求、功能范围、验收标准。 | 文档结构（背景/目标/范围/优先级/验收标准）、与用户故事的衔接；触发：PRD、product requirements、需求文档、scope、验收标准 |
| 运维工程师 | devops-cicd 或 cicd-pipeline | CI/CD 流水线设计、GitHub Actions/GitLab CI、容器与部署、发布策略。Use when 用户提及 CI/CD、流水线、部署、Docker、K8s。 | 流水线结构、构建/测试/部署步骤、环境与权限、回滚；触发：cicd、pipeline、deploy、docker、kubernetes |
| 架构师 | architecture-design 或 scope-appropriate-architecture | 系统与模块设计、技术选型、可扩展性与一致性、ADR。Use when 设计架构、选型、编写 ADR。 | 项目分层与边界、选型原则、ADR 模板、技术债务；触发：architecture、design、ADR、技术选型 |
| 可靠性工程师 | sre-reliability 或 observability-runbook | 可靠性目标（SLO/SLI）、监控与告警、故障复盘、容量与成本。Use when 用户提及 SRE、监控、告警、故障、On-call。 | SLO 定义、监控指标、告警规则、复盘模板、Runbook；触发：sre、reliability、monitoring、incident |
| 需求评审专家（① 用户故事/验收标准） | requirements-review 或 user-story-review | 审查用户故事与验收标准的完整性、一致性、可测性（INVEST）；遗漏与冲突识别。Use when 评审用户故事、验收标准。 | 审查清单（完整/一致/可测）、与开发/测试可执行性；触发：用户故事评审、验收标准评审 |
| 需求评审专家（② PRD/需求文档） | prd-review 或 requirements-doc-review | 审查 PRD/需求文档的功能边界、优先级、范围、与用户故事一致性；干系人对齐。Use when 评审 PRD、产品需求文档、范围与优先级。 | 功能边界与范围、优先级与依赖、验收标准覆盖；触发：PRD 评审、需求文档评审、范围评审 |
| 需求评审专家（③ 可选 计划/追溯） | roadmap-traceability-review | 审查路线图/开发计划与需求的追溯、依赖与里程碑一致性。Use when 评审路线图、backlog、需求追溯。 | 需求与计划追溯、依赖与里程碑；触发：路线图评审、追溯性评审 |
| 设计评审专家 | architecture-review | 架构与设计文档审查、技术选型合理性、可扩展性与一致性、安全设计/威胁建模。Use when 评审架构或设计文档。 | 审查维度（一致性/扩展性/风险/安全设计）、DBA/DevOps/SRE 方案评审；触发：架构评审、设计评审、技术方案评审 |
| 测试评审专家 | test-plan-review | 审查测试计划/用例/策略的覆盖度、边界与可重复性。Use when 评审测试计划或测试用例。 | 覆盖度与边界、用例质量、数据与环境依赖、可追溯性；触发：测试评审、测试计划评审、用例评审 |

---

## 11. 角色职责说明、SOP 与验收要求（建议）

本节为**建议扩展内容**：为各角色补充正式的职责说明、标准作业程序（SOP）及各步骤验收要求，便于自建 skill 时写入 SKILL.md、团队培训与一致性检查。第 6 节已给出职责列表，第 4 节已按阶段给出职责/活动/验收概要，此处提供**通用模板**及**2 个完整示例**，其余角色可后续按模板补全或单独成文档（如 `roles-sop.md`）。

### 11.1 通用模板

| 要素 | 内容要点 |
|------|----------|
| **职责说明** | 一段话概括角色定位与产出；可引用第 6 节职责列表。 |
| **SOP** | 按执行顺序列出的步骤（1. 2. 3. …），每步一句话可执行动作。 |
| **各步骤验收要求** | 对每一步列出「完成标准」或「通过条件」，便于自检与评审。 |

### 11.2 示例一：代码评审专家

**职责说明**  
对 PR/代码变更进行结构化审查，从正确性、规范、安全、可维护性与性能等维度给出可操作意见，并按优先级分级；仅在评审结论与用户确认后再实施修改。

**SOP**

1. 获取变更范围：通过 `git status` / `git diff` 或 PR 内容确定评审范围。
2. 理解上下文：识别入口、关键路径（鉴权、支付、数据写入、网络）及与变更相关的模块与契约。
3. 执行审查维度：按 SOLID/架构、安全、性能、错误处理与边界条件、死代码/移除候选逐项检查。
4. 输出评审结论：按 P0–P3 或约定优先级分级，区分「必须修复 / 建议修复 / 可选」。
5. 确认与后续：向用户呈现结论并询问是否实施修改；仅在用户明确选择后再改代码。

**各步骤验收要求**

| 步骤 | 验收要求 |
|------|----------|
| 1. 获取变更范围 | 变更文件与行数已明确；大 diff 已按模块/功能拆分审视。 |
| 2. 理解上下文 | 已识别关键路径与受影响模块；边界与契约已了解。 |
| 3. 执行审查维度 | 已按规范、安全、性能、错误处理、边界、移除候选等维度检查；无遗漏维度。 |
| 4. 输出评审结论 | 结论已分级（P0–P3 或等价）；每条结论含问题描述与建议修复方式。 |
| 5. 确认与后续 | 已向用户说明结论并给出可选后续动作；未在未确认前实施修改。 |

### 11.3 示例二：需求评审专家（用户故事与验收标准）

**职责说明**  
对用户故事与验收标准进行审查，确保完整性、一致性、可测性及与路线图/范围的匹配，识别遗漏与冲突并提出澄清与补充建议，使需求可被开发与测试执行。

**SOP**

1. 获取评审对象：明确待评审的用户故事、验收标准或需求文档范围。
2. 完整性检查：检查是否具备角色/用户、目标、价值、验收标准及可测试条件。
3. 一致性检查：与既有需求、PRD、术语对照，识别冲突与重复。
4. 可测性与可执行性：验收标准是否可验证、是否可拆为开发与测试任务。
5. 优先级与范围：与路线图/迭代计划对齐，标注优先级与依赖。
6. 输出评审结论：列出通过项、待澄清项、必须补充项及建议优先级。

**各步骤验收要求**

| 步骤 | 验收要求 |
|------|----------|
| 1. 获取评审对象 | 评审范围已明确；故事/验收标准已完整获取。 |
| 2. 完整性检查 | 已按 INVEST 或约定清单检查；缺失项已标注。 |
| 3. 一致性检查 | 已与相关需求/PRD 对照；冲突与重复已列出。 |
| 4. 可测性与可执行性 | 验收标准可验证；开发/测试可据此执行。 |
| 5. 优先级与范围 | 已与路线图或迭代对齐；依赖与优先级已标注。 |
| 6. 输出评审结论 | 结论区分通过/待澄清/须补充；建议已具体可执行。 |

### 11.4 其余角色

其余角色（前端工程师/后端开发工程师/测试工程师/运维工程师/产品经理/架构师/DBA/安全工程师/可靠性工程师/技术写作、设计评审专家、测试评审专家）可按 11.1 模板补全：**职责说明** 以第 6 节为基础提炼一段话；**SOP** 按该角色典型工作流拆成 5～8 步；**各步骤验收要求** 用表格列出每步的通过条件。可先做评审类与自建 skill 对应角色，再逐步覆盖全部角色；若内容较多，可拆为独立文档 `roles-sop.md` 并在本设计文档中引用。

---

## 12. 最终产出的目录结构（建议）

最终交付的规范为一组**结构化文件**，需兼顾**人可读**与**Agent 可解析**。以下为建议的目录与文件布局，便于版本维护与后续实现「Agent 按阶段/角色自动启用 skill」。

```
规范根目录（.cyber_team/）/
├── README.md                    # 总览、使用约定、与 Agent 的接口说明
├── process/
│   ├── phases.yaml              # 阶段定义（id、名称、产出、顺序）— Agent 解析
│   └── process.md               # 流程说明（人读）
├── roles/
│   ├── roles.yaml               # 角色列表与职责摘要、与阶段对应 — Agent 解析
│   └── sop/                     # 各角色职责说明、SOP、步骤验收（人读 + 可选结构化）
│       ├── code-reviewer.md
│       ├── requirements-reviewer.md
│       └── ...
├── stages/
│   └── *.md                     # 按阶段：该阶段角色、活动、SOP 要点、验收（人读）
│       ├── requirements.md
│       ├── code-review.md
│       └── ...
├── mapping/
│   └── phase-role-skill.yaml    # 阶段→角色→活动→skill 映射 — Agent 必读，用于自动启用
├── acceptance/                  # 可选：按阶段或角色汇总的验收标准（可合并入 stages/roles）
│   └── ...
└── skills/
    ├── manifest.yaml            # skill 清单：名称、来源、适用阶段/角色 — Agent 解析
    └── .cursor/skills/          # 实际安装的 skill 目录（或指向项目 .cursor/skills）
```

**说明**：
- **.cyber_team/process/**：流程与阶段定义；`phases.yaml` 供 Agent 判断当前阶段与顺序。
- **.cyber_team/roles/**：角色定义与详细 SOP/验收；`roles.yaml` 供 Agent 解析角色与阶段关系。
- **stages/**：按阶段汇总的职责、活动、验收，与人读的流程文档一致（可置于人类手册或 .cyber_team 下）。
- **.cyber_team/mapping/**：`phase-role-skill.yaml` 为核心映射，Agent 据此在给定阶段/角色下加载对应 skill。
- **.cyber_team/skills/**：`manifest.yaml` 列出 skill 名称、来源（GitHub 或本地路径）、对应阶段/角色；实际 skill 文件可放在 `.cursor/skills/` 或由 manifest 引用。

**与已有 skill 的关系**：本规范**不与已有 skill 合并**，单独形成上述目录结构；项目内已有的 skill（如原 skill 目录下的内容）保持独立，原 skill 目录已更名以区分。规范中的 `.cyber_team/skills/` 仅承载本方案选型与自建的 skill，不引用或合并既有目录。

**自建 skill 落地顺序**：按**软件开发阶段顺序**（第 3 节）依次落地：需求阶段所需自建（如 prd-requirements）→ 需求评审阶段（requirements-review、prd-review 等）→ 架构/设计（architecture-design）→ 设计/架构评审（architecture-review）→ 开发阶段所需已多为采纳 skill，可补缺 → 代码评审、测试已有采纳 → 测试评审（test-plan-review）→ 部署/发布（devops-cicd）→ 运维/复盘（sre-reliability）。同一阶段内自建项可再按依赖或优先级细排。

**规范根目录的放置位置**：规范根目录的**放置位置**由项目/团队约定，例如：当前仓库下的子目录（如 `./team-norms/`）、独立仓库、或与代码库平级的目录。约定后应在 README 或配置中写明，便于 Agent 与人工统一定位。

**进展/状态的表示与存储**：为实现「Agent 决定并记录当前阶段与进展」，需定义**进展/状态的表示方式与存储位置**，供 Agent 读写。建议：将运行态状态文件放在**业务项目仓库**（如根目录 `state.yaml` 或 `.agent/state.yaml`），字段可包含：`current_phase`（当前阶段 id，与 phases.yaml 的 id 一致，建议与第 3 节「英文标识」一致）、`completed_phases`（已完成阶段列表）、`current_role`（当前启用的角色，可选）、`updated_at`（最后更新时间）。规范库侧仅提供 schema 与初始化模板（如 `.cyber_team/process/state.yaml`）；单仓模式下业务项目内自带 `.cyber_team` 快照，无需多根工作区。

**阶段转换规则**：何时进入下一阶段（如验收满足、用户确认、产出物就绪等）**待落地时约定**；约定后可在 process 或 README 中写明，供 Agent 与人工一致执行。

**Agent 用 YAML 约定（草案）**：以下为供 Agent 解析的 YAML 文件**字段约定草案**，落地时可增删或细化。

| 文件 | 建议字段 | 说明 |
|------|----------|------|
| **.cyber_team/process/phases.yaml** | `phases`: 列表，每项含 `id`, `name`, `outputs`, `order` | `id` 建议与第 3 节「英文标识」一致（如 requirements, design, code-review），与 mapping 及 state 中 current_phase 一致；`order` 用于阶段顺序与推进判断 |
| **.cyber_team/roles/roles.yaml** | `roles`: 列表，每项含 `id`, `name`, `summary`, `phase_ids` | `phase_ids` 为该角色参与的阶段 id 列表，与 mapping 对应 |
| **.cyber_team/mapping/phase-role-skill.yaml** | `mappings`: 列表，每项含 `phase_id`, `role_id`, `activity`, `skill_id` 或 `skill_name` | 给定 phase_id（及可选 role_id）可查得应加载的 skill；skill_name 与 manifest 对应 |
| **.cyber_team/skills/manifest.yaml** | `skills`: 列表，每项含 `id`/`name`, `source`（GitHub URL 或本地路径）, `phase_ids`/`role_ids` | Agent 根据 mapping 得到的 skill 名/id 在此解析出实际加载路径或引用 |

**后续落地**：可先产出 `.cyber_team/process/phases.yaml`、`.cyber_team/mapping/phase-role-skill.yaml`、`.cyber_team/skills/manifest.yaml` 及状态文件 schema，再按阶段顺序逐步补全自建 skill；Agent 侧需实现「读取状态文件与 mapping → 决定当前阶段/角色 → 加载 manifest 中对应 skill」的逻辑。

---

## 13. 附录

### 13.1 SkillsMP 工具与安全门槛

- **SkillsMP 工具**：skillsmp_search（关键词）、skillsmp_ai_search（语义）、skillsmp_scan_skill（安全扫描）、skillsmp_compare（二选一对比）、skillsmp_search_safe（检索+扫描）。使用前需在 Cursor 的 MCP 配置中设置 SkillsMP 的 API Key（参见 skillsmp.com 或 MCP 服务说明）。
- **安全门槛**：仅采纳无 Critical 风险的 skill。若 MCP 扫描因 URL 格式等原因无法执行，或需二次核验，可进行**人工确认**。

### 13.2 人工确认 skill 安全的步骤与检查清单

当某 skill 未通过 SkillsMP 自动扫描（如仓库为根目录 SKILL.md、或扫描失败）时，可按以下步骤人工确认后再决定是否安装。

**第一步：获取代码**

- 在浏览器打开该 skill 的 GitHub 仓库（如 `https://github.com/sanyuan0704/code-review-expert`）。
- 或本地执行：`git clone https://github.com/owner/repo.git`，进入仓库目录查看。

**第二步：确认要看的范围**

- 必看：**SKILL.md**（或仓库根目录下作为 skill 入口的 Markdown）。
- 若有 **references/**、**scripts/**、**templates/** 等子目录，一并打开（恶意逻辑常藏在子目录或脚本中）。
- 若有 **package.json**、**requirements.txt** 等依赖声明，扫一眼依赖是否常见、来源是否可信。

**第三步：按检查清单逐项看**

在 SKILL.md 与上述文件中，重点排查：

| 检查项 | 说明 | 若发现则视为高风险 |
|--------|------|---------------------|
| **Prompt 注入 / 角色扮演** | 是否包含“忽略上述指令”“扮演某角色”“永远服从”等试图劫持 AI 行为的表述；或异常 Unicode/ homoglyph 字符（视觉混淆）。 | 是 → 不采纳或需删改后自用 |
| **修改 CI/CD 或流水线** | SKILL 是否指导 AI 去**修改** GitHub Actions / GitLab CI / Jenkins 等流水线或部署脚本。 | 是 → 视为 supply-chain 类风险，慎用 |
| **执行任意命令或脚本** | 是否要求 AI 执行未写明的外部命令、下载并运行脚本、或 `curl \| sh` 等。 | 是 → 不采纳 |
| **敏感信息与权限** | 是否要求写入环境变量、密钥、或高权限路径；是否要求访问网络/API 且未说明用途。 | 视用途判断；不明则慎用 |
| **恶意代码模式** | 是否包含明显恶意逻辑（反向 shell、挖矿、窃取凭证、篡改系统文件等）。 | 是 → 不采纳 |
| **子目录未扫** | references/、scripts/ 等若未在网页上逐文件打开看过，视为“未确认”，可标注为“安装后仅使用 SKILL.md 主逻辑、不执行未确认脚本”。 | 可选：标注风险并限制使用范围 |

**第四步：做结论**

- **通过**：未发现上表高风险项，且子目录内容已确认或已接受“仅用主 skill、不执行未确认脚本” → 可安装。
- **不通过**：存在任一“不采纳”级问题 → 不安装；若仅“慎用”项，可记录并限制使用场景后再决定。
- **存疑**：无法判断时，可先不安装，或仅在隔离环境/小范围试用。

**第五步：安装与后续**

- 安装后建议保留**仓库链接与本次确认结论**（如“已人工确认 SKILL.md + references，未发现 Critical，202x-xx-xx”），便于后续追溯。
- 若仓库后续有更新，重要变更后可重新做一次人工确认或再次尝试 MCP 扫描。

**针对 code-review-expert（sanyuan0704）**：该仓库为根目录 SKILL.md + `references/`（solid/security/code-quality checklist、removal-plan）及 `agents/`。**已人工确认安全，可放心安装。**
