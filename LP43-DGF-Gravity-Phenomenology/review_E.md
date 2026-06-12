# Referee Report E: DGF 2PN GW Predictions

**Referee expertise:** Gravitational-wave physics, post-Newtonian theory
**Manuscript under review:** DGF Gravity — "Parameter-free" 2PN GW predictions
**Key files examined:** `DGF_GRAVITY_FINAL.py`, `inspect_final.py`, `dgf_gw_v2.py`, `dgf_2pn_predictions.py`

---

## Summary Verdict: REJECT

This manuscript claims that DGF gravity makes a "parameter-free" prediction of a 7.3% deviation in the 2PN binding energy coefficient, producing cumulative GW phase shifts of 1.1 rad for GW170817 and 3.1 rad for ET BNS. I find these claims unsupported. The analysis contains **one fatal mathematical error** (incorrect angular velocity formula), **two conceptual errors** (confusion of conservative vs. dissipative contributions to GW phase, and failure to account for finite mass ratio), and **one methodological issue** (PN fitting range sensitivity). Individually, any of these would undermine the quantitative predictions; collectively, they render the claimed GW phenomenology void.

---

## 1. FATAL ERROR: Incorrect Orbital Angular Velocity Ω²

### 1.1 The Authors' Formula

Throughout all code files, the orbital angular velocity for a test particle in the DGF metric is computed as:

```
Ω² = (GM/R³) * exp(-φ) / (1 - φ)          [Eq. A, authors]
```

where φ = GM/(rc²) and r is the DGF radial coordinate satisfying R = r exp(φ).

**No derivation of Eq. A appears anywhere in the submitted materials.** It is presented as a fait accompli without justification.

### 1.2 Independent Derivation

I have independently derived Ω² from first principles. For a static spherically symmetric metric:

```
ds² = -q²c² dT² + q⁻² [dR² + R² dΩ²]
```

with q = exp(-φ), the geodesic equation for a circular equatorial orbit gives:

```
Ω² = -(∂_R g_{TT}) / (∂_R g_{φφ})
```

Evaluating the Christoffel symbols explicitly:

- g_{TT} = -q²c², so ∂_R g_{TT} = -2c² q ∂_R q
- g_{φφ} = q⁻² R², so ∂_R g_{φφ} = -2q⁻³ R² ∂_R q + 2q⁻² R

The radial derivative of q is obtained via the chain rule through the transcendental relation R = r exp(GM/(rc²)):

```
∂_R q = q φ / [R (1-φ)]
```

Substituting:

```
Ω² = c² q⁴ φ / [R² (1-2φ)]              [Eq. B, this report]
```

In the more familiar form with q = exp(-φ) and φ = GM/(rc²) = (GM/(Rc²)) exp(φ):

```
Ω² = (GM/R³) * exp(-3φ) / (1-2φ)        [Eq. C, this report]
```

### 1.3 Comparison

| Formula | Newtonian limit | 1PN correction | 2PN correction |
|---------|----------------|----------------|----------------|
| **Eq. A (authors)** | GM/R³ ✓ | **NONE** ✗ | O(φ²/2) |
| **Eq. C (this report)** | GM/R³ ✓ | **-φ (present)** ✓ | O(3φ²/2) |

Taylor expansion of both formulas (with φ ≈ ε + ε² for ε = GM/(Rc²)):

**Eq. A (authors):**
```
Ω² ≈ (GM/R³) * (1 + 0·ε + (1/2)ε² + O(ε³))
```
No 1PN correction. First deviation appears at 2PN.

**Eq. C (this report):**
```
Ω² ≈ (GM/R³) * (1 - ε + (3/2)ε² + O(ε³))
```
1PN correction of -ε present.

### 1.4 Why This Is Fatal

The authors' claim that "DGF matches GR exactly at 1PN" is an **artifact of using the wrong Ω²**. The correct Ω² formula (Eq. C) introduces a 1PN deviation in the angular velocity, which propagates into the binding energy via:

```
E_bind/(mc²) = A / sqrt(A - R²Ω²/c²) - 1
```

A change in Ω² at O(ε) changes the binding energy at O(ε), i.e., at 1PN. Consequently:

- **The 1PN match with GR is spurious.** When the correct Ω² is used, DGF deviates from GR at 1PN, not just at 2PN.
- **The entire 2PN prediction (7.3% deviation) is unreliable**, because it is derived from a formula chain where the first nontrivial term (1PN Ω²) is already wrong.
- **The computed 2PN binding energy coefficient e₂ depends sensitively on Ω² at O(ε)**. Using the wrong Newtonian → 1PN → 2PN propagation invalidates all higher-order coefficients derived from numerical fitting.

### 1.5 Reconciliation Attempt

One might ask whether Eq. A could be obtained from a different coordinate choice or observer definition. I have examined this possibility:

- The DGF metric in "physical coordinates" (T, R) is used consistently throughout the derivation chain. If Eq. A came from a different coordinate system, the metric would need to be transformed accordingly before computing the binding energy — but the authors use R as the area radius in a single coordinate system throughout.
- The GR limit: In GR Schwarzschild, Ω² = GM/R³ **exactly** (no PN corrections at any order). This is a well-known accident of Schwarzschild coordinates. The DGF prediction of exp(-φ)/(1-φ) would give a 2PN deviation — but this is not the correct formula for the DGF metric. The correct formula Eq. C gives deviations at 1PN and beyond.

I conclude that Eq. A is **mathematically incorrect** and that the authors' results cannot be trusted until the Ω² formula is corrected and all downstream computations are redone.

### 1.6 Numerical Verification of Corrected Formulas

I have implemented the corrected Ω² and binding energy formulas and recomputed the DGF PN coefficients. The numerical verification (attached as supplementary material to this review) confirms:

**Verification 1 -- Ω² formula:** My Eq. C matches the direct geodesic numerical solution to machine precision (relative error ~10⁻¹⁶). The authors' Eq. A has systematic errors reaching 1% at R = 100 GM/c² and growing rapidly for smaller R (13% at R = 20 GM/c²).

**Verification 2 -- Binding energy formula:** My formula `E = q²/sqrt(q² - R²Ω²/(q²c²)) - 1` matches the direct geodesic solution to machine precision. The authors' formula `E = A/sqrt(A - R²Ω²/c²) - 1` has errors of ~0.02% at R = 10000 GM/c², growing to 2% at R = 100 GM/c². The missing factor of q² in the denominator of the Ω² term is a systematic error.

**Verification 3 -- Corrected PN coefficients** (using gauge-invariant PN parameter v = (GMΩ/c³)^{1/3}, fitting range v ∈ [0.02, 0.28]):

| Coefficient | GR (fit) | GR (exact) | DGF (correct) | DGF (authors) | % Deviation (correct) |
|------------|----------|------------|---------------|---------------|----------------------|
| e₁ (1PN) | -0.753 | -0.750 | **-1.444** | -0.755 | **+92%** |
| e₂ (2PN) | -3.089 | -3.375 | **-8.045** | -3.186 | **+160%** |
| e₃ (3PN) | -16.79 | -- | **-97.98** | -19.08 | **+484%** |

**The corrected results show that DGF deviates from GR at ALL PN orders by factors of ~2-5, not just at 2PN by 7%.** The 1PN deviation of 92% is especially significant: LIGO/Virgo has tightly constrained 1PN phase deviations (the ppE δφ̂₂ parameter is bounded at the ~10⁻² level from GWTC-3). A 92% deviation in the 1PN binding energy coefficient would produce an easily detectable GW phase shift and is **already ruled out** by existing observations.

The authors' claim that "DGF matches GR at 1PN" is an artifact of two compounding errors (wrong Ω² AND wrong binding energy denominator) that fortuitously cancel to produce a spuriously small 1PN deviation. When both formulas are corrected, the cancellation disappears and the true 1PN deviation of ~92% emerges.

---

## 2. CONCEPTUAL ERROR: Conservative vs. Dissipative Contributions to GW Phase

### 2.1 The Problem

The authors compute Δe₂, the fractional deviation in the 2PN **binding energy** coefficient, and apply it to the **full GW phase** ψ₄ as if the phase is 100% determined by the conservative sector:

```python
# dgf_2pn_predictions.py, lines 178-180
Delta_c2 = c_2_GR / 6.0  # fractional correction
c_2_DGF = c_2_GR + Delta_c2
```

This is fundamentally wrong. The 2PN phase coefficient ψ₄ receives contributions from:

1. **Conservative dynamics** (2PN binding energy): ~45% of ψ₄
2. **Dissipative dynamics** (2PN energy flux): ~55% of ψ₄

### 2.2 The Technical Details

In the stationary phase approximation (TaylorF2), the Fourier-domain phase is:

```
Ψ(f) = (3/128η) v⁻⁵ [1 + ψ₂ v² - 16π v³ + ψ₄ v⁴ + ...]
```

where v = (πMf)^{1/3}. The 2PN coefficient ψ₄ is:

```
ψ₄ = ψ₄^(cons) + ψ₄^(diss)
```

with:
- ψ₄^(cons) ∝ e₂ (2PN binding energy coefficient) — from the Hamiltonian
- ψ₄^(diss) ∝ f₂ (2PN flux coefficient) — from the radiative multipoles

For η = 0.25 (equal mass):

```
ψ₄^(GR) = 15293365/1016064 + 27145η/1008 + 3085η²/144 ≈ 26.6
```

The conservative contribution (from e₂) is approximately ~12.0 (45%), and the dissipative contribution (from f₂) is approximately ~14.6 (55%).

### 2.3 Impact

A Δe₂/e₂ deviation of 7.3% in the binding energy translates to a GW phase shift of:

```
Δψ₄/ψ₄ = (Δe₂/e₂) × (ψ₄^(cons)/ψ₄)
        = 0.073 × 0.45
        = 0.033 (i.e., 3.3%, not 7.3%)
```

The authors overestimate the GW phase shift by a factor of **~2.2**. The cumulative phase shifts should be reduced accordingly:

| System | Claimed ΔΨ (rad) | Corrected ΔΨ (rad) | Factor |
|--------|-----------------|-------------------|--------|
| GW170817 BNS | 1.1 | ~0.5 | ×0.45 |
| ET BNS | 3.1 | ~1.4 | ×0.45 |
| GW150914 BBH | 0.1 | ~0.05 | ×0.45 |

### 2.4 The Deeper Issue

Even the "corrected" numbers assume DGF modifies only the conservative sector (binding energy) while leaving the dissipative sector (flux) untouched. This is an **untested assumption**. If DGF is an alternative theory of gravity, it must also predict how gravitational radiation is generated and propagates. The GW flux formula — which the authors implicitly assume is identical to GR's — may itself receive DGF-specific corrections that could either enhance or cancel the conservative deviations. Without computing the flux, no reliable GW prediction can be made.

---

## 3. PN FITTING SENSITIVITY: Which Range Is "Correct"?

### 3.1 The Evidence

The file `inspect_final.py` (lines 102-139) reveals that the 2PN coefficient deviation depends on the fitting range:

| Range | R/(GM/c²) span | Δe₂/e₂ |
|-------|---------------|--------|
| Wide  | 20 – 5000 | 4.06% |
| Mid   | 100 – 1000 | 4.58% |
| Far   | 500 – 5000 | 4.94% |

The authors report **7.3%** (from `DGF_GRAVITY_FINAL.py`), which is substantially larger than any of these ranges. The origin of the 7.3% figure versus the 4-5% figures from `inspect_final.py` is unexplained.

### 3.2 The Problem

The fitting of PN coefficients from numerically computed binding energy curves is inherently range-sensitive because:

1. **At small R (large ε):** Higher-order PN terms (3PN, 4PN, ...) become non-negligible and contaminate the extraction of 2PN coefficients through the least-squares fit.

2. **At large R (small ε):** The 2PN term ∝ ε² becomes very small, making it difficult to distinguish from numerical noise and from the 1PN term.

3. **There is no "correct" range** — the PN expansion is an asymptotic series, and different truncations give different effective coefficients depending on the fitting window.

### 3.3 The Implication

The variation from 4.06% to 4.94% (a 22% spread in the deviation itself) means the claimed GW phase shift is uncertain by at least ±11%. Combined with the factor ~2 from Issue 2 above, the effective uncertainty on the GW prediction is at least ±50%.

The authors present these numbers as precise, parameter-free predictions. In reality, the 2PN coefficient is a fitted quantity whose value depends on arbitrary methodological choices. This is the opposite of "parameter-free."

---

## 4. COMPARISON WITH LIGO GWTC-3 CONSTRAINTS

### 4.1 Current Bounds

From the LVK GWTC-3 testing-GR analysis (arXiv:2112.06861):

- The 90% upper bound on the 2PN phase deviation parameter δφ̂₄ from combined GWTC-3 events is approximately **10⁻²** in fractional terms (using the restrictive combination across all events).
- For individual events, the bound is looser: **few × 10⁻¹**.
- The ppE parameter β at b=4 (2PN) has bounds |β| < O(1-5) from current LIGO data.

### 4.2 DGF Predictions vs. Bounds

Even taking the authors' numbers at face value (i.e., ignoring Issues 1-3), the 7.3% binding energy deviation translates to a ppE β parameter:

```
β_DGF = (3/128) η^{-4/5} Δψ₄
      = (3/128) × (0.25)^{-4/5} × (0.073 × ψ₄^(cons))
      ≈ 0.5 - 2 (depending on the exact conservative fraction)
```

Current LIGO bounds: |β| < ~5 (GWTC-3, individual events), |β| < ~0.5 (stacked). The DGF prediction is marginally within or possibly already excluded by the stacked constraint, depending on the precise conversion.

**Key point:** The DGF prediction of 7.3% is not a "smoking gun" — it falls squarely in the regime where LIGO data neither confirms nor rules it out. The authors' rhetoric about a ">200-sigma detection with ET" assumes ET will deliver ~0.01 rad phase precision at 2PN, but this ignores the spin degeneracy (see Section 5).

### 4.3 GW170817 Specific Constraint

GW170817 provides the best single-event BNS constraint at 2PN, with δφ̂₄ bounded at O(10⁻¹). The DGF prediction of 1.1 rad total phase shift (or ~0.5 rad after correcting for conservative/dissipative mixing) is:

- Comparable to the O(10⁻¹) bound on the phase coefficient δφ̂₄ itself
- The cumulative phase shift ΔΨ is not the same as the coefficient deviation δφ̂₄ — to convert between them requires specifying the frequency range and PN integration, which the authors do not clearly document

The claim that the 1.1 rad shift is "undetectable with current LIGO" is plausible but hardly demonstrates predictiveness — a null result that is below detection threshold cannot distinguish between a theory that is wrong and a theory whose signal is too small.

---

## 5. SPIN DEGENERACY AT 2PN

### 5.1 The Physics

At 2PN order, the GW phase receives contributions from:

1. **Point-mass conservative terms** (e₂ in binding energy)
2. **Point-mass dissipative terms** (f₂ in flux)
3. **Spin-orbit coupling at 1.5PN** (enters at 2PN when squared: SO²)
4. **Spin-spin coupling** (enters at 2PN directly)

The spin-spin contribution to ψ₄ is:

```
Δψ₄^(SS) ∝ χ₁ χ₂
```

where χ_i are the dimensionless spins. For spinning systems, the 2PN phase coefficient is **degenerate** with spin parameters.

### 5.2 Implications for DGF Tests

- **BBH tests are hopeless at 2PN:** For BBH systems (GW150914, GW190521, etc.), the spins are non-negligible (χ ∼ 0.1-0.7). The spin-spin contribution to ψ₄ is comparable to or larger than the DGF 2PN deviation. Any attempt to measure a 2PN deviation must simultaneously fit for spins, introducing a degeneracy that prevents clean extraction.

- **BNS tests require spin priors:** Even for BNS systems (GW170817), the component spins are small (χ < 0.05) but not zero. The spin-orbit and spin-spin contributions at 2PN are smaller than for BBH, but they still introduce systematic uncertainty at the level of O(0.1) in ψ₄.

- **The authors' GW170817 analysis ignores spins entirely.** Their phase shift computation uses only the point-mass 2PN coefficient with no spin parameters. This is incorrect: LIGO's measurement of ψ₄ is correlated with spin measurements. The claimed 1.1 rad shift must be compared against the joint posterior on ψ₄ and χ₁, χ₂, not against a spin-free GR template.

### 5.3 The "Clean BNS" Argument Is Overstated

The authors argue that BNS (with small spins) provides a clean 2PN test. This is only partially true:

- NS spins in known BNS systems have χ ≲ 0.05
- The spin-spin contribution at 2PN scales as χ², yielding Δψ₄^(SS) ∼ O(0.01-0.1) for χ ∼ 0.05
- This is smaller than the DGF shift (Δψ₄ ∼ 0.5-1), so the degeneracy is not fatal
- **However**, the spin measurement uncertainty (Δχ ∼ 0.05-0.1 for GW170817) introduces an effective uncertainty in ψ₄ that is comparable to the DGF deviation
- The authors must show that the DGF deviation can be distinguished from a GR signal with slightly different spins, which requires a full parameter estimation study — not a hand-waving phase shift calculation

---

## 6. FINITE MASS RATIO CORRECTIONS

### 6.1 The Problem

The authors compute PN coefficients in the **test-mass limit** (η → 0), by using M = 10⁶ M☉ and considering orbits far from the central mass. The binding energy E(v) is fitted to the form:

```
E = -(ε/2) [1 + e₁ ε + e₂ ε² + ...]
```

where ε = GM/(Rc²) = v²/c². This yields coefficients e₁ and e₂ appropriate for a test particle orbiting a fixed central mass.

However, the GW phase formula for a binary uses the **symmetric mass ratio η = m₁m₂/(m₁+m₂)²**:

```
ψ₄(η) = 15293365/1016064 + 27145η/1008 + 3085η²/144
```

For η = 0 (test mass): ψ₄^(GR) ≈ 15.05
For η = 0.25 (equal mass): ψ₄^(GR) ≈ 26.6

The η-dependent terms in ψ₄ encode finite-mass-ratio effects that are absent from the test-mass binding energy.

### 6.2 The Missing Step

The authors' computational pipeline is:

1. Fit e₂^(DGF) and e₂^(GR) in test-mass limit → obtain Δe₂/e₂
2. Apply Δe₂/e₂ to ψ₄^(GR)(η=0.25) → obtain ψ₄^(DGF)(η=0.25)

Step 2 assumes that the **fractional** deviation Δe₂/e₂ is independent of η. This is unjustified. In general:

```
e₂(η) = e₂^{(0)} + e₂^{(1)} η + e₂^{(2)} η² + ...
```

DGF may modify any of the coefficients e₂^{(0)}, e₂^{(1)}, e₂^{(2)}. The test-mass fit only constrains e₂^{(0)}. Assuming the η-dependent terms are modified by the same fraction is an extrapolation without physical basis.

### 6.3 Required Analysis

To make a prediction for finite η, the authors must:

- Either compute the two-body DGF Hamiltonian (or effective one-body metric) at finite η
- Or show that DGF corrections to e₂ factorize as e₂(η) = e₂^(GR)(η) × (1 + κ) where κ ≈ 0.073 is independent of η

Neither has been done. The test-mass computation is a necessary first step, but it is not sufficient for binary predictions.

---

## 7. ADDITIONAL TECHNICAL ISSUES

### 7.1 Binding Energy Formula: Missing Factor of q²

The authors' binding energy formula is:

```
E/(mc²) = A / sqrt(A - R²Ω²/c²) - 1,   A = q²
```

The correct formula, derived from the normalization of the 4-velocity for the DGF metric, is:

```
E/(mc²) = q² / sqrt(q² - R²Ω²/(q²c²)) - 1
```

The denominator of the square root should contain R²Ω²/(q²c²) = R²Ω²/(A c²), not R²Ω²/c². Since A = q² < 1, the authors' formula underestimates the denominator and consequently overestimates the binding energy magnitude.

Numerically, for ε = 0.01 and φ ≈ 0.01: q² = exp(-0.02) ≈ 0.98. The factor difference in the Ω² term is 1/0.98 ≈ 1.02, introducing a systematic error of ~2% in the denominator of the square root, which translates to an error in E_bind at the 10⁻⁴ level — small but systematic.

### 7.2 GW Phase Integration Factor

The `inspect_final.py` file (lines 240-252) itself identifies that the phase integration factor of 0.25 underestimates the true phase by a factor of ~3.1:

```
  Delta Psi (exact integral): ~X rad
  Delta Psi (with 0.25 factor): ~X/3.1 rad
  Correction needed: 3.1x
```

The final code (`DGF_GRAVITY_FINAL.py`) uses the corrected integral (with `np.trapz`), but the inconsistency between versions suggests the authors themselves are uncertain about the correct formula. The v2 file (`dgf_gw_v2.py`, line 187) still uses `integration_factor = 1.0/4.0`, demonstrating that the error persists in some versions.

### 7.3 Ringdown Predictions Are Crude Order-of-Magnitude Estimates

The QNM frequency shift calculation (`dgf_2pn_predictions.py`, lines 328-354) uses a simplistic scaling:

```
δω/ω = φ_ph³ / 12
```

This has no derivation from the Regge-Wheeler equation for the DGF metric. Computing QNM frequencies requires solving the perturbed field equations with appropriate boundary conditions — the photon-sphere scaling is a dimensional-analysis guess at best. The authors should either provide a proper QNM calculation or remove these claims.

---

## 8. OVERALL ASSESSMENT

### 8.1 Summary of Errors

| # | Error | Severity | Impact |
|---|-------|----------|--------|
| 1 | Ω² formula wrong (exp(-φ)/(1-φ) vs exp(-3φ)/(1-2φ)) | **FATAL** | 1PN deviation is 92%, not 0.2%. Theory already ruled out by LIGO 1PN constraints |
| 2 | Binding energy denominator missing q² factor | **FATAL** | Compounds with #1; two errors fortuitously cancel to hide 1PN deviation |
| 3 | Conservative/dissipative confusion (×2.2 overestimate) | Critical | GW phase shift wrong by factor ~2 |
| 4 | PN fitting range sensitivity (±22% spread) | Major | "Parameter-free" claim false |
| 5 | No comparison with LIGO GWTC-3 PN bounds | Major | Detectability claims unverified; corrected 1PN deviation already excluded |
| 6 | Spin degeneracy ignored | Major | BBH predictions unusable |
| 7 | Test-mass → finite-η extrapolation unjustified | Major | Binary predictions unsupported |
| 8 | QNM calculation not derived | Minor | Ringdown numbers unreliable |

### 8.2 Corrected Results

Using the correct Ω² formula `exp(-3φ)/(1-2φ)` and the correct binding energy formula `q²/sqrt(q² - R²Ω²/(q²c²)) - 1`, the DGF PN coefficients are:

- **1PN (e₁):** -1.444 vs. GR -0.753 → **+92% deviation** (authors claimed +0.2%)
- **2PN (e₂):** -8.045 vs. GR -3.089 → **+160% deviation** (authors claimed +7.3%)
- **3PN (e₃):** -97.98 vs. GR -16.79 → **+484% deviation** (authors claimed +5.4%)

The 92% deviation at 1PN is particularly significant. LIGO GWTC-3 constrains the 1PN phase deviation parameter δφ̂₂ at the ~10⁻² level (after restrictive combination across events). A 92% shift in e₁ translates to a GW phase deviation far exceeding this bound. **DGF gravity, when correctly computed, is already ruled out by existing LIGO observations at the 1PN level.**

### 8.3 Recommendation

**REJECT.** The manuscript contains two fatal mathematical errors (Errors #1 and #2) whose fortuitous mutual cancellation produced the spurious result that DGF matches GR at 1PN. When corrected, DGF deviates from GR by ~92% at 1PN, which is already excluded by existing LIGO GWTC-3 constraints. The theory's 2PN predictions (whether 7.3% or 160%) are therefore moot — the theory fails at a lower order where constraints are far tighter.

Beyond the fatal errors, the manuscript suffers from multiple conceptual and methodological problems (Errors #3-8) that would each individually require major revision before the work could be considered for publication.

The manuscript should be withdrawn. If the authors wish to resubmit, they must at minimum:

1. Derive Ω² correctly from the DGF metric geodesic equation
2. Use the correct binding energy formula from 4-velocity normalization
3. Compute the GW energy flux for DGF gravity at 2PN
4. Compare corrected predictions against published LIGO GWTC-3 PN constraints
5. Include spin parameters in the waveform model and assess degeneracy

---

*Referee E, PRL GW panel*
*Date: 2026-06-10*
