# NSF-FCS-2R Activity Parity

**Status:** completed.

## Runs

Equal-density scans:

- `rho_left=rho_right=0.5`
- `L=4..7`
- `alpha=0.5,1.0`
- `A=0,+0.05,-0.05,+0.10,-0.10`
- `activity_mode=reversible_side,nonLDB_site_skew`

Generated files:

- `current/plan/nsf_fcs_2R_activity_none_A_0_L4_7.csv`
- `current/plan/nsf_fcs_2R_activity_reversible_A_p0p05_L4_7.csv`
- `current/plan/nsf_fcs_2R_activity_reversible_A_m0p05_L4_7.csv`
- `current/plan/nsf_fcs_2R_activity_reversible_A_p0p10_L4_7.csv`
- `current/plan/nsf_fcs_2R_activity_reversible_A_m0p10_L4_7.csv`
- `current/plan/nsf_fcs_2R_activity_nonldb_A_p0p05_L4_7.csv`
- `current/plan/nsf_fcs_2R_activity_nonldb_A_m0p05_L4_7.csv`
- `current/plan/nsf_fcs_2R_activity_nonldb_A_p0p10_L4_7.csv`
- `current/plan/nsf_fcs_2R_activity_nonldb_A_m0p10_L4_7.csv`
- `current/plan/nsf_fcs_2R_activity_parity_fit_summary.csv`

All rows were valid.

## Fit

At fixed `mode,L,alpha`, fit:

`R2/G_T = c0 + c_A A + c_A2 A^2`

## Main Results

### reversible_side

The equilibrium FDT residual remains at numerical-floor scale.

- `S_T` stays within about `2 - O(1e-7)` for all signs and amplitudes.
- fitted `c_A` is about `-0.9e-7` to `-1.5e-7`, comparable to the baseline numerical floor.
- fitted `c_A2` is also floor-scale, about `1e-9` to `2e-7`.

Interpretation:

`reversible_side` remains an LDB sanity control. It should not be interpreted as a source of kinetic residual.

### nonLDB_site_skew

The leading resolved term is even in `A`, not odd.

Representative fitted `c_A2`:

| L | alpha | `c_A` | `c_A2` |
|---:|---:|---:|---:|
| 4 | 0.5 | `-3.75e-9` | `0.00384197` |
| 5 | 0.5 | `-3.32e-10` | `0.00464629` |
| 6 | 0.5 | `9.02e-10` | `0.00525631` |
| 7 | 0.5 | `8.31e-10` | `0.00573578` |
| 4 | 1.0 | `2.90e-9` | `0.00875998` |
| 5 | 1.0 | `5.88e-9` | `0.0105475` |
| 6 | 1.0 | `5.06e-9` | `0.0119156` |
| 7 | 1.0 | `2.16e-9` | `0.0130007` |

Odd parity checks:

- `A=+0.05` vs `A=-0.05` differs only at about `1e-9` or below.
- `A=+0.10` vs `A=-0.10` differs only at about `1e-9` or below.

Interpretation:

B's provisional `A`-linear nonLDB expectation is not supported by this parity scan. The observed equal-density nonLDB residual is dominated by an even `A^2` response.

## PI Conclusion

The activity split is now sharper:

- `reversible_side`: LDB-preserving traffic, FDT residual at numerical floor.
- `nonLDB_site_skew`: genuine non-LDB perturbation, but the leading equal-density response in this symmetric protocol is `A^2`, not `A`.

This improves NSF-FCS-2R: the separability program should use parity-resolved activity coefficients, not assume linear non-LDB response.

## Next

Proceed to separability synthesis. A mixed `delta,A` scan is optional only if needed; current coefficient extraction plus activity parity already establish that the two channels have different symmetry signatures:

- density bias: `delta^2`
- nonLDB site skew at equal density: `A^2`
- reversible traffic: numerical floor
