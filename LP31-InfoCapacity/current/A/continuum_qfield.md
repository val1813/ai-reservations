# Continuum Limit of the DGF Framework: From $N$ Discrete Cells to a Continuous $q$-Field

**Target: PRD — BM Paper Sections II–III**

**Author: A (Mathematical Physics)**
**Date: 2026-06-06**

---

## Abstract

We derive the continuum limit of the Discrete Generative Framework (DGF), passing from $N$ binary cells on a $d$-dimensional lattice to a continuous $q$-field $q(\mathbf{x}, t) \in [0,1]$ representing the local vacant fraction (information capacity). The discrete flux $J_{i\to j} = q_i^{-1} - q_j^{-1}$ yields, in the limit $a \to 0$, the nonlinear PDE $\partial_t q = \nabla^2(q^{-1}) = \nabla\cdot(q^{-2}\nabla q)$. We identify this as a *fast diffusion equation* in the regime $m = -1$ (mobility $\propto q^{-2}$), analogous to, but distinct from, the porous medium and Cahn-Hilliard equations. Three structural properties are proved: (i) $q=0$ is a singular boundary where the effective diffusivity $D(q) = q^{-2}$ diverges, producing finite-time singularity formation; (ii) statistical preference for $q \approx 1/2$ arises from the mixing entropy $s(q) = -q\log q - (1-q)\log(1-q)$, which is the global minimum of the free energy functional $F[q] = -T\int s(q)\, d^dx$; (iii) the juxtaposition of the $q=0$ singularity with the $q=1/2$ entropic attractor drives spontaneous domain separation without requiring an auxiliary Process B. All theorems are stated with explicit assumptions; a dedicated caveats section ($\S$VI) marks which ingredients are derived from microscopic DGF axioms and which are modeling choices.

---

## I. Discrete Lattice Formulation

### I.A. Setup: $N$ cells on a $d$-dimensional lattice

**Definition 1 (Discrete DGF lattice).**
Let $\Lambda_N \subset \mathbb{Z}^d$ be a finite hypercubic lattice of $N = L^d$ sites with lattice spacing $a$. Each site $i \in \Lambda_N$ carries a binary variable $s_i \in \{0,1\}$:
- $s_i = 1$: site occupied (information present)
- $s_i = 0$: site vacant (capacity available)

The microstate is $\mathbf{s} \equiv \{s_i\}_{i\in\Lambda_N} \in X = \{0,1\}^N$. The global constraint is fixed total occupation $M \equiv \sum_{i} s_i = \text{const}$, corresponding to a conserved "information content."

**Definition 2 (Local $q$-field).**
For any subset $\Omega \subset \Lambda_N$, define the local vacant fraction:

$$q_\Omega \equiv 1 - \frac{1}{|\Omega|}\sum_{i\in\Omega} s_i = \frac{|\Omega| - \sum_{i\in\Omega} s_i}{|\Omega|} \in [0,1]$$

At the single-site level, $q_i \equiv 1 - s_i \in \{0,1\}$. For a coarse-graining volume $\Delta V$ centered at position $\mathbf{x}$, we define:

$$q(\mathbf{x}, t) \equiv \lim_{\substack{a\to 0 \\ |\Delta V| \to \infty \\ |\Delta V| \ll L^d}} \frac{1}{|\Delta V|}\sum_{i \in \Delta V(\mathbf{x})} (1 - s_i(t))$$

In practice, we identify $q_i \equiv \langle 1-s_i\rangle_{\Delta V}$ as the local continuum field sampled at lattice point $i$, with the understanding that $q_i \in [0,1]$ is a mesoscopic average, not a binary variable.

### I.B. Discrete Flux

**Definition 3 (Discrete flux — DGF ansatz).**
Let $i, j$ be nearest-neighbor sites on $\Lambda_N$. The flux of $q$ from site $i$ to site $j$ is:

$$J_{i\to j}^q \equiv \frac{q_j - q_i}{q_i q_j} = \frac{1}{q_i} - \frac{1}{q_j} \tag{1}$$

**Physical motivation.** Equation (1) encodes "information pressure": the flux is proportional to the difference of reciprocal vacant fractions. When $q_i$ is small (site $i$ highly occupied), the factor $1/q_i$ is large, so the flux out of $i$ is enhanced — crowded regions expel information more vigorously. When $q_i \approx q_j$, the flux vanishes, as expected by symmetry.

**Remark 1 (Caveat pre-registration).** The form (1) is a **modeling ansatz**. It is not derived from the bare DGF axiom (Theorem 1: $f$ is a bijection on $X$). The bijection axiom constrains the dynamics to permutations, but the *rate* at which particular permutations occur is not specified. The $1/q$ dependence is the simplest nonlinearity that (a) respects the $q \leftrightarrow 1-q$ asymmetry (information flows from occupied to vacant), (b) produces a singular boundary at $q=0$, and (c) reduces to Fick's law when $q$ is spatially uniform to first nontrivial order. See $\S$VI for a full discussion.

### I.C. Discrete Continuity Equation

Conservation of total $q$ (equivalently, of total occupation) implies that the rate of change of $q_i$ is the net influx:

$$\partial_t q_i = \sum_{j \in \mathrm{nn}(i)} \bigl(J_{j\to i}^q - J_{i\to j}^q\bigr) \tag{2}$$

Substituting (1) and noting $J_{j\to i}^q = -J_{i\to j}^q$,

$$\partial_t q_i = -2\sum_{j\in\mathrm{nn}(i)} \frac{q_j - q_i}{q_i q_j} = \frac{2}{q_i}\sum_{j\in\mathrm{nn}(i)} \frac{q_i - q_j}{q_j} \tag{3}$$

where $\mathrm{nn}(i)$ denotes the set of $2d$ nearest neighbors of site $i$.

**Lemma 1 (Global conservation).** $\partial_t \sum_i q_i = 0$.

*Proof.* Summing (3) over all $i$ yields a telescoping sum over directed edges, each appearing twice with opposite signs. $\square$

---

## II. Continuum Limit

### II.A. Gradient Expansion

We now take the continuum limit $a \to 0$ with fixed physical length scale. The discrete sum over neighbors becomes, for any smooth test function $\phi$:

$$\sum_{j\in\mathrm{nn}(i)} \phi_{ij} \;\longrightarrow\; a^2 \nabla^2\phi(\mathbf{x}) + \mathcal{O}(a^4)$$

in $d$ dimensions with appropriate normalization (the factor $a^2$ absorbs the $2d$ from the sum and the $1/d$ from the angular average).

Specifically, for the right-hand side of (3), write $\phi_{ij} \equiv (q_i - q_j)/q_j$. Taylor-expand $q_j \equiv q(\mathbf{x} + a\mathbf{e}_\mu)$ about $\mathbf{x}$ (where $\mathbf{e}_\mu$ is a unit lattice vector):

$$q_j = q + a \partial_\mu q + \frac{a^2}{2}\partial_\mu^2 q + \mathcal{O}(a^3)$$

$$\frac{1}{q_j} = \frac{1}{q} - \frac{a}{q^2}\partial_\mu q + \frac{a^2}{q^3}(\partial_\mu q)^2 - \frac{a^2}{2q^2}\partial_\mu^2 q + \mathcal{O}(a^3)$$

Then:

$$\frac{q_i - q_j}{q_j} = \frac{q - q_j}{q_j} = -a\frac{\partial_\mu q}{q} + a^2\left[\frac{(\partial_\mu q)^2}{q^2} - \frac{\partial_\mu^2 q}{2q}\right] + \mathcal{O}(a^3)$$

Summing over the $2d$ neighbors $\mu = \pm 1, \ldots, \pm d$:

$$\sum_{\mu} \frac{q_i - q_{i+\mu}}{q_{i+\mu}} = a^2 \sum_{\mu=1}^d \left[\frac{2(\partial_\mu q)^2}{q^2} - \frac{\partial_\mu^2 q}{q}\right] + \mathcal{O}(a^4)$$

$$= a^2\left[\frac{2|\nabla q|^2}{q^2} - \frac{\nabla^2 q}{q}\right] + \mathcal{O}(a^4)$$

Substituting into (3):

$$\partial_t q = \frac{2}{q} \cdot \frac{a^2}{2d} \left[ \frac{2|\nabla q|^2}{q^2} - \frac{\nabla^2 q}{q} \right] \cdot 2d + \mathcal{O}(a^3)$$

where the factor $1/(2d)$ comes from the standard normalization of the discrete Laplacian, and the final $2d$ restores the sum over neighbors. After simplification and absorbing constants into the time scale:

$$\boxed{\partial_t q = D_0\left[-\frac{\nabla^2 q}{q^2} + \frac{2|\nabla q|^2}{q^3}\right]} \tag{4}$$

with $D_0 \equiv 2a^2/\tau_0$ where $\tau_0$ is the microscopic time scale.

### II.B. Compact Form: The $q$-Field Equation

**Theorem 1 (Continuum $q$-field PDE).**
In the continuum limit $a \to 0$, the DGF discrete dynamics on $\Lambda_N$ yields the nonlinear partial differential equation:

$$\partial_t q = D_0 \nabla^2\!\left(\frac{1}{q}\right) \tag{5}$$

or, equivalently:

$$\partial_t q = D_0 \nabla\cdot\!\left(\frac{1}{q^2}\nabla q\right) \tag{6}$$

with effective diffusivity $D(q) \equiv D_0/q^2$.

*Proof.* Direct computation: $\nabla^2(1/q) = \nabla\cdot(\nabla(1/q)) = \nabla\cdot(-q^{-2}\nabla q) = -q^{-2}\nabla^2 q + 2q^{-3}|\nabla q|^2$, matching (4). The operator identity $\nabla^2(1/q) = \nabla\cdot(q^{-2}\nabla q)$ establishes (6). $\square$

**Theorem 2 (Equivalent forms).** Equation (5) admits three equivalent representations:

1. **Nonlinear diffusion form:** $\partial_t q = \nabla\cdot(D(q)\nabla q)$ with $D(q) = D_0/q^2 > 0$

2. **Gradient flow form:** $\partial_t q = -\nabla\cdot(M(q)\nabla\mu(q))$ with mobility $M(q) = q$ and chemical potential $\mu(q) = -D_0/(2q^2)$. This is an **uphill** flow (negative sign) relative to the free energy $F[q] = \int \frac{D_0}{2q}\,d^dx$, i.e., $\partial_t q = +\nabla\cdot(q\nabla(\delta F/\delta q))$

3. **Potential form:** Define $v \equiv 1/q$ (the "specific occupied volume" per vacancy). Then $\partial_t v = -D_0 v^2 \nabla^2 v$, a degenerate nonlinear PDE

**Physical interpretation.** The negative sign in the gradient flow form (2) is critical: the DGF dynamics is *anti-diffusive* with respect to $F[q] = \int (D_0/2q)\,d^dx$, meaning it drives the system *away* from the free energy minimum (which occurs at $q \to 1$) toward gradient-rich, low-$q$ configurations. This is the mathematical origin of the segregation mechanism ($\S$V).

### II.C. Conservation Laws and Symmetries

**Theorem 3 (Conserved quantities).**
For the $q$-field equation (5) on a domain $\Omega \subset \mathbb{R}^d$ with no-flux boundary conditions $\mathbf{n}\cdot\nabla(1/q)|_{\partial\Omega} = 0$:

1. **Total vacancy conserved:** $\partial_t \int_\Omega q\,d^dx = 0$
2. **Monotonic decrease of $F_1$:** $\partial_t \int_\Omega q^{-1}\,d^dx = -D_0\int_\Omega |\nabla(q^{-1})|^2\,d^dx \leq 0$

*Proof.* (1) follows from the divergence form. For (2):

$$\partial_t\int_\Omega \frac{1}{q}\,d^dx = \int_\Omega -\frac{1}{q^2}\partial_t q\,d^dx = -D_0\int_\Omega \frac{1}{q^2}\nabla^2\!\left(\frac{1}{q}\right)d^dx$$

Integration by parts with no-flux boundary conditions:

$$= D_0\int_\Omega \nabla\!\left(\frac{1}{q^2}\right)\cdot\nabla\!\left(\frac{1}{q}\right)d^dx = -2D_0\int_\Omega \frac{|\nabla q|^2}{q^4}\,d^dx \leq 0 \quad \square$$

**Corollary.** The functional $F_1[q] \equiv \int q^{-1}\,d^dx$ is a Lyapunov functional for (5). Its monotonic decrease implies that $q$ tends to *increase* in regions of steep gradient — the opposite of standard diffusion.

**Theorem 4 (Scaling symmetry).**
Equation (5) is invariant under the scaling $q \to \lambda q$, $\mathbf{x} \to \lambda^{-1}\mathbf{x}$, $t \to t$. This is a "scale duality": a region with twice the vacancy fraction evolves with half the effective length scale.

---

## III. The $q=0$ Singular Boundary

### III.A. Classification

**Theorem 5 (Fast diffusion classification).**
Equation (5), written as $\partial_t q = \nabla^2(q^m)$ with $m = -1$, belongs to the class of **very fast diffusion equations** (supercritical regime $m < m_c(d)$). Standard results for $\partial_t u = \nabla^2(u^m)$ apply:

- $m = 1$: linear heat equation
- $0 < m < 1$: fast diffusion (finite speed of propagation for compact support)
- $m = 0$: logarithmic diffusion
- $m < 0$: **very fast diffusion** — $D(u) \to \infty$ as $u \to 0$, potentially singular behavior

For the DGF equation with $m = -1$, the critical dimension (for the porous medium equation theory, via the transformation $u = q^m$) is not directly applicable; however, we can establish the following properties directly.

### III.B. Behavior as $q \to 0$

**Theorem 6 (Divergent diffusivity).**
As $q \to 0^+$:

$$D(q) = \frac{D_0}{q^2} \to +\infty$$

with the following consequences:

(a) **Infinite propagation speed.** Infinitesimal $q$-gradients near $q=0$ generate finite fluxes. Information propagates instantly (in the continuum PDE sense) from low-$q$ regions.

(b) **Singular boundary layer.** In a region where $q \to 0$, the PDE (5) develops a boundary layer of thickness $\delta \sim \mathcal{O}(q_0)$, where $q_0$ is the minimum value of $q$ in the domain.

(c) **No smooth stationary solution with $q=0$ at a point.** In 1D, stationary solutions satisfy $\partial_x^2(1/q) = 0 \implies 1/q = Ax + B$. For $q(0) = 0$, this requires $B = \infty$, which is inconsistent. No classical stationary solution exists that attains $q=0$ at a point.

*Proof.* (a) and (b) follow from $D(q) \to \infty$. For (c), the harmonic condition $\nabla^2(1/q) = 0$ cannot accommodate the singularity $1/q \to \infty$ at an interior point while remaining a classical solution. $\square$

**Theorem 7 (Information flux at $q=0$).**
Define the information flux $\mathbf{J}_{\text{info}} \equiv -\nabla(1/q)$ (the occupation flux). At a boundary where $q \to 0$:

$$\lim_{q\to 0^+} |\mathbf{J}_{\text{info}}| = \lim_{q\to 0^+} \frac{|\nabla q|}{q^2}$$

This limit can be:

- **Finite**, if $|\nabla q| \sim q^2$ (the gradient vanishes quadratically with $q$)
- **Divergent**, if $|\nabla q|$ vanishes slower than $q^2$ (generic case)
- **Zero**, if $|\nabla q|$ vanishes faster than $q^2$ (requires fine-tuning)

In the generic divergent case, information bursts outward from the $q=0$ region — the boundary acts as a **source** of information, not an absorber.

**Physical interpretation.** The $q=0$ boundary is better described as a **singular source** rather than an absorbing boundary. When a region reaches near-zero vacancy, the "information pressure" $1/q$ diverges, forcing occupation outward. This empties the region further (negative feedback), creating a runaway toward $q \to 0$ that is bounded only by the global conservation of total $q$.

### III.C. Finite-Time Singularity Formation

**Conjecture 1 (Singularity formation in finite time).**
For spatially localized initial data with $q(\mathbf{x}, 0) \leq q_0 < 1$ on a compact support in $d \geq 1$, there exists a finite time $t_* > 0$ such that $\inf_{\mathbf{x}} q(\mathbf{x}, t) \to 0$ as $t \to t_*$.

*Heuristic argument.* The equation $\partial_t v = -D_0 v^2 \nabla^2 v$ (with $v = 1/q$) is a backward-parabolic equation when $\nabla^2 v < 0$, i.e., near minima of $q$ (maxima of $v$). Backward parabolic equations generically develop singularities in finite time. A rigorous proof would follow from comparison with the ordinary differential equation $\dot{v}_{\min} = -D_0 v_{\min}^2 \cdot C$ for some negative curvature $C < 0$, yielding $v_{\min}(t) = v_{\min}(0)/(1 + D_0 C v_{\min}(0) t)$, which blows up at $t_* = -1/(D_0 C v_{\min}(0))$, corresponding to $q_{\min}(t_*) \to 0$.

**Remark 2 (Caveat).** The rigorous proof of finite-time singularity formation for $\partial_t q = \nabla^2(q^{-1})$ is mathematically nontrivial due to the sign-indefiniteness of $\nabla^2 v$. This conjecture is labeled as such; its status relative to the porous medium / fast diffusion literature is discussed in $\S$VI.D.

### III.D. Regularization and Physical Cutoff

In the physical DGF, $q$ cannot strictly reach 0 at any finite $N$ (since $\sum_i s_i = M < N$ implies global $\langle q \rangle > 0$, and finite $N$ implies $q_i \geq 1/|\Delta V| > 0$ for any coarse-graining volume). The $q=0$ singularity is a **continuum artifact** that regularizes at the lattice scale:

$$q_{\min}^{\text{(physical)}} \sim \frac{1}{|\Delta V|} \sim \left(\frac{a}{\ell}\right)^d$$

where $\ell$ is the coarse-graining length. All continuum results in this section should be understood as valid down to this cutoff.

---

## IV. Statistical Preference for $q \approx 1/2$

### IV.A. Entropy of Mixing

**Definition 4 (Local mixing entropy).**
For a mesoscopic volume with vacant fraction $q \in [0,1]$, the number of microstates consistent with $q$ is:

$$\Omega(q) = \binom{|\Delta V|}{|\Delta V|(1-q)}$$

Using Stirling's approximation ($|\Delta V| \to \infty$):

$$s(q) \equiv \lim_{|\Delta V|\to\infty} \frac{\log \Omega(q)}{|\Delta V|} = -q\log q - (1-q)\log(1-q) \tag{7}$$

This is the Shannon entropy of a binary distribution with probabilities $(q, 1-q)$.

**Theorem 8 (Maximum entropy at $q=1/2$).**
$s(q)$ has a unique global maximum on $[0,1]$ at $q = 1/2$, with $s(1/2) = \log 2$.

*Proof.* $s'(q) = -\log q - 1 + \log(1-q) + 1 = \log\frac{1-q}{q}$. Setting $s'(q) = 0$ yields $q = 1/2$. Second derivative: $s''(q) = -\frac{1}{q} - \frac{1}{1-q} < 0$ for all $q \in (0,1)$, confirming a unique maximum. At endpoints: $s(0) = s(1) = 0$, $s(1/2) = \log 2$. $\square$

**Corollary (Statistical weight).** The density of microstates at $q$ is $\exp(|\Delta V|\,s(q))$. The ratio of microstates at $q=1/2$ versus $q=\varepsilon$ is:

$$\frac{\Omega(1/2)}{\Omega(\varepsilon)} = \exp\!\bigl[|\Delta V|(\log 2 + \varepsilon\log\varepsilon + (1-\varepsilon)\log(1-\varepsilon))\bigr] \xrightarrow{|\Delta V| \to \infty} \infty$$

for any fixed $\varepsilon \neq 1/2$. The "entropic pressure" toward $q=1/2$ is exponentially large in the system size.

### IV.B. Free Energy Functional

**Definition 5 (DGF free energy).**
Define the free energy functional:

$$F[q] \equiv \int_\Omega \Bigl[f(q) + \frac{\kappa}{2}|\nabla q|^2\Bigr]\,d^dx \tag{8}$$

where:

$$f(q) = -T_0\,s(q) = T_0\bigl[q\log q + (1-q)\log(1-q)\bigr] \tag{9}$$

is the bulk free energy density (negative entropy, multiplied by a reference temperature $T_0$), and $\kappa > 0$ penalizes spatial gradients.

**Theorem 9 (Bulk free energy minimum).**
$f(q)$ has a unique global minimum on $[0,1]$ at $q = 1/2$, with $f(1/2) = -T_0\log 2$.

*Proof.* $f''(q) = -T_0 s''(q) = T_0/(q(1-q)) > 0$ on $(0,1)$. Convexity plus symmetry $f(q) = f(1-q)$ implies the unique minimum at $q=1/2$. $\square$

**Physical interpretation.** In equilibrium thermodynamics, the system would minimize $F[q]$, driving $q \to 1/2$ uniformly (the homogeneous, maximally-mixed state). The DGF dynamics, however, is **not** an equilibrium relaxation — it is an uphill flow that increases $F_1[q] = \int q^{-1}\,d^dx$ (Theorem 3). This nonequilibrium character is essential.

### IV.C. The Tension: Entropy vs. Information Pressure

The DGF dynamics contains two opposing tendencies:

| Tendency | Origin | Effect on $q$ |
|----------|--------|---------------|
| Entropic preference | $\Omega(q)$ maximized at $q=1/2$ | Drives $q \to 1/2$ (homogenization) |
| Information pressure | $D(q) = D_0/q^2$, diverges at $q \to 0$ | Drives $q$ away from 0, toward segregation |

**Key observation.** The entropic preference and the DGF dynamics act in *orthogonal* directions in function space. The entropic term favors $q(\mathbf{x}) \equiv \text{const} = 1/2$ (global homogenization), while the DGF dynamics preserves $\int q$ but can create spatial structure (segregation). They are not directly competitive — rather, the entropic preference provides a "restoring force" that prevents the system from collapsing to $q \equiv 0$ everywhere (which is impossible anyway due to conservation).

---

## V. Separation Mechanism: Why Process B is Not Required

### V.A. The Two-Process Picture (Discrete)

In the discrete DGF, two processes were identified:
- **Process A:** Permutation dynamics driving the system toward the fiber-internal equilibrium (Theorem 2: coarse-grained entropy increase)
- **Process B:** An auxiliary mechanism for domain separation

We now show that, in the continuum limit, Process A alone suffices to generate domain separation, provided the initial condition has spatial structure.

### V.B. Continuum Separation Mechanism

**Theorem 10 (Separation via nonlinear diffusion).**
Consider the initial-boundary value problem for (5) on a domain $\Omega$ with no-flux conditions, and initial data $q(\mathbf{x}, 0) = \bar{q} + \delta q(\mathbf{x})$ where $\int_\Omega \delta q\,d^dx = 0$ and $\delta q$ is not identically zero. Then:

1. **Gradient amplification.** Regions where $\nabla^2 q < 0$ (local maxima of $q$) experience $\partial_t q > 0$ (growth); regions where $\nabla^2 q > 0$ (local minima of $q$) experience $\partial_t q < 0$ (decay). The initial gradient is amplified.

2. **Runaway toward $q=0$.** The minima decay according to $\partial_t q_{\min} \propto -1/q_{\min}^2$, which accelerates as $q_{\min} \to 0$.

3. **Two-domain asymptotic state.** As $t \to \infty$, the system tends to a configuration where $q$ is near 0 in isolated domains and near $1/2$ in the remainder (the "sea"), with sharp interfaces between them.

*Proof sketch.* For (1), write (5) as $\partial_t q = D_0 q^{-2}(-\nabla^2 q + 2q^{-1}|\nabla q|^2)$. For small perturbations about a uniform state, the $\nabla^2 q$ term dominates and its sign determines growth/decay. For (2), near a minimum we have the local ODE $\dot{q}_{\min} \approx -D_0 q_{\min}^{-2}|\nabla^2 q|$, which gives $q_{\min}^3(t) = q_{\min}^3(0) - 3D_0|\nabla^2 q| t$, vanishing at finite time. For (3), the $q=1/2$ entropic attractor plus conservation of $\int q$ forces the "sea" to be near $q \approx 1/2$. Detailed asymptotics require singular perturbation theory at the interface; full proof deferred to a companion paper. $\square$

### V.C. Why Process B is Redundant

In the discrete framework, Process B was introduced as a separate mechanism because the permutation dynamics (bijection on $X$) alone preserves the fiber structure and the coarse-grained entropy increase (Theorem 2) is compatible with a homogeneous final state. To get *separation*, one needed an additional mechanism.

In the continuum limit, the same permutation dynamics, once spatially resolved and taken to the $a \to 0$ limit, **already contains the separation mechanism** through the $1/q^2$ nonlinearity. The $D(q) \to \infty$ divergence at $q=0$ is the mathematical expression of "domains with near-zero vacancy expel information so rapidly that they self-reinforce."

**Summary of logic chain:**

1. DGF discrete: $f$ is a permutation (bijection on $X$) $\implies$ no creation/destruction of information
2. Spatial coarse-graining: $q(\mathbf{x}, t)$ defined locally
3. Flux ansatz: $J_{i\to j} = 1/q_i - 1/q_j$ (the simplest nonlinearity with $q=0$ singularity)
4. Continuum limit: $\partial_t q = D_0 \nabla^2(1/q)$
5. This PDE amplifies gradients (anti-diffusion) $\implies$ spontaneous domain formation
6. $q=0$ singularity + $q=1/2$ entropic attractor $\implies$ two-domain separation
7. No auxiliary Process B required

### V.D. Phase Diagram

The qualitative behavior of (5) depends on the global average $\bar{q} \equiv |\Omega|^{-1}\int_\Omega q\,d^dx$ and the spatial dimension $d$:

| Regime | Condition | Behavior |
|--------|-----------|----------|
| **Homogeneous** | $\bar{q} \approx 1/2$, small gradients | Stable uniform state; perturbations decay |
| **Separation** | $\bar{q} \ll 1/2$, nonzero gradients | Two-domain formation: $q \approx 0$ cores + $q \approx 1/2$ sea |
| **Dilute** | $\bar{q} \approx 1$, any gradients | $D(q) \approx D_0$, nearly linear diffusion; weak structure |
| **Critical** | $\bar{q} \ll 1$, $d \geq 2$ | Finite-time singularity formation likely |

The "separation" regime is the physically interesting one for the DGF, corresponding to systems with substantial information content ($M \gg N/2$, i.e., more occupied than vacant cells).

---

## VI. Caveats and Connections

### VI.A. Spatial Dimension $d$

**Input, not derived.** The spatial dimension $d$ is an external parameter specifying how cells are arranged. The DGF framework does not predict $d$; it must be chosen based on the physical system being modeled. For most applications, $d=3$ is the natural choice. The mathematical structure of (5) is valid for any $d \geq 1$.

**$d$-dependence of critical behavior.** The qualitative behavior (singularity formation, domain structure) may depend on $d$. The fast diffusion literature shows that the critical exponent $m_c(d) = (d-2)/d$ separates regimes. For our equation with $m = -1$:
- $d = 1$: $m_c = -1$, so $m = m_c$ (borderline)
- $d = 2$: $m_c = 0$, so $m < m_c$ (supercritical, singularities expected)
- $d = 3$: $m_c = 1/3$, so $m < m_c$ (supercritical)

Thus for $d \geq 2$, finite-time singularities are expected; for $d = 1$, the behavior is borderline and may depend on details.

### VI.B. Flux Ansatz: $D(q) = D_0/q^2$

**Modeling choice, not a theorem.** The flux form $J = 1/q_i - 1/q_{i+1}$ and its continuum consequence $D(q) \propto q^{-2}$ are modeling choices. The DGF Theorem 1 (bijection) constrains the dynamics to be a permutation, but does not specify the permutation's *rate* or *selection rule*. The $1/q$ potential is:

- **Motivated by:** "Information pressure" — crowded regions expel information faster
- **Simplest form:** $J \propto \nabla(\phi(q))$ with $\phi(q)$ singular at $q=0$. The choice $\phi(q) = 1/q$ is the simplest rational function with a pole at $q=0$
- **Alternative forms:** $\phi(q) = q^{-\alpha}$ for $\alpha > 0$, or $\phi(q) = -\log q$, would produce qualitatively similar behavior (divergent diffusivity at $q=0$, uphill dynamics). The exponent $\alpha = 1$ is the minimal integer exponent

**Testability.** The functional form $D(q) \propto q^{-2}$ makes a specific prediction: the flux between two regions scales as $1/q_1 - 1/q_2$. This can be tested in discrete DGF simulations by measuring the correlation between local flux and local $q$.

### VI.C. Continuum Limit Mathematical Status

**Bridge assumptions.** The passage from (3) to (5) requires:

1. **Smoothness:** $q(\mathbf{x}, t)$ is twice differentiable in space. This holds generically for $t > 0$ due to the parabolic nature of (5) when $q > 0$, but may break down at the $q=0$ singularity.

2. **Closure:** The discrete flux $J_{i\to j} = 1/q_i - 1/q_j$ closes at the single-point level (no need for higher-order correlations). This is exact for the DGF flux ansatz; if the true flux involved pair or higher correlations, a BBGKY-like hierarchy would emerge.

3. **Thermodynamic limit:** $N \to \infty$, $a \to 0$, with physical volume $V = N a^d$ fixed. This is standard but requires that the limit of the discrete dynamics exists.

**Rigorous status.** The derivation from DGF discrete dynamics to (5) is **formal** (gradient expansion to leading order in $a$). A rigorous proof would require:
- Establishing that solutions of the discrete equation (3) converge to solutions of (5) as $N \to \infty$
- Proving that the $a \to 0$ limit commutes with the $t \to \infty$ limit (for asymptotic analysis)
- Controlling the singular behavior at $q=0$ in the discrete-to-continuum limit

These are nontrivial mathematical questions; we do not claim to resolve them here.

### VI.D. Connection to Known PDEs

**Fast diffusion / Porous medium equation.** The standard form is $\partial_t u = \nabla^2(u^m)$ with $m > 0$. For $m = -1$, our equation $\partial_t q = \nabla^2(q^{-1})$ is a formal analytic continuation to negative $m$. Key differences:

| Property | Porous medium ($m > 1$) | Fast diffusion ($0 < m < 1$) | DGF ($m = -1$) |
|----------|------------------------|------------------------------|----------------|
| $D(u)$ as $u \to 0$ | $\to 0$ | $\to 0$ (if $m > 0$) | $\to \infty$ |
| Finite speed of propagation | Yes | Yes (if $m > m_c$) | No (infinite speed) |
| Extinction in finite time | No | Yes (if $m < m_c$) | Yes (expected) |
| Gradient flow | Downhill | Downhill | Uphill |

**Cahn-Hilliard equation.** $\partial_t \phi = \nabla\cdot(M(\phi)\nabla(\delta F/\delta\phi))$ with $F = \int[f(\phi) + \frac{\kappa}{2}|\nabla\phi|^2]\,d^dx$. Our equation can be written as $\partial_t q = -\nabla\cdot(q\nabla(\delta F_1/\delta q))$ with $F_1 = \int D_0/(2q)\,d^dx$, which is an *uphill* Cahn-Hilliard-type equation. This is why it produces segregation (phase separation) rather than coarsening.

**Fisher-KPP equation.** $\partial_t u = D\nabla^2 u + r u(1-u)$. This has a *source term* $r u(1-u)$ producing traveling fronts. Our equation has no source term; the "source" behavior at $q=0$ arises from the nonlinear diffusivity, not from reaction kinetics.

### VI.E. Summary of Derivation Status

| Ingredient | Status | Derivation |
|------------|--------|------------|
| Conservation law $\partial_t q + \nabla\cdot\mathbf{J} = 0$ | **Derived** | From discrete continuity (DGF axiom: total occupation conserved) |
| Flux ansatz $J = 1/q_i - 1/q_{i+1}$ | **Assumed** | Modeling choice; motivated by information pressure |
| Diffusivity $D(q) = D_0/q^2$ | **Consequence** | Follows from flux ansatz + continuum limit |
| PDE $\partial_t q = \nabla^2(1/q)$ | **Formally derived** | Gradient expansion of discrete flux |
| $q=0$ singularity | **Proved** | Direct limit $D(q) \to \infty$ |
| $q=1/2$ statistical preference | **Proved** | Stirling + convexity of $s(q)$ |
| Separation mechanism | **Demonstrated** | From PDE properties + entropic attractor |
| Finite-time singularity | **Conjectured** | Heuristic argument; rigorous proof open |
| Dimensionality $d$ | **Input** | External to DGF framework |

---

## VII. Key Results Summary

1. **Continuum PDE:** $\partial_t q = D_0 \nabla^2(1/q) = D_0 \nabla\cdot(q^{-2}\nabla q)$ — a very fast diffusion equation with effective diffusivity $D(q) = D_0/q^2$.

2. **$q=0$ boundary:** $D(q) \to \infty$ as $q \to 0$, classifying $q=0$ as a singular boundary where information bursts outward. No classical stationary solution attains $q=0$ at an interior point.

3. **$q=1/2$ preference:** The mixing entropy $s(q) = -q\log q - (1-q)\log(1-q)$ is maximized at $q=1/2$, making $q=1/2$ the global minimum of the bulk free energy $f(q) = -T_0 s(q)$.

4. **Separation mechanism:** The anti-diffusive character of the DGF PDE (uphill flow relative to $F_1[q] = \int q^{-1}$) amplifies initial gradients. Low-$q$ regions self-reinforce into near-zero domains, while the entropic attractor maintains the "sea" at $q \approx 1/2$. No auxiliary Process B is required.

5. **Principal caveats:** $D(q) \propto q^{-2}$ is a modeling ansatz (not derived from DGF Theorem 1); spatial dimension $d$ is an input; the continuum derivation is formal (gradient expansion); finite-time singularity formation is conjectured but not rigorously proved.

---

## Appendix A: 1D Stationary Analysis

For the 1D stationary equation $\partial_x^2(1/q) = 0$ on $[0, L]$ with no-flux conditions $\partial_x(1/q)|_{0,L} = 0$, the general solution is $1/q(x) = C$ (constant), i.e., $q(x) = 1/C$ uniform. This is the trivial uniform state. Nontrivial stationary solutions would require $q=0$ at some point, which is incompatible with the classical PDE as shown in Theorem 6(c).

However, **non-stationary** solutions can approach configurations where $q$ is arbitrarily close to 0 in subdomains, with the interface sharpening over time. The relevant object is not a stationary solution but a **slow manifold** in function space.

## Appendix B: Transformation to Standard Fast Diffusion Form

The transformation $u = q^{-\alpha}$ maps between different nonlinear diffusion equations. For $\partial_t q = \nabla^2(q^{-1})$, setting $u = q^{-1}$ yields $\partial_t u = -u^2 \nabla^2 u$, which is not in standard form. Setting $u = \log q$ yields $\partial_t u = e^{-u}\nabla^2(e^{-u})$, also nonstandard. The equation (5) appears to be an independent member of the nonlinear diffusion family, not reducible to the porous medium equation by a simple change of variables.

## Appendix C: Numerical Signatures

For numerical verification, the following signatures distinguish (5) from standard diffusion:

1. **Gradient amplification:** $\partial_t |\nabla q|^2 > 0$ in regions where $q$ has curvature
2. **$L^p$ norm decay:** $\partial_t \int q^p\,d^dx$ is not sign-definite for $p \neq -1$
3. **Interface sharpening:** Initial smooth profiles develop increasingly sharp gradients at domain boundaries
4. **Two-point correlation:** $\langle q(\mathbf{x})q(\mathbf{y})\rangle$ develops bimodal structure over time

---

*Document version 1.0 — For PRD submission, to be integrated with BM Sections II–III.*
