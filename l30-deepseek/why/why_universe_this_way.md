# Why the Universe Had to Be This Way

**Huang Zhongchang**  
Independent Researcher, Nanjing, China  
Draft v1.0 | 2026-06-05

---

## Abstract

We ask why the universe operates by the laws it does, rather than some other laws. We show that three minimal axioms about information—that distinguishable states exist, that capacity is bounded, and that overflow is irreversible—uniquely determine the dynamics of any information-processing system. Efficiency is not assumed; it emerges as the only self-consistent behavior under these constraints. From these three axioms alone, we derive: a unique evolution equation with no free parameters, the origin of classical behavior, the definition of mass as locked information density, the spontaneous origin of the Big Bang, and a cyclic mechanism requiring no external input. The framework does not claim the universe is unique—it claims that whatever universe exists, its dynamical laws could not have been otherwise.

---

## I. Introduction

The question "why does the universe obey these laws and not others?" has three standard answers in modern physics.

The first is the anthropic principle: the laws are as they are because only these laws permit observers to exist. This is logically consistent but explanatorily empty—it tells us why we observe these laws, not why these laws exist.

The second is cosmic natural selection (Smolin 1992; Bassani & Magueijo 2025): universes reproduce through black holes, and laws that produce more black holes propagate. This requires an enormous ensemble of trial universes and explains laws as selected, not necessary.

The third is the multiverse: all possible laws are realized somewhere, and we happen to inhabit a region with these laws. This is in principle untestable.

We propose a fourth answer: **the laws could not have been otherwise**. Not because of selection, not because of observation bias, but because any information system subject to three minimal constraints is forced into a unique dynamical behavior. The laws are not selected from a menu of possibilities—the menu has only one item.

This paper establishes the conditions under which this claim holds. We show that three axioms, each representing a minimal necessary condition for any information system to exist, jointly force: a unique evolution equation, the emergence of classical behavior from quantum origins, a definition of mass, and a cyclic cosmology—all without free parameters.

The contrast with Bassani & Magueijo (2025) is instructive. They ask *how* to make a universe, and answer: through natural selection operating on random mutations in the constants of nature. We ask *why* the universe had to be this way, and answer: because no other way is self-consistent under the axioms of information existence.

---

## II. Three Axioms

We state three axioms, each representing a minimal necessary condition. We show that removing any one axiom causes the framework to collapse.

### Axiom 1: Information Exists

There exist distinguishable states. No spacetime, mass, or energy is presupposed. The only content of this axiom is that two configurations can in principle be told apart.

**Necessity:** Without distinguishable states, no physical description is possible. This axiom is the logical prerequisite for any theory.

**What it gives us:** A minimum resolvable unit—1 bit, the information content of distinguishing between two states. This unit is not assumed; it follows from the binary nature of distinguishability (occupied vs. unoccupied).

### Axiom 2: Capacity Is Bounded

Each minimum information unit (a cell) carries at most 1 bit. This introduces a single scale $\mathfrak{l}$—the physical size of the minimum cell—as the framework's one dimensional input, fixed by experiment rather than derived.

**Necessity:** Without bounded capacity, information has no resolution limit. Unbounded capacity is equivalent to no capacity at all—any state could be encoded anywhere, making distinguishability meaningless. Axiom 2 gives Axiom 1 operational content.

**What it gives us:** A maximum information density $\rho_{max} = \ln 2 / \mathfrak{l}^3$, and a natural definition of the accessible coherence fraction:

$$\boxed{q = \frac{\text{unoccupied cells}}{\text{total cells}} \in [0,1]}$$

$q = 1$: all cells empty, maximum capacity available.  
$q = 0$: all cells full, no capacity remaining.  
$A = 1 - q$: locked fraction.

### Axiom 3: Overflow Is Irreversible

When a cell reaches capacity, excess information transfers to lower-occupancy cells and cannot spontaneously return. This is the information-theoretic arrow of time.

**Necessity:** Without irreversibility, information flow has no direction. A reversible system has no time arrow, no causal structure, no distinction between past and future. Axiom 3 is the minimum condition for causality to exist.

**What it gives us:** A preferred direction of information flow, derivable from Shannon entropy alone (Section III).

### The Minimality of the Three Axioms

Each axiom is necessary; together they are sufficient to determine the dynamics uniquely (Sections III–IV). No axiom can be weakened or removed:

| Axiom removed | Consequence |
|---------------|-------------|
| Axiom 1 | No distinguishable states; no framework |
| Axiom 2 | No resolution limit; Axiom 1 becomes vacuous |
| Axiom 3 | No time direction; no causal dynamics |

---

## III. What the Axioms Force: Efficiency Without Assumption

We now show that the three axioms, together with a derived conservation law, force a unique dynamical structure. **Efficiency is not assumed—it is the only self-consistent behavior.**

### Information Conservation (from Axioms 1 and 2)

**Theorem:** Information is conserved.

**Proof:** Axiom 1 requires that state transitions be injective (distinguishable inputs map to distinguishable outputs). Axiom 2 fixes the total number of cells. An injective map on a finite set is bijective. Therefore information is neither created nor destroyed. $\square$

### The Direction of Flow (from Axiom 3 and Shannon Entropy)

Consider two systems $A$ (high occupancy, low $q_A$) and $B$ (low occupancy, high $q_B$). Transfer $\delta$ units of information from $A$ to $B$. The total Shannon entropy change is:

$$\Delta S = \left[\ln\frac{1-q_B}{q_B} - \ln\frac{1-q_A}{q_A}\right]\delta$$

When $q_A < q_B$, this quantity is positive. By Axiom 3 (irreversibility drives entropy increase), information flows spontaneously from low-$q$ to high-$q$ regions.

**Information flows from high occupancy to low occupancy. No force is required—this is thermodynamic necessity.**

### The Transfer Rate $\kappa = 1$ (from Conservation and Axiom 3)

The transfer rate $\kappa$ measures bits transferred per step per cell boundary.

$\kappa < 1$: each step transfers less than 1 bit. The remainder is stranded in the source cell, requiring additional steps and consuming additional capacity. Under Axiom 3, this additional capacity expenditure is irreversible—permanently lost. This violates information conservation.

$\kappa > 1$: each step transfers more than 1 bit per cell boundary. But Axiom 2 limits each cell to 1 bit. Transferring more than 1 bit across a single cell boundary in one step would require the boundary cell to momentarily hold more than 1 bit. This violates Axiom 2.

Therefore: $\kappa = 1$. **Not assumed. Forced.**

### The Step Size $d\tau = 1$ bit (from Axioms 1 and 2)

Each elementary step processes exactly 1 bit.

**Lower bound (Axiom 1):** The minimum resolvable information unit is 1 bit (two distinguishable states). Processing less than 1 bit per step would require resolving a sub-bit distinction, which does not exist under Axiom 1.

**Upper bound (Axioms 1 and 2 with nearest-neighbor constraint):** Each step transfers information to the nearest neighbor cell only (derived below). Each cell holds at most 1 bit (Axiom 2). Therefore each step transfers at most 1 bit.

Lower and upper bounds coincide: $d\tau = 1$ bit per step. **Not assumed. Forced.**

### The Neighbor Structure: Nearest-Neighbor Only (from Axioms 1 and 2)

Suppose information jumps from cell $A$ to cell $C$, bypassing intermediate cell $B$.

During the jump, the information is not present in any cell. But Axiom 1 requires that information exist in distinguishable states at all times—information cannot be "in transit" without occupying a cell. A jump bypassing $B$ would require information to exist in no cell during transit. This violates Axiom 1.

Therefore information transfers only to adjacent cells. **Not assumed. Forced.**

### Summary: Efficiency Is a Theorem, Not an Axiom

| Parameter | Value | Forced by |
|-----------|-------|-----------|
| Transfer rate $\kappa$ | $1$ | Conservation + Axiom 3 |
| Step size $d\tau$ | $1$ bit | Axioms 1 + 2 |
| Neighbor structure | nearest-neighbor | Axioms 1 + 2 |

The most efficient possible information processing is not a design goal. It is the **only self-consistent behavior** under the three axioms. Non-efficient behavior is not suboptimal—it is logically impossible.

---

## IV. The Unique Evolution Equation

### Derivation

The osmotic pressure driving information flow is proportional to the concentration gradient of locked information:

$$\Pi \propto \frac{1-q}{q}$$

The information flux is:

$$J = \frac{\kappa}{q^2}\nabla q = \frac{1}{q^2}\nabla q$$

with $\kappa = 1$ from Section III. Applying information conservation in discrete form:

$$\boxed{\Delta q = -\frac{\Delta^2 q}{q^2}}$$

where $\Delta^2 q = q_{i+1} - 2q_i + q_{i-1}$ is the discrete Laplacian.

### Continuous Limit

In the regime where $q$ varies on scales much larger than $\mathfrak{l}$ (valid for all macroscopic systems), Taylor expansion gives $\Delta^2 q \approx \mathfrak{l}^2 \partial_x^2 q$. With $\mathfrak{l}/(\mathfrak{l}/c) = c$:

$$\partial_t q = -t_p \cdot \frac{\partial_x^2 q}{q^2}$$

where $t_p = \mathfrak{l}/c$ is the Planck time (an experimental input, not a derived quantity).

**Note:** The continuous equation holds when the characteristic scale of $q$ variation is much larger than $\mathfrak{l}$. Near the Planck scale, the discrete equation is the correct description.

### Verification of Boundary Behavior

- $q \to 1$ (quantum limit): equation reduces to linear diffusion, $q$ slowly homogenizes. ✓
- $q \to 0$ (classical limit): diffusion coefficient $\sim 1/q^2 \to \infty$, evolution accelerates toward deadlock. ✓
- $\nabla q = 0$ (equilibrium): $\Delta q = 0$, evolution stops. ✓

### No Free Parameters

The equation contains no adjustable parameters. The only input is $t_p$, which is an experimental calibration constant (the ratio of the cell size to the maximum propagation speed), not a theoretical degree of freedom.

---

## V. Emergence

### Classical Behavior

**Definition (operational):** A system is classical if it cannot respond to external information input—if additional information cannot change its state.

Response requires available capacity. When $q = 0$, all cells are full; no capacity remains; the system cannot accept new information; its state is fixed.

$$q \to 0 \implies \text{no available capacity} \implies \text{state fixed} \implies \text{classical behavior}$$

No reference to quantum mechanical phase, superposition, or wave functions is required. Classical behavior is the operational consequence of capacity exhaustion under Axiom 2.

**Note:** This operational definition agrees with standard quantum mechanics in the limits $q \to 0$ (classical) and $q \to 1$ (quantum). The correspondence in intermediate regimes is an open problem.

### Mass

Locked information (fraction $A = 1-q$) cannot flow, cannot participate in state changes, and has only one remaining function under the axioms: **resistance to change of state**.

Resistance to change of state is the operational definition of inertial mass.

With cells independent (maximally efficient storage, forced by the nearest-neighbor constraint), the mass density is:

$$\boxed{\rho_m = \frac{A \cdot \ln 2}{\mathfrak{l}^3}}$$

Mass density is locked information density. The quantity $\ln 2 / \mathfrak{l}^3$ is not a free constant—it is the information capacity per unit volume, determined entirely by Axiom 2 and the cell size $\mathfrak{l}$.

### The Big Bang

At $q = 1$, all cells are empty. Axiom 1 requires that occupied and unoccupied states be distinguishable, which means spontaneous occupation has nonzero probability:

$$P(\text{spontaneous occupation}) = \frac{1}{2^N} \neq 0$$

where $N$ is the total number of cells. This probability is vanishingly small but strictly positive. Given sufficient evolution steps, the first spontaneous occupation **must** occur.

When it does: a local $q$ gradient appears ($\Delta q = 1/N$), Axiom 3 activates, information begins flowing outward, and the diffusion wave propagates at maximum speed $c$.

**The Big Bang is not an energy singularity. It is the first spontaneous information occupation event, triggering an outward diffusion wave. Its occurrence is guaranteed by Axiom 1. Its location is random, explaining large-scale homogeneity.**

### The Cyclic Mechanism

As $q \to 0$ locally, information density approaches $\ln 2 / \mathfrak{l}^3$. New overflow events (guaranteed by Axiom 1) have nowhere to go—all cells are full. This creates a pressure that violates Axiom 2 (bounded capacity). The only resolution consistent with Axiom 2 is forced cell reset: a new Big Bang.

$$q = 1 \xrightarrow{\text{Axiom 1}} \Delta q \neq 0 \xrightarrow{\text{Axiom 3}} q \to 0 \xrightarrow{\text{Axiom 2 violation}} q \to 1$$

The cycle closes without external input. Each reset carries a residual imprint ($\sim 10^{-5}$, observed in CMB power spectrum; theoretical origin is an open problem shared with all cyclic cosmologies).

---

## VI. Why This Way and No Other

### The Standard View: Nature Optimizes

Conventional physics invokes variational principles: least action, maximum entropy, shortest path. The implicit picture is that nature surveys possible behaviors and selects the optimal one.

This picture has a hidden assumption: that suboptimal behaviors exist as possibilities from which the optimal is chosen.

### The DGF View: Suboptimal Behaviors Do Not Exist

Under our three axioms, behaviors with $\kappa < 1$, $d\tau \neq 1$, or non-nearest-neighbor transfer are not suboptimal—they are **logically inconsistent**. They violate the axioms directly.

There is no menu of possible behaviors from which efficiency is selected. The menu has one item.

This resolves the explanatory gap in variational principles: we no longer need to explain why nature chooses the optimal—we show that only the optimal is self-consistent.

### The Role of Irreversibility

Among the three axioms, Axiom 3 (irreversibility) is the load-bearing one. It is the source of:

- The direction of information flow (entropy gradient)
- The time arrow (information accumulates, never spontaneously disperses)
- The forced efficiency (wasted capacity is permanently lost)
- The cyclic mechanism (deadlock forces reset)

Axioms 1 and 2 define the space of possible states. Axiom 3 defines what happens in that space.

**Irreversibility is not a feature of the universe. It is the condition under which a universe can exist at all.**

### Contrast with Natural Selection

Bassani & Magueijo (2025) model the origin of physical laws as cosmic natural selection: random mutations in the constants of nature, with diffeomorphism-invariant states as absorbers. Laws are explained as survivors of selection.

Our framework makes a stronger claim: the laws require no selection because no alternatives exist. The absorbing state of their Markov chain is our unique fixed point—but we derive it from constraints rather than selecting it from an ensemble.

The two frameworks are complementary: theirs explains *how* order can emerge from chaos through selection; ours explains *why* the selected order had to be this particular order.

---

## VII. Open Problems

We state three open problems explicitly. Their existence does not undermine the results of Sections III–VI, which are self-contained.

| Problem | Status |
|---------|--------|
| Why 3 spatial dimensions | The information adjacency graph has an unspecified topology. Why it realizes 3-dimensional space is not addressed by the axioms. |
| The $\sim 10^{-5}$ residual | Each cycle carries a residual imprint into the next. The value $\sim 10^{-5}$ matches CMB observations but is an observational input, not a derived prediction. Its theoretical origin is an open problem in all cyclic cosmologies. |
| Gravity | The $q$-gradient produces information flow. Whether and how this flow curves spacetime in the sense of general relativity requires a connection between the information graph and Riemannian geometry that we do not establish here. |

---

## VIII. Conclusions

We have shown that three axioms—information exists, capacity is bounded, overflow is irreversible—uniquely determine the dynamics of any information system:

1. Information is conserved (theorem from Axioms 1 and 2).
2. Information flows from high to low occupancy (theorem from Axiom 3 and Shannon entropy).
3. Transfer rate, step size, and neighbor structure are each uniquely fixed (not assumed).
4. The evolution equation $\Delta q = -\Delta^2 q / q^2$ has no free parameters.
5. Classical behavior, mass, the Big Bang, and cosmic cycling all emerge without additional assumptions.

The central result is not a new equation or a new prediction. It is a logical claim: **under these three axioms, no other dynamics is possible**. The universe operates this way not because it was designed to, not because it was selected from alternatives, but because these are the only self-consistent dynamics available to any system in which information exists, capacity is finite, and change is irreversible.

The question "why the universe had to be this way" has an answer: **because the alternatives are not merely improbable—they are logically inconsistent with the existence of information itself.**

---

## References

- Bassani, P.M. & Magueijo, J. (2025). How to make a Universe. *Phys. Rev. D* **111**, 103529.
- Bekenstein, J.D. (1973). Black holes and entropy. *Phys. Rev. D* **7**, 2333.
- Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM J. Res. Dev.* **5**, 183.
- Neukart, F., Marx, E. & Vinokur, V. (2024). The Quantum Memory Matrix. *Entropy* **26**, 1039.
- Penrose, R. (2010). *Cycles of Time*. Bodley Head.
- Shannon, C.E. (1948). A mathematical theory of communication. *Bell Syst. Tech. J.* **27**, 379.
- Smolin, L. (1992). Did the universe evolve? *Classical Quantum Gravity* **9**, 173.
- Wheeler, J.A. (1990). Information, physics, quantum: the search for links. In *Complexity, Entropy, and the Physics of Information*.
- Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Rev. Mod. Phys.* **75**, 715.

---

## Appendix: Calibration Constants

The framework is internally dimensionless. Contact with measured physics requires three experimental inputs:

| Constant | Role | Value |
|----------|------|-------|
| $c$ | Maximum propagation speed (cell size / step time) | $3 \times 10^8$ m/s |
| $\hbar$ | Quantum of action | $1.055 \times 10^{-34}$ J·s |
| $G$ | Gravitational calibration | $6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻² |

From these: $\mathfrak{l} = l_p = \sqrt{\hbar G/c^3}$, $t_p = l_p/c$, $m_p = \sqrt{\hbar c/G}$.

These constants do not enter the logical structure of the framework. They enter only when translating dimensionless information-theoretic results into SI units.
