# Flux Form Classification Under A1+A2+A3 Constraints

## Minimal Assumption Analysis for Information Capacity Framework

**Date**: 2026-06-06
**Status**: Mathematical analysis — A5 decision pending

---

## 1. Function Space of Admissible Flux Forms

### 1.1 Setup and Conventions

Let $q_i \in [0,1]$ be the information occupancy of cell $i$. The flux $J_{i \to j}$ denotes the rate at which information flows **from** cell $i$ **to** cell $j$.

**Constraint C1** (Directionality): Information flows from lower $q$ to higher $q$:
$$J(q_i, q_j) > 0 \quad \text{when} \quad q_j > q_i$$

**Constraint C2** (Antisymmetry): Flux is antisymmetric:
$$J(q_i, q_j) = -J(q_j, q_i)$$

**Constraint C3** (Empty-cell divergence): The flux involving a nearly-empty cell must diverge, ensuring that cells at $q \to 0$ immediately receive or shed information to stay within $[0,1]$.

**Constraint C4** (Containment): The dynamics $\partial_t q_i = \sum_{j \in \mathcal{N}(i)} J_{j \to i}$ preserves $q_i \in [0,1]$.

### 1.2 Lemma: C1 + C2 + Irrotationality Implies Additive Form

**Claim.** Under C1, C2, and the additional assumption of **irrotationality** (zero circulation around any loop):
$$J(q_i, q_j) + J(q_j, q_k) + J(q_k, q_i) = 0 \quad \forall q_i, q_j, q_k \tag{IR}$$
the flux must take the additive form:
$$J(q_i, q_j) = F(q_j) - F(q_i) \tag{1}$$
where $F: [0,1] \to \mathbb{R}$ is a strictly monotone function.

**Proof.** Fix an arbitrary reference point $q_0 \in [0,1]$. Define $F(q) \equiv J(q_0, q)$. Then for any $q_i, q_j$:
$$J(q_i, q_j) = J(q_i, q_0) + J(q_0, q_j) \quad \text{(by (IR))}$$
$$= -J(q_0, q_i) + J(q_0, q_j) \quad \text{(by C2)}$$
$$= F(q_j) - F(q_i) \tag{2}$$

C1 requires $J(q_i, q_j) > 0$ when $q_j > q_i$, hence $F(q_j) > F(q_i)$ when $q_j > q_i$ — i.e., $F$ is **strictly increasing**. $\square$

**Remark on irrotationality.** Without (IR), C1+C2 alone admits the broader class:
$$J(q_i, q_j) = (q_j - q_i) \cdot H(q_i, q_j) \tag{3}$$
where $H(q_i, q_j) = H(q_j, q_i) > 0$ is any symmetric positive function. The additive form (1) corresponds to the special case $H(q_i, q_j) = \frac{F(q_j) - F(q_i)}{q_j - q_i}$ (i.e., the divided difference of $F$), which is guaranteed symmetric.

**Physical motivation for (IR).** In any physical system where the flux derives from a potential gradient, the circulation vanishes. The condition (IR) is the discrete analog of $\nabla \times \mathbf{J} = 0$ and is equivalent to the statement that $J$ is an **exact 1-form** on the space of configurations. We adopt (IR) as a minimal physical regularity condition — it says that there is no "information vortex" that would allow perpetual circulation around a triangle of cells. This is the weakest condition that collapses the general $H$-parametrized class to the additive form.

**Alternative view: (IR) as a naturalness condition.** The dynamics $dq_i/dt = \sum_j J_{j \to i}$ involves sums over neighbors. If $J$ is not exact, then the steady state $\sum_j J_{j \to i} = 0$ imposes constraints that depend on the graph topology in a non-universal way. Only when $J$ is exact does the steady-state condition factorize: $F(q_i) = \text{const}$ across all cells, i.e., **all cells reach the same $q$ at equilibrium**. This factorization is a strong physical desideratum — it says the equilibrium is independent of the lattice structure.

Henceforth we assume (IR) and work with the additive form (1), with $F$ strictly increasing.

### 1.3 Constraint C3 in Terms of $F$

C3 demands that $F(q)$ diverge as $q \to 0$. With $F$ increasing, this means:
$$\lim_{q \to 0^+} F(q) = -\infty \tag{4}$$

**Physical interpretation.** When $q_i \to 0$, $F(q_i) \to -\infty$, so $J_{i \to j} = F(q_j) - (-\infty) = +\infty$ — an empty cell **floods** its neighbors with whatever remnant information it carries. This acts as a repulsive barrier at $q=0$: no cell can stably approach zero occupancy without triggering a divergent restorative flux.

Equivalently, in the discrete integrate-and-fire picture: a cell with $q=0$ has zero "inertia" and any incoming flux immediately passes through. The divergence of $F$ at $q=0$ encodes this instantaneous transmission in the continuum limit.

### 1.4 Constraint C4 in Terms of $F$

The continuum dynamics (derived in Section 2) must preserve $q \in [0,1]$. This requires:
- $F$ is finite on $(0,1]$ (regular interior and upper boundary)
- The singularity structure of $F$ near $q=0$ must be such that the numerical time step $\Delta t \propto q_{\min}^2$ (adaptive) suffices to prevent violation of the lower bound
- $F$ must be $C^1$ on $(0,1)$ for the diffusion equation to be well-posed

**No constraint at $q=1$ from C4.** The upper bound is maintained by the dynamics of the $q=1$ cell spontaneously "firing" (overflow) — this is controlled by C1+C2, not by a singularity in $F$.

---

## 2. Continuum Limit and the Diffusion Function $D(q)$

### 2.1 Derivation

Consider a 1D lattice with spacing $h$. The flux from $i$ to $i+1$ is:
$$J_{i \to i+1} = F(q_{i+1}) - F(q_i)$$

The rate equation for cell $i$:
$$\frac{dq_i}{dt} = J_{i-1 \to i} + J_{i+1 \to i} = [F(q_i) - F(q_{i-1})] + [F(q_i) - F(q_{i+1})]$$

Wait — careful with indices. The flux **into** $i$ comes from neighbors:
$$\frac{dq_i}{dt} = J_{i-1 \to i} + J_{i+1 \to i}$$
$$= [F(q_i) - F(q_{i-1})] + [F(q_i) - F(q_{i+1})]$$
$$= 2F(q_i) - F(q_{i-1}) - F(q_{i+1})$$

Taylor expand $F(q_{i \pm 1})$ about $q_i$:
$$F(q_{i \pm 1}) = F(q_i) + F'(q_i)(q_{i \pm 1} - q_i) + \tfrac{1}{2}F''(q_i)(q_{i \pm 1} - q_i)^2 + O(h^3)$$

Using $q_{i \pm 1} - q_i = \pm h \partial_x q + \tfrac{1}{2}h^2 \partial_x^2 q + O(h^3)$:
$$F(q_{i \pm 1}) = F(q_i) \pm h F' q_x + \tfrac{1}{2}h^2(F' q_{xx} + F'' q_x^2) + O(h^3)$$

Summing:
$$F(q_{i-1}) + F(q_{i+1}) = 2F(q_i) + h^2(F' q_{xx} + F'' q_x^2) + O(h^3)$$

Therefore:
$$\frac{dq_i}{dt} = -h^2\left[F'(q_i)\partial_x^2 q + F''(q_i)(\partial_x q)^2\right] + O(h^3)$$
$$= -h^2 \partial_x\left[F'(q)\partial_x q\right]$$

Take the continuum limit $h \to 0$ with diffusive scaling $t \to \tau = h^2 t$:
$$\boxed{\frac{\partial q}{\partial \tau} = -\nabla \cdot [F'(q)\nabla q]} \tag{5}$$

### 2.2 Defining the Effective Diffusivity

Equation (5) is **anti-diffusive** when $F'(q) > 0$ (recall $F$ is increasing), because the standard diffusion equation is $\partial_t q = +\nabla \cdot (D\nabla q)$ with $D > 0$. The minus sign means that information **concentrates** rather than spreads — it flows **up** the $q$-gradient, consistent with C1 (low $q$ → high $q$).

Define the **positive effective diffusivity**:
$$\boxed{D(q) \equiv F'(q) > 0} \tag{6}$$

Then:
$$\frac{\partial q}{\partial \tau} = -\nabla \cdot [D(q)\nabla q] \tag{7}$$

Equation (7) is the **backward** heat equation with diffusion coefficient $D(q)$. It drives $q$ toward sharp gradients (pattern formation) rather than toward uniformity.

### 2.3 Note on Alternative Normalization

The problem statement uses $D(q) = -q^2 F'(q)$, which differs from (6) by factors of $q^2$ and a sign. This alternative normalization arises if one absorbs the lattice-dependent prefactors differently, or if the flux is defined with an additional $q$-dependent coupling (e.g., $J_{i \to j} = q_i q_j [F(q_j) - F(q_i)]$). The classification of $F$ families below is insensitive to this normalization choice — we work with $D(q) = F'(q)$ for clarity and note the conversion where relevant.

---

## 3. Classification of $F(q)$ Families

We now classify all functions $F: (0,1] \to \mathbb{R}$ satisfying:
1. **Strictly increasing**: $F'(q) > 0$ on $(0,1)$
2. **C3 divergence**: $\lim_{q \to 0^+} F(q) = -\infty$
3. **C4 regularity**: $F \in C^1(0,1)$, finite on $(0,1]$
4. **(IR) exact 1-form**: already encoded in the additive form

### 3.1 Family I: Power-Law (Inverse Monomial)

$$F(q) = -A q^{-\alpha} + B, \quad \alpha > 0, \quad A > 0 \tag{8}$$

**Properties:**
- $F'(q) = \alpha A q^{-\alpha-1} > 0$ ✓
- $\lim_{q \to 0^+} F(q) = -\infty$ ✓ (for any $\alpha > 0$)
- $D(q) = \alpha A q^{-\alpha-1}$ — diverges as $q \to 0$

**Sub-family $\alpha = 1$ (DGF):**
$$F(q) = -\frac{A}{q} + B, \quad D(q) = \frac{A}{q^2}$$
This is the **Dual Graviton Flux** (DGF) form. The divergence is $O(q^{-2})$ — the strongest among power-law families for a given $\alpha$.

**Conversion to problem's $D$ normalization**: The problem's $D_{\text{prob}}(q) = -q^2 F'(q) = -q^2(\alpha A q^{-\alpha-1}) = -\alpha A q^{1-\alpha}$. For this to be positive (as a diffusion coefficient should be), we need the minus sign absorbed, or the definition adjusted. Under the convention $F$ decreasing (as in the problem statement), $F(q) = A q^{-\alpha}$ (increasing alternative: $F(q) = -A q^{-\alpha}$), and $D_{\text{prob}} = \alpha A q^{1-\alpha}$. For $\alpha = 1$: $D_{\text{prob}} = A$ (constant).

### 3.2 Family II: Logarithmic

$$F(q) = A\log(q) + B, \quad A > 0 \tag{9}$$

**Properties:**
- $F'(q) = A/q > 0$ ✓ (strictly increasing)
- $\lim_{q \to 0^+} F(q) = -\infty$ ✓ (C3 satisfied)
- $F(1) = B$ (finite, regular at upper boundary) ✓
- $D(q) = F'(q) = A/q$ — diverges mildly as $q \to 0$

**Note on sign convention.** The naive form $F(q) = -A\log(q)$ with $A > 0$ gives $F'(q) = -A/q < 0$ (decreasing), which is excluded under our increasing-$F$ convention. However, $F(q) = +A\log(q)$ with $A > 0$ is correct: $\log(q) \to -\infty$ as $q \to 0^+$, and a positive coefficient $A$ ensures $F$ is increasing from $-\infty$ upward. The crucial point is that $\log(q)$ is negative on $(0,1)$, so multiplying by a POSITIVE coefficient sends it to $-\infty$ at $q=0$ while maintaining an increasing profile.

**Physical flux.** $J_{i \to j} = A\log(q_j/q_i)$. This is the **log-ratio flux**: the flow is proportional to the logarithm of the occupancy ratio. For $q_j > q_i$, $\log(q_j/q_i) > 0$ ✓.

**This is a valid family.** It has the mildest possible divergence at $q=0$ ($D \sim 1/q$) among all families satisfying C3. Whether this mildness is physically correct or insufficient depends on the microscopic firing mechanism.

(Under the problem's decreasing-$F$ convention: $F(q) = -A\log(q)$ with $A > 0$, giving $F'(q) = -A/q < 0$, $F(0^+) = +\infty$. The two conventions are related by $F_{\text{this}} = -F_{\text{problem}}$.)

### 3.3 Family III: Osmotic Pressure (Rational)

$$F(q) = A\frac{1-q}{q} + B, \quad A > 0 \tag{10}$$

**Properties:**
- $F'(q) = -A/q^2 < 0$ — decreasing, not increasing
- To make it increasing: $F(q) = -A(1-q)/q + B$, then $F'(q) = A/q^2 > 0$

But $F(q) = -A(1-q)/q + B = -A/q + A + B$. As $q \to 0^+$, $F \to -\infty$ ✓. As $q \to 1$, $F \to -A + A + B = B$. Regular at upper boundary ✓.

This is **identical to the power-law family with $\alpha = 1$** up to an additive constant! The $(1-q)$ factor cancels:
$$-A\frac{1-q}{q} + B = -\frac{A}{q} + A + B = -\frac{A}{q} + B'$$

So Family III with increasing $F$ **reduces to Family I with $\alpha = 1$ (DGF)**.

### 3.4 Family IV: Entropy Gradient (Logit Family)

$$F(q) = A\log\left(\frac{q}{1-q}\right) + B, \quad A > 0 \tag{11}$$

**Properties:**
- $F'(q) = A\left(\frac{1}{q} + \frac{1}{1-q}\right) = \frac{A}{q(1-q)} > 0$ ✓
- $\lim_{q \to 0^+} F(q) = -\infty$ ✓
- $\lim_{q \to 1^-} F(q) = +\infty$ — divergence at both ends!
- $D(q) = \frac{A}{q(1-q)}$ — symmetric under $q \leftrightarrow 1-q$

**Physical interpretation.** $F(q)$ is the **chemical potential** of a binary system with entropy $S(q) = -q\log q - (1-q)\log(1-q)$. Indeed, $\partial S/\partial q = \log((1-q)/q) = -F(q)/A$. The flux is proportional to the **entropy gradient**, the most fundamental driving force in statistical mechanics.

**Key difference from DGF.** The logit family diverges at **both** boundaries ($q=0$ and $q=1$), encoding equal resistance to both emptying and filling. The DGF family diverges only at $q=0$ and is regular at $q=1$. This makes qualitatively different predictions for the dynamics near saturation.

### 3.5 Family V: Generalized Power-Law with Saturation

$$F(q) = -A q^{-\alpha}(1-q)^\beta + B, \quad \alpha > 0, \quad \beta \geq 0, \quad A > 0 \tag{12}$$

Wait, with the minus sign this is increasing? Let's check:
$$F'(q) = -A[-\alpha q^{-\alpha-1}(1-q)^\beta + \beta q^{-\alpha}(1-q)^{\beta-1}(-1)]$$
$$= A[\alpha q^{-\alpha-1}(1-q)^\beta + \beta q^{-\alpha}(1-q)^{\beta-1}] > 0 \quad \text{for } q \in (0,1)$$

✓ Increasing. As $q \to 0^+$: $F \to -\infty$ (if $\alpha > 0$) ✓.

Special sub-cases:
- $\beta = 0$: **DGF** ($F \propto -q^{-\alpha}$)
- $\beta = 1$: $F(q) = -A q^{-\alpha}(1-q) + B = -A q^{-\alpha} + A q^{1-\alpha} + B$
- $\alpha = 1, \beta = 1$: $F(q) = -A(1-q)/q + B$ — already shown to reduce to DGF

### 3.6 Family VI: Exotic (Non-Power-Law)

$$F(q) = -A \exp(1/q) + B \tag{13}$$
$$F(q) = -A \frac{e^{1/q}}{q} + B \tag{14}$$

These satisfy all constraints but involve essential singularities at $q=0$. They are not scale-covariant and have no known physical motivation. We include them for completeness but they will be excluded by the naturalness arguments in Section 4.

### 3.7 Summary Table

| Family | $F(q)$ (increasing) | $D(q) = F'(q)$ | $q\to 0$ | $q\to 1$ |
|--------|---------------------|-----------------|----------|----------|
| Logarithmic | $A\log q + B$ | $A/q$ | $-\infty$ | $B$ |
| DGF ($\alpha=1$) | $-\frac{A}{q} + B$ | $\frac{A}{q^2}$ | $-\infty$ | $-A+B$ |
| Power-law ($\alpha>0$) | $-A q^{-\alpha} + B$ | $\alpha A q^{-\alpha-1}$ | $-\infty$ | $-A+B$ |
| Logit (entropy) | $A\log\frac{q}{1-q} + B$ | $\frac{A}{q(1-q)}$ | $-\infty$ | $+\infty$ |
| Generalized ($\alpha,\beta$) | $-A q^{-\alpha}(1-q)^\beta + B$ | $A q^{-\alpha-1}(1-q)^{\beta-1}[\alpha(1-q) + \beta q]$ | $-\infty$ | depends on $\beta$ |
| Essential | $-A e^{1/q} + B$ | $\frac{A}{q^2}e^{1/q}$ | $-\infty$ | $-Ae+B$ |

**Key observation.** Among all families:
- The **logit family** (IV) has symmetry under $q \leftrightarrow 1-q$, diverging at both boundaries.
- The **logarithmic family** (II) has the mildest divergence at $q=0$ ($D \sim 1/q$).
- The **DGF family** (I, $\alpha=1$) has $D \sim 1/q^2$ — the strongest power-law divergence among physically common forms.
- All power-law families are asymmetric, diverging only at the lower boundary. This asymmetry is not a flaw — it reflects the physical fact that information CAPACITY (A2) bounds occupancy from above but not from below.

---

## 4. Physical Principles That Can Constrain $F(q)$

Given the large function space remaining after C1-C4+(IR), we now examine additional physical principles that could narrow the choice.

### 4.1 Principle P1: Scale Invariance

**Statement.** If all occupancies are rescaled by a common factor $q \to \lambda q$, the physics of information flow should be unchanged, up to an overall rescaling of time.

**Mathematical formulation.** Under $q \to \lambda q$, $\tau \to \lambda^\gamma \tau$, equation (7) should be covariant:
$$\frac{\partial q}{\partial \tau} = -\nabla \cdot [D(q)\nabla q]$$

Under scaling: LHS $\to \lambda^{1-\gamma} \partial_\tau q$, RHS $\to -\nabla \cdot [D(\lambda q) \cdot \lambda \nabla q] = -\lambda \nabla \cdot [D(\lambda q)\nabla q]$.

Covariance requires $D(\lambda q) = \lambda^{-\gamma} D(q)$. If time does not rescale ($\gamma = 0$), then $D(\lambda q) = D(q)$ — $D$ is scale-invariant.

**Applying to power-law family.** $D(q) \propto q^{-\alpha-1}$ (from Section 3.1, with the $D=F'$ convention). Then $D(\lambda q) \propto \lambda^{-\alpha-1} q^{-\alpha-1} = \lambda^{-(\alpha+1)} D(q)$.

For scale invariance ($D(\lambda q) = D(q)$): we need $\alpha+1 = 0 \implies \alpha = -1$. But $\alpha > 0$ is required for C3!

Scale invariance with $\gamma \neq 0$: $D(\lambda q) = \lambda^{-\gamma} D(q)$ requires $\alpha+1 = \gamma$. Any $\alpha$ can be made scale-covariant with an appropriate time rescaling exponent $\gamma = \alpha+1$. There is **no unique** $\alpha$ from scale covariance alone.

**Scale invariance of $F$ directly.** An alternative approach: require that $F$ itself is a homogeneous function: $F(\lambda q) = \lambda^k F(q)$. For $F(q) = -A q^{-\alpha}$:
$$F(\lambda q) = -A \lambda^{-\alpha} q^{-\alpha} = \lambda^{-\alpha} F(q)$$
So $k = -\alpha$. If we demand $k = -1$ (the simplest nontrivial homogeneity), then $\alpha = 1$ — the DGF form.

**The claim in the problem statement** that $F(\lambda q) = \lambda^{-1} F(q)$ selects $F \propto 1/q$ is correct **if** we demand that $F$ itself be homogeneous of degree $-1$. But this is a choice: why degree $-1$ rather than degree $-2$ or $-\frac{1}{2}$?

### 4.2 The Fundamental Tension: Scale Invariance vs. A2

**Critical observation.** A2 imposes a **hard upper bound** $q \leq 1$. This bound explicitly breaks scale invariance: you cannot freely rescale $q \to \lambda q$ and remain within $[0,1]$ unless $\lambda \leq 1$. Thus:

> **Scale invariance cannot be an exact symmetry of the theory. It can only hold approximately in the dilute limit $q \ll 1$.**

This is analogous to:
- **Fermi-Dirac statistics**: at low occupation, scale invariance (Maxwell-Boltzmann) holds; at high occupation, the exclusion principle ($q \leq 1$) breaks it.
- **Critical phenomena**: scale invariance emerges near critical points, not as a fundamental axiom.
- **Quantum gravity**: scale invariance of the Einstein-Hilbert action is broken by the Planck scale.

**Consequence.** If scale invariance is only approximate (IR, $q \ll 1$), then it constrains the **leading behavior** of $F(q)$ as $q \to 0$ but **not** the global functional form. Specifically, for any $F$ in the power-law or generalized families:
$$F(q) \sim -A q^{-\alpha} \quad \text{as } q \to 0$$
Scale invariance in the IR picks out $\alpha = 1$, giving $F(q) \sim -A/q$ near $q=0$. But the behavior at finite $q$ (approaching $q=1$) remains unconstrained by scale invariance.

### 4.3 Principle P2: Information Potential and the Gradient Flow

**Statement.** There exists a scalar information potential $\Phi(q)$ such that the flux is the negative gradient of the chemical potential in $q$-space:
$$J_{i \to j} = -[\Phi(q_j) - \Phi(q_i)]$$

This is equivalent to our additive form with $F = -\Phi$. The question is: what physical principle determines $\Phi(q)$?

**Candidate A: Thermodynamic entropy.** If each cell is a binary information store, its entropy is $S(q_i) = -q_i \log q_i - (1-q_i) \log(1-q_i)$. The chemical potential is $\mu_i = \partial S/\partial q_i = \log((1-q_i)/q_i)$. Then:
$$\Phi(q) = \log\frac{1-q}{q}$$
$$F(q) = -\Phi(q) = \log\frac{q}{1-q}$$

This is the **logit family (Family IV)**. It's symmetric, physically motivated, but gives $D(q) \to 0$ as $q \to 0$ (empty cells barely interact), which seems at odds with C3's requirement of strong interaction near $q=0$.

**Candidate B: Capacity pressure.** If we view $q$ as a "volume fraction" and the pressure as $P \propto 1/(1-q)$ (diverging as $q \to 1$, like in granular materials), then the flux is driven by the pressure gradient:
$$F(q) = -\frac{1}{1-q}$$
But this diverges at $q=1$, not $q=0$, violating C3.

**Candidate C: Geometric potential.** If $q$ lives on a hyperbolic space with metric $ds^2 = dq^2/q^2$, then the natural potential is $F(q) \propto 1/q$. This is the DGF form. The metric $ds^2 = dq^2/q^2$ is the unique metric (up to scale) on $(0,1)$ that is invariant under $q \to \lambda q$. This connects back to scale invariance.

### 4.4 Principle P3: IR Fixed Point and Universality

**Statement.** The continuum limit $h \to 0$ of the lattice model defines a renormalization group (RG) flow. The IR fixed point of this flow determines the universal long-wavelength behavior, independent of microscopic details.

**Analysis.** Consider the continuum equation:
$$\partial_\tau q = -\nabla \cdot [q^{-(\alpha+1)} \nabla q] \tag{15}$$
where we've specialized to the power-law family $F \propto -q^{-\alpha}$, $D \propto q^{-(\alpha+1)}$.

Under an RG transformation (coarse-graining by factor $b$):
$$x \to x/b, \quad \tau \to \tau/b^z, \quad q \to b^{\Delta_q} q$$

The equation becomes:
$$b^{-\Delta_q - z} \partial_\tau q = -b^{-2} \nabla \cdot [b^{\Delta_q(\alpha+1)} q^{-(\alpha+1)} \cdot b^{\Delta_q} \nabla q]$$

For covariance: $-\Delta_q - z = -2 + \Delta_q(\alpha+2)$.

The dynamical exponent $z$ and the scaling dimension $\Delta_q$ are related to $\alpha$. For each $\alpha$, there is a different RG fixed point with different critical exponents. **There is no RG argument that singles out $\alpha = 1$ uniquely**, unless additional symmetry constraints are imposed.

However, the **stability** of the fixed point under perturbations matters. Perturbations to $F(q)$ that preserve C1-C4 and are analytic near $q=0$ will flow to the power-law form in the IR (since power-law singularities dominate over analytic corrections as $q \to 0$). The exponent $\alpha$ is determined by the leading singularity.

### 4.5 Principle P4: Minimal Divergence (Occam's Razor)

**Statement.** Among all $F$ satisfying C1-C4, choose the one with the **mildest** divergence at $q=0$ that still satisfies C3.

For power-law family $F \sim -q^{-\alpha}$, the divergence strength increases with $\alpha$:
- $\alpha \to 0^+$: $D \sim q^{-1}$ — approaches the logarithmic form (Section 3.2)
- $\alpha = 1$: $D \sim q^{-2}$ — DGF
- $\alpha > 1$: $D \sim q^{-(\alpha+1)}$ — stronger than inverse-square

Among power-law families, the logarithmic family ($F = A\log q$) has the mildest divergence: $D \sim 1/q$. The DGF family ($\alpha=1$) has $D \sim 1/q^2$.

If we adopt "mildest divergence" (Occam's razor in singularity strength) as the selection principle, we get the **logarithmic family**, not DGF. This would mean $F(q) = A\log(q)$ is the minimal choice.

However, "mildest divergence" is not a physical principle — it is an aesthetic one. The actual divergence strength should be determined by the microscopic information transfer mechanism, not by a preference for mildness. If the integrate-and-fire cellular automaton produces $1/q$ behavior (firing rate proportional to accumulated information), then logarithmic $F$ emerges. If it produces $1/q^2$ behavior (firing rate proportional to the square of accumulated information, as in DGF), then $\alpha=1$ emerges.

### 4.6 Principle P5: Connection to Known Diffusion Universality Classes

**Statement.** In the $q \approx 1$ limit (near saturation), the dynamics should recover a known diffusion universality class.

Near $q = 1$, expand $q = 1 - \varepsilon$ with $\varepsilon \ll 1$:
- **DGF ($\alpha=1$)**: $F(1-\varepsilon) \approx -A(1+\varepsilon)$, $D(1) = A$ (constant). Near saturation, the dynamics is **standard anti-diffusion with constant coefficient** — the simplest possible behavior.
- **Logit**: $F(1-\varepsilon) \approx A\log(1/\varepsilon)$, $D(1-\varepsilon) \approx A/\varepsilon$. Near saturation, $D$ diverges — the cell at $q=1$ "explodes" with infinite diffusivity.
- **Logarithmic**: $F(1-\varepsilon) \approx -A\varepsilon$, $D(1-\varepsilon) \approx A$ (constant). Same as DGF near $q=1$!

**DGF and Logarithmic families coincide near $q=1$** (both give $D \approx$ const near saturation). They differ only near $q=0$, where DGF diverges as $1/q^2$ and logarithmic diverges as $1/q$.

This suggests that the **near-saturation behavior does not distinguish** between many families. The key difference is in the dilute limit $q \ll 1$.

---

## 5. Scale Invariance: Rigorous Analysis

### 5.1 What Scale Invariance Actually Demands

Scale invariance of the **equation of motion** (not of $F$ alone):

$$\partial_\tau q = -\nabla \cdot [D(q)\nabla q]$$

Under $q \to \lambda q$, $x \to \lambda^{\nu} x$, $\tau \to \lambda^z \tau$:

$$\lambda^{-z} \partial_\tau (\lambda q) = -\lambda^{-2\nu} \nabla \cdot [D(\lambda q) \cdot \lambda \nabla q]$$
$$\lambda^{1-z} \partial_\tau q = -\lambda^{1-2\nu} \nabla \cdot [D(\lambda q) \nabla q]$$

For covariance: $\lambda^{1-z} = \lambda^{1-2\nu} \implies z = 2\nu$.

And we need $D(\lambda q) = \lambda^\kappa D(q)$ for some $\kappa$. This gives $D(q) \propto q^{\kappa}$. Power-law $D$ is selected.

With $D \propto q^{-(\alpha+1)}$ (power-law $F$): $\kappa = -(\alpha+1)$. Then:

$$\lambda^{1-z} = \lambda^{1-2\nu} \cdot \lambda^{\kappa(1)}$$

Wait, the scaling of $D(\lambda q) = \lambda^\kappa D(q)$ means $D$ contributes $\lambda^\kappa$ to the RHS scaling. But $D$ acts on $\nabla q$, which is inside $\nabla \cdot [\cdots]$. Let me redo this more carefully.

Actually, the equation inside is $-\nabla \cdot [D(\lambda q) \nabla (\lambda q)] = -\nabla \cdot [\lambda^\kappa D(q) \cdot \lambda \nabla q] = -\lambda^{\kappa+1} \nabla \cdot [D(q)\nabla q]$.

Under spatial rescaling $x \to \lambda^\nu x$, $\nabla \to \lambda^{-\nu} \nabla$, so $-\nabla \cdot [\cdots] \to \lambda^{-2\nu} \cdot (-\nabla \cdot [\cdots])$.

So RHS scales as $\lambda^{-2\nu + \kappa + 1}$.

LHS: $\partial_\tau (\lambda q) = \lambda \partial_\tau q$, with $\tau \to \lambda^z \tau$: $\partial_\tau \to \lambda^{-z} \partial_\tau$. LHS scales as $\lambda^{1-z}$.

Covariance: $1-z = -2\nu + \kappa + 1$, i.e., $z = 2\nu - \kappa$.

With $\kappa = -(\alpha+1)$: $z = 2\nu + \alpha + 1$.

**Conclusion: Any $\alpha$ admits a scale-covariant formulation with appropriate dynamical exponent $z$.** Scale invariance alone does **not** select $\alpha = 1$.

### 5.2 The Special Status of $\alpha = 1$

There are two independent arguments that make $\alpha = 1$ special:

**Argument 1: Strict invariance.** Is there a choice of $\nu, z$ such that the equation is strictly invariant (no rescaling of $x$ or $\tau$)? Setting $\nu = 0, z = 0$: the covariance condition $1-z = -2\nu + \kappa + 1$ gives $1 = \kappa + 1$, so $\kappa = 0$, implying $D(\lambda q) = D(q)$, i.e., $D$ is scale-invariant. For $D \propto q^{-(\alpha+1)}$, this requires $\alpha = -1$. But C3 demands $\alpha > 0$. So strict invariance ($\nu=0, z=0$) is impossible for any $\alpha > 0$. All power-law families require at least time rescaling or spatial rescaling.

But consider the COMBINED transformation $q \to \lambda q$, $\tau \to \lambda^2 \tau$ with $\nu = 0$ (no spatial rescaling). Then $z = 2$, and $1-2 = \kappa + 1$, so $\kappa = -2$, giving $\alpha = 1$. This means: for $\alpha=1$ (DGF), the time rescaling $\tau \to \lambda^2 \tau$ is sufficient — no spatial rescaling is needed. For $\alpha \neq 1$, either spatial rescaling or a different time exponent is required.

This is a genuine distinction: DGF ($\alpha=1$) is the unique power-law for which scale invariance can be restored by time rescaling alone, without touching spatial coordinates.

**Argument 2: Dimensional analysis of the discrete model.** The lattice equation is:
$$\frac{dq_i}{dt} = \sum_j [F(q_j) - F(q_i)]$$

Since $q$ is dimensionless, $dq/dt$ has dimension $[T]^{-1}$. Both sides must match. With $F(q) \propto -q^{-\alpha}$, the RHS involves terms like $q^{-\alpha}$. For the continuum limit to be well-defined, there must be a natural scale that relates $q$ to the lattice structure. If we demand that no new scale enters (i.e., the only dimensionless parameter is $q$ itself), then the equation must be homogeneous in $q$. This forces:

The RHS involves $q^{-\alpha}$. The LHS involves $dq/dt$. For dimensional consistency in the absence of an external scale, we need a relation between $t$ and $q$. But $q$ is dimensionless and $t$ has dimension. So we MUST introduce an external timescale unless the equation is homogeneous in the sense that both sides scale the same way under a rescaling of the "units" of $t$ and $q$.

This gets into subtle dimensional analysis territory. The clean statement is:

> **If the theory has no intrinsic scale other than the lattice spacing and the total capacity (which is set to 1 by A2), then the only scale-invariant choice is $\alpha = 1$.**

But this is circular — it assumes scale invariance to derive $\alpha=1$, then uses $\alpha=1$ to claim scale invariance.

### 5.3 True Distinction: Behavior of $D(q)$ at $q=0$

| Family | $D(q)$ near $q=0$ | $D(0^+)$ |
|--------|-------------------|----------|
| Logarithmic ($F \sim \log q$) | $A/q$ | $\infty$ |
| DGF ($F \sim -1/q$) | $A/q^2$ | $\infty$ |
| Power-law ($\alpha > 1$) | $\propto q^{-(\alpha+1)}$ | $\infty$ |
| Power-law ($0 < \alpha < 1$) | $\propto q^{-(\alpha+1)}$ | $\infty$ |
| Logit ($F = \log\frac{q}{1-q}$) | $A/q$ | $\infty$ |

All have divergent $D(q)$ at $q=0$. The difference is in the **rate** of divergence:
- $\alpha > 1$: stronger than $1/q$ divergence
- $\alpha = 1$: $1/q^2$ divergence (DGF)
- $\alpha < 1$ and logarithmic: $1/q$ or slower

---

## 6. The Minimal Assumption: What Truly Selects $F(q)$?

### 6.1 Candidates for the "Minimum Additional Assumption"

We evaluate each candidate for parsimony, physical motivation, and power to constrain $F$.

**Candidate M1: Full scale invariance.** $F(\lambda q) = \lambda^{-1}F(q)$.
- **Selects**: DGF ($F \propto -1/q$).
- **Physical motivation**: Strong — fundamental principle of physics.
- **Problem**: Explicitly broken by A2 ($q \leq 1$ hard bound). Can only hold approximately in $q \ll 1$ limit.
- **Power**: Uniquely selects $\alpha=1$.
- **Verdict**: Too strong to be an axiom — cannot be exact given A2.

**Candidate M2: IR scale invariance.** $F(q) \sim -A/q$ as $q \to 0$ (leading behavior).
- **Selects**: Asymptotic DGF near $q=0$, but leaves $q \sim O(1)$ behavior unconstrained.
- **Physical motivation**: Scale invariance emerges in the dilute limit where $q \ll 1$ and the upper bound $q=1$ is irrelevant. This is analogous to how conformal invariance emerges in critical theories when the correlation length diverges.
- **Power**: Constrains only the IR. Multiple UV completions are possible.
- **Verdict**: Physically defensible but under-constrains. The global $F(q)$ is not uniquely selected.

**Candidate M3: Simplicity (Occam/Optimality).** Among all $F$ satisfying C1-C4, choose the one with the simplest analytic form.
- **Selects**: $F(q) = -A/q + B$ (two parameters, rational function).
- **Physical motivation**: No new physical principle — purely aesthetic.
- **Power**: Selects DGF, but the justification is weak.
- **Verdict**: Works, but not a physical axiom. A "minimal model" choice rather than a derived one.

**Candidate M4: Gradient of binary entropy.** $F(q) = \partial S/\partial q$ where $S$ is the Shannon entropy of a binary variable.
- **Selects**: Logit family $F(q) = A\log(q/(1-q))$.
- **Physical motivation**: Strong — information theory is the foundation of the framework.
- **Power**: Uniquely selects the logit form.
- **Problem**: $D(q) \to 0$ as $q \to 0$, meaning empty cells barely interact. This may or may not be physically correct, but it's a definite prediction.
- **Verdict**: Physically the most defensible single additional axiom, but its phenomenological consequences differ from DGF and need to be checked against data.

**Candidate M5: Coulomb/inverse-square analogy.** The flux between two cells should be analogous to the gravitational/electrostatic force between two "information charges."
- **Selects**: DGF ($F \propto -1/q$, giving $D \propto 1/q^2$, analogous to inverse-square force).
- **Physical motivation**: Weak analogy — gravitational force goes as $1/r^2$, not $1/q^2$.
- **Power**: Selects DGF.
- **Verdict**: Weak physical justification; the analogy is superficial.

**Candidate M6: Linear-response near saturation.** As $q \to 1$, $D(q)$ should approach a constant (standard anti-diffusion).
- **Selects**: DGF and logarithmic families (both give $D(1) =$ const).
- **Excludes**: Logit family ($D \to \infty$ at $q=1$).
- **Physical motivation**: Near saturation, the system should have the simplest possible dynamics — constant "conductivity." This is the principle of **normal behavior at the UV cutoff**.
- **Power**: Excludes the logit family, but doesn't distinguish DGF from logarithmic.
- **Verdict**: Reasonable, but insufficient alone to select DGF.

### 6.2 The True Minimal Assumption

After eliminating candidates that are either too strong (M1, violates A2), too weak (M2, under-constrains), or physically unmotivated (M3, M5), we arrive at a **two-principle minimal set**:

> **M_minimal = M6 (Normal UV) + M2 (IR scale invariance)**

1. **M6 (Normal behavior near $q=1$)**: $D(q) \to \text{const} > 0$ as $q \to 1$. This says that near saturation, information redistributes with constant effective diffusivity — the simplest possible dynamics. This excludes the logit family and the $\beta > 0$ generalized families.

2. **M2 (IR scale invariance, $q \ll 1$)**: $D(q) \sim q^{-2}$ as $q \to 0$. This says that in the dilute limit, the dynamics is scale-invariant, which picks $\alpha = 1$ among the power-law family (and excludes logarithmic $D \sim q^{-1}$).

Together, M2 + M6 select the DGF form **uniquely** among all families in Section 3:

$$F(q) = -\frac{A}{q} + B, \quad D(q) = \frac{A}{q^2}$$

But wait — do M2 and M6 together exclude the logarithmic family? Logarithmic has $D \sim 1/q$ near $q=0$ (not $1/q^2$). M2 demands $D \sim q^{-2}$, so logarithmic is excluded. Good.

Do they exclude $\alpha \neq 1$ power-law? Power-law with $\alpha \neq 1$: $D \sim A\alpha q^{-(\alpha+1)}$. Near $q=1$, $D(1) = A\alpha$ (constant). So M6 is satisfied for all $\alpha$. M2 picks $\alpha = 1$ from IR scale invariance. ✓

Do they exclude generalized families? Generalized $F = -A q^{-\alpha}(1-q)^\beta$:
- Near $q=0$: $F \sim -A q^{-\alpha}$, $D \sim A\alpha q^{-(\alpha+1)}$. M2 picks $\alpha = 1$.
- Near $q=1$: $F \sim -A(1-q)^\beta$, $D \sim A\beta(1-q)^{\beta-1}$.
  - If $\beta > 1$: $D(1) = 0$ — violates M6.
  - If $\beta = 1$: $D(1) = A$ — satisfies M6. But $\beta = 1, \alpha = 1$ reduces to DGF.
  - If $0 < \beta < 1$: $D(1) \to \infty$ — violates M6.
  - If $\beta = 0$: DGF ($\alpha=1$).
  
So M2 + M6 select precisely the DGF form. ✓

### 6.3 Alternative Minimal Path: M4 Alone

If instead we adopt M4 (entropy gradient), we get the logit form directly, with no need for scale invariance arguments. The logit form:
- Automatically satisfies C1-C4 ✓
- Has $D(q) \to 0$ as $q \to 0$ (empty cells barely interact) — different physics from DGF
- Has $D(q) \to \infty$ as $q \to 1$ — full cells "explode" with information pressure

This is a **single axiom** with strong physical motivation. Whether it's the CORRECT axiom depends on which behavior matches the microscopic model:
- If empty cells greedily absorb information, $D(0) \to \infty$ (DGF-like) is correct.
- If empty cells are inert until they accumulate information, $D(0) \to 0$ (logit-like) is correct.

---

## 7. Judgment: Should Scale Invariance Be Elevated to A5?

### 7.1 Arguments FOR Elevating Scale Invariance to A5

1. **Universality argument.** Scale invariance at critical points is one of the most successful organizing principles in theoretical physics (Wilson's RG, conformal field theory, critical phenomena). Elevating it to axiom status places the information capacity framework in this tradition.

2. **Predictive power.** A5 (scale invariance) + A1-A3 uniquely determines the flux form to be DGF ($F \propto -1/q$). Without A5, there are infinitely many admissible flux forms, and the theory loses predictive power.

3. **Connection to known results.** The DGF form yields the double-domain universality structure discovered by Expert 2. If this universality is robust (many $F$ forms flow to the same IR), then the specific choice of $F$ matters less — but scale invariance provides the cleanest derivation.

4. **Minimal parameter count.** DGF has the fewest free parameters (one amplitude $A$, plus an irrelevant additive constant $B$) among all admissible $F$ forms. This satisfies Occam's razor.

### 7.2 Arguments AGAINST Elevating Scale Invariance to A5

1. **A2 explicitly breaks scale invariance.** The hard bound $q \leq 1$ means $q \to \lambda q$ with $\lambda > 1$ is not a symmetry of the configuration space. Scale invariance can at best be an **emergent** symmetry in the IR, not a fundamental axiom on par with A1-A3.

2. **Many physical theories with hard bounds work without scale invariance.** Fermi liquids, lattice gauge theories, and granular materials all have natural bounds (Brillouin zone, maximum occupancy, close-packing) and do not elevate scale invariance to axiom status. They treat scale invariance as a useful approximation in certain limits.

3. **The logit (entropy gradient) alternative is physically compelling.** If the framework is fundamentally about INFORMATION, then the Shannon entropy $S(q) = -q\log q - (1-q)\log(1-q)$ is the natural starting point. The entropy gradient $F = \partial S/\partial q = \log(q/(1-q))$ produces the logit flux form. This requires no scale invariance — only the definition of information entropy.

4. **The double-domain universality (Expert 2) may protect physical conclusions.** If many different $F$ forms produce the same qualitative phase structure (two domains separated by a critical $q$), then the choice between DGF and logit (or any other form) does not affect the main physical predictions. In that case, elevating scale invariance to A5 is unnecessary — the theory is structurally robust.

5. **SSB of scale invariance is more interesting.** Rather than imposing scale invariance as an axiom, it may be more fruitful to study how scale invariance is **spontaneously broken** by the dynamics. The $q=1$ bound could be seen as the result of spontaneous symmetry breaking of an underlying scale-invariant theory at high density. This is analogous to how the Higgs mechanism breaks electroweak symmetry — the symmetry is in the Lagrangian, not in the ground state. Making scale invariance an emergent phenomenon rather than an axiom leads to richer physics.

### 7.3 Recommended Position

**We recommend AGAINST elevating scale invariance to A5 as a fundamental axiom.**

Instead, we recommend the following stratified approach:

**Tier 1 (Axioms, essential):**
- A1: Distinguishability → bijection
- A2: Capacity bound ($q \in [0,1]$)
- A3: Locality (finite neighborhood)

**Tier 2 (Regularity conditions, strongly motivated):**
- R1: Irrotationality ($\oint J = 0$ → additive form $J = F(q_j) - F(q_i)$)
- R2: $C^1$ smoothness of $F$ on $(0,1)$

**Tier 3 (Physical selection, empirically testable):**
- P_a: IR scale invariance ($F(q) \sim -A/q$ as $q \to 0$) → **DGF form**
- P_b: Entropy gradient ($F = \partial S/\partial q$) → **Logit form**

The choice between P_a and P_b (or other Tier 3 principles) should be made based on:
1. **Microscopic derivation**: What is the actual rule for information transfer in the discrete cellular automaton? This should determine $F$ from first principles.
2. **Numerical evidence**: Simulate the discrete model and measure the effective $F(q)$ from the observed flux statistics.
3. **Phenomenological fit**: Which $F$ form better describes real information-capacity-limited systems (neural networks, social networks, etc.)?

### 7.4 The Conservative Bottom Line

If forced to choose **one minimal additional assumption** without microscopic derivation:

> **Assume that $F(q)$ is the gradient of the binary entropy: $F(q) = \partial S/\partial q = \log(q/(1-q))$.**

This is the **single most natural** additional principle for an information-theoretic framework:
- It requires no new physics beyond Shannon's definition of entropy
- It is symmetrical between $q=0$ and $q=1$ (information and its absence are dual)
- It produces a specific, testable prediction: $D(q) = 1/[q(1-q)]$

However, if the microscopic model is an **integrate-and-fire** automaton (rather than an entropic system), then the **DGF form** ($F \propto -1/q$) is more likely to emerge, because:
- Integrate-and-fire naturally produces $1/q$ type singularities (the firing rate diverges as the threshold approaches)
- The capacity bound $q=1$ is enforced by the firing mechanism, not by entropic repulsion
- Scale invariance in the dilute limit emerges naturally from the Poisson statistics of rare firing events

**The resolution of this tension requires specifying the microscopic update rule** — a task that lies between A1-A3 (which constrain the macro-level) and the flux form (which is the bridge between micro and macro).

---

## 8. The Flux Form in the Full Continuum Theory

### 8.1 Summary of the Selected Form (DGF, assuming P_a)

$$J_{i \to j} = A\left(\frac{1}{q_i} - \frac{1}{q_j}\right) \tag{16}$$

Equivalently: $F(q) = -\frac{A}{q}$ (up to an irrelevant additive constant).

**Continuum equation:**
$$\frac{\partial q}{\partial \tau} = -\nabla \cdot \left[\frac{A}{q^2} \nabla q\right] = A\nabla \cdot \left[\nabla\left(\frac{1}{q}\right)\right] = A\nabla^2\left(\frac{1}{q}\right) \tag{17}$$

This is the **backward heat equation for the variable $u = 1/q$**:
$$\frac{\partial q}{\partial \tau} = A\nabla^2 u, \quad u = 1/q \tag{18}$$

In terms of $u$: $\partial_\tau(1/u) = A\nabla^2 u$, or:
$$\partial_\tau u = -A u^2 \nabla^2 u \tag{19}$$

### 8.2 Summary of the Alternative Form (Logit, assuming P_b)

$$J_{i \to j} = A\log\frac{q_j(1-q_i)}{q_i(1-q_j)} \tag{20}$$

Equivalently: $F(q) = A\log\frac{q}{1-q}$.

**Continuum equation:**
$$\frac{\partial q}{\partial \tau} = -\nabla \cdot \left[\frac{A}{q(1-q)} \nabla q\right] \tag{21}$$

In terms of the logit variable $\ell = \log(q/(1-q))$:
$$\frac{\partial q}{\partial \tau} = -A\nabla^2 \ell \tag{22}$$

Since $q = \sigma(\ell) = 1/(1+e^{-\ell})$, this is a nonlinear diffusion in $\ell$-space.

### 8.3 Key Phenomenological Differences

| Observable | DGF ($F \propto -1/q$) | Logit ($F = \log\frac{q}{1-q}$) |
|------------|------------------------|--------------------------------|
| $D(q \to 0)$ | $\to \infty$ (explosive) | $\to \infty$ (weaker) |
| $D(q \to 1)$ | $\to A$ (constant) | $\to \infty$ (explosive) |
| Information flow at low density | Vacant cells are strong sources | Vacant cells are weak sources |
| Information flow at high density | Full cells flow at constant rate | Full cells explode with pressure |
| Symmetry $q \leftrightarrow 1-q$ | Broken (only $q=0$ is singular) | Preserved (both ends singular) |
| Connection to entropy | Indirect (via scale invariance) | Direct ($F = \partial S/\partial q$) |
| Free parameters | 1 (amplitude $A$) | 1 (amplitude $A$) |

---

## 9. Conclusion: The Hierarchy of Assumptions

```
Level 0 (microscopic):  Discrete CA update rule
        ↓ determines
Level 1 (axioms):       A1 (bijection), A2 (bound), A3 (locality)
        ↓ + irrotationality (R1)
Level 2 (form):         J = F(q_j) - F(q_i), F increasing
        ↓ + C3 (divergence at q=0)
Level 3 (families):     Power-law, logarithmic, logit, generalized
        ↓ + M2 (IR scale invariance) OR M4 (entropy gradient)
Level 4 (selection):    DGF (F ∝ -1/q) OR Logit (F = logit(q))
        ↓ numerical / experimental
Level 5 (validation):   Compare with discrete CA statistics
```

**The honest answer to "what is the minimal additional assumption?":**

There is no **single** minimal assumption that uniquely and inevitably selects the DGF form. The DGF form is selected by the **combination** of:
1. IR scale invariance ($q \ll 1$ dilute limit)
2. Normal behavior near saturation ($D(1) =$ const)

OR equivalently, by the single assumption that **the flux derives from an information potential that is homogeneous of degree $-1$ in occupancy**.

But the logit form is an equally valid alternative, selected by the single assumption that **the flux is the gradient of the binary Shannon entropy**.

**The choice between these two cannot be resolved at the level of axioms alone — it requires specifying the microscopic dynamics of the cellular automaton that A1-A3 constrain.** This is not a weakness of the framework; it is a feature. It means the framework is rich enough to accommodate different microscopic implementations, and the flux form is the **order parameter** that distinguishes between them.

---

## Appendix A: Sign Convention Reconciliation

The problem statement uses $F$ decreasing and $J = F(q_i) - F(q_j)$. In our analysis, we used $F$ increasing and $J = F(q_j) - F(q_i)$. The two conventions are equivalent under $F \to -F$. All physical conclusions are convention-independent.

| Convention | Flux form | $F$ monotonicity | C3 behavior | $D(q)$ |
|------------|-----------|------------------|-------------|--------|
| This document | $J = F(q_j) - F(q_i)$ | Increasing | $F(0^+) = -\infty$ | $D = F' > 0$ |
| Problem statement | $J = F(q_i) - F(q_j)$ | Decreasing | $F(0^+) = +\infty$ | $D = -q^2 F'$ |

The conversion: $F_{\text{this}} = -F_{\text{problem}}$.

## Appendix B: The $q^2$ Factor in $D(q)$

The problem's $D(q) = -q^2 F'(q)$ differs from our $D(q) = F'(q)$ by a factor of $-q^2$. This arises if the discrete flux is defined with a $q$-dependent coupling:

$$J_{i \to j} = q_i q_j [F_{\text{eff}}(q_j) - F_{\text{eff}}(q_i)]$$

In this case, the continuum limit yields $D = -q^2 F_{\text{eff}}'$. The factor of $q_i q_j$ can be motivated by: cells with more occupancy interact more strongly. This is an additional modeling choice beyond A1-A3+C1-C4.

With this factor: for $F_{\text{eff}}(q) = 1/q$ (decreasing convention), $D = -q^2 \cdot (-1/q^2) = 1$ (constant diffusivity). The DGF flux then gives **standard diffusion** in the effective variable, which is aesthetically appealing and may be the origin of the problem's preference for $D \propto 1/q$.

---

*Analysis completed 2026-06-06. Next step: integrate with Expert 2's double-domain universality analysis to determine whether the DGF vs. logit distinction matters for macroscopic predictions.*
