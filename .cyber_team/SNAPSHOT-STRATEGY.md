# `.cyber_team` 快照与 `.cursor` 生成策略

本文约定新建业务项目时，如何从规范库复制规范快照到业务项目 `.cyber_team/`，以及如何从 `.cursor-templates/` 生成业务项目的 `.cursor/`。

## 1. 要复制的规范子集（进入业务项目 `.cyber_team/`）

- **process/** — 流程与阶段定义、产出物约定、state 模板、project-docs 模板等（不含仅人类手册用途的说明）。
- **roles/** — roles.yaml 及角色定义。
- **mapping/** — phase-role-skill.yaml 等映射。
- **skills/** — 自建 skill 的 SKILL.md 及子目录（规范库中 `skills/manifest.yaml` 里 `source: ./xxx` 的本地 skill）；外部采纳的 skill（GitHub 等）不拷贝到快照，由业务项目按 manifest 引用或按需安装。
- **rules/** — 规范规则（如 role-boundary-and-intent-confirmation.md、project-docs-discovery.md），供规范内引用与可选复制到 `.cursor/rules/`。
- **CONVENTIONS-paths-and-links.md** — 路径与逻辑链接约定（必须保留）。
- **不复制**：`人类手册/`（仅供规范库侧人类阅读，不进入业务项目快照）。

## 2. SNAPSHOT 元数据格式

在业务项目 `.cyber_team/SNAPSHOT.yaml` 中必须包含：

```yaml
source_repo: cyber_team   # 或实际仓库名
source_commit: "<git sha>"
generated_at: "<ISO8601>"
notes: ""                # 可选：裁剪说明、补丁说明等
```

生成快照时由脚本或人工填入 `source_commit` 与 `generated_at`。

## 3. 从 `.cursor-templates` 生成业务项目 `.cursor/`

1. **rules**  
   - 将 `.cursor-templates/rules/*.mdc.tpl` 复制到业务项目 `.cursor/rules/`，文件名去掉 `.tpl` 后缀（即 `xxx.mdc.tpl` → `xxx.mdc`）。  
   - 可选：同时复制 `.cyber_team/rules/*.md` 到 `.cursor/rules/` 并改为 `.mdc`（兼容未迁移到模板的规则）。

2. **skills**  
   - 将 `.cursor-templates/skills/` 下各 skill 子目录（含其 SKILL.md 入口）复制到业务项目 `.cursor/skills/`，保持目录结构。  
   - 业务项目可在此基础上增删或覆盖为自定义 skill。

## 4. 推荐初始化顺序

1. 在业务项目根目录创建 `.cyber_team/`。
2. 从规范库复制上述子集到 `.cyber_team/`（process、roles、mapping、skills、rules、CONVENTIONS）。
3. 在 `.cyber_team/` 下写入 `SNAPSHOT.yaml`（含 source_repo、source_commit、generated_at）。
4. 在业务项目根目录创建 `.cursor/rules/`、`.cursor/skills/`，从 `.cursor-templates/` 按上节生成内容。
5. 按需复制 docs 索引、state 模板、update_state 脚本等（由初始化脚本完成；本文件不再引用人类手册路径）。

## 5. 规范库目录说明

规范库中：**智能体依赖的规范**（process、roles、mapping、skills、rules）位于 `.cyber_team/` 下；**人类手册**（`人类手册/`）位于仓库根，仅供人读，不随规范快照复制到业务项目。复制到业务项目时，将 `.cyber_team/` 下的 process、roles、mapping、skills、rules 及约定文档复制到**业务项目**的 `.cyber_team/` 下，使业务项目内规范根统一为 `.cyber_team/`。
