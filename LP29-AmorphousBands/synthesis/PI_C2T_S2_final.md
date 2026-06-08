# PI final synthesis: LP29-C2T-S2

Date: 2026-06-04

## North Star

`LP29-C2T-S2 / context baseline vs reproduced Srivastava exact O_s baseline`

## Inputs

- A Round 1-3: `current/A/C2T_S2_round*.json`
- B Round 1-3: `current/B/C2T_S2_round*.json`
- A attempt contract: `current/A/artifacts/S2_Srivastava_reproduction_attempt_contract.csv`
- B executor modes: `current/B/artifacts/S2_reproduction_executor_modes.csv`
- INSPECTOR reports: `synthesis/inspector_A_C2T_S2_round*.md`, `synthesis/inspector_B_C2T_S2_round*.md`
- N=3 REVIEWER: `synthesis/reviewer_C2T_S2_N3.md`
- Re-escalation: `synthesis/reescalation_PI_C2T_S2.md`
- Contradiction deepening: `synthesis/contradiction_deepening_PI_C2T_S2.md`
- Subpropositions: `synthesis/subpropositions_PI_C2T_S2.md`

## Final Result

S2 closes as a bounded reproducibility/admissibility result:

> Srivastava 2019 can be used as reported orbital-overlap/effective-mass context, but cannot currently be used as a reproduced exact `O_s` baseline for residual validation.

The exact baseline remains blocked because the current evidence lacks:

- source row/page provenance
- structure identity and coordinate/hash witness
- pair cutoff and generated pair list
- `N_pair` provenance
- raw overlap sum
- executable normalization formula/code
- same-structure mapping
- executor trace

## Executor Interpretation

The current admissible mode is:

- `reported_context_only`: allowed as literature context

The current blocked modes are:

- `fixed_density_attempt`
- `fixed_pair_attempt`
- `exact_reproduction_attempt`
- any material-validation request based on the Srivastava rows

## REVIEWER Resolution

N=3 REVIEWER found the fatal risk to be evidence-level promotion: treating reported `OI_norm` as reproduced exact `O_s`.

The reviewer did not require Round 4. Round 4 is only needed if a future provenance package is submitted for targeted audit.

## Re-escalated Insight

The larger surviving claim is:

> `O_s` is a provenance-conditioned observable, not a naked scalar descriptor.

For graph-vs-overlap validation, the baseline is not admissible until the observable identity is fixed by a proof-carrying contract over source row, structure identity, pair construction, raw sum, normalization, same-structure mapping, and executor trace.

## Allowed Claims

- Srivastava 2019 may be cited as reported orbital-overlap/effective-mass context.
- S2 defines a machine-reviewable witness burden for exact `O_s` baseline admission.
- Current exact `O_s` reproduction is blocked under available evidence.
- Future unblock requires a complete provenance package, not a better prose citation.

## Forbidden Claims

- exact Srivastava `O_s` has been reproduced
- graph metrics beat orbital-overlap baseline
- graph-vs-overlap residual regression has been run
- material validation is allowed
- exact `O_s` is impossible in principle

## Next Candidate

Register and consider `LP29-C2T-S2-R1`: `O_s` as provenance-conditioned observable / proof-carrying baseline contract.

This candidate has score 1.95 and ties the existing C2T top candidates. It should be considered after S2 closeout, with priority determined by executable unblock value.
