# R1 REVIEWER REPORT — PRD Anonymous Referee
## Verdict: MAJOR REVISION (bordering on REJECT)

---

## PART A: Main Paper Review

### A1. Narrative Logic

**Core claim:** A driven-dissipative ensemble of cosmic two-level systems (qubits), whose collective dynamics follow a complex Langevin equation with mean-field nonlinearity, provides a microscopic theory for the empirical correlation between structure formation and dark energy evolution reported by Gough (2025), with phantom crossing emerging as a dynamical threshold at a calculable critical determination fraction a_c^2.

**Gap description in Introduction:** The Introduction correctly frames Gough's work as empirical correlation without microscopic theory, and correctly identifies that single-field quintessence and phantom models cannot cross w=-1 alone. However, the Introduction conflates two distinct motivations: (a) "DESI sees phantom crossing, existing models struggle" and (b) "Gough found an empirical SFR-w correlation." The connection between (a) and (b) is never established beyond Gough's claim — i.e., there is no independent evidence that structure formation actually causes dark energy, as opposed to being correlated with it. The gap is therefore imprecise: "prior work lacked a microscopic theory" presupposes that a microscopic theory of this specific mechanism is needed, which assumes the mechanism exists.

**Derivation chain:** The paper attempts a six-step chain: qubit ensemble → mean-field Hamiltonian → a_c^2 → Langevin equation → driving function → w(z) → DESI comparison. However, the chain breaks at two critical junctures (see A2 below): the Langevin equation used in the main text is not the equation derived from the Lindblad master equation in the SM, and the a_c^2 derivation in the SM is algebraically incomplete.

**Discussion of limitations:** The Discussion is unusually honest for a theory paper: it explicitly flags the Landauer assumption as "the weakest link," discusses the kappa-a_c^2 degeneracy, acknowledges that Δχ^2 is "indicative, not a detection," and states that DESI DR3 could falsify the model. This is a strength. However, an important limitation is missing: the Discussion does not address what happens at high redshift (z > 2), where the model predicts w → -1 + κ a_c^2 ≠ -1 unless finely tuned — a tension with CMB constraints that is not discussed.

### A2. Physics/Mathematics Correctness

**FATAL ISSUE 1: The Langevin equation is not correctly derived from the Lindblad equation.**

The SM derivation (Section 1.2) starts correctly from the Lindblad master equation and obtains:

d⟨σ_-⟩/dt = -(i/ħ)ΔE_eff ⟨σ_-⟩ — γ⟨σ_-⟩ + i(ηf/ħ)⟨σ_z⟩

Substituting ΔE_eff = ΔE_0 + 2g(1-2|A|^2) and ⟨σ_z⟩ = 1-2|A|²:

dA/dt = -i[ω_0 + (2g/ħ)(1-2|A|²)]A — γA + i(ηf/ħ)(1-2|A|²)      [Eq. SM-derived]

The main text Eq. (5) presents:

dA/dt = -iω_0(1 — |A|²/a_c²)A — γA + ηf(t)                       [Eq. MT]

These two equations are NOT equivalent. I verified this explicitly: using a_c² = (ΔE_0+2g)/4g and ω_0 = ΔE_0/ħ, the coherent terms match only when |A|² = a_c² (exactly at the critical point). Away from the critical point — which is where the model is used over 0 < z < 2, with |A|²/a_c² varying from 0.01 to 0.85 according to SM Table 3 — the two equations differ by O(|A|²/a_c² — 1).

The differences are: (i) the MT equation is missing a factor of i in the drive term (the drive should cause rotation in the complex plane, not real displacement); (ii) the MT equation is missing the factor ⟨σ_z⟩ = 1-2|A|² in the drive term, which provides a self-limiting feedback (the drive changes sign when |A|² crosses 1/2); (iii) the coherent term in the SM-derived equation has a different functional form. The SM states that "the drive term ∝ ⟨σ_z⟩ [is] absorbed into the definition of η" — but ⟨σ_z⟩ varies from +1 to approximately -1 across the redshift range of interest. Absorbing a state-dependent factor that changes sign into a constant parameter is not mathematically justified.

**FATAL ISSUE 2: The SM evidence contradicts the core claim of phantom crossing for the P_coll driver.**

The main text abstract states: "The predicted w(z) crosses -1 at z ~ 0.5-1, consistent with DESI reconstructions." This is presented as a general prediction of the model. However, SM Table 2 shows that for the P_coll driver (the "more fundamental" driver, claimed as an improvement over SFR), w(z) > -1 at all four DESI bins: w(0.25) = -0.79, w(0.75) = -0.91, w(1.25) = -0.91, w(2.0) = -0.80. SM Table 3 further confirms that |A|²/a_c² peaks at 0.85 (at z=1.0), meaning |A|² < a_c² everywhere, and therefore w(z) > -1 everywhere under Eq. (7). The phantom crossing occurs only for the SFR driver (w(1.25) = -1.01), which the paper claims to improve upon by replacing it with the P_coll driver.

The paper's narrative is that P_coll is the refined, more fundamental driver, and that the qualitative prediction is "robust across all variants" (line 193-194). The SM data directly refutes this: the P_coll variant does NOT produce phantom crossing. This is a direct contradiction between the main text's core qualitative claim and the quantitative evidence presented in the SM.

**FATAL ISSUE 3: The derivation of the dynamical a_c² in SM Section 2.2 is incomplete and potentially circular.**

The SM writes the steady-state condition (setting dA/dt = 0 in Eq. MT), then states: "Expanding about the critical point |A|² = a_c² — δ with small δ, and solving the resulting equation: δ = a_c² · γ/√(γ²+ω_0²)." No intermediate steps are shown. I attempted to reconstruct the derivation:

From the steady state: [ω_0²(δ/a_c²)² + γ²](a_c² — δ) = η²f²

Dropping the ω_0² term (unjustified when ω_0 is comparable to or larger than γ, as in the P_coll best-fit where ω_0/H_0 = 20 > γ/H_0 = 10): γ²(a_c² — δ) ≈ η²f². This gives δ = a_c² — η²f²/γ², not the claimed result δ = a_c² · γ/√(γ²+ω_0²).

The derivation from the steady-state equation to the claimed δ formula is not shown and does not appear to follow from the stated premises. Furthermore, the derivation uses a_c² in the ODE to derive a corrected a_c² — the equilibrium a_c² and the dynamical a_c² are not clearly distinguished. The reader cannot verify that Eq. (4) of the main text follows from the stated assumptions.

**MAJOR ISSUE 1: The w(z) relation is ad hoc.**

Equation (7), w(z) = -1 + κ(a_c² — |A|²), is stated to be the "first-order Taylor expansion of a more general relation w+1 = F(|A|²) about the critical point." The function F is never specified. No physical principle connects the determination fraction of an abstract qubit ensemble to the cosmological equation of state. The linear relation is a guess, not a derivation. The paper acknowledges that the linear approximation is marginal (|A|²/a_c² — 1 is not ≪ 1 over much of the redshift range), but does not provide the full nonlinear expression F, without which the reader cannot assess the error introduced by linearization.

**MAJOR ISSUE 2: High-redshift behavior is inconsistent with ΛCDM and is not discussed.**

As z → ∞, f(z) → 0 (no structure formation), so A → 0 (the trivial steady state; stability is confirmed since Re(eigenvalue) = -γ < 0). Then w(z→∞) = -1 + κ a_c². For any non-zero κ and a_c², this gives w(z→∞) ≠ -1, contradicting the requirement that dark energy be negligible at early times (the model's own premise is that dark energy emerges from structure formation, which did not occur at high z). The paper never discusses this limit or explains how the model recovers ΛCDM at high redshift.

**MAJOR ISSUE 3: The gravitational collapse power calculation uses a non-standard formation rate formula.**

The SM Equation for Γ(M,z) in Section 3.3 is given as: Γ(M,z) = (dn/dM) · (dδ_c/dz) · (dz/dt) · (1/σ²)|dσ²/dM|. This is not the standard extended Press-Schechter formation rate (see Sasaki 1994, MNRAS 269, 161; Lacey & Cole 1993, MNRAS 262, 627). The standard expression involves the conditional mass function and a derivative with respect to the critical threshold. The formula shown appears to be dimensionally motivated but is not derived or referenced to the standard EPS literature. The authors should either derive this formula from the standard EPS formalism or use one of the standard expressions (e.g., the Sasaki parameterization).

**MAJOR ISSUE 4: a_c² depends on the choice of driver function, contradicting its claimed status as a microscopic parameter.**

SM Table 2 shows a_c² = 0.28 for the P_coll driver and a_c² = 0.15 for the SFR driver — nearly a factor of 2 difference. But a_c² is defined in terms of the microscopic Hamiltonian parameters g, ΔE_0, and the damping rate γ (Eq. 4). If a_c² is truly a derived parameter of the qubit Hamiltonian, it should be independent of which astrophysical proxy (P_coll or SFR) is used for the driving function f(t). The fact that different drivers require different a_c² values indicates that ω_0 and γ are not fundamental parameters but phenomenological fitting variables, undermining the paper's claim to provide a "microscopic theory."

**MINOR ISSUE 1: Limiting case γ ≫ ω_0 gives a_c² → 0 in Eq. (5).**

If a_c² → 0, then the term |A|²/a_c² in the Langevin equation diverges unless |A|² → 0 at least as fast. The dynamics become singular in the strong-damping limit. The paper states this limit as "strong damping prevents the phase transition" but does not address the mathematical singularity in the ODE.

**MINOR ISSUE 2: Dimensions are consistent throughout.**

All parameters have consistent dimensions: ω_0, γ, η have [time]⁻¹; a_c², |A|², f(t), κ are dimensionless. No dimensional errors detected.

### A3. Data/Evidence Support

**MAJOR ISSUE 5: Figures are missing.**

The submission contains multiple instances of "Figure 1 (to be included)" and "Figure 2 (to be included)." A referee cannot evaluate whether figures support the claims. This alone is grounds for returning the manuscript to the authors before review.

**MAJOR ISSUE 6: Binned w(z) data is not from the official DESI DR2 likelihood.**

The paper acknowledges (line 165): "these binned values are derived from non-parametric reconstructions that carry their own model-dependence." The χ² values are described as "indicative" and "not based on the official DESI DR2 likelihood." This is honest, but it means the quantitative comparison — the paper's primary piece of evidence — is not reliable. A proper MCMC analysis using the full DESI likelihood is required for any quantitative claim.

**MAJOR ISSUE 7: The χ² improvement is driven by a single data point.**

I verified the χ² calculation from the SM Table 2 numbers. For ΛCDM, the total χ² = 5.69 breaks down as: z=0.25: 5.44; z=0.75: 0.11; z=1.25: 0.05; z=2.00: 0.08. Almost the entire χ² penalty for ΛCDM (96%) comes from a single data point at z=0.25 (w = -0.72 ± 0.12 vs. ΛCDM's w = -1.00). The model's Δχ² ≈ 4.7-5.2 depends almost entirely on fitting this one point. This is not evidence for a new model — it is evidence that one DESI binned data point prefers w > -1. The paper should note this explicitly.

**MAJOR ISSUE 8: No error estimates on best-fit parameters.**

The best-fit ω_0/H_0 and γ/H_0 values are reported without confidence intervals. Are ω_0/H_0 = 20 and γ/H_0 = 10 uniquely determined, or is there a broad degeneracy? Given the small number of data points (4) and the acknowledged κ-a_c² degeneracy, the parameter constraints are likely very weak. Without error estimates, the reader cannot assess whether the model makes sharp predictions or merely accommodates the data.

**MAJOR ISSUE 9: Calibration to w_0 = -0.785 is methodologically inconsistent.**

The paper calibrates w(z=0) to the DESI CPL-extrapolated value w_0 = -0.785 (line 140). But the model's w(z) is not of CPL form. Using a CPL-extrapolated value as a calibration target for a non-CPL model introduces a systematic bias: the CPL fit projects the redshift-binned constraints onto a two-parameter form that the present model does not share. The calibration target should be derived from a model-independent reconstruction.

**MINOR ISSUE 3: The χ²/dof < 1 for both model variants.**

The reported χ²/dof = 0.47 (P_coll) and 0.26 (SFR) indicate that the DESI error bars substantially over-encompass the model predictions. This is not an error per se, but combined with the small number of data points, it means the model is essentially unconstrained by current data — a point the paper acknowledges in passing but should state more prominently.

### A4. Citation Completeness

**MAJOR ISSUE 10: Three ghost citations in the bibliography.**

Mishra:2026 (line 321), Zhao:2009 (line 324), and Martineau:2005 (line 327) appear as \bibitem entries in the bibliography but are never cited with \cite{} anywhere in the main text body. The cover letter references "Martineau & Brandenberger 2005, Zhao et al. 2009" as examples of prior art, but they do not appear in the main text itself. These must either be cited in the text body or removed from the bibliography.

**MAJOR ISSUE 11: Missing key references.**

- The extended Press-Schechter halo formation rate formalism should cite Sasaki (1994, MNRAS 269, 161) and/or Lacey & Cole (1993, MNRAS 262, 627), not just Sheth & Tormen (1999) for the mass function.
- The Lindblad master equation and open quantum systems should cite a standard textbook (e.g., Breuer & Petruccione, "The Theory of Open Quantum Systems"; or Gardiner & Zoller, "Quantum Noise").
- For the analog quantum simulation proposal, references to existing small-scale quantum simulations of Ising/Curie-Weiss models on superconducting qubit platforms are appropriate (e.g., Salathe et al. 2015, Phys. Rev. X 5, 021027; Barends et al. 2016, Nature 534, 222).
- The Dicke model and superradiant phase transitions, which are closely related to the mean-field Ising model in the thermodynamic limit, are not referenced despite being direct precursors to the proposed mechanism.

**MAJOR ISSUE 12: DGF:2024 is an unpublished internal note.**

Reference [15] is listed as "H. Zhongchang, DGF framework (2024-2026), internal notes." This is the author citing their own unpublished work. Internal notes are not publicly accessible and cannot be verified by readers or referees. If the DGF framework is essential to the paper's narrative, it must be published or included as part of the present work. If it is inessential, the citations should be removed and any necessary content included in the present manuscript or SM.

**MINOR ISSUE 4: Citation format inconsistency.**

Some arXiv references use the old identifier format (e.g., astro-ph/0510523 for Martineau:2005), while others use the current format (e.g., 2503.14738 for DESI:2025). This is a minor formatting issue but should be standardized.

**Citation spot-check results (3 verifiable citations):**
- Hu:2005 (PRD 71, 047301): The paper characterizes it as showing "generic internal degrees of freedom enable phantom crossing through specific kinetic couplings." This is a reasonable characterization of Hu's result about the necessity of internal degrees of freedom for phantom crossing. ACCURATE.
- Feng:2005 (PLB 607, 35): The paper describes it as the quintom model requiring "two distinct fields (one quintessence, one phantom)." This is accurate. ACCURATE.
- Sheth:1999 (MNRAS 308, 119): Cited for the halo mass function. Used appropriately. ACCURATE.
- Landauer:1961 (IBM J. Res. Dev. 5, 183): The classic Landauer principle paper. The paper correctly notes the limitations of applying Landauer's principle to self-gravitating systems. ACCURATE.

**Recent paper ratio:** 12 out of 25 references (48%) are from 2024-2026. PASSES the 30% threshold.

### A5. Testability

**MAJOR ISSUE 13: Core predictions are qualitative, not quantitative.**

The paper states that "the crossing redshift z_cross should correlate with the P_coll peak redshift (a prediction unique to this model)" (line 226). However, no specific correlation is given: what is the predicted functional relationship? What numerical range for z_cross? What is the predicted CPL slope w_a? The reader cannot evaluate whether DESI DR3 would confirm or refute the model without specific numerical predictions with error bands.

**Boundary case — proposed quantum simulation:**

The quantum simulation proposal (Section 5.4) is described as "a proposed experiment, not an executed one." The review checklist asks: "Are there any 'in principle possible' or 'awaits future experiments'-type hand-waving claims?" The quantum simulation is exactly this type of claim. However, I classify this as MAJOR rather than FATAL because: (a) the paper is explicit that the experiment has not been executed; (b) the core cosmological predictions are separately testable with DESI DR3; (c) the simulation proposal is supplementary to the main argument. That said, presenting an unexecuted experiment as supporting evidence weakens the paper's empirical grounding.

**Testability summary:**
- DESI DR3: Dataset specified (DESI), observable specified (w(z) bins), but numerical range not given → PARTIAL
- z_cross - P_coll correlation: Observable specified, but no quantitative prediction → INSUFFICIENT
- Analog quantum simulation: Proposed but not executed → NOT TESTED
- Landauer assumption: Explicitly labelled as a hypothesis, not tested → NOT TESTED

---

## PART B: Supplemental Material Review

**B1. Main text → SM cross-references: MISSING.**

The main text never references the Supplemental Material document. The main text has two appendices (A: Langevin derivation, B: P_coll computation details) that overlap in content with SM Sections 1 and 3. There is no statement in the main text such as "see Supplemental Material for details." The SM is a standalone document whose relationship to the main text is unclear. This must be fixed.

**B2. SM internal self-consistency: FAILS at one critical point.**

SM Section 1.2 derives the Langevin equation from the Lindblad master equation and obtains dA/dt with a drive term i(ηf/ħ)⟨σ_z⟩. SM Equation (3) then presents the simplified form dA/dt = -iω_0(1-|A|²/a_c²)A - γA + ηf(t), claiming the drive term was "absorbed." As discussed in A2 above, the two forms are inequivalent away from the critical point. The SM contains an internal contradiction: its own derivation does not lead to the equation it claims to derive.

**B3. SM numbers consistency with main text: PARTIALLY CONSISTENT.**

- Best-fit parameters (ω_0/H_0, γ/H_0): SM Table 2 matches main text Table 1. ✓
- χ² values: SM reports 0.95 (P_coll) and 0.52 (SFR); main text reports 0.95 and 0.52. ✓
- a_c² values: SM reports 0.28 (P_coll) and 0.15 (SFR). I verified these follow from Eq. (5) with the stated ω_0, γ values. ✓
- w(z) predictions at DESI bins: SM Table 2 values are internally consistent with each other and with the χ² values reported. ✓
- HOWEVER: SM Table 2 w(z) values for P_coll contradict the main text claim of phantom crossing. ✗

**B4. SM figures: NOT PRESENT.**

SM Figure 1 (w(z) prediction band) is mentioned in the text but not included. The SM is incomplete.

**B5. SM contains additional assumptions not in main text.**

- Gaussian decoupling approximation (⟨σ_z σ_-⟩ ≈ ⟨σ_z⟩⟨σ_-⟩) is stated in SM Section 1.2 but not mentioned in the main text. This is a non-trivial approximation.
- Fiducial M_min = 10⁸ M_⊙ and M_max = 10¹⁶ M_⊙ are specified in SM Section 3.4 but not in the main text. The main text says M_min is "uncertain by ~14 orders of magnitude" (line 115), but the SM only varies M_min over 6 orders of magnitude (10⁶ to 10¹²) in the systematic uncertainty band.
- The claim that "1/N corrections are O(1/N) and negligible for cosmological ensembles (N ≫ 10⁸⁰)" appears in SM Section 1.2 but not in the main text. Given the all-to-all coupling (1/N normalization in Eq. 1), standard mean-field theory requires N → ∞ for exactness — the claim of negligibility should be justified.

**B6. SM conclusions consistent with main text: NO (see FATAL Issue 2).**

The SM data for the P_coll driver shows w(z) > -1 at all bins, while the main text claims phantom crossing at z ~ 0.5-1. This is a direct contradiction.

**B7. SM independent references: NONE.**

The SM has no reference list of its own. It relies entirely on references defined in the main text. While this is acceptable for some journals, PRD typically expects the SM to be self-contained.

**Additional SM issues:**

**MAJOR ISSUE 14: SM Table 1 (driving function values) reveals factor-of-2 variation between halo mass functions.**

The Tinker (2008) mass function gives P_coll(z=2.0) / P_coll(0) = 7.67, while Sheth-Tormen gives 3.88. This is a factor-of-2 variation in the driving function at the highest-redshift DESI bin. The paper claims that "the qualitative prediction...is robust across all variants" (main text line 193-194). A factor-of-2 variation in the core input function at z=2 challenges this claim, especially given that the DESI error bar at z=2.0 is ±0.35 — large enough to accommodate either value.

---

## PART C: Cover Letter Review

**C1. Claimed findings vs. main text and SM: EXAGGERATION DETECTED.**

The cover letter states: "the first to provide dynamical equations, a Hamiltonian, and derived (not fitted) parameters" (emphasis in original). This is misleading. The parameters ω_0 and γ are fitted to DESI binned data. a_c² is algebraically related to ω_0 and γ through Eq. (4), so it inherits the fitted status of ω_0 and γ. The only "derived" quantities are expressions that depend on fitted inputs. The claim of "derived (not fitted) parameters" is an exaggeration.

**C2. Novelty claim precision: PARTIALLY MATCHES.**

The cover letter's novelty claims (items 1-4) align with the Introduction's framing of the gap (Gough's phenomenological correlation lacking microscopic theory). However, the claim about the driving function having "zero phenomenological inputs" is overstated — P_coll depends on the halo model (Press-Schechter/Sheth-Tormen/Tinker, all of which are calibrated to N-body simulations), the Eisenstein-Hu transfer function (calibrated to CMB data), and Planck 2018 cosmological parameters (fitted to multiple datasets). These are standard but they are still phenomenological inputs.

**C3. Limitations omitted from cover letter: SIGNIFICANT.**

The following limitations discussed in the main text and SM are absent from the cover letter:
- The κ-a_c² degeneracy (main text Section 5.3)
- The marginal validity of the linear w+1 expansion (main text line 140-141; SM Section 5)
- The fact that figures are not yet included in the manuscript
- That the quantitative comparison uses binned data from non-parametric reconstructions, not the official DESI likelihood
- That the χ²/dof < 1 indicates the model is essentially unconstrained by current data
- That the P_coll driver does NOT show phantom crossing in the binned data (SM Table 2)

**C4. Forbidden phrases: NONE FOUND (pass).**

No "in principle possible," "awaits future experiments," "we hope," or "we are confident" detected in the cover letter.

**C5. Length: APPROPRIATE (well under 1 page).**

**C6. Journal-specific requirements: NOT MENTIONED.**

The cover letter does not reference any PRD-specific submission requirements (e.g., statement about prior publication, author agreement, suggested referees' conflicts of interest, etc.). While the letter mentions "honest scoping" as appropriate for PRD, it does not follow PRD's cover letter guidelines.

---

## PART D: Cross-Consistency Check (Three Materials)

**D1. Three-way consistency of core claims: FAILS.**

| Core Claim | Main Text | SM Evidence | Cover Letter |
|---|---|---|---|
| Phantom crossing at z~0.5-1 | Claims crossing occurs (abstract, line 188) | P_coll driver: NO crossing. SFR driver: crossing at z~1. | Claims phantom crossing mechanism |
| P_coll driver is "more fundamental" | Claims P_coll is refinement over SFR (line 157) | P_coll performs WORSE (χ²=0.95 vs 0.52) and does NOT cross -1 | Claims "zero phenomenological inputs" |
| Parameters are "derived" | States a_c² is "derived" (line 80-81) but ω_0, γ are fitted | Same parameters fitted | Claims "derived (not fitted)" |

**FATAL ISSUE 4 (Cross-consistency): The core qualitative prediction is contradicted by the SM quantitative evidence.**

The main text and abstract claim that the model predicts phantom crossing at z ~ 0.5-1. The SM's best-fit results for the P_coll driver — the variant presented as the primary model — show w(z) > -1 at all DESI bins and |A|²/a_c² < 1 everywhere. The three documents are not telling the same story. This is a three-way inconsistency between main text claim, SM evidence, and cover letter framing.

**D2. Symbol consistency: PARTIALLY CONSISTENT.**

- ω_0, γ, a_c², A, f(t), η, κ: defined identically across main text and SM. ✓
- P_coll vs. 𝒫_coll: the symbol 𝒫_coll in the main text appears as P_coll in the SM. Minor formatting difference.
- a_c² is sometimes boxed (main text Eq. 4) and sometimes not. Minor formatting.

**D3. Numerical value consistency: CONSISTENT (where comparable).**

Verified values: ω_0/H_0 = 20 (P_coll), γ/H_0 = 10, χ² = 0.95 (P_coll) / 0.52 (SFR), ΛCDM χ² = 5.69, a_c² = 0.28 (P_coll) / 0.15 (SFR). All values match between main text Table 1 and SM Table 2.

---

## PART E: AI Writing Patterns (Preliminary)

**FLAGGED PATTERNS:**

1. **Uniform paragraph length.** Most paragraphs in the main text are 3-5 sentences of similar length. Natural academic writing typically shows more variation.

2. **Systematic "honesty" disclaimers.** The phrases "Important caveat:", "This is the weakest link", "We emphasize that this is not a detection", and "We therefore treat X as a hypothesis" appear at regular intervals. While scientifically commendable, the systematic placement of these disclaimers reads like AI-generated self-criticism — the paper seems to preemptively address every possible criticism in a checklist-like manner.

3. **Enumeration-heavy structure.** The Introduction enumerates 4 types of prior mechanisms (quintom, DM-DE interaction, Horndeski, coupled quintessence). The cover letter enumerates 4 novelty claims. The Discussion enumerates 3 limits of a_c². This pattern, while common in AI-generated text, is also common in physics papers — flag is preliminary only.

4. **Predictable transition phrases.** "In this paper, we provide...", "The structure of this paper is as follows...", "This framework differs from prior mechanisms in several respects." These are neutral but form a recognizable template.

5. **Repetitive emphasis.** The main text uses \emph{} 21 times for emphasis, which is unusually frequent and creates a hectoring tone.

**Note:** These are preliminary observations for the AI-writing detection phase. The primary scientific issues detailed above are independent of the writing style.

---

## Summary of Issues

### FATAL (must fix or reject)

| # | Location | Description | Why FATAL |
|---|---|---|---|
| F1 | Main text Eq. (5); SM Eq. (3) vs. SM §1.2 derivation | The Langevin equation in the main text is NOT the equation derived from the Lindblad master equation. It differs by: (a) missing factor of i in the drive term, (b) missing ⟨σ_z⟩ = 1-2\|A\|² factor in the drive (self-limiting feedback), (c) different functional form of the coherent term. The two forms match only at \|A\|² = a_c², but the model is used globally over 0 < z < 2. | Core dynamical equation is incorrectly derived. All subsequent results (w(z), χ², phantom crossing) depend on this equation. |
| F2 | SM Table 2 + SM Table 3 vs. main text abstract and §5 line 188 | The P_coll driver's best-fit shows w(z) > -1 at all DESI bins and \|A\|²/a_c² < 1 everywhere. The paper's core claim — that the model predicts phantom crossing at z ~ 0.5-1 — is contradicted by the SM's own data for the primary (P_coll) driver variant. | Core qualitative claim is falsified by the paper's own quantitative results. The main text, SM, and cover letter are three-way inconsistent on the central prediction. |
| F3 | SM §2.2 | Derivation of dynamical a_c² is missing critical algebraic steps. The reader cannot verify that the claimed result follows from the stated equations. The derivation uses a_c² in the ODE to derive a corrected a_c², with equilibrium and dynamical versions not clearly distinguished. | Key parameter a_c² — which appears in the Langevin equation and the w(z) relation — has an unverifiable derivation. |
| F4 | Cover letter line 18 vs. main text §5 | Cover letter claims "derived (not fitted) parameters." ω_0 and γ are fitted to DESI data. a_c² is an algebraic function of fitted parameters, not an ab initio prediction. | Misrepresentation of the model's empirical status. Claimed microscopic derivation is actually phenomenological fitting. |

### MAJOR (must address)

| # | Location | Description |
|---|---|---|
| M1 | Main text Eq. (7) | w(z) = -1 + κ(a_c² - \|A\|²) is ad hoc. The general function F(\|A\|²) is never specified, so the linear approximation error cannot be quantified. |
| M2 | Not discussed | High-z limit: as z → ∞, f(z) → 0, \|A\|² → 0, w → -1 + κ a_c² ≠ -1. This contradicts ΛCDM at early times and the model's own premise. |
| M3 | SM §3.3 | Non-standard halo formation rate formula. Should cite Lacey & Cole (1993) and Sasaki (1994) and derive or reference the standard EPS formation rate. |
| M4 | SM Table 2 | a_c² differs by factor ~2 between P_coll and SFR drivers (0.28 vs. 0.15), contradicting its status as a microscopic (driver-independent) parameter. |
| M5 | Main text §1, §5 | All figures marked "to be included." Submission is incomplete — referee cannot evaluate figure-dependent claims. |
| M6 | Main text §5 line 165 | Quantitative comparison uses binned data from non-parametric reconstructions, not the official DESI DR2 likelihood. Δχ² is indicative only. |
| M7 | Main text §5 | χ² improvement is driven almost entirely by a single data point (z=0.25, contributing 5.44 of ΛCDM's 5.69 χ²). Not a genuine model preference. |
| M8 | Main text §5 | No error estimates on best-fit parameters (ω_0, γ). Parameter degeneracies not quantified. |
| M9 | Main text §4 line 140 | Calibrating to CPL-extrapolated w_0 = -0.785 for a non-CPL model is methodologically inconsistent. |
| M10 | Main text bibliography | Three ghost citations: Mishra:2026, Zhao:2009, Martineau:2005 appear in bibliography but are never cited in the text body. |
| M11 | Main text bibliography | Missing references: Lacey & Cole 1993, Sasaki 1994 (halo formation rate); Breuer & Petruccione (open quantum systems); small-scale quantum Ising simulation experiments. |
| M12 | Main text bibliography | DGF:2024 is an unpublished internal note. Either publish it or remove the citation. |
| M13 | Main text §6 | Testable predictions are qualitative, not quantitative. No specific numerical range for z_cross or w_a with DESI DR3 forecast uncertainties. |
| M14 | SM Table 1 | Factor-of-2 variation in driving function between halo mass function variants at z=2 challenges the "robustness" claim. |
| M15 | Main text → SM | Main text never references the Supplemental Material document. The two are not integrated. |

### MINOR

| # | Location | Description |
|---|---|---|
| m1 | Main text line 79 | The γ ≫ ω_0 limit (a_c² → 0) makes the ODE singular — not addressed. |
| m2 | Cover letter | Does not mention journal-specific submission requirements. |
| m3 | Bibliography | Inconsistent arXiv identifier formats (old vs. new). |
| m4 | Main text Eq. (4) | Boxed equation formatting is unusual for PRD. |
| m5 | Main text (throughout) | Excessive use of \emph{} for emphasis (21 instances) — hectoring tone. |
| m6 | SM §1.2 | Gaussian decoupling approximation and 1/N negligibility claim not mentioned in main text. |
| m7 | Main text line 115 vs. SM §3 | Main text says M_min uncertainty is "~14 orders of magnitude"; SM varies it over only 6 orders of magnitude. |
| m8 | SM | SM has no independent reference list. |

---

## Overall Assessment

This paper attempts something genuinely novel: connecting quantum many-body physics to late-time cosmology through an information-theoretic bridge. The scientific ambition and the honesty about limitations are commendable. However, the execution has fatal flaws that make the manuscript unsuitable for publication in its current form.

The most serious problem is that the paper's core dynamical equation (the complex Langevin equation, Eq. 5) is not correctly derived from the stated microscopic starting point (the Lindblad master equation). The equation presented in the main text is a simplified form that is valid only at a single point (|A|² = a_c²), but the model is applied over a range where this approximation fails. All subsequent results — the w(z) predictions, the χ² comparison, the phantom crossing mechanism — depend on this equation.

Compounding this, the paper's flagship quantitative result (P_coll driver as the "more fundamental" improvement) does not actually produce the qualitative phenomenon it claims (phantom crossing). The SFR driver shows crossing; the P_coll driver does not. This is not a minor numerical discrepancy — it is the central prediction of the paper being absent from its primary model variant.

The paper also contains several issues that individually would require major revision: ad hoc w(z) relation, incomplete derivation of a_c², ghost citations, reliance on non-official DESI data products, missing figures, and exaggeration in the cover letter.

I recommend MAJOR REVISION (bordering on REJECT). The authors must:
1. Correctly derive the Langevin equation from the Lindblad master equation and use the correct form globally, or prove that the simplified form is an adequate approximation with quantified error bounds.
2. Reconcile the P_coll driver results with the claimed phantom crossing — either the P_coll driver must show crossing, or the paper must honestly state that only the SFR driver (which the paper claims to improve upon) produces the claimed effect.
3. Provide a complete derivation of the dynamical a_c² with all algebraic steps shown.
4. Include all figures.
5. Remove ghost citations, replace the DGF:2024 internal note, and add missing references.
6. Either calibrate to a model-independent w(z=0) measurement or justify the CPL extrapolation.
7. Provide quantitative testable predictions with error forecasts for DESI DR3.
8. Integrate the SM with the main text via explicit cross-references.
9. Remove or substantially qualify the "derived (not fitted)" claim in the cover letter.
