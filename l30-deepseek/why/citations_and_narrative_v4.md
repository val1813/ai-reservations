# Revised Sections for `why_universe_v3.md`

**Instructions:** The sections below replace the corresponding sections in `why_universe_v3.md`. Sections II--VII (mathematical derivations) remain unchanged. Section IX (Open Problems) remains unchanged. The References section below should replace the current References block. The Supplemental Material (`why_universe_v3_SM.md`) does not require changes from this revision; the SM comparison table (S12) already references the relevant frameworks.

---

## I. Introduction [Replaces current Section I]

### The Standard Picture and Its Gap

The emergence of classical behavior from quantum mechanics is one of the deepest open problems in physics. The dominant framework---environment-induced decoherence (Zurek 2003; Schlosshauer 2007)---explains why macroscopic superpositions are never observed: interaction with environmental degrees of freedom destroys phase coherence, leaving pointer states that behave classically.

This framework is powerful and experimentally supported. But it has a structural gap: it explains *how* decoherence happens given an environment, not *why* an environment is needed, or *why* the universe contains both quantum and classical systems in the first place. The framework takes the existence of the quantum/classical divide as given and explains the mechanism of crossing it. It does not explain why the divide exists.

Recent work has pushed toward intrinsic mechanisms. Aguiar and Matsas (2025) propose gravitational self-decoherence: particles with masses approaching the Planck mass $M_P$ experience coherence leakage to spacetime quantum degrees of freedom, without requiring a conventional environment. Other work shows that decoherence without entanglement is possible through dynamical mixing, but finds that system-environment entanglement is still needed for the emergence of objective classical reality.

We take a fundamentally different approach. We ask not *how* decoherence is generated, but *what classical behavior fundamentally is*. Our answer: **classical behavior is the state of a system whose information capacity is exhausted**. Not approximately exhausted---exactly exhausted at $q = 0$. A system with zero remaining capacity cannot respond to new information, cannot maintain phase relationships, cannot participate in interference. It is, operationally and necessarily, classical. No environment, no gravitational coupling, no measurement apparatus is required to make it so.

### The Inversion: Why the Causal Arrow Is Reversed

There is a hidden assumption buried in the standard decoherence program: that quantum mechanics is the fundamental theory and classical behavior is the phenomenon that must be explained. In this standard picture, quantum systems are special, fragile, and in need of protection; decoherence is the process that destroys their special properties; and classical behavior is the default that remains after decoherence has done its work. The causal arrow points from quantum to classical: quantum is the starting point, classical is the destination.

This paper argues that the causal arrow is reversed.

**The DGF picture.** Quantum behavior---characterized by full capacity to encode, process, and respond to information---is the *original, default state* of any physical system. A system born into a universe governed by information-capacity constraints starts with all cells empty ($q = 1$): maximum capacity, full responsiveness, complete freedom to participate in superposition and interference. There is nothing special about being quantum. Being quantum is the initial condition.

Classical behavior is not what quantum systems become. Classical behavior is what quantum systems *lose*.

As information accumulates irreversibly---through spontaneous distinguishability events (Axiom 1) that cannot be undone (Axiom 3) and eventually fill the finite capacity (Axiom 2)---the accessible coherence fraction $q$ decreases monotonically. When $q$ reaches zero at a given location, that region is operationally classical. Not because it has been "decohered" by an external environment acting upon it. Because it has exhausted its capacity to participate in any further information processing. The classical world is not the product of decoherence; the classical world is the depleted residue of an originally quantum universe.

This reframing has a visceral consequence. You, the reader, are made of cells whose information capacity is largely or entirely exhausted. Your classicality---the fact that you occupy a definite location, that your state does not exhibit macroscopic superposition, that you cannot participate in quantum interference with distant objects---is not a feature you acquired through interaction with an environment. It is a capacity you lost over cosmological time. The quantum world is the original. You are what remains after capacity ran out.

Sienicki (2025) has made a related observation: classical mechanics is a lossy, computationally compressed encoding of quantum reality, with classical descriptions requiring $O(N)$ bits while quantum descriptions require $O(2^N)$. In DGF, this compression is not a mathematical convenience or an epistemic shortcut---it is a physical necessity forced by bounded capacity. The compression ratio is precisely $q$, and irreversible compression to $q = 0$ is forced by the axioms over cosmological time.

This inversion is not merely philosophical. It has a specific, falsifiable mathematical consequence that distinguishes DGF from every existing decoherence framework: **classical behavior requires no environment.** It requires only that a system's information capacity approach zero---a condition forced by the axioms themselves, operating over sufficient time, without any external coupling. The standard question---"why do quantum systems decohere?"---is replaced by a different question: "why do some systems still retain enough capacity to remain quantum?" The answer is not mysterious: because they are small enough or young enough that spontaneous occupation has not yet saturated their cells. Retaining quantum behavior is a matter of size and time, not of isolation from an environment.

### What This Paper Does

We establish this picture rigorously from three axioms about information (Section II). We derive the unique evolution equation for the accessible coherence fraction $q$ (Sections III--V). We show that two dynamically distinct timescales are forced by the axioms, not assumed (Section VI). We discuss the emergence of classical behavior, mass, and cyclic cosmology (Section VII). We compare with existing frameworks---including Zurek's einselection, Aguiar--Matsas gravitational self-decoherence, informational derivations of quantum theory, digital physics, and entropic gravity---and state open problems honestly (Sections VIII--IX).

### Honest Scope

This paper does **not** derive quantum mechanics. It does not produce a Hilbert space, a Schrodinger equation, or a Born rule. No wave functions, state vectors, or density matrices appear in the formalism. The axioms are not quantum mechanical, and the derivations do not employ quantum mechanical reasoning. The framework does not explain why the high-$q$ regime takes the specific mathematical form of quantum mechanics rather than some other theory of superposition and interference.

What this paper provides is an information-theoretic explanation for **why** classical and quantum regimes differ: they are different phases of a single information system, distinguished by their remaining capacity $q$. The framework explains the existence of the divide, the direction of information flow across it, and the timescale separation between microphysical and cosmological dynamics---all from three axioms about information alone, without invoking quantum mechanics, environmental coupling, or gravitational self-interaction.

The precise quantitative mapping between $q$ and standard quantum mechanical coherence measures (off-diagonal density matrix elements, quantum discord, entanglement measures) is an open problem. The framework is qualitatively consistent with the quantum-to-classical limit---high $q$ corresponds to full responsiveness and interference capability; $q \to 0$ corresponds to classical unresponsiveness---but the mapping is not established at the level of equations. This is discussed in Section IX (Open Problem O5).

---

## VIII. Relation to Existing Work [Replaces current Section VIII]

### Zurek's Einselection and Quantum Darwinism

Zurek's einselection framework explains classicality through environment-induced superselection: the environment monitors certain observables, destroying interference between pointer states, enforcing an effective ban on most of Hilbert space (Zurek 2003, 2022). Quantum Darwinism extends this picture: only states that produce redundant information imprints on the environment become objective---the states we perceive as classical are those that many observers can independently measure without disturbing each other.

Our framework agrees on the conclusion (classical behavior involves information loss) but differs in mechanism:

|  | Zurek einselection | DGF |
|---|---|---|
| Requires environment | Yes | No |
| Mechanism | Environmental monitoring | Capacity exhaustion |
| Pointer states | Selected by environment | Defined by $q = 0$ |
| Classical = | Einselected stable states | Zero-capacity states |

The two frameworks are complementary rather than competing. Zurek explains *which* states survive decoherence when an environment is present, and why those states exhibit objective, classical properties. DGF explains *why* decoherence must occur at all, with or without an environment: because bounded capacity under irreversible accumulation forces a system toward $q = 0$. In a universe without environments, DGF's mechanism would still produce classical behavior; Zurek's would not. In a universe with environments, the two mechanisms operate simultaneously, with einselection determining the *basis* of classicality and capacity exhaustion determining its *inevitability*.

### Aguiar--Matas Gravitational Self-Decoherence

Aguiar and Matsas (2025) propose gravitational self-decoherence: particles with masses approaching the Planck mass $M_P$ experience unavoidable coherence leakage to spacetime quantum degrees of freedom. Their mechanism produces classical behavior for macroscopic objects without requiring a conventional environment---gravity itself serves as the decohering agent.

Our framework shares the conclusion (classical behavior requires no conventional environment) but arrives at it through a fundamentally different mechanism. In DGF, classicality is not produced by coupling to gravity or spacetime degrees of freedom; it is produced by the exhaustion of internal information capacity. The mass scale for classicality emerges as $\rho_m \sim m_p/\mathfrak{l}^3$, which is consistent with the Planck-mass threshold identified by Aguiar and Matsas, but the causal chain is inverted: in DGF, mass is a consequence of locked information (Section VII); the coincidence of scales is a consequence of dimensional analysis, not of a shared mechanism.

The key difference: Aguiar and Matsas require spacetime quantum degrees of freedom as the decohering channel. DGF requires no external channel at all. A system with exhausted capacity is classical regardless of what it is or is not coupled to. The frameworks are not in contradiction---gravitational self-decoherence could operate as an additional channel in the high-$q$ regime---but DGF provides the more fundamental explanation for why classicality must occur: because capacity is bounded and information accumulates.

### Sienicki (2025): Classical Mechanics as Lossy Compression

Sienicki (2025) argues that classical mechanics is a lossy, computationally compressed encoding of quantum reality, requiring $O(N)$ bits to describe a classical system while the underlying quantum description requires $O(2^N)$. In Sienicki's picture, classical mechanics is an efficient but information-discarding approximation of quantum dynamics.

DGF makes this precise and physical. The compression ratio is $q$: the fraction of cells still capable of carrying information. When $q = 1$, the system requires the full $2^N$ description; when $q = 0$, the $O(N)$ classical description is exact, not approximate. Crucially, in DGF the compression from $O(2^N)$ to $O(N)$ is not an epistemic choice made by a modeller---it is a physical process forced by the axioms. The universe does the compression. Sienicki's insight that the classical description is compressed becomes, in DGF, a theorem about the endpoint of information accumulation.

### Informational Derivations of Quantum Theory

A significant research program seeks to derive quantum mechanics from informational or operational postulates, without presupposing Hilbert spaces or unitary evolution. DGF occupies a different level in the explanatory hierarchy from these programs, as the following comparisons make clear.

#### Chiribella, D'Ariano, and Perinotti (2011): Informational Derivation of Quantum Theory

Chiribella, D'Ariano, and Perinotti (CDP) achieved a landmark result: the derivation of finite-dimensional quantum mechanics from five informational postulates---causality, perfect distinguishability, ideal compression, local distinguishability, and pure conditioning (Chiribella et al. 2011). Their framework shows that the mathematical structure of quantum theory (Hilbert spaces, tensor products, unitary evolution, and the Born rule) follows necessarily from operational principles about how information can be processed. It is one of the most complete reconstructions of quantum formalism from informational axioms.

**How DGF differs.** CDP derive the formalism of quantum mechanics. DGF explains why a classical/quantum divide exists at all, without deriving or presupposing any quantum mechanical formalism. In CDP, the result is quantum theory; in DGF, the result is that two regimes (high-$q$ and low-$q$) must exist in any information system satisfying the three axioms, and that one of them is necessarily classical regardless of what dynamics operates in the high-$q$ regime. The frameworks are hierarchically complementary: if CDP's derivation is placed inside DGF, it would explain why the high-$q$ regime takes the specific mathematical form of finite-dimensional quantum mechanics. DGF provides the outer envelope---the explanation of why a high-$q$ regime exists to begin with, and what happens to any system within it as capacity is exhausted. CDP asks "what must information processing look like such that it yields quantum theory?" DGF asks "why must there be two distinct regimes of information processing at all?"

#### Caticha (2009): Entropic Dynamics

Caticha derives quantum mechanics from the principle of maximum entropy applied to infinitesimal steps of inference, combined with an information-geometric notion of distance between probability distributions (Caticha 2009). In entropic dynamics, the Schrodinger equation emerges as the equation governing the flow of probabilities under entropic updating, and the Born rule emerges from the design of the inference procedure. The framework is powerful because it derives unitary evolution and measurement probabilities without postulating either.

**How DGF differs.** Caticha derives quantum mechanics. DGF does not. The critical distinction is that Caticha's framework operates entirely within the quantum regime and explains its internal structure; DGF explains the boundary between quantum and classical regimes without needing the structure of either. In DGF, the distinction is not between "quantum dynamics" and "classical dynamics" as categories of physical law, but between high remaining capacity ($q \sim 1$) and exhausted capacity ($q \sim 0$). Caticha asks "why do probabilities flow according to the Schrodinger equation?" DGF asks "why is there a low-capacity regime in which probabilities do not flow at all?" The two questions are at different levels. Caticha's answer to his question would describe what happens inside the $q \sim 1$ regime; DGF's answer explains why the boundary of that regime is a physical necessity.

#### D'Ariano and Perinotti (2017): Quantum Cellular Automata and Field Theory

D'Ariano and Perinotti derive free quantum field theories---specifically the Weyl, Dirac, and Maxwell equations---from the axioms of quantum cellular automata: discrete, local, unitary evolution on a computational lattice, constrained by causality and homogeneity (D'Ariano & Perinotti 2017). Their framework reconstructs relativistic quantum fields as the continuum limit of discrete informational dynamics, achieving one of the most successful derivations of specific physical laws from discrete first principles.

**How DGF differs.** D'Ariano and Perinotti derive specific field equations *within* the quantum regime. DGF operates one level deeper: it derives the existence of two distinct regimes (quantum and classical) from axioms about information capacity, without specifying the dynamical equations within either regime. If D'Ariano and Perinotti were placed inside DGF, their framework would describe the dynamics of the high-$q$ regime; DGF explains why a high-$q$ regime and a low-$q$ regime must both exist, and why the transition between them is irreversible. The two programs are hierarchically related: DGF provides the regime architecture (why two phases, why irreversible flow between them, why timescale separation); D'Ariano--Perinotti provides the field-theoretic content of one of those phases. Neither framework derives the other, but they are logically compatible and complementary.

### Computational Approaches to Fundamental Physics

#### Lloyd (2006): Programming the Universe

Lloyd (2006) articulates the vision of the universe as a quantum computer: a physical system performing approximately $10^{120}$ quantum logical operations on approximately $10^{90}$ bits over the history of the universe. In Lloyd's picture, the universe computes its own evolution, the laws of physics are constraints on what can be computed, and the hierarchy of physical scales---fast quantum operations at the Planck scale, slow cosmological evolution at the Hubble scale---reflects the computational architecture of the system.

**How DGF relates.** Lloyd's computational hierarchy maps directly onto DGF's two-timescale structure. Process A (information homogenization, with characteristic timescale $\tau_A \sim L^2 q^2/(\mathfrak{l} \cdot c)$) corresponds to Lloyd's fast quantum computation at the Planck scale. Process B (spontaneous occupation, with characteristic timescale $\tau_B \sim N/P_{\text{global}} \cdot t_p$) corresponds to the slow cosmological accumulation. The timescale ratio $\tau_B/\tau_A \sim L/(\mathfrak{l} \cdot q^2) \sim 10^{60}$ is consistent with Lloyd's estimate of the ratio between the total operation count and the operation rate. DGF provides an axiomatic origin for Lloyd's computational hierarchy: the two processes are forced by independent axioms (Axiom 3 for Process A, Axiom 1 for Process B), and their timescale separation follows necessarily from the scaling $N \propto (L/\mathfrak{l})^3$. In Lloyd's framework, the hierarchy is an observation about the universe; in DGF, it is a theorem about any macroscopic system satisfying the three axioms.

Lloyd's estimate of $10^{90}$ bits and $10^{120}$ operations is also naturally interpreted within DGF: $10^{90}$ is the number of Planck-scale cells in the observable universe, and $10^{120}$ is the number of steps required for Process B to fill those cells. The numbers are not independent parameters; they are the same number ($N$) and its square ($N^{4/3}$ for a process that fills volume in diffusive time), reflecting a single underlying fact---the universe is a finite-capacity information system of approximately $10^{90}$ cells.

#### Wolfram (2002): A New Kind of Science

Wolfram's program (2002) explores the universe as a cellular automaton---a discrete computational system evolving by simple local rules. His central claim is that complex behavior, including the full complexity observed in physical law, can emerge from extremely simple computational rules, and that the correct approach to fundamental physics is to search the space of possible CA rules for those that reproduce observed phenomena. Wolfram's approach is fundamentally empirical within rule space: enumerate candidate rules, simulate their behavior, and identify those whose output matches physical reality.

**How DGF differs.** Wolfram enumerates possible rules and examines their behavior. DGF constrains rules from axioms. The difference is methodological at its core. Wolfram's approach is exploratory---"here is the space of all possible rules; let us see what each one does." DGF's approach is deductive---"here are three axioms that any information system must satisfy if it is to support distinguishable states, bounded capacity, and causal structure; let us see what rules they force." In DGF, the evolution equation for $q$ is not one candidate among many in a rule space to be enumerated. It is the unique consequence of the axioms (up to the modeling choice of osmotic pressure form, whose alternatives are catalogued in Section V). The physical content is not in the discrete computational structure---which DGF shares with Wolfram---but in the derivation of the specific rule from first principles.

A further difference: Wolfram's program does not address the quantum/classical divide as such. It seeks to produce all physical phenomena from CA rules, but does not explain why the universe distinguishes between quantum and classical regimes. DGF's central result---that the divide is a phase structure of information systems, forced by capacity exhaustion---goes beyond what Wolfram's program attempts to explain.

#### Fredkin, Toffoli, and Margolus: Digital Physics

The digital physics tradition (Fredkin 1990; Toffoli & Margolus 1990) posits that the universe is fundamentally a computational process---specifically, a reversible cellular automaton in which information is conserved at the micro level and physics emerges from computation. Fredkin's "digital mechanics" treats the universe as a giant CA whose microscopic reversibility gives rise to all observed physical laws. Toffoli and Margolus developed the mathematical theory of invertible (reversible) CA, demonstrating that reversible computation can be embedded in CA dynamics and that locality, reversibility, and conservation laws are mutually constraining in precise ways.

**How DGF differs.** Fredkin, Toffoli, and Margolus posit reversible CA as a paradigm for fundamental physics. DGF derives reversibility as a theorem. This is the crucial difference. In digital physics, microscopic reversibility is an input assumption---motivated by physical principles such as the conservation of information and the reversibility of fundamental laws, but ultimately posited rather than derived. In DGF, reversibility at the micro level follows from the axioms (Section III, SM S1): Axiom 1 requires state transitions to be injective (distinguishable states remain distinguishable), and Axiom 2 fixes the state space to be finite (each cell holds at most 1 bit, total states $2^N$). An injective map on a finite set is bijective. Microscopic reversibility is not an assumption; it is a consequence of the requirement that distinguishable states exist and capacity is bounded.

Furthermore, the digital physics program does not address the quantum/classical divide. Fredkin's digital mechanics aims to reproduce all physics from reversible computation, but it does not explain why the universe contains both quantum and classical regimes, nor why the transition between them is irreversible at the macro level. DGF's core result---that irreversible macroscopic dynamics (the flow from high-$q$ to low-$q$) emerges from reversible microscopic dynamics through coarse-graining---provides a bridge that digital physics lacks.

The relationship can be summarized: digital physics says "the universe is a reversible CA, therefore physics." DGF says "if distinguishable states exist (Axiom 1) and capacity is bounded (Axiom 2), the universe must be a reversible CA; and if overflow is irreversible (Axiom 3), the macro-level dynamics must exhibit a directed flow from quantum to classical." DGF derives the digital physics paradigm from simpler axioms and extends it to explain the regime structure that digital physics takes as given.

### Information, Gravity, and Mass

#### Verlinde (2011): Entropic Gravity

Verlinde (2011) derives Newton's law of gravitation and the Einstein equations from entropic principles: gravity is an entropic force arising from the statistical tendency of matter to maximize entropy, with spacetime geometry emerging from the information stored on holographic screens. In Verlinde's framework, mass is not a fundamental property but an emergent consequence of the information associated with material bodies relative to holographic surfaces.

**How DGF relates.** Verlinde and DGF share a fundamental premise: mass and gravity have information-theoretic origins rather than being fundamental constituents of reality. In Verlinde's framework, the gravitational force is proportional to the gradient of entropy, which is itself proportional to the information content of matter. In DGF, mass density is proportional to locked information density: $\rho_m \propto (1-q)/\mathfrak{l}^3$ (Section VII). Both frameworks identify mass as a manifestation of information.

The two approaches are complementary rather than equivalent. Verlinde derives the dynamical laws of gravity (the force equation, the field equations) from information, but takes mass as a given quantity that sources the information. DGF derives the origin of mass (as locked information) from axioms about capacity exhaustion, but does not derive the force law that locked mass obeys. A synthesis---in which DGF's $q$-field provides the information-density field that drives Verlinde's entropic force---is a natural direction for future work. At present, neither framework derives the other; they address different segments of the chain from information to gravity. Verlinde derives force from information; DGF derives mass from information. Connecting them would require a derivation, not yet achieved, of the gravitational force law from the $q$-field dynamics.

### Overview of Comparisons

| Framework | What is derived | Classicality mechanism | Requires environment? | Relation to DGF |
|---|---|---|---|---|
| Zurek einselection | Pointer states, superselection rules | Environmental monitoring | Yes | Complementary: DGF explains inevitability |
| Aguiar--Matsas (2025) | Gravitational decoherence rate | Spacetime quantum coupling | No (spacetime) | Same conclusion, different mechanism |
| Chiribella et al. (2011) | Finite-dimensional QM formalism | Not addressed | Not applicable | Hierarchical: CDP inside DGF's high-$q$ regime |
| Caticha (2009) | Schrodinger eq., Born rule | Not addressed | Not applicable | DGF explains regime boundary; Caticha explains regime interior |
| D'Ariano--Perinotti (2017) | Weyl, Dirac, Maxwell eqs. | Not addressed | Not applicable | DGF provides regime architecture; D'Ariano--Perinotti provides field content |
| Lloyd (2006) | Computational hierarchy | Not addressed | Not applicable | DGF derives Lloyd's hierarchy from axioms |
| Wolfram (2002) | CA rule candidates (enumerated) | Not addressed | Not applicable | DGF derives rule from axioms; Wolfram enumerates |
| Fredkin/Toffoli/Margolus | Reversible CA paradigm | Not addressed | Not applicable | DGF derives reversibility as theorem |
| Verlinde (2011) | Gravity from entropy | Not addressed | Not applicable | Complementary: DGF derives mass as information |
| Sienicki (2025) | Classical as lossy compression | Informational compression | Not addressed | DGF makes compression ratio physical ($q$) |
| DGF (this work) | $q$ evolution, timescales, regime structure | Capacity exhaustion | **No** | --- |

---

## X. Conclusions [Replaces current Section X]

We have shown that three minimal axioms about information---distinguishable states exist (Axiom 1), capacity is bounded (Axiom 2), and overflow is irreversible (Axiom 3)---force the following conclusions without additional physics:

1. **Classical behavior is capacity exhaustion.** No environment, no gravitational coupling, no ensemble of observers is required. A system with zero remaining information capacity ($q = 0$) is operationally classical by definition: it cannot respond to new information, cannot maintain phase relationships, cannot participate in interference. Classicality is not a process that happens to a system; it is a state a system arrives at when it runs out of capacity.

2. **The causal arrow is reversed.** The standard view---quantum $\to$ decoherence $\to$ classical---treats classical behavior as what quantum systems become. DGF demonstrates that this gets the arrow backwards. Quantum (high $q$) is the original, default, information-complete state. Classical (low/zero $q$) is the depleted residue. You, the classical observer, are not what quantum systems become after decoherence. You are what remains after information capacity was irreversibly exhausted. The question is not why systems decohere, but why some systems still retain enough capacity to remain quantum.

3. **Information flows from full cells to empty cells.** This is not imposed as an additional dynamical law. It follows from Shannon entropy increase alone (Section III). The flow direction is a thermodynamic necessity, not a postulate about forces or interactions. The arrow of information flow and the arrow of time share a common origin in Axiom 3.

4. **Two dynamically distinct processes coexist inevitably.** Process A (information homogenization, from Axiom 3) and Process B (spontaneous occupation, from Axiom 1) are independent consequences of independent axioms. Neither requires the other; both are unavoidable in any system satisfying all three axioms. Their timescale separation $\tau_B/\tau_A \sim L/\mathfrak{l} \sim 10^{60}$ follows from the scaling $N \propto (L/\mathfrak{l})^3$ and provides an axiomatic explanation for the observed hierarchy between quantum and cosmological dynamics.

5. **A cyclic cosmology follows from a natural boundary condition.** The axioms become incompatible at $q = 0$: Axiom 1 demands continued spontaneous occupation; Axiom 2 forbids exceeding 1 bit per cell. The natural resolution---Axiom 2 (a structural constraint on state space) takes precedence, forcing a reset to $q = 1$---yields a cyclic universe. This is a boundary-condition interpretation, not a dynamical theorem, and carries the caveat discussed in Section VII.

This framework is not a theory of everything. It does not derive quantum mechanics, general relativity, or the specific values of the constants of nature. What it provides is a unified information-theoretic origin for the structural features that any fundamental theory must possess: a directed flow of information, a distinction between high-capacity and low-capacity regimes, a separation between microscopic and cosmological timescales, and a cyclic global history. The remaining open problems---dimensionality, the gravitational correspondence, the osmotic pressure form, the spontaneous occupation rate, and the $q$-to-coherence mapping---define the program's current frontier.

The central insight is that the quantum/classical divide is not a mystery about quantum mechanics. It is a phase structure of information systems with bounded capacity under irreversible dynamics. Quantum mechanics, whatever its precise mathematical formulation may be, is what physics looks like in the high-$q$ regime. Classical mechanics is what physics looks like at $q = 0$. The transition between them is not a dynamical process requiring an environment or a measurement apparatus. It is the inevitable accumulation of information over time, slowly exhausting the capacity that once made the universe quantum.

---

## References [Replaces current References section]

- Aguiar, G.H.S. & Matsas, G.E.A. (2025). A simple gravitational self-decoherence model. *Phys. Rev. D* **112**, 046004.
- Bassani, P.M. & Magueijo, J. (2025). How to make a Universe. *Phys. Rev. D* **111**, 103529.
- Caticha, A. (2009). Entropic dynamics. *J. Phys. A* **42**, 345401.
- Chiribella, G., D'Ariano, G.M. & Perinotti, P. (2011). Informational derivation of quantum theory. *Phys. Rev. A* **84**, 012311.
- Cover, T.M. & Thomas, J.A. (2006). *Elements of Information Theory*, 2nd ed. Wiley.
- D'Ariano, G.M. & Perinotti, P. (2017). Quantum cellular automata and free quantum field theory. *Front. Phys.* **12**, 120301.
- Fredkin, E. (1990). Digital mechanics. *Physica D* **45**, 254--270.
- Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM J. Res. Dev.* **5**, 183.
- Lloyd, S. (2006). *Programming the Universe*. Knopf.
- Neukart, F., Marx, E. & Vinokur, V. (2024). The Quantum Memory Matrix. *Entropy* **26**, 1039.
- Penrose, R. (2010). *Cycles of Time*. Bodley Head.
- Schlosshauer, M. (2007). *Decoherence and the Quantum-to-Classical Transition*. Springer.
- Shannon, C.E. (1948). A mathematical theory of communication. *Bell Syst. Tech. J.* **27**, 379.
- Sienicki, K. (2025). Classical mechanics as an emergent compression of quantum information. arXiv:2503.07666.
- Smolin, L. (1992). Did the universe evolve? *Classical Quantum Gravity* **9**, 173.
- Toffoli, T. & Margolus, N. (1990). Invertible cellular automata: A review. *Physica D* **45**, 229--253.
- Verlinde, E. (2011). On the origin of gravity and the laws of Newton. *JHEP* **04**, 029.
- Wheeler, J.A. (1990). Information, physics, quantum: the search for links. In *Complexity, Entropy, and the Physics of Information*.
- Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.
- Zurek, W.H. (1989). Algorithmic randomness and physical entropy. *Phys. Rev. A* **40**, 4731.
- Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Rev. Mod. Phys.* **75**, 715.
- Zurek, W.H. (2022). Quantum theory of the classical. *Entropy* **24**, 1520.
