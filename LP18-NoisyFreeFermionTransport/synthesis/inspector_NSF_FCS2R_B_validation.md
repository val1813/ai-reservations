# INSPECTOR-B: NSF-FCS-2R validation B

**Checked file:** `current/B/NSF-FCS-2R_validation_B.md`  
**Role:** INSPECTOR-B validation only.  
**Boundary:** no prior-art REVIEWER check; did not use A-side validation as evidence.  
**Verdict:** WARNING.

## Q1. Dimensional Check

Ledger convention assumed by the package: the FCS counting field, time, and conductance normalization are already nondimensionalized so that the equilibrium finite-volume identity is `lambda_T'' = 2 G_T`. Under this convention:

1. `R2 = lambda_T'' - 2 G_T`
   - LHS unit: ledger conductance / second cumulant rate unit.
   - RHS unit: `lambda_T''` and `G_T` same ledger unit by FDT normalization.
   - Match: pass, conditional on the stated ledger convention.

2. `R2_density = C_L(alpha) delta^2 + D_L(alpha) delta^4`
   - `delta` is density difference, dimensionless.
   - `C_L`, `D_L` carry the same ledger unit as `R2`.
   - Match: pass.

3. `R2_nonLDB/G_T = b_L(alpha) A^2 + O(A^4)`
   - `R2/G_T` is dimensionless.
   - Activity skew `A` is used as a dimensionless ledger perturbation parameter.
   - `b_L` dimensionless.
   - Match: pass.

4. `Delta_mix = R2(delta,A)-R2(delta,0)-R2(0,A)+R2(0,0)`
   - All terms have the same `R2` unit.
   - Match: pass.

5. `R2/G_T = c0 + c_delta delta^2 + c_A2 A^2 + c_deltaA delta A + c_delta2A2 delta^2 A^2`
   - LHS dimensionless.
   - With dimensionless `delta,A`, all coefficients are dimensionless.
   - Match: pass.

Transcendental arguments: no `exp`, `sin`, `log`, `sinh` formula arguments are introduced in B's validation text.

Q1 result: no dimensional error found. The only condition is preserving the FDT ledger normalization whenever `lambda_T''=2G_T` or `R2/G_T` is used.

## Q2. Sign / Direction Check

1. Density bias direction:
   - B claims centered density bias is even under `delta -> -delta` and starts as `delta^2`.
   - PI coefficient extraction fits raw `R2 = C_L delta^2 + D_L delta^4` for `delta=0.02..0.08`, with `C_L>0` for every tested `L=4..7`, `alpha=0.5,1.0`.
   - Direction: pass.

2. Equal-density nonLDB activity:
   - B claims `A=+a` and `A=-a` collapse to numerical precision and the resolved nonLDB term is `A^2`.
   - PI parity summary gives nonLDB `c_A` around `1e-9` while `c_A2` is `0.00384..0.0130`; odd differences are about `1e-9` or below.
   - Direction: pass.

3. Mixed additivity:
   - B claims nonLDB mixed additivity is good to about `1e-4` relative.
   - PI separability summary reports `nonLDB_site_skew` relative mixed defect `1.04e-4`.
   - Direction: pass.

4. Reversible traffic:
   - B claims `reversible_side` keeps equilibrium residual at numerical floor but changes density-biased curvature coefficient at a few-percent level.
   - PI separability summary reports reversible mixed relative defect `5.88e-2`, and activity parity reports equilibrium residual/fitted coefficients at numerical-floor scale.
   - Direction: pass.

5. New prediction `delta A`:
   - B says at finite density bias nonLDB skew "should generate a symmetry-allowed mixed odd term" and then proposes a signed falsifier.
   - Current PI mixed scans are only at `delta=0.04`, `A=+/-0.10`; they do not fit signed `delta=+/-` data and therefore do not establish nonzero `c_deltaA`.
   - Direction warning: the term is symmetry-allowed and worth testing, but should be phrased as "may generate / is the first allowed place to test sign reappearance", not as an expected nonzero result.

Q2 result: no reversed sign or denominator/numerator inversion found. One warning on predictive wording for `delta A`.

## Q3. Circularity Check

1. `delta^2` claim:
   - Verification data were generated as raw `R2` at multiple deltas, then fitted to `C_L delta^2 + D_L delta^4`.
   - This does not merely divide by `delta^2` first, so the earlier `Qhat` circularity risk is materially avoided.
   - Pass.

2. `A^2` claim:
   - Equal-density parity was checked with both signs and two amplitudes of `A`.
   - The even conclusion comes from sign-paired data, not from imposing an even-only model.
   - Pass.

3. Mixed separability:
   - Mixed rows are compared against density-only plus activity-only predictions.
   - This is a direct residual check rather than a restatement of the fitted model.
   - Pass, finite-window only.

4. REVIEWER_GATE decision:
   - B's gate verdict is a judgment built on PI data plus mandatory downgrades. It is not a numerical derivation.
   - No logical circularity found, but the gate label should remain attached to "finite-window ledger diagnostic", not theorem/asymptotic status.

Q3 result: no blocking circular argument found.

## Q4. Order-of-Magnitude Check

Checked numerical comparisons:

1. Coefficient extraction:
   - Relative fit residuals are `9.60e-6..2.34e-4`.
   - `R2/delta^2` ranges are stable at the `1e-4..1e-3` relative level.
   - No order-of-magnitude mismatch.

2. nonLDB parity:
   - Odd coefficients/differences are about `1e-9`.
   - Even `A^2` coefficients are about `3.8e-3..1.3e-2`.
   - Separation is roughly `10^6..10^7`, supporting B's "collapse to numerical precision" direction.

3. reversible parity:
   - `c_A` and `c_A2` are around `1e-7` or lower, comparable to baseline floor.
   - Supports numerical-floor statement.

4. mixed separability:
   - nonLDB interaction maximum `6.75e-8`, relative `1.04e-4`.
   - reversible interaction maximum `3.23e-5`, relative `5.88e-2`.
   - B's "few-percent" reversible renormalization is consistent with `5.88e-2`.

Q4 result: no order-of-magnitude gap over 3 orders found. The very large odd/even separation should be explicitly tied to the equal-density protocol and current numerical precision.

## Q5. Algebra / Numerical Source Check

1. Additive defect algebra:
   - B uses `Delta_mix = R2(delta,A)-R2(delta,0)-R2(0,A)+R2(0,0)`.
   - This is the correct inclusion-exclusion residual for additivity around baseline.
   - Pass.

2. Fit forms:
   - Density fit `R2 = C_L delta^2 + D_L delta^4` matches PI coefficient extraction.
   - Activity fit `R2/G_T = c0 + c_A A + c_A2 A^2` underlies B's even `A^2` conclusion.
   - Mixed proposed fit basis includes the relevant even and signed mixed terms.
   - Pass.

3. Numerical provenance:
   - B cites PI synthesis files and CSV paths under `current/plan`.
   - Concrete data sources exist: coefficient fit summary, activity parity fit summary, and mixed separability summary.
   - Source level: PI synthesis / local full CSV outputs, adequate for validation.

4. Unsupported numerical specifics:
   - B assigns score `8.7/10`. This is a qualitative strategy score, not a derived number.
   - Warning only: do not treat this score as evidence-bearing.

Q5 result: algebra and numerical sources are adequate. No blocking numerical-source error found.

## Q6. Integrated Judgment

No blocking dimensional, sign, circularity, order-of-magnitude, algebraic, or source-provenance error was found in B's validation file.

Warnings:

1. The `delta A` prediction is scientifically useful, but B's wording at lines 91-95 is stronger than current data support. Current data establish equal-density `A^2` and one-signed-density mixed additivity; they do not establish nonzero signed `c_deltaA`.
2. The `REVIEWER_GATE` label should remain explicitly conditional: finite-window ledger diagnostic only, not analytic theorem, asymptotic scaling claim, or universal response algebra.
3. "Parity tomography" is a good compression but must stay tied to the tested windows `L=4..7`, `alpha=0.5,1.0`, `delta=0.02..0.08`, `A=+/-0.05,+/-0.10`, and current ledger normalization.

## Q6.3 Claim Shrinkage Check

Compared with the previous B line in the same branch, current B shrinks the claim from information-geometric "second normal curvature" and possible linear nonLDB displacement toward a finite-window parity-resolved response algebra with explicit `A^2` equal-density behavior. This shrinkage is justified by the new parity and separability data, and B explicitly states the mandatory downgrade. No penalty-level shrinkage problem found.

## Q6.4 Alternative Explanation Check

B explicitly raises the simpler alternative that equal-density centering projects out a hidden odd nonLDB component, and proposes signed mixed-parity tests to separate "projected channel" from stronger separability. This satisfies the alternative-explanation check at the validation level. The answer is not complete experimentally, but B does not present it as complete.

## Q6.5 Grounding Check

The "no prior blank" type claim is grounded in concrete PI outputs:

- coefficient extraction: multiple `delta` CSVs and fit summary;
- activity parity: equal-density sign-paired `A` CSVs and fit summary;
- separability: mixed `delta=0.04`, `A=+/-0.10` CSVs and summary.

The landing is finite-window and numeric, not merely order-of-magnitude. Pass.

--- 投喂下一轮 ---
阻断级必须修正:
  1. None.

警告级建议修正:
  1. Rephrase the finite-density `delta A` statement from "should generate" to "may generate / is symmetry-allowed and is the first place to test sign reappearance"; current data do not establish nonzero `c_deltaA`.
  2. Keep `REVIEWER_GATE` explicitly conditional on "finite-window ledger diagnostic"; do not let it imply theorem status, asymptotic `L` scaling, or universal response algebra.
  3. Treat the `8.7/10` score as qualitative prioritization only; do not recycle it as quantitative validation evidence.
  4. Preserve all protocol qualifiers for `A^2`: equal density, `nonLDB_site_skew`, tested `A=+/-0.05,+/-0.10`, `L=4..7`, `alpha=0.5,1.0`.
---

Verdict: WARNING
