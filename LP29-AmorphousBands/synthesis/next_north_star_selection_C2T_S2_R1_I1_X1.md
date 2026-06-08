# Next north star selection

Date: 2026-06-05

## Priority Matrix Readout

After X1 closeout, the active follow-up candidates are:

- `LP29-C2T-S2-R1-I1-X1-H1 / malformed expected-contract hardening`: score 0.98.
- `LP29-C2T-S2-R1-I1-X1-P1 / proof-object authenticity validation before terminal-status admission`: score 1.50.

## Decision

Enter:

`LP29-C2T-S2-R1-I1-X1-P1 / proof-object authenticity validation before terminal-status admission`

## Rationale

X1 now protects fixture-level state transitions. The next larger unresolved risk is that `witness.predicates` are trusted booleans; the validator does not yet authenticate source locators, structure digests, pair sets, raw sums, normalization formulae, executor traces, or tolerance provenance. P1 addresses that evidence-authenticity gap before terminal-status admission can be applied to real proof objects.

`H1` remains a lower-priority hardening candidate.
