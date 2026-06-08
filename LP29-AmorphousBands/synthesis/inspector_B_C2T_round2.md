# INSPECTOR: B / LP29-C2T Round 2

Date: 2026-06-04

Reviewed inputs:
- `current/B/C2T_round2.json`
- `synthesis/inspector_B_C2T_round1.md`
- `current/plan/C2T_joined_table_schema.csv`
- `current/plan/C2T_field_blockers.csv`
- `current/B/artifacts/C2_material_graph_rows_blocked.csv`

Forbidden inputs not read:
- `current/A/C2T_round2.json`
- A outputs
- `current/C2T_round2.json`

## Conclusion

WARN

B Round2 is acceptable as a conservative row-audit template and claim-boundary artifact. It carries forward the Round1 warning, keeps current candidate rows blocked or diagnostic-only, and does not incorrectly upgrade any row to material validation. In the reviewed blocked-row artifact, all five candidate rows have `material_validation_allowed=false`.

The result is not a PASS because the proposed tests are only partially executable against the currently declared joined-table schema. B added several fields needed for real execution, but those fields are not yet present in `C2T_joined_table_schema.csv`; therefore downstream use still requires a schema update or a separate row-audit record format before any material row can pass.

## Findings

1. Same-sample crosswalk tests are logically correct but not directly executable on the current schema.
   - B defines SSX-01 through SSX-05 with the right failure modes: pre-label sample key lock, structure-label identity, cross-source mismatch screen, snapshot/window compatibility, and family/batch leakage key.
   - Execution gap: `sample_id_creation_record`, `structure_id`, `snapshot_id_or_window`, `material_id`, and a documented crosswalk object are not present in the current CSV schema.
   - Consequence: these tests can be used as acceptance criteria, but a joined row cannot yet be mechanically audited from the current schema alone.

2. Graph convention lock tests are directionally executable, but require fields not yet in the joined-table schema.
   - B correctly requires pre-label graph protocol lock, `L_sym` convention, budget-normalized weighted adjacency spectral radius, matched random attack control, removed-budget accounting, seed policy, and same-graph consistency across all `G1_*` metrics.
   - Execution gap: the current schema has the three `G1_*` columns and provenance text, but lacks explicit `graph_convention_provenance_id`, `graph_cutoff_rule`, `structure_id`, and `snapshot_id_or_window`.
   - Consequence: graph residual claims remain blocked until these convention-lock fields are materialized per row.

3. Forbidden-control row audit logic is usable as a protocol, but not yet as a table-native row check.
   - B's per-row checks cover onsite variance, carrier density, mobility-edge margin, batch/family leakage, graph-generated labels, synthetic labels, and silent missingness.
   - Execution gap: `forbidden_control_audit` is only a string field in the current schema. B's minimum audit record requires timestamp/version, auditor role, per-check field results, provenance notes, and a derived row decision, but no structured columns or JSON schema for that record are yet declared.
   - Consequence: a future row may not pass by setting `forbidden_control_audit=pass` unless the detailed audit record is attached and reviewable.

4. Circular leakage is currently contained but not eliminated for future rows.
   - No active circular material claim is made in B Round2.
   - B explicitly blocks target-derived sample keys, graph-generated labels, synthetic labels, same-measurement carrier-density inversion, target Wannier onsite variance, same-fit mobility-edge margins, and post-label family keys.
   - Residual risk remains if future joins rely on material/composition name matching, post-label convention choices, or a manual `forbidden_control_audit=pass` without row-level provenance. This is a future execution risk, not an observed Round2 material-validation leak.

5. `material_validation_allowed` is not incorrectly enabled.
   - `C2_material_graph_rows_blocked.csv` contains five candidate rows and all have `material_validation_allowed=false`.
   - B Round2 defines `material_validation_allowed` as a derived final gate, not a manually asserted field.
   - The true gate is strict enough: all required fields, same-sample crosswalk, graph convention lock, forbidden-control audit, `synthetic_label_flag=false`, `is_external_to_graph_proxy=true`, valid material source flag, external label payload, and locked O_s/surrogate baseline must all pass.

## Schema Mismatch Audit

Fields present in B's audit template but absent from `C2T_joined_table_schema.csv`:
- `row_id`
- `material_id`
- `structure_id`
- `snapshot_id_or_window`
- `external_label_payload`
- `is_external_to_graph_proxy`
- `material_source_flag`
- `graph_convention_provenance_id`
- `graph_cutoff_rule`

Field present in the current schema but not named directly in B's template:
- `external_Hall_Drude_Wannier_spectral_label`

This mismatch is not fatal for a template, but it blocks direct row-level execution until reconciled.

## Checklist

- same-sample crosswalk tests: WARN. Correct criteria, incomplete execution fields.
- graph convention lock tests: WARN. Correct lock logic, missing explicit convention and graph-row identity fields in current schema.
- forbidden-control row audit logic: WARN. Correct audit content, needs structured row record beyond a string status.
- circular leakage: WARN. No current material-validation leakage, but future rows remain leakage-prone unless the missing provenance fields are enforced.
- `material_validation_allowed`: PASS. No reviewed row is wrongly enabled; B's gate remains conservative.
- claim boundary: PASS. B states protocol-template-only, synthetic rows diagnostic only, and no material validation.

## Required Feed Forward

Before any downstream material-validation use:

1. Reconcile B Round2's added audit fields with `C2T_joined_table_schema.csv`, or define a separate structured row-audit JSON schema linked by `row_id`.
2. Require machine-reviewable records for `sample_id_creation_record`, graph convention pre-label lock, crosswalk evidence, and forbidden-control per-check results.
3. Preserve `material_validation_allowed=false` for all current candidate rows until the row-level evidence exists and passes.

Final decision: WARN.
