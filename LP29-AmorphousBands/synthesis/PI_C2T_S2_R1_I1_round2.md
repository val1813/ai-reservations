# PI synthesis: LP29-C2T-S2-R1-I1 Round 2

Date: 2026-06-05

## Inputs

- A: `current/A/C2T_S2_R1_I1_round2.json`
- A artifact: `current/A/artifacts/I1_partial_context_resolution_round2.csv`
- B: `current/B/C2T_S2_R1_I1_round2.json`
- B artifact: `current/B/artifacts/I1_authoritative_case_manifest_round2.csv`
- INSPECTOR A: `synthesis/inspector_A_C2T_S2_R1_I1_round2.md`
- INSPECTOR B: `synthesis/inspector_B_C2T_S2_R1_I1_round2.md`

## Round 2 Result

A resolved the legacy status ambiguity:

> `PARTIAL_CONTEXT_ONLY` is deprecated and never emitted as validator terminal status. Legacy inputs return `BLOCK` with `DEPRECATED_PARTIAL_CONTEXT_ONLY`. Only explicit `target_mode=reported_context` with F01-F03 passing can return `CONDITIONAL_CONTEXT_PASS`.

B resolved the case inventory ambiguity:

> the CSV adversarial matrix is the authoritative executable matrix; JSON is summary/framework only. The manifest covers all 17 rows and marks each `authoritative=true`.

## INSPECTOR Status

- A: PASS.
- B: PASS.

## Current Claim

I1 is now implementation-scope-ready:

- legacy status behavior is fixed
- authoritative test matrix is fixed
- no validator has been implemented or executed yet

## Next Round Need

Round 3 should specify the minimal implementation package:

- `validation/validate.py`
- fixture JSONL/CSV inputs
- expected outputs
- regression command
- no-silent-upgrade tests

No code should be claimed complete until actually implemented and run.
