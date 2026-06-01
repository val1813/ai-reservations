## AB Validation: Pseudogap-SC Competition in Cuprates

---

### A-Doctor: Formal Attack

#### Step 0 — Concept Check

| Concept | Candidate Definition | Verdict | Notes |
|---|---|---|---|
| **Pseudogap (PG)** | Partial suppression of electronic density of states near EF below T* (T* > Tc) | **Correct** | Standard definition; T* is a crossover, not a phase transition. |
| **Preformed pairs** | Cooper pairs existing above Tc without long-range phase coherence | **Correct** | Supported by Nernst effect, diamagnetism above Tc, and autocorrelated ARPES JDOS (Shah/Zhao/Chatterjee, APS SES Oct 2025). |
| **Competing order** | Distinct electronic order (CDW, PDW, stripe) that fights SC for spectral weight | **Correct** | Well-established: CDW observed via RIXS in underdoped cuprates; stripe order in La-based systems. |
| **Time-resolved ARPES (tr-ARPES)** | Pump-probe ARPES with femtosecond time resolution to track electronic structure dynamics | **Correct** | The Armanno/Boschini group at INRS has published tr-ARPES on Bi2212 (arXiv:2505.03900, May 2025; arXiv:2511.20768, Nov 2025). |

**Step 0 Score: 3/3** — All concepts correctly defined.

---

#### Core Contradiction Attack

**Score: 1/3** — Significant framing problems identified.

**Attack 1: False Dichotomy.** The candidate frames the question as a binary: "Proposition A (PG promotes SC) vs Proposition B (PG competes with SC)." But the 2025-2026 literature demonstrates this is a false choice. The PG is not a monolithic phenomenon — it has multiple components (spin, charge, pairing) that may behave differently:

- **Lee & Haase (arXiv:2604.19215, Apr 2026):** NMR shift decomposition across dozens of cuprates reveals TWO independent spin components ("A-spin" and "B-spin") in the pseudogap. Optimal Tc arises from a special MATCH between these two components. This is neither "promotes" nor "competes" — it is a more complex coupling.

- **Markiewicz/Matzelle/Bansil (arXiv:2509.13543, Sep 2025):** Proposes the PG is a textured short-range AFM with charged domain walls. The three CDW branches are topological textures. This "intertwined orders" framework dissolves the competition vs. precursor binary — both are aspects of the same underlying texture.

- **Shimizu/Toda et al. (arXiv:2510.10906, Oct 2025, updated Mar 2026):** Finds micrometer-scale spatial correlation between SC and PG threshold fluences — the PG is intrinsically inhomogeneous but locally correlated with SC. This supports NEITHER pure competition NOR pure precursor — it suggests spatial coexistence with local coupling.

**Attack 2: The "Same Degrees of Freedom" Argument is Oversimplified.** The candidate argues that "the same electronic degrees of freedom near the antinode cannot simultaneously promote AND suppress superconductivity." This ignores momentum-space differentiation:
- The PG at the **antinode** (near (pi,0)) may compete with SC (gap opening at EF reduces density of states available for pairing).
- The PG near the **node** may be a precursor (pairing fluctuations without phase coherence).
- A single phenomenon can have both effects in different k-space regions. The tr-ARPES data itself is momentum-resolved and may show different behavior at different Fermi surface locations.

**Attack 3: Ignored Alternative — PG as Orthogonal Order.** The Meng/Wang et al. high-pressure study (arXiv:2604.10207, Apr 2026) shows that under 37 GPa, T* rises monotonically while Delta_PG is continuously SUPPRESSED, and Tc/DELTA_SC trace a correlated dome EVOLVING INDEPENDENTLY of the PG. If PG and SC were truly competing (trading spectral weight in a zero-sum game), they should anti-correlate under pressure. Instead, they DECOUPLE — challenging both the competition AND precursor views. The PG may simply be an orthogonal instability of the doped Mott insulator that shares some degrees of freedom with SC but does not directly control it.

**Attack 4: The "Why Cannot Both Be True" Argument Fails Under Doping Evolution.** The PG evolves continuously with doping — from a large gap at very low doping (where it is essentially the Mott gap) to zero at optimal doping. At very low doping, the PG IS the Mott gap and SC is impossible (no carriers). At intermediate doping, the PG may preform pairs that condense at Tc (precursor). Near optimal doping, residual PG correlations may compete with SC for the remaining spectral weight. The candidate's binary framing ignores this doping evolution.

---

#### S1 [Time-Domain PG-SC Dynamics] — Attack

**Score: 1/3**

**Factual Issue with Citation.** The candidate describes "Armanno/Boschini et al. (Nov 2025)" as observing "spectral weight transfers from PG to SC on femtosecond timescales" and frames this as "the first DIRECT dynamical observation of competition." The actual Nov 2025 paper (arXiv:2511.20768, "Light-induced Asymmetric Pseudogap below Tc") does show that when SC is fully restored after pump excitation, the PG is suppressed. However:

1. **The May 2025 paper by the same group (arXiv:2505.03900) is about phase fluctuations**, not spectral weight transfer between PG and SC. The candidate conflates or selectively cites from the group's output.

2. **The Nov 2025 paper studies OPTIMALLY-DOPED Bi2212.** At optimal doping, the PG is weakest or nearly absent in equilibrium. Observing PG suppression when SC is restored at optimal doping is expected under BOTH competition and precursor models: in the precursor model, PG spectral weight should ALSO decrease as it condenses into SC. The key test is in UNDERDOPED samples where PG is strong — the paper does not report these data.

3. **Shah/Zhao/Chatterjee (APS SES, Oct 2025) find the OPPOSITE** from autocorrelated ARPES on underdoped Bi2212: JDOS peak dispersions show particle-hole symmetry that persists across Tc, directly supporting the preformed pairing (precursor) interpretation.

4. **Bayesian evidence ratio is premature.** A proper Bayesian model comparison would require: (a) defining likelihood functions for both models given tr-ARPES data, (b) computing marginal likelihoods integrating over model parameters, (c) accounting for systematic errors in pump-probe experiments (heating, fluence dependence, non-thermal distributions). The candidate proposes computing a Bayesian evidence ratio with no discussion of how to define the likelihood or what priors to use. This is a non-trivial statistical challenge given the model complexity.

**Verdict:** The tr-ARPES data are genuinely important but do not "definitively establish competition." Both precursor and competition models can explain the same data under reasonable parameter choices. The sub-proposition overstates the conclusiveness of a single experiment.

---

#### S2 [QFI Entanglement Diagnostic] — Attack

**Score: 0/3** — Contains a critical factual error.

**Factual Error: Fang et al. (2025) did NOT study cuprates.** Fang et al., "Amplified multipartite entanglement witnessed in a quantum critical metal," Nature Communications 16, 2498 (March 2025), studies heavy fermion metals (Kondo lattice systems) near a Kondo destruction QCP — NOT cuprate superconductors. The QFI peaks at the Kondo destruction QCP in heavy fermions, which is a different physical system with different physics. This is a Category 1 citation error: wrong system attributed to the cited work.

**The correct cuprate QFI reference is:** Bippus, Krsnik, Kitatani et al., "Entanglement in the pseudogap regime of cuprate superconductors," Physical Review B 112, L081110 (August 2025), arXiv:2503.12463. Their key findings:

- QFI/Quantum Variance computed from AFM susceptibility of the 2D Hubbard model (dynamical vertex approximation, DGammaA).
- Entanglement enhanced in PG regime; ln(1/T) divergence cut off by Tc onset.
- At T=52K, at least 3-partite entanglement within PG regime.
- Qualitative agreement with neutron scattering for Hg1201, LSCO, YBCO.

**Does Bippus et al. distinguish competition from precursor?** The candidate claims the QFI gives "DIFFERENT QFI temperature-doping maps" for the two scenarios. This is unsubstantiated speculation:
- Bippus et al. do NOT compute QFI maps for the two competing scenarios. They compute QFI for the Hubbard model (which produces BOTH PG and SC) and compare to experiment.
- The ln(1/T) divergence cut off by Tc is consistent with BOTH interpretations: in competition, SC suppresses the PG (and its associated entanglement); in precursor, PG entanglement condenses into SC coherence (and the QFI of the superconducting state is lower because pairs are now phase-coherent).
- The candidate's claim that the two scenarios produce "DIFFERENT QFI temperature-doping maps" is an unsupported assertion — no such calculation exists in the literature.

**Additional concern:** The QFI is an INTEGRATED measure over all frequencies and momenta. It cannot resolve whether entanglement at different energy scales comes from PG fluctuations or SC fluctuations — this is the same ambiguity that plagues all PG-SC studies. Using QFI as a "diagnostic" without demonstrating that it can actually discriminate between the two scenarios is circular.

**Verdict:** This sub-proposition is built on a misattributed reference and makes unsupported claims about what QFI can discriminate. The core idea (using entanglement measures to probe PG-SC relationship) is interesting but the execution as stated is invalid.

---

#### S3 [Hubbard Model at Realistic Parameters] — Attack

**Score: 1/3** — Feasibility overestimated.

**Attack 1: Time-resolved spectra are computationally prohibitive.** The candidate proposes computing "time-resolved ARPES spectra" using DMRG on 6x6 clusters (36 sites). Standard DMRG computes GROUND STATE and low-lying eigenstates. Time-resolved ARPES requires:
- Real-time evolution of the many-body wavefunction after a pump pulse (simulating the laser excitation).
- Computing the time-dependent single-particle Green's function G(k, t, t') with femtosecond resolution.
- This requires time-dependent DMRG (tDMRG) which has well-known exponential growth of entanglement entropy with time — the "entanglement barrier." For a 6x6 2D Hubbard model at U/t=8, the entanglement entropy after even ~5-10 hopping times (sufficient for tr-ARPES dynamics) would require bond dimensions far beyond current computational capabilities.

**Attack 2: 6x6 may be too small to resolve PG physics.** The PG in cuprates is associated with a T* line that is ~100-300K (10-25 meV). On a 6x6 cluster, the finite-size gap between discrete momentum points is ~2pi* t / 6 ~ t ~ 400 meV (with t ~ 400 meV for cuprates), which is MUCH larger than the PG energy scale. The PG features will be broadened beyond recognition by finite-size effects. DMRG on 6x6 clusters at U/t=8 can reliably compute ground-state properties (spin correlations, pairing correlations), but resolving fine spectral features at the meV scale requires much larger clusters (at least 12x12) or embedding methods.

**Attack 3: The question is ill-posed for the Hubbard model.** The Hubbard model with only on-site U and nearest-neighbor t does not contain the structural complexity (multiple CuO2 layers, apical oxygens, disorder, electron-phonon coupling) of real cuprates. If the Hubbard model reproduces tr-ARPES spectra supporting competition, that tells us the Hubbard model physics favors competition — but does not resolve whether real cuprates, with additional ingredients, work the same way. If it does NOT reproduce the spectra, the candidate's framing ("what ingredient is missing?") opens an infinite regress — there are dozens of candidate missing ingredients (long-range Coulomb, electron-phonon, disorder, interlayer coupling, oxygen degrees of freedom...).

**Verdict:** Ground-state DMRG on 6x6 clusters is feasible and valuable for equilibrium properties, but time-resolved spectral functions are computationally out of reach. The sub-proposition needs dramatic rescoping (e.g., compute equilibrium spectral functions and compare to equilibrium ARPES, or use cluster perturbation theory instead of full time evolution).

---

#### S4 [Universality Across Cuprate Families] — Attack

**Score: 2/3** — Strongest sub-proposition with minor concerns.

**Strengths:**
- This is a genuinely valuable question regardless of whether PG competes or is a precursor. Systematically comparing PG-SC relationship across families is important descriptive science.
- Published ARPES and RIXS data exist for all major families: La-based (LSCO, LBCO), Y-based (YBCO), Bi-based (Bi2201, Bi2212, Bi2223), Hg-based (Hg1201, Hg1212, Hg1223).
- The candidate correctly notes that if the relationship is universal, this is strong evidence for a single mechanism (competition OR precursor); if family-dependent, the phase diagram is more complex. Both outcomes are interesting.

**Attacks:**
1. **Doping control is not uniform across families.** La-based cuprates can be doped across the full phase diagram (0-0.3 holes/Cu). Hg-based cuprates are hard to dope below p~0.08. Bi-based cuprates have intrinsic disorder from Bi/Sr substitution. Comparing "the same doping" across families is not straightforward — chemical pressure, disorder, and structural differences affect Tc and T* independently of intrinsic PG-SC physics.

2. **The sub-proposition is descriptive, not mechanistic.** Even if we find that PG and SC anti-correlate universally, that does not tell us WHY — is it competition for spectral weight, or is there a third variable (e.g., the Mott gap) that controls both? The universal anti-correlation of Tc and T* across families is already known (Tallon & Loram, Physica C 2001) — what new information does this add?

3. **Feasibility concern with Hg-based cuprates:** Hg-1201 is the "cleanest" cuprate structurally but is chemically unstable in air and requires specialized synthesis. Published ARPES data on Hg-based cuprates is sparse compared to Bi-based systems.

**Verdict:** This is a solid descriptive project suitable for a review or meta-analysis (PRB/Physical Review X, not Nature Physics/PRL as claimed). It is feasible with published data but needs sharper mechanistic hypotheses to rise to the claimed journal tier.

---

### B-Doctor: Cross-Domain Attack

#### Cross-Domain 1: Pseudogap <-> Ultracold Atoms (Fermi-Hubbard Quantum Simulation)

**Score: 2/3** — Strong connection, partially explored.

**What optical lattice experiments can contribute:**

The Harvard (Greiner) and Munich (Bloch) groups have achieved breakthroughs in 2025-2026 that are directly relevant:

1. **Greiner group (Kendrick/Xu et al., Nature 642, 909-915, 2025):** First direct observation of the pseudogap metal phase in a 2D Fermi-Hubbard quantum simulator. A novel spectroscopic technique resolved partial gap opening correlated with a thermodynamic anomaly. The data hints at a link between PG and charge order — directly relevant to the competition vs. precursor question. Charge order is a competing instability, so if PG is linked to charge order in the Hubbard simulator, that supports the competition view.

2. **Bloch group (Chalopin et al., PNAS 123, e2525539123, 2026):** Direct observation of magnetic polarons, magnetically-mediated hole pairing, and incipient stripe formation at the onset of the pseudogap phase. Stripes are a competing order — again supporting competition.

3. **Key advantage over cuprate experiments:** In optical lattices, one can measure spin and charge correlations with SINGLE-SITE RESOLUTION (quantum gas microscopy). This means one can directly image whether PG correlations and SC correlations occupy the same or different spatial regions — something impossible in cuprates where you get k-space averages. If PG and SC anticorrelate spatially at the single-site level, that is definitive evidence for competition. If they correlate, that is evidence for precursor.

4. **Universal magnetic energy scale (arXiv:2604.15234, Apr 2026):** A single energy scale J* governs both static and dynamic magnetic correlations and sets T* via kBT* = cJ*. This provides a theoretical framework for understanding what controls PG strength — if J* also controls Tc, it suggests common origin (precursor); if Tc and J* are independent, supports competition.

**Limitation:** Optical lattice temperatures (T/t ~ 0.05 in the cryogenic regime) still correspond to O(100-200K) for cuprate-relevant t ~ 400 meV. This is ABOVE Tc for most cuprates, meaning optical lattice experiments can access the PG regime but NOT the SC regime yet. The competition vs. precursor question requires observing what happens when SC turns on — which requires even lower temperatures.

**Specific test the candidate missed:** Measure the single-particle spectral function A(k,omega) via momentum-resolved RF spectroscopy in the Hubbard simulator at the same doping/temperature where tr-ARPES on cuprates is performed. Directly compare the PG spectral features. If the Hubbard model PG matches cuprate PG, AND the Hubbard model shows competition, that closes the loop.

---

#### Cross-Domain 2: Pseudogap <-> Particle Physics (Chiral Symmetry Breaking in QCD)

**Score: 1/3** — Analogy is suggestive but stretched.

**The analogy:** In QCD with Nf=2 massless quarks, chiral symmetry is spontaneously broken below T_c ~ 155 MeV — the chiral condensate <psibar psi> forms, producing constituent quark masses ~300 MeV (a "gap") but without color superconductivity (which requires much higher density). Above T_c, chiral symmetry is restored. The "gap without superconductivity" in QCD is analogous to the PG as a "gap without phase coherence."

**Where the analogy works:**
- Both are spectral gaps that open at a temperature/doping above the SC transition.
- Both involve preformed pairs in some sense: the chiral condensate is a <psibar psi> pair condensate in the scalar channel (0+), while SC pairing is in the vector channel (1-).
- Both have been studied with spectral functions (lattice QCD computes quark spectral functions; ARPES measures electron spectral functions).

**Where the analogy fails:**
1. **Chiral symmetry breaking is a true thermodynamic phase transition (in the chiral limit)** — with an order parameter (<psibar psi>), universality class (O(4)), and critical exponents. The PG in cuprates is a CROSSOVER — there is no order parameter, no diverging correlation length, no universality class. This is a fundamental disanalogy. The candidate's phrase "analogous 'gap without order' phenomenon" is misleading — the PG lacks an order parameter because it IS NOT a phase transition, not because the order parameter is exotic.

2. **The QCD "gap" is in the particle spectrum (constituent quark mass), not at the Fermi level.** In cuprates, the PG is a suppression of spectral weight at EF — it directly affects transport. In QCD, chiral symmetry breaking produces hadron masses ~1 GeV while the quark Fermi surface (relevant for color superconductivity) exists only at baryon chemical potential >~1 GeV, a completely different regime. The analogy conflates two different kinds of "gap."

3. **Can QCD methods help?** Lattice QCD has developed sophisticated spectral function reconstruction (Maximum Entropy Method, Bayesian reconstruction, Backus-Gilbert) to extract real-frequency spectral functions from imaginary-time data. These methods could potentially be applied to quantum Monte Carlo data for the Hubbard model to extract A(k,omega). But this is a technical transfer of spectral reconstruction methods, not a conceptual insight about competition vs. precursor.

**Verdict:** The analogy is evocative for a general audience but does not provide discriminating power for the competition vs. precursor question. The structural differences (phase transition vs. crossover, gap location in energy, fermiology) limit its usefulness.

---

#### Cross-Domain 3: Pseudogap <-> Information Theory

**Score: 2/3** — Novel and potentially powerful, but needs operationalization.

**The idea:** Compute mutual information I(ARPES; RIXS) = H(ARPES) + H(RIXS) - H(ARPES, RIXS) between ARPES spectral function A(k,omega) and RIXS intensity I(q,omega). Under the competition hypothesis, PG and SC compete for spectral weight, so knowing the ARPES PG gap depth should reduce uncertainty about the RIXS charge order intensity (high mutual information). Under the precursor hypothesis, PG and SC are the same pairs in different phase-coherence states, so mutual information should be high between ARPES pairing gap and RIXS pair-breaking peak, but LOW between ARPES PG and RIXS charge order.

**Strengths:**
- This is genuinely cross-domain — applying information-theoretic measures to spectroscopy is not standard in condensed matter physics.
- Mutual information is model-free: it does not require assuming a particular Hamiltonian, just joint probability distributions of spectral intensities.
- Could discriminate between scenarios: competition predicts MI(ARPES_PG, RIXS_charge_order) > MI(ARPES_PG, RIXS_pair_excitation); precursor predicts the opposite inequality.

**Attacks:**
1. **Estimating mutual information from experimental data is non-trivial.** ARPES and RIXS are typically measured on different samples, under different conditions, with different resolutions. Computing a reliable joint distribution requires simultaneous or near-simultaneous measurements on the same sample — which is experimentally challenging (though not impossible; some beamlines offer both).

2. **Systematic errors dominate.** ARPES intensity is affected by matrix elements, final-state effects, and surface sensitivity. RIXS intensity depends on incident photon energy, polarization, and intermediate-state resonances. The apparent mutual information may reflect shared experimental artifacts rather than intrinsic physics.

3. **The candidate does not define the random variables.** What exactly are we computing mutual information between? The PG gap value at a specific k-point? The integrated spectral weight over the antinodal region? The full 2D maps? The choice of coarse-graining will affect the result. Without specifying the random variables, the sub-proposition is not testable.

4. **Alternative that the candidate missed:** Use transfer entropy (a directional, time-resolved version of mutual information) between tr-ARPES and time-resolved RIXS. This would capture not just correlation but CAUSAL influence — does perturbing the PG (via pump) cause the SC gap to change (competition) or does the PG signal simply convert into SC signal without causal influence (precursor)?

**Verdict:** The mutual information approach is creative and worth developing as a methodology paper, but as stated it lacks operationalization. The transfer entropy variant (time-resolved) would be more powerful for the competition vs. precursor question.

---

### Additional Fact-Checking Findings

1. **Fang et al. misattribution (CRITICAL):** As detailed under S2, Fang et al. (Nature Comms, March 2025) studied heavy fermion metals, not cuprates. The correct cuprate QFI reference is Bippus et al. (PRB 112, L081110, August 2025). This is a Category 1 citation error.

2. **Armanno/Boschini paper content (MODERATE):** The candidate describes the Nov 2025 paper as "the first DIRECT dynamical observation of competition." While the paper does show PG suppression when SC recovers, it studies optimally-doped Bi2212 (where PG is weakest), and the same group's May 2025 paper emphasizes phase fluctuations, not PG-SC spectral weight transfer. The candidate overstates the conclusiveness.

3. **Missing key 2025-2026 papers (MODERATE):**
   - Meng/Wang (arXiv:2604.10207, Apr 2026): High-pressure decoupling of PG and SC — if PG and SC truly compete, they should anticorrelate under pressure. Instead they decouple. This directly challenges the competition framing.
   - Lee/Haase (arXiv:2604.19215, Apr 2026): Two-component NMR — PG arises from coupling between A-spin and B-spin components, not from competition OR precursor dynamics.
   - Shah/Zhao/Chatterjee (APS SES, Oct 2025): Autocorrelated ARPES supporting preformed pairing.

4. **Journal target optimism:** Nature Physics / PRL requires either (a) a decisive experiment, (b) a theoretical breakthrough resolving a long-standing problem, or (c) a surprising discovery. A meta-analysis/statistical re-evaluation of published data, even with Bayesian methods, is more likely a PRB/PRX paper. The candidate's framing as "new data reanalysis resolves 40-year debate" is the right ambition but the actual content (S1-S4) does not deliver a resolution — it proposes investigating whether a resolution is possible.

---

### Summary & Recommendation

| Dimension | Score | Notes |
|---|---|---|
| **Concept Check (Step 0)** | 3/3 | All concepts correctly defined. |
| **Core Contradiction** | 1/3 | False dichotomy; ignored multi-component PG evidence; pressure decoupling data challenges both A and B. |
| **S1: Time-Domain Dynamics** | 1/3 | Overstates conclusiveness of single experiment; misses contradictory autocorrelated ARPES data; Bayesian evidence ratio is premature. |
| **S2: QFI Diagnostic** | 0/3 | CRITICAL: Fang et al. studied heavy fermions, not cuprates. Correct reference is Bippus et al. (PRB 2025). Unsupported claims about QFI discrimination. |
| **S3: Hubbard Model** | 1/3 | Time-resolved spectra on 6x6 computationally infeasible; finite-size effects too large for PG physics. |
| **S4: Universality** | 2/3 | Solid descriptive project but needs mechanistic sharpening for target journal tier. |
| **B1: Ultracold Atoms** | 2/3 | Strong connection; optical lattice experiments are entering PG regime and can provide single-site resolution impossible in cuprates. |
| **B2: Particle Physics** | 1/3 | Analogy evocative but structurally flawed (phase transition vs. crossover); limited discriminating power. |
| **B3: Information Theory** | 2/3 | Creative and potentially powerful; transfer entropy variant more discriminating; needs operationalization. |
| **Citation Accuracy** | CRITICAL BUG | Fang et al. misattribution invalidates S2 as stated. |

**Core Score (A-Doctor): 6/18 = 1.0/3 average**
**Core Score (B-Doctor): 5/9 = 1.7/3 average**
**Overall: FIX — Resubmit with major revisions**

**Recommendation: FIX (not KILL, not PASS).** The central question — does the pseudogap promote or suppress superconductivity in cuprates? — is genuinely one of the most important unresolved problems in condensed matter physics. The arrival of tr-ARPES (Armanno/Boschini), quantum gas microscopy of PG in optical lattices (Greiner/Bloch), and QFI entanglement measures (Bippus et al.) does make this newly attackable. The candidate correctly identifies the timeliness.

However, the candidate has three fixable problems and one that requires fundamental reframing:

**Fixable:**
1. **Correct the Fang et al. citation (Critical):** Replace with Bippus et al. (PRB 2025) for cuprate QFI. If using Fang et al., correctly state it is heavy fermions and use it as a methodological cross-reference (QFI methodology), not as cuprate data.
2. **Incorporate the key missing 2025-2026 papers:** Meng/Wang pressure decoupling (arXiv:2604.10207), Lee/Haase two-component NMR (arXiv:2604.19215), Shah/Zhao/Chatterjee autocorrelated ARPES, Shimizu/Toda spatial correlation.
3. **Rescope S3:** Change from time-resolved spectra to equilibrium spectral functions (ground-state DMRG + cluster perturbation theory for A(k,omega)) and compare to equilibrium ARPES — this is feasible and still valuable.

**Requires fundamental reframing:**
4. **Abandon the binary A vs. B framing.** The 2025-2026 evidence strongly suggests the PG is multi-component, doping-dependent, and cannot be reduced to "competition" or "precursor" as a global statement. Reframe as: "Under what conditions (doping, temperature, momentum, cuprate family) does the PG promote vs. suppress SC?" This is a richer, more answerable question, and the sub-propositions S1-S4 can all contribute to answering it. The Bayesian framework (S1) becomes more natural under this reframing: model selection among multi-component models, not binary hypothesis testing.

**Revised journal target:** PRX (extensive multi-method study) or PRB (if scoped to one sub-proposition). Nature Physics only if the tr-ARPES reanalysis (S1) produces a genuinely surprising result that overturns the community consensus — which is possible but should not be assumed.

---

*AB Validation conducted 2026-06-01. Searches: pseudogap competition 2025-2026, tr-ARPES cuprate pseudogap 2025, QFI cuprate entanglement 2025, Armanno/Boschini tr-ARPES 2025, Fang QFI Nature Comms 2025, ultracold atoms Fermi-Hubbard pseudogap 2025-2026. Key sources: arXiv:2511.20768, arXiv:2505.03900, Bippus et al. PRB 112 L081110 (2025), Fang et al. Nat. Comms. 16 2498 (2025), Meng/Wang arXiv:2604.10207, Lee/Haase arXiv:2604.19215, Kendrick/Xu et al. Nature 642 909-915 (2025), Chalopin et al. PNAS 123 e2525539123 (2026), Shimizu/Toda arXiv:2510.10906, Shah/Zhao/Chatterjee APS SES Oct 2025.*
