# Authenticity results: LP29-C2T-S2-R1-I1-X1-P1

Date: 2026-06-05

## Implemented Artifacts

- `validation/authenticity.py`
- `validation/fixtures/authenticity_cases.jsonl`
- `tests/test_authenticity.py`

## Commands Run

```powershell
python -m pytest tests/test_authenticity.py
```

Result: 6 passed.

```powershell
python -m pytest tests/test_validate.py tests/test_authenticity.py
```

Result: 11 passed.

## Fixture Coverage

- valid proof-object
- missing source locator
- bad structure digest
- pair-count mismatch
- normalization formula mismatch
- unbound execution trace
- missing predeclared tolerance
- direct forged all-true payload without authenticity
- direct forged all-true payload with `authenticity_status=BLOCK`
- self-contradictory `comparison.verdict=match` where reported and recomputed values differ beyond tolerance

## Interface Outcome

`validate_authenticity(proof_object)` returns a F01-F22 predicate map plus `authenticity_status`. `payload_from_proof_object(...)` converts that result into a terminal-validator payload.

Combined smoke confirms:

- valid proof-object -> `ADMITTED_EXACT` positive control fixture
- missing locator -> authenticity `BLOCK`, terminal validator remains `BLOCK` with first_failed `F02`
- direct exact-admission payloads without `authenticity_status=PASS` are blocked unless they are explicitly fixture-contract namespace cases from X1
- exact `match` requires reported scalar and recomputed value to satisfy the predeclared tolerance

## Boundary

P1 validates proof-object shape and provenance metadata sufficient for fixture-level admission preconditions. It does not recompute physical `O_s`, reproduce Srivastava exact `O_s`, validate material rows, or run graph-vs-overlap residual regression.
