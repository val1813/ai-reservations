## AB Validation: Hubble Tension — Is ΛCDM Incomplete or Are Local Measurements Systematically Biased?

**Date:** 2026-06-01
**Validator:** A-Doctor + B-Doctor dual-attack
**Sources:** 16 web searches spanning H0DN, SH0ES, Planck, DESI, CCHP, TDCOSMO, EDE, Bayesian evidence, quantum Fisher information, tension metrics

---

### A-Doctor (Formal Attack)

#### Step 0 — Concept Check

| Term | Candidate Claim | Verified Claim | Verdict |
|------|----------------|----------------|---------|
| **H0DN 2026 H0** | 73.50 +/- 0.81 km/s/Mpc | Confirmed: H0DN/Casertano et al., A&A 708, A166 (April 2026). Baseline 73.50 +/- 0.81. All-indicator 73.22 +/- 0.68. | PASS |
| **Planck H0** | 67.27 +/- 0.46 (Planck 2025) | The candidate's "Planck 2025" value is atypical. Standard Planck 2018 = 67.36 +/- 0.54. CMB+LambdaCDM (used by H0DN as comparison) = 67.24 +/- 0.35. "Planck 2025" as a distinct data release does not exist in the literature — Planck's final cosmology release was 2018 (PR3). The number 67.27 is close to correct but the label is wrong. This matters because the 7.1-sigma tension H0DN quotes uses 67.24 +/- 0.35 as the CMB baseline, not 67.27 +/- 0.46. | MINOR ERROR |
| **5-7 sigma over 13 years** | Tension at 5-7sigma | Partially confirmed. H0DN 2026 quotes 7.1-sigma vs CMB+LambdaCDM and 5.0-sigma vs BBN+BAO/DESI DR2. da Rocha et al. (2025) decompose the ~6.4-sigma observed tension into ~5.64-sigma real physical tension + measurement error + information loss. The range 5-7sigma is accurate but the candidate should specify which baseline. | PASS with note |
| **"No single probe drives the tension"** | H0DN network analysis claim | Confirmed. H0DN paper explicitly states: removing either Cepheids or TRGB has minimal effect on H0; replacing SNe Ia with galaxy-based indicators changes H0 by <0.1 km/s/Mpc. | PASS |
| **"Multiple independent probes converge on H0~73"** | All probes point to ~73 | **PARTIALLY FALSE.** CCHP (Freedman et al., ApJ 985, 203F, 2025) using JWST TRGB gives H0 = 70.39 +/- ~2.0 (HST+JWST) and 68.81 +/- ~2.2 (JWST-only). CCHP JAGB gives 67.80 +/- ~2.7. These are consistent with Planck at ~1-2sigma, NOT with SH0ES at ~73. CCHP authors explicitly state their results are consistent with LambdaCDM "without the need for additional new physics." TDCOSMO strong lensing gives 71.6 +3.9/-3.3 — intermediate, overlapping both. The claim that all probes converge on ~73 is a selective reading that ignores CCHP. | MAJOR ISSUE |
| **"DESI DR1 BAO data public"** | All DESI DR1 data public | Confirmed. DESI DR1 public. DR2 (2025-2026) also public. | PASS |
| **Bayesian model comparison feasible with public data** | Feasibility claim | Confirmed. Multiple groups have performed such comparisons (Hubble Olympics, CosmoVerse WP, Zhang et al. 2026, Chatrchyan et al. 2025). Public likelihood chains exist for Planck, DESI, Pantheon+. | PASS |
| **Abiuso et al. 2025 "Planckian bound proof"** | Quantum estimation analogy | Abiuso et al. work on Planckian bounds in quantum thermodynamics (finite-time Carnot engines, speed limits). The connection to cosmological H0 measurement is a category error. Quantum estimation bounds in de Sitter space exist (Huang, Feng, Zhang & Fan, Annals of Physics 2018, arXiv:1806.08922) but these are theoretical QFI bounds for idealized Unruh-DeWitt detectors — they do NOT constrain practical H0 measurements from CMB or SN Ia data. The candidate conflates two unrelated research programs. | FATAL ERROR for S4 |

#### Core Contradiction Attack

**Claim under attack:** Proposition A (LambdaCDM complete, local H0 biased by systematics) vs Proposition B (LambdaCDM incomplete, new physics required) are mutually exclusive — either H0 is ~67 or ~73.

**Attack 1 — False Dichotomy (Score impact: -1):** The candidate presents a binary "either/or" framing that does not match the state of the field. At least three intermediate positions exist and are actively debated:

1. **Partial systematics + partial new physics:** da Rocha et al. (2025) decompose the tension as ~78% real + ~13% measurement error + ~9% information loss. Even if the dominant component is real, 22% non-real contribution is substantial and could reduce a 7-sigma tension to ~5-sigma — still significant but qualitaively different.

2. **Redshift-dependent effects:** The DESI DR2 BAO data shows 2-3sigma evidence for dynamical dark energy with phantom crossing. If dark energy is dynamical, compressing the expansion history into a single scalar H0 is misleading. The recent reformulation as E(z) history (arXiv:2605.05691, May 2026) reduces the tension to merely 1.1-2.1sigma — suggesting the "tension" may be partly an artifact of scalar compression.

3. **CCHP undermines Proposition B's central claim:** The candidate asserts that multiple independent local probes converge on H0~73. CCHP TRGB and JAGB (JWST, 2025) give H0~68-70, consistent with Planck. If TRGB — the second-most-important distance indicator — does NOT see the tension, then Proposition B's core empirical motivation is weakened. SH0ES and CCHP disagree at the ~2-3sigma level with each other, pointing to unresolved systematics in at least one of them.

**Attack 2 — Neglected Alternative: Sound Horizon Crisis (Score impact: -1):** The tension may not be a "local H0" problem at all. A growing number of papers (DESI DR1 H0-without-sound-horizon, arXiv:2510.19149; sound-horizon-agnostic methods, arXiv:2509.16202, arXiv:2604.24050) show that removing the sound horizon assumption pushes H0 toward ~71-72 even from CMB+BAO data alone. This reframes the tension as a "sound horizon crisis" — the early-universe sound horizon r_d may be miscalibrated, not the local distance ladder. The proposition fails to engage with this framing.

**Attack 3 — Proposition A's "unaccounted systematic errors" are increasingly constrained (Score impact: +1 for the proposition):** JWST has ruled out crowding/blending in Cepheid photometry at 8.2sigma (Riess et al., Sep 2025). H0DN shows that removing any single distance indicator has negligible effect. The Bayesian jackknife (Hughes, Wilensky & Bull, 2025) finds the "no measurements biased" model is strongly disfavored. Systematics-only explanations are objectively losing ground. This is a genuine strength of the topic.

**Attack 4 — But Proposition B's "new physics" models are also struggling (Score impact: -1):** The Hubble Olympics (Schoneberg et al., updated to 2025) tested 19 models. Early-universe finalists reduce tension to 3sigma at best — none eliminate it. EDE requires fine-tuned parameter space (f~0.8 at z_c~6x10^4) and Bayesian evidence only favors it in narrow regions. DESI DR2 BAO data itself shows ~2sigma tension with Planck CMB WITHIN LambdaCDM — so EDE models that "resolve" the tension may be fitting a data-data discrepancy, not discovering new physics. No model consistently fits all datasets. The candidate presents Proposition B as more promising than the evidence warrants.

**Core Score: 1/3**

The Hubble tension is genuinely one of the most important open problems in cosmology and Nature/Nature Physics-worthy. The H0DN 2026 result is a landmark. BUT the candidate's framing contains a critical factual error (CCHP TRGB does NOT converge on 73), presents a false dichotomy, ignores the sound-horizon reframing, and overstates the case for new physics models. The core is salvageable with revision.

---

#### S1 [Tension Robustness] Attack

**Claim:** Can we quantify the degree of systematic error required to reconcile Planck and local H0 using public likelihood chains? Are they statistically independent?

**Score: 2/3**

- **Strengths:** This is a well-posed and feasible sub-proposition. da Rocha et al. (2025) have already performed a Bayesian error decomposition quantifying the real vs systematic vs information-loss components. Public Planck and SH0ES likelihood chains exist. The Bayesian jackknife approach (Hughes, Wilensky & Bull, 2025) provides a model-agnostic framework. This sub-proposition could produce a publishable analysis.
- **Weaknesses:** (a) "Statistically independent" is overstated. Planck and SH0ES share no raw data, but all local measurements share astrophysical assumptions (SN Ia standardization, reddening laws, metallicity calibrations). Systematic errors can be correlated across "independent" probes. (b) The quantification of "degree of systematic error required" has already been done — the candidate needs to specify what their analysis would ADD beyond da Rocha et al. and the Bayesian jackknife. (c) The candidate doesn't specify which tension metric they would use (Suspiciousness, Bayes ratio, Bhattacharyya coefficient, KL divergence), which is a critical methodological choice.

---

#### S2 [Model Selection] Attack

**Claim:** What is the Bayesian evidence for LambdaCDM vs EDE vs extra DeltaN_eff using combined Planck+DESI+H0DN data? Is there a single model that consistently fits all datasets?

**Score: 1/3**

- **Serious Problem — Prior Art Not Acknowledged:** This Bayesian model comparison has been EXTENSIVELY performed. The Hubble Olympics (Schoneberg et al., Phys. Rep. 984, updated 2025) compared 19 models against Planck+BAO+Pantheon+SH0ES. Chatrchyan et al. (2025, PRD 111, 043536) constrained cold NEDE with Planck NPIPE + Pantheon+ + DESI BAO. Zhang et al. (2026, ApJ 999) performed multi-model Bayesian comparison with DESI DR2. The CosmoVerse White Paper (arXiv:2504.01669, 400+ pages, 400+ authors) comprehensively reviewed all models. SPT-3G + DESI (Khalife et al., arXiv:2507.23355, 2025) constrained axion EDE. The candidate's sub-proposition, as stated, would be a replication of published work unless a novel angle is specified.
- **What could be novel:** (a) Using H0DN 2026 as a new dataset in the comparison (H0DN was published April 2026, after most of the above analyses). (b) A unified information-theoretic framework rather than simple Delta-ln(E) comparison. (c) Joint constraints on model classes rather than individual models. But the candidate does not articulate any of these angles.
- **The "single model fitting all data" question is already answered:** No. All existing reviews conclude no single model resolves all tensions without fine-tuning. This is not a new research question.

---

#### S3 [Distance Ladder Independence] Attack

**Claim:** Can TRGB-only, Mira-only, and strong-lensing-only H0 measurements independently distinguish between systematic bias and new physics?

**Score: 1/3**

- **TRGB-only:** CCHP 2025 (Freedman et al., ApJ 985, 203F) already provides this. H0 = 70.39 +/- 2.0 (HST+JWST) and 68.81 +/- 2.2 (JWST-only). These are consistent with Planck and do NOT support the ~73 value. At current precision (~3%), TRGB-only cannot distinguish between 67 and 73 at high significance (the 2-sigma error bar covers both). The candidate's premise that TRGB converges on ~73 is factually wrong.
- **Mira-only:** NO standalone Mira-only H0 measurement exists in the 2025-2026 literature. Miras are included in H0DN as a first-rank indicator, but there is no Mira-only pipeline producing an independent H0 value with competitive precision. This sub-proposition is currently not feasible without new Mira data.
- **Strong-lensing-only:** TDCOSMO 2025 gives H0 = 71.6 +3.9/-3.3. The ~5% uncertainty is too large to distinguish 67 from 73 at >2sigma. This will improve with JWST+NIRSpec kinematics (already underway for 6/8 lenses) but the sub-proposition overstates what current data can deliver.
- **The sub-proposition is backwards:** The point of independent probes is not that they individually distinguish systematics from new physics (they can't, at current precision). The point is that their CONSENSUS does. H0DN already does this. S3, as framed, is asking probes with 3-5% precision to resolve a ~9% discrepancy — this is statistically underpowered.

---

#### S4 [Information-Theoretic Tension Metric] Attack

**Claim:** Can quantum estimation theory / Fisher information bounds provide a model-independent tension metric that avoids prior-dependence of standard Bayesian methods?

**Score: 0/3**

- **FATAL — Category Error:** The Abiuso et al. (2025) reference concerns Planckian bounds in quantum thermodynamics (finite-time Carnot cycles, quantum speed limits). This is a completely different research program from cosmological parameter estimation. The "Planckian bound" refers to bounds on heat engine efficiency approaching the Planck scale, not to the Planck CMB satellite.
- **Quantum Fisher Information in cosmology exists but does not do what the candidate claims:** Huang, Feng, Zhang & Fan (Annals of Physics, 2018, arXiv:1806.08922) derived QFI bounds for estimating the Hubble parameter using Unruh-DeWitt detectors in de Sitter space. Piotrak, Colas, Alonso-Serrano et al. (arXiv:2507.12228, 2025) applied QFI to quantify information loss in cosmological parameter estimation. These are theoretical results about idealized quantum detectors — they do NOT constrain practical H0 measurements from CMB power spectra or SN Ia light curves, which are fundamentally classical measurements of classical fields.
- **The gap between QFI and classical FI is precisely the problem:** Piotrak et al. (2025) show that practical (classical) measurements fall far short of the QFI bound because accessing the full quantum state of primordial fluctuations would require measuring the decaying mode, which is fundamentally inaccessible. The QFI bound is not a practical constraint on measurement precision — it is a theoretical curiosity.
- **Model-independent tension metrics already exist and avoid prior-dependence:** Handley & Lemos (2019, Phys. Rev. D) developed "Suspiciousness" — a tension metric based on the ratio of posterior to prior volume that is prior-insensitive by construction. The Bhattacharyya coefficient, KL divergence, and posterior predictive p-values are also used. The candidate does not acknowledge these existing methods.
- **The candidate confuses "model-independent" with "parameterization-independent":** QFI depends on the quantum state of the probe, the coupling, and the choice of vacuum — it introduces MORE modeling assumptions, not fewer.
- **This sub-proposition is unsalvageable in its current form.** It would need to be completely rewritten to focus on information-theoretic tension metrics (KL divergence, mutual information, Suspiciousness extensions) without the quantum estimation angle, which is a red herring.

---

### B-Doctor (Cross-Domain Attack)

#### Domain Mappings Analysis

**Mapping 1: Hubble Tension <-> Information Theory**

- **Tension metrics as information divergences:** The Hubble tension is fundamentally an information-theoretic problem: two posterior distributions (CMB-derived and local-distance-ladder-derived) disagree on H0. The natural information-theoretic quantities are the Kullback-Leibler divergence D_KL(P_local || P_CMB), the Jensen-Shannon distance, or the Bhattacharyya coefficient. These are already used in cosmology (Seehars et al., 2014; Handley & Lemos, 2019, 2021). The candidate's S4 gestures at this but doesn't engage with the existing literature.
- **Jeffreys-Lindley paradox:** This is DEEPLY relevant. With modern datasets (Planck: O(10^6) modes, DESI: 14M galaxies), Bayesian evidence automatically penalizes complex models through the Occam factor, even when frequentist significance favors new physics. The Hubble tension sits exactly in this regime: 5-7sigma frequentist significance but Bayesian evidence only mildly favors new physics models (or disfavors them, depending on the prior). This paradox explains why EDE can reduce tension to 1.5sigma in chi^2 while LambdaCDM retains stronger Bayesian evidence — the Occam penalty on EDE's additional parameters (~3) is substantial with these sample sizes. The candidate mentions "Jeffreys-Lindley paradox" in domain mappings but doesn't incorporate this insight into any sub-proposition. This is a MISSED OPPORTUNITY.
- **Mutual information between datasets:** A natural information-theoretic framing: how many bits of mutual information do Planck and SH0ES share? If the answer is "fewer than expected if LambdaCDM is correct," this is a model-independent quantification of tension. This approach avoids the prior-dependence problem entirely. The candidate does not mention it.
- **Score for this mapping: 2/3 for richness, 0/3 for candidate's execution.**

**Mapping 2: Hubble Tension <-> Statistical Physics / EFT**

- **Is LambdaCDM an EFT?** Yes. The theory of cosmological perturbations is an EFT. At linear order, LambdaCDM is a free field theory on FLRW background. At nonlinear order (structure formation), it admits an EFT description (EFTofLSS, Baumann et al. 2012; Carrasco et al. 2012). The relevant question for the Hubble tension is whether the EFT breaks down at the sound horizon scale (~150 Mpc comoving), which would manifest as a mismatch between early-universe (CMB) and late-universe (BAO, SNe) parameter inference. This is a legitimate and deep question.
- **But this is not the question the candidate is asking.** The EFT framing naturally leads to asking whether LambdaCDM's parameters (H0, Omega_m, sigma_8) are scale-dependent — i.e., whether the EFT has relevant operators that become important at late times. This maps to dynamical dark energy or modified gravity, which are being actively tested. However, the candidate's sub-propositions don't engage with the EFT framing — S2 is a standard model comparison, S3 is about distance indicators, neither uses EFT concepts like operator dimension, cutoff scale, or renormalization group flow.
- **Dark energy as a cosmological constant is the ultimate EFT problem:** The cosmological constant problem is the worst EFT fine-tuning problem in physics (120 orders of magnitude). The Hubble tension could be a manifestation of this EFT breakdown. But this connection, while profound, is not operationalized in any sub-proposition.
- **Score for this mapping: 2/3 for depth, 0/3 for operationalization.**

**Mapping 3: Hubble Tension <-> Quantum Estimation Theory**

- **The QFI bound for H0 measurement:** Huang et al. (2018) derived that the variance of any unbiased estimator of H satisfies Var(H) >= 1 / [N * F_Q(H)], where F_Q is the QFI of a two-level Unruh-DeWitt detector in de Sitter space. The QFI depends on the detector energy gap Omega, the coupling constant, the measurement time, and the choice of vacuum (Bunch-Davies vs alpha-vacua).
- **Why this does not constrain CMB-based H0:** The CMB is NOT a quantum measurement of a Unruh-DeWitt detector. CMB temperature anisotropies are classical random fields — the quantum-to-classical transition occurred during inflation when each mode crossed the Hubble horizon. By the time of last scattering (z~1100), all observable modes were classical. The QFI bound from de Sitter quantum metrology is irrelevant to the CMB power spectrum measurement of H0.
- **Where QFI could matter — and why the candidate misses it:** The primordial B-mode polarization signal from inflationary gravitational waves is a genuinely quantum probe (the tensor perturbations are quantized). QFI bounds could constrain the ultimate precision of r (tensor-to-scalar ratio) measurement. But r is not the Hubble constant. The candidate conflates different parameters.
- **The Abiuso et al. confusion:** The candidate cites "Abiuso et al. 2025 Planckian bound proof" — this refers to work on quantum thermodynamic uncertainty relations and Planckian bounds on finite-time Carnot cycles. The word "Planckian" here means "fundamental bounds on thermodynamic processes at the scale of ~k_B T" — NOT the Planck satellite. The candidate has confused two completely different uses of "Planck/Planckian" in physics.
- **Score for this mapping: 1/3 for conceptual interest, -1/3 for conflation error.**

#### Cross-Domain Insight

The strongest cross-domain connection the candidate SHOULD have made: **The Hubble tension is an instance of the Jeffreys-Lindley paradox applied to cosmology.** With O(10^7) data points (Planck + DESI), Bayesian evidence acquires an enormous Occam penalty. A model with 3 extra parameters (EDE: f_EDE, z_c, theta_i) can improve chi^2 substantially while Delta ln(E) still favors LambdaCDM. This means the "5-7sigma" framing (frequentist) and the "no model beats LambdaCDM" framing (Bayesian) are not contradictory — they are two sides of the Jeffreys-Lindley paradox. An information-theoretic tension metric based on mutual information or minimum description length could bridge this gap WITHOUT invoking quantum estimation theory. The candidate gestures at information theory but misses the central insight.

#### B-Doctor Core Score: 1/3

The candidate identifies promising cross-domain connections (information theory, EFT, quantum estimation) but: (a) the quantum estimation connection is based on a category error (confusing Planckian thermodynamic bounds with Planck satellite CMB data), (b) the information-theoretic connection exists but doesn't engage with the relevant literature (Suspiciousness, KL divergence, Jeffreys-Lindley), (c) the EFT connection is legitimate but completely unoperationalized. The cross-domain framing adds novelty but the execution is weak.

#### B-Doctor S1-S4 Scores

- **S1 (Tension Robustness, info-theoretic angle): 2/3** — The Bayesian error decomposition of da Rocha et al. (2025) is exactly the right approach. An information-theoretic extension using mutual information between datasets (rather than variance decomposition) would be genuinely novel. But the candidate doesn't propose this.
- **S2 (Model Selection, info-theoretic angle): 1/3** — Standard Bayesian model comparison. The Jeffreys-Lindley insight (large-N Occam penalty) could justify a minimum description length or normalized maximum likelihood approach instead of standard Bayes factors. The candidate doesn't mention this.
- **S3 (Distance Ladder Independence, EFT angle): 1/3** — CCHP TRGB vs SH0ES Cepheids disagree at ~2-3sigma. This is itself a tension. The EFT framing would ask: are Cepheid and TRGB distances systematically different at the ~1% level due to different astrophysical environments (metallicity, age) probing different effective theories? Interesting but not developed.
- **S4 (Tension Metric, QET angle): 0/3** — As analyzed above. The quantum Fisher information connection is a category error. The sub-proposition as stated is based on a misunderstanding of the referenced literature.

---

### Summary Table

| Component | A-Doctor | B-Doctor | Notes |
|-----------|----------|----------|-------|
| **Core Proposition** | 1/3 | 1/3 | Topic is genuine Nature/NatPhys caliber. Framing is oversimplified, contains factual error about CCHP TRGB convergence. |
| **S1 (Tension Robustness)** | 2/3 | 2/3 | Feasible but prior art exists. Needs information-theoretic angle for novelty. |
| **S2 (Model Selection)** | 1/3 | 1/3 | Extensively done. H0DN dataset is new but incremental. Needs reframing around Jeffreys-Lindley. |
| **S3 (Distance Ladder Independence)** | 1/3 | 1/3 | Mira-only doesn't exist. CCHP TRGB contradicts candidate's premise. Individual probes are underpowered. |
| **S4 (Tension Metric)** | 0/3 | 0/3 | FATAL. QFI connection is a category error (confuses Planckian thermodynamics with Planck satellite). Unsavageable as written. |
| **Overall** | **1.0/3** | **1.0/3** | **RECOMMENDATION: FIX** |

---

### Recommendation: FIX

**Justification:** The Hubble tension is a genuine L5 Type A proposition — a 5-7sigma confrontation between theory and experiment spanning 13+ years, Nature/NatPhys-worthy, all public data, no new experiment needed. The H0DN (2026) result makes the topic TIMELY: the 7.1sigma result with 1.1% precision, published April 2026, is the strongest statement yet that the tension is real. All core data are public and Bayesian reanalyses are feasible with existing tools.

However, the proposition requires SUBSTANTIAL REVISION before it can proceed to PaperSpine build:

**Required Fixes (blocking):**

1. **Correct the CCHP omission (S3 blocker):** The claim that "multiple independent local probes independently converge on H0~73" is factually wrong. CCHP TRGB (Freedman et al., ApJ 985, 2025) gives H0 = 70.39 +/- 2.0 — consistent with Planck, NOT with SH0ES. The proposition must acknowledge and engage with the SH0ES-vs-CCHP tension (which is itself a ~2-3sigma discrepancy within the local distance ladder). This is not optional — it's the most important counter-evidence to Proposition B.

2. **Rewrite or delete S4 (non-negotiable):** The quantum Fisher information connection is based on conflating "Planckian bound" (quantum thermodynamics) with "Planck satellite" (CMB cosmology). These are entirely different research programs. S4 must either be: (a) rewritten as an information-theoretic tension metric sub-proposition using KL divergence, mutual information, or minimum description length (no quantum estimation), or (b) dropped entirely and replaced. The Abiuso et al. reference must be removed.

3. **Acknowledge prior art in S2:** The Hubble Olympics (Schoneberg et al.), CosmoVerse White Paper, Chatrchyan et al. (NEDE+DESI), and Zhang et al. (dynamical DE+DESI DR2) have already performed extensive Bayesian model comparison. S2 is only novel if it (a) uses H0DN 2026 as a new dataset and (b) uses an information-theoretic framework beyond simple Delta-ln(E) comparison. This must be explicit.

**Recommended Fixes (quality improvement):**

4. **Soften the false dichotomy:** Replace "Either the true Hubble constant is ~67 or ~73" with a more nuanced framing that acknowledges: (a) CCHP at ~70, (b) the possibility of partial systematics + partial new physics, (c) the sound-horizon reframing (the tension may be in r_d, not H0). The da Rocha et al. 78%-real decomposition provides a natural framework.

5. **Add a "Sound Horizon" sub-proposition:** Replace S4 with an analysis of whether the tension is in H0 or in r_d, using sound-horizon-agnostic BAO analyses (already demonstrated with DESI DR1 and DR2, arXiv:2510.19149, arXiv:2604.24050). This is computationally feasible (public DESI likelihoods), novel (H0DN dataset not yet included in such analyses), and directly relevant to the core contradiction.

6. **Drop Mira-only from S3:** Since no standalone Mira H0 measurement exists, replace "Mira-only" with JAGB (CCHP has JWST JAGB at 67.80 +/- 2.7) or surface brightness fluctuations, both of which have actual published measurements.

7. **Engage with the Jeffreys-Lindley paradox:** The information-theoretic domain mapping naturally leads to the insight that the frequentist 5-7sigma vs Bayesian "no model beats LambdaCDM" is the Jeffreys-Lindley paradox in action. A sub-proposition that quantifies this explicitly (e.g., computing the Occam factor for EDE with DESI+H0DN sample sizes, or comparing AIC/BIC/DIC/Watanabe-Akaike IC across models) would be genuinely novel.

**If the candidate fixes items 1-3 above, re-evaluate for PASS. Otherwise, KILL on S4 alone (the QFI error is fatal and renders the proposition non-credible to reviewers).**

---

### Source Index

1. H0DN Collaboration (Casertano et al.), "The Local Distance Network," A&A 708, A166 (2026). DOI: 10.1051/0004-6361/202557993
2. da Rocha, Ribeiro & Oliveira, "On the True Significance of the Hubble Tension," Universe 11(9), 303 (2025). arXiv:2509.09034
3. Freedman et al. (CCHP), "Status Report on the CCHP: H0 Using HST and JWST," ApJ 985, 203F (2025). DOI: 10.3847/1538-4357/adc8a1
4. TDCOSMO Collaboration, "Strong Lensing H0 with JWST NIRSpec Kinematics," A&A 704 (2025). DOI: 10.1051/0004-6361/20255580
5. CosmoVerse White Paper, arXiv:2504.01669v2 (2025)
6. Schoneberg et al., "Hubble Olympics," Phys. Rep. 984, 1-55 (2022, updated 2025)
7. Khalife et al., "SPT-3G D1: Axion EDE with CMB and DESI," arXiv:2507.23355 (2025)
8. Chatrchyan et al., "Confronting Cold NEDE with Updated Data," PRD 111, 043536 (2025)
9. Zhang, Xu & Chen, "Dynamical DE and the Unresolved Hubble Tension," ApJ 999, 248 (2026). arXiv:2512.07281
10. Hughes, Wilensky & Bull, "Systematic Assessment via Bayesian Jackknife," arXiv:2511.19341 (2025)
11. Riess et al. (SH0ES), "JWST Crowding Test," Sep 2025
12. Huang, Feng, Zhang & Fan, "Quantum Estimation in an Expanding Spacetime," Annals of Physics 397, 336 (2018). arXiv:1806.08922
13. Piotrak, Colas, Alonso-Serrano et al., "Quantum Estimation of Cosmological Parameters," arXiv:2507.12228 (2025)
14. Handley & Lemos, "Quantifying Suspiciousness," PRD 100, 023512 (2019). arXiv:1906.06781
15. Adi, "Lowering the Horizon on Dark Energy," JCAP 03 (2026). arXiv:2509.12331
16. Poulin et al., "Double the Axions, Half the Tension," arXiv:2604.13535 (2026)
17. "From Scalar H0 to E(z): Reformulating the Hubble Tension," arXiv:2605.05691 (2026)
18. "Dissecting the Hubble Tension: 83 Sound-Horizon-Free Measurements," arXiv:2601.00650 (2026)
19. DESI DR1 H0 Without Sound Horizon, arXiv:2510.19149 (2025)
20. W. Wu et al., "Sound-Horizon-Free H0 from DESI DR2 BAO Using ANN," arXiv:2604.24050 (2026)
