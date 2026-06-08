# PI synthesis: LP29-C2T-S2-R1-I1 Round 1

Date: 2026-06-05

## Inputs

- A: `current/A/C2T_S2_R1_I1_round1.json`
- A implementation plan: `current/A/artifacts/I1_validator_implementation_plan_round1.csv`
- B: `current/B/C2T_S2_R1_I1_round1.json`
- B adversarial matrix: `current/B/artifacts/I1_adversarial_test_matrix_round1.csv`
- INSPECTOR A: `synthesis/inspector_A_C2T_S2_R1_I1_round1.md`
- INSPECTOR B: `synthesis/inspector_B_C2T_S2_R1_I1_round1.md`
- R1 prior intercept: `synthesis/R1_prior_search_C2T_S2_R1_I1.md`

## Round 1 Result

A produced a 12-task validator implementation plan. It correctly frames the output as a plan, not an implemented validator.

B produced a 17-row adversarial no-silent-upgrade test matrix covering locator-only, scalar-only, context-only, numeric-closeness, executor-quality-only, full-exact, and mismatch cases.

## Inspector Status

- A: PASS WITH WARNING.
- B: PASS WITH WARNING.

Warnings:

- Decide legacy `PARTIAL_CONTEXT_ONLY` behavior before coding.
- Synchronize B JSON/CSV cases or declare the CSV as authoritative.

## PI Decision

Proceed to Round 2.

Round 2 should not implement yet unless A/B converge on exact scope. It should resolve:

1. `PARTIAL_CONTEXT_ONLY` compatibility rule.
2. authoritative adversarial matrix source.
3. minimal file set for implementation: `validation/validate.py`, fixtures, tests, README.

## Forbidden Claims

- no exact Srivastava `O_s` reproduced
- no material validation
- no graph-vs-overlap residual regression
- no graph beats overlap
- no exact impossible-in-principle claim
- no claim that validator already exists or has passed
