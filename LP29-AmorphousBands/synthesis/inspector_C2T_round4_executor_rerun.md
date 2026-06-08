# INSPECTOR rerun: LP29-C2T Round 4 executor

Date: 2026-06-04

Conclusion: PASS

## Scope

Read and inspected:

- `current/C2T/scripts/C2T_executor.py`
- `current/C2T/artifacts/C2T_witness_payload_examples.jsonl`
- `current/C2T/artifacts/C2T_executor_expected_results.csv`
- `current/C2T/artifacts/C2T_executor_actual_results.csv`
- `current/C2T/artifacts/C2T_executor_unit_examples.jsonl`
- `current/C2T/artifacts/C2T_executor_unit_expected_results.csv`
- `current/C2T/artifacts/C2T_executor_unit_actual_results.csv`
- `synthesis/PI_C2T_round4_executor.md`

## Regression checks

Negative regression: PASS.

- Re-ran `C2T_executor.py` on `C2T_witness_payload_examples.jsonl` into a temporary CSV.
- Temporary rerun output matched `C2T_executor_actual_results.csv` exactly.
- Field-level comparison against `C2T_executor_expected_results.csv` found no mismatches for the executor decision columns.
- All five material candidate audit rows remain `row_decision=BLOCK` and `material_validation_allowed=false`.

Unit regression: PASS.

- Re-ran `C2T_executor.py` on `C2T_executor_unit_examples.jsonl` into a temporary CSV.
- Temporary rerun output matched `C2T_executor_unit_actual_results.csv` exactly.
- Field-level comparison against `C2T_executor_unit_expected_results.csv` found no mismatches for `row_decision` or `material_validation_allowed`.
- Synthetic unit rows behave as expected: `C2T-AUDIT-9001` gives `PASS/true`; `C2T-AUDIT-9002` gives `WARN/false`.

## Boundary checks

No evidence that synthetic unit tests were folded into the negative/material candidate regression:

- Negative actual output contains only `C2T-AUDIT-0001` through `C2T-AUDIT-0005`.
- Unit actual output contains only `C2T-AUDIT-9001` and `C2T-AUDIT-9002`, with `candidate_source` explicitly marked synthetic executor unit.
- PI synthesis explicitly states the unit cases are synthetic executor tests only and do not validate LP29 physics.

No evidence that real candidate material validation was opened:

- Real candidate rows `0001-0005` all output `material_validation_allowed=false`.
- The executor only sets `material_validation_allowed=true` when `row_decision == PASS`, `material_validation_claimed is False`, every required gate is `PASS`, and optional OI is `PASS` or `NOT_APPLICABLE`.
- The current real candidate payloads all retain blocking required gates, so the true branch is unreachable for them.

## Script review

No blocking script problem found in the rerun scope.

Relevant behavior in `C2T_executor.py`:

- Required gates are recomputed from payload fields rather than trusting declared statuses.
- Optional OI/Srivastava gate is included when applicable.
- `BLOCK` dominates `WARN`, and `WARN` dominates `PASS`.
- Row output includes only audit decision fields, not a material claim payload.

Non-blocking note:

- The executor does not internally enforce a distinction between synthetic unit payloads and material candidate payloads. This is acceptable for the present regression because unit inputs are isolated in separate files and expected outputs, and real candidate outputs remain blocked. If the executor is later used as a production material-validation gate, add an explicit `payload_kind`/source boundary or separate command mode.

## Verdict

PASS: negative regression and unit regression match; synthetic unit tests are separated from the material candidate regression; real candidate material validation remains disabled; no blocking executor issue remains in the inspected scope.
