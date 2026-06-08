# PI 综合 Round 3

## 汇合判断

A/B 汇合为一个可执行 protocol，而不是已成立的新机制。

- A 线: 修复 Hall factor 公式，明确 `mu_D=mu_H/r_H`、`n_true=r_H*n_H`，并把 A1 目标改成独立 `l_reported`、TCR/activation、optical/THz `tau` 或 residual class，避免 `k_F l(mu_H)` 回归同一个 `mu_H`。
- B 线: 将图阈值声张降格为 measurement protocol + reproducible synthetic toy benchmark。P1 方向修正为 mobility/Drude/ridge coherence 随 `z_eff/S_GC` 降低而降低。

## INSPECTOR 状态

- A Round 3: 无阻断。警告: A1 是弱落地；需真实数字化数据；linewidth 每行必须记录 convention；无独立 target 时标 `non-decisive`。
- B Round 3: 无阻断。警告: toy 表内一致但缺 seed-level CSV/脚本/坐标/edge list；controls 尚未应用到外部标签。

## 当前结论

LP29 不应声称“发现非晶带状输运新机制”。当前最诚实的北极星是:

> 构建并执行一个判据比较 protocol：在 Hall factor、linewidth convention、matched `n/E_F-E_c`、onsite variance 和 finite-size controls 下，测试 mobility-edge/Ioffe-Regel 指标与 In-s graph metrics 谁对独立 Hall/Drude/Wannier/spectral observables 有残差预测力。

## 下一步最小实做

1. A1: 数字化 Furubayashi 2019 的 Hall/transport 表，生成 corrected CSV。若独立 `l_reported/TCR/optical tau` 缺失，A1 标 `non-decisive`。
2. B1: materialize toy ensemble script 和 seed-level CSV/edge lists，使 synthetic benchmark 可复现。
3. A2/B2: 查 Jankousky SI 是否有 raw structures/QSGW subset；若无，使用 Aliano 2011 AIMD fallback。

## AHA 检查

本轮 AHA 仍是“mobility edge 可能是 graph spectral projection”。但 REVIEWER 前不注册为新北极星；先接受恶意审稿。
