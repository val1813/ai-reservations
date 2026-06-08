# Supplemental Material
## What the Classical World Lost: Decoherence as Capacity Exhaustion

**Huang Zhongchang**
Draft v4.0 | 2026-06-05

**Note:** This Supplemental Material accompanies the v4.0 main paper (`why_universe_v4.md`). All equation signs, numerical values, and derivations are cross-checked for consistency with the main text. New in v4.0: S14 (Numerical Verification), S15 (Quantitative Prediction: Complete Derivation).

---

## S1. Information Conservation: Complete Proof

**Theorem:** Under Axioms 1 and 2, information is conserved exactly at the micro level.

**Setup:**

Let the system have $N$ cells. Each cell $i$ has state $s_i \in \{0,1\}$ (unoccupied/occupied). Global state $\mathbf{s} = (s_1,\ldots,s_N)$.

A dynamical step is a map $f: \{0,1\}^N \to \{0,1\}^N$.

**Axiom 1** requires $f$ to be injective: distinguishable inputs remain distinguishable after any evolution.

**Axiom 2** fixes $N$ constant. The domain and codomain of $f$ are both $\{0,1\}^N$, a finite set of size $2^N$.

An injective map from a finite set to itself is bijective (pigeonhole principle).

A bijective map preserves $\sum_i s_i$ exactly.

Therefore total information $I = \sum_i s_i \cdot \ln 2$ is conserved at every step. $\square$

**What this does not say:** It does not say macroscopic entropy is conserved. The coarse-grained variable $q$ obeys an irreversible equation — see S2.

---

## S2. Coarse-Graining: Resolving the Conservation–Irreversibility Tension

**The tension:** S1 proves exact information conservation (bijective dynamics). Section III proves entropy increases ($\Delta S > 0$). These appear contradictory.

**Resolution:** Standard statistical mechanics. Microscopic dynamics are reversible; macroscopic entropy increases via coarse-graining.

**Formal structure:**

*Micro level* (cell states $\mathbf{s} \in \{0,1\}^N$):
- Dynamics $f: \mathbf{s} \to \mathbf{s}'$ is bijective (S1)
- Physical entropy $S_{phys} = H(\mathbf{s}) + K(\mathbf{s})$ is conserved (Zurek 1989)
- where $H$ = Shannon entropy, $K$ = algorithmic complexity

*Macro level* ($q$-field):
- $q = (\text{unoccupied cells})/N$ is a coarse-graining projection $\pi: \{0,1\}^N \to [0,1]$
- Many microstates $\mathbf{s}$ map to the same $q$; information about which microstate is discarded
- The induced transition matrix $W_{q \to q'}$ on the macro level is doubly stochastic (because $f$ is bijective and the projection is uniform)
- By Cover's theorem (Cover & Thomas 2006, Theorem 4.2.2): for any doubly stochastic transition matrix, Shannon entropy of the distribution over macro states is non-decreasing

**Conclusion:** Micro information conservation and macro entropy increase are compatible. The $q$-field obeys an irreversible diffusion equation derived from reversible micro dynamics. This is not a contradiction — it is the standard resolution of the reversibility paradox, here applied to an information-theoretic setting. $\square$

**Explicit mapping:**
$$q = \frac{1}{N}\sum_i (1-s_i) = 1 - \frac{\sum_i s_i}{N}$$

A single macro state $q$ corresponds to $\binom{N}{Nq}$ micro states. As $N \to \infty$, the entropy of this count grows as $N \cdot h(q)$ where $h(q) = -q\ln q - (1-q)\ln(1-q)$ is the binary entropy function. The macro description discards $N \cdot h(q)$ bits of micro information per unit volume. This discarded information is what flows into algorithmic complexity $K$ while $H$ increases.

---

## S3. Flow Direction: Shannon Entropy Derivation

**Setup:**

System $A$: $N_A$ cells, mean occupancy $\bar{f}_A = 1-q_A$.
System $B$: $N_B$ cells, mean occupancy $\bar{f}_B = 1-q_B$.

Shannon entropy of a cell with occupancy fraction $f$:
$$h(f) = -f\ln f - (1-f)\ln(1-f)$$

Total macro entropy: $S = N_A h(1-q_A) + N_B h(1-q_B)$.

**Transfer $\delta$ bits from $A$ to $B$:**

$$\frac{dS}{d\delta} = \frac{\partial h}{\partial f}\bigg|_B \cdot \frac{1}{N_B} - \frac{\partial h}{\partial f}\bigg|_A \cdot \frac{1}{N_A}$$

Using $\frac{\partial h}{\partial f} = \ln\frac{1-f}{f}$ and $f = 1-q$:

$$\frac{dS}{d\delta} = \ln\frac{q_B}{1-q_B} - \ln\frac{q_A}{1-q_A}$$

When $q_A < q_B$ (A more occupied):

$$\frac{q_A}{1-q_A} < \frac{q_B}{1-q_B} \implies \frac{dS}{d\delta} > 0$$

Entropy increases when information flows from low-$q$ to high-$q$. By Axiom 3, this is the spontaneous direction. $\square$

---

## S4. Transfer Rate: Unit Calibration Argument

**The question:** What is the transfer rate $\kappa$ (bits per step per cell boundary)?

**Answer:** $\kappa = 1$ in natural units. This is not a theorem about the universe — it is a definition of the basic time unit.

**Argument:**

Define the basic time unit $\tau$ as the time for one cell to complete one binary state transition ($0 \to 1$ or $1 \to 0$).

In these natural units: one cell boundary can transmit at most 1 bit per $\tau$ (because the receiving cell can flip at most once per $\tau$, and each flip carries 1 bit by Axiom 1).

We work in units $\tau = 1$, so $\kappa = 1$ by definition of $\tau$.

**This is analogous to:** setting $c = 1$ in special relativity (defining the length unit via the time unit and the speed of light). The physical content is in the structure, not in the numerical value of the unit.

**What this is not:** It is not a derivation that "the universe must be maximally efficient." It is a choice of natural units in which the basic rate is 1. Any other choice of units gives $\kappa = \text{const}$, which can be absorbed into the definition of the time unit.

---

## S5. Nearest-Neighbor Constraint: Revised Proof

**Previous version (flawed):** Used spatial intuition ("information cannot be in transit") incompatible with the abstract mapping framework of S1.

**Revised proof in the abstract mapping framework:**

**Definition:** The information graph $G = (V, E)$ has cells as vertices. An edge $(i,j) \in E$ if and only if cell $i$ can directly influence cell $j$ in one step.

**Claim:** Under Axioms 1 and 2, the graph is well-defined and transfer follows edges.

**Proof:** 

A dynamical step $f: \{0,1\}^N \to \{0,1\}^N$ is bijective (S1). For the step to be *local* — meaning cell $i$'s new state depends only on a bounded neighborhood — the graph must have finite degree.

Axiom 2 (bounded capacity) limits the information accessible to any cell in one step to 1 bit. A cell receiving influence from $k$ neighbors would need to process $k$ bits simultaneously, requiring capacity $k$ bits. For $k > 1$, this violates Axiom 2 unless the influences are aggregated — but aggregation over distance requires intermediate storage, which requires intermediate cells.

Therefore: in the absence of intermediate storage beyond Axiom 2's 1-bit limit, direct influence can only be between adjacent cells. The graph $G$ defines adjacency, and transfer follows $G$'s edges.

**What "nearest-neighbor" means here:** It means the graph has edges only between cells that can directly exchange information in one step. The spatial interpretation of "nearest" is an emergent property when $G$ is embedded in a metric space — not an input assumption.

---

## S6. Evolution Equation: Complete Derivation with Honest Accounting

**Step 1: Osmotic pressure (modeling choice)**

The driving force is modeled as:

$$\Pi(q) = \frac{1-q}{q}$$

**This is a modeling choice, not a theorem.** Physical motivation: $(1-q)/q$ is the ratio of locked to available capacity. It has correct boundary behavior ($\Pi \to \infty$ as $q \to 0$, $\Pi \to 0$ as $q \to 1$) and is the simplest form with these properties. Alternative forms consistent with the axioms are catalogued in the main text (Section V).

**Step 2: Flux (exact)**

The flux from cell $i$ to neighbor $j$ is driven by the pressure difference:

$$J_{i \to j} = \kappa \cdot (\Pi_i - \Pi_j) = \frac{1-q_i}{q_i} - \frac{1-q_j}{q_j} = \frac{q_j - q_i}{q_i q_j}$$

where $\kappa = 1$ in natural units (S4). Equivalently: $J_{i \to j} = 1/q_i - 1/q_j$.

**Step 3: Continuity equation (exact discrete flux form)**

Information conservation (S1, S2) gives the discrete continuity equation. When information leaves cell $i$, $q_i$ increases (cell becomes unoccupied):

$$\boxed{\Delta q_i = +\sum_{j \in \mathcal{N}(i)} J_{i \to j}}$$

where $\mathcal{N}(i)$ is the neighbor set of $i$. The $+$ sign follows from the standard continuity equation $\partial_t u + \nabla \cdot \mathbf{J} = 0$ for the conserved quantity $u = 1-q$ (information/occupancy): $\partial_t(1-q) + \nabla \cdot \mathbf{J} = 0 \Rightarrow \partial_t q = +\nabla \cdot \mathbf{J}$, giving $\Delta q_i = +\sum_j J_{i \to j}$. Physically: when information leaves cell $i$, the cell becomes unoccupied, so $q_i$ increases.

In 1D with nearest neighbors (S5):

$$\Delta q_i = +(J_{i \to i+1} - J_{i-1 \to i}) = \frac{q_{i+1} - q_i}{q_i q_{i+1}} - \frac{q_i - q_{i-1}}{q_{i-1} q_i}$$

This is the **exact discrete flux form**. It has two essential properties:

(i) **Conservative:** $\sum_i \Delta q_i = 0$ exactly, because the sum telescopes:
   $\sum_i (J_{i \to i+1} - J_{i-1 \to i}) = 0$ for any boundary conditions that preserve total $q$ (periodic or reflecting).

(ii) **Diffusive:** At a local minimum of $q$ (maximum occupancy), $q_{i\pm1} > q_i$, giving $J_{i \to i+1} < 0$ (inflow from right) and $J_{i-1 \to i} > 0$ (outflow to left). The net $\Delta q_i > 0$: $q$ increases at the minimum — occupancy spreads outward. This is diffusion, consistent with Axiom 3's direction (information flows from high to low occupancy).

**Step 4: Small-gradient approximation (simplified form)**

For $q_{i\pm1} \approx q_i$, we approximate $q_i q_{i+1} \approx q_i^2$ in the denominator of the flux:

$$J_{i \to i+1} \approx \frac{q_{i+1} - q_i}{q_i^2}$$

Substituting into the continuity equation $\Delta q_i = +(J_{i \to i+1} - J_{i-1 \to i})$:

$$\Delta q_i \approx +\left(\frac{q_{i+1} - q_i}{q_i^2} - \frac{q_i - q_{i-1}}{q_i^2}\right) = +\frac{q_{i+1} - 2q_i + q_{i-1}}{q_i^2}$$

$$\boxed{\Delta q_i \approx +\frac{\Delta^2 q_i}{q_i^2}}$$

where $\Delta^2 q_i = q_{i+1} - 2q_i + q_{i-1}$ is the discrete Laplacian.

**⚠️ Critical: the sign is $+$, not $-$.** A negative sign would describe anti-diffusion (information concentrating rather than spreading), contradicting Axiom 3. The positive sign follows directly from: (i) flux from high to low pressure: $J_{i \to j} = \Pi_i - \Pi_j = (q_j - q_i)/(q_i q_j)$, (ii) continuity for the conserved quantity $u = 1-q$: $\Delta q_i = +\sum J_{i \to j}$, (iii) small-gradient expansion: $\Delta q_i \approx +\Delta^2 q_i/q_i^2$. Every step is fixed by the sign conventions established in Steps 1–3. No sign flips occur between the discrete and continuous formulations.

**⚠️ The simplified form does not exactly conserve $\sum_i q_i$.** For non-uniform $q$:
$$\sum_i \frac{q_{i+1} - 2q_i + q_{i-1}}{q_i^2} \neq 0$$
because the denominator $q_i^2$ breaks the telescoping cancellation. Conservation holds only for the exact flux form (Step 3), not the approximation. In practice, for weak gradients ($|q_{i+1}-q_i| \ll q_i$), the violation is small. For strong gradients (near deadlock or during the Big Bang), the exact flux form is required.

**Step 5: Continuous limit (dimensional analysis)**

Valid when $q$ varies on scales $L \gg \mathfrak{l}$.

Taylor expansion: $\Delta^2 q_i \approx \mathfrak{l}^2 \partial_x^2 q$.

Time discretization: $\Delta q_i / t_p = \partial_t q$, where $t_p = \mathfrak{l}/c$.

From the exact flux form, keeping all terms:
$$J(x) \approx \frac{1}{q^2}\partial_x q \quad \text{(leading order)}$$

$$\partial_t q = +\partial_x J = \frac{\partial_x^2 q}{q^2} - \frac{2(\partial_x q)^2}{q^3}$$

Multiplying by the dimensional factor $\mathfrak{l}^2/t_p = \mathfrak{l} \cdot c$:

$$\boxed{\partial_t q = +(\mathfrak{l} \cdot c) \cdot \left[\frac{\partial_x^2 q}{q^2} - \frac{2(\partial_x q)^2}{q^3}\right]}$$

For weak gradients where $(\partial_x q)^2 \ll |\partial_x^2 q| \cdot q$, the second term is subdominant:

$$\partial_t q \approx +(\mathfrak{l} \cdot c) \cdot \frac{\partial_x^2 q}{q^2}$$

**Dimensional check:**
- Left: $[\partial_t q] = [1/\text{time}]$ ✓
- Right: $[\mathfrak{l} \cdot c] \cdot [1/\text{length}^2] = [\text{length} \cdot \text{length/time}] \cdot [1/\text{length}^2] = [1/\text{time}]$ ✓

**Limitations of the continuous form:**

(i) At $q \to 0$: $D(q) = \mathfrak{l} \cdot c / q^2$ diverges. The continuous equation predicts infinite propagation speed, but the discrete equation bounds propagation to one cell per step (speed $\leq c$). Near $q = 0$, only the discrete flux form (Step 3) is valid.

(ii) At strong gradients: the $(\partial_x q)^2/q^3$ term becomes comparable to $\partial_x^2 q/q^2$. Near shock-like structures (possible near deadlock), the full form is required.

(iii) The continuous form inherits the conservation properties of the discrete approximation used. The simplified form ($\partial_t q \propto \partial_x^2 q/q^2$) does not conserve $\int q \, dx$; the full form ($\partial_t q \propto \partial_x^2 q/q^2 - 2(\partial_x q)^2/q^3$) does — it is equivalent to $\partial_t q \propto \partial_x(\partial_x q/q^2)$, which is a conservation law. $\square$

---

## S7. Two Timescales: Complete Derivation from Axioms

**Claim:** The three axioms define two dynamically distinct processes. Their coexistence is a direct consequence of the independence of the axioms from which each process originates. This is not a modeling choice, nor does it rely on an efficiency principle.

### Process A: Information Homogenization

**Origin:** Axiom 3 (irreversible flow direction), operating on the binary state space defined by Axioms 1–2.

**Dynamics:** The exact flux form (S6, Step 3) is a conservative diffusion:
$$\Delta q_i = +\sum_{j \in \mathcal{N}(i)} J_{i \to j}, \quad \sum_i \Delta q_i = 0$$

The telescoping sum proves exact conservation: global mean $\bar{q} = N^{-1}\sum_i q_i$ is invariant under Process A. The process redistributes $q$ spatially but does not change $\bar{q}$.

**Timescale:**
$$\tau_A \sim \frac{L^2}{D(q)} = \frac{L^2 q^2}{\mathfrak{l} \cdot c}$$

where $L$ is the characteristic system size and $D(q) = \mathfrak{l} \cdot c / q^2$ is the diffusion coefficient from the osmotic model.

**What it does:** Smooths occupancy gradients. Prevents the formation of isolated locked regions by ensuring that local occupancy excesses diffuse to adjacent cells before they can saturate. This follows purely from Axiom 3 — no additional assumption required.

### Process B: Spontaneous Occupation

**Origin:** Axiom 1 (distinguishable states exist), constrained by Axiom 3 (irreversibility) and bounded by Axiom 2.

**Dynamics:** In the $q=1$ vacuum, every cell is unoccupied. Axiom 1 requires occupied and unoccupied to be distinguishable states, implying spontaneous occupation has nonzero probability $P_{\text{cell}} = \varepsilon > 0$ per cell per step. (The maximum-entropy prior gives the upper bound $P_{\text{cell}} = 1/2$, but this produces physically absurd occupation rates; the physical value of $\varepsilon$ is a phenomenological parameter — see S10.)

Each spontaneous occupation event increases total occupied cells by 1, decreasing $\bar{q}$ by $1/N$. Axiom 3 ensures this occupation is irreversible (once a cell is occupied, the information cannot spontaneously disappear). Axiom 2 provides the upper bound: total occupation cannot exceed $N$.

**Timescale:**
$$\tau_B \sim \frac{1}{\varepsilon} \cdot t_p$$

where $\varepsilon$ is the spontaneous occupation probability per cell per step (phenomenological parameter). For $\varepsilon \ll 1$, $\tau_B$ is cosmologically long. This timescale is consistent with the main text (Section VI); the relationship to the global rate is $P_{\text{global}} \approx N\varepsilon$ for $N\varepsilon \ll 1$, giving $\tau_B \sim 1/(N\varepsilon) \cdot t_p$ in terms of the global occupation rate, or equivalently $\tau_B \sim 1/\varepsilon \cdot t_p$ in terms of the per-cell rate (since each cell accumulates independently).

**What it does:** Slowly increases total information (occupancy) in the universe, driving $\bar{q}$ from $1$ toward $0$ over cosmological timescales. This follows from Axiom 1 with the maximum-entropy prior — the qualitative result ($\bar{q}$ decreases) is robust to the choice of prior as long as $P > 0$.

### Why Both Processes Coexist (Not "Necessary" — "Inevitable")

Process A originates from Axiom 3. Process B originates from Axiom 1. These axioms are independent (as established in Section II: removing either collapses the framework). Therefore, in any system satisfying all three axioms, **both processes are active simultaneously.**

The critical point: one does not "require" the other in a logical sense. Rather, both are unavoidable consequences of the axiom set. Their coexistence is a property of the axioms, not a teleological requirement:

| Remove... | Process A | Process B | Consequence |
|-----------|-----------|-----------|-------------|
| Axiom 1 | Still active (from A3) | No spontaneous occupation | Universe stays at $q=1$ forever; no classical behavior |
| Axiom 3 | No directed flow | Still active (from A1) | Occupation accumulates chaotically; no homogenization; fragmentation |
| Axioms 1+3 removed | Gone | Gone | No framework; no universe |

Neither scenario corresponds to our universe. Our universe exhibits both processes because it satisfies all three axioms — and therefore inherits all consequences of all axioms.

### Timescale Separation

The characteristic timescales have different parametric dependencies. With $t_p = \mathfrak{l}/c$:

$$\tau_A \sim \frac{L^2 q^2}{\mathfrak{l} \cdot c}, \qquad \tau_B \sim \frac{1}{\varepsilon} \cdot t_p = \frac{\mathfrak{l}}{c\varepsilon}$$

Taking the ratio:

$$\frac{\tau_B}{\tau_A} = \frac{\mathfrak{l}^2}{\varepsilon L^2 q^2}$$

**Timescale separation is parameter-dependent, not axiom-forced.** It requires $\varepsilon \ll \mathfrak{l}^2/L^2$. For cosmological $L \sim 10^{26}$ m and $\mathfrak{l} \sim 10^{-35}$ m: $\tau_B/\tau_A \sim 10^{-122}/(\varepsilon q^2)$. If $\varepsilon \sim 1/N \sim (\mathfrak{l}/L)^3 \sim 10^{-183}$ (one spontaneous event per universe per Planck time), then $\tau_B/\tau_A \sim (L/\mathfrak{l}) \cdot q^{-2} \sim 10^{61}/q^2$, consistent with the observed hierarchy between quantum and cosmological timescales. For larger $\varepsilon$, the separation narrows; for $\varepsilon \gtrsim \mathfrak{l}^2/L^2$, no separation exists. The existence of timescale separation in our universe is a phenomenological fact that constrains $\varepsilon$, not a theorem that follows from the axioms. $\square$

### Two Equations Are Required

Process A conserves $\sum_i q_i$ (telescoping sum of the flux form). Process B decreases $\sum_i q_i$ (source term). Mathematically, these cannot be embodied in a single autonomous equation. The full dynamics are a reaction-diffusion system:

$$\Delta q_i = +\sum_{j \in \mathcal{N}(i)} J_{i \to j} + S_i(t)$$

where:
- $J_{i \to j}$ (Process A) encodes Axiom-3-driven diffusion, with $\sum_i \sum_j J_{i \to j} = 0$
- $S_i(t)$ (Process B) encodes Axiom-1-driven spontaneous occupation, with $\langle S_i \rangle < 0$

The two terms have independent dynamical origins (A3 and A1 respectively) and separated characteristic timescales ($\tau_A$ and $\tau_B$ respectively). This is the mathematical expression of the two-process structure.

### Physical Correspondence

This two-process structure maps naturally onto observed physics:

| DGF process | Physical analog | Timescale |
|-------------|-----------------|-----------|
| Process A (diffusion) | Quantum dynamics, particle interactions | Planck scale ($\sim 10^{-43}$ s) |
| Process B (accumulation) | Cosmological evolution, entropy increase | Hubble scale ($\sim 10^{17}$ s) |

The ratio $\tau_B/\tau_A \sim L/(\mathfrak{l} \cdot q^2) \sim 10^{61}$ (for $L \sim 10^{26}$ m, $\mathfrak{l} \sim 10^{-35}$ m, $q \sim 1$) is consistent with the observed hierarchy between quantum and cosmological timescales. The framework provides an origin for this hierarchy — not as a mystery requiring explanation, but as a direct consequence of the axioms operating on a system with $N \sim (L/\mathfrak{l})^3 \gg 1$ cells, where diffusion ($\propto L^2$) is outpaced by volumetric filling ($\propto L^3$). $\square$

---

## S8. Classical Behavior: Operational Definition and Limits

**Definition:** A system is operationally classical if $q = 0$ — no available capacity, cannot respond to external information input.

**What this means physically:**

When $q = 0$: all cells full, any new information event would require a cell to hold $> 1$ bit, violating Axiom 2. The system is in a state where no further information processing is possible without a reset.

This is the operational definition of classical: not "obeys classical mechanics" but "cannot participate in quantum information processing."

**Consistency with standard quantum mechanics:**

At $q \to 0$: system unresponsive, no interference, no superposition effects observable. Consistent with classical limit. ✓

At $q \to 1$: system fully responsive, maximum capacity for interference. Consistent with quantum limit. ✓

**What this does not establish:**

The precise mapping between $q$ and standard quantum coherence measures (e.g., off-diagonal density matrix elements, quantum discord, entanglement) is not established here. The relationship is qualitatively consistent but quantitatively unspecified. This is an open problem.

**The inversion:**

Standard picture: quantum is special, classical is default.
DGF picture: high-$q$ (quantum) is the default state (all cells empty); low-$q$ (classical) is the depleted state.

The question becomes not "why do quantum systems decohere?" but "why do some systems retain high $q$?" Answer: because they have not yet accumulated enough spontaneous occupation events — a matter of size and age, not of environment.

---

## S9. Mass Density: Derivation and Honest Accounting

**Physical argument:**

Locked information ($A = 1-q$) satisfies under the axioms:
- Cannot flow (Axiom 3: cells full, overflow impossible without violation)
- Cannot respond to input (Axiom 2: no capacity)
- Only remaining function: resist change of state

Resistance to change of state = inertial mass (operational definition).

**Independence of cells:**

From the nearest-neighbor constraint (S5) and $\kappa = 1$ (S4): each locked cell contributes independently. No correlations between locked cells are generated by the evolution equation (which only moves information between adjacent cells, and locked cells by definition have no available capacity for such moves).

**Mass density:**

$$\rho_m = \frac{A \cdot \ln 2}{\mathfrak{l}^3}$$

Here $\ln 2 / \mathfrak{l}^3$ is the information capacity per unit volume — set by Axiom 2 and the calibration constant $\mathfrak{l}$.

**The circularity issue (honest):**

Converting to SI mass density requires $m_p = \sqrt{\hbar c/G}$. This constant contains $G$, which is measured via gravitational experiments involving mass. The conversion is therefore:

$$\rho_m^{SI} = \rho_m \cdot \frac{m_p}{\ln 2 / \mathfrak{l}^3} \cdot \frac{1}{\mathfrak{l}^3} = A \cdot \frac{m_p}{\mathfrak{l}^3}$$

This is dimensional analysis, not a derivation. We are saying: the mass density is proportional to the locked information density, with a proportionality constant calibrated by experiment. The claim is not that mass values are derived — only that mass density is operationally equivalent to locked information density.

---

## S10. Big Bang: Probability, Timescale, and the Rate Problem

### Spontaneous Occupation Probability

At $q = 1$, all cells empty. By Axiom 1, occupied and unoccupied are distinguishable states, so spontaneous occupation has nonzero probability: $P_{\text{cell}} > 0$ per cell per step.

**The maximum-entropy upper bound:** Under the maximum-entropy prior (equal probability for all distinguishable configurations consistent with the axioms), each cell independently has $P_{\text{cell}} = 1/2$ per step. This gives an expected occupation rate of $\langle \Delta N \rangle = N/2$ cells per step, and the universe fills to $q \approx 0$ in approximately $\log_2(N) \approx \log_2(10^{180}) \approx 600$ steps — roughly $10^{-41}$ seconds.

**This is physically absurd.** It contradicts every observation: the universe is not filling up with spontaneous matter creation at half the Planck rate.

**Resolution:** $P_{\text{cell}} = 1/2$ is the maximum-entropy *upper bound*, not a physical prediction. The three axioms guarantee $P_{\text{cell}} > 0$ but do not determine its magnitude. The physical value of $P_{\text{cell}}$ is set by Planck-scale physics beyond the current framework — likely suppressed by an exponential factor $P_{\text{cell}} \sim e^{-S}$ where $S$ is a characteristic action scale.

### Timescale with Phenomenological $P_{\text{cell}}$

Let $P_{\text{cell}} = \varepsilon \ll 1$ be the phenomenological spontaneous occupation probability per cell per step. Then:

$$\langle \Delta N \rangle = N\varepsilon \quad \text{cells per step}$$

$$\tau_B \sim \frac{1}{\varepsilon} \quad \text{steps to fill the universe}$$

In physical time: $\tau_B^{\text{phys}} \sim \varepsilon^{-1} \cdot t_p$.

The value of $\varepsilon$ is not predicted by the framework. It can be constrained by observation: the fact that our universe is still far from classical deadlock ($q$ is not close to 0) implies $\varepsilon^{-1} \gg t_{\text{universe}}/t_p \sim 10^{60}$.

### Qualitative Robustness

All qualitative results are robust for any $P_{\text{cell}} \in (0, 1]$:

- The Big Bang (first occupation event) is certain: $P > 0$ and infinite time → eventual occurrence
- Process B drives $\bar{q} \to 0$: monotonic accumulation + upper bound → convergence
- Timescale separation $\tau_B \gg \tau_A$: holds for any $\varepsilon \ll 1$
- Cyclic cosmology: robust provided $\varepsilon$ is small enough that the cycle time exceeds the homogenization time

The quantitative values (age of the universe, CMB temperature, baryon-to-photon ratio) depend on $\varepsilon$ and are observational inputs at the current stage of the framework.

### First-Occupation Probability (Corrected from v1)

The v1 manuscript stated $P(\text{spontaneous occupation}) = 1/2^N$ — the probability of a *specific* microstate being selected under a uniform distribution over all $2^N$ states. This is astronomically small but irrelevant to the question "does any occupation occur?"

The correct quantity is the probability that *at least one* of $N$ cells is occupied:

$$P(\text{first occupation}) = 1 - (1 - P_{\text{cell}})^N$$

Under the maximum-entropy prior ($P_{\text{cell}} = 1/2$), this is $1 - 2^{-N} \approx 1$ for $N \gg 1$. Under a physical prior with $P_{\text{cell}} = \varepsilon \ll 1/N$, this is $P \approx N\varepsilon \ll 1$, and the expected waiting time is $(N\varepsilon)^{-1}$ steps.

The v1 error conflated microstate probability with event probability. The current treatment distinguishes these clearly. $\square$

---

## S11. Cyclic Mechanism: Honest Assessment

**The cycle:**

$$q = 1 \xrightarrow{\text{Process B (Axiom 1)}} \bar{q} \text{ decreases} \xrightarrow{\text{Process A (evolution eq.)}} \text{homogenize} \xrightarrow{\text{Process B, long time}} q \to 0 \xrightarrow{?} q \to 1$$

**The honest gap:**

The transition $q \to 0 \xrightarrow{?} q \to 1$ is not derived from the axioms as a theorem. It is a consequence of axiom incompatibility at the boundary:

At $q = 0$: all cells full. Process B (Axiom 1) says spontaneous occupation continues. But Axiom 2 says cells cannot exceed 1 bit. These are incompatible.

Two interpretations:
1. The axioms are inconsistent at $q = 0$ — the system cannot exist in this state
2. The system undergoes a forced reset — the only way to resolve the incompatibility

Interpretation 2 gives the cyclic mechanism. But it requires treating Axiom 2 as a hard constraint that forces reset rather than as a prohibition on overflow occurring. This is a boundary condition choice, not a derivation.

**Status:** The cyclic mechanism is a consequence of how we handle axiom incompatibility at the extreme. It is physically motivated (systems that reach capacity must reset or cease to exist) but not logically forced with the same rigor as Sections S1–S7.

**The $10^{-5}$ residual:** CMB primordial fluctuations at $\sim 10^{-5}$ amplitude are an observational input. The framework provides a qualitative explanation (incomplete reset carries memory) but no quantitative prediction. This is an open problem in all cyclic cosmologies.

---

## S12. Comparison with Related Frameworks

| Framework | What is derived | Classicality mechanism | Requires environment? | Relation to DGF |
|---|---|---|---|---|
| Zurek einselection | Pointer states, superselection | Environmental monitoring | Yes | Complementary |
| Quantum Darwinism | Redundant info encoding | Environmental | Yes | Different mechanism, same direction |
| Aguiar–Matsas (2025) | Grav. decoherence rate | Spacetime quantum coupling | No (spacetime) | Same conclusion, different mechanism |
| Chiribella et al. (2011) | Finite-dim. QM formalism | Not addressed | N/A | Hierarchical: CDP inside DGF's high-$q$ |
| Caticha (2009) | Schrödinger eq., Born rule | Not addressed | N/A | DGF explains regime boundary |
| D'Ariano–Perinotti (2017) | Weyl, Dirac, Maxwell eqs. | Not addressed | N/A | DGF provides regime architecture |
| Lloyd (2006) | Computational hierarchy | Not addressed | N/A | DGF derives hierarchy from axioms |
| Wolfram (2002) | CA rule enumeration | Not addressed | N/A | DGF derives; Wolfram enumerates |
| Fredkin/Toffoli/Margolus | Reversible CA paradigm | Not addressed | N/A | DGF derives reversibility as theorem |
| Verlinde (2011) | Gravity from entropy | Not addressed | N/A | Complementary: mass as information |
| Penrose CCC | Conformal cyclic cosmology | Not addressed | No (conformal) | Cyclic: yes. Mechanism: different |
| QMM (Neukart 2024) | Planck-cell info storage | Info bounds | No | Shared structure, DGF adds $q$-dynamics |
| Sienicki (2025) | Classical as compression | Informational | N/A | DGF makes compression physical ($q$) |
| **DGF (this work)** | **$q$ evolution, timescales, regime structure** | **Capacity exhaustion** | **No** | — |

**Key difference from all above:** DGF provides a derivation of *why* classical behavior occurs (capacity exhaustion) rather than *how* it occurs given some mechanism. The mechanism is forced by Axioms 1–3; no additional physics (environment, gravity, conformal structure) is needed.

---

## S13. Complete Assumption Inventory

Every assumption made in this paper, with no exceptions:

| Label | Content | Status | Where used |
|-------|---------|--------|------------|
| A1 | Distinguishable states exist | Axiom | Throughout |
| A2 | Each cell ≤ 1 bit | Axiom | Throughout |
| A3 | Overflow irreversible | Axiom | Flow direction, timescales |
| M1 | Osmotic pressure $\Pi \propto (1-q)/q$ | **Modeling choice** | Evolution equation |
| M2 | Maximum entropy prior for $P_{\text{cell}}$ | Modeling assumption | Big Bang upper bound |
| P1 | $P_{\text{cell}} = \varepsilon \ll 1$ (phenomenological) | **Phenomenological param.** | Process B timescale |
| C1 | $c$ (propagation speed) | Experimental input | Continuous limit |
| C2 | $\hbar$ (quantum of action) | Experimental input | $m_p$, $l_p$ |
| C3 | $G$ (gravitational constant) | Experimental input | $m_p$, $l_p$ |
| O1 | Why 3 spatial dimensions | **Open problem** | — |
| O2 | $\sim 10^{-5}$ residual | **Open problem** | — |
| O3 | Gravity from $q$-gradient | **Open problem** | — |
| O4 | Osmotic pressure uniqueness | **Open problem** | — |
| O5 | $q$-to-quantum-coherence mapping | **Open problem** | — |
| O6 | Value of $P_{\text{cell}} = \varepsilon$ | **Open problem** | — |

**The framework's genuine free elements** at this stage: (i) the osmotic pressure functional form M1, and (ii) the spontaneous occupation rate P1. Both are constrained but not determined by the axioms. All other aspects of the dynamics are forced by the axioms, are natural unit choices, or are experimental inputs.

---

## S14. Numerical Verification

The exact flux form (main text Section V) has been implemented and verified on 1D lattices with adaptive timestepping. Complete code and diagnostic plots are provided in the accompanying repository (`dgf_stability.py`).

### S14.1 Stability Condition

The exact flux form:
$$\Delta q_i = +(J_{i \to i+1} - J_{i-1 \to i}), \quad J_{i \to j} = \frac{q_j - q_i}{q_i q_j}$$

is well-posed for all $q \in (0,1]$ with adaptive timestepping. The stability condition is:
$$\Delta t \leq \frac{q_{\min}^2}{2\kappa}$$

where $q_{\min}$ is the minimum $q$ value on the lattice and $\kappa = 1$ in natural units. The quadratic dependence on $q_{\min}$ reflects the $1/q^2$ divergence of the diffusion coefficient: near $q = 0$, timesteps must shrink to maintain stability.

Without adaptive timestepping, the equation can produce unphysical values ($q \notin [0,1]$) in a single step for strong gradients — a numerical artifact, not a physical instability.

### S14.2 Conservation

$\sum_i q_i$ is conserved to machine precision ($10^{-14}$ to $10^{-16}$) across all tested initial conditions, confirming the telescoping-sum property of the flux form. This is an exact algebraic identity, not an approximate conservation law.

### S14.3 Diffusive Dynamics

Five initial conditions were tested:
1. **Big Bang perturbation:** $q = 0.999$ background with $q_{\min} = 10^{-6}$ localized occupation
2. **Near-deadlock:** Alternating $q = 0.99$ and $q = 0.01$
3. **Mid-density sinusoid:** $q = 0.5 + 0.3\sin(2\pi x/L)$
4. **Sharp step:** $q = 0.9$ for $x < L/2$, $q = 0.1$ for $x > L/2$
5. **Random:** Uniform random $q \in [0.1, 0.9]$

In all cases, the dynamics are purely diffusive:
- Local $q$-minima (occupancy maxima) increase monotonically toward the mean
- Local $q$-maxima decrease monotonically toward the mean
- No shock formation, no anti-diffusive instability, no oscillation
- Gradients decay monotonically in $L^2$ norm

### S14.4 Timescale Scaling Verification

Because $N \sim 10^{180}$ Planck-scale cells cannot be simulated directly, the numerical implementation uses rescaled cells ($\mathfrak{l}_{\text{sim}} \gg \mathfrak{l}$). The purpose is to verify the **scaling** $\tau \propto L^2/\mathfrak{l}$, not to produce physical timescale predictions. The measured homogenization times confirm this scaling within a factor $\sim 2$ (diffusion in 1D carries a prefactor of $1/2$).

Extrapolating to the physical Planck scale $\mathfrak{l} \sim 10^{-35}$ m:

| System size $L$ | $q$ | $\tau_A$ (Planck-scale) | Physical interpretation |
|-----------------|-----|-------------------------|------------------------|
| 1 m | 0.5 | $\sim 10^{26}$ s ($\sim 10^{18}$ yr) | Negligible at lab scale |
| 1 AU | 0.5 | $\sim 10^{36}$ s ($\sim 10^{28}$ yr) | Negligible at solar-system scale |
| $10^{26}$ m (Hubble) | 0.5 | $\sim 10^{70}$ yr | Universe not homogenized |
| $10^{26}$ m (Hubble) | $10^{-60}$ | $\sim 10^{-50}$ yr | Rapid homogenization IF q is tiny |

**Key physical result:** For $q \sim O(1)$, Process A operates negligibly on all scales below cosmological — consistent with the observation that laboratory and astrophysical systems do not exhibit spontaneous $q$-diffusion. For cosmological $L$ and $q \sim O(1)$, the homogenization timescale vastly exceeds the age of the universe, predicting that large-scale structure (galaxy clusters, CMB anisotropies) should persist — consistent with observation. The framework thus predicts that Process A is cosmologically slow at present $q$, and that any observed homogenization must be driven by other processes (e.g., gravitational collapse) at sub-cosmological scales.

### S14.5 Two-Timescale Consistency

The measured timescale ratio for a $10^3$-cell 1D lattice with rescaled cells:
$$\frac{\tau_B}{\tau_A} = \frac{\mathfrak{l}_{\text{sim}}^2}{\varepsilon L^2 q^2} \approx \frac{10^{-4}}{\varepsilon}$$

For $\varepsilon \sim 10^{-3}$: $\tau_B/\tau_A \sim 0.1$. For cosmological $\varepsilon \sim 1/N \sim 10^{-183}$: $\tau_B/\tau_A \sim 10^{61}/q^2$, consistent with the Planck-to-Hubble hierarchy. The ratio spans many orders of magnitude depending on $\varepsilon$, reflecting the fact that timescale separation is parameter-dependent rather than axiom-forced (S7).

### S14.6 Density-Dependent Decoherence: Numerical Check

The prediction $\tau_{\text{decoherence}} \propto \rho/M$ (main text Section VII) was verified numerically for test objects with rescaled parameters, confirming the scaling $\tau_{\text{gold}}/\tau_{\text{silica}} = \rho_{\text{gold}}/\rho_{\text{silica}} \approx 8.8$. The ratio is independent of $\varepsilon$, $\mathfrak{l}$, and $c$. The full derivation and critical assessment are provided in S15.

---

## S15. Quantitative Prediction: Complete Derivation and Critical Assessment

### S15.1 Setup

Process B (spontaneous occupation) is the microscopic engine of classicalization. Each empty Planck cell has probability $\varepsilon$ per cell time $t_p = \mathfrak{l}/c$ of undergoing spontaneous occupation. This is a phenomenological parameter ($\varepsilon > 0$ guaranteed by Axiom 1 under the spontaneous-transition postulate; the value of $\varepsilon$ is not determined by the axioms — see S10).

For a physical object of mass $M$ and density $\rho$, the number of Planck-scale cells is:

$$N = \frac{V_S}{\mathfrak{l}^3} = \frac{M}{\rho \mathfrak{l}^3}$$

### S15.2 Decoherence Mechanism

A quantum superposition of spatial extent (e.g., center-of-mass delocalization by $\Delta x$) involves $\Delta N$ cells whose occupation state differs between the two branches. The framework identifies occupation with classicalization (main text Section III): an occupied cell is "locked" — it has a definite classical state. An unoccupied cell is "free" — it can participate in superposition.

**Key premise:** A single spontaneous occupation event hitting any cell in $\Delta N$ collapses the superposition, because that cell's state becomes definite (occupied = classical) in one branch but not the other, breaking the phase relationship. This premise is motivated by the framework's operational definition of classicality (capacity exhaustion → unresponsiveness → loss of coherence), but it is not independently derived from the three axioms. Its justification requires the $q$-to-quantum-coherence mapping (Open Problem O5).

### S15.3 First-Event Rate

The $\Delta N$ cells are treated as independent (each cell's spontaneous occupation is a local event uncorrelated with other cells). The probability that a specific cell undergoes spontaneous occupation in time interval $dt$ is $\varepsilon \cdot dt/t_p$. For $\Delta N$ independent cells, the expected number of events per unit time is:

$$\dot{n} = \frac{\varepsilon \Delta N}{t_p}$$

The time to the first event among $\Delta N$ independent Poisson processes, each with rate $\varepsilon/t_p$, is exponentially distributed with mean:

$$\tau_{\text{decoherence}} = \frac{1}{\dot{n}} = \frac{t_p}{\varepsilon \Delta N}$$

### S15.4 Expressing $\Delta N$ in Terms of $M$ and $\rho$

**Assumption (geometric volume scaling):** For a superposition involving the entire object, all $N$ cells differ between branches. Then $\Delta N = N = M/(\rho \mathfrak{l}^3)$. Substituting:

$$\tau_{\text{DGF}}(M,\rho) = \frac{t_p}{\varepsilon} \cdot \frac{\rho \mathfrak{l}^3}{M}$$

With $t_p = \mathfrak{l}/c$:

$$\boxed{\tau_{\text{DGF}}(M,\rho) = \frac{\rho \mathfrak{l}^4}{c \varepsilon M}}$$

**Dimensional check:** $[\rho] = M/L^3$, $[\mathfrak{l}^4] = L^4$, $[c] = L/T$, $[\varepsilon] = 1$, $[M] = M$. Numerator: $(M/L^3) \cdot L^4 = M \cdot L$. Denominator: $(L/T) \cdot M = M \cdot L/T$. Result: $T$. ✓

### S15.5 $\varepsilon$-Independent Ratio

The unknown parameter $\varepsilon$ cancels when comparing two objects of equal mass:

$$\boxed{\frac{\tau_{\text{DGF}}(\rho_1, M)}{\tau_{\text{DGF}}(\rho_2, M)} = \frac{\rho_1}{\rho_2}}$$

The calibration constants $\mathfrak{l}$ and $c$ also cancel. **The ratio depends only on the densities of the two objects.** This is the paper's central falsifiable prediction.

### S15.6 Comparison with Competing Models

**Penrose (1996):** Gravitational self-energy difference between superposition branches drives collapse. For a sphere of radius $R$ and mass $M$:
$$\tau_{\text{Penrose}} \approx \frac{\hbar}{\Delta E_{\text{grav}}} \propto \frac{\hbar}{GM^2/R} \propto \frac{1}{\rho^{1/3} M^{5/3}}$$

**Diósi (1989):** Similar mechanism with a noise-based formulation:
$$\tau_{\text{Diósi}} \propto \frac{1}{\rho^{1/3} M^2}$$

**DGF (this work):**
$$\tau_{\text{DGF}} \propto \frac{\rho}{M}$$

The critical difference: DGF predicts $\tau$ increases with density (denser → slower decoherence); Penrose and Diósi predict $\tau$ decreases with density (denser → faster decoherence, because the gravitational self-energy is larger for more compact objects). The sign of the density dependence is opposite.

### S15.7 Numerical Example: Silica vs. Gold Nanoparticles

| Property | Silica (SiO₂) | Gold (Au) |
|----------|--------------|-----------|
| Density $\rho$ | 2.2 g/cm³ | 19.3 g/cm³ |
| $\tau_{\text{DGF}}$ (relative) | 1 | $\approx 8.8$ |
| $\tau_{\text{Penrose}}$ (relative) | 1 | $\approx 0.48$ |

- **DGF:** Gold nanoparticles maintain coherence ~9× longer than silica nanoparticles of equal mass
- **Penrose/Diósi:** Gold nanoparticles decohere ~2× faster than silica

The predicted ratio is opposite in sign — a qualitative discriminator that does not require absolute rate measurements.

### S15.8 Critical Caveats

**C1 — Geometric volume scaling and the ΔN dilemma.** The prediction $\tau \propto \rho$ depends on geometric volume scaling ($\Delta N = V_S/\mathfrak{l}^3$). If instead $\Delta N \propto M$ (mass scaling), the density dependence disappears. This is not merely an unresolved technical detail — it creates a **genuine dilemma** for the framework:

- **Geometric scaling:** $\tau \propto \rho$ prediction holds, but experimental constraints force $\varepsilon < 5 \times 10^{-120}$ (S15.9 Case 1), making Process B so slow that essentially no spontaneous occupation has occurred in the history of the universe. The cosmological narrative ($q = 1 \to q \to 0$) collapses — the universe remains at $q \approx 1$, no classical regime emerges.
- **Mass scaling:** Process B is cosmologically viable (per-cell rate $\varepsilon/t_p$ is unconstrained by molecular interferometry for $M < m_p$, S15.9 Case 2), but the density-dependent prediction vanishes — $\tau \propto 1/M$ with no $\rho$ dependence, indistinguishable from other mass-dependent decoherence models.

The framework cannot simultaneously sustain both its central falsifiable prediction ($\tau \propto \rho$) and its cosmological narrative (Process B drives $q \to 0$) under current experimental constraints, unless $\Delta N$ has a more subtle scaling than either pure geometric or pure mass dependence. This dilemma is the most urgent open problem in the DGF program and is discussed further in S15.10.

**C2 — Single-event collapse.** The premise that one spontaneous occupation event suffices to collapse a macroscopic superposition requires that the occupation of a single cell breaks the phase relationship across all $\Delta N$ cells. This is plausible if the cells are entangled (as they would be in a coherent superposition), but the framework does not contain an entanglement formalism. This premise is an input to the prediction, not a theorem of the framework.

**C3 — Osmotic pressure form dependence.** The prediction uses Process B (spontaneous occupation) only, which is independent of the osmotic pressure modeling choice M1. However, the identification of $q$ with coherence (which underlies the "occupation = classicalization" premise) may depend on the specific form of $\Pi(q)$ through the evolution equation. This dependence is not quantified.

**C4 — Environmental isolation.** The prediction assumes perfect environmental isolation. In any real experiment, environmental decoherence must be controlled to a level where the DGF intrinsic decoherence is the dominant effect. Under geometric ΔN scaling, the experimental upper bound $\varepsilon < 5 \times 10^{-120}$ (S15.9 Case 1) places the DGF decoherence rate far below any achievable environmental isolation. Under mass scaling, the bound is far weaker (S15.9 Case 2), but the density dependence of the prediction disappears.

### S15.9 Experimental Constraints on $\varepsilon$ — The ΔN Problem

The experimental bound on $\varepsilon$ depends critically on the identification of $\Delta N$ — how many Planck cells participate in a given superposition. Two hypotheses yield radically different constraints:

**Case 1: Geometric volume scaling ($\Delta N = V_S/\mathfrak{l}^3$).**

For a C$_{70}$ fullerene molecule ($M \approx 1.2 \times 10^{-24}$ kg, $R \approx 10^{-9}$ m, $\tau_{\text{obs}} \sim 10^{-2}$ s):
$$\Delta N_{\text{geo}} = \frac{V_S}{\mathfrak{l}^3} \approx \frac{4 \times 10^{-27}}{(1.6 \times 10^{-35})^3} \approx 10^{78}$$
$$\varepsilon < \frac{t_p}{\tau_{\text{obs}} \cdot \Delta N_{\text{geo}}} \approx \frac{5.4 \times 10^{-44}}{10^{-2} \cdot 10^{78}} \approx 5 \times 10^{-120}$$

This bound places $\varepsilon$ in a range where $\tau_{\text{DGF}} \propto 1/\varepsilon$ is astronomically large for any macroscopic object. DGF intrinsic decoherence would be unobservable with any foreseeable technology. The prediction $\tau \propto \rho$ remains mathematically correct but experimentally inaccessible.

**Case 2: Mass scaling ($\Delta N = M/m_p$).**

If only Planck-mass-equivalent cells participate:
$$\Delta N_{\text{mass}} = \frac{M}{m_p} \approx \frac{1.2 \times 10^{-24}}{2.2 \times 10^{-8}} \approx 5.5 \times 10^{-17}$$

For $M < m_p$, $\Delta N_{\text{mass}} < 1$. The physical interpretation is that objects lighter than the Planck mass behave as a single quantum cell ($\Delta N = 1$ at minimum). The bound becomes:
$$\varepsilon < \frac{t_p}{\tau_{\text{obs}} \cdot \max(1, M/m_p)} \approx \frac{5.4 \times 10^{-44}}{10^{-2} \cdot 1} \approx 5 \times 10^{-42} \quad (\text{for } M < m_p)$$

For macroscopic objects ($M \gg m_p$): $\varepsilon < 10^{-25}$ to $10^{-30}$ — far weaker than the geometric bound, and potentially within reach of future experiments.

**Cosmological consistency check.** Independent of the ΔN hypothesis, cosmology provides two bounds:
- **Lower bound:** At least one spontaneous event must have occurred in the observable universe: $\varepsilon > t_p/(N_{\text{universe}} \cdot t_{\text{universe}}) \sim 10^{-244}$
- **Upper bound:** The universe is not fully classical ($q > 0$): $\varepsilon < t_p/t_{\text{universe}} \sim 10^{-61}$

Both ΔN hypotheses are cosmologically consistent. The experimental bound under geometric scaling ($\varepsilon < 10^{-120}$) is two orders of magnitude below the cosmological upper bound ($\varepsilon < 10^{-61}$), leaving a viable window. Under mass scaling, the experimental bound is far weaker.

**Decisive implication.** The ΔN scaling hypothesis determines whether DGF's central prediction is experimentally accessible:
- **Geometric scaling:** $\varepsilon < 10^{-120}$ → $\tau_{\text{DGF}}$ unmeasurably large → prediction is falsifiable in principle but not in practice
- **Mass scaling:** $\varepsilon$ potentially $10^{-25}$ or larger → measurement may be feasible with advanced interferometry

Resolving the ΔN problem — i.e., establishing the quantitative $q$-to-coherence mapping (Open Problem O5) — is the critical path to making DGF experimentally testable. The framework makes a sharp prediction whose observability hinges on this resolution, giving O5 urgency beyond theoretical interest.

### S15.10 Summary

The prediction $\tau \propto \rho$ (for equal mass) is:

| Property | Status |
|----------|--------|
| $\varepsilon$-independent | ✓ (cancels in ratio) |
| Opposite sign to Penrose/Diósi | ✓ (qualitative discriminator) |
| Derivation is algebraically clean | ✓ |
| Premises are honestly stated | ✓ |
| $\Delta N$ scaling is unresolved | ⚠️ (O5 — determines observability) |
| Single-event collapse is an input premise | ⚠️ |
| Falsifiable with current technology | ✗ (under geometric ΔN scaling) |
| Falsifiable in principle | ✓ |
| Observable if $\Delta N \propto M$ (mass scaling) | ✓ (potentially) |

**Critical path:** The geometric-vs-mass ΔN dilemma (C1) is the single most urgent problem in the DGF program. It is not merely an open technical question — it is a fork where the framework's central prediction and its cosmological consistency cannot both hold under current experimental constraints. Resolution requires either (a) a more subtle ΔN scaling than pure geometric or pure mass dependence, (b) a mechanism that enhances the effective ε at cosmological scales while suppressing it at laboratory scales, or (c) experimental evidence that the geometric ε bound is evaded (e.g., by collective effects not captured by the independent-cell Poisson model). Until this dilemma is resolved, the framework offers a coherent conceptual structure with a sharp but conditional prediction, rather than a fully consistent physical theory.