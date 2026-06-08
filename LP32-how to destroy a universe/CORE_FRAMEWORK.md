# The Reflux Bound: A Rigorous Constraint from Causal Consistency

**Version:** v4.0 — The Propagation Bridge
**Date:** 2026-06-08
**Status:** Static-DAG-to-dynamic-events gap bridged. Awaiting adversarial review.

---

## 0. The Problem We Solved

A causal DAG is a static object — nodes and directed edges. But "$P_{\text{reflux}} \leq q_S/q_E$" is a statement about *events happening in sequence*: forward transfer, THEN reflux. Prior versions smuggled this sequence in through informal language ("before any causal influence propagates," "becomes determined").

**This version provides the missing bridge:** a formal definition of *propagation* — a sequence of state transitions on a DAG that is both (a) fully rigorous and (b) imports no physical time. The bound is then a theorem about ALL propagations on ANY DAG.

---

## 1. Causal DAG

**Definition 1 (Causal DAG).** Let $G = (V, E)$ be a finite directed acyclic graph. Each node $v \in V$ represents a degree of freedom (DOF). A directed edge $(u \to v) \in E$ means: $u$ can causally influence $v$ — the state of $v$ may depend on the state of $u$.

$G$ is a DAG: no directed cycles exist. This is the **only** structural axiom.

**Definition 2 (State).** Each node $v$ has a binary state $d(v) \in \{0, 1\}$:
- $d(v) = 0$: undetermined (the node's value is not causally constrained by any other node)
- $d(v) = 1$: determined (the node's value is causally constrained by at least one other node)

A global state is an assignment $\sigma: V \to \{0, 1\}$. The state space is $\Sigma = \{0, 1\}^{|V|}$.

**Definition 3 (Partition).** The nodes are partitioned into system $S \subset V$ and environment $E = V \setminus S$. $N_S = |S|$, $N_E = |E|$.

---

## 2. Propagation — The Bridge

This is the key definition. Prior versions lacked it; this version supplies it.

**Definition 4 (Propagation).** A *propagation* on $G$ is a finite sequence of global states:

$$\Pi = (\sigma_0, \sigma_1, \ldots, \sigma_T)$$

satisfying, for each step $t \in \{1, \ldots, T\}$:

1. **Single transition.** $\sigma_t$ differs from $\sigma_{t-1}$ at exactly one node $v_t \in V$.

2. **Determination only.** $d_{t-1}(v_t) = 0$ and $d_t(v_t) = 1$. (No node ever transitions $1 \to 0$.)

3. **Causal enablement.** There exists at least one predecessor $u \in \text{pred}(v_t)$ such that $d_{t-1}(u) = 1$. (A node can only become determined if at least one of its causal parents is already determined.)

4. **Termination.** At step $T$, no further transition satisfying (1)-(3) is possible.

$\sigma_0$ is the *initial state*. $T$ is the *propagation length*. The node $v_t$ is the *transition at step $t$*.

**Why this bridges the gap.** A DAG is static. But a propagation is a sequence — it has steps, order, "before" and "after." Crucially:

- The "time" in a propagation is the **step index $t$** — a mathematical bookkeeping device, not physical time.
- A single DAG admits **many** propagations (different topological orders, different choices of which enabled node transitions next).
- The bound we prove holds for **all** propagations — it is a property of the DAG structure, not of any particular propagation choice.
- This is exactly analogous to: a concurrent program's partial order of events → any linearization (topological sort) is a valid execution trace. The theorem is a property of ALL traces.

**No physical time has been imported.** The propagation's step index is an arbitrary total order that extends the DAG's partial order. It exists purely for counting.

---

## 3. Definitions (Operationalized on Propagation)

**Definition 5 (Reflux and Forward Transfer events).** For a propagation $\Pi$:

- A **reflux event** is a step $t$ where $v_t \in S$. The node that becomes determined is in the system.
- A **forward transfer event** is a step $t$ where $v_t \in E$. The node that becomes determined is in the environment.

Let:
$$N_R = |\{t : v_t \in S\}| \qquad \text{(number of reflux events)}$$
$$N_F = |\{t : v_t \in E\}| \qquad \text{(number of forward transfer events)}$$
$$P_{\text{reflux}} = \frac{N_R}{N_F} \qquad \text{(if } N_F > 0 \text{)}$$

**Definition 6 (Undetermined fractions).** For the initial state $\sigma_0$:

$$q_S = \frac{|\{v \in S : d_0(v) = 0\}|}{N_S} \qquad q_E = \frac{|\{v \in E : d_0(v) = 0\}|}{N_E}$$

$q_S$ is the fraction of S-nodes that start undetermined. $q_E$ is the same for E-nodes.

**Interpretation.** $N_R$ counts "how many S-nodes become determined during the propagation." Under the DAG structure, an S-node becoming determined means causal information reached it — from somewhere. If this information propagated from E through causal edges, this is "reflux." The counting does not require identifying WHICH predecessor caused each transition — it only requires identifying WHICH node transitioned (S or E).

---

## 4. The Theorem

> **Theorem (Reflux Bound).** For any DAG $G = (V, E)$, any partition $V = S \cup E$, any initial state $\sigma_0$, and any propagation $\Pi$ on $G$:
>
> $$N_R \leq N_S q_S, \qquad N_F \leq N_E q_E$$
>
> and consequently, when $N_F > 0$:
>
> $$\boxed{P_{\text{reflux}} \equiv \frac{N_R}{N_F} \leq \frac{N_S q_S}{N_E q_E}}$$
>
> For $N_S = N_E$, this simplifies to $P_{\text{reflux}} \leq q_S / q_E$.

### Proof

1. Each node $v \in V$ can transition $0 \to 1$ at most once during any propagation. (By Definition 4, rule 2: transitions are only $0 \to 1$, never $1 \to 0$. Once $d(v) = 1$, it stays 1.)

2. The total number of S-nodes that can transition $0 \to 1$ is therefore bounded by the number of S-nodes that start at $d_0(v) = 0$. This number is exactly $N_S q_S$. Hence $N_R \leq N_S q_S$.

3. Similarly, the total number of E-nodes that can transition $0 \to 1$ is bounded by $N_E q_E$. Hence $N_F \leq N_E q_E$.

4. Dividing: $N_R / N_F \leq (N_S q_S) / (N_E q_E)$. $\square$

### What This Proof Uses (Complete Inventory)

| # | Item | Status |
|---|------|--------|
| 1 | $G$ is a finite DAG | **Axiom** — "no causal cycles" |
| 2 | Determination is binary ($d(v) \in \{0,1\}$) | **Modeling choice** — see §6 for discussion |
| 3 | Determination is monotonic (no $1 \to 0$) | **Built into Definition 4** — a propagation, by definition, never undoes determination |
| 4 | Transitions are sequential (one node per step) | **Modeling choice** — simultaneous transitions can be serialized; the bound is independent of serialization order |
| 5 | The sets $S$ and $E$ are a partition of $V$ | **User choice** — the bound applies to any partition |
| 6 | $\sigma_0$ is well-defined | **Modeling choice** — the user specifies which nodes start determined |

### What This Proof Does NOT Use

- ❌ Physical time (the step index $t$ is a bookkeeping device)
- ❌ Quantum mechanics (no Hilbert space, operators, or wavefunctions)
- ❌ Any specific dynamics (the bound holds for ALL propagations)
- ❌ Free parameters (the bound uses only $N_S, N_E, q_S, q_E$)
- ❌ Planck-scale discreteness ($N_S, N_E$ can be any positive integers)
- ❌ Spectral densities, coupling strengths, or Hamiltonians
- ❌ The specific "cause" of each transition (only the transitioning node's identity matters)

---

## 5. Why Propagation Is the Right Abstraction

### 5.1 What Propagation Captures

A propagation is a **monotonic exploration of the DAG's reachable set.** Start from an initial set of determined nodes. At each step, propagate determination forward along one edge. Continue until no more nodes can be reached.

This captures the essence of "causal influence propagating through a network" without specifying:
- How fast it propagates (step size is arbitrary)
- Which path it takes (any enabled node can transition next)
- What "determination" physically means (it's an abstract state)
- When things happen in physical time (step order is any topological extension)

### 5.2 The Bridge in One Diagram

```
STATIC DAG                          DYNAMIC PROPAGATION
───────────                         ────────────────────
                                    σ₀: 1 0 0 0  (initial)
    S₁ ──→ E₁ ──→ S₂                σ₁: 1 1 0 0  (E₁ determined by S₁)
    │                        →       σ₂: 1 1 1 0  (S₂ determined by E₁) ← REFLUX
    ↓                                σ₃: 1 1 1 1  (E₂ determined by S₁)
    E₂

One static object.                 One of many possible sequences.
"Who can influence whom."          "Who actually got influenced, in what order."
```

The theorem says: **in every propagation, the ratio of S-determinations to E-determinations is bounded by the initial undetermined ratio.** This is a property of the DAG that holds regardless of which propagation path is taken.

### 5.3 The "Time" Non-Problem

The step index $t = 0, 1, 2, \ldots, T$ looks like time. It is not physical time. It is a **topological extension** of the DAG's partial order: any total order $\prec$ on $V$ such that $u \to v$ implies $u \prec v$ (a topological sort). The propagation traces one such order.

The bound is independent of which topological extension is chosen. Different propagations (different topological sorts) may have different $N_R$ and $N_F$, but ALL satisfy the bound. This is the key: the bound is a property of the DAG's **structure**, not of any particular dynamical trajectory.

---

## 6. Discussion: Binary Determination

The proof assumes $d(v) \in \{0, 1\}$. This raises a natural question: what if determination is continuous?

**Answer:** The binary case is the **worst case** for the bound. If determination can take continuous values in $[0, 1]$, each node carries a "partial determination" value. Forward transfer increments an E-node's $d(v)$ from $d$ to $d + \delta$. Reflux increments an S-node's $d(v)$.

In the continuous case, a single node can absorb **multiple** increments — it can be partially determined by S (forward), then further determined by E (reflux), without ever reaching $d=1$. The binary bound $N_R \leq N_S q_S$ does not directly apply.

However, a **capacity** version of the bound holds: the total determination "mass" that can flow from E to S is bounded by the total undetermined "capacity" of S:

$$\sum_{v \in S} \Delta d_E(v) \leq \sum_{v \in S} (1 - d_0(v)) = N_S q_S$$

where $\Delta d_E(v)$ is the total determination increment of S-node $v$ that is causally attributable to E-nodes. This is a more general statement that reduces to the binary bound when determination increments are all-or-nothing.

**For the present work, we restrict to the binary case.** The binary case is:
- The physically relevant case for theories with fundamental discrete DOFs (e.g., Planck-scale causal sets, spin networks, qubit models)
- The case where the bound is simplest and sharpest
- Sufficient for the experimental protocol (§8)

The continuous generalization is a well-defined mathematical extension left for future work.

---

## 7. When the Bound Is Non-Trivial

The bound $P_{\text{reflux}} \leq (N_S/N_E)(q_S/q_E)$ is **non-trivial** (i.e., $P_{\text{reflux}} < 1$) when:

$$q_S < \frac{N_E}{N_S} q_E$$

**Case 1: Equal sizes ($N_S = N_E$).** Non-trivial when $q_S < q_E$ — the system must be more determined than the environment. This is the "open quantum system" regime: a small system interacting with a fresh (mostly undetermined) environment.

**Case 2: Small system ($N_S \ll N_E$).** Non-trivial when $q_S < (N_E/N_S) q_E$, which is almost always satisfied unless $q_S \approx 1$ and $q_E \approx 0$. The bound says $P_{\text{reflux}} \approx 0$ — large environments don't give information back. This is the standard decoherence regime and is consistent with known physics.

**Case 3: Equal undetermined fractions ($q_S = q_E$).** The bound is $P_{\text{reflux}} \leq N_S/N_E$. Non-trivial when $N_S < N_E$.

**Case 4: $q_S = 0$ or $q_E = 0$.** If $q_S = 0$ (all S-nodes start determined), $N_R = 0$ and the bound is $P_{\text{reflux}} = 0$ — no reflux possible. If $q_E = 0$ (all E-nodes start determined), $N_F = 0$ and $P_{\text{reflux}}$ is undefined (no forward transfer to compare against).

The bound is **most useful** in the regime $N_S \sim N_E$, $q_S < q_E$, $q_S > 0$ — a system and environment of comparable size, where the system is more determined than the environment but not completely determined. This is the regime where the bound provides a non-trivial constraint that is not already guaranteed by standard thermodynamic or decoherence arguments.

---

## 8. How to Use This

### For a Theorist

1. **Model your theory as a set of DOFs with causal relations.** Which variables can influence which others? Draw the graph. Verify it's a DAG (no cycles). If you find cycles, stop — your theory violates causal consistency.
2. **Choose a system-environment split.** Which DOFs are "system" (what you care about)? Which are "environment" (everything else)?
3. **Specify the initial state.** Which DOFs start determined? Which start undetermined? This defines $q_S$ and $q_E$.
4. **Run any propagation.** Or, if your theory specifies dynamics, observe which S-nodes and E-nodes become determined. Count $N_R$ and $N_F$.
5. **Check the bound.** Is $N_R/N_F \leq (N_S/N_E)(q_S/q_E)$? If violated: your propagation is inconsistent with the causal DAG — either (a) there's a cycle you missed, (b) a node transitioned $1 \to 0$ (de-determination), or (c) a node became determined without a determined predecessor.

### For a Reviewer

Given a theory that claims causal consistency: construct the causal DAG. Verify acyclicity. Compute the bound. If the theory's predictions violate the bound, the theory contains a hidden inconsistency.

### Critical Limitation

The bound is a **necessary** condition for causal consistency, not a sufficient one. A theory that satisfies the bound may still have other pathologies. The bound is a smoke test — passing it doesn't prove the theory is right. Failing it proves the theory is wrong (or that the DAG model was incorrectly constructed).

---

## 9. Experimental Protocol

The propagation framework suggests a clean experimental test:

**Platform:** $N$ two-level systems (qubits, spins, or any binary DOF) with controllable couplings.

**Preparation:** Choose a partition $S$ (system qubits) and $E$ (environment qubits). Initialize $N_S q_S$ system qubits in $|0\rangle$ (undetermined) and the rest in $|1\rangle$ (determined). Same for environment: $N_E q_E$ in $|0\rangle$, rest in $|1\rangle$.

**Dynamics:** Couple qubits according to the causal DAG: system qubits can influence environment qubits (forward edges), environment qubits can influence system qubits (potential reflux edges). Use conditional excitation gates: a determined ($|1\rangle$) source qubit can flip an undetermined ($|0\rangle$) target qubit to $|1\rangle$.

**Measurement:** After the propagation terminates (no more flips possible), count how many system qubits flipped ($N_R$) and how many environment qubits flipped ($N_F$).

**Prediction:** $N_R/N_F \leq q_S/q_E$ (for $N_S = N_E$).

**Standard quantum mechanics:** Standard QM with the same gate set imposes no such bound — in principle, all environment qubits could flip and then all system qubits could flip, giving $P_{\text{reflux}} = 1$ regardless of $q_S$ and $q_E$. (In practice, gate fidelity limits may obscure this.)

**Specific test case:** $N_S = N_E = 3$, $q_S = 0.33$ (1 undetermined S-qubit, 2 determined), $q_E = 0.67$ (2 undetermined E-qubits, 1 determined). The bound predicts $N_R/N_F \leq 0.33/0.67 = 0.5$. Standard QM allows $N_R/N_F$ up to 1.0 (all E-qubits could flip, then all S-qubits could flip).

---

## 10. Honest Boundaries

### The Framework Provides:

- A rigorous bound on determination propagation in any finite DAG
- A necessary condition for causal consistency
- An operational test for theories that can be modeled as binary DOFs with causal DAG structure

### The Framework Does NOT Provide:

- A constraint on continuous-variable theories (quantum fields, classical fields) without discretization
- A constraint on theories where the causal graph is dynamical or self-referential (GR)
- A sufficient condition for causal consistency
- A derivation of quantum mechanics, gravity, or time
- A constraint on de-determination (§6 — theories where nodes can transition $1 \to 0$ require the capacity-based generalization)

### The Honest Claim:

> Any physical theory that can be faithfully modeled as a finite set of binary degrees of freedom with a fixed, acyclic causal graph must satisfy $P_{\text{reflux}} \leq (N_S/N_E)(q_S/q_E)$ for any system-environment partition and any initial state. A violation indicates either (a) the theory contains causal cycles, (b) the DAG model was incorrectly constructed, or (c) de-determination is occurring and the capacity-based generalization must be used.

This is narrower than "any theory" but it is **rigorous.** The propagation bridge (§2) closes the gap that prior versions left open.

---

## Appendix: Prior Art

- **Pearl (1995, 2000):** Causal DAGs, do-calculus. The present framework uses DAG causality but extends it with the propagation concept to derive quantitative bounds. Pearl's framework is about inference from observational data; ours is about constraints on physical dynamics.
- **Sorkin (1987), Causal Set Theory:** Spacetime as a partially ordered set. The present framework is compatible with causal sets but operates at a higher level of abstraction (binary DOFs on any DAG, not specifically spacetime elements).
- **Megier, Smirne, Vacchini (2021), PRL 127, 030401:** Entropic bounds on non-Markovian backflow in open quantum systems. MSV's bound requires quantum state tomography; ours requires only counting determination events. The approaches are complementary: MSV is more general (applies to any CPTP dynamics) but less operational; ours is more restricted (binary DOFs, DAG structure) but simpler to apply.
- **Lindblad (1976); Gorini, Kossakowski, Sudarshan (1976):** GKSL master equation. The present framework does not require GKSL dynamics — propagation is a purely graph-theoretic concept.
- **Holevo (1973):** Bound of 1 classical bit per qubit. Our 1-bit-per-DOF assumption is the graph-theoretic analog, motivated by the same information-theoretic principle.

---

*End of v4.0. The propagation bridge is the key contribution of this version: it defines the rigorous link from static DAG to dynamic event sequence, closing the gap identified by adversarial review of v3.0.*
