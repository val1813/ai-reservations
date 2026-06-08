# GATE -1: LP29-C2T-S2-R1 contradiction validation

Date: 2026-06-04

## Candidate

`LP29-C2T-S2-R1 / O_s as provenance-conditioned observable / proof-carrying baseline contract`

## Candidate A/B

A: A reported orbital-overlap descriptor can be treated as a reusable scalar baseline once its DOI, row label, and reported value are known.

B: Exact `O_s` is not a reusable scalar baseline until its observable identity is fixed by a proof-carrying provenance contract: source row/page, structure identity, pair construction, raw sum, normalization, same-structure mapping, and executor trace.

## Why Both Cannot Be True

If A is true, the descriptor label and citation are sufficient to admit the baseline, and missing provenance is only documentation debt.

If B is true, the descriptor label is not enough; missing provenance means the baseline object is unidentified, so residual validation cannot start.

The two positions disagree about the identity condition for a computed observable.

## GATE -1 Verdict

PASS.

The candidate is not a mere implementation clean-up. It targets a basic admissibility question: whether `O_s` is a naked reported scalar or a provenance-conditioned observable.

## Starting Boundary

This phase must not claim:

- exact Srivastava `O_s` has been reproduced
- material validation is allowed
- graph-vs-overlap residual regression has been run
- graph beats overlap
- exact `O_s` is impossible in principle
