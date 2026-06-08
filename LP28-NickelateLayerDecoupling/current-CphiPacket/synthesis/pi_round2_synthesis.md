# PI Synthesis: LP28-CphiPacket Round 2

## Inputs

- A Round 2: `current-CphiPacket/A/round2.json`
- B Round 2: `current-CphiPacket/B/round2.json`
- INSPECTOR A Round 2: `WARNING`, no blocker
- INSPECTOR B Round 2: `WARNING`, no blocker

## Core Result

Round 2 turned the packet problem into a tiered gate.

A showed that a prospective row schema is internally coherent.

B showed that a claim-bearing packet needs much stricter independence, batch/lab separation, and held-out validation than A's minimum executability threshold.

The unified result:

1. `N=12`: rehearsal only.
2. `N=24`, `>=18` valid uncensored `P_oe` rows, `>=2` batches: minimum executable protocol, not claim-bearing.
3. `N=48`, `>=36` complete rows, `>=4` batches, `>=3` labs, leave-one-batch/lab-out validation: decision-grade / B-concession target.

These are protocol gates, not statistical power theorems and not laws of nature.

## P_oe Standardization

Round 1 definition drift is fixed.

Canonical:

`P_oe = (chi_odd - chi_even)/(chi_odd + chi_even)`

The denominator floor censors rows; it does not replace the denominator.

Allowed diagnostic:

`P_oe_L1_diagnostic = (chi_odd - chi_even)/max(abs(chi_odd)+abs(chi_even), epsilon_L1)`

This diagnostic cannot substitute for canonical `P_oe` in the primary residual-collapse call.

## Current Packet Gate

The packet is still not found.

The packet is now prospective and schema-defined:

- row genealogy;
- frozen q/omega/qz/polarization/T/P grid;
- raw spectra and calibration archive;
- canonical `P_oe` with censoring;
- full `B_min`;
- frozen `U_miss`;
- output-label custodian;
- B_min/P_oe firewall;
- timestamped blind-ID audit;
- batch/lab/probe controls.

## Main Remaining Risk

The decisive risk is still qz/c-axis/matrix-element same-source pollution.

If ordinary c-axis coherence or qz proxies inside `B_min` require the same odd/even fitted state, channel-mixing nuisance terms, or RIXS background choices used to compute `P_oe`, the packet is non-identifiable.

Round 3 must harden this into an audit table:

- green rows: independent enough for primary analysis;
- yellow rows: sensitivity-only;
- red rows: excluded / protocol failure.

## Sibling / Montage Risk

A's same-sample vs sibling rules are useful but not yet sufficient.

Round 3 must define pre-output mismatch tolerances for:

- oxygen microtexture;
- phase fraction;
- pressure path;
- beam damage;
- c-axis state;
- sample quality.

Rows cannot be rescued by comparing sibling mismatch to observed residuals after the fact.

## Breakthrough-Direction Check

This is closer to actual progress than Round 1 because it creates a concrete gate that can stop the project:

- if the green-row firewall cannot be satisfied, `R_oe` remains protocol-only;
- if a decision-grade packet can be designed, `R_oe` becomes experimentally decidable.

Still not a breakthrough. It is a decision architecture for whether a breakthrough object can be tested.

## AHA Check

No new AHA stronger than `eta/R_oe`.

But the live contradiction sharpened:

`R_oe` requires not just data, but row-level independence between the qz odd/even extraction state and the baseline state. If those cannot be separated, the object is not merely unmeasured; it is non-identifiable for this packet class.

## Round 3 Task

A must produce a final feasible packet protocol:

- green/yellow/red row firewall;
- pre-output sibling mismatch tolerances;
- facility/probe acceptance metrics;
- exact minimum vs decision-grade thresholds;
- what counts as executable in near future.

B must produce the final kill table:

- which violations make the packet `NOT_FOUND`, `NON_DECISION_GRADE`, `NON_IDENTIFIABLE`, or `PROTOCOL_FAILURE`;
- which conditions force B to concede `PACKET_FEASIBLE_NEAR_FUTURE`;
- whether any structural incompatibility remains after the firewall.

## Stop Condition

N = 2 < 3. No hard stop. Continue Round 3.
