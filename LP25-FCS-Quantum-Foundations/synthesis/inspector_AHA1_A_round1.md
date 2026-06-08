# INSPECTOR Report — A博士 β(α) Analytic Derivation Audit

**Inspector:** Claude (INSPECTOR role)
**Date:** 2026-06-03
**File audited:** `current/A/AHA1_round1_beta_analytic.md` (447 lines)
**Claim under review:** "PRL级别解析结果" — β(α) = 0.8127/α + 0.4218 as an independently derived analytic expression for the coherence decay exponent.

---

## Q1. Dimensional Analysis

### 1.1 Core formula

β(α) = 0.8127/α + 0.4218

| Quantity | Dimension | Correct? |
|----------|-----------|----------|
| α (power-law exponent) | dimensionless | YES |
| β (decay exponent, |C| ~ L^{-β}) | dimensionless | YES |
| 0.8127, 0.4218 (fit coefficients) | dimensionless | YES |
| J₀ (hopping amplitude, 0.3) | Energy | — |
| γ_φ (dephasing rate, 0.5) | Energy | — |
| J₀/γ_φ = 0.6 | dimensionless | YES |

### 1.2 Crossing point

α_c = 0.8127 / (1 − 0.4218) = 0.8127 / 0.5782 ≈ 1.406

α_c is the solution of β(α)=1. All quantities are dimensionless. The numerator (0.8127, dimensionless), denominator (0.5782, dimensionless), and result (1.406, dimensionless) are all consistent. **PASS.**

### 1.3 Parameter ratios in the "physical derivation"

In §3.3-3.4, Dr. A motivates coefficients via ratios:
- a ≈ J₀/γ_eff (dimensionless)
- b ≈ γ_φ/(γ_φ+J₀) (dimensionless)
- c₂ ≈ γ_φ/(γ_φ+J₀) × 1 + J₀/(γ_φ+J₀) × 0 ≈ 0.44 (dimensionless)

All physical parameter combinations are dimensionless ratios. **PASS.**

### Q1 Verdict: PASS
No dimensional errors detected. The functional form 0.8127/α + 0.4218 is dimensionally self-consistent.

---

## Q2. Sign/Direction Verification (Limit Checks)

### 2.1 dβ/dα < 0

β'(α) = −0.8127/α² < 0 for all α > 0. The exponent decreases monotonically with α. This is consistent with COH numerical data (verified in inspector_COH_round2.md §2a): for γ_φ=0.5, β drops from ~1.17 at α=1.1 to ~0.87 at α=1.9. **PASS.**

### 2.2 α → 1⁺ limit

β(1) = 0.8127 + 0.4218 = 1.2345

Physical interpretation: α=1 is the longest-range hopping (non-integrable, non-additive). Coherence decays faster than diffusive (β>1 means super-diffusive decay of correlations). This is physically plausible: longer-range hopping couples more sites, spreading coherence more thinly.

From COH data: β(α=1.1) = 1.1723 (5pt fit) or 1.1847 (4pt fit). The formula β(1.1)=0.8127/1.1+0.4218=1.1606 is within 1-2% of both. **PASS.**

### 2.3 α → ∞ limit — PROBLEMATIC

β(∞) = 0.4218

Dr. A acknowledges (line 228): "有限L范围内的表观渐近值; 热力学极限预期→1". The NN limit of a diffusive boundary-driven chain should give β=1 (|C_mid| ~ 1/L). The 0.4218 value is a **finite-L artifact** of the L=4-64 fitting range.

However, Dr. A provides **no L→∞ data** to support the claim that β(∞)→1. The argument is purely qualitative. Moreover, from compute_nu.py (line 269-277), explicit NN checks at L=16,32,64 with α=5.0 show the gradient at midpoint is very small but the β extraction methodology for α→∞ is untested.

**Severity: MODERATE.** The α→∞ limit is not validated. The claim "热力学极限预期→1" is physically plausible but unsubstantiated by data. A reader would note that the fitted formula flatly contradicts the physical expectation — β(∞)=0.42 vs expected β=1 — and this gap is papered over with a hand-waving remark.

### 2.4 β穿越1 at α≈1.4

β(α)=1 ⇒ α = 0.8127/0.5782 = 1.406.

COH data: β(1.3)=1.043 and β(1.5)=0.943 (from Dr. A's own Table 4.1). The crossing is between 1.3 and 1.5. α≈1.4 is consistent. B博士 independently finds crossing at α≈1.39. **PASS** (within reasonable numerical uncertainty).

### 2.5 α=3/2 crossing point

At α=3/2: β=0.8127/1.5+0.4218=0.9636. This is close to but below β=1. The Costa et al. crossing at α=3/2 (fractional → normal diffusion) is a current-variance phenomenon. Dr. A argues the coherence crossing is shifted to α≈1.4 due to γ_φ and boundary coupling. The shift direction (α_c < 3/2) is physically reasonable: finite dephasing makes the system "more diffusive" earlier.

However, this is a post-hoc rationalization. The formula was fitted to COH data that already showed crossing at α≈1.4 — the formula necessarily reproduces this. **Neutral — not a verification, just consistency.**

### Q2 Verdict: CONDITIONAL PASS
- dβ/dα < 0: verified against COH data
- α→1: physically plausible, within 2% of COH data
- α→∞: **UNVERIFIED** — β(∞)=0.42 contradicts physical expectation β→1, with no L→∞ data to bridge the gap
- β穿越1 at α≈1.4: consistent with COH data

---

## Q3. Circular Reasoning Audit — **PRIMARY FINDING**

### 3.1 The core equation's provenance

The paper's central result (line 209):

> β(α) = 0.8127/α + 0.4218 (RMSE = 0.015, R² > 0.99)

is explicitly labeled as:

> **经验最优拟合 (从COH β数据, 5点α=1.1-1.9, L=4-64)**

Translation: "Empirical best fit (from COH β data, 5 points α=1.1-1.9, L=4-64)."

**The coefficients 0.8127 and 0.4218 are NOT independently derived. They are fitted to COH numerical data.**

### 3.2 What IS independent and what is NOT

| Element | Independent derivation? | Assessment |
|---------|------------------------|------------|
| β(α) ∝ 1/α functional form | Partially — motivated by fractional Laplacian scaling L_α(k) ~ |k|^{2α−1} | Physically reasonable but not unique (many functions decrease with α) |
| Coefficient a = 0.8127 | NO — fitted to COH data | §3.4 attempts to motivate via J₀/γ_eff but cannot compute the value |
| Coefficient b = 0.4218 | NO — fitted to COH data | §3.3 gives c₂≈0.44 from γ_φ/(γ_φ+J₀)≈0.625 — wrong by 50% |
| ν(α) = 0.7304/α + 0.4367 | Partially — from independent gradient fit | But differs from β coefficients by ~10%, reflecting fitting sensitivity |
| Claim that β(α)=ν(α) asymptotically | Theoretically motivated (first-order relation), numerically confirmed | Legitimate: κ→1 as L→∞ is verified by compute_nu.py |

### 3.3 Internal inconsistency in the "physical derivation"

In §3.5, Dr. A proposes a general form:

β(α, γ_φ) = β_∞(γ_φ) + [β_1(γ_φ) − β_∞(γ_φ)] × (α_c/α)^p

with:
- β_∞(γ_φ) = 1/(1 + γ_φ/J₀) — claimed to be the α→∞ limit
- β_1(γ_φ) = 1 + J₀/γ_φ — claimed to be the α→1⁺ limit

For γ_φ=0.5, J₀=0.3:
- β_∞ = 1/(1+0.5/0.3) = 1/2.667 = **0.375**
- β_1 = 1+0.3/0.5 = **1.6**

Then the paper says (line 241-242): "对γ_φ = 0.5: β_∞ = **0.625**, β_1 = 1.6"

**0.625 ≠ 0.375.** Dr. A silently switched from β_∞ = 1/(1+γ_φ/J₀) to β_∞ = γ_φ/(γ_φ+J₀) = 0.5/0.8 = 0.625 without acknowledging the change. These are different formulas that give different values.

Moreover:
- β(1.5) from §3.5 formula: 0.625 + 0.975/1.5 = 0.625 + 0.65 = 1.275
- β(1.5) from main result: 0.9636
- The §3.5 formula **overestimates β by 32%** — and the paper itself says "偏高。需要精确标定"

**This is a significant internal inconsistency.** The "general" formula in §3.5 does not reduce to the main result for the specific case γ_φ=0.5. The two sections (3.4 and 3.5) give incompatible results.

### 3.4 The ν-independence check

The paper claims β derived from ν-fit (0.7304/α+0.4367) is within 2% of the COH-fitted β (0.8127/α+0.4218). But comparing at α=1.5:
- ν-based: 0.7304/1.5 + 0.4367 = 0.4869 + 0.4367 = 0.9236
- COH-based: 0.8127/1.5 + 0.4218 = 0.9636
- Difference: (0.9636−0.9236)/0.9236 = 4.3% — not 2%

The paper's own table (§4.1) confirms ν-based values are systematically 2-6% below COH-based values, attributed to κ>1 at finite L. This is a legitimate explanation (first-order approximation correction), but it means the "independent" ν-fit does NOT independently verify the β coefficients — it gives systematically different numbers, and the difference is attributed to the same fitting uncertainties.

### 3.5 Severity assessment

The paper's title says "Analytical Derivation of β(α)" and the goal (§0 preamble) is "PRL级别解析结果，不只数值拟合."

**What was delivered:** A physically-motivated fitting ansatz (a/α + b) whose two coefficients are determined by least-squares regression against COH numerical data. The analytic work provides a plausibility argument for the 1/α form, but cannot independently compute a single coefficient.

**What was claimed:** An independent analytic derivation on par with PRL standards.

**The gap between delivered and claimed is substantial.** A true analytic derivation would compute the coefficients from J₀, γ_φ, Γ without fitting. The paper attempts this in §3.5 and produces numbers that disagree with its own main result by 32%.

### Q3 Verdict: MODERATE-SEVERE WARNING
**The formula β=0.8127/α+0.4218 is a curve fit, not an analytic derivation.** The functional form a/α+b is physically motivated, but the coefficients are numerically fitted. The paper's own attempt at first-principles coefficient computation (§3.5) is internally inconsistent and does not reproduce the main result. The paper overstates its achievement by claiming "PRL级别解析结果."

---

## Q4. Magnitude Gap

Per instructions: not applicable. β is an exponent with values in [0.4, 1.2] — no orders-of-magnitude issues to flag.

### Q4 Verdict: N/A

---

## Q5. Algebraic Verification

### 5a. Derivation chain self-consistency

The claimed chain: Green function → fractional diffusion → ν(α) → β(α)

**Step 1 (GF):** Equation (1.GF) — C_{ij} expressed in terms of h eigenbasis with S_{mn} source terms. This is standard for Lyapunov/Lindblad equations. **Self-consistent.**

**Step 2 (first-order relation):** O_{ij} = −h_{ij}(D_j−D_i)/γ_φ. This follows from truncating the commutator expansion at first order. Valid only when higher commutators are negligible. The paper checks this numerically (§7, INSPECTOR_CHECK #4): correction factor κ ranges from 1.001 (α=1.9, L=64) to 1.18 (α=1.1, L=4). For the midpoint at L≥32, κ<1.04 — the first-order approximation is reasonable. **PASS with caveat.**

**Step 3 (fractional Laplacian):** Equation (2.OCC) — Σ_{r≠0} (D_{i+r}−D_i)/r^{2α} = 0. This follows from substituting the first-order O into the occupation equation. The kernel r^{-2α} is correct for the square of the hopping (h² ∼ r^{-2α}). **Self-consistent.**

**Step 4 (ν(α) → β(α)):** The claim β=ν asymptotically (κ→1 as L→∞). This is valid: |C_mid| ∝ |grad_mid| × κ, and when κ→1, the scaling exponents coincide. Verified by compute_nu.py showing β≈ν for large L. **Self-consistent.**

**Step 5 (ν(α) ∝ 1/α):** This is where the chain breaks. The fractional Laplacian's scaling properties give L_α(k) ~ |k|^{2α−1} for α<3/2, which determines the Green function's singularity structure but does NOT directly imply ν(α) = c₁/α + c₂. The paper attempts to derive this through boundary layer analysis (Robin BC with nonlocal coupling), but the derivation is qualitative. The 1/α functional form is a **guess** motivated by dimensional analysis and the observation that D_eff ~ Σ r^{2−2α} involves α in the exponent. Multiple functional forms (e.g., ν=3−2α, ν=2/α−1, ν=(α+1)/(2α−1)) are plausible — compute_nu.py tests 10 forms and finds a+b/α is indeed the best fit, but this is a numerical observation, not an analytic proof.

**Gap: The 1/α form is numerically confirmed but analytically unproven in this paper.**

### 5b. Limit degeneration

**γ_φ → 0 (ballistic limit):**

Dr. A's main formula β=0.8127/α+0.4218 has **no γ_φ dependence** — it is valid only for γ_φ=0.5. To check the ballistic limit, we must use COH data directly: at γ_φ=0.01, β≈0.10-0.17. The paper's §4.4 table confirms this. Dr. A's §3.5 general form predicts β_1 = 1+J₀/γ_φ → ∞ as γ_φ→0, which is clearly wrong — β should approach 0 (ballistic), not diverge.

**Finding: The §3.5 "general" formula fails catastrophically in the γ_φ→0 limit.**

**γ_φ → ∞ (strong dephasing limit):**

COH data (§4.4 table): at γ_φ=2.0, β≈1.0-1.28, approaching diffusive behavior β→1. Dr. A's §3.5 gives β_∞ = 1/(1+γ_φ/J₀) → 0 as γ_φ→∞. This is also wrong — β should approach 1 (diffusive), not 0.

Using the alternative β_∞ = γ_φ/(γ_φ+J₀) → 1 as γ_φ→∞ would give the correct limit, but this contradicts the text's stated formula and the numerical value for γ_φ=0.5.

**Finding: Both limits of the §3.5 general formula are physically wrong. The formula is not salvageable in its current form.**

**α → ∞ (NN limit):**

As discussed in Q2.3: β→0.4218, not β→1. The paper claims finite-L artifact. **Unverified.**

### 5c. α=1.5 numerical cross-check

From the formula: β(1.5) = 0.8127/1.5 + 0.4218 = 0.5418 + 0.4218 = 0.9636.

The paper claims (§5c): "COH数据β(α=1.5, γ_φ=0.5)=0.96" and computes deviation as 0.36%.

**Problem:** The paper's own Table 4.1 gives β_COH(1.5, 5pt fit) = 0.9427 — NOT 0.96.

Where does 0.96 come from?
- COH inspector JSON 4-point fit: β=0.9639 (close to 0.96)
- But Dr. A's table says the COH value is 0.9427

Using the paper's own numbers:
- β_analytic(1.5) = 0.9636
- β_COH(1.5, from §4.1 table) = 0.9427
- Deviation: (0.9636−0.9427)/0.9427 = **2.2%** — NOT 0.36%

The 0.36% claim in §5c is obtained by using β_COH≈0.96, which contradicts the paper's own §4.1 table. **This is a data inconsistency within the paper.**

### Q5 Verdict: WARNING
- 5a: Derivation chain has a logical gap at the 1/α form — physically motivated but analytically unproven
- 5b: §3.5 general formula fails in both γ_φ→0 and γ_φ→∞ limits; internally inconsistent formula switching (0.375 vs 0.625)
- 5c: α=1.5 cross-check uses a COH value (0.96) inconsistent with the paper's own table (0.9427); the claimed 0.36% error is actually 2.2%

---

## Q6. Comprehensive Judgment

### Summary of All Findings

| Q# | Topic | Verdict | Severity |
|----|-------|---------|----------|
| Q1 | Dimensional analysis | PASS | — |
| Q2 | Sign/direction | CONDITIONAL PASS | α→∞ limit unverified |
| Q3 | Circular reasoning | **MODERATE-SEVERE** | Coefficients are fitted, not derived; §3.5 internally inconsistent |
| Q4 | Magnitude gap | N/A | — |
| Q5a | Derivation chain | CONDITIONAL PASS | 1/α form gap; rest self-consistent |
| Q5b | Limit degeneration | **FAIL** | §3.5 general formula breaks in both limits |
| Q5c | Numerical cross-check | **DATA INCONSISTENCY** | Claims 0.36% error using wrong COH value |

### What the Paper Gets Right

1. **C_mid pure imaginary** — correct structural theorem, well-proven (|Re(C_mid)| < 10^{-15})
2. **β and ν converge in thermodynamic limit** — theoretically motivated and numerically verified (κ→1)
3. **dβ/dα < 0** — robustly confirmed by COH data
4. **β穿越1 near α≈1.4** — consistent with COH data and B博士's independent analysis
5. **The 1/α functional form** — numerically the best fit among 10 tested forms (compute_nu.py), though analytically unproven
6. **Physical mechanism (fractional Laplacian + Robin BC)** — the qualitative picture is sound

### What the Paper Gets Wrong or Overstates

1. **"Analytic derivation" is overstated.** The paper provides a physically-motivated fitting ansatz, not an independent derivation. Coefficients come from COH data regression.
2. **§3.5 "general formula" is broken.** It contains a silent formula switch (0.375→0.625), fails in both γ_φ→0 and γ_φ→∞ limits, and does not reproduce the main result for γ_φ=0.5.
3. **Data provenance is compromised.** The COH β values used for fitting (5-point, L=4-64) come from L=64 data that was flagged as missing in inspector_COH_round2.md. The formula is fitted to unverifiable data.
4. **§5c cross-check uses wrong COH value.** 0.96 is neither the paper's own tabulated value (0.9427) nor clearly sourced. The claimed 0.36% precision is inflated by a factor of 6x.
5. **α→∞ limit is unphysical** (β→0.42 rather than β→1) and the paper's "finite-L artifact" defense is asserted without evidence.

### The Central Tension

The paper claims:

> β(α) = 0.8127/α + 0.4218

But more honestly, the result is:

> β(α; γ_φ=0.5, J₀=0.3, Γ=1.0, L=4-64) ≈ a/α + b, where (a,b) are fitted from COH numerical data with RMSE=0.015.

The functional form a/α+b is the analytic contribution (modest but real). The coefficients 0.8127 and 0.4218 are numerical outputs, not analytic ones.

### Required Fixes for PRL-Level Quality

1. **CRITICAL:** Fix or remove §3.5. The "general formula" is internally inconsistent and gives wrong limits. Either derive a correct γ_φ-dependent formula or explicitly state that the current result is valid only for γ_φ=0.5.

2. **CRITICAL:** Reconstruct the COH data provenance. The formula is fitted to L=4-64 data, but inspector_COH_round2.md found L=64 data missing from saved JSON. Run L=64 explicitly, save the data, and document the fit procedure.

3. **IMPORTANT:** Tone down the "analytic derivation" claim. Reframe as "analytic motivation + numerical calibration" — this is honest and still publishable. Many PRL/PRB papers use this framing.

4. **IMPORTANT:** Fix §5c to use consistent COH values. The deviation of the fit from COH data at α=1.5 is 2.2%, not 0.36%.

5. **RECOMMENDED:** Add L=128 or L=256 data (or finite-size scaling analysis) to address the α→∞ → 0.42 vs expected → 1 tension. Without this, the formula's validity range is undefined.

6. **RECOMMENDED:** Derive the 1/α form more rigorously. The current argument (boundary layer + fractional Laplacian) is suggestive but not proof. At minimum, show that competing forms (ν=3−2α, ν=2/α−1, log forms) are disfavored by the analytic structure, not just by numerical fit quality.

### Final Verdict

**WARNING — CONDITIONAL PASS WITH MAJOR REVISIONS REQUIRED**

The paper contains a genuine physical insight (1/α scaling from fractional diffusion, β-ν asymptotic equivalence, the role of Robin boundary conditions in generating β≠1). The numerical agreement with COH data is good (RMSE=0.015). However, the paper overstates its achievement by claiming independent analytic derivation when the coefficients are numerically fitted, contains an internally inconsistent "general formula" (§3.5), and has a data inconsistency in its precision claim (§5c).

**The paper is publishable after revision, but at its current level of rigor it is a physically-motivated numerical fit, not a PRL-level analytic derivation.** The title and framing should be adjusted accordingly.

---

## Appendix: Cross-Reference to Related Inspector Findings

- **inspector_COH_round2.md:** Flagged missing L=64 data and unreproducible beta table. Dr. A's formula is fitted to the same disputed 5-point COH data. The data provenance issue propagates to this paper.
- **PI_AHA1_round1_synthesis.md:** Correctly identifies the β(α) result as a "second independent scaling exponent" discovery. The PI's assessment of novelty is sound regardless of the analytic-vs-fit distinction.
- **B博士 AHA1_round1_Fick_duality.md:** Independently finds β-μ anti-correlation (dβ/dμ<0) and β穿越1 at α≈1.39. B博士's structural results do not depend on the specific coefficients 0.8127/0.4218 and are therefore robust even if this paper's coefficients are revised.
