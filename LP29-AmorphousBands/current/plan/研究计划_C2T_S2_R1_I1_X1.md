# Research plan: LP29-C2T-S2-R1-I1-X1

Date: 2026-06-05

## Objective

Implement and execute the `O_s` baseline-admission regression firewall specified by I1.

## Inputs

- `current/A/artifacts/I1_minimal_implementation_package_round3.csv`
- `current/B/artifacts/I1_regression_command_contract_round3.csv`
- `current/A/artifacts/S2_R1_validator_payload_schema_round3.json`
- `current/A/artifacts/S2_R1_A_expected_cases_round3.csv`
- `current/B/artifacts/I1_authoritative_case_manifest_round2.csv`

## Work Plan

1. Build `validation/validate.py` with shared API/CLI core.
2. Encode status gates and strict no-silent-upgrade rules.
3. Create JSONL fixtures and `expected_results.csv`.
4. Create pytest regression suite and CLI smoke tests.
5. Run pytest and CLI regression, recording actual outputs.
6. Close only if actual outputs preserve the frozen status semantics.

## Non-Goals

- No material validation.
- No exact Srivastava `O_s` reproduction claim.
- No graph-vs-overlap residual regression.
- No graph beats overlap claim.
- No exact-impossible-in-principle claim.
