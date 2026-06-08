# NSF-FCS-2R Coefficient Extraction

**Status:** completed.

## Runs

Ledger command family:

`python scripts\nsf_fcs_transport_ledger.py --sector exclusion --L 4,5,6,7 --alpha 0.5,1.0 --rho-left ... --rho-right ... --activity-mode none --eps 1e-2,5e-3,2.5e-3 --delta 1e-2,5e-3`

Centered density windows:

- `delta=0.02`: `rho_left=0.49`, `rho_right=0.51`
- `delta=0.04`: `rho_left=0.48`, `rho_right=0.52`
- `delta=0.06`: `rho_left=0.47`, `rho_right=0.53`
- `delta=0.08`: `rho_left=0.46`, `rho_right=0.54`

Generated files:

- `current/plan/nsf_fcs_2R_coeff_delta_0p02_L4_7.csv`
- `current/plan/nsf_fcs_2R_coeff_delta_0p04_L4_7.csv`
- `current/plan/nsf_fcs_2R_coeff_delta_0p06_L4_7.csv`
- `current/plan/nsf_fcs_2R_coeff_delta_0p08_L4_7.csv`
- `current/plan/nsf_fcs_2R_coeff_fit_summary.csv`

All ledger rows were valid.

## Fit

At fixed `L,alpha`, fit raw residual:

`R2 = C_L(alpha) delta^2 + D_L(alpha) delta^4`

| L | alpha | `C_L` | `D_L` | relative fit residual | `R2/delta^2` range |
|---:|---:|---:|---:|---:|---:|
| 4 | 0.5 | `0.0769133643` | `0.0119936330` | `2.34e-4` | `0.0766295615` to `0.0769881224` |
| 5 | 0.5 | `0.0988030881` | `0.0131401728` | `1.99e-4` | `0.0984937547` to `0.0988850117` |
| 6 | 0.5 | `0.1189134613` | `0.0140069307` | `1.75e-4` | `0.1185855235` to `0.1190007706` |
| 7 | 0.5 | `0.1375468422` | `0.0148754421` | `1.62e-4` | `0.1371969292` to `0.1376395497` |
| 4 | 1.0 | `0.0700926580` | `0.0019619928` | `4.25e-5` | `0.0700457788` to `0.0701048915` |
| 5 | 1.0 | `0.0828390012` | `0.0014509334` | `2.62e-5` | `0.0828048610` to `0.0828480498` |
| 6 | 1.0 | `0.0928999630` | `0.0009990946` | `1.56e-5` | `0.0928771144` to `0.0929061914` |
| 7 | 1.0 | `0.1010624685` | `0.0006219803` | `9.60e-6` | `0.1010471897` to `0.1010663414` |

## PI Interpretation

The sharpened coefficient statement passes the first validation:

- `C_L(alpha)` is positive for every tested `L,alpha`.
- `R2/delta^2` is stable across `delta=0.02..0.08`.
- The quartic term is small enough that the quadratic coefficient is not an artifact of the largest delta window.

This supports the finite-volume curvature-like coordinate phrasing:

`R2 = C_L(alpha) delta^2 + D_L(alpha) delta^4`

It still does not establish asymptotic `L` scaling. The observed increase of `C_L` with `L` is a finite-window fact only.

## Next

Proceed to activity parity with `A=+a,-a` before making any claim about nonLDB skew being linear or quadratic in activity bias.
