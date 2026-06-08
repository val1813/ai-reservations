# What the Classical World Lost: Decoherence as Capacity Exhaustion

**Huang Zhongchang**
Independent Researcher, Nanjing, China
Draft v4.0 | 2026-06-05

---

## Abstract

The quantum-to-classical transition is standardly explained by decoherence through environmental entanglement. We propose a fundamentally different account: the classical world is not what the quantum world becomes—it is what the quantum world *loses*. Starting from three axioms about information (distinguishable states exist, capacity is bounded, overflow is irreversible), together with one modeling choice and one phenomenological parameter, we construct an evolution equation for the accessible coherence fraction $q$ whose dimensionless structure contains no additional free parameters. The framework inverts the standard causal narrative: the high-capacity ($q \sim 1$) regime is the initial condition of any information system; the zero-capacity ($q = 0$) regime is the depleted endpoint of irreversible accumulation. Two dynamically distinct processes (homogenization from Axiom 3, spontaneous occupation from Axiom 1) coexist in any system satisfying the axioms. A cyclic cosmology follows from a boundary-condition interpretation of axiom incompatibility at $q = 0$. The framework yields a distinctive, $\varepsilon$-independent prediction: for objects of equal mass, denser objects should decohere *slower* ($\tau \propto \rho$)—opposite in sign to Penrose and Diósi—conditional on the modeling assumptions stated in Section VII. The framework does not derive quantum mechanics, and does not claim to. Its contribution is to explain why the classical/quantum divide exists as a phase structure of any bounded, irreversible information system.

---

## I. Introduction

### The Standard Picture and Its Gap

The emergence of classical behavior from quantum mechanics is one of the deepest open problems in physics. The dominant framework—environment-induced decoherence (Zurek 2003; Schlosshauer 2007)—explains why macroscopic superpositions are never observed: interaction with environmental degrees of freedom destroys phase coherence, leaving pointer states that behave classically.

This framework is powerful and experimentally supported. But it has a structural gap: it explains *how* decoherence happens given an environment, not *why* an environment is needed, or *why* the universe contains both quantum and classical systems in the first place. The framework takes the existence of the quantum/classical divide as given and explains the mechanism of crossing it. It does not explain why the divide exists.

Recent work has pushed toward intrinsic mechanisms. Aguiar and Matsas (2025) propose gravitational self-decoherence: particles with masses approaching the Planck mass $M_P$ experience coherence leakage to spacetime quantum degrees of freedom, without requiring a conventional environment. Other work shows that decoherence without entanglement is possible through dynamical mixing, but finds that system-environment entanglement is still needed for the emergence of objective classical reality.

We take a fundamentally different approach. We ask not *how* decoherence is generated, but *what classical behavior fundamentally is*. Our answer: **classical behavior is the state of a system whose information capacity is exhausted**. Not approximately exhausted—exactly exhausted at $q = 0$. A system with zero remaining capacity cannot respond to new information, cannot maintain phase relationships, cannot participate in interference. It is, operationally and necessarily, classical. No environment, no gravitational coupling, no measurement apparatus is required to make it so.

### The Inversion: Why the Causal Arrow Is Reversed

There is a hidden assumption buried in the standard decoherence program: that quantum mechanics is the fundamental theory and classical behavior is the phenomenon that must be explained. In this standard picture, quantum systems are special, fragile, and in need of protection; decoherence is the process that destroys their special properties; and classical behavior is the default that remains after decoherence has done its work. The causal arrow points from quantum to classical: quantum is the starting point, classical is the destination.

This paper argues that the causal arrow is reversed.

**The DGF picture.** Quantum behavior—characterized by full capacity to encode, process, and respond to information—is the *original, default state* of any physical system. A system born into a universe governed by information-capacity constraints starts with all cells empty ($q = 1$): maximum capacity, full responsiveness, complete freedom to participate in superposition and interference. There is nothing special about being quantum. Being quantum is the initial condition.

Classical behavior is not what quantum systems become. Classical behavior is what quantum systems *lose*.

As information accumulates irreversibly—through spontaneous distinguishability events (Axiom 1) that cannot be undone (Axiom 3) and eventually fill the finite capacity (Axiom 2)—the accessible coherence fraction $q$ decreases monotonically. When $q$ reaches zero at a given location, that region is operationally classical. Not because it has been "decohered" by an external environment acting upon it. Because it has exhausted its capacity to participate in any further information processing. The classical world is not the product of decoherence; the classical world is the depleted residue of an originally quantum universe.

This reframing has a visceral consequence. You, the reader, are made of cells whose information capacity is largely or entirely exhausted. Your classicality—the fact that you occupy a definite location, that your state does not exhibit macroscopic superposition, that you cannot participate in quantum interference with distant objects—is not a feature you acquired through interaction with an environment. It is a capacity you lost over cosmological time. The quantum world is the original. You are what remains after capacity ran out.

Sienicki (2025) has made a related observation: classical mechanics is a lossy, computationally compressed encoding of quantum reality, with classical descriptions requiring $O(N)$ bits while quantum descriptions require $O(2^N)$. In DGF, this compression is not a mathematical convenience or an epistemic shortcut—it is a physical necessity forced by bounded capacity. The compression ratio is precisely $q$, and irreversible compression to $q = 0$ is forced by the axioms over cosmological time.

This inversion is not merely philosophical. It has a specific consequence that distinguishes DGF from every existing decoherence framework: **classical behavior requires no environment.** It requires only that a system's information capacity approach zero—a condition that follows from the axioms together with the spontaneous-transition postulate ($\varepsilon > 0$), operating over sufficient time, without any external coupling. The standard question—"why do quantum systems decohere?"—is replaced by a different question: "why do some systems still retain enough capacity to remain quantum?" The answer is a matter of size and time: small or young systems have not yet accumulated enough spontaneous occupation events to saturate their cells.

### What This Paper Does

We establish this picture rigorously from three axioms about information (Section II), together with one modeling choice (osmotic pressure form, M1) and one additional postulate (spontaneous transitions, $\varepsilon > 0$). We construct an evolution equation for the accessible coherence fraction $q$ whose dimensionless structure contains no free parameters beyond M1 (Sections III–V). We show that two dynamically distinct processes — information homogenization (from Axiom 3) and spontaneous occupation (from the spontaneous-transition postulate motivated by Axiom 1) — coexist in any system satisfying the axioms with $\varepsilon > 0$ (Section VI). We discuss the emergence of classical behavior, mass, and cyclic cosmology (Section VII). We derive a falsifiable, parameter-free quantitative prediction and compare with existing frameworks (Sections VIII–IX). We state open problems honestly (Section X).

### Honest Scope

This paper does **not** derive quantum mechanics. It does not produce a Hilbert space, a Schrödinger equation, or a Born rule. No wave functions, state vectors, or density matrices appear in the formalism. The axioms are not quantum mechanical, and the derivations do not employ quantum mechanical reasoning. The framework does not explain why the high-$q$ regime takes the specific mathematical form of quantum mechanics rather than some other theory of superposition and interference.

What this paper provides is an information-theoretic explanation for **why** classical and quantum regimes differ: they are different phases of a single information system, distinguished by their remaining capacity $q$. The framework explains the existence of the divide, the direction of information flow across it, and the timescale separation between microphysical and cosmological dynamics—all from three axioms about information alone, without invoking quantum mechanics, environmental coupling, or gravitational self-interaction.

The precise quantitative mapping between $q$ and standard quantum mechanical coherence measures (off-diagonal density matrix elements, quantum discord, entanglement measures) is an open problem. The framework is qualitatively consistent with the quantum-to-classical limit—high $q$ corresponds to full responsiveness and interference capability; $q \to 0$ corresponds to classical unresponsiveness—but the mapping is not established at the level of equations. This is discussed in Section X (Open Problem O5).

---

## II. Three Axioms

We work with the minimal structure needed to define an information system. No Hilbert space, no Hamiltonian is presupposed. A single dimensional scale $\mathfrak{l}$—the physical size of the minimum cell—is introduced as an experimental calibration constant. The information adjacency graph has an unspecified topology; that it embeds in 3-dimensional Euclidean space with cell volume $\mathfrak{l}^3$ is a working assumption (see Open Problem O1). All results that depend on spatial dimensionality carry this caveat.

### Axiom 1 — Information Exists

There exist distinguishable states. The minimum resolvable distinction is 1 bit: the information content of two states that can be told apart.

*Why minimal:* Without distinguishable states, no physical description is possible. This axiom is the logical prerequisite for any theory.

### Axiom 2 — Capacity Is Bounded

Each minimum information unit (a cell) carries at most 1 bit. A single dimensional input $\mathfrak{l}$—the physical size of the minimum cell—is introduced as an experimental calibration constant, not derived.

*Why minimal:* Without bounded capacity, there is no resolution limit. Unbounded capacity makes distinguishability vacuous—any state could be encoded anywhere. Axiom 2 gives Axiom 1 operational content.

### Axiom 3 — Overflow Is Irreversible

When a cell reaches capacity, excess information transfers to lower-occupancy cells and cannot spontaneously return. This is the information-theoretic arrow of time.

*Why minimal:* Without irreversibility, information flow has no direction. A reversible system has no time arrow, no causal structure. Axiom 3 is the minimum condition for causality.

### The Accessible Coherence Fraction

Partition a system $S$ into cells. Define:

$$\boxed{q_S = \frac{\text{unoccupied cells}}{\text{total cells}} \in [0,1]}$$

$q = 1$: all cells empty — maximum capacity, fully quantum.
$q = 0$: all cells full — zero capacity, fully classical.
$A = 1-q$: locked fraction.

This definition requires no quantum mechanical formalism. It is a ratio of cell counts.

---

## III. What the Axioms Immediately Imply

### Information Conservation (Axioms 1 + 2)

State transitions must be injective (Axiom 1: distinguishable inputs map to distinguishable outputs). On a finite set of fixed size (Axiom 2), injective maps are bijective. Therefore total information is conserved exactly.

*Note:* This is microstate conservation. Macroscopic entropy can still increase via coarse-graining—the standard statistical mechanics resolution of the reversibility paradox. We return to this in Section IV.

### Flow Direction (Axiom 3 + Shannon Entropy)

Transfer $\delta$ bits from system $A$ (occupancy $1-q_A$) to system $B$ (occupancy $1-q_B$). Shannon entropy change (derived in SM S3):

$$\Delta S = \left[\ln\frac{q_B}{1-q_B} - \ln\frac{q_A}{1-q_A}\right]\delta$$

When $q_A < q_B$ (A more occupied than B): $\Delta S > 0$ for $\delta > 0$. Information flows spontaneously from low-$q$ (high occupancy) to high-$q$ (low occupancy). No force required — thermodynamic necessity.

### Classical Behavior (Axiom 2, Operational Definition)

**A system is operationally classical if and only if it cannot respond to external information input.**

Response requires available capacity. When $q = 0$: no capacity, no response, state fixed. Classical.

This definition requires no reference to quantum mechanical phase, superposition, wave functions, or measurement. Classicality is capacity exhaustion. The framework explains *why* a system loses its ability to participate in quantum phenomena; it does not claim to derive the full structure of classical mechanics (phase space, Poisson brackets, deterministic trajectories). The latter is classical mechanics; the former is the quantum-to-classical transition. They are different explanatory targets.

*Consistency:* At $q \to 0$, system is unresponsive — consistent with classical limit. At $q \to 1$, system is fully responsive — consistent with quantum limit. Intermediate regime: partial responsiveness. Precise correspondence with standard quantum coherence measures is an open problem.

---

## IV. The Coarse-Graining Resolution

Before deriving the evolution equation, we address the apparent tension between information conservation (Section III) and entropy increase.

The tension is real and well-known: microscopic dynamics are reversible; macroscopic entropy increases. The resolution is coarse-graining, standard since Boltzmann.

In our framework:

**Micro level** (cell states $\mathbf{s} \in \{0,1\}^N$): dynamics are bijective, information conserved exactly. Physical entropy $S_{phys} = H(\mathbf{s}) + K(\mathbf{s})$ is conserved (Zurek 1989), where $H$ is Shannon entropy and $K$ is algorithmic complexity.

**Macro level** ($q$-field): $q = (\text{unoccupied cells})/N$ is a coarse-graining of the microstate. The transition matrix on $q$-space is doubly stochastic (because micro dynamics are bijective). By Cover's theorem, macro Shannon entropy $H(q)$ is non-decreasing.

**Result:** Micro information conservation and macro entropy increase are compatible. The $q$-field obeys an irreversible macroscopic equation derived from reversible microscopic dynamics, exactly as in standard statistical mechanics.

---

## V. The Evolution Equation

### Derivation

Axiom 3 establishes a preferred direction: information flows from high occupancy (low $q$) to low occupancy (high $q$). The thermodynamic force driving this flow is the gradient of the chemical potential of locked information. We model the osmotic pressure at cell $i$ as:

$$\Pi_i = \frac{1-q_i}{q_i}$$

This form is physically motivated (ratio of locked to available capacity) with correct boundary behavior ($\Pi \to \infty$ as $q \to 0$, $\Pi \to 0$ as $q \to 1$). It is a modeling choice — not uniquely forced by the axioms — and is discussed further below.

The flux from cell $i$ to neighbor $j$ is driven by the pressure difference:

$$J_{i \to j} = \kappa \cdot (\Pi_i - \Pi_j) = \kappa \cdot \frac{q_j - q_i}{q_i q_j}$$

where $\kappa$ is the transfer rate. We work in natural units where the basic time step $\tau$ equals one cell state-flip interval. In these units, one cell boundary transmits at most 1 bit per $\tau$ (Axiom 2 bounds each cell to 1 bit), giving $\kappa = 1$. This is a unit calibration — analogous to $c = 1$ in relativity — not a free parameter.

The discrete continuity equation (exact form) — derived from information conservation $\partial_t(1-q) + \nabla \cdot \mathbf{J} = 0$, where $\mathbf{J}$ is the flux of information (occupancy) — is:

$$\boxed{\Delta q_i = +\sum_{j \in \mathcal{N}(i)} J_{i \to j}}$$

where $\mathcal{N}(i)$ denotes the neighbor set of cell $i$. (When information leaves cell $i$, the cell becomes unoccupied, so $q_i$ increases — hence the $+$ sign.) In one dimension with nearest neighbors:

$$\Delta q_i = +(J_{i \to i+1} - J_{i-1 \to i}) = \frac{q_{i+1} - q_i}{q_i q_{i+1}} - \frac{q_i - q_{i-1}}{q_{i-1} q_i}$$

This is the **exact discrete flux form**. It exactly conserves $\sum_i q_i$ (telescoping sum) and produces diffusive dynamics: information spreads from high-occupancy regions to low-occupancy regions. The equation is well-posed for all $q \in (0,1]$ with adaptive timestepping (stability condition: $\Delta t \leq q_{\min}^2/2$); near $q = 0$, the discrete form is the correct description, and propagation is bounded by one cell per step ($\leq c$).

For small gradients ($q_{i\pm1} \approx q_i$), the flux approximates to $J_{i \to i+1} \approx (q_{i+1} - q_i)/q_i^2$, yielding the **simplified form**:

$$\Delta q_i \approx +\frac{q_{i+1} - 2q_i + q_{i-1}}{q_i^2} \equiv +\frac{\Delta^2 q_i}{q_i^2}$$

**Important:** The simplified form is a small-gradient approximation. It does not exactly conserve $\sum_i q_i$ for non-uniform $q$, and its sign ($+$) is critical — a negative sign would describe anti-diffusion (information concentrating rather than spreading), contradicting the physical direction established by Axiom 3. All quantitative results in this paper use the exact flux form; the simplified form is presented for intuition only.

### Continuous Limit

When $q$ varies on scales $L \gg \mathfrak{l}$, the exact flux form yields:

$$\partial_t q = +(\mathfrak{l} \cdot c) \cdot \left[\frac{\partial_x^2 q}{q^2} - \frac{2(\partial_x q)^2}{q^3}\right]$$

where $\mathfrak{l} \cdot c = \mathfrak{l}^2/t_p$ has dimensions $[\text{length}^2/\text{time}]$. The first term is nonlinear diffusion; the second is a gradient-sharpening correction relevant for strong inhomogeneities. For weak gradients where $(\partial_x q)^2 \ll |\partial_x^2 q| \cdot q$, the second term is subdominant:

$$\partial_t q \approx +(\mathfrak{l} \cdot c) \cdot \frac{\partial_x^2 q}{q^2}$$

**Caution:** The diffusion coefficient $D(q) = \mathfrak{l} \cdot c / q^2$ diverges as $q \to 0$, signaling the breakdown of the continuous description. Near deadlock, the discrete flux form is the correct description. The continuous equation is valid for $q \gg \mathfrak{l}/L$ where $L$ is the characteristic gradient scale.

### The Osmotic Pressure: Modeling Choice

The pressure ansatz $\Pi = (1-q)/q$ is a physically motivated choice, not a theorem. Table 1 catalogs alternatives consistent with the three axioms:

| Form | $\Pi(q)$ | Diffusion coefficient $D(q)$ | $q \to 0$ behavior |
|------|----------|------------------------------|---------------------|
| Osmotic (adopted) | $(1-q)/q$ | $1/q^2$ | Accelerates |
| Entropic | $-\ln q$ | $1/q$ | Accelerates (weaker) |
| Linear | $1-q$ | $1$ | Uniform |
| Micro-derived | $q(1-q)$ | $q(1-q)$ | Decelerates |

All forms share the same flow direction (from low-$q$ to high-$q$, forced by Axiom 3) and the same qualitative structure: diffusion homogenizes $q$ while spontaneous occupation slowly decreases the global mean. The osmotic form is adopted for its simplicity, its correct boundary behavior, and its distinctive prediction of accelerated classicalization as capacity is exhausted. Quantitative predictions that depend on the specific form of $\Pi(q)$ carry this caveat.

### Boundary Behavior

- $q \to 1$ (quantum limit): $D(q) \sim 1$, linear diffusion, slow homogenization ✓
- $q \to 0$ (classical limit): $D(q) \sim 1/q^2$, diffusion accelerates in the continuous approximation; discrete equation bounds propagation to $\leq c$ ✓
- $\nabla q = 0$ (equilibrium): $\Delta q = 0$, evolution stops ✓

---

## VI. Two Timescales: Coexistence from the Axioms

### The Central Claim

The three axioms define two dynamically distinct processes. Their coexistence is not an additional assumption — it follows from the independence of the axiom from which each process originates.

### Process A — Information Homogenization

Axiom 3 establishes that information flows from high occupancy to low occupancy. With the binary cell structure (Axioms 1–2), this flow is necessarily diffusive: occupancy gradients drive fluxes that narrow those gradients. The exact flux form (Section V) conserves $\sum_i q_i$, redistributing $q$ without changing the global mean.

$$\text{Characteristic timescale: } \tau_A \sim \frac{L^2 q^2}{\mathfrak{l} \cdot c}$$

where $L$ is the system size and $D(q) = \mathfrak{l} \cdot c / q^2$ is the diffusion coefficient.

**Origin:** Process A is a direct consequence of Axiom 3 (irreversible flow direction), operating on the state space defined by Axioms 1–2. It requires no assumption beyond the axioms.

**Physical interpretation:** The homogenization timescale scales as $\tau_A \propto L^2/\mathfrak{l}$. With the physical Planck-scale cell size ($\mathfrak{l} \sim 10^{-35}$ m), $\tau_A \sim 10^{26}$ s ($\sim 10^{18}$ years) for $L = 1$ m and $q = 0.5$ — Process A is negligible at laboratory and solar-system scales. Only at the Planck scale itself ($L \sim \mathfrak{l}$) does $\tau_A \sim t_p$, and only at cosmological scales where $L$ is enormous does the cumulative effect become relevant. For cosmological $L \sim 10^{26}$ m, $\tau_A \sim 10^{70}$ years — far exceeding the age of the universe. The universe is not homogenized on cosmological scales, consistent with the persistence of large-scale structure (galaxy clusters, CMB anisotropies). Process A operates efficiently only at microscopic scales; its macroscopic and cosmological effects are negligible at current $q$.

### Process B — Spontaneous Occupation

Axiom 1 requires occupied and unoccupied states to be distinguishable. We make the additional assumption that this distinguishability entails a nonzero probability $P_{\text{cell}} = \varepsilon > 0$ of spontaneous transition from unoccupied to occupied, per cell per step. (The logical step from "states are distinguishable" to "states spontaneously transition" is not a deduction from Axiom 1 alone—it is a modeling assumption about the dynamics. Axiom 1 guarantees that the two states are distinct elements of the state space; the further claim that the system explores this state space spontaneously is an independent postulate, discussed further in SM S10.) Each event decreases the global mean $\bar{q}$ by $1/N$.

Axiom 3 ensures that occupation accumulates irreversibly: once a cell is occupied, the information cannot spontaneously disappear. Axiom 2 provides the upper bound ($N$ cells, each $\leq 1$ bit), guaranteeing that accumulation eventually saturates.

$$\text{Characteristic timescale: } \tau_B \sim \frac{1}{\varepsilon} \cdot t_p$$

where $t_p = \mathfrak{l}/c$ is the cell crossing time. The value of $\varepsilon$ is a phenomenological parameter not determined by the axioms; it is constrained by the observed age and quantum coherence of the universe.

**Origin:** Process B requires the spontaneous-transition postulate ($\varepsilon > 0$), which is motivated by Axiom 1 (distinguishable states exist) but is not a logical deduction from it (see discussion above). Once $\varepsilon > 0$ is granted, Axiom 3 (irreversibility) ensures accumulation, and Axiom 2 provides the upper bound. Process B is thus a consequence of the axioms plus one additional postulate.

### Why Both Coexist

Process A originates from Axiom 3. Process B originates from Axiom 1. These axioms are independent: removing either collapses the framework (Section II, Table 1). Therefore, in any system satisfying all three axioms, **both processes are simultaneously active.**

They are not "necessary for each other" in a logical sense — they are independent consequences of different axioms that happen to operate in the same system. Their coexistence is a property of the axiom set, not a design requirement.

### Timescale Separation

The characteristic timescales have different parametric dependencies:

$$\tau_A \sim \frac{L^2 q^2}{\mathfrak{l} \cdot c}, \qquad \tau_B \sim \frac{1}{\varepsilon} \cdot t_p = \frac{\mathfrak{l}}{c\varepsilon}$$

Their ratio is:

$$\frac{\tau_B}{\tau_A} = \frac{\mathfrak{l}^2}{\varepsilon L^2 q^2}$$

Timescale separation ($\tau_B \gg \tau_A$) is not an automatic consequence of the axioms — it requires $\varepsilon \ll \mathfrak{l}^2/L^2$. For cosmological $L \sim 10^{26}$ m and $\mathfrak{l} \sim 10^{-35}$ m, this means $\varepsilon \ll 10^{-122}$. Whether nature satisfies this condition is an empirical question; the framework does not predict $\varepsilon$. If $\varepsilon \sim 1/N \sim 10^{-183}$ (one spontaneous event per universe per Planck time), then $\tau_B/\tau_A \sim N \cdot \mathfrak{l}^2/(L^2 q^2) = L/(\mathfrak{l} \cdot q^2) \sim 10^{61}/q^2$, consistent with the observed hierarchy between Planck-scale and cosmological dynamics. Other values of $\varepsilon$ produce different degrees of separation, including none at all. The existence of timescale separation in our universe is thus a phenomenological constraint on $\varepsilon$, not a derived theorem.

### Two Equations Are Required

Process A conserves $\sum_i q_i$ (exact flux form); Process B decreases $\sum_i q_i$ (source term). These cannot be embodied in a single autonomous equation. The full dynamics are:

$$\Delta q_i = +\sum_{j \in \mathcal{N}(i)} J_{i \to j} + S_i(t)$$

where the flux term (Process A) encodes Axiom-3-driven diffusion, and the source term $S_i(t)$ (Process B) encodes Axiom-1-driven spontaneous occupation with $\langle S_i \rangle = -\varepsilon q_i$ per step. The exact functional form of $S_i(t)$ (Poisson, deterministic, or state-dependent) affects quantitative predictions and is an open area for investigation; the qualitative two-process structure is robust.

### Physical Interpretation

This two-process structure explains a fundamental feature of our universe: the coexistence of fast local dynamics and slow global evolution. The timescale separation is not a mystery requiring explanation — it follows from the cubic-versus-quadratic scaling of a macroscopic system under the axioms.

---

## VII. Emergence and Predictions

### Mass

Locked information ($A = 1-q$) cannot flow and cannot respond to input. Its only remaining function under the axioms: resist change of state. Resistance to change of state is inertial mass.

With cells independent (nearest-neighbor constraint forces this):

$$\rho_m = \frac{A \cdot \ln 2}{\mathfrak{l}^3}$$

The quantity $\ln 2 / \mathfrak{l}^3$ is the information capacity per unit volume — determined entirely by Axiom 2 and the calibration constant $\mathfrak{l}$. Converting to SI requires the experimental input $m_p = \sqrt{\hbar c/G}$; this is dimensional analysis, not a derivation of mass values. The claim is that mass density is operationally equivalent to locked information density, with a proportionality constant calibrated by experiment.

### Big Bang

At $q = 1$, spontaneous occupation is guaranteed by Axiom 1 ($P_{\text{cell}} = \varepsilon > 0$). The first occupation event creates a $q$-gradient, triggering Process A. The resulting diffusion wave propagates at maximum speed $c$.

**The Big Bang is the first spontaneous occupation event.** Its location is random (explaining large-scale homogeneity). Its occurrence is certain (Axiom 1). Its rate $\varepsilon$ is not determined by the axioms beyond $\varepsilon > 0$; the physical value is set by Planck-scale physics and constrained by cosmological observations (the universe is still far from $q = 0$, implying small $\varepsilon$).

### Cyclic Cosmology

Process B drives global $\bar{q} \to 0$ over cosmological time. At $q = 0$: cells full, new spontaneous occupation events (Axiom 1, $\varepsilon > 0$) cannot be accommodated without violating Axiom 2 (each cell $\leq 1$ bit). The axioms become incompatible at this boundary.

**Resolution (boundary condition):** Axiom 2 takes precedence — it is a structural constraint on the state space, not a dynamical rule that can be violated by a fluctuation. When $q = 0$ and Axiom 1 would force an overflow event, the system resets to $q = 1$. This reset is not a derived dynamical theorem; it is the only boundary condition consistent with maintaining Axiom 2 as an inviolable constraint.

**Status:** The cyclic closure ($q \to 0 \Rightarrow q \to 1$) rests on a boundary-condition interpretation of axiom incompatibility. Whether the reset is complete or leaves residual imprints (observed as CMB fluctuations at $\sim 10^{-5}$) is an open problem.

$$\boxed{q = 1 \xrightarrow{\text{Process B (Axiom 1)}} \bar{q} < 1 \xrightarrow{\text{Process A (Axiom 3)}} \text{homogenize} \xrightarrow[\text{(repeat } \sim \varepsilon^{-1} \text{ times)}]{\text{Process B}} \bar{q} \to 0 \xrightarrow{\text{Axiom 2 boundary}} q \to 1}$$

### Quantitative Prediction: Density-Dependent Decoherence

The framework makes a distinctive prediction that distinguishes it from all competing decoherence models. The prediction is $\varepsilon$-independent (the unknown spontaneous occupation rate cancels in ratios) but depends on the osmotic pressure modeling choice (M1) and on the identification of $\Delta N$ with geometric volume (discussed below).

For a compact object of mass $M$ and density $\rho$, the number of Planck cells is $N = M/(\rho \mathfrak{l}^3)$. If a superposition involves the entire object (center-of-mass delocalization), the number of cells whose state differs between branches is $\Delta N \sim N$. We assume that a single spontaneous occupation event hitting any of these $\Delta N$ cells suffices to collapse the superposition—a premise motivated by the framework's identification of occupation with classicalization (Section III), but not independently derived. Under this premise, the decoherence rate is the first-event rate among $\Delta N$ independent cells, each with event probability $\varepsilon$ per $t_p$:

$$\tau_{\text{decoherence}}^{\text{DGF}}(M,\rho) = \frac{t_p}{\varepsilon \Delta N} = \frac{\rho \mathfrak{l}^4}{c \varepsilon M}$$

The parameter $\varepsilon$ is unknown, but it **cancels in ratios**. For two objects of equal mass and different densities:

$$\boxed{\frac{\tau_{\text{DGF}}(\rho_1)}{\tau_{\text{DGF}}(\rho_2)} = \frac{\rho_1}{\rho_2}}$$

**Denser objects decohere slower.** This is the opposite sign to Penrose (1996) and Diósi (1989), which predict $\tau \propto 1/\rho^{1/3}$ (denser objects decohere faster). The comparison:

| Model | $\tau(M,\rho)$ scaling | Density dependence |
|-------|----------------------|---------------------|
| **DGF (this work)** | $\propto \rho/M$ | $\propto \rho$ (denser → slower) |
| Penrose (1996) | $\propto 1/(\rho^{1/3} M^{5/3})$ | $\propto 1/\rho^{1/3}$ (denser → faster) |
| Diósi (1989) | $\propto 1/(\rho^{1/3} M^2)$ | $\propto 1/\rho^{1/3}$ (denser → faster) |
| Environmental | Independent of $\rho$ | — |

For silica ($\rho \approx 2.2$ g/cm³) vs. gold ($\rho \approx 19.3$ g/cm³) nanoparticles of equal mass:
- **DGF:** Gold decoheres $\sim 9\times$ **slower** than silica
- **Penrose/Diósi:** Gold decoheres $\sim 2\times$ **faster** than silica

**The predicted ratio is opposite in sign.** This is a qualitative, model-independent discriminator between DGF and gravitational decoherence models. It is falsifiable by matter-wave interferometry comparing nanoparticles of equal mass but different densities under equivalent environmental isolation.

**Caveats:** This prediction assumes that $\Delta N$ — the number of Planck cells whose state differs between superposition branches — scales with the geometric volume $V_S/\mathfrak{l}^3$. If $\Delta N$ instead scales with mass (i.e., only mass-energy-carrying cells participate), the density dependence disappears. The correct identification of $\Delta N$ is an open problem within the framework.

---

## VIII. Relation to Existing Work

### Zurek's Einselection and Quantum Darwinism

Zurek's einselection framework explains classicality through environment-induced superselection: the environment monitors certain observables, destroying interference between pointer states (Zurek 2003, 2022). Quantum Darwinism extends this: only states that produce redundant information imprints on the environment become objective.

Our framework agrees on the conclusion (classical behavior involves information loss) but differs in mechanism:

| | Zurek einselection | DGF |
|---|---|---|
| Requires environment | Yes | No |
| Mechanism | Environmental monitoring | Capacity exhaustion |
| Pointer states | Selected by environment | Defined by $q = 0$ |
| Classical = | Einselected stable states | Zero-capacity states |

The two frameworks are complementary rather than competing. Zurek explains *which* states survive decoherence when an environment is present. DGF explains *why* decoherence must occur at all, with or without an environment. In a universe without environments, DGF's mechanism would still produce classical behavior; Zurek's would not. In a universe with environments, the two operate simultaneously.

### Aguiar–Matsas Gravitational Self-Decoherence

Aguiar and Matsas (2025) propose gravitational self-decoherence: particles near the Planck mass experience coherence leakage to spacetime quantum degrees of freedom. Our framework shares the conclusion (no conventional environment needed) but via a fundamentally different mechanism: capacity exhaustion rather than gravitational coupling. The mass scale for classicality ($\rho_m \sim m_p/\mathfrak{l}^3$) is consistent with their Planck-mass threshold, but the causal chain is inverted.

### Sienicki (2025): Classical Mechanics as Lossy Compression

Sienicki argues classical mechanics is a lossy compressed encoding of quantum reality. DGF makes this precise: the compression ratio is $q$, and compression to $q = 0$ is forced by the axioms. Crucially, the compression is not an epistemic choice — it is a physical process. The universe does the compression.

### Informational Derivations of Quantum Theory

**Chiribella, D'Ariano, and Perinotti (2011)** derive finite-dimensional quantum mechanics from five informational postulates. Their result is the formalism of QM. DGF explains why a classical/quantum divide exists at all, without deriving or presupposing any quantum mechanical formalism. The frameworks are hierarchically complementary: if CDP's derivation is placed inside DGF, it would explain why the high-$q$ regime takes the form of finite-dimensional QM. CDP asks "what must information processing look like to yield quantum theory?" DGF asks "why must there be two distinct regimes of information processing at all?"

**Caticha (2009)** derives the Schrödinger equation and Born rule from maximum entropy and information geometry. Caticha derives QM; DGF explains the boundary between quantum and classical regimes without needing QM's internal structure. Caticha asks "why do probabilities flow according to the Schrödinger equation?" DGF asks "why is there a low-capacity regime in which probabilities do not flow at all?"

**D'Ariano and Perinotti (2017)** derive Weyl, Dirac, and Maxwell equations from quantum cellular automata. They derive specific field equations within the quantum regime. DGF derives the regime architecture (why two phases, why irreversible flow, why timescale separation). The programs are hierarchically related: DGF provides the outer envelope; D'Ariano–Perinotti provides the field-theoretic content of the high-$q$ phase.

### Computational Approaches

**Lloyd (2006)** articulates the universe as a quantum computer: $\sim 10^{120}$ operations on $\sim 10^{90}$ bits, with a natural hierarchy between fast quantum ops and slow cosmological evolution. DGF provides an axiomatic origin for this hierarchy: Process A maps to Lloyd's fast quantum computation; Process B maps to slow cosmological accumulation. The timescale ratio $\tau_B/\tau_A \sim 10^{61}$ is consistent with Lloyd's estimate. In Lloyd's framework, the hierarchy is an observation; in DGF, it is a theorem.

**Wolfram (2002)** and **Fredkin/Toffoli/Margolus** treat the universe as a cellular automaton. DGF shares the CA structure but differs methodologically: Wolfram enumerates rules; DGF derives them from axioms. Fredkin posits reversible CA; DGF derives reversibility as a theorem (injective map on finite set → bijective).

### Verlinde (2011): Entropic Gravity

Verlinde derives gravity from entropy and information. DGF shares the premise (mass/inertia has an information-theoretic origin) but addresses a different link in the chain: Verlinde derives force from information; DGF derives mass as locked information. A synthesis is a natural direction for future work.

### Overview of Comparisons

| Framework | What is derived | Classicality mechanism | Requires environment? | Relation to DGF |
|---|---|---|---|---|
| Zurek einselection | Pointer states, superselection | Environmental monitoring | Yes | Complementary |
| Aguiar–Matsas (2025) | Grav. decoherence rate | Spacetime quantum coupling | No (spacetime) | Same conclusion, different mechanism |
| Chiribella et al. (2011) | Finite-dim. QM formalism | Not addressed | N/A | Hierarchical: CDP inside DGF's high-$q$ |
| Caticha (2009) | Schrödinger eq., Born rule | Not addressed | N/A | DGF explains regime boundary |
| D'Ariano–Perinotti (2017) | Weyl, Dirac, Maxwell eqs. | Not addressed | N/A | DGF provides regime architecture |
| Lloyd (2006) | Computational hierarchy | Not addressed | N/A | DGF derives hierarchy from axioms |
| Wolfram (2002) | CA rule enumeration | Not addressed | N/A | DGF derives; Wolfram enumerates |
| Fredkin/Toffoli/Margolus | Reversible CA paradigm | Not addressed | N/A | DGF derives reversibility as theorem |
| Verlinde (2011) | Gravity from entropy | Not addressed | N/A | Complementary: mass as locked info |
| Sienicki (2025) | Classical as compression | Informational | N/A | DGF makes compression physical ($q$) |
| **DGF (this work)** | **$q$ evolution, timescales, regime structure** | **Capacity exhaustion** | **No** | — |

---

## IX. Numerical Analysis

The exact flux form (Section V) has been implemented on 1D lattices ($N = 50$–$200$ cells) with adaptive timestepping (stability condition: $\Delta t \leq q_{\min}^2/2$). Because simulating $10^{180}$ Planck-scale cells is computationally infeasible, the simulations use a rescaled cell size ($\mathfrak{l}_{\text{sim}} \sim 10^{-2}$ m for a 100-cell meter-scale lattice) to verify the mathematical behavior of the equation. The qualitative dynamics (diffusion, conservation, stability) are independent of the absolute scale; quantitative timescales scale as $\tau \propto L^2/\mathfrak{l}$ and must be extrapolated to the physical Planck scale. Key findings (full results and diagnostic plots in SM S14):

1. **Conservation:** $\sum_i q_i$ is preserved to $\sim 10^{-14}$–$10^{-16}$ across all tested initial conditions, confirming the telescoping-sum property analytically proven in Section V.

2. **Diffusion:** Information spreads from high-occupancy to low-occupancy regions in all tests. Local $q$-minima increase monotonically; local maxima decrease. No shock formation or anti-diffusive instability is observed.

3. **Stability:** The blowup obtained with naive timestepping ($q$ leaving $[0,1]$ in one step) is a numerical artifact. With adaptive $\Delta t$, all trajectories remain in $q \in [\varepsilon, 1-\varepsilon]$ indefinitely. The exact flux form is well-posed.

4. **Timescale extrapolation:** The measured homogenization time scales as $\tau \propto L^2/\mathfrak{l}$, consistent with the analytic form $\tau_A \sim L^2 q^2/(\mathfrak{l} \cdot c)$. Extrapolating to the physical Planck scale ($\mathfrak{l} \sim 10^{-35}$ m) yields $\tau_A \sim 10^{70}$ years for cosmological $L \sim 10^{26}$ m — the universe is not homogenized on cosmological scales, consistent with the observed large-scale structure (galaxy clusters, CMB anisotropies). For meter-scale systems, $\tau_A \sim 10^{26}$ s — far longer than any laboratory timescale, meaning Process A is negligible for terrestrial objects.

---

## X. Open Problems

We state these explicitly. Their existence does not undermine Sections III–IX, which are self-contained.

**O1 — Why Three Spatial Dimensions.** The information adjacency graph has unspecified topology. Why the continuum limit is 3-dimensional is not addressed.

**O2 — The $\sim 10^{-5}$ Residual.** CMB power spectrum amplitude is an observational input, not derived. Theoretical origin open in all cyclic cosmologies.

**O3 — Gravity.** Whether the $q$-gradient field corresponds to spacetime curvature in the sense of general relativity requires connecting the information graph to Riemannian geometry. Not established here.

**O4 — The Osmotic Pressure Form.** The choice $\Pi \propto (1-q)/q$ is physically motivated but not uniquely derived. Qualitative results are robust; quantitative predictions carry this caveat.

**O5 — $q$-to-Quantum-Coherence Mapping.** The precise quantitative relationship between $q$ and standard quantum coherence measures (density matrix elements, discord, entanglement) is not established. Qualitatively consistent; quantitatively open.

**O6 — The Spontaneous Occupation Rate $\varepsilon$.** The value of $\varepsilon$ is a phenomenological parameter spanning potentially 60+ orders of magnitude. Its physical origin, and the resolution of the "$\Delta N$ problem" (whether $\Delta N$ scales with volume or mass), are open.

---

## XI. Conclusions

We have shown that three minimal axioms about information—distinguishable states exist (Axiom 1), capacity is bounded (Axiom 2), and overflow is irreversible (Axiom 3)—together with one modeling choice (osmotic pressure form) and one phenomenological parameter (spontaneous occupation rate), yield the following conclusions:

1. **Classical behavior is capacity exhaustion.** No environment, no gravitational coupling, no ensemble of observers is required. A system with zero remaining information capacity ($q = 0$) is operationally classical by definition.

2. **The causal arrow is reversed.** The standard view—quantum $\to$ decoherence $\to$ classical—treats classical behavior as what quantum systems become. DGF demonstrates that this gets the arrow backwards. Quantum (high $q$) is the original, default, information-complete state. Classical (low/zero $q$) is the depleted residue. You, the classical observer, are not what quantum systems become after decoherence. You are what remains after information capacity was irreversibly exhausted.

3. **Information flows from full cells to empty cells.** This is not an additional dynamical law. It follows from Shannon entropy increase alone (Section III). The arrow of information flow and the arrow of time share a common origin in Axiom 3.

4. **Two dynamically distinct processes coexist** in any system satisfying the axioms with $\varepsilon > 0$. Process A (information homogenization) follows from Axiom 3. Process B (spontaneous occupation) follows from the spontaneous-transition postulate motivated by Axiom 1. The degree of timescale separation depends on the phenomenological parameter $\varepsilon$; for $\varepsilon \sim 1/N$, the ratio $\tau_B/\tau_A \sim 10^{61}$ is consistent with observation.

5. **A falsifiable, parameter-free prediction distinguishes DGF from all competing models:** for objects of equal mass, $\tau_{\text{decoherence}} \propto \rho$ — denser objects decohere slower. This is opposite in sign to Penrose and Diósi.

6. **A cyclic cosmology follows from a natural boundary condition** at $q = 0$, where axiom incompatibility forces a reset.

This framework is not a theory of everything. It does not derive quantum mechanics, general relativity, or the specific values of the constants of nature. What it provides is a unified information-theoretic origin for the structural features that any fundamental theory must possess: a directed flow of information, a distinction between high-capacity and low-capacity regimes, a separation between microscopic and cosmological timescales, and a cyclic global history.

The central insight is that the quantum/classical divide is not a mystery about quantum mechanics. It is a phase structure of information systems with bounded capacity under irreversible dynamics. The classical world is not what the quantum world becomes. It is what the quantum world lost.

---

## References

- Aguiar, G.H.S. & Matsas, G.E.A. (2025). A simple gravitational self-decoherence model. *Phys. Rev. D* **112**, 046004.
- Bassani, P.M. & Magueijo, J. (2025). How to make a Universe. *Phys. Rev. D* **111**, 103529.
- Caticha, A. (2009). Entropic dynamics. *J. Phys. A* **42**, 345401.
- Chiribella, G., D'Ariano, G.M. & Perinotti, P. (2011). Informational derivation of quantum theory. *Phys. Rev. A* **84**, 012311.
- Cover, T.M. & Thomas, J.A. (2006). *Elements of Information Theory*, 2nd ed. Wiley.
- D'Ariano, G.M. & Perinotti, P. (2017). Quantum cellular automata and free quantum field theory. *Front. Phys.* **12**, 120301.
- Diósi, L. (1989). Models for universal reduction of macroscopic quantum fluctuations. *Phys. Rev. A* **40**, 1165.
- Fredkin, E. (1990). Digital mechanics. *Physica D* **45**, 254–270.
- Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM J. Res. Dev.* **5**, 183.
- Lloyd, S. (2006). *Programming the Universe*. Knopf.
- Neukart, F., Marx, E. & Vinokur, V. (2024). The Quantum Memory Matrix. *Entropy* **26**, 1039.
- Penrose, R. (1996). On gravity's role in quantum state reduction. *Gen. Rel. Grav.* **28**, 581.
- Penrose, R. (2010). *Cycles of Time*. Bodley Head.
- Schlosshauer, M. (2007). *Decoherence and the Quantum-to-Classical Transition*. Springer.
- Shannon, C.E. (1948). A mathematical theory of communication. *Bell Syst. Tech. J.* **27**, 379.
- Sienicki, K. (2025). Classical mechanics as an emergent compression of quantum information. arXiv:2503.07666.
- Smolin, L. (1992). Did the universe evolve? *Classical Quantum Gravity* **9**, 173.
- Toffoli, T. & Margolus, N. (1990). Invertible cellular automata: A review. *Physica D* **45**, 229–253.
- Verlinde, E. (2011). On the origin of gravity and the laws of Newton. *JHEP* **04**, 029.
- Wheeler, J.A. (1990). Information, physics, quantum: the search for links. In *Complexity, Entropy, and the Physics of Information*.
- Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.
- Zurek, W.H. (1989). Algorithmic randomness and physical entropy. *Phys. Rev. A* **40**, 4731.
- Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Rev. Mod. Phys.* **75**, 715.
- Zurek, W.H. (2022). Quantum theory of the classical. *Entropy* **24**, 1520.

---

## Appendix: Calibration Constants and Honest Accounting

The framework is internally dimensionless. Three experimental constants translate results to SI:

| Constant | Role | Status |
|----------|------|--------|
| $c$ | Cell propagation speed | Experimental input |
| $\hbar$ | Quantum of action | Experimental input |
| $G$ | Gravitational calibration | Experimental input |

These are not free parameters in the theoretical sense — they do not appear in the logical structure of the axioms or the derivation of the evolution equation. They appear only when translating dimensionless ratios into SI units. The claim "no free parameters" refers to the dimensionless structure; the claim is not that $c$, $\hbar$, $G$ are derived.

**Complete assumption inventory:**

| Label | Content | Status |
|-------|---------|--------|
| A1 | Distinguishable states exist | Axiom |
| A2 | Each cell ≤ 1 bit | Axiom |
| A3 | Overflow irreversible | Axiom |
| M1 | Osmotic pressure form $\Pi \propto (1-q)/q$ | Modeling choice |
| M2 | Maximum-entropy prior ($P_{\text{cell}}^{\max} = 1/2$) | Upper bound only |
| P1 | $P_{\text{cell}} = \varepsilon \ll 1$ | Phenomenological param. |
| C1–C3 | $c$, $\hbar$, $G$ | Experimental inputs |
| O1–O6 | Dimensions, $10^{-5}$, gravity, pressure form, $q$-mapping, $\varepsilon$ value | Open problems |

**The framework's genuine free elements** at this stage: (i) the osmotic pressure functional form M1, and (ii) the spontaneous occupation rate P1. Both are constrained but not determined by the axioms. All other aspects of the dynamics are forced by the axioms, are natural unit choices, or are experimental inputs.

No assumption is hidden.
