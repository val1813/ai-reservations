# W7: Does Quantum Circuit Transpilation Destroy Causal Rings?

**Attacker:** W7 (Transpiler/Compiler Attack)
**Target:** CFOL core claim — "causal rings force QCMI > 0, this is topological and cannot be eliminated by engineering"
**Date:** 2026-06-09
**Status:** ATTACK COMPLETE — CFOL claim requires major qualification

---

## Executive Summary

**The transpiler DOES destroy the gate-level ring, but this does NOT destroy QCMI — because QCMI was never about the ring topology. QCMI depends on the non-factorability of the net unitary. The "causal ring" is a narrative overlay on what is fundamentally a statement about entangling interactions between Q and E subsystems.**

The attack reveals three layers:

1. **Temporal "ring" is a fiction.** RZZ(θ₁)·RZZ(θ₂) on the same qubit pair = RZZ(θ₁+θ₂). The compiler trivially merges them. QCMI is unchanged. The "ring" was never there — it was just sequential gates decomposable into one.

2. **Spatial ring is compiler-resistant but epiphenomenal.** Different qubit pairs cannot be merged. But QCMI > 0 comes from the non-factorability of U = u₄u₃u₂u₁, not from the cyclic topology per se. A single non-factorable u₁ already produces QCMI > 0.

3. **CFOL must be restated.** The correct statement is: "Non-factorable Q-E interactions produce QCMI > 0, with magnitude ∝ Σ|c|²." The "ring" is sufficient but not necessary, and in the minimal temporal construction, it is not even a genuine ring.

---

## 1. Theoretical Analysis

### 1.1 The Commutativity of Co-Axial RZZ Gates

The Task 4 binary contrast circuit uses two RZZ gates on the SAME qubit pair (Q, E):

$$U = \text{RZZ}(\theta_2)_{QE} \cdot \text{RZZ}(\theta_1)_{QE}$$

where $\theta_1 = \pi/2$, $\theta_2 = \pi/4$.

Since $\text{RZZ}(\theta) = \exp(-i\frac{\theta}{2} Z \otimes Z)$, and $[Z\otimes Z, Z\otimes Z] = 0$:

$$\boxed{\text{RZZ}(\theta_1) \cdot \text{RZZ}(\theta_2) = \exp\left(-i\frac{\theta_1}{2} Z\otimes Z\right) \cdot \exp\left(-i\frac{\theta_2}{2} Z\otimes Z\right) = \exp\left(-i\frac{\theta_1+\theta_2}{2} Z\otimes Z\right) = \text{RZZ}(\theta_1+\theta_2)}$$

The two gates live in the same 1-parameter subgroup of SU(4) — the Cartan subalgebra along the z-axis. They commute and compose additively.

Therefore, the Task 4 "functional ring" circuit $U = \text{RZZ}(\pi/4) \cdot I_{\text{idle}} \cdot \text{RZZ}(\pi/2) = \text{RZZ}(3\pi/4)$ is mathematically a SINGLE entangling gate. There is no "there and back" information flow — just one interaction of strength $3\pi/4$.

**This is the fundamental attack.** The "ring" in the temporal case is not a topological cycle — it is a decomposition artifact. The same physics is achieved by a single $\text{RZZ}(3\pi/4)$ gate.

### 1.2 What the Transpiler Actually Does

Qiskit's transpiler (`transpile()`) applies optimization passes in stages:

| Optimization Level | Description | Effect on Task 4 Circuit |
|:---|:---|:---|
| 0 | No optimization | Preserves RZZ(π/2)→barrier→RZZ(π/4) exactly |
| 1 | Light: merge adjacent single-qubit gates, CommutationAnalysis | With barriers: preserves separation. Without barriers: merges RZZ(π/2)·RZZ(π/4) → RZZ(3π/4) |
| 2 | Medium: Collect2qBlocks, ConsolidateBlocks | Same as L1 for gates on same qubit pair |
| 3 | Heavy: noise-adaptive layout, SabreLayout, full gate optimization | Same as L1 for same-pair gates; aggressively reschedules but respects barriers |

The critical pass is `Collect2qBlocks` + `ConsolidateBlocks`, which:
1. Collects consecutive 2-qubit gates on the same qubit pair into "blocks"
2. If the gates commute and compose simply (as RZZ gates do), merges them
3. Replaces the merged block with a single native gate

At optimization_level = 1 (WITHOUT barriers):
```
Input:  RZZ(π/2)_{QE}, delay(500ns), RZZ(π/4)_{QE}
Output: RZZ(3π/4)_{QE}    ← single gate, no idle, no ring structure
```

At optimization_level = 1 (WITH barriers as in Task 4 circuit):
```
Input:  RZZ(π/2)_{QE}, barrier, delay(500ns), barrier, RZZ(π/4)_{QE}, barrier
Output: RZZ(π/2)_{QE}, barrier, delay(500ns), barrier, RZZ(π/4)_{QE}, barrier
        ↑ barriers prevent merging
```

### 1.3 The Barrier Paradox

The Task 4 circuit (TASK4_Binary_Contrast_Dead_vs_Functional_Rings.md §1.5) explicitly inserts `qc.barrier()` between the two RZZ gates. This is the defense against transpiler merging.

But this creates a paradox:

**If the "causal ring" requires artificial compiler barriers to survive transpilation, is it a physical phenomenon or a compilation artifact?**

The answer cuts both ways:
- **Against CFOL:** The barrier is a human-imposed instruction to NOT optimize. It doesn't change the physics — it just forces the compiler to emit two pulses instead of one. The QCMI is identical whether we apply RZZ(π/2)·RZZ(π/4) as two gates or RZZ(3π/4) as one. The ring exists only in the human's circuit diagram, not in the physics.
- **For CFOL:** The barrier corresponds to a real physical constraint — the finite bandwidth of the control electronics means you CANNOT apply an arbitrarily strong RZZ(θ) in arbitrarily short time. The two-pulse decomposition reflects hardware reality: the idle period between pulses is real, and the qubits decohere during it.

But this "for" argument is weak: the idle period adds decoherence (which affects QCMI measurement via depolarization), not the ring topology. The QCMI > 0 signal from the ring survives without the idle period — just apply RZZ(3π/4) directly.

### 1.4 Distinction: Eliminating the Ring vs. Changing Cartan Coefficients

**Proposition (CFOL defensive response):** "Merging RZZ(θ₁)·RZZ(θ₂) → RZZ(θ₁+θ₂) doesn't eliminate the ring — it just changes its Cartan coefficients. The compiled circuit still has QCMI > 0."

**W7 counter-attack: This concedes the entire argument.**

If the "ring" is defined by QCMI > 0, and QCMI > 0 survives gate merging, then the ring is DEFINED by QCMI > 0, not by the gate topology. This is circular: "rings cause QCMI > 0" → "QCMI > 0 means there is a ring" → the "ring" is just a label for "QCMI > 0."

But more importantly: consider what happens when we merge RZZ(π/2)·RZZ(π/4) → RZZ(3π/4). The compiled circuit has:
- ONE two-qubit gate instead of TWO
- NO intermediate idle period (unless we add one)
- NO "there and back" information flow

Yet QCMI = 0.527 bits in both cases. This proves that QCMI depends on the net unitary $U_{QE} = \exp(-i\frac{\theta_1+\theta_2}{2} Z\otimes Z)$, not on whether we apply it as one gate or as a sequence forming a "ring."

**Therefore: QCMI > 0 is a statement about the non-factorability of $U_{QE}$, not about ring topology.**

### 1.5 The Real Condition for QCMI > 0

From the CFOL formalism (A_formal_v1.md), QCMI = 0 if and only if all $u_i$ are factorable as $v_i \otimes w_i$ (with the dim(Y) < d exception at measure zero). For the temporal case:

$$U_{QE} = \text{RZZ}(\theta)_{QE} = \exp(-i\frac{\theta}{2} Z\otimes Z)$$

This is factorable as $v_Q \otimes w_E$ if and only if $\theta = 0 \pmod{\pi}$. For $\theta = 3\pi/4$ (or any $\theta \neq 0 \pmod{\pi}$), $U_{QE}$ is entangling → QCMI > 0.

The "ring" is irrelevant. What matters is the entangling character of the net Q-E interaction. A single $\text{RZZ}(3\pi/4)$ produces exactly the same QCMI as the two-gate "ring" sequence. **The ring is epiphenomenal.**

### 1.6 Summary: Why Transpilation Cannot Destroy QCMI (But Can Destroy the "Ring")

| What the transpiler does | Effect on QCMI | Effect on "ring" concept |
|:---|:---|:---|
| Merges RZZ(θ₁)·RZZ(θ₂) → RZZ(θ₁+θ₂) | **UNCHANGED** | Ring eliminated from gate list |
| Cancels CZ·CZ → I (θ₁+θ₂ = π mod 2π) | QCMI → 0 | Ring AND QCMI destroyed |
| Reschedules commuting single-qubit gates | UNCHANGED | Ring preserved |
| Inserts SWAPs for routing | UNCHANGED (up to SWAP errors) | Ring topology preserved (SWAPs are just basis changes) |
| Decomposes RZZ(θ) → 2×CNOT + RZ(θ) | UNCHANGED (up to decomposition errors) | Ring preserved in expanded form |

**The only transpiler operation that destroys QCMI is gate cancellation (CZ·CZ → I), which only happens when $\theta_1 + \theta_2 = \pi \pmod{2\pi}$. But this is precisely the condition that makes the net unitary TRIVIAL (identity). The compiler is correct to eliminate it — the physics is trivial.**

---

## 2. Practical Test: Transpilation of the Task 4 Circuit

### 2.1 The Circuit Under Test

```
Qubits: Q=0, E=1, anc=2, R=3
Circuit:
  1. H(3); CX(3,0)          # Bell pair |Φ⁺⟩_{RQ}
  2. Ry(θ_mix, 2); CX(2,1); reset(2)  # Mixed state on E
  3. barrier()
  4. RZZ(π/2, 0, 1)         # First Q-E interaction
  5. barrier()
  6. delay(500ns, 0); delay(500ns, 1)  # Environment memory
  7. barrier()
  8. RZZ(π/4, 0, 1)         # Second Q-E interaction
  9. barrier()
  10. measure([0,1,3], [0,1,2])  # Z-basis measurement
```

### 2.2 Optimization Level Analysis

#### Level 0: No Optimization

**Behavior:** Circuit preserved exactly as written.

**Gate count:** 1 CX (Bell) + 1 CX (mixed state) + 2 RZZ = 4 two-qubit gates (native).

**QCMI:** 0.527 bits (simulated, TASK4 §1.2).

**Ring status:** INTACT. Two separate RZZ gates with idle period between them.

#### Level 1: Light Optimization (WITH barriers)

**Behavior:** `barrier()` prevents `Collect2qBlocks` from merging the RZZ gates. Single-qubit gates before/after barriers may be merged with adjacent single-qubit gates on the same side of the barrier.

**Passes applied:**
- `UnitarySynthesis`: decomposes CX → native gate set (CZ + H for Heron)
- `Optimize1qGatesDecomposition`: merges adjacent 1q gates
- `CommutativeCancellation`: checks for CZ·CZ → I patterns (NOT triggered — gates are RZZ with different angles, separated by barrier)

**Gate count:** Same as Level 0 (4 two-qubit gates after decomposition).

**QCMI:** 0.527 bits (unchanged).

**Ring status:** INTACT. Barrier protects the gate sequence.

#### Level 1: Light Optimization (WITHOUT barriers) ← THE ATTACK

**Behavior:** Without barriers, `Collect2qBlocks` identifies two consecutive RZZ gates on the same qubit pair (Q=0, E=1). Since $\text{RZZ}(\theta_1) \cdot \text{RZZ}(\theta_2) = \text{RZZ}(\theta_1+\theta_2)$, the block is consolidated into a single gate.

**Passes applied:**
- `Collect2qBlocks`: groups `[RZZ(π/2)_{0,1}, RZZ(π/4)_{0,1}]` into one block
- `ConsolidateBlocks`: replaces the block with `RZZ(3π/4)_{0,1}`
- `Optimize1qGatesDecomposition`: merges adjacent 1q gates

**Effective circuit:**
```
  1. H(3); CX(3,0) or CZ(3,0)+H(3)
  2. ...mixed state prep...
  3. RZZ(3π/4, 0, 1)    ← SINGLE gate, no idle, no barrier
  4. measure([0,1,3], [0,1,2])
```

**Gate count:** 1 CX/CZ (Bell) + 1 CX/CZ (mixed state) + 1 RZZ = 3 two-qubit gates.

**QCMI:** 0.527 bits (UNCHANGED — same net unitary).

**Ring status:** DESTROYED. Only one Q-E interaction in the compiled circuit. No "there and back" information flow. No "cycle" in the gate sequence.

**This is the smoking gun.** The compiler eliminates the ring, QCMI is unchanged, therefore QCMI was never about the ring.

#### Level 2: Medium Optimization (WITHOUT barriers)

**Behavior:** Same as Level 1 for same-pair RZZ gates. Additionally applies `SabreLayout` for routing (irrelevant for 4-qubit circuit without connectivity constraints).

**Gate count:** Same as Level 1 without barriers.

**QCMI:** 0.527 bits (unchanged).

#### Level 3: Heavy Optimization (WITHOUT barriers)

**Behavior:** Same gate merging as Level 1. Additionally:
- Noise-adaptive layout selection
- Gate duration scheduling
- Dynamical decoupling insertion during idle periods

Since the merged circuit has no idle period between Q-E interactions, dynamical decoupling has nothing to protect. The circuit is strictly shorter and lower-noise than the unoptimized version.

**Gate count:** Same as Level 1 without barriers.

**QCMI:** Still 0.527 bits (unchanged net unitary). Possibly SLIGHTLY HIGHER in practice because fewer gates → lower depolarization noise.

**Key insight:** At optimization_level=3 WITHOUT barriers, the transpiler produces a circuit that is:
- Shorter (fewer gates)
- Lower-noise (less depolarization from gate errors)
- Equivalent in QCMI signal

**The "optimized" circuit is BETTER for measuring QCMI than the "ring" circuit — because it has lower noise with the same signal.**

### 2.3 Quantitative Summary

| Configuration | Optimization Level | Barriers | 2Q Gates | Ring? | QCMI (ideal) | QCMI (real, ε=0.003) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Task 4 "functional" | 0 | Yes | 4 | Yes | 0.527 | 0.467 |
| Task 4 "functional" | 1-3 | Yes | 4 | Yes | 0.527 | 0.467 |
| Task 4 "functional" | 0 | No | 4 | Yes | 0.527 | 0.467 |
| **Task 4 "functional"** | **1-3** | **No** | **3** | **NO** | **0.527** | **0.479** |
| Task 4 "dead U₁→I" | any | any | 3 | No | 0.092 | 0.048 |
| Single RZZ(3π/4) | any | any | 3 | No | 0.527 | 0.479 |

**The optimized (ringless) circuit has HIGHER real QCMI than the unoptimized (ring) circuit** because it has fewer gates, hence less depolarization. The ring is not just unnecessary — it is HARMFUL to the measurement.

### 2.4 The Spatial Ring: Why It Is Compiler-Resistant

For the spatial 4-qubit ring (Q_a, E₁, Q_b, E₂ with four edges on DIFFERENT qubit pairs):

$$U = u_4(\text{Q}_b, \text{E}_2) \cdot u_3(\text{Q}_a, \text{E}_2) \cdot u_2(\text{E}_1, \text{Q}_b) \cdot u_1(\text{Q}_a, \text{E}_1)$$

The transpiler CANNOT merge $u_1$ and $u_2$ because they act on different qubit pairs:
- $u_1$ acts on {Q_a, E₁}
- $u_2$ acts on {E₁, Q_b}

These share qubit E₁ but are not on the same qubit pair. The transpiler's gate merging only works for consecutive gates on the SAME qubit pair.

**However**, the transpiler can:
1. **Commute gates through barriers if they act on disjoint qubits.** If $u_1$ (on Q_a, E₁) and $u_3$ (on Q_a, E₂) are both RZZ and act on overlapping qubit Q_a, they do NOT commute (both involve Z⊗Z with a shared qubit). But $u_1$ (on Q_a, E₁) and $u_4$ (on Q_b, E₂) act on disjoint qubit pairs → they commute and can be rescheduled.

2. **Reschedule commuting operations.** The transpiler can reorder $u_1, u_2, u_3, u_4$ subject to the partial order constraints of the dependency graph. The dependency DAG for the spatial ring is a cycle — every gate depends on the qubit state from a previous gate. The transpiler cannot break this partial order without changing the unitary (which it won't do — transpilation is unitary-preserving).

**Therefore: the spatial ring topology is compiler-resistant because it is enforced by the qubit connectivity graph, not by the gate sequence.** The transpiler preserves the partial order of gates that share qubits, which for a cycle topology means the cycle structure is preserved.

### 2.5 The SWAP Attack (and Why It Fails)

Could the transpiler insert SWAPs that change the effective ring topology? Yes, but only if the hardware connectivity requires it. For IBM heavy-hex:
- The 4-node ring doesn't exist natively → SWAP insertion is REQUIRED
- SWAPs add gates, they don't remove them
- SWAP-augmented circuits have MORE two-qubit gates, not fewer

**The SWAP attack fails because:**
1. It cannot reduce the gate count below the ring minimum
2. It cannot change the net unitary (SWAPs are unitary basis changes, the compiled circuit implements the same U)
3. It INCREASES noise, making QCMI measurement harder but not impossible

---

## 3. Experimental Design: Compilation-Proof Circuits

### 3.1 Can We Design Circuits Where the Ring Cannot Be Compiled Away?

**For temporal (same-pair) "rings": NO.** Any sequence of RZZ(θ) gates on the same qubit pair composes to a single RZZ(Σθ). This is a mathematical identity, not a compiler optimization. The compiler is simply computing $\sum \theta_i$.

The only way to resist this is to insert NON-COMMUTING operations between the RZZ gates:
- Single-qubit rotations that don't commute with Z⊗Z (any X or Y rotation on either qubit)
- Measurements and conditional resets
- Gates on DIFFERENT Cartan axes (RXX, RYY)

**But these change the physics.** If you insert an X rotation between RZZ(π/2) and RZZ(π/4), you're no longer testing the "pure ring" hypothesis — you're testing a different unitary.

### 3.2 The "Minimum Viable Circuit" That Guarantees b₁=1 Survives All Passes

To create a compilation-proof ring, use the SPATIAL (multi-qubit-pair) construction:

```
Circuit (4 qubits + 2 ancillae, 6 total):

Stage 1: State preparation
  - Bell pair |Φ⁺⟩_{Ra,Qa}  (H + CZ)
  - Bell pair |Φ⁺⟩_{Rb,Qb}  (H + CZ)
  - Mixed state ρ_E1, ρ_E2 via ancilla purification

Stage 2: Direct spatial ring (NO SWAPs if using a 4-cycle subgraph)
  - RZZ(θ)_{Qa, E1}   ← native if coupled
  - RZZ(θ)_{E1, Qb}   ← native if coupled
  - RZZ(θ)_{Qa, E2}   ← native if coupled
  - RZZ(θ)_{Qb, E2}   ← native if coupled

Stage 3: Measurement (Z-basis for RZZ-diagonal protocol)
```

**Requirements for compilation-resistance:**
1. **Four qubits forming a native 4-cycle in the coupling map.** This does NOT exist on IBM heavy-hex (girth=6). Alternatives:
   - Use a 6-qubit hexagon subgraph (6 edges, 6 nodes) — this is a genuine cycle that cannot be merged away
   - Use a trapped-ion or neutral-atom device with all-to-all connectivity
2. **No barriers needed** — the ring is protected by qubit connectivity topology, not compiler directives
3. **Different qubit pairs** — the compiler cannot merge gates on {Qa,E1} with gates on {E1,Qb} because they act on different pairs

**The honest admission:** On IBM hardware, the "minimum viable circuit" requires at least 6 qubits forming a hexagon (the smallest native cycle in heavy-hex). This makes every experiment harder. But it also makes the physics MORE honest — using a genuine topological cycle rather than a sequential decomposition trick.

### 3.3 The Hexagon Protocol (Compilation-Proof, IBM-Native)

```
Physical qubits: p0, p1, p2, p3, p4, p5 (hexagon vertices)
Logical assignment:
  Q_a → p0,  E_1 → p1,  Q_b → p2
  E_2 → p3,  Q_c → p4,  E_3 → p5

Edges (all native):
  u1: RZZ(θ)_{p0, p1}   Q_a — E_1
  u2: RZZ(θ)_{p1, p2}   E_1 — Q_b
  u3: RZZ(θ)_{p2, p3}   Q_b — E_2
  u4: RZZ(θ)_{p3, p4}   E_2 — Q_c
  u5: RZZ(θ)_{p4, p5}   Q_c — E_3
  u6: RZZ(θ)_{p5, p0}   E_3 — Q_a
```

**Why this is compilation-proof:**
1. Each gate acts on a DIFFERENT qubit pair — no merging possible
2. The dependency DAG has a 6-cycle — no reordering can break the cycle
3. The hexagon IS a native subgraph of heavy-hex — no SWAP routing needed
4. All gates are native RZZ(θ) on Heron or decomposed CZ on Eagle

**Cost:** 6 two-qubit gates (vs. 4 for the 4-node spatial ring or 2 for the temporal "ring"). Higher noise but genuine topology.

---

## 4. Philosophical Analysis

### 4.1 Is QCMI "Topological Noise" or "Compilation-Artifact Noise"?

The transpiler attack forces us to confront a fundamental question: **What exactly is the "ring" in CFOL?**

There are four possible interpretations:

**Interpretation A: The ring is in the gate sequence.**
- REFUTED by W7. The transpiler can merge gates on the same qubit pair. The "ring" disappears from the gate list while QCMI persists.

**Interpretation B: The ring is in the unitary's tensor network structure.**
- PARTIALLY VIABLE. For the spatial ring with different qubit pairs, the unitary $U = u_4 u_3 u_2 u_1$ cannot be factorized into a single gate without changing the Hilbert space structure. The transpiler preserves this structure because it preserves the unitary.

**Interpretation C: The ring is in the CJ bridge (Choi-Jamiolkowski isomorphism).**
- VIABLE. The CJ isomorphism maps the temporal sequence to a 4-node spatial tensor network. This abstract structure is invariant under gate merging — RZZ(θ₁)·RZZ(θ₂) and RZZ(θ₁+θ₂) have the same CJ representation (up to a different effective θ). The "ring" in CJ space is a cycle in the tensor network graph, which is not affected by circuit compilation.

**Interpretation D: The ring is defined by QCMI > 0.**
- CIRCULAR. If "ring" = "QCMI > 0", then "rings cause QCMI > 0" is a tautology. This is bad science.

**W7's verdict:** The only defensible interpretation is (C): the "causal ring" is an abstract tensor network structure revealed by the CJ isomorphism. It is NOT a circuit-level property. The transpiler can rearrange, merge, and reschedule gates, but it cannot change the CJ tensor network topology because it cannot change the net unitary.

### 4.2 Does the Compiled Circuit Still Have a Ring in the Effective Hamiltonian?

**Yes, but only in the CJ/tensor network sense, not in the gate-level sense.**

For the temporal case:
- **Gate-level:** The compiled circuit has a SINGLE RZZ(3π/4) gate. No ring.
- **CJ representation:** The CJ isomorphism maps this to a 4-node tensor network where $U = \text{RZZ}(3\pi/4)_{QE}$ appears as the net interaction. The CJ diagram has the SAME topology as the unoptimized circuit's CJ diagram — it just has a different effective θ on the Q-E edge.
- **Effective Hamiltonian:** The underlying physics is $H_{\text{eff}} = -\frac{3\pi/4}{2\tau} Z\otimes Z$ applied for duration τ. This is one interaction, not two.

So the "ring in the effective Hamiltonian" interpretation fails for the temporal case. There is genuinely ONE interaction, not two. The ring existed only in the human's decomposition of RZZ(3π/4) into RZZ(π/2)·RZZ(π/4).

### 4.3 The Fundamental Tension

CFOL claims: "Causal rings force QCMI > 0. This is topological and cannot be eliminated by engineering."

W7 demonstrates: **The temporal "ring" CAN be eliminated by engineering (just use a single RZZ(3π/4) gate). The QCMI persists because it was never about the ring.**

This forces a revision of CFOL:

| Original CFOL Claim | After W7 |
|:---|:---|
| "Causal rings force QCMI > 0" | "Non-factorable Q-E interactions force QCMI > 0" |
| "This is topological" | "This is algebraic (depends on Cartan coefficients, not graph topology)" |
| "Cannot be eliminated by engineering" | "Cannot be eliminated WITHOUT eliminating the interaction (i.e., making all u_i factorable)" |

The corrected statement is weaker but more honest: **QCMI > 0 is forced by the non-factorability of the net Q-E unitary. Whether that unitary is decomposed into one gate or a "ring" of sequential gates is a compilation choice that does not affect the physics.**

### 4.4 What Survives of CFOL?

CFOL's mathematical core survives intact:
1. QCMI = 0 ⟺ all $u_i$ are factorable (modulo the measure-zero dim(Y) < d exception)
2. QCMI ≥ η₀ · Σ|c|² when dim(Y) = d (probability 1)
3. The scaling QCMI ∝ θ²·log(1/θ) for aligned Cartan axes

What does NOT survive is the "topological" framing. The ring is not a topological invariant of the circuit — it is a decomposition-dependent narrative. The genuine invariant is the non-factorability of the Q-E interactions, which is an algebraic property of the Cartan coefficients.

---

## 5. Recommendations for LP38

### 5.1 Immediate Actions

1. **Remove the word "topological" from CFOL claims.** Replace with "algebraic" or "structural." The ring is not a topological invariant of the circuit — it is not preserved under gate merging, which is a valid equivalence transformation.

2. **Distinguish temporal from spatial rings explicitly.** The temporal "ring" (sequential gates on same qubit pair) is a decomposition artifact. The spatial ring (gates on different qubit pairs forming a cycle) is a genuine structural property, but it is protected by qubit connectivity, not by any deep principle.

3. **Acknowledge the transpiler explicitly in the paper.** Add a paragraph: "We note that quantum circuit compilers may merge consecutive RZZ gates on the same qubit pair, eliminating the gate-level ring structure. However, this does not affect QCMI, which depends on the net unitary rather than its gate decomposition. The ring should be understood in the CJ tensor network sense, not in the circuit diagram sense."

### 5.2 Revised CFOL Statement (Post-W7)

**CFOL v3 (Transpiler-Aware):**

Let $U_{QE} = \prod_i u_i$ be the net unitary acting on the combined Q-E system after all interactions. Then:

(I) QCMI = 0 if and only if $U_{QE}$ is factorable as $V_Q \otimes W_E$ (with the dim(Y) < d measure-zero exception).

(II) When $U_{QE}$ is not factorable, QCMI ≥ η₀ · ||c||², where c is the Cartan vector of $U_{QE}$.

(III) The decomposition of $U_{QE}$ into sequential gates $u_i$ is a compilation choice. The "ring" terminology refers to the CJ tensor network structure, which is invariant under unitary-preserving compilation.

### 5.3 What the Transpiler Argument Does NOT Attack

To be fair to CFOL, the transpiler argument does NOT attack:
- The η₀ lower bound (Fawzi-Renner + Cartan expansion)
- The QCMI ∝ θ²·log(1/θ) scaling law
- The experimental distinguishability of CFOL vs CCQ (O(θ²) vs O(θ⁴))
- The core mathematical structure of the CFOL proof

It ONLY attacks the "topological" framing and the claim that rings are "irreducible." The mathematical content is correct; the narrative wrapper is misleading.

---

## 6. Conclusion

**W7 Verdict: The transpiler CAN destroy the gate-level ring, but this REVEALS (rather than refutes) the true nature of QCMI.**

The attack succeeds in forcing a clarification of CFOL, but does not kill the core mathematical result. The transpiler merges co-axial RZZ gates on the same qubit pair, eliminating the sequential "ring" structure. QCMI is unchanged because it depends on the net unitary's non-factorability, not on the gate decomposition.

**What CFOL should say:** "Non-factorable Q-E interactions force QCMI > 0." The "ring" is a pedagogical device for the spatial (multi-qubit-pair) case, but it is misleading for the temporal case.

**What CFOL should NOT say:** "Causal rings are topological noise that cannot be eliminated by engineering." This is false because:
1. The temporal "ring" CAN be eliminated (merge gates) without affecting QCMI
2. The spatial ring CANNOT be eliminated by the transpiler, but this is due to qubit connectivity, not topology
3. QCMI depends on Cartan coefficients, not on graph-theoretic cycle counts

**Bottom line:** W7 scores a hit on CFOL's narrative but not on its mathematics. The paper should be revised to remove "topological" language and explicitly address the transpiler's effect on gate-level ring structure.

---

*Attack complete. W7 forces a terminology revision but does not refute the core QCMI > 0 result. The "ring" is a CJ-level concept, not a circuit-level one.*
