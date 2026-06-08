# Proof-object authenticity schema boundary: P1

Date: 2026-06-05

## Source Inputs Read

- `synthesis/reviewer_C2T_S2_R1_I1_X1_recheck.md`
- `current/A/artifacts/S2_R1_validator_payload_schema_round3.json`
- `validation/validate.py`

## Authenticity Groups

- Source: F01-F03
- Structure identity: F04-F07
- Pair policy and population: F08-F12
- Arithmetic and normalization: F13-F15
- Execution provenance: F16-F20
- Replay comparison: F21-F22

## Interface Boundary

`validation/authenticity.py` validates proof-object authenticity and returns:

- `authenticity_status`: `PASS` or `BLOCK`
- `predicate_results`: F01-F22 boolean map
- `diagnostics`
- `missing_fields`
- `invalid_fields`
- `first_failed_predicate`

The terminal-status validator remains `validation/validate.py`. P1's connection rule is:

> A real proof object may be converted to terminal-status validation payload only after `authenticity_status == PASS`; otherwise it must remain `BLOCK` at the authenticity layer.

This preserves X1's fixture-level state machine while adding a precondition for real proof-object admission.

## Non-Claims

This schema validates object shape, provenance pointers, hashes, declared formulas, execution binding, and comparison metadata. It does not independently recompute physical `O_s`, validate material rows, or establish graph-vs-overlap conclusions.
