# PI 综合 Round 2

## 汇合判断

A/B 继续互补，但声张整体收缩为 measurement protocol。

- A 修复了 Round 1 的落地阻断，给出两个 artifact 蓝图: `A1_Furubayashi2019_digitized_transport.csv` 和 `A2_Jankousky_structure_spectral_join.csv`。
- B 修复了 Round 1 的量纲/归一化/自证循环警告，把图模型拆成 `structure X -> graph metrics M(X)` 与独立观测 `Y`。

## INSPECTOR 结论

### A Round 2

- 原 Q6.5 落地阻断已修复。
- 新阻断: Hall factor 密度换算方向错误。应为 `n_true = r_H*n_H`，即 `n_m3 = n_H_cm3*1e6*r_H`，不是 `/r_H`。
- 警告: A1 是弱落地；避免用由 `mu_H` 计算出的 `k_F l` 再预测同一个 `mu_H`；`tau=hbar/(2*DeltaE)` 需确认 linewidth 定义。

### B Round 2

- 阻断: 无。
- 警告: P1 方向措辞需修；toy 表不是单个离散图实算产物；还没有外部标签或 matched-control residual；controls 需量化；声张缩水需登记。

## 当前最坚固结论

LP29 仍值得推进，但已经不是“提出新物理机制”的强命题，而是一个可证伪 protocol:

> 在 matched carrier density、matched `E_F-E_c`、matched onsite-disorder variance 后，检验结构派生的 In-s graph metrics 是否仍能独立预测 Hall/Drude/Wannier/spectral observables。

## Round 3 摘要

A 必须修复 Hall factor 公式: `mu_D=mu_H/r_H`, `n_true=r_H*n_H`, 因此 `k_F∝r_H^(1/3)`, `tau∝r_H^-1`, `k_F l∝r_H^(-1/3)`。A 还必须避免 `k_F l(mu_H)` 预测 `mu_H` 的循环，改预测 temperature flag、independent `l_reported`、optical `tau` 或 residual class。B 必须修正 P1 方向措辞，并把 toy 表升级为可复现产物: seed/坐标生成规则/边列表或均值方差；给 controls 的量化 pass/fail 标准。

## 矩阵更新

- LP29-S1: 已完成数量级和落地蓝图，但 A 公式需 Round 3 修正。
- LP29-S2: 继续主攻；B 无阻断但需可复现实算。
- 声张保真度: 从“判据/机制”降为“measurement protocol”。影响宽度下降，严谨性上升。
