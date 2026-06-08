# PI Synthesis: LP28-CphiCollapse Round 3

## Inputs

- A Round 3: `current-CphiCollapse/A/round3.json`
- B Round 3 original: `current-CphiCollapse/B/round3.json`
- B Round 3 revised: `current-CphiCollapse/B/round3_revised.json`
- INSPECTOR A Round 3: `WARNING`, no blocker
- INSPECTOR B Round 3: initial `BLOCKER`, then revised recheck `PASS`

## Core Result

Round 3 did not prove that independent `C_phi` exists. It also did not prove collapse.

It did something more useful: it converted the vague scalar `C_phi` problem into a killable object:

`R_oe = P_oe - E_crossfit[P_oe | B_min]`

with

`P_oe = (chi_odd - chi_even) / (chi_odd + chi_even)`

The north-star contradiction is now operational:

- A survives only if a same-sample, leakage-free, denominator-conditioned packet shows residual odd/even bilayer parity-transfer content after measured `B_min` is removed.
- B wins only if measured `B_min`, not tautological `B_plus`, annihilates `R_oe` out of sample under frozen matched-pair / permutation / negative-control tests.

This is a real theoretical hinge, not a paper protocol. It can kill the phase-bus variable or preserve a specific residual object.

## What A Established

A made `P_oe/R_oe` into a candidate variable with execution guards:

- `chi_odd` and `chi_even` must share calibrated `chi_unit`.
- denominator-failed rows are censored, not regularized into artificial `P_oe`.
- temperature grid is frozen and cannot use same-row `Tc`, zero resistance, Meissner, gap, spin resonance, or output-trained labels.
- `B_min` excludes `P_oe`, odd/even kernel residuals, superconducting outputs, and output-trained latent quality.
- small-N, negative `CV_R2`, and `0.65 < CV_R2 < 0.85` are handled as weak/gray-zone rather than discovery claims.

Inspector A warning: this is still a go/no-go protocol. The denominator reference set must be non-circular, and raw `S_channel -> chi_unit` calibration must be explicit before real execution.

## What B Established

B correctly retreated from universal no-go.

`B_plus` is a tautological full-kernel closure and cannot count as empirical evidence. The only meaningful collapse claim is:

measured, pre-registered `B_min` annihilates `R_oe` out of sample.

The first B Round 3 had a blocker: signed pair residual direction was not frozen, and "same-sign abs(Delta_r_pair)" was mathematically invalid. The revised B fixed this:

- primary test becomes direction-free `abs(R_oe_left - R_oe_right)` plus frozen permutation or hierarchical measurement-error null;
- signed tests are allowed only if the orientation axis is frozen before `P_oe/R_oe` extraction and is blind to them;
- qz/c-axis proxies in `B_min` cannot reuse target-generating odd/even susceptibility extraction;
- `U_miss` must have an independent frozen envelope and cannot absorb residuals post hoc;
- batch, sample-quality, and probe-calibration controls are execution requirements.

Inspector B recheck: previous blocker resolved; current status `PASS` with warning that no empirical no-go has been shown.

## Updated AHA

Round 1 AHA is now stabilized:

The true object is not scalar `C_phi`; it is the identity of `eta` in `X_pre = g(B, eta)`.

Round 3 sharpens it:

`eta` is either a measurable odd/even bilayer residual `R_oe`, or it is missing baseline / measurement uncertainty bounded by `B_min + U_miss + epsilon_meas`.

No new north star is stronger than this one yet. The useful AHA is not a new label; it is the signed-to-unsigned correction: survival cannot depend on post-hoc direction. A real residual must survive either direction-free paired magnitude tests or a signed test whose axis was frozen before the residual exists.

## Breakthrough-Direction Check

This moves closer to a real theoretical breakthrough.

If `R_oe` survives, it would change the interpretation of nickelate phase-bus readiness: ordinary c-axis coherence is not enough; an input-side bilayer parity-transfer residual exists. This would open a concrete route for materials screening by normal-state odd/even susceptibility transfer.

If `R_oe` collapses, it kills the current `C_phi/I_phi` route and prevents us from wasting time optimizing relabeled c-axis coherence, sample quality, oxygen disorder, strain, or self-doping.

Estimated impact if true: it would change a meaningful subset of nickelate phase-coherence and screening claims, especially any claim treating c-axis coherence-like observables as a new phase-bus variable without baseline-collapse testing. It opens one new experimental direction: same-sample pressure-row parity-transfer metrology with sealed superconducting outputs.

## Current Decision

No survival/collapse call.

Status: protocol-level north-star resolution is ready; data-level decision is not.

Required packet:

- same-sample pressure or matched-specimen rows;
- qz/polarization/form-factor odd/even susceptibility extraction;
- full measured `B_min` before superconducting output reveal;
- independent raw-to-`chi_unit` calibration;
- frozen denominator reference rule;
- frozen `U_miss` envelope;
- batch, sample-quality, and probe-calibration controls.

## Next Context For REVIEWER

Attack the strongest version:

`R_oe` is a real independent input-side bilayer parity-transfer residual if and only if it survives `B_min` residualization in a leakage-free same-sample packet under denominator censoring, frozen `U_miss`, and direction-free paired residual / pre-frozen signed-axis tests.

Reject if:

- this is still just c-axis coherence or sample quality in odd/even notation;
- `B_min` quietly contains target-generating qz/odd-even information;
- the denominator / calibration / temperature window can manufacture `P_oe`;
- sample count and controls cannot support any non-gray-zone call.

## Stop Condition

N = 3 is reached. Mandatory REVIEWER is triggered next.
