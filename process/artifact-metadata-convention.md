# 产出物元数据约定

本约定用于多智能体协作：通过文档头部的可机读元数据，让 Agent 快速发现当前阶段产出、评审状态与责任角色，便于衔接与消费。

## 适用范围

- **适用文档**：各阶段的主要产出物（PRD、架构设计、ADR、测试计划、发布说明等）。代码与配置文件可不带元数据。
- **放置位置**：Markdown 或其它支持 YAML frontmatter 的文档，在正文前用 `---` 包裹一段 YAML。

## 标准字段

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `phase` | string | 是 | 阶段 id，与 `process/phases.yaml` 的 `phases[].id` 一致，如 `requirements`、`design`、`testing`。 |
| `type` | string | 是 | 产出物类型，便于过滤与索引，如 `prd`、`architecture`、`adr`、`test-plan`、`release-notes`。 |
| `status` | string | 是 | 生命周期状态：`draft`（草稿）、`in-review`（评审中）、`approved`（已通过）。 |
| `owner_role` | string | 建议 | 负责该文档的角色 id，与 `roles/roles.yaml` 的 `roles[].id` 一致，如 `product-requirements`、`architect`。 |
| `updated_at` | string | 建议 | 最后更新时间，ISO 8601 日期或日期时间，如 `2026-03-09` 或 `2026-03-09T14:00:00Z`。 |

## 可选字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | string | 文档标题，便于展示与检索。 |
| `version` | string | 文档版本号，如 `1.0`、`v2`。 |
| `replaces` | string | 若替代某旧文档，可写旧文档相对路径。 |
| `related` | array of string | 关联文档路径列表，如关联的 ADR、API 文档。 |

## 阶段与 type 建议

| phase | 建议 type 示例 |
|-------|----------------|
| initiation | `project-plan`, `process-tailoring`, `phase-activity-list`, `charter-summary` |
| requirements | `prd`, `user-stories`, `acceptance-criteria`, `backlog` |
| requirements-review | `review-record` |
| design | `architecture`, `api-spec`, `database-design`, `adr` |
| design-review | `review-record` |
| development | `module-design`, `dev-guide`（可选） |
| code-review | `review-record` |
| testing | `test-plan`, `test-cases`, `test-report` |
| test-review | `review-record` |
| deployment | `release-notes`, `rollback-plan`, `deploy-guide` |
| operations | `runbook`, `postmortem`, `slo-report` |

## 示例

**PRD（需求阶段）**

```yaml
---
phase: requirements
type: prd
status: approved
owner_role: product-requirements
updated_at: "2026-03-09"
title: "智能体协作平台 V1 产品需求说明"
---
# 产品需求文档
...
```

**架构设计（设计阶段）**

```yaml
---
phase: design
type: architecture
status: in-review
owner_role: architect
updated_at: "2026-03-09T10:00:00Z"
related:
  - docs/design/adr/001-service-split.md
---
# 系统架构设计
...
```

**ADR**

```yaml
---
phase: design
type: adr
status: approved
owner_role: architect
updated_at: "2026-03-08"
title: "ADR-001 服务拆分策略"
---
# ADR-001 服务拆分策略
...
```

## Agent 使用方式

1. **发现当前阶段产出**：根据**业务项目** `state.yaml` 的 `current_phase`，在项目文档索引（`docs/project-docs-index.yaml`）中找到对应路径，读取文档并解析 frontmatter 的 `phase`、`type`、`status`。
2. **判断是否可消费**：若下游阶段依赖该产出，可检查 `status == approved` 再继续。
3. **阶段是否可推进**：阶段出口条件见 `process/exit-criteria.yaml`；满足该阶段 required_artifacts 与 key_status（或用户确认）后可推进到下一阶段。
4. **责任角色**：`owner_role` 可用于提示应由哪类角色维护或评审该文档。

## 与项目文档索引的关系

- **元数据**：写在单篇文档内部，描述该文档自身。
- **项目文档索引**：写在项目 **docs 目录**或约定路径的 `project-docs-index.yaml`（默认 `docs/project-docs-index.yaml`），列出各阶段产出物的**路径**，供 Agent 快速定位文档，再结合文档内元数据解析状态与角色。

两者配合使用：先查索引获路径，再读文档取元数据。
