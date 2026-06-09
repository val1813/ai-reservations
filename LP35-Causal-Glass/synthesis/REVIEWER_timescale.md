# Nature Physics Referee Report — LP35-Causal-Glass (Timescale Variant)

**Manuscript under review:** Hypothesis that "phantom dark energy behavior is a phase transition signal arising when the universe's deceleration-to-acceleration switch causes causal structure to freeze, producing w(z) asymmetry about z~0.7 with sharp phantom dip and slow relaxation toward -1."

**Reviewer stance:** Fundamental skepticism — every claim presumed unsupported until independently verified. I have cross-checked the cited claims against the actual DESI DR2 publications and the extant literature on cosmological phase transitions, causal structure, and dark energy reconstruction.

**Date:** 2026-06-08

---

## OVERALL RECOMMENDATION: REJECT

**Reason in one sentence:** The manuscript's core conceptual mechanism was published 19 years ago in JCAP (She 2007), its key observational claim (w = -1.48 at z~0.9) does not appear in the cited source, the term "causal graph freezing" has zero precedent in the cosmological literature, no equation connects expansion kinematics to w(z), and the proposed "asymmetric phantom dip" prediction is a 2-parameter description of 4 data points that CPL(w0,wa) already captures with equal or fewer free parameters.

---

## GATE 1: CITATION FABRICATION (引用虚构)

### Finding 1.1: The claimed DESI DR2 value w = -1.48 at z~0.9 is unattested

C1 states: "DESI DR2's w(z) reaches phantom deepest at z~0.9 with w ≈ -1.48." I have searched the published DESI DR2 papers (arXiv:2503.14738, Results II; arXiv:2503.14743, Extended DE Analysis) and the leading binned reconstruction follow-up (Li & Wang, arXiv:2506.22953). None of these papers reports w = -1.48 at any redshift.

What the DESI DR2 papers actually say:
- The CPL fit prefers (w0 > -1, wa < 0) at 2.8-4.2 sigma depending on dataset combination (2503.14738).
- Non-parametric binned reconstructions show "deviations from the cosmological constant reaching at least 2.13 sigma" (Li & Wang 2506.22953).
- The extended analysis (2503.14743) states there is "a clear preference for models that feature a phantom crossing" but immediately qualifies: "alternatives lacking this feature are disfavored, they cannot yet be ruled out."
- Mishra (arXiv:2605.27301, 2026) explicitly warns that "the statistical significance of these trends remains limited" and that "effective phantom behaviour does not necessarily imply the existence of a fundamental phantom field."

The specific value w = -1.48 at z~0.9 appears to come from a 4-bin reconstruction with error bars large enough that w = -1 is within 1-2 sigma of every bin. Presenting this as an established measurement rather than a low-significance bin with large uncertainties is a material misrepresentation of the cited source.

**Verdict: GATE 1.1 — FAIL.** The central observational anchor of the paper (C1) is not supported by the cited source at the claimed precision.

### Finding 1.2: "Causal graph freezing" has zero precedent in the peer-reviewed literature

The manuscript's core physical mechanism uses the term "causal graph freezing" and presents it as a cosmological phase transition. I have searched arXiv, INSPIRE-HEP, and the ADS abstract service for the following terms:
- "causal graph freeze" / "causal graph freezing" in cosmological context: **zero results**
- "causal structure phase transition cosmic expansion": no results matching the claimed mechanism
- "P_reflux" as a cosmological quantity: **zero results outside the authors' own DGF/CEP framework**

The closest existing concepts are:
1. **Causal set theory** (Bombelli, Lee, Meyer & Sorkin 1987; Rideout & Sorkin, PRD 61, 024002, 2000): the sequential growth dynamics of causal sets, where elements can only be added ("0 to 1"). This is a quantum gravity program with decades of literature — none cited.
2. **The w-w' "freezing" classification** (Caldwell & Linder, PRL 95, 141301, 2005): a phenomenological classification of scalar field dark energy based on whether the field evolution slows ("freezes") or accelerates ("thaws"). This has nothing to do with causal graphs.
3. **Cosmological horizon as a causal boundary**: standard Friedmann cosmology, not a novel phase transition mechanism.

If the authors are introducing a genuinely new concept ("causal graph freezing as a phase transition driven by expansion overtaking causal exploration"), they must present it as a hypothesis requiring independent definition — not as an established framework with literature support. The manuscript's tone implies this framework exists; it does not.

**Verdict: GATE 1.2 — FAIL.** The core conceptual framework rests on terminology invented by the authors that has no grounding in the existing literature. Where the literature does exist (causal set theory), it is not cited.

### Finding 1.3: "AG thermal activation all variants falsified" presented as established fact

C4 claims that "AG thermal activation all variants are falsified — C[G] freezing cannot be Cooling, must be Quench." This is presented as a settled result. In reality:
- The Adam-Gibbs relation has been studied and empirically validated across 60 years of glass physics (Ngai, J. Phys. Chem. B 1999; Starr et al., J. Chem. Phys. 2013; MRS Bulletin 2025 review issue).
- The specific cancellation argument (that N_coop cancels in the relaxation exponent) depends on a particular assumption about the prefactor A = k_B * T_eff * N_coop * ln 2, which is not the general form of AG modifications (Ngai 1999; the coupling model modifies this prefactor differently).
- The authors have derived a consequence of their own assumption about A and then presented it as a falsification of AG — this is circular. AG is not falsified; one specific parameterization of AG is shown to be incompatible with the authors' model, assuming their other premises hold.

This is a category error: deriving that your own model's assumptions exclude a certain parameter regime of an established theory does not constitute falsification of that theory.

**Verdict: GATE 1.3 — FAIL.** Self-consistency within the authors' framework is presented as external falsification of a 60-year-old theory.

### Gate 1 Summary: FAIL on three independent grounds.

---

## GATE 2: PRIOR ART CONFLICT (先发冲突)

### Finding 2.1: She (2007), JCAP 02, 021 — FATAL PRIOR ART

**Jian-Huang She, "An Accelerating Universe Emergent from the Landscape," JCAP02(2007)021, arXiv:hep-th/0702006.**

This paper, published 19 years ago in a peer-reviewed IOP journal, already proposed:

| This Manuscript's Claim | She (2007) Precedent |
|---|---|
| C[G] landscape non-ergodicity in expanding universe | "The universe exists in a quantum glass state" with "extremely large effective viscosity slowing long-distance dynamics" |
| Causal structure freezing at cosmic horizon | "Glass transition point = location of cosmic horizon where viscosity diverges" |
| Λ emerges from glassy/structural dynamics | "Cosmological constant problem solved: Λ ~ 10^{-120} is not fine-tuning but extreme slowing" |
| Freezing is structural (quench), not thermal | "Dynamical arrest" at horizon, "separation of time scales" for short vs long distance dynamics |
| Landscape + expansion → glassy freezing | "Landscape suggests quantum glass → slowing → explanation for slow-roll and dark energy" |

She (2007) has been cited only once on Semantic Scholar — it is obscure but definitively published. The manuscript under review neither cites it nor provides a structured differentiation from it. The internal FINAL_CLOSURE.md acknowledges this conflict (Section 五: "She(2007)先发 — 必须引用为 'landscape→glass→Λ' 概念链首发作, 明确区分粘度vs淬火机制"), but the manuscript itself does not.

Under *Nature Physics* editorial policy, failure to cite and distinguish from pre-existing published work that anticipates the core conceptual claims constitutes grounds for rejection regardless of other merits.

**Verdict: GATE 2.1 — FAIL. Fatal prior art. The concept "landscape → glassy freezing at horizon → explains Λ" was published in JCAP in 2007.**

### Finding 2.2: Kibble-Zurek mechanism in cosmology — competitive framework

The Kibble-Zurek mechanism (KZM) provides a well-established framework for understanding phase transitions in expanding/cooling systems where causality limits the propagation of symmetry-breaking information. Del Campo, Kibble & Zurek (J. Phys.: Condens. Matter 25, 404210, 2013) explicitly analyze how "causality" and "the competition between inherited and spontaneous symmetry breaking" determine the density of topological defects in cosmological phase transitions, with the key parameter being the ratio of front propagation velocity to sound speed.

The manuscript's claim that "causal structure cannot keep up with expansion, producing stress that manifests as phantom w(z)" is conceptually isomorphic to KZM's central insight: when the quench rate exceeds the system's causal relaxation rate, non-equilibrium structures (defects/stress) freeze in. The KZM gives a quantitative prediction for defect density as a power law in quench rate with universal critical exponents. The manuscript gives no comparable quantitative prediction.

The difference is that KZM is a rigorous framework with testable power-law predictions and verified laboratory analogs (cold atoms, liquid crystals, spin ices — Fan, Del Campo & Chern 2023). The manuscript's "causal graph freezing" has no such rigor.

**Verdict: GATE 2.2 — FAIL. A competing framework (KZM) already provides a quantitative, experimentally tested account of how causality limits phase transitions in expanding systems. The manuscript does not engage with it.**

### Finding 2.3: The w-w' "freezing/thawing" classification — terminology conflict

Caldwell & Linder (PRL 95, 141301, 2005) introduced the "freezing" vs "thawing" classification of dark energy models in the w-w' plane. While this is a different concept from the manuscript's "causal graph freezing," the reuse of the term "freezing" in a dark energy context — without acknowledgment, differentiation, or citation — creates confusion and fails to situate the work in the existing literature.

**Verdict: GATE 2.3 — MINOR. Not fatal alone, but compounds the pattern of failure to engage with existing concepts.**

### Gate 2 Summary: FAIL. Fatal prior art from She (2007), plus failure to engage with KZM cosmology.

---

## GATE 3: LOGIC CHAIN RUPTURE (逻辑断裂)

### The claimed chain:

```
Deceleration→acceleration transition (z≈0.7)
    → "Time runs faster than matter"
    → Causal graph freezes
    → Irreversible phase transition (P_reflux → 0)
    → Non-monotonic w(z): sharp phantom dip + slow relaxation to -1
```

### Finding 3.1: Step 1→2 is a metaphor, not a physical equation

"Time runs faster than matter" is not a statement derivable from the Friedmann equations. In FLRW cosmology, cosmic time t is the proper time of comoving observers — it does not "run faster" or "slower" relative to matter. The deceleration-to-acceleration transition is defined by d^2a/dt^2 changing sign, which is a property of the scale factor's second derivative, not of "time" relative to "matter."

There is no equation in the manuscript that translates the condition d^2a/dt^2 > 0 (acceleration) into a statement about causal connectivity. The particle horizon continues to grow monotonically through the acceleration transition: R_ph = a(t) * integral_0^t dt'/a(t'). While the event horizon exists only during acceleration (d^2a/dt^2 > 0), the particle horizon — which determines causal connectivity — never shrinks.

**The central physical image is false at the level of standard FLRW cosmology.** The particle horizon does NOT "freeze" at z≈0.7. It continues to grow. Causal connections are never "severed" by the onset of acceleration; they are merely added more slowly.

**Verdict: GATE 3.1 — FAIL. The proposed mechanism contradicts the basic behavior of the particle horizon in ΛCDM cosmology.**

### Finding 3.2: Step 2→3 ("causal graph freezes" → "irreversible phase transition") assumes what it needs to prove

The claim that a change in the rate of causal connection addition constitutes an "irreversible phase transition" with a well-defined order parameter (P_reflux → 0) requires:
1. A definition of the phase (what are the two phases?)
2. An order parameter that is computable from cosmology
3. A demonstration that the order parameter changes discontinuously or with a diverging susceptibility at the transition

None of these are provided. P_reflux is defined within the authors' own DGF framework, has no independent operational definition, and its mapping to observable w(z) is asserted rather than derived (see also Gate 4).

**Verdict: GATE 3.2 — FAIL. The existence of a phase transition is asserted, not demonstrated.**

### Finding 3.3: Step 3→4→5 ("phase transition" → "phantom dip" → "asymmetric relaxation") has no dynamical equation

Even if one grants the existence of a phase transition at z~0.7, the manuscript provides no Lagrangian, no field equation, no effective action, and no stress-energy tensor modification that would produce w(z) < -1 at z~0.9 and w(z) > -1 at z~0. This is pure phenomenology dressed as mechanism.

The comparison to C5's claim is instructive: the manuscript asserts it makes a "unique prediction" distinguishing it from all other models. But a prediction that comes with no equation from which it can be derived is not a prediction — it is a qualitative story that can be adjusted to fit whatever data appears.

**Verdict: GATE 3.3 — FAIL. The claimed "unique prediction" is not derivable from any equation in the manuscript.**

### Gate 3 Summary: FAIL on all three steps. The logic chain is a sequence of metaphors without equations.

---

## GATE 4: MAGNITUDE PARADOX (量级悖论)

### Finding 4.1: The energy scale of the claimed mechanism is vanishingly small

The physical mechanism proposed is: the expansion of the universe (characterized by H) overtakes the "causal exploration rate" (characterized by some velocity v_causal). At the transition z~0.7:
- H(z=0.7) ≈ H_0 * sqrt(Ω_m*(1+z)^3 + Ω_Λ) ≈ 70 * sqrt(0.3*1.7^3 + 0.7) ≈ 100 km/s/Mpc
- In natural units: H(z=0.7) ≈ 10^-33 eV
- The causal "stress" energy density associated with this mismatch would scale as H^2 * M_Pl^2 in the most optimistic dimensional analysis

The observed phantom signal Δw ≈ 0.5 (from w≈-1 to w≈-1.48 at the dip) corresponds to an additional dark energy density of Δρ_DE ~ (0.5) * Ω_DE * ρ_crit ~ 0.35 * (3H_0^2/8πG) ~ 10^-47 GeV^4, or equivalently an energy scale of ~10^-3 eV for the dark energy density.

The causal mismatch energy scale: if we estimate the "energy cost" of a frozen causal edge as ~1/L_horizon ~ H ~ 10^-33 eV, then N ~ (H_0 * t_0)^3 ~ 10^3 edges in the current Hubble volume gives total "causal stress" energy ~ 10^-30 eV. This is **33 orders of magnitude too small** to account for Δw ≈ 0.5.

The manuscript provides no amplification mechanism. A phase transition can produce order-1 effects on the order parameter, but only if the free energy difference between phases is of the same order as the observed effect. There is no calculation of the free energy of the "causal glass transition."

**Verdict: GATE 4.1 — FAIL. A back-of-envelope estimate suggests the causal mismatch energy scale is ~30+ orders of magnitude too small to drive Δw ≈ 0.5.**

### Finding 4.2: The "timescale" argument fails dimensional analysis

The manuscript's core intuition — "time runs faster than matter" at z~0.7 — compares two quantities with different dimensions:
- The expansion timescale: t_expand = 1/H ~ 10^10 years at z~0.7
- The "causal exploration timescale": undefined in the manuscript

For a meaningful comparison, both quantities must be timescales with the same dimensionality. The manuscript does not define τ_explore in terms of cosmological observables, making the claimed "crossover" at z~0.7 an assertion without dimensional foundation.

**Verdict: GATE 4.2 — FAIL. The central timescale comparison is dimensionally undefined.**

### Gate 4 Summary: FAIL. The proposed mechanism is energetically impossible without an amplification mechanism that is neither provided nor plausibly sketched.

---

## GATE 5: FATAL ALTERNATIVE EXPLANATION — CPL SUFFICIENCY

### Finding 5.1: CPL(w0, wa) captures all current data with fewer assumptions

The DESI DR2 cosmological constraints paper (2503.14738, PRD 112, 083514, 2025) reports that CPL(w0, wa) provides a better fit than ΛCDM at 2.8-4.2σ significance depending on dataset combination. The preferred solution is w0 > -1, wa < 0, corresponding to quintessence at low z crossing to phantom at higher z.

The manuscript proposes a "causal glass" mechanism requiring:
- A "causal graph" with undefined vertex set and edge dynamics
- A "phase transition" with undefined order parameter
- A "freezing" mechanism requiring at least 2 uncalibrated parameters (coupling constant γ between causal stress and w, and the freeze threshold Φ_q)
- A mapping from "causal freeze stress" to Δw that has no field equation

CPL requires: w0, wa (2 parameters).

Occam's razor: CPL wins. The manuscript's framework introduces conceptual complexity (causal graphs, phase transitions, P_reflux, quench dynamics) without improving the fit to data. The claimed "unique prediction" — asymmetry of w(z) about z~0.7 with sharp phantom dip — is:
1. Described qualitatively, not quantitatively (what is the predicted value of dw/dz at z=0.7?)
2. Not unique: any model with a preferred redshift (e.g., where DE begins to dominate) can produce asymmetric w(z)
3. Not yet tested against data beyond the 4 bins it was designed to explain

### Finding 5.2: The "prediction" is a postdiction fitted to 4 data points

The manuscript's C5 prediction — "sharp phantom dip + slow relaxation" — is inferred from exactly 4 DESI DR2 binned w(z) data points. A 2-parameter function (dip depth, relaxation rate) fitted to 4 data points leaves 2 degrees of freedom — the same as CPL. There is no predictive content here beyond what CPL already provides.

The claimed testability with "Euclid DR1's 8-10 bins" is a promissory note: any model can promise future distinguishability. The question is whether the model is falsifiable with current data, and the answer is no — because the model has enough adjustable parameters (dip depth, dip location, relaxation rate, asymptotic w_inf) to fit any smooth w(z) that crosses -1.

**Verdict: GATE 5.1 — FAIL. CPL(w0, wa) fits the data with 2 parameters and fewer assumptions. The manuscript adds conceptual overhead without statistical improvement.**

**Verdict: GATE 5.2 — FAIL. The claimed "prediction" is a postdiction with 4 parameters fitted to 4 data points.**

### Gate 5 Summary: FAIL. CPL is the simpler, sufficient explanation.

---

## SYNTHESIS AND FINAL JUDGMENT

### Crossing pattern of failures

| Gate | Finding | Severity | Independent of other gates? |
|------|---------|----------|---------------------------|
| G1.1 | DESI w=-1.48 not in cited source | FATAL | Yes — observational basis is false |
| G1.2 | "Causal graph freezing" not in literature | FATAL | Yes — conceptual framework is invented |
| G1.3 | AG falsification is circular | MAJOR | Yes |
| G2.1 | She (2007) prior art | FATAL | Yes — published 19 years ago |
| G2.2 | KZM competitive framework | MAJOR | Yes |
| G3.1 | Particle horizon does not freeze | FATAL | Yes — contradicts basic FLRW |
| G3.2 | Phase transition asserted, not derived | FATAL | Yes |
| G3.3 | No dynamical equation for w(z) | FATAL | Yes |
| G4.1 | Energy scale mismatch (~30 orders) | FATAL | Yes |
| G4.2 | Dimensional analysis failure | MAJOR | Yes |
| G5.1 | CPL is simpler and sufficient | FATAL | Depends on G1.1 |
| G5.2 | Prediction is a postdiction | FATAL | Depends on G1.1 |

**Five gates. Each independently fatal. No single fix addresses more than one.**

### What would be minimally required for Major Revision

Even if the authors were to correct all observational misrepresentations and cite She (2007) with explicit differentiation, the following structural problems would remain:

1. **No dynamical equation.** Cosmology papers that claim to "explain" w(z) must provide a Lagrangian, field equation, or effective action from which w(z) can be computed. The manuscript has none.

2. **Energy scale problem.** An amplification mechanism spanning ~30 orders of magnitude is not a detail — it is the entire physical content of the model. Without it, the mechanism is energetically impossible.

3. **FLRW contradiction.** The particle horizon grows monotonically. The claim that causal connections are "severed" at z~0.7 is contradicted by the behavior of a(t)*integral(dt/a) in ΛCDM.

These three problems cannot be fixed by revision. They require an entirely new physical theory — one that the authors acknowledge they do not have (internal GAP_ANALYSIS.md: Step 2 and Step 5 marked as "⛔⛔⛔" with the note "需要新的物理理论").

### The honest path forward

The authors' internal documents acknowledge the gaps honestly:
- GAP_ANALYSIS.md labels Steps 2 ("d^2SFR/dz^2 → decoherence") and Step 5 ("P_reflux → w") as ⛔⛔⛔ structural gaps requiring "quantum gravity or holographic derivation"
- TIMESCALE_HYPOTHESIS.md lists under "当前局限": "从'时间-物质脱耦'到w(z)的具体函数形式尚未推导——目前只有物理图像"
- UNIFIED_HYPOTHESIS.md acknowledges under "诚实声明": "α和β尚未从第一原理推导"

These honest internal assessments are in direct tension with the manuscript's presentation of C1-C6 as "conclusions." A paper whose internal gap analysis admits that the two central steps in the derivation chain require a new theory of quantum gravity cannot simultaneously claim to have explained phantom dark energy.

**A publishable paper could be written from this material** — but it would be a speculative 2-page hypothesis paper in a venue like *Physical Review D Brief Report* or as a Letter, titled something like "A Causal Glass Interpretation of the DESI Phantom Crossing Preference," where:
- The She (2007) prior art is cited and differentiated
- All claims are explicitly qualified as speculative
- The observational claim is accurately stated (2-4σ preference, not discovery)
- The model is presented as a conceptual framework awaiting quantitative development, not as an explanation

That is not the manuscript under review.

### Final recommendation

**REJECT.**

The manuscript fails all five independent rejection gates. The failures include fatal misrepresentation of cited data (G1.1), fatal prior art conflict with a published JCAP paper (G2.1), a core physical mechanism that contradicts basic FLRW cosmology (G3.1), an energy scale mismatch of ~30 orders of magnitude (G4.1), and a failure to improve upon the 2-parameter CPL model (G5.1).

Each of these failures alone would justify rejection. Together, they indicate that this work is not ready for peer-reviewed publication in any form resembling the current manuscript.

---

*This report reflects my independent assessment as an anonymous referee. I have no competing interests with the authors and have not collaborated with them.*
