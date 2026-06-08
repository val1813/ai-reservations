# INSPECTOR Report: A C2T Round 3

Role: INSPECTOR  
Object: `current/A/C2T_round3.json`  
Date: 2026-06-04

Reviewed inputs only:
- `current/A/C2T_round3.json`
- `synthesis/inspector_A_C2T_round2.md`
- `current/C2T/artifacts/C2T_joined_table_schema.csv`
- `current/C2T/artifacts/C2T_field_blocker_table.csv`
- `current/A/artifacts/C2_forbidden_controls_rules.csv`

Boundary: this inspection did not read any B output. Mechanical `validate.py` was not run because the task supplied a closed read-input set and no validation directory/file was included in that set; Q1-Q6.5 were checked manually against the supplied artifact and tables.

## Verdict

PASS AS EXECUTABLE CONTRACT; NOT MATERIAL VALIDATION.

A Round 3 resolves the Round 2 executable-template warnings. It explicitly adds `OI_comparison_mode`, `N_pair`, and `N_pair_provenance_id` to the A-side schema extension and makes them mode-dependent blockers in the row-gate algorithm. It also converts `forbidden_control_audit` into a normalized one-row-per-rule output contract with required columns sufficient for parser-level audit.

The artifact keeps the correct scientific boundary: `material_validation_allowed=false`, `Srivastava_baseline_status=reported_context_candidate_not_reproduced`, `Srivastava_reproduced=false`, and `graph_beats_Srivastava_allowed=false`. No current row is claimed to pass validation.

## Blocking Items

None for the stated Round 3 goal: an executable row-level audit contract.

Important scope note: this is not a pass for material validation. The supplied C2T field blocker table still marks every material-validation gate as unavailable or partial, and A Round 3 correctly derives current rows as `blocked_context_only`.

## Q1. Dimensional Check

PASS for contract-level equations.

The two explicit equations are dimensionally coherent if interpreted as schema-defined overlap units:
- `OI_norm == OI_raw_sum / cell_volume_m3`: raw overlap sum divided by volume gives a volume-normalized overlap quantity.
- `OI_pair_mean == OI_raw_sum / N_pair`: raw overlap sum divided by a dimensionless counted-pair denominator gives per-pair mean overlap.

No exponential, logarithmic, trigonometric, or hyperbolic function arguments appear in the supplied Round 3 formulas.

## Q2. Sign / Direction Check

PASS.

A Round 3 does not assert a graph feature direction, graph-beats-OI direction, or material-performance direction. Its directional logic is gate logic: missing required provenance or forbidden-control failure forces `blocked_context_only`, `failed_forbidden_control`, or `material_validation_allowed=false`. That direction is consistent with the supplied blocker table, where all material-validation entries are currently false.

## Q3. Circular Argument Check

PASS.

No active circular validation is present. A Round 3 explicitly blocks:
- material validation from reported `OI_norm` alone;
- Srivastava reproduction without raw sum, exact normalization, pair cutoff, same-row structure mapping, and provenance;
- Hall mobility leakage through same-measurement carrier-density inversion;
- graph-independent claims from OI, pair density, or volume without explicit controls;
- synthetic labels from becoming validation labels.

The normalized forbidden-control audit contract is no longer just a high-level JSON blob; it requires per-rule rows with `rule_id`, `target_type`, `namespace`, `columns_checked`, `result`, `reason`, `provenance_checked`, and `blocker_code`.

## Q4. Order-of-Magnitude / Scope Check

PASS / NOT APPLICABLE.

No numerical material-performance or graph-effect magnitude is claimed. The artifact's quantitative content is schema/gate structure, not a measured validation result. The supplied blocker table confirms current validation status remains false for every field.

## Q5. Algebraic / Limit Check

PASS.

Key limit behavior is correct:
- If `OI_raw_sum` is missing, both fixed-density and fixed-pair OI claims are blocked.
- If `OI_comparison_mode=no_claim`, the row can remain context-only but cannot support material validation.
- If `OI_comparison_mode=fixed_density`, the contract requires `OI_raw_sum`, `OI_norm`, `pair_density`, `cell_volume_m3`, and `OI_normalization_formula_id`.
- If `OI_comparison_mode=fixed_pair`, the contract additionally requires `OI_pair_mean`, `N_pair`, and `N_pair_provenance_id`.

This directly fixes the Round 2 warning that fixed-density/fixed-pair evaluation referred to `N_pair` provenance without guaranteeing the corresponding schema fields.

## Q5d. Source / Provenance Level

PASS WITH SCOPE LIMIT.

The artifact does not claim that real row provenance is populated. It marks current rows as incomplete or blocked:
- `OI_raw_sum`: `required_missing_for_current_rows`
- `OI_normalization_formula_id`: `required_missing_for_current_rows`
- `pair_cutoff_A`: `required_missing_for_current_rows`
- `pair_density`: `required_missing_for_current_rows`
- `N_pair`: conditionally required for fixed-pair
- `N_pair_provenance_id`: conditionally required for fixed-pair

This is acceptable because the Round 3 object is a contract. It would be unacceptable only if presented as a populated validation table.

## Q6. Integrated Judgment

PASS as a row-level audit contract.

A Round 3 truly added the missing Round 2 executability fields:
- `OI_comparison_mode` appears in `A_side_schema_extension`, `required_fields_status`, forbidden-control audit rule `FC_OI_mode_fixed_density_fixed_pair`, and row gate step 4.
- `N_pair` appears in `A_side_schema_extension`, `required_fields_status`, forbidden-control columns, and row gate step 4.
- `N_pair_provenance_id` appears in `A_side_schema_extension`, `required_fields_status`, forbidden-control columns, and row gate step 4.

These fields are not present in the base `C2T_joined_table_schema.csv`, but Round 3 explicitly declares them as A-side schema extensions. That resolves the prior ambiguity for A's Srivastava/OI audit contract without pretending the base joined table is already populated.

## Q6.3 Claim Shrinkage

No problematic shrinkage.

Relative to Round 2, A Round 3 narrows the artifact status from a near-executable template to `minimal_executable_contract`. This is not hidden shrinkage; it is explicitly declared and aligned with the blockers. The core boundary remains stable: no material validation and no reproduced Srivastava claim.

## Q6.4 Alternative Explanation Check

PASS for this artifact type.

The simpler alternative explanation is that current Srivastava/OI values are context candidates rather than reproduced baselines and that missing row-level provenance, not a graph mechanism, explains the present inability to validate. A Round 3 explicitly accepts this alternative by setting:
- `Srivastava_baseline_status=reported_context_candidate_not_reproduced`
- `no_material_validation_performed=true`
- default `row_decision=blocked_context_only`
- `graph_beats_Srivastava_allowed=false`

## Q6.5 Landing Calculation Check

PASS.

A Round 3 does not claim a no-prior-art blank with no landing calculation. Its landing object is concrete and executable at the contract level: required row fields, mode-specific OI blockers, a normalized forbidden-control audit table, and a deterministic row-gate algorithm. It also states that actual rows still lack the same-sample structure-label-baseline crosswalk and therefore cannot proceed to material validation.

## Focus Checks Requested by PI

1. Did A really fill `OI_comparison_mode` / `N_pair` / `N_pair_provenance_id`?

Yes, as contract fields and gate inputs. They are present in the A-side schema extension, required-field status, fixed-pair gate logic, and forbidden-control audit contract. They are not falsely presented as populated values for real material rows.

2. Does A still falsely claim Srivastava is reproduced?

No. A explicitly says `reported_context_candidate_not_reproduced`, `Srivastava_reproduced=false`, and no graph-vs-Srivastava claim is allowed.

3. Is `material_validation_allowed=false` maintained?

Yes. It is false in `findings`, false in default current-row derivation, and false for all current blocker-table rows. The final derivation allows true only after all gates pass; no current row is asserted to pass.

4. Is this an executable contract rather than validation?

Yes. The artifact defines row-level fields, blockers, normalized audit rows, and derivation logic. It does not populate complete same-sample rows, run material validation, or report validation performance.

## Residual Warnings

1. The A-side extension must be carried forward explicitly whenever joined-table automation is implemented. The base C2T schema alone still lacks the Srivastava/OI audit fields.

2. `material_validation_allowed` must remain derived, not manually set. Round 3 states this correctly; future populated rows must enforce it through the row-gate algorithm.

3. The next round should not cite Round 3 as evidence that Srivastava `O_s` has been reproduced. It is only evidence that the blocker logic for testing such a claim is now specified.

## Feed To Next Round

--- 投喂下一轮 ---

必须修正（阻断级）:

None for the contract stage.

建议修正（警告级）:

1. When implementing populated rows, include the A-side extension fields explicitly: `OI_comparison_mode`, `OI_raw_sum`, `OI_norm`, `OI_normalization_formula_id`, `pair_cutoff_A`, `pair_density`, `OI_pair_mean`, `N_pair`, and `N_pair_provenance_id`.
2. Keep all Srivastava/OI rows `blocked_context_only` until exact normalization, raw sum, pair cutoff, structure mapping, and same-row provenance are populated.
3. Do not set `material_validation_allowed=true` directly; derive it only after schema completeness, same-sample provenance, B0/G1 independence, synthetic-label, and forbidden-control audit gates pass.

---
