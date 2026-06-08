# PI final synthesis: LP29-C2T

Date: 2026-06-04

## Conclusion type

`executor-contract-ready / no provenance-complete material rows / validation blocked`

## Core artifacts

- `current/C2T/artifacts/C2T_joined_table_schema.csv`
- `current/C2T/artifacts/C2T_source_inventory.csv`
- `current/C2T/artifacts/C2T_field_blocker_table.csv`
- `current/C2T/artifacts/C2T_A_witness_requirements_round4.csv`
- `current/C2T/artifacts/C2T_witness_payload_schema.json`
- `current/C2T/artifacts/C2T_witness_payload_examples.jsonl`
- `current/C2T/artifacts/C2T_gate_predicates.csv`
- `current/C2T/scripts/C2T_executor.py`
- `current/C2T/artifacts/C2T_executor_expected_results.csv`
- `current/C2T/artifacts/C2T_executor_actual_results.csv`
- `current/C2T/artifacts/C2T_executor_unit_expected_results.csv`
- `current/C2T/artifacts/C2T_executor_unit_actual_results.csv`

## Main result

C2T did not produce a provenance-complete material row. It produced a witness-payload schema, gate predicates, and executor contract that can derive `BLOCK/WARN/PASS` and `material_validation_allowed` from payloads.

All five current candidate rows remain:

`row_decision=BLOCK`, `material_validation_allowed=false`.

## Allowed claim

LP29 now has an executable pre-validation witness/executor contract for C2T candidate rows. The executor regression and synthetic unit-boundary tests match expected outputs.

## Forbidden claims

- No material validation.
- No Srivastava reproduction.
- No graph-beats-overlap baseline claim.
- No same-sample closure for Jankousky/Furubayashi/Jang.
- No synthetic unit test may be treated as material evidence.

## Re-escalated candidate

`LP29-C2T-R1`: proof-carrying row / witness-executor admissibility calculus as the scientific unit for materials-mechanism comparison.

## Next step

Run a dedicated phase on one concrete candidate row: either Jankousky single-row audit or Srivastava exact `O_s` reconstruction. Until at least one real row reaches `PASS`, do not run graph-vs-overlap residual regression.
