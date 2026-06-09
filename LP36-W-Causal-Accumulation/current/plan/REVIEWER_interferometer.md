# REVIEWER REPORT — LP37 "因果环是量子干涉仪"

**Reviewer:** Anonymous Referee (PRL-level adversarial review)
**Date:** 2026-06-08
**Recommendation:** **REJECT**

---

## OVERALL ASSESSMENT

This manuscript claims that causal cycles in quantum Bayesian networks function as "quantum interferometers," with commuting gates producing destructive interference (bonus ≤ 0) and non-commuting gates producing constructive interference (bonus > 0). The claim is supported by numerical data on 4-qubit systems and extended to a b₁-generalization conjecture.

**The central claim is experimentally refuted by the authors' own data, once a confounding variable (n_E mismatch) is controlled.** In a fair comparison (both tree and cycle with n_E = 3), the Haar-random (non-commuting) gate yields bonus = -0.47, directly contradicting the headline "non-commuting → constructive interference" rule. The interferometer analogy is a metaphor unsupported by any interference fringe, phase parameter, or quantum mechanical phase measurement. The "20+ gates verified" claim in the asset table is not supported by the data tables shown (7 gates). The b₁ generalization claims a "strict proof" for edge-disjoint cycles that appears nowhere in the text beyond a one-line handwave ("tensor product additivity + CFOL").

**The manuscript should be rejected.** I provide a detailed breakdown of each fatal flaw below, along with a concrete revision path should the authors wish to salvage publishable components.

---

## DIMENSION 1: THEORETICAL MOTIVATION (FATAL)

### 1.1 "Interferometer" is a Metaphor, Not Physics

The authors use the term "quantum interferometer" to describe a causal cycle over 4 qubits (Q_a, Q_b, E_1, E_2). The claim is that the two paths Q→E_1→Q' and Q→E_2→Q' "interfere" at the shared nodes.

**Question: What is the physical quantity that interferes?**

In a Mach-Zehnder interferometer, a single photon traverses two paths, accumulating a relative phase φ = k·ΔL, and the output intensity exhibits the interference pattern I(φ) ∝ 1 + cos(φ). The signature of interference is a **periodic modulation** of an observable as a function of a continuously tunable phase parameter.

In the present manuscript:
- There is **no tunable phase parameter**. The "phase" is never defined mathematically.
- There are **no interference fringes**. The data show at best a binary classification (bonus positive vs. negative), not a periodic function of any control parameter.
- The "phase" is conflated with the **commutator norm** ||[U_{01}, U_{02}]|| between gates sharing a node. This is not a phase — it is an operator-algebraic quantity that measures non-commutativity, not a U(1) phase angle.

**The Rxx(theta) scan is particularly revealing.** The authors claim that theta ≈ 0.18π is a "threshold" where the interferometer "activates." If this were truly an interferometer, one would expect Rxx(theta) to produce a periodic modulation of bonus as a function of theta — something like bonus ∝ cos(2θ) or sin(θ) — because Rxx(theta) = exp(-iθ/2 · X⊗X) has eigenvalues e^{-iθ/2} (triplet) and e^{i3θ/2} (singlet), producing a nontrivial θ-dependence in any genuine interference effect. Instead, the data show a **single sign flip** at θ ≈ 0.18π, with monotonic behavior on either side. A sign flip is not an interference fringe — it is a threshold crossing in some other physical quantity (see Dimension 4).

### 1.2 What Would Constitute Genuine Interference?

For the interferometer claim to carry physical content, the authors would need to demonstrate at minimum:

1. **Define the interfering quantity.** What are the two "paths" in Hilbert space? Are they Kraus operators K^{(1)}_{ab} and K^{(2)}_{ab}? If so, what is the inner product ⟨K^{(1)}, K^{(2)}⟩ that produces the interference term?

2. **Identify the phase parameter.** In the standard quantum interferometer, the relative phase between two paths is controlled by a physical parameter (path length, voltage, magnetic flux). What is the analogous parameter here? The gate angle θ? The commutator norm? Something else?

3. **Demonstrate periodic modulation.** Run Rxx(theta) for theta ∈ [0, 2π] at fine resolution (Δθ ≤ 0.01π) and plot bonus vs. theta. If there are genuine interference fringes, they should be visible. The current data (5 theta values per gate type) are insufficient to rule out or confirm any periodic structure.

4. **Connect to the standard quantum interference formula.** The probability of an outcome in a two-path interferometer is P = |ψ₁ + ψ₂|² = |ψ₁|² + |ψ₂|² + 2|ψ₁||ψ₂|cos(Δφ). Can the authors write an analogous expression for QCMI in terms of the two "paths" through the cycle, with an identifiable interference term proportional to cos(something)?

**Until these are provided, the "interferometer" is a suggestive analogy at best and a misleading label at worst.** The observed binary bonus sign can be explained by mundane mechanisms (see Dimension 4).

---

## DIMENSION 2: EXPERIMENTAL DESIGN (FATAL)

### 2.1 The n_E Confound (Inspector Audit Confirmed)

The original experiment compared:
- **Tree:** n_E = 3 (3 environment qubits), 4 total qubits in QE system
- **Cycle:** n_E = 2 (2 environment qubits), 4 total qubits in QE system

These differ in **three independent dimensions**: (i) graph topology (b₁ = 0 vs. 1), (ii) number of environment qubits (3 vs. 2), and (iii) number of Q-E edges (3 vs. 4). It is impossible to attribute any observed bonus to topology alone.

The internal Inspector audit (LP37_inspector_audit_interferometer.md) demonstrated that when n_E is equalized at 3 for both tree and cycle, the Haar bonus flips sign:

| Condition | Tree QCMI | Cycle QCMI | Bonus |
|-----------|-----------|------------|-------|
| Original (n_E mismatched) | 3.0790 | 3.2220 | **+0.14** |
| Fair (both n_E=3) | 3.8457 | 3.3747 | **-0.47** |

**This is a fatal confound.** The headline result — "non-commuting → constructive interference (positive bonus)" — is an artifact of unequal environment dimensions. When the confound is removed, the result reverses. The interferometer hypothesis, in its current form, is experimentally falsified.

### 2.2 Qubit Count Inequality

The tree(5QE) vs. cycle(4QE) comparison uses different total Hilbert space dimensions:
- Tree: 5 qubits in QE system → dim = 32
- Cycle: 4 qubits in QE system → dim = 16

The definition bonus = QCMI(cycle) - QCMI(tree) subtracts quantities defined on **different Hilbert spaces**. While QCMI is a scalar (in bits), the physical processes being compared involve different numbers of degrees of freedom. A smaller environment (2 qubits, dim=4 for E) saturates more quickly than a larger one (3 qubits, dim=8 for E), as the Inspector audit noted. This alone could produce apparent "interference" effects that are merely finite-dimensional saturation artifacts.

### 2.3 Why n_E = 3?

The choice n_E = 3 appears arbitrary. The manuscript provides no justification for why this particular environment size was chosen for the "fair comparison." If n_E = 4 were used, would the conclusions change? What about n_E = 1? A systematic scan over n_E is necessary to establish robustness, particularly since the central claim was already shown to be n_E-dependent.

---

## DIMENSION 3: OVERSTATED CLAIMS

### 3.1 "20+ Gates Verified" — Where?

The asset table (Section 六 of LP37_干涉仪_成果记录.md) lists:

> | 干涉仪机制(三机制分类) | ✅ | 20+门验证 |

However, the actual data tables in the same document and in `interference_test.py` show exactly **7 gate types**:
1. CNOT
2. XX(π/2)
3. XX(π/4)
4. ZZ(π/2)
5. weak Haar 0.06
6. weak Haar 0.10
7. Haar full

The `gate_classification.py` script adds SWAP, CZ, iSWAP, sqrtSWAP, CS, T⊗T, and two random non-Clifford gates — bringing the total to at most 15 distinct gate types, many of which are minor variations (e.g., random non-Clifford at different α values). Even counting generously, "20+" is not supported by the codebase.

**Where are the other 13+ gate types?** If they exist, their data must be presented. If they do not exist, this claim is a fabrication and must be retracted.

### 3.2 "Strict Proof" for b₁ > 1 Edge-Disjoint Cycles — Missing

The manuscript states:

> 边不相交环: QCMI ≥ k·η（严格，因张量积可加性+CFOL）

The claimed proof sketch is: "tensor product additivity + CFOL." This is **not a proof**. It is a one-line handwave. Specifically:

1. **Tensor product additivity of QCMI**: Christandl-Winter (2004) proved that squashed entanglement is additive under tensor products. But QCMI = I(R;E'|Q') is **not** squashed entanglement — it is the quantity being minimized to obtain squashed entanglement. Does the additivity of N_sq imply additivity of QCMI for product states? This is non-trivial and requires proof.

2. **CFOL (Cycle Factorization Obstruction Lemma)**: This lemma (proving QCMI > 0 for a single cycle) does not automatically compose to k independent cycles. Even if each cycle individually contributes η, the cycles may "interfere" (in the authors' own language) through shared boundary conditions — the Q and E nodes that appear in multiple cycles.

3. **The edge-disjoint claim assumes independence**: Two edge-disjoint cycles share vertices (they are subgraphs of the same Hasse diagram). The QCMI contributions from different cycles are not tensor-product independent unless the cycles act on disjoint sets of qubits — which they do not, by construction of the causal graph.

**A genuine proof would require:**
- Formal definition of the multi-cycle QCMI decomposition
- Proof that edge-disjoint → cycle QCMI contributions are additive
- Handling of shared vertices and their effect on the Kraus operator structure

Until this proof is written down and verified, the claim "可严格证明" is misleading. The current state should be labeled as **conjecture**, not theorem.

### 3.3 The b₁ = 3 "Bound" Has No Predictive Power

The manuscript claims QCMI ≥ k·η where η = η₀ = 1/(8 ln 2) ≈ 0.180 bits. The actual data for the b₁ ≈ 3 case show QCMI = 1.8509.

The claimed lower bound: k·η₀ = 3 × 0.180 = 0.54 bits.
The actual value: 1.85 bits.
**Ratio: 1.85 / 0.54 = 3.4×.**

A lower bound that is 3.4 times smaller than the actual value has essentially **zero predictive power**. Any physical theory can produce a bound that is an order of magnitude below the data. The scientific content of a lower bound lies in its tightness — how close it comes to saturating the actual values. A bound of 0.54 on a quantity that is never observed below 1.82 (from the η_scan data for Haar-random gates) is vacuous.

Compare: the Bekenstein bound S ≤ 2πkRE/ħc is interesting precisely because it is close to saturation in many physical systems. A bound that is 3-10× below all observations is a triviality.

---

## DIMENSION 4: ALTERNATIVE EXPLANATIONS

### 4.1 The "Entangling Power" Confound

The core observation — that different gate types produce different bonus values — admits a much simpler explanation that requires no "interferometer":

**Bonus sign correlates with the entangling power of the two-qubit gate.**

- **CNOT** (maximal entangling power for Clifford gates, ep = 2/9): bonus ≈ 0
- **SWAP** (zero entangling power — it only permutes): bonus = -2.0 (most negative)
- **XX(π/2)** (moderate entangling power): bonus = -1.0
- **ZZ(π/2)** (moderate entangling power): bonus = -0.78
- **Haar random** (average entangling power ~ 2/5): bonus slightly negative to slightly positive depending on n_E

The pattern is: **higher entangling power → less negative (or positive) bonus.** This is exactly what one expects if the cycle creates additional pathways for Q-E entanglement, and the effectiveness of those pathways depends on how much entanglement each gate can generate.

To test this directly, the authors should:
1. Compute the entangling power e_p(U) for each gate type using the standard formula (Zanardi et al., PRA 62, 030301, 2000)
2. Plot bonus vs. e_p(U) for all gate types
3. If the correlation is strong (R² > 0.8), the "interferometer" is simply a convoluted redescription of entangling power variation

### 4.2 The "Loop Feedback Cancellation" Interpretation

The Inspector audit proposed "Loop Feedback Cancellation" (LFC) as an alternative: the cycle provides feedback paths that partially return leaked information from E back to Q, reducing net QCMI compared to a tree. Under LFC:
- Bonus is **always ≤ 0** (cycle ≤ tree), because feedback can only reduce, not increase, information leakage
- The magnitude of cancellation depends on gate properties (entangling power, basis alignment)
- The fair comparison data (all bonuses negative or zero) is naturally explained
- No "interference," no "phase," no exotic quantum effect — just classical feedback through the causal graph

**LFC is both simpler and more consistent with the fair-comparison data than the interferometer hypothesis.** Occam's razor favors LFC.

### 4.3 The "Weak Gate Threshold" Reinterpreted

The observation that Rxx(theta < 0.18π) gives bonus > 0 while Rxx(theta > 0.18π) gives bonus < 0 is presented as evidence for "interferometer activation." An alternative interpretation:

**At small theta, Rxx(theta) ≈ I ⊗ I + O(θ), so the gates are near-identity.** Near-identity gates barely entangle Q and E, so QCMI is small for both tree and cycle. The cycle bonus is slightly positive because the cycle has one additional Q-E edge (4 vs. 3), providing one extra weak coupling channel. At larger theta, the gates generate substantial Q-E entanglement, the feedback cancellation mechanism kicks in, and the cycle's extra edge becomes a liability rather than an asset.

This interpretation predicts:
1. bonus(θ → 0) → 0⁺ (weakly positive, from extra edge count)
2. bonus(θ) crosses zero at some finite θ_c (when feedback cancellation exceeds extra-edge benefit)
3. bonus(θ → π) < 0 (feedback cancellation dominates)

These predictions match the data **without invoking interference**. The threshold θ_c ≈ 0.18π is simply the crossing point where the two competing effects balance.

---

## DIMENSION 5: RELATION TO EXISTING LITERATURE

### 5.1 Buscemi et al. (2025) Already Covers Gate-Type Dependence

Buscemi et al. (PRX Quantum 6, 020316, 2025) established the framework for distinguishing genuine vs. non-genuine causal回流 using squashed non-Markovianity N_sq. Their Theorem 1 (N_sq = 0 ⇔ QCMI = 0) and Theorem 2 (quantitative relationship between QCMI and recovery maps) already imply that **different gate choices will produce different QCMI values**, because different gates produce different recovery map fidelities.

The present manuscript's contribution must be evaluated against this baseline: **what does the "interferometer" add that is not already implied by Buscemi's framework?**

Specifically:
- Buscemi already showed that N_sq depends on the unitary U (implicitly, through the channel it defines)
- Buscemi already showed that some U produce N_sq = 0 (classical gates) and others produce N_sq > 0 (quantum gates)
- The topological dependence (tree vs. cycle) was partially explored in Buscemi's Section V (multi-step processes)

The novel claim here is that **topology (b₁) and gate commutativity interact in a specific way** — the "interferometer" mechanism. But if this mechanism is experimentally falsified (Dimension 2), what remains that is both true and novel?

### 5.2 "Interferometer" Analogies in Quantum Network Literature

The authors should cite and distinguish their work from:
- Chiribella et al. (PRA 88, 022318, 2013) on quantum networks with indefinite causal order — where genuine quantum interference between causal orders is rigorously defined
- Oreshkov et al. (Nature Communications 3, 1092, 2012) on the quantum SWITCH — where a control qubit determines the order of two gates, producing measurable interference between causal orders
- Araujo et al. (PRA 92, 062126, 2015) on computational advantages from coherent control of causal orders

**These works define "interference" precisely in terms of coherent superposition of causal orders.** The present manuscript's usage is qualitatively different — it refers to "interference" between paths within a fixed causal order. The authors must clarify this distinction and justify why the term "interferometer" is appropriate given the different physical mechanism.

---

## SUMMARY OF FATAL FLAWS

| # | Flaw | Severity | Reversible? |
|---|------|----------|-------------|
| 1 | Interferometer is undefined — no phase, no fringes, no interference formula | **Fatal** | Requires complete reconceptualization |
| 2 | n_E confound produces spurious bonus sign; fair comparison reverses the headline result | **Fatal** | Fixable experimentally, but kills the current claim |
| 3 | "20+ gates" claim unsupported by data (7 shown, ≤15 in code) | **Fatal** | Must retract or provide data |
| 4 | b₁ > 1 "strict proof" is a one-line handwave | **Serious** | Requires actual proof |
| 5 | Lower bound QCMI ≥ k·η is 3.4× below data — no predictive power | **Serious** | Requires tight bound derivation |
| 6 | "Weak gate threshold" is naturally explained by entangling power crossover | **Serious** | Requires ruling out alternative |
| 7 | Entangling power correlates with bonus — no need for interferometer | **Serious** | Requires ruling out alternative |
| 8 | Buscemi (2025) already implies gate-type dependence of N_sq | **Moderate** | Requires clearer novelty statement |

---

## DECISION: REJECT

**The manuscript is rejected.** The central "interferometer" claim is simultaneously (a) physically ill-defined, (b) experimentally falsified by the authors' own data under fair comparison, and (c) replaceable by a simpler explanation (entangling power variation with feedback cancellation).

**However, not all is lost for this research program.** The following salvageable components can form the basis of a revised manuscript:

### Salvageable Components

1. **Theorem 1 (QCMI identity):** I(R;E'|Q') = 4 - I(R;Q') is a clean, verified mathematical result that holds for the 4-qubit causal cycle. This is publishable as a short note or as Lemma 1 in a larger paper.

2. **Theorem 2 (Existence):** The CNOT cycle construction proving QCMI > 0 is rigorous and provides a concrete counterexample to the conjecture that all causal cycles have zero QCMI.

3. **Theorem 3 (Genericity):** The semi-algebraic argument that QCMI > 0 for almost all unitaries is mathematically sound (after the Inspector's correction from analytic to semi-algebraic).

4. **The negative bonus phenomenon:** The finding that cycles *reduce* QCMI compared to trees with equal environment size is genuinely counterintuitive and interesting. "More connections → less information leakage" is a non-obvious result that deserves investigation.

### Recommended Revision Path

1. **Abandon the "interferometer" label entirely.** Replace with descriptive language: "gate-dependence of QCMI in cyclic causal graphs" or "loop feedback cancellation in quantum Bayesian networks."

2. **Fix the experimental design:**
   - Equalize n_E across all comparisons
   - Scan n_E systematically (n_E = 1, 2, 3, 4) to map the finite-dimensional effects
   - Increase N to ≥ 200 per condition for robust statistics
   - Scan Rxx(theta) at Δθ ≤ 0.01π resolution to check for periodicity (or lack thereof)

3. **Test the LFC hypothesis directly:**
   - Compute entangling power e_p(U) for all gate types
   - Test whether bonus(e_p) is monotonic
   - If confirmed, the story becomes: "Cyclic topology creates feedback paths whose cancellation efficiency depends on gate entangling power"

4. **Either prove or retract the b₁ > 1 generalization:**
   - Provide a complete proof of edge-disjoint additivity, or
   - Present it honestly as a conjecture with supporting numerical evidence (which already exists in b1_scaling.py)

5. **In the revised manuscript, frame the contribution as:**
   > "We demonstrate that in quantum Bayesian networks with cyclic causal structure, the QCMI is systematically *lower* than in tree-structured networks with equal environment size. This counterintuitive result — more Q-E connections produce less information leakage — is explained by a loop feedback cancellation mechanism whose efficiency is modulated by the entangling power of the two-qubit gates. For classical (Clifford) gates with low entangling power, cancellation is nearly complete; for Haar-random gates with high entangling power, cancellation is partial."

This framing is honest, novel, supported by the data, and does not require the physically unjustified "interferometer" metaphor.

---

### Additional Minor Issues

- **Repetition in documentation:** The file `LP37_干涉仪_成果记录.md` contains the same Section 四 (weak gate threshold), Section 五 (b₁ > 1 generalization), and Section 六 (asset inventory) copypasted **at least 15 times** verbatim. This suggests hasty assembly and raises concerns about the care with which the experimental data were analyzed.

- **N=40 statistical power:** For small effects like Haar bonus = +0.14, standard error is approximately 0.05-0.1 at N=40. A 1.4-2.8σ effect in the original (confounded) experiment is marginal significance at best.

- **Fixed seed in commutativity tests:** `verify_setup()` hardcodes seeds (99, 199) for commutativity testing. While this does not affect the results, it is poor experimental practice and should use random seeds with error bars.

- **Order dependence not tested:** The unitary U = U₄U₃U₂U₁ is applied in a fixed order determined by the causal partial order. The authors do not verify that permuting the order (where consistent with causality) does not affect the conclusions. This is especially relevant since the "interference" between paths may depend on gate ordering.

---

**END OF REVIEW**
