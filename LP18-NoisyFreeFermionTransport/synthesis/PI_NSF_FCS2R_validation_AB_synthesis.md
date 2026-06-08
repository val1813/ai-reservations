# NSF-FCS-2R Validation A/B Synthesis

**Date:** 2026-06-03

## Inputs

- A: `current/A/NSF-FCS-2R_validation_A.md`, verdict `DOWNGRADE`.
- B: `current/B/NSF-FCS-2R_validation_B.md`, verdict `REVIEWER_GATE` with mandatory downgrade.
- INSPECTOR-A: `synthesis/inspector_NSF_FCS2R_A_validation.md`, verdict `PASS`.
- INSPECTOR-B: `synthesis/inspector_NSF_FCS2R_B_validation.md`, verdict `WARNING`.

No `BLOCKED` result.

## A/B Convergence

A and B agree on the substantive object:

- no asymptotic `Qhat` or power-law claim;
- no universal FDT anomaly claim;
- no proven second-normal-curvature claim;
- current value is a finite-window, parity-resolved ledger diagnostic.

They disagree on readiness:

- A says `DOWNGRADE`: standard nonequilibrium response / MFT / frenetic-response frameworks may cover much of the interpretation.
- B says `REVIEWER_GATE`: package is gate-ready if framed only as finite-window parity-resolved response algebra.

## PI Decision

**Verdict: REDIRECT, not final REVIEWER gate yet.**

Reason:

The best object has sharpened again. It is no longer just "curvature/separability"; it is:

> parity tomography of finite-volume FDT-residual response channels.

This absorbs the strongest evidence:

- density bias: even `delta^2`;
- equal-density nonLDB skew: even `A^2`;
- nonLDB mixed additivity in the tested window;
- reversible traffic: equilibrium FDT sanity but NESS curvature renormalization.

It also exposes the next decisive missing test:

- whether a signed mixed `delta A` channel appears away from equal density.

B's `REVIEWER_GATE` is acceptable only after this signed mixed-parity ambiguity is either resolved or explicitly bounded. A's downgrade is therefore used as the safer PI route.

## Active North Star

### NSF-FCS-2T: parity tomography of FDT-residual response channels

**One sentence:** In open long-jump exclusion, the finite-volume residual `R2=lambda_T''-2G_T` separates density-gradient curvature, non-LDB activity power, and reversible traffic renormalization by their transformation signatures under `delta -> -delta` and `A -> -A`.

**Conservative score:** `8.7/10` as a qualitative priority, not evidence.

## Required Wording

- Say "finite-window parity-resolved response algebra" or "parity tomography ledger".
- Say `A^2` only for equal-density `nonLDB_site_skew` in the tested protocol.
- Say signed `delta A` is symmetry-allowed and untested; do not say it is established.
- Keep reviewer-gate language conditional.
- Treat standard response/MFT/frenetic-response coverage as an open alternative explanation.

## Next Minimal Test

Run signed mixed-parity scan:

- `L=4..7`
- `alpha=0.5,1.0`
- `rho_bar=0.5`
- `delta=0,+0.02,-0.02,+0.04,-0.04`
- `A=0,+0.05,-0.05,+0.10,-0.10`
- `activity_mode=nonLDB_site_skew,reversible_side`

Fit:

`R2/G_T = c0 + c_delta2 delta^2 + c_A2 A^2 + c_deltaA delta A + c_delta2A2 delta^2 A^2`

Decision:

- if `c_deltaA` is stable and above numerical floor for nonLDB skew, keep parity tomography but weaken equal-density separability to projected-channel language;
- if `c_deltaA` is floor-scale and `c_A2` remains stable, promote finite-window separability toward reviewer gate;
- if reversible mixed defect grows under signed tests, downgrade reversible traffic to uncontrolled NESS coefficient renormalizer.
