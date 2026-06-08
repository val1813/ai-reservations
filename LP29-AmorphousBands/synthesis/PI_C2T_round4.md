# PI synthesis: LP29-C2T Round 4

Date: 2026-06-04

## Trigger

Round 4 was forced by `synthesis/reviewer_C2T_round3.md`.

Reviewer fatal point: Round 3 had a blocker-status CSV but no executable witness payload schema; therefore `BLOCK/WARN/PASS` was reviewer-readable, not reproducible.

## Inputs

- A: `current/A/C2T_round4.json`
- B: `current/B/C2T_round4.json`
- INSPECTOR A: `synthesis/inspector_A_C2T_round4.md`
- INSPECTOR B: `synthesis/inspector_B_C2T_round4.md`

## Produced artifacts

- `current/C2T/artifacts/C2T_A_witness_requirements_round4.csv`
- `current/C2T/artifacts/C2T_witness_payload_schema.json`
- `current/C2T/artifacts/C2T_witness_payload_examples.jsonl`
- `current/C2T/artifacts/C2T_gate_predicates.csv`
- `current/C2T/artifacts/C2T_executor_expected_results.csv`

## Result

Round 4 responds to the reviewer fatal point at infrastructure level.

A contribution:
- Defines OI/Srivastava witness requirements, including `OI_comparison_mode`, `OI_raw_sum`, `OI_norm`, `OI_normalization_formula_id`, `pair_cutoff_A`, `pair_density`, `OI_pair_mean`, `N_pair`, `N_pair_provenance_id`, `structure_id`, and `source_row_id`.
- Keeps Srivastava baseline status as `not_reproduced`.
- Keeps all current candidates `BLOCK`.

B contribution:
- Defines witness payload JSON schema.
- Provides five JSONL witness examples.
- Defines eight gate predicates mapping payload fields to `BLOCK/WARN/PASS`.
- Defines expected executor results for five candidate rows.

PI correction after INSPECTOR B:
- `C2T-AUDIT-0001` and `C2T-AUDIT-0002` had `external_label_independence=WARN`; by G3 they must be `BLOCK`.
- `C2T_executor_expected_results.csv` has been corrected.

## INSPECTOR status

- A Round 4: pass for A-side reviewer response; no Srivastava reproduction or material validation claim.
- B Round 4: warn with one mechanical correction; correction completed by PI. The final boundary remains unchanged.

## Current scientific status

C2T now has a reproducible audit contract and witness payload schema. It still has no passing material row.

Allowed:
- Claim that `BLOCK/WARN/PASS` can now be derived from witness payloads in principle.
- Claim that current five candidate rows are expected to remain `BLOCK`.

Forbidden:
- No material validation.
- No Srivastava reproduction.
- No graph-beats-overlap claim.
- No same-sample closure claim.

## Next step

Return to the checklist at North-Star closeout. GATE 1.5 must check deepening fields in A/B Round 4 or require a supplement before re-escalation.
