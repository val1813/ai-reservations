# PI synthesis: LP29-C2T-S2-R1 Round 2

Date: 2026-06-05

## Inputs

- A: `current/A/C2T_S2_R1_round2.json`
- A schema: `current/A/artifacts/S2_R1_executable_witness_schema_round2.csv`
- B: `current/B/C2T_S2_R1_round2.json`
- B predicate table: `current/B/artifacts/S2_R1_executor_predicates_round2.csv`
- INSPECTOR A: `synthesis/inspector_A_C2T_S2_R1_round2.md`
- INSPECTOR B: `synthesis/inspector_B_C2T_S2_R1_round2.md`

## Round 2 Result

A converted the 22-field witness contract into a predicate-ready schema:

- `F01-F22`
- ordered gates from source locator to recomputation/tolerance
- statuses: `BLOCK`, `PARTIAL_CONTEXT_ONLY`, `CONDITIONAL_CONTEXT_PASS`, `CANDIDATE_EXACT_REPLAY`, `DIAGNOSED_MISMATCH`, `ADMITTED_EXACT`

B converted the proof-carrying observable calculus into a 9-row executor predicate table:

- locator/context gate
- structure binding
- pair policy
- raw sum
- normalization
- executor trace
- exact certification
- scalar-only rejection
- no-silent-upgrade transition guard

## Inspector Status

- A: PASS.
- B: WARN, no BLOCK.

The remaining warning is mechanical: no project `validation/validate.py` exists, so checks remain manual.

## Key Repair

Round 2 fixed the Round 1 context-PASS ambiguity:

> `reported_context` is not unconditional PASS. It can only pass as context when a stable source locator and exact scalar parse exist. It never implies exact `O_s`.

Current evidence still leaves exact `O_s` as BLOCK.

## Current Claim

Round 2 supports a stronger executable design claim:

> Exact `O_s` baseline admission can be represented as a schema-plus-predicate contract. A scalar enters exact certification only through ordered proof objects over source, structure, pair population, raw sum, normalization, same-structure mapping, execution trace, recomputed value, and tolerance.

## Forbidden Claims

- no exact Srivastava `O_s` reproduced
- no material validation
- no graph-vs-overlap residual regression
- no graph beats overlap
- no exact impossible-in-principle claim

## Next Round Need

Round 3 should instantiate a minimal validator-facing bundle:

1. merge A `F01-F22` schema with B `P0-P8` predicates,
2. define expected statuses for null/current/future-complete witness payloads,
3. show that current Srivastava context remains `BLOCK` or `CONDITIONAL_CONTEXT_ONLY`, not exact PASS.
