# Regression results: LP29-C2T-S2-R1-I1-X1

Date: 2026-06-05

## Commands Run

```powershell
python -m pytest tests/test_validate.py
```

Result: 5 passed, including a negative test proving that a deliberately wrong expected CSV makes suite mode exit nonzero.

```powershell
python validation/validate.py --suite current/B/fixtures/I1_authoritative_cases_round3.jsonl --expected current/B/artifacts/I1_regression_command_contract_round3.csv --emit-csv validation/results.csv --strict-no-silent-upgrade --no-legacy-partial-context-only
```

Result: exit code 0; generated `validation/results.csv` with all 17 rows marked `pass=true`.

Legacy stdin check:

```powershell
{"payload_id":"legacy_check","target_mode":"PARTIAL_CONTEXT_ONLY","witness":{"predicates":{"F01":true,"F02":true,"F03":true}}} | python validation/validate.py --stdin
```

Result: `BLOCK`, diagnostic `DEPRECATED_PARTIAL_CONTEXT_ONLY`, `migration_required=true`.

## 17-Case Status Distribution

- `BLOCK`: 8
- `CONDITIONAL_CONTEXT_PASS`: 2
- `CANDIDATE_EXACT_REPLAY`: 1
- `ADMITTED_EXACT`: 1
- `DIAGNOSED_MISMATCH`: 5

## Expected-Contract Enforcement

Reviewer found that the first implementation parsed `--expected` but did not compare it. This has been fixed.

Current behavior:

- suite mode reads `--expected`
- status mismatch makes the case `pass=false`
- first-failed-predicate mismatch makes the case `pass=false`
- any mismatch returns process exit code `1`
- `tests/test_validate.py` includes a wrong-expected negative test

## Critical Guards

- `I1_CURRENT_SRIVASTAVA_SUMMARY_BLOCK` -> `BLOCK`
- `I1_CURRENT_SRIVASTAVA_CONTEXT_ONLY_NOT_EXACT` -> `CONDITIONAL_CONTEXT_PASS`
- raw `PARTIAL_CONTEXT_ONLY` -> `BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY + migration_required=true`

## Boundary

This validates the executable regression firewall behavior for the fixture suite. It does not claim material validation, exact Srivastava `O_s` reproduction, graph-vs-overlap residual regression, graph beats overlap, or exact-impossible-in-principle.
