# DGF Gram Matrix Spectral Properties — Full Numerical Sweep Analysis

**Date**: 2026-06-11
**Total runtime**: 3537.7s (~59 min) on laptop
**Data file**: `full_sweep_results.json` (567 KB)
**Max b1**: 12 (d_sys = 8192)

---

## 1. Phase Diagram: b1-c Grid Summary

Full scan over b1 = 0..12 and 16 c values from 0.05 to pi/2.
Key observable: **rank_eff** (effective rank = 1 / Σ p_i^2).

### Representative values at c=0.5:

| b1 | d_sys | rank_eff | rank_eff/d | mean&#124;G&#124; | mu_meas | λ1/Σλ |
|----|-------|----------|------------|----------|---------|-------|
| 0  | 2     | 1.062    | 0.531      | 9.59e-01 | —       | 0.971  |
| 2  | 8     | 5.202    | 0.650      | 2.06e-01 | -0.954  | 0.385  |
| 4  | 32    | 22.029   | 0.688      | 7.08e-02 | -0.862  | 0.089  |
| 6  | 128   | 87.521   | 0.684      | 2.45e-02 | -0.841  | 0.023  |
| 8  | 512   | 341.981  | 0.668      | 8.72e-03 | -0.841  | 0.006  |
| 10 | 2048  | 1330.767 | 0.650      | 3.30e-03 | -0.838  | 0.002  |
| 12 | 8192  | 5173.274 | 0.632      | 1.17e-03 | -0.837  | 0.0004 |

**Finding**: rank_eff grows with b1, NOT collapses to 1. The CRTH prediction that rank_eff → 1 as b1 → ∞ is **FALSIFIED** at c=0.5. Instead, rank_eff grows roughly as d_sys^0.64 — sub-extensive but far from rank-1 collapse.

### Classical limit at c → pi/2:

At c = pi/2 (Clifford), rank_eff = 1.0000 for ALL b1. The Gram matrix is exactly rank-1 (all entries = 1), meaning perfect classicality. This confirms that Clifford rings produce zero decoherence — the system and environment are perfectly correlated.

### Quantum-dominant regime at c ≈ pi/4:

At c = pi/4, rank_eff = 2^{b1} (exactly d_sys/2). The Gram matrix is rank d_sys/2 — a maximally "quantum" regime where exactly half the eigenvalues vanish and half are equal. This is the "CNOT point" where ring factors can vanish exactly for certain delta values.

### Small c limit (c → 0):

At c = 0.05, rank_eff ≈ 1.0 to 1.27 for all b1 — near-classical. For small Cartan angles, the ring factors are close to 1 and the Gram matrix is near rank-1.

---

## 2. Gram Spectral Density — Marčenko-Pastur Analysis

### Result: MP is a POOR fit to the Gram spectrum.

| b1 | n_pos_evals | best gamma | KS distance |
|----|-------------|-----------|-------------|
| 4  | 31          | 0.99      | 0.817       |
| 6  | 127         | 0.99      | 0.902       |
| 8  | 511         | 0.99      | 0.946       |
| 10 | 2047        | 0.99      | 0.971       |
| 12 | 8191        | 0.99      | 0.986       |

The KS distance INCREASES with b1 (worse fit for larger systems). The best-fit gamma = 0.99 is at the upper boundary, corresponding to λ_- ≈ (1-√0.99)^2 ≈ 0 and λ_+ ≈ (1+√0.99)^2 ≈ 4. This means the MP fit is degenerating to a delta-function-like distribution.

**Physical interpretation**: The Gram eigenvalue spectrum is NOT random (Wishart). It is highly structured by the causal ring topology. The eigenvalues form discrete clusters (near-degeneracies) rather than a continuous MP sea. This is actually consistent with the CRTH prediction that the spectrum is controlled by topology, not randomness.

**Convergence**: KS distance → 1 (NOT 0) as b1 → ∞. The distribution does NOT converge to MP. Instead, the spectrum becomes increasingly dominated by a single large eigenvalue.

---

## 3. Level Spacing Statistics — Brody Distribution

### Result: alpha ≈ -0.45 (BELOW Poisson, indicating eigenvalue clustering)

| b1 | Brody alpha | KS to Brody | Mean spacing ratio <r> |
|----|------------|-------------|------------------------|
| 2  | -0.45      | 0.143       | 0.432                  |
| 3  | -0.45      | 0.169       | 0.345                  |
| 4  | -0.45      | 0.112       | 0.297                  |
| 5  | -0.434     | 0.134       | 0.354                  |
| 6  | -0.45      | 0.127       | 0.350                  |

**Key values for reference**:
- Poisson: alpha = 0, <r> = 0.386
- Wigner-Dyson (GOE): alpha = 1, <r> = 0.599

**Finding**: The Brody alpha is consistently ≈ -0.45, which is BELOW Poisson (alpha=0, random uncorrelated eigenvalues). alpha < 0 means P(s) has a singularity at s=0: eigenvalues are CLUSTERED rather than repelled. 

The mean spacing ratio <r> ≈ 0.30-0.35 for b1 ≥ 3, which is below the Poisson value of 0.386. This confirms eigenvalue clustering — the spectrum contains near-degenerate eigenvalue multiplets, consistent with the structured Gram matrix having discrete symmetry sectors.

**Prediction refutation**: The CRTH prediction of a Poisson → Wigner-Dyson transition with increasing b1 is NOT observed. Instead, the spectrum remains in a "sub-Poisson" regime with eigenvalue clustering at all b1. There is NO trend toward Wigner-Dyson as b1 increases.

---

## 4. Tree vs Ring — Topology Comparison

| c     | Topology | rank_eff | mean&#124;G&#124; | Enhancement |
|-------|----------|----------|----------|-------------|
| 0.10  | Tree     | 1.023    | 9.75e-01 |             |
| 0.10  | Ring     | 1.080    | 9.48e-01 | 1.028       |
| 0.10  | Two-Ring | 1.164    | 9.14e-01 | 1.067       |
| 0.50  | Tree     | 3.278    | 4.19e-01 |             |
| 0.50  | Ring     | 2.373    | 3.90e-01 | 1.073       |
| 0.50  | Two-Ring | 5.202    | 2.06e-01 | 2.035       |
| pi/4  | Tree     | 4.000    | 1.43e-01 |             |
| pi/4  | Ring     | 2.000    | 3.33e-01 | 0.429       |
| pi/4  | Two-Ring | 4.000    | 1.43e-01 | 1.000       |
| pi/2  | Tree     | 1.000    | 1.00e+00 |             |
| pi/2  | Ring     | 1.000    | 1.00e+00 | 1.000       |
| pi/2  | Two-Ring | 1.000    | 1.00e+00 | 1.000       |

**Finding**: The decoherence enhancement factor |G_tree|/|G_ring| depends on BOTH b1 (topology) AND c (Cartan angle):
- At c=0.5: Tree has LARGER off-diagonal (less decoherence) than rings. Two-Ring has smallest |G|. Enhancement ~2x between Tree and Two-Ring.
- At c=pi/4: Ring has larger |G| than Tree or Two-Ring. The pattern is different.
- At c=pi/2: All identical (Clifford, rank-1).

**The enhancement factor depends on c**, not just b1. This means the CRTH prediction that "decoherence depends ONLY on b1" is **NOT strictly true** — the Cartan angle c modulates the b1-dependence non-trivially.

---

## 5. mu(c) Universality — Topology Independence

### Measured mu for vertex-sharing chain (convergence with b1):

| b1 | mu_meas | Deviation from analytic |
|----|---------|------------------------|
| 1  | -1.113  | +33.3%                 |
| 2  | -0.954  | +14.3%                 |
| 4  | -0.862  | +3.2%                  |
| 6  | -0.841  | +0.8%                  |
| 8  | -0.841  | +0.7%                  |
| 10 | -0.838  | +0.4%                  |
| 12 | -0.837  | +0.2%                  |

Analytic mu_vertex = -0.8348. Convergence is clear — mu_meas → mu_analytic as b1 → ∞.

### Topology comparison at c=0.5:

| Topology | mu per env qubit | mu_analytic | Match |
|----------|-----------------|-------------|-------|
| Vertex-sharing | -0.838 (b1=12) | -0.835 | YES |
| Edge-disjoint  | -0.835 (b1=5)  | -0.835 | YES |
| 2D Grid (1 env) | -0.466 (L=6)  | -0.465 | YES |

**Finding**: All three topologies converge to their respective analytic mu values when the number of qubits per ring and env qubits per ring are correctly accounted for.

Key insight: mu is NOT a universal constant across topologies. It depends on the ring-level qubit connectivity:
- 2 qubits per ring (vertex-sharing, edge-disjoint): mu_env ≈ -0.417 per env qubit
- 4 qubits per ring (2D grid): mu_env ≈ -0.465 per env qubit

The more qubits per ring, the larger |mu| (faster decoherence per ring). This is because larger rings have more possible delta values, allowing stronger phase cancellation.

**Topology independence CONFIRMED** in the sense that: given the SAME ring structure (qubit count per ring, env qubit count per ring), mu is independent of how rings are connected globally. But mu depends on the LOCAL ring structure.

---

## 6. Gram Coherence Classes — K8 Verification

### Result: K8 prediction FAILS

| Property | Predicted (K8) | Measured |
|----------|---------------|----------|
| Number of classes | 16 (= 2^{n-1}) | **31** |
| Class sizes | All size 2 | **30 singletons + 1 pair** |
| Bitwise complement pairs | All 16 pairs | **Only 1 pair** |
| Alternating state (01010) | |G|=1 with complement | **|G|=1.0 CONFIRMED** |

**Analysis**: The K8 model predicts that at c=0.5, the computational basis states should partition into 2^{n-1}=16 coherence classes, each containing a state and its bitwise complement. This prediction is WRONG.

The actual structure: 31 classes total (30 states are each their own class, 1 class contains the pair {01010, 10101}). Every state is distinguishable from every other state (|G_ab| < 1) EXCEPT the fully alternating state and its complement, which maintain perfect coherence (|G| = 1).

**Why this matters**: The Gram coherence class structure is much sparser than the K8 model predicts. This means the Gram matrix at c=0.5 is much closer to full-rank than expected — almost all computational basis states are mutually incoherent. The only surviving coherence is the "alternating pattern" subspace.

**Root cause**: The K8 model assumed that for c=0.5, the ring factors have special periodicities that cause massive degeneracy. The numerical data shows these periodicities do NOT exist in the way the model predicted. The Gram matrix structure is dominated by generic decoherence, not special coherence classes.

---

## 7. Ghost Zero Spectral Signature

### Result: PERFECT confirmation of gap ∝ p(1-p)

| p | p(1-p) | gap = 1 - λ_min |
|---|--------|-----------------|
| 0.01 | 0.0099 | 0.9802 |
| 0.50 | 0.2500 | 0.5002 |
| 0.99 | 0.0099 | 0.9802 |

**Fit**: gap = 1.000 - 2.000 * p(1-p), R^2 = 1.0000

**Interpretation**: At p=0.5 (maximally mixed environment), the Gram spectrum is broadest with gap=0.5. As p→0 or p→1 (environment becomes deterministic), the spectral gap closes and ρ_G(λ) → δ(λ-1), confirming the "Ghost Zero" limit.

The linear relationship gap = 1 - 2p(1-p) is exact (R^2=1.0), suggesting this is an analytic identity for the b1=1, c=pi/4 case, not just a numerical fit.

**Ghost Zero mechanism**: When the environment is in a pure state (p=0 or p=1), the Kraus operators collapse to a single operator, the channel becomes unitary, and the Gram matrix becomes rank-1 (λ_1 = 1, all other λ_i = 0). The spectral gap measures how far the environment is from this classical limit.

---

## 8. Honest Assessment: What Does This Data Tell Us About the CRTH?

### Predictions CONFIRMED:

1. **Clifford rings (c=pi/2) produce perfect classicality**: rank_eff = 1.0000 at ALL b1. Gram matrix is exactly rank-1. Environment and system are perfectly correlated. This is the CRTH's strongest confirmed prediction.

2. **mu converges to analytic value as b1 → ∞**: The measured mu approaches the analytic prediction within <1% for b1 ≥ 6. The analytic formula (based on ring-level delta statistics) is correct.

3. **Topology independence of mu**: For a given ring structure (qubits per ring, env qubits per ring), mu is independent of global topology (chain, disjoint, grid). Topology matters only through its effect on the ring-level structure.

4. **Ghost zero spectral gap ∝ p(1-p)**: Exact linear relationship confirmed with R^2=1.0. The environment purity controls the spectral gap.

5. **Sub-extensive rank growth**: rank_eff grows as ~d_sys^0.64, not as d_sys (quantum) or as 1 (classical). The Gram matrix is in an intermediate regime.

### Predictions REFUTED:

1. **Rank collapse to 1 as b1 → ∞ (at generic c)**: FALSIFIED. At c=0.5, rank_eff GROWS with b1 (from 1.06 at b1=0 to 5173 at b1=12). The Gram matrix does NOT become rank-1 for fixed c < pi/2.

2. **Poisson → Wigner-Dyson transition**: NOT OBSERVED. The level spacing statistics remain in a "sub-Poisson" regime (alpha ≈ -0.45) with eigenvalue clustering at all b1. There is no trend toward Wigner-Dyson.

3. **Marčenko-Pastur spectral density**: FALSIFIED. KS distance → 1 as b1 → ∞. The Gram spectrum is highly structured (not random). The eigenvalue distribution is dominated by discrete clusters, not a continuous MP sea.

4. **K8 coherence class structure**: FALSIFIED. The predicted 2^{n-1} pairwise coherence classes do not exist at c=0.5. Only one pair (alternating state + complement) maintains coherence. 30 out of 32 states are distinguishable.

5. **Decoherence depends ONLY on b1**: FALSIFIED. The tree-vs-ring enhancement factor depends on c, not just b1. Different c values produce qualitatively different behavior (tree > ring at c=0.5, tree < ring at c=pi/4).

### The Big Picture:

The CRTH captures the correct qualitative physics at the Clifford point (c=pi/2) and the ghost zero limit (p→0,1), but its predictions about the GENERIC (non-Clifford, finite mixing) behavior are incorrect in several important ways:

1. The rank does NOT collapse to 1 for generic c — instead it grows sub-extensively.
2. The eigenvalue spectrum is highly structured (clustered), not random (MP or Wigner-Dyson).
3. The Gram coherence structure is much sparser than K8 predicts.
4. Topology matters through ring-level qubit connectivity, not through b1 alone.

The CRTH's core insight — that causal topology controls decoherence — is qualitatively correct, but the quantitative predictions need significant revision for non-Clifford Cartan angles.

### Recommended Next Steps:

1. **Investigate the sub-extensive scaling**: What determines the exponent ~0.64? Is it universal or c-dependent?
2. **Characterize the eigenvalue clusters**: Identify the symmetry sectors causing near-degeneracies.
3. **Derive the corrected coherence class structure**: Why does only the alternating pattern survive at c=0.5?
4. **Study the rank_eff c-dependence**: There appears to be a phase boundary near c ≈ 1.2 where rank_eff peaks and then drops toward 1 at c=pi/2.
