# LP29-C2T-S2 Re-escalation PI synthesis

Date: 2026-06-04

## Killed Claims

1. Reported Srivastava/OI context is sufficient to serve as a reproduced exact `O_s` baseline.
2. Reported `OI_norm` can be promoted to same-structure `O_s` without row/page provenance, structure hash, pair construction, `N_pair`, raw overlap sum, normalization code, same-structure mapping, and executor trace.
3. A graph-vs-overlap residual comparison can be run before exact Srivastava baseline reproduction.

Killed by: A/B Round 1-3 blocker convergence and N=3 REVIEWER. The reviewer identified evidence-level promotion from reported context to reproduced exact baseline as the fatal error.

## A/B Convergence

A-side larger claim:

> A valid `O_s` baseline is a provenance-complete reproduction contract. It becomes auditable only when source row/page, structure identity, coordinates/hash, pair cutoff/list, `N_pair`, raw sum, normalization formula/code, same-structure map, and executor trace are closed.

B-side larger claim:

> `O_s` is a provenance-conditioned observable, not a naked scalar descriptor. Its physical meaning is defined by a provenance equivalence class; reported OI/effective-mass context only supplies narrative context.

These claims are complementary. A supplies the executor contract; B supplies the physical interpretation: the observable identity of `O_s` is not defined until the provenance chain is closed.

## PI Re-escalated Claim

**LP29-C2T-S2-R1: In amorphous-band graph-vs-overlap validation, an orbital-overlap baseline is not an admissible observable until its provenance equivalence class is closed. Reported Srivastava `OI_norm` is context; reproduced exact `O_s` requires a proof-carrying baseline contract over source row, structure identity, pair construction, raw sum, normalization, same-structure mapping, and executor trace.**

This is larger than the failed baseline-use claim because it reframes the validation object itself: the scientific unit is not a reported scalar but a reproducible observable with identity conditions.

## Testable Predictions

1. With only reported Srivastava context, any exact reproduction executor must fail before residual validation.
2. Varying cutoff, pair list, or normalization under the same reported context can generate multiple candidate `O_s` values, so reported context alone does not identify the observable.
3. Once the provenance contract closes, an independent executor should reproduce a single trace-bound `O_s`; if not, the conflict localizes to data/code inconsistency rather than interpretation.

## Registration Decision

Register `LP29-C2T-S2-R1` during queue update.

Provisional score:

- impact breadth: 3
- self-confirmation risk: 0.5
- completion bonus: 1.3
- claim fidelity: 1.0
- breakthrough potential: 1.0
- score: 1.95

Boundary:

- no material validation
- no graph-vs-overlap residual regression
- no graph beats overlap
- no exact `O_s` impossible-in-principle claim
- no promotion of DOI `10.1063/1.5096042` to reproduced exact baseline
