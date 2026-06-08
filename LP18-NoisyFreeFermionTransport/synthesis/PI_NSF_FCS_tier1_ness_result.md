# PI NSF-FCS Tier 1 NESS Result

## 输入

- Script: `scripts/nsf_fcs_transport_ledger.py`
- Tier 0 split ledgers: `current/plan/nsf_fcs_tier0_split_*.csv`
- Tier 1 NESS ledger: `current/plan/nsf_fcs_tier1_ness_exclusion.csv`

## Tier 0: affinity split sanity

命令族：

`python scripts\nsf_fcs_transport_ledger.py --sector exclusion --L 4,5,6 --alpha 1.0 --m-tail 1000 --affinity-split a --out current\plan\nsf_fcs_tier0_split_a.csv`

`a in {0,0.25,0.5,0.75,1}`。

结果：所有行 valid，`S_T≈2`。pure affinity split 不破坏 equilibrium FDT，符合 Round 5 的判断。

## Tier 1A: NESS density bias

正式命令：

`python scripts\nsf_fcs_transport_ledger.py --sector exclusion --L 4,5,6,7 --alpha 0.5,1.0,1.5 --m-tail 2000 --rho-left 0.4 --rho-right 0.6 --out current\plan\nsf_fcs_tier1_ness_exclusion.csv`

结果：

- rows = 12
- valid = 12
- `S_T=lambda_T''/G_T` 明确偏离 2，并随 L 增大。

## 数值摘要

| alpha | slope(log G_T) | slope(log lambda_T'') | slope(log |S_T-2|) | slope(log |R2|) | S_T range |
|---:|---:|---:|---:|---:|---|
| 0.5 | 0.542296 | 0.543458 | 0.496859 | 1.039155 | 2.004069389..2.005370746 |
| 1.0 | 0.112415 | 0.115432 | 0.542479 | 0.654894 | 2.009584394..2.012976138 |
| 1.5 | -0.247342 | -0.242497 | 0.564290 | 0.316948 | 2.014747978..2.020212280 |

其中 `R2=lambda_T''-2G_T`。

## 判断

Tier 1A 成功把 equilibrium FDT corollary 打开：在 `rho_left=0.4`、`rho_right=0.6` 的 NESS 背景下，`lambda_T''=2G_T` 不再成立，且 `FDT_residual_R2` 出现稳定非零标度。

这给出比原 NSF-FCS-1 更有价值的重写方向：

> NSF-FCS-2: long-jump open exclusion 在 NESS 背景下的 FDT residual scaling：`R2(L)=lambda_T''(L)-2G_T(L)` 是否携带 reservoir-tail / fractional conductance 的新标度？

## 下一步

1. 扩大 NESS 扫描：`rho_left/rho_right` 多组偏置，并加入 `L=8` 作为可承受上限。
2. 加入 non-LDB / activity forcing，对照 NESS residual 与 kinetic residual。
3. 若 residual 斜率稳定，启动新的 A/B 轮，把 NSF-FCS-2 登记为当前最高优先级。
