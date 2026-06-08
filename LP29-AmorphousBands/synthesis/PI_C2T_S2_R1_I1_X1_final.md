# PI final synthesis: LP29-C2T-S2-R1-I1-X1

Date: 2026-06-05

## Final Status

`LP29-C2T-S2-R1-I1-X1` closes as:

> executed `O_s` baseline-admission regression firewall / fixture-level validator regression passed / no material validation.

## Implemented Artifacts

- `validation/validate.py`
- `validation/__init__.py`
- `validation/fixtures/a_expected_cases.jsonl`
- `validation/fixtures/legacy_partial_context.jsonl`
- `validation/fixtures/expected_results.csv`
- `current/B/fixtures/I1_authoritative_cases_round3.jsonl`
- `tests/test_validate.py`
- `validation/README.md`
- `validation/results.csv`

## Commands Executed

```powershell
python -m pytest tests/test_validate.py
```

Result: 5 passed, including a negative test for wrong expected-contract enforcement.

```powershell
python validation/validate.py --suite current/B/fixtures/I1_authoritative_cases_round3.jsonl --expected current/B/artifacts/I1_regression_command_contract_round3.csv --emit-csv validation/results.csv --strict-no-silent-upgrade --no-legacy-partial-context-only
```

Result: generated `validation/results.csv`; all 17 rows are `pass=true`; status distribution matches B contract:

- `BLOCK`: 8
- `CONDITIONAL_CONTEXT_PASS`: 2
- `CANDIDATE_EXACT_REPLAY`: 1
- `ADMITTED_EXACT`: 1
- `DIAGNOSED_MISMATCH`: 5

Reviewer-discovered blocker repaired:

- `--expected` is now loaded in suite mode.
- Expected status and expected first-failed predicate are compared per case.
- Any mismatch marks `pass=false` and exits nonzero.

## Critical Guard Outcomes

- Current Srivastava summary evidence -> `BLOCK`.
- Current Srivastava reported-context evidence -> `CONDITIONAL_CONTEXT_PASS`, not exact admission.
- Raw `PARTIAL_CONTEXT_ONLY`, even with F01-F03 true -> `BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY + migration_required=true`.
- No emitted result uses terminal status `PARTIAL_CONTEXT_ONLY`.

## Allowed Claims

- The fixture-level executable regression firewall exists and passes the current test suite.
- The CLI suite enforces the expected contract and fails on a deliberately wrong expected CSV.
- The implementation exposes `validate_payload(payload: dict) -> dict` and a CLI path.
- The validator preserves the frozen no-silent-upgrade semantics for the 17 authoritative cases and legacy partial-context fixtures.

## Forbidden Claims

- exact Srivastava `O_s` has been reproduced.
- material validation.
- graph-vs-overlap residual regression.
- graph beats overlap.
- exact `O_s` impossible in principle.
- the validator proves physical correctness beyond the encoded fixture contract.

## PI Judgment

X1 successfully converts I1 from specification-only to an executed fixture-level regression firewall. The remaining frontier is not more admission semantics prose; it is whether future real proof-carrying `O_s` witness bundles can be constructed for actual source rows without violating the same gates.
