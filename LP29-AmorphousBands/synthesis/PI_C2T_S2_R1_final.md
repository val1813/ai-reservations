# PI final synthesis: LP29-C2T-S2-R1

Date: 2026-06-05

## North Star

`LP29-C2T-S2-R1 / O_s as provenance-conditioned observable / proof-carrying baseline contract`

## Final Result

S2-R1 closes as:

> bounded / protocol-ready validator contract / not executed validator.

The phase produced a proof-carrying baseline-admission contract for exact `O_s`:

- payload schema: `current/A/artifacts/S2_R1_validator_payload_schema_round3.json`
- expected cases: `current/A/artifacts/S2_R1_A_expected_cases_round3.csv`
- transition oracle: `current/B/artifacts/S2_R1_transition_oracle_round3.csv`

## Scientific Boundary

Current Srivastava exact `O_s` remains `BLOCK`.

`reported_context` may only be a locator-gated context mode / `CONDITIONAL_CONTEXT_PASS`. It cannot be unconditional PASS and cannot upgrade to exact certification.

## REVIEWER Status

N=3 REVIEWER accepts the result as bounded / protocol-ready closeout.

Reviewer does not require Round 4 theory work. If the claim is to upgrade from protocol-ready to executed validation, the next step must be validator implementation.

## Remaining Warnings

- No project `validation/validate.py` exists.
- A terminal status `PARTIAL_CONTEXT_ONLY` is listed but not mapped to a target mode/case. It must be defined or removed before implementation.

## Allowed Claims

- The project has specified a proof-carrying `O_s` baseline-admission validator contract.
- The contract includes payload schema, expected cases, and transition oracle.
- Current exact Srivastava `O_s` admission remains blocked.

## Forbidden Claims

- exact Srivastava `O_s` has been reproduced
- validator has been executed
- material validation
- graph-vs-overlap residual regression
- graph beats overlap
- exact `O_s` impossible in principle

## Next Candidate

`LP29-C2T-S2-R1-I1 / executable O_s baseline-admission validator`.

This candidate should implement the validator and run fixtures; it should not add another purely theoretical round unless implementation reveals a specific formal gap.
