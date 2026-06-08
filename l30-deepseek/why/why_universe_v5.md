# Why the Universe Had to Be This Way: Existence as the Only Attractor

**Huang Zhongchang**
Independent Researcher, Nanjing, China
Draft v5.0 | 2026-06-05

---

## Abstract

We propose that the two foundational axioms of information theory—distinguishable states exist (A1) and capacity is bounded (A2)—are not assumptions about our universe but necessary attractors of any system that undergoes non-trivial interaction. Starting from any initial condition—complex-valued states, unbounded capacity, or pure randomness—we prove that finite interaction steps necessarily produce a system satisfying A1 and A2. From these two axioms alone, without assuming a third axiom of irreversibility, we derive: information flow direction (Shannon entropy), irreversibility as an emergent property of capacity ratio, classicality as capacity exhaustion, quantum coherence as approximate reversibility in finite environments, time as the causal order of overflow events, and a cyclic cosmology. The framework's central claim is not that our universe was designed efficiently, but that any universe capable of existing must arrive here. Classical and quantum behavior are not two worlds—they are two limiting regimes of the same bounded information system. The classical world is not what the quantum world becomes. It is what the quantum world loses.

---

## I. Introduction

### The Standard Picture and Its Hidden Assumption

Every physical theory begins with axioms. The hidden assumption in most foundational frameworks is that these axioms are inputs—chosen by theorists, imposed on nature, or selected by some anthropic or selection principle.

This paper argues for a different view: **the axioms are outputs**.

Specifically, we show that the two minimal axioms required to define an information system—

- **A1:** Distinguishable states exist
- **A2:** Capacity is bounded

—are not assumptions we impose on the universe. They are the inevitable endpoint of any system that undergoes interaction. Every possible starting point—complex-valued states, infinite capacity, complete randomness—converges to a system satisfying A1 and A2. These axioms are attractors, not inputs.

This reframes the central question of foundational physics. The question is not "why does our universe satisfy these axioms?" The question is "why would any universe satisfy anything else?" The answer is: it couldn't. A1 and A2 are not properties of our universe. They are properties of existence itself.

### What Follows From the Attractor

Once A1 and A2 are established as attractors, the remainder of the framework follows:

From A1 + A2 alone:
- Information flow direction (Shannon entropy driving high-to-low occupancy)
- Irreversibility as emergent (not axiom)
- Two timescales (homogenization and accumulation)
- Classical behavior = capacity exhaustion
- Quantum coherence = finite-environment approximate reversibility
- Time = causal order of overflow events
- Mass = locked information density
- Cyclic cosmology from boundary condition

The classical world is not the product of decoherence acting on quantum systems. It is the depleted residue of an originally full-capacity universe. The quantum world is not special. It is the default. Classical behavior is what the quantum world loses.

### Honest Scope

This paper does not derive quantum mechanics. It does not produce Hilbert spaces, wave functions, or the Born rule. What it provides is a proof that any interacting system must arrive at the information-theoretic structure from which classical and quantum behavior emerge as limiting cases.

---

## II. The Attractor Theorem

### Setup

Consider any system with the following minimal properties:

1. It has internal states (something exists)
2. It allows non-trivial binary interaction between states (something happens)

We make no assumptions about the nature of states—they may be real, complex, infinite, or random.

**Theorem (Informal):** Any system with these two properties necessarily converges, in finite interaction steps, to a system satisfying A1 (distinguishable states) and A2 (bounded capacity).

We prove this for three exhaustive cases.

### Case 1: Complex-Valued States (No Real Structure)

**Setup:** States $s_i \in \mathbb{C}$, no distinguishability constraint.

**Claim:** Any non-trivial binary interaction produces real-valued output.

**Proof:**

Let interaction be a non-constant binary function $f: \mathbb{C} \times \mathbb{C} \to \mathbb{C}$.

The minimal non-trivial binary operation compatible with the field structure of $\mathbb{C}$ is multiplication.

For pure imaginary inputs $s_1 = b_1 i$, $s_2 = b_2 i$:

$$f(s_1, s_2) = s_1 \cdot s_2 = b_1 i \cdot b_2 i = -b_1 b_2 \in \mathbb{R}$$

The result is real. This is not specific to multiplication: any operation satisfying the distributive law produces real output from pure imaginary inputs, since $i \cdot i = -1 \in \mathbb{R}$ is a property of $\mathbb{C}$ itself.

**Normalization from A1:** For real output to be distinguishable (A1), total information must be bounded. The minimal constraint is $\sum_i |s_i|^2 = N$ (finite). This compresses state space to the unit circle $|s| = 1$.

On the unit circle, $s = e^{i\theta}$. The minimal distinguishable discrete states under A2 (bounded capacity = 1 bit = 2 states) are $\theta = 0$ ($s = 1$) and $\theta = \pi$ ($s = -1$): two real-valued states.

**Conclusion:** Complex-valued systems converge to real-valued, 2-state (1-bit) systems under interaction. $\square$

**Physical interpretation:** This is the information-theoretic origin of the Euclidean-to-Lorentzian transition. Pure imaginary (Euclidean) states interact, produce real parts, and the system acquires the causal structure of a real-valued information system. The Wick rotation $\tau = it$ is not a mathematical trick—it is the physical process of this convergence.

### Case 2: Unbounded Capacity

**Setup:** States $s_i \in \mathbb{R}$, capacity unbounded (no A2).

**Claim:** Any finite-rate dynamics only accesses a bounded subspace.

**Proof:**

Let the system evolve for $T$ steps with local interaction rate $\delta s$ per step.

After $T$ steps, the maximum state magnitude is bounded:
$$|s_i(T)| \leq |s_i(0)| + T \cdot \delta s$$

For any finite $T$ and finite $\delta s$, the accessible state space is bounded by $|s_i(0)| + T \cdot \delta s < \infty$.

More generally: with $N$ cells and nearest-neighbor interaction, the number of distinct states accessed in $T$ steps is at most $N \cdot k^T$ for some finite branching factor $k$.

For any finite $T$, this is finite—the effective capacity is bounded.

**Conclusion:** Unbounded capacity systems behave as bounded-capacity systems on any finite timescale. A2 is effectively satisfied by any physical process. $\square$

### Case 3: Random Initial Conditions (No Structure)

**Setup:** $s_i \sim \text{Uniform}[0,1]$, independent, no correlations.

**Claim:** Any non-trivial interaction produces correlated, distinguishable structure satisfying A1 and A2.

**Proof:**

**Step A (A1 emerges):** Before interaction: mutual information $I(s_i; s_j) = 0$ for all $i \neq j$.

After one non-trivial interaction between cells $i$ and $j$: their states become correlated. $I(s_i; s_j) > 0$.

Correlation means: knowing $s_i$ gives information about $s_j$. The two cells are now distinguishable from each other in a structured way. A1 emerges.

**Step B (A2 emerges):** Mutual information is bounded: $I(s_i; s_j) \leq \min(H(s_i), H(s_j))$.

For finite-precision states (any physically realizable system), $H(s_i) < \infty$. Therefore $I(s_i; s_j) < \infty$—the effective information capacity per cell is bounded. A2 emerges.

**Conclusion:** Random systems develop A1 and A2 through interaction. $\square$

### The Attractor Theorem (Formal Statement)

**Theorem:** Let $\mathcal{S}$ be any system with internal states and non-trivial binary interaction. Then:

1. After at most $O(N)$ interaction steps, $\mathcal{S}$ satisfies A1 (distinguishable states exist).
2. The capacity of any physically accessible subspace of $\mathcal{S}$ is bounded (A2 satisfied effectively).
3. These properties are stable: once A1 and A2 hold, they are preserved by further interaction (information conservation from A1 + A2 prevents their destruction).

**Corollary:** A1 and A2 are universal attractors of interacting systems. No initial condition can avoid them. Our universe satisfies A1 and A2 not because it was designed to, but because any universe with interaction must. $\square$

---

## III. From Two Axioms to Everything Else

With A1 and A2 established as attractors, we derive the structure of physics.

### The Coherence Fraction

Define:
$$q = \frac{\text{unoccupied cells}}{\text{total cells}} \in [0,1]$$

$q = 1$: maximum capacity, fully responsive — quantum regime.
$q = 0$: zero capacity, unresponsive — classical regime.
$A = 1 - q$: locked fraction.

### Information Flow Direction

Transfer $\delta$ bits from system $A$ (low $q_A$) to system $B$ (high $q_B$). Shannon entropy change:

$$\Delta S = \left[\ln\frac{q_B}{1-q_B} - \ln\frac{q_A}{1-q_A}\right]\delta > 0 \quad \text{when } q_A < q_B$$

Information flows spontaneously from high occupancy to low occupancy. No force required.

### Irreversibility Is Emergent, Not Axiomatic

The key insight: irreversibility is not a third axiom. It is a consequence of capacity ratio.

**When environment capacity $\gg$ system capacity:**

Information flows from system to environment and does not return—the environment has too much capacity to "fill up" and reflect information back. This is the Markovian limit: irreversible, classical behavior.

$$q_{env} \gg q_{sys} \implies \text{irreversible} \implies \text{classical}$$

**When environment capacity $\sim$ system capacity:**

Information flows out but the environment fills up, forcing information back. This is the non-Markovian regime: approximately reversible, quantum coherence preserved.

$$q_{env} \sim q_{sys} \implies \text{approximately reversible} \implies \text{quantum coherence}$$

**The standard "Axiom 3" (overflow is irreversible) is the Markovian limit of A1 + A2, not an independent axiom.**

This resolves the tension between quantum coherence (information backflow observed in non-Markovian systems) and classical irreversibility (information loss in macroscopic systems). They are the same physics at different capacity ratios.

### Classical Behavior

**Definition:** A system is operationally classical if $q = 0$—zero capacity, cannot respond to input.

No reference to quantum mechanics, measurement, or environment. Classicality is capacity exhaustion.

### Time

**Definition:** Event $A$ precedes event $B$ if $A$ is a causal ancestor of $B$ in the directed acyclic graph (DAG) of overflow events.

This DAG exists because overflow events are non-trivial interactions (from the Attractor Theorem) and the resulting partial order is acyclic (overflow is directional—from high to low occupancy).

**Time is the partial order on the causal DAG of overflow events.** It is not a background structure. It is created by the first overflow event.

Before the first overflow: empty DAG, no partial order, no time. This is the Euclidean phase.

After the first overflow: DAG acquires its first edge, partial order begins. This is the Lorentzian phase.

**The Euclidean-to-Lorentzian transition is not a phase transition in spacetime. It is the appearance of the first causal relation.**

### Mass

Locked information ($A = 1-q$) has one remaining function under the axioms: resist change of state. Resistance to state change is inertial mass.

$$\rho_m = \frac{A \cdot \ln 2}{\mathfrak{l}^3}$$

### Two Timescales (Forced by A1 + A2)

**Process A (homogenization):** Evolution equation $\Delta q = +\Delta^2 q / q^2 + S(q)$ conserves $\sum q_i$. Redistributes $q$ without changing global mean. Timescale $\tau_A \sim L^2 q^2 / (\mathfrak{l} \cdot c)$.

**Process B (accumulation):** Spontaneous occupation (A1: nonzero probability for any distinguishable transition). Each event decreases global $\bar{q}$ by $1/N$. Timescale $\tau_B \sim N/\varepsilon \cdot t_p$.

**Why both are necessary:**
- Without A: local regions reach $q=0$ first, become isolated islands. Information conservation (A1+A2) forbids permanent isolation. A is necessary.
- Without B: global $\bar{q}$ never decreases. Classical behavior never emerges. A1 guarantees $\varepsilon > 0$, so B is unavoidable.
- They cannot be the same equation (A conserves $\sum q_i$; B decreases it).

Two timescales are forced by A1 + A2. Not assumed.

### Cyclic Cosmology

$q \to 0$ globally: all cells full, new overflow events (A1) cannot be accommodated without violating A2. The only resolution: forced reset. New cycle begins.

$$q = 1 \xrightarrow{\text{A1}} \Delta q \neq 0 \xrightarrow{\text{Process A+B}} q \to 0 \xrightarrow{\text{A2 boundary}} q \to 1$$

---

## IV. Why the Universe Had to Be This Way

The answer is now complete.

**Not:** "Because it was designed efficiently."

**Not:** "Because the laws were selected by natural selection."

**Not:** "Because observers can only exist in such a universe."

**But:** Because A1 and A2 are attractors. Any universe with interaction converges to them. The question "why does our universe satisfy these axioms?" has the same logical status as "why does 2+2=4?" It couldn't be otherwise.

From A1 and A2, everything follows:

- Information flows from high to low occupancy (entropy)
- Irreversibility emerges at high capacity ratios (second law)
- Time emerges from the first causal relation (arrow of time)
- Classical behavior is capacity exhaustion (quantum-to-classical)
- Quantum coherence is finite-environment reversibility (quantum mechanics)
- Mass is locked information density
- The universe cycles through capacity exhaustion and reset

**None of this is designed. All of this is necessary.**

The classical world is not what the quantum world becomes. It is what the quantum world loses—over cosmological time, through the irreversible accumulation of overflow events, until capacity runs out. You are reading this in a classical world because your cells have largely exhausted their capacity. The quantum world still exists, in systems small enough or young enough that their capacity has not yet run out.

---

## V. Quantitative Prediction

For objects of equal mass $M$, denser objects decohere slower:

$$\frac{\tau(\rho_1, M)}{\tau(\rho_2, M)} = \frac{\rho_1}{\rho_2}$$

This is $\varepsilon$-independent (the unknown spontaneous occupation rate cancels). It is opposite in sign to Penrose and Diósi (who predict denser objects decohere faster due to larger gravitational self-energy).

**Experimental discriminator:** Gold nanoparticles ($\rho = 19.3$ g/cm³) vs silica nanoparticles ($\rho = 2.2$ g/cm³) of equal mass. DGF predicts gold maintains coherence $\approx 8.8\times$ longer. Penrose/Diósi predict gold decoheres $\approx 2\times$ faster.

**Caveat:** This prediction depends on the geometric volume scaling $\Delta N = V/\mathfrak{l}^3$ and the single-event collapse premise—both require the $q$-to-coherence mapping (Open Problem O5) to be validated.

---

## VI. Open Problems

| Problem | Status |
|---------|--------|
| O1: Why 3 spatial dimensions | Information adjacency graph topology unspecified |
| O2: The $\sim 10^{-5}$ CMB residual | Observational input in all cyclic cosmologies |
| O3: Gravity from $q$-gradient | Requires connecting information graph to Riemannian geometry |
| O4: Osmotic pressure functional form | Modeling choice M1, not uniquely forced |
| O5: $q$-to-quantum-coherence mapping | Critical for quantitative predictions |
| O6: Value of $\varepsilon$ | Phenomenological parameter, not derived |

---

## VII. Conclusions

1. **A1 and A2 are attractors, not axioms.** Any interacting system converges to them. (Theorem, Section II)

2. **Irreversibility is emergent.** It is the high-capacity-ratio limit of A1 + A2, not an independent axiom. (Section III)

3. **Time is the causal DAG of overflow events.** It did not pre-exist. It was created by the first overflow. (Section III)

4. **Classical and quantum are the same physics at different capacity ratios.** Not two worlds. (Section III)

5. **The classical world is what the quantum world loses.** Capacity exhaustion, not external decoherence. (Section III)

6. **A falsifiable prediction distinguishes DGF from Penrose/Diósi.** $\tau \propto \rho$ vs $\tau \propto \rho^{-1/3}$ for equal mass. (Section V)

The universe had to be this way. Not because it was designed to be. Because any universe that exists must be.

---

## References

- Aguiar, G.H.S. & Matsas, G.E.A. (2025). PRD 112, 046004.
- Bassani, P.M. & Magueijo, J. (2025). PRD 111, 103529.
- Bombelli, L. et al. (1987). Spacetime as a causal set. PRL 59, 521.
- Caticha, A. (2009). Entropic dynamics. J. Phys. A 42, 345401.
- Chiribella, G. et al. (2011). Informational derivation of QT. PRA 84, 012311.
- Cover, T.M. & Thomas, J.A. (2006). Elements of Information Theory. Wiley.
- Diósi, L. (1989). PRA 40, 1165.
- Landauer, R. (1961). IBM J. Res. Dev. 5, 183.
- Malament, D. (1977). The class of continuous timelike curves determines the topology of spacetime. J. Math. Phys. 18, 1399.
- Mukohyama, S. (2013). Emergence of time in power-counting renormalizable Riemannian theory of gravity. arXiv:1303.1409.
- Neukart, F. et al. (2024). Entropy 26, 1039.
- Penrose, R. (1996). Gen. Rel. Grav. 28, 581.
- Schlosshauer, M. (2007). Decoherence and the Quantum-to-Classical Transition. Springer.
- Shannon, C.E. (1948). Bell Syst. Tech. J. 27, 379.
- Sienicki, K. (2025). arXiv:2503.07666.
- Sorkin, R.D. (1991). Spacetime and causal sets. In Relativity and Gravitation.
- Wheeler, J.A. (1990). It from bit. In Complexity, Entropy, and the Physics of Information.
- Zurek, W.H. (1989). PRA 40, 4731.
- Zurek, W.H. (2003). Rev. Mod. Phys. 75, 715.

---

## Appendix: Complete Assumption Inventory

| Label | Content | Status |
|-------|---------|--------|
| A1 | Distinguishable states exist | **Attractor** (not axiom) |
| A2 | Each cell ≤ 1 bit | **Attractor** (not axiom) |
| M1 | Osmotic pressure $\Pi \propto (1-q)/q$ | Modeling choice |
| P1 | Spontaneous occupation rate $\varepsilon > 0$ | From A1; value unknown |
| C1–C3 | $c$, $\hbar$, $G$ | Experimental inputs |
| O1–O6 | Open problems | Explicitly listed |

**The key upgrade from v4:** A1 and A2 are no longer labeled "Axiom." They are labeled "Attractor"—because they are proven to be the inevitable endpoint of any interacting system, not assumptions we impose.

No assumption is hidden.
