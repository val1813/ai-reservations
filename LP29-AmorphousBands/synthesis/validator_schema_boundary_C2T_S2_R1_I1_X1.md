# Validator schema and state boundary: X1

Date: 2026-06-05

## Source Contracts Read

- `current/A/artifacts/I1_minimal_implementation_package_round3.csv`
- `current/B/artifacts/I1_regression_command_contract_round3.csv`
- `current/A/artifacts/S2_R1_validator_payload_schema_round3.json`

## Implementation Input Convention

The executable validator accepts a JSON object:

- `payload_id`: string
- `target_mode`: string
- `witness`: object

For executable fixtures, `witness.predicates` may provide auditable boolean predicate values for `F01` to `F22`. This is a compact proof-carrying representation of the round-3 schema. Additional fields may include:

- `diagnostics`: list of diagnostic strings
- `first_failed_predicate_hint`: string
- `comparison`: object with `verdict` equal to `match`, `mismatch`, or `not_run`

## Output Convention

`validate_payload(payload: dict) -> dict` returns:

- `payload_id`
- `target_mode_raw`
- `target_mode_resolved`
- `terminal_status`
- `diagnostics`
- `missing_fields`
- `invalid_fields`
- `first_failed_predicate`
- `predicate_results`
- `migration_required`
- `comparison`

## Hard State Boundaries

- Emitted terminal statuses exclude `PARTIAL_CONTEXT_ONLY`.
- Raw `PARTIAL_CONTEXT_ONLY` always returns `BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY + migration_required=true`.
- `reported_context` requires F01-F03 and returns `CONDITIONAL_CONTEXT_PASS`.
- `candidate_exact_replay` requires F01-F20 and returns `CANDIDATE_EXACT_REPLAY`.
- `admitted_exact` requires F01-F22 and a predeclared matching comparison.
- `diagnosed_mismatch` requires replay completeness plus a failed comparison or declared mismatch predicate.
- Current Srivastava summary evidence remains `BLOCK`.
