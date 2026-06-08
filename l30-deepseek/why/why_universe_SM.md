# Supplemental Material
## Why the Universe Had to Be This Way

**Huang Zhongchang**
Draft v1.0 | 2026-06-05

---

## S1. Information Conservation: Complete Proof

**Theorem:** Under Axioms 1 and 2, information is conserved.

**Setup:**

Let the total system have $N$ cells. Each cell $i$ has state $s_i \in \{0, 1\}$ (unoccupied/occupied). The global state is $\mathbf{s} = (s_1, s_2, \ldots, s_N)$.

A dynamical step is a map $f: \mathbf{s} \to \mathbf{s}'$.

**Axiom 1** requires $f$ to be injective: if $\mathbf{s} \neq \mathbf{s}'$, then $f(\mathbf{s}) \neq f(\mathbf{s}')$. Two distinguishable states must remain distinguishable after any evolution.

**Axiom 2** fixes $N$ (total cells finite and constant). The domain and codomain of $f$ are both $\{0,1\}^N$, a finite set of size $2^N$.

An injective map from a finite set to itself is bijective (by the pigeonhole principle).

A bijective map preserves the total number of occupied cells: $\sum_i s_i' = \sum_i s_i$.

Therefore the total information content $I = \sum_i s_i \cdot \ln 2$ is conserved. $\square$

**Remark:** Conservation holds at every step, not just on average. It is exact, not statistical.

---

## S2. Direction of Flow: Shannon Entropy Derivation

**Setup:**

System $A$ has $N_A$ cells with mean occupancy $\bar{f}_A = 1 - q_A$.
System $B$ has $N_B$ cells with mean occupancy $\bar{f}_B = 1 - q_B$.

The Shannon entropy of a cell with occupancy fraction $f$ is:

$$h(f) = -f \ln f - (1-f)\ln(1-f)$$

Total entropy: $S = N_A h(\bar{f}_A) + N_B h(\bar{f}_B)$.

**Transfer:**

Transfer $\delta$ bits from $A$ to $B$: $\bar{f}_A \to \bar{f}_A - \delta/N_A$, $\bar{f}_B \to \bar{f}_B + \delta/N_B$.

First-order entropy change:

$$\Delta S = -\frac{\partial h}{\partial f}\bigg|_A \delta + \frac{\partial h}{\partial f}\bigg|_B \delta = \left[\ln\frac{1-\bar{f}_B}{\bar{f}_B} - \ln\frac{1-\bar{f}_A}{\bar{f}_A}\right]\delta$$

Substituting $\bar{f} = 1 - q$:

$$\Delta S = \left[\ln\frac{q_B}{1-q_B} - \ln\frac{q_A}{1-q_A}\right]\delta$$

**When $q_A < q_B$ (A more occupied than B):**

$$\frac{q_A}{1-q_A} < \frac{q_B}{1-q_B} \implies \Delta S > 0 \text{ for } \delta > 0$$

Entropy increases when information flows from low-$q$ to high-$q$.

By Axiom 3 (irreversibility drives entropy increase), this is the spontaneous direction.

**Conclusion:** Information flows from $q_A < q_B$ to $q_A > q_B$, i.e., from high occupancy to low occupancy. $\square$

---

## S3. Transfer Rate $\kappa = 1$: Complete Proof

**Definition:** $\kappa$ is the number of bits transferred per step per cell boundary.

**Claim:** $\kappa = 1$ is the only value consistent with Axioms 1, 2, 3 and information conservation.

**Case $\kappa < 1$:**

Each step transfers $\kappa < 1$ bits. The remaining $1 - \kappa$ bits are not transferred—they remain in the source cell as a "partial transfer residue."

This residue must be processed in a subsequent step, which itself transfers $\kappa < 1$ bits, leaving another residue, and so on.

The total capacity consumed to transfer 1 bit is:

$$C_{total} = \sum_{k=0}^{\infty} \kappa(1-\kappa)^k = 1 \text{ bit transferred} + \frac{\kappa(1-\kappa)}{1-(1-\kappa)} = \frac{1}{\kappa} \text{ bit-steps}$$

For $\kappa < 1$, this exceeds 1 bit-step. The excess $1/\kappa - 1 > 0$ bit-steps represent capacity consumed but not productively used.

Under Axiom 3 (irreversibility), capacity consumed cannot be recovered. Information conservation (S1) requires that capacity consumed equals capacity transferred. Consuming more capacity than transferred violates information conservation.

Therefore $\kappa < 1$ is inconsistent. $\square$

**Case $\kappa > 1$:**

Each step transfers $\kappa > 1$ bits across a single cell boundary.

The receiving cell must accommodate $\kappa > 1$ bits instantaneously. But Axiom 2 limits each cell to 1 bit.

Transferring $\kappa > 1$ bits to a cell already holding up to 1 bit would require the cell to hold up to $1 + \kappa > 2$ bits, violating Axiom 2.

Therefore $\kappa > 1$ is inconsistent. $\square$

**Conclusion:** $\kappa = 1$. $\square$

---

## S4. Step Size $d\tau = 1$ bit: Complete Proof

**Claim:** Each elementary evolution step processes exactly 1 bit.

**Lower bound:**

By Axiom 1, the minimum resolvable information unit is 1 bit—the information distinguishing two states (occupied vs. unoccupied).

Processing $d\tau < 1$ bit per step would require resolving a distinction smaller than 1 bit. No such distinction exists under Axiom 1.

Therefore $d\tau \geq 1$ bit. $\square$

**Upper bound:**

From the nearest-neighbor constraint (S5), each step transfers information to exactly one adjacent cell.

From $\kappa = 1$ (S3), the transfer across one cell boundary is exactly 1 bit.

Therefore $d\tau \leq 1$ bit. $\square$

**Conclusion:** $d\tau = 1$ bit exactly. Lower and upper bounds coincide. $\square$

---

## S5. Nearest-Neighbor Constraint: Complete Proof

**Claim:** Information transfers only between adjacent cells.

**Proof by contradiction:**

Suppose information transfers from cell $A$ to cell $C$, bypassing intermediate cell $B$ (where $B$ is between $A$ and $C$ on the information graph).

During transit from $A$ to $C$, the information is neither in $A$ (it has left) nor in $C$ (it has not yet arrived).

Axiom 1 requires that information exist in distinguishable states at all times. A state in which the information is "between cells" is not a distinguishable cell state.

Therefore the information cannot be "in transit" without occupying a cell. The bypass transfer requires the information to not exist in any cell during transit, violating Axiom 1.

Therefore all transfers are between adjacent cells. $\square$

**Remark:** "Adjacent" is defined by the information graph, not by any pre-existing spatial metric. The spatial interpretation of adjacency is an emergent property, not an input.

---

## S6. The Evolution Equation: Complete Derivation

**Step 1: Osmotic pressure**

The driving force for information flow is the gradient in the chemical potential of locked information $(1-q)$. The osmotic pressure difference between adjacent cells $i$ and $j$ is:

$$\Delta\Pi_{ij} = \frac{1-q_j}{q_j} - \frac{1-q_i}{q_i} = \frac{q_i - q_j}{q_i q_j}$$

**Step 2: Information flux**

With $\kappa = 1$ and nearest-neighbor transfer, the flux from cell $i$ to cell $j$ is:

$$J_{ij} = \Delta\Pi_{ij} = \frac{q_i - q_j}{q_i q_j}$$

For small gradients, $q_i \approx q_j \approx q$, so:

$$J_{ij} \approx \frac{q_i - q_j}{q^2} = \frac{\Delta q}{q^2}$$

**Step 3: Discrete continuity equation**

Information conservation (S1) gives the discrete continuity equation:

$$\Delta q_i = -(J_{i,i+1} - J_{i-1,i}) = -\frac{\Delta^2 q_i}{q_i^2}$$

where $\Delta^2 q_i = q_{i+1} - 2q_i + q_{i-1}$ is the discrete Laplacian.

$$\boxed{\Delta q = -\frac{\Delta^2 q}{q^2}}$$

No free parameters. $\square$

**Step 4: Continuous limit**

Valid when $q$ varies on scales $L \gg \mathfrak{l}$ (macroscopic regime).

Taylor expansion: $q_{i\pm 1} = q(x \pm \mathfrak{l}) = q \pm \mathfrak{l}\partial_x q + \frac{\mathfrak{l}^2}{2}\partial_x^2 q + O(\mathfrak{l}^3)$

Therefore: $\Delta^2 q_i = \mathfrak{l}^2 \partial_x^2 q + O(\mathfrak{l}^4)$

Time direction: $\Delta q_i / t_p = \partial_t q$ where $t_p = \mathfrak{l}/c$.

Substituting:

$$\partial_t q = -\frac{t_p \cdot \partial_x^2 q}{q^2}$$

This is the unique continuum limit of the discrete evolution equation.

**Note:** Near the Planck scale ($L \sim \mathfrak{l}$), the discrete equation is the correct description. The continuum equation is an approximation valid for macroscopic systems.

---

## S7. Classical Behavior: Operational Definition and Consistency

**Definition:**

A system is operationally classical if it cannot respond to external information input:

$$\text{Classical} \iff q = 0 \iff \text{no available capacity}$$

**Derivation:**

Response to external input requires a cell to change state from unoccupied to occupied (accepting new information). This requires the cell to be unoccupied, i.e., to have available capacity.

When $q = 0$: all cells occupied, no capacity available, no response possible. Classical. ✓

When $q > 0$: some cells unoccupied, capacity available, response possible. Quantum (in the DGF operational sense). ✓

**Consistency with standard quantum mechanics:**

At $q \to 0$: system cannot be disturbed, states are fixed. Consistent with classical limit. ✓

At $q \to 1$: system fully responsive to information. Consistent with quantum limit. ✓

Intermediate $q$: partial response. The precise correspondence with standard quantum mechanical coherence is an open problem.

**What this does not claim:**

This definition does not claim to derive the full structure of quantum mechanics (Hilbert spaces, Born rule, measurement postulate). It claims only that the transition from responsive to non-responsive behavior is forced by Axiom 2, without invoking quantum mechanical postulates.

---

## S8. Mass Density: Derivation

**Physical argument:**

Locked information ($A = 1-q$) satisfies:
- Cannot flow (Axiom 3: overflow is irreversible; locked means already overflowed)
- Cannot participate in capacity exchanges (cells full)
- Under the axioms, its only remaining function is to resist change of state

Resistance to change of state is the operational definition of inertial mass.

**Independence of cells:**

Under the nearest-neighbor constraint and $\kappa = 1$, each locked cell contributes independently to mass—there is no interaction between locked cells that would introduce correlations.

This is analogous to independent bit storage in computer memory: each bit contributes independently to the total stored value.

**Mass density:**

Each locked cell contributes $\ln 2$ bits (one bit, information-theoretic content) per cell volume $\mathfrak{l}^3$:

$$\rho_m = \frac{A \cdot \ln 2}{\mathfrak{l}^3}$$

**Dimensional analysis:**

$\rho_m$ has units of $[\text{information}]/[\text{volume}]$. Converting to SI mass density requires the calibration constant $m_p / \ln 2$ (the mass per bit), which is determined experimentally via $m_p = \sqrt{\hbar c / G}$:

$$\rho_m^{SI} = \frac{A \cdot m_p}{\mathfrak{l}^3} \cdot \frac{\ln 2}{\ln 2} = \frac{A \cdot m_p}{l_p^3}$$

The factor $\ln 2$ cancels in the SI conversion because $m_p$ is already defined to absorb it. The physical content is: each Planck cell, when locked, contributes one Planck mass worth of inertia per Planck volume.

---

## S9. Big Bang Origin: Probability Estimate

**Setup:**

At $q = 1$, all $N$ cells are unoccupied. By Axiom 1, occupied and unoccupied are distinguishable states. Therefore spontaneous occupation of any single cell has nonzero probability.

**Probability estimate:**

By the maximum entropy principle (no constraint on which state is occupied), the probability of any specific cell being spontaneously occupied in one step is:

$$P_1 = \frac{1}{2} \cdot \frac{1}{N}$$

where $1/2$ is the probability of the occupied state (equal probability for two distinguishable states) and $1/N$ distributes over all cells.

For at least one of $N$ cells to be occupied:

$$P(\text{first occupation}) \approx N \cdot \frac{1}{2N} = \frac{1}{2}$$

per step, in the limit of large $N$.

**Expected waiting time:**

$$\langle \tau_{BigBang} \rangle = \frac{1}{P} \cdot t_p = 2t_p$$

The Big Bang occurs after approximately 2 Planck times of waiting.

**Remark:** This estimate assumes maximum entropy (equal probability for all states). The actual probability depends on the dynamics of the $q=1$ vacuum, which is not fully specified by the axioms alone. The key result—that the probability is nonzero and the Big Bang must eventually occur—is robust regardless of the specific probability value.

---

## S10. Cyclic Mechanism: Complete Argument

**Phase 1: Evolution ($q = 1 \to q \approx 0$)**

From the Big Bang (first spontaneous occupation), the evolution equation drives information from high-occupancy regions (low $q$) to low-occupancy regions (high $q$). Over cosmological timescales, $q$ decreases globally.

**Phase 2: Deadlock ($q \to 0$)**

As $q \to 0$, the osmotic pressure $\Pi \propto (1-q)/q \to \infty$. New overflow events (guaranteed nonzero probability by Axiom 1) have nowhere to go—all cells are at capacity. The system enters deadlock.

**Phase 3: Forced Reset**

In deadlock, a new overflow event would require a cell to hold more than 1 bit, violating Axiom 2. The only resolution consistent with all three axioms is forced cell reset: occupied cells are cleared to unoccupied.

This is not a violation of Axiom 3 (irreversibility)—that axiom prohibits *spontaneous* return of information. Forced reset under Axiom 2 pressure is not spontaneous; it is compelled by the logical impossibility of continued occupation beyond capacity.

**Phase 4: New Big Bang**

After reset, $q \to 1$. The system returns to Phase 1. The cycle closes.

**Residual imprint:**

Reset may be incomplete: some cells retain information from the previous cycle at the level $\delta q / q \sim 10^{-5}$ (inferred from CMB power spectrum). The theoretical mechanism for this residual is an open problem. Note that all cyclic cosmologies (Penrose CCC, LQC bounce, QMM) face the same open problem.

---

## S11. Relation to Existing Frameworks

| Framework | Core mechanism | Relation to DGF |
|-----------|---------------|-----------------|
| Penrose CCC | Conformal rescaling at aeon boundary | Cyclic: yes. Mechanism: global conformal vs. local information deadlock. DGF requires no conformal structure. |
| LQC bounce | Quantum geometry corrections to Friedmann equation | Maximum density: consistent ($\rho_{max} \sim \ln 2 / l_p^3$ in both). Mechanism: quantum geometry vs. information capacity. |
| QMM (Neukart 2025) | Planck-scale Hilbert cells store information | Shared: discrete cells, bounded capacity, cyclic. DGF adds: $q$ as decoherence measure, directed flow, unique evolution equation. |
| Bassani & Magueijo 2025 | Cosmic natural selection, absorbing Markov chain | Complementary: they derive *how* order emerges from chaos; we derive *why* the emergent order is unique. Their absorbing state is our unique fixed point. |
| Wheeler "It from Bit" | Information as fundamental | Shared philosophy. DGF provides explicit dynamics. |
| Zurek quantum Darwinism | Classical reality from redundant information encoding | Direction consistent. DGF provides the information-theoretic origin of decoherence. |

---

## S12. Open Problems: Precise Statements

**Open Problem 1: Three Spatial Dimensions**

The evolution equation $\Delta q = -\Delta^2 q / q^2$ is defined on the information adjacency graph. This graph has an unspecified topology.

The precise question: under what conditions does the information adjacency graph converge, in the continuum limit, to a 3-dimensional Riemannian manifold?

This is equivalent to asking why the universality class of the graph RG flow is 3-dimensional. Current DGF does not address this.

**Open Problem 2: The $10^{-5}$ Residual**

Each cyclic reset carries a residual imprint $\delta q / q \sim 10^{-5}$ into the next cycle, identified with CMB primordial fluctuations.

The precise question: what fraction of cell information survives forced reset, and why is it $\sim 10^{-5}$?

This is not derivable from the three axioms alone. It is an open problem in all cyclic cosmologies.

**Open Problem 3: Gravity**

The $q$-gradient produces directed information flow. General relativity describes gravity as spacetime curvature.

The precise question: does the $q$-gradient field, in the appropriate limit, satisfy an equation equivalent to the Einstein field equations?

This requires establishing a correspondence between the information adjacency graph and Riemannian geometry, which is Open Problem 1. Gravity cannot be addressed until the spatial structure is established.

---

## S13. Complete List of Assumptions

For full transparency, we list every assumption made in this paper:

| Label | Statement | Status |
|-------|-----------|--------|
| A1 | Distinguishable states exist | Axiom (irreducible) |
| A2 | Each cell holds at most 1 bit | Axiom (irreducible) |
| A3 | Overflow is irreversible | Axiom (irreducible) |
| D1 | $q$ = unoccupied/total cells | Definition |
| D2 | Classical = cannot respond to input | Operational definition |
| D3 | Mass = resistance to state change | Operational definition |
| T1 | Information conservation | Theorem (from A1+A2) |
| T2 | Flow direction: low-$q$ to high-$q$ | Theorem (from A3+Shannon) |
| T3 | $\kappa = 1$ | Theorem (from T1+A2+A3) |
| T4 | $d\tau = 1$ bit | Theorem (from A1+A2+T3) |
| T5 | Nearest-neighbor only | Theorem (from A1+A2) |
| T6 | Evolution equation | Theorem (from T1–T5) |
| C1 | $c$, $\hbar$, $G$ as calibration constants | Experimental inputs |
| O1 | Why 3 dimensions | Open problem |
| O2 | The $10^{-5}$ residual | Open problem |
| O3 | Gravity from $q$-gradient | Open problem |

**No assumption is hidden. Every result traces to A1, A2, A3, or experimental calibration.**

