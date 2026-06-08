# REVIEWER F — PRD Editorial Board: Publication Standard Assessment

**Role:** PRD Editorial Board Member
**Date:** 2026-06-06
**Paper:** "Why the Universe Looks Different at Different Scales: Quantum, Classical, and Gravity as Phases of Finite Information" (v2)
**Reference Benchmark:** Bassani & Magueijo, "How to Make a Universe", PRD 111, 103529 (2025)
**Question:** Does this paper meet PRD's publication standard?

---

## Dimension 1: Physical Significance

### The question

Is the physical content **significant** (changes our understanding of something) or **marginal** (provides an alternative formulation of known physics)?

### Assessment: MARGINAL

The paper's core physical claim is that quantum coherence and classical irreversibility are two phases of a finite information system governed by $\partial_t q = D_0\nabla^2(1/q)$, with the static limit yielding the Laplace equation $\nabla^2(1/q)=0$ — structurally identical to the Newtonian gravitational field equation.

This is a novel and internally coherent narrative. But it is a narrative about **how things could be arranged**, not a discovery about **how things are**. The paper does not:

1. **Change any specific physical prediction.** In every regime where both the framework and standard physics apply, they give the same answer. The $q$-field equation is new mathematics but old physics — its static limit reproduces Newtonian gravity, which we already had.

2. **Resolve any outstanding puzzle.** Standard decoherence theory already explains how the quantum-to-classical transition occurs. The paper asks "why this structure rather than another" — a legitimate question, but answering it with "because information is finite" is a reframing of the explanandum, not an explanation of it. The answer has the form: "The universe separates into quantum and classical regimes because it is a finite information system" — but this simply restates the phenomenon in new vocabulary (capacity ratios) without identifying a new causal mechanism.

3. **Provide new constraints on physical parameters.** The framework does not constrain $G$, $\hbar$, $c$, $\eta$, $d$, or any other physical parameter. It accepts them as inputs and shows consistency. Consistency is not discovery.

4. **Explain numerical scales.** The paper's title promises to explain why the universe looks different "at different scales," but the framework does not predict the scale of the quantum-classical boundary ($\sim 10^{-10}$ m). That scale is an input via $G$, $c$, and the calibration of $\kappa$.

**Contrast with the BM benchmark:** Bassani & Magueijo (2025) derive the **complete Einstein equations** (including the cosmological constant $\Lambda$) from unimodular gravity plus natural selection on a Markov chain. This is a genuine derivation: they start with a subset of GR and end with the full thing, including a resolution of the cosmological constant problem (emergence of $\Lambda$ as an integration constant). BM changes our understanding of where the Einstein equations and $\Lambda$ come from. DGF does not change our understanding of where the Laplace/Poisson equation comes from — it shows that it can be reached from a different starting point, with more inputs.

**Verdict: The physical content is marginal for PRD standards.** PRD requires "significant physical content" — content that changes our understanding of a physical phenomenon. This paper offers a conceptual reframing that is internally consistent but does not alter any specific physical claim.

---

## Dimension 2: Mathematical Rigor

### The question

v2 has honestly downgraded from "prove" to "show." After this downgrade, is the mathematics sufficient?

### Assessment: BORDERLINE — Sufficient for Foundations of Physics, Marginal for PRD

The paper's mathematical structure can be divided into three tiers:

**Tier 1 — Rigorous (Theorems 1-3, reflux bound):**
- Bijectivity from injectivity on finite sets (pigeonhole principle): correct.
- Entropy identity under doubly stochastic coarse-graining: correct (this is essentially a known information-theoretic identity).
- Kac recurrence scaling: correct under stated ergodicity assumptions.
- Reflux combinatorial bound: correct under the Uniform Mixing Property assumption.

These are clean combinatorial results. They are not deep — the bijectivity theorem is the pigeonhole principle, the entropy identity is a standard decomposition — but they are correct.

**Tier 2 — Formal but unproven (continuum $q$-field, fast diffusion):**
- The derivation $\partial_t q = D_0\nabla^2(1/q)$ from the discrete flux ansatz $J_{i\to j} = 1/q_i - 1/q_j$ via gradient expansion is **formal**. No error bounds are provided. The truncation of $O(a^4)$ terms is not justified near the $q\to 0$ singularity where gradients may be large. The flux ansatz itself is a modeling choice, not derived from A1-A3.
- The fast diffusion classification ($m=-1$, supercritical for $d\ge 2$) is a formal analytic continuation of standard fast diffusion theory (which is proved for $m>0$). The extrapolation to negative $m$ is not justified by reference to any existence/regularity theorem.
- The static limit $\nabla^2(1/q)=0$ is a necessary condition, but existence of static solutions is not proved. In fact, the internal supporting document proves that **no classical stationary solution exists that attains $q=0$ at an interior point** — meaning the static equation cannot describe the interior of a "mass." The paper's physical conclusions depend on the exterior static solution, but the mismatch at $q=0$ is not addressed in the main text.

**Tier 3 — Conjectural (two-domain asymptotics, separation mechanism):**
- The claim that the asymptotic state consists of compact $q\approx 0$ cores embedded in a $q\approx 1/2$ sea is not proved. The supporting document admits "proof sketch; full proof deferred." The main v2 text has downgraded from "Theorem 10" but the argument remains heuristic: gradient amplification in the linearized regime + divergent diffusivity at $q=0$ + entropic preference at $q=1/2$ do not constitute a proof of asymptotic phase coexistence. The nonlinear interaction of these mechanisms — the hard part — is not analyzed.
- The self-organized criticality (SOC) analogy to the BTW sandpile is qualitative. No critical exponents, no power-law distributions, no $1/f$ noise are derived. The analogy is a physical picture, not a mathematical result.

**Honesty assessment:** v2 is more honest than v1. The "Honest Boundaries" section (VIII) explicitly lists what is and is not explained. The paper says "we do not prove this principle; we show that if you accept it..." This is the right epistemic stance. But the residual problem is that the claims most interesting to physicists (the separation mechanism, the gravity correspondence) depend on the least rigorous parts of the derivation.

**Can this be fixed?** Partially. The formal continuum derivation could be strengthened with error estimates. The fast diffusion singularity could be analyzed numerically. The two-domain asymptotics could be downgraded to Conjecture 1 with explicit caveats. But the deepest gap — the flux ansatz $J = 1/q_i - 1/q_j$ is not derivable from A1-A3 — is structural, not technical.

**Verdict: The mathematics is sufficient for a conceptual/foundations paper but marginal for PRD.** PRD expects mathematical rigor commensurate with the claims. A paper that claims to "show" that gravity emerges from information axioms but whose derivation chain contains five unproven steps (UMP assumption, flux ansatz, gradient expansion without error bounds, fast diffusion analytic continuation, static solution existence) falls short of PRD's mathematical standard.

---

## Dimension 3: Distinction from Existing Work

### The question

Are the distinctions from Zurek, Penrose/Diósi, BM, and Vopson clear and substantive, or are they "we're complementary" fuzzy treatments?

### Assessment: INSUFFICIENT — Systematically Fuzzy

The paper discusses four existing frameworks. In all four cases, the strategy is the same: claim complementarity rather than competition.

**Zurek (quantum Darwinism):** "Quantum Darwinism describes the *mechanism* of classicalization; DGF describes the *condition* under which it is inevitable."

This is a distinction without a difference that matters. Zurek's quantum Darwinism already describes the condition (environment-induced superselection) AND the mechanism (information proliferation). DGF's "condition" (capacity exhaustion) does not add a testable constraint on top of what quantum Darwinism already provides. If two theories are "complementary" in the sense that they never make conflicting predictions in any accessible regime, their complementarity is empirically vacuous.

**Penrose/Diósi (gravitational decoherence):** "Complementary rather than competitive: in DGF, gravitational attraction *is* the static geometry of capacity exhaustion."

This is a category error in the comparison. Penrose and Diósi make a specific, quantitative claim: gravitational self-energy $\Delta E_{\text{grav}}$ sets a decoherence timescale $\tau \sim \hbar/\Delta E_{\text{grav}}$. This has been experimentally tested (and largely ruled out for the original Diósi model, constrained for Penrose). DGF makes no quantitative claim about decoherence timescales. Calling them "complementary" when one makes testable quantitative predictions and the other does not is misleading.

**Bassani & Magueijo:** "BM provides the mechanism; DGF provides the architecture."

This is the most problematic comparison because:

1. BM is the direct benchmark — a PRD paper addressing the same class of question (emergence of physical laws).
2. BM's structure is substantially richer: 9 sections, Hamiltonian formulation with Poisson brackets, Dirac hypersurface deformation algebra, explicit connection to unimodular gravity, Monte Carlo simulations of absorbing Markov chains, 6 figures showing mass distribution functions with fractal structure.
3. BM's input-output ratio is superior: 1 physical input (unimodular gravity) $\to$ complete Einstein equations (including $\Lambda$). DGF: 5 inputs ($G$ calibration, $\eta$, $d=3$, static assumption, $a/c$ identification) $\to$ Laplace equation (static Newtonian limit).
4. The "architecture vs. mechanism" framing avoids confronting the fact that BM derives more physical structure from fewer and physically better-motivated inputs.

A more honest comparison would acknowledge: BM starts from known physics (a sub-theory of GR) and derives more known physics. DGF starts from new, unvalidated axioms and reaches a smaller, less novel result (the Laplace equation in the static limit). BM's strategy is conservative and successful; DGF's strategy is ambitious and incomplete. These are different projects — but they are not peers in achievement.

**Vopson (infodynamics):** "The apparent contradiction is terminological, not physical."

Vopson's second law of infodynamics claims that information entropy *decreases* in isolated systems — the exact opposite of the standard second law, and the opposite of DGF's Theorem 2 (which has Shannon entropy increasing from its initial lower bound). Dismissing this as "terminological" without analyzing whether Vopson's "information entropy" is the same mathematical quantity as DGF's Shannon entropy is too quick. If they are different quantities, the paper should explain the mapping. If they are the same, one of the two frameworks is wrong.

**The deeper problem:** The "complementary" strategy is a rhetorical device that allows the paper to claim relevance to major research programs without having to demonstrate superiority over any of them. This might be acceptable in a review article or a Foundations of Physics paper. In a PRD paper, where the standard requires "clear distinction from existing work," it is insufficient.

**Verdict: The distinctions are not sharp enough for PRD.** The paper needs to either (a) identify a specific, quantitative claim on which DGF and at least one existing framework make conflicting predictions, or (b) stop framing the relationship as "complementary" and instead clearly acknowledge that DGF is a conceptual reframing that does not (yet) compete with established theories on empirical grounds.

---

## Dimension 4: Experimental Contact

### The question

v2 has honestly downgraded S1 from "core prediction" to "capacity constraint," admitted closed-system DGF=QM, and admitted IBM data is insufficient. After honest downgrading, is the experimental contact sufficient?

### Assessment: INSUFFICIENT — Effectively Zero Distinguishable Empirical Content

Let us inventory what remains after honest downgrading:

| Claim | Status after v2 downgrade | Distinguishes DGF from standard physics? |
|-------|--------------------------|----------------------------------------|
| S1 reflux bound $P \le q_S/q_E$ | Capacity constraint, not core prediction | No — closed-system: DGF=QM; open-system: DGF lacks theory |
| $\nabla^2(1/q)=0$ gravity correspondence | Post-diction (matches known Newtonian gravity) | No — reproduces known result |
| $1/r$ decay | Geometric fact about $d=3$ Laplace equation | No — known since Newton |
| $q\approx 0$ = classical, $q\approx 1/2$ = quantum | Definitional (phases defined by the theory) | No — labels, not predictions |
| Table 1 ($q$ at surfaces) | Computed from known $G$, $M$, $R$ using Newtonian formula | No — circular: input known quantities, output restated as "explanation" |
| Entropy identity | Information-theoretic identity | No — standard Gibbs/Shannon result |
| Kac recurrence | Standard ergodic theory result | No — Kac (1947) |
| Two-domain coexistence | Conjecture | Not testable — $q$ not measurable |

**The bottom line:** After stripping away claims that (a) reproduce known physics, (b) are definitional rather than predictive, (c) are standard information theory, or (d) are untestable because $q$ is not a measurable quantity, the paper has **zero empirical content that distinguishes it from standard physics in any currently accessible experimental regime.**

This is not an exaggeration. The paper's authors have been honest in v2 about the limitations. But honesty about having no testable predictions does not create testable predictions. It merely makes the absence visible.

**The specific problems:**

1. **$q$ is not independently measurable.** $q = (N - \sum s_i)/N$ requires knowing the total number of "cells" $N$ and the occupation state of each cell. Neither is operationally accessible. The operational proxy $q_S \approx T_2/(T_1+T_2)$ is a heuristic, not a derivation ($T_2/T_1$ at best correlates with coherence, but the functional form is unvalidated).

2. **$N_E$ has no independent calibration scheme.** The number of environmental cells is not directly measurable. Different estimation schemes give $N_E$ ranging from 0 to 80,000. Without independent calibration, any experimental "test" becomes curve-fitting: choose $N_E$ to match the data, then claim the data supports the theory.

3. **Closed-system equivalence blocks discrimination.** In the only regime where DGF has a well-defined theory (closed systems), it predicts the same as standard QM. In the regime where it could potentially differ (open systems), it has no theory.

4. **$\eta$ [kg/bit] is completely unconstrained.** The mass-information conversion factor — the parameter that makes the gravity correspondence physically meaningful — has no estimated value, no order-of-magnitude bound, and appears in no testable formula. A free parameter that appears nowhere in any prediction is not a parameter — it is a placeholder for missing physics.

5. **The "zero temperature" regime is physically inaccessible.** At 35 mK, thermal excitation probability ($\sim 0.11\%$) and quasiparticle background ($\sim 0.1\%$) together exceed the DGF signal for $N_E \gtrsim 200$. Lower temperatures reduce thermal noise but not quasiparticle noise, which saturates at $\sim 0.1\%$ due to non-equilibrium effects.

**The PRD standard requires "testable predictions or clear connection to experimental data."** This paper has neither. The reflux bound is not testable with current technology (and may not be testable in principle if the open-system DGF theory converges to standard Lindblad, which the paper's own "full compatibility with QM" stance suggests). The gravity correspondence is a post-diction, not a prediction.

**Verdict: The experimental contact is insufficient for PRD.** This alone is disqualifying.

---

## Dimension 5: Overall Judgment — Which Journal?

### The PRD Publication Spectrum

| Journal | Requirements | Fit with DGF v2 |
|---------|-------------|-----------------|
| **PRL** | Breakthrough result + broad interest + extreme concision | **No.** No breakthrough result. |
| **PRD** | Significant physical content + rigorous math + clear motivation + experimental contact | **No.** Marginal significance, borderline rigor, fuzzy distinction, zero empirical content. |
| **PRD Letter** | Same as PRD but shorter | **No.** Same problems. |
| **Foundations of Physics** | Conceptual framework + philosophical depth + mathematical rigor can be moderate | **Yes.** This is the natural home. The paper's strength is precisely what FoP values: a conceptual reframing of foundational questions (quantum-classical transition, arrow of time, emergence of gravity) in information-theoretic terms. |
| **Entropy** (MDPI) | Information theory + physics + open access | **Yes.** The information-theoretic framing fits. Lower prestige but appropriate scope. |
| **European Journal for Philosophy of Science** | Conceptual analysis + scientific methodology | **Possible.** The paper's "definitions of existence and interaction" framing is philosophical. |
| **arXiv only** | None | **Always an option.** The paper is conceptually interesting and deserves to be publicly available for discussion. |

### Recommended Strategy

**Primary recommendation: Foundations of Physics.**

The paper is fundamentally a contribution to the foundations of quantum mechanics and gravity. It proposes that information capacity constraints provide a unifying perspective on quantum coherence, classical irreversibility, and gravitational attraction. This is exactly the kind of work that Foundations of Physics was created to publish:

1. The conceptual framework is novel and interesting.
2. The mathematical structure (the $q$-field equation and its static limit) is original.
3. The paper is honest about its limitations — a virtue in foundations work.
4. The audience (philosophers of physics, foundations-oriented theoretical physicists) is the right one for this paper.
5. The mathematical requirements are lower — formal derivations without rigorous error bounds are acceptable when the conceptual contribution is clear.

**Secondary option: Entropy** (MDPI, open access). The information-theoretic framing ($q$ as capacity, Shannon entropy evolution, reflux bound) is directly in scope. The peer review is typically lighter than PRD. The open access model ensures wide readership.

**Not recommended: PRD.** Resubmission to PRD would be inappropriate given the four-dimensional insufficiency documented above. The paper's honest downgrades in v2 have moved it further from the PRD standard, not closer — because they have made explicit what was previously implicit: that the framework lacks the empirical content and mathematical completion that PRD requires.

**Also not recommended: PRL.** PRL requires both breakthrough significance and extreme concision. This paper is neither.

---

## Dimension 6: Editorial Decision

### If I were the PRD editor receiving this paper

**Decision: REJECT.**

**One-sentence reason for the author:**

> The paper offers a genuinely interesting conceptual reframing of quantum-classical separation in information-theoretic terms, but it lacks the experimental contact, sharp distinction from existing work, and completed mathematical derivation chain that PRD requires; it would be a strong submission to Foundations of Physics, where its conceptual strengths would be appropriately valued.

### Detailed editorial letter (draft)

```
Dear Dr. Huang,

I have read your manuscript "Why the Universe Looks Different at 
Different Scales" with interest. The central idea — that quantum 
coherence and classical irreversibility can be understood as phases 
of a finite information system governed by a nonlinear diffusion 
equation — is original and conceptually appealing.

However, after careful consideration, I cannot send this manuscript 
out for peer review at Physical Review D, for the following reasons:

1. EXPERIMENTAL CONTACT. The manuscript's empirical content is, by 
its own honest admission in v2, limited to a single inequality bound 
that is not testable with current technology. PRD requires either 
testable predictions or a clear connection to experimental data. 
The honest downgrading of S1 from "core prediction" to "capacity 
constraint" is scientifically commendable, but it leaves the paper 
without the empirical anchor that PRD requires.

2. MATHEMATICAL COMPLETENESS. The derivation chain from information 
axioms to the gravitational Laplace equation contains multiple 
unproven steps: the flux ansatz, the continuum limit without error 
bounds, the fast diffusion classification via formal analytic 
continuation, the existence of static solutions, and the two-domain 
asymptotic conjecture. The paper's adoption of "show" rather than 
"prove" language is appropriate, but the gap between what is shown 
and what is claimed remains substantial for a PRD article.

3. DISTINCTION FROM EXISTING WORK. The manuscript frames its 
relationship to Zurek, Penrose/Diósi, Bassani-Magueijo, and Vopson 
as uniformly "complementary." While intellectual generosity is 
admirable, a PRD paper must articulate a clear, substantive 
distinction from existing literature — preferably one that could, in 
principle, be settled by experiment or observation. The uniformly 
complementary framing suggests that the framework does not yet make 
contact with empirical reality in a way that could distinguish it 
from alternatives.

I believe this work has genuine value as a contribution to the 
foundations of physics. The q-field equation, the capacity-ratio 
perspective on quantum-classical separation, and the structural 
connection to the Laplace equation are interesting ideas that 
deserve to be in the literature. I would encourage submission to 
Foundations of Physics or Entropy, where the conceptual contribution 
would be evaluated on its own terms rather than against PRD's 
requirement of completed mathematical derivation and empirical 
contact.

Sincerely,
[PRD Editor]
```

---

## Synthesis: Cross-Reviewer Convergence

Comparing my assessment with the three previous reviewers:

| Dimension | Reviewer A (Math) | Reviewer B (Experiment) | Reviewer C (Concept) | Reviewer F (PRD Standard) |
|-----------|-------------------|------------------------|---------------------|--------------------------|
| Math rigor | FATAL: Theorem 10 mislabeled, continuum gap | — | — | BORDERLINE: Honest after downgrade, but claims exceed proofs |
| Experimental contact | — | FATAL × 4: Zero empirical content | — | INSUFFICIENT: Zero distinguishable empirical content |
| Conceptual foundation | — | — | FATAL: A3 carries all weight, q type confusion, BM comparison collapses | MARGINAL: Conceptual reframing, not physical discovery |
| Distinction from literature | — | — | FATAL: BM comparison is the weakest pillar | INSUFFICIENT: Uniformly fuzzy "complementary" framing |
| Overall verdict | Major revision required | REJECT | REJECT (needs framework-level reconstruction) | REJECT from PRD; recommend Foundations of Physics |

**Convergence:** All four reviewers independently reach the conclusion that this paper should not be published in PRD in its current form. The reasons differ (mathematical overclaim, empirical emptiness, conceptual confusion, PRD standard mismatch), but the endpoint is the same.

**Divergence on post-rejection path:** 
- Reviewer A believes major revision could make it PRD-ready (fix Theorem 10, add assumption tracker, clarify continuum derivation).
- Reviewer B believes the empirical content problem is structural and unfixable — the paper should be split into a math paper (reflux bound) and a review article (conceptual framework).
- Reviewer C believes the concept-level problems require framework reconstruction, not just editing.
- Reviewer F (this review) believes the paper will never be a PRD paper but could be a strong Foundations of Physics paper with modest revisions (fix the BM comparison, downgrade two-domain claim to conjecture, clarify that A3 carries most physical content).

**The most important single fix, regardless of venue:** The Bassani-Magueijo comparison in Section 7.3. Currently it reads as "BM does mechanism, we do architecture" — implying parity. This is the paper's most exposed flank because any referee familiar with the BM paper will immediately see the asymmetry. A honest rewrite would acknowledge: BM derives more (complete Einstein equations) from less (one known physical input). DGF derives less (static Laplace equation) from more (five inputs, some new and unvalidated). The two projects are on different trajectories — BM is a completed derivation within known physics, DGF is an exploratory derivation from new axioms. Both are legitimate. They are not peers in achievement.

---

## Final Recommendation Summary

| Item | Verdict |
|------|---------|
| Physical significance | MARGINAL (conceptual reframing, not discovery) |
| Mathematical rigor | BORDERLINE (clean combinatorics, formal continuum) |
| Distinction from existing work | INSUFFICIENT (uniformly fuzzy "complementary" framing) |
| Experimental contact | INSUFFICIENT (zero distinguishable empirical content) |
| Suitable for PRD? | **NO** |
| Suitable for PRL? | **NO** |
| Suitable for Foundations of Physics? | **YES** — this is the natural home |
| Suitable for Entropy? | **YES** — information-theoretic framing fits |
| Editorial decision at PRD | **REJECT** |
| One-sentence reason | The paper offers an interesting conceptual reframing but lacks the experimental contact, sharp distinction from existing work, and completed mathematical derivation that PRD requires — submit to Foundations of Physics instead. |

---

*REVIEWER F assessment completed. This review is based on the v2 manuscript (main_prd_v2.tex), the three prior reviewer reports (A/B/C), and the Bassani & Magueijo (2025) benchmark paper (PRD 111, 103529, arXiv:2502.00081).*
