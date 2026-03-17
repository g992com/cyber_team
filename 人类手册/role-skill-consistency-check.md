# 角色技能与方案一致性检查

对照 `role-skills-design.md` 第 5 节（角色-活动-技能对照）、第 8 节（推荐安装表）、第 9 节（选型结果）、第 10 节（自建规格），核对各角色技能为**引用（采纳）**还是**自建**是否与方案一致。

## 对照表

| 阶段 | 角色 | 活动 | 方案 skill（名称） | 方案类型 | 当前 .cyber_team/mapping、.cyber_team/skills/manifest | 当前类型 | 一致 |
|------|------|------|-------------------|----------|------------------------|----------|------|
| 需求 | 产品经理 | 用户故事与验收标准 | user-story (razbakov) | 引用 | user-story，source 为 GitHub | 引用 | ✅ |
| 需求 | 产品经理 | PRD/需求文档 | prd-requirements（自建或检索） | 自建 | prd-requirements，source 为 ./prd-requirements | 自建 | ✅ |
| 需求评审 | 需求评审专家 | 用户故事/验收标准评审 | user-story 兼顾 或 requirements-review（自建） | 自建 | requirements-review，source 为 ./requirements-review | 自建 | ✅ |
| 需求评审 | 需求评审专家 | PRD/需求文档评审 | prd-review（自建） | 自建 | prd-review，source 为 ./prd-review | 自建 | ✅ |
| 架构/设计 | 架构师 | 架构与 ADR | architecture-design（自建） | 自建 | architecture-design，source 为 ./architecture-design | 自建 | ✅ |
| 架构/设计 | DBA | 数据模型与迁移 | flyway-migration (martinellich) | 引用 | flyway-migration，source 为 GitHub | 引用 | ✅ |
| 设计/架构评审 | 设计评审专家 | 架构/设计/安全设计评审 | audit-full 可选 或 architecture-review（自建） | 自建（方案为可选采纳或自建，取自建） | architecture-review，source 为 ./architecture-review | 自建 | ✅ |
| 开发 | 前端工程师 | 前端实现 | frontend-design / frontend-style-guide | 引用（二选一或并列） | mapping 用 frontend-design；manifest 含 frontend-design、frontend-style-guide 均为 GitHub | 引用 | ✅ |
| 开发 | 后端开发工程师 | 后端与 API | backend-development (MOODMNKY) | 引用 | backend-development，source 为 GitHub | 引用 | ✅ |
| 开发 | 技术写作 | 文档 | technical-writer (sjungling) | 引用 | technical-writer，source 为 GitHub | 引用 | ✅ |
| 代码评审 | 代码评审专家 | PR/代码审查 | code-review-expert / review-pr / code-review（三选一或并列） | 引用 | mapping 用 code-review-expert；manifest 含 code-review-expert、review-pr、code-review 均为 GitHub | 引用 | ✅ |
| 代码评审 | 代码评审专家 | 实现层安全 | code-review (folio) 与设计/架构评审配合 | 引用 | code-review，source 为 GitHub | 引用 | ✅ |
| 测试 | 测试工程师 | 测试编写与策略 | pytest；可选 testing-patterns | 引用 | pytest，source 为 GitHub（testing-patterns 为可选未入 manifest） | 引用 | ✅ |
| 测试评审 | 测试评审专家 | 测试计划/用例评审 | test-plan-review（自建） | 自建 | test-plan-review，source 为 ./test-plan-review | 自建 | ✅ |
| 部署/发布 | 运维工程师 | CI/CD 与发布 | devops-cicd（自建） | 自建 | devops-cicd，source 为 ./devops-cicd | 自建 | ✅ |
| 运维/复盘 | 可靠性工程师 | 可靠性、监控、复盘 | sre-reliability（自建） | 自建 | sre-reliability，source 为 ./sre-reliability | 自建 | ✅ |
| 架构/设计 | 安全工程师 | 安全与合规要点 | code-review (folio) 与设计/架构评审配合 | 引用 | code-review，source 为 GitHub | 引用 | ✅ |

## 结论

- **所有角色的技能**（自建 vs 引用）与 `role-skills-design.md` 第 5、8、9、10 节**一致**。
- 方案中的「可选」项处理：
  - **设计/架构评审**：方案为「audit-full 可选 或 architecture-review（自建）」；当前采用自建 `architecture-review`，未将 audit-full 列入 manifest，符合「或」的取舍。
  - **testing-patterns**：方案为 pytest 采纳、testing-patterns 可选；当前仅列 pytest，可选未入 manifest，符合方案。
- 方案中「三选一或并列」「二选一或并列」的 skill（代码评审、前端）：mapping 中各选一个主 skill，manifest 中列出全部采纳 skill，Agent 可按需选用，与方案一致。
