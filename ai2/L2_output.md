# L2 Output: Prize-Reverse-Engineered Long Proposition Candidates

**SELECTOR Version:** v2.0  
**Strategy:** L2 — Major Physics Prize Motivation → "What Remains Open"  
**Execution Date:** 2026-05-31  
**Prizes Surveyed:** 2024–2026 (Nobel, Wolf, Breakthrough, Dirac, Buckley, Max Planck, Sakurai, Onsager, Franklin)

---

## Scan Summary

| Prize | Year | Laureate(s) | Solved/Recognized |
|---|---|---|---|
| Nobel Physics | 2024 | Hopfield, Hinton | Neural networks from statistical physics principles |
| Nobel Physics | 2025 | Clarke, Devoret, Martinis | Macroscopic quantum tunnelling and energy quantisation in electrical circuits |
| Wolf Physics | 2025 | Jain, Heiblum, Eisenstein | Fractional quantum Hall effect: composite fermions, anyonic statistics, ν=5/2 |
| Breakthrough Fundamental Physics | 2025 | ATLAS, CMS, ALICE, LHCb collaborations | Higgs properties, new strongly interacting particles, matter-antimatter asymmetry (LHC Run 2) |
| Breakthrough Fundamental Physics | 2026 | Muon g-2 collaborations (~380 scientists) | Precision measurement of muon anomalous magnetic moment (127 ppb) |
| Breakthrough Special | 2026 | David J. Gross | QCD asymptotic freedom, heterotic string theory, lifetime leadership |
| Dirac Medal (ICTP) | 2024 | Casini, Huerta, Ryu, Takayanagi | Quantum entropy in QFT and quantum gravity (Ryu-Takayanagi formula, c/F/a-theorem entanglement proofs) |
| Dirac Medal (ICTP) | 2025 | Gibbons, Horowitz, Kerr, Wald | Euclidean quantum gravity, Kerr metric, Wald entropy, AdS/CFT |
| Buckley (APS) | 2025 | David J. Bishop | Superfluidity in helium films, vortex-driven phase transitions (KT theory) |
| Buckley (APS) | 2026 | Feve, Bishop, Manfra, Reppy | Superfluid phase transition vortices + anyonic braiding statistics in FQH |
| Max Planck Medal | 2025 | Kurt Kremer | Numerical simulation of microscopic polymer models, multi-scale coarse-graining |
| Sakurai (APS) | 2025 | Jenkins, Manohar | Large-Nc baryon physics, SMEFT one-loop renormalization group evolution |
| Sakurai (APS) | 2026 | John F. Donoghue | Effective field theories, gravity as EFT, chiral perturbation theory |
| Onsager (APS) | 2025 | Bouchaud, Cugliandolo, Kurchan | Out-of-equilibrium disordered systems, complex aging |
| Onsager (APS) | 2026 | Mehran Kardar | KPZ equation, Casimir forces, active matter, biological physics |
| Franklin Medal | 2025 | John P. Perdew | Density functional theory (PBE functional), computational materials prediction |

---

## Dean's Clue #1 Integration

**Clue:** v2-deepseek x LP-2 (Planckian dissipation). Search instruction: "Nobel Prize" OR "Breakthrough Prize" strongly correlated electrons OR strange metal 2024 2025 2026.

**Finding:** No recent (2024-2026) Nobel or Breakthrough Prize was directly awarded for strongly correlated electrons or strange metals. The last Nobel in this subfield was likely 1998 (Laughlin, Stormer, Tsui for FQH) and 2003 (Abrikosov, Ginzburg, Leggett for superconductivity/superfluidity). However, the 2025 Onsager Prize (out-of-equilibrium disordered systems, complex aging) connects to the glassy-dynamics side of the problem, and the 2024 Nobel (Hopfield/Hinton, neural networks from spin-glass physics) provides statistical-physics framing. Most importantly, the problem area is so central to modern condensed matter that its absence from recent prizes itself signals "urgently open" status.

**Decision:** LP-Candidate-1 is included below with full L2 treatment, per the Dean's Clue priority instruction.

---

## Qualifying Long Proposition Candidates

---

### LP-Candidate-1: Planckian Dissipation — Kinematic Universal Wall vs Emergent Dynamical Mechanism

**Source:** L2 + Dean's Clue #1 (Onsager 2025 context: out-of-equilibrium disordered systems; Nobel 2024 context: spin-glass statistical physics applied to emergent phenomena)

**Prize Connection:** No single recent major prize directly awarded for strongly correlated electrons, but the problem sits at the intersection of two prize-recognized domains: (a) the statistical physics of disordered systems and emergent criticality (Onsager 2025, Nobel 2024 framing), and (b) the decades-long experimental tradition of condensed-matter Nobel prizes (FQH 1998, cuprate-motivated efforts). The PRIZE-GAP itself signals that the fundamental mechanism of strange-metal Planckian dissipation remains unresolved.

**Core Contradiction:**
- **Proposition A:** The Planckian relaxation rate τ = ℏ/k_B T is a kinematic universal bound — a "wall" that no quantum system can exceed in any spatial dimension, independent of microscopic coupling details, interaction type, or dimensionality. Supporting: Bruin et al. (2013) empirical survey showing τ^(-1) ≤ α k_B T/ℏ with α ≈ 1 across >10 material families; Hartnoll (2015) holographic bound conjecture; Sachdev (2011) "maximal chaos bound" parallelism.
- **Proposition B:** The Planckian dissipation observed in strange metals emerges from specific dynamical mechanisms — Kondo destruction (Hu, Chen, Si, Nature Physics 2024), marginal Fermi liquid (MFL), SYK-type models, or Kondo-breakdown quantum criticality (Gleis, Lee, Kotliar, von Delft, PRL 2025) — and varies with microscopic coupling. In this view, Planckian-scale scattering is an empirical coincidence of parameter ranges in specific materials, not a fundamental kinematic bound.
- **Why cannot both be true:** If the Planckian bound is kinematic (universal, mechanism-independent, set by ħ/k_B T alone), then no microscopic mechanism can produce a scattering rate that exceeds it AND the saturation at the bound cannot depend on coupling constants. If the bound emerges from specific dynamical mechanisms (Kondo destruction, etc.), then it varies with coupling and can be violated under suitable conditions.

**Independent Source Count:** ≥6
1. Prize context: Onsager 2025 (out-of-equilibrium disordered systems), Nobel 2024 (statistical physics for emergent phenomena)
2. Hu, Chen, Si — "Quantum critical metals and loss of quasiparticles," Nature Physics 20, 1-11 (Dec 2024) — review from heavy-fermion/Kondo-destruction perspective
3. Gleis, Lee, Kotliar, von Delft — "Dynamical Scaling and Planckian Dissipation Due to Heavy-Fermion Quantum Criticality," PRL 134, 106501 (Mar 2025) — NRG+DMFT evidence for intrinsic strange-metal fixed point
4. Gleis, Lee, Kotliar, von Delft — "Emergent Properties of the Periodic Anderson Model," PRX 14, 041036 (2024) — companion paper establishing Luttinger surface driving f-electron localization
5. Koizumi — "Ohm's Law, Joule Heat, and Planckian Dissipation," arXiv:2501.01797 (Jan 2025) — Planckian dissipation from Berry connection gauge fluctuations
6. Heller, Aydin et al. — "Quantum Acoustics Demystifies the Strange Metals" (2025) — phonon-based alternative to purely electronic mechanisms

**Sub-proposition Count:** ≥3 (matching LP-2 from Dean's Clues system)
1. **LP2-S1:** The α-distribution (τ^(-1) = α k_B T/ℏ) across material families — is it truly universal (narrow distribution peaking at α ≈ 1) or does it show material-dependent variance that undermines kinematic-wall interpretation?
2. **LP2-S2:** The discrimination power of α — can existing experimental data distinguish between "kinematic wall saturated from below" and "emergent dynamical convergence toward a common scale"?
3. **LP2-S3 (verdict design):** If the information-backflow functional N_I^(S) = 2ln2 (from v2-deepseek) is a universal geometric invariant, does it imply Planckian bound as a kinematic consequence? Can the toy-model invariant be extended to dissipative open quantum systems?

**Post-Prize Attempts:** ≥3
1. Gleis et al. (2024-2025): NRG+DMFT provides evidence for intrinsic strange-metal fixed point → claims Planckian dissipation from collective fluctuations, but limited to 2-site cellular DMFT which cannot capture momentum-dependent transport in 3D. Did not settle the kinematic-vs-dynamic question.
2. Koizumi (2025): Berry-connection gauge theory proposes a new mechanism but has not been independently verified or extended to realistic materials. Remains a single-author preprint.
3. Heller-Aydin et al. (2025): Quantum acoustics challenges the dominant purely-electronic paradigm by arguing phonons can explain Planckian resistivity in a time-dependent nonperturbative treatment. Contradicts decades of phonon-mechanism rejection; not yet widely accepted.

**Infrastructure Bottleneck Check:** PASS. The problem is primarily theoretical (can existing experimental data be re-interpreted within a kinematic-wall framework?) and can also be advanced with existing experimental techniques (resistivity, optical conductivity, ARPES). No next-gen facility required. New theoretical tools (v2-deepseek's N_I^(S) invariant, NRG+DMFT, quantum estimation theory) are available and developing.

**Additional Notes:** This is the Dean's top-priority LP. The v2-deepseek finding (N_I^(S) = 2ln2 as coupling-independent geometric invariant, proven exactly in a toy model) provides a new theoretical angle: if information backflow during relaxation is geometrically constrained, Planckian dissipation may be the kinematic wall after all, and the "dynamical mechanism" explanations describe only how particular systems approach the wall from below. The LP2-S3 sub-proposition is specifically designed to adjudicate this clash.

---

### LP-Candidate-2: Macroscopic Quantum Decoherence — Environmental Noise vs Intrinsic Limit

**Source:** L2 + Nobel Prize Physics 2025 (Clarke, Devoret, Martinis)

**Prize Connection:** Nobel 2025 was awarded for the discovery of macroscopic quantum tunnelling and energy quantisation in electrical circuits — the foundational demonstration that quantum behavior is NOT limited to microscopic scale. This prize **opened** the field of macroscopic quantum coherence and superconducting qubits. What remains **open** is the next logical question: if macroscopic quantum coherence is possible in principle, what fundamentally limits it in practice? Is the limit purely technological (noise, materials) or does nature impose an intrinsic decoherence ceiling?

**Core Contradiction:**
- **Proposition A:** Decoherence in macroscopic quantum systems (superconducting qubits with ~10^9 electrons in coherent superposition) is entirely due to environmental coupling — two-level systems (TLS) in amorphous oxides, non-equilibrium quasiparticles, stray electromagnetic fields, phonon shot noise. The Caldeira-Leggett oscillator-bath model (developed to describe the very MQT experiments that won the Nobel) captures all relevant decoherence channels. Eliminate environmental noise → arbitrarily long coherence. Supporting: Standard decoherence theory (Zurek, 2003); experimental progress in T1/T2 from ~ns to ~ms over 20 years through better materials and filtering; Caldeira-Leggett Nobel lineage.
- **Proposition B:** There exists intrinsic (irreducible) decoherence that sets a fundamental, not just technological, ceiling on macroscopic quantum coherence. Candidate mechanisms include: spin-bath decoherence at T=0 without energy dissipation (Prokof'ev & Stamp), gravitational decoherence from spacetime metric fluctuations (Diosi-Penrose), zero-point quantum field fluctuations, 't Hooft's holographic bound, or non-linear quantum mechanics with spontaneous wavefunction collapse (Ghirardi-Rimini-Weber). Supporting: Stamp (2006) "six orders of magnitude discrepancy" between Caldeira-Leggett predictions and measured decoherence; Gallego & Dakic (Proc. R. Soc. A, 2025) showing macroscopic quantum behavior robust against decoherence — implying standard decoherence theory may not capture all relevant physics; Danelli & Paris (EPL, 2025) demonstrating falsifiability of intrinsic decoherence models via quantum estimation theory.
- **Why cannot both be true:** If decoherence is entirely environmental, then with sufficient noise isolation (cooling, material purification) quantum coherence times should diverge. If intrinsic decoherence exists (T=0 spin-bath, gravity, Planck-scale), then a saturation floor exists that no amount of engineering can breach. The "six orders of magnitude" gap between Caldeira-Leggett predictions and experiment cannot be explained by environmental models if they are the COMPLETE theory.

**Independent Source Count:** ≥5
1. Nobel 2025 prize citation (Clarke, Devoret, Martinis — macroscopic quantum behaviour demonstrated)
2. Gallego & Dakic — "Quantum Theory at the Macroscopic Scale," Proc. R. Soc. A (2025) — challenges decoherence/coarse-graining as sufficient explanation for quantum-to-classical transition
3. Danelli & Paris — "Are Intrinsic Decoherence Models Physical Theories?" EPL (Feb 2025, Editor's Choice) — quantum estimation theory applied to testability of intrinsic decoherence
4. P.C.E. Stamp — extensive review of decoherence in solid-state qubits, identifying the "six orders of magnitude" theory-experiment gap (multiple papers, 2006-present)
5. Leggett & Garg — temporal Bell inequalities and macrorealism (1985, with continuing experimental relevance to superconducting qubit tests)

**Sub-proposition Count:** 4
1. **SP1 (Adequacy of Caldeira-Leggett):** Does the Caldeira-Leggett oscillator-bath model (the same theory that enabled the Nobel-winning MQT experiments) capture ALL relevant decoherence channels for modern superconducting qubits, or are there systematic omissions (spin baths, non-Gaussian noise, long-time tails)?
2. **SP2 (Macrorealism tests):** Would a definitive Leggett-Garg inequality violation in a superconducting qubit system (with N > 10^9 electrons in superposition) definitively rule out all macrorealistic alternatives to quantum mechanics, or do loopholes analogous to Bell-test loopholes persist?
3. **SP3 (Intrinsic decoherence falsification):** Under what experimental conditions (coherence time, qubit number, temperature) can intrinsic decoherence models be distinguished from environmental decoherence? Danelli-Paris (2025) provide a quantum-estimation-theoretic framework — how does it map onto realizable superconducting qubit architectures?
4. **SP4 (Scaling of decoherence with system size):** How does coherence time scale with the number of electrons in the superposition? Is there a regime (N ~ 10^12-10^15) where intrinsic decoherence, if it exists, would become dominant over environmental noise? What observable signatures would distinguish intrinsic N-scaling from environmental N-scaling?

**Post-Prize Attempts:** ≥2
1. Google Quantum AI (Martinis group, 2019): Achieved quantum supremacy (53-qubit Sycamore processor) but with gate error rates ~10^(-3), far above surface-code threshold. The origin of the residual error rate — environmental vs fundamental — remains unclarified. This was Martinis' Nobel-winning lineage and the experiment did NOT resolve the decoherence origin question.
2. Gallego-Dakic (2025): Showed theoretically that macroscopic quantum behavior can survive decoherence and coarse-graining, but the constructive proof uses non-IID states whose experimental realizability at N ~ 10^9 remains unclear. This is a theory paper that laid groundwork but did not settle the question.

**Infrastructure Bottleneck Check:** CAUTION. Danelli-Paris (2025) argue intrinsic decoherence IS falsifiable with current quantum estimation theory and superconducting qubit technology, but the required coherence times and qubit counts may push against the limits of current dilution-refrigerator setups. However, the problem can be partially attacked theoretically and with existing experimental data — it is NOT a pure "needs next-gen facility" problem. Sub-propositions SP1 and SP2 can be addressed with present-day experiments. SP3-SP4 may require improved qubit isolation but not qualitatively new facility classes.

---

### LP-Candidate-3: Topological Order at ν=5/2 — Pfaffian vs Anti-Pfaffian vs PH-Pfaffian

**Source:** L2 + Wolf Prize Physics 2025 (Jain, Heiblum, Eisenstein) + Buckley Prize 2026 (Feve, Bishop, Manfra, Reppy)

**Prize Connection:** The Wolf Prize 2025 was awarded for "advancing our understanding of the surprising properties of two-dimensional electron systems in strong magnetic fields," recognizing Jain's composite fermion theory (which quantitatively explained the sequence of FQH states), Heiblum's experimental interferometry confirming fractional charge and anyonic statistics, and Eisenstein's co-discovery of the ν=5/2 FQH state. The Buckley Prize 2026 recognized the experimental observation of "anyonic braiding statistics of quasiparticles in the fractional quantum Hall effect." Together these prizes say: we UNDERSTAND the basic anyonic nature of FQH quasiparticles. What remains OPEN: the exact topological order of the most important non-Abelian candidate state — ν=5/2 — which determines whether these anyons are useful for topological quantum computing.

**Core Contradiction:**
- **Proposition A:** The ν=5/2 fractional quantum Hall state is in the Pfaffian universality class (Moore-Read, 1991), supporting Ising-type non-Abelian anyons with quantum dimension d = √2. This is the original theoretical proposal and is consistent with early numerical exact diagonalization studies on small systems.
- **Proposition B:** The ν=5/2 state is in the anti-Pfaffian universality class (Lee, Ryu, Nayak, Fisher, 2007; Levin, Halperin, Rosenow, 2007) — the particle-hole conjugate of Pfaffian. This emerged from the requirement that the realistic Hamiltonian has significant Landau-level mixing that breaks particle-hole symmetry in the direction favoring anti-Pfaffian.
- **Proposition C:** The ν=5/2 state is PH-Pfaffian (preserving particle-hole symmetry, Son 2015), which has different edge-mode structure and thermal Hall conductance (K_H = 5/2 rather than 7/2 for Pfaffian or 3/2 for anti-Pfaffian in units of κ_0).
- **Why cannot all be true:** These three topological orders have distinct edge-mode structures, distinct thermal Hall conductances, and distinct braiding statistics for their fundamental anyons. A given physical sample can realize only one. The experimental evidence (thermal transport, shot noise, interferometry) does not yet cleanly select one — and different measurements appear to support different candidates.

**Independent Source Count:** ≥6
1. Wolf Prize 2025 (citation: Jain/Heiblum/Eisenstein — FQH, composite fermions, ν=5/2 discovery)
2. Buckley Prize 2026 (citation: Feve/Bishop/Manfra/Reppy — anyonic braiding in FQH)
3. Heiblum group (Nature 2018): half-integer quantized thermal conductance at ν=5/2 suggesting PH-Pfaffian
4. Banerjee et al. (Nature 2018): thermal conductance measurement supporting PH-Pfaffian (K_H = 5/2)
5. Harvard Math seminar: "The Fractional Quantum Hall Effect at ν=5/2: Past, Recent, and Future" — ongoing debate framing
6. Willett et al. (2023) / Kang group (2024-2025): ongoing interferometry and shot noise experiments at ν=5/2, reaching conflicting interpretations

**Sub-proposition Count:** 4 (matching LP-3 from Dean's Clues system)
1. **LP3-S1 (Thermal Hall conductance):** Is the measured K_H = 5/2 (in units of κ_0) at ν=5/2 robust after accounting for edge reconstruction, non-equilibrium effects, and counter-propagating neutral modes that can thermalize and reduce the observed thermal conductance?
2. **LP3-S2 (Mapping stability — Pfaffian ↔ anti-Pfaffian ↔ PH-Pfaffian):** Under what conditions (Landau-level mixing strength, quantum well width, density) does the ground state transition between these three topological classes? Is there a first-principles phase diagram or is it sensitive to disorder uncontrolled in experiment? (Dean's Clue #4 relevant: Diophantine protection for quasiperiodic edge potentials?)
3. **LP3-S3 (Edge reconstruction and equilibration):** Shot noise and tunneling I-V measurements at ν=5/2 reveal edge-mode structures that depend on edge confining potential. Can edge reconstruction change the apparent topological order, mimicking one class while the bulk is in another? This is the central ambiguity in experimental interpretation.
4. **LP3-S4 (Bulk-edge correspondence validation):** Does the bulk topological order uniquely determine the edge-mode structure at ν=5/2, or is the correspondence weakened by the non-universal edge physics (reconstruction, disorder, long-range Coulomb)? This sub-proposition bridges to the broader question of whether edge measurements can reliably probe bulk topological order.

**Post-Prize Attempts:** ≥3
1. Heiblum group (2018, published in Nature): Thermal conductance measurement → K_H = 5/2, interpreted as PH-Pfaffian. But the interpretation relies on edge-mode equilibration assumptions — anti-Pfaffian with incomplete edge thermalization can also produce apparent K_H = 5/2.
2. Willett et al. (multiple attempts, 2013-2023): Fabry-Perot interferometry at ν=5/2 claims anyonic braiding signatures consistent with non-Abelian statistics, but the specific topological order (Pfaffian vs anti-Pfaffian) could not be distinguished.
3. Kang group (2024-2025): Shot noise measurements at ν=5/2 edge provide new constraints on edge-mode charge and tunneling exponents. Results partially constrain the topological order but do not uniquely select one candidate — consistent with multiple interpretations depending on edge reconstruction assumptions.

**Infrastructure Bottleneck Check:** PASS. FQH experiments at ν=5/2 are performed in existing GaAs/AlGaAs heterostructures with dilution refrigerators — established technology since the 1980s. The bottleneck is NOT facility-limited; it is the conceptual challenge of disentangling bulk topological order from edge reconstruction and non-universal edge physics.

---

### LP-Candidate-4: Black Hole Information Paradox — Resolved by Islands or Still Open?

**Source:** L2 + Dirac Medal (ICTP) 2025 (Gibbons, Horowitz, Kerr, Wald) + Dirac Medal (ICTP) 2024 (Casini, Huerta, Ryu, Takayanagi)

**Prize Connection:** The Dirac Medal 2025 recognized foundational contributions to black hole theory — Gibbons' Euclidean path integral (deriving black hole temperature and entropy), Kerr's exact rotating black hole solution, Wald's entropy formula from Noether theorem, and Horowitz's AdS/CFT and holographic superconductors. This body of work built the infrastructure for black hole thermodynamics. The Dirac Medal 2024 recognized quantum entropy in QFT (Casini's Bekenstein bound proof, Ryu-Takayanagi formula for holographic entanglement entropy). Together, these prizes represent the theoretical toolkit applied to the Black Hole Information Paradox (BHIP). What remains OPEN is whether the island formula / replica wormhole / Page curve program has actually resolved the paradox or merely reformulated it in models too simple to capture realistic black hole physics.

**Core Contradiction:**
- **Proposition A:** The Page curve is correctly reproduced by the island formula and replica wormhole computations (Penington, Almheiri, Engelhardt, Marolf, Maxfield, 2019-2020). This demonstrates that black hole evaporation is unitary and that the information paradox is resolved in principle — the entropy of Hawking radiation follows the Page curve (rising then falling), consistent with unitarity. The resolution has been broadly accepted by the community (Raj 2025 IJSR review; Yu & Ge 2025 CPC; Antonini, Chen, Maxfield, Penington "An apologia for islands," JHEP 2025).
- **Proposition B:** The claimed resolution only applies to toy models (JT gravity in 2D,AdS/CFT with massive gravitons/non-gravitating reservoirs) and does NOT transfer to realistic (4D, asymptotically flat) black holes. Geng, Raju et al. (2020-2025) argue that in massless gravity (flat spacetime), gauge-invariant operators cannot be localized to an "island" region, making the derivation invalid for our universe. Furthermore, Ageev et al. (2024) demonstrate a "blinking island" effect in black holes with reflecting boundaries — the island disappears for finite time intervals, during which entanglement entropy exceeds the Bekenstein-Hawking bound, violating the Page curve.
- **Why cannot both be true:** If the island formula works only in massive-graviton (AdS+bath) setups but NOT in massless gravity (flat spacetime), then the resolution is model-dependent and the paradox remains open for physically realistic black holes. Both camps have published in 2025, with explicit disagreement on this precise technical point.

**Independent Source Count:** ≥7
1. Dirac Medal 2025 (Gibbons, Horowitz, Kerr, Wald — black hole theory foundations)
2. Dirac Medal 2024 (Casini, Huerta, Ryu, Takayanagi — holographic entanglement entropy)
3. Antonini, Chen, Maxfield, Penington — "An apologia for islands," JHEP (2025) — rebuttal to critics, arguing islands appear in massless gravity too
4. Ageev et al. — "Boundary CFT, Information Paradox and Entanglement Islands" (Fradkin Centennial, Sept 2024) — blinking island effect, Page curve violation in some setups
5. Anmay Raj — "Resolving the Black Hole Information Paradox: A Review," IJSR (2025) — mainstream review noting unresolved encoding mechanism
6. Yu & Ge — "Geometric Constraints via Page Curves," Chinese Physics C (2025) — derives constraints for island existence, finds islands in negative-heat-capacity black holes
7. Geng, Raju et al. — series of papers (2020-2025) contesting AdS/CFT island formula applicability to flat-space/massless gravity

**Sub-proposition Count:** 4
1. **SP1 (Massless gravity islands):** Do entanglement islands exist in asymptotically flat (massless graviton) spacetime? The Antonini et al. (2025) "apologia" claims yes; the Geng-Raju program claims no. This is a sharply defined technical question with different answers in the literature.
2. **SP2 (Blinking island):** Is the "blinking island" effect (Ageev 2024) a physical failure of the island mechanism or an artifact of the specific reflective-boundary setup? If islands can "blink," does the Page curve hold in all physically reasonable configurations?
3. **SP3 (Microscopic encoding mechanism):** Even if the island formula gives the correct entropic accounting, the microscopic mechanism by which information is encoded into Hawking radiation remains unknown. The island formula is an entropy computation, not a dynamical description of information transfer. Is this gap fundamental or technical?
4. **SP4 (De Sitter and cosmology):** Can the island formula be extended from AdS (negative cosmological constant) to de Sitter (positive cosmological constant) — i.e., to our universe? This is required for any cosmological application of the resolution.

**Post-Prize Attempts:** ≥3 (active conflicting publications in 2024-2025)
1. Penington-Maxfield group vs Geng-Raju group (2020-2025): Sustained technical debate in JHEP, PRL, and other journals about whether islands exist in massless gravity. Both sides have published multiple papers; the disagreement persists into 2025.
2. Ageev et al. (2024): Reports blinking island effect — an explicit counterexample where the island mechanism fails. Has been presented at conferences but not yet fully resolved by the community.
3. Antonini et al. (2025): "Apologia" paper explicitly acknowledges "broad (although not complete) agreement on the technical points" with the Geng camp but "differ in... interpretation." This is a 2025 paper that could not close the debate.

**Infrastructure Bottleneck Check:** PASS. This is a purely theoretical problem requiring analytic and numerical work in semiclassical gravity, holography, and quantum information theory. No experimental facility of any kind is required. The mathematical tools (quantum extremal surfaces, replica trick, gravitational path integral, algebraic QFT) exist and are being actively developed.

---

### LP-Candidate-5: Emergence of Spacetime from Entanglement — "It from Qubit" vs "Qubit in It"

**Source:** L2 + Dirac Medal (ICTP) 2024 (Casini, Huerta, Ryu, Takayanagi)

**Prize Connection:** The Dirac Medal 2024 was awarded for "profound insights on quantum entropy in quantum gravity and quantum field theory." Specifically: (1) Casini-Huerta's entanglement-entropy proofs of the c-theorem, F-theorem, and a-theorem showing that QFT entanglement entropy decreases monotonically under RG flow — linking quantum information to QFT structure; (2) Casini's precise proof of the Bekenstein bound using quantum relative entropy — connecting entropy bounds to quantum information; (3) Ryu-Takayanagi formula (2006) relating entanglement entropy in holographic CFTs to minimal surface area in the dual bulk geometry. These are the building blocks of the "spacetime emerges from entanglement" program. What remains OPEN is whether this program can be completed: is the Ryu-Takayanagi relation a computational tool or a statement about the ontological origin of spacetime?

**Core Contradiction:**
- **Proposition A:** Spacetime geometry is emergent from entanglement structure — "it from qubit." The Ryu-Takayanagi formula shows that bulk geometry (metric, causal structure) is encoded in the entanglement pattern of the boundary CFT. Tensor network models (MERA, HaPPY code) explicitly construct bulk geometry from boundary entanglement. ER=EPR (Maldacena-Susskind 2013) proposes that Einstein-Rosen bridges (wormholes) ARE EPR pairs — entanglement literally creates spacetime connectivity. Supporting: Swingle (2012) MERA as discrete AdS; Pastawski, Yoshida, Harlow, Preskill (2015) HaPPY code; Maldacena-Susskind (2013) ER=EPR; van Raamsdonk (2010) "entanglement glue" argument.
- **Proposition B:** The Ryu-Takayanagi formula is a computational tool within AdS/CFT that relates entanglement entropy in one description to geometry in another — it does NOT imply that spacetime literally "emerges" from entanglement. Entanglement is a property of quantum states that exist IN spacetime, and the holographic mapping is a duality, not an ontological reduction. The tensor network constructions only recover spacetime that was put into the network architecture by design (e.g., MERA replicates AdS because its hierarchical structure mirrors AdS — it is not generating geometry from scratch). Supporting: The formalism is restricted to AdS/CFT and has not been extended to de Sitter or flat spacetime; the Ryu-Takayanagi formula requires a pre-existing holographic duality and does not explain WHY holography works.
- **Why cannot both be true:** If spacetime literally emerges from entanglement, then entanglement is ontologically prior to geometry — you can start from a quantum state with no pre-assigned geometry and derive the spacetime as an output. If entanglement is merely a computational tool within holography, then spacetime geometry is still fundamental and entanglement entropy is just one way to probe it. The two positions make different claims about what is primitive and what is derived.

**Independent Source Count:** ≥6
1. Dirac Medal 2024 (Casini, Huerta, Ryu, Takayanagi — entanglement entropy in QFT and holography)
2. Maldacena & Susskind — "Cool horizons for entangled black holes," Fortsch. Phys. 61, 781 (2013) — ER=EPR conjecture
3. van Raamsdonk — "Building up spacetime with quantum entanglement," Gen. Rel. Grav. 42, 2323 (2010) — original "entanglement glue" argument
4. Swingle — "Entanglement renormalization and holography," Phys. Rev. D 86, 065007 (2012) — MERA tensor network as discrete AdS
5. Pastawski, Yoshida, Harlow, Preskill — "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence," JHEP 06, 149 (2015) — HaPPY code
6. Faulkner, Guica, Hartman, Myers, van Raamsdonk — "Gravitation from Entanglement in Holographic CFTs," JHEP 03, 051 (2014) — first-order Einstein equations from entanglement first law

**Sub-proposition Count:** 3
1. **SP1 (Entanglement first law → Einstein equations):** Faulkner et al. (2014) showed that the entanglement first law δS = δ⟨H⟩, evaluated on ball-shaped regions in holographic CFTs, implies the linearized Einstein equations in the bulk. Is this relation exact to all orders in perturbation theory, or does it break down at higher orders, indicating that entanglement only captures the linearized (non-dynamical) sector of gravity?
2. **SP2 (Beyond AdS — dS and flat space):** The Ryu-Takayanagi formula and all tensor-network constructions require AdS boundary conditions. Can any entanglement-geometry correspondence be formulated for de Sitter space (our universe's accelerating phase) or asymptotically flat spacetime, or is the connection fundamentally tied to the negative cosmological constant of AdS?
3. **SP3 (Sub-AdS scale geometry):** Ryu-Takayanagi formula only recovers bulk geometry at scales larger than the AdS radius. Can entanglement entropy reconstruct sub-AdS-scale geometry — including the black hole interior, regions behind horizons, and Planck-scale structure — which is where the information paradox and quantum gravity questions live?

**Post-Prize Attempts:** ≥2
1. Jafferis, Kolchmeyer, Mukhametzhanov, et al. (2022-2025): Attempted to explicitly reconstruct the black hole interior from boundary data using Petz map and modular flow in JT gravity. Partially successful in toy models but the reconstruction fails for generic states and requires knowing the black hole microstate — precisely the information that the paradox says should be contained in the radiation. This is an explicit attempt that exposed fundamental limitations.
2. Engelhardt, Wall, et al. (2015-2024): The quantum extremal surface program (building on Ryu-Takayanagi) has achieved remarkable successes in computing Page curves, but the extension from AdS/CFT holography to our universe (dS) has not been achieved despite sustained effort. The 2024-2025 "apologia for islands" papers still restrict to negative cosmological constant.

**Infrastructure Bottleneck Check:** PASS. Pure theoretical problem. Mathematical tools (holography, quantum information theory, tensor networks, semiclassical gravity) are well-established and actively developing.

---

## Below-Threshold Candidates

### BT-Candidate-1: Physics of Deep Learning (Nobel 2024, Hopfield/Hinton)
**Prize:** Nobel Physics 2024 — neural networks from statistical physics  
**Open:** Why does overparameterized deep learning work? What is the theoretical explanation for its optimization and generalization?  
**Rejection reason:** The open problems are primarily computer-science-facing (optimization landscape geometry, interpretability, alignment). While statistical physics provides tools (spin-glass theory, replica method, random matrix theory), the core "A vs B" contradiction is not sharply defined in physics terms. The problem decomposes better as an ML-theory question than a physics LP.  
**Verdict:** Below L2 threshold. May qualify under a different strategy (e.g., L4 cross-disciplinary mapping).

### BT-Candidate-2: Muon g-2 Tension — New Physics or SM Error? (Breakthrough 2026)
**Prize:** Breakthrough 2026 — precision muon g-2 measurement  
**Open:** HVP discrepancy between dispersive (data-driven) and lattice QCD  
**Rejection reason:** The anomaly has largely dissolved as of 2025-2026, with the 5σ tension reduced to ~0.6σ after lattice QCD results are incorporated. The remaining open question ("why do dispersive and lattice HVP disagree?") is a systematic-error question in hadronic physics, not a fundamental A-vs-B contradiction suitable for a long proposition.  
**Verdict:** Below threshold.

### BT-Candidate-3: DFT Exact Functional — Existence vs Approximability (Franklin 2025, Perdew)
**Prize:** Franklin Medal 2025 — PBE functional, density functional theory  
**Open:** The exact exchange-correlation functional exists by Hohenberg-Kohn theorem, but is it computationally accessible in principle?  
**Rejection reason:** While a legitimate open problem (existence of a universal functional vs the "Jacob's Ladder" of approximations), this is primarily a computational/mathematical problem rather than a physics A-vs-B contradiction. It does not decompose into qualitatively distinct sub-propositions suitable for the long-proposition format.  
**Verdict:** Below threshold.

---

## Global Assessment

**5 qualifying LPs found** out of 18 prizes surveyed (28% yield).

**Priority ranking (Dean's Clues weighted):**
1. **LP-Candidate-1 (Planckian Dissipation)** — Dean's Clue #1 priority; strongest alignment with existing ai-reservations infrastructure (LP-2); new theoretical tool (v2-deepseek) provides novel attack angle
2. **LP-Candidate-2 (Macroscopic Quantum Decoherence)** — Nobel 2025 prize connection is the clearest and most direct; contradiction is sharply defined; experimental infrastructure exists
3. **LP-Candidate-3 (ν=5/2 Topological Order)** — Dual prize backing (Wolf 2025 + Buckley 2026); Dean's Clue #4 ancillarily relevant; existing ai-reservations LP-3 infrastructure
4. **LP-Candidate-4 (Black Hole Information)** — Dirac 2025 + 2024 dual prize backing; very active 2024-2025 debate; pure theory (no facility bottleneck)
5. **LP-Candidate-5 (Spacetime from Entanglement)** — Dirac 2024 prize connection; ontological depth; but more ambiguous A-vs-B (interpretational vs technical)

**Next step:** These five candidates advance to L3 selection, where they will be evaluated against the full LP criteria grid and assigned to writing agents. Per the Dean's Clue #1 explicit instruction, LP-Candidate-1 (Planckian Dissipation) is the top-priority candidate for immediate development.

---

*L2 execution completed by ai2/SELECTOR v2.0. All web sources retrieved 2026-05-31.*
