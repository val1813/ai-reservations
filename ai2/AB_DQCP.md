# AB Validation: DQCP

**LP Candidate:** Is Deconfined Quantum Criticality Genuinely Continuous or Weakly First-Order?
**Date:** 2026-05-31
**Phase:** AB Validation (Phase 2), SELECTOR v2.0

---

## A-Doctor (Formal Attack)

### Step 0 -- Concept Check

**C1: "Deconfined quantum critical point" (DQCP)**

DEFINED, but with critical ambiguity. The term was introduced by Senthil, Vishwanath, Balents, Sachdev, and Fisher (Science, 2004) as a theoretical paradigm: a continuous quantum phase transition between two ordered phases breaking unrelated symmetries, where the critical theory is described by deconfined fractionalized excitations (spinons) coupled to an emergent U(1) gauge field. This is a well-defined theoretical concept.

However, the LP uses "DQCP" in THREE different senses without distinguishing them:
(a) The theoretical paradigm (a class of transitions with certain properties)
(b) The specific SU(2) candidate in the J-Q model on the square lattice
(c) The general phenomenon of "deconfined quantum criticality" that may appear in diverse settings (SU(N), non-Hermitian, field-driven)

The core contradiction between Propositions A and B is only well-posed if the referent is fixed. If A and B are about different instances of DQCP (e.g., A about SU(8) DQCP and B about SU(2) DQCP), there is no contradiction at all. The LP needs to specify: "the SU(2) DQCP between Neel and VBS in the J-Q model" -- or the analysis must be done separately for each instance.

**Verdict: Defined but ambiguous (tolerable; fix in L7). Not a category error.**

**C2: "Unitary CFT"**

DEFINED. In conformal field theory, unitarity means all states have positive norm (reflection positivity) and operator dimensions satisfy unitarity bounds (Delta >= d/2 - 1 for scalars, etc.). This is a mathematically precise concept. However, its APPLICATION to DQCP is precisely what is at issue. The phrase "described by a unitary CFT" in Proposition A is a HYPOTHESIS, not an established fact. The LP correctly frames this as part of Proposition A, so this is not a definitional problem per se.

**Verdict: Defined. Not a category error.**

**C3: "Weakly first-order"**

DEFINED OPERATIONALLY but lacks a sharp mathematical threshold. The term is used across the DQCP literature with the following operational meaning: a phase transition that exhibits (i) a small but non-zero order parameter discontinuity at the transition, (ii) a large but finite correlation length at the transition, (iii) pseudo-critical scaling over a wide range of scales, (iv) drifting effective exponents that never reach true fixed-point values, and (v) an underlying RG mechanism of fixed-point annihilation (merger into the complex plane). 

The running exponent diagnostic (D'Emidio, Eberharter, Lauchli, SciPost Physics 2023, arXiv:2106.15462) provides an operational test: [1/delta](lambda) drifts to zero for first-order but saturates to a finite universal value for continuous transitions.

However, the BOUNDARY between "weakly first-order" and "continuous with large corrections to scaling" is NOT mathematically sharp. At any finite system size or finite experimental resolution, a sufficiently weakly first-order transition is INDISTINGUISHABLE from a continuous one. The distinction only becomes sharp in the thermodynamic limit, which is inaccessible.

This is the deepest conceptual problem with the LP. If the correlation length at a weakly first-order transition is 10^6 lattice spacings, but our simulation reaches 10^3, we CANNOT distinguish A from B. The question "Is it A or B?" then becomes empirically undecidable at current capabilities.

**Verdict: Operationally defined but not sharply bounded from "continuous with large corrections." This is a genuine ambiguity, not a fatal category error. It affects the scoring of the core contradiction (see below).**

**C4: "Finite-size effects" in Proposition B**

The phrase "masked by finite-size effects" in Proposition B implies that the first-order character would be visible in the thermodynamic limit. But this raises the question: WHAT SIZE is required? If the correlation length at the transition is 10^6 and we can simulate 10^3, then B is TRUE but A is INDISTINGUISHABLE from truth at accessible scales. The LP's word "masked" presupposes B is true -- this is question-begging.

**Verdict: Circular phrasing. The LP's Proposition B is not a testable proposition but a methodological critique of Proposition A's evidence. This undermines the claim that A and B are symmetric alternatives.**

---

### Core Contradiction Attack

**Derivation of "both cannot be true":**

```
Step 1: Proposition A asserts that at the DQCP, the correlation length xi diverges (xi -> infinity)
        and the order parameter vanishes continuously. This is the definition of a continuous transition.
Step 2: Proposition B asserts that at the DQCP, the correlation length is finite (xi < infinity)
        and the order parameter has a non-zero discontinuity. This is the definition of a first-order transition.
Step 3: xi cannot be simultaneously infinite (Step 1) and finite (Step 2).
Step 4: Therefore, A and B cannot both be true.
```

**Stuck point analysis:**

The derivation APPEARS logically valid but breaks at **Step 2**, and the break reveals a deeper problem.

**Break at Step 2: Proposition B does not claim that xi IS finite at the transition point.** Proposition B claims that the APPARENT divergence of xi is an artifact of finite-size simulations, and that IN THE THERMODYNAMIC LIMIT, the transition would be first-order. This is an epistemological claim about the reliability of evidence for A, not a direct ontological claim about xi.

More precisely, the logical structure is:
- Proposition A: "The transition IS continuous" (ontological claim)
- Proposition B: "The evidence for continuity is misleading; the transition is actually weakly first-order" (epistemological + ontological claim)

These are ASYMMETRIC. Proposition B does not need to assert a specific finite value for xi; it only needs to assert that xi does NOT diverge in the thermodynamic limit -- something that NO finite-size simulation can verify. This means B is unfalsifiable at any given computational capability, while A IS falsifiable (if you find a finite xi in a large enough system).

**The real stuck position:**

The "both cannot be true" derivation is VALID for a given physical system at a given point in parameter space -- the transition either is or is not continuous. BUT:

1. For the SPECIFIC case of the SU(2) J-Q model DQCP, the 2024-2025 evidence decisively favors B (weakly first-order). The conformal bootstrap (Li 2018, JHEP 2022) excludes a unitary SO(5) CFT at lattice-observed scaling dimensions. The running exponent diagnostic shows drift to zero. The Nordic walking mechanism (Hawashin et al., Nature Comms 2025) provides an RG understanding of why it appears continuous but is first-order. Song et al. (Science Advances 2025) find that for N=2 (SU(2)), the anomalous logarithmic EE correction persists -- the smoking gun of non-conformality.

2. HOWEVER, this does NOT kill the DQCP PARADIGM -- it only establishes that the simplest (SU(2)) realization is weakly first-order. For SU(N) with N >= 8, Song et al. show that the anomalous log-correction VANISHES for smooth boundaries, and DQCP IS consistent with a unitary CFT (Abelian Higgs with N components). So the LP's framing as a binary A-vs-B about "the DQCP" conflates a specific instance with a theoretical paradigm.

3. The LP mentions the Takahashi-Sandvik claim about a "sign-problematic region" -- this is a MOVING TARGET. If continuous DQCP requires accessing parameters that are currently computationally inaccessible (sign-problematic), then Proposition A becomes "DQCP is continuous in an inaccessible region of parameter space," which is unfalsifiable for computationally different reasons.

**Score: 2 -- The stuck position itself is an interesting new question.**

The contradiction between A and B for the SU(2) case IS sharp and real (if we accept the 2024-2025 evidence, B is correct). But the stuck position is deeper:

> "If DQCP is weakly first-order for SU(2) but genuinely continuous for SU(N>=8), does the deconfined quantum criticality PARADIGM survive the falsification of its original candidate? And if the Nordic walking/complex CFT interpretation is correct, is 'weakly first-order DQCP' still a paradigm beyond Landau-Ginzburg-Wilson?"

This is a productive Polaris candidate: **"New Polaris candidate: Does deconfined quantum criticality as a paradigm require true continuity, or does weakly first-order pseudocriticality with emergent gauge fields and fractionalized excitations constitute a meaningful extension of the paradigm?"**

---

### Sub-proposition Attacks

#### S1 [Entanglement Diagnostic]

**Claim:** "Is the anomalous logarithmic subleading correction to entanglement entropy at smooth boundaries a robust diagnostic of weakly first-order behavior, or can it be explained by unconventional CFT features? Song et al. (2025) found log-correction vanishes for N>=8."

**Attack:**

The sub-proposition is well-posed. Let me check: is this a genuine diagnostic, or is it ambiguous?

Decomposition:
1. In a unitary CFT in d=2+1, the entanglement entropy for a region with smooth boundary scales as S = a*L - gamma + ... with NO logarithmic term (gamma is the topological entanglement entropy, a constant).
2. For a weakly first-order transition, an anomalous logarithmic subleading correction appears: S = a*L + s*log(L) + ... with s < 0 (or generically non-zero) even for smooth boundaries.
3. Song et al. find that for N=2,3,5,7, s != 0 (anomalous) for smooth boundaries, and for N>=8, s = 0.

**Where it breaks:**

The diagnostic is not model-independent. The D'Emidio-Sandvik 2024 PRL result shows that the anomalous logarithmic correction that PREVIOUSLY appeared in the J-Q model (with negative coefficient) was an ARTIFACT of the lattice bipartition geometry (cut along lattice axes). With a 45-degree tilted cut, the smooth-boundary log-correction vanishes even for N=2, and the corner log-coefficient matches the SO(5) CFT prediction (a_s = 0.131(5) vs. prediction 0.12975).

This means: (a) the diagnostic is sensitive to microscopic details of how the entanglement cut is made, and (b) the Song et al. result might ALSO be sensitive to their specific bipartition choice. The diagnostic is real but requires careful control of lattice artifacts.

**Additionally:** The "anomalous log-correction" interpretation assumes that the absence of such a correction is NECESSARY for a unitary CFT. But this is true only for smooth boundaries. What if the CFT has an unconventional boundary condition that generates a log term? The boundary CFT of DQCP could have features (self-duality, topological terms) that make the standard CFT boundary analysis inapplicable.

**Score: 2** -- The diagnostic IS genuinely useful but not yet proven to be completely robust. The stuck position -- "How do we know the entanglement bipartition isn't introducing artifacts?" -- is itself a productive research question that the D'Emidio-Sandvik paper partly resolves but does not close for arbitrary lattice models.

---

#### S2 [Sign Problem Crossing]

**Claim:** "Can the sign-problematic region of the extended J-Q model (where Takahashi & Sandvik claim true SO(5) DQCP resides) be accessed via new numerical methods (NQS, tensor networks, quantum computing)?"

**Attack:**

Decomposition:
1. Takahashi, Shao, Zhao, Guo, and Sandvik (2024) claim that in an extended J-Q model with multi-spin interactions (J-Q_n for n=2,3), the AFM-VBS transition is first-order, with discontinuity increasing with n. 
2. They identify a MULTICRITICAL point with emergent SO(5) symmetry that potentially hosts genuine continuous DQCP.
3. This multicritical point lies in a region of parameter space with a sign problem, making it inaccessible to standard QMC.
4. The sub-proposition asks whether new methods (NQS, tensor networks, quantum computing) can cross the sign problem barrier.

**Where it breaks:**

Step 3 is problematic. The claim that the "true SO(5) DQCP" resides in a sign-problematic region is a SPECULATION -- it is not empirically established. It is a "DQCP of the gaps" argument: "The DQCP IS continuous, but you can't see it because it's in an inaccessible region of parameter space." This is structurally similar to arguments about SUSY being broken at the Planck scale.

Furthermore:
- NQS (neural quantum states) currently cannot reach the system sizes needed to resolve weakly first-order transitions (the correlation length at the transition exceeds what NQS can represent).
- Tensor networks in 2D are limited by area-law entanglement; at a critical point (even weakly first-order), the logarithmic entanglement scaling violates area law, making tensor network methods inefficient.
- Quantum computing: the system sizes accessible on near-term quantum computers (50-100 qubits) are far below what's needed to distinguish continuous from weakly first-order (need hundreds of lattice sites, each requiring multiple qubits).

The sub-proposition is asking about a RESEARCH PROGRAM ("can we develop methods to access...?") rather than a falsifiable proposition. As a research direction it is valuable, but as a testable sub-proposition it scores poorly.

**Score: 1** -- Stuck but circumventable. The sub-proposition's framing as "can we access..." rather than "does it exist..." makes it about computational feasibility, not physics. The more interesting question is: "If the true continuous DQCP requires fine-tuning to a multicritical point in a sign-problematic region, is it physically meaningful?" That is a Polaris candidate.

---

#### S3 [Experimental Realization]

**Claim:** "Can SrCu2(BO3)2 under magnetic field or other candidate platforms provide a definitive experimental test distinguishing continuous from weakly first-order?"

**Attack:**

Decomposition:
1. An experiment can distinguish continuous from first-order if it can measure either (a) latent heat, (b) order parameter discontinuity, (c) correlation length divergence vs. saturation, at the transition.
2. SrCu2(BO3)2 is a candidate material: the Shastry-Sutherland lattice compound with plaquette-singlet to antiferromagnetic transition under pressure and/or magnetic field.
3. Guo et al. (Communications Physics 2025): zero-field pressure-driven PS-to-AF transition is clearly first-order -- latent heat observed, phase coexistence seen. DQCP "lost."
4. Cui et al. (arXiv:2411.00302, 2025): two distinct plaquette-singlet phases, field-driven transition from empty-plaquette to AFM shows DQCP scaling (1/T1 ~ T^0.6).

**Where it breaks:**

Step 3 and 4 are in tension. Guo et al. find first-order; Cui et al. find a DIFFERENT transition (field-driven, different PS phase) that appears continuous. The question "can SrCu2(BO3)2 resolve the A-vs-B debate" is answered YES by Guo et al. (it did -- first-order for one transition) but the answer is NEGATIVE for the broader question because the field-driven pathway shows different behavior.

The stuck point: "Definitive experimental test" faces the same finite-resolution problem as simulations. Guo et al.'s measurement reached 0.4 K at 3.1 GPa -- impressive, but still finite temperature. If the latent heat were 100x smaller, they wouldn't see it. So the experiment falsifies "strongly continuous" DQCP but cannot rule out "extremely weakly first-order."

Furthermore, the experimental debate is actually between two DIFFERENT transitions in the SAME material (zero-field vs. field-driven PS-to-AF). This suggests the DQCP question may not have a single answer even for a single compound.

**Score: 1** -- Stuck but circumventable. The experimental question is real but the framing as "a definitive test" is naive. The material has multiple transitions with different characters. A more precise sub-proposition would be: "Does the field-driven EP-to-AF transition in SrCu2(BO3)2 represent a genuine continuous DQCP, as suggested by Cui et al.?"

---

#### S4 [Complex DQCP]

**Claim:** "If SU(2) DQCP is weakly first-order in real parameter space, does it become genuinely continuous in complex (non-Hermitian) extensions? (Zou et al., arXiv:2511.03456, 2025)"

**Attack:**

Decomposition:
1. If the weakly first-order character of DQCP comes from fixed-point annihilation (two real fixed points merge and move into the complex plane), then the ghost of the real fixed points persists as a pair of complex-conjugate fixed points (complex CFTs).
2. The complex CFT framework (Gorbenko, Rychkov, Zan, JHEP 2018) predicts that near the annihilation point, the RG flow is slow ("walking"), producing pseudo-critical behavior.
3. Zou et al. construct a non-Hermitian easy-plane J-Q model (no sign problem for QMC) and show that increasing non-Hermiticity WEAKENS the first-order character, suggesting approach to a complex fixed point described by a non-unitary CFT.

**Where it breaks:**

Step 3 has a subtle problem. The non-Hermitian model is sign-problem-free for QMC -- but SO IS the standard Hermitian J-Q model. The non-Hermiticity does not solve the sign problem; it introduces a DIFFERENT parameter (non-Hermitian coupling) that tunes the system CLOSER to criticality. This is interesting physics but does not directly answer whether "real" DQCP becomes continuous in complex space.

The DEEPER question is: does a complex CFT (non-unitary) count as a "genuinely continuous" DQCP? In the complex CFT framework, the physical (real-coupling) transition IS first-order, and the continuous fixed point exists only at COMPLEX couplings -- which are physically inaccessible. The non-Hermitian extension makes the complex coupling PHYSICAL (since non-Hermitian Hamiltonians have complex parameters), but the resulting theory is non-unitary.

If "continuous DQCP" means "described by a unitary CFT at physically accessible real couplings," then S4's answer is NO -- complex DQCP in non-Hermitian systems is continuous but non-unitary, which violates Proposition A's "unitary CFT" clause. If "continuous DQCP" just means "diverging correlation length, no latent heat," then S4's answer is potentially YES -- but in a different (non-unitary) physical setting.

**Score: 2** -- The sub-proposition uncovers a genuinely new question: "What does it mean for a phase transition to be 'continuous' if the fixed point lies in complex coupling space?" This connects to broader questions about analytic continuation in quantum many-body physics and the physical interpretation of complex CFTs. **New Polaris candidate: "Can complex CFT fixed points (non-unitary, in complex coupling space) generate physically observable universal scaling in real-coupling systems undergoing weakly first-order transitions?"**

---

## B-Doctor (Cross-Domain Attack)

### Core Contradiction Attack

**Cross-domain connection: Conformal Bootstrap x High-Energy Physics x DQCP = The "complex CFT/walking" framework unifies weakly first-order transitions across condensed matter and particle physics via fixed-point annihilation.**

**Detailed reasoning:**

The conformal bootstrap (Zhijin Li, JHEP 2022, arXiv:1812.09281) provides a FROM-OUTSIDE attack on Proposition A. The bootstrap does not simulate a specific lattice model -- it asks: "Assuming unitarity, SO(5) global symmetry, and a given spectrum of low-lying operators, does there EXIST any unitary CFT in 2+1D that could describe the transition?" The answer is NO: the bootstrap gives a lower bound Delta_phi >= 0.79 for the SO(5) vector, while all lattice estimates for the DQCP candidate fall in [0.60, 0.68]. Therefore, IF the transition is continuous, it CANNOT be both unitary and SO(5)-symmetric simultaneously.

This is a cross-domain attack because it uses the mathematical framework of the conformal bootstrap (developed primarily in high-energy theory for constraining CFTs) to constrain a condensed-matter phenomenon. The bootstrap is agnostic to microscopic details -- it only cares about symmetry, unitarity, and crossing symmetry. This means it provides a MODEL-INDEPENDENT constraint that lattice simulations cannot evade.

However, the bootstrap attack has a loophole: it ASSUMES unitarity. If the DQCP is described by a COMPLEX (non-unitary) CFT, the bootstrap constraints do not apply. This is precisely the resolution offered by the Gorbenko-Rychkov-Zan framework (JHEP 2018): the DQCP is weakly first-order because the real fixed points have annihilated and moved into the complex plane, leaving behind a "walking" RG flow that appears conformal at intermediate scales.

From high-energy physics, this is the EXACT SAME mechanism that explains:
- The conformal window in QCD-like gauge theories (walking technicolor): as the number of flavors decreases, the IR fixed point annihilates with another fixed point, and the theory becomes confining with a large but finite correlation length (Miransky scaling).
- The 2D Potts model for Q > 4: the phase transition goes from continuous (Q <= 4) to weakly first-order (Q > 4) via fixed-point annihilation.

The DQCP is thus the condensed-matter analog of "walking technicolor" or "near-conformal QCD": a theory that appears almost conformal (giving rise to pseudo-critical scaling, deconfined spinons, emergent SO(5)) but is ultimately gapped/confined/first-order at the longest scales.

This cross-domain connection STRENGTHENS the LP because it shows that the A-vs-B tension in DQCP is not an isolated problem but an instance of a UNIVERSAL mechanism across physics. The question "continuous or weakly first-order?" is the condensed-matter version of "conformal or confining?" in high-energy gauge theories.

**Score: 2 -- Cross-domain attack reveals the LP's question is a specific instance of a universal RG phenomenon, but also shows that A and B are NOT simple alternatives: the weakly first-order interpretation (B) is RICHER than a simple "it's just first-order" because it preserves pseudo-critical phenomena with emergent symmetries. New Polaris: "Does the complex CFT/walking mechanism provide a unified framework for understanding all weakly first-order transitions as proximity to fixed-point annihilation, and what are its universal experimental signatures?"**

---

### Sub-proposition Attacks (B-Doctor)

#### S1 [Entanglement Diagnostic]

**Cross-domain: Quantum Information x DQCP = Entanglement entropy as a phase transition diagnostic is model-dependent; the bipartition geometry problem (D'Emidio-Sandvik) is a quantum information problem about subsystem choices, not a condensed matter problem about criticality.**

The D'Emidio-Sandvik 2024 resolution of the anomalous EE sign shows that the diagnostic is not purely about the transition order -- it is about the INTERACTION between the entanglement cut and the emergent order. In quantum information terms: the reduced density matrix of a subsystem depends on how the subsystem boundary treats different VBS patterns. This is a feature of ANY diagnostic based on spatial bipartition: the bipartition itself can break the symmetry that one is trying to detect.

This connects to the broader quantum information literature on symmetry-resolved entanglement and entanglement-based diagnostics of topological order. The lesson is that entanglement-based diagnostics of phase transitions are POWERFUL but must be interpreted with careful attention to the symmetry properties of the partition.

**Score: 2** -- Cross-domain insight: the "anomalous" logarithmic correction may not be a property of the transition but of the MEASUREMENT PROTOCOL (the entanglement cut). This is a quantum information insight that condensed matter physicists often overlook.

---

#### S2 [Sign Problem Crossing]

**Cross-domain: Computational Complexity Theory x DQCP = The sign problem is not just a technical inconvenience; it is a COMPLEXITY BARRIER (#P-hard for worst-case instances). Claiming "true DQCP is behind the sign problem barrier" may be claiming it is computationally undecidable.**

From computational complexity: the fermionic sign problem is #P-hard in the worst case (Troyer and Wiese, PRL 2005). This means that any method claiming to "solve" the sign problem for general sign-problematic Hamiltonians would imply P = #P (or BQP = #P for quantum computing). While specific instances may be tractable, the general problem is believed to be exponentially hard.

This does not mean the sign-problematic DQCP is inaccessible -- it means that IF the continuous DQCP lives exclusively in a region that is sign-problematic, AND no sign-problem-free reformulation exists, THEN the question "is DQCP continuous?" may be COMPUTATIONALLY UNDECIDABLE at current complexity-theoretic understanding. This is a deep cross-domain constraint that the LP does not address.

Neural quantum states, tensor networks, and quantum computers each face specific complexity-theoretic barriers: NQS optimization is NP-hard in general; 2D tensor network contraction is #P-hard; quantum computers would need to overcome the sign problem via quantum phase estimation, which has its own exponential scaling with precision.

**Score: 1** -- The sub-proposition's computational framing is naive about complexity-theoretic barriers. The deeper cross-domain question is: "Is the existence of continuous DQCP in the sign-problematic region of the J-Q model computationally decidable?"

---

#### S3 [Experimental Realization]

**Cross-domain: Materials Science/High-Pressure Physics x DQCP = The experimental question is not "can SrCu2(BO3)2 resolve the debate" but "how many candidate materials and experimental probes are needed to build a statistically convincing case, given that ANY single experiment faces the finite-resolution problem?"**

The classic resolution template from classical statistical mechanics is WEAK CRYSTALLIZATION theory (Brazovskii 1975, Kats-Lebedev-Muratov 1993). In weak crystallization, the liquid-to-crystal transition IS first-order (due to cubic invariants and fluctuation effects), but can be arbitrarily weak near specific points in the P-T plane. The pre-transitional fluctuations show critical-like scaling with anomalously large exponents.

The key cross-domain insight: in weak crystallization theory, it took DECADES of study across MANY materials to establish that these were first-order transitions with pseudo-critical pre-transitional effects, not genuinely continuous transitions. A SINGLE experiment on a SINGLE material could not have resolved the question. The RESOLUTION came from the ACCUMULATION of evidence across many systems, combined with a theoretical framework (Brazovskii's Ginzburg-Landau + fluctuation theory) that explained how first-order and pseudo-critical features coexist.

Applied to DQCP: the lesson is that SrCu2(BO3)2 alone cannot provide a "definitive" test. The resolution, if it comes, will come from a CONSILIENCE of experiments on multiple platforms (Shastry-Sutherland, kagome, triangular lattices) combined with theoretical understanding (Nordic walking, complex CFTs). The Guo et al. and Cui et al. papers together are valuable not because either is definitive, but because their TENSION (different results for different transitions in the same material) reveals the richness of the physics.

**Score: 1** -- The sub-proposition's framing as a "definitive test" from one material is inconsistent with the history of how analogous debates were resolved in classical statistical mechanics. The realistic pathway is consilience across multiple systems.

---

#### S4 [Complex DQCP]

**Cross-domain: Non-Hermitian Physics x CFT x DQCP = Complex extensions of DQCP connect to the broader program of understanding phase transitions with non-Hermitian/PT-symmetric Hamiltonians, where the standard classification of phase transitions (first-order vs. continuous) may need to be extended.**

The non-Hermitian extension (Zou et al. 2025) is part of a broader revolution in non-Hermitian quantum physics. Key cross-domain insights:

1. Non-Hermitian criticality has its OWN classification, with exceptional points, the non-Hermitian skin effect, and modified scaling relations. A "continuous" transition in a non-Hermitian system may belong to a DIFFERENT universality class than any Hermitian transition.

2. The notion of "unitarity" in non-Hermitian systems is replaced by PT-symmetry or pseudo-Hermiticity. The complex CFT that describes the non-Hermitian DQCP is non-unitary in the standard sense but may satisfy modified consistency conditions.

3. From the conformal bootstrap perspective: extending the bootstrap to non-unitary CFTs (complex scaling dimensions allowed) would remove the unitarity bound (Delta_phi >= 0.5) and potentially allow the lattice-observed scaling dimensions. This is an open research program -- no one has done a full non-unitary bootstrap for SO(5) or related symmetries.

**Score: 2** -- Cross-domain insight: if the DQCP fixed point lives at complex couplings, then making it physically accessible via non-Hermitian Hamiltonians changes the universality class. The resulting transition is "continuous" in the non-Hermitian sense but may not satisfy the standard definition of a continuous phase transition (it may have exotic features like complex-conjugate pairs of scaling dimensions). This produces a genuinely new question about how to CLASSIFY phase transitions in non-Hermitian systems.

---

## AB Score Summary

| Item | A | B | Total | Survive? (>=4/6 or A=2/B=2) |
|------|---|---|-------|------|
| Core | 2 | 2 | **4/6** | **YES** (A=2, B=2) |
| S1 | 2 | 2 | **4/6** | **YES** (A=2, B=2) |
| S2 | 1 | 1 | **2/6** | **NO** -- needs reformulation |
| S3 | 1 | 1 | **2/6** | **NO** -- needs reformulation |
| S4 | 2 | 2 | **4/6** | **YES** (A=2, B=2) |

**Overall LP survival: CONDITIONAL PASS** (3 of 5 items survive, core survives)

---

## Recommendation

**FIX** -- not KILL, not PASS as-is. The LP's core contradiction and the two strongest sub-propositions (S1 and S4) survive AB validation. The core question about whether DQCP is continuous or weakly first-order is a PRODUCTIVE, real, and unresolved (for the paradigm as a whole) scientific tension, even though the specific SU(2) case is largely settled as weakly first-order.

**Required fixes before L7 decomposition:**

1. **Fix the referent ambiguity:** The LP must specify whether it is asking about:
   - (a) The SU(2) DQCP in the standard J-Q model (largely settled: weakly first-order);
   - (b) The SU(N) DQCP for general N (settled: N>=8 continuous, N<8 weakly first-order per Song et al. 2025);
   - (c) The DQCP PARADIGM as a class of transitions (productive open question: does the paradigm require continuity, or does pseudocriticality with fractionalization suffice?).

   Recommend: focus on (c), using (a) and (b) as case studies.

2. **Drop or reformulate S2 and S3:** These scored 2/6 each. S2 is about computational feasibility, not physics. S3's framing as a single "definitive test" is inconsistent with the historical resolution of analogous debates. Reformulate as:
   - S2': "Does the multicritical SO(5) point identified by Takahashi & Sandvik (2024) in the extended J-Q model provide a genuine continuous DQCP, and if so, what are its universal properties?"
   - S3': "What observable in SrCu2(BO3)2 or other candidate materials would UNEQUIVOCALLY distinguish weakly first-order from continuous behavior, given finite experimental resolution?"

3. **Define "weakly first-order" precisely:** For L7, the LP needs to specify operational criteria: what correlation length threshold, what latent heat threshold, what drift rate in running exponents counts as "weakly first-order" vs. "continuous"? The D'Emidio-Eberharter-Lauchli running exponent diagnostic (SciPost 2023) provides a quantitative framework.

4. **Incorporate the complex CFT cross-domain insight:** The strongest finding from B-Doctor is that the A-vs-B binary is dissolved by the complex CFT/walking framework. A "weakly first-order" DQCP IS a physical manifestation of a complex CFT -- it is MORE than just a failed continuous transition. The LP should explicitly address whether "complex CFT-controlled pseudocriticality" is a viable THIRD option beyond the A/B binary.

**New Polaris candidates generated by this AB validation:**

1. "Does deconfined quantum criticality as a paradigm require true continuity, or does weakly first-order pseudocriticality with emergent gauge fields and fractionalized excitations constitute a meaningful extension of the paradigm?" (from Core)

2. "Can complex CFT fixed points (non-unitary, in complex coupling space) generate physically observable universal scaling in real-coupling systems undergoing weakly first-order transitions?" (from S4)

3. "Is the transition between weakly first-order DQCP and truly continuous DQCP as a function of N (number of spin components) itself a novel universality class?" (from S1)

---

**References consulted:**

- Senthil et al., Science 303, 1490 (2004) -- DQCP original definition
- Li, JHEP 11, 005 (2022), arXiv:1812.09281 -- Conformal bootstrap of SO(5) DQCP
- Gorbenko, Rychkov, Zan, JHEP 10, 108 (2018), arXiv:1807.11512 -- Walking, weak first-order transitions, complex CFTs
- Song et al., Science Advances 11, eadr0634 (2025), arXiv:2307.02547 -- SU(N) EE at DQCP, N_c ~ 7-8
- Hawashin et al., Nature Communications 16, 20 (2025), arXiv:2312.11614 -- Nordic walking mechanism
- D'Emidio & Sandvik, PRL 133, 166702 (2024), arXiv:2401.14396 -- Tilted cut EE, SO(5) CFT match
- D'Emidio, Eberharter, Lauchli, SciPost Physics (2023), arXiv:2106.15462 -- Running exponent diagnostic
- Takahashi, Shao, Zhao, Guo, Sandvik (2024) -- SO(5) multicriticality in J-Q models
- Guo et al., Communications Physics 8, 75 (2025) -- DQCP lost in pressurized SrCu2(BO3)2
- Cui et al., arXiv:2411.00302 (2025) -- Two PS phases, field-driven DQCP in SrCu2(BO3)2
- Zou, Yin, Li, Yao, arXiv:2511.03456 (2025) -- Non-Hermitian DQCP
- Brazovskii, JETP 41, 85 (1975); Kats, Lebedev, Muratov, Phys. Rep. 228, 1 (1993) -- Weak crystallization theory
