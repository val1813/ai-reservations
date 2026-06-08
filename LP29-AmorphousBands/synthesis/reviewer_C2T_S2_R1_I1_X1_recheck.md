# REVIEWER recheck: LP29-C2T-S2-R1-I1-X1 blocker repair

Date: 2026-06-05

## Verdict

**PASS for the X1 blocker recheck.**

The previous blocker was that suite mode accepted `--expected` but did not enforce it. That blocker is repaired for the valid B command-contract CSV: suite mode now loads expected rows, compares `expected_status`, compares expected `first_failed_predicate`, writes per-row `pass`, and returns nonzero on mismatch.

X1 may close as:

> executed fixture-level `O_s` baseline-admission regression firewall / no material validation.

The close remains fixture-level only. It still does not reproduce exact Srivastava `O_s`, validate material rows, run graph-vs-overlap residual regression, or prove graph beats overlap.

## Files Rechecked

- `validation/validate.py`
- `tests/test_validate.py`
- `synthesis/regression_results_C2T_S2_R1_I1_X1.md`
- `synthesis/PI_C2T_S2_R1_I1_X1_final.md`

## Implementation Check

`validate.py` now contains an expected-contract path:

- `_load_expected_contract(expected_path)` reads the CSV.
- It accepts either `fixture_id` or `test_id`.
- It accepts either `expected_terminal_status` or `expected_status`.
- `_parse_expected_first_failed()` extracts `expected_first_failed_predicate`, or parses `first_failed_predicate=` from `expected_stdout_or_file`.
- `_run_suite()` compares each observed result to expected status and first-failed predicate.
- Mismatches append `EXPECTED_STATUS_MISMATCH:<expected>` or `EXPECTED_FIRST_FAILED_MISMATCH:<expected>`, mark `pass=false`, and return process exit code `1`.

This directly fixes the prior `--expected` no-op.

## Commands Executed

```powershell
python -m pytest tests/test_validate.py
```

Observed: `5 passed`.

The test suite now includes `test_cli_suite_fails_wrong_expected_contract`, which mutates the expected status and asserts nonzero return plus `pass=false`.

```powershell
python validation/validate.py --suite current/B/fixtures/I1_authoritative_cases_round3.jsonl --expected current/B/artifacts/I1_regression_command_contract_round3.csv --emit-csv validation/results.csv --strict-no-silent-upgrade --no-legacy-partial-context-only
```

Observed:

- exit code `0`
- `pass=true`: 17 rows
- `BLOCK`: 8
- `CONDITIONAL_CONTEXT_PASS`: 2
- `CANDIDATE_EXACT_REPLAY`: 1
- `ADMITTED_EXACT`: 1
- `DIAGNOSED_MISMATCH`: 5

## Negative Tests

Wrong expected status, no-BOM temp CSV:

- changed first expected row from `BLOCK` to `ADMITTED_EXACT`
- observed exit code `1`
- first row emitted `pass=false`
- diagnostic contained `EXPECTED_STATUS_MISMATCH:ADMITTED_EXACT`

Wrong expected first-failed predicate, no-BOM temp CSV:

- changed first expected row to `first_failed_predicate=WRONG_FIRST`
- observed exit code `1`
- first row emitted `pass=false`
- diagnostic contained `EXPECTED_FIRST_FAILED_MISMATCH:WRONG_FIRST`

These two manual checks cover the requested `expected_status` and `first_failed` mismatch behavior.

## Formal Suite Status

The formal 17-case suite is now a real comparator run, not just an observed CSV generator. All 17 rows are marked `pass=true` in `validation/results.csv`, and the distribution matches the B contract.

## Residual Risk

One hardening issue remains but is not a blocker for this recheck: if an expected CSV is malformed such that no rows expose `fixture_id` or `test_id` / expected status columns, `_load_expected_contract()` returns `{}` and suite mode silently runs without comparison. I confirmed this with a deliberately malformed expected CSV: exit code remained `0`.

This does not affect the official B contract file, and the requested wrong-status / wrong-first-failed cases now fail correctly. Recommended hardening: if `--expected` is supplied and zero valid expected rows are parsed, return exit code `2` or mark all rows failed with `INVALID_EXPECTED_CONTRACT`.

## Boundary Audit

The updated PI and regression reports keep the correct scope boundary:

- allowed: fixture-level executable regression firewall
- allowed: CLI expected contract enforcement for current fixtures
- forbidden: exact Srivastava `O_s` reproduced
- forbidden: material validation
- forbidden: graph-vs-overlap residual regression
- forbidden: graph beats overlap
- forbidden: physical correctness beyond encoded fixture contract

No overclaim was introduced by the blocker repair.

## Final Recommendation

Close X1 at fixture-level executed regression firewall scope. The prior fatal blocker is repaired. Keep the malformed/empty expected-contract behavior as a follow-up hardening item, not a closure blocker.
