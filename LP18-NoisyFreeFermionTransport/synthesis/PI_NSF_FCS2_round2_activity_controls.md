# NSF-FCS-2 Round 2 Activity Controls

**Status:** completed as reviewer major-revision response.

## Control design

Implemented explicit activity controls in `scripts/nsf_fcs_transport_ledger.py`.

- `activity_mode=none`: exact legacy reservoir-rate convention.
- `activity_mode=reversible_side`: multiplies same-side in/out rates by the same site-dependent traffic factor. This changes kinetics but preserves the local in/out ratio, so it is an LDB sanity control, not evidence for a kinetic residual.
- `activity_mode=nonLDB_site_skew`: changes the site-dependent in/out ratio. Left reservoirs receive `+A phi_x`; right reservoirs receive `-A phi_x`, with `phi_x=(x-(L+1)/2)/L`. This cannot be absorbed into a site-independent reservoir chemical potential.

The CSV ledger now records `activity_mode` and `activity_bias`.

## Sanity runs

All runs used finite-density exclusion, `L=4,5,6`, `alpha=0.5,1.0`, `eps=1e-2,5e-3,2.5e-3`, and `delta=1e-2,5e-3`.

Generated files:

- `current/plan/nsf_fcs_round2_activity_none_eq_L4_6.csv`
- `current/plan/nsf_fcs_round2_activity_reversible_eq_L4_6.csv`
- `current/plan/nsf_fcs_round2_activity_nonldb_eq_L4_6.csv`
- `current/plan/nsf_fcs_round2_activity_reversible_ness_L4_6.csv`
- `current/plan/nsf_fcs_round2_activity_nonldb_ness_L4_6.csv`

Equilibrium, `rho_left=rho_right=0.5`:

| mode | max `|R2|` | `S_T` range |
|---|---:|---:|
| `none` | `1.80e-7` | `1.999999798` to `1.999999957` |
| `reversible_side`, `A=0.1` | `1.88e-7` | `1.999999789` to `1.999999944` |
| `nonLDB_site_skew`, `A=0.1` | `4.95e-5` | `2.000038217` to `2.000119114` |

NESS, `rho_left=0.4,rho_right=0.6`:

| mode | max `|R2|` | `S_T` range |
|---|---:|---:|
| `reversible_side`, `A=0.1` | `4.12e-3` | `2.003440755` to `2.011302554` |
| `nonLDB_site_skew`, `A=0.1` | `4.81e-3` | `2.004107065` to `2.012219605` |

## PI interpretation

The reviewer-requested split is now operational. The reversible control preserves equilibrium FDT to numerical precision, so it should only be used as an LDB/normalization sanity check. The non-LDB skew produces a distinct finite residual already at equal reservoir density, consistent with the intended role as a true non-LDB kinetic perturbation.

For the current NSF-FCS-2 mainline, do not merge these two mechanisms rhetorically. Existing NESS residual claims should remain tied to density-bias NESS unless a later A/B round specifically establishes a stronger non-LDB scaling statement.
