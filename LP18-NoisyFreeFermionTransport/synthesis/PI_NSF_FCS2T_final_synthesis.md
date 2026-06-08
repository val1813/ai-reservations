# PI NSF-FCS-2T Final Synthesis

**Date:** 2026-06-03

## Current Claim

NSF-FCS-2T:

> In the tested finite-volume long-jump open-exclusion ledger, `R2=lambda_T''-2G_T` acts as a parity-tomography diagnostic: centered density bias contributes an even `delta^2` channel, equal-density nonLDB site skew contributes an even `A^2` channel, the signed mixed `delta A` channel is numerical-floor in the tested window, and reversible LDB traffic preserves equilibrium FDT while renormalizing density-biased NESS coefficients.

Mandatory scope:

- finite-window only;
- dimensionless Markov-affinity ledger convention;
- not theorem;
- not universal FDT anomaly;
- not asymptotic scaling.

## Evidence Package

Completed and retained:

- REVIEWER Round 2 response:
  - raw `R2~delta^2`;
  - off-center reverse bias;
  - FDT normalization;
  - `Qhat` model comparison downgrade;
  - activity split.
- NSF-FCS-2R:
  - coefficient extraction `R2=C_L delta^2 + D_L delta^4`;
  - activity parity: equal-density nonLDB response is `A^2`, not `A`;
  - mixed separability: nonLDB additive, reversible traffic renormalizes NESS.
- NSF-FCS-2T:
  - signed mixed grid over `delta=0,±0.02,±0.04`, `A=0,±0.05,±0.10`;
  - `c_deltaA` remains numerical-floor for nonLDB in `L=4..7`, `alpha=0.5,1.0`;
  - reversible traffic is not a strict null.

## Reviewer Outcome

Independent REVIEWER recommendation: `major revision`.

PI verification:

- no direct duplicate found;
- no direct contradiction found;
- no citation fabrication found;
- standard-framework coverage risk is real.

Confirmed relevant coverage frameworks:

- Baiesi-Maes-Wynants nonequilibrium linear response / frenetic terms;
- Seifert-Speck NESS FDT;
- Bertini et al. MFT;
- open-exclusion FCS/current statistics;
- long-jump reservoir exclusion / fractional Fick-law background.

## PI Verdict

**Major revision continuation.**

Do not close. Do not claim acceptance. The data package is coherent and valuable, but the novelty bar is not yet met against standard response/FCS frameworks.

## Required Next Work

1. Symmetry derivation:
   derive from the finite Markov generator and protocol symmetries why `delta`, `A`, and `delta A` vanish in the centered nonLDB protocol.

2. Ledger convention proof:
   write a self-contained normalization note for `lambda_T''=2G_T`, including counting field, time unit, conductance unit, and factor 2.

3. Numerical-floor robustness:
   rerun the signed mixed fit with precision/fit-window checks:
   - `eps` grids;
   - `delta,A` window variation;
   - alternative basis with/without higher terms;
   - residual and condition-number reporting.

4. Framework positioning:
   explicitly state what NSF-FCS-2T adds beyond frenetic response, Seifert-Speck NESS FDT, MFT, and open-exclusion FCS.

5. Reversible traffic:
   either analytically separate reversible traffic as coefficient renormalization or demote it to a caveated control only.

## Next Phase

Open `NSF-FCS-2T major-revision response` phase. First task: finite Markov-generator symmetry derivation for parity constraints.
