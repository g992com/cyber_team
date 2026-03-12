---
description: 项目文档索引与阶段产出物发现 — 先读 project-docs-index.yaml 再按路径读具体文档
alwaysApply: true
---

# 项目文档索引与产出物发现

本项目采用 **cyber_team 流程** 管理阶段产出物。智能体在读写需求、设计、测试、发布等文档时，必须通过**项目文档索引**定位路径，再按路径读取或更新具体文档。

## 必读索引

- **索引文件路径**：项目 **docs 目录**下的 `project-docs-index.yaml`（即 `docs/project-docs-index.yaml`；若项目约定放在其他路径，以项目约定为准）。
- **何时读取**：在需要发现或引用某阶段的产出物（如 PRD、用户故事、架构文档、测试计划、发布说明等）时，**先读取** `docs/project-docs-index.yaml`，根据阶段 id 或任务目标找到对应条目，再按条目中的相对路径读取具体文档。
- **路径含义**：索引中的路径均为相对于索引文件所在目录的相对路径；不存在的路径表示该产出尚未创建。

## 索引结构说明

- 第一层 key 为**阶段 id**（如 `requirements`、`design`、`testing`），与流程阶段一致。
- 每个阶段下列出该阶段产出物类型与路径（如 `prd`、`user_stories`、`architecture`、`test_plan` 等）。
- 若**业务项目**中有 `state.yaml` 且包含 `current_phase`，可优先查看当前阶段对应的索引区块，再按需查看其他阶段（避免在多根工作区中误读规范仓库的示例 `state.yaml`）。

## 使用流程

1. 读取 `docs/project-docs-index.yaml`，确定目标阶段与产出物类型对应的文件路径。
2. 按路径读取具体文档；若文档含 YAML frontmatter（`phase`、`type`、`status`、`owner_role`、`updated_at`），可解析以判断状态与责任角色。
3. 写入或更新产出物时，仍按索引中约定的路径创建/更新文件，并保持 frontmatter 与 `artifact-metadata-convention` 一致（若项目采用该约定）。

## 注意

- 未在索引中列出的路径，不应默认视为流程规定的产出物路径。
- 索引文件可从本规范仓库的 `process/project-docs/project-docs-index.yaml` 复制到业务项目 **docs 目录**后，按实际产出填写或新增路径。
