# A博士 Phase 2 — 边界区分类

## 分类原则

LP4-S3 的边界不能统一命名为“相变线”。应分为三类：

1. `T-line`：bulk 拓扑/结构相变线。
2. `D-line`：诊断分段线。
3. `C-zone`：有限尺寸、边界条件或实现约束导致的 caveat 区。

## T-line：bulk 结构边界

### T1 局域耗散 no-go 边界

条件：

`L_j = sqrt(gamma) c_j`

结论：

局域耗散不能反转 NHSE 方向。

类别：`T-line/no-go`

### T2 非局域 jump 方向反转线

条件：

`L_j = sqrt(G)(c_j + i c_{j+1})`

bulk 判据：

`gamma_c = 1 - (t_L - t_R)/G`

类别：`T-line/conditional`

边界：依赖非局域 jump operator 的物理实现与相位锁定。

## D-line：诊断分段线

### D1 填充率方向性分段

条件：

DR-NHDD 低填充率多为正，高填充率多为负。

类别：`D-line`

边界：不是拓扑相变；不能写成量子化不变量。

### D2 `rho≈0.75` 过渡带

条件：

DR-NHDD 在中间填充附近受 freeze/PBC/OBC/sector 影响。

类别：`D-line + C-zone`

## C-zone：caveat 区

### C1 OBC 有限尺寸母空间边界区

母空间方向反转在有限 OBC 中可被 boundary-dominated resolvent 放大。热力学极限下该窗口收缩。

类别：`C-zone`

### C2 实现约束区

非局域 jump 需要单一耗散通道相干耦合相邻格点并锁定 π/2 相位。

类别：`C-zone`

### C3 原始 QLIF 未重算区

原始 entropy-flow QLIF 尚未独立重算，不能纳入相图主判据。

类别：`C-zone`

## A侧相图格式

建议论文图分三层：

- Panel A：`T-line` 结构图
- Panel B：`D-line` 诊断图
- Panel C：`C-zone` caveat overlay

核心结论：相图存在，但不是单一拓扑相图，而是多层级边界图。
