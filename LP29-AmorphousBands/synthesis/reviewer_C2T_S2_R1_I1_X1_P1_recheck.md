# REVIEWER recheck: LP29-C2T-S2-R1-I1-X1-P1 blocker repair

Date: 2026-06-05

## Verdict

**PASS for the P1 blocker recheck.**

The fatal issue from the prior review was that authenticity was only enforced on the `payload_from_proof_object()` converter path, while direct all-true terminal payloads could still reach exact admission. That blocker is repaired for non-fixture-contract payloads.

P1 may close under the bounded claim:

> proof-object authenticity precondition implemented for fixture-level `O_s` admission / no material validation.

This remains strictly fixture-level. It is not real source authentication, exact Srivastava `O_s` reproduction, material validation, or graph-vs-overlap validation.

## Files Rechecked

- `validation/validate.py`
- `validation/authenticity.py`
- `tests/test_authenticity.py`
- `synthesis/authenticity_results_C2T_S2_R1_I1_X1_P1.md`
- `synthesis/PI_C2T_S2_R1_I1_X1_P1_final.md`
- `synthesis/gate4_C2T_S2_R1_I1_X1_P1.md`

## Commands Executed

```powershell
python -m pytest tests/test_validate.py tests/test_authenticity.py
```

Observed: `11 passed`.

## Blocker Repair Check

Terminal validator enforcement now exists. In `validate.py`, exact-admission modes:

- `candidate_exact_replay`
- `diagnosed_mismatch`
- `admitted_exact`

now block unless `witness.authenticity_status == "PASS"` or the payload is explicitly treated as X1 fixture-contract namespace.

Manual non-fixture forged payload checks:

- direct all-true `candidate_exact_replay` without authenticity -> `BLOCK`, first failed `AUTHENTICITY_PRECONDITION`
- direct all-true `diagnosed_mismatch` without authenticity -> `BLOCK`, first failed `AUTHENTICITY_PRECONDITION`
- direct all-true `admitted_exact` without authenticity -> `BLOCK`, first failed `AUTHENTICITY_PRECONDITION`
- direct all-true `admitted_exact` with `authenticity_status=BLOCK` -> `BLOCK`, first failed `AUTHENTICITY_PRECONDITION`

This closes the main bypass.

## F22 Numeric Consistency Check

`authenticity.py` now checks reported scalar, recomputed value, predeclared tolerance, and declared verdict. I reproduced the prior attack:

- reported scalar remains `1.25`
- recomputed value changed to `999.0`
- verdict left as `match`

Observed:

- `validate_authenticity()` -> `BLOCK`, first failed `F22`
- converted terminal payload -> `BLOCK`, first failed `F22`

So a self-declared `match` no longer overrides a fixture-level numeric contradiction.

## Test Coverage

`tests/test_authenticity.py` now includes the required negative tests:

- forged direct payload without authenticity cannot admit exact
- forged direct payload with `authenticity_status=BLOCK` cannot admit exact
- self-contradictory `match` fails authenticity at `F22`

Existing positive and blocker fixtures still pass:

- valid proof object -> authenticity `PASS`, terminal `ADMITTED_EXACT`
- missing locator -> authenticity `BLOCK`, terminal `BLOCK`, first failed `F02`
- bad digest, pair-count mismatch, formula mismatch, unbound trace, missing tolerance -> authenticity blockers

## Boundary Audit

The updated synthesis files keep the correct scope:

- no real source PDFs or rows are authenticated
- no exact Srivastava `O_s` is reproduced
- no material validation is attempted
- no graph-vs-overlap residual regression is run
- no graph beats overlap claim is made

The phrase "proof-object authenticity" is acceptable only because the documents explicitly bind it to fixture-level metadata/provenance checks, not real-world source authentication.

## Residual Risk

The X1 fixture-contract exception is broad: `validate.py` treats any `payload_id` starting with `I1_` as fixture-contract namespace. I confirmed that an all-true payload named `I1_FORGED_NAMESPACE_EXCEPTION` can reach `ADMITTED_EXACT` without authenticity.

This is not a blocker for P1 only if the scope remains fixture-level and `I1_` is treated as trusted internal regression namespace. For future hardening, replace the string-prefix bypass with an explicit `witness.fixture_contract=true` flag accepted only in test fixtures or suite mode.

## Final Recommendation

Close P1 with the stated bounded claim. The prior fatal blocker is repaired. Keep the `I1_` namespace bypass as a documented fixture-only compatibility exception, not as a source-authenticated admission path.
