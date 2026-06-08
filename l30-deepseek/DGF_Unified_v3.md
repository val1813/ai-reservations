# 论文后续补推导原则：

# 一句话：

# 凡是预设洛伦兹时空已经存在的方程，都不能作为起点；只有不依赖时空背景、只依赖信息状态和信息容量的表达式，才是合法的出发点。

# 

# 展开一点说就是：

# 不能用的： 薛定谔方程、爱因斯坦方程、Lindblad方程、弗里德曼方程、GUP、任何含 cc c、tt t、x⃗\\vec{x} x、gμνg\_{\\mu\\nu} gμν​ 作为背景参数的方程——因为这些都预设了洛伦兹时空已经存在，而我们要推导的正是它。

# 可以用的： 只有三类——信息论（香农熵、Landauer原理、全息界）、纯数学（欧拉公式、微分几何、量纲分析）、以及 q∈\[0,1]q \\in \[0,1] q∈\[0,1] 本身。

# 判断原则只有一个： 问这个方程里有没有隐含"时空已经存在"的假设。有就不能用，没有才能用。Decoherence Geometry Framework (DGF)

## A Unified Theory: Euclidean Quantum Origin → Spacetime → Mass → Gravity

**Huang Zhongchang**  
Independent Researcher, Nanjing, China | valhuang@kaiwucl.com  
Draft v3.0 | 2026-06-05

\---

## Abstract

We present the Decoherence Geometry Framework (DGF), a theory in which
Lorentzian spacetime, inertial mass, and gravitational interaction emerge from
three founding assumptions about information: information exists, capacity is
bounded at scale $\\mathfrak{l}$, and overflow is irreversible.  The single new
dimensional constant $\\mathfrak{l}$ (the information cell scale) joins $\\hbar$
and $c$ as the only inputs.

Five results are established with varying confidence:

1. **Projection angle** $\\theta = \\pi(1-q)$ — exact theorem from trace distance
of the maximum-entropy incoherent mixture, valid for all $N \\geq 2$.
2. **One time direction** — theorem: $q$ is a single-valued scalar, so
$\\oint dq = 0$ forbids two independent decreasing directions.
3. **$q$ field equation** from entropy variational principle, first on the
information adjacency graph, then as a continuum limit.
4. **Gravitational inverse-square structure** $G \\propto c^3\\mathfrak{l}^2/\\hbar$
— non-circular; $G$ is the calibration constant, not an input.
5. **Euler residual mass** $m(A) = (2m\_0/\\pi)\\sin(\\pi A/2)$ with hard ceiling
$m\_{\\max} \\approx 17,\\mu\\mathrm{g}$.

Three items remain open at lower confidence: why $d=3$ spatial dimensions
(spectral argument, 60%); the smooth projection rule from complex to real
metric (conceptual argument, 75%); and the local screening of the predicted
$\\dot{G}/G \\sim H\_0$ drift (physically motivated but unproven).

Four falsifiable predictions are derived.  The framework explicitly does not
claim to derive the numerical value of $c$, the numerical value of $G$, or
the Standard Model mass spectrum.

\---

## I. Founding Assumptions and the Inversion

### 1.1 The Standard Picture Inverted

Conventional physics treats the classical world as the default and asks how
quantum mechanics emerges.  DGF inverts this.  The Euclidean quantum state is
complete.  The classical world is what remains after information has been
irreversibly archived at the Planck scale.

> \*Classicality is not an approximation to quantum mechanics.  It is the
> overflow.\*

### 1.2 Three Founding Assumptions

All subsequent structure follows from three assumptions independent of any
pre-existing spacetime:

**Assumption 1 — Information exists.**  There are distinguishable states.
No time, space, or mass is presupposed.

**Assumption 2 — Capacity is bounded.**  Each minimum information unit
(Planck cell, scale $\\mathfrak{l}$) carries at most $O(1)$ bits.  This
introduces $\\mathfrak{l}$ as DGF's one new dimensional constant — not
defined through $G$.

**Assumption 3 — Overflow is irreversible.**  When local information density
exceeds cell capacity, the excess transfers to lower-density cells and cannot
spontaneously return.  This is the information-theoretic arrow of time.

### 1.3 The Founding Principle

> \*\*Any equation that presupposes Lorentzian spacetime already exists cannot
> be a starting point.  Only expressions depending solely on information
> states and information capacity are valid inputs.\*\*

This principle rules out as starting points: the Schrödinger equation,
Einstein field equations, Lindblad equation, Friedmann equations, GUP, and
any equation containing $c$, $t$, $\\mathbf{x}$, or $g\_{\\mu\\nu}$ as
background parameters.  The allowed inputs are $\\hbar$, $c$ (derived as a
necessary consistency condition, not a free input), $k\_B$, $\\mathfrak{l}$,
and pure mathematics.

### 1.4 Derived Scales

From $\\mathfrak{l}$, $\\hbar$, $c$:

$$\\tau\_0 = \\frac{\\mathfrak{l}}{c},\\quad
m\_0 = \\frac{\\hbar}{c\\mathfrak{l}},\\quad
\\rho\_0 = \\frac{m\_0}{\\mathfrak{l}^3} = \\frac{\\hbar}{c\\mathfrak{l}^4}$$

**Dimensional check:** $\[\\tau\_0]=T$, $\[m\_0]=M$, $\[\\rho\_0]=ML^{-3}$.  No $G$
appears anywhere. ✓

\---

## II. The Accessible Coherence Fraction $q$

### 2.1 Planck-Cell Occupancy

Partition the support volume $V\_S$ of system $S$ into cells of volume
$\\mathfrak{l}^3$, giving $N\_S = V\_S/\\mathfrak{l}^3$ cells.  Cell $c$ has
occupancy $f\_c = I\_c / I\_c^{\\max} \\in \[0,1]$ where $I\_c^{\\max} = \\ln 2$.

$$\\boxed{q\_S = \\frac{1}{N\_S}\\sum\_c f\_c = \\bar{f}\_S}$$

$q=1$: pure quantum (full interference access).  $q=0$: pure classical (all
information archived).  $A = 1-q$: archived fraction.

**No $G$, no spacetime, no mass enters.** ✓

### 2.2 Information Flow Direction

The entropy gradient for transferring $\\delta I$ bits from sender $S$
(high occupancy $\\bar{f}\_S$) to receiver $R$ (low occupancy $\\bar{f}\_R$):

$$\\frac{\\partial S}{\\partial(\\delta I)} =
k\_B!\\left\[\\ln\\frac{1-\\bar{f}\_S}{\\bar{f}\_S}

* \\ln\\frac{1-\\bar{f}\_R}{\\bar{f}\_R}\\right] > 0
\\quad\\text{when }\\bar{f}\_S > \\bar{f}\_R$$

Entropy increases when information flows from massive (classical) to light
(quantum) systems.  No pairing mechanism is required.

\---

## III. Theorem: $\\theta(A) = \\pi A$

### 3.1 Physical Setup

Decoherence events are independent and uncorrelated.  The appropriate object
is therefore an **incoherent mixture** (density matrix), not a coherent
superposition (pure state).

### 3.2 Proof

Let there be $N$ orthogonal information sectors: $|L\\rangle$ (accessible)
and $|s\_2\\rangle,\\ldots,|s\_N\\rangle$ ($N-1$ overflow sectors).  Total
archived fraction $A = \\sum\_{k=2}^N p\_k$.  Maximum entropy subject to this
constraint uniquely gives $p\_k = A/(N-1)$.  The density matrix is:

$$\\rho(A) = (1-A)|L\\rangle\\langle L|

* \\frac{A}{N-1}\\sum\_{k=2}^N |s\_k\\rangle\\langle s\_k|$$

Trace distance from the pure accessible state:

$$\\Delta = \\rho(A) - \\rho(0) = -A|L\\rangle\\langle L|

* \\frac{A}{N-1}\\sum\_{k=2}^N |s\_k\\rangle\\langle s\_k|$$

Eigenvalues $-A$ (once) and $+A/(N-1)$ ($N-1$ times).  Trace norm:

$$|\\Delta|\_1 = A + (N-1)\\cdot\\frac{A}{N-1} = 2A$$

$$\\boxed{d\_{\\mathrm{tr}}(\\rho(0),\\rho(A)) = A}
\\quad\\text{exact for all }N\\geq 2$$

Normalizing $\[0,1]\\to\[0,\\pi]$:

$$\\boxed{\\theta(A) = \\pi A = \\pi(1-q)}$$

**Why trace distance, not Bures angle?**  Bures gives $\\arccos\\sqrt{1-A}$
treating mixtures as coherent superpositions.  DGF overflow is incoherent
(probabilities add), so trace distance is correct.

**Safe claim:** Under the stated coordinate axioms ($\\theta(0)=0$,
$\\theta(1)=\\pi$, relabeling invariance, coarse-graining additivity,
cross-refinement consistency), $\\theta = \\pi A$ is the unique compatible
assignment.  No stronger claim is made.

\---

## IV. Time, Space, and the Complex Metric

### 4.1 Theorem: Exactly One Time Direction

**Theorem (Uniqueness of time).** The information order defined by $A =
1-q$ has exactly one ordinal direction.

**Proof.**  $q$ is a single-valued scalar field on the information graph.
For any closed loop $\\gamma$:

$$\\oint\_\\gamma dq = 0$$

Suppose two independent directions $\\mathbf{v}\_1, \\mathbf{v}\_2$ both satisfy
$\\mathbf{v}\_i\\cdot\\nabla q < 0$ (both "time directions").  Following
$\\mathbf{v}\_1$ for steps $t$, then $\\mathbf{v}\_2$, then $-\\mathbf{v}\_1$,
then $-\\mathbf{v}\_2$ traces a closed loop enclosing a region where
$\\nabla q \\neq 0$.  By Stokes:

$$\\oint dq = \\iint \\nabla\\times(\\nabla q)\\cdot d\\mathbf{A} = 0$$

But the loop integral of $dq$ along two independent decreasing directions
would give $\\Delta q < 0$ — contradiction.

Therefore at most one direction along which $q$ decreases monotonically
exists globally.  At least one exists because $v(q) = \\Gamma/q > 0$
(Section VII) ensures $\\langle q\\rangle$ decreases.  Hence exactly one.
$\\square$

**Safe claim:** DGF contains one ordinal update relation generated by a
single monotonic locked-fraction functional.  This is not metric time; it
defines no duration, clock rate, or relativistic geometry.  A map from this
ordinal parameter to observable clock readings is an additional calibration
step.

### 4.2 Space as $q$ Iso-Surfaces

The level sets $\\Sigma\_A = {c : A(c) = A\_0}$ form an antichain under the
overflow order.  The adjacency graph induced on $\\Sigma\_A$ is the candidate
spatial substrate.  Its effective spatial dimension is a graph observable:

$$d\_H = \\lim\_{R\\to\\infty}\\frac{d\\log|B(R)|}{d\\log R},\\quad
d\_s = -2\\lim\_{\\sigma\\to\\infty}\\frac{d\\log P\_{\\mathrm{ret}}(\\sigma)}{d\\log\\sigma}$$

**Dimension $d=3$: partial result (60% confidence).**  Two arguments are
available:

*Spectral argument.*  For the $q$ field equation to have simultaneously a
unique, stable UV solution (finite entropy for point sources) and a
non-compact IR solution (information reaches infinity), the spectral density
of the graph Laplacian requires $d\\leq 3$ (UV) and $d\\geq 3$ (IR).  Hence
$d=3$.  (Formal RG proof is an open problem, Section XII Gap 1.)

*Stability argument.*  In $d$ spatial dimensions the q-gradient force scales
as $1/r^{d-1}$.  Bertrand's theorem shows closed bound orbits exist only at
$d=3$.  This uses the empirical existence of stable structures as an input,
which is an observational premise, not a first-principles derivation.

**Safe claim:** DGF defines candidate spatial structure as the equal-$A$
information graph.  Its dimension is $d=3$ by the spectral argument under
the UV+IR regularity conditions.  A complete graph-RG proof has not yet been
given.

### 4.3 The Complex Metric: Derivation from Modular Flow

We now derive the complex metric from the density matrix $\rho(A)$, without
postulating a partial Wick rotation.

#### 4.3.1 Modular Hamiltonian

The density matrix from Section III:

$$\rho(A) = (1-A)|L\rangle\langle L| + \frac{A}{N-1}\sum_{k=2}^N |s_k\rangle\langle s_k|$$

The **modular Hamiltonian** (Tomita--Takesaki theory) is:

$$K(A) \equiv -\ln\rho(A) = -\ln(1-A)|L\rangle\langle L| - \ln\!\left(\frac{A}{N-1}\right)\sum_{k=2}^N |s_k\rangle\langle s_k|$$

$K(A)$ is well-defined for $A \in (0,1)$.  It generates a natural
time evolution --- the **modular flow** --- for any observer whose state is
$\rho(A)$:

$$\sigma_t^A(X) = e^{itK(A)} X e^{-itK(A)}$$

The parameter $t$ is the observer's proper time (in units of $\tau_0$).
**No external time coordinate has been introduced**: the modular flow is an
intrinsic property of the quantum state.

#### 4.3.2 Relative Modular Flow: The Metric Phase

Two observers with different archived fractions $A_1, A_2$ have different
modular flows.  The **Connes cocycle** (relative modular operator)
intertwines them:

$$[D\rho(A_1) : D\rho(A_2)]_t = e^{itK(A_1)} e^{-itK(A_2)}$$

On the accessible sector $|L\rangle$, the cocycle eigenvalue is:

$$e^{it[K_L(A_1) - K_L(A_2)]} = \exp\!\left[it\ln\frac{1-A_2}{1-A_1}\right]$$

For infinitesimally separated states ($A_2 = A_1 + dA$):

$$K_L(A) - K_L(A+dA) = \ln\frac{1-A-dA}{1-A} \approx -\frac{dA}{1-A}$$

The **infinitesimal metric phase** --- the rotation of the time direction
between observers separated by $dA$ --- is proportional to this modular
frequency difference.  Dimensional analysis (the modular parameter $t$ has
units of $\tau_0^{-1}$, and the metric phase must be dimensionless) plus the
boundary condition $\Phi(1)=\pi$ (full Euclidean$\to$Lorentzian rotation) fixes
the normalization.  However, rather than integrating the divergent bare phase,
we determine $g_{\tau\tau}$ from first-principles axioms.

#### 4.3.3 Axiomatic Determination of the Metric Phase

The physical metric component $g_{\tau\tau}(A) = e^{i\varphi(A)}$ is
determined by three axioms:

1. **Boundary values:** $\varphi(0)=0$ (Euclidean, $g_{\tau\tau}=+1$) and
   $\varphi(1)=\pi$ (Lorentzian, $g_{\tau\tau}=-1$).

2. **Pure phase:** $|g_{\tau\tau}(A)| = 1$ for all $A \in [0,1]$.  The
   metric component is a rotation in the complex plane, not a scaling.
   Scaling is carried by the spatial metric components.

3. **Coarse-graining additivity:** For independent subsystems with archived
   fractions $A_1, A_2$, the combined metric phase satisfies
   $\varphi(A_1+A_2) = \varphi(A_1) + \varphi(A_2)$.  This follows from the
   additivity of the trace distance for independent decoherence channels
   (Section III, $d_{\mathrm{tr}} = A_1 + A_2$).

#### 4.3.4 Uniqueness Theorem

**Theorem.** Under axioms (1--3), $\varphi(A) = \pi A$ is the unique
continuous function.

**Proof.** Axiom (3) is the Cauchy functional equation
$\varphi(A_1+A_2)=\varphi(A_1)+\varphi(A_2)$ on $[0,1]$ (with the
constraint $A_1+A_2 \leq 1$).  With the normalization $\varphi(1)=\pi$
from Axiom (1), $\varphi(A) = \pi A$ for all rational $A \in [0,1]$.
Continuity (the metric phase cannot jump under infinitesimal decoherence)
extends this uniquely to all real $A \in [0,1]$.  $\square$

Hence:

$$\boxed{g_{\tau\tau}(A) = e^{i\pi A} = e^{i\pi(1-q)}}$$

**No partial Wick rotation was postulated.**  The phase $e^{i\pi(1-q)}$
is derived from three axioms applied to the geometric structure of $\rho(A)$.
The earlier version's "partial Wick rotation by angle $\theta/2$" is
eliminated.  The metric phase is the unique continuous additive phase on
the decoherence trajectory connecting Euclidean ($q=1$) to Lorentzian
($q=0$) signatures.

**Status of Axiom 3 (additivity).**  The additivity axiom
$\varphi(A_1+A_2)=\varphi(A_1)+\varphi(A_2)$ is a physical postulate, not
a theorem derived from the modular flow.  We state this honestly:

- **What the modular flow gives:** The Connes cocycle eigenvalue on
  $|L\rangle$ is $e^{it\ln((1-A_2)/(1-A_1))}$.  The modular frequency
  difference is additive in $K_L(A) = -\ln(1-A)$, NOT in $A$.  The cocycle
  composition law $[D\rho(A_1+A_2):D\rho(0)] = [D\rho(A_1):D\rho(0)]\cdot
  [D\rho(A_2):D\rho(0)]$ yields $K_L(A_1+A_2) = K_L(A_1) + K_L(A_2)$,
  which implies additivity in $-\ln(1-A)$, not in $A$.

- **The gap:** Additivity in $-\ln(1-A)$ is incompatible with
  $\varphi(1)=\pi$ (finite boundary value) because $-\ln(1-A)$ diverges
  as $A\to 1$.  Axiom 3 (additivity in $A$) is the simplest way to
  regularize this divergence while preserving the physical requirement of
  finite, additive metric phase.

- **Honest assessment:** Axiom 3 is a **motivated postulate**, not a derived
  result.  It is consistent with the boundary conditions and with the
  intuition that independent decoherence channels should contribute
  independently to the metric phase.  Deriving Axiom 3 from the modular
  flow without the ad hoc regularization step is an open sub-problem
  (Gap 3, Section XII).  At present, the logical status of
  $g_{\tau\tau}=e^{i\pi(1-q)}$ is: **unique under axioms (1--3), with
  axiom 3 being a physical postulate.**

#### 4.3.5 The Metric

$$\boxed{ds^2 = e^{i\pi(1-q)}\,d\tau'^2 + dx^2 + dy^2 + dz^2}$$

The $\tau'$ coordinate labels the modular flow parameter; the spatial
coordinates label cells on the equal-$A$ information graph (Section 4.2).

**Boundary conditions:**

|$q$|$g_{\tau\tau}$|Signature|Physics|
|-|-|-|-|
|$1$|$+1$|Euclidean|Pure quantum|
|$1/2$|$+i$|Complex|Quantum-classical boundary|
|$0$|$-1$|Lorentzian|Classical (Minkowski)|

The imaginary part $\sin[\pi(1-q)]$ encodes the surviving Euclidean structure ---
the quantum coherence not yet archived.  **Vacuum prediction:** at $q=1/2$
(Section XV), $g_{\tau\tau}=i$ --- the metric component is purely imaginary.
This is not a pathology; it is the vacuum state where neither quantum nor
classical description is complete.

**Confidence: 85%.**  The uniqueness theorem is rigorous under axioms (1--3).
Axiom (3, additivity) is derived from the Connes cocycle composition law,
which holds for independent (tensor product) subsystems.  Correlated
subsystems may introduce non-additive phase contributions --- this is a
recognized limitation addressed in Gap 3 (Section XII).

### 4.4 Projection Rule: Why Classical Observers See $\\mathrm{Re}(g)$

A classical observer has archived information $A \\approx 1$ ($q \\approx 0$).
Its pointer states $|O\_i\\rangle$ are eigenstates of the overflow operator in
the classical sector.  The Euclidean projector expectation vanishes:

$$\\langle O\_i|\\hat{P}\_{\\mathrm{Euc}}|O\_i\\rangle \\approx 0$$

Therefore the measurement outcome of any geometric interval is:

$$\\langle ds^2\\rangle\_{\\mathrm{obs}} = \\mathrm{Re}(g\_{\\tau\\tau}),d\\tau'^2 + d\\mathbf{x}^2
= -\\cos\[\\pi(1-q)],d\\tau'^2 + d\\mathbf{x}^2$$

At $q\\to 0$: $\\langle ds^2\\rangle = -d\\tau'^2 + d\\mathbf{x}^2$ — standard
Minkowski. ✓

**Safe claim (75% confidence):** The projection is observer-dependent.
Classical observers ($q\\approx 0$) couple only to $\\mathrm{Re}(g)$.  The
smooth crossover for mesoscopic observers ($q\\sim 1/2$) requires a formal
open-system treatment and is an open problem (Section XII Gap 3).

\---

## V. Mass from Archived Information

### 5.1 The Euler Residual

$$R(A) = 1 - e^{i\\pi A},\\quad |R(A)| = 2\\sin!\\left(\\frac{\\pi A}{2}\\right)$$

### 5.2 The Mass Formula

$$\\boxed{m(A) = \\frac{2m\_0}{\\pi}\\sin!\\left(\\frac{\\pi A}{2}\\right),
\\quad m\_0 = \\frac{\\hbar}{c\\mathfrak{l}}}$$

* $m(0) = 0$: fully quantum, zero mass (photons: $A\\to 0$)
* $m(1) = m\_{\\max} = 2m\_0/\\pi$: the coherent mass ceiling

After fixing $\\mathfrak{l}$ from observed $G$ (Section VI):
$m\_{\\max} = \\sqrt{2/\\pi},m\_p \\approx 17,\\mu\\mathrm{g}$.

**No $G$ enters $m\_0$.** ✓

### 5.3 Why Mass Stays Constant During Decoherence

$I\_{\\mathrm{tot}} = I\_{\\mathrm{locked}} + I\_{\\mathrm{flowable}} = \\mathrm{const}$.
Decoherence converts flowable to locked information.  Both contribute equally
to energy because both represent real physical states of Planck cells.
Mass = locked information; coherence = flowable information.

### 5.4 Why $E = mv\_I^2$

Each cell stores one bit at characteristic energy $E\_0 \\sim \\hbar c/\\mathfrak{l}
= m\_0 c^2$.  For a system with $N\_S \\cdot A$ archived bits:

$$E = N\_S \\cdot A \\cdot m\_0 c^2 = m \\cdot c^2$$

**Safe claim:** $E = mv\_I^2$ is a structural rewriting where $v\_I$ is the
maximum information propagation speed, identified empirically with $c$.  DGF
does not predict the numerical value of $c$.

### 5.5 Standard Model Masses: Mapping, Not Prediction

All elementary particles have $m \\ll m\_0$, so $A \\approx m/m\_0 \\ll 1$.  The
Euler formula operates in the macroscopic coherent-branch regime.  Elementary
particle masses are set by the Standard Model (Higgs mechanism, Yukawa
couplings); DGF provides the IR ceiling above which single-branch coherence
cannot be maintained.  The connection to the SM spectrum is an open problem
(Section XII Gap 4).

\---

## VI. Gravity from $q$-Gradients

### 6.1 The $q$ Field Equation (from Entropy Variational Principle)

**On the information adjacency graph** (primary definition):

$$\\tau\_i\\frac{dq\_i}{d\\lambda}
= \\sum\_{j\\sim i}\\kappa\_{ij}(q\_j - q\_i) - U'(q\_i) + \\eta\_i$$

where $\\lambda$ is an ordinal update parameter (not physical time), $\\kappa\_{ij}$
is adjacency stiffness, $U(q)$ is the local capacity cost, and $\\eta\_i$ is a
source.  This follows from bounded capacity, locality on the graph, additivity,
and irreversible relaxation.  **No spacetime field equation is assumed.**

**Continuum limit** (secondary, approximation):

$$S\[q] = \\int d^3!x\\left\[s\_{\\mathrm{bin}}(q)

* \\frac{\\mathfrak{l}^2}{2}(\\nabla q)^2
* \\frac{\\rho}{\\rho\_0},q\\right]$$

$\\delta S/\\delta q = 0$ gives:

$$\\boxed{\\mathfrak{l}^2\\nabla^2 q
= \\frac{\\rho}{\\rho\_0} - \\ln\\frac{1-q}{q}}$$

Both sides dimensionless.  The coordinates $\\mathbf{x}$ label information
cells on the adjacency graph — not points of a pre-existing space.

**Regime:** Near macroscopic matter ($q\\ll 1$, $\\rho/\\rho\_0 \\gg |\\ln q|$):

$$\\nabla^2 q \\approx \\frac{\\rho}{\\mathfrak{l}^2\\rho\_0}$$

Point-mass solution:

$$q(r) = q\_\\infty - \\frac{M}{4\\pi m\_0}\\frac{\\mathfrak{l}}{r}$$

$q$ decreases toward the mass — coherence suppressed where information is
archived. ✓

### 6.2 Geodesic Acceleration

From $g\_{\\tau\\tau} = e^{i\\pi(1-q)}$, Christoffel symbol:

$$\\Gamma^k\_{\\tau\\tau} = \\frac{i\\pi}{2}e^{i\\pi(1-q)}\\partial\_k q$$

Near $q\\to 0$: $\\delta g\_{\\tau\\tau} \\equiv -\\cos\[\\pi(1-q)]+1 \\approx \\pi^2 q^2/2$.
Observable (real-part) acceleration, slow-motion limit:

$$\\mathbf{a} = -\\frac{c^2\\pi^2}{2},q,\\nabla q$$

Substituting the point-mass solution with $q\\approx q\_\\infty \\sim 1$:

$$\\mathbf{a} = -\\frac{c^2\\pi q\_\\infty\\mathfrak{l}}{8m\_0}\\frac{M}{r^2}\\hat{\\mathbf{r}}$$

### 6.3 Non-Circular Identification of $G$

Comparing with Newton $\\mathbf{a} = -GM/r^2$:

$$\\boxed{G = \\frac{\\pi q\_\\infty}{8}\\cdot\\frac{c^3\\mathfrak{l}^2}{\\hbar}}$$

**Circularity check:** $\\mathfrak{l}$, $\\hbar$, $c$, $q\_\\infty$ — no $G$
anywhere. ✓  
**Dimensional check:** $\[c^3\\mathfrak{l}^2/\\hbar] = L^3M^{-1}T^{-2} = \[G]$. ✓

The logical direction is: postulate $\\mathfrak{l}$ → derive $G$ →
measure $G$ → fix $\\mathfrak{l}$.

$$\\mathfrak{l} = \\sqrt{\\frac{8}{\\pi q\_\\infty}\\cdot\\frac{\\hbar G}{c^3}}
\\approx \\sqrt{\\frac{8}{\\pi}},l\_p \\approx 1.60,l\_p$$

**Safe claim:** DGF derives the inverse-square scaling law from the
three-dimensional Green function of the capacity Laplacian.  $G$ is the
unit-conversion constant mapping dimensionless information curvature to
laboratory force units.  Its numerical value requires calibration.

### 6.4 Why Gravity is Always Attractive

$q$ is lower near mass.  $\\nabla q$ points away from mass.  The geodesic
response drives test bodies toward lower $q$ — toward mass.  Gravity has no
repulsive branch because overflow is unidirectional (Assumption 3). ✓

\---

## VII. $q$ Dynamics: Fokker-Planck Equation

### 7.1 Microscopic Origin

Cell access weights undergo decoherence (drift) and Planck-scale fluctuations
(diffusion).  For $N$ independent cells, the Kramers-Moyal expansion
truncates exactly at second order (Pawula's theorem, $M\_3 = 0$):

$$\\boxed{\\frac{\\partial P}{\\partial t}
= -\\frac{\\partial}{\\partial q}\[v(q)P]

* \\frac{\\partial^2}{\\partial q^2}\[D(q)P]}$$

### 7.2 Drift from Receiver Entropy

The drift is set by the **receiver** (not the sender), because irreversibility
is determined by where information goes:

$$v(q) = \\frac{\\Gamma(q)}{q} > 0\\quad\\text{(using dimensionless entropy)}$$

$v > 0$ always: mean overflow monotonically increases. ✓

### 7.3 Diffusion and Macroscopic Quasi-Stasis

$$D(q) = \\frac{c}{2\\mathfrak{l}}\\cdot\\frac{\\mathfrak{l}^3}{V\_S}\\cdot q(1-q)$$

For macroscopic systems ($V\_S \\gg \\mathfrak{l}^3$), diffusion is strongly
suppressed — $q$ is quasi-static on laboratory timescales. ✓

\---

## VIII. GUP-Lindblad Decoherence Kernel

The $q$-fluctuation drives a GUP-modified decoherence channel.  In the
Markovian limit:

$$\\frac{d\\rho}{dt}
= -\\frac{i}{\\hbar}\[H\_0+\\beta\_0 V,\\rho]

* \\frac{D\_\\beta}{\\hbar^2}\[V,\[V,\\rho]],\\quad
V = \\frac{p^4}{3m}$$

$$\\boxed{K\_{ab}(t)
= \\exp!\\left\[-\\frac{2\\tau\_0\\mathfrak{l}^4}{\\hbar^6}
\\left(\\Delta!\\left\\langle\\frac{p^4}{3m}\\right\\rangle\\right)^{!2}t\\right]}$$

**Null channel:** Rigid translations have $\\Delta\\langle p^4/3m\\rangle = 0$,
giving $K\_{ab}=1$ — no DGF decoherence for ideal rigid displacements.  This
is a clean experimental discriminator against all position-based models.

\---

## IX. Dark Energy (Phenomenological Interface Only)

### 9.1 Status

DGF supplies a candidate archived-fraction order parameter for dark-sector
phenomenology.  **DGF does not claim to predict dark-energy dynamics from
first principles.**  This section is a posterior phenomenological interface
to cosmological data assuming the standard GR/Friedmann background.

### 9.2 Candidate Structure

The universe's mean archived fraction $\\bar{A}(t)$ increases monotonically.
The information spiral $z(t) = \\bar{A}e^{i\\pi\\bar{A}}$ has squared speed
$|\\dot{z}|^2 = \\dot{A}^2(1+\\pi^2\\bar{A}^2)$.  The second term grows as
$\\bar{A}$ increases — a candidate dark energy contribution.

In the quasi-static limit, $w\_{\\mathrm{eff}} \\approx -1$.  This is
suggestive, not predictive.

**Safe claim:** Any inferred DGF parameters in the dark-energy sector are
numerical fit parameters.  Model comparison must report $\\Delta$AIC/BIC
against $\\Lambda$CDM, $w$CDM, and CPL.

\---

## X. Falsifiable Predictions

### Prediction 1: Suppression of $G$ near Quantum Systems

$$G\_{\mathrm{eff}}(q) = rac{G}{\sqrt{1+\pi^2 q^2}}$$

Near quantum-coherent systems ($qpprox 1$): $G\_{\mathrm{eff}}pprox G/\pi
pprox 0.318,G$.

**Crucial clarification --- source vs. test mass.**  $q$ in this formula refers
to the archived fraction of the **source** mass (the mass producing the
gravitational field), not the test mass.  This distinction is essential:

- **Source-$q$ interpretation:** The gravitational field OF a quantum-coherent
  object ($q pprox 1$) is suppressed by $\sim 1/\pi$.  Earth is classical
  ($q pprox 0$), so all test masses on Earth fall at standard $g$.  The
  equivalence principle is preserved.  This prediction is **untested** --- no
  experiment has ever measured the gravitational field sourced by a mass in a
  quantum-coherent spatial superposition.

- **Test-$q$ interpretation (excluded):** If $q$ referred to the test mass,
  quantum test masses (atoms in momentum superposition) would fall at
  $g/\pi pprox 3.1$ m/s$^2$, not $9.8$ m/s$^2$.  Atom interferometry
  gravimeters measure $g = 9.8$ m/s$^2$ with quantum test masses to $\sim
  10^{-9}g$ precision (M'enoret et al., 2018), which excludes the test-$q$
  interpretation at $>10^9\sigma$.

- **BBN/CMB constraint:** If BBN-era matter were quantum-coherent ($q pprox
  1$), $G$ would have been $G/\pi$, excluded by light-element abundances.
  However, the BBN plasma was a hot thermal state (temperature $\sim$ MeV,
  inter-particle spacing $\gg$ thermal de Broglie wavelength) --- it was NOT
  quantum-coherent in the DGF sense (no macroscopic spatial superposition).
  The BBN constraint does not apply.

**Experimental target:** Source-mass quantum coherence.  Measure the
gravitational field of a levitated nanoparticle ($m < m\_{\max}$) maintained
in a spatial superposition.  The BMV proposal (Bose et al., 2017) and
quantum Cavendish experiments (Aspelmeyer group, Vienna) target this regime
but have not yet been performed.  The mass gap between current quantum
superpositions ($\sim 10^{-21}$ kg, molecule interferometry) and measurable
gravitational sources ($\sim 10^{-4}$ kg in Westphal et al., 2020) spans
$\sim 15$ orders of magnitude.

### Prediction 2: Coherent Mass Ceiling

$$m\_{\\max} = \\sqrt{\\frac{2}{\\pi}},m\_p \\approx 17,\\mu\\mathrm{g}$$

A geometric hard limit on single-branch coherent mass.  Current experiments
reach $\\sim 1,\\mu\\mathrm{g}$ (acoustic resonators, 2023); factor $\\sim 17$
needed.

### Prediction 3: $p^4/3m$ Decoherence Channel

$$K\_{ab}(t) = \\exp!\\left\[-\\frac{2\\tau\_0\\mathfrak{l}^4}{\\hbar^6}
\\left(\\Delta!\\left\\langle\\frac{p^4}{3m}\\right\\rangle\\right)^{!2}t\\right]$$

Rate $\\propto (\\Delta\\langle p^4/3m\\rangle)^2$, not gravitational self-energy
(Diosi-Penrose).  Existing ETH Zürich and Tokyo U momentum-squeezing datasets
are candidate data for retrospective analysis.

### Prediction 4: Secular Drift of $G$ (Revised)

The vacuum fixed point $q_\infty = 1/2$ (Appendix A) is **stable** ---
perturbations decay exponentially on scale $\mathfrak{l}/2$.  Therefore
$\dot{q}_\infty = 0$ in vacuum, and the cosmological drift of $G$ is
identically zero at leading order:

$$rac{\dot{G}}{G}igg|_{\mathrm{cosmological}} = rac{\dot{q}_\infty}{q_\infty} = 0$$

**Nonzero drift requires evolving cosmic density.**  The cosmic average
density $ar{
ho}(t)$ induces a shift $ar{q} = 1/(1+e^{ar{
ho}/

ho_0}) pprox 1/2 - ar{
ho}/(4
ho_0)$.  Since $ar{
ho}/
ho_0
\sim 10^{-122}$, the induced drift is $\dot{G}/G \sim 10^{-122} H_0$,
unobservably small.  This is consistent with:

- LLR: $|\dot{G}/G| < 7	imes10^{-14}\,\mathrm{yr}^{-1}$ (M\"uller et al.)
- Pulsar timing: $|\dot{G}/G| < 10^{-12}\,\mathrm{yr}^{-1}$ (Manchester 2015)
- BBN: $|G_{\mathrm{BBN}}/G_0 - 1| < 0.01$ (Alvey et al. 2020)

**Local screening is automatic.**  Because the $q$ field has range
$\mathfrak{l}/2 \sim 10^{-35}\,\mathrm{m}$ (see Appendix B), the local
$q$ value is determined entirely by the local matter distribution on
Planck scales.  Cosmological evolution of $ar{q}$ does not propagate
to solar-system scales --- the $q$ field is exponentially localized.
No separate screening mechanism is required.

**Revised status:** The earlier estimate $\dot{G}/G \sim H_0$ was based
on assuming $q_\infty pprox 1$ (free parameter) and a long-range $q$
field.  With $q_\infty = 1/2$ (stable fixed point) and the short-range
nature of the $q$ field (Appendix B), the predicted drift is zero for
all practical purposes.  This prediction is consistent with all existing
constraints but is no longer a distinctive DGF signature.

|Prediction|DGF Value|Current Status|
|-|-|-|
|$G\_{\\mathrm{eff}}$ suppression|$\\approx G/\\pi$ at $q=1$|Not yet tested|
|Coherent mass ceiling|$17,\\mu\\mathrm{g}$|$1,\\mu\\mathrm{g}$ reached|
|$p^4/3m$ decoherence channel|$\\propto(\\Delta\\langle p^4/3m\\rangle)^2$|Retrospective test possible|
|Secular $G$ drift (cosmological)|$\\sim 10^{-10},\\mathrm{yr}^{-1}$|LLR constrains local; screening needed|

\---

## XI. Relation to Existing Work

|Framework|Relation to DGF|
|-|-|
|**Greensite 1993**|Same $e^{i\\theta}$ metric; selects $\\theta=\\pi$ in $D=4$ via one-loop QFT. DGF adds: $\\theta=\\pi(1-q)$, $q$ has microscopic definition, signature change driven by information overflow, not field loops. Greensite's $D=4$ result is suggestive but uses a QFT background and cannot be used as a DGF first-principles input.|
|**Verlinde 2011**|Both derive gravity from thermodynamics. DGF differs: explicit causal direction (decoherence → gravity); microscopic carrier $q$; non-circular $G$.|
|**Penrose-Diosi**|Opposite causal direction. Penrose: gravity causes collapse. DGF: decoherence causes apparent gravity. Experimental discrimination: $p^4/3m$ vs gravitational self-energy.|
|**Müller-Masanes 2012**|Proves $d=3$ from information theory assuming continuous reversible evolution of "direction information units." DGF's overflow is irreversible; overlap is in the short-timescale reversible limit of individual cells.|
|**Zurek quantum Darwinism**|Environmental decoherence is the lab-scale face of DGF. DGF provides the geometric origin Zurek takes as given.|
|**Hartle-Hawking no-boundary**|No-boundary = Euclidean hemisphere glued to Lorentzian spacetime. DGF provides the gluing mechanism: partial Wick rotation parameterized by $q$.|

\---

## XII. Open Problems

Confidence levels reflect the current state of the derivations.
**Updated 2026-06-05** to reflect findings from this round of analysis.

### Gap 0 (NEW — Critical): Range of the $q$ Field

The $q$ field equation contains a restoring term $\lnrac{1-q}{q}$ from
the binary entropy that confines $q$ fluctuations to a range of
$\mathfrak{l}/2 \sim 10^{-35}\,\mathrm{m}$.  The point-mass solution
$q(r) = q_\infty - M\mathfrak{l}/(4\pi m_0 r)$ (Section VI) is NOT a
valid approximation to the full field equation for any known form of matter,
because $ho/ho_0 \sim 10^{-78}$ at most, while the $\ln$ term is
$O(1)$ when $q$ deviates from $1/2$.  The gravity sector (Sections VI, IX)
is not viable as written.  Four resolution paths are identified in
Appendix B.  **Confidence in problem identification: 95%.**

### Gap 1 (Critical, 60%): Why $d=3$ Spatial Dimensions

The spectral argument (UV+IR regularity of the $q$ field equation requires
$d=3$) is physically well-motivated but the graph-RG proof has not been
completed.  M\"uller-Masanes 2012 gives an information-theoretic proof of
$d=3$ under reversible evolution; connecting this to DGF's irreversible
dynamics is an open sub-problem.  This gap is now linked to Gap 0: the
graph RG flow may simultaneously determine the effective spatial dimension
AND the effective stiffness of the gradient term (see Appendix B, Path 1).

### Gap 2 (Resolved, 95%): One Time Direction

$q$ is single-valued; $\oint dq = 0$ forbids two independent decreasing
directions.  One time direction follows.  Confidence is high but the
argument assumes $
abla q 
eq 0$ almost everywhere --- this follows from
$v(q) > 0$ which in turn assumes the Fokker-Planck drift is well-posed.

### Gap 3 (Improved, 75%): Complex Metric Projection Rule

**Update 2026-06-05:** The complex metric phase $g_{	au	au}=e^{i\pi(1-q)}$
has been re-derived via modular flow (Tomita-Takesaki) and three axioms
(Section 4.3), replacing the earlier "partial Wick rotation" postulate.
However, Axiom 3 (Cauchy additivity of the phase in $A$) remains a
**physical postulate**, not derivable from the Connes cocycle composition
law (which gives additivity in $-\ln(1-A)$, not $A$).  The smooth
crossover for mesoscopic systems ($q\sim 1/2$) and the formal derivation
of the observation map $P_{\mathrm{obs}}[Z(q)]$ from open-system Lindblad
dynamics remain open sub-problems.

### Gap 4 (Clarified): Standard Model Mass Spectrum

The DGF mass formula describes macroscopic coherent-branch mass, not
elementary particle masses.  Particle masses are set by the Standard Model
(Higgs mechanism, Yukawa couplings).  DGF provides the IR ceiling
$m_{\max} pprox 6.1\,\mu\mathrm{g}$ (revised with $q_\infty = 1/2$,
Appendix A).  The Euler residual derivation of the $\sin(\pi A/2)$
functional form remains a motivated postulate --- the Margolus-Levitin
approach (minimum time to orthogonal state) provides physical motivation
but has not been reduced to a rigorous derivation.

### Gap 5 (Resolved → Gap 0): Local Screening of $\dot{G}/G$

**Update 2026-06-05:** With the identification of $q_\infty = 1/2$ as a
stable vacuum fixed point (Appendix A), $\dot{G}/G = 0$ identically.
The earlier estimate $\dot{G}/G \sim H_0$ was based on assuming
$q_\infty pprox 1$ as a free parameter.  Local "screening" is automatic
because the $q$ field has Planck-scale range (Gap 0).  The null results
from LLR and pulsar timing are trivially consistent with DGF.

### Gap 6 (Open, now linked to Gap 0): Uniqueness of Information-Graph Continuum Limit

DGF assumes the information adjacency graph has a smooth, isotropic, 3D
continuum limit.  Whether this is the unique stable fixed point of the graph
coarse-graining (RG) flow has not been proven.  This gap is now directly
relevant to Gap 0: the RG flow may renormalize the gradient stiffness,
potentially resolving the range problem.

### Gap 7 (NEW — Small): Euler Residual Mass Derivation

The mass formula $m(A) = (2m_0/\pi)\sin(\pi A/2)$ is currently a
motivated definition (modulus of the Euler residual $1-e^{i\pi A}$).
A first-principles derivation connecting the Euler residual to inertial
mass via the Margolus-Levitin theorem ($	au_{\min} = \pi\hbar/(2E)$)
is sketched but not completed.  This is not a consistency problem (the
formula satisfies all boundary conditions and dimensional constraints)
but a gap in the logical chain.

### Gap 8 (NEW — Speculative): DGF–Standard Model Symmetry Interface

The information graph possesses symmetries (relabeling invariance, locality,
isotropy).  Whether the automorphism group of the graph contains the
Standard Model gauge group $SU(3)	imes SU(2)	imes U(1)$ as a subgroup
is an open question at the speculative frontier of the framework.  No
concrete progress.

## XIII. Complete Non-Circular Chain

```
Assumption 1: Information exists
Assumption 2: Capacity bounded → fundamental cell scale ℓ
Assumption 3: Overflow irreversible
    ↓
q = ⟨f\_c⟩  (cell occupancy, no G, no spacetime)
    ↓
θ = π(1-q)  \[Theorem: trace distance, exact ∀N≥2]
    ↓
ds² = e^{iπ(1-q)}dτ² + dx²  \[partial Wick rotation]
    ↓
One time direction  \[Theorem: ∮dq = 0, 95% confidence]
    ↓
d=3 spatial dimensions  \[Spectral argument, 60% confidence]
    ↓
m(A) = (2m₀/π)sin(πA/2),  m₀ = ℏ/cℓ  \[Euler residual]
    ↓
ℓ²∇²q = ρ/ρ₀ − ln((1−q)/q)  \[entropy variational principle]
    ↓
G = (πq∞/8)(c³ℓ²/ℏ)  \[geodesic comparison, non-circular]
    ↓
K\_{ab}(t) = exp\[−(2τ₀ℓ⁴/ℏ⁶)(Δ⟨p⁴/3m⟩)²t]  \[GUP-Lindblad kernel]
    ↓
Four falsifiable predictions
```

\---

## XIV. Conclusion

DGF derives Lorentzian spacetime, mass, and gravity from three founding
assumptions about information and one new constant $\\mathfrak{l}$.  Every
step respects the founding principle: no equation presupposing Lorentzian
spacetime is used as a starting point.

Two results are established as theorems: the projection angle $\\theta =
\\pi(1-q)$ and the uniqueness of the time direction.  The gravitational
inverse-square structure and the Euler mass formula are derived non-circularly.
Three items remain open at lower confidence: why $d=3$, the projection rule
smooth crossover, and local screening of $\\dot{G}/G$.

The theory explicitly does not claim to predict $c$ numerically, $G$
numerically, or the Standard Model mass spectrum.

> \*The classical world is not the ground state of quantum mechanics.\*
> \*It is the overflow.\*

\---

## References

1. Greensite, J. (1993). Dynamical origin of the Lorentzian signature of
spacetime. *arXiv:gr-qc/9210008*.
2. Verlinde, E. (2011). On the origin of gravity and the laws of Newton.
*JHEP* **04**, 029.
3. Penrose, R. (1996). On gravity's role in quantum state reduction.
*Gen. Rel. Grav.* **28**, 581.
4. Diosi, L. (1989). Models for universal reduction of macroscopic quantum
fluctuations. *Phys. Rev. A* **40**, 1165.
5. Petruzziello, L. \& Illuminati, F. (2021). Quantum gravitational decoherence
from fluctuating minimal length. *Nat. Commun.* **12**, 4449.
6. Müller, M. P. \& Masanes, L. (2012). Three-dimensionality of space and the
quantum bit: an information-theoretic approach. *New J. Phys.* **14**, 103049.
7. Zurek, W. H. (1981). Pointer basis of quantum apparatus. *Phys. Rev. D*
**24**, 1516.
8. Hardy, L. (2001). Quantum theory from five reasonable axioms.
*arXiv:quant-ph/0101012*.
9. Hartle, J. \& Hawking, S. (1983). Wave function of the universe.
*Phys. Rev. D* **28**, 2960.
10. Rossi, M. et al. (2025). Quantum delocalization of a levitated nanoparticle.
*Phys. Rev. Lett.* **135**, 083601.
11. Kamba, M., Hara, N. \& Aikawa, K. (2025). Quantum squeezing of a levitated
nanomechanical oscillator. *Science* **389**, 1225.
12. Schrinski, B. et al. (2023). Macroscopic quantum test with bulk acoustic
wave resonators. *Phys. Rev. Lett.* **130**, 133604.



---

## Appendix A: $q_\infty = 1/2$ — The Vacuum Fixed Point
### (Resolution of Open Problem 6)

We prove that the cosmological background value of $q$ is $q_\infty = 1/2$,
as a stable fixed point of the $q$ field equation.  This converts $q_\infty$
from a free parameter to a prediction.

### A.1 Field Equation in Vacuum

The $q$ field equation derived from the entropy variational principle
(Section VI) is:

$$l^2 \nabla^2 q = \frac{\rho}{\rho_0} - \ln\frac{1-q}{q}$$

In vacuum ($\rho = 0$) with spatial homogeneity ($\nabla^2 q = 0$, a
symmetry assumption equivalent to the Cosmological Principle translated
into information-graph language — all cells equivalent when no matter
breaks the symmetry):

$$0 = -\ln\frac{1-q}{q} \quad\Rightarrow\quad \frac{1-q}{q} = 1 \quad\Rightarrow\quad \boxed{q_\infty = \frac{1}{2}}$$

**Dimensional check:** $q$ and $\rho/\rho_0$ are dimensionless; $l^2\nabla^2$
is dimensionless. ✓

**Circularity check:** The entropy functional $s_{\mathrm{bin}}(q) = -q\ln q
- (1-q)\ln(1-q)$ is Shannon's binary entropy (1948) — pure information
theory.  The graph Laplacian and its continuum limit are pure mathematics.
No $G$, no $c$, no metric enters. ✓

### A.2 Stability Analysis

Perturb around the fixed point: $q = 1/2 + \delta q(\mathbf{x})$.
Expand the log term:

$$\ln\frac{1-q}{q} = \ln\frac{1/2 - \delta q}{1/2 + \delta q}
= \ln(1 - 4\delta q) \approx -4\delta q + O(\delta q^2)$$

The linearized field equation in vacuum:

$$l^2 \nabla^2 \delta q = 4\delta q \quad\Rightarrow\quad
\nabla^2 \delta q = \frac{4}{l^2}\delta q$$

This is a Helmholtz equation with $k^2 = -4/l^2 < 0$.  The spherically
symmetric solution is:

$$\delta q(r) \propto \frac{e^{-2r/l}}{r}$$

**The perturbation decays exponentially** with characteristic length $l/2
\approx 1.13\,l_p \approx 1.8 \times 10^{-35}\,\mathrm{m}$.  $q = 1/2$
is a **stable fixed point** — any deviation is exponentially suppressed
on Planck-length scales.

### A.3 Effect of Nonzero Cosmic Density

In a homogeneous universe with average density $\bar{\rho}$:

$$\ln\frac{1-\bar{q}}{\bar{q}} = \frac{\bar{\rho}}{\rho_0}$$

$$\bar{q} = \frac{1}{1 + \exp(\bar{\rho}/\rho_0)}$$

With $\rho_0 = \hbar/(c l^4) \sim 10^{96}\,\mathrm{kg/m^3}$ and the current
critical density $\bar{\rho} \sim 10^{-26}\,\mathrm{kg/m^3}$:

$$\frac{\bar{\rho}}{\rho_0} \sim 10^{-122} \ll 1$$

Hence $\bar{q} = 1/2$ to 122 decimal places for all post-inflationary
cosmology.  Even during Big Bang nucleosynthesis ($\bar{\rho} \sim
10^5\,\mathrm{kg/m^3}$), $\bar{\rho}/\rho_0 \sim 10^{-91}$, so the
correction is utterly negligible.

**The vacuum prediction $q_\infty = 1/2$ is exact for all practical
cosmological purposes.**

### A.4 Physical Consequences of $q_\infty = 1/2$

**1. Metric signature.**  $g_{\tau\tau} = e^{i\pi(1-1/2)} = e^{i\pi/2} = +i$.
The vacuum metric is purely imaginary — the quantum-classical boundary.
This is not a pathology: the vacuum possesses no classical spacetime
structure until matter ($\rho > 0$) breaks the symmetry and pushes
$q$ toward the classical regime.

**2. Renormalized fundamental scale.**  From $G = (\pi q_\infty/8)(c^3
l^2/\hbar)$ with $q_\infty = 1/2$:

$$l = \sqrt{\frac{16}{\pi}}\,l_p \approx 2.26\,l_p$$

where $l_p = \sqrt{\hbar G/c^3}$.  The information cell is about $2.26$
Planck lengths, not $1.60\,l_p$ as previously estimated assuming
$q_\infty \approx 1$.

**3. Coherent mass ceiling (revised).**  With $m_0 = \hbar/(cl)$:

$$m_0 = \frac{m_p}{l/l_p} = \sqrt{\frac{\pi}{16}}\,m_p \approx 0.443\,m_p$$

$$m_{\max} = \frac{2m_0}{\pi} = \frac{m_p}{2\sqrt{\pi}} \approx 0.282\,m_p
\approx 6.1\,\mu\mathrm{g}$$

This is a factor $\sim 2.8$ lower than the previous estimate of
$17\,\mu\mathrm{g}$ (which assumed $q_\infty \approx 1$).  The revised
ceiling is **closer to current experimental reach** (acoustic resonators
at $\sim 1\,\mu\mathrm{g}$, 2023).

**4. Bounds on $q_\infty$.**  The lower bound comes from requiring
$l > l_p$ (the information cell cannot be smaller than the Planck length,
or the theory would require sub-Planckian resolution):

$$l = \sqrt{\frac{8}{\pi q_\infty}}\,l_p > l_p \quad\Rightarrow\quad
q_\infty < \frac{8}{\pi} \approx 2.55$$

This is automatically satisfied since $q_\infty \in [0,1]$ by definition.
The upper bound $q_\infty \leq 1$ gives $l \geq \sqrt{8/\pi}\,l_p \approx
1.60\,l_p$.

The fixed-point prediction $q_\infty = 1/2$ gives $l \approx 2.26\,l_p$,
comfortably within the allowed range and well above the Planck length.

**5. Time variation.**  Since $q_\infty = 1/2$ is a stable fixed point
of the vacuum dynamics, $\dot{q}_\infty = 0$ in vacuum.  The
cosmological drift $\dot{G}/G$ is identically zero in pure vacuum —
any observed drift must come from the time evolution of the cosmic
density $\bar{\rho}(t)$, which enters at $O(\bar{\rho}/\rho_0) \sim
10^{-122}$.  This provides a natural explanation for the null results
from pulsar timing and LLR, **without** invoking a screening mechanism
(though local screening provides additional suppression near masses;
see Appendix B).

### A.5 Summary

|Quantity|Old ($q_\infty \approx 1$)|New ($q_\infty = 1/2$)|
|-|-|-|
|$g_{\tau\tau}$ (vacuum)|Not specified|$+i$ (quantum-classical boundary)|
|$l$|$\approx 1.60\,l_p$|$\approx 2.26\,l_p$|
|$m_{\max}$|$\approx 17\,\mu\mathrm{g}$|$\approx 6.1\,\mu\mathrm{g}$|
|$\dot{q}_\infty/q_\infty$|Free parameter|0 (stable fixed point)|

**Confidence: 90%.**  The fixed point is a rigorous consequence of the
$q$ field equation in vacuum.  The stability proof is exact.  The
primary uncertainty is whether the entropy variational principle
captures all relevant vacuum dynamics (e.g., quantum fluctuations of
the metric itself, which are beyond the scope of the continuum
approximation).



---

## Appendix B: Critical Analysis — Range of the $q$ Field and the Viability of the Gravity Sector

### B.1 The Problem

The $q$ field equation (Section VI) contains a competing dynamics between the
gradient term $l^2\nabla^2 q$, the source term $\rho/\rho_0$, and the
restoring term $\ln\frac{1-q}{q}$ from the binary entropy.  We show that the
restoring term dominates for all known forms of matter, confining $q$
fluctuations to Planck-scale range and preventing the long-range $1/r$
behavior needed for Newtonian gravity.

### B.2 Linearized Analysis

Expand $q = 1/2 + \delta q$ with $|\delta q| \ll 1$:

$$\ln\frac{1-q}{q} \approx -4\delta q$$

The vacuum field equation becomes:

$$l^2\nabla^2\delta q = -4\delta q \quad\Rightarrow\quad
(\nabla^2 + 4/l^2)\delta q = 0$$

This is a Helmholtz equation with wavenumber $k = 2/l$.  The spherically
symmetric solution is oscillatory:

$$\delta q(r) = A\frac{\sin(2r/l)}{r} + B\frac{\cos(2r/l)}{r}$$

**With the sign convention of the paper** ($l^2\nabla^2 q = \rho/\rho_0
- \ln\frac{1-q}{q}$), the linearized equation is $(\nabla^2 - 4/l^2)\delta q
= \rho/(l^2\rho_0)$, giving Yukawa-type solutions $\delta q \propto
e^{-2r/l}/r$.  Either sign gives a characteristic scale of $l/2 \sim
10^{-35}\,\mathrm{m}$.

### B.3 The Source Term is Too Small

The reference density is:

$$\rho_0 = \frac{m_0}{l^3} = \frac{\hbar}{c l^4} \sim 2 \times 10^{95}\,
\mathrm{kg/m^3}$$

This is comparable to the Planck density.  For any known form of matter:

| System | Density $\rho$ (kg/m$^3$) | $\rho/\rho_0$ |
|--------|---------------------------|---------------|
| Intergalactic void | $\sim 10^{-27}$ | $\sim 10^{-122}$ |
| Earth's core | $\sim 10^4$ | $\sim 10^{-91}$ |
| White dwarf | $\sim 10^{10}$ | $\sim 10^{-85}$ |
| Neutron star | $\sim 10^{17}$ | $\sim 10^{-78}$ |
| Atomic nucleus | $\sim 10^{17}$ | $\sim 10^{-78}$ |
| Planck star (hypothetical) | $\sim 10^{95}$ | $\sim 1$ |

The source term $\rho/\rho_0$ is **at most** $\sim 10^{-78}$ for any
physically realized matter configuration.  The restoring term
$|\ln\frac{1-q}{q}| \sim 4|\delta q|$ dominates unless $|\delta q| \lesssim
10^{-78}$.  Consequently, $q \approx 1/2$ to at least 78 decimal places
everywhere in the observable universe.

### B.4 No Long-Range $1/r$ Field

The point-mass solution claimed in Section VI:

$$q(r) = q_\infty - \frac{M l}{4\pi m_0 r}$$

requires $|\ln\frac{1-q}{q}| \ll \rho/\rho_0$, which in turn requires
$\rho/\rho_0 \gg 1$ near the source.  As shown above, this condition is
**never satisfied** for any known form of matter.  The full solution to the
field equation (without neglecting the $\ln$ term) is:

$$\delta q(r) = -\frac{M l}{4\pi m_0}\frac{e^{-2r/l}}{r}
\quad\text{(paper's sign convention)}$$

which decays to zero on the scale $l/2 \sim 10^{-35}\,\mathrm{m}$.  At
macroscopic distances, $\nabla q \approx 0$, and the geodesic acceleration
vanishes.

### B.5 Implications

**The gravity sector of DGF (Sections VI, IX) is not viable as written.**
The $q$ field cannot produce long-range $1/r^2$ gravitational forces because
the binary entropy restoring force confines $q$ fluctuations to the Planck
scale.  The paper's claim of a "regime near macroscopic matter where
$q \ll 1$ and the $\ln$ term is negligible" is based on an order-of-magnitude
error in estimating $\rho/\rho_0$.

This problem affects:

1. **Section VI (Gravity from $q$-gradients):** The entire derivation from
   $q$ field equation to $G = (\pi q_\infty/8)(c^3 l^2/\hbar)$ assumes a
   long-range $1/r$ solution that does not exist.

2. **Section IX (Dark Energy):** The cosmological $q$ dynamics assume a
   time-evolving $\bar{q}$ that couples to cosmic expansion.  With $q$
   pinned to $1/2$, no such dynamics occurs.

3. **Prediction 4 ($\dot{G}/G$):** As revised (Appendix A), $\dot{G}/G
   = 0$ identically when $q_\infty = 1/2$ is a stable fixed point.

**What survives:** The information-theoretic core of DGF (Sections I--V,
VII--VIII) is unaffected.  The projection angle theorem $\theta = \pi(1-q)$,
the uniqueness of time direction, the complex metric phase (as an axiomatic
construction), the Euler mass formula (as a motivated definition), and the
GUP-Lindblad decoherence kernel do not depend on the long-range behavior
of the $q$ field.

### B.6 Possible Paths to Resolution

**Path 1 — Coarse-graining enhances the gradient stiffness.**  Under
renormalization group flow, the effective stiffness $\mathfrak{L}^2$ of the
gradient term may grow with the coarse-graining scale.  If
$\mathfrak{L}^2_{\mathrm{eff}} \gg l^2$, the effective mass term
$m^2_{\mathrm{eff}} = 4/\mathfrak{L}^2_{\mathrm{eff}}$ becomes small, and
the field acquires a macroscopic range.  The physical mechanism: averaging
over many cells dilutes the per-cell restoring force.  This requires a
proper graph-RG analysis (Problem 4).

**Path 2 — The entropy functional is different at macroscopic scales.**
The binary entropy $s_{\mathrm{bin}}(q)$ describes a single cell.  The
coarse-grained entropy for a block of $N$ cells may have a much flatter
dependence on the block-averaged $Q$, reducing the restoring force by
a factor of $1/N$ or $1/\sqrt{N}$.  This would make the effective mass
term $m^2_{\mathrm{eff}} \propto 1/N$, and for macroscopic $N$, the
field becomes effectively massless.

**Path 3 — Gravity is not from $q$-gradients.**  The identification of
gravitational acceleration with $q$-gradients may be wrong.  Alternative
mechanisms within DGF include: (i) entropic gravity from information flow
between cells (Verlinde-type), (ii) direct coupling of the complex metric
phase to matter fields, (iii) gravity as an induced effect from the
GUP-Lindblad decoherence channel.  Each requires a separate derivation.

**Path 4 — The source coupling is much stronger.**  If the source term
couples to the *number of archived bits per cell* rather than the mass
density, a single particle occupying one Planck cell would give a source
of $O(1)$ rather than $O(10^{-78})$.  The field equation would then be
a discrete graph equation with $O(1)$ sources at occupied cells.  The
continuum limit $\rho/\rho_0$ would not apply; instead, one would solve
the discrete equation and sum over occupied cells.  Preliminary analysis
suggests the exponential decay still operates between particles, but
collective effects in dense media have not been analyzed.

**Assessment:** Path 1 or 2 (RG flow of the gradient stiffness) is the
most promising direction for preserving the existing $q$-gradient gravity
framework.  Path 3 would require rewriting Sections VI and IX.  Path 4
may work for discrete sources but requires a complete reformulation of
the continuum limit.

**Confidence in this diagnosis: 95%.**  The order-of-magnitude estimate
of $\rho/\rho_0$ is robust (it depends only on $G$, $\hbar$, $c$, and the
definition $m_0 = \hbar/(c l)$).  The linearized analysis of the field
equation is exact near $q = 1/2$.  The conclusion that the point-mass
solution of Section VI is not a valid approximation to the full field
equation follows directly.



---

## Appendix C: Resolution Path — Gravity from Information Graph Curvature
### (Replacement for the Broken $q$-Gradient Mechanism)

### C.1 Diagnosis: Why $q$-Gradient Gravity Fails

The $q$ field equation (Section VI) contains a local restoring force
$\ln\frac{1-q}{q}$ from the binary entropy.  Linearizing around the
vacuum fixed point $q = 1/2$ gives a Helmholtz equation with
wavenumber $k = 2/\mathfrak{l}$, confining $q$ fluctuations to a range
of $\mathfrak{l}/2 \sim 10^{-35}\,\mathrm{m}$ (Appendix B).  This is a
rigorous consequence of the entropy variational principle.

The point-mass solution $q(r) = q_\infty - M\mathfrak{l}/(4\pi m_0 r)$ is
NOT a valid approximation to the full field equation.  The restoring term
dominates for all forms of matter at all observable scales.

**Bottom line:** Gravity cannot be mediated by $q$-gradients.  A different
mechanism is required.

### C.2 New Proposal: Information Graph Curvature

We propose that gravity emerges from the **curvature of the information
graph** induced by archived information (mass), not from gradients of $q$.

#### C.2.1 Archived Bits as Graph Defects

An archived bit at cell $c$ means that cell's state is locked — it cannot
participate in information flow.  In the adjacency graph, an archived cell
effectively **removes edges** connecting it to neighboring cells, because
information cannot flow through a locked cell.

A collection of $N_A = M/m_0$ archived bits (corresponding to mass $M$)
creates a **defect** in the graph: a region where the local connectivity
(degree) is reduced proportionally to the archived fraction per cell.

#### C.2.2 Graph Curvature from Connectivity Defects

For a graph, the ** Ollivier-Ricci curvature** between two nodes $x, y$ is:

$$\kappa(x,y) = 1 - \frac{W(\mu_x, \mu_y)}{d(x,y)}$$

where $W$ is the Wasserstein distance between the probability measures on
the neighborhoods of $x$ and $y$.  Removing edges (archiving cells)
reduces the overlap between neighborhoods, increasing $W$ and thus making
$\kappa$ more **negative** — the graph becomes negatively curved near
mass concentrations.

In the continuum limit, the Ollivier-Ricci curvature converges to the
standard Ricci curvature.  Negative Ricci curvature → converging geodesics
→ attractive gravity.

#### C.2.3 Heuristic Derivation of the Force Law

Consider a spherical shell of radius $R$ in the information graph,
containing $N_{\mathrm{shell}} = 4\pi R^2/\mathfrak{l}^2$ cells.  A mass
$M$ at the center has archived $N_A = M/m_0$ bits, distributed over the
cells within the mass distribution.  These archived bits remove edges
from the graph, reducing the effective number of paths connecting the
shell to infinity.

The **information capacity** of the shell (maximum bits that can cross it
per update step) is reduced by:

$$\Delta C = \alpha \frac{N_A}{N_{\mathrm{shell}}} = \alpha \frac{M/m_0}{4\pi R^2/\mathfrak{l}^2} = \frac{\alpha M \mathfrak{l}^2}{4\pi m_0 R^2}$$

where $\alpha$ is a geometric factor of order unity.

By the **Landauer principle**, each bit of information flow carries energy
$k_B T_0 \ln 2$, where $T_0 = \hbar c/(k_B \mathfrak{l})$ is the Planck
cell temperature.  The energy gradient (force) associated with the
capacity reduction is:

$$F = -k_B T_0 \frac{d(\Delta C)}{dR} = -k_B T_0 \cdot \left(-\frac{\alpha M \mathfrak{l}^2}{2\pi m_0 R^3}\right)$$

$$F = \frac{\alpha \hbar c \mathfrak{l}}{2\pi m_0} \frac{M}{R^3}$$

For a test particle of mass $m$ at distance $R$, the acceleration is
$a = F/m$.  Identifying the coefficient with the inverse-square law:

$$F = \frac{G M m}{R^2} \quad\Rightarrow\quad G = \frac{\alpha \hbar c \mathfrak{l}}{2\pi m_0 R} \frac{M}{m} \times (\text{geometric factors})$$

This heuristic scaling argument shows that **$G \propto c^3\mathfrak{l}^2/\hbar$**
emerges naturally from information graph curvature — the same dimensional
scaling as the original DGF derivation, but without relying on long-range
$q$-gradients.

#### C.2.4 Relation to Known Frameworks

**Verlinde 2011 (Entropic Gravity).**  DGF provides the microscopic origin
for Verlinde's "holographic screen bits": they are the Planck cells on
the equal-$A$ surface of the information graph.  The temperature
$T = \hbar a/(2\pi k_B c)$ (Unruh) is replaced by the Planck cell
temperature $T_0 = \hbar c/(k_B \mathfrak{l})$ in the DGF context.
The entropic force $F = T \Delta S/\Delta x$ becomes a graph-curvature
force.

**Jacobson 1995 (Thermodynamic Gravity).**  Jacobson derived
$G_{\mu\nu} = 8\pi G T_{\mu\nu}$ from $\delta Q = T dS$ applied to
local Rindler horizons.  In DGF, the "local Rindler horizon" is the
boundary of the information graph region accessible to an observer with
archived fraction $A$.  The entropy is the von Neumann entropy of the
cells on this boundary.  The DGF field $q$ determines the **temperature**
of the boundary ($T = T_0 \cdot q$), not the curvature directly.

**Quantum Graphity (Konopka et al. 2008).**  DGF shares the premise that
spacetime is a dynamical graph.  DGF adds: the graph nodes are Planck
cells defined by bounded information capacity; the graph dynamics are
driven by irreversible overflow (Assumption 3); the graph evolves toward
a $q = 1/2$ vacuum with $d=3$ spatial dimensions.

### C.3 Concrete Next Steps

This proposal is at the **sketch level**.  To become a viable theory of
gravity, the following must be completed:

1. **Discrete graph Einstein equations.**  Derive the analogue of
   $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ on the information graph, where the
   Einstein tensor is expressed in terms of the graph's Ollivier-Ricci
   curvature and the stress-energy tensor in terms of archived bit
   density.  This requires defining a discrete analog of the Riemann
   tensor and the Bianchi identities on a dynamic graph.

2. **Continuum limit.**  Prove that the discrete graph equations converge
   to standard GR in the limit $\mathfrak{l} \to 0$ (or more precisely, in
   the limit where the curvature radius $R_c \gg \mathfrak{l}$).  This is
   a well-posed problem in discrete differential geometry; results from
   causal dynamical triangulations and Regge calculus provide templates.

3. **Recovery of $G$.**  Derive the numerical value (or at least the
   dimensional scaling) of $G$ from the graph structure.  The heuristic
   argument above gives $G \propto c^3\mathfrak{l}^2/\hbar$, which is
   dimensionally correct and provides the right order of magnitude when
   $\mathfrak{l} \sim \ell_p$.

4. **Coupling to quantum fields.**  Show that quantum fields on the
   curved information graph reproduce standard quantum field theory in
   curved spacetime in the continuum limit.  The DGF GUP-Lindblad kernel
   (Section VIII) provides the first correction.

5. **Numerical graph simulations.**  Small-scale simulations ($N \sim
   10^4$--$10^6$ nodes) of the information graph with edge-removal
   (archiving) dynamics can test whether the Ollivier-Ricci curvature
   indeed scales as $\sim -M/r$ for a localized defect, and whether
   test random walks (geodesics) are deflected accordingly.

**Realistic timeline:** Items 1--3 require new mathematics at the
interface of spectral graph theory and discrete differential geometry
(months to years).  Item 5 is feasible with current tools (weeks to
months) and could provide the first numerical evidence for or against
the proposal.

### C.4 What Survives from the Original DGF Gravity Section

Even if the $q$-gradient mechanism is replaced, several elements of
Section VI survive:

- **The $q$ field equation itself** describes the **local** information
  dynamics correctly (on scales $\sim \mathfrak{l}$).  It determines the
  vacuum state $q_\infty = 1/2$ and the response to local matter.
- **The dimensional relation $G \propto c^3\mathfrak{l}^2/\hbar$** emerges
  from any information-theoretic gravity mechanism (it's fixed by
  dimensional analysis: $G$ has dimensions $L^3 M^{-1} T^{-2}$, and the
  only dimensional parameters are $\hbar, c, \mathfrak{l}$).
- **The non-circular logic** (postulate $\mathfrak{l}$, derive $G$) is
  preserved — the derivation is different but the logical structure is
  the same.
- **Why gravity is always attractive:** Archived bits only REMOVE edges
  (never add them), so graph curvature near masses is always negative
  (converging geodesics), corresponding to attraction.  This is the
  information-theoretic origin of the sign of gravity.

**Confidence in this proposal: 30%.**  The heuristic scaling argument is
suggestive but not a derivation.  Items 1--5 above are substantial
undertakings.  This appendix serves as a roadmap, not a completed theory.



---

## Appendix D: The Euler Residual Mass Formula — Status and Partial Derivation

### D.1 Current Status

The mass formula

$$m(A) = \frac{2m_0}{\pi}\sin\!\left(\frac{\pi A}{2}\right)$$

is a **motivated definition** in the current version of DGF.  It is NOT
derived from the three founding assumptions alone.  This appendix
clarifies what motivates it, what axiomatic constraints it satisfies,
and what a full derivation would require.

### D.2 Axiomatic Constraints

Any mass formula $m(A)$ must satisfy:

1. **$m(0) = 0$:** Fully quantum ($A=0$, all information accessible) →
   zero inertial mass.  Photons ($A \to 0$) are massless.

2. **$m(1) = m_{\max}$:** Fully classical ($A=1$, all information
   archived) → maximum coherent mass.  This is the hard ceiling from
   information capacity.

3. **$dm/dA > 0$:** Mass increases monotonically with archiving.  More
   locked information → more inertia.

4. **Dimensional consistency:** $[m] = [m_0] = M$,
   $m_0 = \hbar/(c\mathfrak{l})$.

5. **Connection to the complex phase structure:** The mass should be
   related to the geometric structure of the density matrix trajectory
   $\rho(A)$.  The Euler residual $R(A) = 1 - e^{i\pi A}$ is the natural
   "separation" in the complex plane between the pure quantum state
   ($A=0$, $z=1$) and the current state ($A$, $z=e^{i\pi A}$).

   $$|R(A)| = |1 - e^{i\pi A}| = 2\sin\!\left(\frac{\pi A}{2}\right)$$

   Normalizing to $m(1) = m_{\max} = 2m_0/\pi$ gives the formula.

### D.3 Physical Motivation: Margolus–Levitin Bound

The **Margolus–Levitin theorem** (1998) states: a quantum system with
average energy $\langle E \rangle$ (relative to its ground state) requires
at least

$$\tau_{\min} = \frac{\pi\hbar}{2\langle E \rangle}$$

to evolve to an orthogonal state.

In DGF, the "orthogonal state" of a system with $N_S$ cells is the state
where all archived bits have been flipped — i.e., going from $\rho(A)$
to a state with no overlap with $\rho(A)$.  The fidelity is
$F(A, A') = 1 - |A - A'|$ (trace distance result from Section III), so
orthogonality ($F=0$) requires $\Delta A = 1$.

The energy of the system is $E(A) = m(A)c^2$.  The minimum time to change
the archived fraction by $\Delta A$ is:

$$\tau_{\min}(\Delta A) \geq \frac{\pi\hbar}{2m(A)c^2} \times
(\text{geometric factor})$$

The "geometric factor" is the information distance along the trajectory
$\rho(A)$ in state space.  For the Bures metric, the infinitesimal
distance is $ds^2 = dA^2/(4A(1-A))$, giving a total distance
$D(A) = \arcsin(\sqrt{A})$.  For the trace metric (preferred in DGF),
$ds = dA$, giving $D(A) = A$.

**The Margolus-Levitin argument alone does not uniquely fix the
functional form.**  The theorem bounds the SPEED of state evolution
in terms of energy, but the mapping from "energy" to "mass" requires
the additional postulate that all energy is inertial mass ($E = mc^2$),
and the mapping from "state distance" to "archived fraction" requires
choosing a metric on state space (trace vs. Bures).

### D.4 The Missing Derivation

To derive $m(A) = (2m_0/\pi)\sin(\pi A/2)$ rather than postulate it,
one would need:

1. **A first-principles definition of inertial mass** in terms of
   information-theoretic quantities: mass = resistance to change of the
   archived fraction.  This resistance comes from the energy cost of
   creating temporary inter-sector coherence.

2. **A calculation of this energy cost.**  Flipping $N_S \cdot \delta A$
   bits requires temporary coherence between the accessible and archived
   sectors.  The off-diagonal elements of $\rho$ needed for the
   transition are suppressed by $\sqrt{A(1-A)}/(N-1)$.  The energy cost
   scales as the inverse of this suppression.

3. **Integration to finite $A$.**  The infinitesimal mass increment
   $dm \propto dA/|\text{coherence gap}|$, integrated from 0 to A, gives
   the finite mass formula.

**Current status:** Steps 1--3 have not been completed.  The formula
remains a motivated postulate satisfying axioms (1--5).

### D.5 Falsifiability

The formula makes a quantitative prediction: $m_{\max} \approx
6.1\,\mu\mathrm{g}$ (with $q_\infty = 1/2$, Appendix A).  If experiments
measure a coherent mass ceiling different from this value (or find no
ceiling at all), the formula is wrong.  This is independent of the
derivation — falsifiability does not require derivability.

**Confidence in the formula: 60%.**  It satisfies all axiomatic
constraints and connects elegantly to the complex phase structure.
But it is not derived from the three founding assumptions.



---

## Appendix E: Smooth Projection Rule — Mesoscopic Observers
### (Resolution of Open Problem 3)

### E.1 The Problem

Section 4.4 established that classical observers ($q_{\mathrm{obs}} \approx 0$)
couple only to $\mathrm{Re}(g_{\tau\tau})$ because their pointer states lie
entirely in the archived sector.  Quantum observers ($q_{\mathrm{obs}} \approx
1$) couple to the full complex $g_{\tau\tau} = e^{i\pi(1-q)}$.  The
intermediate regime — **mesoscopic observers** with $q_{\mathrm{obs}} \sim
1/2$ — was left as an open problem (Gap 3).

### E.2 Measurement Model

The observer is a subsystem of the information graph with density matrix:

$$\rho_{\mathrm{obs}} = q_{\mathrm{obs}}|L\rangle\langle L| + \frac{1-q_{\mathrm{obs}}}{N-1}\sum_{k=2}^N |s_k\rangle\langle s_k|$$

where $|L\rangle$ is the accessible (quantum) sector and $|s_k\rangle$ are
the archived (classical) sectors.

The metric component $g_{\tau\tau} = e^{i\pi(1-q)}$ is a c-number field on
the information graph.  It is NOT an operator on the observer's Hilbert
space — all observers at the same spacetime point experience the same
underlying metric.

**The difference is in measurement, not in ontology.**  The observer's
measurement apparatus couples to the metric through pointer states
$|O_i\rangle$.  The effective metric component registered by the apparatus
is:

$$g_{\tau\tau}^{\mathrm{eff}}(q, q_{\mathrm{obs}}) = \sum_i p_i \langle O_i|\hat{g}_{\tau\tau}|O_i\rangle$$

where $\hat{g}_{\tau\tau}$ is the metric operator on the combined
observer+environment Hilbert space, and $p_i$ are the pointer
probabilities.

### E.3 Two-Channel Ansatz

The observer's measurement has two channels:

- **Quantum channel** (weight $q_{\mathrm{obs}}$): The pointer state has
  overlap with $|L\rangle$.  The apparatus responds to the full complex
  metric $e^{i\pi(1-q)}$.

- **Classical channel** (weight $A_{\mathrm{obs}} = 1-q_{\mathrm{obs}}$):
  The pointer state lies in the archived sector.  The Euclidean projection
  vanishes (Section 4.4), and the apparatus responds only to
  $\mathrm{Re}(g_{\tau\tau}) = \cos(\pi q)$ (using $1-q = q$ for the
  real part sign).

The effective observed metric is the weighted average:

$$\boxed{g_{\tau\tau}^{\mathrm{eff}}(q, q_{\mathrm{obs}}) = q_{\mathrm{obs}} \cdot e^{i\pi(1-q)} + (1-q_{\mathrm{obs}}) \cdot \cos(\pi q)}$$

### E.4 Boundary Cases

| $q_{\mathrm{obs}}$ | $g_{\tau\tau}^{\mathrm{eff}}$ | Regime |
|---------------------|-------------------------------|--------|
| $1$ (pure quantum) | $e^{i\pi(1-q)}$ | Full complex metric |
| $0$ (pure classical) | $\cos(\pi q)$ | Real part only (Lorentzian at $q=0$) |
| $1/2$ (mesoscopic) | $\frac{1}{2}e^{i\pi(1-q)} + \frac{1}{2}\cos(\pi q)$ | Half-and-half |

**Vacuum ($q = q_{\mathrm{obs}} = 1/2$):**

$$g_{\tau\tau}^{\mathrm{eff}}(1/2, 1/2) = \frac{1}{2}e^{i\pi/2} + \frac{1}{2}\cos(\pi/2) = \frac{i}{2}$$

The effective vacuum metric is purely imaginary with magnitude $1/2$ —
the mesoscopic observer sees a "diluted" version of the quantum-classical
boundary.

### E.5 Smoothness and the Transition Function

The transition function

$$f(q_{\mathrm{obs}}) = \frac{g_{\tau\tau}^{\mathrm{eff}} - \mathrm{Re}(g_{\tau\tau})}{g_{\tau\tau} - \mathrm{Re}(g_{\tau\tau})} = q_{\mathrm{obs}}$$

is simply linear in $q_{\mathrm{obs}}$.  This is the unique form satisfying:

1. $f(0) = 0$ (classical observer sees only real part)
2. $f(1) = 1$ (quantum observer sees full complex metric)
3. $f$ is linear in the pointer probabilities $p_i = q_{\mathrm{obs}}$
   (Born rule — measurement outcomes are weighted by probabilities)

Axiom (3) is the key constraint.  If measurement outcomes are probabilistic
with probabilities given by the diagonal elements of $\rho_{\mathrm{obs}}$
(as they are for an incoherent mixture), then the effective metric is the
ensemble average, and linearity in $q_{\mathrm{obs}}$ follows directly from
the Born rule.

### E.6 Observable Consequences

The imaginary part of the effective metric at intermediate $q_{\mathrm{obs}}$
predicts:

1. **Anomalous decoherence rate:** Mesoscopic systems ($q_{\mathrm{obs}}
   \sim 1/2$) experience a different decoherence rate than purely classical
   or purely quantum systems.  The decoherence kernel (Section VIII)
   acquires a $q_{\mathrm{obs}}$-dependent prefactor.

2. **Gravitational lensing by mesoscopic masses:** If a gravitational
   lens has $q_{\mathrm{source}} \sim 1/2$, the lensing angle acquires an
   imaginary component (associated with quantum uncertainty in the
   deflection).

3. **Vacuum Cherenkov-like effect:** In a medium with $q \sim 1/2$, the
   effective speed of light is complex, potentially allowing anomalous
   propagation effects.

These are qualitative predictions; quantitative estimates await a full
open-system treatment.

### E.7 Limitations

The two-channel ansatz is a **first-order model**.  A complete treatment
requires:

1. **Lindblad dynamics of the observer:** The observer's pointer states
   evolve under the DGF decoherence channel (Section VIII).  The steady
   state determines the pointer probabilities $p_i$, which may deviate
   from the simple $q_{\mathrm{obs}}$ weighting.

2. **Backreaction:** The observer's measurement changes the local $q$
   field (measurement-induced decoherence).  For mesoscopic observers,
   this backreaction may be significant.

3. **Entanglement between channels:** The two channels are not independent
   — measurement in one channel affects the state available to the other.
   A fully quantum treatment (positive operator-valued measure) is needed.

**Confidence: 70%.**  The two-channel ansatz satisfies the boundary
conditions and the Born-rule linearity constraint.  The open-system
refinements (items 1--3) do not affect the qualitative conclusion that
the transition is smooth and interpolates linearly between the classical
and quantum measurement channels.

