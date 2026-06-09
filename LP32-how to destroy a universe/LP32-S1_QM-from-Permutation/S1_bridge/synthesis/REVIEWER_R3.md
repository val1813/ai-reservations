# REVIEWER REPORT — R3

**Manuscript**: S1 Quantum Bridge: BLP Non-Markovianity Bound from Combinatorial Capacity
**Venue**: Physical Review Letters
**Reviewer**: Anonymous (adversarial review)
**Recommendation**: **REJECT**

---

## OVERALL ASSESSMENT

This manuscript claims to prove that, under a strict unidirectionality assumption (M3), the BLP non-Markovianity measure satisfies N_BLP ≤ min(N_S·q_S, N_E·q_E) · |1-2q_E|. The result emerges from three rounds (R1-R3) of internal adversarial research, with two independent derivations (combinatorial by "A博士" and W_1 optimal-transport by "B博士") converging on the same expression. The authors present this as a rigorous, parameter-free bound on quantum non-Markovian backflow.

I recommend rejection. My reasoning follows the five standard criteria, but the fatal problems concentrate in three areas: (1) the bound is physically vacuous for any system with N_S > 4, which is all realistic quantum devices; (2) the core model assumption (M3) is not physically justified for the small systems to which the bound would apply; and (3) the internal derivations contain an unresolved logical contradiction between the two independent paths, meaning the claimed "dual-path convergence" is illusory. I detail each below.

---

## 1. NOVELTY

### 1.1 Prior coverage by Megier-Smirne-Vacchini (2021)

The MSV entropic bound [Phys. Rev. Lett. 127, 030401 (2021)] establishes that trace-distance revivals (i.e., BLP backflow) are upper-bounded by system-environment correlations and environmental-state changes, quantified through the Holevo skew divergence (telescopic relative entropy). This bound applies to **any CPTP dynamics** — no restriction to CNOT gates, diagonal states, pointer bases, or unidirectional jumps.

The present manuscript's bound is a strict special case of the MSV framework: MSV applies to all CPTP maps, and the present model (CNOT + diagonal states + M3 unidirectionality) is one specific CPTP instance. The authors acknowledge this (PRL manuscript §4: "MSV for dynamical generality, ours for operational simplicity") but fail to address the logical consequence: **any bound that is provably valid in this specific model is already covered by the MSV bound**, because the MSV bound is valid for all CPTP dynamics and therefore valid for this model in particular. The claimed "complementarity" masks the fact that the present result is not a new physical constraint — it is a special-case evaluation of an existing general bound.

### 1.2 Triviality of the counting argument

The core combinatorial step — "each qubit toggles |0⟩ → |1⟩ at most once, therefore N_back ≤ N_S·q_S" — is the pigeonhole principle applied to binary state labels. The mathematical content is:

> There are N_S·q_S qubits initially in |0⟩. Each backflow event consumes one. Therefore at most N_S·q_S backflow events can occur.

This is a tautology dressed in physics notation. The only non-trivial step is connecting event counts to the BLP trace-distance integral via the encoding efficiency |1-2q_E|. But this connection (Fact F2, A博士 R1 Eq. 7) is a single-qubit algebraic identity that follows directly from the CNOT truth table — it is a calculation, not a discovery.

The question a PRL referee must ask is: **does the translation from event-counting to trace-distance integral reveal a structure that was not already obvious from the model assumptions?** The answer is no. The entire bound can be summarized as: "In a model where information can only flow forward and each qubit has one bit of capacity, backflow is limited by the number of qubits that haven't been written to yet." This is a restatement of the model, not a theorem about it.

### 1.3 Difference from existing bounds

The authors emphasize that their bound requires only projective population measurements, not full tomography (unlike MSV). This operational claim is addressed under Testability (§4) — it does not hold up. Even if it did, operational convenience is not a substitute for physical novelty. A simplified measurement protocol for evaluating an existing bound is an experimental technique paper, not a PRL theory paper.

---

## 2. TECHNICAL CORRECTNESS

### 2.1 Fatal: The min(N_S·q_S, N_E·q_E) form is not proved

This is the most serious technical flaw. The claimed bound contains two branches joined by `min`:

- **N_S·q_S branch**: Claims backflow events are limited by the number of S-qubits initially in |0⟩. This is the pigeonhole argument and is mathematically sound under M3.
- **N_E·q_E branch**: Claims backflow events are limited by the number of E-qubits that can be encoded. **This branch is not proved**, and the authors' own analysis demonstrates why.

A博士's §1.5-1.6 explicitly analyzes whether E-qubit information can be "reused" for multiple backflow events. The conclusion (A博士 §1.6) is unambiguous:

> "在纯粹M3下，N_E·q_E分支退化为条件1（非瓶颈），而N_S·q_S分支提供实际约束"
>
> Translation: "Under pure M3, the N_E·q_E branch degenerates to condition 1 (non-bottleneck), while the N_S·q_S branch provides the actual constraint."

A博士 further states that the min form holds only under an "additional assumption that E encoded information is not reused across backflow events" (§1.6.1). **This additional assumption is not part of M3 and is not physically justified in the manuscript.**

The physical reason is clear: in a CNOT gate, the control qubit is not modified. When CNOT_{E_j→S_i} is applied (Type R backflow), E_j retains its state and therefore retains its encoded distinguishability. The same E_j can subsequently serve as control for CNOT_{E_j→S_k}, encoding the same distinguishability into a different S-qubit S_k. The "information asset" in E_j is not consumed by reading. A博士 recognized this explicitly (§1.5):

> "E_j的信息虽然不因CNOT控制而被消耗，但当它被读入S_i后，区分度现在同时存在于E_j和S_i"
>
> Translation: "E_j's information, while not consumed by CNOT control, after being read into S_i, the distinguishability now exists simultaneously in E_j and S_i."

Therefore, the number of backflow events is bounded by S-side capacity (N_S·q_S) but **not** by E-side encoding capacity (N_E·q_E). The min form is incorrect; only the N_S·q_S branch is rigorous. The claimed theorem should read:

```
N_BLP ≤ N_S · q_S · |1-2q_E|    (only this is proved)
```

not

```
N_BLP ≤ min(N_S·q_S, N_E·q_E) · |1-2q_E|    (not proved)
```

### 2.2 Contradiction between A博士 and B博士 on E-qubit information consumption

B博士's W_1 derivation (§3.2, Step 5) makes a claim that directly contradicts A博士's analysis:

> "每个E_j的W_1在一个回流中被'读空'——因为跳后E_j的区分度被混叠到S_i中，而E_j自身因跳的非双射性丢失了区分度"
>
> Translation: "Each E_j's W_1 is 'read empty' in one backflow event — because after the jump, E_j's distinguishability is aliased into S_i, and E_j itself loses distinguishability due to the non-bijectivity of the jump."

This claim is **physically false**. The Lindblad jump operator L_{E_j→S_i} = |1⟩⟨1|_{E_j} ⊗ |1⟩⟨0|_{S_i} acts on the target S_i, not on the control E_j. The control qubit's state is unchanged — this is true for both the unitary CNOT and the restricted Lindblad jump (the jump operator contains the projector |1⟩⟨1| on the control, which is idempotent and does not alter the control's state). E_j's marginal distribution is invariant under L_{E_j→S_i}.

B博士's claim that E_j "loses distinguishability due to non-bijectivity" confuses two distinct concepts:
- The map L is non-bijective on the **joint** {E_j, S_i} space (two input states can map to the same output).
- But L acts as identity on the **marginal** of E_j (the control qubit is untouched).

The distinguishability stored in E_j's marginal — which is what drives backflow — is not erased by a Type R jump. B博士's entire W_1 contraction argument for the N_E·q_E branch rests on this error.

**The two "independent derivations" do not converge.** A博士's honest analysis shows the N_E·q_E branch is not rigorous. B博士's derivation asserts it is, but through a mathematical error. The claimed dual-path convergence is an artifact of B博士 making a stronger claim than his framework supports, and the PI synthesis papering over the discrepancy.

### 2.3 M3 is not physically justified for the relevant system sizes

The M3 assumption (strict unidirectionality: no |1⟩ → |0⟩) is defended by quantum Darwinism: pointer-basis states are redundantly recorded in the environment, making reversal require Kac recurrence times exceeding the age of the universe (Zurek 2009, Riedel-Zurek 2011).

This argument applies to **macroscopic** environments with N_red ≈ 100 or more redundant records. The systems studied in this manuscript have N_total = N_S + N_E = 6 (original PRL six-qubit model) to perhaps 10-20. At these scales:

1. **Kac recurrence is irrelevant.** For N=6 qubits, the state space has dimension 64. The CNOT dynamics on {0,1}^6 generates a subgroup of the symmetric group S_64. The recurrence time for CNOT sequences on 6 qubits is determined by the order of this subgroup, which is vastly smaller than 2^64. More importantly, CNOT² = I means recurrence can happen in **2 gate steps** — not "longer than the age of the universe."

2. **Quantum Darwinism has not been demonstrated for N<10.** The redundant recording mechanism requires many environment fragments independently encoding the same pointer-basis information. With N_E = 3 (the PRL manuscript's collision model), there are simply not enough environment qubits to establish redundancy. The claim that |1⟩→|0⟩ is "effectively forbidden" by quantum Darwinism in a 3+3 qubit system is a category error — applying a thermodynamic limit argument to a manifestly finite, small quantum system.

3. **CNOT self-inverse creates effective reversibility.** A博士 himself acknowledges this in §5.2 (Mode B): "对N_total=6 (N_S=3, N_E=3)，所有可能的CNOT序列构成对称群S_64上的一个子群。在其中搜索CNOT²=I的实例是简单的。" The M3 "prohibition" on |1⟩→|0⟩ is not a physical prohibition — it is a **gate selection rule** imposed by the theorist. An experimentalist applying CNOT gates has no physical barrier preventing them from applying CNOT twice to achieve |1⟩→|0⟩.

The authors acknowledge this vulnerability (A博士 §5.3 provides a table of M3's "physical validity domain") but fail to recognize the implication: **the theorem is about a model that does not correspond to any realizable experiment.** If CNOT²=I is accessible in the lab (gate time ~100 ns, T_2 ~100 μs), then M3 is a voluntary restriction, not a physical necessity. A theorem proved under a voluntary restriction is a mathematical exercise, not a physical law.

### 2.4 Encoding efficiency in multi-round, correlated states

The encoding relation Δp = δ · |1-2q_E| (Fact F2) is derived for a single forward CNOT acting on an initial product state. After multiple rounds of gates, S-E correlations develop, and subsequent forward encoding events act on correlated states. The encoding efficiency for correlated states may deviate from |1-2q_E|. B博士 acknowledges this concern (§9, Attack 1) and argues the deviation makes the bound looser (more conservative). This is plausible but not proved. Since the bound is already loose to the point of triviality (§3), this does not independently sink the paper, but it adds to the cumulative case that the "rigorous proof" claims are overstated.

---

## 3. PHYSICAL SIGNIFICANCE

### 3.1 The bound is trivial for all systems with N_S ≥ 5

This is the fatal problem for physical significance. Consider typical parameters:

- N_S = 5 (a small system by any standard)
- q_S ≈ 0.5 (half the qubits initially in |0⟩)
- |1-2q_E| ≈ 0.5 (moderate environmental polarization)

Then N_S · q_S · |1-2q_E| = 5 · 0.5 · 0.5 = 1.25 > 1.

Since N_BLP ≤ 1 always (trace distance between any two quantum states is bounded by 1), the bound provides **zero constraint**. It is vacuously satisfied by all possible dynamics.

For the bound to be non-trivial (N_S · q_S · |1-2q_E| < 1), one needs extreme parameters. For N_S = 5, one needs q_S · |1-2q_E| < 0.2. For N_S = 10, one needs q_S · |1-2q_E| < 0.1. These are not typical experimental conditions — they require nearly all S-qubits to start in |1⟩ (q_S ≈ 0) or the environment to be nearly maximally mixed (q_E ≈ 0.5, making |1-2q_E| ≈ 0).

The bound is only non-trivially constraining for **N_S ≤ 4 with carefully tuned parameters**. The PI synthesis from R1 already identified this as the "N_S scaling disaster" (N_S标度灾难), noting that both A博士 and B博士's bounds are trivial for N_S ≥ 5. R3 was supposed to solve this. It did not.

### 3.2 No realistic quantum device is constrained by this bound

Current superconducting quantum processors have 50-100+ qubits. Ion trap systems have 20-50+. Even the smallest meaningful quantum devices have N_S ≥ 5. For all of these, N_S · q_S · |1-2q_E| ≥ 1, and the bound is vacuous.

A bound that can only constrain systems with N_S = 1, 2, 3, or 4 qubits is a bound on toy models, not on quantum devices. Physical Review Letters publishes results of broad physical significance. A combinatorial inequality that reduces to N_BLP ≤ 1 for all systems of practical interest does not meet this standard.

### 3.3 The claimed "experimental predictions" are model tautologies

The predictions listed in A博士 §4.2 are:

- **Prediction 1 (linear scaling):** N_BLP grows at most linearly with N_S. But this is because the bound itself is ∝ N_S, so "predicting" linear scaling is predicting the bound, not predicting nature.
- **Prediction 2 (polarization dependence):** N_BLP ∝ |1-2q_E|. This follows from Fact F2, a single-qubit algebraic identity. It is a property of the CNOT encoding, not a prediction about non-Markovianity.
- **Prediction 3 (pigeonhole saturation):** N_BLP → N_S when q_S → 1 and |1-2q_E| → 1. This is the bound evaluated at its extremum. It is not a prediction; it is the bound's own edge case.

None of these are falsifiable predictions about quantum dynamics that were not already encoded in the model assumptions.

---

## 4. TESTABILITY

### 4.1 The claimed "projective measurement only" advantage is misleading

The original PRL manuscript claims the bound "requires only projective population measurements without full quantum state tomography." This conflates two distinct tasks:

1. **Measuring q_S and q_E**: These are single-qubit ⟨0|ρ|0⟩ expectations. They can indeed be measured with projective measurements on individual qubits, without full state tomography. So far so good.

2. **Measuring N_BLP**: The BLP measure is defined as N_BLP = ∫_{Ḋ>0} Ḋ(t) dt, where D(t) is the trace distance between two reduced system states evolved from two different initial conditions. To compute D(t) at each time t, one needs the full probability distribution over the 2^{N_S} computational basis states of the system — this is, by definition, **pointer-basis state tomography**. For N_S = 3, this requires measuring 2^3 = 8 probabilities at each time point. For N_S = 5 (where the bound is already trivial), it requires 32 probabilities. The measurement cost scales exponentially with N_S.

The claim of "operational simplicity" compares the present method to full **quantum** state tomography (which would require measuring off-diagonal elements in multiple bases). But the fair comparison is to the MSV bound's information-theoretic evaluation, which also requires only the reduced states — the MSV bound needs ϱ_S, ϱ_E, and ϱ_SE, whose diagonal elements in the pointer basis are exactly what the present method also needs. The present method is not meaningfully simpler for the task of measuring N_BLP.

### 4.2 Event counting is not operationally defined

The original PRL manuscript defines N_back as "the total count of backflow events" — individual |0⟩→|1⟩ toggles of S-qubits. Counting such events requires either:

(a) **Intermediate measurements** after each gate, which collapse the quantum state and destroy the very dynamics being measured, or
(b) **Process tomography** to reconstruct the gate sequence and infer which toggles occurred, which is exponentially expensive.

Neither option is discussed in the manuscript. The bound's key quantity (N_back) is not independently measurable without disrupting the experiment. This is a fundamental obstacle to experimental verification that the manuscript simply ignores.

### 4.3 No concrete experimental proposal exists

The manuscript provides a table of numerical examples (SM Table I) but no experimental blueprint. There is no specification of:
- Which physical platform (superconducting, ion trap, photonic, etc.)
- How to prepare the two initial states ϱ_S(0) and σ_S(0) with controlled q_S values
- How to implement the unidirectional Lindblad jump L without the CNOT²=I reversibility loophole
- How to measure D_S(t) at intermediate times without state collapse
- What signal-to-noise ratio is needed to distinguish a bound violation from gate errors

The SM §5 discussion of gate-level implementation acknowledges 28% cumulative gate infidelity for a 3×3 system, which already exceeds the precision needed to test a bound that is only non-trivial in narrow parameter regimes. If the gate error exceeds the gap between the bound and the trivial bound (N_BLP ≤ 1), the bound is not experimentally testable.

---

## 5. INTERNAL CONSISTENCY

### 5.1 M3 self-consistency for small N

As argued in §2.3, quantum Darwinism requires N_red ≫ 1 redundant records. The systems considered have N_total ≤ 10. The claim that |1⟩→|0⟩ is "effectively forbidden by quantum Darwinism" in a 6-qubit system is internally inconsistent — the very mechanism invoked to justify the assumption does not operate at the scale where the assumption is applied.

### 5.2 The A博士 / B博士 contradiction on E-qubit information reuse

This is the deepest internal inconsistency and is detailed in §2.2. To summarize:

- **A博士** (§1.5): E-qubit information is NOT consumed by Type R backflow events. The same E_j can drive multiple backflow events to different S-qubits. Therefore N_E·q_E is not a hard constraint; only N_S·q_S limits backflow.
- **B博士** (§3.2 Step 5): E-qubit W_1 is "read empty" after one backflow event. Each encoded E-qubit supports at most one backflow event. Therefore N_E·q_E IS a hard constraint, justifying the min form.

These are logically contradictory claims about the same physical process. The PI synthesis (PI_synthesis_R2.md) does not resolve this contradiction — it simply declares both paths converged and moves on. The R3 final theorem presents `min(N_S·q_S, N_E·q_E)` as if both branches are equally proved, when in fact one author's analysis shows one branch is not proved and the other author's derivation of that same branch contains a mathematical error.

**A theorem whose two "independent proofs" rest on contradictory physical mechanisms is not a theorem — it is a disputed conjecture.**

### 5.3 W_1 contraction framework vs. CNOT identity

B博士's W_1 framework in R2 was built on the fact that CNOT is a permutation on {0,1}^N, hence W_1-preserving (an isometry). In R3, B博士 switches to the Lindblad jump operator L, which is non-bijective, hence W_1-contracting.

The problem: the **physical** operation is still CNOT. M3 is a **selection rule** on which CNOT applications are permitted — it does not change the fact that CNOT is the physical gate being applied. When CNOT is applied (within M3's allowed domain), it remains a bijection on the subspace where it acts. The W_1 contraction B博士 derives comes from restricting to the domain where the jump is non-bijective — but on that restricted domain, the map is still injective on the subspace of states that actually occur under M3.

Specifically: under M3, the target qubit is always |0⟩ before a jump (otherwise the jump is prohibited). On the subspace of states with target=|0⟩, L acts as |c, 0⟩ → |c, c⟩ (c ∈ {0,1}). This map IS injective on this subspace (|00⟩→|00⟩, |10⟩→|11⟩ — two distinct inputs map to two distinct outputs). The non-bijectivity only manifests when considering inputs that M3 prohibits (target=|1⟩). Therefore, under M3, L is effectively injective on the accessible subspace, and W_1 should be **preserved**, not contracted.

B博士's W_1 contraction result (§2.5, Lemma 2) applies to the unrestricted operator, not to the M3-restricted dynamics. This is a subtle but fatal error in the mathematical foundation of the W_1 derivation path.

---

## SUMMARY OF FATAL FLAWS

| # | Flaw | Severity | Section |
|---|------|----------|---------|
| 1 | min(N_S·q_S, N_E·q_E) not proved — N_E·q_E branch requires unproven assumption | **FATAL** | 2.1 |
| 2 | A博士/B博士 contradictory claims about E-qubit information reuse | **FATAL** | 2.2, 5.2 |
| 3 | Bound trivial (N_BLP ≤ 1) for all N_S ≥ 5 with typical parameters | **FATAL** | 3.1 |
| 4 | W_1 contraction argument invalid under M3 restriction (effective injectivity) | **MAJOR** | 5.3 |
| 5 | M3 not physically justified for N < 10 (quantum Darwinism category error) | **MAJOR** | 2.3 |
| 6 | CNOT²=I self-inverse provides effective |1⟩→|0⟩ in any real experiment | **MAJOR** | 2.3 |
| 7 | N_BLP measurement requires exponential pointer-basis tomography | **MAJOR** | 4.1 |
| 8 | N_back event counting not operationally defined without state collapse | **MAJOR** | 4.2 |
| 9 | Encoding efficiency for correlated multi-round states not proved | **MODERATE** | 2.4 |
| 10 | MSV (2021) already provides a stronger, more general bound | **MODERATE** | 1.1 |
| 11 | "Predictions" are model tautologies, not falsifiable claims | **MODERATE** | 3.3 |

---

## VERDICT: REJECT

The manuscript fails on all three essential criteria for PRL:

1. **Physical significance (FATAL)**: The bound constrains no system with N_S ≥ 5. A PRL paper must have implications for real physical systems. A bound that only applies to N_S = 1-4 qubit toy models — and even then only with carefully tuned parameters — does not meet this bar.

2. **Technical correctness (FATAL)**: The claimed theorem `N_BLP ≤ min(N_S·q_S, N_E·q_E) · |1-2q_E|` is not proved. Only the N_S·q_S branch is rigorous. The N_E·q_E branch rests on an unproven additional assumption (A博士's own analysis) or a mathematical error about control-qubit distinguishability erasure (B博士's derivation). The "dual-path convergence" is synthetic — the two paths converge only by selective reading of their conclusions.

3. **Novelty (MAJOR)**: The core counting argument is tautological. The only non-trivial step (connecting event counts to trace distance via |1-2q_E|) is a single-qubit algebraic identity. The MSV (2021) entropic bound already provides a stronger, more general constraint that covers this model as a special case.

---

## PATH TO CORRECTION (if the authors wish to revise)

The conceptual core — that combinatorial constraints on information flow in finite-dimensional state spaces can bound non-Markovian backflow — is potentially interesting. But the current execution does not yield a publishable result. A salvageable version would need:

1. **Abandon the min(N_S·q_S, N_E·q_E) claim.** Keep only the provable N_S·q_S·|1-2q_E| bound, and be honest that this is always ≥ 1 for N_S ≥ 5 with typical parameters.

2. **Either (a) find a bound that does not scale linearly with N_S**, or (b) prove that N_BLP genuinely does scale with N_S and demonstrate this scaling experimentally or numerically in systems where the bound is below 1 (requiring very small N_S or very extreme q_S, q_E).

3. **Resolve the M3 justification** for small systems. The quantum Darwinism argument does not work for N < 100. Either provide a different justification for unidirectionality at small N, or relax M3 and derive the weaker (but honest) Corollary R3.2: N_BLP ≤ 2N_S · |1-2q_E|.

4. **Provide a concrete experimental proposal** including a platform, state preparation protocol, measurement scheme, and error analysis demonstrating that the bound can be tested with better precision than the trivial bound N_BLP ≤ 1.

5. **Fix B博士's W_1 contraction error** or abandon the W_1 path entirely. Under M3, the accessible subspace makes L effectively injective; W_1 is preserved, not contracted. The W_1 framework does not provide independent support for the bound.

6. **Honestly compare to MSV (2021).** If the bound is always looser than the MSV bound for the same model (as it appears to be), acknowledge this and explain what value the combinatorial perspective adds beyond MSV.

Without these corrections — particularly items 1-3 — the manuscript is not suitable for publication in Physical Review Letters or any other journal. The result as currently formulated is a mathematically flawed bound on a physically unrealistic model, with no demonstrated experimental relevance.

---

**Confidential note to editor**: The internal research logs (R1-R3) provided to me as background demonstrate that the authors themselves have identified most of these flaws (particularly the N_S scaling disaster, the M3 small-N inconsistency, and the E-qubit information reuse problem). The fact that these honest internal analyses exist but the final manuscript does not adequately address them — instead presenting `min(N_S·q_S, N_E·q_E)` as a proved theorem — is concerning. I recommend the authors incorporate their own best criticisms into a substantially revised manuscript, or redirect this research direction entirely.

---

*Reviewer declines to reveal identity. Recommendation: REJECT.*
