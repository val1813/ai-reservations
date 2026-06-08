# Information Flux Functional Form: Derivation from First Principles

**Context**: DGF framework (LP31-InfoCapacity), Axioms A1 (injectivity) + A2 (finite state space) + A3 (occupation number conservation).

**Question**: Can the flux form $J_{i\to j} = 1/q_i - 1/q_j$ be *derived* from A1+A2+A3, or is there a minimal additional assumption?

**Author**: Mathematical Physics Analysis
**Date**: 2026-06-06

---

## 0. Preliminaries: What the Axioms Actually Say

### 0.1 Definitions

- $N$ binary cells, each $s_i \in \{0,1\}$ (0 = vacant, 1 = occupied)
- $q_i = 1 - s_i$ at the mesoscopic level: **vacant fraction** (fraction of capacity that is free)
  - $q \to 0$: cell nearly full (saturated with information)
  - $q \to 1$: cell nearly empty (lots of free capacity)
- Microstate space: $X = \{0,1\}^N$, $|X| = 2^N$

### 0.2 What the Axioms Constrain

| Axiom | Statement | What it constrains about flux |
|-------|-----------|-------------------------------|
| **A1** | $f: X \to X$ is injective | $f$ is a permutation (T1a). Dynamics preserve distinguishability. **Does NOT specify which permutation occurs.** |
| **A2** | $\|X\| = 2^N < \infty$ | Finite state space. Makes A1 $\Rightarrow$ bijection. **No constraint on rates.** |
| **A3** | $\sum_i s_i = \sum_i f(s)_i$ | Total occupation conserved. In continuum limit: $\partial_t \int q \, d^dx = 0$. **Gives continuity equation structure, but NOT the flux functional form.** |

**Critical observation**: A1+A2+A3 constrain the *kinematics* (permutation, conservation) but not the *dynamics* (which permutation, at what rate). The flux $J$ is a **rate** — it specifies how fast information moves from cell $i$ to cell $j$. The axioms do not specify rates.

This is exactly analogous to classical mechanics: Newton's laws specify that energy is conserved but not *how* energy flows between degrees of freedom. The flux is a constitutive relation, not a conservation law.

---

## 1. General Mathematical Structure

### 1.1 Constraints on $J(q_i, q_j)$

**C1 (Directionality)**: Information flows from low $q$ to high $q$ (from full to empty cells).
$$\text{sgn}[J(q_i, q_j)] = \text{sgn}(q_j - q_i)$$

**C2 (Antisymmetry)**: $J(q_i, q_j) = -J(q_j, q_i)$. The net flow from $i$ to $j$ is the negative of the net flow from $j$ to $i$.

**C3 (Locality)**: $J$ depends only on $q_i$ and $q_j$. This follows from the nearest-neighbor interaction picture.

**C4 (Capacity constraint)**: 
- As $q \to 0$ (cell nearly full): "repulsion" $\to \infty$, effective diffusivity $D(q) \to \infty$
- As $q \to 1$ (cell nearly empty): "resistance" $\to 0$

**C5 (Conservation compatibility)**: The continuity equation
$$\partial_t q_i + \sum_{j \in \text{nn}(i)} J_{i\to j} = 0$$
must preserve $0 \leq q_i \leq 1$ for all cells.

### 1.2 The Most General Form Compatible with C1+C2

From antisymmetry (C2) alone, any sufficiently smooth $J$ can be written as:
$$J(q_i, q_j) = \sigma(q_i, q_j) \cdot (q_j - q_i)$$
where $\sigma(q_i, q_j) = \sigma(q_j, q_i) > 0$ is a symmetric, positive function.

From C1, $\sigma > 0$ ensures the correct sign.

From C3, $\sigma$ depends only on $(q_i, q_j)$.

**The additive separable form** $J = f(q_i) - f(q_j)$ corresponds to the special case:
$$\sigma(q_i, q_j) = \frac{f(q_i) - f(q_j)}{q_i - q_j}$$

This is a strong restriction: it means the "conductance" $\sigma$ between two cells depends on the pair in a way that factors through a single function $f$.

### 1.3 The Loop Condition and Additive Separability

**Definition (Loop Condition / Path Independence)**. For any three cells $i, j, k$:
$$J_{i\to j} + J_{j\to k} + J_{k\to i} = 0$$

This says the net flux around any closed loop is zero — the information flux is "irrotational" or "conservative" in the discrete sense.

**Theorem 1 (Loop condition $\Leftrightarrow$ additive separability).** 
$J$ satisfies C2 and the loop condition if and only if there exists a function $P: (0,1) \to \mathbb{R}$ such that:
$$J(q_i, q_j) = P(q_i) - P(q_j)$$

*Proof.*
($\Rightarrow$) Fix a reference state $q_0$ and define $P(q) = J(q_0, q)$. Then for any $q_i, q_j$:
$$J(q_i, q_j) = J(q_i, q_0) + J(q_0, q_j) \quad \text{(loop condition with } k = q_0\text{)}$$
$$= -J(q_0, q_i) + J(q_0, q_j) \quad \text{(C2)}$$
$$= -[P(q_0) - P(q_i)] + [P(q_0) - P(q_j)]$$
$$= P(q_i) - P(q_j)$$

($\Leftarrow$) If $J = P(q_i) - P(q_j)$, then:
$$J_{i\to j} + J_{j\to k} + J_{k\to i} = (P_i - P_j) + (P_j - P_k) + (P_k - P_i) = 0$$

And antisymmetry C2 is automatic: $J(q_i, q_j) = -J(q_j, q_i)$. $\square$

**Physical interpretation**: The loop condition is the discrete analog of $\nabla \times \mathbf{J} = 0$ in the continuum. It states that the information flux is derivable from a scalar potential $P(q)$. This is the same structure as:
- Electrostatics: $\mathbf{E} = -\nabla V$ (since $\nabla \times \mathbf{E} = 0$)
- Thermodynamics: heat flux $\propto \nabla T$ (Fourier's law)
- Chemical diffusion: particle flux $\propto -\nabla \mu$ (Fick's law / Onsager)

The loop condition is **not** derivable from A1+A2+A3. It is an additional physical postulate. However, it is a very natural one: it says there are no "information vortices" — you cannot have a cyclic flow of information that goes $i \to j \to k \to i$ without any gradient in the macroscopic variable driving it.

### 1.4 Constraints on $P(q)$ from C1, C4, C5

Once we accept additive separability $J = P(q_i) - P(q_j)$, the constraints translate to:

**From C1**: $q_i < q_j \Rightarrow P(q_i) > P(q_j)$, so $P$ is strictly decreasing: $P'(q) < 0$.

**From C4**: In the continuum limit, $J \approx P'(q)(q_i - q_j) = -P'(q)(q_j - q_i)$. The effective diffusivity is:
$$D(q) = -P'(q)$$

(Up to a factor of lattice spacing $a^2$ and time scale.) Therefore:
- $D(0) = -P'(0) = +\infty$: $P'(q) \to -\infty$ as $q \to 0^+$
- $D(1) = -P'(1)$ should be "small." The strictest reading of C4 is $D(1) = 0$, i.e., $P'(1) = 0$

**From C5**: When $q_i \to 0$, the flux out of cell $i$ is $P(0) - P(q_j)$ which can be finite or infinite depending on $P(0)$. If $P$ diverges at 0, the flux out of a nearly-full cell is infinite — this is physically sensible (information bursts out). When $q_i \to 1$, the flux into cell $i$ is $P(q_j) - P(1)$, which should approach 0 (a completely empty cell can't receive information? Actually no — an empty cell CAN receive information. C5 is about boundedness of $q \in [0,1]$, not about flux going to zero.)

**Summary of constraints on $P$**:
1. $P'(q) < 0$ for all $q \in (0,1)$
2. $\lim_{q\to 0^+} P'(q) = -\infty$
3. $\lim_{q\to 1^-} P'(q) = 0$ (strict reading) or finite (relaxed reading)

These constraints admit infinitely many functions $P$. The question is which one is "correct."

---

## 2. Four Derivation Paths

### Path A: Shannon Entropy Gradient

#### A.1 Setup

Define the local entropy density (mixing entropy of a mesoscopic cell):
$$s(q) = -q \log q - (1-q) \log(1-q)$$

This is the Shannon entropy per cell for a binary distribution with vacant probability $q$ and occupied probability $1-q$. It counts the log-number of microstates consistent with macroscopic $q$:
$$\Omega(q) = \binom{|\Delta V|}{|\Delta V|(1-q)} \approx \exp(|\Delta V| \cdot s(q))$$

The information-chemical potential is the variation of entropy with respect to $q$:
$$\mu(q) = \frac{\partial s}{\partial q} = \log\frac{1-q}{q}$$

This is the standard thermodynamic derivative: $\mu$ is the entropic "force" conjugate to the variable $q$.

#### A.2 Flux from Chemical Potential Gradient

In Onsager's linear response theory, fluxes are proportional to gradients of thermodynamic forces:
$$J_{i\to j} \propto \mu(q_i) - \mu(q_j)$$

This gives:
$$J_{i\to j} = \Gamma \left[\log\frac{1-q_i}{q_i} - \log\frac{1-q_j}{q_j}\right] = \Gamma \log\frac{q_j(1-q_i)}{q_i(1-q_j)}$$

where $\Gamma > 0$ is a kinetic coefficient (Onsager coefficient).

In the small-$q$ regime ($q \ll 1$, cells nearly full — the regime of interest):
$$\mu(q) = \log\frac{1-q}{q} \approx -\log q$$

So $J \approx \Gamma \log(q_j/q_i)$ for small $q$.

#### A.3 Effective Diffusivity

The potential is $P_A(q) = -\Gamma \log\frac{1-q}{q}$ (the negative sign because flux is $\mu_i - \mu_j$, and we need $P$ decreasing).

Wait — let me be precise. If $J = \mu_i - \mu_j$, then $P = \mu$. But $\mu(q) = \log((1-q)/q)$. Is this decreasing?

$$\mu'(q) = -\frac{1}{1-q} - \frac{1}{q} = -\frac{1}{q(1-q)} < 0$$

Yes, $\mu$ is decreasing. So $P_A(q) = \log((1-q)/q)$ satisfies C1.

The effective diffusivity is:
$$D_A(q) = -P_A'(q) = \frac{1}{q(1-q)}$$

#### A.4 Check Against Constraints

| Constraint | Status | Detail |
|-----------|--------|--------|
| C1 (direction) | $\checkmark$ | $P_A' < 0$ |
| C2 (antisymmetry) | $\checkmark$ | $J = P_A(q_i) - P_A(q_j)$ |
| C3 (locality) | $\checkmark$ | Depends only on $q_i, q_j$ |
| C4: $D(0) = \infty$ | $\checkmark$ | $D_A(q) \sim 1/q$ as $q\to 0$, diverges |
| C4: $D(1) = 0$ | $\times$ | $D_A(q) \sim 1/(1-q)$ as $q\to 1$, diverges! |
| C5 (boundedness) | $\sim$ | $J$ is finite for all $q\in(0,1)$; the divergence at both ends is symmetric |

**The critical failure of Path A**: The diffusivity $D_A(q) = 1/(q(1-q))$ diverges at **both** $q=0$ and $q=1$. This means:
- Information bursts out of nearly-full cells ($q\to 0$) — physically correct
- Information ALSO bursts into nearly-empty cells ($q\to 1$) — physically wrong

The symmetry $q \leftrightarrow 1-q$ in the Shannon entropy is the culprit. In the DGF framework, $q$ and $1-q$ are not symmetric: information flows from occupied to vacant, not vice versa. The Shannon entropy is symmetric under this exchange, but the dynamics is not.

#### A.5 Small-$q$ Limit

In the limit $q \ll 1$: $D_A(q) \approx 1/q$, giving $P_A(q) \approx -\log q + \text{const}$.

This is a different potential from the DGF ansatz ($P = 1/q$). The difference matters:
- $P = -\log q$: $J = \log(q_j/q_i)$ — logarithmic sensitivity
- $P = 1/q$: $J = 1/q_i - 1/q_j$ — power-law sensitivity

For $q_i = 0.01, q_j = 0.02$:
- Logarithmic: $J = \log(2) \approx 0.69$
- Power-law: $J = 100 - 50 = 50$

The power-law form is 72 times larger — it produces much stronger fluxes from nearly-full cells, leading to sharper segregation dynamics. The phase diagram of the DGF framework depends critically on this difference.

**Conclusion for Path A**: Shannon entropy gradient gives a well-motivated but *wrong* flux form (wrong behavior at $q\to 1$, wrong $q\leftrightarrow 1-q$ symmetry). It cannot be the correct derivation without additional symmetry-breaking terms.

---

### Path B: Information Pressure

#### B.1 Setup

Postulate that each cell exerts an "information pressure" on its neighbors, proportional to some function of its occupancy. The flux is the pressure difference:
$$J_{i\to j} = P(q_i) - P(q_j)$$

The question is: what is $P(q)$?

#### B.2 Physical Motivation for $P(q) = 1/q$

**Argument 1 (Ideal gas analogy)**. Think of occupied slots as "particles" confined to a cell of capacity $C$. The vacant fraction is $q$, so the available "volume" for occupied slots is $qC$. By analogy with the ideal gas law $p = NkT/V$, the "information pressure" is:
$$p \propto \frac{\text{occupied slots}}{\text{vacant volume}} \propto \frac{1-q}{q}$$

For $q \ll 1$ (nearly full cells): $p \approx 1/q$.

**Argument 2 (Excluded volume)**. Each bit of information excludes other bits from occupying the same slot (Pauli-like exclusion). When $q$ is small, each remaining vacant slot is "squeezed" by $(1-q)/q$ occupied neighbors. The pressure to move information out scales as the inverse of available space: $p \sim 1/q$.

**Argument 3 (Dimensional analysis)**. $q$ is dimensionless. The only dimensionless singular function with $p \to \infty$ as $q \to 0$ is $1/q$ (up to logarithms and powers). Among power laws $q^{-\alpha}$, the case $\alpha = 1$ is the "marginal" case — it is the boundary between integrable ($\alpha < 1$) and non-integrable ($\alpha > 1$) singularities at $q=0$.

#### B.3 Check Against Constraints

| Constraint | Status | Detail |
|-----------|--------|--------|
| C1 (direction) | $\checkmark$ | $P(q) = 1/q$, $P'(q) = -1/q^2 < 0$ |
| C2 (antisymmetry) | $\checkmark$ | $J = P(q_i) - P(q_j)$ |
| C3 (locality) | $\checkmark$ | Depends only on $q_i, q_j$ |
| C4: $D(0) = \infty$ | $\checkmark$ | $D(q) = 1/q^2 \to \infty$ |
| C4: $D(1) = 0$ | $\sim$ | $D(1) = 1$, finite but not zero |
| C5 (boundedness) | $\checkmark$ | $q_i$ stays bounded in $[0,1]$ |

**The $D(1)$ issue**: With $P = 1/q$, the diffusivity at the empty limit is $D(1) = 1$, not 0. This means information flows into an empty cell at a finite rate, not an infinite one — which is physically fine (empty cells should receive information). The "strict" reading of C4 that $D(1)=0$ is arguably too strong: the resistance to flow INTO a cell should be zero when the cell is empty, corresponding to infinite conductance, not zero conductance. 

Actually, let me re-examine this carefully. $D(q)$ is the effective diffusivity. The flux in continuum is $\mathbf{J} = -D(q) \nabla q$. When $q \to 1$ (cell nearly empty), should $D(1)$ be large or small?

- If $D(1)$ is large: small gradients produce large fluxes → information flows easily into empty cells ✓
- If $D(1) = 0$: no flux regardless of gradient → empty cells resist information flow ✗

So $D(1)$ being finite (not zero) is actually physically correct for an empty cell! The strict reading of C4 gets the sign wrong on the $q\to 1$ end. The physical requirement should be:

**C4 (corrected)**: 
- $q \to 0$ (cell full): information strongly repelled → $D(q) \to \infty$ (large flux out)
- $q \to 1$ (cell empty): no resistance to incoming information → $D(q)$ finite (not zero)

With this correction, $P = 1/q$ (giving $D = 1/q^2$) satisfies both ends: $D(0) = \infty$, $D(1) = 1$.

#### B.4 The Gap

The pressure analogy is a *physical picture*, not a derivation. Why $1/q$ and not $1/q^2$ or $\log(1/q)$?

- $P = 1/q^2$: $D(q) = 2/q^3$, even stronger divergence at $q\to 0$
- $P = -\log q$: $D(q) = 1/q$, weaker divergence
- $P = e^{1/q}$: $D(q) = e^{1/q}/q^2$, extremely strong divergence

All of these satisfy C1-C5 (with corrected C4). The choice $P = 1/q$ requires additional justification.

**Conclusion for Path B**: The pressure analogy provides a compelling physical picture and nicely motivates $P=1/q$, but it does not *uniquely* determine $P$. It is a heuristic, not a derivation.

---

### Path C: Scale-Invariant Potential

#### C.1 Setup

Consider the transformation: rescale all vacant fractions by a factor $\lambda$:
$$q \to \lambda q$$

This corresponds to uniformly multiplying the free capacity of every cell. What should happen to the information potential?

**Scale invariance postulate**: If every cell's free capacity is multiplied by $\lambda$, the information "pressure" should be divided by $\lambda$ (more space $\Rightarrow$ less pressure):
$$P(\lambda q) = \frac{1}{\lambda} P(q)$$

#### C.2 Unique Determination

This functional equation, together with the requirement that $P$ is decreasing, has a unique solution (up to a multiplicative constant):

Differentiate with respect to $\lambda$:
$$\frac{d}{d\lambda} P(\lambda q) = q P'(\lambda q) = -\frac{1}{\lambda^2} P(q)$$

Set $\lambda = 1$:
$$q P'(q) = -P(q)$$

This is a separable ODE:
$$\frac{P'(q)}{P(q)} = -\frac{1}{q} \quad \Rightarrow \quad \log P(q) = -\log q + \text{const} \quad \Rightarrow \quad P(q) = \frac{C}{q}$$

The constant $C > 0$ sets the overall scale (can be absorbed into the time unit).

**Uniqueness**: No other function satisfies $P(\lambda q) = P(q)/\lambda$ for all $\lambda > 0$. (Proof: the ODE $qP' = -P$ has exactly this as its general solution.)

#### C.3 Check Against Constraints

All constraints satisfied (same as Path B). Additionally, the scale invariance provides a principled reason for the specific power $\alpha = 1$.

#### C.4 Domain of Validity

The scale invariance argument strictly works only on $(0, \infty)$, but $q \in (0,1)$ is bounded. The transformation $q \to \lambda q$ can take $q$ outside $(0,1)$ for $\lambda > 1/q$.

However, in the physically relevant regime $q \ll 1$ (nearly-full cells driving the dynamics), the upper boundary at $q=1$ is distant and the scale invariance holds approximately. For $q \sim \mathcal{O}(1)$, boundary effects modify the scaling.

#### C.5 Physical Interpretation of Scale Invariance

Scale invariance $P(\lambda q) = P(q)/\lambda$ has a concrete physical meaning: **the information potential is a homogeneous function of degree $-1$**. This is the same scaling as:
- Gravitational potential: $V \propto 1/r$ (homogeneous of degree $-1$ in distance)
- Coulomb potential: $V \propto 1/r$
- Ideal gas pressure: $p \propto 1/V$ (homogeneous of degree $-1$ in volume)

In each case, the $-1$ scaling comes from a conservation law (Gauss's law for $1/r$ potentials; $pV = \text{const}$ for ideal gas). For the DGF, the conservation law is the total vacancy $\int q \, d^dx = \text{const}$ — but this alone doesn't fix the degree of homogeneity.

**Conclusion for Path C**: Scale invariance uniquely determines $P(q) = C/q$. This is the strongest mathematical argument among the three paths. The physical justification is that the information potential should scale inversely with capacity — a natural but not logically necessary postulate.

---

### Path D: Extremal Principle (Lagrangian/Variational)

#### D.1 Setup

Can the flux be derived from an action principle? Consider an action functional:
$$S[q] = \int dt \int d^dx \; \mathcal{L}(q, \partial_t q, \nabla q)$$

The Euler-Lagrange equation $\delta S = 0$ yields the equation of motion, which we want to match to the continuity equation with flux $J$.

#### D.2 Symmetry Constraints on $\mathcal{L}$

By Noether's theorem, symmetries of $\mathcal{L}$ correspond to conserved quantities:

1. **Time translation invariance** $\Rightarrow$ energy conservation. The Lagrangian should not depend explicitly on $t$.

2. **Total vacancy conservation** ($\int q \, d^dx = \text{const}$) $\Rightarrow$ the Lagrangian should be invariant under shifts of a potential $\phi$ where $\mathbf{J} = \nabla \phi$. This suggests a gauge structure.

3. **Spatial translation invariance** $\Rightarrow$ momentum conservation (if the lattice is uniform).

#### D.3 The Onsager Variational Principle

A more promising variational approach is the Onsager principle for dissipative systems (Onsager 1931, Doi 2011):

Define the Rayleighian:
$$\mathcal{R}[\dot{q}, q] = \dot{\mathcal{F}}[q] + \Phi[\dot{q}, q]$$

where:
- $\mathcal{F}[q]$ is the free energy functional
- $\Phi[\dot{q}, q] = \frac{1}{2} \int d^dx \, \dot{q} M(q)^{-1} \dot{q}$ is the dissipation function
- $M(q)$ is the mobility

The dynamics follows from minimizing $\mathcal{R}$ with respect to $\dot{q}$:
$$\frac{\delta \mathcal{R}}{\delta \dot{q}} = 0 \quad \Rightarrow \quad \partial_t q = -\nabla \cdot \left(M(q) \nabla \frac{\delta \mathcal{F}}{\delta q}\right)$$

This is the standard gradient flow structure. For the DGF, we need:
$$\partial_t q = \nabla^2(1/q) = \nabla \cdot (q^{-2} \nabla q)$$

Comparing to the Onsager form:
$$\nabla \cdot \left(M(q) \nabla \frac{\delta \mathcal{F}}{\delta q}\right) = -\nabla \cdot (q^{-2} \nabla q)$$

This requires either:
- $M(q) \nabla(\delta\mathcal{F}/\delta q) = -q^{-2} \nabla q$, with $\delta\mathcal{F}/\delta q$ to be determined

One natural choice consistent with the earlier identification (continuum_qfield.md, Theorem 2):
- $M(q) = q$ (mobility proportional to vacant fraction)
- $\mathcal{F}[q] = \int \frac{D_0}{2q} \, d^dx$ (free energy)

Then $\delta\mathcal{F}/\delta q = -D_0/(2q^2)$, and:
$$\partial_t q = +\nabla \cdot \left(q \nabla \frac{D_0}{2q^2}\right) = \nabla \cdot (q \cdot (-D_0/q^3) \nabla q) = -\nabla \cdot (D_0/q^2 \nabla q)$$

Wait — this has the wrong sign. The continuum limit of the DGF gives $\partial_t q = +\nabla^2(1/q) = +\nabla \cdot (q^{-2} \nabla q)$ (it's an **anti-diffusion**: $q$ increases at maxima and decreases at minima).

In the Onsager framework, this means the free energy is being *maximized*, not minimized — the dynamics goes uphill in free energy. This is a signature of an *active* or *driven* system, not a passive relaxational one.

#### D.4 The Correct Variational Structure

The continuum equation $\partial_t q = \nabla^2(1/q)$ can be written as:
$$\partial_t q = -\nabla \cdot \mathbf{J}, \quad \mathbf{J} = -\nabla(1/q) = \frac{1}{q^2} \nabla q$$

This is a **gradient flow** with respect to the functional $\mathcal{G}[q] = \int q^{-1} \, d^dx$, but with the *negative* mobility:
$$\partial_t q = -\nabla \cdot \left(-M_0 \nabla \frac{\delta \mathcal{G}}{\delta q}\right) = +M_0 \nabla^2(1/q)$$

with $\delta\mathcal{G}/\delta q = -1/q^2$ and $M_0 > 0$.

The minus sign in the mobility indicates this is a gradient *ascent*, not descent. This is unusual but well-defined mathematically: it's a Wasserstein gradient flow with negative mobility, corresponding to maximizing $\mathcal{G}$ rather than minimizing it.

#### D.5 What the Variational Approach Reveals

The extremal principle approach reveals that:
1. The flux $J = -\nabla(1/q)$ is the gradient of a potential $1/q$ (in the continuum).
2. The dynamics is a gradient flow (ascent) on the functional $\mathcal{G}[q] = \int q^{-1}$.
3. The choice of potential $\mathcal{G} \propto \int 1/q$ (rather than $\int \log q$ or $\int 1/q^2$) is the **minimal** choice consistent with the existence of a variational principle and the boundary conditions.

However, the variational principle itself does not *derive* $\mathcal{G} = \int 1/q$ — it just repackages the flux choice in a different mathematical language. It is circular: choosing the action $\mathcal{G}$ IS choosing the flux.

**Conclusion for Path D**: The variational approach provides elegant mathematical structure but does not uniquely determine the flux form. Any decreasing $P(q)$ gives a valid gradient flow (ascent) with $\mathcal{G} = \int P(q) d^dx$. The variational principle is descriptive, not prescriptive.

---

## 3. Comparative Analysis

### 3.1 Summary Table

| Path | Potential $P(q)$ | $D(q) = -P'(q)$ | Uniquely determines $P$? | Extra assumptions |
|------|-----------------|-----------------|------------------------|-------------------|
| **A**: Shannon entropy | $\log\frac{1-q}{q}$ | $\frac{1}{q(1-q)}$ | Yes, from entropy | None beyond standard stat mech |
| **B**: Info pressure | $\frac{1}{q}$ | $\frac{1}{q^2}$ | No (infinitely many decreasing functions) | $P \propto 1/q$ is a postulate |
| **C**: Scale invariance | $\frac{C}{q}$ | $\frac{C}{q^2}$ | **Yes**, from $P(\lambda q)=P(q)/\lambda$ | Scale invariance of potential |
| **D**: Extremal principle | Any decreasing $P$ | $-P'(q)$ | No | Choice of action functional |

### 3.2 Path A: Why It Fails

Path A is the most "principled" in the sense that it uses only standard information theory (Shannon entropy + Onsager linear response). It fails because the Shannon entropy treats $q$ and $1-q$ symmetrically, while the DGF dynamics is fundamentally asymmetric: information flows from occupied (low $q$) to vacant (high $q$).

This asymmetry is encoded in A1 (injectivity) — the dynamics is a permutation, which preserves the total number of configurations but does NOT treat $q \leftrightarrow 1-q$ symmetrically in terms of rates. The Shannon entropy captures the *static* counting of states, but the *dynamic* rates are a separate ingredient.

**Path A gives the wrong answer not because the entropy argument is wrong, but because the Onsager coefficient $\Gamma$ is not constant — it must depend on $q$ to break the $q \leftrightarrow 1-q$ symmetry.**

Specifically, if we allow a state-dependent Onsager coefficient $\Gamma(q)$:
$$J = \Gamma(\bar{q}) [\mu(q_i) - \mu(q_j)]$$

where $\bar{q} = (q_i + q_j)/2$. If $\Gamma(q) \propto q^{-1}$, then:
$$J \propto \frac{1}{q} \cdot \frac{q_j - q_i}{q(1-q)} \approx \frac{q_j - q_i}{q^2} \quad \text{for small } q$$

This recovers the $1/q^2$ diffusivity! The additional $1/q$ factor in the mobility breaks the $q \leftrightarrow 1-q$ symmetry.

So Path A can be *salvaged* by introducing a state-dependent kinetic coefficient. The corrected form is:
$$J_{i\to j} = \Gamma(q_i, q_j) \left[\log\frac{1-q_i}{q_i} - \log\frac{1-q_j}{q_j}\right]$$

with $\Gamma(q_i, q_j) \propto 1/\sqrt{q_i q_j}$ (or some symmetric average). In the small-$q$ limit this reduces to $J \propto 1/q_i - 1/q_j$ because:
$$\frac{1}{\sqrt{q_i q_j}} \log\frac{q_j}{q_i} \approx \frac{q_j - q_i}{q_i^{3/2} q_j^{1/2}}$$

Hmm, this doesn't quite give $1/q_i - 1/q_j$. Let me be more careful.

For $q \ll 1$, $\mu(q) \approx -\log q$. The flux with state-dependent mobility $\Gamma$:
$$J = \Gamma(q_i, q_j) (\log q_j - \log q_i) = \Gamma(q_i, q_j) \log(q_j/q_i)$$

For small differences $\Delta = q_j - q_i \ll q_i$:
$$\log(q_j/q_i) \approx \frac{\Delta}{q_i}$$

So $J \approx \Gamma(q_i, q_i) \cdot \Delta / q_i$. For this to match $1/q_i - 1/q_j \approx \Delta/q_i^2$, we need $\Gamma \propto 1/q$.

Thus, the "salvaged Path A" requires $\Gamma(q) \propto 1/q$, which is equivalent to postulating $D(q) \propto 1/q^2$ — it just repackages the same assumption in different notation.

### 3.3 Path C: The Most Promising

Path C (scale invariance) is the only path that **uniquely** determines $P(q) = C/q$ from a simple, physically interpretable postulate. The postulate $P(\lambda q) = P(q)/\lambda$ is:
- Mathematically precise (a functional equation with unique solution)
- Physically interpretable (capacity doubling $\Rightarrow$ pressure halving)
- Consistent with known physics (ideal gas law, $1/r$ potentials)
- Minimal — it uses only scaling symmetry, no additional microscopic assumptions

The weakness is that scale invariance is an *assumption*, not a theorem. It cannot be derived from A1+A2+A3. But it is arguably the *simplest* assumption that selects a unique flux form.

### 3.4 An Alternative Argument: The "Matching Condition"

Here is a different argument that may strengthen Path C. Consider two adjacent cells with vacant fractions $q_1, q_2$. The total free capacity is $q_1 + q_2$ (in appropriate units). The information flux between them should satisfy:

**Matching condition**: If two pairs of cells $(q_1, q_2)$ and $(q_1', q_2')$ have the same ratio $q_2/q_1 = q_2'/q_1'$, then the flux should scale as $J(q_1', q_2') = (q_1/q_1') J(q_1, q_2)$.

The physical reasoning: the ratio $q_2/q_1$ sets the "gradient direction," while the overall scale $q_1$ (or $q_2$) sets the "magnitude" — smaller $q$ means larger flux (more pressure). This scaling is:
$$J(\lambda q_1, \lambda q_2) = \frac{1}{\lambda} J(q_1, q_2)$$

which is precisely the scale invariance condition. Combined with additive separability ($J = P(q_1) - P(q_2)$), this forces $P(q) = C/q$.

---

## 4. The Minimal Additional Assumption

### 4.1 What Cannot Be Derived

**Honest statement**: The flux functional form $J(q_i, q_j)$ CANNOT be uniquely derived from A1+A2+A3 alone.

Reason: A1+A2+A3 constrain the kinematics (permutations preserving occupation number) but not the dynamics (rates of specific permutations). The flux $J$ is a rate — it specifies how fast information moves. The axioms leave an infinite-dimensional space of possible rate functions. This is exactly the same situation as in classical statistical mechanics: the Hamiltonian determines the phase space and conserved quantities, but the transport coefficients (viscosity, thermal conductivity, diffusion constant) require additional input (Boltzmann equation, Green-Kubo relations, etc.).

### 4.2 What CAN Be Derived

Given additional assumptions, specific flux forms can be derived:

1. **Additive separability** ($J = P(q_i) - P(q_j)$) follows from the loop condition (no information vortices). This is a natural but not logically necessary postulate.

2. **The functional form $P(q)$ is constrained** by C1-C5 to be decreasing with $P'(0) = -\infty$.

3. **Scale invariance uniquely picks $P(q) = C/q$.**

### 4.3 Proposed Axiom A5

If we wish to formalize the flux derivation, the minimal additional axiom is:

> **Axiom A5 (Scale-Invariant Information Potential)**: There exists a scalar information potential $P: (0,1) \to \mathbb{R}^+$ such that:
> (a) The information flux between adjacent cells is $J_{i\to j} = P(q_i) - P(q_j)$.
> (b) $P$ is scale-invariant: $P(\lambda q) = \lambda^{-1} P(q)$ for all $\lambda > 0$ and $q \in (0, 1/\lambda)$.
>
> Equivalently: $J(\lambda q_i, \lambda q_j) = \lambda^{-1} J(q_i, q_j)$.

Part (a) encodes the loop condition (no information vortices). Part (b) encodes scale invariance. Together they uniquely imply $J_{i\to j} = C(1/q_i - 1/q_j)$.

### 4.4 Alternative Minimal Assumptions

If scale invariance seems too strong, one could instead postulate:

**A5' (Information Pressure ∼ Occupied/Free ratio)**: $P(q) = \alpha \cdot (\text{occupied fraction})/(\text{vacant fraction}) = \alpha(1-q)/q$.

This is equivalent to $P(q) \propto 1/q$ for $q \ll 1$, with the benefit of being well-behaved at $q \to 1$ (since $P(1) = 0$). The flux would be:
$$J_{i\to j} = \alpha\left(\frac{1-q_i}{q_i} - \frac{1-q_j}{q_j}\right) = \alpha\left(\frac{1}{q_i} - \frac{1}{q_j}\right)$$

This is identical to $1/q_i - 1/q_j$ (the constant shift cancels).

Or even more minimally:

**A5'' (Simplicity/Occam's Razor)**: Among all decreasing functions $P(q)$ with $P'(0) = -\infty$, the function $P(q) = 1/q$ is the simplest (fewest parameters, lowest degree rational function).

This is not a physical argument but a methodological one. It is commonly used in physics (e.g., linear response theory picks the linear term in a Taylor expansion).

---

## 5. Honest Conclusion

### 5.1 What the Paper Should Say

The current paper claims (or implies) that $J = 1/q_i - 1/q_j$ follows from the DGF framework. This should be **corrected** to:

> The discrete flux $J_{i\to j} = q_i^{-1} - q_j^{-1}$ is a constitutive ansatz. It is not uniquely determined by axioms A1-A3. Among all flux functions satisfying the physical constraints (C1-C5), this form is selected by the additional postulate of scale invariance: $P(\lambda q) = \lambda^{-1} P(q)$, which is the unique functional equation yielding $P(q) \propto 1/q$. This postulate has a clear physical interpretation: doubling the free capacity of all cells halves the information pressure between them.

### 5.2 Sensitivity Analysis

A crucial question: **how sensitive are the paper's conclusions to the choice of flux form?**

If $P(q) = -\log q$ (Path A, small-$q$ limit), the continuum equation becomes:
$$\partial_t q = \nabla^2(-\log q) = \nabla \cdot (q^{-1} \nabla q)$$

with $D(q) = 1/q$ instead of $1/q^2$. This is still a fast diffusion equation ($m = 0$, logarithmic diffusion) but with weaker singularity at $q=0$. The key qualitative features likely persist:
- Finite-time singularity formation (weaker but still present)
- Domain separation (entropic $q=1/2$ vs. singular $q=0$)
- Uphill diffusion character

However, the **quantitative** predictions (phase boundaries, critical exponents, time scales) would change. This sensitivity should be acknowledged.

### 5.3 Bottom Line

| Question | Answer |
|----------|--------|
| Can $J = 1/q_i - 1/q_j$ be derived from A1+A2+A3? | **No.** |
| What is the minimal additional assumption? | Scale invariance $P(\lambda q) = P(q)/\lambda$, or equivalently A5. |
| Is this assumption physically reasonable? | **Yes.** It has clear physical interpretation and is the simplest choice satisfying all constraints. |
| Are there alternative flux forms that satisfy all constraints? | **Yes, infinitely many.** Any decreasing $P(q)$ with $P'(0) = -\infty$ works. |
| Does this undermine the paper? | **Not necessarily.** The paper's conclusions may be robust to the choice of $P$, provided the qualitative features (singularity at $q=0$, uphill diffusion) are preserved. This should be checked. |
| Which path is most promising for a principled derivation? | **Path C** (scale invariance) supplemented by the loop condition. Path A (Shannon entropy) can be salvaged with a state-dependent Onsager coefficient. |

---

## Appendix A: The Loop Condition as a Physical Principle

The loop condition $J_{i\to j} + J_{j\to k} + J_{k\to i} = 0$ is equivalent to the existence of a potential $P(q)$. Why should we believe this?

**Argument from thermodynamics**: In equilibrium thermodynamics, all fluxes are driven by gradients of intensive variables (temperature, pressure, chemical potential). The flux between two systems depends only on the values of these variables at the two systems — this is the "zeroth law" generalized to transport. Information flux in the DGF should follow the same logical structure.

**Argument from information theory**: The information content of a cell is a function of its state $q$. The "driving force" for information transfer should be the difference in some information-theoretic potential. This is a standard assumption in nonequilibrium thermodynamics (Onsager reciprocity).

**Counterargument**: In turbulent or active systems, fluxes can have non-potential (solenoidal) components. If the DGF dynamics has "information vortices," the loop condition would fail. But the simplest (and most natural) assumption is that it holds in the absence of external driving.

## Appendix B: Connection to Known Physics

### B.1 Fast Diffusion Equations

The continuum limit $\partial_t q = \nabla^2(q^{-1})$ belongs to the class:
$$\partial_t u = \nabla^2(u^m), \quad m = -1$$

This is the **very fast diffusion** regime ($m < 0$). Key known results (Vazquez 2007, *The Porous Medium Equation*):
- $m = 0$: logarithmic diffusion, $\partial_t u = \nabla^2(\log u)$
- $m = -1$: inverse diffusion, $\partial_t u = \nabla^2(u^{-1})$
- For $m < 0$, the diffusivity $D(u) = |m| u^{m-1}$ diverges as $u \to 0$
- Finite-time extinction (for $m < 1$ in subcritical dimensions) vs. finite-time blowup

The DGF with $m = -1$ is at the boundary of known theory — most rigorous results are for $m > 0$ (porous medium) or $0 < m < 1$ (fast diffusion). The $m < 0$ regime is mathematically challenging and physically unusual.

### B.2 Onsager Relations

In Onsager's theory, fluxes $J_\alpha$ and forces $X_\beta$ are related by:
$$J_\alpha = \sum_\beta L_{\alpha\beta} X_\beta$$

with symmetric Onsager coefficients $L_{\alpha\beta} = L_{\beta\alpha}$. For the DGF, the thermodynamic force is $X = \nabla(\delta S/\delta q)$, and the Onsager coefficient $L$ can be state-dependent. The flux $J = 1/q_i - 1/q_j$ corresponds to:
$$L(q) \propto \frac{1}{q}, \quad X = \nabla\left(\frac{1}{q}\right)$$

or equivalently:
$$L(q) \propto 1, \quad X = \nabla\left(\frac{1}{q}\right)$$

The state-dependent mobility $L(q) \propto 1/q$ has a natural interpretation: the mobility for information transfer is inversely proportional to the vacant fraction — fuller cells are more "mobile" in terms of information outflow.

### B.3 Exclusion Processes

The simple symmetric exclusion process (SEP) on a lattice has flux:
$$J_{i\to j}^{\text{SEP}} = \frac{1}{2}[n_i(1-n_j) - n_j(1-n_i)]$$

where $n_i \in \{0,1\}$. In the continuum limit (hydrodynamic limit), this gives standard diffusion: $\partial_t \rho = \nabla^2 \rho$.

The DGF flux $J = 1/q_i - 1/q_j$ is fundamentally different from SEP — it is an "anti-exclusion" process where the jump rate INCREASES when the target cell is full (low $q$). This is the opposite of the exclusion principle.

---

## References

1. Onsager, L. (1931). Reciprocal relations in irreversible processes. *Physical Review*, 37, 405-426; 38, 2265-2279.
2. Vazquez, J.L. (2007). *The Porous Medium Equation: Mathematical Theory*. Oxford University Press.
3. Doi, M. (2011). Onsager's variational principle in soft matter. *Journal of Physics: Condensed Matter*, 23, 284118.
4. Cover, T.M. & Thomas, J.A. (2006). *Elements of Information Theory*, 2nd ed. Wiley.
5. Kipnis, C. & Landim, C. (1999). *Scaling Limits of Interacting Particle Systems*. Springer.
6. Spohn, H. (1991). *Large Scale Dynamics of Interacting Particles*. Springer.
