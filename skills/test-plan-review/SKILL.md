---
name: test-plan-review
description: Reviews test plans, test cases, and test strategy for coverage, boundary cases, and repeatability. Use when reviewing test plan or test cases, or when the user asks for test review.
---

# 测试计划/用例评审

## 评审维度

| 维度 | 检查要点 |
|------|----------|
| **覆盖度** | 需求/场景/边界是否被测试计划或用例覆盖；缺口 |
| **边界与等价类** | 边界值、等价类与异常路径是否考虑 |
| **可重复性** | 用例可重复执行；前置条件与数据依赖明确 |
| **数据与环境** | 测试数据与环境准备；依赖与清理 |
| **可追溯性** | 与需求/设计的追溯；门禁与通过标准明确 |

## 流程

1. **获取测试产物**：测试计划、策略、用例列表或文档。
2. **覆盖度与边界检查**：对照需求与设计；标注未覆盖或弱覆盖项。
3. **用例质量**：边界与等价类、步骤与预期、数据与环境。
4. **输出结论**：覆盖度与可追溯性是否满足；改进建议与优先级。

## 输出要求

评审结论明确；覆盖度与可追溯性满足要求；建议具体可执行。
