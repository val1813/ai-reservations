# Research plan: LP29-C2T-S2-R1-I1-X1-P1

Date: 2026-06-05

## Objective

Define and implement a proof-object authenticity precondition for terminal-status admission.

## Inputs

- `synthesis/reviewer_C2T_S2_R1_I1_X1_recheck.md`
- `current/A/artifacts/S2_R1_validator_payload_schema_round3.json`
- `validation/validate.py`
- `tests/test_validate.py`

## Work Plan

1. Extract authenticity requirements from F01-F22 into source, structure, pairs, arithmetic, execution, and comparison groups.
2. Implement `validation/authenticity.py` as a separate precondition validator.
3. Create proof-object fixtures covering valid and failing authenticity cases.
4. Add tests proving authenticity failures block before terminal-status admission.
5. Keep terminal-status regression separate from evidence-authenticity claims.

## Non-Goals

- No material validation.
- No exact Srivastava `O_s` reproduction.
- No graph-vs-overlap residual regression.
- No graph beats overlap.
