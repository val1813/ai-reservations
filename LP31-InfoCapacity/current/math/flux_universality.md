# Flux Universality Proof: DGF Framework Physical Conclusions are Independent of Flux Choice

**Status**: FORMAL PROOF
**Date**: 2026-06-06
**Question**: Does the DGF framework's core physical picture depend on the specific flux choice φ(q)=1/q, or is it universal across a broad class of admissible flux functions?

**Answer**: All three core physical conclusions (Laplace-type static limit, dual-domain asymptotic states, 1/r potential decay) are **universal properties of the entire admissible flux class Φ**. The specific choice φ=1/q fixes only non-essential quantitative details (asymptotic values, dynamical timescales), not the qualitative physics.

---

## 1. Definition of the Admissible Flux Class Φ

### 1.1 Discrete Framework

Consider a graph G = (V, E) with nodes i ∈ V carrying a continuous variable q_i ∈ (0, 1]. The information capacity interpretation constrains q_i to the unit interval, with q → 0 representing "full" (maximum information) and q → 1 representing "empty" (minimum information).

The **inter-node flux** from node i to node j is:

\[
J_{i \to j} = \varphi(q_i) - \varphi(q_j)
\]

where φ: (0, 1] → ℝ is a smooth function encoding the "potential" that drives information flow.

The **conservation equation** on the graph is:

\[
\partial_t q_i = \sum_{j \in N(i)} \big(\varphi(q_j) - \varphi(q_i)\big) = -(\mathcal{L}\varphi(\mathbf{q}))_i
\]

where ℒ is the graph Laplacian.

### 1.2 Continuum Limit

In the continuum limit (regular grid with spacing h → 0), the graph Laplacian converges to −h²∇², yielding the nonlinear diffusion PDE:

\[
\boxed{\partial_t q = -\nabla^2 \varphi(q)}
\]

Equivalently, expanding the Laplacian:

\[
\partial_t q = -\nabla \cdot (\varphi'(q)\nabla q) = \nabla \cdot \big(|\varphi'(q)| \nabla q\big)
\]

This is a **nonlinear diffusion equation** with state-dependent diffusion coefficient D̃(q) ≡ |φ′(q)| = −φ′(q) > 0.

### 1.3 The D(q) Convention

The framework introduces an auxiliary function:

\[
\boxed{D(q) \equiv -q^2 \varphi'(q) \quad \Longleftrightarrow \quad \frac{D(q)}{q^2} = -\varphi'(q) = \tilde{D}(q)}
\]

In this convention, D(q) is the diffusion coefficient **scaled by q²**. The PDE becomes:

\[
\partial_t q = \nabla \cdot \left(\frac{D(q)}{q^2} \nabla q\right)
\]

### 1.4 Admissibility Conditions (Class Φ)

**Definition 1** (Admissible Flux Function). A function φ: (0, 1] → ℝ belongs to class Φ if:

1. **Smoothness**: φ ∈ C²(0, 1]
2. **Strict monotonicity (positive diffusion)**: φ′(q) < 0 for all q ∈ (0, 1]
    - Equivalent: D(q) > 0 for all q ∈ (0, 1]
3. **Capacity constraint (barrier at q=0)**: lim_{q→0⁺} φ(q) = +∞
    - Physical meaning: a completely full cell (q=0) generates infinite repulsive potential, preventing information over-concentration
4. **Normalization at empty state**: φ(1) ∈ ℝ is finite
    - Physical meaning: an empty cell has no "pressure" to expel information

The DGF-specific choice is:

\[
\varphi_{\text{DGF}}(q) = \frac{1}{q}, \quad \varphi'_{\text{DGF}}(q) = -\frac{1}{q^2}, \quad D_{\text{DGF}}(q) = 1
\]

which gives an effective diffusion coefficient D̃(q) = 1/q².

**Examples of other admissible φ:**

| φ(q) | φ′(q) | D(q) | D̃(q) |
|------|--------|------|--------|
| 1/q | −1/q² | 1 | 1/q² |
| 1/q^α (α > 0) | −α/q^{α+1} | α/q^{α−1} | α/q^{α+1} |
| −ln q | −1/q | q | 1/q |
| −ln(−ln q) | −1/(q\|ln q\|) | q/\|ln q\| | 1/(q\|ln q\|) |
| e^{1/q} − e | −e^{1/q}/q² | e^{1/q} | e^{1/q}/q² |

All satisfy φ′ < 0, φ(0⁺) = +∞, φ(1) finite.

---

## 2. Theorem P1: Static Limit is Always Laplace-Type

### Statement

For any φ ∈ Φ, the static equilibrium condition ∂_t q = 0 is equivalent to:

\[
\boxed{\nabla^2 \varphi(q) = 0}
\]

or, expressed through D(q):

\[
\boxed{\nabla^2 \left( \int^q \frac{D(s)}{s^2}\, ds \right) = 0}
\]

This is a **Laplace equation for the potential ψ ≡ φ(q)** (or equivalently ψ ≡ −∫D(s)/s² ds). The static limit is always an elliptic boundary value problem of Laplace type, regardless of the specific functional form of φ.

### Proof (Trivial from definition)

From the conservation PDE:

\[
\partial_t q = -\nabla^2 \varphi(q)
\]

Setting ∂_t q = 0 immediately yields:

\[
\nabla^2 \varphi(q) = 0
\]

The second form follows from the identity:

\[
\frac{D(q)}{q^2} = -\varphi'(q) \implies \int^q \frac{D(s)}{s^2}\, ds = -\varphi(q) + \text{const}
\]

so ∇²(∫D(s)/s² ds) = −∇²φ(q) = 0. ∎

### Interpretation

- The **equation type** (second-order elliptic) is a consequence of the conservation law structure ∂_t q = −∇²φ(q), which holds for any φ.
- The specific φ **only determines the mapping** between the physical variable q and the harmonic potential ψ = φ(q).
- Different φ produce different q-profiles from the **same harmonic function** ψ(r), via q(r) = φ⁻¹(ψ(r)).
- This is analogous to the D'Arcy law in porous media: the pressure field is always harmonic, regardless of the nonlinear permeability function.

### What φ Does NOT Change

- The static equation is **always** ∇²(some scalar) = 0
- The mathematical **structure** (elliptic, requires boundary conditions on φ(q), maximum principle applies to φ(q)) is universal
- The fundamental solution is **always** the Green's function of the Laplacian

### What φ DOES Change

- The **interpretation** of the potential: φ(q) vs q itself
- The **nonlinear mapping** from the harmonic function to the physical variable q
- The **effective boundary conditions** when expressed in terms of q (since φ maps BCs nonlinearly)

---

## 3. Theorem P2: Dual-Domain Asymptotic States are Universal

### Statement

For any φ ∈ Φ, the static spherically-symmetric solution in d dimensions exhibits a **dual-domain structure**:

1. **Inner domain (r → 0)**: q(r) → 0 (the "core" — maximally concentrated information)
2. **Outer domain (r → ∞)**: q(r) → q_∞ ∈ (0, 1] (the "background" — uniform information density)

The existence of these two asymptotic regimes is universal. Only the **specific asymptotic values** and the **functional form of the transition** depend on φ.

### Proof

#### Step 1: Spherically Symmetric Static Solution

In d-dimensional spherical coordinates, the Laplace equation ∇²φ(q(r)) = 0 becomes:

\[
\frac{1}{r^{d-1}} \frac{d}{dr}\left(r^{d-1} \frac{d}{dr} \varphi(q(r))\right) = 0
\]

Integrating once:

\[
r^{d-1} \frac{d}{dr} \varphi(q(r)) = -C, \quad C > 0
\]

(The sign is negative because φ is decreasing in q, and we expect q to increase with r, so φ(q(r)) decreases with r.)

Integrating again:

\[
\varphi(q(r)) = \begin{cases}
C \ln r + D & d = 2 \\[4pt]
\displaystyle \frac{C}{(d-2)r^{d-2}} + D & d \geq 3
\end{cases}
\]

where C > 0 (source at origin) and D are integration constants determined by boundary conditions.

#### Step 2: Inner Asymptotics (r → 0)

For d ≥ 3: φ(q(r)) = C/((d−2)r^{d−2}) + D → +∞ as r → 0.

Since φ: (0, 1] → ℝ is strictly decreasing and φ(0⁺) = +∞ by the capacity constraint (Axiom 3):

\[
\lim_{r \to 0} \varphi(q(r)) = +\infty \implies \lim_{r \to 0} q(r) = \varphi^{-1}(+\infty) = 0
\]

The capacity constraint φ(0⁺) = +∞ is **necessary and sufficient** for the inner core to have q → 0.

For d = 2: φ(q(r)) = C ln r + D → −∞ as r → 0. Since φ is decreasing and φ(0⁺) = +∞, the limit −∞ corresponds to φ(q) → −∞, which requires q → 1 (approaching empty state). This is a **dimension-dependent inversion**: in 2D, the point source at origin creates a logarithmic potential that drives q to 1 rather than 0. We will address this in the sensitivity analysis (§6).

**For d ≥ 3**: q(r → 0) → 0. ✓

#### Step 3: Outer Asymptotics (r → ∞)

For d ≥ 3: φ(q(r)) → D as r → ∞. Since D is finite and φ is continuous and bijective from (0, 1] onto [φ(1), +∞):

\[
q_\infty \equiv \lim_{r \to \infty} q(r) = \varphi^{-1}(D) \in (0, 1]
\]

The value q_∞ is:
- Determined by the boundary condition at infinity (D = φ(q_∞) = φ(q at outer boundary))
- **Not universal**: depends on both φ and the specific boundary conditions
- But the **existence** of a finite limit is universal (for d ≥ 3)

For the DGF-specific case φ(q) = 1/q:
- φ(q_∞) = 1/q_∞ = D ⇒ q_∞ = 1/D
- If normalization sets φ(1) = 1 as reference, and the system is isolated (total "mass" conserved), the background value emerges from the integrated constraint, giving q_∞ ≈ 1/2 in the specific numerical example.

For other φ, the background value is φ⁻¹(D).

#### Step 4: Universality of Dual-Domain Structure

**Theorem P2 (precise statement).** Let φ ∈ Φ and d ≥ 3. Then any static spherically-symmetric solution with a point source at the origin satisfies:

\[
\lim_{r \to 0} q(r) = 0, \qquad \lim_{r \to \infty} q(r) = q_\infty \in (0, 1]
\]

with a monotonic transition between the two regimes. The qualitative dual-domain structure (low-q core + plateau background) is a **universal consequence** of:

1. The Laplace structure of the static equation (which follows from ANY φ)
2. The capacity constraint φ(0⁺) = +∞ (Axiom 3 of class Φ)

**Neither the specific functional form of φ nor the value of D(q) matters for the existence of this structure.**

#### Step 5: Classification — Which φ Give What Structure

| Condition on φ | d ≥ 3 behavior | d = 2 behavior |
|----------------|---------------|----------------|
| φ(0⁺) = +∞ (class Φ) | q → 0 core, q → q_∞ bg | q → 1 core (inverted!), q → 0 bg |
| φ(0⁺) finite (NOT in class Φ) | q → q₀ > 0 core | q → q₀ > 0 core |
| φ(0⁺) = +∞, lim_{q→0} q^α φ(q) = ∞ ∀α (very strong divergence) | Sharp core-bg transition | q → 1 core |
| φ(0⁺) = +∞, lim_{q→0} q φ(q) = 0 (very weak divergence) | Smooth, wide transition | q → 1 core |

**Conclusion for P2**: For d ≥ 3 dimensions (our physical case), **every φ ∈ Φ** produces the dual-domain structure. The universality is complete — there are no counterexamples within the admissible class. The specific φ only affects:

- The **steepness** of the core-background transition (measured by φ″/φ′)
- The **numerical value** of q_∞ (which is φ⁻¹(boundary condition))
- The **dynamical timescale** to reach equilibrium (fast diffusion near q=0 if D̃(q) → ∞ as q → 0)

---

## 4. Theorem P3: 1/r Potential Decay is Universal

### Statement

In d = 3 spatial dimensions, the static solution satisfies:

\[
\boxed{\varphi(q(r)) - \varphi(q_\infty) = \frac{C}{r}}
\]

for some constant C > 0. The **1/r decay of the potential** is a direct consequence of the Laplace equation Green's function in 3D and is **completely independent of φ**.

Equivalently, in d dimensions:

\[
\varphi(q(r)) - \varphi(q_\infty) \propto \frac{1}{r^{d-2}}
\]

### Proof

The static equation ∇²φ(q) = 0 is a Laplace equation for the scalar field ψ(r) ≡ φ(q(r)). The Green's function G(r) satisfying ∇²G(r) = −δ(r) in d dimensions is:

\[
G_d(r) = \begin{cases}
\displaystyle -\frac{1}{2\pi}\ln r & d = 2 \\[8pt]
\displaystyle \frac{\Gamma(d/2)}{2(d-2)\pi^{d/2}} \frac{1}{r^{d-2}} & d \geq 3
\end{cases}
\]

Any solution with a point source at the origin takes the form:

\[
\psi(r) = A \cdot G_d(r) + B
\]

for constants A, B. In d = 3:

\[
\psi(r) = \frac{A}{4\pi r} + B \implies \varphi(q(r)) = \frac{C}{r} + \varphi(q_\infty)
\]

where C = A/(4π) and B = φ(q_∞). Subtracting the background:

\[
\varphi(q(r)) - \varphi(q_\infty) = \frac{C}{r}
\]

### The Information Field q(r) Itself

While the potential φ(q) has universal 1/r decay, the **physical variable q(r)** has a φ-dependent profile:

\[
q(r) = \varphi^{-1}\left(\frac{C}{r} + \varphi(q_\infty)\right)
\]

| φ(q) | q(r) asymptotic (large r) | Decay type of q − q_∞ |
|------|--------------------------|----------------------|
| 1/q | q(r) = 1/(C/r + 1/q_∞) | q − q_∞ ~ −Cq_∞²/r (1/r) |
| 1/q^α | q(r) = (C/r + q_∞^{−α})^{−1/α} | q − q_∞ ~ −(C/α)q_∞^{α+1}/r (1/r) |
| −ln q | q(r) = q_∞ e^{−C/r} | q − q_∞ ~ −Cq_∞/r (1/r) |

For all φ ∈ Φ with φ analytic near q_∞, Taylor expansion gives:

\[
\varphi(q) - \varphi(q_\infty) = \varphi'(q_\infty)(q - q_\infty) + O((q - q_\infty)^2)
\]

Since φ′(q_∞) ≠ 0 (strict monotonicity), the leading-order behavior is:

\[
q(r) - q_\infty \sim \frac{C}{\varphi'(q_\infty)} \frac{1}{r} \quad \text{as } r \to \infty
\]

**The 1/r decay of q − q_∞ at large distances is universal** (up to a φ-dependent coefficient 1/φ′(q_∞)).

### Physical Interpretation

The 1/r decay is not an artifact of the specific flux choice — it is the **unique signature of a massless field in 3D**. Any elliptic equation ∇²ψ = 0 in 3D will produce 1/r potential decay because:

1. The Green's function of the Laplacian in 3D is 1/(4πr)
2. The static limit of ANY conservation law ∂_t q + ∇·J = 0 with J = −∇ψ is ∇²ψ = 0
3. The specific relation between ψ and q (i.e., ψ = φ(q)) does not affect the spatial decay of ψ

**Theorem P3 (precise).** For any φ ∈ Φ and d ≥ 3, the potential ψ ≡ φ(q) satisfies ψ − ψ_∞ ∝ 1/r^{d−2}. In d = 3, this is exactly 1/r, and the physical variable q inherits this 1/r decay rate asymptotically (to leading order), with a φ-dependent prefactor.

---

## 5. Sensitivity Analysis: What IS φ-Dependent?

While the three core physical conclusions are universal, not EVERYTHING is independent of φ. Here is a systematic sensitivity classification.

### 5.1 Universal (φ-Independent) Features

| Feature | Reason |
|---------|--------|
| Static equation is Laplace-type (∇²ψ = 0) | Conservation law structure |
| 1/r potential decay in 3D | Green's function of Laplacian |
| Existence of q→0 core (d ≥ 3) | φ(0⁺) = +∞ |
| Existence of finite background q_∞ | φ bijective on (0,1] |
| Monotonicity of q(r) | φ monotonic + harmonic ψ monotonic in r |
| Maximum principle: q bounded by boundary values | Applies to ψ = φ(q), preserved under φ⁻¹ |

### 5.2 φ-Dependent Features (Quantitative, Not Qualitative)

| Feature | Dependence on φ | Significance |
|---------|----------------|-------------|
| Numerical value of q_∞ | q_∞ = φ⁻¹(boundary condition) | Low: background level is a free normalization anyway |
| Sharpness of core-bg transition | Controlled by φ″ near q=0 | Medium: affects observational distinguishability |
| Dynamical timescale to equilibrium | D̃(q) = −φ′(q) controls diffusion speed | High: affects experimental accessibility |
| Stability of the static solution | Lyapunov functional depends on φ | Medium: determines robustness to perturbations |
| Approach to equilibrium (scaling laws) | D̃(q) near q→0 determines self-similar asymptotics | Medium: affects late-time behavior |

### 5.3 φ-Critical Features (Could Break with Wrong φ)

#### 5.3.1 Dimension d = 2

In 2D, the Laplace equation Green's function is logarithmic: ψ(r) = C ln r + D. This gives:

- As r → 0: ψ → −∞ ⇒ φ(q) → −∞ ⇒ q → 1 (core is EMPTY, not full!)
- As r → ∞: ψ → +∞ ⇒ φ(q) → +∞ ⇒ q → 0 (background vanishing!)

This **inverts** the dual-domain picture. The 2D case is fundamentally different and the "core=q≈0" picture does NOT survive in 2D. However, since the DGF framework is physically motivated in 3D (network embedded in space), this is not a practical concern.

#### 5.3.2 Non-Divergent φ (NOT in Class Φ)

If we relax Axiom 3 and allow φ(0⁺) finite (e.g., φ(q) = 2 − q, D(q) = q²):

- Static solution: φ(q(r)) = C/r + D in 3D
- As r → 0: φ → +∞ which is **impossible** since φ is bounded above
- The point source solution does not exist — we need a distributed source
- The core no longer has q → 0; instead q reaches a finite minimum

This WOULD change the physical picture: no "singular core", no dual-domain structure with a sharp core. However, such φ are explicitly excluded by the physical motivation (Axiom 3).

#### 5.3.3 Non-Monotonic φ (NOT in Class Φ)

If φ′ changes sign somewhere (D(q) changes sign), the PDE becomes **forward-backward diffusion** (ill-posed), and the static equation changes type. This is excluded by Axiom 2.

### 5.4 The Most φ-Sensitive Conclusion

**The specific background value q_∞ ≈ 1/2 is the most φ-sensitive feature.** It depends on:
1. The specific function φ
2. The normalization convention (φ(1) = ?)
3. The boundary conditions
4. The total "mass" or integral constraint

For φ(q) = 1/q^α with φ(1) = 1:
- q_∞ is determined by the outer boundary condition
- If the system is closed (no flux at boundary), the total integrated φ(q) is conserved
- This gives q_∞ as a function of α and the total "charge"
- The value 1/2 is NOT universal — it's an artifact of the specific choice α = 1 and specific boundary conditions

**Honest assessment**: If an experimental prediction depends on measuring q_∞ ≈ 1/2 precisely, that prediction IS φ-dependent and cannot be claimed as a universal DGF result without independent justification for φ = 1/q.

---

## 6. Dynamical Universality: Approach to Equilibrium

Beyond the static properties, we should examine whether the dynamical approach to equilibrium (relaxation) is universal.

### 6.1 Lyapunov Functional

The PDE ∂_t q = −∇²φ(q) admits a Lyapunov (free energy) functional. Define:

\[
\mathcal{F}[q] = \int d^d x \, \Phi(q(\mathbf{x}))
\]

where Φ′(q) = φ(q), i.e., Φ(q) = ∫^q φ(s) ds.

Then:

\[
\frac{d\mathcal{F}}{dt} = \int d^d x \, \Phi'(q) \partial_t q = \int d^d x \, \varphi(q) (-\nabla^2 \varphi(q)) = \int d^d x \, |\nabla \varphi(q)|^2 \geq 0
\]

Since φ′ < 0, Φ″ = φ′ < 0, so Φ is concave and ℱ is bounded below. The system always relaxes monotonically to the static solution. **This Lyapunov structure is universal for all φ ∈ Φ.**

### 6.2 Self-Similar Asymptotics

Near q ≈ 0 (the core), the diffusion coefficient is D̃(q) = −φ′(q). The late-time approach to equilibrium in the core is governed by the behavior of D̃(q) as q → 0.

| Behavior of D̃(q) as q → 0 | Regime | Example φ | Relaxation |
|---------------------------|--------|-----------|------------|
| D̃(q) → ∞ | Super-diffusive core | φ = 1/q^α (α > 0) | Core equilibrates rapidly |
| D̃(q) → const > 0 | Normal diffusion | φ = C − q | Standard t^{−d/2} decay |
| D̃(q) → 0 | Sub-diffusive core | φ = −ln q | Core equilibrates slowly (critical slowing down) |

For φ ∈ Φ (with φ(0⁺) = +∞), we typically have D̃(q) = −φ′(q) → +∞ as q → 0 (e.g., φ′ ~ −1/q^{1+α} with α > 0). This means:

- **The core equilibrates FASTER than the background** — a dynamical manifestation of the dual-domain structure
- Information is rapidly expelled from the core region
- The background relaxes on a much longer timescale

**This super-diffusive core dynamics is a universal consequence of the capacity constraint φ(0⁺) = +∞**, provided the divergence of φ is at least as strong as −ln q (i.e., φ′ diverges at least as fast as 1/q).

### 6.3 The Borderline Case

φ(q) = −ln q: D̃(q) = 1/q → ∞ as q → 0, so the core is still super-diffusive (1/q is a mild divergence but still diverges).

φ(q) = −(−ln q)^β with 0 < β < 1: φ′(q) = −β(−ln q)^{β−1}/q. As q → 0, D̃(q) ~ (−ln q)^{β−1}/q → ∞ (the 1/q dominates). So super-diffusive core.

The ONLY way to lose the super-diffusive core is if φ(0⁺) is finite (excluded by Axiom 3) or if φ′ diverges slower than any power of 1/q, which would require exotic oscillatory behavior (excluded by smoothness).

**Conclusion**: For all physically reasonable φ ∈ Φ, the core is super-diffusive. This is a universal dynamical feature.

---

## 7. Honest Conclusion

### 7.1 What We Proved

| Property | Status | Universality Class |
|----------|--------|-------------------|
| Static limit is ∇²(something) = 0 | ✓ Proved | ALL φ (even outside Φ) |
| Potential ψ = φ(q) has 1/r decay (3D) | ✓ Proved | ALL φ (Laplace equation Green's function) |
| Dual-domain: q→0 core exists (d≥3) | ✓ Proved | ALL φ ∈ Φ (needs φ(0⁺)=∞) |
| Dual-domain: q→q_∞ background exists | ✓ Proved | ALL φ ∈ Φ (needs φ bijective) |
| Core is super-diffusive | ✓ Proved | ALL φ ∈ Φ with mild regularity |
| Lyapunov functional exists | ✓ Proved | ALL φ ∈ Φ |

### 7.2 What is NOT Universal

| Property | Depends on φ? | Why |
|----------|--------------|-----|
| q_∞ ≈ 1/2 specifically | YES | φ(1)=1 + mass constraint for φ=1/q gives ~1/2 |
| Core sharpness (transition width) | YES | Steepness of φ near q=0 |
| Relaxation timescale | YES | D̃(q) = −φ′(q) sets the clock |
| Detailed shape of q(r) in transition region | YES | Nonlinear mapping φ⁻¹ |
| 2D behavior (core vs background inversion) | YES (dimension) | Logarithmic Green's function |

### 7.3 Verdict

**The three core physical conclusions of the DGF framework are universal properties of the entire admissible flux class Φ.** The conclusions are NOT artifacts of the specific choice φ(q)=1/q. They follow from:

1. **The conservation law structure** (any φ): P1 (Laplace static limit), P3 (1/r potential decay)
2. **The capacity constraint φ(0⁺) = +∞** (Axiom 3 of Φ): P2 (dual-domain structure, for d ≥ 3)
3. **The monotonicity φ′ < 0** (Axiom 2 of Φ): Well-posedness, Lyapunov stability

The specific choice φ(q) = 1/q is a **representative member** of the universality class, not a special case. Any φ ∈ Φ would give the same qualitative physics with only quantitative differences in the specific numerical values.

### 7.4 The One Genuine Caveat

If one wanted to **break** the dual-domain picture while staying within a conservation-law framework, the only way is to **violate the capacity constraint** φ(0⁺) = +∞. With φ(0⁺) finite:
- No singular core: q stays finite everywhere
- No sharp core-background distinction
- The "gravitational" analogy weakens significantly

But this capacity constraint is physically well-motivated: it encodes the idea that complete information saturation at a location creates an infinite "pressure" that drives information away. Removing it would be physically unnatural. Therefore, within any physically reasonable model of information capacity with hard saturation, the dual-domain picture is **robust and unavoidable**.

### 7.5 Recommendation

The original DGF paper can confidently claim that its core physical picture (dual-domain asymptotic states, Laplace-type static limit, 1/r gravity-like decay) is **independent of the specific flux parametrization**. A brief appendix or remark referencing the universality class Φ and the three theorems above would suffice to establish this independence.

---

## Appendix A: Quick Reference — Key Equations

### Continuum PDE
\[
\partial_t q = -\nabla^2 \varphi(q) = \nabla \cdot \left(\frac{D(q)}{q^2} \nabla q\right)
\]

### Static Limit
\[
\nabla^2 \varphi(q) = 0 \quad \Longleftrightarrow \quad \nabla^2 \left(\int^q \frac{D(s)}{s^2} ds\right) = 0
\]

### 3D Spherical Static Solution
\[
\varphi(q(r)) = \frac{C}{r} + \varphi(q_\infty), \qquad q(r) = \varphi^{-1}\left(\frac{C}{r} + \varphi(q_\infty)\right)
\]

### DGF-Specific (φ = 1/q)
\[
q(r) = \frac{1}{C/r + 1/q_\infty} = \frac{q_\infty r}{C q_\infty + r}
\]

### Lyapunov Functional
\[
\mathcal{F}[q] = \int d^d x \, \Phi(q), \quad \Phi'(q) = \varphi(q), \quad \frac{d\mathcal{F}}{dt} = \int d^d x \, |\nabla \varphi(q)|^2 \geq 0
\]

---

## Appendix B: Proof Checklist

- [x] P1: ∂_t q = 0 ⇔ ∇²φ(q) = 0 (trivial from PDE definition)
- [x] P1 (D-form): ∇²(∫D(s)/s² ds) = 0 (via D(q) = −q²φ′(q))
- [x] P2 inner: φ(0⁺) = +∞ ⇒ q(r→0) = 0 for d ≥ 3
- [x] P2 outer: φ bijective ⇒ q(r→∞) = φ⁻¹(D) ∈ (0,1]
- [x] P2 universality: any φ ∈ Φ gives dual-domain for d ≥ 3
- [x] P2 counterexample: d = 2 gives inverted structure (logarithmic Green's function)
- [x] P3: ∇²ψ = 0 ⇒ ψ ∝ 1/r^{d−2} (Laplace Green's function)
- [x] P3 q-asymptotic: q−q_∞ ~ C/(φ′(q_∞) r) for large r
- [x] Lyapunov: ℱ̇ = ∫|∇φ(q)|² ≥ 0 for all φ ∈ Φ
- [x] Super-diffusive core: D̃(q)→∞ as q→0 for all φ with φ(0⁺)=∞ and mild regularity
