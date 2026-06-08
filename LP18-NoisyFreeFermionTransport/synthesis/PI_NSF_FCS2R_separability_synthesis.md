# NSF-FCS-2R Separability Synthesis

**Status:** completed.

## Inputs

- Coefficient extraction: `synthesis/PI_NSF_FCS2R_coefficient_extraction.md`
- Activity parity: `synthesis/PI_NSF_FCS2R_activity_parity.md`
- Mixed scans:
  - `current/plan/nsf_fcs_2R_mixed_delta_0p04_reversible_A_p0p10_L4_7.csv`
  - `current/plan/nsf_fcs_2R_mixed_delta_0p04_reversible_A_m0p10_L4_7.csv`
  - `current/plan/nsf_fcs_2R_mixed_delta_0p04_nonldb_A_p0p10_L4_7.csv`
  - `current/plan/nsf_fcs_2R_mixed_delta_0p04_nonldb_A_m0p10_L4_7.csv`
  - `current/plan/nsf_fcs_2R_mixed_separability_summary.csv`

All mixed rows were valid.

## Established Symmetry Channels

Current finite-window evidence supports three distinct response signatures:

1. Density-bias NESS:
   - raw `R2 = C_L(alpha) delta^2 + D_L(alpha) delta^4`;
   - `C_L(alpha)>0` for all tested `L=4..7`, `alpha=0.5,1.0`.

2. Equal-density `reversible_side` traffic:
   - equilibrium FDT residual remains at numerical floor;
   - not kinetic residual evidence.

3. Equal-density `nonLDB_site_skew`:
   - response is even in `A`;
   - leading resolved term is `A^2`, not `A`.

## Mixed Separability Check

For `delta=0.04`, `A=+0.10,-0.10`, compare

`mixed(delta,A)` vs `density_only(delta) + activity_only(A) - baseline`.

Using `R2/G_T = S_T-2`:

| mode | max additive residual | relative to mixed |
|---|---:|---:|
| `reversible_side` | `3.23e-5` | `5.88e-2` |
| `nonLDB_site_skew` | `6.75e-8` | `1.04e-4` |

## PI Interpretation

The separability claim must be asymmetric:

- `nonLDB_site_skew` is highly additive with density-bias curvature at this finite window. This supports treating nonLDB skew as a distinct even-activity perturbation channel.
- `reversible_side` preserves equilibrium FDT, but under density bias it changes the effective curvature coefficient at the few-percent level. It is not a residual source at equilibrium, yet it can reweight NESS transport curvature.

Therefore the correct statement is:

> Density bias and nonLDB site skew are separable to current numerical precision in the tested mixed window, with signatures `delta^2` and `A^2`. Reversible-side traffic is an equilibrium LDB sanity control, but in NESS it can renormalize the density-bias curvature coefficient and should not be used as a strict separability null.

## Consequence For NSF-FCS-2R

This is stronger and cleaner than the previous `Qhat` story:

- the main observable is finite-volume coefficient structure, not an exponent;
- density bias and nonLDB skew have parity-resolved signatures;
- reversible activity has a precise role: equilibrium sanity and NESS traffic-renormalization control.

## Remaining Risk

All statements remain finite-window ledger claims. No asymptotic `L` law is established.
