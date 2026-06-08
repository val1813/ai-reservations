# PI NSF-FCS-2 Round 2 Off-Center Reverse-Bias Check

## Purpose

Reviewer attack 3 warned that the reverse-bias check had only been done at `rho_bar=0.5`. This check repeats the reversal off center.

## Inputs

Forward/off-center ledgers:

- `current/plan/nsf_fcs_tier1_ness_offcenter_0p30_0p50_L4_7.csv`
- `current/plan/nsf_fcs_tier1_ness_offcenter_0p55_0p75_L4_7.csv`

Reverse/off-center ledgers:

- `current/plan/nsf_fcs_round2_reverse_offcenter_0p50_0p30_L4_7.csv`
- `current/plan/nsf_fcs_round2_reverse_offcenter_0p75_0p55_L4_7.csv`

All new rows are `ROW_VALID`.

## Result

| pair compared | max abs Delta S_T | max abs Delta R2 |
|---|---:|---:|
| `0.30->0.50` vs `0.50->0.30` | `4.10e-8` | `6.03e-9` |
| `0.55->0.75` vs `0.75->0.55` | `2.96e-8` | `8.01e-9` |

## Verdict

Off-center reverse-bias checks show no detectable odd contamination at the current numerical precision. Reviewer attack 3 is materially answered for `L=4..7`, `delta=0.2`, `rho_bar=0.4` and `rho_bar=0.65`.

Remaining limitation: this is still a finite-size numerical check, not a proof for arbitrary density or forcing.
