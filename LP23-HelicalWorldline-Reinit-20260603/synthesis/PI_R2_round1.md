# PI 综合 | LP23-R2 Round1

日期：2026-06-03

## A/B 汇合判断

A/B 框架独立：

- A 路：协变几何光学 + NP/GHP + spinoptics + 本构/非局域电动力学。
- B 路：量子纠错 syndrome 网络 + 多路径一致性 holonomy。

二者没有互读。A 从标准覆盖边界压缩活口；B 从网络 cohomology 给出可计算 toy model。

## Round1 结论

R2 继续存活，但生死线进一步变窄：

> 真空几何光学、`O(1/omega)` spinoptics、局域 `chi^{abcd}` 三支都不能作为 LP23-R2 新 residual。唯一活口是非局域、历史依赖、端点校准不可压缩的 kernel/network residual。

A 路给出唯一活口：

`I_K[Gamma] = [ C_beta F_beta(K_beta; Gamma) - C_beta' F_beta'(K_beta'; Gamma) ] / G_standard`

其中 `Gamma` 不是单条 ray，而是含 caustic/multipath/beam weighting 的 path family；`K` 需使用协变体积测度 `dV_{x'}` 并证明不等价于局域 `chi delta_V`、spinoptics 或已知 nonlocal electrodynamics kernel。

B 路给出可计算过滤器：

- 边 residual `r` 若是 endpoint calibration 的 coboundary，则闭合 cycle syndrome 为零。
- 真候选应满足 `[R] != 0 in H^1(network,O) / standard_model_subspace`。
- 最小数值判据：`I_bridge = ||P_perp r||^2`，其中 `P_perp` 是投影到 endpoint calibration 子空间正交补的投影。

## INSPECTOR

A/B 均警告通过，无阻断。警告已修正：

- A：固定 screen 旋转约定；将非局域积分写成 `dV_{x'}` 并固定 `delta_V` 归一化。
- B：固定 cycle 符号约定；区分 `B r` 与正交投影残差；非交换版本保留 `Omega_Gamma` / `Tr(Omega_Gamma)` / eigenphase，不把 `log` 当全局对象。

## 本地计算

已新增轻量脚本：

`scripts/r2_syndrome_toy.py`

用途：对三节点闭合网络计算 edge residual 是否可由 endpoint calibration 吸收，并输出 cycle syndrome、正交投影残差和 `I_bridge`。

本轮不需要 GPU，也不需要 VPS。

## 下一轮任务

Round2 不应再抽象讨论“桥接结构”。必须把 A 的非局域 `K(x,x')` 活口与 B 的网络 syndrome 合并：

1. A 路：判断 toy `K` 是否只是局域/频散 `chi(omega,k)` 或 Mashhoon kernel 的已知特例。
2. B 路：扩展脚本，把 endpoint calibration、spinoptics template、局域 constitutive template 都作为 design matrix 投影掉，检查 `||P_perp r||`。
3. PI：若脚本和文献都不能留下非零 `I_bridge`，R2 触发硬停止；若留下，进入 Round3 生死检验。

## 当前状态

N=1。未触发硬停止。按 SOP，N<3 且未硬停止，必须进入 Round2。
