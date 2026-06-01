## AB Validation: Macroscopic Quantum Decoherence — Environmental Noise vs Intrinsic Limit

---

### A-Doctor (Formal Attack)

**Step 0 — Concept Check:**

The LP rests on four core concepts. Each is examined for precision and empirical anchoring.

**Concept 1: "Macroscopic quantum coherence" — precisely defined?**

No. This concept is fundamentally ambiguous. The LP references "~10^9 electrons in coherent superposition" for superconducting qubits, but this is the naive carrier count. Rigorous microscopic analysis by Korsbakken, Wilhelm & Whaley (2009/2010, arXiv:1003.5294) using the actual fermionic many-body wavefunction shows that the number of electrons in *distinguishably different states* between the two superposition branches is only ~10^1--10^3. The supercurrent involves billions of Cooper pairs, but Fermi statistics and the small ratio of superfluid velocity to Fermi velocity mean that only a thin sliver of electrons near the Fermi surface are actually displaced. There is no sharp, agreed-upon numerical threshold separating "microscopic" from "macroscopic" — this is a long-standing debate in quantum foundations (Leggett 2002, "Testing the limits of quantum mechanics: motivation, state of play, prospects"). The LP's reliance on "N = 10^9" as a benchmark for macroscopicity is misleading because the effective superposition size is 6--7 orders of magnitude smaller.

Severity: **Moderate.** The ambiguity does not kill the LP outright — the qualitative question about scaling coherence with system size remains well-posed — but it means SP4 ("Scaling with system size") must be reframed from "N ~ 10^9 → 10^12-10^15" to a more careful measure of superposition size. The LP's framing conflates carrier count with entanglement depth, overstating how "macroscopic" current experiments actually are.

**Concept 2: "Intrinsic decoherence" — well-defined physical concept?**

Partially. The term bifurcates into two distinct meanings in the literature:

- **(a) Intrinsic as fundamental new physics**: Modifications to the Schrodinger equation itself (GRW collapse, CSL, Diosi-Penrose gravitational collapse) that introduce irreducible stochasticity not describable as system-environment coupling within standard QM. These are sharply defined — they make specific quantitative predictions with free parameters (λ_CSL, r_C, etc.).

- **(b) Intrinsic as material-immanent limit**: Decoherence channels that arise from physical mechanisms inherent to the device/material (quasiparticles in disordered superconducting gaps, spontaneous emission from cavity modes, chaos-assisted tunneling) but are NOT modifications to QM itself. These are "intrinsic" to particular realizations but are fully described by standard open quantum systems theory.

The LP slides between these two meanings. Proposition B lists mechanisms from both categories side by side (spin-bath decoherence at T=0, zero-point fluctuations are category (b); gravitational decoherence, GRW collapse are category (a)). This conflation matters profoundly: category (b) limits are specific to particular materials/designs and can potentially be engineered around; category (a) limits are claims about the structure of physical law.

Danelli & Paris (EPL 149, 50001, February 2025) provide the most rigorous recent treatment: they define Intrinsic Decoherence Models (IDMs) as models "where decoherence emerges from temporal evolution rather than interaction with an external environment" and use quantum estimation theory to prove these models ARE falsifiable. This supports the LP's claim that intrinsic vs. environmental decoherence can be distinguished in principle — but the paper is restricted to two simple models (intrinsic dephasing, intrinsic dissipation) in two-level systems and harmonic oscillators. Generalization to arbitrary architectures is not provided.

Severity: **Moderate-High.** The conflation of category (a) and (b) "intrinsic" decoherence is a structural weakness. The LP addresses a meaningful question, but the question needs to be disambiguated: "Is there fundamental (QM-modifying) intrinsic decoherence?" is a different scientific problem from "Are there irreducible material-specific decoherence channels in superconducting qubits?"

**Concept 3: "Caldeira-Leggett model" — precise domain of validity?**

Yes, this is well-understood. The CL oscillator-bath model assumes: (i) harmonic bath oscillators, (ii) bilinear system-bath coupling, (iii) Gaussian noise statistics, (iv) Born-Markov approximation for master equation derivations, (v) weak perturbation of individual bath modes. Proven limitations include: inability to capture non-Gaussian noise, absence of "topological terms" that produce decoherence without dissipation (Prokof'ev & Stamp's spin bath), bounded spectra of spin environments, and anharmonic system potentials where the invertibility problem arises (Ivanov et al. 2014).

However, Halataei (2025, Scientific Reports, "Toward the universality of the Caldeira-Leggett oscillator bath") has significantly expanded the recognized domain. He demonstrates that many effects previously claimed unique to spin baths (pure dephasing without dissipation, relaxation rate decreasing with bias) can be reproduced by the CL model with appropriate non-trivial spectral densities. The CL model is "broader and more universal than previously recognized." The key debate is about whether the genuinely *strong*-coupling, *finite* spin bath regime lies inside or outside the CL universality class — Halataei acknowledges this remains open.

Severity: **Low.** The CL model has a well-characterized domain. The LP correctly identifies that its adequacy is contested.

**Concept 4: "Six orders of magnitude discrepancy" (Stamp 2006) — still valid in 2026?**

No, this claim is empirically outdated to the point of being misleading.

The historical timeline of superconducting qubit coherence:
- 1999-2002: T_2 ~ 1-10 ns (first charge/flux qubit demonstrations)
- ~2005: T_2 ~ 500 ns (quantronium, Vion et al., Saclay)
- ~2010: T_2 ~ 1-5 μs (3D transmon, Paik et al., Yale)
- ~2015: T_2 ~ 100 μs (planar transmons, Martinis/Google)
- ~2020: T_2 ~ 300 μs (advanced transmons)
- 2025: T_2 > 1 ms = 1,000 μs (Princeton, Houck & de Leon, Nature Nov 2025; Aalto/VTT Finland, Nature Communications 2025)

From ~1 ns to ~1 ms represents **exactly six orders of magnitude** of improvement — achieved entirely through environmental engineering: better materials (Ta replacing Al, Si replacing sapphire), cleaner fabrication (etch-resistant materials), improved shielding, smarter qubit design (3D cavities, transmons, Purcell filters). No new physics was needed. Every improvement came from identifying and suppressing a specific environmental decoherence channel (TLS defects in amorphous surface oxides, non-equilibrium quasiparticles, stray EM fields).

If Stamp's 2006 discrepancy was between CL predictions and measured decoherence at that time, the intervening 20 years of experimental progress have effectively closed that gap through systematic elimination of environmental noise sources. The residual discrepancy, if it exists, is now at the level of specific material bounds (Charpentier et al. 2025/2026: universal quasiparticle dissipation bound in disordered superconductors) rather than a generic six-order mystery.

Severity: **Critical.** The LP's rhetorical framing depends on this gap being a standing anomaly pointing to new physics. In 2026, it is better described as a engineering problem where steady progress has tracked CL predictions once unknown environmental channels were identified and suppressed.

---

**Core Contradiction Attack:**

The LP frames two propositions as mutually exclusive: "If decoherence is entirely environmental, coherence times should diverge with sufficient isolation. If intrinsic decoherence exists, a saturation floor exists that no engineering can breach."

This framing contains a logical error: the two propositions are NOT mutually exclusive in the way presented. A system can simultaneously have (a) environmental decoherence channels that can be progressively eliminated AND (b) some irreducible floor at much longer timescales. Empirically, we have no evidence that we have reached such a floor. The ms-scale coherence is limited by known, identifiable, environment-adjacent mechanisms (surface dielectric loss, quasiparticle poisoning, radiative loss), not by unknown fundamental limits.

**Step-by-step decomposition:**

(1) Premise: "CL model captures all relevant decoherence channels."
(2) If (1) true, then eliminating all CL-modeled environmental couplings → arbitrarily long coherence.
(3) Observation: Coherence has improved 6 orders of magnitude purely through environmental engineering.
(4) We have NOT reached any apparent saturation floor — progress continues with each new materials improvement.
(5) Therefore: The LP's proposed contradiction is not empirically motivated. We don't know if a floor exists because we haven't exhausted the CL channels yet.

**First break point:** (3). The empirical trend over 25 years shows no sign of asymptotic saturation. Each new decoherence mechanism identified turns out to be environmental in a progressively more refined sense. The burden of proof is on Proposition B to show a specific mechanism that would survive all plausible environmental elimination strategies — and of the candidates listed, the parameter-free Diosi-Penrose model (the strongest B-candidate as an actual QM modification) has been ruled out by diffusion measurements (Donadi 2025).

However, because the logical possibility of Proposition B is not logically excluded (it is just empirically unmotivated at present), this is NOT a category error.

**Score: 1** — Stuck (the core contradiction is not actually contradictory at the current experimental frontier) but circumventable (the question can be reframed as: "What are the observational signatures that would distinguish saturation due to an intrinsic limit from diminishing returns on environmental engineering?")

---

**Sub-proposition Attacks:**

**SP1 [Adequacy of Caldeira-Leggett]:**
**Score: 2** — The question is well-posed and its answer has shifted substantially in 2024-2025. Halataei's work demonstrating that many claimed unique spin-bath effects are reproducible with appropriate CL spectral densities constitutes a genuine development. The open question — whether the strong-coupling finite spin bath regime lies inside or outside the CL universality class — is precise, falsifiable, and connects to concrete experiments (molecular magnets, rare-earth spin systems). This is a genuine research frontier, not a stale debate. The LP's framing correctly identifies a live question. However, the LP slightly overstates the "systematic omissions" side — the 2025 evidence leans toward CL having broader universality than previously claimed, narrowing rather than widening the gap.

**SP2 [Macrorealism tests — Leggett-Garg inequality]:**
**Score: 2** — This sub-proposition is empirically validated and theoretically sharp. The 2025 demonstrations of LGI violation on IBM superconducting qubits at >5σ (Rybotycki et al. EPJ Quantum Tech, July 2025) AND extreme violations beyond the temporal Tsirelson bound (Chatterjee et al. PRL Nov 2025) confirm that LGI violations are robustly observable. However, the LP's specific framing ("Would a definitive Leggett-Garg inequality violation with N > 10^9 electrons rule out all macrorealistic alternatives, or do loopholes persist?") has a precise answer from the existing literature: LGI violations have already been demonstrated, and the remaining loopholes (clumsiness loophole, noninvasive measurability) have been addressed by the quantum nondemolition measurement protocol (Genova group, Phys. Rev. A May 2025) and by using genuinely noninvasive weak measurements on real hardware. The "N > 10^9" framing is a red herring — as discussed under Concept 1, the effective superposition size is much smaller. SP2 is a well-structured question with answerable components using 2025 data.

**SP3 [Intrinsic decoherence falsification — Danelli-Paris framework]:**
**Score: 2** — Danelli & Paris (2025) provide exactly the theoretical framework the LP asks for, proving that intrinsic dephasing and intrinsic dissipation models ARE falsifiable via quantum estimation theory. The optimal conditions they derive (effective evolution time ~ inverse of IDM parameters, maximum initial coherence) provide a concrete experimental recipe. However, the framework is currently limited to simple systems (two-level system, harmonic oscillator). Mapping it onto "realizable architectures" is precisely the next step — a genuine and tractable research problem. This is the strongest sub-proposition. Score 2 because the question maps directly onto a recently published theoretical framework that provides falsifiability criteria, AND the next step (extension to multi-qubit architectures) is non-trivial but well-defined.

**SP4 [Scaling with system size — N ~ 10^12-10^15]:**
**Score: 1** — This sub-proposition has two problems. First, as discussed under Concept 1, "N" conflates total carrier count with effective superposition size. The relevant "N" for decoherence scaling is the number of degrees of freedom in distinguishably different states, which for superconducting qubits is vastly smaller than the total electron count. Second, the claim that intrinsic decoherence "would dominate" at N ~ 10^12-10^15 is unsupported extrapolation from an already-question-begging premise. If the decoherence mechanisms that dominate at N ~ 10^3 are environmental, there is no theoretical principle that requires a transition to intrinsic mechanisms at larger N — it depends on the scaling of environmental coupling with system size, which is platform-specific. The Charpentier et al. (2025) universal quasiparticle bound is already a scaling limit, but it is a material-science limit, not a QM-modifying limit. SP4 is stuck (extrapolates from an unresolved question to a speculative claim) but can be circumvented by reframing in terms of specific decoherence channel scaling (e.g., how do surface participation ratios scale with qubit size?).

---

### B-Doctor (Cross-Domain Attack)

**Core Contradiction Attack:**
**Score: 1**
Cross-domain connection: **Quantum Error Correction (surface codes, fault-tolerant thresholds) x Macroscopic Decoherence = Sharp criterion.**

The threshold theorem in quantum error correction provides the most powerful framework for evaluating this LP. The theorem states: if physical error rates are below a code-specific threshold, logical error rates can be exponentially suppressed by increasing code distance. The implication for the LP's core contradiction: if Proposition A is true (decoherence is entirely environmental with no intrinsic floor), then ANY physical error rate, no matter how close to the threshold, can achieve arbitrarily low logical error rates *if the noise is sufficiently understood and modeled*. If Proposition B is true (an intrinsic floor exists), then the effective error rate *cannot go below* a mechanism-dependent bound, setting a hard limit on logical error suppression.

In 2025-2026, the evidence weighs heavily against Proposition B as a QEC-relevant constraint:

- Google's Willow chip (2024/2025) demonstrated exponential logical error suppression with increasing code distance, the hallmark of below-threshold operation. This was achieved with standard transmon architecture using aluminum on sapphire.
- Lavasani & Vijay (Phys. Rev. Research 7, 023166, May 2025) proved that even coherent adiabatic (non-Pauli, intrinsically correlated) noise can be handled by QEC with a well-defined threshold. The toric code's decoding transition under such noise belongs to the 2D Ising universality class — a theoretically clean result.
- Bosonic AQEC (arXiv:2509.22191, Sept 2025) surpassed break-even, extending logical coherence beyond the best physical qubit without measurement feedback.
- The universal bound on microwave dissipation (Charpentier et al. 2025/2026) is NOT a QEC-killing bound: it sets materials-level constraints, but these are engineering constraints, not Gödel-type limitative theorems.

The cross-domain insight is that **QEC converts the vague "intrinsic vs. environmental" debate into a precise operational question**: does logical error rate monotonically decrease with increasing code distance, or does it asymptote? The asymptotic value (if nonzero) IS the intrinsic decoherence floor expressed in QEC language. Current data shows no asymptote — suppression continues with distance, consistent with Proposition A.

**Score 1**: Not stuck because Proposition B is not logically excluded by QEC (QEC operates within standard QM and would not detect a QM-modifying intrinsic collapse mechanism that operates on timescales longer than current logical gate times). But the operational QEC criterion shows that if a floor exists, it remains below current detection thresholds and has no practical relevance for near-term fault-tolerant quantum computing.

---

**Sub-proposition Attacks (Cross-domain):**

**SP1 [Adequacy of CL]: Score 2**
Cross-domain: **Mesoscopic Physics x CL model**
The spin bath vs. oscillator bath debate has been most intensely fought in mesoscopic magnetism (single-molecule magnets Fe8, Mn12). The mesoscopic literature provides the cleanest experimental tests because (a) environmental nuclear spins are a naturally occurring, well-characterized spin bath, and (b) tunneling rates can be measured to high precision. Prokof'ev & Stamp's original argument was built on SMM tunneling data. Halataei's 2025 rebuttal showing CL can reproduce the bias-dependent relaxation rate quantitatively narrows this gap. However, Segal (2014) showed qualitative differences persist for non-equilibrium heat transport, and the strong-coupling finite-N regime remains unresolved. The mesoscopic connection keeps SP1 genuinely open, not resolved in either direction.

**SP2 [Leggett-Garg]: Score 2**
Cross-domain: **Quantum Foundations x Quantum Computing Hardware**
The 2025 LGI violation results on public quantum computers (IBM superconducting, IonQ trapped ions) are significant for the cross-domain connection: they show that macrorealism violations are NOT confined to specialized tabletop experiments but are observable on industrial-grade hardware with realistic noise. The QND measurement protocol (Phys. Rev. A May 2025) directly addresses the clumsiness loophole that historical Leggett-Garg tests suffered from. The key remaining question is not whether LGI can be violated (it can) but whether the violation is sufficient to exclude ALL macrorealist theories including those with noninvasive-measurability loopholes cleverly disguised as systematic errors. This is a question about the epistemic status of quantum foundations tests, not about qubit physics per se — and it remains partially open.

**SP3 [Danelli-Paris]: Score 2**
Cross-domain: **Quantum Metrology x Quantum Foundations**
Danelli & Paris use quantum estimation theory (Quantum Fisher Information, signal-to-noise ratio bounds) — tools from quantum metrology, not standard decoherence theory — to assess whether IDMs are physical theories. This cross-domain mapping is powerful because it provides operational meaning: an IDM is a physical theory iff its parameters are estimable to arbitrary precision with finite resources. The mapping onto realizable architectures (SP3's explicit question) translates to: can we build a quantum sensor whose Fisher information about the IDM parameter diverges as T→∞? This is precisely the question quantum metrologists ask about any parameter estimation problem. The cross-domain connection sharpens SP3 into a quantitative, architecture-independent research program.

**SP4 [Scaling with N]: Score 1**
Cross-domain: **Gravitational Physics x Mesoscopic Magnetism**
The cross-domain comparison actually weakens SP4. The gravitational decoherence literature (Diosi-Penrose, string-theory embeddings with colored noise, gravitoelectromagnetic extensions) is rapidly evolving: the parameter-free DP model is already falsified (Donadi 2025), and Aspelmeyer (2026) argues that observation of gravitationally induced entanglement would rule out all current collapse models. The mesoscopic magnetism literature shows no evidence of intrinsic decoherence scaling with system size — larger SMMs decohere faster because they couple MORE strongly to environmental spins (larger magnetic moments couple more strongly to nuclear spin baths), which is an environmental effect, not an intrinsic one. The cross-domain evidence suggests that scaling with N is dominated by environmental coupling coefficients that scale differently in different platforms, not by a universal intrinsic mechanism. SP4's extrapolation from N ~ 10^3 (current experiments) to N ~ 10^15 is unsupported by any cross-domain precedent.

---

### AB Score Summary

| Proposition/SP | A-Doctor Score | B-Doctor Score | Average | Verdict |
|---|---|---|---|---|
| Core Contradiction | 1 | 1 | 1.0 | Stuck but circumventable |
| SP1 (CL adequacy) | 2 | 2 | 2.0 | Live research question |
| SP2 (Leggett-Garg) | 2 | 2 | 2.0 | Viable with caveats |
| SP3 (Intrinsic falsification) | 2 | 2 | 2.0 | Strongest sub-proposition |
| SP4 (Scaling with N) | 1 | 1 | 1.0 | Stuck, needs reframing |
| **Overall** | **1.6** | **1.6** | **1.6** | **BORDERLINE — needs Fix** |

---

### Recommendation: FIX (with specific surgery)

The LP has a genuinely interesting core — the operational distinction between environmental and intrinsic decoherence — but is undermined by two fixable structural problems and one possibly fatal empirical problem:

**Problem 1 (Fixable): Conflating two meanings of "intrinsic decoherence."** The LP must disambiguate between:
- Type A: Fundamental QM-modifying decoherence (GRW, CSL, DP) — testable by looking for deviations from QM predictions in specific regimes.
- Type B: Material-immanent decoherence channels (universal quasiparticle dissipation bounds, chaos-assisted tunneling) — characterized within QM but setting practical ceilings for specific platforms.

These are distinct scientific questions with distinct falsification criteria. The LP should either pick one (recommend Type A, as it connects to Nobel-level foundations work) or treat them as separate sub-propositions.

**Problem 2 (Fixable): The "six orders of magnitude" framing is empirically outdated.** The gap has been largely closed by 20 years of materials engineering. The LP should reframe around the *current* frontier: what is the nature of the residual decoherence limiting ms-scale coherence? Is it surmountable (another environmental channel to suppress) or asymptotic (approaching a bound)?

**Problem 3 (Potentially fatal): The core contradiction is not actually a contradiction.** Both environmental and intrinsic decoherence can simultaneously be true at different timescales and for different physical mechanisms. QEC theory shows that logical coherence can be extended arbitrarily even with irreversible physical decoherence, provided error rates are below threshold. The LP's framing as a binary Proposition A vs. Proposition B is a false dichotomy.

**Recommended fix:** Reframe the LP around the question:
> "What are the operational criteria — accessible to current architectures — that would distinguish between (a) continuing improvement in coherence through environmental engineering alone, (b) saturation at a QM-respecting material limit, and (c) saturation at a QM-modifying intrinsic decoherence floor?"

This reframing transforms a false binary into a three-way classification problem with concrete experimental protocols at each branch. It preserves SP3 (the Danelli-Paris framework for IDM falsification) and SP2 (LGI as a macrorealism benchmark) while dropping SP4's unsupported extrapolation.

**If FIX is accepted:** The LP should be rewritten with (i) disambiguated "intrinsic" concept, (ii) updated empirical baseline (ms-scale coherence, not six-order gap), (iii) three-way rather than binary framing, (iv) SP4 replaced with a platform-specific scaling analysis (e.g., "How does surface participation ratio scale with transmon pad size?" — a precise, answerable engineering question that bears on the environmental-vs-intrinsic distinction).

**If forced to choose PASS/KILL on current form:** **KILL** — the combination of conflation error (Problem 1) and false dichotomy (Problem 3) means the LP as stated would generate confused rather than productive research. But the underlying question is excellent, and a fixed version would score substantially higher.
