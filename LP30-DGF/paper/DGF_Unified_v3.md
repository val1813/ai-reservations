# 论文后续补推导原则：

# 一句话：

# 凡是预设洛伦兹时空已经存在的方程，都不能作为起点；只有不依赖时空背景、只依赖信息状态和信息容量的表达式，才是合法的出发点。

# 

# 展开一点说就是：

# 不能用的： 薛定谔方程、爱因斯坦方程、Lindblad方程、弗里德曼方程、GUP、任何含 cc c、tt t、x⃗\\vec{x} x、gμνg\_{\\mu\\nu} gμν​ 作为背景参数的方程——因为这些都预设了洛伦兹时空已经存在，而我们要推导的正是它。

# 可以用的： 只有三类——信息论（香农熵、Landauer原理、全息界）、纯数学（欧拉公式、微分几何、量纲分析）、以及 q∈\[0,1]q \\in \[0,1] q∈\[0,1] 本身。

# 判断原则只有一个： 问这个方程里有没有隐含"时空已经存在"的假设。有就不能用，没有才能用。Decoherence Geometry Framework (DGF)

## An Effective Information-Geometry Framework for Decoherence, Metric Representations, and Gravitational Interfaces

**Huang Zhongchang**  
Independent Researcher, Nanjing, China | valhuang@kaiwucl.com  
Draft v3.1-prd | 2026-06-05

\---

## Abstract

We present the Decoherence Geometry Framework (DGF) as an effective
information-geometric program, not as a completed derivation of spacetime,
mass, and gravity.  The framework asks how far one can proceed from three
assumptions about information: information exists, capacity is bounded at
scale $\\mathfrak{l}$, and overflow is irreversible.  The dimensional constant
$\\mathfrak{l}$ is treated as an information-cell scale whose absolute
normalization is not predicted in the present version.

The present draft separates established results from proposed interfaces:

1. **Projection angle** $\\theta = \\pi(1-q)$ — exact theorem from trace distance
of the maximum-entropy incoherent mixture, valid for all $N \\geq 2$.
2. **One time direction** — theorem: $q$ is a single-valued scalar, so
$\\oint dq = 0$ forbids two independent decreasing directions.
3. **$q$ field equation** as a candidate entropy-relaxation equation, first on
the information adjacency graph and then as a continuum limit.
4. **Gravitational inverse-square interface** $G \\propto c^3\\mathfrak{l}^2/\\hbar$
— obtained only after an effective $q$-gradient-to-acceleration map is
introduced and calibrated.
5. **Euler residual mass map** $m(A) = (2m\_0/\\pi)\\sin(\\pi A/2)$ — a candidate
information-distance-to-inertia relation, not yet a strict derivation of the
Standard Model or macroscopic mass spectrum.

Four structural gaps remain open: the strict graph-RG proof of $d=3$; the
derivation of the complex metric representation from information-only
principles; the first-principles bridge from $q$-gradients to laboratory
acceleration; and any nonlinear local screening mechanism for a cosmological
$\\dot{G}/G$ drift.  In the present version, the complex line element and the
force law are effective representation maps, not completed first-principles
derivations.

The proposed phenomenology is therefore downgraded to conditional tests and
consistency checks.
In particular, an order-unity suppression of gravity for coherent quantum
probes is not viable: existing atom-interferometric gravity measurements would
already have seen such an effect.  The framework explicitly does not claim to
derive the numerical value of $c$, the numerical value of $G$, the Standard
Model mass spectrum, or the absolute normalization of $q\_\\infty$ without an
independent determination of $\\mathfrak{l}$.

\---

## I. Founding Assumptions and the Inversion

### 1.1 The Standard Picture Inverted as a Working Program

Conventional physics treats the classical world as the default and asks how
quantum mechanics emerges.  DGF explores the inverse working hypothesis: the
accessible quantum information state is primary, and classical observables are
what remains after part of that information has been irreversibly archived at
the cell scale.

> \*Working slogan: classicality is the archived part of inaccessible
> information.\*

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
background parameters.  The allowed inputs are information-theoretic
quantities, $\\hbar$, $k\_B$, $\\mathfrak{l}$, and pure mathematics.  The speed
$c$ enters only as a posterior conversion scale in effective spacetime
interfaces, not as a numerically predicted constant.

### 1.4 Status and Scope of This Draft

This draft is a constrained effective framework.  Its purpose is to separate
which parts of DGF are information-theoretic statements, which parts are
representation choices, and which parts are phenomenological interfaces to
standard spacetime physics.

Four limitations are part of the result, not afterthoughts:

* A coherent quantum probe does not imply an order-unity suppression of
  gravity.  Existing atom-interferometric gravity measurements exclude that
  interpretation.
* The linear point-source $q$ solution does not screen a cosmological
  $\\dot{G}/G$ drift.
* $G$ fixes only $q\_\\infty\\mathfrak{l}^2$, so the absolute normalization of
  $q\_\\infty$ is not identifiable without an independent $\\mathfrak{l}$.
* The graph continuum limit should be stated as a three-dimensional isotropic
  universality class, not as microscopic uniqueness of $\\mathbb{Z}^3$.

Accordingly, the paper should be read as an auditable parametrization and
interface hypothesis.  It does not yet provide a fundamental derivation of
Lorentzian geometry, inertia, or gravitational acceleration.

### 1.5 Derived Scales

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

### 4.3 The Complex Metric-Like Representation

The exact result from Section III is the information angle
$\\theta=\\pi(1-q)$.  A minimal one-parameter complex quadratic representation
that realizes the two required endpoints is:

$$\\boxed{Q\_q = e^{i\\pi(1-q)},d\\tau'^2 + dx^2 + dy^2 + dz^2}$$

This is not yet a first-principles derivation of a physical metric.  It is a
representation map from the information coordinate $q$ into a complex
quadratic form.  Deriving why this representation, rather than another
monotone embedding of $\\theta$, is forced by information-only axioms remains
open.

**Boundary conditions:**

|$q$|$Q\_{\\tau\\tau}$|Effective signature|Physics|
|-|-|-|-|
|$1$|$+1$|Euclidean|Pure quantum ✓|
|$1/2$|$+i$|Complex|Quantum-classical boundary ✓|
|$0$|$-1$|Lorentzian|Classical (Minkowski) ✓|

The imaginary part $\\sin\[\\pi(1-q)]$ is not discarded in the representation.
It encodes the surviving Euclidean component — the quantum coherence that has
not been archived.  Schrödinger, Lindblad, or path-integral dynamics may be
used later as consistency interfaces, but not as starting points for deriving
this map, because they already presuppose time-evolution structure.

### 4.4 Projection Rule: Why Classical Observers See $\\mathrm{Re}(g)$

A classical observer has archived information $A \\approx 1$ ($q \\approx 0$).
Its pointer states $|O\_i\\rangle$ are eigenstates of the overflow operator in
the classical sector.  The Euclidean projector expectation vanishes:

$$\\langle O\_i|\\hat{P}\_{\\mathrm{Euc}}|O\_i\\rangle \\approx 0$$

Therefore the measurement outcome of any represented geometric interval is:

$$\\langle Q\_q\\rangle\_{\\mathrm{obs}} = \\mathrm{Re}(Q\_{\\tau\\tau}),d\\tau'^2 + d\\mathbf{x}^2
= -\\cos\[\\pi(1-q)],d\\tau'^2 + d\\mathbf{x}^2$$

At $q\\to 0$: the represented interval approaches
$-d\\tau'^2 + d\\mathbf{x}^2$ — the Minkowski form. ✓

**Safe claim (lowered):** The projection is observer-dependent in this
effective representation.  Classical observers ($q\\approx 0$) couple only to
the real Lorentzian component.  The smooth crossover for mesoscopic observers
($q\\sim 1/2$), and the derivation of the observation map
$P\_{\\mathrm{obs}}[Q\_q]$ from information-only principles, remain open
(Section XII Gap 3).  Lindblad dynamics can only be used as a posterior
laboratory interface, not as the fundamental derivation.

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

### 6.2 Effective Acceleration Interface

If the complex quadratic representation is interpreted in the classical
sector as an effective metric-like object, its real part gives the following
GR-language translation.  This is an interface calculation, not a
first-principles derivation of the geodesic equation from the information
graph.

From $Q\_{\\tau\\tau} = e^{i\\pi(1-q)}$, the corresponding formal Christoffel
symbol would be:

$$\\Gamma^k\_{\\tau\\tau} = \\frac{i\\pi}{2}e^{i\\pi(1-q)}\\partial\_k q$$

Near $q\\to 0$: $\\delta g\_{\\tau\\tau} \\equiv -\\cos\[\\pi(1-q)]+1 \\approx \\pi^2 q^2/2$.
Observable (real-part) acceleration, slow-motion limit:

$$\\mathbf{a} = -\\frac{c^2\\pi^2}{2},q,\\nabla q$$

Substituting the point-mass solution with $q\\approx q\_\\infty \\sim 1$:

$$\\mathbf{a} = -\\frac{c^2\\pi q\_\\infty\\mathfrak{l}}{8m\_0}\\frac{M}{r^2}\\hat{\\mathbf{r}}$$

### 6.3 Calibration of $G$ and Parameter Identifiability

Comparing with Newton $\\mathbf{a} = -GM/r^2$:

$$\\boxed{G = \\frac{\\pi q\_\\infty}{8}\\cdot\\frac{c^3\\mathfrak{l}^2}{\\hbar}}$$

**Circularity check:** $\\mathfrak{l}$, $\\hbar$, $c$, $q\_\\infty$ — no $G$
is used to define the microscopic variables.  The comparison with Newtonian
gravity is, however, an empirical calibration of the effective interface, not
a derivation of the numerical value of $G$. ✓  
**Dimensional check:** $\[c^3\\mathfrak{l}^2/\\hbar] = L^3M^{-1}T^{-2} = \[G]$. ✓

The measured Newton constant fixes only the product:

$$\\boxed{q\_\\infty\\mathfrak{l}^2=\\frac{8}{\\pi}l\_P^2}$$

Therefore $q\_\\infty$ is not separately identifiable from $G$ unless
$\\mathfrak{l}$ is independently determined.  If $0<q\_\\infty\\leq 1$, then:

$$\\boxed{\\mathfrak{l}\\geq \\sqrt{\\frac{8}{\\pi}}\\,l\_P}$$

but there is no nonzero lower bound on $q\_\\infty$ from $G$ alone.

$$\\mathfrak{l} = \\sqrt{\\frac{8}{\\pi q\_\\infty}\\cdot\\frac{\\hbar G}{c^3}}
= \\sqrt{\\frac{8}{\\pi q\_\\infty}}\,l\_P$$

**Safe claim:** DGF obtains the inverse-square scaling from the
three-dimensional Green function of the capacity Laplacian, conditional on a
three-dimensional continuum limit.  The conversion from dimensionless
information curvature to laboratory acceleration is an effective interface
whose normalization is calibrated by $G$.  Cosmological probes can constrain
the evolution of $q\_\\infty\\mathfrak{l}^2$; with constant $\\mathfrak{l}$ they
constrain $q\_\\infty(z)/q\_\\infty(0)$, not the absolute value of
$q\_\\infty(0)$.

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

## X. Conditional Tests and Consistency Checks

### Test 1: Conditional Source-State Gravity Modification

$$G\_{\\mathrm{eff}}(q) = \\frac{G}{\\sqrt{1+\\pi^2 q^2}}$$

At $q=1$, this formula gives $G\_{\\mathrm{eff}}/G=1/\\sqrt{1+\\pi^2}\\approx
0.303$, an order-unity suppression.

**Status:** The formula cannot be interpreted as a suppression caused merely
by a coherent quantum probe.  Atom-interferometric measurements of gravity
and $G$ already use coherent quantum probes to measure classical source
masses; an order-unity reduction would have been seen.  Therefore the present
formula is not a valid prediction for BEC or atom-interferometer probes of
ordinary classical sources.

**Downgraded target:** A future test would have to place the source mass
density degrees of freedom themselves in a controlled low-archive state and
specify a source-test-environment coupling function.  Until that coupling is
derived, this item is a conditional research program, not a quantitative
prediction.

### Conditional Test 2: Coherent Mass Scale

$$m\_{\\max} = \\sqrt{\\frac{2}{\\pi}},m\_p \\approx 17,\\mu\\mathrm{g}$$

A candidate scale for single-branch coherent mass, conditional on the Euler
residual map being a physical inertia map rather than only an information
distance ansatz.  Current experiments reach $\\sim 1,\\mu\\mathrm{g}$ (acoustic
resonators, 2023); factor $\\sim 17$ needed for a direct stress test of the
scale.

### Candidate Test 3: $p^4/3m$ Decoherence Channel

$$K\_{ab}(t) = \\exp!\\left\[-\\frac{2\\tau\_0\\mathfrak{l}^4}{\\hbar^6}
\\left(\\Delta!\\left\\langle\\frac{p^4}{3m}\\right\\rangle\\right)^{!2}t\\right]$$

If the GUP-Lindblad interface is retained as a posterior laboratory model, the
rate scales as $(\\Delta\\langle p^4/3m\\rangle)^2$, not as gravitational
self-energy (Diosi-Penrose).  This is a conditional discriminator for the
laboratory interface, not a derivation from the founding assumptions.  Existing
ETH Zürich and Tokyo U momentum-squeezing datasets are candidate data for
retrospective analysis.

### Consistency Check 4: Secular Drift of $G$ (Cosmological Scale)

$$\\frac{\\dot{G}}{G} = \\frac{\\dot{q}\_\\infty}{q\_\\infty} \\sim H\_0
\\approx 2.3\\times10^{-18},\\mathrm{s}^{-1}$$

**Linear no-screening lemma:** The linear point-source solution does not
screen the cosmological drift.  For fixed $M$, $\\mathfrak{l}$, and $m\_0$,

$$q(r,t)=q\_\\infty(t)-\\frac{M}{4\\pi m\_0}\\frac{\\mathfrak{l}}{r}
\\quad\\Longrightarrow\\quad
\\partial\_t q(r,t)=\\dot q\_\\infty(t).$$

The local static offset and gradient do not suppress the time drift.  Hence
the current linear $q$ field equation cannot explain the difference between a
cosmological $\\dot{G}/G$ and LLR bounds.  Any viable screening mechanism must
come from a nonlinear capacity potential, source-locking boundary condition,
or other explicit dynamical completion, and must be solved in that extended
equation.

|Item|DGF status|Current status|
|-|-|-|
|Source-state gravity modification|Requires low-archive source state|No quantitative prediction yet; coherent-probe suppression is excluded|
|Coherent mass scale|$17,\\mu\\mathrm{g}$ conditional on Euler inertia map|$1,\\mu\\mathrm{g}$ reached|
|$p^4/3m$ decoherence channel|$\\propto(\\Delta\\langle p^4/3m\\rangle)^2$|Retrospective test possible|
|Secular $G$ drift (cosmological)|$\\sim 10^{-10},\\mathrm{yr}^{-1}$|Linear screening route fails; nonlinear completion needed|

\---

## XI. Relation to Existing Work

|Framework|Relation to DGF|
|-|-|
|**Greensite 1993**|Same $e^{i\\theta}$ metric; selects $\\theta=\\pi$ in $D=4$ via one-loop QFT. DGF adds: $\\theta=\\pi(1-q)$, $q$ has microscopic definition, signature change driven by information overflow, not field loops. Greensite's $D=4$ result is suggestive but uses a QFT background and cannot be used as a DGF first-principles input.|
|**Verlinde 2011**|Both organize gravitational phenomenology using information/thermodynamic language. DGF explores an archived-information order parameter $q$ and an effective acceleration interface, but does not yet derive gravity from first principles.|
|**Penrose-Diosi**|Opposite causal direction. Penrose: gravity causes collapse. DGF: decoherence causes apparent gravity. Experimental discrimination: $p^4/3m$ vs gravitational self-energy.|
|**Müller-Masanes 2012**|Gives an information-theoretic route to three-dimensional direction structure under continuous reversible dynamics of direction information units. DGF cannot directly import the result; it is compatibility support only if DGF's effective direction degrees of freedom are independently shown to satisfy the required axioms.|
|**Zurek quantum Darwinism**|Environmental decoherence motivates the accessible/archived information split. DGF uses this split as a candidate bridge toward geometry, but the geometric origin is not yet derived.|
|**Hartle-Hawking no-boundary**|No-boundary = Euclidean hemisphere glued to Lorentzian spacetime. DGF supplies a candidate $q$-parameterized representation of such a transition, but the gluing mechanism is not yet derived from information-only principles.|

\---

## XII. Open Problems

Confidence levels reflect the current state of the derivations.

**Gap 1 (Critical, 60%): Why $d=3$ spatial dimensions**

The spectral argument (UV+IR regularity of the $q$ field equation requires
$d=3$) is physically well-motivated but the graph-RG proof has not been
completed.  Müller-Masanes gives an information-theoretic route to
three-dimensional direction structure under continuous reversible dynamics of
direction information units.  DGF cannot directly import that theorem: short
time intra-cell reversibility plus long-time irreversible coarse-graining does
not determine the large-scale graph dimension.  At most, if DGF's effective
directional degrees of freedom are independently shown to satisfy the
Müller-Masanes axioms, their theorem gives compatibility support for $d=3$,
not a proof of the DGF RG fixed point.

**Gap 2 (Resolved, 95%): One time direction**

$q$ is single-valued; $\\oint dq = 0$ forbids two independent decreasing
directions.  One time direction follows.  Confidence is high but the argument
assumes $\\nabla q \\neq 0$ almost everywhere — this follows from $v(q) > 0$
which in turn assumes the Fokker-Planck drift is well-posed.

**Gap 3 (Open): Complex metric representation and projection rule**

The current complex line element is an effective representation map, not a
completed derivation of a physical metric from information-only principles.
Classical observers are modeled as coupling to the real component because
their pointer states have negligible Euclidean projector expectation.  The
smooth crossover for mesoscopic systems ($q\\sim 1/2$), and the formal
derivation of $P\_{\\mathrm{obs}}[Q\_q]$ without using Schrödinger/Lindblad
dynamics as a starting point, remain open.

**Gap 4 (Clarified): Standard Model mass spectrum**

The DGF mass formula describes macroscopic coherent-branch mass, not
elementary particle masses.  Particle masses are set by the Standard Model
(Higgs mechanism, Yukawa couplings).  DGF provides the IR ceiling $m\_{\\max}
\\approx 17,\\mu\\mathrm{g}$.  The connection to the SM spectrum is a
future-work item.

**Gap 5 (Open, linear route failed): Local screening of $\\dot{G}/G$**

DGF may allow a cosmological drift of the effective coupling, but the linear
point-source solution does not screen it: fixed sources give
$\\partial\_tq(r,t)=\\dot q\_\\infty(t)$.  LLR measures
$|\\dot{G}/G|\_{\\mathrm{local}} < 7\\times10^{-14},\\mathrm{yr}^{-1}$, so any
cosmological drift requires a nonlinear or source-locked completion.  The
linear Green-function route is insufficient.

**Gap 6 (Open, uniqueness downgraded): Information-graph continuum limit**

DGF assumes the information adjacency graph has a smooth, isotropic, 3D
continuum limit.  It should not claim that the unique microscopic fixed point
is $\\mathbb{Z}^3$.  Coarse-graining generally selects a universality class,
not a unique graph representative: cubic, BCC/FCC-like, random geometric, or
triangulated graphs may share the same three-dimensional isotropic continuum
limit.  The defensible target is therefore a 3D isotropic continuum
universality class.

\---

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
Q\_q = e^{iπ(1-q)}dτ² + dx²  \[effective complex quadratic representation]
    ↓
One time direction  \[Theorem: ∮dq = 0, 95% confidence]
    ↓
d=3 spatial dimensions  \[Spectral argument, 60% confidence]
    ↓
m(A) = (2m₀/π)sin(πA/2),  m₀ = ℏ/cℓ  \[Euler residual]
    ↓
ℓ²∇²q = ρ/ρ₀ − ln((1−q)/q)  \[entropy variational principle]
    ↓
G = (πq∞/8)(c³ℓ²/ℏ)  \[effective calibration; fixes q∞ℓ²]
    ↓
K\_{ab}(t) = exp\[−(2τ₀ℓ⁴/ℏ⁶)(Δ⟨p⁴/3m⟩)²t]  \[GUP-Lindblad kernel]
    ↓
Conditional tests and open completions
```

\---

## XIV. Conclusion

DGF v3.1-prd provides an auditable effective language for organizing
decoherence, complex quadratic representations, and acceleration-scale
interfaces.  It does not establish a new fundamental theory of spacetime,
mass, or gravity.  The current version establishes two information-theoretic
results and then introduces effective representation maps whose
first-principles derivation remains incomplete.  The founding principle is
retained: no equation presupposing Lorentzian spacetime may be used as a
starting point.

Two results are established as theorems: the projection angle $\\theta =
\\pi(1-q)$ and the uniqueness of the time direction.  The gravitational
inverse-square structure, the Euler mass map, and the complex line element are
conditional effective structures.  Their value depends on future
system-level discriminants that are not polluted by normalization freedom in
$q\_\\infty$ or by a posterior choice of the acceleration interface.  The
$d=3$ graph-RG proof, the metric representation derivation, the
information-graph-to-acceleration bridge, and local screening of any
cosmological $\\dot{G}/G$ drift remain open.

The theory explicitly does not claim to predict $c$ numerically, $G$
numerically, $q\_\\infty$ absolutely without an independent $\\mathfrak{l}$, or
the Standard Model mass spectrum.

> \*The working hypothesis is not that classicality is fundamental.\*
> \*It is that classical observables track archived information.\*

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
