# REVIEWER D — Fix Authenticity Audit

**Role:** REVIEWER D (Fix Auditor)
**Date:** 2026-06-06
**Task:** Verify whether v2 genuinely fixes v1 problems, rewrites labels without changing substance, ignores problems, or makes them worse.
**Materials compared:** v2 (`main_prd_v2.tex`) vs. v1 (as documented in REVIEWER_A/B/C reports and synthesis)

---

## Executive Summary

**Overall judgment: v2 is a REWORDING PASS, not a FIX PASS.** Of the 8 claimed fixes, 2 are genuinely FIXED, 4 are REWORDED (substance unchanged), 1 is PARTIALLY FIXED (mixed), and 1 is BROKEN_MORE. The most systematic change---verb replacement ("prove"→"show", "Theorem 10"→unnamed paragraph)---does lower the epistemic temperature of the paper, but the mathematical content and argument structure are nearly identical to v1. The problems identified by REVIEWERs A, B, and C remain present in the mathematics; they are now simply described with softer language.

---

## Item-by-Item Audit

### 1. Theorem 10降级: REWORDED

**v1 status:** Theorem 10 (Two-Domain Asymptotics) was labeled a Theorem in the main manuscript, while supporting documents admitted "proof sketch... full proof deferred to a companion paper." Fatal misrepresentation.

**v2 claim:** Theorem numbers removed entirely. The content of Theorem 10 now appears in §4.4 "The separation mechanism" as a 5-step enumeration introduced by "The emergence of two distinct domains follows from the $q$-field dynamics without additional assumptions."

**What changed:**
- Theorem label: removed (genuine improvement).
- Numbered theorems eliminated from the entire paper -- all theorems are now unnumbered.

**What did NOT change:**
- The epistemic claim "follows from... without additional assumptions" is logically equivalent to claiming the status of a derivation. It presents the conclusion as logically inevitable given the premises -- the exact same epistemic stance as "Theorem," just without the label.
- The 5-step mechanism (start from q≈1, inhomogeneity creates gradient, 1/q² amplifies, q≈0 becomes critical, q≈1/2 is entropic attractor) is identical to v1's Theorem 10 proof sketch.
- The v1 supporting documents' admissions ("proof sketch," "full proof deferred," "requires singular perturbation theory at the interface") are absent from v2. v2 does not acknowledge that the "follows from" argument is incomplete.
- The interaction of anti-diffusion, singular diffusivity, and entropic preference -- which v1's supporting docs admitted was unproven -- is still presented as if it follows directly.

**REVIEWER A's original attack:** "A statement whose proof is incomplete, and whose key steps rely on unverified approximations, should be labeled a Conjecture, not a Theorem."

**v2's response:** Remove the "Theorem" label. Keep the claim. Don't add a "Conjecture" label. Don't discuss what is unproven.

**Verdict: REWORDED.** The label that would trigger a reviewer's "this is not a theorem" response was removed. The underlying epistemic overclaim -- that the separation mechanism is logically forced by the q-field dynamics -- was preserved and even reinforced ("without additional assumptions"). The supporting documents remain more honest than the main manuscript. This is the pattern throughout v2: strip problematic labels, keep problematic claims, soften verbs.

**What would constitute FIXED:** Either (a) label the separation mechanism as "Conjecture" or "Heuristic scenario" with explicit acknowledgment of unproven steps, or (b) provide the deferred full proof from the companion paper.

---

### 2. S1从"核心预言"→"容量约束": PARTIALLY FIXED

**v1 status:** S1 presented as the paper's "one clean experimental prediction," framed as distinguishing DGF from standard quantum mechanics. Straw man comparison: DGF in closed system vs. Lindblad in open system at T=0.

**v2 changes:**
- Framing: "The framework makes contact with experiment not through a single decisive prediction, but through constraints that any finite-capacity information system must satisfy."
- Explicit caveat added: "We emphasize that in closed-system microcanonical dynamics, DGF and standard quantum mechanics give the same prediction."
- The reflux bound is now called a "capacity constraint" and "not a 'smoking gun' that distinguishes DGF from all other theories."

**What is genuinely improved:**
- The claim is explicitly downgraded from "decisive prediction" to "constraint." This is a real reduction in claimed empirical force.
- The closed-system equivalence with standard QM is stated explicitly.
- The "not a smoking gun" language is honest.

**What is still problematic:**
- The Lindblad T=0 straw man comparison remains in the text: "In standard Lindblad theory at T=0, the probability of the qubit re-exciting after decaying to |g⟩ is strictly zero. The S1 reflux bound, in contrast, allows a finite upper limit." This continues to contrast DGF (closed system) with Lindblad (open system) -- an asymmetric comparison that REVIEWER B called FATAL.
- The operational proxy q_S ≈ T₂/(T₁+T₂) is still presented without stronger caveats about its heuristic nature. It says "can be operationally estimated as" -- which is gentler language but doesn't address REVIEWER B's demonstration that the proxy has structural bias (max value 0.67, never reaching q_S≈1).
- N_E estimation still says "a transmon qubit coupled to a readout cavity or ancilla qubit array" without the detailed feasibility analysis REVIEWER B demanded.

**Verdict: PARTIALLY FIXED.** The framing downgrade is genuine. The closed-system equivalence admission is genuine. But the straw man comparison structure (DGF-vs-Lindblad) is preserved, and the operational proxy caveats remain insufficient for an experimental physicist evaluating executability.

---

### 3. BM比较从"更强"→"互补": REWORDED

**v1 status:** DGF positioned itself as "stronger" than Bassani & Magueijo -- claiming to derive what BM takes as input. REVIEWER C demonstrated that DGF actually requires MORE inputs (5: G calibration, η, d=3, static assumption, a/c) than BM (1: unimodular gravity).

**v2 change:** §8.1 (Discussion): "BM provides the mechanism; DGF provides the architecture." The relationship is now framed as "complementary" and addressing "a different question."

**What did NOT change:**
- No honest input counting was added. The paper still does not acknowledge that DGF requires 5 external inputs to reach Laplace's equation while BM requires 1 to reach Einstein's equation.
- The "What is derived and what is not" table in §5.4 still presents "Derived structure: The Laplace/Poisson form... 1/r decay... Gauss's law structure... all follow from Eq. (q-field) in the static limit." The word "derived" obscures that these "derivations" require: d=3 dimension (input), static limit assumption (input), a/c identification (input), Gaussian calibration of κ (input). What is actually derived is only: "IF you assume a parabolic PDE ∂_t q = D₀∇²(1/q), THEN in its static limit you get ∇²(1/q)=0." This is a property of the PDE class, not a physical derivation.
- REVIEWER C's core critique -- that DGF's "derivation" is input-amplification disguised as logical deduction -- is not addressed.

**Verdict: REWORDED.** The competitive language ("we derive what they assume") was replaced with complementary language ("different questions"). The underlying mathematical situation -- DGF has more inputs than BM, not fewer -- was not discussed, and the word "derived" continues to obscure how many inputs are needed. This is the most transparent example of v2's strategy: change the framing, not the facts.

---

### 4. 引力从"推导"→"结构推导+G校准": PARTIALLY FIXED

**v1 status:** Spherical solution derivation blurred the line between derivation and calibration. C₁ = GM/c² presented as following from the Laplace equation, when it actually requires κ calibration to Newtonian gravity.

**v2 changes:**
- Explicit separation added: "The coupling constant κ is calibrated to 4πG/c² by matching to Newtonian gravity. The form of the equation is derived; the value of the coupling is measured."
- §5.4 categorizes outputs into "Derived structure," "Calibrated constants," and "Open."
- "Calibrated constants" explicitly lists G, η [kg/bit], and c.

**What is genuinely improved:**
- The form/vs/value distinction is now explicit. This is a real conceptual clarification.
- Acknowledging that G, η, and c are not derived is honest.

**What is still problematic:**
- The derivation text in §5.2 still reads: "This yields the Newtonian correspondence 1/q = 1 - Φ/c² where Φ = -GM/r." The flow suggests the correspondence emerges from the mathematics, when it actually requires the calibration step that was just (correctly) separated in the surrounding text. The derivation text itself was not rewritten -- the caveat was added around it.
- The claim "The 1/r decay is a geometric fact about the Laplace equation in d=3 dimensions, not a separate postulate about gravity" continues to obscure that d=3 is an input, not a derived fact. Gravity's 1/r² law being "a statement about the dimensionality of space" is true regardless of DGF -- it's a property of the Laplace equation, not a discovery of DGF.
- η [kg/bit] is still completely unconstrained (REVIEWER B, Attack 8). Admitting it's calibrated is honest, but the paper still draws physical conclusions from it (Table 1, "Earth is an extraordinarily quantum object") that depend on η having a specific value.
- The claim "gravity is weak because almost all information capacity is vacant" requires η to be small. But η is not derived -- it's fit. This means the "explanation" for gravity's weakness is circular: η is chosen to make the numbers work, then the numbers are presented as confirming the framework.

**Verdict: PARTIALLY FIXED.** The explicit calibration admission is a genuine improvement over v1. But the derivation text flow was not rewritten to reflect the calibration step, the d=3 input is still presented as an insight rather than an assumption, and η remains an unconstrained parameter used to generate "explanatory" numbers that are actually retro-fits.

---

### 5. 诚实边界移到正文: FIXED

**v1 status:** Honesty caveats were buried in §6 (experimental section) appendix-like notes, or absent from the main manuscript entirely (present only in supporting documents like continuum_qfield.md and gravity_theorems.md).

**v2 change:** §8 "Honest Boundaries" is a full, prominent section with two subsections.

**Content quality assessment:**
- "What the framework explains" (5 items): clearly stated, appropriately bounded.
- "What the framework does not explain" (5 items): includes c/ℏ/G values, d=3 dimensionality, QFT bridging, specific scale of quantum-classical boundary, gravitational waves.
- The specific scale admission is genuinely honest: "The framework explains that a boundary exists and why it is sharp. It does not explain why the boundary falls at approximately 10⁻⁶--10⁻¹⁰ m rather than, say, 10⁻³ m or 10⁻¹⁵ m."

**Comparison to v1:**
- "Cannot derive: propagation speed (currently parabolic, not hyperbolic)" -- was buried; now in main section.
- "No classical stationary solution exists that attains q=0" -- was in supporting doc only; now the section states the framework doesn't describe interior solutions.
- The "single most serious mismatch" (infinite propagation speed as continuum artifact) is now acknowledged in §4.2.

**Verdict: FIXED.** This is the one unambiguous improvement in v2. The honest boundaries are now a structural element of the paper, not an appendix afterthought. The content is substantive and covers the major limitations. The only minor criticism is that some limitations (e.g., the UMP/ergodicity assumptions in the statistical theorems) are still not tracked in this section.

---

### 6. IBM数据从"一致"→"不足以检验": PARTIALLY FIXED

**v1 status:** IBM data presented as "confirming" or "consistent with" DGF's reflux bound (39.2% upper bound satisfied by 5% observation). REVIEWER B called this the "most serious scientific integrity issue" -- a loose upper bound being satisfied by data was presented as empirical support.

**v2 change:** "Current experimental data (IBM 127-qubit processor) show trace distance revivals of approximately 5%, consistent with the reflux bound $q_S/q_E\approx 39\%$ but insufficient to test it."

**What is genuinely improved:**
- "Insufficient to test it" is an honest admission that was absent from v1.
- The word "confirm" was removed.

**What is still problematic:**
- "Consistent with" in physics literature means "the data and prediction agree within error bars." Here, the "agreement" is the trivial logical fact that 5% ≤ 39.2%. This is not empirical consistency -- it is logical satisfaction of an inequality by a value 8× below the bound. The word "consistent" carries connotations the logical situation does not support.
- A more honest formulation would be: "The reflux bound (≤39.2%) is not violated by current IBM data (~5%), but the bound is too loose to be tested by these data. A violation would require observing >39.2% reflux, which is far above typical experimental values."
- The paper still does not discuss the standard non-Markovian explanation for IBM's observed revivals (1/f noise, TLS defects), which REVIEWER B identified as an omission that creates a misleading impression of DGF's explanatory uniqueness.

**Verdict: PARTIALLY FIXED.** "Insufficient to test" is honest. "Consistent with" continues to borrow the scientific authority of that phrase for a situation that is purely logical, not empirical.

---

### 7. A3公理化: PARTIALLY FIXED

**v1 status:** A3 presented as an equal member of the "three axioms," obscuring that A1+A2 are nearly empty (as proven by A4_analysis.md) while A3 carries most of the physical content. REVIEWER C showed that A3 is independent and extremely restrictive (excludes almost all A1+A2-compatible dynamics).

**v2 changes:**
- §2.1 now says about locality: "This follows from finite propagation speed---a physical fact that the framework acknowledges as input rather than deriving."
- Introduction: "We do not prove this principle. We show that if you accept it as a definition..."
- Conclusion: "three definitional truths about information" (not "axioms")

**What is genuinely improved:**
- A3 is explicitly acknowledged as "input rather than deriving." In v1 this was not stated.
- The overall framing shifted from "axioms we prove things from" to "definitions we show consequences of."

**What is still problematic:**
- The deep asymmetry between A1+A2 (nearly empty -- they constrain almost nothing about dynamics) and A3 (extremely restrictive -- excludes almost all dynamics) is not discussed. v1's A4_analysis.md proved this asymmetry is a profound mathematical fact. v2 mentions A3 is "input" but does not explain WHY it needs to be input -- because A1+A2 alone are too weak.
- The paper still says "three definitional truths about information" -- but A3 (locality) is not "about information." It is about spacetime structure. Calling it a "truth about information" is category confusion.
- The Introduction's "we begin with three axioms that define what it means for a system to 'exist' and 'interact'" (from v1) was softened but the underlying claim -- that the axioms are definitional rather than postulational -- persists.
- REVIEWER C's demand for a discussion of "why 3 axioms rather than 2" was not met.

**Verdict: PARTIALLY FIXED.** Acknowledging A3 as "input" is a real improvement. But the asymmetry between the axioms is not explained, the category of A3 (spacetime, not information) is not clarified, and the paper still groups all three as if they emerge from the same conceptual source ("information").

---

### 8. 尺度问题: BROKEN_MORE

**v1 status:** Title claimed to explain "Why the Universe Looks Different at Different Scales." Paper did not derive any specific scale. REVIEWER C documented the claim-delivery gap: mechanism explained, specific scale not explained.

**v2 change:** Title is IDENTICAL: "Why the Universe Looks Different at Different Scales: Quantum, Classical, and Gravity as Phases of Finite Information"

**But the Honest Boundaries section now says:**
"The framework explains that a boundary exists and why it is sharp. It does not explain why the boundary falls at approximately 10⁻⁶--10⁻¹⁰ m rather than, say, 10⁻³ m or 10⁻¹⁵ m. This scale depends on the parameters a, c, and the initial q-gradient, none of which the framework predicts."

**The problem:** The title claims to explain "at Different Scales." The text explicitly admits it does NOT explain the scale. The title and the text now directly contradict each other. In v1, this was an unacknowledged gap. In v2, it is an **explicitly acknowledged** gap that the title continues to claim is closed.

This is worse than v1 because:
- v1: ambiguous claim, could be interpreted as about structure not numerical scale.
- v2: explicit admission that scale is not explained + title that says scale IS explained. The contradiction is now visible and documented. A reviewer will immediately flag this.

**Verdict: BROKEN_MORE.** v1 had a claim-delivery gap. v2 makes the gap explicit while keeping the claim. This transforms an ambiguous overclaim into a documented contradiction. The title should be changed to "Why the Quantum and Classical Worlds Separate" or "into Two Regimes" as REVIEWER C suggested.

---

## Special Attack: The Verb Replacement Strategy

**The strategy:** v2 systematically replaced epistemic operators throughout the paper:
- "prove" → "show"
- "Theorem 10" → unnamed paragraph
- "core prediction" → "capacity constraint"
- "consistent with" → "consistent with but insufficient to test"
- "we derive" → "we show" / "the structure is derived"
- "necessary" → (softened, but "follows from" preserved)
- "axiom" → "definitional truth"

**Conclusion (v2):** "These are not proofs. They are recognitions."

**Assessment of the strategy:**

The verb replacement is a GENUINE but INCOMPLETE epistemic downgrade. Genuinely: calling something a "recognition" rather than a "proof" lowers the burden the paper claims to meet. A paper that claims to "recognize" a structural correspondence is making a weaker claim than one that claims to "prove" a theorem. This matters for peer review.

But incompletely: the mathematical content that the verbs describe HAS NOT CHANGED. The same q-field equation. The same static limit. The same spherical solution. The same 5-step separation mechanism. The problems REVIEWER A identified -- the incomplete proof of separation, the unproven commutation of limits, the unverified gradient expansion, the conjectural singularity -- are all still there in the mathematics, regardless of what verb introduces them.

**The acid test:** If a reviewer reads v2's §4.4 ("The separation mechanism") and asks "Has this been proved?", the honest answer is still "No -- the proof sketch is incomplete, the full proof is deferred, and key steps rely on unverified approximations." The fact that v2 no longer calls it a "Theorem" makes this harder for a casual reviewer to notice, but it does not resolve the underlying mathematical gap.

**The verb replacement is a rhetorical improvement that makes v2 harder to reject but not more correct.**

---

## What v2 Did NOT Fix (Problems Shared by Both Versions)

These problems identified by REVIEWERs A/B/C appear in both v1 and v2 with identical or near-identical mathematical content:

| Problem | Reviewer | Severity | Status in v2 |
|---------|----------|----------|-------------|
| Continuum limit derivation lacks error bounds, smoothness assumptions, closure proof | A-SEVERE | Attack 3 | Unchanged -- still presented as direct derivation |
| Static limit: existence not proved, inner BC unspecified, q=0 interior incompatible | A-SEVERE | Attack 4 | Unchanged -- §5.4 mentions "static limit" as input but doesn't address existence |
| Fast diffusion m=-1: singularity is conjecture, post-singularity unexplored | A-SEVERE | Attack 5 | Unchanged -- still "Theorem" in §4.2, same conclusions drawn |
| UMP/ergodicity not derived from A1-A3, not tracked transparently | A-SEVERE | Attack 8 | Unchanged -- no assumption tracker added |
| q_S proxy T₂/(T₁+T₂) is heuristic, structural bias unaddressed | B-SEVERE | Attack 3 | Marginally addressed -- "operationally estimated" is softer but no bias analysis |
| N_E estimation has no independent verification scheme | B-SEVERE | Attack 4 | Unchanged |
| 35 mK thermal background issue not resolved | B-FATAL | Attack 5 | Mentioned as "experimental obstacle" but feasibility not re-evaluated |
| η completely unconstrained, gravity derivation hollow | B-SEVERE | Attack 8 | Admitted as "calibrated" but Table 1 still uses it as if derived |
| q's capacity-vs-state type confusion | C-SEVERE | Attack 3 | Unchanged -- both definitions still present, no resolution of tension |
| Parabolic vs. hyperbolic PDE incompatibility | C-SEVERE | Attack 5 | Admitted in Honest Boundaries but implications not discussed |
| "Information flow" as law vs. statistical tendency | C-MODERATE | Attack 7 | One-word fix: "statistically, not as an iron law" added to §6.2 |
| SOC analogy lacks quantitative features | C-MODERATE | Attack 4 | Unchanged -- still qualitative analogy without power-law distributions |

---

## Summary Table

| # | Fix Claimed | Status | Key Evidence |
|---|------------|--------|-------------|
| 1 | Theorem 10降级 | **REWORDED** | Label removed, claim preserved as "follows from... without additional assumptions" |
| 2 | S1预言→容量约束 | **PARTIALLY FIXED** | Framing genuinely downgraded; straw man comparison (DGF-vs-Lindblad) preserved |
| 3 | BM"更强"→"互补" | **REWORDED** | Competitive language replaced with complementary; honest input counting not added |
| 4 | 引力"推导"→"结构+G校准" | **PARTIALLY FIXED** | Form/vs/value distinction added; derivation text flow unchanged; η still unconstrained |
| 5 | 诚实边界移到正文 | **FIXED** | Full §8 section with substantive content; structural element, not appendix |
| 6 | IBM"一致"→"不足检验" | **PARTIALLY FIXED** | "Insufficient to test" is honest; "consistent with" still misleading; no discussion of standard explanation |
| 7 | A3公理化 | **PARTIALLY FIXED** | A3 acknowledged as "input"; asymmetry with A1+A2 not explained; still grouped as "information truth" |
| 8 | 尺度问题 | **BROKEN_MORE** | Title unchanged ("at Different Scales"); text now explicitly admits scale not explained; direct contradiction |
| -- | Verb replacement strategy | **MIXED** | Genuine epistemic downgrade but mathematical gaps unchanged; harder to reject, not more correct |

---

## Final Judgment

**Is v2 better than v1?** Yes, marginally. The verb replacement and the Honest Boundaries section make v2 more defensible in peer review -- a reviewer looking for overclaims will find fewer explicit ones.

**Is v2 good enough for PRD?** No. The core problems identified by three independent reviewers remain in the mathematics:
1. The separation mechanism (old Theorem 10) is still presented as logically forced by the dynamics, when the proof is incomplete.
2. The experimental section still contrasts DGF (closed system) with Lindblad (open system) -- a straw man.
3. The input-amplification structure (5 inputs → Laplace equation → claim "derived gravity") is obscured, not clarified.
4. The title now explicitly contradicts the text's own admissions about scale.

**The deepest issue:** v2 represents a REJECTION-AVOIDANCE strategy, not a TRUTH-SEEKING revision. The changes are designed to make the paper harder to reject -- softer verbs, moved caveats, explicit boundaries -- without addressing the underlying mathematical and conceptual gaps that the reviewers identified. The verb "prove" was replaced with "show," but the gap between what is shown and what is claimed remains.

**What a genuine fix would require:**
1. Conjecture labels where proofs are incomplete (separation mechanism, singularity formation).
2. Removal of the DGF-vs-Lindblad straw man -- or fair closed-system-vs-closed-system comparison.
3. Honest input counting: "To reach Laplace's equation from A1-A3, we need 5 additional inputs: d=3, static limit assumption, a/c identification, κ calibration to G, η for mass-information conversion."
4. Title change: "Different Scales" → "Two Regimes" or similar.
5. Assumption tracker: which theorems depend on UMP, ergodicity, flux ansatz, continuum validity.

**Bottom line: v2 would receive a softer rejection than v1, but still a rejection, because the same mathematical and empirical gaps that the reviewers identified are still present. They are just harder to find.**

---

*REVIEWER D audit completed 2026-06-06.*
