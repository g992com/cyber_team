# 多根工作区配置说明

本目录提供 **Cursor / VS Code 多根工作区** 配置模板，用于将**业务项目**与**规范仓库（cyber_team）** 同时打开，使 Skills 与 process/roles/mapping 等规范路径在多会话协作下可用。

## 模板文件

- **cursor-multi-root-workspace.code-workspace.template**  
  Cursor/VS Code 多根工作区配置模板。使用前请复制为 `xxx.code-workspace`（例如放在业务项目根目录或规范仓库根目录），并按下面说明修改 `folders` 中的 `path`。

## 如何填写 path

模板中两个 `folders` 条目含义如下：

| 条目 | name       | path 说明 |
|------|------------|-----------|
| 第一个 | 业务项目   | 业务项目仓库的根目录。若将复制后的 `.code-workspace` 放在**规范仓库内**，可写相对路径（如 `../my-app`）或绝对路径；若放在**业务项目内**，此处填 `.` 表示当前项目。 |
| 第二个 | cyber_team 规范 | 规范仓库（cyber_team）的根目录。若将 `.code-workspace` 放在**规范仓库内**，此处填 `.`；若放在**业务项目内**，填规范仓库的相对路径（如 `../cyber_team`）或绝对路径。 |

**示例（模板放在规范仓库内）**：业务项目在 `../my-app`，规范仓库为当前目录，则第一个 path 改为 `../my-app`，第二个为 `.`。

**示例（.code-workspace 放在业务项目内）**：第一个 path 填 `.`，第二个填 `../cyber_team`（或你的规范仓库路径）。

## 使用步骤

1. 将 `cursor-multi-root-workspace.code-workspace.template` 复制为 `cyber-team-multi-root.code-workspace`（或任意名称），放到你方便的位置（规范仓库根目录或业务项目根目录）。
2. 用编辑器打开该 `.code-workspace` 文件，按上表修改两个 `path` 为实际路径。
3. 在 Cursor 中：**文件 → 打开工作区来自文件**，选择该 `.code-workspace` 并打开。
4. 打开后，工作区应显示两个根（业务项目、cyber_team 规范）。多会话方案中的 pinned prompt 所写的 `process/`、`roles/`、`mapping/`、`skills/` 等路径将相对于规范仓库根解析。

## 业务项目侧仍需准备

- **project-docs-index.yaml**：从本规范仓库 `process/project-docs/project-docs-index.yaml` 复制到业务项目 **docs 目录**（即 `docs/project-docs-index.yaml`），并按阶段填写各产出物路径。
- **state.yaml（业务项目根目录）**：从本规范仓库 `process/state.yaml` 复制到业务项目仓库根目录为 `state.yaml`（或团队约定路径）。多根工作区下更新进展时，务必写入业务项目的 `state.yaml`，不要写错仓库。
- **可选：用脚本更新 state**：将本规范仓库 `process/project-docs/status/update_state.py` 复制到业务项目（例如 `scripts/update_state.py`），并在业务项目根目录终端运行它来更新 `state.yaml`（脚本会基于 git root 做防越界校验，减少更新错仓库的风险）。
- **.cursor/rules/**：至少将本规范仓库的 `rules/project-docs-discovery.md` 复制到业务项目的 `.cursor/rules/` 下，使智能体在业务项目中先读索引再读文档。

详见《Cursor-多会话协作落地方案》中「在实际项目中的部署结构」与「Rules 与 Skills 的关联」。
