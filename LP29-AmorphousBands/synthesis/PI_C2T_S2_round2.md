# PI synthesis: LP29-C2T-S2 Round 2

Date: 2026-06-04

## Inputs

- A: `current/A/C2T_S2_round2.json`
- A blocker table: `current/A/artifacts/S2_Srivastava_reproduction_blocker_table.csv`
- B: `current/B/C2T_S2_round2.json`
- B failure modes: `current/B/artifacts/S2_Os_reproduction_payload_failure_modes.csv`
- INSPECTOR A: `synthesis/inspector_A_C2T_S2_round2.md`
- INSPECTOR B: `synthesis/inspector_B_C2T_S2_round2.md`

## Round 2 result

Round 2 converted the Round 1 boundary into two concrete negative artifacts:

- A produced a 36-row field-level blocker table for exact Srivastava `O_s` reproduction.
- B produced a 15-row proof-payload failure-mode table.

Both preserve the same boundary:

- Srivastava 2019 is `reported_context_only`.
- Exact `O_s` reproduction remains `BLOCK`.
- This is not a claim that exact `O_s` is impossible in principle.
- No material validation or graph-vs-overlap regression is allowed.

## INSPECTOR result

- A: PASS.
- B: PASS with minor implementation warning: production executor statuses should be normalized to fixed enums or explicit mode branches.

## Current strongest conclusion

The blocker is no longer vague. The missing package is:

- source-row/page provenance
- exact structure_id and coordinates/file hash
- pair cutoff and generated pair list
- `N_pair` / `N_pair_provenance_id`
- raw overlap sum
- exact normalization formula/code
- same-structure mapping to reported `OI_norm`

## Breakthrough check

Still not a theory breakthrough. It is a sharper admissibility result: reported context is not a reproduced baseline.

## AHA check

No AHA trigger. The next useful step is to normalize failure modes into an executable reproduction-attempt contract.

## Next round context

Round 3 should attempt a minimal executor-style `S2_reproduction_attempt_contract`:

- fixed enum statuses
- explicit mode branches (`reported_context_only`, `fixed_density_attempt`, `fixed_pair_attempt`, `exact_reproduction_attempt`)
- expected result for each of the four Srivastava rows
- no material validation
