# REVIEWER I — Final Judgment (30-Year PRD Reviewer)

**Date:** 2026-06-06
**Paper:** "Information Capacity and the Structure of Physical Law: Why Quantum, Classical, and Gravity are Phases of Finite Information" (v3)
**Materials reviewed:** v3 manuscript + REVIEWER_A through REVIEWER_F + INSPECTOR_surprisal

---

## Prelude

I have been reviewing for Physical Review D for three decades. I have seen papers that changed physics. I have seen papers that should never have been written. I have seen papers that were technically flawless and physically empty. I have seen papers that were technically flawed and physically profound. This paper is none of those things. It is something rarer: a paper that has been through six rounds of adversarial attack and emerged with a core that is genuinely interesting—but which still cannot honestly claim what its title and abstract claim.

Let me be clear about what I am doing. I am not going to repeat the eight mathematical attacks of Reviewer A, the eight experimental attacks of Reviewer B, or the eight conceptual attacks of Reviewer C. Those reviews exist. They are thorough. The authors have read them. v3 incorporates some of their findings and ignores others. My job is different. I am here to say what kind of paper this is, in the grand scheme of things.

---

## 1. What Category Does This Paper Belong To?

The options:

- (a) Breakthrough—changes our understanding of physics
- (b) Valuable contribution—advances a specific direction
- (c) Interesting attempt—insight present, execution incomplete
- (d) Philosophy disguised as physics
- (e) Wrong

**My answer: (c), with a non-trivial amount of (b).**

The paper is not (a). A breakthrough changes what we can predict. This paper predicts nothing that we did not already know, except perhaps the absence of a sharp event horizon—and that prediction is presented as a "qualitative target for future development," not a calculable result.

The paper is not (d). Unlike much of what passes for "information-theoretic gravity," this paper has actual equations. The q-field PDE is a specific, well-defined mathematical object. The universality class Φ is a theorem, not a slogan. The Kac recurrence theorem says something precise about relaxation vs. recurrence timescales. This is not philosophy.

The paper is not (e). The mathematics—where it is rigorous—is correct. The pigeonhole principle gives bijectivity. The entropy identity is a valid decomposition. The static limit of the q-field PDE does produce the Laplace equation. These are not errors.

The paper is (c) because the gap between what the mathematics establishes and what the narrative claims is substantial. But it edges into (b) because the core idea—that classicality is a self-organized critical state of information dynamics, not merely the passive absence of quantum coherence—is a genuine conceptual contribution that standard decoherence theory does not offer.

I have rejected hundreds of papers. Most of them I forget within a week. I will remember this one.

---

## 2. What Is the "Hard Core" That Survived v1→v2→v3?

The paper's claims have been downgraded at every revision:

- v1: "The universe must separate into quantum and classical regimes" (necessity claim)
- v2: "The separation follows from the dynamics without additional assumptions" (derivation claim, softened verbs)
- v3: "We show that three definitional truths are sufficient to explain the structural form..." (sufficiency claim, universality class)

The flux form has changed twice:

- v1: J ∝ 1/q² (osmotic pressure, scale invariance argument)
- v2: J ∝ 1/q² (same, with more caveats)
- v3: J ∝ -∇(ln q) (surprisal/self-information, Shannon uniqueness argument)

After all this evolution, **what remains standing?**

**The universality class Φ.** This is the paper's most important mathematical result. Theorem (v3 §3.4): For any flux function φ(q) that is smooth on (0,1], has φ'(q) < 0, φ(0⁺) = +∞, and finite φ(1), the qualitative conclusions—dual-domain asymptotic states, Laplace-type static limit, and 1/r gravitational decay—are universal. This means the paper's core physical picture does NOT depend on the specific choice of flux form. The 1/q² form, the -ln q form, any monotonic function with a pole at q=0 and finite value at q=1—they all produce the same qualitative structure.

This is a genuine, non-trivial result. It was not in v1 or v2 (at least not as a theorem). It protects the paper's qualitative conclusions from the most damaging attack: "You just picked the flux form that gives the answer you wanted." The universality theorem says: any reasonable flux form gives the same qualitative answer.

**The competition of pressures.** Diffusion pressure (driven by the 1/q nonlinearity, amplifying gradients toward q≈0) vs. entropic pressure (driven by the statistical preference for q≈1/2). This competition produces a two-phase structure: compact q≈0 cores (classical objects) embedded in a q≈1/2 sea (quantum background). This picture is independent of the specific flux form (by the universality theorem) and is genuinely different from standard decoherence theory's narrative of "environment selects pointer states."

**The self-organized criticality picture.** Regardless of whether the BTW sandpile analogy is quantitatively accurate (it isn't—see Reviewer C, Attack 4), the idea that q→0 is an attractor that makes classical objects *active sources* of information outflow rather than *passive sinks* of quantum coherence is a conceptual reframing worth having.

**Is this worth publishing?** Yes. The universality theorem and the competition-of-pressures picture belong in the literature. They would make a strong Foundations of Physics paper. They are not enough for PRD, because PRD requires empirical contact, and this paper has none (see Reviewer B's eight attacks, which remain largely unaddressed in v3).

---

## 3. What Form Should This Paper Take?

**A Foundations of Physics article, with an honest abstract.**

Not a PRD paper. Not a PRL. Not a monograph. Not a blog post. And not "not worth existing."

The paper should exist. It should be publicly available. It should be citable. The universality class Φ theorem, the competition-of-pressures picture, and the q-field equation ∂_t q = κ∇²(ln q) with its static limit ∇²(ln q)=0—these are original contributions to the foundations of physics.

But the paper should not claim to have "derived gravity." It should claim to have "identified a structural correspondence between information capacity dynamics and the Laplace/Poisson equation that governs Newtonian gravity—a correspondence that is universal across a broad class of flux functions." This is what was actually achieved.

The paper should not claim to explain "Why the Universe Looks Different at Different Scales." It should claim to explain "Why Quantum and Classical Behavior Coexist as Phases of Finite Information." The title's "at Different Scales" is a documented contradiction with the paper's own Honest Boundaries section (see Reviewer D, Item 8).

The paper should not present the separation mechanism as "following from the dynamics without additional assumptions." It should present it as "a physical picture supported by: (i) the universality theorem, (ii) the divergent diffusivity at q→0, (iii) the entropic maximum at q≈1/2, and (iv) numerical evidence. A rigorous proof of asymptotic phase coexistence remains an open problem."

These are not cosmetic changes. They are changes in what the paper claims to have achieved. But the paper can make them without changing a single equation.

---

## 4. What Is the Biggest Problem? (Structural, One Sentence)

**The paper systematically conflates "showing that a conclusion is mathematically consistent with the axioms" with "showing that the axioms force the conclusion to be true"—and this conflation, present in every section from Introduction to Conclusion, is the engine of every overclaim that six reviewers have independently identified.**

This is not a problem with the mathematics. The mathematics—where rigorous—is correct. This is a problem with the *genre* of the paper. The paper is written as if it is a derivation: "From these axioms, we prove that..." But what it actually does is something different and more modest: it constructs a mathematical model (the q-field, with a chosen flux function) that is *consistent with* the axioms and that *produces as its static limit* an equation that *structurally resembles* the Newtonian gravitational field equation. This is model-building, not derivation. Model-building is legitimate science. But calling model-building "derivation from axioms" is not.

The six previous reviewers all converged on this point from different angles:
- Reviewer A: "The flux ansatz is a modeling choice, not derived from A1-A3."
- Reviewer B: "The 'derivation' of gravity requires 5 external inputs."
- Reviewer C: "The core narrative conflates definition with deduction."
- Reviewer D: "v2 is a rewording pass—the underlying overclaims persist."
- Reviewer E: "The flux function is chosen, not derived."
- Reviewer F: "The input-amplification structure is obscured."

v3 partially addresses this by introducing the universality class Φ, which reduces the dependence on any specific flux form. But the paper still says "we prove that the information flux J = -κ∇(ln q) is the unique form satisfying Shannon's uniqueness theorem" (v3 §3.2-3.3)—as if Shannon's theorem, which is about the uniqueness of entropy as an information measure, directly selects a *flux function* for a *dynamical PDE*. It does not. Shannon proved that -∑p_i log p_i is the unique additive information measure. He did not prove that -ln q is the unique information flux potential. The jump from "entropy is unique" to "flux is -κ∇(ln q)" requires the additional postulate that the flux potential IS the self-information of vacancy—which is physically motivated but not logically forced.

---

## 5. What Is the Biggest Value? (One Sentence)

**The insight that classicality can be understood as an active, self-organized critical phase of information dynamics—a phase that drives information outflow and whose static geometry we measure as gravity—rather than as the passive decay of quantum coherence, is genuinely original and reframes the quantum-classical transition in a way that neither standard decoherence theory nor any existing competitor offers.**

If the author abandoned this direction tomorrow, what would physics lose? It would lose a perspective in which gravity and classicality are two manifestations of the same underlying phenomenon: the exhaustion of information capacity. This perspective is not present in Zurek's quantum Darwinism (which explains how classicality emerges from quantum systems through environmental monitoring, but does not connect to gravity). It is not present in Penrose/Diosi (which connects gravity to decoherence but through gravitational self-energy, not information capacity). It is not present in Verlinde's entropic gravity (which derives gravity from entropy but does not address the quantum-classical transition). It is not present in Bassani & Magueijo (which explains how physical laws emerge through natural selection but starts from known gravity).

The fact that this perspective is *unique* does not make it *correct*. But it means that losing it would leave a hole in the space of ideas that no existing framework fills.

The competition-of-pressures picture—diffusion pressure driving toward q≈0, entropic pressure driving toward q≈1/2, the two coexisting as phases—is the paper's most valuable specific idea. Even if the q-field equation turns out to be the wrong equation, the *structure* of the explanation (two competing attractors producing phase coexistence) might survive in a better theory.

---

## 6. Editorial Decision

**Decision: REJECT from Physical Review D.**

**One-sentence reason:** The paper offers a genuinely original conceptual reframing of the quantum-classical transition with a mathematically interesting universality theorem at its core, but it lacks the empirical content, completed derivation chain, and sharp distinction from existing work that PRD requires—it would be a strong submission to Foundations of Physics after three specific revisions.

**Three revisions required before resubmission anywhere:**

1. **Change the title.** "Why the Universe Looks Different at Different Scales" promises an explanation of scale that the paper's own Honest Boundaries section admits it cannot deliver. Change to: "Quantum, Classical, and Gravity as Phases of Finite Information" (drop the "Why" clause entirely) or "Why Quantum and Classical Worlds Coexist: An Information Capacity Perspective."

2. **Rewrite the Abstract.** The current Abstract says "We prove that three definitional truths... are sufficient to explain the structural form of the quantum-classical separation, the arrow of time, and the Newtonian gravitational field equation." Change to: "We show that three definitional truths about information, together with a physically motivated flux ansatz, are sufficient to construct a model—the q-field—whose static limit is structurally identical to the Laplace equation for the Newtonian gravitational potential. The qualitative conclusions (dual-domain asymptotic states, Laplace-type static limit, 1/r decay) are universal across a broad class of flux functions. The model makes one falsifiable prediction (absence of sharp event horizons) and provides a conceptual reframing of classicality as a self-organized critical state of information dynamics."

3. **Add an assumption dependency graph.** A table or diagram showing exactly which conclusions depend on which assumptions beyond A1-A3. The UMP/ergodicity assumptions. The flux ansatz. The gradient expansion validity. The static limit assumption. The d=3 input. The κ calibration. The η placeholder. This exists implicitly in Reviewer A's Attack 8 chain. Make it explicit. The paper's honesty would be transformed by this one addition.

---

## Closing Reflection

Thirty years ago, when I started reviewing for PRD, I believed that a paper was either right or wrong, publishable or not. I no longer believe this. A paper can be right in its mathematics and wrong in its claims. It can be unpublishable at PRD and valuable to physics. It can be flawed in execution and profound in conception.

This paper is all of those things. The mathematics of the q-field is interesting. The universality class Φ is a real theorem. The claim to have "derived gravity from information axioms" is false—or at least, not true in the sense that the paper's rhetoric implies. The paper should not be published in PRD. But it should be published somewhere, because the competition-of-pressures picture and the self-organized criticality reframing of classicality are ideas that physicists thinking about the foundations of quantum mechanics and gravity should encounter.

I have rejected papers that were technically flawless and physically empty—perfect calculations about things that don't matter. This paper is the opposite: imperfect calculations about something that might matter a great deal. In the long run, the second kind of paper is more valuable than the first.

But PRD is not the place for it. Foundations of Physics is.

---

*REVIEWER I. Thirty years. This one was interesting.*
