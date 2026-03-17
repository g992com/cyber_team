# 试点验证说明（单仓 + `.cyber_team` + `.cursor-templates`）

## 验证结论

已使用规范库内 `人类手册/scripts/setup_business_project.py` 对**试点业务项目**执行初始化，确认：

- **`.cyber_team/` 快照**：包含 `process/`、`roles/`、`mapping/`、`skills/`、`rules/`、`CONVENTIONS-paths-and-links.md`、`SNAPSHOT-STRATEGY.md` 及 `SNAPSHOT.yaml`（含 source_repo、source_commit、generated_at）。
- **`.cursor/` 从模板生成**：`.cursor/rules/` 下存在由 `.cursor-templates/rules/*.mdc.tpl` 生成的 `.mdc` 规则；`.cursor/skills/` 下存在由 `.cursor-templates/skills/` 复制的各 skill 入口目录。
- **其余初始化**：`docs/project-docs-index.yaml`、`state.yaml`、`scripts/update_state.py`、任务板等按原脚本逻辑正常生成。

智能体在**仅打开该业务项目仓库**时，应以本仓 `.cyber_team/` 为规范根、以 `.cursor/rules/` 与 `.cursor/skills/` 为入口，无需多根工作区。

## 复现步骤

1. 在规范库根目录外或内创建空业务项目目录，例如：`pilot-business-project`。
2. 执行：`python 人类手册/scripts/setup_business_project.py <业务项目根目录绝对路径>`。
3. 检查业务项目根下是否生成 `.cyber_team/`、`.cursor/`、`docs/`、`scripts/`、`state.yaml`。
4. 用 Cursor 仅打开该业务项目仓库，验证规则与 skill 路径解析（如读取 `.cyber_team/process/phases.yaml`、执行 skill 时先读 `.cyber_team/skills/<id>/SKILL.md`）。

## 试点目录

- 仓库内 `pilot-business-project/` 为早期试点目录，已通过 `.gitignore` 忽略提交。
- 本次（2026-03-17）对 `D:\my_ai_project\tt_test_cases` 执行初始化并验证通过。
