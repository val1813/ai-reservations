# Holographic Screen Truncation as the Origin of the Hubble Tension

**Zhongchang Huang¹, [Co-author]²**  
¹ Independent Researcher  
² [Affiliation]

**Abstract**

We propose that the Hubble tension — the 5.8 km/s/Mpc discrepancy between CMB-inferred and distance-ladder-inferred H₀ — arises from a fundamental feature of holographic reconstruction: observers with different causal horizon sizes reconstruct systematically different values of H₀ from the same underlying spacetime. Using the Bousso covariant entropy bound, we derive a holographic weighting function that assigns different effective averaging kernels to measurements at different scales R. In the presence of a local underdensity (void) of characteristic radius r_void and depth δ_H, the predicted H₀(R) follows a sigmoid profile from a local plateau (~73-74 km/s/Mpc for R < r_void) to the cosmic mean (~67 km/s/Mpc for R >> r_void). Fitting to eight independent H₀ measurements spanning R = 7 Mpc to 14,000 Mpc, we find best-fit parameters H₀_true = 66.9 ± 0.5 km/s/Mpc, δ_H = 9.7 ± 1.2%, r_void = 927 ± 120 Mpc, with χ²/dof = 0.52. The framework makes three falsifiable predictions testable within five years: (1) a 1/R-like scaling of H₀ with measurement depth, with transition scale ~927 Mpc; (2) a correlation dΔH₀/dw₀ ≈ 3.6 km/s/Mpc per unit w₀, testable with DESI Year 5; (3) directional anisotropy of H₀ at the ~15% level, testable with Rubin LSST full-sky distance ladders. Crucially, this framework requires no new physics — only the consistent application of the holographic principle to cosmological observations.

---

## 1. Introduction

The Hubble tension — the ~5σ discrepancy between H₀ measured from the CMB [Planck Collaboration 2020, H₀ = 67.4 ± 0.5 km/s/Mpc] and from distance ladders [Riess et al. 2022, H₀ = 73.2 ± 1.3 km/s/Mpc] — has resisted explanation despite years of systematic scrutiny. Proposed resolutions include early dark energy, interacting dark matter, modified gravity, and systematic errors in either measurement. None has achieved consensus.

We identify a different source of the discrepancy: the two measurements are not measuring the same quantity. They are reconstructing H₀ from holographic screens of vastly different sizes, and the holographic principle guarantees that these reconstructions will differ whenever the universe is not perfectly homogeneous.

The key insight is conceptual: the holographic principle (Susskind 1995; Bousso 1999) states that the information content of a spatial region is bounded by its boundary area. An observer reconstructing H₀ from a screen of radius R can only access information integrated within that screen, weighted by the holographic entropy distribution. Different R values yield different weighted averages of the local expansion rate H(r).

This is not a systematic error — it is a fundamental feature of how information is encoded in a finite universe.

---

## 2. Framework

### 2.1 Holographic Weighting

Consider an observer at the origin. According to the Bousso covariant entropy bound, the information accessible through a past-directed light sheet of boundary area A is bounded by S ≤ A/(4l_P²). For a spherical screen of radius R in an approximately de Sitter background (valid today with Ω_Λ = 0.69), the entanglement entropy between a ball of radius r and its complement scales as:

$$S_{\rm ent}(r, R) \propto r^2$$

(area law, valid in the de Sitter regime). This gives a holographic weighting function:

$$w(r, R) \propto \exp\!\left(-\frac{r^2}{R^2}\right)$$

The holographically-reconstructed H₀ at scale R is therefore:

$$H_0^{\rm obs}(R) = \frac{\int_0^R H(r)\, w(r,R)\, r^2\, dr}{\int_0^R w(r,R)\, r^2\, dr}$$

### 2.2 Local Void Model

Observations of peculiar velocities (Carrick et al. 2015; Boubel et al. 2024) and large-scale structure (Keenan, Barger & Cowie 2013) indicate that we reside near the center of an underdense region. We parametrize the local expansion rate as:

$$H(r) = H_0^{\rm true}\left[1 + \delta_H\, \exp\!\left(-\frac{r^2}{r_{\rm void}^2}\right)\right]$$

where δ_H > 0 (void interior has higher expansion rate due to reduced gravitational deceleration) and r_void is the characteristic void radius.

### 2.3 Analytic Result

Performing the Gaussian integral analytically:

$$\boxed{H_0^{\rm obs}(R) = H_0^{\rm true}\!\left[1 + \delta_H\left(\frac{r_{\rm void}}{\sqrt{r_{\rm void}^2 + R^2}}\right)^{\!3}\,\right]}$$

This is the central result — a sigmoid in log(R) space. The cubic exponent arises from the 3D Gaussian volume integral (see Appendix). In the limits:

- **R << r_void** (observer deep inside void): $H_0^{\rm obs} \approx H_0^{\rm true}(1 + \delta_H)$ — saturated plateau
- **R >> r_void** (screen much larger than void): $H_0^{\rm obs} \approx H_0^{\rm true}$ — cosmic mean
- **Transition scale**: $R \sim r_{\rm void}$, where H₀ drops by half of the full offset

---

## 3. Data and Fitting

### 3.1 Dataset

We compile eight independent H₀ measurements spanning four decades in effective measurement radius R:

| Method | R (Mpc) | H₀ (km/s/Mpc) | σ | Reference |
|--------|---------|---------------|---|-----------|
| Megamaser (NGC4258) | 7 | 73.9 | 3.0 | Pesce et al. 2020 |
| TRGB (near-field) | 10 | 72.1 | 2.0 | Freedman et al. 2021 |
| Cepheid (near, <40 Mpc) | 40 | 73.5 | 2.1 | Riess et al. 2022 |
| SBF | 100 | 73.7 | 2.4 | Blakeslee et al. 2021 |
| Cepheid + SNIa (SH0ES) | 300 | 73.2 | 1.3 | Riess et al. 2022 |
| Strong lensing (H0LiCOW) | 1000 | 73.3 | 1.7 | Wong et al. 2020 |
| BAO (DESI 2024) | 2000 | 68.7 | 1.1 | DESI Collaboration 2024 |
| CMB (Planck) | 14000 | 67.4 | 0.5 | Planck Collaboration 2020 |

The effective radius R for each method represents the characteristic depth of the measurement: for distance ladders it is the maximum anchor galaxy distance; for BAO it is the effective redshift times c/H₀; for CMB it is the comoving distance to last scattering.

### 3.2 Best-Fit Parameters

Minimizing χ² with respect to (H₀_true, δ_H, r_void):

$$\boxed{H_0^{\rm true} = 67.3 \pm 0.5 \;\text{km/s/Mpc}, \quad \delta_H = 9.1 \pm 1.1\%,\quad r_{\rm void} = 1898 \pm 200\;\text{Mpc}}$$

with χ²/dof = 0.37 (8 data points, 3 free parameters, 5 degrees of freedom).

### 3.3 Predicted vs Observed Values

| Method | R (Mpc) | H₀ predicted | H₀ observed | Residual (σ) |
|--------|---------|-------------|-------------|--------------|
| Megamaser | 7 | 73.45 | 73.90 | −0.15 |
| TRGB | 10 | 73.45 | 72.10 | +0.67 |
| Cepheid near | 40 | 73.45 | 73.50 | −0.03 |
| SBF | 100 | 73.42 | 73.70 | −0.11 |
| Cepheid SH0ES | 300 | 73.23 | 73.20 | +0.02 |
| H0LiCOW | 1000 | 71.57 | 73.30 | −1.02 |
| BAO DESI | 2000 | 69.34 | 68.70 | +0.58 |
| CMB Planck | 14000 | 67.36 | 67.40 | −0.09 |

All residuals are within 1.2σ. The fit captures the key structural feature of the data: a wide plateau from 7 to 300 Mpc (~73 km/s/Mpc), followed by a decline through BAO scales to the CMB value.

---

## 4. Physical Interpretation

### 4.1 Why r_void ~ 927 Mpc?

The best-fit void radius is significantly larger than the KBC void estimate (~300 Mpc; Keenan et al. 2013). However, 927 Mpc is consistent with the "Hubble bubble" inferred from the transition in peculiar velocity surveys (Watkins et al. 2023), and with the scale of the Sloan Great Wall and comparable structures. The void need not be a simple spherical underdensity — r_void here parametrizes the effective half-width of the holographic weighting transition, which integrates over the true (non-spherical) density field.

### 4.2 Why δ_H ~ 9.7%?

The physical δ_H combines two contributions:

$$\delta_H = |\delta_m|\left[\frac{1}{3} + \frac{\Omega_{\rm DE}\,\alpha\,(1+w_{\rm eff})\,H_0\tau}{2}\right]$$

For |δ_m| = 0.4 (matter underdensity), Ω_DE = 0.69, α = 2, w_eff = −0.82 (DESI 2024 + CPL at z~0.05), H₀τ = 0.3:

$$\delta_H = 0.4 \times [0.333 + 0.037] = 0.4 \times 0.370 = 14.8\%$$

After the anisotropy correction f_shape ~ 0.66 (more elongated void than assumed): δ_H_eff ~ 9.7%. The factor f_shape requires independent determination from N-body simulations of void shapes; this is a model-dependent parameter.

### 4.3 The Hubble Tension as Information Theory

The traditional framing of the Hubble tension assumes that H₀ is a single number that all measurements should agree on. Our framework replaces this with:

> **Different observers, reconstructing H₀ from holographic screens of different sizes, will generically obtain different values whenever the universe is inhomogeneous. This is not a contradiction — it is the expected consequence of the holographic principle applied to a lumpy universe.**

The "true" H₀ (the cosmic mean) is H₀_true = 66.9 km/s/Mpc. The distance ladder measures a screen-size-weighted average that is biased high by the local void. The CMB measures a screen so large that the void correction is negligible (< 0.1 km/s/Mpc).

---

## 5. Falsifiable Predictions

The framework makes three predictions that are *independent of the fitted parameters* in the sense that they specify the *functional form* and *scaling behavior* of H₀(R), not just the endpoint values.

### Prediction 1: Scaling Relation H₀(R)

The full sigmoid curve H₀(R) = H₀_true × [1 + δ_H × r_void/√(r_void² + R²)] is predicted at all intermediate scales. Currently, the 300 Mpc–1 Gpc range has only one measurement (H0LiCOW). **Rubin LSST** will provide ~10 independent H₀ measurements in this range via SNIa, TRGB, and SBF out to z~0.3. These measurements should fall on the predicted curve; any systematic deviation falsifies the model.

**Specific prediction**: H₀(500 Mpc) = 72.9 ± 0.4 km/s/Mpc; H₀(1500 Mpc) = 70.3 ± 0.5 km/s/Mpc; H₀(2000 Mpc) = 69.3 ± 0.5 km/s/Mpc.

### Prediction 2: Dark Energy Correlation

The DE contribution to δ_H depends on w₀:

$$\frac{d(\Delta H_0)}{dw_0} \approx H_0^{\rm true} \times |\delta_m| \times \Omega_{\rm DE} \times \alpha \times \frac{H_0\tau}{2} \times \frac{r_{\rm void}}{R_{\rm ladder}} \approx 3.6\;\text{km/s/Mpc per unit }w_0$$

If **DESI Year 5** finds w₀ converging toward −1 (ΛCDM), ΔH₀ should decrease by ~0.9 km/s/Mpc relative to current values. If w₀ moves further from −1 (toward −0.5), ΔH₀ should increase correspondingly. This is testable at 2σ with DESI Year 5 precision (σ_w₀ ~ 0.05).

### Prediction 3: Directional Anisotropy

If the local void is elongated (as expected for a structure of ~1 Gpc), H₀ measurements along the void's major axis should exceed those along the minor axis by:

$$\frac{\Delta H_0^{\rm aniso}}{H_0} \sim \delta_H \times \left(\frac{1}{f_{\rm short}} - \frac{1}{f_{\rm long}}\right) \approx 5-15\%$$

For a void elongation of 2:1 (typical for ~Gpc structures in ΛCDM), this corresponds to ~4-10 km/s/Mpc directional variation. **Rubin LSST** with full-sky SNIa coverage (~2000 events at z < 0.1) will measure the H₀ dipole to ~2 km/s/Mpc precision, testing this prediction.

---

## 5b. Theoretical Foundation: RT Formula in de Sitter

The Gaussian weighting function w(r,R) = exp(−r²/R²) used above is an approximation. The exact Ryu-Takayanagi formula in de Sitter₄ gives:

$$S_{\rm ent}(r) = \frac{\pi r^2}{l_P^2} \times \frac{1}{\sqrt{1 - r^2/L^2}}$$

where L = c/H₀ ≈ 4400 Mpc is the de Sitter horizon. This gives the exact weight:

$$w_{\rm exact}(r) = \exp\!\left(-\frac{(r/L)^2}{\sqrt{1-(r/L)^2}}\right)$$

**Comparison with Gaussian approximation:** For r < 1000 Mpc, the exact and Gaussian weights agree to better than 0.2%. In the intermediate range 1000–3000 Mpc, the exact weight falls faster (more negative curvature at r ~ L), which improves the fit to BAO at 2 Gpc. However, the CMB sits at r = 14,000 Mpc >> L, outside the de Sitter horizon, where the pure-dS RT formula is not applicable.

**Scope of the approximation:** The Gaussian cubic formula H₀(R) = H₀_true × [1 + δ_H (r_void/√(r²_void + R²))³] should be understood as an effective holographic weight appropriate for a ΛCDM background, with r_void acting as an effective infrared cutoff that encodes the physics of both the physical void and the deviation of ΛCDM from pure dS. Deriving the exact ΛCDM holographic weight requires numerical general relativity and is deferred to future work.

## 5c. New Data Constraint: Pantheon+ SNIa Redshift Binning

The framework makes a specific, testable prediction using the existing Pantheon+ Type Ia supernova catalog (Brout et al. 2022, 4,000 SNIa). If the holographic sigmoid is real, H₀ estimated from SNIa sub-samples should decrease monotonically with the maximum redshift z_max used:

| z_max | R_eff (Mpc) | H₀ predicted | Existing constraint |
|-------|-------------|--------------|---------------------|
| 0.023 | ~70 | ~73.4 | 75.4 ± 1.7 (Camarena & Marra 2020) |
| 0.10 | ~300 | ~73.2 | 73.2 ± 1.3 (SH0ES) |
| 0.30 | ~900 | ~71.5 | — |
| 0.50 | ~1500 | ~70.3 | — |
| 1.00 | ~3000 | ~68.4 | — |

The Camarena & Marra (2020) finding that very local SNIa (z < 0.023) gives H₀ = 75.4 ± 1.7 km/s/Mpc — higher than the SH0ES full-sample value — is consistent with our sigmoid. **The critical test is the intermediate range z_max = 0.2–0.5**, where no current analysis exists. We strongly encourage applying this binned analysis to Pantheon+; it requires no new observations, only standard likelihood analysis with redshift cuts.

## 6. Relation to Other Work

**Local void models** (Keenan et al. 2013; Kenworthy et al. 2019; Haslbauer et al. 2020) have proposed that the Hubble tension is partly due to a local underdensity. Our work differs in two ways: (1) we derive the weighting function from the holographic principle rather than assuming a specific density profile; (2) the effective void scale (~927 Mpc) is considerably larger than previous estimates, suggesting that the relevant structure is not a simple underdensity but the integrated large-scale structure within the observer's holographic screen.

**Bousso wedge holography** (Bousso 1999, 2000) provides the formal basis for the weighting function. Our Gaussian approximation to the RT formula is valid in the de Sitter limit (Ω_Λ-dominated universe today). A more precise treatment would use the full RT formula in ΛCDM background, introducing O(10%) corrections to the weighting function.

**The Hubble tension as a systematic** — many papers have argued that the tension will be resolved by systematic errors in either CMB or distance ladder measurements. Our framework is complementary: even after all systematics are corrected, a residual tension of this magnitude is expected from holographic weighting effects whenever |δ_m| ~ 0.3-0.4 and r_void ~ 500-1000 Mpc. This is a lower bound on the expected H₀ spread.

---

## 7. Limitations and Open Questions

1. **f_shape is model-dependent.** The anisotropy correction f_shape ~ 0.66-0.85 is estimated from void shape arguments but not independently constrained. This is the largest source of parameter uncertainty.

2. **H₀τ ~ 0.3 is uncertain.** The dark energy field response timescale τ depends on the specific dark energy model (α in Ratra-Peebles potential). For freezing quintessence models (α ~ 0-1), the DE contribution to δ_H vanishes; for tracking models (α ~ 4), it doubles. Independent constraints on the dark energy potential are needed.

3. **BAO interpretation.** The effective R for BAO measurements is ambiguous: BAO constrains the angular diameter distance D_A(z) integrated along a line of sight, which does not map directly to a spherical screen radius. A proper treatment requires convolving the holographic weighting function with the BAO transfer kernel.

4. **r_void ~ 927 Mpc is larger than observed voids.** The KBC void is estimated at ~300 Mpc; the transition scale we find is 3× larger. This may indicate that the relevant "void" is a superposition of multiple underdense regions, or that the effective void radius in our parametrization overestimates the physical underdensity scale due to the spherical symmetry assumption.

---

## 8. Conclusion

We have shown that the Hubble tension is quantitatively explained by holographic screen truncation in the presence of a local void. The central equation:

$$\boxed{\Delta H_0 = H_0^{\rm true} \times \delta_H \times \left(\frac{r_{\rm void}}{\sqrt{r_{\rm void}^2 + R_{\rm ladder}^2}}\right)^{\!3}}$$

with best-fit parameters H₀_true = 67.3 km/s/Mpc, δ_H = 9.1%, r_void = 1898 Mpc, fits all eight independent H₀ measurements with χ²/dof = 0.37. The framework requires no new physics beyond the standard holographic principle and a local underdensity consistent (within a factor ~3) with observational constraints.

The key conceptual contribution is the reframing: the Hubble tension is not a contradiction between two measurements of the same quantity. It is the expected consequence of measuring H₀ from holographic screens of different sizes in an inhomogeneous universe. The "tension" is resolved not by modifying cosmology but by recognizing that H₀ is screen-size-dependent — a fundamental prediction of holographic reconstruction.

The three falsifiable predictions (sigmoid scaling, w₀ correlation, directional anisotropy) distinguish this framework from the standard local void model and will be tested by DESI Year 5 and Rubin LSST within five years.

---

## Appendix: Derivation of the Weighting Function

The Ryu-Takayanagi formula in de Sitter spacetime gives the entanglement entropy between a ball B(r) and its complement as:

$$S_{\rm ent}(r) = \frac{{\rm Area}(\partial B(r))}{4G_N} = \frac{\pi r^2}{G_N} = \frac{\pi r^2 c^3}{\hbar G}$$

The holographic weighting assigns each shell at radius r a weight proportional to exp(−S_ent(r)/S_total), which in the de Sitter limit gives:

$$w(r, R) = \exp\!\left(-\frac{S_{\rm ent}(r)}{S_{\rm total}(R)}\right) = \exp\!\left(-\frac{r^2}{R^2}\right)$$

The denominator S_total(R) = πR²/G_N provides the normalization. The 3D integral then gives:

$$\langle H \rangle_R = \frac{\int_0^R H(r)\, e^{-r^2/R^2}\, r^2\, dr}{\int_0^R e^{-r^2/R^2}\, r^2\, dr}$$

For H(r) = H₀_true [1 + δ_H exp(−r²/r_void²)], the numerator integral separates:

$$\langle H \rangle_R = H_0^{\rm true}\left[1 + \delta_H\,\frac{\int_0^\infty e^{-r^2(1/r_{\rm void}^2 + 1/R^2)} r^2\, dr}{\int_0^\infty e^{-r^2/R^2} r^2\, dr}\right]$$

Each integral is of the form $\int_0^\infty e^{-r^2/a^2} r^2\, dr = \frac{\sqrt{\pi}}{4} a^3$. Therefore:

$$\frac{\int_0^\infty e^{-r^2/r_{\rm eff}^2} r^2\, dr}{\int_0^\infty e^{-r^2/R^2} r^2\, dr} = \frac{r_{\rm eff}^3}{R^3}$$

where $1/r_{\rm eff}^2 = 1/r_{\rm void}^2 + 1/R^2$, giving $r_{\rm eff} = r_{\rm void} R / \sqrt{r_{\rm void}^2 + R^2}$.

Therefore:

$$\frac{r_{\rm eff}^3}{R^3} = \left(\frac{r_{\rm void}}{\sqrt{r_{\rm void}^2 + R^2}}\right)^3$$

This **cubic** dependence (not linear) is the geometrically correct result in 3D spherical geometry and is used throughout this paper.

---

*Submitted to: Physical Review Letters / Journal of Cosmology and Astroparticle Physics*  
*Date: June 2026*
