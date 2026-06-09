# Nature Physics — Anonymous Referee Report

**Manuscript:** "Causal Freeze: Why Dark Energy Must Return to w=-1"
**Referee Stance:** Fundamental skepticism
**Date:** 8 June 2026

---

## OVERALL VERDICT: REJECT

The manuscript attempts a bold claim — that the dark energy equation of state w(z) *must*, as a consequence of causal structure in an expanding universe, exhibit a single phantom dip and then exponentially relax back to w=-1. The conclusion is presented as a derivation from first principles, not a fit. This is a claim that, if true, would be of exceptional importance to cosmology.

I regret to report that the manuscript does not meet the standards for publication in Nature Physics, nor in any reputable physics journal in its current form. The problems are not peripheral or fixable by minor revision; they strike at the core of every link in the paper's argument chain. I detail my findings below along five independent axes, plus one additional critical finding.

---

## ATTACK 1: CITATION FABRICATION — FATAL

**Question:** Do "C[G] landscape" and "causal graph" exist as established concepts in the cosmological literature? Who proved the N_coop cancellation in Adam-Gibbs theory applied to cosmology?

**Finding:**

1. **"C[G] landscape" is undefined and unattested.** No reference in the cosmological literature uses this term. The string landscape is an established concept (Bousso-Polchinski, KKLT, etc.), and there is exactly *one* paper that connects glass transition physics to the cosmological landscape: She (2007), "Accelerating universe emergent from the landscape," JCAP 0702:021 [hep-th/0702006]. This paper is not cited in the present manuscript. The She paper already (a) applies glass transition physics to cosmology, (b) identifies a glass transition point with the cosmic horizon, (c) uses the landscape as the energy surface, and (d) reconstructs a de Sitter-like metric from the glassy dynamics. The author's "C[G] landscape" appears to be a novel notation for the same conceptual space, but without citation to the existing work. If "C[G]" denotes something different or extends the She framework, the paper must say so explicitly and cite the prior work.

2. **"N_coop exact cancellation" is unverified.** The Adam-Gibbs (AG) relation is a 1965 theory of molecular glass formers in condensed matter physics. Its application to cosmology was first proposed by She (2007, op. cit.). The present manuscript asserts that in a "C[G] landscape," N_coop (the cooperatively rearranging region size) undergoes an *exact cancellation* in the AG exponential, yielding τ_α ≈ τ_0. This is a specific mathematical claim. Who proved it? Under what assumptions? What is the configuration entropy in the cosmic context — the entropy of causal patches? The She paper does not claim this; standard AG theory in condensed matter certainly does not. The paper provides no derivation and no citation. This is not scholarship; it is invention presented as established fact.

3. **"Causal graph" in the specific sense used here does not appear in the cosmology literature.** The term "causal graph" exists in causal set theory (Sorkin, Rideout, et al.) where it refers to a discrete partial order of spacetime elements, and in Pearl's causal inference framework. The present manuscript's usage — a graph whose nodes are "causal regions" and whose edges are "light-cone connections that evolve under expansion" — defines a novel construct. Novel constructs are permissible, but they must be defined rigorously and situated relative to existing literature. Neither is done here.

**Severity: FATAL.** The paper's foundation rests on three terms that are either entirely novel without definition, or borrowed from one subfield and applied to another without acknowledging prior art or providing the mathematical bridge. A paper claiming "derivation" cannot proceed when its own starting vocabulary is unattested.

---

## ATTACK 2: PRIOR ART CONFLICT — MAJOR

**Question:** Has anyone already published a similar argument — that w(z) is derivable from first principles and must return to w=-1?

**Finding: Yes, multiple times.**

1. **Zhao, Zhang, and Tong (2009), "Quantum Yang-Mills Condensate Dark Energy Models" [arXiv:0909.3874].** From the abstract: "In the late stage, w_y naturally runs to the critical state with w_y = -1... These characters are independent of the choice of the initial condition, and the cosmic coincidence problem is avoided." The YMC model derives w(z) behavior from quantum field theory — the effective Yang-Mills Lagrangian is "completely determined by the quantum field theory, there is no adjustable parameter in the model except the energy scale." This is a genuine derivation from first principles, published 17 years before the present manuscript, making essentially the same claim with actual QFT backing. The manuscript does not cite it.

2. **She (2007), "Accelerating universe emergent from the landscape" [hep-th/0702006, JCAP 0702:021].** As discussed under Attack 1, this paper already proposed that the accelerating universe emerges from a glass transition in the string landscape. It predates the present manuscript by 19 years and uses the same conceptual machinery (landscape, glass transition, configurational entropy) applied to cosmology. The manuscript does not cite it.

3. **Smirnov (2025), "Dynamical Dark Energy Emerges from Massive Gravity" [arXiv:2505.03870].** A healthy, self-consistent theory that accommodates phantom dark energy with a "technically natural, small asymptotic cosmological constant" — meaning the return to w=-1 is derived from massive gravity, not fit. Published 1 year before the present manuscript. Not cited.

4. **Multiple post-DESI-DR2 models (2025-2026).** Since DESI DR2 reported evidence for dynamical dark energy, the literature has exploded with models proposing specific physical mechanisms: interacting dark energy (Figueruelo et al. 2026, van der Westhuizen et al. 2025), scalar-tensor modified gravity (Efstratiou et al. 2025), braneworld models (Mishra, Sahni et al. 2025), and coupled quintessence (Antusch et al. 2026). The manuscript's claim of being the *only* model that "derives" rather than "fits" the w(z) shape is demonstrably false. The YMC model (2009) derived it. She (2007) derived a framework for it. Smirnov (2025) derived it from a specific gravity theory.

The manuscript's rhetorical strategy of dismissing all field-theoretic models as "fitting" while claiming its own "derivation" status is not supported by the literature.

**Severity: MAJOR.** The paper is not the first to claim a derivation of w→-1 from first principles. It is, at best, the latest in a 19-year line of such claims, but it is unclear what it adds beyond prior work — especially given that the prior work is grounded in established physics (QFT, massive gravity, string theory) while the present manuscript invents its own framework.

---

## ATTACK 3: LOGIC GAPS — FATAL

**Question:** From "AG thermal activation is falsified" to "w(z) has exactly one phantom dip" — how many steps are skipped? Why does Φ_q crossing 1 produce a phantom dip rather than a quintessence bump?

**Finding: The logical chain has multiple non-sequiturs.**

1. **AG falsification → Quench.** The paper argues that AG thermal activation cannot produce causal freezing, therefore freezing *must* be a quench (landscape expansion > exploration). But this is a false dichotomy. The argument only shows that one specific mechanism (AG thermal activation, which itself has not been shown to apply to cosmology) fails. It does not exclude other non-quench mechanisms: quantum tunneling between vacua, dynamical attractors in field space (as in the YMC model), entropy production in the dark sector, or any of the dozens of field-theoretic mechanisms already in the literature. The logic is: "I proved mechanism A doesn't work, therefore it must be mechanism B." This is valid only if A and B are proven to be the only possible mechanisms — a claim neither made nor supported.

2. **Causal edge monotonicity → Φ_q monotonicity.** The paper asserts: "Causal edges can only be added, not deleted (GR: spacelike → timelike is irreversible) → Φ_q is monotonically increasing → freezing is irreversible." This chain conflates two different notions. The irreversibility of spacelike-timelike conversion in an expanding FLRW universe is a statement about the global causal structure — once two worldlines enter each other's particle horizon, they cannot leave it (in standard cosmology). But this does not imply that the *rate of landscape exploration* is monotonic. The "causal graph" has a fixed expansion rate (set by H(z)), but τ_explore — the time to explore new vacua — could increase, decrease, or oscillate depending on the landscape topology, independent of the monotonic addition of causal edges. A graph can grow its nodes while the search algorithm on that graph can slow down or speed up. The proof of monotonicity requires an additional assumption about the relation between graph growth and search efficiency that is not provided.

3. **Φ_q > 1 → phantom dip specifically.** This is the central non-sequitur. Φ_q > 1 means the landscape exploration timescale exceeds the expansion timescale — the system is "quenched." In condensed matter, a quench can produce *either* an undershoot or an overshoot depending on the sign of the order parameter and the shape of the free energy landscape. The paper asserts that the cosmic quench produces w < -1 (phantom), not w > -1 (quintessence). Why? The sign of the deviation from w = -1 depends on whether the frozen-in stress-energy corresponds to positive or negative kinetic energy in the effective dark energy fluid. The paper provides no derivation of this sign. It is simply asserted as "the phantom dip." Without this sign determination, the framework is equally consistent with *either* a phantom dip or a quintessence bump — meaning it predicts nothing.

4. **"Exactly one extremum."** The paper claims w(z) has "precisely one" phantom dip because the quench happens once. But why does the quench happen only once? Couldn't there be multiple epochs where τ_explore/τ_expand crosses 1 as the expansion rate H(z) changes through radiation, matter, and dark energy dominated eras? In fact, H(z) changes by orders of magnitude across cosmic history — the ratio of landscape exploration time to expansion time could easily cross 1 multiple times, producing multiple quench events. The "exactly one" claim is asserted without justification.

5. **Relaxation form: d(Δw)/dt = -λΔw.** After the quench, the paper claims exponential relaxation back to w = -1 with a single timescale λ. But relaxation in glassy systems is famously non-exponential (stretched exponential, Kohlrausch-Williams-Watts). Why should cosmic relaxation be purely exponential? This is an assumption, not a derivation. If the relaxation is stretched-exponential or power-law, the entire "three-sandwich" shape changes and may no longer match data.

**Severity: FATAL.** Of the five logical steps in the paper's core argument, four are non-sequiturs and one is an unjustified assumption. The paper does not establish a logical chain from premises to conclusion; it asserts a series of metaphors and treats them as derivations.

---

## ATTACK 4: MAGNITUDE PARADOX — FATAL

**Question:** τ_explore is never quantified. Without this number, what does the quench criterion actually predict?

**Finding: The paper's central quantity is undefined, making the theory unfalsifiable.**

The paper's own Section 4 (honest limitations) concedes: "τ_explore未定量推导(依赖图搜索效率c)." Translation: "τ_explore has not been quantitatively derived (depends on graph search efficiency c)."

This is not an honest limitation — it is a fatal omission. The entire predictive machinery of the paper depends on Φ_q = τ_explore/τ_expand crossing 1 at some redshift. Consider the possibilities:

- If τ_explore ≈ 10^100 years: Φ_q is always ≪ 1. No quench ever occurs. No phantom dip. The theory predicts w = -1 always — it reduces to ΛCDM.
- If τ_explore ≈ 10^{-100} seconds: Φ_q is always ≫ 1. The quench happened in the very early universe. The phantom dip occurred at z ≫ 10^6 and is completely unobservable. w = -1 today. Again, the theory reduces to ΛCDM.
- If τ_explore is comparable to the Hubble time at some interesting redshift: then the phantom dip could be observable. But the paper cannot compute this — it does not know τ_explore.

The paper effectively says: "Somewhere, at some redshift, for some reason, the quench happened, and it produced a phantom dip of some amplitude. The data happen to show a dip at z=0.87, so that must be where the quench happened." This is post-hoc reasoning disguised as prediction. The theory cannot *predict* the dip redshift because it does not know τ_explore. It can only *retrodict* it by fitting the data. This makes the paper exactly what it claims not to be: a fit, not a derivation.

Furthermore, the "graph search efficiency c" is not a parameter that appears in any known physical theory. What sets its value? The landscape topology? The tunneling amplitudes between vacua? The quantum coherence time of the wavefunction of the universe? Without defining c, τ_explore is not just unquantified — it is undefined.

**Severity: FATAL.** A theory whose central dynamical quantity is undefined is not a physical theory. It is a metaphor. The paper would need to derive τ_explore from independently measurable quantities (the string landscape statistics? the Hubble constant? the density of states of dark energy vacua?) to make any falsifiable prediction. In its current form, it makes none.

---

## ATTACK 5: FATAL ALTERNATIVE (CPL) — MAJOR

**Question:** The CPL parametrization (w0, wa) uses 2 parameters to fit all current data. Why does cosmology need this more complex "causal freeze" framework?

**Finding: CPL is simpler, more predictive, and grounded in standard cosmology.**

1. **Parameter count paradox.** The paper claims to be "simpler" because it derives rather than fits. But let us count the paper's effective parameters:
   - τ_explore normalization (undetermined)
   - Quench redshift z_q (not predicted, fitted from data)
   - Phantom dip amplitude Δw_max (not predicted, fitted from data)
   - Relaxation rate λ (not predicted, fitted from data)
   - The entire landscape graph topology (undefined)
   - "Graph search efficiency c" (undefined)
   
   This is *at minimum* 3-4 effective free parameters (z_q, Δw_max, λ, and some implicit normalization), and possibly many more when the landscape structure is accounted for. CPL uses exactly 2: w0 and wa. The causal freeze framework is not simpler; it is radically more complex with fewer constraints.

2. **Predictive power.** CPL makes a definite prediction: w(z) is monotonic in the variable z/(1+z). This means that if we observe w(z) at two redshifts, CPL predicts w(z) at all other redshifts. It is falsifiable. The causal freeze framework says: "w(z) has exactly one phantom dip. We don't know where. We don't know how deep. We don't know how fast it relaxes." This is not falsifiable. If DESI had found monotonic w(z), the paper could claim the dip is at z > 2 (unobservable). If Euclid finds no dip, the paper could claim it's at z > 5. The theory can accommodate any data by adjusting parameters that it cannot compute from first principles.

3. **CPL already fits the data.** The DESI DR2 results, combined with CMB and SNIa, show a preference for dynamical dark energy at ~3σ using CPL. The paper provides no evidence that its "causal freeze" fits the data better than CPL. In fact, it provides no statistical comparison at all. Without showing Δχ² or ΔAIC/BIC relative to CPL, there is no reason to prefer the more complex model.

4. **What does the paper add?** CPL says w(z) evolves. That is already known from DESI DR2. The paper says w(z) *must* evolve in a specific shape, but cannot predict the parameters of that shape. What new observable consequence does the paper provide that CPL does not? The paper's one novel claim (exactly one extremum) is untestable without knowing the extremum's location — and the paper cannot predict it.

5. **The "derivation" is actually more post-hoc than fitting.** CPL is a Taylor expansion — it is honest about being a parametrization. The paper presents itself as a derivation but, as shown in Attacks 3 and 4, it is actually a post-hoc rationalization of a data feature (the phantom crossing in DESI DR2) using an unfalsifiable mechanism. This is epistemically *worse* than CPL, not better.

**Severity: MAJOR.** The paper fails to demonstrate any advantage over the standard CPL parametrization. It is more complex, less predictive, and its "derivation" status is compromised by undefined parameters that must be fit to data.

---

## ADDITIONAL FINDING: DATA CLAIMS DO NOT MATCH PUBLISHED RESULTS — CRITICAL

**The paper claims:**
- "DESI DR2: w(z) non-monotonic at 86.5%, deepest phantom at z=0.87"
- "Pantheon+ 1624 SNe: z<0.1 mu residual = -0.003±0.008, consistent with ΛCDM"
- Together forming a "three-sandwich": -1 → phantom dip → -1

**What published data actually show:**

1. **DESI DR2 (2025):** The standard analysis (arXiv:2503.14743) using the CPL parametrization finds w0 > -1 (quintessence today) and wa < 0 (phantom in the past). This yields a *monotonic* w(z) that crosses from phantom (w<-1, high z) to quintessence (w>-1, low z), with the crossing at z ≈ 0.4-0.5. The w(z) shape is monotonic in the standard parametrization. The specific numbers in the paper — "z=0.87," "deepest phantom," "86.5% non-monotonic" — do not appear in any published DESI DR2 analysis I can locate. These numbers appear to be either the author's own fit using a non-standard parametrization, or fabricated.

2. **Direction of the phantom crossing is reversed.** The paper claims phantom at intermediate z with return to w=-1 at both low and high z (a "dip"). The actual DESI data show phantom at high z crossing to quintessence at low z (a monotonic crossing). These are qualitatively different shapes. The paper's "three-sandwich" does not match the data it claims to explain.

3. **Pantheon+ low-z residuals.** The Pantheon+ analysis (Brout, Scolnic, Riess et al., 2022, ApJ 938, 110) finds w0 = -0.90±0.14 from SNe Ia alone, consistent with ΛCDM at ~1σ. The paper's specific number (-0.003±0.008 mag) may be correct for very low z (z<0.1) residuals, but this is unremarkable — nearly all cosmological models reduce to ΛCDM at sufficiently low redshift. The fact that the low-z universe looks like ΛCDM does not support the causal freeze model over CPL, wCDM, or any other model that asymptotes to w=-1 today.

**Severity: CRITICAL.** If the paper's data claims are fabricated or reflect a non-standard analysis not described in the manuscript, this alone is grounds for rejection. The claim that DESI DR2 data show the "three-sandwich" at 86.5% confidence with the deepest phantom at z=0.87 cannot be verified against published results and appears to contradict them.

---

## SUMMARY OF FINDINGS

| Attack | Finding | Severity |
|--------|---------|----------|
| 1. Citation Fabrication | "C[G] landscape" and "causal graph" are unattested; N_coop cancellation unverified; prior glass-cosmology paper (She 2007) uncited | **FATAL** |
| 2. Prior Art Conflict | YMC (2009), She (2007), Smirnov (2025) all derive w→-1 from principles predating this work | **MAJOR** |
| 3. Logic Gaps | AG→Quench is false dichotomy; Φ_q monotonicity conflates graph growth with search rate; phantom sign unproven; "exactly one extremum" unjustified; exponential relaxation assumed | **FATAL** |
| 4. Magnitude Paradox | τ_explore undefined; central prediction (quench redshift) cannot be computed; theory unfalsifiable | **FATAL** |
| 5. Fatal Alternative (CPL) | CPL uses 2 parameters, makes definite predictions; causal freeze uses 3+ undefined parameters, makes no falsifiable predictions | **MAJOR** |
| Additional: Data Claims | Claimed DESI DR2 "three-sandwich" shape contradicts published DESI DR2 results; specific numbers (z=0.87, 86.5%) unverifiable | **CRITICAL** |

---

## RECOMMENDATION

**REJECT.**

The paper presents a series of metaphors (landscape glass transition, causal graph, quench, relaxation) as a derivation. At every level of the argument — conceptual foundation, mathematical derivation, quantitative prediction, data comparison — the paper fails to meet the standards of a physics research article.

The paper would require, at minimum:

1. A rigorous definition of the "causal graph" and its mapping to FLRW spacetime
2. A derivation of τ_explore from independently measurable quantities (or at minimum, an order-of-magnitude estimate grounded in known physics)
3. A proof that Φ_q > 1 produces phantom (w < -1) rather than quintessence (w > -1)
4. Citation and engagement with the prior literature (She 2007, YMC 2009, and the post-DESI-DR2 model landscape)
5. A proper statistical comparison with CPL and other benchmark models
6. Correction or justification of the claimed DESI DR2 data points against published results

These are not minor revisions. They require rebuilding the paper from its foundations. I cannot recommend publication in any form.

---

**Confidential note to editor:** The manuscript's combination of undefined central quantities, incorrect data claims, and non-citation of directly relevant prior art raises concerns beyond scientific quality. I recommend checking the claimed DESI DR2 numbers (z=0.87, 86.5%) against the actual data — if these are fabricated, this is a research integrity issue, not just a quality issue.
