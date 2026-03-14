# 模板与清单索引

业务项目初始化时，可在规范库中按下列路径获取模板或参考，并在**业务项目**中创建对应资产。规范库为唯一事实来源；业务项目**不复制**阶段/角色/映射定义，仅创建项目特有的 state、文档索引与产出物路径。

| 规范库路径 | 业务项目落点 | 说明 |
|------------|--------------|------|
| `process/state.yaml` | 业务项目**根目录** `state.yaml` | 进展状态模板；复制后**更新必须**通过业务项目 `scripts/update_state.py`（见下），不可直接编辑 |
| `process/project-docs/status/update_state.py` | 业务项目 `scripts/update_state.py` | 更新 state 的脚本（init / set-phase / add-completed / set-tailoring / add-blocker / add-risk）；业务项目**必须**配置，所有对 state.yaml 的写入均通过此脚本 |
| `process/project-docs/project-docs-index.yaml` | 业务项目 `docs/project-docs-index.yaml` | 项目文档索引；复制后按实际产出填写各阶段文档路径 |
| `process/project-docs/status/role-status.md` | 业务项目 `docs/status/{role_id}.md` | 角色进展日志模板；按角色复制并重命名 |
| `process/project-docs/status/project-manager.md` | 业务项目 `docs/status/project-manager.md` | 项目经理进展日志模板 |
| `docs/process-tailoring.md` | 业务项目 `docs/process-tailoring.md` | 由项目启动阶段产出，记录裁剪理由与适用条件（不复制规范库内容） |
| `rules/project-docs-discovery.md` | 业务项目 `.cursor/rules/` 下 | 文档发现规则，供智能体先读 project-docs-index 再按路径读文档 |

**说明**：阶段定义、角色、映射等见规范库 `process/phases.yaml`、`roles/roles.yaml`、`mapping/phase-role-skill.yaml`；业务项目通过引用规范库（如多根工作区）使用，不复制上述文件。规范库人类向说明文档（流程说明、阶段说明、角色 SOP 等）见 `人类手册/` 目录。
