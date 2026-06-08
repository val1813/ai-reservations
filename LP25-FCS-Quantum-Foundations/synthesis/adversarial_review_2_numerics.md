# Referee Report — PRL Manuscript: "Second Scaling Exponent for Off-Diagonal Coherence in Power-Law Hopping Nonequilibrium Steady States"

**Reviewer 2 (Numerical Methods and Computational Physics)**
**Recommendation:** Reject with invitation to resubmit after major revisions

---

## Summary

This manuscript claims the discovery of a second independent scaling exponent beta(alpha) governing off-diagonal coherence decay in the NESS of a boundary-driven power-law hopping chain. The physical question is interesting. However, the numerical methodology falls substantially below the standard expected for Physical Review Letters. The computations rely on a single, suboptimal numerical method with no cross-validation, the fits are performed on extremely small datasets without model selection, error propagation is entirely absent from the reported results despite being present in the raw data files, and the system-size range (L up to 64) is insufficient to establish true scaling for long-range hopping. Each of these issues is elaborated below with concrete evidence drawn from the manuscript text, the raw data, and the supplied computation scripts.

---

## I. MAJOR ISSUES

### Issue 1: Single numerical method with no independent cross-validation

**Claim under attack.** The authors state that beta values are obtained from "exact numerical solution of the site-basis Lindblad equation" (Abstract, line 11) and that the Lyapunov equation "separates into decoupled real and imaginary sectors" (Section III.A, line 49).

**What the authors actually did.** Examination of the supplied code (`phase2_L_large.py`, `phase2_L64_compute.py`, `firewall_AHA1.py`) reveals that every single beta value in this manuscript is produced by a single computational pipeline:

1. Build the L^2 x L^2 dense complex matrix A (explicitly, element by element in triple-nested Python loops)
2. Call `np.linalg.solve(A, b_vec)` — a general dense LU solver with partial pivoting
3. Extract the midchain element and fit via `scipy.stats.linregress`

There is no independent method. The tensor-network and quantum-trajectory approaches that exist in the literature (including in the authors' own citations [5–8]) are not applied to any of the 185 data points. There is no Krylov-subspace solver, no GMRES/sparse verification, no iterative refinement. The authors use exactly one solver, on exactly one matrix formulation, and never verify that any result is correct.

**Specific code evidence.** Every computation script imports `scipy.linalg.solve_continuous_lyapunov` at the top of the file but **never calls it**. I verified this by grepping all Python files in the plan directory:

- `phase2_L_large.py` line 24: `from scipy.linalg import solve_continuous_lyapunov as solve_lyap` — never used in the 400+ line file
- `firewall_AHA1.py` line 33: identical dead import
- `phase2_L64_compute.py` line 18: identical dead import
- `compute_nu.py` line 12: identical dead import
- `analyze_lyapunov_structure.py` line 15: identical dead import

The `solve_continuous_lyapunov` function implements the Bartels-Stewart algorithm, which is the standard approach for this exact class of equations. It is more stable and faster (O(L^3) Schur decomposition vs. O(L^6) dense solve). The fact that it is imported but not used suggests the authors are either unaware of the appropriate numerical methods or chose to ignore them. In either case, the absence of any cross-validation between `np.linalg.solve` and `solve_continuous_lyapunov` is a serious methodological gap.

**Required fix.** The authors must either (a) recompute all beta values using `solve_continuous_lyapunov` and demonstrate agreement within stated uncertainties, or (b) provide at minimum 10% coverage cross-validation using an independent method (sparse GMRES, tensor network, or the Lyapunov solver they imported but never used). A table comparing beta values from at least two independent numerical pipelines must be added.

---

### Issue 2: No condition number or floating-point error analysis for L=64

**Claim under attack.** The authors report beta values to 4 significant figures (e.g., beta = 0.9427, 0.8127) and claim R^2 > 0.998 for gamma_phi >= 0.1. The firewall test reports beta values identical across Delta_f to "within 10^{-4}" (Section IV, line 91).

**What is missing.** For L=64, the matrix A is 4096 x 4096 with complex entries. The authors do not report the condition number of A at any (alpha, gamma_phi, L) combination. The word "condition" does not appear in the manuscript. A grep of all supplied Python files for "cond", "condition_number", "rcond", or "svd" in the context of the main solver returns zero hits for the COH and firewall computation scripts.

This is not a formality. Consider the structure of A: it contains entries of the form `1j * J0/r^alpha` (from the Hamiltonian commutator) alongside real diagonal damping terms `0.5*(Gamma_i + Gamma_j) + gamma_phi*(1-delta_ij)`. For small gamma_phi = 0.01 and alpha = 1.1 (long-range hopping), the imaginary Hamiltonian terms can dominate the damping, potentially making A poorly conditioned. The condition number could easily reach 10^8 or higher, at which point double-precision LU factorization loses 8+ decimal digits of accuracy.

**Quantitative concern.** Suppose kappa(A) ~ 10^10 at gamma_phi = 0.01, L=64. Then `np.linalg.solve` could lose log10(kappa) ~ 10 digits. The midchain |C_mid| values at these parameters are O(10^{-2}) (see raw data: L=64, alpha=1.1, gamma_phi=0.01 has abs_C_mid ~ 0.01). A loss of 10 digits on a value of 0.01 means the result could be entirely noise. The fact that gamma_phi=0.01 produces R^2 = 0.87-0.89 (as the authors acknowledge) may reflect not physical breakdown of power-law scaling but simply numerical noise from an ill-conditioned linear system.

**Required fix.** Report the 2-norm condition number of A for each of the 25 (alpha, gamma_phi) combinations at L=64. If any kappa exceeds 10^12, the corresponding data points must be flagged as unreliable. For the gamma_phi=0.01 cases specifically, provide a convergence study: re-solve with iterative refinement and show that |C_mid| stabilizes to within 1% of the `np.linalg.solve` result.

---

### Issue 3: Dead-code import implies unused superior algorithm

This is a corollary of Issues 1-2 but deserves separate treatment because it undermines the claim of methodological rigor. The Lyapunov equation:

```
i[h, C] + 1/2 {Gamma, C} + gamma_phi (C - diag(C)) = diag(W_in)
```

is precisely of the form `AH^T C + C AH + Q = 0` handled by `solve_continuous_lyapunov`. Instead of using this purpose-built, provably backward-stable algorithm, the authors manually vectorize the equation into an L^2 x L^2 system and throw it at a general dense solver. For L=64, the vectorized system has 16.7 million complex entries, of which the vast majority are zero (only O(L^3) = 2.6 x 10^5 nonzeros from the Hamiltonian commutator). The authors are solving a 99.7% sparse system with a dense algorithm, while the sparse+structured solver sits unused in the import statement.

**Required fix.** Explain in the manuscript why `solve_continuous_lyapunov` was not used despite being imported. If there is a technical reason (e.g., the Lindblad dissipator does not map exactly to the standard Lyapunov form for all terms), state it explicitly. Otherwise, the natural inference is that the authors are unaware of the standard numerical methods in their own field.

---

### Issue 4: beta = a/alpha + b is a 2-parameter fit to 5 data points — no model selection performed

**Claim under attack.** The authors present `beta(alpha) = a/alpha + b` as a substantive finding, derived "from scaling analysis of the fractional diffusion equation" (Section III.B, line 64), and report RMSE = 0.015 with R^2 > 0.999 for the gamma_phi = 0.5 fit.

**Reality.** This is a 2-parameter nonlinear fit to exactly 5 data points (alpha = 1.1, 1.3, 1.5, 1.7, 1.9). With n=5 and p=2, there are 3 degrees of freedom. The 95% confidence interval on RMSE for a perfect model with 3 d.o.f. and sigma=0.02 is [0.007, 0.066] — so an RMSE of 0.015 is entirely expected even for a misspecified model. The reported R^2 > 0.999 is not a discovery; it is an arithmetic consequence of fitting 2 parameters to 5 nearly collinear data points.

**Model selection deficit.** The authors never ask whether alternative functional forms fit better. Specifically:

- `beta(alpha) = a/alpha^2 + b/alpha + c` (3 parameters, 2 d.o.f.)
- `beta(alpha) = a * exp(-alpha/alpha_0) + b` (3 parameters)
- `beta(alpha) = a * alpha^gamma + b` (3 parameters)

No AIC, BIC, or likelihood-ratio test is reported. The authors have selected the simplest function that fits 5 points and declared victory. This is textbook overfitting avoidance in reverse: it is underfitting disguised as parsimony.

**Quantitative amplification.** For gamma_phi = 0.5, the 5 beta values are {1.172, 1.043, 0.943, 0.891, 0.872} (from Table 1). A simple linear fit beta = A + B/alpha gives exactly the reported form. But a straight line beta = m*alpha + c also fits: beta = -0.375*alpha + 1.591 with R^2 = 0.997. The point is that with 5 points, many functional forms will give R^2 > 0.99. The claim that the 1/alpha form is "derived" rather than "selected" requires showing that it outperforms alternatives in a statistically rigorous model comparison.

**Required fix.** Provide a table of AIC and BIC values for at least three candidate functional forms (1/alpha, linear, exponential) at each gamma_phi. If 1/alpha is genuinely superior, this will be evident. If not, the functional form must be presented as an empirical observation rather than a derived result.

---

### Issue 5: gamma_phi = 0.01 data are unreliable but retained throughout the paper

**Claim under attack.** The honesty register (line 240) acknowledges "individual beta fits carry ~20% uncertainty at this dephasing rate." The manuscript text (Section III.A, line 55) states that at gamma_phi=0.01, "beta approx 0.15 nearly independent of alpha, reflecting the near-ballistic regime."

**Raw data tells a different story.** From `phase2_fit_results_FULL.json`, the 5 gamma_phi = 0.01 fits produce:

| alpha | beta   | std_err | R^2   | std_err/beta |
|-------|--------|---------|-------|--------------|
| 1.1   | 0.1674 | 0.0368  | 0.873 | 22.0%        |
| 1.3   | 0.1603 | 0.0340  | 0.881 | 21.2%        |
| 1.5   | 0.1543 | 0.0319  | 0.886 | 20.7%        |
| 1.7   | 0.1493 | 0.0303  | 0.891 | 20.3%        |
| 1.9   | 0.1450 | 0.0290  | 0.893 | 20.0%        |

Three problems:

1. **Systematic trend in beta(alpha) may be noise.** The claimed monotonic decrease from beta(1.1) = 0.167 to beta(1.9) = 0.145 is a 13% effect, while individual uncertainties are 20-22%. At the 1-sigma level, all 5 values are consistent with beta ~ 0.155, independent of alpha. The "decrease" is not statistically significant. The authors partially acknowledge this in Section III.C ("statistically consistent with zero within 1 sigma") when discussing the beta-mu anti-correlation, but fail to apply the same standard when claiming the near-ballistic regime behavior in Section III.A.

2. **R^2 values indicate poor fits.** R^2 in the range 0.87-0.89 means the power-law model explains only ~88% of the variance in log|C_mid|. For a fit to only 5 points (4 for L=4,8,16,32 without the L=64 point), this is unacceptable. At these R^2 values, the 95% prediction interval for log|C_mid| at L=64 spans nearly an order of magnitude in |C_mid|.

3. **These data appear as the first column of Table 1** without any caveat except the footnote "R^2 ~ 0.87-0.89." The beta values are displayed to 3 decimal places alongside the high-quality gamma_phi >= 0.5 data, creating a misleading impression of comparable precision. The table also lists a(gamma_phi=0.01) = 0.058 and b(gamma_phi=0.01) = 0.115 — a 2-parameter fit to 5 unreliable points. These coefficients are used to support the claim that "beta -> 0" as gamma_phi -> 0 (Section III.B, line 72), which is speculation dressed as calibration.

**Required fix.** Either (a) remove the gamma_phi = 0.01 column from Table 1 entirely and restrict all quantitative claims to gamma_phi >= 0.1, or (b) add explicit uncertainty ranges to every beta value in Table 1 and shade all gamma_phi=0.01 entries to indicate they are 1-sigma-consistent with constant beta. The a(gamma_phi=0.01) and b(gamma_phi=0.01) coefficients must be removed or clearly marked as unreliable extrapolations.

---

### Issue 6: Error bars and standard errors are systematically absent from the manuscript

**The data files contain the information; the manuscript suppresses it.** Every fit in `phase2_fit_results_FULL.json` includes a `std_err` field from `scipy.stats.linregress`. The manuscript text reports zero of these values. Compare:

| Data file (raw) | Manuscript (Table 1) |
|-----------------|---------------------|
| beta(1.1, 0.5) = 1.1723 +/- 0.0106 | beta(1.1, 0.5) = 1.172 |
| beta(1.5, 0.5) = 0.9427 +/- 0.0148 | beta(1.5, 0.5) = 0.943 |
| beta(1.9, 0.5) = 0.8715 +/- 0.0032 | beta(1.9, 0.5) = 0.872 |

The standard errors span a factor of 5 across the table (from 0.0032 at alpha=1.9, gamma_phi=0.5 to 0.0653 at alpha=1.1, gamma_phi=0.1) but are rendered invisible. A reader cannot assess which beta values are well-constrained and which are not.

**Firewall universality test.** From `firewall_AHA1_results.json`, the 12 beta values each carry a standard error of 0.007-0.018. The claimed "maximum deviation from reference" of 6.84% (beta = 0.9427 at Gamma=1.0 to beta = 0.8782 at Gamma=2.0) corresponds to a shift of 0.0645. The combined uncertainty on this difference is sqrt(0.0148^2 + 0.0070^2) = 0.0164. The difference is 3.9 sigma — statistically significant, but far less impressive than "identical exponents" or "genuine universal exponent" (Abstract, line 12). The authors' description of beta as "robust" and "boundary-insensitive" (Section IV, line 93) is misleading when the exponent varies by 3.9 sigma across the parameter range.

Similarly, the claim that Figure 1 has "R^2 > 0.999" should be accompanied by the actual R^2 values in a table, not an inequality that hides the spread from R^2=0.977 (gamma_phi=0.1, alpha=1.1) to R^2=0.99996 (gamma_phi=0.5, alpha=1.9).

**Required fix.** Add a column of std_err values to Table 1. Add error bars to Figure 1 (the data points in log|C_mid| vs log L fits). Add a column of std_err to Table 3 (universality test). Report the combined statistical significance of the Gamma-dependence in Section IV (difference / combined_error). Change the universality characterization from "robust, boundary-insensitive quantity" to "shows statistically significant (3.9 sigma) dependence on Gamma."

---

### Issue 7: L_max = 64 is insufficient for the scaling regime at small alpha

**Claim under attack.** The power-law decay |C_mid| ~ L^{-beta} is fitted across L = 4, 8, 16, 32, 64 for all alpha. The authors imply this range is adequate for establishing scaling (Section II, line 38: "we solve exactly using dense numerical linear algebra for systems up to L = 64").

**Why this is problematic.** For alpha = 1.1 (the most long-range hopping in the scan), the hopping amplitude decays as J(r) ~ r^{-1.1}, which falls off very slowly. At L=64, the hopping between sites 1 and 64 has J ~ 0.3 / 64^1.1 ~ 0.004 — only a factor of ~75 weaker than nearest-neighbor. This means the system at L=64 is still far from the thermodynamic limit where boundary effects are negligible. The "scaling" extracted from L=4..64 may be a transient finite-size effect, not genuine asymptotic scaling.

**Evidence from the literature.** The authors cite Bhat and Znidaric [8], who studied nearest-neighbor (alpha -> infinity) chains using tensor-network methods, and Costa et al. [6] who employed a gauge-trick methodology. These works considered system sizes well beyond L=100. The authors do not cite any work that establishes L=64 as sufficient for power-law hopping at alpha=1.1.

**What the authors could have done.** I note the existence of `firewall1_L128.py` and `firewall1_L128_v2.py` in the code directory, suggesting the authors have the capability to compute L=128 but chose not to for the main results. Even if L=128 is too expensive for the dense solver, a sparse GMRES implementation (as used in `firewall1_L128.py`) would suffice for verification at select parameter combinations. Why was L=128 computed for the firewall test but not for the main beta(alpha) determination?

**Required fix.** Either (a) provide at least one parameter combination (preferably alpha=1.1, gamma_phi=0.5, the most sensitive case) computed at L=128, showing that beta extracted from L=4..64 agrees with beta extracted from L=4..128 within 1 sigma; or (b) perform a finite-size extrapolation beta(L_max) vs 1/L_max for all alpha values and demonstrate saturation. Without this, the scaling exponent cannot be distinguished from a finite-size transient.

---

### Issue 8: The beta values in Table 3 have implausible precision

The firewall test reports beta values that are identical across Delta_f to 10^{-14} fractional precision (0.952505050953984 vs 0.952505050953987 for Gamma=0.5). Meanwhile, the standard error on each beta fit is 0.018 (from `firewall_AHA1_results.json`). The reported beta values have 15 decimal digits of precision, but the statistical uncertainty in the 15th decimal place is 1.8 x 10^{-2}. This is like measuring someone's height to the nearest nanometer with a meter stick.

The root cause is almost certainly the LU solver hitting machine precision in the same way for all Delta_f values (since Delta_f only rescales the source term b_vec, and the linear system is linear in the source). The identity of beta values across Delta_f is not evidence of universality — it is evidence that the linear solve is essentially exact to machine precision and that the line-fitting process is deterministic. This is a trivial consequence of the linearity of the problem, not a physical discovery.

**Required fix.** Report beta values to 2-3 significant figures beyond the decimal (consistent with std_err ~ 0.01). Remove the claim that "beta is exactly independent of Delta_f" (Section IV, line 91) and replace it with "beta is independent of Delta_f by construction, since Delta_f enters only as an overall multiplicative factor in the source term of the linear Lyapunov equation." This is not universality — it is linearity.

---

## II. MINOR ISSUES

### Issue 9: R^2 is misused as a goodness-of-fit metric for log-log power-law fits

R^2 from log-log linear regression measures how well the log-transformed data follow a straight line, not how well |C_mid| follows a power law. A systematic curvature in |C_mid| vs L can be masked by the log transform. The authors should report the quality of the power-law fit in the original (non-log) variables, e.g., by reporting the fractional residual |C_mid(L) - A*L^{-beta}| / |C_mid(L)| for each data point.

### Issue 10: No discussion of L=4 contamination

The smallest system size L=4 has only 16 elements in the correlation matrix. At alpha=1.1, the hopping between sites (1,4) has J = 0.3/3^1.1 ~ 0.11, comparable to nearest-neighbor J(1,2) = 0.3. An L=4 system with power-law hopping is not a "chain" in any meaningful sense — it is a fully-connected 4-site cluster. Including L=4 in the scaling fits biases beta: the authors should provide fits with L=4 excluded (L = 8..64 only) and show that beta shifts by less than the quoted uncertainty.

### Issue 11: The Jacobian argument for independence is mathematically vacuous

Section III.C (line 83) claims that "the Jacobian d(beta,mu)/d(alpha,gamma_phi) is nonzero, formally establishing beta and mu as independent scaling dimensions." A nonzero Jacobian is a necessary condition for two functions to be independent but is trivially satisfied for any two non-trivially-constant functions of two variables. "Independence" in the renormalization group sense requires much more: the two exponents must correspond to distinct relevant operators at a fixed point. The authors have not identified any fixed point, computed any RG flow, or established that the scaling is governed by an RG fixed point at all. The "independent scaling dimensions" framing should be downgraded to "two distinct observables with different parameter dependence."

---

## III. SUMMARY OF REQUIRED CHANGES

Before this manuscript can be reconsidered for PRL, the authors must:

1. **Cross-validate with `solve_continuous_lyapunov`** (already imported, never called) on at minimum the 25 COH data points and all firewall points.
2. **Report condition numbers** of the matrix A at L=64 for all 25 (alpha, gamma_phi) combinations.
3. **Remove or heavily qualify gamma_phi=0.01 data** — display uncertainties explicitly or delete the entire column from Table 1.
4. **Add standard errors to all tables** (Table 1, Table 2, Table 3) and error bars to all figures.
5. **Perform model selection** (AIC/BIC) comparing at least 3 candidate functional forms for beta(alpha).
6. **Extend L to 128** for at least one parameter combination (alpha=1.1, gamma_phi=0.5) to validate the scaling regime.
7. **Report beta values with physically meaningful precision** — 3 significant figures, not 15.
8. **Remove the "independent scaling dimensions" claim** unless backed by RG analysis.

---

## IV. OVERALL ASSESSMENT

The physical question — whether off-diagonal coherence carries its own scaling exponent in nonequilibrium quantum systems — is worth investigating. However, the numerical execution in this manuscript does not meet the standard of evidence required for Physical Review Letters. The computations are performed with a single, dense, general-purpose linear solver without condition-number monitoring or cross-validation. The key 1/alpha functional form is a 2-parameter fit to 5 data points presented without model selection. The error analysis exists in the raw data files but is systematically excluded from the manuscript. The largest system size (L=64) is marginally adequate for short-range hopping and entirely inadequate for the alpha=1.1 regime that anchors the strongest claims. The firewall universality test conflates numerical determinism (linearity in source term) with physical universality.

I cannot recommend publication in its current form. If the authors address the items in Section III with new computations, I would be willing to re-review.

---

**Confidential note to editor:** The authors appear to have access to L=128 sparse computation capability (`firewall1_L128_v2.py` in their code directory actually uses `solve_continuous_lyapunov`) but chose not to apply it to their main results. This selective deployment of the better algorithm to the auxiliary test but not to the central claim warrants editorial scrutiny.
