# PI synthesis: LP29-C2T Round 4 executor

Date: 2026-06-04

## Motivation

User constraint: do not downgrade. REVIEWER/state constraint: do not stop at a human-readable audit template if a machine-readable witness/executor contract is required.

## Round 4 artifacts

- Witness payload schema: `current/C2T/artifacts/C2T_witness_payload_schema.json`
- Witness payload examples: `current/C2T/artifacts/C2T_witness_payload_examples.jsonl`
- Gate predicates: `current/C2T/artifacts/C2T_gate_predicates.csv`
- Expected results: `current/C2T/artifacts/C2T_executor_expected_results.csv`
- Executor script: `current/C2T/scripts/C2T_executor.py`
- Actual results: `current/C2T/artifacts/C2T_executor_actual_results.csv`

## Executor contract

Command:

```powershell
python current\C2T\scripts\C2T_executor.py `
  --input current\C2T\artifacts\C2T_witness_payload_examples.jsonl `
  --output current\C2T\artifacts\C2T_executor_actual_results.csv
```

Decision rule:
- Required gates G0-G4 are recomputed from payload fields.
- Optional OI/Srivastava gate G5 is applied when `applies_to_row=true`.
- `BLOCK` dominates `WARN`, which dominates `PASS`.
- `material_validation_allowed=true` only when row decision is `PASS`, `material_validation_claimed=false`, and all required gates pass.

## Regression result

The executor output matches `C2T_executor_expected_results.csv` for all 5 witness examples.

All current examples remain:

`row_decision=BLOCK`, `material_validation_allowed=false`.

## Unit boundary tests

Added:

- `current/C2T/artifacts/C2T_executor_unit_examples.jsonl`
- `current/C2T/artifacts/C2T_executor_unit_expected_results.csv`
- `current/C2T/artifacts/C2T_executor_unit_actual_results.csv`

Results:

- negative regression: PASS
- unit regression: PASS

The unit cases are synthetic executor tests only. They are not material rows and do not validate LP29 physics.

## Boundary

Round 4 upgrades C2T from human audit-template-ready to `executor-contract-ready` for negative blocker witnesses. It still does not validate any material row.
