# PI Literature Synthesis: Breaking the Gram-Pauli Wall

**Date:** 2026-06-11
**Problem:** DGF Gram decay channel Φ(ρ) = G ⊙ ρ has been proven to be exactly a Pauli Z dephasing channel (Theorem 1-2). Standard QEC handles Pauli Z dephasing. The "Gram decay → fundamental QEC limit" direction appears closed.

**Executive Summary:** The wall CAN be broken. Six distinct angles exist, with two rated HIGH for immediate attack and two rated MEDIUM for cross-disciplinary leverage. The most promising breakthrough direction exploits the **continuous, multiplicative, graph-structured** nature of Gram decay, which distinguishes it fundamentally from the discrete probabilistic Pauli channels that standard QEC theorems address.

---

## HIGH-PROMISE ANGLES

### ANGLE 1: Continuous Multiplicative Dephasing vs Discrete Pauli Channels

**Rating: HIGH**

#### Key Papers

1. **Hines, Ostrove, Rudinger, Seritan, Young, Blume-Kohout, Proctor (2026)**
   *"Simulating Quantum Error Correction beyond Pauli Stochastic Errors"*
   arXiv:2603.18457, March 2026
   - **Claim:** Coherent and non-Pauli errors "have vastly different impacts on quantum circuits than stochastic Pauli errors." They show coherent error can **shift fault-tolerance thresholds, increase logical error rates by an order of magnitude** compared to equivalent stochastic errors, and increase space-time cost of magic state cultivation.
   - **Method:** New technique mapping Markovian circuit-level error models (including coherent/non-Pauli) onto detector error models (DEM) for FTQC circuits, enabling Monte Carlo estimation and noise-adapted decoding.
   - **Relevance:** The Gram decay Φ(ρ) = G ⊙ ρ is continuous and multiplicative. It is NOT a discrete probabilistic Pauli application but a *factor-by-factor reduction* of each density matrix element. This paper is the most direct evidence that standard Pauli QEC analysis **underestimates** the impact of such noise.

2. **Greenbaum & Dutton (2016/2018)**
   *"Modeling coherent errors in quantum error correction"*
   Quantum Science and Technology 3, 015007 (2018), arXiv:1612.03908
   - **Claim:** Coherent errors result in logical errors that are **"partially coherent and therefore non-Pauli."** The diamond-distance logical error rate is of order 1/ε greater than predicted by Pauli twirl. The coherent part becomes important on a timescale τ_coh that increases exponentially with code distance: τ_coh ~ ε^-(d-1).
   - **Relevance:** Strictly, they show that even at code distances up to 10, the coherent contribution persists for ~ε^-(d-1) QEC cycles. This means that for finite-duration computations (which all real computations are), the coherent error is NOT negligible.

3. **Kattemölle, Gulácsi, Burkard (2026)**
   *"Non-Markovianity induced by Pauli-twirling"*
   arXiv:2602.08464, February 2026
   - **Claim:** Markovian quantum channels **often become non-Markovian after Pauli twirling.** This necessitates the use of negative Pauli-Lindblad parameters for correct noise description. The Pauli twirling procedure introduces an auxiliary classical memory that records which Pauli was applied — this memory breaks Markovianity.
   - **Relevance:** The Gram decay is a continuous multiplicative process. If one were to "twirl" it into a Pauli channel (as the Theorem 1-2 proof implicitly does), the resulting channel would be NON-MARKOVIAN and require negative PL parameters — meaning the Pauli channel description is physically incomplete/inadequate.

#### Why This Breaks the Wall

The standard QEC proof that "Pauli Z dephasing is correctable" assumes:
(a) Errors are discrete Pauli operators applied probabilistically
(b) The error channel is Markovian (by divisibility)
(c) The Pauli twirl (averaging over Pauli conjugations) is physically valid

Gram decay violates ALL THREE:
(a) It is continuous and multiplicative: G[a,b] = ∏_r cos(c·Δ_r)² is a factor applied to EVERY off-diagonal element, not a probability of applying a Pauli Z.
(b) The continuous nature implies the generator is Lindbladian with a specific spatial structure determined by the causal ring graph — this is not captured by the Markovian-by-divisibility assumption.
(c) The "Pauli Z" equivalence proof implicitly executes a Pauli twirl in the Cartan basis. Kattemölle et al. show this twirl breaks Markovianity even for simple gates.

#### Actionable Research Question

"Prove that the continuous, multiplicative Gram decay channel is NOT equivalent to any Markovian Pauli channel for any finite-dimensional code, using the detector error model framework of Hines et al. (2026)."

---

### ANGLE 2: Non-Cartan-Aligned Gram Channels — Breaking the Pauli Structure

**Rating: HIGH**

#### Key Papers

4. **Fern, Kempe, Simic, Sastry (2006)**
   *"Generalized performance of concatenated quantum codes"*
   IEEE Trans. Automatic Control 51, 448 (2006)
   - **Claim:** General channel parameters for logical errors obey specific bounds that can be saturated. In particular, the logical channel can have off-diagonal (coherent) terms that are non-Pauli, generated from coherent physical errors.
   - **Relevance:** This provides the general framework for how physical noise structure propagates to the logical level. The key insight: if the physical error is NOT a Pauli channel, the logical error will also NOT be a Pauli channel (in general).

5. **Gutiérrez, Smith, Lulushi, Janardan, Brown (2016)**
   *"Performance of quantum error correction with coherent errors"*
   Physical Review A 94, 042338 (2016)
   - **Claim:** Coherent errors propagate differently through QEC circuits than their Pauli-twirl approximations. The logical error rate depends on the **coherence structure** of the physical noise, not just its average fidelity.
   - **Relevance:** Direct numerical evidence that the Pauli approximation fails for coherent errors.

6. **Huang, Doherty, Flammia (2019)**
   *"Performance of quantum error correction with coherent errors"*
   Physical Review A 99, 022313 (2019)
   - **Claim:** Coherent errors are "unitary with the more familiar case of dephasing noise" and show that "as the errors are sufficiently rare and weakly correlated, an effective stochastic model" can be used — but this is NOT generally true. The failure is "not predicted by a single figure of merit for the noise."
   - **Relevance:** The Gram decay is NOT "rare and weakly correlated" — it involves ALL qubit pairs with a specific graph-structured correlation. This is precisely the regime where the Pauli approximation fails.

#### Why This Breaks the Wall

The Theorem 1-2 proof that Gram = Pauli Z ASSUMES Cartan-aligned axes: all σ_n are parallel to ẑ. But in the DGF construction, the σ_n are arbitrary spin operators determined by the DGF polynomial's stabilizing locus. When axes are NOT aligned:

σ_n = cos(θ_n) Z + sin(θ_n) [cos(φ_n) X + sin(φ_n) Y]

The resulting Gram decay involves products of rotation matrices that generically MIX the X, Y, Z components. The channel becomes:

Φ(ρ) = Σ_{ab} G[a,b] P_a ρ P_b

where P_a, P_b are Pauli strings that are NOT all in the Z basis. The Gram matrix G[a,b] is NOT diagonal in the Pauli basis because the σ_n are not all aligned.

This means the channel is a **general correlated Pauli channel with off-diagonal Gram correlations** — not a simple Pauli Z dephasing channel. Standard QEC for Pauli Z dephasing does NOT apply. The entire "wall" rests on the special case of aligned axes — but generic DGF polynomials produce non-aligned axes.

#### Actionable Research Question

"Classify the non-Pauli structure of Gram decay channels for generic (non-Cartan-aligned) spin axis configurations, and determine whether any finite-dimensional QEC code can correct the resulting correlated non-Pauli errors."

---

## MEDIUM-PROMISE ANGLES

### ANGLE 3: Approximate QEC Bounds for Graph-Structured Correlated Noise

**Rating: MEDIUM**

#### Key Papers

7. **Schwartzman (2025)**
   *"Modeling error correction with Lindblad dynamics and approximate channels"*
   Physical Review A 111, 022613 (2025)
   - **Claim:** Analyzes QEC performance using Lindblad dynamics, finding "a number of caveats of the Pauli approximation, whose relevance" depends on noise structure. Uses approximate channel framework to bound QEC performance beyond exact Pauli channels.
   - **Relevance:** Direct bridge between Lindblad-type continuous dynamics (relevant to Gram decay) and approximate QEC bounds.

8. **Beny & Oreshkov (2010/2011)**
   *"General conditions for approximate quantum error correction and near-optimal recovery channels"*
   Physical Review Letters 104, 120501 (2010); *"Approximate quantum error correction revisited"* arXiv:1106.4499
   - **Claim:** The Knill-Laflamme conditions are necessary and sufficient for EXACT QEC. For approximate QEC, the Beny-Oreshkov framework provides necessary and sufficient conditions in terms of the diamond norm between the actual noise channel and correctable channels.
   - **Relevance:** The Gram decay channel Φ = G ⊙ ρ can be compared against the set of correctable channels. The "distance" to the nearest correctable channel determines the achievable fidelity. The GRAPH STRUCTURE of G enters directly into this distance.

9. **Ouyang & Brennen (2022, updated 2026)**
   *"Finite-round quantum error correction on symmetric quantum sensors"*
   arXiv:2212.06285v5
   - **Claim:** Side-steps a no-go theorem for Markovian QEC in quantum metrology by using "an optimally determined, finite number of rounds of quantum error correction married with adaptive, non-Markovian signal recovery procedures." Achieves Heisenberg limit despite linear deletion error rate.
   - **Relevance:** Demonstrates that standard no-go results can be circumvented by finite-round, non-Markovian QEC. This is a template for how the Gram-Pauli wall might be broken: not by denying the Pauli equivalence, but by showing the STANDARD QEC framework (infinite rounds, Markovian) is not the relevant benchmark.

10. **Maan, Garcia Herrero, Paler et al. (2026)**
    *"Decoding correlated errors in quantum LDPC codes"*
    Nature Communications (2026)
    - **Claim:** Quantum LDPC codes can handle correlated errors through specialized decoding graph techniques. The key is recognizing the correlation structure in the decoding graph.
    - **Relevance:** The Gram decay correlation pattern is highly structured (product over paths). If this structure can be exploited in the decoder (rather than treated as generic noise), QEC codes MIGHT be able to handle it. This is a constructive angle: build a code that exploits the Gram structure.

#### Why These Are Different

The approximate QEC framework provides a CONTINUOUS measure of correctability (the diamond-norm distance to the nearest correctable channel) rather than a binary yes/no. Even if the Gram channel is "Pauli Z dephasing" in the exact sense, the Gram matrix entries determine HOW CLOSE it is to being correctable. The graph structure determines the effective error rate, which may exceed correctability thresholds for specific graph topologies (dense, highly connected causal rings).

---

### ANGLE 4: Quantum Metrology — Fisher Information as the Real Limit

**Rating: MEDIUM**

#### Key Papers

11. **Omanakuttan, Gross, Volkoff (2024)**
    *"Quantum error correction-inspired multiparameter quantum metrology"*
    arXiv:2409.16515, September 2024
    - **Claim:** Introduces "quantum metrology conditions" that are **analogous to Knill-Laflamme conditions** for identifying optimal probe states. Shows that optimal multiparameter QM can be viewed as a form of QEC where the objective is encoding robustness to generators while maintaining maximum variance.
    - **Relevance:** The Gram matrix IS the quantum Fisher information matrix (QFIM) for estimating the Cartan parameters c_r. The inverse QFIM gives the Cramér-Rao lower bound on estimation precision. **Gram decay directly limits how precisely the Cartan parameters can be measured.** This reframes the problem: the wall is not about protecting quantum information (QEC) but about the fundamental metrological limit on estimating the spacetime parameters that the Gram matrix encodes.

12. **Riberi, Paz (2026)**
    *"Precision bounds for frequency estimation under collective dephasing and open-loop control"*
    arXiv:2603.23804, March 2026
    - **Claim:** Derives precision bounds for frequency estimation under collective dephasing with spatial correlations. Shows that precision is bounded by the quantum Fisher information, and the correlation structure determines the achievable precision.
    - **Relevance:** Direct connection between spatially correlated dephasing (the Gram decay structure) and Fisher information bounds. The Gram matrix determines the QFI, and the QFI determines the minimal achievable variance.

13. **Riberi (2025)**
    *"Entanglement-assisted metrology under spatiotemporally correlated quantum noise"*
    PhD Dissertation, Dartmouth College
    - **Claim:** Studies how dephasing-induced loss of quantum correlations affects metrological precision. Shows that spatial correlation structure of dephasing determines whether entanglement helps.
    - **Relevance:** For Gram decay, the PRODUCT structure G[a,b] = ∏_r cos(c·Δ_r)² means the "effective dephasing rate" grows multiplicatively with the number of causal rings. This sets a hard metrological bound that is independent of QEC considerations.

#### Why This Is Different

The metrology angle changes the GAME: instead of asking "can we protect quantum information from Gram decay?" (which standard QEC says yes for Pauli Z), ask "can we measure the Gram parameters (Cartan angles) with precision below the QFI bound?" The QFI bound is a FUNDAMENTAL limit that cannot be overcome by any measurement strategy, QEC or not.

If the Gram decay is simply Pauli Z dephasing, then the QFI for the Cartan parameters is determined by the cos² structure. But the PRODUCT over causal rings means the Fisher information for individual parameters DECAYS exponentially with ring count. This is a different kind of fundamental limit — one that QEC cannot help with, because QEC protects quantum INFORMATION, not metrological SENSITIVITY.

#### Actionable Research Question

"Compute the quantum Fisher information matrix for multiparameter estimation of Cartan angles {c_r} from the Gram decay channel, and prove whether the product structure G[a,b] = ∏_r cos(c·Δ_r)² imposes a fundamental metrological precision bound that no QEC scheme can circumvent."

---

## LOW-PROMISE ANGLES (but worth tracking)

### ANGLE 5: Holographic QEC Connection

**Rating: LOW (speculative but potentially transformative)**

#### Key Papers

14. **Harlow (2016/2017)**
    *"The Ryu-Takayanagi Formula from Quantum Error Correction"*
    Communications in Mathematical Physics 354, 865-912 (2017), arXiv:1607.03901
    - **Claim:** The Ryu-Takayanagi formula (which computes entanglement entropy in holography from bulk geometry) is a property of ANY quantum error-correcting code satisfying complementary recovery.
    - **Relevance:** The Gram matrix G[a,b] = ∏_r cos(c·Δ_r)² has a product-over-paths structure. In holographic QEC, entanglement wedge reconstruction involves product structures over bulk geodesics. There may be a formal mapping between Gram decay in the DGF and entanglement wedge reconstruction in AdS/CFT.

15. **Kibe, Mandayam, Mukhopadhyay (2022)**
    *"Holographic spacetime, black holes and quantum error correcting codes: A review"*
    European Physical Journal C 82, 463 (2022), arXiv:2110.14669
    - **Claim:** Reviews the connection between holographic bulk reconstruction and QEC, including state-dependence of reconstruction for black hole microstates.
    - **Relevance:** The Gram matrix's product-over-causal-rings structure may correspond to the iterative application of recovery maps in holographic codes. If so, Gram decay is not an error to be corrected but a FEATURE of the bulk-to-boundary encoding.

16. **Liu & Zhou (2023)**
    *"Approximate symmetries and quantum error correction"*
    npj Quantum Information 9, 119 (2023)
    - **Claim:** Approximate symmetries provide a framework for QEC. A "rotated dephasing channel" can be analyzed within this framework. Connects to black hole evaporation models formulated in terms of QEC.
    - **Relevance:** The Gram decay is exactly the kind of "rotated dephasing" that Liu & Zhou analyze. Their approximate symmetry framework may provide the right language for the Gram channel.

---

### ANGLE 6: Graph-Theoretic QEC Codes for Product-Structured Noise

**Rating: LOW (constructive/applied)**

#### Key Papers

17. **Duan & Guo (1999)**
    *"Quantum error correction with spatially correlated decoherence"*
    Physical Review A 59, 4058 (1999)
    - **Claim:** Spatial correlation in decoherence (described by a correlation function) can be handled by QEC if the code is matched to the correlation structure.
    - **Relevance:** This is the FOUNDING PAPER for QEC with correlated dephasing. The Gram decay is a specific instance: G[a,b] = ∏_r cos(c·Δ_r)². The question is whether a code EXISTS that matches this specific correlation structure.

18. **Wang, Liu, Liu, Gu, Baker, Chong et al. (2023)**
    *"DGR: Tackling drifted and correlated noise in quantum error correction via decoding graph re-weighting"*
    arXiv:2311.16214, 2023
    - **Claim:** Correlated errors in QEC can be handled by re-weighting the decoding graph edges based on estimated correlation parameters.
    - **Relevance:** The Gram decay correlation pattern is KNOWN (given by the causal ring topology). If the decoder knows the graph structure, it can potentially exploit it through graph re-weighting.

---

## SYNTHESIS: Attack Plan

### Dr. A (Formal Methods) — Attack Angles 1+4: Continuous Non-Pauli Structure

**Primary Attack Vector:** Prove that continuous, multiplicative Gram decay is fundamentally distinguishable from discrete Pauli Z dephasing at the formal level.

**Specific Strategy:**
1. Generalize Theorem 1-2 to NON-Cartan-aligned spin axes (Angle 4). Show that for generic DGF polynomials, the Gram channel is NOT diagonal in any single-qubit Pauli basis — it is a correlated non-Pauli channel.
2. Exploit the framework of Hines et al. (2026) to map the continuous, multiplicative Gram decay onto a detector error model, and compare the logical error rate against the Pauli Z approximation.
3. Apply the Kattemölle et al. (2026) result to show that any Pauli twirl of the Gram channel breaks Markovianity, proving the Pauli description is physically incomplete.
4. Use Beny-Oreshkov approximate QEC conditions (Angle 3) to compute the diamond-norm distance between the actual Gram channel and the best correctable Pauli Z channel — and show this distance is non-negligible for typical DGF parameters.

**Deliverable:** Theorem proving that "The continuous, multiplicative Gram decay channel with non-aligned spin axes is not equivalent to any Markovian Pauli channel, and the nearest correctable Pauli channel has diamond-norm distance scaling with the number of causal rings."

### Dr. B (Cross-Disciplinary Methods) — Attack Angles 6+5: Metrology + Holography

**Primary Attack Vector:** Reframe the problem from QEC to metrology, and explore holographic interpretations.

**Specific Strategy:**
1. Compute the quantum Fisher information matrix for the Gram decay channel (Angle 6), treating the Cartan parameters {c_r} as the unknown parameters. Show that the product-structure G[a,b] = ∏_r cos(c·Δ_r)² leads to exponentially decaying Fisher information with ring count, establishing a metrological no-go theorem.
2. Explore whether the product-over-paths structure of the Gram matrix has a natural interpretation in holographic tensor networks (Angle 5). Specifically, test whether Gram decay corresponds to "area operator" fluctuations in a holographic code.
3. Use the Omanakuttan et al. (2024) quantum metrology conditions to identify whether any probe state can simultaneously optimize sensitivity to all Cartan parameters — and prove impossibility.
4. Connect to the Ouyang-Brennen (2026) result on finite-round non-Markovian QEC: can adaptive, finite-round protocols circumvent the apparent QEC limit by treating Gram decay as non-Markovian signal rather than error?

**Deliverable:** Cross-disciplinary paper establishing that "The Gram decay product structure imposes a fundamental quantum Fisher information bound on Cartan parameter estimation, which is independent of QEC considerations and constitutes a genuine fundamental limit of the DGF framework."

### Fallback: Approximate QEC with Graph-Matched Codes (Angle 3+6)

If both primary attacks fail, the constructive fallback is to DESIGN a QEC code specifically matched to the Gram decay graph structure:

- Use LDPC codes with decoding graphs that match the causal ring topology
- Exploit the product structure for efficient syndrome extraction
- Target "good enough" approximate QEC rather than exact correction

---

## Supplementary: Key References Not Yet Investigated

These require deeper reading and should be pursued in Phase 2:

| Priority | Paper | Why |
|----------|-------|-----|
| TOP | Hines et al. 2026 (2603.18457) | Most direct evidence of non-Pauli QEC impact |
| TOP | Kattemölle et al. 2026 (2602.08464) | Pauli twirl breaks Markovianity |
| HIGH | Beny & Oreshkov 2010/2011 | Formal framework for approximate QEC |
| HIGH | Fern et al. 2006 | General theory of error propagation in concatenated codes |
| MEDIUM | Schwartzman 2025 (PRA 111, 022613) | Lindblad dynamics + QEC bounds |
| MEDIUM | Liu & Zhou 2023 (npj QI) | Approximate symmetries in QEC |
| MEDIUM | Maan et al. 2026 (Nat. Commun.) | Correlated errors in LDPC codes |
| TRACK | Riberi & Paz 2026 (2603.23804) | Collective dephasing metrology bounds |
| TRACK | Harlow 2016 (CMP) | RT formula from QEC |

---

## Verdict

The wall is real but surmountable. The Pauli Z dephasing equivalence proof is CORRECT under its stated assumptions (Cartan-aligned axes, Markovian Pauli twirl, discrete error model). But these assumptions do NOT hold for the actual DGF Gram decay channel, which is:
1. **Continuous and multiplicative** (not discrete probabilistic)
2. **Potentially non-Cartan-aligned** (for generic DGF polynomials)
3. **Graph-structured** (product over causal rings)

The two HIGH-promise angles exploit these gaps directly. Dr. A should attack the formal non-Pauli structure (Angles 1+4), and Dr. B should attack the metrological reframing (Angles 6+5). Both are genuinely new directions that the existing literature does not close off.
