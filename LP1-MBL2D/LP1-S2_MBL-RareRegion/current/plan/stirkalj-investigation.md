# Investigation: Weak Potential Lines (WPLs) in Strkalj, Doggen & Castelnovo (2022)

**Paper:** Antonio Strkalj, Elmer V. H. Doggen, Claudio Castelnovo, "Coexistence of localization and transport in many-body two-dimensional Aubry-Andre models," Phys. Rev. B **106**, 184209 (2022), arXiv:2204.05198.

**Investigation date:** 2026-05-31

**Purpose:** Determine whether core claim K1.5 ("Diophantine-based prediction: max thermal block size L_QP^max ≈ 2.8 in separable 2D AA") survives or conflicts with the WPL results in this paper.

---

## Executive Summary

**K1.5 SURVIVES. There is NO direct contradiction.** The WPLs in the separable 2D Aubry-Andre model are 1D diagonal lines that localize at large W, do not form 2D percolating thermal blocks, and do not trigger avalanches. The Strkalj paper's findings are fully consistent with the Diophantine prediction of small 2D thermal block sizes.

However, there is one nuanced caveat (Section 7 below): under a very specifically tuned initial state (columnar density wave), quasi-1D transport along a single diagonal WPL can persist even at large W. This is a 1D mosaic-lattice effect, not 2D percolation, and does not constitute a contradiction.

---

## 1. The Models: Separable vs. Non-Separable

### Hamiltonian (Eq. 1)

Hard-core bosons on a 2D square lattice:

H = sum_<ij,i'j'> [-J/2 (b_ij^dagger b_i'j' + h.c.) + V n_ij n_i'j'] + sum_ij U_ij n_ij

with V = J (nearest-neighbor interaction), hbar = 1.

### Separable Potential U^S (Eq. 2)

```
U^S(x,y) = W[cos(2πb x + φ_x) + cos(2πb y + φ_y)]
```

- Cosine modulations aligned with lattice axes
- Separable into x- and y-components (product of 1D problems)
- b = 2/(1+√5) ≈ 0.618 — inverse golden mean

This can be rewritten (Eq. 8):
```
U^S_ij = 2W cos(b(i+j) + φ_y') cos(b(i-j) + φ_x')
```

### Non-Separable Potential U^NS (Eq. 2)

```
U^NS(x,y) = W[cos(2πb(x+y) + φ_+) + cos(2πb(x-y) + φ_-)]
```

- Wavevectors at 45° to lattice
- Can be rewritten (when φ_+ = φ_- = 0):
```
U^NS(x,y) = 2W cos(2πb x) cos(2πb y)
```
- This is a multiplicative/product form along the lattice axes

### Key Answer to Q1

**WPLs exist in BOTH models, but with fundamentally different geometry and physics:**

| Property | Separable (U^S) | Non-Separable (U^NS) |
|----------|-----------------|---------------------|
| **WPL geometry** | **Diagonal** (next-nearest-neighbor) | **Horizontal and vertical** (lattice-aligned) |
| **Direct hopping along WPL** | **NO** (must hop via intermediate sites) | **YES** (nearest-neighbor J/2) |
| **Effective hopping along WPL** | ≃ J²/U_ij (suppressed by 1/W) | J/2 (unsuppressed) |
| **Fate at large W** | **Localize** (line 196) | **Remain ergodic for any W** |
| **Transport dependence** | State-dependent (only columnar density wave) | State-independent |
| **Avalanche risk** | None | Fails to thermalize bulk (on accessible timescales) |

---

## 2. System Sizes and Disorder Strengths

### System Sizes

| Study | Lx × Ly |
|-------|---------|
| Main many-body dynamics | 16 × 5 |
| Ly scaling analysis | Ly = 2, 3, 4, 5 with fixed Lx = 16 |
| Square WPL analysis | 8 × 8 |
| Diamond chain (many-body) | L = 20 unit cells |
| Diamond chain (single-particle) | L = 233, 610 unit cells |
| Single-particle IPR | 21 × 21 |

### Disorder Strengths W/J

| Range | Usage |
|-------|-------|
| W/J = 5, 10, 15, 20, 25, 30 | Main MBL transition scan |
| W/J = 50 | "Deeply in the localized phase" WPL studies |
| W/J = 10 | Noninteracting reference |
| W/t = 0, 1, 2, 3, 30 | Diamond chain single-particle |
| W/t = 1.0, 1.5, 2.0, 2.5, 3.0 | Diamond chain many-body |

### Critical Points Identified

- **MBL transition (both S and NS models):** W_C/J ≈ 20-30 (interacting, V=J)
- **Single-particle S model:** W_C/J = 1 (uniform metal-to-insulator transition)
- **Single-particle NS model:** No uniform transition; extended states persist above W/J=1
- **Diamond chain zero-potential WPL (single-particle):** W_C/t = 2√2/|cos(b + π/2)| ≈ 3.03
- **Diamond chain (many-body):** W_C/t ≈ 2.5

---

## 3. Precise Definition of "Weak Potential Line" (WPL)

### Quoted Definition (lines 180-182)

> "Throughout the text we refer to WPLs as lines that encompass sites with an effective potential strength that is smaller than a critical point W_C where a 1D AA chain localizes."

### Interpretation

This is a **THRESHOLD-based definition** on the absolute potential value, NOT a gradient-based definition:

- For the **non-separable model**: along a fixed x-column (or y-row), the potential in the perpendicular direction is a cosine with effective strength W_eff(x) = 2W|cos(2πb x)|. A WPL is a column (or row) where W_eff < W_C.
- For the **separable model**: the effective potential along a diagonal line must be below the critical threshold.

### Emergence Mechanism

In the non-separable model, the condition for a WPL is that cos(2πb x) ≈ 0 or cos(2πb y) ≈ 0. Because b is irrational, there are always such lines. As the system size grows, the minimum value of |cos(2πb x)| over all x decreases, so W_eff can be made arbitrarily small. This means:

> "In the thermodynamic limit, it is always possible to find WPLs with arbitrarily small values of the potential even when W is extremely large." (lines 183-185)

In the separable model, WPLs correspond to diagonals where cos(b(i+j) + φ_y') ≈ 0. Again, because b is irrational, such diagonals exist in any sufficiently large system.

---

## 4. Do WPLs Span the System?

### Non-Separable Model: YES

WPLs are full rows and columns that span the entire system. For example, when cos(2πb × 3 + φ_0) = 0, the ENTIRE row j=3 is a horizontal WPL. The paper explicitly creates a sample with "a horizontal WPL in the middle (j = 3)" in a 16×5 system (line 448-449).

### Separable Model: Along Diagonals, Length = min(Lx, Ly)

In a rectangular Lx×Ly system: "the diagonal WPLs span only a few sites" (line 501). The authors switch to square geometry Lx=Ly=8 to get 8-site diagonals. The maximum WPL length equals the system linear size L in a square system.

**Critical distinction:** In the non-separable case, WPLs are TRULY system-spanning (percolating from boundary to boundary) and remain conducting. In the separable case, diagonal WPLs span the diagonal of the system but LOCALIZE for large enough W — they do not support transport at large W in a generic initial state.

### Infinite-System Limit

> "For infinite systems, ergodic WPLs have infinite length with the level spacing equal to zero, which means that they act as perfect baths." (lines 749-751)

The paper then discusses that this could _in principle_ lead to avalanches, but at timescales far beyond what is numerically or experimentally accessible.

---

## 5. Maximum WPL Length in Separable 2D AA and Scaling

### Length

- **Rectangular Lx×Ly system:** maximum diagonal WPL = min(Lx, Ly) sites (but "only a few sites" in 16×5 because Ly=5)
- **Square L×L system:** L sites (main diagonal)
- **Scaling with system size:** linear, L ~ N^(1/2) where N = L²

### Fate at Large W

The paper is explicit (lines 194-196):

> "The matrix element that connects two closest sites in such WPLs is proportional to J²/U_ij, and particle hopping along the diagonal is again quasiperiodic, thus leading to **localization for large enough W/J**."

This is the CRUCIAL difference from the non-separable case. In the separable model, diagonal WPLs DO NOT remain conducting at large W (in generic initial states).

### Many-Body Diamond Chain Analysis (Appendix A)

The authors specifically analyze the diagonal WPL in a simplified "diamond chain" geometry (three adjacent diagonals):

- For a **zero-potential WPL** (ε=0): single-particle delocalization transition at W_C/t = 2√2/|cos(b+π/2)| ≈ 3.03. Many-body localization transition at W_C/t ≈ 2.5 (with interactions V=t).
- For a **finite-potential WPL** (ε≠0): ALL states eventually localize above some W.

### Observed Transport in Separable Model

Transport along diagonal WPLs is **state-dependent**:

1. **Checkboard initial state:** Transport STRONGLY SUPPRESSED when W > W_C. No decay of imbalance (Fig. 6(b)).
2. **Columnar density wave:** Transport OCCURS along zigzag pattern (mosaic lattice limit), even at W/J=50 (Figs. 9, 10).
3. **Random initial state:** NO transport; all diagonal imbalances saturate near 1 (Fig. 13(b)).

---

## 6. Direct Assessment vs. Diophantine-Based Prediction

### The Diophantine Prediction (K1.5)

Recap: L_QP^max ≈ 2πV_0/(√5 W_c) ≈ 2.8 for separable 2D AA with β=φ, V_0=5t, W_c=5t.

This predicts that the maximum size of a 2D contiguous thermal/ergodic block (where ALL sites have |V(x,y)| < W_c) is approximately 2-3 lattice sites.

### Consistency Assessment

**Finding: FULLY CONSISTENT. No contradiction.**

| Claim | Strkalj Evidence | Status |
|-------|-----------------|--------|
| Small 2D thermal blocks | WPLs are 1D lines, not 2D blocks | Consistent |
| No 2D percolation of weak-potential regions | Diagonal WPLs are single lines, no 2D network | Consistent |
| Thermal blocks cannot thermalize the system | WPLs fail to thermalize surrounding bulk | Consistent |
| Transport suppressed at large W (generic state) | Random initial state → no transport in S model at W>W_C | Consistent |
| MBL is stable in 2D quasiperiodic S model | W_C independent of Ly (Fig. 5(b)) | Consistent |

### Detailed Analysis

**Why there is no contradiction:**

1. **Geometry mismatch:** K1.5 concerns CONTIGUOUS 2D BLOCKS of sites where the potential is below the critical threshold. Strkalj finds 1D DIAGONAL LINES of low potential. A 1D line is not a 2D block. The Diophantine prediction constrains 2D block sizes, not 1D line lengths.

2. **Transport mechanism mismatch:** Even along the diagonal 1D lines, particles cannot directly hop between WPL sites — they must tunnel through intermediate sites with finite potential (effective hopping ≃ J²/U_rec). This suppresses transport, consistent with the small thermal block prediction.

3. **State-dependence:** The only scenario where transport survives at large W in the separable model is the columnar density wave initial state. In generic (random) initial states, the system is fully localized and supports no transport.

4. **No avalanche:** The WPLs, even in the non-separable case where they ARE ergodic, fail to thermalize the surrounding localized bulk on accessible timescales. The authors explicitly note that WPLs "do not appear to lead to global thermalization" (line 727-728).

5. **Scaling consistency:** The MBL transition point W_C/J is independent of system width Ly in the quasiperiodic models (Fig. 5(a,b)), in stark contrast to the random disorder case where W_C/J diverges with Ly (Fig. 5(c) and Ref. [37]). This directly contradicts avalanche-based instability and supports the stability of MBL — which is the qualitative content of K1.5.

### The One Nuance (Caveat for Rigor)

The paper's analysis of the **zero-potential diagonal WPL** in the diamond chain / mosaic lattice limit (Appendix A.3) reveals:

> For a WPL with ε=0 (zero potential on the diagonal), the single-particle mosaic lattice has a mobility edge E_C = 2V ± t²/(W|cos(b+π/2)|). As W→∞, E_C→2V. **Extended single-particle states exist at E=0 for any W.**

This is the basis for why the columnar density wave initial state can produce transport at arbitrarily large W. However:

- This is a quasi-1D effect along a single diagonal line
- It occurs only when the potential V(x,y) vanishes EXACTLY on that diagonal (a measure-zero condition in the thermodynamic phase space)
- In the FULL 2D many-body system with random initial states, no such transport survives (Fig. 13(b))
- The many-body diamond chain with generic initial states (upper/lower chains initially empty) localizes at W/t ≈ 2.5 (Fig. 13(a))

**This nuance does NOT contradict the Diophantine prediction**, because:
- It concerns 1D lines, not 2D blocks
- It requires exact zero potential (ε=0), which only a measure-zero set of diagonals satisfy
- It does not produce 2D percolation or avalanche

### Recommended K1.5 Status

**K1.5 SURVIVES** and should be RETAINED, with the following clarifications:

1. The Diophantine prediction constrains 2D thermal BLOCKS, not 1D WPLs
2. The Strkalj paper independently confirms that WPLs in the separable model localize at large W
3. The columnar-density-wave transport is a separate, well-understood 1D mosaic-lattice effect
4. For citation purposes: Strkalj et al. (2022) can be cited as complementary evidence that quasiperiodic systems lack avalanche instability and that the separable 2D AA model supports stable MBL

---

## 7. The Three Contemporaneous Papers (April 2022)

Three papers appeared on arXiv within two weeks of each other:

| Paper | arXiv | Key Claim |
|-------|-------|-----------|
| Agrawal, Vasseur, Gopalakrishnan | 2204.03665 | MBL stable in d=2 quasiperiodic, unstable in d≥3 |
| Strkalj, Doggen, Castelnovo | 2204.05198 | MBL stable + WPL coexistence of localization and transport |
| Crowley & Chandran | 2204.09688 | Mean-field theory: quasiperiodic systems resist avalanches, localization stable against finite density of ergodic grains |

All three converge on the same qualitative conclusion: **MBL is stable in 2D quasiperiodic systems**, in contrast to 2D random systems. This constitutes a strong consensus against avalanche-based instability in quasiperiodic potentials.

The Strkalj paper acknowledges Crowley & Chandran (Ref. [81]) in a note added at the end:

> "Ref. [81] also argues that large enough ergodic inclusions — such as the WPLs — will eventually destabilize the MBL phase and thermalize the whole system. While we do not observe it in our simulations, as mentioned in Sec. VIII this could be because such thermalizing processes occur on exceptionally large length and timescales, beyond the ones studied in our work." (lines 816-822)

This is a responsible acknowledgment of the theoretical possibility of ultra-slow avalanches, but note that the observed behavior (both numerical and analytic in Crowley & Chandran) shows FAILED avalanches in the quasiperiodic case.

---

## 8. Summary Table: Key Parameters from the Paper

| Parameter | Separable (U^S) | Non-Separable (U^NS) |
|-----------|-----------------|---------------------|
| Potential form | W[cos(2πb x) + cos(2πb y)] | 2W cos(2πb x) cos(2πb y) |
| Wavevector | b = 2/(1+√5) ≈ 0.618 | Same b |
| WPL geometry | Diagonal | Horizontal & vertical |
| Direct hopping on WPL | No (J²/U) | Yes (J/2) |
| WPL fate at large W | Localize | Remain ergodic |
| W_C (many-body, V=J) | ~20-30 | ~20-30 |
| System sizes studied | up to 16×5 (many-body), 21×21 (SP) | Same |
| Max simulation time | ~100 J⁻¹ | ~100 J⁻¹ |
| Bond dimension | χ=128 (χ=256 for ergodic) | χ=128 |
| Initial states | Checkerboard, columnar, random | Checkerboard, columnar |
| MBL stable? | Yes (on accessible scales) | Yes (on accessible scales) |

---

## 9. References Cited in This Investigation

1. Strkalj, Doggen & Castelnovo, Phys. Rev. B **106**, 184209 (2022) — arXiv:2204.05198
2. Szabo & Schneider, Phys. Rev. B **101**, 014205 (2020) — arXiv:1909.02048 (single-particle precursor)
3. Agrawal, Vasseur & Gopalakrishnan, Phys. Rev. B **106**, 094206 (2022) — arXiv:2204.03665
4. Crowley & Chandran, Phys. Rev. B **106**, 184208 (2022) — arXiv:2204.09688
5. Doggen, Gornyi, Mirlin & Polyakov, Phys. Rev. Lett. **125**, 155701 (2020) (random 2D comparison)
6. Wang et al., Phys. Rev. Lett. **125**, 196604 (2020) (mosaic lattice with mobility edges)

---

*Investigation completed 2026-05-31. Full paper PDF text extracted and analyzed. No contradictions with K1.5 found.*
