# PI NSF-FCS-2 Round 2 Direct Delta Test

## Purpose

Reviewer attack 2 warned that `Qhat=R2/(delta^2 G_T)` could bake in the quadratic law. This test fits raw `R2` against `delta` before using `Qhat`.

## Inputs

Centered density pairs around `rho_bar=0.5`:

- `delta=0.05`: `0.475 -> 0.525`, new file `current/plan/nsf_fcs_round2_delta_0p475_0p525_L4_7.csv`
- `delta=0.10`: `0.45 -> 0.55`, existing file
- `delta=0.15`: `0.425 -> 0.575`, new file `current/plan/nsf_fcs_round2_delta_0p425_0p575_L4_7.csv`
- `delta=0.20`: `0.40 -> 0.60`, existing file
- `delta=0.30`: `0.35 -> 0.65`, existing file

Window: `L=4..7`, `alpha=0.5,1.0,1.5`.

All new rows are `ROW_VALID`.

## Result

Raw `R2` delta exponent fits:

| L | alpha=0.5 | alpha=1.0 | alpha=1.5 |
|---:|---:|---:|---:|
| 4 | 2.000108 | 2.000020 | 1.999994 |
| 5 | 2.000085 | 2.000009 | 1.999986 |
| 6 | 2.000074 | 2.000007 | 2.000003 |
| 7 | 2.000068 | 2.000008 | 1.999968 |

`Qhat=R2/(delta^2 G_T)` remains nearly delta-independent at fixed `L,alpha`; the residual spread is small and grows mildly for `alpha=1.5`.

## Verdict

Reviewer circularity attack is materially answered for centered density, `L=4..7`: the quadratic law is visible directly in raw `R2`, before dividing by `delta^2`.

Remaining limitation: this still does not prove asymptotic `L` scaling or off-center bias parity.
