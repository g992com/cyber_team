---
name: devops-cicd
description: Designs and guides CI/CD pipeline setup, GitHub Actions/GitLab CI, containers and deployment, release strategy. Use when the user mentions CI/CD, pipeline, deployment, Docker, or Kubernetes.
---

# CI/CD 与发布

角色边界与意图/需求确认见 `skills/_common/role-boundary-and-intent-confirmation.md`；本角色仅负责 mapping 规定的本角色产出，不得代做其他角色产出。

## 流水线结构

- **构建**：编译/打包、依赖安装、产物产出。
- **测试**：单元、集成、E2E（按项目约定）；门禁与失败策略。
- **部署**：环境配置、发布步骤、回滚预案。
- **权限与审计**：流水线与环境的访问控制；审计日志。

## 关键要点

| 要点 | 说明 |
|------|------|
| **环境** | 开发/测试/预发/生产等；配置与密钥管理 |
| **发布策略** | 蓝绿、金丝雀、滚动等；与业务与风险匹配 |
| **回滚** | 回滚条件、步骤与验证；可快速回滚 |
| **容器与编排** | Docker 镜像与 K8s/编排（如适用）；资源与探针 |

## 流程

1. **设计流水线**：构建→测试→部署阶段；触发条件与分支策略。
2. **配置环境与权限**：环境变量、密钥、权限与审计。
3. **发布与验证**：发布步骤与健康检查；发布说明更新。
4. **回滚预案**：定义回滚触发与步骤；确保可回滚。

## 验收

流水线可用；发布可回滚；发布说明与变更可追溯。
