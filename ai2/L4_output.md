# SELECTOR v2.0 — Strategy L4 Output
## Long-Standing Open Problems + New Tools (2021-2026)

**Generated:** 2026-06-01
**Target Quality:** Nature Physics / Physical Review Letters level
**Method:** Search for problems explicitly listed as "open/unsolved" in review papers spanning >=20 years, where new tools in 2021-2026 make them newly attackable.

---

## Evaluation Summary

| # | Candidate | Age | Review Span | New Tool 2021-26 | >=3 Sub-prop | Not Infra | ≥2 Fields | Score |
|---|---|---|---|---|---|---|---|---|
| L4-1 | Pseudogap-SC Competition | ~40yr | 1999-2025 | Time-res. ARPES, RIXS, QFI | 4 | YES | YES | 6/6 |
| L4-2 | QSL Positive Identification via QFI | ~53yr | 1973-2025 | QFI-INS, QFI-RIXS | 4 | YES | YES | 6/6 |
| L4-3 | Strange Metal: Phase or Phenomenon? | ~37yr | 1989-2025 | QFI witness, Quantum acoustics | 3 | YES | YES | 6/6 |
| L4-4 | Ideal Glass Transition Existence | ~50yr | 1995-2026 | MLIPs (M-atom), Info-theory | 4 | PARTIAL | YES | 5/6 |
| L4-5 | Turbulence Intermittency First-Principles | ~140yr | 1883-2026 | EddyFormer, AI closure | 3 | NO | YES | 4/6 |
| L4-6 | DM Small-Scale Crisis vs. Baryonic Fdbk | ~30yr | 1994-2026 | JWST wide binaries | 3 | NO | YES | 3/6 |

---

## LP-Candidate-L4-1: Does the Pseudogap Phase Promote or Suppress Superconductivity in Cuprates?

**Age:** ~40 years (since cuprate discovery, 1986; pseudogap discovered ~1996 by Ding et al., Nature 382, 51)

**Old Stuck Reason:** The pseudogap phase is the defining enigma of the cuprate phase diagram, but until 2024-2025, all probes were static — they measured equilibrium spectral properties (ARPES, STM, transport) that could not distinguish between (A) the pseudogap as preformed Cooper pairs that promote SC, and (B) the pseudogap as a competing order that suppresses SC. The two phases coexist in equilibrium, so only time-domain experiments could disentangle causal direction.

**New Tools (2021-2026):**
- **Time-resolved ARPES** (Armanno, Boschini et al., Nov 2025, arXiv:2511.20768): First direct real-time observation of pseudogap-SC competition in optimally-doped Bi-2212. When SC is disrupted by a laser pulse, pseudogap emerges below Tc; when SC recovers, pseudogap is suppressed. Directly challenges the "preformed pairs → phase coherence" paradigm.
- **Ultra-high-resolution polarimetric RIXS** (Scott et al., PRB 109, 125126, 2024; Huang et al., PRB 112, L041124, July 2025): Full polarization-resolved RIXS at Cu-L3 and O-K edges now disentangles spin, charge, and phonon contributions to the pseudogap and SC energy scales. Detwinning under uniaxial strain reveals isotropic quantum critical charge dynamics decoupled from static stripe order.
- **Quantum Fisher Information from INS** (Bippus et al. 2025; Fang et al., Nat. Commun. 16, 2498, March 2025): Multipartite entanglement peaks in the pseudogap regime and is cut off by SC onset — providing an entanglement-based order parameter for the pseudogap state.
- **AI/ML approaches** (Yamaji, NIMS Nature Commun., Oct 2025): Neural network wavefunctions probe the pseudogap's many-body structure beyond what analytical methods can reach.

**Core Contradiction:** (A) Pseudogap = preformed Cooper pairs lacking phase coherence → SC emerges when pairs condense (promotes SC). (B) Pseudogap = distinct competing order (charge/spin/pair-density-wave) that gaps the Fermi surface → suppresses SC by stealing spectral weight. The 2025 time-resolved ARPES result strongly favors (B), but preformed-pair advocates (Solovjov et al. 2025; Shah et al. 2025) point to particle-hole symmetry in equilibrium ARPES above Tc as evidence for (A). This direct contradiction is now experimentally resolvable for the first time.

**Sub-propositions:**
1. **Causality test:** Does pseudogap amplitude increase when SC is suppressed on femtosecond timescales? (Testable: time-resolved ARPES at multiple dopings)
2. **Spectral weight bookkeeping:** Does the pseudogap gap magnitude equal the SC gap at the same k-point? (Testable: high-resolution polarimetric RIXS + ARPES joint analysis)
3. **Entanglement structure:** Is the multipartite entanglement in the pseudogap regime of the same type as in the SC state? (Testable: QFI from INS on multiple cuprate families)
4. **Uniaxial strain tuning:** Can pseudogap and SC be separated by symmetry? (Testable: RIXS under uniaxial strain on detwinned crystals — Huang et al. 2025 already shows isotropic charge dynamics)

**Journal Level:** Nature Physics — this is THE sharpest sub-question within THE most famous unsolved problem in condensed matter physics. The 2025 time-resolved ARPES result (Armanno/Boschini) already made waves; a systematic multi-doping, multi-probe study resolving the promote-vs-suppress question would be a cover story.

**References (Key Reviews Marking It as Open):**
- Wittlin, Acta Phys. Pol. A 147, 370 (2025): "The mechanism of high-temperature superconductivity remains a subject of research"
- Elliwan, Al-Imad J. Appl. Human Sci. (July 2025): "A unified theory for unconventional pairing in cuprates and iron-based systems remains elusive"
- Clement et al., Asian J. Res. Rev. Phys. (Nov 2025): Comprehensive pseudogap review; notes different probes locate pseudogap boundary at different doping levels
- Nature Physics (2025, on Yamaji effect): "The nature of the Fermi surface in the pseudogap state has remained a fundamental open question"
- Anderson, Science 235, 1196 (1987): Original RVB proposal for cuprates — framing the problem
- Tallon & Loram, Physica C 349, 53 (2001): Early review marking pseudogap as key unsolved puzzle

**Years covered by reviews:** 1987-2025 (38 years)

---

## LP-Candidate-L4-2: Can Quantum Fisher Information from Inelastic Neutron/RIXS Positively Distinguish Intrinsic Quantum Spin Liquid from Disorder-Induced Random Singlet States?

**Age:** ~53 years (Anderson's RVB proposal, Mater. Res. Bull. 8, 153, 1973)

**Old Stuck Reason:** Quantum spin liquids (QSLs) are defined by the absence of conventional order — they have no order parameter. For 50 years, experiments could only report "no magnetic order down to X mK" and "continuum of excitations" — both consistent with either a genuine QSL OR a random singlet glass produced by quenched disorder. No positive experimental witness existed that could say "this is a QSL, not something else." The problem was fundamentally tool-limited: you cannot measure what you cannot define operationally.

**New Tools (2021-2026):**
- **QFI from Inelastic Neutron Scattering** (Sabharwal, Shimokawa & Shannon, Phys. Rev. Res. 7, 023271, 2025; Zhou, Zhou, Kim & Meng, arXiv:2603.19951, March 2026): QFI — a metrological quantity bounding multipartite entanglement depth — extracted from INS data provides the first positive entanglement witness for QSL states. Crucially, it can distinguish intrinsic QSLs from disorder-driven random singlet states because only the former exhibits a specific finite-temperature entanglement scaling signature. The Zhou et al. (2026) work maps the critical behavior of the transition into a Z2 QSL on the kagome lattice, identifying the (2+1)d XY* universality class with a large anomalous dimension — a fingerprint inaccessible to conventional probes.
- **QFI extended to RIXS** (Shen, Ding, Zhao, Evangelista & Wang, arXiv:2512.06718, Dec 2025): Construction of Hermitian generators from polarization-reversed RIXS spectra enables QFI computation in systems with intrinsic spin-orbital entanglement. This is critical because real Kitaev/QSL candidate materials (iridates, ruthenates) have non-factorizable spin-orbital wavefunctions that the "qubit" assumption of standard QFI inherits from quantum information theory cannot handle.
- **Optical detection of Kitaev QSL** (UNIST-Yonsei, Nature Commun., Feb 2025): Exciton-based optical detection of spin fluctuations in 20-nm Co-oxide thin films with strong Kitaev interactions, providing an alternative to neutron methods that struggle with thin-film geometries.
- **Charge-transfer engineering** (Ojeda-Aristizabal et al., arXiv:2511.13838, Nov 2025): 21-author review showing work-function-mediated charge transfer can enhance Kitaev interactions by up to 50% in heterostructures — a new materials engineering lever unavailable before 2024.
- **Ultraclean single-crystal synthesis** (Xing et al., npj Quantum Materials, 2025): Two-step sublimation producing α-RuCl3 crystals with dramatically reduced stacking faults, enabling re-evaluation of whether the half-quantized thermal Hall effect is intrinsic.

**Core Contradiction:** (A) Candidate materials like α-RuCl3, YCu3(OH)6Br3, and NaYbSe2 host bona fide QSL ground states with fractional excitations and topological order. (B) All candidate materials contain disorder (stacking faults, chemical inhomogeneity) that could produce the observed featureless susceptibility and excitation continua without any QSL physics. The QFI framework now provides the first positive criterion: a multipartite entanglement depth signature that is specific to QSL states and survives in the presence of realistic disorder levels.

**Sub-propositions:**
1. **QFI discrimination theorem:** For a given material and disorder level, does QFI from INS data exceed the maximum possible value for a random singlet state? (Testable: INS + QFI analysis on YCu3(OH)6Br3, NaYbSe2, α-RuCl3)
2. **Spin-orbital entanglement benchmark:** Can QFI from RIXS distinguish Kitaev QSL from conventional spin-orbital order in iridate/ruthenate candidates? (Testable: Polarimetric RIXS at Ir L3 / Ru L3 edges)
3. **Finite-temperature QSL formation:** At what temperature does multipartite entanglement emerge, and how does it scale with system parameters? (Testable: QFI-T phase diagram from INS, Sabharwal et al. 2025 framework)
4. **Universal QSL criticality:** Is the XY* universality class (Zhou et al. 2026) universal across all kagome QSL candidates? (Testable: QFI scaling analysis across materials)

**Journal Level:** Nature Physics / Physical Review Letters. Half a century of searching for QSLs with no positive identification — a work that provides the first definitive entanglement witness establishing or excluding QSL in a real material would be a landmark. The QFI framework was only completed in 2025; no experiment has yet applied the full protocol to a candidate material.

**References (Key Reviews Marking It as Open):**
- Willsher, PhD thesis TU Munich (July 2025): "Conclusive experimental observation remains outstanding. Many challenges remain unresolved."
- Ramirez & Syzranov, Materials Advances (Jan 2025): "There is no consensus that QSLs have been conclusively identified in specific materials."
- Matsuda, Shibauchi & Kee, Rev. Mod. Phys. 97, 043003 (2025): "Results and interpretations remain actively debated."
- Sabharwal et al., arXiv:2511.15144 (Nov 2025): "Unambiguous identification still presents many challenges, in both theory and experiment."
- Anderson, Mater. Res. Bull. 8, 153 (1973): Original RVB/QSL proposal
- Lee, Rev. Mod. Phys. 78, 17 (2006): Classic review of RVB and QSL theory
- Balents, Nature 464, 199 (2010): Landmark review "Spin liquids in frustrated magnets"
- Savary & Balents, Rep. Prog. Phys. 80, 016502 (2017): Comprehensive QSL review marking problem as unsolved

**Years covered by reviews:** 1973-2025 (52 years)

---

## LP-Candidate-L4-3: Is Strange Metallicity a Phase of Matter or a Phenomenon Tied to Quantum Critical Points?

**Age:** ~37 years (linear-in-T resistivity in cuprates recognized since ~1989; non-Fermi liquid anomalies reviewed by Varma et al., PRL 1989; "strange metal" term established by 1990s)

**Old Stuck Reason:** Strange metals violate Landau Fermi liquid theory — they exhibit linear-in-T resistivity (ρ ∝ T) down to the lowest temperatures with a "Planckian" scattering rate (τ^-1 ~ k_B T / hbar) independent of material details. But for decades, the ONLY experimental handle was DC transport — which could not distinguish between competing theories: (A) strange metallicity requires proximity to a quantum critical point (QCP), where critical fluctuations destroy quasiparticles; (B) strange metallicity is a distinct phase extending over a finite region of the phase diagram, with spatial randomness as the key ingredient. Transport alone cannot tell you whether "quasiparticle death" is a critical phenomenon or a robust phase property.

**New Tools (2021-2026):**
- **Quantum Fisher Information as entanglement witness** (Fang, Mahankali, Wang, Chen, Hu, Paschen & Si, Nature Communications 16, 2498, March 2025): QFI extracted from inelastic neutron scattering data on heavy fermion strange metals (CeCu5.9Au0.1, Ce3Pd20Si6) reveals at least tripartite entanglement that peaks exactly at the Kondo destruction QCP. This provides the first positive experimental characterization of "quasiparticle death" — the hallmark of strange metallicity. The entanglement is multipartite (pairwise two-tangle vanishes), ruling out simple spin-singlet pictures.
- **Quantum acoustics framework** (Heller et al., arXiv:2511.01853, Nov 2025): 14-author work establishing quantum acoustics as a new nonperturbative tool. Treats the Frohlich electron-phonon model nonperturbatively and derives Planckian transport, polarons, CDWs, and pseudogaps from first principles. Uncovers "Planckian diffusion" as a generalization of Anderson localization to dynamic media. This is a theoretical tool that was technically impossible before 2024 — the required nonperturbative many-body techniques did not exist.
- **High-field transport to ~100T** (Campbell et al., Nature Physics, Nov 2025): Suppression of SC at high fields reveals that low-energy magnetic fluctuations are the primary driver of strange metal transport in cuprates — not phonons and not disorder alone.
- **Spatially random interaction quantum Monte Carlo** (Patel et al., Physical Review X, Sept 2025): Large-scale QMC on models with spatially random antiferromagnetic interactions naturally yields T-linear resistivity with Planckian dissipation over an extended phase (not a point). Shows strange metallicity does not require a quantum critical point — it can be a gapless phase.
- **Strain-tuned ARPES** (Hunter et al., 2025): Direct spectroscopic mapping of non-Fermi liquid quasiparticles in Sr2RuO4, showing quasiparticles acquire anomalous scattering but remain robust through the QCP — settling a 30-year debate about whether quantum-critical systems host quasiparticles at all.

**Core Contradiction:** (A) Strange metals are fundamentally quantum critical — their anomalous transport requires proximity to a QCP where critical bosonic fluctuations destroy Landau quasiparticles (Hertz-Millis-Moriya paradigm, extended by Si/Paschen's Kondo destruction scenario). (B) Strange metals are a distinct gapless phase stabilized by spatial randomness, occupying an extended region of the phase diagram without fine-tuning to a QCP (Patel et al. 2025, PRX). Both pictures now make specific, testable predictions about multipartite entanglement that QFI can measure.

**Sub-propositions:**
1. **Entanglement phase diagram:** Does multipartite entanglement (QFI > bipartite bound) exist only at a QCP, or over an extended region? (Testable: QFI from INS as a function of doping/magnetic field/pressure)
2. **Disorder entanglement test:** Do QFI signatures in spatially random models (Patel et al. 2025) match those in real strange metals? (Testable: QFI computed from QMC + comparison to INS data)
3. **Quantum acoustic predictions:** Can the Heller et al. (2025) prediction of "Planckian diffusion" be tested via ultrasound attenuation in cuprate strange metals? (Testable: resonant ultrasound spectroscopy across the phase diagram)

**Journal Level:** Nature Physics / Physical Review X. The Nature Communications 2025 paper already demonstrated the QFI tool; a comprehensive entanglement-based phase classification of strange metals across multiple material families would resolve a 37-year debate and unify correlated electron physics under entanglement.

**References (Key Reviews Marking It as Open):**
- Sreenivasan & Schumacher, Ann. Rev. Cond. Matt. Phys. 16, 121 (2025): Broader context of unsolved complex systems problems
- DFG/ANR Project 568833081 (2025-2026): "Are strange metals hydrodynamic or quantum critical?" — official framing as open
- Fang et al., Nat. Commun. 16, 2498 (2025): "The strange metal phase... the nature of quasiparticle loss has remained elusive"
- Varma et al., PRL 63, 1996 (1989): Early identification of non-Fermi liquid anomalies
- Stewart, Rev. Mod. Phys. 73, 797 (2001): Review of non-Fermi liquid behavior in f-electron systems
- Keimer et al., Nature 518, 179 (2015): Review of strange metal in cuprates as major open problem

**Years covered by reviews:** 1989-2025 (36 years)

---

## LP-Candidate-L4-4: Does an Ideal Glass Transition Exist, or Is Vitrification Purely Kinetic?

**Age:** ~50 years (Anderson, Science 267, 1615, 1995: "The deepest and most interesting unsolved problem in solid state theory is probably the theory of the nature of glass and the glass transition"; problem recognized since the 1960s-70s)

**Old Stuck Reason:** Atomistic simulations of supercooled liquids could not reach experimentally relevant cooling rates (~1 K/s) or system sizes (~10^6+ atoms) to test whether an "ideal glass transition" exists as a true thermodynamic singularity, or whether vitrification is a purely kinetic (dynamic) phenomenon where the relaxation time diverges only at T=0. Classical MD with empirical potentials at ~10^4 atoms can only quench at ~10^9-10^11 K/s — 10 orders of magnitude too fast. This kinetic limitation meant all simulation-based conclusions were extrapolations over 10+ decades that could not distinguish between competing theories (Adam-Gibbs, RFOT, dynamic facilitation, mode-coupling).

**New Tools (2021-2026):**
- **Universal ML interatomic potentials at million-atom scale** (NEP89, arXiv:2504.21286, April 2025): First universal MLIP covering 89 elements that achieves empirical-potential speed (~3-4 orders of magnitude faster than competing foundation models) while maintaining near-DFT accuracy. Explicitly demonstrated on million-atom metallic glass compression. This closes the length-scale gap.
- **Knowledge-distilled MLIPs** (LightPFP, arXiv:2510.23064, 2025): Distills universal MLIPs into task-specific potentials achieving 1-2 orders of magnitude further speedup. Validated on SiO2 amorphization under shock compression — a canonical glass problem.
- **Equivariant architecture scaling** (AlphaNet, npj Comput. Mater. 11, 332, Nov 2025): New local-frame-based equivariant architecture eliminating the accuracy-efficiency tradeoff, enabling ab initio accuracy at empirical speed for arbitrary compositions.
- **Slow-quench DFT-accuracy B2O3** (J. Chem. Phys. 162, 044503, Jan 2025): First demonstration of DFT-accuracy glass simulation at <=10^11 K/s quenching rates while maintaining large system sizes — simultaneously satisfying the three historically conflicting requirements for glass simulation.
- **ML-derived structural order parameters** (CIG — Confidence Index for Glass, ScienceDirect 2024): Machine learning applied to 2D projections of MD configurations identifies glassy-vs-liquid structures more clearly than traditional measures (volume, potential energy), providing the missing structural fingerprint.
- **Information-theoretic bounds on relaxation** (PNAS/arXiv 2024-2025): New results bounding the configurational entropy and relaxation time divergence from information theory — providing theory-independent constraints on whether a finite-T singularity is allowed.

**Core Contradiction:** (A) RFOT theory (Wolynes, Lubchenko, Biroli, Bouchaud): An ideal glass transition exists at finite temperature T_K as a thermodynamic singularity — an entropy crisis where the configurational entropy vanishes. The laboratory glass transition T_g is a kinetically rounded vestige of this ideal transition. (B) Dynamic facilitation / kinetically constrained models (Chandler, Garrahan): No thermodynamic transition exists; the dramatic slowdown is purely kinetic, emerging from hierarchical dynamical constraints without any underlying static singularity. The relaxation time diverges only at T=0 (Vogel-Fulcher-Tammann is an effective fit, not fundamental). MLIPs now make it possible — via enhanced sampling methods like swap Monte Carlo combined with DFT-accuracy forces — to directly simulate whether configurational entropy extrapolates to zero at finite T, resolving the 50-year debate.

**Sub-propositions:**
1. **Configurational entropy equation of state:** Does the configurational entropy of a model glassformer, computed from MLIP-MD at DFT accuracy, extrapolate linearly to zero at finite T? (Testable: thermodynamic integration with NEP89/LightPFP)
2. **Diverging length scale identification:** Does the ML-derived structural order parameter (CIG-type) show a growing static correlation length that diverges at T_K? (Testable: finite-size scaling of structural features from MLIP simulations at million-atom scale)
3. **Universal relaxation function:** Does the relaxation time τ_α(T) follow a universal functional form across all glassformers, and does information theory bound the possible extrapolations? (Testable: MLIP-MD across multiple compositions + info-theoretic analysis)
4. **Thermodynamic vs. kinetic separation:** Can external fields (shear, pressure) probe configurations near the putative ideal glass state, distinguishing static from dynamic contributions to the slowdown? (Testable: non-equilibrium MLIP-MD with enhanced sampling)

**Journal Level:** Nature Physics / PRL. The question was framed by a Nobel laureate as the deepest unsolved problem. A definitive computational answer — enabled by tools that literally did not exist before 2024 — would be a landmark. Caveat: Some may argue this is infrastructure-limited rather than tool-limited; however, MLIPs are an algorithmic/conceptual breakthrough, not merely "bigger computers." The speedup is 10^3-10^4 fold at comparable accuracy — a qualitative change that makes formerly impossible calculations routine.

**References (Key Reviews Marking It as Open):**
- Pica Ciamarra, Dyre, Lerner & Wyart, arXiv:2603.05209 (March 2026): "The dramatic slowdown of dynamics... remains one of the central unresolved problems in condensed matter physics."
- Nature Reviews Physics (2026): "Three unsolved problems in glass science" — including ideal glass existence
- Anderson, Science 267, 1615 (1995): Canonical framing as "deepest unsolved problem"
- Debenedetti & Stillinger, Nature 410, 259 (2001): "Supercooled liquids and the glass transition" — review marking as unsolved
- Berthier & Biroli, Rev. Mod. Phys. 83, 587 (2011): "Theoretical perspective on the glass transition"
- Roadmap on ML Glassy Dynamics, Nature Reviews Physics (Feb 2025): "The difficulty in sampling equilibrated configurations at low temperatures hampers thorough investigations"

**Years covered by reviews:** 1995-2026 (31 years)

---

## LP-Candidate-L4-5: Can Small-Scale Intermittency in Turbulence Be Derived from First Principles?

**Age:** ~140 years (Reynolds 1883 identified the laminar-turbulent transition; universal small-scale statistics recognized by Kolmogorov 1941; anomalous scaling / intermittency recognized as a problem since the 1960s-70s; Feynman 1964 called turbulence "the most important unsolved problem of classical physics")

**Old Stuck Reason:** The Navier-Stokes equations are known, but the nonlinearity generates an infinite hierarchy of moment equations (the closure problem). Small-scale intermittency — the failure of Kolmogorov's 1941 self-similarity hypothesis — means that velocity gradient statistics deviate systematically from dimensional analysis, with anomalous scaling exponents ζ_n < n/3. These exponents were measured experimentally but could not be derived from Navier-Stokes without uncontrolled approximations. The computational barrier: DNS could access only moderate Reynolds numbers (Re_λ ~ 10^3), far below the asymptotic regime where universality should set in, and the required resolution scales as Re^(9/4) — making asymptotic-Re DNS computationally impossible on foreseeable hardware.

**New Tools (2021-2026):**
- **EddyFormer — 30x speedup for DNS-class accuracy** (NeurIPS 2025, arXiv:2510.24173): Transformer-based spectral-element architecture achieving DNS-level accuracy for 3D isotropic turbulence at 256^3 resolution with 30x speedup. Generalizes to domains 4x larger than training size without retraining. This changes the scaling: if ML-surrogates can substitute DNS at a fraction of the cost, larger effective Re become accessible.
- **AI-discovered analytical subgrid closure** (Jakhar et al., PRL, accepted Dec 2025): Sparse equation discovery combined with fluid physics yields a 4th-order analytical closure (NGM4) that reproduces DNS statistics including extreme events with >0.99 pattern correlation. This is a qualitative advance: the closure is human-interpretable (it is the 4th-order Taylor expansion), not a black-box neural network.
- **Online DNS-embedded RANS training** (oRANS, arXiv Oct 2025): Embeds a DNS subdomain inside a RANS simulation for real-time closure training, eliminating the overfitting to limited precomputed datasets that plagued earlier ML closures.
- **Multi-stepex MoE for long-horizon stability** (Ms-MoE-IFactFormer, arXiv:2604.12794, April 2026): Solves the long-standing problem of instability in autoregressive turbulence prediction at fine temporal resolution.
- **Quantum computing for Navier-Stokes** (emerging ~2023-2025): Quantum algorithms for the nonlinear advection term (Carleman linearization + HHL-type solvers) remain at proof-of-concept stage but represent a genuinely new computational paradigm not available before ~2022.

**Core Contradiction:** (A) Intermittency is a statistical property of Navier-Stokes that can in principle be derived from the equations via renormalization group or instanton methods — the anomalous exponents are universal numbers computable from first principles. (B) Intermittency is not universal but depends on large-scale flow geometry, boundary conditions, and the energy injection mechanism — no set of universal exponents exists, and the apparent scaling is an artifact of finite-Re measurements. The new ML tools enable direct computation at higher effective Re, which can distinguish the two possibilities: universal exponents should converge to Re-independent values, while geometry-dependent scalings should not.

**Sub-propositions:**
1. **Universal exponent convergence:** Do longitudinal and transverse structure function exponents converge to universal values as Re → ∞, as measured by ML-augmented DNS at decade-higher effective Re? (Testable: EddyFormer at 1024^3+ resolution)
2. **Analytical closure validation:** Can the PRL 2025 NGM4 analytical closure reproduce the full hierarchy of anomalous exponents across multiple flow geometries? (Testable: NGM4-LES vs filtered DNS)
3. **Spontaneous stochasticity at Re = ∞:** Do Euler solutions become non-unique in the singular limit, as predicted by the ANR TURBO project (Bec et al. 2025)? (Testable: ML closure or quantum algorithm approaching infinite Re)

**Journal Level:** Journal of Fluid Mechanics / Physical Review Letters. Competing with LP-Candidate-L4-1 through L4-4 for top-tier physics journals; this is more of a fluid dynamics JFM paper. The problem is clearly unsolved, but the path to resolution is less clean than L4-1/L4-2 because: (a) the theoretical framework (Kolmogorov 1941 + multifractal corrections) already provides a phenomenological description — the open question is derivation, not description; (b) the new tools (ML-DNS) accelerate computation but may not resolve the fundamental closure problem; (c) the Clay Millennium Prize problem (Navier-Stokes regularity) is a math problem, not a physics problem.

**Filter Concern:** This candidate partially fails Filter 5 (infrastructure bottleneck) and Filter 4 (decomposability): while ML-DNS provides computational acceleration, the fundamental barrier is analytic intractability of the Navier-Stokes hierarchy, not lack of data. Increasing effective Re by 30x may not answer the foundational question of whether anomalous exponents exist as universal numbers.

**References (Key Reviews Marking It as Open):**
- Buaria & Pumir, J. Fluid Mech. (May 2026): "Turbulence remains notoriously difficult to characterise and predict... a faithful and predictive characterisation of small scales remains elusive"
- Sreenivasan & Schumacher, Ann. Rev. Cond. Matt. Phys. 16, 121 (2025): "What Is the Turbulence Problem, and When May We Regard It as Solved?"
- Sevilla, arXiv:2603.18913 (March 2026): "Turbulence remains one of the central open problems in classical physics"
- Jimenez, arXiv:2506.13417 (June 2025): Otto Laporte lecture: "Most of turbulence cannot yet be described by coherent structures"
- Feynman, 1964: "The most important unsolved problem of classical physics"
- Frisch, "Turbulence: The Legacy of A.N. Kolmogorov" (Cambridge, 1995): Classic monograph

**Years covered by reviews:** 1883-2026 (143 years)

---

## LP-Candidate-L4-6: Does the Dark Matter Small-Scale Crisis Signal New Physics, or Is It Resolved by Baryonic Feedback?

**Age:** ~30 years (core-cusp problem identified ~1994 by Flores & Primack, Moore 1994; "small-scale crisis" term established by ~1999-2000; missing satellites problem recognized since Klypin et al. 1999)

**Old Stuck Reason:** Cosmological N-body simulations of cold dark matter (CDM) predict steep central density cusps (ρ ∝ r^-1), an overabundance of subhalos (missing satellites), and overly dense subhalos (too-big-to-fail). Observations of dwarf galaxies typically show flat cores, fewer satellites, and less dense subhalos. For 30 years, the field could not settle whether these discrepancies signal new dark matter physics (warm DM, self-interacting DM, fuzzy DM, MOND) or are artifacts of incomplete baryonic physics (stellar feedback, supernova-driven outflows) not captured in DM-only simulations. The bottleneck: cosmological simulations with full baryonic physics were too computationally expensive to run at the resolution and sample size needed to make statistically meaningful statements. Furthermore, direct measurements of DM distributions in the faintest dwarfs — the cleanest testbeds where baryonic effects should be minimal — were limited by telescope sensitivity.

**New Tools (2021-2026):**
- **JWST resolving wide binaries in ultra-faint dwarfs** (Shariat et al., arXiv:2509.04555, 2025): First robust detection of wide binaries in an external galaxy (Bootes I UFD) using JWST/NIRCam. The binary separation distribution truncates at ~16,000 AU — consistent with Milky Way field binaries — and directly constrains the DM density profile and PBH abundance. This is a genuinely new observational lever impossible before JWST's resolution and sensitivity.
- **JWST + HST resolving individual stars in UFDs** (Sanchez Almeida et al., ApJL 2024): Stellar density profiles of 6 UFD satellites mapped to unprecedented precision, showing cored stellar profiles that naturally map to cored DM profiles.
- **DESI Milky Way Survey** (Yang et al., ApJ 2025): New kinematic data for Draco, Sextans, Ursa Minor revealing diverse inner DM profiles — not uniformly cuspy or cored — and failing to reproduce earlier claims of clean anti-correlations supporting baryonic feedback.
- **FIRE-3 simulations with black holes + cosmic rays** (Koudmani et al., MNRAS 2024-2025): First cosmological zoom-in simulations of dwarfs including AGN feedback and cosmic rays, showing DM profile diversity matching observations within ΛCDM + full baryonic physics.
- **Self-interacting DM constraints converging** (Zhang et al., Nature 2025): Independent constraint σ/m ≈ 0.3 cm^2/g from dwarf galaxy clustering; two-component SIDM simultaneously addresses core-cusp, strong-lensing anomalies, and "little dark dots."
- **LZ/XENONnT null results entering "neutrino fog"** (Dec 2025-May 2026): Direct detection of WIMPs now excluded for cross-sections down to the irreducible neutrino background, fundamentally changing the landscape of the dark matter problem.

**Core Contradiction:** (A) The small-scale "crisis" is resolved by baryonic feedback (stellar winds, supernovae, AGN, cosmic rays) within standard ΛCDM — the apparent discrepancies are artifacts of comparing DM-only simulations to real galaxies. FIRE-3 simulations with full baryonic physics reproduce the observed diversity. (B) Persistent discrepancies in ultra-faint dwarfs — where stellar mass is too low for baryonic feedback to reshape DM halos — signal genuine failure of collisionless CDM and require new physics (SIDM, warm DM, fuzzy DM, or modified gravity). The new data from JWST (wide binaries, resolved stellar populations) and DESI (kinematics) can now test this directly because UFDs are the regime where the two hypotheses make maximally different predictions.

**Sub-propositions:**
1. **Wide binary test of DM profile:** Do the separation distributions of wide binaries in multiple UFDs favor cuspy (CDM) or cored (SIDM/WDM) DM profiles? (Testable: JWST Cycle 3/4 programs targeting additional UFDs)
2. **Feedback-free zone:** Is there a minimum stellar mass below which baryonic feedback cannot flatten a DM cusp, and do observed UFDs below this threshold show cusps or cores? (Testable: FIRE-3-type simulations + JWST-resolved UFD profiles)
3. **SIDM convergence test:** Does the independent σ/m ≈ 0.3 cm^2/g from dwarf clustering (Zhang 2025) agree with core-collapse SIDM predictions for cluster strong-lensing and high-redshift "little red dots"? (Testable: joint SIDM fit to all scales)

**Journal Level:** Nature Astronomy / Physical Review Letters. This is a major question but the filter concerns are significant: (a) The "new tools" (JWST, DESI) are primarily observational infrastructure — more and better data, not a qualitatively new methodology; (b) The problem may already be largely resolved in favor of baryonic feedback (Di Cintio 2024: "So far NO sign at all of ΛCDM failing at small scales"); (c) The direct detection program has hit the neutrino fog — suggesting the DM particle identity question needs a new experimental paradigm (quantum sensors, paleo-detectors, axion haloscopes) that is still in development.

**Filter Concerns:** This candidate partially fails Filters 5 (significant infrastructure component — JWST, Rubin, Euclid are telescope infrastructure) and 2 (the issue may be insufficient data volume/statistics rather than absence of conceptual tools). The JWST wide binary result (Shariat 2025) is genuinely novel, but it constrains PBH/MACHO DM more cleanly than it discriminates cusp vs. core.

**References (Key Reviews Marking It as Open):**
- Communications Physics 9, 105 (2026): "Dark matter constitutes ~85% of the universe's total mass, yet its nature remains a mystery"
- Bramante, arXiv:2602.23708 (Feb 2026): "The nature of dark matter remains a mystery"
- Vegetti & White et al., Nature Astronomy (2025): "Dark matter makes up 85% of cosmic matter, but its nature is still unknown"
- Natarajan et al., ApJL (May 2026): CDM anomalies in cluster cores require new physics
- Navarro, Frenk & White, ApJ 490, 493 (1997): NFW profile — origin of cusp prediction
- Bullock & Boylan-Kolchin, ARAA 55, 343 (2017): "Small-scale challenges to the ΛCDM paradigm"
- Di Cintio, UNDARK 2024 presentation: Assessment that no sign of ΛCDM failure exists

**Years covered by reviews:** 1994-2026 (32 years)

---

## Consolidated Filtering Rationale

### Top Tier (6/6 filters passed):

**L4-1: Pseudogap-SC Competition** — The strongest candidate. Every filter is cleanly satisfied. The 40-year problem has been stuck specifically because no tool could observe real-time causal dynamics; time-resolved ARPES (2025) now provides exactly that. The contradiction (promote vs. suppress) is sharply defined, experimentally testable, and probing it requires the new tool. Resolution would change the consensus in cuprate superconductivity, quantum materials, and computational physics (the Hubbard model debate).

**L4-2: QSL Positive Identification via QFI** — Equally strong on paper, with the longest review span (53 years). The tool gap was conceptual as much as experimental: QSLs had no positive definition. QFI provides one for the first time (2024-2025), mapping entanglement depth as a function of temperature and disorder. The core contradiction (intrinsic QSL vs. disorder singlet) is the central debate in the field. Experimentally realistic protocols (INS + QFI) exist and await application to candidate materials.

**L4-3: Strange Metal Phase vs. QCP** — Strong on all filters. The 37-year puzzle of T-linear resistivity and Planckian dissipation now has a positive experimental probe (QFI entanglement witness) and a new theoretical framework (quantum acoustics) — both from 2025. The sub-propositions are somewhat harder to experimentally decompose than L4-1/L4-2 because QFI from INS requires large single crystals of strange metal compositions, which are often hard to grow. Still a fully qualifying L4 candidate.

### Mid Tier (5/6 filters passed):

**L4-4: Ideal Glass Transition Existence** — Passes all criteria cleanly except a partial concern on Filter 5 (infrastructure). MLIPs represent a genuine algorithmic/conceptual breakthrough (10^3-10^4x speedup at DFT accuracy), not merely "bigger computers." However, the computational demands to reach true laboratory cooling rates (~1 K/s) remain enormous even with MLIP acceleration, and some may argue the fundamental barrier is simulation time, not tool absence. The case is strengthened by the existence of complementary new theoretical tools (information-theoretic bounds on relaxation).

### Lower Tier (3-4/6 filters passed):

**L4-5: Turbulence Intermittency** — The problem is unquestionably old and unsolved (140 years). However, it partially fails Filter 2 (stuck reason is mathematical intractability, not insufficient tools — we know the NS equations) and Filter 5 (resolving it requires analytic breakthroughs more than new measurement/computation tools). ML-accelerated DNS is promising but may not answer the foundational question of whether anomalous exponents are universal numbers derivable from first principles.

**L4-6: Dark Matter Small-Scale Crisis** — While clearly a 30+ year problem with multiple reviews marking it as unsolved, the candidate suffers from: (a) the "new tools" (JWST, DESI) are primarily infrastructure — more and better data from expensive telescopes; (b) the baryonic feedback resolution (FIRE-3 with AGN+CR) may already be settling the question in favor of ΛCDM; (c) the next-generation direct detection program faces the neutrino fog — a pure infrastructure bottleneck.

---

## Recommended Priority for Next Steps

1. **L4-1 (Pseudogap-SC)** — Move to Strategy L5 (expert validation). The sharpest question with the most direct tool-problem fit.
2. **L4-2 (QSL via QFI)** — Move to Strategy L5 in parallel. Slightly more theoretical than L4-1 but equally clean.
3. **L4-3 (Strange Metal)** — Prepare for L5 but identify specific material targets where QFI experiments are feasible.
4. **L4-4 (Glass)** — Hold for L5 if L4-1/L4-2 show weaknesses; strong candidate but infrastructure concern needs addressing.
5. **L4-5/L4-6** — Deprioritize relative to top tier; use as backup candidates.
