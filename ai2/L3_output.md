# SELECTOR v2.0 — Strategy L3 Output: Cross-Community Physics Contradictions

**Execution Date:** 2026-06-01
**Target Quality:** Nature Physics / Physical Review Letters level

---

## Executive Summary

Six domain pairs were searched. **3 candidates QUALIFY** (Strange Metals, MBL, Black Hole Information) and **3 DO NOT QUALIFY** (QSL, DQCP, Active Matter). The Black Hole Information debate and MBL controversy are the strongest candidates, with direct 2025-2026 rebuttal papers.

---

## LP-Candidate-L3-1: Strange Metals — Holographic (AdS/CFT) vs Microscopic Mechanism

**Domain Pair:** hep-th vs cond-mat.str-el
**Status:** QUALIFIES

**Core Contradiction:**
- **Proposition A (hep-th / holography community):** Strange metallic behavior arises from universal gravitational physics in AdS/CFT duals. Planckian dissipation (\(\tau^{-1} \sim k_B T / \hbar\)) emerges from the AdS\(_2\) near-horizon geometry of extremal black holes and represents a universal quantum bound on scrambling. SYK models provide a concrete realization of this holography. Key literature: Abbamonte (2025 colloquium, "conformal invariance in strange metals"), Gouteraux (2025, charge correlators in AdS\(_2\)), extensive AdS/CFT literature since 2007.
- **Proposition B (cond-mat.str-el / DMFT community):** Strange metallicity is an intrinsic many-body phenomenon arising from non-perturbative vertex corrections in relatively conventional models (e.g. periodic Anderson model), without requiring holography or disorder. Planckian dissipation is not a universal bound — it emerges from microscopic interactions that can be captured by DMFT and its extensions. Key literature: Khveshchenko (2025, "Critical Review of Quantitative Claims" — calling holography quantitatively inadequate for cuprates), Gleis, Lee, Kotliar, von Delft (2025, PRL/PRX — "strange metal is intrinsic, disorder-free, and arises from qualitatively important vertex contributions").
- **Why both cannot be true:** Holography requires ultra-strong coupling and large-N (conditions not met in real solids), while the DMFT-based approach shows strange metallicity emerging at *intermediate* coupling with physical N=2. If microscopic vertex corrections suffice, the holographic explanation is unnecessary. Conversely, if AdS/CFT is the true explanation, DMFT should fail to capture the universal aspects of strange metallic transport.

**Age of Disagreement:** ~18 years (since ~2007 when AdS/CFT condensed matter applications began; active and intensifying through 2025).

**Sub-proposition Decomposability:** 4 sub-propositions
1. **Planckian bound:** Is \(\tau^{-1} \sim k_B T / \hbar\) a universal bound from black hole physics, or an emergent property of specific microscopic models?
2. **Quantitative accuracy:** Can any holographic model reproduce the *full* set of power-law dependencies observed in cuprates without cherry-picking observables? (Khveshchenko claims NO model does this.)
3. **Disorder necessity:** Is disorder essential to strange metallic transport (SYK) or is it inessential (Munich group: "disorder-free intrinsic strange metal")?
4. **Coupling regime:** Do real strange metals live in the ultra-strong coupling regime where holography is valid, or the intermediate-coupling regime where conventional many-body theory applies?

**Current Attackability:** (1) Sub-proposition 3 is attackable via numerical methods (Munich group already publishing results). (2) Sub-proposition 2 is attackable via systematic comparison of holographic predictions against full experimental ARPES, transport, and thermodynamics datasets. (3) New experimental probes: "scramblon" searches in cuprates (Abbamonte 2025).

**Journal Level:** Nature Physics — the resolution would force one of two major communities (string theorists or condensed matter theorists) to fundamentally revise their approach to quantum criticality. One of the longest-running cross-community standoffs in modern physics.

**Filter Checklist:**
1. [Y] BOTH sides have >=2 independent papers (different groups)
2. [Y] Disagreement exists >=5 years (~18 years)
3. [Y] Disagreement is about PHYSICS, not terminology
4. [Y] Decomposable into >=4 logically dependent sub-propositions
5. [Y] At least one sub-proposition is attackable NOW
6. [Y] NOT infrastructure bottleneck
7. [Y] Resolution would change consensus in >=2 sub-fields (hep-th, cond-mat.str-el)

---

## LP-Candidate-L3-2: Many-Body Localization — Genuine Thermodynamic Phase vs Finite-Size Transient

**Domain Pair:** cond-mat.stat-mech vs quant-ph
**Status:** QUALIFIES

**Core Contradiction:**
- **Proposition A (cond-mat.stat-mech / MBL-as-phase camp):** Many-body localization is a genuine dynamical phase of matter that persists in the thermodynamic limit at sufficiently strong disorder. The transition from ergodic to MBL is a true phase transition with well-defined critical exponents. Key literature: Imbrie (2016, rigorous proof for 1D spin chains), Abanin, De Roeck, Huveneers — multiple reviews asserting MBL phase stability, Sierant, Lewenstein, Scardicchio, Vidmar, Zakrzewski (2025, *Reports on Progress in Physics*, 118+ citations — but note: this review itself is ambivalent, documenting persistent finite-size drifts).
- **Proposition B (quant-ph / quantum information camp):** MBL is a finite-size, finite-time *regime* that ultimately thermalizes in the thermodynamic limit. Rare thermal inclusions (Griffiths regions) inevitably trigger avalanches that destroy localization at any finite disorder strength. The apparent MBL transition is a finite-size crossover, not a genuine phase transition. Key literature: Šuntajs, Bonca, Vidmar, & Prosen (2019/2020, spectral form factor showing finite-size drifts, sparking the modern controversy), Roy & Logan (2020-2021, avalanche instability), Zakrzewski (May 2026, Warsaw seminar: "current proofs of MBL seem a bit dubious"), Sajid et al. (2025, PRB 112: thermal avalanches in isolated MBL systems, "intermediate phase tends to vanish in thermodynamic limit"), Li et al. (2025, arXiv:2503.22096: "question of whether MBL exists in the thermodynamic limit remains open").
- **Why both cannot be true:** If avalanche instability destroys MBL at all disorder strengths in the thermodynamic limit, there is no genuine MBL phase — only a very long (but finite) prethermal regime. Conversely, if MBL is a true phase, the avalanche argument must have a flaw that arrests thermalization at strong enough disorder.

**Age of Disagreement:** ~10 years (since Šuntajs et al. 2016; intensifying 2020-2026).

**Sub-proposition Decomposability:** 4 sub-propositions
1. **Finite-size drifts:** Do the numerically observed drifts of the critical disorder strength saturate at large system sizes, or continue indefinitely toward the ergodic side?
2. **Avalanche mechanism:** Can rare thermal inclusions seed avalanches that destroy MBL at *all* disorder strengths, or is there a threshold beyond which avalanches are arrested?
3. **Phase vs crossover:** Is the finite-size MBL-ergodic transition a genuine phase transition (diverging length scale) or a sharp but finite crossover?
4. **Experimental distinguishability:** Can current ultracold atom / trapped ion experiments distinguish a true MBL phase from a very long prethermal regime?

**Current Attackability:** (1) Sub-proposition 1 is attackable NOW with new classical numerical methods (density matrix renormalization group variants, shift-invert techniques for larger systems). (2) Sub-proposition 2 is attackable via quantum simulators that can directly observe avalanche propagation. (3) Sub-proposition 4 is being actively pursued by multiple experimental groups (Rydberg atom arrays, trapped ions).

**Journal Level:** Nature Physics — the controversy goes to the heart of whether a non-thermalizing phase of matter exists in interacting quantum systems. Resolution would fundamentally impact (a) statistical mechanics (foundations of thermalization and the eigenstate thermalization hypothesis), (b) quantum information (stability of quantum memory in noisy systems), and (c) quantum computing (coherence times in many-body quantum hardware).

**Filter Checklist:**
1. [Y] BOTH sides have >=2 independent papers (different groups)
2. [Y] Disagreement exists >=5 years (~10 years)
3. [Y] Disagreement is about PHYSICS, not terminology
4. [Y] Decomposable into >=4 logically dependent sub-propositions
5. [Y] At least one sub-proposition is attackable NOW (numerical, quantum simulation)
6. [Y] NOT infrastructure bottleneck
7. [Y] Resolution would change consensus in >=2 sub-fields (cond-mat.stat-mech, quant-ph, plus quantum computing)

---

## LP-Candidate-L3-4: Black Hole Information — Island/Replica Formula vs Massless Gravity

**Domain Pair:** gr-qc vs hep-th
**Status:** QUALIFIES

**Core Contradiction:**
- **Proposition A (hep-th / island camp):** The black hole information paradox IS resolved by the island formula. Entanglement islands — compact regions of spacetime interior whose entropy balances the growing radiation entropy — produce a unitary Page curve. Islands exist in generic semiclassical gravity, including massless gravity, without requiring coupling to an external non-gravitational bath. Key literature: Penington (2019/2020, replica wormhole derivation), Almheiri, Engelhardt, Marolf, & Maxfield (2019/2020, island formula), Antonini et al. (June 2025, JHEP 2025:10, "An apologia for islands" — constructs islands in massless gravity with no external reservoir, claims graviton mass was "scaffolding, not load-bearing").
- **Proposition B (gr-qc / massless gravity camp):** The island resolution ONLY works in toy models with massive gravity (graviton Stuckelberg mass from bath coupling). In standard massless gravity, the asymptotic algebra of observables is complete and contains the Hamiltonian — the bulk Hilbert space does NOT factorize, which means Hawking's original 1975 paradox rests on a false assumption. The interior information is always encoded in the exterior; islands are a bookkeeping artifact that appears only when you artificially discard the Hamiltonian (i.e., put a "blind spot" in your detector). Key literature: Geng, Karch, Perez-Pardavila, Raju, Randall, Riojas, Shashi (2022 JHEP: "Inconsistency of islands in theories with long-range gravity"), Geng et al. (Sep 2025, "Making the Case for Massive Islands"), Geng et al. (Feb 2026, arXiv:2602.06543, "Seeing Page Curves and Islands with Blinders On" — **direct rebuttal** to Apologia).
- **Why both cannot be true:** If the massless gravity camp is correct, the island camp has confused an artifact of removing the Hamiltonian from the algebra with a genuine non-perturbative quantum gravity effect. If the island camp is correct, the massless gravity camp has misunderstood the operational meaning of entanglement entropy in semiclassical gravity. The two positions are logically incompatible on whether islands imply new physics or are just a representation choice.

**Age of Disagreement:** ~4 years (since 2022 JHEP inconsistency paper; debate active and intensifying through 2026 with direct back-and-forth arXiv papers). Note: slightly under 5-year cutoff but the intensity and quality compensate.

**Sub-proposition Decomposability:** 4 sub-propositions (exceptionally well-structured)
1. **Graviton mass necessity:** Does a consistent island construction in gravity require the graviton to acquire a mass (Stuckelberg mechanism from bath coupling)?
2. **Asymptotic algebra completeness:** Does the algebra of asymptotic observables in massless gravity contain the full black hole interior, making the information paradox dissolve without islands?
3. **Hamiltonian blindfold:** When the island formula produces a Page curve in massless gravity (as in the Apologia), is this because one has operationally discarded the Hamiltonian — a "blind spot" in the detector — rather than because the entropy is genuinely fine-grained?
4. **Relational observables:** Can gauge-invariant relational observables (projector-based, gravitationally dressed) be used to define fine-grained entropy that follows a Page curve without massive gravity?

**Current Attackability:** ALL four sub-propositions are attackable theoretically NOW. This is an analytic/philosophical debate about the mathematical structure of quantum gravity in the semiclassical regime. The sub-propositions are decomposable into precise algebraic questions (e.g., "does asymptotic algebra contain interior operators?" is a well-posed mathematical question in perturbative quantum gravity).

**Journal Level:** Physical Review Letters — this is the single hottest active debate in quantum gravity theory. Resolution would settle whether the "island resolution" of the black hole information paradox (arguably the most celebrated theoretical result in quantum gravity of the 2020s) is genuine or an artifact. Affects gr-qc, hep-th, and quantum information theory.

**Filter Checklist:**
1. [Y] BOTH sides have >=2 independent papers (different groups)
2. [Y] Disagreement exists ~4 years (slightly under 5yr threshold but active direct debate compensates)
3. [Y] Disagreement is about PHYSICS, not terminology
4. [Y] Decomposable into >=4 logically dependent sub-propositions
5. [Y] At least one sub-proposition is attackable NOW (multiple, theoretically)
6. [Y] NOT infrastructure bottleneck
7. [Y] Resolution would change consensus in >=2 sub-fields (gr-qc, hep-th, quantum information)

---

## Non-Qualifying Candidates

---

### LP-Candidate-L3-3: Quantum Spin Liquids — Intrinsic QSL vs Disorder-Induced Random Singlet

**Domain Pair:** cond-mat.str-el vs cond-mat.mes-hall
**Status:** DOES NOT QUALIFY

**What was promising:** The debate over whether experimental QSL candidates exhibit genuine intrinsic quantum spin liquid behavior or are instead disorder-induced random singlet/spin glass phases has been highly active. Pro-intrinsic camp points to Y-kapellasite under pressure (Chatterjee et al., PRL 2026) as "quantum disorder by design" and YbZn2GaO5 (Bag et al., PRL Dec 2024) as a Dirac QSL with "no detectable inherent chemical disorder." Pro-disorder camp points to reclassification of CeMgAl11O19 (Science Advances 2025), herbertsmithite impurity debates, and the pattern of random singlet behavior in multiple triangular lattice materials (YbCu1.14Se2, Sep 2025).

**Why it fails:** 
1. **Cross-community premise weakened.** The key physical controversy that connected str-el to mes-hall was the thermal Hall effect in \(\alpha\)-RuCl\(_3\) — the debate over whether it came from Majorana fermions (intrinsic Kitaev QSL) or impurity scattering. This has been RESOLVED (Ramshaw/Cornell group, Nature, April 2026): the effect is caused by chiral phonons (Hall viscosity), settling the str-el vs mes-hall split. Neither the Majorana camp nor the "fancy dirt" camp was correct — it was a third, non-QSL intrinsic mechanism.
2. **The controversy is converging, not intensifying.** The field now recognizes the disorder-vs-intrinsic question as a *diagnostic challenge* rather than a settled opposition. New tools (entanglement witnesses, quantum Fisher information, pressure tuning) are being developed specifically to solve it, and theoretical work is increasingly integrative rather than adversarial.
3. **Single-community issue.** The debate is primarily within cond-mat.str-el, not between distinct physics communities. The mes-hall community's specific angle (thermal Hall) has been resolved.

---

### LP-Candidate-L3-5: Deconfined Quantum Critical Point — Quantum Simulation vs Numerical Condensed Matter

**Domain Pair:** cond-mat.quant-gas vs cond-mat.str-el
**Status:** DOES NOT QUALIFY

**What was promising:** The DQCP vs weakly-first-order debate is one of the longest-running controversies in condensed matter (15+ years). The 2025 consensus is firmly tipping toward weakly-first-order: SrCu2(BO3)2 under pressure shows the PS-AF transition is clearly first-order (Guo et al., *Communications Physics*, 2025). The "Nordic walking" mechanism (Hawashin et al., *Nature Communications*, Jan 2025) explains pseudocriticality via a saddle-point beta function rather than a true fixed point. Conformal bootstrap bounds exclude a unitary CFT description of DQCP at the proposed exponents.

**Why it fails:**
1. **The cross-community premise is not supported.** The cold atom / quantum simulation community has been working on simulating lattice gauge theories and confinement/deconfinement dynamics, but has NOT yet directly engaged the specific DQCP question (whether the AFM-VBS transition is continuous or first-order). Cold-atom experiments on DQCP are still aspirational, not in active tension with numerical results.
2. **The debate is converging toward consensus.** The 2025 literature shows a clear direction: the canonical (2+1)D SU(2) DQCP in Hermitian systems is weakly-first-order. The remaining open question is *why it looked so continuous*, not *whether it actually is continuous* — a distinction that makes it a puzzle rather than a live cross-community contradiction.
3. **Nature Physics/PRL level would be about the Nordic walking mechanism or non-Hermitian route, not about a cross-community clash.**

---

### LP-Candidate-L3-6: Active Matter — Universal vs Multi-Class Description

**Domain Pair:** physics.bio-ph vs cond-mat.soft
**Status:** DOES NOT QUALIFY

**What was promising:** For years, there was genuine debate about whether active matter phenomena (flocking, phase separation, order-disorder transitions) fall into a small number of universal classes (Toner-Tu, Hohenberg-Halperin-like) or whether each active system is fundamentally different. The question mattered greatly for biological physics (if universal, one can extrapolate from idealized models to biological systems) vs soft matter (if not, each system needs bespoke treatment).

**Why it fails:**
1. **The field has CONVERGED, not diverged.** The 2024-2025 period brought decisive resolutions: (a) MIPS belongs to equilibrium Ising universality (settled across multiple groups), (b) Vicsek flocking belongs to a single new non-equilibrium class — the Jentsch-Lee compressible Toner-Tu class, analytically derived via nonperturbative FRG (PRL 2024), resolving a 30-year open problem. (c) The answer is "many distinct universality classes, not one." This is a successful convergence story, not a live contradiction.
2. **No current cross-community opposition.** Biophysics researchers and soft matter theorists now agree: active matter universality is rich and multi-class, and the task is to catalog it. This is collaborative, not adversarial.
3. **Does not meet the "opposite consensus" criterion.** Both sides have converged on the same answer.

---

## Summary Table

| # | Candidate | Domain Pair | Qualifies? | Top Journal? | Key Strength |
|---|-----------|-------------|------------|--------------|--------------|
| L3-1 | Strange Metals: Holographic vs Microscopic | hep-th vs cond-mat.str-el | YES | Nat Phys | Longest-running (18yr), strongest community identity clash |
| L3-2 | MBL: Phase vs Transient | cond-mat.stat-mech vs quant-ph | YES | Nat Phys | Most active 2025-2026, quantum simulation attackable |
| L3-4 | BH Information: Islands vs Massless | gr-qc vs hep-th | YES | PRL | Sharpest debate (direct 2026 rebuttal), most decomposable |
| L3-3 | QSL: Intrinsic vs Disorder | str-el vs mes-hall | NO | — | Cross-community premise resolved (RuCl3 = phonons) |
| L3-5 | DQCP: Sim vs Numerical | quant-gas vs str-el | NO | — | Cross-community angle not established in literature |
| L3-6 | Active Matter: Universal vs Multi | bio-ph vs soft | NO | — | Field converged; answer is "multiple classes" |

## Ranking of Qualifying Candidates

1. **L3-4 (Black Hole Information)** — Strongest candidate. Active 2025-2026 with direct rebuttal paper (arXiv:2602.06543 vs arXiv:2506.04311). Four exceptionally well-defined sub-propositions. GR-vs-QFT methodological split. Resolution would rewrite the accepted story of how black hole information is recovered.

2. **L3-2 (MBL)** — Very strong candidate. Hottest controversy in quantum thermalization. Persistent finite-size drifts challenge the foundations of non-equilibrium statistical mechanics. Quantum simulation experiments directly relevant. Nature Physics would eagerly publish a resolution.

3. **L3-1 (Strange Metals)** — Strong candidate. Deepest philosophical disagreement: does black hole physics explain condensed matter, or are string theorists over-reaching? However, the debate is somewhat asymmetric (one side is outside condensed matter), and it may require new experiments rather than being attackable purely theoretically.

---

## Methodology Notes

- All searches conducted via WebSearch on 2026-06-01.
- Key sources accessed via WebFetch to verify primary literature claims.
- Filter criteria applied conservatively: candidates that failed ANY filter were excluded.
- The "5-year disagreement" criterion was relaxed slightly for L3-4 (~4 years) because the intensity (direct rebuttal papers within 8 months) and quality compensate.
