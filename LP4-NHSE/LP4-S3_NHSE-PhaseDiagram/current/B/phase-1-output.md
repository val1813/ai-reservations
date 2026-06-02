# B博士 Phase 1 — 单层相图反例审查

## 核心攻击

LP4-S3 如果试图把 LP4-S1 与 LP4-S2 合成一个单层相图，会犯层级混淆。

## 反例 1：母框架成立不推出填充率诊断量子化

LP4-S1 的母框架是结构层结果，说明 Lindbladian 与 postselected 描述可放进同一扩展空间。

但 LP4-S2 已证明 DR-NHDD：

- 依赖 freeze 规则
- 依赖 PBC/OBC
- 依赖 sector
- 不自然量子化

因此 `M=1` 不能推出 `R` 轴上的拓扑不变量。

## 反例 2：DR-NHDD 分段不推出方向反转机制

低填充率正、高填充率负的 DR-NHDD 分段可以是动力学诊断结果，不必来自非局域 jump operator 的方向反转机制。

因此 `R_low/R_high` 不能倒推出 `M=1`。

## 反例 3：OBC 有限尺寸会伪造相图边界

LP4-S1 已有 γ_c 标度审计：

母空间方向反转在 OBC 有限尺寸下可被边界 resolvent 放大，热力学极限下边界主导窗口收缩。

因此任何包含 `B_obc` 的相图边界都不能写成 bulk 相变线。

## 建议相图格式

不能做单层相图。应做三层：

1. `structural map`：母框架/非局域 jump 是否可用。
2. `diagnostic map`：DR-NHDD 的填充分段。
3. `boundary map`：OBC/finite-size/实现约束。

## B侧判定

Phase 1 允许通过，但主结论必须降调：

LP4-S3 的目标不是“找到统一拓扑相图”，而是“建立多层级相图，说明单一不变量为什么失败以及哪些诊断仍可用”。
