# What the Classical World Lost: Decoherence as Capacity Exhaustion

**Huang Zhongchang**
Independent Researcher, Nanjing, China
Draft v3.0 | 2026-06-05

---

## Abstract

The quantum-to-classical transition is standardly explained by decoherence through environmental entanglement. We propose a different account: the classical world is not what the quantum world becomes—it is what the quantum world *loses*. Starting from three minimal axioms about information (distinguishable states exist, capacity is bounded, overflow is irreversible), we show that classical behavior emerges necessarily from information capacity exhaustion, without invoking an environment, an observer, or any additional physics. The core result is an inversion of the standard picture: quantum systems are information-complete; classical systems are information-deficient. Decoherence, in this framework, is not a process that acts *on* quantum systems from outside—it is the inevitable consequence of bounded capacity under irreversible overflow. We derive a unique evolution equation governing the accessible coherence fraction $q$, identify two dynamically distinct timescales whose coexistence is forced by the axioms, and show that a cyclic cosmology follows without free parameters. The framework makes contact with Zurek's einselection and Aguiar–Matsas gravitational self-decoherence, while differing from both in mechanism: classicality requires no environment, only capacity.

---

## I. Introduction

### The Standard Picture and Its Gap

The emergence of classical behavior from quantum mechanics is one of the deepest open problems in physics. The dominant framework—environment-induced decoherence (Zurek 2003; Schlosshauer 2007)—explains why macroscopic superpositions are never observed: interaction with environmental degrees of freedom destroys phase coherence, leaving pointer states that behave classically.

This framework is powerful and experimentally supported. But it has a structural gap: it explains *how* decoherence happens given an environment, not *why* an environment is needed, or *why* the universe contains both quantum and classical systems in the first place.

Recent work has pushed toward intrinsic mechanisms. Aguiar and Matsas (2025) propose gravitational self-decoherence: particles with masses approaching the Planck mass $M_P$ experience coherence leakage to spacetime quantum degrees of freedom, without requiring a conventional environment. Other work shows that decoherence without entanglement is possible through dynamical mixing, but finds that system-environment entanglement is still needed for the emergence of objective classical reality.

We take a different approach. We ask not *how* decoherence is generated, but *what classical behavior fundamentally is*. Our answer: **classical behavior is the state of a system whose information capacity is exhausted**. Not approximately exhausted—exactly exhausted. A system with zero remaining capacity cannot respond to new information, cannot maintain phase relationships, cannot participate in interference. It is, operationally, classical.

This reframes the quantum-to-classical transition entirely. Sienicki (2025) has argued that classical mechanics is a lossy, computationally compressed encoding of quantum reality, with classical systems requiring $O(N)$ bits and quantum descriptions requiring $O(2^N)$. We make this precise: the compression is not a mathematical convenience—it is a physical necessity forced by bounded capacity.

### The Inversion

Standard picture: quantum systems are special; classical behavior is the default that quantum mechanics must explain.

Our picture: **quantum systems are information-complete; classical systems are information-deficient**. The question is not why quantum systems decohere, but why some systems retain enough capacity to remain quantum.

This inversion is not merely philosophical. It has a specific mathematical consequence: decoherence requires no environment in our framework. It requires only that a system's information capacity approach zero—a condition forced by the axioms themselves, without any external coupling.

### What This Paper Does

We establish this picture rigorously from three axioms (Section II). We derive the unique evolution equation for the accessible coherence fraction $q$ (Sections III–IV). We show that two dynamically distinct timescales are forced by the axioms, not assumed (Section V). We discuss the emergence of classical behavior, mass, and cyclic cosmology (Section VI). We compare with existing frameworks and state open problems honestly (Sections VII–VIII).

---

## II. Three Axioms

We work with the minimal structure needed to define an information system. No spacetime, no Hilbert space, no Hamiltonian is presupposed.

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

When $q_A < q_B$ (A more occupied than B): $q_A/(1-q_A) < q_B/(1-q_B)$, so $\Delta S > 0$ for $\delta > 0$. Information flows spontaneously from low-$q$ (high occupancy) to high-$q$ (low occupancy). No force required — thermodynamic necessity.

### Classical Behavior (Axiom 2, Operational Definition)

**A system is operationally classical if and only if it cannot respond to external information input.**

Response requires available capacity. When $q = 0$: no capacity, no response, state fixed. Classical.

This definition requires no reference to quantum mechanical phase, superposition, wave functions, or measurement. Classicality is capacity exhaustion.

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

This is the **exact discrete flux form**. It exactly conserves $\sum_i q_i$ (telescoping sum) and produces diffusive dynamics: information spreads from high-occupancy regions to low-occupancy regions.

For small gradients ($q_{i\pm1} \approx q_i$), the flux approximates to $J_{i \to i+1} \approx (q_{i+1} - q_i)/q_i^2$, yielding the **simplified form**:

$$\Delta q_i \approx +\frac{q_{i+1} - 2q_i + q_{i-1}}{q_i^2} \equiv +\frac{\Delta^2 q_i}{q_i^2}$$

**Important:** The simplified form is a small-gradient approximation. It does not exactly conserve $\sum_i q_i$ for non-uniform $q$, and its sign ($+$) is critical — a negative sign would describe anti-diffusion (information concentrating rather than spreading), contradicting the physical direction established by Axiom 3. All quantitative results in this paper use the exact flux form; the simplified form is presented for intuition only.

### Continuous Limit

When $q$ varies on scales $L \gg \mathfrak{l}$, the exact flux form yields:

$$\partial_t q = +(l_p \cdot c) \cdot \left[\frac{\partial_x^2 q}{q^2} - \frac{2(\partial_x q)^2}{q^3}\right]$$

where $l_p \cdot c = l_p^2/t_p$ has dimensions $[\text{length}^2/\text{time}]$. The first term is nonlinear diffusion; the second is a gradient-sharpening correction relevant for strong inhomogeneities. For weak gradients where $(\partial_x q)^2 \ll |\partial_x^2 q| \cdot q$, the second term is subdominant:

$$\partial_t q \approx +(l_p \cdot c) \cdot \frac{\partial_x^2 q}{q^2}$$

**Caution:** The diffusion coefficient $D(q) = l_p \cdot c / q^2$ diverges as $q \to 0$, signaling the breakdown of the continuous description. Near deadlock, the discrete flux form is the correct description; it bounds propagation to one cell per step (speed $\leq c$), consistent with Axiom 2.

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

## VI. Two Timescales: Coexistence Forced by the Axioms

### The Central Claim

The three axioms define two dynamically distinct processes. Their coexistence is not an additional assumption — it follows from the independence of the axiom from which each process originates.

### Process A — Information Homogenization

Axiom 3 establishes that information flows from high occupancy to low occupancy. With the binary cell structure (Axioms 1–2), this flow is necessarily diffusive: occupancy gradients drive fluxes that narrow those gradients. The exact flux form (Section V) conserves $\sum_i q_i$, redistributing $q$ without changing the global mean.

$$\text{Characteristic timescale: } \tau_A \sim \frac{L^2}{D(q)} = \frac{L^2 q^2}{l_p \cdot c}$$

where $L$ is the system size and $D(q) = l_p \cdot c / q^2$ is the diffusion coefficient.

**Origin:** Process A is a direct consequence of Axiom 3 (irreversible flow direction), operating on the state space defined by Axioms 1–2. It requires no assumption beyond the axioms.

### Process B — Spontaneous Occupation

Axiom 1 requires occupied and unoccupied states to be distinguishable. In the $q = 1$ vacuum, this implies spontaneous occupation has nonzero probability $P > 0$ per step (under the maximum-entropy prior consistent with Axiom 1; the qualitative result is robust to the choice of prior). Each event decreases the global mean $\bar{q}$ by $1/N$.

Axiom 3 ensures that occupation accumulates irreversibly: once a cell is occupied, the information cannot spontaneously disappear. Axiom 2 provides the upper bound ($N$ cells, each $\leq 1$ bit), guaranteeing that accumulation eventually saturates.

$$\text{Characteristic timescale: } \tau_B \sim \frac{N}{P} \cdot t_p$$

where $N$ is the total number of cells and $t_p$ is the Planck time.

**Origin:** Process B is a direct consequence of Axiom 1 (spontaneous distinguishability), constrained by Axiom 3 (irreversibility) and bounded by Axiom 2. It requires no assumption beyond the axioms.

### Why Both Coexist

Process A originates from Axiom 3. Process B originates from Axiom 1. These axioms are independent: removing either collapses the framework (Section II, Table 1). Therefore, in any system satisfying all three axioms, **both processes are simultaneously active.**

They are not "necessary for each other" in a logical sense — they are independent consequences of different axioms that happen to operate in the same system. Their coexistence is a property of the axiom set, not a design requirement.

### Timescale Separation

The characteristic timescales depend on different parameters:

$$\frac{\tau_B}{\tau_A} \sim \frac{N}{P} \cdot \frac{l_p \cdot c}{L^2 q^2}$$

For a macroscopic universe ($N \gg 1$, $L \gg l_p$) with $P \sim O(1)$ per step: $\tau_B \gg \tau_A$. The separation is not fine-tuned — it follows from the scaling $N \propto (L/l_p)^3$ in three dimensions:

$$\frac{\tau_B}{\tau_A} \sim \frac{N \cdot l_p^2}{P \cdot L^2 q^2} \sim \frac{(L/l_p)^3 \cdot l_p^2}{L^2 q^2} \sim \frac{L}{l_p \cdot q^2} \gg 1$$

For $L \sim 10^{26}$ m (Hubble radius) and $l_p \sim 10^{-35}$ m: $\tau_B/\tau_A \sim 10^{61}$, consistent with the observed hierarchy between Planck-scale and cosmological dynamics.

### Two Equations Are Required

Process A conserves $\sum_i q_i$ (exact flux form); Process B decreases $\sum_i q_i$ (source term). These cannot be embodied in a single autonomous equation. The full dynamics are:

$$\Delta q_i = -\sum_{j \in \mathcal{N}(i)} J_{i \to j} + S_i(t)$$

where the flux term (Process A) encodes Axiom-3-driven diffusion, and the source term $S_i(t)$ (Process B) encodes Axiom-1-driven spontaneous occupation with $S_i < 0$ on average. The two terms have independent dynamical origins and separated characteristic times.

### Physical Interpretation

This two-process structure explains a fundamental feature of our universe: the coexistence of fast local dynamics (quantum processes at the Planck scale) and slow global evolution (cosmological expansion and cooling). The timescale separation is not a mystery requiring explanation — it is a direct consequence of the axioms operating on a macroscopic system ($N \gg 1$, $L \gg l_p$).

---

## VII. Emergence

### Mass

Locked information ($A = 1-q$) cannot flow and cannot respond to input. Its only remaining function under the axioms: resist change of state. Resistance to change of state is inertial mass.

With cells independent (nearest-neighbor constraint forces this):

$$\rho_m = \frac{A \cdot \ln 2}{\mathfrak{l}^3}$$

The quantity $\ln 2 / \mathfrak{l}^3$ is the information capacity per unit volume — determined entirely by Axiom 2 and the calibration constant $\mathfrak{l}$. Converting to SI requires the experimental input $m_p = \sqrt{\hbar c/G}$; this is dimensional analysis, not a derivation of mass values.

### Big Bang

At $q = 1$, spontaneous occupation is guaranteed by Axiom 1 ($P_{\text{cell}} > 0$). The first occupation event creates a $q$-gradient, triggering Process A. The resulting diffusion wave propagates at maximum speed $c$.

**The Big Bang is the first spontaneous occupation event.** Its location is random (explaining large-scale homogeneity). Its occurrence is certain (Axiom 1). Its rate $P_{\text{cell}}$ is not determined by the axioms beyond $P_{\text{cell}} > 0$; the physical value is set by Planck-scale physics and constrained by cosmological observations (the universe is still far from $q = 0$, implying a small $P_{\text{cell}}$).

### Cyclic Cosmology

Process B drives global $\bar{q} \to 0$ over cosmological time. At $q = 0$: cells full, new spontaneous occupation events (Axiom 1, $P > 0$) cannot be accommodated without violating Axiom 2 (each cell $\leq 1$ bit). The axioms become incompatible at this boundary.

**Resolution (boundary condition):** Axiom 2 takes precedence — it is a structural constraint on the state space, not a dynamical rule that can be violated by a fluctuation. When $q = 0$ and Axiom 1 would force an overflow event, the system resets to $q = 1$. This reset is not a derived dynamical theorem; it is the only boundary condition consistent with maintaining Axiom 2 as an inviolable constraint.

**Status:** The cyclic closure ($q \to 0 \Rightarrow q \to 1$) rests on a boundary-condition interpretation of axiom incompatibility, not on the same level of rigor as the derivations in Sections III–VI. Whether the reset is complete or leaves residual imprints (observed as CMB fluctuations at $\sim 10^{-5}$) is an open problem.

$$\boxed{q = 1 \xrightarrow{\text{Process B (Axiom 1)}} \bar{q} < 1 \xrightarrow{\text{Process A (Axiom 3)}} \text{homogenize} \xrightarrow[\text{(repeat } \sim N \text{ times)}]{\text{Process B}} \bar{q} \to 0 \xrightarrow{\text{Axiom 2 boundary}} q \to 1}$$

---

## VIII. Relation to Existing Work

### Zurek's Einselection and Quantum Darwinism

Zurek's einselection framework explains classicality through environment-induced superselection: the environment monitors certain observables, destroying interference between pointer states, enforcing an effective ban on most of Hilbert space.

Our framework agrees on the conclusion (classical behavior involves information loss) but differs in mechanism:

| | Zurek einselection | DGF |
|---|---|---|
| Requires environment | Yes | No |
| Mechanism | Environmental monitoring | Capacity exhaustion |
| Pointer states | Selected by environment | Defined by $q = 0$ |
| Classical = | Einselected stable states | Zero-capacity states |

The two frameworks are complementary: Zurek explains *which* states survive decoherence; we explain *why* decoherence occurs at all without an environment.

### Aguiar–Matsas Gravitational Self-Decoherence

Aguiar and Matsas argue that the macroscopic world requires new physics, proposing gravitational self-decoherence where coherence leaks to spacetime quantum degrees of freedom for masses near the Planck mass.

Our framework shares the conclusion (classical behavior requires no conventional environment) but has a different origin: capacity exhaustion rather than gravitational coupling. Our mass scale for classicality ($\rho_m \sim m_p/l_p^3$) is consistent with their Planck-mass threshold, but the derivation is different.

### Sienicki (2025)

Sienicki argues classical mechanics is a lossy compressed encoding of quantum reality. We make this precise: the compression ratio is $q$, and compression to $q = 0$ is forced by the axioms.

### Cellular Automata

The framework has structural similarity to cellular automata (discrete cells, local update rules, binary states). The difference: we derive the update rule from axioms rather than positing it. The physical content is in the derivation, not the structure.

---

## IX. Open Problems

We state these explicitly. Their existence does not undermine Sections III–VII, which are self-contained.

**O1 — Why Three Spatial Dimensions**
The information adjacency graph has unspecified topology. Why the continuum limit is 3-dimensional is not addressed.

**O2 — The $\sim 10^{-5}$ Residual**
CMB power spectrum amplitude is an observational input, not derived. Theoretical origin open in all cyclic cosmologies.

**O3 — Gravity**
Whether the $q$-gradient field corresponds to spacetime curvature in the sense of general relativity requires connecting the information graph to Riemannian geometry. Not established here.

**O4 — The Osmotic Pressure Form**
The choice $\Pi \propto (1-q)/q$ is physically motivated but not uniquely derived from the axioms. The qualitative results (two timescales, cyclic cosmology) are robust to this choice; quantitative predictions depend on it.

---

## X. Conclusions

We have shown that three minimal axioms about information — existence, bounded capacity, irreversible overflow — force the following:

1. Classical behavior is capacity exhaustion (not environmental decoherence)
2. Information flows from high to low occupancy (Shannon entropy, no forces)
3. An evolution equation for $q$ with one modeling choice (osmotic pressure form)
4. Two dynamically distinct processes whose coexistence follows inevitably from the axioms
5. A cyclic cosmology with two phenomenological inputs (osmotic pressure form and spontaneous occupation rate)

The central claim is an inversion of the standard quantum-to-classical picture: **the classical world is not what the quantum world becomes — it is what the quantum world loses**. Quantum systems are information-complete; classical systems are information-deficient. Decoherence, in this framework, is not imposed from outside. It is the inevitable endpoint of bounded capacity under irreversible dynamics.

This differs from environment-induced decoherence (no environment needed), from gravitational self-decoherence (no gravity needed at the foundational level), and from natural selection models (no ensemble needed). The key structural features of the laws of physics — directed information flow, capacity-limited dynamics, and timescale separation — follow from three axioms and one modeling choice. The remaining open problems (dimensionality, gravitational correspondence, the osmotic pressure form, and the spontaneous occupation rate) define the program's current frontier.

---

## References

- Aguiar, G.H.S. & Matsas, G.E.A. (2025). A simple gravitational self-decoherence model. *Phys. Rev. D* **112**, 046004.
- Bassani, P.M. & Magueijo, J. (2025). How to make a Universe. *Phys. Rev. D* **111**, 103529.
- Cover, T.M. & Thomas, J.A. (2006). *Elements of Information Theory*, 2nd ed. Wiley.
- Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM J. Res. Dev.* **5**, 183.
- Neukart, F., Marx, E. & Vinokur, V. (2024). The Quantum Memory Matrix. *Entropy* **26**, 1039.
- Penrose, R. (2010). *Cycles of Time*. Bodley Head.
- Schlosshauer, M. (2007). *Decoherence and the Quantum-to-Classical Transition*. Springer.
- Shannon, C.E. (1948). A mathematical theory of communication. *Bell Syst. Tech. J.* **27**, 379.
- Sienicki, K. (2025). Classical mechanics as an emergent compression of quantum information. arXiv:2503.07666.
- Smolin, L. (1992). Did the universe evolve? *Classical Quantum Gravity* **9**, 173.
- Wheeler, J.A. (1990). Information, physics, quantum: the search for links. In *Complexity, Entropy, and the Physics of Information*.
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

The osmotic pressure form (Section V) introduces one functional choice not forced by the axioms. This is the framework's genuine free element at the current stage of development.

**Complete assumption inventory:**

| Label | Content | Status |
|-------|---------|--------|
| A1 | Distinguishable states exist | Axiom |
| A2 | Each cell ≤ 1 bit | Axiom |
| A3 | Overflow irreversible | Axiom |
| M1 | Osmotic pressure form $\Pi \propto (1-q)/q$ | Modeling choice |
| P1 | $P_{\text{cell}} = \varepsilon \ll 1$ | Phenomenological param. |
| C1–C3 | $c$, $\hbar$, $G$ | Experimental inputs |
| O1–O5 | Three dimensions, $10^{-5}$, gravity, pressure form, $P_{\text{cell}}$ value | Open problems |

**The framework's genuine free elements** at this stage: (i) the osmotic pressure functional form M1, and (ii) the spontaneous occupation rate P1. Both are constrained but not determined by the axioms. All other aspects of the dynamics are forced by the axioms, are natural unit choices, or are experimental inputs.
