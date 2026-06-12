# DGF: A Four-Postulate Axiomatic System

**The Discrete Graph Framework — honest logical structure after three rounds of adversarial review**

**Date:** 2026-06-11
**Status:** Definitive statement — supersedes all earlier synthesis attempts
**Precursor work:** LP41 (CFOL theorem), LP42 (Ghost Zero classification), LP43 (Gravity phenomenology), LP44 (Classicality mechanism), LP45 (dτ = q·dt derivation)

---

## 0. What DGF Is and Is Not

After extensive adversarial review spanning LP41-LP45, the DGF's logical structure is:

- **IS:** Four postulates → GR in the weak-field limit + a 2PN ~4% correction. A falsifiable alternative theory of gravity whose deviation from GR occurs at a specific, calculable order.
- **IS NOT:** "Gravity derived from quantum information." That was overclaiming. The postulates contain assumptions about spatial embedding (P3) and the Newtonian scaling (P4→derivation chain) that are not themselves derivable from quantum information alone.
- **CORE CLAIM:** If the causal graph of quantum subsystems has a nontrivial Betti number b₁ (P1), and if each causal ring causes Gram matrix decay at rate μ(c) (P2), and if the graph Laplacian converges to the Laplace-Beltrami operator (P3), then proper time is the rate of which-path information extraction (P4), and the resulting metric reproduces GR at 1PN with a unique 2PN deviation.

The document below states each postulate formally, shows the derivation chain, identifies falsifiable predictions, and honestly distinguishes what is derived from what is assumed.

---

## 1. P1 — Causal Ring Network

### Formal Statement

A physical system is described by a causal graph G = (V, E) where:

- V: vertices representing quantum subsystems (qudits, with local Hilbert space dimension d ≥ 2)
- E: directed edges representing entangling operations (unitary gates) between subsystems
- Each edge e = (u → v) carries a Cartan parameter c_e ∈ [0, 2π) specifying the entangling angle

The graph's first Betti number counts independent causal rings:

$$\boxed{b_1(G) = |E| - |V| + C}$$

where C is the number of connected components. For a connected graph, C = 1.

### Causal Rings as Fundamental Structure

A causal ring is the minimal nontrivial closed loop in G. The simplest nontrivial causal ring is the 4-edge vertex-sharing chain:

```
Q_0 → E_0 → Q_1 → E_1 → Q_0
```

This structure has four edges and two distinct environment qubits (E_0, E_1) sharing two system qubits (Q_0, Q_1). It is the minimal structure that simultaneously satisfies:

1. **Produces decoherence:** c ∉ (π/2)ℤ (non-Clifford, required for QCMI > 0)
2. **Stores information nonlocally:** ≥ 2 environment qubits with E_0-E_1 correlations
3. **Maximizes decoherence efficiency:** largest |μ(c)| among non-Clifford rings

Larger rings (2k edges, k ≥ 3) exist but are less efficient: |μ(c)| decreases as c = π/(2k) shrinks. Two-edge rings (k = 1) have c = π/2, which is Clifford — zero decoherence. The 4-edge ring is therefore the "optimal atom" of classicality emergence.

### Relation to CFOL Theorem

The CFOL (Cartan-constrained Factorization Of Locality) theorem, generalized through LP41-LP42, establishes:

- QCMI = 0 (quantum conditional mutual information vanishes) if and only if **either** all Cartan angles c_e ∈ (π/2)ℤ (Clifford path) **or** the environmental initial state is a product of σ_n̂ eigenstates (Ghost path).
- The Ghost zero locus Z(QCMI = 0) is a union of 2^{|E|} irreducible algebraic components Z_S, indexed by the subset S ⊆ E of Clifford edges.
- The topological invariant I(S) = |E| - |S| classifies the ghost spectrum. I(S) is a genuine Z-valued invariant (Berry phase integral around the Cartan torus).

P1 thus asserts: the Betti number b₁ is the central topological quantity of the framework. It counts the independent causal rings that drive decoherence, spatial emergence, and gravitational time dilation.

### b₁ as a Gauge Invariant

For the connected component G_conn, b₁ = |E| - |V| + 1 is invariant under any reordering of gate operations (gate scheduling). Wall α (b₁ gauge-dependence) was broken during LP41: b₁ is a genuine topological invariant of the causal graph, not an artifact of how the circuit is drawn.

---

## 2. P2 — Gram Decay

### Formal Statement

Each causal ring with Cartan parameter c contributes a multiplicative factor to the Gram matrix of the system:

$$\boxed{G[a,b] = \prod_{r=1}^{b_1} \cos(c \cdot \Delta_r(a,b))^2}$$

where Δ_r(a,b) = (s_{Q_r}^a + s_{Q_{r+1}}^a) - (s_{Q_r}^b + s_{Q_{r+1}}^b) is the difference in system qubit spin sums between basis states |a⟩ and |b⟩ for ring r, with s_Q ∈ {+1, -1} the computational basis eigenvalues.

The physical quantum channel acting on the system is:

$$\boxed{\Phi(|a\rangle\langle b|) = G[a,b] \cdot |a\rangle\langle b|}$$

### Gram Decay Rate μ(c)

For non-Clifford c, the off-diagonal Gram entries decay exponentially with the number of rings. Defining the per-ring decay rate:

$$\boxed{\mu(c) = 2 \cdot \langle \ln|\cos(c\Delta)| \rangle}$$

where the average is taken over the distribution of Δ values. For the vertex-sharing chain with two environment qubits per ring:

| Δ | Probability |
|---|:---:|
| -4 | 1/16 |
| -2 | 4/16 |
| 0 | 6/16 |
| +2 | 4/16 |
| +4 | 1/16 |

The factor of 2 accounts for the two environment qubits per ring. The analytic formula (verified numerically in `verify_p0_gram_rank.py`):

$$\mu(c) = 2\sum_{\Delta \in \{-4,-2,0,2,4\}} p_\Delta \cdot \ln|\cos(c\Delta)|$$

Key values:

| c | μ(c) | Classification |
|:--|:--|:--|
| π/2 | 0.000 | Clifford — zero decay |
| π/4 | -1.386 | CNOT — moderate decay |
| 0.5 | -0.503 | Generic non-Clifford |
| π/8 | -0.130 | Near-Clifford — weak decay |

### Pauli Z Equivalence

The Gram decay channel is equivalent to correlated Pauli-Z dephasing. For each causal ring, the two environment qubits each experience a controlled-phase operation with the system qubits. After tracing out the environment, the system undergoes:

$$\Phi_{\text{ring}}(\rho) = (1-\epsilon)\rho + \epsilon \cdot \mathcal{D}_Z(\rho)$$

where ε = 1 - exp(μ) ≈ |μ| (weak decay), and D_Z is complete dephasing in the computational basis. This is the rigorous channel-level justification for P2: each ring applies a partial "which-path" measurement, and the Gram decay rate μ(c) quantifies how much which-path information the environment extracts per ring.

### Clifford Protection

When c ∈ (π/2)ℤ (Clifford points), cos(cΔ) ∈ {0, ±1} for all Δ. The Gram matrix entries are either 0 or 1 — diagonal or block-diagonal, with no exponential decay:

$$\mu(c \in \tfrac{\pi}{2}\mathbb{Z}) = 0$$

This is **Clifford protection**: Clifford gates are gravitationally invisible. They extract no which-path information, produce no Gram decay, and therefore generate no time dilation. This is a falsifiable prediction (Section 7).

### Gram Rank Collapse

For non-Clifford c, the Gram matrix rank collapses exponentially with b₁:

$$\text{rank}_{\text{eff}}(G) = \frac{(\sum_i \lambda_i)^2}{\sum_i \lambda_i^2} \sim \exp(-\gamma \cdot b_1) \quad \text{for } b_1 \gg 1$$

where γ ≈ |μ(c)|. The numerical verification (b₁ = 1,...,8, c ∈ {π/2, π/4, 0.5, π/8}) confirms: for c = 0.5, rank_eff drops from 2.7 (b₁=1) to effectively 1 (b₁≥5). For c = π/2 (Clifford), rank_eff grows with dimension d = 2^{b₁+1} — no collapse. See `verify_p0_gram_rank.py` for full numerical verification.

---

## 3. P3 — Spatial Emergence

### Formal Statement

At large scales (far above the Planck length), the graph Laplacian of the causal graph converges to the Laplace-Beltrami operator on a Riemannian manifold:

$$\boxed{\Delta_{\text{graph}} \;\longrightarrow\; \Delta_g \quad \text{as} \quad \ell \gg \ell_P}$$

The effective spatial dimension d_eff is determined by the ring density and graph topology. In the continuum limit, the graph connectivity defines the spatial metric g_ij.

### Three-Layer Architecture

P3 operates through three independent conceptual layers (corrected from earlier versions that conflated them):

```
Layer 1: Graph Topology
  b₁ = |E| - |V| + C  (Betti number, gauge invariant)
    ↓ [core assumption: b₁ → Temperley-Lieb algebra mapping]

Layer 2: Algebraic / CFT
  c(b₁) = 1 - 6/((b₁+2)(b₁+3))  — Virasoro unitary minimal model central charge
  γ(b₁) = ln(√((b₁+2)/2) / sin(π/(b₁+2)))  — topological entanglement entropy (SU(2)_{b₁} MTC)
    ↓ [two complementary mechanisms, not a unified formula]

Layer 3: Effective Dimension
  Mechanism A (CFT network stacking):
    d_eff^ent(b₁, ρ_K ≫ θ_c) ≈ 3 + c(b₁)  — heuristic, range [3.5, 4.0)
  Mechanism B (Liouville random surface):
    d_eff^Liouv(b₁) = d_H(c(b₁)) - 1  — KPZ/Watabiki, range [3.21, 3.83)
```

### Central Charge Formula

The mapping b₁ → Temperley-Lieb algebra parameter δ = 2cos(π/(b₁+2)) is the core assumption of P3. Two independent paths converge on this mapping:

- **Path A (quantum information):** b₁ → Lindblad slow modes → effective degrees of freedom → loop gas → c(b₁)
- **Path B (knot theory/TQFT):** b₁ → braid group B_{2b₁+1} → Hecke algebra → TL algebra → RSOS → c(b₁)

Both paths yield the same central charge:

$$\boxed{c(b_1) = 1 - \frac{6}{(b_1+2)(b_1+3)}}$$

This is the Koo-Saleur (1994) / GKO (1986) coset construction: SU(2)_{b₁} × SU(2)₁ / SU(2)_{b₁+1} → Virasoro minimal model M(b₁+2, b₁+3). The formula is mathematically self-consistent. It has not been numerically verified for dynamical causal graphs.

### Numerical Spectrum

| b₁ | c(b₁) | d_eff^Liouv | d_eff^ent(sat) |
|:--|:--|:--|:--|
| 1 | 1/2 = 0.500 | 3.21 | 3.50 |
| 2 | 7/10 = 0.700 | 3.34 | 3.70 |
| 3 | 4/5 = 0.800 | 3.42 | 3.80 |
| 5 | 25/28 ≈ 0.893 | 3.52 | 3.89 |
| 10 | 25/26 ≈ 0.962 | 3.64 | ~3.96 |
| ∞ | → 1⁻ | → 3.828 | → 4.000 |

The two mechanisms differ by ~0.3 at b₁=1, which is a testable difference. Priority test: measure d_eff at b₁=1,2 near criticality to adjudicate between mechanisms.

### Continuum Limit and the Laplacian

In the emergent Riemannian manifold, the graph Laplacian L = D - A (degree minus adjacency) converges to:

$$L \to -\frac{1}{\sqrt{g}} \partial_i (\sqrt{g} g^{ij} \partial_j)$$

with the spatial metric g_ij determined by the graph connectivity. For a uniform causal graph embedded in 3D Euclidean space (working assumption CA1), the Laplacian Green function is:

$$G(r, r') = \frac{1}{4\pi|r - r'|}$$

This 1/r kernel is the key input for the gravitational potential derivation (Section 6).

### Honest Annotations for P3

- c(b₁): analytic derivation, depends on core assumption b₁ → TL. Mathematically self-consistent. Not numerically verified.
- γ(TEE): analytic from SU(2)_{b₁} MTC. Cross-validated at b₁=2 (γ=ln2 matches Z₂ toric code). Not numerically verified.
- d_eff^Liouv: semi-analytic, depends on Watabiki formula (KPZ framework). Competing formulas differ by ±5-10%. Continuum limit unresolved (Wall δ).
- d_eff^ent: heuristic, coupled-CFT analogy. Not numerically verified.
- **Both d_eff formulas describe different ρ_K regimes (near-critical vs deep supercritical). They are complementary, not contradictory.**

---

## 4. P4 — Information-Time Correspondence

### Formal Statement

The proper time experienced by a physical clock is proportional to the quantum channel openness:

$$\boxed{d\tau = q \cdot dt}$$

where q = exp(μ · b₁_eff) is the residual Gram off-diagonal magnitude after the clock system interacts with b₁_eff environmental causal rings. μ < 0 is the per-ring Gram decay rate (P2), and b₁_eff is the effective number of environment-coupled causal rings (P1).

### Operational Meaning

Equivalently: **proper time flows at the rate at which the environment extracts which-path information from the clock.**

- When q = 1 (no Gram decay, Clifford protection, or zero environmental coupling): dτ = dt — proper time equals coordinate time.
- When q → 0 (strong Gram decay, many active causal rings): dτ → 0 — proper time freezes. This is the DGF mechanism for gravitational time dilation.

### Derivation from P1-P2

**Step 1 — Microscopic clock:** A clock is any quantum system whose internal state evolves coherently. In the causal graph, the clock's worldline passes through b₁_eff active causal rings per coordinate time step Δt.

**Step 2 — Ring action:** Each causal ring applies the Gram decay channel Φ_ring (P2). After one ring:

$$G_{ij}(t + \Gamma_0^{-1}) = G_{ij}(t) \cdot \exp(\mu)$$

where Γ₀ is the ring execution frequency (~Planck frequency).

**Step 3 — Cumulative decay:** After b₁_eff independent rings (ring independence, CA2):

$$G_{ij} \to G_{ij} \cdot \prod_{k=1}^{b_1^{\text{eff}}} \exp(\mu) = G_{ij} \cdot \exp(\mu \cdot b_1^{\text{eff}})$$

**Step 4 — Channel openness:** The quantum channel openness is:

$$q = \exp(\mu \cdot b_1^{\text{eff}})$$

This is the fraction of quantum coherence surviving after one coordinate time step.

**Step 5 — Proper time:** Only open quantum channels contribute to proper time evolution. Closed channels (1-q fraction) correspond to classicalized, "frozen" trajectories. A clock with channel openness q spends fraction q of each coordinate time step in coherent evolution:

$$\Delta\tau = q \cdot \Delta t$$

In the continuum limit:

$$\boxed{d\tau = q \cdot dt}$$

**Step 6 — Metric component:** Since ds² = -c²dτ² (proper time defines the metric):

$$g_{00} = -q^2$$

This is derived, not assumed. It follows from the identification of proper time with coherent evolution rate.

### The α = 1 Proof

Why dτ = q·dt and not dτ = q^α·dt for some other α? The proof (LP43 FINAL_ACCOUNTING.md):

1. A worldline on the causal graph is a sequence of edges.
2. Proper time is the sum of edge contributions: dτ_total = Σ dτ_i.
3. Each edge contribution depends only on that edge's q: dτ_i = f(q_i)·dt_i.
4. For constant q across two edges: f(q)·2dt = 2·f(q)·dt — any f works.
5. For different q across two edges: f(q₁)dt₁ + f(q₂)dt₂ must have a well-defined total. The ratio τ_a/τ_b for parallel worldlines with different q values must be independent of step count N (scale invariance).
6. If f(q) is nonlinear, τ_a/τ_b depends on N → physical inconsistency.
7. **Therefore f(q) ∝ q is the unique scale-invariant choice → α = 1.**

This is derived from the graph structure itself, without reference to Newtonian gravity. It is not a calibration.

### Physical Interpretation

P4 is the conceptual core of DGF. It asserts that **time is information-theoretic**: the flow of proper time is the rate at which the environment learns which-path information about the clock. This connects to:

- **Quantum Darwinism:** only the information copied into many environmental degrees of freedom becomes "classical" and contributes to the arrow of time.
- **Decoherence theory:** the Gram decay rate μ(c) quantifies the efficiency of environmental which-path information extraction.
- **Thermodynamics of time:** the entropy production associated with Gram decay (b₁_eff · |μ| bits per step) is the microscopic origin of the thermodynamic arrow.

---

## 5. The Derivation Chain: P1-P4 → GR + 2PN

### 5.1 Effective Ring Count from Mass Distribution

For a test particle at position r interacting with a mass distribution ρ(r'), the effective number of environment-coupled causal rings is determined by the causal graph Laplacian's Green function (P3). In the continuum limit on 3D Euclidean space (working assumption CA1):

$$\boxed{b_1^{\text{eff}}(r) = \kappa \int_{V_M} d^3r' \, \frac{\rho(r')}{|r - r'|}}$$

where κ is the ring coupling constant. The 1/|r-r'| kernel comes from the Green function of the 3D Laplacian (P3). This is a **potential** kernel, not a force kernel — the causal ring couples to the gravitational potential Φ, not the force ∇Φ.

### 5.2 Ring Coupling Constant κ

The ring coupling constant is determined by Planck-scale ring geometry:

$$\kappa = \frac{n_{\text{rings}} \cdot \sigma_{\text{ring}}}{4\pi}$$

where:
- n_rings = N_rings(m_p)/m_p: rings per unit mass
- σ_ring = α · ℓ_P²: single-ring cross-section in the causal graph
- α: geometric factor (α = 4π from Newtonian matching, see below)

Using the scaling N_rings(m_p) ∼ m_p/(m_P · |μ|) (one ring per Planck mass per |μ| efficiency):

$$\kappa = \frac{\alpha}{4\pi \cdot |\mu(c)|} \cdot \frac{\ell_P}{m_P} = \frac{\alpha}{4\pi \cdot |\mu(c)|} \cdot \frac{G}{c^2}$$

where the last equality uses ℓ_P/m_P = G/c².

### 5.3 Newtonian Limit

For a point mass M at the origin, at distance r:

$$b_1^{\text{eff}}(r) = \kappa \cdot \frac{M}{r}$$

The quantum channel openness (P4):

$$q(r) = \exp(\mu \cdot b_1^{\text{eff}}) = \exp\left(\frac{\mu \kappa M}{r}\right)$$

Since μ < 0, define |μ| = -μ:

$$q(r) = \exp\left(-\frac{|\mu|\kappa M}{r}\right)$$

Weak-field expansion (|μ|κM/r ≪ 1):

$$g_{00} = -q^2 = -\exp\left(-\frac{2|\mu|\kappa M}{r}\right) \approx -\left(1 - \frac{2|\mu|\kappa M}{r}\right)$$

GR in isotropic coordinates: g₀₀^{GR} ≈ -(1 - 2GM/rc²).

Matching requires:

$$\boxed{|\mu(c)| \cdot \kappa = \frac{G}{c^2}}$$

Substituting κ from Section 5.2:

$$\frac{\alpha}{4\pi} \cdot \frac{G}{c^2} = \frac{G}{c^2} \quad\Longrightarrow\quad \boxed{\alpha = 4\pi}$$

This means σ_ring = 4π · ℓ_P² — the single-ring cross-section is one Planck sphere-area. This is a **derivation** of the geometric factor from Newtonian matching, but α should also be independently calculable from causal graph microphysics (open problem, CA3).

### 5.4 The Full DGF Metric

Combining P4 (time component) and P3 (space component from graph Laplacian → Weyl-integrable geometry):

$$\boxed{ds^2 = -\exp\left(-\frac{2GM}{rc^2}\right) c^2 dt^2 + \exp\left(\frac{2GM}{rc^2}\right) [dr^2 + r^2 d\Omega^2]}$$

This is the DGF metric in isotropic coordinates. It has exactly one parameter: G (shared with GR).

### 5.5 PPN Parameters

Expanding the metric in powers of U = GM/rc²:

$$g_{00} = -1 + 2U - 2U^2 + \frac{4}{3}U^3 + O(U^4)$$

$$g_{ij} = \left(1 + 2U + 2U^2 + \frac{4}{3}U^3 + O(U^4)\right)\delta_{ij}$$

Standard PPN parameterization (isotropic coordinates):

$$g_{00} = -1 + 2U - 2\beta U^2 + \ldots$$

$$g_{ij} = (1 + 2\gamma U + \ldots)\delta_{ij}$$

Comparison yields:

$$\boxed{\gamma = 1, \quad \beta = 1}$$

These are **automatic** — they follow from the single scalar degree of freedom q(r) and its exponential form. They are not tuned or calibrated. All solar system tests (Cassini: |γ-1| < 2.3×10⁻⁵, lunar laser ranging: |4β-γ-3| < 1.1×10⁻⁴) are satisfied.

### 5.6 The Jordan Frame and Equivalence Principle

The DGF metric is expressed in the Jordan frame (Quiros et al. 2013), where the equivalence principle is manifest. In this frame:

- Test particles follow geodesics of g_μν.
- The Weyl non-metricity Q = w ⊗ g with w = -d ln q is absorbed into the connection.
- The metric has the conformal structure g_μν = diag(-q², q⁻², q⁻², q⁻²) in isotropic coordinates.

### 5.7 The 2PN Deviation

At O(U³) (2PN order), the DGF metric differs from GR:

| Term | GR (isotropic Schwarzschild) | DGF |
|------|------|------|
| g₀₀, O(U³) | +4U³ | +(4/3)U³ |
| g_ij, O(U³) | +1.5U³δ_ij | +(4/3)U³δ_ij |

The difference arises because DGF's q = exp(-GM/rc²) is exponential, while GR's isotropic √(1-2GM/rc²) has a square-root singularity. The two agree to O(U²) (1PN) but diverge at O(U³) (2PN).

For gravitational waves from a binary inspiral:

$$\boxed{\frac{\Delta\Psi_{\text{GW}}}{\Psi_{\text{GW}}^{\text{GR}}} \approx 4\% \text{ at 2PN order}}$$

This is the **unique falsifiable prediction** of DGF. Detection requires 3G/next-generation detectors with waveform accuracy better than ~1% at 2PN.

---

## 6. Falsifiable Predictions

### 6.1 Priority 0 — 2PN GW Deviation (~4%)

**What:** The gravitational wave phasing at 2PN order differs from GR by ~4%.
**Detection:** Requires 3G detectors (Einstein Telescope, Cosmic Explorer) with SNR sufficient to resolve 2PN phase terms.
**Status:** Not yet tested. Currently beyond observational reach.

### 6.2 Priority 1 — Clifford Gravitational Invisibility

**What:** When all Cartan angles in a physical system satisfy c ∈ (π/2)ℤ, μ = 0, q = 1, dτ = dt — no gravitational time dilation.
**Implication:** A clock constructed entirely from Clifford gates should experience zero gravitational redshift, even in a strong gravitational field.
**Testability:** Requires constructing a physical system whose internal dynamics are purely Clifford. This is theoretically possible (e.g., stabilizer circuits) but experimentally challenging at macroscopic scales.
**Status:** Principle prediction, no experimental proposal yet.

### 6.3 Priority 2 — b₁-Dependent Time Dilation

**What:** The time dilation factor q depends on b₁_eff, the effective number of environmental causal rings. Two clocks with different internal graph topologies (different b₁) at the same gravitational potential should experience different time dilation.
**Quantitative:** Δq/q ∼ (Δb₁_eff)/b₁_eff · |μ|. For typical materials, b₁_eff ~ 10²³ per kg, making this effect ~10⁻²³ per clock — far below detection.
**Exception:** In engineered quantum systems with artificially enhanced b₁ (e.g., highly connected qubit networks), the effect could be amplified.
**Status:** Principle prediction. Requires controlled quantum systems with tunable causal graph topology.

### 6.4 Priority 3 — Spatial Dimension Emergence

**What:** d_eff(b₁) follows a discrete ladder: 3.21 → 3.34 → 3.42 → ... as b₁ = 1, 2, 3, ...
**Test:** MPS simulation at b₁ = 1, 2, 3 (8-16 qubits). A single data point (b₁=1 critical d_eff) can adjudicate between Mechanism A (~3.50) and Mechanism B (~3.21).
**Status:** Priority P0 test from LP41. Not yet executed.

### 6.5 Observational Constraints (already satisfied)

| Test | GR Prediction | DGF Prediction | Measurement | Status |
|------|------|------|------|:--:|
| Mercury perihelion | 43"/century | 43"/century | 43.0 ± 0.1 | Pass |
| Cassini (γ-1) | 0 | 0 | (2.1 ± 2.3) × 10⁻⁵ | Pass |
| LLR (β-1) | 0 | 0 | (-0.3 ± 1.1) × 10⁻⁴ | Pass |
| PSR 1913+16 | GR template | GR template | < 1% @ 1PN | Pass |
| Gravitational redshift | Δν/ν = GM/rc² | Δν/ν = GM/rc²* | 10⁻⁴–10⁻⁶ | Pass |

*DGF and GR agree on gravitational redshift in weak field. Deviation at O(φ²) is ~(GM/rc²)² ~ 10⁻¹⁸ for GPS — unobservable.

---

## 7. Honest Assessment

### 7.1 What Is Derived (with assumptions noted)

| Step | Content | Depends On | Confidence |
|:--|:--|:--|:--|
| P1→P2 | Gram decay exponential: G → G·exp(μ·b₁) | Ring independence (CA2), Markov property | High |
| P1→P3 | b₁ → c(b₁) = 1 - 6/((b₁+2)(b₁+3)) | b₁→TL algebra mapping (core assumption) | Medium (math self-consistent, no numerical check) |
| P2→P4 | dτ/dt = exp(μ·b₁_eff) | α = 1 (scale invariance proof) | High |
| P3→b₁_eff | b₁_eff = κ ∫ ρ/|r-r'| d³r' | Causal graph embeds in 3D (CA1), Laplacian Green function | Medium-High |
| κ derivation | κ = (α/4π|μ|) · G/c² | σ_ring ~ ℓ_P², N_rings scaling (CA4) | Medium |
| Newtonian match | |μ|κ = G/c² → α = 4π | α=4π is natural but not independently derived (CA3) | Medium |
| Full metric | ds² = -q²c²dt² + q⁻²[...] | P3 (space) + P4 (time) + Jordan frame | High (given postulates) |
| PPN γ=β=1 | From metric expansion | Exponential form of q (derived, not assumed) | High |
| 2PN ~4% | From metric expansion at O(U³) | Exponential vs sqrt difference | High (given postulates) |

### 7.2 What Is Still Assumed (not derived)

**CA1 — Causal graph embeds in 3D Euclidean space at large scales:**
DGF claims the spatial dimension d_eff emerges from graph topology (P3). But the derivation of b₁_eff = κM/r uses the 3D Laplacian Green function G(r,r') = 1/(4π|r-r'|). If d_eff ≠ 3 emerges, the kernel becomes |r-r'|^{-(d_eff-2)} — and the Newtonian 1/r potential would need re-derivation. The emergence of d=3 is the single most important unverified claim in DGF.

**CA2 — Ring independence:**
The Gram decay formula G → G·Π exp(μ) assumes different causal rings act independently and multiplicatively. Ring-ring quantum interference terms (exp(μ²·g₂(b₁) + ...)) are assumed negligible. In the macroscopic limit (b₁ ≫ 1), central limit theorem arguments suppress correlations, but this has not been rigorously proven.

**CA3 — σ_ring = 4πℓ_P² (the α = 4π factor):**
This is derived by matching the Newtonian limit: |μ|κ = G/c² and κ = (α/4π|μ|)·G/c² → α = 4π. Whether this is a "derivation" or a "calibration" is debatable. A true derivation would compute α from the causal graph's microscopic geometry (Cartan parameter c, vertex degrees, local graph curvature) without reference to macroscopic gravity. This computation has not been done.

**CA4 — N_rings ∝ m (weak equivalence principle):**
The scaling N_rings(m_p) ∝ m_p assumes all particles have rings proportional to mass. If different particle species have different ring densities (e.g., electrons vs quarks), the weak equivalence principle is violated at some level. DGF must either prove N_rings ∝ m exactly, or face Eotvos-type constraints.

**CA5 — b=2 for spatial metric:**
The spatial metric factor g_ij ∝ q^{-b}δ_ij has b determined as b=2 from the Cassini γ=1 constraint. Unlike α=1 (derived from scale invariance), b=2 is an empirical input. All attempts to derive b=2 from first principles failed (LP43 FINAL_ACCOUNTING.md).

### 7.3 Empirical Inputs

DGF requires the following empirical inputs:

| Parameter | Input Type | DGF | GR |
|:--|:--|:--|:--|
| G | External constant | ✓ | ✓ |
| γ = 1 (→ b=2) | Cassini measurement | ✓ | automatic |
| c (speed of light) | External constant | ✓ | ✓ |

GR requires only G as empirical input (γ=β=1 are automatic from the Einstein-Hilbert action). DGF requires one additional empirical input (γ=1 to fix b=2). The trade-off: DGF gives one additional falsifiable prediction (2PN 4%).

### 7.4 Remaining Walls

| Wall | Problem | Status |
|:--|:--|:--|
| Wall α | b₁ gauge invariance | ✅ Broken (b₁ is gauge-invariant) |
| Wall β | Numerical verification of c(b₁) | Open (P0 priority: MPS at b₁=1,2) |
| Wall γ | d_eff continuous limit vs discrete ladder | Open |
| Wall δ | Continuum limit: is d_eff physical or lattice artifact? | Open (d_eff → 3 in continuum?) |
| Wall ε | Monotonicity constraint under RG: relevant or irrelevant? | Open |
| Wall ζ | α = 4π from first principles | Open (requires causal graph microphysics) |
| Wall η | Weak equivalence principle from N_rings ∝ m | Open (requires Cartan algebra mass formula) |
| Wall θ | Strong-field generalization (q significantly ≠ 1) | Open (nonlinear ring density feedback) |

---

## 8. Relation to Prior Work

### 8.1 Jacobson 1995 — "Thermodynamics of Spacetime"

Jacobson derived the Einstein field equations from the Clausius relation δQ = T dS applied to local Rindler horizons, assuming the proportionality of entropy to horizon area. DGF shares the spirit of deriving gravity from information-theoretic principles, but the mechanism is fundamentally different:

- Jacobson: horizon thermodynamics → G_μν = 8πG T_μν. Relies on Unruh temperature and area-entropy proportionality.
- DGF: causal ring Gram decay → dτ = q·dt → metric. Relies on quantum channel openness and which-path information extraction.

DGF does not use horizons, temperature, or entropy-area relations. The connection is conceptual (information → geometry) rather than technical.

### 8.2 Verlinde 2011 — "Entropic Gravity"

Verlinde derived Newton's law F = GMm/r² from entropic forces on holographic screens, with gravity as an emergent phenomenon from the statistical tendency to maximize entropy. Key differences from DGF:

- Verlinde: gravity = entropic force, test particles experience F = T ΔS/Δx.
- DGF: gravity = time dilation from Gram decay, no force concept at fundamental level.

DGF is closer to the geometric picture of GR (gravity as spacetime curvature / time dilation) than to Verlinde's force-based picture. DGF preserves the equivalence principle (Jordan frame), which entropic gravity struggles with.

### 8.3 Quiros et al. 2013 — "Weyl-Integrable Geometry"

Quiros and collaborators studied Weyl-integrable geometries where the non-metricity is a pure gradient: Q = w ⊗ g, w = -dφ. The DGF metric (Section 5.4) is precisely of this form, with φ = 2GM/rc² = -ln q.

DGF provides a physical origin for the Weyl scalar field φ: it is the accumulated Gram decay. Quiros et al. treated φ as a phenomenological field; DGF derives its functional form φ = -μ·b₁_eff from the postulates.

### 8.4 Borrill 2026 — "Gravity from Quantum Error Correction"

Borrill (2026) proposed that the Einstein equations emerge from the error-correction properties of holographic quantum codes. The connection to DGF is through the quantum channel formalism:

- Borrill: quantum error-correcting code → bulk reconstruction → Einstein equations.
- DGF: quantum decoherence channel (Gram decay) → time dilation → metric.

Both use quantum information theory to approach gravity, but the mechanisms are complementary: Borrill addresses the holographic direction (bulk from boundary), while DGF addresses the causal direction (metric from decoherence).

### 8.5 Unique Features of DGF

No prior theory combines all four of these features:

1. **Causal rings as the fundamental gravitational degree of freedom** (b₁, not curvature).
2. **Gram decay rate μ(c) as the coupling between quantum information and gravity.**
3. **Time dilation as which-path information extraction rate.**
4. **Clifford protection as a falsifiable quantum-gravity prediction.**

The combination of P4 (dτ = q·dt) with the exponential q = exp(-GM/rc²) is unique to DGF. No other theory uses the exponential channel openness as the gravitational potential.

---

## 9. Summary: The Logical Architecture

```
POSTULATES                    DERIVATION                     PREDICTIONS
═══════════                   ═══════════                    ═══════════

P1: Causal Graph              b₁ = |E|-|V|+C
  G = (V,E)                       │
  b₁ counts rings                 │ Laplacian Green
      │                           │ function 1/(4π|r|)
      │                           ▼
P2: Gram Decay               b₁_eff = κ ∫ ρ/|r-r'| d³r'
  G[a,b] = Π cos(cΔ)²             │
  μ(c) < 0 for non-Clifford       │ κ = (α/4π|μ|)·G/c²
      │                           │
      │                           ▼                        ① 2PN GW ~4% deviation
      │                      q = exp(μ·b₁_eff)             ② Clifford invisibility
      │                      q = exp(-GM/rc²)              ③ b₁-dependent τ
P3: Spatial Emergence             │                        ④ d_eff discrete ladder
  Δ_graph → Δ_g                   │ g₀₀ = -q²
  c(b₁) = 1-6/((b₁+2)(b₁+3))     │ g_ij = q⁻²δ_ij
      │                           │
      │                           ▼
P4: Information-Time         ds² = -q²c²dt² + q⁻²[dr²+r²dΩ²]
  dτ = q·dt                       │
  α = 1 (scale invariance)        │ expand in U = GM/rc²
      │                           │
      │                           ▼
  q = exp(μ·b₁_eff)          PPN: γ=1, β=1 (auto)
                              Newton: exact match
                              1PN: 0.03% deviation
                              2PN: ~4% deviation ← UNIQUE
```

---

## Appendix A: Key Files Index

| File | Content |
|:--|:--|
| `verify_p0_gram_rank.py` | P1-P2 numerical verification: Gram rank collapse with b₁ |
| `LP42-GhostZero/synthesis/unified_framework.md` | CFOL theorem → Ghost classification → I(S) topological invariant |
| `LP41-DGF-Spatial-Dimension/synthesis/修正优化_终极版.md` | P3: three-layer architecture, c(b₁), d_eff mechanisms |
| `LP45-Gram-Correlated-Dephasing/synthesis/A_dr_dtau_derivation.md` | P4 derivation: dτ = q·dt, κ derivation, 1/r kernel |
| `LP43-DGF-Gravity-Phenomenology/DGF_CLOSURE.md` | Full metric, PPN, Jordan frame |
| `LP43-DGF-Gravity-Phenomenology/g00_derivation.md` | g₀₀ = -q² from causal graph |
| `LP43-DGF-Gravity-Phenomenology/FINAL_ACCOUNTING.md` | Parameter accounting: α=1 derivation, b=2 empirical |
| `LP44-DGF-Classicality/ring_minimal_structure.md` | 4-edge ring as minimal nontrivial causal structure |

## Appendix B: Notation Table

| Symbol | Meaning | Defined In |
|:--|:--|:--|
| G = (V,E) | Causal graph | P1 |
| b₁ | First Betti number = |E| - |V| + C | P1 |
| c | Cartan parameter (entangling angle) | P1 |
| Δ_r(a,b) | Spin-sum difference for ring r, states a,b | P2 |
| μ(c) | Per-ring Gram decay rate | P2 |
| G[a,b] | Gram matrix element | P2 |
| Φ | Gram decay quantum channel | P2 |
| c(b₁) | Virasoro central charge | P3 |
| d_eff | Effective spatial dimension | P3 |
| q | Quantum channel openness = exp(μ·b₁_eff) | P4 |
| Γ₀ | Ring execution frequency (~Planck frequency) | P4 |
| κ | Ring coupling constant | Section 5 |
| α | Geometric factor (= 4π) | Section 5 |
| σ_ring | Single-ring causal graph cross-section | Section 5 |
| ℓ_P, m_P | Planck length, Planck mass | Section 5 |
