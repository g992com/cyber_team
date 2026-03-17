# 模板与清单索引

业务项目初始化时，可在规范库中按下列路径获取模板或参考，并在**业务项目**中创建对应资产。规范库为唯一事实来源；业务项目**不复制**阶段/角色/映射定义，仅创建项目特有的 state、文档索引与产出物路径。

| 规范库路径 | 业务项目落点 | 说明 |
|------------|--------------|------|
| `.cyber_team/process/state.yaml` | 业务项目**根目录** `state.yaml` | 进展状态模板；复制后**更新必须**通过业务项目 `scripts/update_state.py`（见下），不可直接编辑 |
| `.cyber_team/process/project-docs/status/update_state.py` | 业务项目 `scripts/update_state.py` | 更新 state 的脚本（init / set-phase / add-completed / set-tailoring / add-blocker / add-risk）；业务项目**必须**配置，所有对 state.yaml 的写入均通过此脚本 |
| `.cyber_team/process/project-docs/project-docs-index.yaml` | 业务项目 `docs/project-docs-index.yaml` | 项目文档索引；复制后按实际产出填写各阶段文档路径 |
| `.cyber_team/process/project-docs/status/role-status.md` | 业务项目 `docs/status/{role_id}.md` | 角色进展日志模板；按角色复制并重命名 |
| `.cyber_team/process/project-docs/status/project-manager.md` | 业务项目 `docs/status/project-manager.md` | 项目经理进展日志模板 |
| （由项目启动阶段产出） | 业务项目 `docs/process-tailoring.md` | 记录裁剪理由与适用条件，不复制自规范库 |
| `.cursor-templates/rules/project-docs-discovery.mdc.tpl` 或 `.cyber_team/rules/project-docs-discovery.md` | 业务项目 `.cursor/rules/` 下（.mdc） | 文档发现规则，供智能体先读 project-docs-index 再按路径读文档 |
| `.cursor-templates/rules/role-boundary-and-intent-confirmation.mdc.tpl` 或 `.cyber_team/rules/role-boundary-and-intent-confirmation.md` | 业务项目 `.cursor/rules/` 下（.mdc） | 角色边界与意图/需求确认，执行任何角色时须遵守 |

**说明**：业务项目以本仓 `.cyber_team/` 为规范根（可从规范库复制快照并附带 SNAPSHOT.yaml）；阶段定义、角色、映射等见 `.cyber_team/process/phases.yaml`、`.cyber_team/roles/roles.yaml`、`.cyber_team/mapping/phase-role-skill.yaml`。规则与 skill 入口从规范库 `.cursor-templates/` 复制到业务项目 `.cursor/` 后生效。规范库人类向说明文档见 `人类手册/` 目录（仅供人读，不随规范快照复制）。

