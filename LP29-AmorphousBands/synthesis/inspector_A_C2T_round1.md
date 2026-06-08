# INSPECTOR Report: A C2T Round 1

Role: INSPECTOR
Object: `current/A/C2T_round1.json`
Date: 2026-06-04

Reviewed inputs:
- `current/A/C2T_round1.json`
- `current/plan/C2T_required_join_fields.md`
- `current/plan/C2T_joined_table_schema.csv`
- `current/A/artifacts/C2_forbidden_controls_rules.csv`
- `synthesis/PI_C2_final.md`

Boundary: this inspection did not use B output.

## Verdict

WARN

No blocking dimensional, directional, circularity, order-of-magnitude, algebraic, or limiting-case defect was found in A's C2T Round 1 output. A correctly keeps `material_validation_allowed=false`, `graph_beats_baseline_allowed=false`, and frames the result as an extractability/blocker report rather than evidence for material validation.

The result can continue, but the warnings below must be carried into the next C2T round.

## Blocking Items

None.

## Warnings

1. `label_provenance_id` is marked `present` for Srivastava rows, but the joined-table schema requires DOI/table/figure/SI/path plus row or digitized point id. A's wording "source_row_id plus DOI" may be acceptable as a partial trace, but it should be downgraded to `candidate` or `partial` until the exact table/SI/path and row-level label source are explicitly locked.

2. A's `required_fields_status` covers the 14 knowledge-graph required fields, but the active joined-table schema also requires `synthetic_label_flag` and `material_validation_allowed`. A mentions these in the claim boundary and minimum table condition, but the field-status block should explicitly include both schema-required flags in the next artifact to prevent row-level gate ambiguity.

3. The forbidden-control rule with `forbidden_namespace=oi;graph` is semantically useful but not mechanically clean unless the audit parser explicitly supports multi-namespace cells. For executable leakage auditing, split it into separate namespace rows or define parser semantics before using it as a pass/fail audit.

4. `B0_carrier_density` is treated as a `candidate` because the Furubayashi schema has `n_H_cm3`, but for Hall-mobility targets carrier density is forbidden if it participates in the same-measurement `sigma/(n*e)` inversion. A flags this, but the next joined table must carry a row-level independence status, not only a source-level candidate status.

5. `O_s_or_exact_overlap_baseline` remains a reported/contextual `OI_norm` candidate, not a reproduced exact Srivastava `O_s`. A states this correctly; the warning is to prevent later claim inflation: no Srivastava reproduction, fixed-density/fixed-pair OI comparison, or graph-beats-baseline statement can be made before `OI_raw_sum`, exact normalization, and row-to-structure mapping are all present.

## Check Matrix

| Dimension | Result | Notes |
|---|---:|---|
| Dimensional consistency | PASS | No new dimensional formula is used for a positive claim. `log(pair_density_a/pair_density_b)` is dimensionless in the forbidden-control rule. |
| Direction/sign | PASS | Missing provenance forces `material_validation_allowed=false`; graph validation is not allowed. Direction matches the gate rule. |
| Circular reasoning | PASS | A blocks graph/material validation when labels, structures, or controls are not independently sourced. No synthetic or graph-generated row is used as material evidence. |
| Order of magnitude | PASS | The only concrete values in the inspected A JSON are Srivastava effective-mass context values around 0.16-0.22 `m0`, and no quantitative conclusion depends on them. |
| Algebraic check | PASS | A correctly identifies Hall mobility leakage risk through same-measurement `sigma/(n*e)` and conductivity/resistivity algebraic transforms. |
| Limiting degeneration | PASS | In the limiting case of any missing provenance-critical field, the row remains blocked; this is consistent with `C2T_required_join_fields.md`. |
| Claim shrinkage | PASS | A's narrowed claim is consistent with `PI_C2_final.md`: protocol-ready / empirical validation paused. |
| Alternative explanations | WARN | A preserves baseline/OI and family/batch controls, but row-level independence and family blocking are not yet executable because no complete joined row exists. |
| Landing calculation | WARN | The minimum unblock plan is concrete, but Round 1 still has no executable joined table row and no row-level audit result. This is acceptable for extractability Round 1 but must not be treated as validation. |
| Forbidden-control leakage | WARN | Rules cover the main leakage channels, but executable audit semantics for multi-namespace rules and same-measurement carrier-density/Hall mobility independence remain unresolved. |

## Feed To Next Round

Blocking fixes:
- None.

Recommended fixes:
1. Downgrade or qualify Srivastava `label_provenance_id=present` until DOI/table/SI/path plus row-level label source is explicit.
2. Add `synthetic_label_flag` and `material_validation_allowed` to A's field-status accounting, not only to the claim boundary.
3. Make forbidden-control rules mechanically auditable: split `oi;graph` or define parser behavior.
4. Add row-level independence status for `B0_carrier_density`, especially for Hall mobility targets.
5. Keep all material-validation and graph-beats-baseline claims frozen until exact `O_s`, `OI_raw_sum`, row-to-structure mapping, B0 controls, G1 metrics, external label provenance, and forbidden-control audit are complete.
