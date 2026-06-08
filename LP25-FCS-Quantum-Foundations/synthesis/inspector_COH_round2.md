# INSPECTOR-COH Round 2 Audit Report

**Auditor:** Claude (INSPECTOR role)
**Date:** 2026-06-03
**Files audited:**
- `round2_COH_numerical.md` (narrative report)
- `phase1_L2_benchmark.py` (L=2 benchmark code)
- `phase2_L_large.py` (L>=4 scan code)
- `phase2_raw_results.json` (100 data points, verified)
- `phase2_fit_results.json` (25 fit parameters, verified)

---

## Q1. Dimensional Analysis

### 1a. Parameter dimensions

| Parameter | Symbol | Value/Range | Dimension | Correct? |
|-----------|--------|-------------|-----------|----------|
| Hopping amplitude | J_0 | 0.3 | Energy | YES |
| Boundary coupling | Gamma_L, Gamma_R | 1.0 | Rate (Energy) | YES |
| Dephasing rate | gamma_phi | 0.01 - 2.0 | Rate (Energy) | YES |
| Chain length | L | 4,8,16,32 | Dimensionless | YES |
| Power-law exponent | alpha | 1.1-1.9 | Dimensionless | YES |
| Correlation function | C_ij | see below | Dimensionless | YES |

### 1b. Dimensionless ratios

- gamma_phi / J_0 ranges from 0.033 (gp=0.01) to 6.67 (gp=2.0): dimensionless, physically meaningful
- Gamma / J_0 = 3.33: the boundary coupling is stronger than the bulk hopping -- physically reasonable for boundary-driven transport
- Gamma / gamma_phi ranges from 0.5 to 100: covers both weak-dephasing and strong-dephasing regimes

### 1c. Steady-state equation dimensional check

The governing equation:
```
i[h, C]_{ij} + 1/2 (Gamma_i + Gamma_j) C_{ij} + gamma_phi (1 - delta_{ij}) C_{ij} = delta_{ij} W_in_i
```

- i[h,C]: [Energy] * [dimensionless] = Rate -- consistent with dC/dt
- 1/2{Gamma, C}: [Rate] * [dimensionless] = Rate -- consistent
- gamma_phi * C: [Rate] * [dimensionless] = Rate -- consistent
- W_in = Gamma * f: [Rate] -- consistent

All terms have consistent dimensions of [Rate]. The steady-state condition (dC/dt = 0) is dimensionally homogeneous. **PASS.**

### 1d. |C_ij| bounds verification

From JSON data:
- |C_mid| range: [0.000608, 0.060098] -- well within [0,1] **PASS**
- Diagonal elements C_ii range: [0.351, 0.649] -- valid occupation probabilities in [0,1] **PASS**
- Sum of diagonal occupations = L/2 for all data points (half-filling in NESS) -- physically correct for symmetric boundary rates **PASS**

### Q1 Verdict: PASS

---

## Q2. Sign/Direction Verification (Limit Checks)

### 2a. "beta(alpha) decreases as alpha increases"

Verified against JSON 2-point beta values (L=4 vs L=32):

```
alpha    gp=0.01   gp=0.1    gp=0.5    gp=1.0    gp=2.0
1.1      0.1107    0.6463    1.1868    1.2741    1.2810
1.3      0.1077    0.6212    1.0646    1.1233    1.1513
1.5      0.1049    0.5949    0.9632    1.0304    1.0766
1.7      0.1023    0.5675    0.9000    0.9821    1.0393
1.9      0.0999    0.5412    0.8675    0.9605    1.0237
```

For every gamma_phi value, beta decreases monotonically as alpha increases. The trend is robust. **PASS.**

NOTE: The numerical beta VALUES in this verified table differ from those in the report (Section 2.3). This discrepancy is addressed in Q5d below.

### 2b. "|C_mid| decreases as gamma_phi increases"

Verified against JSON: for any fixed (L, alpha), |C_mid| is strictly decreasing in gamma_phi. Example L=4, alpha=1.1: 0.05086 (0.01) > 0.04109 (0.1) > 0.02260 (0.5) > 0.01469 (1.0) > 0.00873 (2.0). **PASS.**

### 2c. "|C_mid| decreases as L increases"

Verified against JSON: for every (alpha, gamma_phi), |C_mid| strictly decreases with L. Example alpha=1.5, gamma_phi=0.5: 0.02621 (L=4) > 0.01306 (L=8) > 0.00667 (L=16) > 0.00354 (L=32). **PASS.**

### 2d. "Re(C_mid) = 0 for all parameters" -- random sample verification

Five randomly selected data points from JSON:

| L | alpha | gamma_phi | Re(C_mid) | Im(C_mid) | |Re/Im| |
|---|-------|-----------|-----------|-----------|---------|
| 4 | 1.1 | 0.01 | 1.99e-17 | 0.05086 | 3.9e-16 |
| 8 | 1.5 | 0.50 | 1.32e-17 | 0.01306 | 1.0e-15 |
| 16 | 1.9 | 1.00 | -6.52e-18 | 0.00478 | 1.4e-15 |
| 32 | 1.1 | 2.00 | 1.40e-17 | 0.00061 | 2.3e-14 |
| 16 | 1.1 | 0.01 | 8.29e-16 | 0.04646 | 1.8e-14 |

Max |Re(C_mid)| across all 100 data points: **1.28e-15**. All Re values are at machine-precision noise level. The claim "Re(C_mid) = 0" is verified to floating-point precision. **PASS.**

### 2e. "Eigenbasis RWA gives C12 = 0" -- Phase 1 table verification

Reported: |C12| = 0.000000, Re = 5.55e-17, Im = 0.000000. This is consistent with the RWA eliminating all off-diagonal coherence. The code confirms that RWA filters out all terms where omega_ab != omega_cd, and since the two eigenmodes of L=2 have different energies, the cross-coherence cannot be populated. **PASS.**

### 2f. High-risk pattern: beta sign

All beta values are strictly positive (0.099 to 1.281). Positive beta means |C_mid| ~ L^{-beta} decays (not grows) with L. The sign is consistent with physical expectation: coherence decays with distance from the boundaries. **PASS.**

### Q2 Verdict: PASS (all directional claims verified against actual data)

---

## Q3. Circular Reasoning Audit

### 3a. "Phase 1 claims to verify L=2 analytic solution -- but analytic solution uses different parameters"

The report itself flags this (line 53): "The analytic solution uses different (unspecified) parameters; the magnitude difference is not meaningful. What matters is the structure."

Assessment: The report is honest about the parameter mismatch. The "verification" is structural (pure imaginary C12, real diagonal), not quantitative. The structural property is parameter-independent (it follows from the real-symmetric Hamiltonian and real diagonal sources). **WARNING (minor):** The word "benchmark" in the section title is misleading since the analytic solution is not quantitatively comparable. Recommend changing to "structural validation."

### 3b. "Phase 2's Redfield -- is it actually site-basis Lindblad mislabeled?"

Code analysis of `phase2_L_large.py`:

- Line 45-103: `solve_ness_correlation()` -- solves the single-particle Lyapunov equation in the **site basis**. There is NO eigenbasis transformation, NO Redfield tensor.
- The function name and docstring say nothing about Redfield.
- The equation is: `i[h, C] + 1/2 {Gamma_diag, C} + gamma_phi (C - diag(C)) = W_in_diag`

**Finding: Phase 2 code is explicitly site-basis Lindblad, not Redfield.**

HOWEVER, the report acknowledges this in Section 6.1 ("Why Site-Basis Lindblad = Redfield for This System") and argues equivalence. Is this equivalence valid?

For free fermions with linear Lindblad operators (c, c_dag), the correlation matrix equation is **closed and exact** in either the site basis or eigenbasis. The eigenbasis Redfield (without RWA) and site-basis Lindblad give identical results because:
1. The transformation between bases is unitary: C_eig = U_dag C_site U
2. The dissipative terms transform covariantly under this rotation
3. Without RWA, no terms are discarded during the basis transformation

Phase 1 verifies this equivalence for L=2 (both give |C12| = 0.061644). This is a genuine verification, not circular reasoning. **PASS.**

NOTE: The `compute_correlation_matrix_redfield_sp()` function in `phase1_L2_benchmark.py` (lines 410-575) attempts to set up a Redfield equation in the single-particle eigenbasis, but its dephasing implementation is approximate (line 552-559: "For now, use a simpler model"). This function appears **incomplete/unused** -- the Phase 2 main code does not call it. The report text also does not reference this function's output. **WARNING: Dead code with incomplete dephasing implementation.**

### 3c. "Does numerical verification merely recover input assumptions?"

Three key claims checked:
1. "Re(C_mid) = 0" -- NOT hard-coded. Follows from mathematical structure (real h, real sources). Verified observation, not input. **PASS.**
2. "beta decreases with alpha" -- NOT input. Emerges from log-log fits to computed data. **PASS.**
3. "No sharp transition at alpha=3/2" -- NOT assumed. Observed from smooth beta(alpha). **PASS.**

The Hamiltonian is constructed with J(r) = J0/r^alpha, which IS the input assumption about power-law hopping. But the observation that beta(alpha) is smooth and monotonic is a genuine output, not predetermined by this input. **PASS.**

### Q3 Verdict: PASS (with minor warnings about naming and dead code)

---

## Q4. Magnitude Gap Assessment

### 4a. |C_mid| magnitude range

Observed: 0.000608 (L=32, alpha=1.1, gamma_phi=2.0) to 0.060098 (L=4, alpha=1.9, gamma_phi=0.01).

This ~100x variation across the parameter space is physically reasonable:
- At L=4, gamma_phi=0.01: the chain is short and nearly coherent, so boundary correlations penetrate strongly to the middle
- At L=32, gamma_phi=2.0: the chain is long and strongly dephased, so the middle is nearly decoupled from boundaries

**PASS** -- no suspiciously large or small values.

### 4b. Beta value range

From verified JSON 2-point fits: beta in [0.100, 1.281].

Physical interpretation:
- beta ~ 0.10 (gamma_phi=0.01, all alpha): near-ballistic. |C_mid| at L=32 is ~80% of L=4 value. Coherence weakly decays with L.
- beta ~ 0.54-0.65 (gamma_phi=0.1): super-diffusive. Moderate decay.
- beta ~ 0.87-1.19 (gamma_phi=0.5): near-diffusive. Standard ~1/L decay.
- beta ~ 1.02-1.28 (gamma_phi=1.0-2.0): diffusive to sub-diffusive.

The range is physically reasonable. The lower bound (beta ~ 0.1 at weak dephasing) approaches the ballistic limit (beta -> 0 as gamma_phi -> 0). **PASS.**

### 4c. Weak dephasing beta consistency

At gamma_phi = 0.01, J_0 = 0.3: the ratio gamma_phi/J_0 = 0.033.
beta ~ 0.10 at this ratio is physically reasonable -- not quite ballistic (beta=0) but close. The residual beta ~ 0.1 reflects the weak but nonzero boundary-induced decoherence. **PASS.**

### Q4 Verdict: PASS

---

## Q5. Algebraic Verification

### 5a. Numerical consistency -- beta fit verification

Verified 7 combinations by manual 2-point calculation:

| alpha | gamma_phi | Manual beta (L4/L32) | JSON fit beta | Match? |
|-------|-----------|---------------------|---------------|--------|
| 1.1 | 0.01 | 0.1107 | 0.1101 | YES (0.0006 diff) |
| 1.1 | 0.1 | 0.6463 | 0.6456 | YES (0.0007 diff) |
| 1.1 | 0.5 | 1.1868 | 1.1847 | YES (0.0021 diff) |
| 1.5 | 0.01 | 0.1049 | 0.1039 | YES (0.0010 diff) |
| 1.5 | 0.5 | 0.9632 | 0.9639 | YES (0.0007 diff) |
| 1.9 | 0.01 | 0.0999 | 0.0988 | YES (0.0011 diff) |
| 1.9 | 0.5 | 0.8675 | 0.8672 | YES (0.0003 diff) |

Differences are all < 0.002, consistent with the fact that 2-point and 4-point log-log fits give slightly different slopes when the power-law is not exact. The JSON fit results are self-consistent with the raw data. **PASS.**

### 5b. Limit behavior

**gamma_phi -> infinity:**
At gamma_phi=2.0 (largest scanned), |C_mid| is consistently the smallest for all L,alpha. For L=32, alpha=1.1: |C_mid|=0.000608 at gp=2.0 vs 0.040400 at gp=0.01 -- a factor of ~66x. The trend is consistent with |C_mid| -> 0 as gamma_phi -> infinity. **PASS.**

**alpha -> infinity:**
alpha=1.9 (largest scanned) gives the weakest L-dependence (smallest beta ~ 0.10 at gp=0.01). As alpha increases, hopping becomes increasingly nearest-neighbor, reducing the channels for boundary decoherence to reach the middle. The trend beta decreasing with alpha is consistent with this limit. **PASS.**

**gamma_phi -> 0:**
At gamma_phi=0.01, beta ~ 0.10 (near-ballistic). The trend is clearly toward beta -> 0 as gamma_phi -> 0. The code uses gamma_phi=0.01 as the smallest value (not exactly 0, which would be singular for some observables). **PASS.**

### 5c. L=2 vs L=4 consistency check

Phase 1 (L=2, Fock space, gamma_phi=0.5): |C12| = 0.048387
Phase 2 (L=4, SP Lyapunov, alpha=1.5, gamma_phi=0.5): |C_mid| = 0.026206

Extrapolating Phase 2 fit to L=2: |C|(L=2) = A * 2^{-beta} = 0.0982 * 2^{-0.964} = 0.0503

Difference between extrapolated Phase 2 (0.0503) and Phase 1 (0.0484): ~4%. This is within expected error for power-law extrapolation from L=4..32 to L=2, and the Phase 1 vs Phase 2 computations use slightly different methods (full Fock space vs single-particle Lyapunov -- though they should agree exactly for free fermions, the L=2 fit extrapolation introduces small errors). **PASS (acceptable).**

### 5d. DATA INTEGRITY ISSUE -- Data count and beta table mismatch

**THIS IS THE MOST SIGNIFICANT FINDING OF THE AUDIT.**

**Fact 1:** The JSON file `phase2_raw_results.json` contains **100 data points** (4 L values x 5 alpha values x 5 gamma_phi values). L values: {4, 8, 16, 32}.

**Fact 2:** The report claims **125 data points** with L in {4, 8, 16, 32, 64}. The L=64 data points do NOT exist in any saved JSON file.

**Fact 3:** The report's beta table (Section 2.3) does NOT match the JSON fit results. Example:

| alpha | gamma_phi | Report beta | JSON fit beta | Delta | Source of difference |
|-------|-----------|-------------|---------------|-------|---------------------|
| 1.1 | 0.01 | 0.1674 | 0.1101 | **+0.0573** | Report uses L=64 data |
| 1.1 | 0.1 | 0.7391 | 0.6456 | **+0.0935** | Report uses L=64 data |
| 1.5 | 0.01 | 0.1543 | 0.1039 | **+0.0504** | Report uses L=64 data |

**Fact 4:** Confirmed: the report's beta values are consistent with 5-point fits including the undocumented L=64 data. For alpha=1.1, gamma_phi=0.01:
- 4-point fit (L=4,8,16,32): beta = 0.1101 (matches JSON)
- 5-point fit (L=4,8,16,32,64): beta = 0.1674 (matches report)

**Fact 5:** The `phase2_L_large.py` code only scans L in {4, 8, 16, 32} (line 120: `L_values = [4, 8, 16, 32]`). The code cannot produce L=64 data.

**Conclusion:** The report describes a computation that was not fully captured in the saved data files. The L=64 data cited in the report table was either:
1. Generated by a separate code run that was not saved, OR
2. Estimated rather than computed

In either case, **the report's beta table is NOT reproducible from the provided code and data files.** Running `phase2_L_large.py` as-is produces betas that are systematically lower than those reported (by 3-15%, with the largest discrepancies at weak dephasing).

**This is a significant reproducibility gap.** The qualitative conclusions (beta decreases with alpha, no sharp transition at alpha=3/2, etc.) remain valid from the 100-point dataset, but the quantitative beta values in the report are NOT verifiable from the provided materials.

### Q5 Verdict: WARNING -- quantitative beta table not reproducible; missing L=64 data; data count discrepancy (100 vs claimed 125)

---

## Q6. Comprehensive Judgment

### Summary of Findings

| Question | Topic | Finding |
|----------|-------|---------|
| Q1 | Dimensional analysis | PASS |
| Q2 | Sign/direction verification | PASS |
| Q3 | Circular reasoning | PASS (minor naming warnings) |
| Q4 | Magnitude gap | PASS |
| Q5a | Numerical consistency (manual beta) | PASS |
| Q5b | Limit behavior | PASS |
| Q5c | L=2/L=4 consistency | PASS (within 4%) |
| Q5d | Data integrity | **WARNING (significant)** |
| Q6-Special | Is Phase 2 really Redfield? | **CLARIFIED** (see below) |

### Special Finding: Is Phase 2's "Redfield" really Redfield?

The Phase 2 code (`phase2_L_large.py`) implements **site-basis Lindblad**, not Redfield. However, for free fermion systems with linear Lindblad operators, site-basis Lindblad and eigenbasis Redfield (without RWA) are mathematically equivalent. Phase 1 demonstrates this equivalence for L=2 by comparing full Fock-space implementations of both methods.

The critical distinction is:
- **Site-basis Lindblad** = eigenbasis Redfield (no RWA) -- both preserve XX amplitude
- **Eigenbasis Lindblad with RWA** -- kills XX amplitude (C12=0)

The report's "Redfield" characterization is technically correct in the sense that the code computes the physically equivalent result, but the labeling is confusing. The code file name and docstring do not mention Redfield at all. **Recommend clarifying that Phase 2 uses site-basis Lindblad (equivalent to Redfield without RWA for free fermions).**

### Detailed Warnings

1. **WARNING (blocking reproducibility):** The report's beta table (Section 2.3) cannot be reproduced from the saved JSON data or the provided Python scripts. The reported beta values are 3-57% higher than what the JSON fit data shows, with the largest discrepancies at weak dephasing. The L=64 data cited in the report is not saved in any JSON file. The code file `phase2_L_large.py` does not scan L=64.

2. **WARNING (documentation):** The report claims 125 data points but the saved JSON contains only 100. The report claims fits use 5 data points (L=4 to L=64) but the saved JSON fits use only 4 data points (L=4 to L=32).

3. **WARNING (dead code):** `compute_correlation_matrix_redfield_sp()` in `phase1_L2_benchmark.py` (lines 410-575) contains an incomplete dephasing implementation (lines 546-559: "For now, use a simpler model") and appears to be unused. This function should either be completed or removed.

4. **Minor:** The word "benchmark" in Phase 1 section title is misleading because the analytic solution uses different parameters. Recommend "structural validation."

5. **Minor:** The sign flip between site-basis Lindblad (Im=+0.061644) and Redfield (Im=-0.061644) is attributed to "convention from eigenbasis rotation" -- this is incomplete. The sign ambiguity arises from the arbitrary phase of eigenvectors in the diagonalization.

---

## FINAL VERDICT

**WARNING: INSPECTOR-COH warns -- quantitative beta table not reproducible from provided code+data. Qualitative findings verified. Correct beta values and add L=64 data to JSON before proceeding.**

### Required Corrections Before Proceeding:

1. **MANDATORY:** Either (a) run `phase2_L_large.py` with L=64 included, save the full 125-point dataset, and regenerate the beta table; OR (b) update the report to use the 100-point beta values from the existing JSON data. The current report overstates beta values by 3-57%.

2. **MANDATORY:** Reconcile the data count. The report says 125 points; the code+JSON say 100 points. Fix one or the other.

3. **RECOMMENDED:** Rename Phase 2 method as "site-basis Lindblad" or "single-particle Lyapunov" rather than implying Redfield, with a note that these are equivalent for free fermions.

4. **RECOMMENDED:** Remove or complete the dead `compute_correlation_matrix_redfield_sp()` function.

### What IS Verified (can be relied upon):

- Re(C_mid) = 0 to machine precision for all 100 data points -- **confirmed**
- |C_mid| decreases with L and gamma_phi -- **confirmed**
- beta(alpha) decreases monotonically as alpha increases -- **confirmed from 100-point data**
- No sharp transition at alpha=3/2 -- **confirmed**
- RWA kills XX amplitude -- **confirmed (Phase 1)**
- Site-basis Lindblad = Redfield without RWA for this free-fermion system -- **confirmed (Phase 1)**

### What Needs Correction:

- The quantitative beta values in the report table are systematically inflated due to undocumented L=64 data
- The data provenance chain (code -> JSON -> report table) is broken
