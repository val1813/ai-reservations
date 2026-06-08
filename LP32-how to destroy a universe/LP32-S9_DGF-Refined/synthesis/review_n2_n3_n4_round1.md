# MALICIOUS REVIEW — Round 1: N2, N3, N4 (Concurrent Attack)

**Date:** 2026-06-08
**Role:** Anonymous Reviewer #4
**Targets:** N2 (SFR circularity), N3 (cross-probe), N4 (Fisher)
**Manuscript:** main_s9_final.tex — "A non-monotonic dark energy equation of state from cosmic structure formation"
**Standard:** PRL / Nature Physics

**Overall Assessment:** Each of the three claims contains a FATAL defect. The paper's conclusions on SFR circularity, CMB consistency, and DESI DR3 sensitivity are unsupported by the evidence presented. All three sections require complete reanalysis before the manuscript can be considered for publication.

---

## N2: SFR CIRCULARITY — FATAL

### The Claim Under Attack

Authors state: "The star formation history input assumes LCDM luminosity distances; our iteration accounts for H(z)-dependence in |dt/dz| but a fully self-consistent recomputation of the SFR from raw survey photometry is needed." They compute a DGF d_L(z) correction to SFR, find d_L ratio ~0.98-0.99 (DGF d_L slightly SMALLER than LCDM), and conclude "SFR correction <1% -> circularity closed."

### Attack 1: The 1.2 Exponent Is Ad-Hoc (FATAL)

The paper states a simplified beta exponent enters the SFR rescaling. The n1_n4_conclusions.md does not specify where beta=1.2 comes from, but any exponent in the SFR-d_L relationship requires derivation.

**The SFR is not a simple power law of d_L.** The star formation rate at redshift z is derived from the UV luminosity function (Schechter fit):

$$\phi(M)dM = \phi^* \left(\frac{L}{L^*}\right)^{\alpha+1} e^{-L/L^*} d\left(\frac{L}{L^*}\right)$$

where L = 4π d_L^2(z) fν (flux fν fixed by observation). A change in d_L(z) therefore changes:
1. The inferred absolute magnitude M_UV* (shifted by 5 log10[d_L^DGF / d_L^LCDM])
2. The characteristic luminosity L* (scales as d_L^2)
3. The Schechter parameters (phi*, alpha) — because the luminosity function is fit to binned data, and a shift in inferred luminosity changes which galaxies fall in which bins

**A 2% change in d_L does NOT produce a simple (0.98)^beta = 0.976 rescaling of SFR.** The SFR density is:

$$\rho_{SFR}(z) = \int_{L_{min}}^\infty L \cdot \phi(L,z) \cdot f_{UV-to-SFR} \cdot dL$$

If d_L shifts by 2%, L shifts by 4% (L ∝ d_L^2), which means:
- The integral lower bound L_min moves by 4% in luminosity space
- The Schechter function at that new L_min has a different value
- The SFR calibration factor f_UV-to-SFR may have its own d_L dependence if calibrated against H-alpha or other tracers

**Required fix 1.1:** Derive beta from the actual Schechter function fit parameters (Madau & Dickinson 2014 or whichever SFR calibration is used). The SFR density must be recomputed by:
(a) Taking the observed UV LF data points (flux bins)
(b) Recomputing L from flux using DGF d_L(z) for each bin
(c) Refitting the Schechter function (M_UV*, phi*, alpha) at each redshift
(d) Integrating to get SFR_DGF(z)
(e) Computing the fractional difference: ΔSFR(z)/SFR(z) = [SFR_DGF(z) - SFR_LCDM(z)] / SFR_LCDM(z)

**Required fix 1.2:** Report ΔSFR(z)/SFR(z) as a function of redshift, not a single number. The d_L ratio varies with z. A 2% average may hide 5% deviations at specific redshifts where the Schechter function is steep.

**Required fix 1.3:** If beta=1.2 comes from a specific reference, cite it. If it is a free parameter, show the sensitivity of the final w(z) to beta ∈ [0.5, 2.0].

### Attack 2: NaN at z=0 Indicates Broken d_L Computation (FATAL)

The authors' code produces NaN at z=0 for the d_L ratio. This is NOT a cosmetic boundary issue. The luminosity distance at z=0 is, by definition:

$$d_L(0) = 0$$

The ratio d_L^DGF(0) / d_L^LCDM(0) should approach 1 in the limit z→0 (both are zero, and by L'Hopital's rule their ratio approaches H_0^LCDM / H_0^DGF). If the code produces NaN, it means at least one of:
- A division by zero in the d_L computation (probably d_L in the denominator of some intermediate expression)
- A 0/0 that is not handled by limit evaluation
- A numerical integration that fails at the z=0 boundary

**This is not a minor bug.** The SFR at z≈0.01-0.05 contributes significantly to the cumulative stellar mass density rho_*(z=0), which enters equation (4) of the manuscript. If d_L computation breaks at low z, the entire normalization of rho_* may be wrong.

**Required fix 2.1:** Fix the d_L computation at z=0. The correct approach:
- Compute d_L(z) = (1+z) * r(z) where r(z) is the comoving distance
- At z=0: r(0) = 0, d_L(0) = 0
- For the RATIO: use lim_{z→0} d_L^DGF / d_L^LCDM = H_0^LCDM / H_0^DGF
- Implement this analytically, not via numerical evaluation at z=0

**Required fix 2.2:** Show d_L^DGF(z), d_L^LCDM(z), and their ratio for z ∈ [0.001, 6.0] in a figure. Any discontinuities, spikes, or NaN regions must be explained or fixed.

**Required fix 2.3:** Test the d_L computation against analytically known limits:
- z << 1: d_L(z) ≈ cz/H_0 (Hubble law)
- Compare DGF d_L to this for z < 0.01 to verify correctness

### Attack 3: The "Circularity Closed" Argument Misunderstands What Circularity Means (FATAL)

The authors frame the circularity problem as: "SFR uses LCDM d_L, but DGF predicts different d_L, so we must recompute SFR with DGF d_L." They then compute a <1% correction and declare victory.

**This is not what circularity means in this context.** The circularity is:

1. The Madau & Dickinson (2014) SFR fit uses LCDM cosmology to convert observed fluxes to luminosities and then to SFR. That fit is the INPUT to the DGF model.
2. The DGF model then predicts w(z) from that SFR input.
3. The predicted w(z) is compared to DESI BAO data.
4. The SFR INPUT was computed assuming LCDM — the very model DGF is being tested against.

**A 2% d_L shift can change the Schechter fit enough to matter.** The SFR density at z~2 (the peak) is ~0.1 M_sun/yr/Mpc^3. A 4% luminosity shift (from 2% d_L shift) changes the inferred SFR density by an amount that depends on the slope of the UV LF at the integration limit. Near L*, the LF is flat (alpha ~ -1.2 to -1.5), but the integral extends to faint magnitudes where the LF slope alpha ~ -1.7 to -2.0. In that regime:

$$\frac{\Delta \rho_{SFR}}{\rho_{SFR}} \approx (|\alpha| - 1) \cdot \frac{\Delta L}{L}$$

For alpha = -1.8: Δrho_SFR / rho_SFR ≈ (1.8 - 1) × 4% = 3.2%.

**A 3.2% SFR change is NOT negligible when the w(z) peak is already mild (w only reaches -0.31).** The SFR enters the w(z) computation through equation (4) — w(z)+1 ∝ SFR(z) / [H(z) * rho_*(z)^{n/(n+1)}]. A 3.2% change in SFR normalization could shift w_0 by several percent, which matters for the AIC comparison against LCDM where the baseline ΔAIC is only +8.1.

**Required fix 3.1:** Perform the full self-consistent recomputation:
(a) Start with LCDM SFR → compute DGF w(z), H(z), d_L(z)
(b) Recompute SFR(z) using DGF d_L(z), refitting the Schechter function at each z
(c) Recompute DGF w(z), H(z) using the new SFR(z)
(d) Iterate until convergence in w_0 (Δw_0 < 0.001)
(e) Report the converged w(z) and the number of iterations

**Required fix 3.2:** If the full iteration is "too expensive" (refitting Schechter functions at each step), then provide an honest error budget:
- What is the systematic uncertainty on w_0 from the SFR circularity?
- What is the systematic uncertainty on the w(z) peak amplitude?
- How do these compare to the statistical uncertainties from DESI DR2?

**Required fix 3.3:** Remove the statement "circularity closed" from the manuscript. Replace with: "We estimate the systematic uncertainty on w(z) from the SFR luminosity distance assumption to be Δw_0 = ±X, based on [method]. A full self-consistent iteration is deferred to future work." Give a specific number for X, not "<1%."

---

## N3: CROSS-PROBE "CONSISTENCY" — FATAL

### The Claim Under Attack

The n1_n4_conclusions.md references a CMB chi2 of 137895 — obviously unphysical — and the manuscript abstract claims the model is "not excluded" by current data but evaluates only against DESI DR2 BAO. The authors admit they "lack proper Planck compressed likelihood."

### Attack 1: The CMB chi2 Is Unphysical — No Cross-Probe Conclusion Is Valid (FATAL)

A chi2 of 137895 for CMB data is 3-4 orders of magnitude too large. For comparison:
- Planck 2018 TTTEEE+lowE: chi2 ~ 2500 for ~2500 data points (chi2/dof ~ 1.0 for LCDM)
- A chi2 of 137895 for ~2500 points means chi2/dof ~ 55 — each data point is >7 sigma off

**This is not "we need a better likelihood." This means the computation is broken.** Possible causes:
1. The CMB power spectrum computed from DGF cosmology is completely wrong (wrong transfer function, wrong recombination physics)
2. The covariance matrix is not being applied (summing squared residuals without inverse covariance weighting)
3. Units mismatch (e.g., using muK^2 where the data is in dimensionless C_ell)
4. Using raw C_ell instead of binned data, inflating the effective number of data points

**Whatever the cause, a chi2 of 137895 means ZERO cross-probe information can be extracted.**

**Required fix 1.1:** Fix the CMB likelihood computation. Use either:
- Planck 2018 compressed likelihood (plik_lite or equivalent) — this is the minimal requirement for any paper claiming CMB consistency
- CosmoMC or Cobaya with the DGF model implemented as a custom dark energy class
- At absolute minimum: compute the CMB shift parameters (l_A, R, omega_b h^2) at the DGF best-fit and compare to Planck 2018 constraints

**Required fix 1.2:** Report the chi2 for EACH probe separately with dof:
- DESI DR2 BAO: chi2 = 19.1, dof = 10 (12 data points - 2 model params), chi2/dof = 1.91
- Planck CMB: chi2 = ?, dof = ?, chi2/dof = ?
- Pantheon+ SN: chi2 = ?, dof = ?, chi2/dof = ?

**Required fix 1.3:** Do not claim "cross-probe consistency SATISFIED" until all three probes are fit with proper likelihoods and the joint chi2 is physically reasonable.

### Attack 2: The Key Cross-Probe Test Is Not Performed (FATAL)

The manuscript only fits DESI DR2 BAO. The abstract claims "the model is not excluded" but this statement is based on ONE probe only.

**The defining test of any modified dark energy model is: can it simultaneously fit BAO+CMB+SN without tension?**

For LCDM, this is well established: the same 6 parameters fit all three probes with chi2/dof ~ 1 for each. For DGF:
- BAO only: chi2 = 19.1 vs 15.0 for LCDM (Δχ^2 = +4.1 for 2 extra params, ΔAIC = +8.1)
- CMB: unknown (calculation broken)
- SN: not even attempted

**The null hypothesis is: DGF cannot simultaneously fit all three probes.** Until this null hypothesis is tested and rejected, the model is effectively falsified by the BAO result alone — it fits BAO WORSE than LCDM while having MORE parameters.

**Required fix 2.1:** Perform the joint BAO+CMB+SN fit. The minimal analysis:
- Use CosmoMC/Cobaya with DGF as a custom dark energy model
- Fit to: DESI DR2 BAO + Planck 2018 plik_lite + Pantheon+ SN
- Free parameters: H_0, omega_b h^2, omega_c h^2, tau_reio, (C, n) or (w_0, w_a) for DGF
- Report: joint best-fit chi2, parameter constraints, and tension metrics

**Required fix 2.2:** If a full MCMC is infeasible, at minimum:
- Compute DGF prediction for the CMB shift parameters: l_A, R, omega_b h^2
- Compare to Planck 2018 constraints (Table 2 of Planck 2018 results VI)
- Compute DGF prediction for the SN distance modulus at Pantheon+ redshifts
- Compare to Pantheon+ compressed likelihood

**Required fix 2.3:** Remove any language implying cross-probe consistency has been demonstrated. Replace with honest statements about what has and has not been tested.

### Attack 3: The BAO-Only Result Actually FAVORS LCDM (MAJOR)

The draft reports ΔAIC = +8.1 for DGF vs LCDM. By standard information criteria, AIC differences of:
- ΔAIC < 2: models are essentially equivalent
- 2 < ΔAIC < 7: considerably less support
- ΔAIC > 10: essentially no support

ΔAIC = +8.1 is in the "considerably less support" to "essentially no support" range. **The BAO data, when the sound horizon is free, prefers LCDM over DGF.**

This is further compounded by:
- DGF has 2 parameters (C, n) vs LCDM's 0
- Even with the extra flexibility, DGF fits WORSE
- Adding kappa (memory term) makes it even worse: ΔAIC = +10.1

The manuscript's framing "the model is not excluded" is technically true (ΔAIC < 10) but misleading. A better summary: "DGF is disfavored by DESI DR2 BAO at ΔAIC = +8.1 relative to LCDM."

**Required fix 3.1:** Honestly report the statistical evidence direction. Add: "The BAO data alone prefer LCDM over DGF by ΔAIC = +8.1. A positive cross-probe detection requires that CMB and/or SN constraints reverse this preference."

---

## N4: FISHER FORECAST — FATAL

### The Claim Under Attack

Authors claim: sigma_w = 0.077 per dz = 0.5 bin for Stage IV surveys, DGF vs CPL distinguishable at 4.5σ combined. The n1_n4_conclusions.md acknowledges the simple estimate is "overly optimistic" and plans to defer quantitative Fisher to "subsequent work."

### Attack 1: The 0.10/sqrt(dz/0.3) Scaling Is Uncited and Likely Wrong (FATAL)

The manuscript uses a sigma_w scaling law without citation. The standard reference for binned w(z) forecasts is:

- Albrecht et al. (2006), "Report of the Dark Energy Task Force" (DETF) — provides Figure of Merit methodology
- Albrecht et al. (2009), "Findings of the Joint Dark Energy Mission Figure of Merit Science Working Group" — discusses binning and correlations
- DESI Collaboration (2016), "The DESI Experiment Part I: Science, Targeting, and Survey Design" — provides DESI-specific forecasts
- Euclid Collaboration (2018, 2020, 2024) — multiple forecasting papers
- Font-Ribera et al. (2014), "DESI and other dark energy experiments" — specific Fisher methodology
- **The LSST Dark Energy Science Collaboration (2018) — the standard reference for Stage IV w(z) bin forecasts**

The 0.10/sqrt(dz/0.3) scaling implies sigma_w = 0.10 for dz = 0.3 bins. Where does this number come from? If from the DETF report, the DETF used CPL parameterization (w0, wa), not binned w(z). The binned w(z) Figure of Merit is a different quantity. If from a specific DESI or Euclid forecasting paper, cite the exact figure/table.

**Required fix 1.1:** Cite the exact source of the sigma_w = 0.10/sqrt(dz/0.3) scaling. If no single source exists, compute it properly using a Fisher matrix forecast.

**Required fix 1.2:** Justify the sqrt(dz) scaling. This scaling assumes:
- Independent measurements in each redshift bin
- Statistical errors that scale as 1/sqrt(N_galaxies) ∝ 1/sqrt(dz)
- No systematic floor

The sqrt(dz) scaling is approximately correct for volume-limited surveys at intermediate redshifts, but it breaks down when:
- Systematics (redshift errors, galaxy bias, nonlinear modeling) dominate
- Bins are narrow enough that radial BAO is unresolved
- At high z where galaxy counts drop sharply

**Required fix 1.3:** Show the scaling breaks down at some dz. At what bin width does the sqrt(dz) scaling fail? If the answer is "we don't know," then the binned w(z) forecast is not quantitative.

### Attack 2: Binned w(z) Measurements Are Correlated (FATAL)

The manuscript treats bins as independent: "sigma_w = 0.077 per dz = 0.5 bin" and combines them by adding chi2 independently.

**This is wrong.** BAO distance measurements at different redshifts are correlated because:
1. The sound horizon r_d is a common parameter — its uncertainty propagates to ALL bins
2. The Alcock-Paczynski effect correlates D_M(z) and D_H(z) measurements
3. Broad-band power spectrum shape information correlates across redshift bins
4. Reconstruction adds its own correlation structure

The correct approach is a Fisher matrix:

$$F_{ij} = \sum_{\ell} \frac{2\ell+1}{2} f_{sky} \text{Tr}\left[C^{-1} \frac{\partial C}{\partial \theta_i} C^{-1} \frac{\partial C}{\partial \theta_j}\right]$$

where C includes the cross-redshift-bin correlations.

**If you add chi2 independently for 5 redshift bins, you will UNDERESTIMATE the uncertainty on w(z) by a factor that depends on the correlation matrix.** For BAO, typical correlations between adjacent bins are 0.3-0.5. A 5-bin analysis with rho = 0.4 between adjacent bins inflates the combined uncertainty by approximately sqrt(1 + (N-1)*rho) ≈ sqrt(1 + 4*0.4) ≈ 1.6 compared to the independent-bin assumption. This turns sigma_w_combined = 0.077/√5 = 0.034 into ~0.055.

**Required fix 2.1:** Compute the full Fisher matrix including the cross-bin correlation structure. At minimum, use the BAO Fisher formalism from Seo & Eisenstein (2007) or the more recent DESI forecasting pipeline methodology.

**Required fix 2.2:** Report the correlation matrix between w(z) bins. A 5x5 matrix showing that bins are 30-50% correlated.

**Required fix 2.3:** Report the combined significance including correlations. If the correlation-corrected significance drops below 3σ, the statement "DGF vs CPL at 4.5σ combined" must be withdrawn.

### Attack 3: DESI DR3 Improvements Are Mischaracterized (FATAL)

The manuscript claims "3.0σ DESI DR3 alone" based on assumed improvements from DR2 to DR3.

**DESI DR3 improvements are not uniform across redshift:**
1. DR3 adds more galaxies, primarily improving statistics at z < 1.5 where the survey is already statistics-limited (not systematics-limited)
2. DR3 does NOT extend the redshift coverage — the z > 1.5 Ly-alpha forest BAO measurements come from a completely different tracer and are not improved by DR3 galaxy counts
3. The z > 1.5 bins are systematics-limited (quasar target selection, Ly-alpha forest modeling), not statistics-limited

If the DGF w(z) peak is at z ≈ 1.5 (as the manuscript claims), then the DESI DR3 improvement at the peak is:
- z ≈ 1.0-1.5 (LRG+ELG): statistics improve by ~sqrt(N_DR3/N_DR2), maybe 20-30%
- z ≈ 1.5-2.0 (ELG+QSO): smaller improvement, systematics-limited
- z > 2.0 (Ly-alpha): essentially NO improvement from DR3

**The peak sensitivity region (z~1.5) is exactly where DR3 improvements are smallest.**

**Required fix 3.1:** Break down the DR3 forecast by redshift bin with DR2→DR3 improvement factors per bin. Cite the actual DESI DR3 survey forecasts (DESI Collaboration 2023 or later) for each tracer type.

**Required fix 3.2:** If the z~1.5 bin is systematics-limited rather than statistics-limited, the DR3 forecast for that bin should use the systematic error floor, not the statistical improvement.

**Required fix 3.3:** The 3.0σ claim for DESI DR3 alone must be justified bin-by-bin. Show: for each redshift bin, what is sigma_w at DR2 precision, what is sigma_w at DR3 precision, and what is the DGF vs CPL signal strength (Δw / sigma_w) in that bin.

---

## CROSS-CUTTING ISSUES

### Issue 1: The Three Claims Are Interdependent

N2 (SFR circularity) affects the w(z) shape, which affects the N4 (Fisher) detectability. N3 (cross-probe) is the actual test of the model's viability, without which N2 and N4 are theoretical exercises.

**The authors cannot fix N4 until N2 is resolved.** The Fisher forecast for detecting a non-monotonic w(z) depends on the amplitude and shape of the peak, which depends on the SFR input, which depends on the circularity correction.

**The authors cannot fix N3 until the CMB likelihood is repaired.** The cross-probe claim is the paper's central result. A broken CMB chi2 means the central result is unsupported.

### Issue 2: The "Qualitative" Fisher Argument in the Abstract Is Misleading

The abstract states: "DESI DR3 and the Euclid mission, with projected binned w(z) precision of sigma_w ~ 0.1-0.2 per Δz ~ 0.3 bin at intermediate redshifts, will test this prediction directly."

This is a qualitative statement, but it quotes quantitative numbers (0.1-0.2 per Δz ~ 0.3). Those numbers must be justified. The n1_n4_conclusions.md acknowledges the Fisher calculation needs to be proper and plans to defer it. **You cannot have it both ways — either the numbers are in the paper (with proper citations and Fisher matrices) or they are removed entirely.**

### Issue 3: The Error Budget Is Missing

The paper has no systematic error budget. At minimum, the following uncertainties must be quantified:
- SFR calibration uncertainty (Madau & Dickinson vs Behroozi et al.): Δw_0 = ±0.03 (mentioned in passing)
- SFR circularity (not computed): Δw_0 = ?
- CMB likelihood approximation (not quantified): Δchi2 = ?
- BAO covariance approximation (12 data points, ρ ≈ -0.5): Δchi2 = ?
- Fisher bin correlation (not computed): Δσ_w = ?
- n exponent uncertainty (scan over n ∈ [0.3, 3.0] changes chi2 by <1 — but does it change w_0?): Δw_0 = ?

---

## REQUIRED FIXES — PRIORITY ORDER

### Tier 1 — Must Fix Before Any Journal Submission

| # | Fix | Section |
|---|-----|---------|
| F1 | Fix CMB likelihood — replace chi2=137895 with proper Planck compressed likelihood | N3 |
| F2 | Perform joint BAO+CMB+SN fit — or remove all cross-probe claims | N3 |
| F3 | Derive SFR correction from actual Schechter function refit, not beta=1.2 rescaling | N2 |
| F4 | Fix NaN at z=0 in d_L computation | N2 |
| F5 | Remove "circularity closed" — replace with quantified systematic uncertainty on w_0 from SFR d_L assumption | N2 |

### Tier 2 — Must Fix Before Claiming Quantitative Forecasts

| # | Fix | Section |
|---|-----|---------|
| F6 | Compute proper Fisher matrix with cross-bin correlations for N4 | N4 |
| F7 | Cite the source of sigma_w scaling or compute it from first principles | N4 |
| F8 | Break down DR3 forecast by redshift bin with tracer-specific improvement factors | N4 |
| F9 | Report binned w(z) correlation matrix | N4 |

### Tier 3 — Must Add Before Resubmission

| # | Fix | Section |
|---|-----|---------|
| F10 | Produce full systematic error budget table | All |
| F11 | Remove "cross-probe consistency SATISFIED" — replace with honest statement of what is tested | N3 |
| F12 | Either remove quantitative sigma_w numbers from abstract or justify them | N4 |
| F13 | Perform full self-consistent SFR-DGF iteration (or quantify the residual uncertainty from not doing it) | N2 |

---

## VERDICT

**N2:** FATAL — the SFR circularity argument uses an ad-hoc exponent, has broken code (NaN at z=0), and misunderstands what "closing the circularity loop" requires. The claim "circularity closed" is unsupported.

**N3:** FATAL — the CMB chi2 of 137895 is unphysical. No cross-probe conclusion can be drawn until a proper Planck likelihood replaces the broken computation. The BAO-only result disfavors DGF at ΔAIC = +8.1.

**N4:** FATAL — the Fisher forecast uses uncited scaling relations, treats correlated bins as independent, and mischaracterizes DESI DR3 improvements at the peak-detection redshift (z~1.5).

**Overall: All three claims require complete reanalysis. The manuscript in its current form is not suitable for submission. Resubmission requires Tier 1 fixes (F1-F5) to be completed and documented before any cross-probe or circularity claims are made.**

---

*This review was conducted with adversarial intent as instructed. The reviewer has no conflict of interest. All charges are supported by: (1) the manuscript text (main_s9_final.tex), (2) the conclusions document (n1_n4_conclusions.md), (3) standard references in cosmological parameter inference (Planck likelihoods, Fisher forecasting, Schechter function fitting).*

*Signed: Anonymous Reviewer #4*
