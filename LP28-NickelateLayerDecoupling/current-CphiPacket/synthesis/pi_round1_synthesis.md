# PI Synthesis: LP28-CphiPacket Round 1

## Inputs

- A Round 1: `current-CphiPacket/A/round1.json`
- B Round 1: `current-CphiPacket/B/round1.json`
- INSPECTOR A Round 1: `WARNING`, no blocker
- INSPECTOR B Round 1: `WARNING`, no blocker
- R1 prior-art/citation check: `synthesis/r1_prior_art_check.md`

## Core Result

Round 1 produced a clean contradiction:

- A: `PACKET_FEASIBLE_NEAR_FUTURE`
- B: `PACKET_NONIDENTIFIABLE_FROM_CURRENT_LITERATURE`

Both agree on the most important negative result:

There is no identified existing leakage-clean same-sample or matched-specimen `P_oe + B_min` packet.

The conflict is now sharper:

Can a new sealed packet be engineered, or is the required independence between `P_oe` and `B_min` physically/metrical fiction?

## A-Side Value

A gives a concrete campaign architecture:

- same-boule or sister-specimen genealogy;
- qz/polarization/form-factor RIXS or neutron/RIXS hybrid for odd/even susceptibility;
- independent oxygen, structure, orbital, disorder, pressure-path, c-axis coherence, and sample-quality blocks;
- output blinding before residual call;
- raw calibration archive, denominator censoring, frozen `U_miss`, batch/sample/probe controls.

This is real progress as protocol architecture, but not evidence.

## B-Side Value

B correctly blocks retrospective montage:

Rows assembled from different papers, probes, pressure paths, oxygen histories, or known superconducting samples are not rows.

B's core non-identifiability objection is specific:

the same latent variables shape both `P_oe` and `B_min`, especially qz/c-axis coherence, pressure path, oxygen/vacancy state, phase fraction, orbital/self-doping balance, matrix elements, and sample quality.

B does not claim universal impossibility. It gives a falsifier: a newly sealed same-sample or genuinely sister-specimen experiment with raw calibration and blinded outputs.

## Inspector Warnings Carried Forward

1. `P_oe` definition drift:

Previous north-star definition:

`P_oe = (chi_odd - chi_even)/(chi_odd + chi_even)`

A Round 1 used a stabilized L1-like denominator:

`(chi_odd - chi_even)/max(abs(chi_odd)+abs(chi_even), epsilon_floor)`

Round 2 must standardize this. The canonical object remains the signed-sum definition with censoring/floor rules, not an unannounced new observable. If an L1-stabilized diagnostic is useful, it must be renamed, e.g. `P_oe_L1`, and not compared directly to prior `P_oe`.

2. `B_min` independence is not proven.

Separate scripts and row IDs are necessary but insufficient. Round 2 must define what information is forbidden to cross from the `P_oe` extraction pipeline into `B_min`.

3. Falsifier threshold is too vague.

B's "several independent rows" must become a concrete threshold: minimum rows, minimum batches, required axes, and what counts as batch/lab independence.

4. Citation hygiene:

Use verified anchors where possible. Research Square and ACS SI component records are not final anchors without parent verification.

## Breakthrough-Direction Check

This round moves closer to actual progress, but not to breakthrough yet.

It prevents a false move: retrospective literature montage cannot decide `R_oe`.

It opens the only serious route: a sealed packet campaign or a proof that such a campaign is non-identifiable.

If Round 2 can quantify the row/batch/calibration requirements and show they are feasible, this becomes a real experimental-theory program. If it shows the requirements are mutually incompatible, it kills the `R_oe` route cleanly.

## AHA Check

No new AHA stronger than the existing `eta/R_oe` object.

But Round 1 adds a useful constraint:

`R_oe` is not data-minable from literature. It is either produced by a sealed row-level packet, or it remains protocol-only.

This should be treated as a guardrail, not a new north star.

## Round 2 Task

A must:

- standardize `P_oe` without definition drift;
- turn the near-future packet into a row schema with minimum `N`, batches, controls, and actual probe order;
- identify which fields can be acquired same-sample vs sister-specimen.

B must:

- quantify the falsifier threshold;
- define exact independence criteria for `B_min` vs `P_oe`;
- state whether any near-future campaign can satisfy them, or whether the incompatibility is structural.

## Stop Condition

N = 1 < 3. No hard stop. Continue Round 2.
