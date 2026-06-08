# PI synthesis: LP29-C2T-S2-R1 Round 1

Date: 2026-06-04

## Inputs

- A: `current/A/C2T_S2_R1_round1.json`
- A artifact: `current/A/artifacts/S2_R1_Os_witness_contract_round1.csv`
- B: `current/B/C2T_S2_R1_round1.json`
- B artifact: `current/B/artifacts/S2_R1_proof_carrying_observable_modes.csv`
- INSPECTOR A: `synthesis/inspector_A_C2T_S2_R1_round1.md`
- INSPECTOR B: `synthesis/inspector_B_C2T_S2_R1_round1.md`
- R1 prior intercept: `synthesis/R1_prior_search_C2T_S2_R1.md`

## Round 1 Result

A produced a 22-field `O_s` witness contract. It frames exact baseline admission as a reproducibility/provenance tuple:

`O_s(P, S, E, M, X)` where provenance, source structure, execution environment, method/normalization, and executor trace are part of the observable identity.

B produced an 8-mode proof-carrying observable calculus. It treats exactness as a predicate over the tuple:

`O_s = (v, R, H, P, n, S, Z, M, E)`

where the scalar projection alone is insufficient.

## Convergence

A and B independently converge on the same core:

> exact `O_s` admission is not scalar comparison; it is proof-carrying observable identity.

A supplies witness fields. B supplies mode/state transitions.

## INSPECTOR Status

- A: PASS.
- B: WARN, no BLOCK.

Warnings carried forward:

- no project `validation/validate.py`; inspections are manual
- B's `reported_context` status is conditional and must not be shortened to unconditional PASS
- search logs are summarized MCP records, not complete citation verification

## R1 Prior Intercept

PASS. No direct prior was found for the exact S2-R1 claim.

## Current Claim

Round 1 supports a bounded design claim:

> A future exact `O_s` baseline should be admitted only through a proof-carrying contract that binds source locator, structure identity, pair population, raw sum, normalization, same-structure mapping, and executor trace.

## Forbidden Claims

- no exact Srivastava `O_s` reproduced
- no material validation
- no graph-vs-overlap residual regression
- no graph beats overlap
- no exact impossible-in-principle claim

## Next Round Need

Round 2 should convert the A witness fields and B state/mode calculus into one executable schema/predicate table, while preserving the conditional status of reported context.
