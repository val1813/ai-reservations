# B博士 Phase 2 — 边界分类攻击

## 攻击目标

检查 A 侧边界分类是否仍然偷换“诊断线”为“相变线”。

## 攻击 1：T2 不是无条件 bulk 线

非局域 jump 方向反转线依赖 `L_j=sqrt(G)(c_j+i c_{j+1})`。如果物理实现只在窄相位窗口成立，`gamma_c` 不是完整相图的普适边界，而是工程约束下的条件线。

判定：

T2 必须写成 `conditional T-line`。

## 攻击 2：D1/D2 不能决定 NHSE 存活

DR-NHDD 的符号分段只能说明方向性诊断量变化，不能直接说明 NHSE 作为谱/本征态趋肤效应存活或消失。

判定：

D-line 必须标为 “diagnostic boundary”，不能写 “phase boundary”。

## 攻击 3：C-zone 不是附录细节

OBC 有限尺寸、实现约束、原始 QLIF 未重算不是小误差。它们决定相图是否能被实验/数值读成 bulk 结果。

判定：

C-zone 必须出现在主图或主文本，不能只放在 supplement。

## B侧裁决

允许 Phase 2 通过，条件是：

1. T/D/C 三类边界在术语上永久分离。
2. 完整相图标题不能叫“topological phase diagram”，应叫“multi-layer survival/suppression map”。
3. 不能声称 LP4 已得到统一拓扑不变量。
