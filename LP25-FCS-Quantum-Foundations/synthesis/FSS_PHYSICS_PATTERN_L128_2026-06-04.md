# FSS Physics Pattern at Lmax=128

**Date:** 2026-06-04
**Inputs:** `fss_gamma0.1_L128_combined.json`, `fss_gamma0.5_L128.json`, `fss_gamma1.0_L128.json`, `fss_gamma2.0_L128.json`

## 1. 主要物理图像

L=128 后，原来的“β 在全 α 区间单调下降”不是最稳定的物理规律。更稳定的图像是：

> β(α,γ_phi) 随 α 先从 long-range boundary-dominated sector 下降，随后流入一个 γ_phi 控制的 near-diffusive plateau。  
> plateau 的位置随 γ_phi 增大向 β≈1 靠近。

这不是为了证明旧稿一定对；这是大 L 数据自己显露出来的结构。

## 2. L>=32 指数表

| γ_phi | α=1.1 | α=1.3 | α=1.5 | α=1.7 | α=1.9 | 物理形状 |
|:--:|--:|--:|--:|--:|--:|:--|
| 0.1 | 1.0548 | 0.9915 | 0.8987 | 0.8075 | 0.7682 | weak-dephasing crossover, still descending |
| 0.5 | 1.1279 | 0.9587 | 0.8833 | 0.8884 | 0.9132 | minimum near α≈1.5, then plateau/rebound |
| 1.0 | 1.1038 | 0.9639 | 0.9251 | 0.9331 | 0.9515 | near-diffusive plateau after α≈1.5 |
| 2.0 | 1.1011 | 0.9884 | 0.9550 | 0.9583 | 0.9719 | stronger approach to β≈1 plateau |

## 3. Consecutive L=64→128 Local β

| γ_phi | α=1.1 | α=1.3 | α=1.5 | α=1.7 | α=1.9 |
|:--:|--:|--:|--:|--:|--:|
| 0.1 | 1.0981 | 1.0167 | 0.8984 | 0.7976 | 0.7801 |
| 0.5 | 1.1160 | 0.9415 | 0.8850 | 0.9045 | 0.9326 |
| 1.0 | 1.0874 | 0.9545 | 0.9274 | 0.9416 | 0.9611 |
| 2.0 | 1.0857 | 0.9793 | 0.9533 | 0.9609 | 0.9757 |

The local exponent confirms the plateau/rebound at γ_phi >= 0.5. The large-L trend is not random finite-size noise; it repeats across γ_phi = 0.5, 1.0, 2.0.

## 4. Revised Physical Claim

The robust claim should not be:

> β decreases monotonically with α across the entire scanned interval.

The stronger physical claim is:

> Long-range hopping creates an enhanced boundary-coherence decay sector at small α. As α increases, β flows downward until the system enters a near-diffusive coherence plateau. The plateau value is controlled by γ_phi and approaches β≈1 as dephasing strengthens.

This preserves the second-exponent discovery while replacing an over-simple one-curve story with a flow/plateau structure.

## 5. Consequence for Manuscript

Needed changes:

1. Replace “β decreases monotonically from α=1.1 to α=1.9” with “β descends from the long-range regime and crosses into a γ_phi-dependent near-diffusive plateau.”
2. Treat α≈1.5 as a coherence-sector minimum/crossover, not simply as a point on a monotone line.
3. Keep `1/α` as the small-to-intermediate α leading coordinate, but do not force it onto the large-α plateau.
4. Use γ_phi=0.1 as weak-dephasing crossover evidence, not as the main scaling window.
5. Stop trying to run γ_phi=0.01 at L=128 on local CPU unless specifically targeting the ballistic limit; it is computationally slow and lower value for the current PRL claim.

## 6. Compute Status

Completed:

- `γ_phi=0.1`, Lmax=128, all α, combined from partial group + single α=1.9 completion.
- `γ_phi=0.5`, Lmax=128, all α.
- `γ_phi=1.0`, Lmax=128, all α.
- `γ_phi=2.0`, Lmax=128, all α.

Not completed:

- `γ_phi=0.01`, Lmax=128. A single α=1.5 run exceeded 15 minutes and was stopped. This regime is the ballistic/near-constant-β limit and is not the highest-value target for the current scaling claim.

## 7. L=256 Anchor Update for γ_phi=0.5

**Date:** 2026-06-05
**Inputs:** `fss_gamma0.5_L256.json`, `fss_gamma0.5_L256_raw.json`

Five L=256 anchor points were computed by reusing the L<=128 data and adding only L=256. Runtime per L=256 point on local CPU:

| α | L=256 runtime | |C_mid(256)| |
|:--:|--:|--:|
| 1.1 | 12.7 min | 1.880190e-04 |
| 1.3 | 19.0 min | 3.748596e-04 |
| 1.5 | 19.8 min | 5.549012e-04 |
| 1.7 | 21.3 min | 6.445630e-04 |
| 1.9 | 23.6 min | 6.777337e-04 |

Updated exponent table:

| α | β(L>=32) | β(L>=64) | local β(64→128) | local β(128→256) |
|:--:|--:|--:|--:|--:|
| 1.1 | 1.1162 | 1.1045 | 1.1160 | 1.0929 |
| 1.3 | 0.9472 | 0.9339 | 0.9415 | 0.9262 |
| 1.5 | 0.8901 | 0.8952 | 0.8850 | 0.9054 |
| 1.7 | 0.9040 | 0.9198 | 0.9045 | 0.9351 |
| 1.9 | 0.9291 | 0.9463 | 0.9326 | 0.9599 |

Interpretation:

- L=256 strengthens the flow/plateau picture rather than the old monotonic picture.
- α=1.1 and α=1.3 continue drifting downward but remain high-to-intermediate.
- α=1.5 is the approximate minimum / crossover point.
- α=1.7 and α=1.9 continue upward toward a near-diffusive plateau.
- The robust statement is now: at γ_phi=0.5, large-L β forms a U-shaped / crossover-to-plateau profile, not a globally monotone 1/α curve.

Manuscript consequence:

The main text should stop using the γ_phi=0.5 table as evidence for global monotonic α-dependence. It should instead present β as a second coherence-sector exponent whose large-L flow has two regimes:

1. long-range boundary-dominated decay for small α;
2. near-diffusive coherence plateau for larger α.
