# GATE 3: B exists and differs from A

Date: 2026-06-04

## Files

- A Round 3: `current/A/C2T_S2_round3.json`
- B Round 3: `current/B/C2T_S2_round3.json`
- A re-escalation: `current/A/C2T_S2_reescalation_A.md`
- B re-escalation: `current/B/C2T_S2_reescalation_B.md`

## Result

PASS.

## Basis

A framework:

- field-level blocker table converted into a row-local reproduction-attempt contract
- four Srivastava samples crossed with four admissibility modes
- exact reproduction blocked by missing witnesses

B framework:

- finite-state reproduction executor contract
- fixed status enums and explicit mode branches
- `O_s` interpreted through proof-carrying execution / provenance-conditioned observable identity

A and B converge on the same boundary but use different frames: A is row-contract/provenance inventory; B is executor automaton/proof-carrying observable identity.
