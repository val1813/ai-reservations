# R1 Block Fixes Summary

**Date:** 2026-06-11
**Trigger:** INSPECTOR_R1 found 3 blocking issues
**Status:** All 3 blocks fixed, both scripts re-run, numbers verified

---

## BLOCK-1 [FATAL]: B博士 G(x) wrong for (1,1) patterns

**Root cause:** `compute_angles.py` line 84-85 assigned |Δ_r| = 4 for all background states when (x_r, x_{r+1}) = (1,1). The correct physics averages over background: 50% of backgrounds give |Δ_r| = 4, 50% give |Δ_r| = 0.

**Fix:** Replaced `delta_abs = 4` with `factor = 0.5 * np.cos(c * 4)**2 + 0.5 * 1.0`

**Impact on B博士's numbers:**

| Quantity | Old (wrong G(x)) | New (correct G(x)) |
|----------|-----------------|-------------------|
| c_0 (n=5) | 0.0702 | **0.0998** |
| KL(Gram\|\|c0-iid) (n=3) | 0.0159 | **0.1033** |
| KL(Gram\|\|c0-iid) (n=5) | 0.0275 | **0.0859** |
| KL per qubit (n=5) | ~0.0055 | **~0.0172** |
| Chernoff ξ (n=3) | 0.0040 | **0.0253** |
| Chernoff ξ (n=5) | 0.0070 | **0.0216** |
| N for 95% conf (n=3) | 242 | **37** |
| N for 95% conf (n=5) | 140 | **45** |
| SVD rank | χ=2 (correct) | χ=2 (unchanged) |

**Conclusion:** B博士's "barely distinguishable" claim was based on wrong G(x). With correct G(x), the Gram signal is ~5x larger in KL terms, requiring ~5x fewer measurements. The "almost indistinguishable" framing is invalidated by the corrected numbers.

---

## BLOCK-2 [SEVERE]: i.i.d. baseline not unified

**Root cause:** A博士 used p_eff-matched i.i.d. (boundary qubit p=0.354), B博士 used c_0-matched i.i.d. (p≈0.37). Two different baselines produce incomparable TVD/KL values.

**Fix:** Both analyses now use **position-dependent i.i.d. baseline** as the primary comparison. A博士's `cz_correlation.py` now computes both uniform-boundary and position-dependent baselines side-by-side.

**Position-dependent i.i.d. definition:**
- c_z^(pos-iid) = ∏_{q: z_q=1} p_q · ∏_{q: z_q=0} (1 - p_q)
- where p_q = ∑_{z: z_q=1} c_z^(gram)
- This matches every single-qubit marginal exactly, without assuming translation invariance.

---

## BLOCK-3 [SEVERE]: p_eff varies per qubit

**Root cause:** A博士 claimed p_eff = 0.354037 is "constant, independent of n" without noting this only applies to boundary qubits (q=0, n-1). Interior qubits have p_interior = 0.457389 (29% higher).

**Fix:** Added `compute_position_dependent_perr()` to compute per-qubit p_q values. Added `position_dependent_iid_distribution()` for position-dependent baseline. All displays now show both p_boundary and p_interior.

**Per-qubit Z-error probabilities (c=0.5, all n≥3):**
- Boundary qubits (q=0, n-1): p = 0.354037 (constant)
- Interior qubits (q=1..n-2): p = 0.457389 (constant)

---

## Corrected Key Results (position-dependent baseline, c=0.5)

### f(1,1) confirmation
- f(1,1) = 0.5866 (correct background average)
- Previously claimed as 0.1732 by B博士 (wrong)

### Weight ratio ρ(w) — corrected

| n | ρ_pos(1) | ρ_pos(6) |
|---|---------|---------|
| 6 | 0.93 (was 0.63) | 1.54 (was 4.28) |

ρ(6) drops from 4.28 to 1.54: Gram high-weight enhancement is much weaker than A博士 originally claimed.

### TVD (position-dependent baseline)

| n | TVD_pos (full) | TVD_pos (weight) |
|---|---------------|-----------------|
| 3 | 0.168 | 0.168 |
| 4 | 0.127 | 0.101 |
| 5 | 0.112 | 0.062 |
| 6 | 0.105 | 0.046 |
| 7 | 0.108 | 0.032 |
| 8 | 0.111 | 0.030 |

Position-dependent TVD is roughly half the uniform-baseline TVD. It does NOT grow monotonically with n.

### KL divergence

| n | KL(Gram \|\| pos-iid) | KL per qubit |
|---|----------------------|-------------|
| 3 | 0.0632 | 0.0211 |
| 4 | 0.0411 | 0.0103 |
| 5 | 0.0362 | 0.0072 |
| 6 | 0.0359 | 0.0060 |
| 7 | 0.0367 | 0.0052 |
| 8 | 0.0379 | 0.0047 |

KL per qubit decreases with n (dilution by interior qubits matching the baseline well).

### Logical error rate enhancement (d=3,5,7 codes, n=7)

| d | p_gram | p_pos_iid | Ratio (ρ_pos) |
|---|--------|----------|--------------|
| 3 | 0.8611 | 0.8761 | **0.983** (Gram is ~2% LOWER) |
| 5 | 0.6282 | 0.6401 | **0.982** (Gram is ~2% LOWER) |
| 7 | 0.3617 | 0.3448 | **1.049** (Gram is ~5% HIGHER) |

**With position-dependent baseline, d=7 Gram logical error is only 5% higher, not 75%.** The 75% figure from A博士's original report was an artifact of using the uniform boundary-qubit p_eff for all qubits.

### Transfer matrix verification
- TVD(transfer_matrix c_z, direct WH c_z) = 9.8 × 10^{-17} -- machine precision
- f_matrix factorization matches exact G_fold(x) with max error 5.6 × 10^{-17}

---

## Qualitative Conclusion (revised)

**The Gram correlated dephasing channel IS distinguishable from i.i.d., but the effect is much weaker than originally claimed when using the correct position-dependent baseline.**

The original A博士 conclusion ("Gram makes QEC strictly harder, 75% higher logical error at d=7") was inflated by using a uniform baseline that underestimated interior qubit error rates. The corrected enhancement is ~5% at d=7.

The original B博士 conclusion ("almost indistinguishable, nearly i.i.d.") was based on an incorrect G(x) computation that systematically underestimated Gram specific structure. With corrected G(x), the KL is ~5x larger.

**Truth in the middle: Gram correlations are measurably different from i.i.d. but the effect on QEC logical error rates is modest (~5% at d=7).**

---

## Files Modified

1. `current/A/cz_correlation.py` — Added `compute_position_dependent_perr()`, `position_dependent_iid_distribution()`, updated all display functions to dual baseline
2. `current/B/compute_angles.py` — Fixed G(x) computation for (1,1) patterns (line 84-89)
3. `current/B/crossdiscipline_reframed.md` — Updated quantitative conclusions

## Files Created

1. `synthesis/R1_block_fixes.md` — This file
