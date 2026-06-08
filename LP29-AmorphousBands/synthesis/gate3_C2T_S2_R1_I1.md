# GATE 3: B exists and B framework differs from A

Date: 2026-06-05

## Files Checked

- A: `current/A/C2T_S2_R1_I1_round3.json`
- A artifact: `current/A/artifacts/I1_minimal_implementation_package_round3.csv`
- B: `current/B/C2T_S2_R1_I1_round3.json`
- B artifact: `current/B/artifacts/I1_regression_command_contract_round3.csv`

## Decision

PASS.

B exists and differs from A:

- A framework: defines the minimal implementation package, API/CLI contract, fixture manifest schema, legacy partial-context handling, and validator module/test/README boundaries.
- B framework: maps 17 authoritative rows into a regression command contract with expected statuses, first-failed predicates, no-silent-upgrade guards, and actual-result CSV requirements.

The two are complementary but not the same framework.

## Boundary

This gate does not claim that either A or B implemented the validator or ran regression tests.
