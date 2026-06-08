# LP29-C2T-S2-R1 subproposition extraction

Date: 2026-06-05

Sources: Rounds 1-3, INSPECTOR reports, N=3 REVIEWER, Re-escalation, contradiction deepening.

## Extracted Subpropositions

1. LP29-C2T-S2-R1-I1: executable `O_s` baseline-admission validator

A: A proof-carrying schema/oracle is enough as a protocol artifact.

B: The scientific gate exists only when a validator executes F01-F22/P0-P8 over fixtures and emits expected terminal statuses.

Score: 1.95.

2. LP29-C2T-S2-R1-I2: `PARTIAL_CONTEXT_ONLY` terminal-status resolution

A: `PARTIAL_CONTEXT_ONLY` can remain as a harmless spare status.

B: Any terminal status without target mode/case creates implementation ambiguity and must be defined or removed before validator release.

Score: 1.50.

3. LP29-C2T-S2-R1-I3: canonicalization conformance fixtures

A: Human-readable predicates over structure, pair list, formula, and trace are sufficient.

B: Cross-implementation exact `O_s` admission requires conformance fixtures for canonical structure serialization, pair-list ordering, formula representation, and trace-output binding.

Score: 1.50.

## PI Decision

Register `LP29-C2T-S2-R1-I1` as the strongest continuation candidate. Keep I2/I3 as implementation subcandidates under I1.

None permits material validation, graph-vs-overlap regression, graph beats overlap, or exact `O_s` reproduction without a complete witness payload.
