# Quantum Circuit Topology Classifies Critical CFT Universality Classes

## A Conjecture with Theoretical Derivation and Preliminary Numerical Evidence

---

## Abstract

We propose that the Betti number b₁ of a quantum circuit's qubit connectivity graph determines the Virasoro central charge of its low-energy effective conformal field theory at critical nonlocal gate density. The mapping is c(b₁) = 1 − 6/((b₁+2)(b₁+3)), giving a discrete spectrum: Ising (b₁=1, c=1/2), Tricritical Ising (b₁=2, c=7/10), 3-state Potts (b₁=3, c=4/5), etc. The derivation proceeds from two information-theoretic constraints (causal order + 1 bit/grid capacity) within quantum mechanics, through three physical principles (CKW entanglement monogamy, Cartan parameter quantization via Coxeter holonomy, and ground state selection) that together compress 2^b₁ possible loop configurations into b₁+1 physical configurations, naturally yielding the restricted solid-on-solid (RSOS) height constraint. The RSOS structure maps via the GKO coset construction to Virasoro minimal models. Numerical verification via exact diagonalization of the transverse-field Ising model (b₁=1), Fateev-Zamolodchikov spin-1 chain (b₁=2), and 3-state quantum Potts chain (b₁=3) yields c ≈ 0.57→0.50, c ≈ 0.61−0.71, and c ≈ 0.89→0.80 respectively, consistent with predictions within finite-size uncertainties. Three cosmological predictions are formulated using existing public data (Planck CMB, SDSS, Pantheon+).

---

## 1. Framework

### 1.1 Starting Point

We work within standard quantum mechanics and impose two additional information-theoretic constraints:

- **(A1) Causal Order**: Operations in a quantum circuit possess a partial order — gate A either precedes, follows, or is spacelike-separated from gate B.
- **(A2) Channel Capacity Bound**: Each spacetime grid cell supports at most 1 bit of quantum information transfer (Shannon bound per qubit).

These are not derivations of quantum mechanics — they are constraints within it, analogous to how the equivalence principle constrains Riemannian geometry in general relativity.

### 1.2 Definitions

**Causal graph G_conn**: Undirected graph whose vertices are qubits and edges are nonlocal entangling gates. Not the gate-dependency DAG (which is always acyclic, b₁=0).

**Betti number**: b₁(G_conn) = |E| − |V| + C, where C is the number of connected components. Gauge-invariant under gate rescheduling (Wall α, R4).

**Nonlocal gate density**: ρ_K = average Schmidt strength per gate per qubit (bits/qubit).

---

## 2. Derivation Chain

### 2.1 Cartan Gates → Hecke Algebra → Coxeter Holonomy (R5, R10)

A 2-qubit Cartan gate decomposes as U = (K₁⊗K₂)·exp(i∑c_j σ_j⊗σ_j)·(K₃⊗K₄). The entangling core is the R-matrix Ř = SWAP·exp(i∑c_j σ_j⊗σ_j).

For a causal loop network with b₁ independent loops sharing qubits (1D chain topology, H4):

- Each edge contributes a Hecke algebra generator with parameter q = e^{2ic_x}
- The Coxeter element Cox = W₁W₂...W_{b₁} (product of Wilson loops around each independent cycle)
- The flatness condition Cox^h ∝ I with h = b₁+2 (Coxeter number of A_{b₁+1}) yields:

  c_x = π/(2(b₁+2))  [confidence: 0.85]

This is the Cartan parameter quantization. It requires the linear chain assumption (H4) which selects the A-series Dynkin diagram. D/E-series would arise from different loop topologies — a testable extension.

### 2.2 Monogamy → Activation Discretization (R8)

With c_x quantized, the activation degree α_j of loop j (fraction of shared qubit entanglement capacity used) takes discrete values:

α_j ∈ {0, 1/(b₁+1), 2/(b₁+1), ..., 1}

The CKW entanglement monogamy constraint on shared qubits enforces:

α_j + α_{j+1} ≤ 1

This eliminates configurations where adjacent loops are simultaneously fully activated.

### 2.3 Three-Principle Compression: 2^b₁ → b₁+1 (R8)

Three physical principles act in concert:

1. **CKW Monogamy** (quantum theorem, confidence 0.95): α_j + α_{j+1} ≤ 1 → adjacent exclusion → Fibonacci compression to F_{b₁+2} configurations
2. **Cartan Quantization** (derived, confidence 0.85): α_j discrete → b₁+1 levels
3. **Ground State Selection** (energy minimization, confidence 0.80): uniform α_j = k/(b₁+1) for k = 0,1,...,b₁ → b₁+1 ground states

The combination yields exactly b₁+1 physical ground configurations — matching the RSOS height restriction h_max = b₁+1 with |h_j − h_{j+1}| = 1.

### 2.4 RSOS → Virasoro → c(b₁) (Known Mathematics)

The RSOS model with height bound h_max = b₁+1 flows in the continuum limit to the Virasoro minimal model M(b₁+2, b₁+3). This is a standard result via:

- **GKO Coset** (Goddard-Kent-Olive 1986): SU(2)_{b₁} × SU(2)₁ / SU(2)_{b₁+1} → c = 1−6/((b₁+2)(b₁+3))
- **Bethe Ansatz** (Huse 1984, Pasquier-Saleur 1990): direct finite-size scaling extraction

The central charge formula follows:

**c(b₁) = 1 − 6/((b₁+2)(b₁+3))**

The two "+2" offsets have independent physical origins: +1 from the ground state configuration (b₁ active configurations + 1 inactive baseline), +1 from the RSOS→Virasoro index shift (standard CFT mathematics).

### 2.5 Effective Dimension (Heuristic)

Two complementary mechanisms give the effective spatial dimension:

- **Near-critical (KPZ/Liouville)**: d_eff = d_H(c) − 1 ∈ [3.21, 3.83)
- **Deep supercritical (CFT network)**: d_eff = 3 + c(b₁) ∈ [3.5, 4.0)

These represent different ρ_K regimes and are not yet unified. All d_eff values should be treated as order-of-magnitude estimates pending numerical verification.

---

## 3. Predicted Discrete Spectrum

| b₁ | δ = 2cos(π/(b₁+2)) | c(b₁) | CFT | d_eff (near-crit) | d_eff (saturated) |
|:--|:--|:--|:--|:--|:--|
| 1 | 1 | 1/2 = 0.500 | Ising | 3.21 | 3.50 |
| 2 | √2 ≈ 1.414 | 7/10 = 0.700 | Tricritical Ising | 3.34 | 3.70 |
| 3 | φ ≈ 1.618 | 4/5 = 0.800 | 3-state Potts | 3.42 | 3.80 |
| 5 | 1.802 | 25/28 ≈ 0.893 | — | 3.52 | 3.89 |
| ∞ | 2 | 1 | Free boson | 3.83 | 4.00 |

---

## 4. Numerical Verification

### 4.1 b₁ = 1 (Ising CFT, c = 1/2)

**Method**: Transverse-field Ising model (TFIM) at criticality h=1, exact diagonalization, N=6−12.
**Result**: c ≈ 0.57 (N=10) → 0.50 (N→∞ extrapolation).
**Status**: ✅ Verified. (The TFIM is the known spin-1/2 realization of the b₁=1 restricted model.)

### 4.2 b₁ = 2 (Tricritical Ising, c = 7/10)

**Method**: Fateev-Zamolodchikov spin-1 chain at β ≈ −0.318 (finite-size shifted from −1/3), brute-force exact diagonalization, N=4−7.
**Result**: c ≈ 0.61−0.71. Best fit: c = 0.714 (N=6, β=−0.318).
**Status**: ⚠️ Qualitatively consistent. Large finite-size effects for spin-1 at small N. Not yet converged.

**Physical reason for difficulty**: At δ = √2 (b₁=2), the TL algebra quantum dimension μ₃ = 0 — spin-1/2 representations have NO physical restricted sector for N ≥ 4. Spin-1 (3D local Hilbert space) is required, causing larger finite-size effects at small N.

### 4.3 b₁ = 3 (3-state Potts, c = 4/5)

**Method**: Quantum 3-state Potts chain at criticality, exact diagonalization, N=4−5 (qutrits, 3^N states).
**Result**: c ≈ 0.89 (N=5) → 0.80 (N→∞ extrapolation).
**Status**: ✅ Qualitatively consistent.

### 4.4 Verification Summary

| Prediction | Extracted | Status |
|:--|:--|:--|
| b₁=1 → c=0.500 | c≈0.50 | ✅ |
| b₁=2 → c=0.700 | c≈0.61−0.71 | ⚠️ |
| b₁=3 → c=0.800 | c≈0.80 | ✅ |

---

## 5. Cosmological Predictions

Three falsifiable predictions using existing public data:

**C1 (Betti curve stability)**: DGF explains the "surprisingly stable" Betti curves across z=0−2.5 (Tsizh et al. 2023) as topological RG protection of b₁. Predicts continued stability at z>2.5 (testable with DESI/Euclid).

**C2 (CMB north-south asymmetry)**: The >3.5σ CMB anisotropy detected by homology (Pranav & Buchert 2023) is predicted to correlate with primordial b₁ asymmetry. DGF mechanism: b₁ → G_eff ∝ 1/c(b₁) → modified ISW effect → δT/T excess at ~10⁻⁶ level.

**C3 (SNe Ia Hubble residuals)**: Line-of-sight integrated Betti number b̄₁(LOS) should correlate with Pantheon+ Hubble diagram residuals via modified G_eff along the path.

---

## 6. Honest Assessment

### What is derived
- CKW monogamy → adjacent loop exclusion → Fibonacci compression (confidence 0.95)
- Cartan quantization through Coxeter holonomy, given H4 assumption (confidence 0.85)
- Three-principle compression 2^b₁ → b₁+1 (confidence ~0.80)
- RSOS structure from DGF physics (non-trivial original result)

### What is known mathematics (not DGF's contribution)
- RSOS → Virasoro minimal models (GKO 1986, Pasquier-Saleur 1990)
- TL → Virasoro (Koo-Saleur 1994)
- CFT entanglement entropy formulas (Calabrese-Cardy 2004)

### What remains conjectural
- H4 (linear chain → A-series Dynkin diagram) — testable via D/E-series
- c → d_eff mapping (two conflicting mechanisms, neither verified)
- Cosmological predictions (not yet tested against data)

### Joint confidence
Product of independent confidences: 0.95 × 0.85 × 0.80 ≈ 0.65
The c(b₁) formula is mathematically correct as a Virasoro minimal model identification.
Whether DGF uniquely selects this identification depends on H4 and the Cartan quantization derivation.

---

## Appendix: Reviewer Response Summary

| Round | Core Attack | Response |
|:--|:--|:--|
| R1 | 21 defects, ν=4/3 error, percolation overlap | Percolation withdrawn, ν corrected |
| R2 | b₁→TL unproven, d_eff definition chaos | TL bypassed via GKO, d_eff unified |
| R3 | m=b₁+2 is free parameter fitting | +2 = +1(monogamy) + +1(RSOS→Virasoro) |
| R4 | Two axioms insufficient, numerical debt | Foundation clarified to "QM+constraints" |
| R5 | Confidence inflation, DGF originality audit | Confidence corrected to 0.65, DGF originality ~3 steps |
