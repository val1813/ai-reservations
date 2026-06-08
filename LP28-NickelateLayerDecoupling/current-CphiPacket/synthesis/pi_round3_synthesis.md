# PI Synthesis: LP28-CphiPacket Round 3

## Inputs

- A Round 3: `current-CphiPacket/A/round3.json`
- B Round 3: `current-CphiPacket/B/round3.json`
- INSPECTOR A Round 3: `PASS with WARNING`
- INSPECTOR B Round 3: `PASS with one WARNING`

## Core Result

Round 3 produced the final packet feasibility state machine.

Current measured packet status:

`NOT_FOUND`

Prospective protocol status:

`PACKET_FEASIBLE_NEAR_FUTURE`, conditional on green-row firewall, pre-output sibling tolerances, facility acceptance, output blinding, and tiered thresholds.

This still does not claim `R_oe` exists or that `C_phi` is independent.

## Final State Priority

Inspector B flagged possible overlap between `PROTOCOL_FAILURE` and `NON_IDENTIFIABLE`. PI resolves it by priority:

1. `PROTOCOL_FAILURE`
   - use when execution violated blinding, locking, pre-registration, canonical `P_oe`, raw archive, or row inclusion rules.
   - this is procedural; no scientific inference is allowed.

2. `NOT_FOUND`
   - use when evidence remains component-only and cannot be reconstructed into row-level packet entries.

3. `NON_DECISION_GRADE`
   - use when a rehearsal/minimum packet exists but lacks decision-grade N/batches/labs/validation.

4. `NON_IDENTIFIABLE`
   - use when a cleanly executed packet still cannot separate `P_oe` from `B_min` because the same fitted qz/c-axis/orbital state or sibling/path ambiguity is load-bearing.

5. `PACKET_FEASIBLE_NEAR_FUTURE`
   - use only for a prospective design satisfying the firewall and facility acceptance requirements at a declared tier.

## Final Thresholds

Rehearsal:

- `N >= 12`
- machinery only, no residual decision.

Minimum executable:

- `N >= 24`
- `>=18` green valid uncensored canonical `P_oe` rows
- `>=2` batches
- output embargo intact
- firewall passes
- not claim-bearing.

Decision-grade / B-concession:

- target `N >= 48`
- `>=36` green complete blinded rows after censoring
- `>=4` batches
- `>=3` labs
- leave-one-batch-out and leave-one-lab-out validation
- zero red rows in primary analysis.

These are protocol thresholds, not statistical power theorems.

## Final Technical Object

Canonical:

`P_oe = (chi_odd - chi_even)/(chi_odd + chi_even)`

The denominator floor only censors rows. It does not replace the denominator.

Diagnostic-only:

`P_oe_L1_diagnostic`

It cannot drive row selection, thresholds, or the primary residual call.

## What Changed From CphiCollapse

`LP28-CphiCollapse` ended with a bounded residual protocol.

`LP28-CphiPacket` now says exactly what would make that protocol executable:

- green row firewall;
- sibling mismatch tolerance before output reveal;
- facility/probe acceptance metrics;
- blind-ID audit logs;
- raw calibration archive;
- `B_min`/`P_oe` information firewall;
- tiered thresholds;
- kill table.

This is real progress as a technology route guardrail. It is not yet a physics breakthrough.

## Breakthrough-Direction Check

Closer, but not there.

We now know the next hard bottleneck:

not "is `C_phi` pretty enough?", but "can a green-row `P_oe+B_min` packet exist without qz/c-axis/matrix-element same-source pollution?"

If yes, the `R_oe` object becomes experimentally decidable.

If no, the independent `C_phi` route dies cleanly for this packet class.

## AHA Check

No new north star stronger than `eta/R_oe`.

But a stronger operational AHA is now stable:

`R_oe` is not a variable until the row firewall exists. Before that, it is only a protocol placeholder.

This should be registered as a guardrail, not as a new theory claim.

## Next Step

Because N=3 is reached, mandatory REVIEWER is triggered next.

Reviewer should attack:

- whether `PACKET_FEASIBLE_NEAR_FUTURE` is still too optimistic;
- whether qz/c-axis/matrix-element firewall is physically impossible;
- whether `N=48/36` is arbitrary protocol theater;
- whether the state machine actually helps technology progress or just delays the hard experiment.
