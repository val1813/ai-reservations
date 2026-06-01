# L1 Strategy Output: Review Paper Open Problem Mining

> SELECTOR v2.0 | Strategy L1 | Executed: 2026-05-31
> Search engine: WebSearch (primary; paper-search-mcp unavailable)
> Status: 4 candidates evaluated, 3 pass all filters, 1 borderline

---

## Search Summary

| # | Query | Key Findings |
|---|-------|-------------|
| 1 | "Reports on Progress in Physics" review 2025 2026 condensed matter | RPP 88 review: Sierant et al. (2025) MBL review; Skyrmion dynamics; Order-to-order QPT without fractionalization |
| 2 | "Reviews of Modern Physics" open problem 2025 2026 | RMP 97(4): Kitaev QSL review (Matsuda, Shibauchi, Kee); Multiple articles on topological/quantum matter |
| 3 | "Annual Review of Condensed Matter Physics" 2025 2026 | Vol.17 (2026): 18+ reviews including FQAH, 't Hooft anomalies, quantum critical Eliashberg theory, 2D ferroics |
| 4 | "Nature Reviews Physics" 2025 2026 | Yang-Mills Millennium problem; Collective dynamics on higher-order networks; Simulating topological order on quantum processors; Quantum geometry and hidden scales |
| 5 | "Physics Reports" review 2025 2026 | Vol.1160 (2026): "Topological Physics in Quantum Critical Systems" (Yu, Xu, Lin); Quantum complexity review |
| 6 | "open problem" quantum spin liquid review 2024-2026 | RMP 97 Kitaev QSL review; Ramirez & Syzranov (2025) Materials Advances; CPL 42 kagome QSL review; Multiple >50y unsolved |
| 7 | "open question" many-body localization review | Sierant et al. RPP 2025; Roy & Logan JPCM 2025; Li et al. 2025 arXiv; Laflorencie colloquium |
| 8 | strange metal / non-Fermi liquid open problems | Hu et al. Nat.Phys. 2024 (QC metals); Else ARCM 2025 ('t Hooft anomalies); Aydin PNAS 2024; Zhan PRL 2025 |
| 9 | DQCP review open problem | Senthil 2024 review; Cui, Yu, Yu CPL 2025; Song et al. 2025 entanglement entropy |
| 10 | High-Tc pairing mechanism | Multiple reviews (Al-Imad 2025, JPCM 2025, Acta Phys.Pol. 2025) confirm unresolved |
| 11 | Dean's Clue #1: Planckian + info | Chowdhury 2026 arXiv (Fisher info bound); Abiuso 2025 (info-theoretic proof); Foini 2026 (classical hydro) |
| 12 | Dean's Clue #2: MBL bath-coupling + avalanche | Zhang et al. Sci.Rep. 2026; Shen et al. 2026 (power-law interactions); Sajid et al. 2025 (embedded thermal inclusion) |
| 13 | Dean's Clue #4: Diophantine + topology | No results found |

---

## LP-Candidate-1: Does Many-Body Localization Exist as a Genuine Thermodynamic Phase?

**Source:** L1 + Dean's Clue #2 (bath-coupling geometry x MBL avalanche)

**Core Contradiction:**
- **Proposition A:** MBL is a genuine thermodynamic phase of matter that survives in the asymptotic limit of infinite system size and infinite evolution time. Localization is robust against rare-region avalanches and quantum Griffiths effects. (Sierant, Lewenstein, Scardicchio, Vidmar, Zakrzewski, Rep. Prog. Phys. 88, 026502, 2025; Abanin et al., Rev. Mod. Phys. 91, 021001, 2019)
- **Proposition B:** MBL is a finite-size/finite-time transient regime that eventually thermalizes in the thermodynamic limit due to quantum avalanches from rare ergodic inclusions. The MBL "phase" is an effective crossover, not a true phase transition. (Roy & Logan, J. Phys. Cond. Mat. 37, 073003, 2025; Li et al., arXiv:2503.22096, 2025; Vanoni, Altshuler, Kravtsov, Scardicchio, PNAS 2024)
- **Why cannot both be true:** A system cannot both thermalize and remain localized in the thermodynamic limit — these are mutually exclusive asymptotic behaviors. The persistent finite-size drifts toward ergodicity seen in numerical data rule out naive single-parameter scaling, making current computational evidence consistent with both interpretations.

**Independent Source Count:** 5 (>=3, pass)
1. Sierant et al. (2025) — Rep. Prog. Phys. 88, 026502 (corresponding: IF PAN Warsaw, ICFO Barcelona, Sapienza Rome, Jozef Stefan Ljubljana, Jagiellonian Krakow)
2. Roy & Logan (2025) — J. Phys. Cond. Mat. 37, 073003 (corresponding: Oxford Chemistry)
3. Li et al. (2025) — arXiv:2503.22096 (explicit: "remains open")
4. Vanoni, Altshuler, Kravtsov, Scardicchio (2024) — PNAS (RG analysis on random regular graphs as MBL proxy)
5. Laflorencie Colloquium (ENS Lyon, Sep 2025) — "Intricacies of the many-body localization problem" — explicit open problem framing

**Sub-proposition Decomposability:** >=3 (pass)
- **LP1-S1 [Scaling & Criticality]:** Does the ETH-MBL crossover exhibit critical scaling consistent with a genuine continuous phase transition, or is it always smeared by finite-size effects? (Logic: If no critical scaling exists, MBL is not a phase transition → B wins. If critical scaling is found → proceed to S2.)
- **LP1-S2 [Avalanche Stability]:** If critical scaling is established (S1 passes), do quantum avalanches from rare thermal inclusions inevitably destroy the MBL phase in the thermodynamic limit? This depends on bath-coupling geometry (Dean's Clue #2): boundary coupling → O(1/sqrt(N)) suppression; distributed coupling → O(1) no suppression. The Z2-preserving Ising Majorana chain (Zhang et al. 2026) and power-law interaction avalanche studies (Shen et al. 2026) provide new tools.
- **LP1-S3 [Dimensionality]:** If MBL survives avalanches in 1D (S2 passes), does it also survive in 2D and higher dimensions? 2D MBL is theoretically more fragile due to enhanced rare-region effects and boundary-to-volume ratio. Current evidence (percolation blocking in 2D) is suggestive but inconclusive. (Reference: 2D MBL self-limiting = percolation obstruction of thermalization front; Dean's Clue #2)
- **LP1-S4 [Quantum Verification]:** Can quantum simulators/processors access system sizes beyond the classical exponential wall to directly test MBL in the thermodynamic limit? This is the ultimate resolution pathway. (Sierant et al. 2025: "quantum computers might open an entirely new chapter")
- **Dependencies:** S1 (no prerequisite) → S2 (depends on S1 passing) → S3 (depends on S2 passing). S4 is parallel (methodological, can proceed independently).

**Recent Progress (2024-2026):** (pass)
- Sierant et al. comprehensive RPP review (Jan 2025) — definitive survey of 795 references, concludes MBL phase status is "central unanswered question"
- Roy & Logan Fock-space perspective review (2025) — new framework for understanding MBL transition via graph theory
- Multiple avalanche instability studies (Zhang et al. Sci.Rep. 2026; Shen et al. arXiv:2601.13485; Sajid et al. arXiv:2506.04834) — provide quantitative criteria for when avalanches destroy localization
- Li et al. (March 2025) — "question of whether MBL exists or not in any system in the thermodynamic limit remains open"
- Quantum computing proposals for MBL verification gaining traction

**Collaboration Monopoly Check:** (pass) — MBL is studied by dozens of independent groups worldwide (Poland/Barcelona/Rome/Ljubljana/Krakow for Sierant review, Oxford for Roy-Logan, Tsinghua/China for avalanche studies, ENS Lyon, Columbia, Princeton, etc.). No single collaboration dominates.

**Infrastructure Bottleneck Check:** (pass) — The problem is theoretical + numerical. Quantum computers may accelerate resolution but are not required; sub-propositions S1-S3 are attackable with classical numerics + analytical theory. Not a "need bigger collider" class problem.

**Cross-field Impact:** Solving MBL would affect (a) statistical mechanics (thermalization/eigenstate thermalization hypothesis foundations), (b) quantum information science (entanglement dynamics in disordered systems), (c) condensed matter physics (disordered quantum materials), and (d) quantum computing (error correction in noisy devices). At least 4 sub-fields.

---

## LP-Candidate-2: What is the Origin of Planckian Dissipation in Strange Metals?

**Source:** L1 + Dean's Clue #1 (v2-deepseek x LP-2 Planckian dissipation)

**Core Contradiction:**
- **Proposition A:** Planckian dissipation (T-linear resistivity with scattering rate ~ kBT/hbar) in strange metals arises from non-quasiparticle physics — the destruction of Landau quasiparticles at a quantum critical point. The T-linear resistivity is a signature of a fundamentally new metallic state without well-defined electronic excitations. (Hu et al., Nat. Phys. 20, 1863, 2024; Else, ARCM 17, 2026; Hong & Xu, arXiv:2410.13858, 2024; Park & Choi, arXiv:2408.14858, 2024)
- **Proposition B:** T-linear resistivity with Planckian scattering rates can emerge from well-defined quasiparticles with anomalous scattering mechanisms (e.g., phonon-based quantum acoustics, extended Boltzmann kinetics). The Planckian timescale is the saturation limit of conventional scattering, not evidence for quasiparticle destruction. (Aydin, Keski-Rahkonen, Heller, PNAS 121, e2404853121, 2024; Zhan et al., PRL 135, 266504, 2025)
- **Why cannot both be true:** Quasiparticles either exist as well-defined excitations (finite Z > 0) or they do not (Z → 0) in the strange metal regime. These are mutually exclusive descriptions of the same electronic state.

**Independent Source Count:** 5 (>=3, pass)
1. Hu et al. (2024) — Nat. Phys. 20, 1863-1873 (review; corresponding: multiple US institutions; Proposition A)
2. Else (2025/2026) — ARCM 17, 71-90 (invited review; "'t Hooft anomalies in metals"; corresponding: Perimeter Institute)
3. Aydin, Keski-Rahkonen, Heller (2024) — PNAS 121, e2404853121 ("origin remains elusive"; corresponding: Aalto/Harvard; Proposition B)
4. Zhan et al. (2025) — PRL 135, 266504 ("open challenge"; corresponding: Zhejiang/Rutgers/Cologne/Max Planck; Proposition B)
5. Hong & Xu (2024) — arXiv:2410.13858 ("unresolved issues in non-Fermi liquids"; Proposition A)

**Sub-proposition Decomposability:** >=3 (pass)
- **LP2-S1 [Quasiparticle Weight Z]:** Does the quasiparticle residue Z vanish in the strange metal regime? This can be tested via ARPES lineshape analysis, STM tunneling, or quantum oscillation measurements. (Logic: If Z > 0 → Proposition B is favored. If Z → 0 → Proposition A is favored.)
- **LP2-S2 [Planckian Bound Nature]:** Is the Planckian bound τ >= hbar/(kBT) a kinematic information-theoretic limit (as proven by Abiuso et al. 2025 from Hamiltonian estimation bounds) or a dynamical bound that depends on specific microscopic mechanisms? If kinematic, then any microscopic model can at most saturate it — the bound itself demands no particular mechanism. If dynamical, the mechanism matters. (Dean's Clue #1: information回流泛函as Planckian bound mechanism)
- **LP2-S3 [Quasiparticle-Free Transport Theory]:** If Z → 0 (S1 passes), can a controlled theoretical framework without quasiparticles quantitatively reproduce the full phenomenology (T-linear resistivity, T-log specific heat, power-law optical conductivity)? Current candidates (SYK, holographic, critical Fermi surface) all have gaps.
- **LP2-S4 [Universality Across Material Classes]:** Why does T-linear resistivity appear in cuprates, heavy fermions, organics, pnictides, and now ferromagnetic strange metals (Zhan 2025)? Is there a universal organizing principle, or are these distinct phenomena with coincidentally similar phenomenology?
- **Dependencies:** S1 (prerequisite for S2,S3) → S2 (depends on S1; establishes kinematic vs dynamical status) → S3 (depends on S1 confirming Z→0). S4 is parallel (phenomenological survey, can proceed independently).

**Recent Progress (2024-2026):** (pass)
- Abiuso et al. (June 2025): First information-theoretic proof of Planckian bound for thermalization — shows τ >= τ_Pl/2 from Hamiltonian estimation
- Chowdhury (Feb 2026): "Information, Dissipation, and Planckian Optimality" — derives universal bound connecting quantum Fisher information to Planckian frequency; Planckian scatterers sit at edge of optimality
- Foini, Kurchan, Pappalardi (May 2026): "Planckian Dissipation from Classical Hydrodynamics" — Planckian scaling emerges as price for classical hydrodynamic describability at low T
- Hu et al. (Nov 2024): Nature Physics review unifying strange metal phenomenology across material classes
- Else (2026): ARCM review framing T-linear resistivity as challenge to 't Hooft anomaly framework
- Zhan et al. (Dec 2025): First observation of strange metal behavior in a ferromagnetic quantum critical system — extends universality
- Aydin et al. (2024): Quantum acoustics as alternative explanation — phonons can produce Planckian resistivity

**Collaboration Monopoly Check:** (pass) — Strange metal research spans hundreds of groups worldwide. No single collaboration dominates.

**Infrastructure Bottleneck Check:** (pass) — The problem is attackable with existing experimental data (ARPES, transport, optical conductivity) + theoretical tools. S1 can be tested with existing ARPES data. Not a "need bigger facility" class problem.

**Cross-field Impact:** Solving would affect (a) strongly correlated electron physics (foundations of non-Fermi liquid theory), (b) quantum thermodynamics (Planckian bound as universal thermodynamic constraint), (c) quantum information (Fisher information/estimation bounds in thermal states), (d) hydrodynamics (limits of classical hydrodynamic description of quantum systems). At least 4 sub-fields.

---

## LP-Candidate-3: Is Deconfined Quantum Criticality Genuinely Continuous or Weakly First-Order?

**Source:** L1

**Core Contradiction:**
- **Proposition A:** The deconfined quantum critical point (DQCP) between Neel and valence-bond-solid phases is a genuine continuous quantum phase transition, described by a unitary conformal field theory with emergent gauge fields, fractionalized excitations (spinons), and enhanced emergent symmetry (e.g., SO(5)). This represents a paradigm beyond Landau-Ginzburg-Wilson. (Senthil, "Deconfined quantum critical points: a review," 50 Years of the Renormalization Group, 2024; Cui, Yu, Yu, Chin. Phys. Lett. 42, 047503, 2025)
- **Proposition B:** The DQCP is actually a weakly first-order transition masked by finite-size effects. The apparent "continuous" scaling is a crossover phenomenon; the entanglement entropy shows anomalous logarithmic corrections incompatible with any unitary CFT at small N. (Song et al., arXiv:2307.02547v5, 2025; Takahashi & Sandvik, arXiv:2405.06607, 2024)
- **Why cannot both be true:** A phase transition cannot be simultaneously continuous (diverging correlation length, no latent heat) and first-order (finite correlation length at transition, latent heat). These are mutually exclusive.

**Independent Source Count:** 4 (>=3, pass)
1. Senthil (2024) — "Deconfined quantum critical points: a review" (MIT, originator of DQCP concept; Proposition A)
2. Cui, Yu, Yu (2025) — Chin. Phys. Lett. 42, 047503 "Deconfined Quantum Critical Point: A Review of Progress" (Renmin Univ.; neutral review of both sides)
3. Song et al. (2025) — arXiv:2307.02547v5 "Evolution of entanglement entropy at SU(N) DQCP" (Proposition B: anomalous log corrections incompatible with unitary CFT)
4. Takahashi & Sandvik (2024) — arXiv:2405.06607 "SO(5) symmetric DQCP in extended J-Q model" (Proposition B: true DQCP may be in sign-problematic region inaccessible to QMC)

**Sub-proposition Decomposability:** >=3 (pass)
- **LP3-S1 [Entanglement Diagnostic]:** Is the anomalous logarithmic subleading correction to entanglement entropy at smooth boundaries a robust diagnostic of weakly first-order behavior, or can it be explained by unconventional CFT features? Song et al. (2025) found log-correction vanishes for N>=8. If the diagnostic is robust, it favors Proposition B for SU(2).
- **LP3-S2 [Sign Problem Crossing]:** Can the sign-problematic region of the extended J-Q model (where Takahashi & Sandvik claim the true DQCP with SO(5) symmetry resides) be accessed via new numerical methods (neural quantum states, tensor networks, quantum computing)? If accessible, does a continuous DQCP exist there?
- **LP3-S3 [Experimental Realization]:** Can SrCu2(BO3)2 under magnetic field or other candidate platforms (honeycomb YbBr3, kagome systems) provide a definitive experimental test that distinguishes continuous from weakly first-order? Current evidence is only "proximate" to DQCP.
- **LP3-S4 [Complex DQCP]:** If SU(2) DQCP is weakly first-order in real (Hermitian) parameter space, does it become genuinely continuous in complex (non-Hermitian) extensions? (Zou et al., arXiv:2511.03456, 2025) This would resolve the contradiction by showing DQCP is a "complex fixed point."
- **Dependencies:** S1 → S2 (if entanglement diagnostic is robust, need to check if true DQCP is elsewhere in parameter space). S3 (experimental) and S4 (complex extension) are parallel alternative resolution paths.

**Recent Progress (2024-2026):** (pass)
- Song et al. (Jan 2025): Systematic entanglement entropy study of SU(N) DQCP — identifies N_c ~ 7-8 as threshold where anomalous log-correction vanishes
- Takahashi & Sandvik (2024): SO(5)-symmetric DQCP found in extended J-Q model but potentially hidden by sign problem
- Zou et al. (2025): Non-Hermitian DQCP — complex fixed point approach may resolve the contradiction
- Yu, Xu, Lin (2026): Physics Reports 1160 — "Topological Physics in Quantum Critical Systems" — comprehensive pedagogical review including DQCP and related beyond-LGW criticality
- SrCu2(BO3)2 experiments: First proximate DQCP evidence via field-induced BEC (2024-2025)

**Collaboration Monopoly Check:** (pass) — DQCP is studied by independent groups at MIT, Boston Univ., Duke, UCSB, ETH Zurich, Renmin Univ., Fudan, Inst. of Physics CAS, and others.

**Infrastructure Bottleneck Check:** (pass) — Problem is theoretical + numerical + existing-experimental. S1-S2 are pure theory/numerics. S3 uses existing experimental platforms. No new collider/detector needed.

**Cross-field Impact:** Solving DQCP would affect (a) quantum criticality theory (beyond-LGW paradigm), (b) high-energy/CFT community (conformal bootstrap bounds, non-unitary CFTs), (c) quantum magnetism (unconventional phase transitions in frustrated magnets), (d) quantum information (entanglement as phase transition diagnostic). At least 4 sub-fields.

---

## LP-Candidate-4 [BORDERLINE]: Are Any Candidate Materials Confirmed Quantum Spin Liquids, or Are All Observed Signatures Due to Disorder?

**Source:** L1

**Core Contradiction:**
- **Proposition A:** Specific candidate materials (herbertsmithite, Ce2Zr2O7, YCu3-Br, alpha-RuCl3 under field) host intrinsic quantum spin liquid ground states with fractionalized spinon excitations and emergent gauge structure. (Matsuda, Shibauchi, Kee, Rev. Mod. Phys. 97, 2025; CPL 42 kagome QSL review 2025)
- **Proposition B:** All QSL-like signatures observed to date can be explained by quenched disorder — random singlet phases, spin glasses, or defect-induced phenomena — rather than intrinsic QSL physics. No material has met the burden of proof for definitive QSL identification. (Ramirez & Syzranov, Materials Advances, 2025; multiple independent studies showing YbMgGaO4/YbZnGaO4 are spin glasses, not QSLs)
- **Why cannot both be true:** A material cannot simultaneously host an intrinsic topological QSL ground state and a disorder-dominated random singlet/spin-glass ground state. The ground state is either one or the other.

**Independent Source Count:** 4 (>=3, pass)
1. Matsuda, Shibauchi, Kee (2025) — RMP 97 (Kyoto/Tokyo/Toronto; neutral: "results and interpretations remain actively debated")
2. Ramirez & Syzranov (2025) — Materials Advances (UC Santa Cruz; strongly skeptical: "no consensus that QSLs have been conclusively identified")
3. CPL kagome QSL review (2025) — Chin. Phys. Lett. 42, 070716 (CAS; identifies disorder/structural randomness as key obstacle)
4. Shimokawa, Sabharwal & Shannon (Jun 2025) — arXiv (OIST; proposes QFI as entanglement witness to distinguish QSL from random singlet)

**Sub-proposition Decomposability:** >=3 (pass but borderline)
- **LP4-S1 [Entanglement Witness]:** Can quantum Fisher information (QFI) or other experimentally accessible entanglement measures definitively distinguish intrinsic QSL ground states from disorder-driven random singlet phases? Shimokawa et al. (2025) propose QFI; this needs experimental validation.
- **LP4-S2 [Candidate Screening]:** If S1 validates QFI as a diagnostic, apply it to leading candidates (herbertsmithite, YCu3-Br, Ce2Zr2O7, alpha-RuCl3) to determine which pass. This would rapidly narrow the field.
- **LP4-S3 [Disorder-Free Synthesis]:** Can chemical synthesis produce a kagome or triangular lattice QSL candidate with defect concentrations below the threshold where disorder mimics QSL signatures? The YCu3-Br family is the current best effort.
- **Dependencies:** S1 (prerequisite) → S2 (depends on S1 diagnostic). S3 is parallel (materials engineering).
- **Weakness:** The sub-proposition dependencies are looser than LP1-3 (S3 could be pursued without S1-S2). More a "parallel challenges" structure than strict logical chain.

**Recent Progress (2024-2026):** (pass, but weaker)
- Ce2Zr2O7 (Dec 2025): "First clear observation of 3D QSL state" — emergent photons via neutron scattering (Rice/TU Wien)
- QFI entanglement witness proposal (Jun 2025): First experimentally viable method to distinguish QSL from disorder
- YCu3-Br: Cleaner kagome platform reduces magnetic impurity problem of herbertsmithite
- EPFL Rydberg simulator (2025): Negative result — topological entanglement entropy never reached expected value under adiabatic preparation
- ErTa7O19: Reentrant QSL (order at 110 mK destabilizes at lower T)

**Collaboration Monopoly Check:** (pass) — QSL research spans many independent groups worldwide.

**Infrastructure Bottleneck Check:** (pass) — Problem is experimental (existing neutron scattering, NMR, muSR facilities) + theoretical.

**BORDERLINE NOTE:** The A vs B structure is weaker than LP1-3. The core tension is real (intrinsic QSL vs disorder-mimic), but the "cannot both be true" framing is at the material-specific level rather than the universal level. The sub-proposition chain is less tightly logically dependent. Quality score: lower than LP1-3. **Recommendation: Include in candidate pool with "LOWER PRIORITY" tag.**

---

## Dean's Clues Integration Summary

| Clue | Quality | LP Connection | Extra Search Results | Integration |
|-------|---------|---------------|---------------------|-------------|
| #1: v2-deepseek x LP-2 Planckian | L2-reliable | LP-Candidate-2 (Planckian bound nature) | 3 papers (Chowdhury 2026, Abiuso 2025, Foini 2026) connecting Planckian bound to QFI, Hamiltonian estimation, classical hydro | LP2-S2 directly addresses: kinematic vs dynamical bound — "information回流泛函" as Planckian bound mechanism |
| #2: bath-coupling x MBL avalanche | L2-reliable | LP-Candidate-1 (MBL avalanche stability) | 3 papers (Zhang 2026, Shen 2026, Sajid 2025) on boundary coupling effects on MBL stability | LP1-S2 incorporates: boundary vs distributed coupling geometry determines avalanche propagation — key to resolving thermodynamic limit question |
| #4: MBL Diophantine x LP-3 topology | L1-pending | No direct LP connection | No results found | Clue domain currently not searchable — no review literature connecting Diophantine conditions to topological protection found. **Recommendation: Schedule re-check in 3 months.** |

---

## Filter Summary

| Candidate | >=3 Reviews | A vs B | >=3 Sub-props | Recent Progress | No Monopoly | Cross-field Impact | Not Infrastructure | Overall |
|-----------|-----------|--------|--------------|-----------------|-------------|-------------------|-------------------|--------|
| LP1: MBL Phase | PASS (5) | PASS | PASS (4) | PASS | PASS | PASS (4 fields) | PASS | **QUALIFIED** |
| LP2: Planckian/Strange Metal | PASS (5) | PASS | PASS (4) | PASS | PASS | PASS (4 fields) | PASS | **QUALIFIED** |
| LP3: DQCP Nature | PASS (4) | PASS | PASS (4) | PASS | PASS | PASS (4 fields) | PASS | **QUALIFIED** |
| LP4: QSL Identification | PASS (4) | PASS (weaker) | PASS (3, loose) | PASS | PASS | PASS (3 fields) | PASS | **BORDERLINE** |

---

## No Qualifying Candidate Found For:

- **High-Tc pairing mechanism:** While >=5 independent reviews confirm it as unsolved, the core issue is "what is the mechanism?" rather than a clean "A vs B, cannot both be true." The problem decomposes into aspects (spin fluctuation, phonon, orbital fluctuation channels) that are potentially cooperative rather than strictly exclusive. Failed Filter 2 (A vs B structure).

- **Dean's Clue #4 (Diophantine x topology):** No review literature found in 2024-2026. This domain may require original research seeding before generating review-level open problems. **Recommendation: flag for ai3/DEAN re-evaluation.**

- **Hubbard model adequacy for cuprates:** The 2025 SLAC PRL paper showing Hubbard model failure in 1D cuprates is a single-source claim. While extremely significant, it has not yet been cited by >=3 independent reviews as a major open problem. Premature for L1 — may mature into a strong candidate within 12-18 months.

- **Yang-Mills mass gap:** Mentioned in Nature Reviews Physics (Douglas 2026) as explicit open problem, but is a millennium-prize mathematical physics problem. Fails Filter 6 (not primarily a condensed matter/quantum physics issue affecting >=2 sub-fields of physics rather than pure mathematics) and Filter 5 (no monopoly, but progress on the problem is essentially stalled). Also pure mathematical formalism bottleneck — not decomposable into experimentally attackable sub-propositions.

---

## Methodological Notes

1. paper-search-mcp was not available as a tool in this execution environment. All searches used WebSearch (Google). While this produced useful results, academic-database-specific search (Semantic Scholar API, arXiv API, INSPIRE-HEP) would likely yield more targeted review paper results. If paper-search-mcp becomes available, recommend re-running the 5 core L1 queries for potentially better review paper recall.

2. Chinese-language reviews (e.g., Chinese Physics Letters, Acta Physica Sinica) were captured but English-language RMP/Nature Reviews/Physics Reports coverage was sparser than expected via WebSearch. Direct journal website browsing may supplement.

3. The Dean's Clue #4 failure (Diophantine x topology) suggests this is a genuine literature gap — an opportunity for the SELECTOR to track an emerging intersection before review-level consensus forms.

4. Total search iterations: 28 WebSearch calls over approximately 30 minutes. Three qualifying long proposition candidates produced. System stopped early per "凑够2个即停" rule, plus one borderline for completeness.
