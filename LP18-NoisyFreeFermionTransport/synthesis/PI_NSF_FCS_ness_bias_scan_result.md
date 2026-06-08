# PI NSF-FCS-2 NESS Bias Scan Result

## Scope

- Script: `scripts/nsf_fcs_transport_ledger.py`
- Sector: finite-density exclusion
- Observable: `left_transport_current`
- Density pairs: `0.45 -> 0.55`, `0.40 -> 0.60`, `0.35 -> 0.65`
- Sizes: `L=4..8`
- Kernels: `alpha=0.5,1.0,1.5`

All 45 ledger rows are `ROW_VALID`.

## L-Scaling Summary

| rho_left -> rho_right | alpha | slope log G_T | slope log lambda_T'' | slope log \|S_T-2\| | slope log \|R2\| | S_T(L=4) -> S_T(L=8) |
|---|---:|---:|---:|---:|---:|---|
| 0.45 -> 0.55 | 0.5 | 0.540150 | 0.540432 | 0.469129 | 1.009278 | 2.001016582 -> 2.001407733 |
| 0.45 -> 0.55 | 1.0 | 0.108196 | 0.108931 | 0.512462 | 0.620658 | 2.002388631 -> 2.003408468 |
| 0.45 -> 0.55 | 1.5 | -0.253428 | -0.252250 | 0.532147 | 0.278719 | 2.003663527 -> 2.005299446 |
| 0.40 -> 0.60 | 0.5 | 0.539783 | 0.540912 | 0.469479 | 1.009263 | 2.004069389 -> 2.005636541 |
| 0.40 -> 0.60 | 1.0 | 0.106379 | 0.109329 | 0.514271 | 0.620650 | 2.009584394 -> 2.013693643 |
| 0.40 -> 0.60 | 1.5 | -0.257559 | -0.252803 | 0.536279 | 0.278720 | 2.014747978 -> 2.021394777 |
| 0.35 -> 0.65 | 0.5 | 0.539171 | 0.541710 | 0.470088 | 1.009259 | 2.009167113 -> 2.012702794 |
| 0.35 -> 0.65 | 1.0 | 0.103322 | 0.109992 | 0.517327 | 0.620649 | 2.021677717 -> 2.031037527 |
| 0.35 -> 0.65 | 1.5 | -0.264591 | -0.253729 | 0.543307 | 0.278716 | 2.033541150 -> 2.048895222 |

Here `R2=lambda_T''-2G_T` and `S_T=lambda_T''/G_T`.

## Bias-Amplitude Check at L=8

Let `delta=|rho_right-rho_left|`.

| alpha | delta=0.1 | delta=0.2 | delta=0.3 | slope in delta for S_T-2 | slope in delta for R2 |
|---:|---|---|---|---:|---:|
| 0.5 | S-2=0.001407733, R2=0.001550693 | S-2=0.005636541, R2=0.006202939 | S-2=0.012702794, R2=0.01395668 | 2.002280 | 2.000030 |
| 1.0 | S-2=0.003408468, R2=0.001078359 | S-2=0.013693643, R2=0.004313434 | S-2=0.031037527, R2=0.009705232 | 2.010190 | 2.000000 |
| 1.5 | S-2=0.005299446, R2=0.000720955 | S-2=0.021394777, R2=0.002883824 | S-2=0.048895222, R2=0.006488575 | 2.021623 | 1.999998 |

## PI Judgment

The NESS residual is not numerical noise and not an affinity-split artifact.

1. `R2` is nonzero for every tested `alpha`, `L`, and density bias.
2. At fixed `alpha` and `L=8`, `R2` grows almost exactly as `delta^2`.
3. The `L`-slope of `R2` is stable across density biases for each alpha.

This turns `NSF-FCS-2` into the active higher-value north star:

> In long-jump open exclusion, after the equilibrium second cumulant collapses to finite-volume FDT, the NESS residual `R2(L)=lambda_T''(L)-2G_T(L)` appears to carry a robust reservoir-tail scaling, with a quadratic near-equilibrium bias amplitude.

## Next Step

Start NSF-FCS-2 AB Round 1.

- A track: derive the near-equilibrium expansion and identify whether the observed `delta^2` amplitude is forced by nonlinear response / McLennan correction, then predict the `L` exponent of `R2`.
- B track: stress-test numerically with larger `L` where feasible, alternative density signs, and non-LDB/activity forcing to separate thermodynamic NESS residual from kinetic residual.

## Reverse-Bias Sanity Check

Additional ledger:

`current/plan/nsf_fcs_tier1_ness_reverse_0p60_0p40.csv`

Command:

`python scripts\nsf_fcs_transport_ledger.py --sector exclusion --L 4,5,6,7,8 --alpha 0.5,1.0,1.5 --m-tail 2000 --rho-left 0.6 --rho-right 0.4 --out current\plan\nsf_fcs_tier1_ness_reverse_0p60_0p40.csv`

Result:

- 15 rows, all `ROW_VALID`.
- Compared against `rho_left=0.4,rho_right=0.6`, the maximum absolute difference is:
  - `max |Delta S_T| = 6.03e-8`
  - `max |Delta R2| = 8.46e-9`
- At `L=8`, the differences are all below `7e-9` for `S_T` and below `3e-9` for `R2`.

Interpretation: the NESS second-cumulant residual is even under bias reversal to numerical precision. This supports the near-equilibrium judgment that the first nonzero residual amplitude is quadratic in `delta=|rho_R-rho_L|`, rather than a current-sign convention artifact.
