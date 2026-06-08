# LP29-C2T Round 4 Executor Inspector

Role: INSPECTOR
Scope: `current/C2T/scripts/C2T_executor.py` plus Round 4 schema, gate predicates, examples, expected results, and actual results.

## Conclusion

WARN

Round 4 regression outputs match expected results exactly, and the actual examples do not erroneously enable `material_validation_allowed`. However, the executor is only regression-tested on negative blocker examples and has several predicate-coverage gaps relative to `C2T_gate_predicates.csv`. Therefore it is acceptable as a Round 4 negative blocker executor, but not yet a fully faithful positive/pass material-validation gate.

## Checks

### 1. Witness payload to BLOCK/WARN/PASS mapping

PASS with caveats.

`C2T_executor.py` recomputes gate statuses from payload fields rather than trusting `declared_status`:

- G0 `required_joined_fields_presence`: `base_gate()` blocks on row_id pattern failure, contradictions, or missing fields; warns on free-text-only fields or absence of any machine-reviewable witness.
- G1 `same_sample_crosswalk`: blocks on contradictions, missing fields, missing/pre-label sample record, weak identity basis, missing structure/snapshot/label provenance, or any mismatch `BLOCK`; warns on mismatch `WARN` or free-text-only fields.
- G2 `graph_convention_lock`: blocks on missing/contradictory convention fields, non-`L_sym`, missing cutoff/rho/same-graph identity, or incomplete attack protocol; warns on free-text-only fields.
- G3 `external_label_independence`: blocks on missing label payload/provenance, non-external label, synthetic label, disallowed source type, or absent graph-proxy exclusion evidence; warns on free-text-only fields.
- G4 `forbidden_control_row_audit`: folds subcheck statuses with BLOCK dominance and warns for missing audit fields/evidence.
- G5 `OI_Srivastava_reproduction`: returns `NOT_APPLICABLE` when not applicable; otherwise blocks on missing/contradictory OI reproduction fields and warns on free-text-only/non-machine witness.
- Final `row_decision`: BLOCK/WARN/PASS dominance across required gates plus applicable OI gate.

Caveats against the predicate CSV:

- G0 checks for at least one machine-reviewable witness, but not that every required field is covered by machine-reviewable provenance.
- G3 requires `graph_proxy_exclusion_evidence` to be nonempty, but does not verify that this evidence is machine-reviewable.
- G4 treats `NOT_APPLICABLE_WITH_RATIONALE` as invalid/BLOCK, although the schema and predicate text allow explicit not-applicable rationale.
- G4 does not check nonempty rationale content except indirectly via status/evidence.

These gaps do not affect the current negative examples, because all rows have hard blockers before any positive pass path.

### 2. Actual vs expected

PASS.

The actual CSV matches expected for all 5 rows across all compared status columns:

- `required_joined_fields_presence_status`
- `same_sample_crosswalk_status`
- `graph_convention_lock_status`
- `external_label_independence_status`
- `forbidden_control_row_audit_status`
- `OI_Srivastava_reproduction_status`
- `row_decision`
- `material_validation_allowed`

All rows are `row_decision=BLOCK`, with G4 at `WARN` and OI either `BLOCK` for Srivastava-applicable rows or `NOT_APPLICABLE` otherwise, matching expected.

### 3. `material_validation_allowed`

PASS for Round 4 regression.

`C2T_executor_actual_results.csv` has:

- `material_validation_allowed=false` for all 5 rows.

The script can emit `true` only when `row_decision == PASS`, `material_validation_claimed is False`, all required gates are PASS, and OI is PASS or NOT_APPLICABLE. No current Round 4 negative blocker example reaches that state.

### 4. Negative blocker executor vs material validation

PASS.

The executor does not perform material validation. It only evaluates machine-readable blocker predicates from witness payload fields and emits gate statuses plus a boolean permission flag. It does not validate physical/material claims, compute graph quantities, verify external measurements, reproduce OI numerics, or adjudicate scientific correctness.

Given the current examples are all `payload_kind=negative_blocker_witness` and all actual decisions are `BLOCK`, this remains a negative blocker executor rather than a material-validation executor.

## Final Inspector Finding

WARN: regression contract passes, no erroneous material-validation opening in actual results, and the tool remains a negative blocker executor. The warning is for incomplete predicate fidelity on positive/pass and edge-case payloads, especially machine-reviewable coverage checks and `NOT_APPLICABLE_WITH_RATIONALE` handling.
