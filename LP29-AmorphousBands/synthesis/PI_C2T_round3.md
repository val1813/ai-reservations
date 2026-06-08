# PI synthesis: LP29-C2T Round 3

Date: 2026-06-04

## Inputs

- A: `current/A/C2T_round3.json`
- B: `current/B/C2T_round3.json`
- INSPECTOR A: `synthesis/inspector_A_C2T_round3.md`
- INSPECTOR B: `synthesis/inspector_B_C2T_round3.md`
- Executed conservative audit artifact: `current/C2T/artifacts/C2T_row_level_audit_record_round3.csv`

## A/B independence and framework difference

A and B were launched as independent agents and were instructed not to read each other.

A framework: minimal executable row-level audit contract for Srivastava/OI-side joined-table rows.

B framework: database transaction-log / type-state contract where each joined material row must be `BLOCK`, `WARN`, or `PASS` before validation can start.

The frameworks are different and complementary. A fixes the OI/Srivastava gate; B fixes the row-audit execution state machine.

## Round 3 result

Round 3 reached `executable contract + conservative executed blocker audit`, not material validation.

A contribution:
- Added `OI_comparison_mode`, `N_pair`, and `N_pair_provenance_id` as mode-dependent gate fields.
- Kept Srivastava status at `reported_context_candidate_not_reproduced`.
- Kept `material_validation_allowed=false`.

B contribution:
- Defined row-by-row mechanical audit fields for same-sample crosswalk, graph convention lock, external label independence, and forbidden-control row audit.
- Explicitly separated `schema_present(field)` from `provenance_valid(field)`.
- Kept every current candidate in `BLOCK`.

PI added the minimal conservative execution artifact `C2T_row_level_audit_record_round3.csv` with five candidate-source rows. All five rows derive `row_decision=BLOCK` and `material_validation_allowed=false`.

## INSPECTOR result

- A: `PASS AS EXECUTABLE CONTRACT; NOT MATERIAL VALIDATION`.
- B: `WARN`; design is correct, but required an actual row-level audit artifact.

PI handling of B warning: created `C2T_row_level_audit_record_round3.csv`. This artifact is a blocker audit, not a validation table.

## Claim boundary

Allowed:
- C2T now has a minimum executable audit contract.
- Current candidate sources can be mechanically classified as `BLOCK`.
- The next unblock task is concrete: populate machine-reviewable witness payloads for at least one row.

Forbidden:
- No material validation.
- No graph-beats-Srivastava claim.
- No Srivastava reproduction claim.
- No same-sample closure claim.

## Breakthrough check

This round is more correct and more executable, but it is not a physics breakthrough. It converts a vague evidence gap into a deterministic audit gate. Breakthrough potential remains low until at least one row can pass the provenance gates.

## AHA check

No new higher-priority north star is registered. The useful insight is procedural: `material_validation_allowed` must be derived from row gates, never manually set.

## Q6.3 / Q6.4

Claim shrinkage is explicit and accepted: C2T is an audit/pre-validation artifact only.

Simpler alternative explanation remains dominant: all apparent validation failure is explained by missing provenance and row identity, not by a material mechanism result.

## Next context for Round 4 or closeout

N=3 is reached. Mandatory reviewer should attack whether the blocker audit is enough to close C2T as a bounded artifact, or whether one additional implementation round is required to produce a JSONL/CSV executor with machine-readable witness payload schemas.
