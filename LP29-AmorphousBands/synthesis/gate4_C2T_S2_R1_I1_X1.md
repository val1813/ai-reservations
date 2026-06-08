# GATE 4: LP29-C2T-S2-R1-I1-X1

Date: 2026-06-05

## Claim Under Gate

X1 claims only:

> fixture-level executed `O_s` baseline-admission regression firewall.

## Evidence

- `validation/validate.py` exists.
- `python -m pytest tests/test_validate.py` passed: 5 tests, including a wrong-expected negative test.
- CLI suite generated `validation/results.csv`.
- CLI suite enforces `--expected`; mismatches return nonzero.
- 17-case status distribution matches the B contract.
- Legacy `PARTIAL_CONTEXT_ONLY` remains `BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY + migration_required=true`.

## Open Issues

- The validator does not recompute physical `O_s`.
- The fixtures are proof-contract fixtures, not material rows.
- No material validation or graph-vs-overlap residual regression has been attempted.

These are not fatal to the fixture-level executable firewall claim because they are explicitly outside scope.

## Decision

PASS.

No open fatal blocker remains for X1's bounded executable-regression claim.
