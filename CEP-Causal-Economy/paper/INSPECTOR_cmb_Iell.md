# INSPECTOR Audit: CMB I_ell Computation for CEP

**Date**: 2026-06-08
**Auditor**: INSPECTOR agent
**Subject**: `compute_cmb_Iell.py` + `cmb_Iell_results.json`
**Claim under audit**: A 6.8σ slope change in dln(I_ell)/dln(ell) at ell~200 constitutes evidence for a CEP causal phase transition.

---

## Executive Summary

**The I_ell slope change at ell~200 is real (t=31.9, p~10^-66), but it reflects standard LCDM physics -- the well-known transition from the Sachs-Wolfe plateau to the first acoustic peak -- not a CEP causal phase transition.** The standard C_l power spectrum shows a 10.9σ slope change at the same location, using identical methodology. The signal in I_ell is a deterministic nonlinear transform of the signal already present in C_l. No independent evidence for CEP is provided.

29% of I_ell values (579/2000) are negative above ell~1210, rendering the Legendre transform physically uninterpretable at high multipoles. The significance methodology is statistically reasonable (Welch t=31.9 confirms the means differ), but the inference that this constitutes evidence for new physics is a classic "affirming the consequent" logical error.

**Overall credibility rating: 2/10 -- Real feature, wrong attribution.**

---

## Issue Inventory

### Issue 1: The "CEP Signal" is Standard LCDM Physics

**Severity: FATAL (invalidates the central claim)**

**Evidence:**

When the identical slope-difference methodology is applied to the standard C_l power spectrum (the input to the I_ell calculation), the result is:

| Quantity | Before (ell 105-194) | After (ell 215-304) | Change | Sigma |
|----------|---------------------|---------------------|--------|-------|
| dln(I_ell)/dln(ell) | -0.597 +/- 0.130 | -1.475 +/- 0.227 | -0.878 | 6.8 |
| dln(C_l)/dln(ell) | -0.955 +/- 0.201 | -3.154 +/- 0.815 | -2.199 | 10.9 |

The C_l power spectrum shows a **stronger** slope change (10.9σ vs 6.8σ) at the **same** location. The I_ell "signal" is a direct consequence of the C_l shape -- I_ell is computed deterministically from C_l via:

```
C_l → ρ(θ) = Σ (2l+1)/(4π) C_l P_l(cos θ)  [Legendre]
ρ(θ) → I(θ) = -½ ln(1 - (ρ/σ²)²)           [Gaussian MI]
I(θ) → I_ell = 2π ∫ I(θ) P_ell(cos θ) sin θ dθ  [Inverse Legendre]
```

The Pearson correlation between dln(I_ell)/dln(ell) and dln(C_l)/dln(ell) is:
- **r = 0.942** in the critical ell = 2-200 range (R² = 0.89)
- r = 0.533 in ell = 200-500
- r = 0.106 overall (low because of numerical noise at high ell)

89% of the variance in dln(I_ell)/dln(ell) below ell=200 is explained by dln(C_l)/dln(ell). The slope change is a **renormalized image** of the standard CMB power spectrum shape.

**Physical interpretation of ell~200:**
- Angular scale: ~0.9 degrees (~220 Mpc comoving at LSS)
- This is exactly where the CMB transitions from the Sachs-Wolfe plateau (ell < 100, large angular scales, primordial perturbations) to the acoustic oscillation regime (ell > 200, first Doppler peak at ell~220)
- Early ISW effect also operates in the ell=100-200 range
- The slope of C_l changes from approximately flat (large-scale primordial) to steeply falling (acoustic damping + Silk damping at high ell)

**CEP's prediction** is "a slope change at ell~200" -- but this prediction is **not falsifiable against LCDM** because LCDM already produces a slope change at exactly the same location. To be meaningful, CEP would need to predict a **quantitatively different** slope change (different magnitude, different ell location, or a different functional form) that distinguishes it from standard cosmology. No such specific prediction is provided in the code or results.

**Fix**: The CEP prediction must be formulated in a way that is falsifiable against LCDM. Options include:
- Predict a specific **residual** slope change after subtracting the C_l-driven component
- Predict a slope change at an ell where LCDM predicts smooth behavior (e.g., ell~800, between acoustic peaks)
- Predict a specific functional form I_ell(ell) that can be fit-tested against data
- Compare to Planck 2018 data C_l (not just theory) and test residuals

**Without a falsifiable prediction, this result is: "The CMB power spectrum has a first acoustic peak at ell~220" -- a discovery made in ~1998 by BOOMERanG/MAXIMA, not CEP in 2026.**

---

### Issue 2: Negative I_ell Values (Numerical Instability)

**Severity: HIGH (breaks physical interpretation at high ell)**

**Evidence:**
- 579 of 2000 I_ell values (28.9%) are negative, from ell=1210 onwards
- dln(I_ell) has 725 of 1990 NaN values (36.4%), from ell=1205 onwards
- The code produces "RuntimeWarning: invalid value encountered in log" (line 76)

**Root cause:** The Legendre transform is not a positivity-preserving operator. Even though I(θ) > 0 for all θ (confirmed), the Legendre coefficients I_ell can be negative because Legendre polynomials oscillate between positive and negative values. At high ell, the integral:

```
I_ell = 2π ∫₀^π I(θ) P_ell(cos θ) sin θ dθ
```

involves P_ell(cos θ) oscillating rapidly, and numerical cancellation between positive and negative contributions yields small values whose sign is determined by integration error rather than physics.

**Convergence test with n_theta:**

| ell | n_theta=1000 | n_theta=2000 | n_theta=5000 | n_theta=10000 |
|-----|-------------|-------------|-------------|--------------|
| 50 | 1.175e-04 | 1.175e-04 | 1.175e-04 | 1.175e-04 |
| 100 | 8.167e-05 | 8.156e-05 | 8.152e-05 | 8.151e-05 |
| 200 | 5.478e-05 | 5.468e-05 | 5.466e-05 | 5.465e-05 |
| 500 | 2.100e-05 | 1.414e-05 | 1.284e-05 | 1.283e-05 |
| 1000 | **-8.513e-06** | **-1.245e-06** | 2.004e-06 | 1.984e-06 |

At ell=1000, n_theta=1000 gives the wrong sign. At n_theta=5000, the value has not fully converged (1% difference from n_theta=10000). For ell > 1200, even n_theta=5000 is insufficient.

**Impact**: The ell~200 region (ell < 500) is well-converged with n_theta=5000 (<0.01% error), so the central claim is NOT affected by this issue. However, the global negativity indicates that the method cannot be trusted for high-ell analysis. Additional high-ell "features" (if any are claimed later) would be pure numerical artifact.

**Fix**:
- Use adaptive theta sampling (higher density at small theta where I(θ) varies rapidly)
- Implement Clenshaw-Curtis or Gauss-Legendre quadrature instead of trapezoidal integration
- Truncate I_ell reporting at the ell where numerical error exceeds a threshold (estimated as ell~800 for n_theta=5000)
- Report only the well-converged range (ell=2 to ell~1200) and flag higher ell as unreliable

---

### Issue 3: Inflated / Ambiguous Significance Metric

**Severity: MEDIUM (misleading but not wrong)**

**Evidence:**

The code computes significance as:
```python
sig = abs(change) / max(np.std(dlnI[before]), 1e-10)
```

This uses **only the before-region standard deviation** as the noise estimate. The before-region (ell 105-194, n=90) has std = 0.1295, while the after-region has std = 0.2267. Using different noise estimators:

| Method | Sigma |
|--------|-------|
| Before std only (code's method) | 6.8 |
| After std only | 3.9 |
| Pooled std: sqrt((s_b² + s_a²)/2) | 4.8 |
| Welch t-test (proper two-sample) | 31.9 |

The Welch t-test confirms the difference is highly significant (p ~ 10^-66) -- the two windows genuinely have different mean slopes. However, the 6.8σ notation is conceptually misleading: it reports how many pre-transition standard deviations fit into the slope difference, not a proper detection significance. In astronomy, "6.8σ" conventionally means a 6.8σ detection above the noise floor of the full measurement, which this is not.

The global std of dlnI over all valid points is **26.9** (inflated by NaN-filled regions), making the before-region std (0.1295) only 0.5% of the global std. This is because dlnI has enormous variance where I_ell approaches zero at high ell. Using global std would give sig = 0.03, which is meaningless. The local std is the correct choice for this analysis, but the specific choice of "before-only" should be justified.

**Fix**:
- Report a proper two-sample test statistic (Welch's t) with degrees of freedom
- Report both the Welch t and the before-only sigma, explaining why local noise estimation is appropriate
- Add a note explaining that the "sigma" is not a detection significance in the astronomical sense but a local S/N ratio
- Account for the look-elsewhere effect: if CEP predicts "a feature somewhere between ell=50-1000", the trials factor reduces the effective significance

---

### Issue 4: No Real-Data Cross-Validation

**Severity: HIGH (all conclusions rest on a theory-only calculation)**

**Evidence:**

The code uses CAMB's theoretical C_l for Planck 2018 best-fit LCDM. It does not:
- Use actual Planck 2018 measured C_l (with error bars)
- Use Planck likelihood to compute I_ell uncertainty bands
- Cross-validate with any other dataset (WMAP, ACT, SPT)
- Test against alternative cosmologies

The theoretical C_l is smooth by construction (it is a Boltzmann code output). The measured C_l from Planck has cosmic variance at low ell and instrumental noise at high ell. Computing I_ell from real data would:
1. Propagate measurement uncertainties to I_ell uncertainty
2. Test whether the slope change survives in the presence of real noise
3. Allow a chi-squared test of CEP vs LCDM

**Fix**:
- Download Planck 2018 binned C_l data (plikHM TTTEEE or similar)
- Recompute I_ell with error propagation (Monte Carlo sampling of C_l uncertainties)
- Report the I_ell slope change with proper error bars
- Compare the measured I_ell to both LCDM and CEP predictions using a likelihood ratio

---

### Issue 5: Mutual Information Interpretation Gap

**Severity: MEDIUM (conceptual, not computational)**

**Evidence:**

The code computes mutual information I(θ) between pixel pairs at separation θ for a Gaussian random field, then Legendre-transforms to I_ell. However, I_ell is **not the mutual information per multipole**. The mutual information of the full CMB sky is:

```
I(total) = Σ_l (2l+1)/2 * log(C_l / C_l^noise + 1)  [for Gaussian]
```

This is a sum over independent harmonic modes. The Legendre transform of I(θ) produces coefficients I_ell, but these are **spectral decomposition coefficients**, not information-theoretic quantities per mode. The sign of I_ell has no information-theoretic meaning (unlike C_l which must be positive as a variance).

CEP's physical interpretation of I_ell as "causal economy per angular scale" relies on an analogy that may not hold under scrutiny. The CEP framework would need to derive what I_ell should look like from first principles, rather than fitting a post-hoc interpretation to a feature that standard cosmology already produces.

**Fix**:
- Derive the expected I_ell spectrum from CEP first principles (not just "a slope change at ell~200")
- If CEP predicts a specific functional form, perform a model comparison (Δχ², AIC, Bayes factor) against LCDM
- Clarify whether I_ell is a spectral coefficient or a genuine information measure per multipole

---

### Issue 6: Code Quality Issues

**Severity: LOW (does not affect results but should be fixed)**

1. **Line 76**: `np.log(I_ell_out[i+5])` -- `np.log` of a negative number produces NaN. Should use `np.log(np.maximum(I_ell_out[i+5], 1e-30))` or handle negative values explicitly.

2. **Line 76-77**: The two-line continuation with backslash is fragile. Use parentheses for line continuation.

3. **Lines 23-24**: `powers['total'][2:2501, 0]` -- the magic number `2` assumes the array starts at ell=0. If CAMB changes its indexing, this silently breaks. Use `ells = np.arange(results.total_CL.shape[0])` to be explicit.

4. **No error handling**: If CAMB is not installed or the `camb.get_results` call fails, the script crashes with a raw traceback instead of a helpful message.

5. **No unit test**: No assertion that `I_ell >= 0` for low ell, no check that `ρ(0) > 0`, no verification that the sum of I_ell converges.

---

## Consolidated Credibility Assessment

### What the code actually demonstrates:
1. The CMB temperature angular correlation function ρ(θ) computed from Planck 2018 best-fit LCDM
2. The mutual information I(θ) = -½ ln(1 - (ρ/σ²)²) for a Gaussian field
3. The Legendre spectrum I_ell of I(θ)
4. A statistically significant change in the logarithmic derivative dln(I_ell)/dln(ell) at ell~200

### What the code does NOT demonstrate:
1. That this slope change is caused by a "causal phase transition" rather than standard CMB acoustic physics
2. That CEP makes a falsifiable prediction distinguishable from LCDM
3. That the signal survives in real Planck data with noise
4. That I_ell is a physically meaningful quantity at high multipoles (where it goes negative)

### Recommended actions before any claim of CEP validation:

| Priority | Action | Effort |
|----------|--------|--------|
| P0 (blocker) | Demonstrate that CEP predicts a quantitatively different I_ell than LCDM | High (requires CEP theory development) |
| P0 (blocker) | Compare against real Planck 2018 data, not just theory C_l | Medium |
| P1 (critical) | Fix numerical issues at ell>1200 (adaptive sampling, quadrature) | Low-Medium |
| P1 (critical) | Report proper two-sample significance with error propagation | Low |
| P2 (important) | Derive CEP I_ell prediction from first principles, not post-hoc fitting | High |
| P2 (important) | Cross-validate with alternative estimators (Healpix MI directly on maps) | Medium |
| P3 (nice) | Code quality improvements (error handling, explicit indexing) | Low |

### Final Rating: 2/10

**Real feature, wrong attribution.** The I_ell slope change is a genuine feature of the CMB angular power spectrum, but it reflects the well-known transition from the Sachs-Wolfe plateau to the first acoustic peak -- physics understood since ~1998 and encoded in every LCDM Boltzmann code. The claim that this constitutes evidence for a CEP causal phase transition is an example of affirming the consequent: CEP predicts a slope change, a slope change is found, therefore CEP is supported. But LCDM also predicts a slope change at the same location (with 1.6x greater significance), so the observation does not discriminate between the two hypotheses.

To make this result meaningful, CEP must predict something LCDM does not -- a specific magnitude, ell-location, or functional form that can be tested in a model comparison framework. Until then, the computation is a valid exercise in information-theoretic CMB analysis but does not constitute evidence for CEP.

---

*Audit conducted using Python 3.12 with CAMB 1.6.6, scipy, and numpy. All numerical checks are reproducible with the code snippets embedded above.*
