# NSF-FCS-2 Round 2 A/B Synthesis

**Date:** 2026-06-03

## Inputs

- A output: `current/A/NSF-FCS-2_round2_A.md`, verdict `KEEP`.
- B output: `current/B/NSF-FCS-2_round2_B.md`, verdict `REDIRECT`.
- INSPECTOR-A: `synthesis/inspector_NSF_FCS2_A_round2.md`, verdict `WARNING`.
- INSPECTOR-B: `synthesis/inspector_NSF_FCS2_B_round2.md`, verdict `WARNING`.

No INSPECTOR output is `BLOCKED`.

## A/B convergence

A and B disagree on the label but converge on the operational content:

- Keep the Round 2 data package: FDT normalization, raw `R2~delta^2`, off-center reverse-bias sanity, model comparison, and activity split are real progress.
- Abandon exponent-centered language: no `Qhat~L^{1/2}`, no asymptotic power-law claim, no `3/2-alpha` story.
- Treat the strongest object as finite-volume response geometry: density-bias NESS creates an even-in-bias displacement from the equilibrium FDT surface, while `reversible_side` and `nonLDB_site_skew` separate LDB traffic from genuine non-LDB forcing.

## INSPECTOR constraints

Carry forward as hard wording constraints:

- Use "curvature-like normal coordinate" or "finite-volume curvature response"; do not state that `R2/G_T` is a proven geometric second normal curvature unless a metric/projection definition is supplied.
- Do not claim an `A`-linear non-LDB response without testing `A=+a,-a` or fitting both `A` and `A^2`.
- Every `Qhat(L)` statement must say finite-window / model-underdetermined; log drift currently beats power-law ansatz.
- Numerical claims need explicit provenance when promoted beyond synthesis: CSV path, script, parameters, fit window, and command.
- Register the claim shrinkage: this is no longer an asymptotic scaling/exponent discovery program.

## PI verdict

**Verdict: REDIRECT-within-KEEP.**

The NSF-FCS-2 data package remains valuable and should not be killed. But the current north-star wording must be sharpened away from "NESS FDT residual scaling" toward a finite-volume diagnostic:

> NSF-FCS-2R: long-jump open exclusion 的 finite-volume FDT-residual curvature/separability diagnostic.

One-sentence claim:

> In the ledger's dimensionless Markov-affinity convention, the robust object is the even-in-density-bias finite-volume residual `R2=lambda_T''-2G_T`, treated as an operational curvature-like coordinate away from the equilibrium FDT surface, with `reversible_side` and `nonLDB_site_skew` separating LDB traffic from non-LDB forcing.

Conservative score: `8.4/10`.

Reason for score reduction from the old `9.0/10`:

- impact remains high because the diagnostic is sharp and reviewer attacks were answered;
- risk is lower on normalization/circularity, but the claim level is smaller;
- no asymptotic scaling has been established.

## Next minimal proposition

Do not resume broad `Qhat(L)` scaling yet. Next run should test the curvature/separability subclaim:

1. Coefficient extraction:
   `R2(L,delta,alpha)=C_L(alpha) delta^2 + D_L(alpha) delta^4 + o(delta^4)` at fixed `L,alpha`.
2. Activity parity:
   compare `A=+a,-a` for `nonLDB_site_skew` and `reversible_side`; fit both `A` and `A^2`.
3. Mixed perturbation:
   fit `R2/G_T = c0 + c_delta delta^2 + c_A A + c_A2 A^2 + c_deltaA delta A` only after the `A` parity is known.

Minimum ledger window:

- `L=4..7`
- `alpha=0.5,1.0`
- `rho_bar=0.5`
- `delta=0,0.02,0.04,0.06`
- `A=0,+0.05,-0.05`
- `activity_mode=none,reversible_side,nonLDB_site_skew`

## Decision

Proceed with NSF-FCS-2R as the active sharpened subclaim. Update project queue/current status, then append a new Phase block for the coefficient/parity validation.
