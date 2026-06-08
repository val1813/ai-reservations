# PI Synthesis: LP28-CphiCollapse Round 2

## Inputs

- A Round 2: `current-CphiCollapse/A/round2.json`
- B Round 2: `current-CphiCollapse/B/round2.json`
- INSPECTOR A Round 2: warning, not blocker
- INSPECTOR B Round 2: warning, not blocker

## Core Result

Round 2 stabilized the AHA but did not close it.

A made `P_oe` operational:

`P_oe = (chi_odd - chi_even)/(chi_odd + chi_even)`

where `chi_odd` and `chi_even` are normal-state odd/even bilayer susceptibility integrals extracted from q_z / polarization / bilayer form-factor spectroscopy. This is now a measurable candidate in principle, not just a metaphor.

B corrected its no-go:

Universal collapse is too strong. The valid B claim is conditional:

- with a tautological `B_plus` including all kernel terms, collapse is true but not experimentally useful;
- with a measured `B_min`, collapse becomes an empirical test.

Thus the real question is now:

Can measured `B_min` annihilate `P_oe`, or does a stable residual `R_oe` remain?

## Updated Contradiction

A:

`R_oe = P_oe - E[P_oe | B_min]` survives matched-pair testing and is a real input-side phase-transfer residual.

B:

`R_oe` vanishes once `B_min` includes oxygen/layer asymmetry, strain, dz2/RE5d/self-doping, dephasing, pressure path, and c-axis coherence.

## Round 2 Inspector Warnings To Feed Round 3

- define `B_min` separately from tautological `B_plus`
- define denominator floor units for `chi_odd + chi_even`
- close Tc-window leakage risk
- handle negative cross-validated R2
- define gray-zone outcomes for `0.65 < CV-R2 < 0.85`
- prevent small-N covariance overfit
- state `eta/R_oe` normalization
- guard `Z_pre` against hidden output leakage

## Breakthrough-Direction Check

This is now a real theory/experiment hinge:

If `R_oe` survives, nickelate phase-bus readiness is a bilayer parity-transfer residual, not generic c-axis coherence. If it dies, then `C_phi` has no independent content and the phase-bus route should stop.

Both outcomes are useful. This is no longer about writing a paper.

## AHA Check

No new AHA beyond Round 1, but AHA #Cphi-1 is stabilized: the object is `R_oe/eta`, not scalar `C_phi`.

## Round 3 Task

Round 3 must produce a go/no-go decision table:

1. A: exact `P_oe/R_oe` measurement and survival thresholds.
2. B: exact `B_min` baseline set and collapse thresholds.
3. Both: matched-pair design with opposite predictions and gray-zone handling.

## Stop Condition

No hard stop. N=2<3, continue Round 3.

