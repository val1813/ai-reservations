# REVIEWER A — Mathematical Rigor Audit

**Paper:** Information Capacity and the Quantum-Classical Separation (PRD submission)
**Reviewer:** A (Mathematical Physicist)
**Date:** 2026-06-06
**Verdict:** **Major revision required.** Two FATAL findings (Theorem 10 mislabeled, continuum flux ansatz gap unclosed). Five SEVERE findings. The paper contains genuine mathematical insights but overstates the epistemic status of key claims. The supporting documents (continuum_qfield.md, gravity_theorems.md) are consistently more honest than the main manuscript.

---

## Attack 1: A1+A2 → Bijection — the Injectivity Gap

**Claim under review:** Theorem 1 (Bijection) — "For any finite set X and injective map f: X→X, f is bijective."

**The gap:**

The proof is trivially correct: an injective map from a finite set to itself is surjective (pigeonhole principle, |f(X)| = |X| ⇒ f(X) = X). The problem is one step earlier: **why is f injective?**

Axiom A1 states: "States that differ can be distinguished." This is a statement about the existence of distinguishable states at a single time. The paper then asserts: "Axiom A1 requires f to be injective: distinguishable states remain distinguishable after evolution."

But A1 as formulated says nothing about dynamics. It does not assert that *if two states are distinguishable at time t, they must be distinguishable at time t+1*. That would be a distinct axiom: **A1' (Dynamic distinguishability):** The dynamics preserves the distinguishability relation, i.e., if s ≠ s', then f(s) ≠ f(s'). 

The gap is not fatal — the fix is a one-sentence reformulation:
> "Axiom A1 (Distinguishability): States that differ can be distinguished. Since `being distinguishable' is an operational property that cannot depend on when the observation is made, the dynamics f must preserve the distinguishability relation: if s ≠ s', then f(s) ≠ f(s')."

But as written, the paper conflates a static epistemological claim (states differ) with a dynamic constraint (evolution preserves difference). This is a logical step, not a deduction.

**Additional nuance:** Even with A1', injectivity requires that the state space is `{0,1}^N` — i.e., that the representation is faithful. If the representation overcounts (multiple labels for the same physical state), f could be non-injective on labels while preserving physical distinguishability. The paper assumes the labeling is faithful without comment.

**Severity: MODERATE**

The gap is fillable with a one-paragraph clarification. It does not threaten the theorem's truth, only its derivation from the stated axioms.

**Prejudged author rebuttal:** "The operational meaning of `distinguishable' is inherently dynamic — if two states become indistinguishable under evolution, they were never operationally distinct in the first place." This is a reasonable defense, but it should be stated explicitly in the axioms, not smuggled in during the proof.

---

## Attack 2: N=2 Counterexample → "Any Macroscopic Quantity" Non-Conservation

**Claim under review:** Theorem 1e (Non-conservation of occupancy) — the N=2, 4-cycle counterexample proves Hamming weight is not conserved. The surrounding text: "no specific macroscopic quantity need be conserved."

**The gap:**

The theorem *statement* is mathematically correct: "Axioms A1-A2 do NOT imply conservation of the total occupation number Σs_i." Proved by a single counterexample (N=2, f = (00→01→10→11→00)). This is sufficient to establish non-implication.

The problem is the surrounding interpretive text: "no specific macroscopic quantity need be conserved." This is a universal claim. From one counterexample disproving one specific quantity, the paper infers a general principle.

**What's missing:**

1. **Invariants of the permutation.** Every permutation on a finite set has invariants: cycle structure partition, parity (for even permutations), and any function that is constant on orbits. For the specific 4-cycle given, the quantity `Σs_i mod 2` is actually conserved (it alternates 0→1→1→0→0, and 0→1→1→0→0: check: 00→01 (0→1), 01→10 (1→1), 10→11 (1→2=0 mod 2), 11→00 (2=0 mod 2→0). No, wait: 00 has weight 0, 01 has weight 1, 10 has weight 1, 11 has weight 2. Evolution: 0→1→1→2→0. Mod 2: 0→1→1→0→0. Not conserved either. But the point stands: there may exist *some* macroscopic quantity that IS conserved for a given f, or for all f satisfying A3 (locality).

2. **No characterization of what CAN be conserved.** The paper never asks: what constraints does A3 (c-locality) place on possible invariants? A c-local bijection on a d-dimensional lattice may have conserved quantities (topological invariants, winding numbers) that the N=2 counterexample cannot address.

3. **The claim depends on a specific choice of "macroscopic quantity."** If we define "macroscopic quantity" as any function Q: X→R, then trivially Q(s) = constant is conserved. The paper's claim is implicitly about "nontrivial" macroscopic quantities, but "nontrivial" is not defined.

**Severity: MODERATE**

The narrow theorem statement is correct. The broader interpretive claim is unsubstantiated. The fix is to restrict the claim: "In particular, the total occupation number need not be conserved" rather than "no specific macroscopic quantity."

**Prejudged author rebuttal:** "The N=2 example is an existence proof of non-conservation for one observable. Since the framework aims to explain why observables are generally not conserved, a single counterexample to conservation is sufficient motivation." Partially valid, but does not justify the universal quantifier.

---

## Attack 3: Continuum Limit Derivation — Gradient Expansion and Closure

**Claim under review:** Theorem 4 (Continuum q-field equation) — ∂_t q = D₀∇²(1/q).

**The gap:**

The derivation in `continuum_qfield.md §II.A` performs a gradient expansion of the discrete flux to O(a²). The result ∂_t q = D₀∇²(1/q) follows from:

1. The flux ansatz J_{i→j} = 1/q_i − 1/q_j
2. Taylor expansion of q_j about x to O(a²)
3. Summation over 2d neighbors and identification of the discrete Laplacian
4. Dropping O(a⁴) terms

**Specific mathematical deficiencies:**

**(a) No error bound.** The O(a⁴) terms are dropped without estimating their magnitude relative to the leading O(a²) term. Near the q→0 singularity, derivatives of q may be large, potentially invalidating the truncation. The paper provides no condition on q(x,t) under which the truncation is justified.

**(b) Smoothness assumption.** The Taylor expansion requires q ∈ C³ in space. For the parabolic equation ∂_t q = D₀∇²(1/q), solutions are indeed smooth for t>0 when q>0 (standard parabolic regularity). But the initial data may be discontinuous (the discrete model starts with binary cells s_i ∈ {0,1}), and the q→0 regime breaks smoothness. The paper does not discuss instant smoothing or its failure at q=0.

**(c) Closure at the one-point level.** The discrete flux J_{i→j} = 1/q_i − 1/q_j assumes that the flux between cells i and j depends only on q_i and q_j — not on correlations, not on the states of other neighbors. This is a mean-field-type closure assumption. If the true dynamics involves multi-cell correlations, the continuum limit would produce higher-derivative terms (∇⁴, etc.) or nonlocal terms. The paper acknowledges this in continuum_qfield.md §VI.C but not in the main manuscript.

**(d) Commutation of limits.** The derivation takes N→∞, a→0, then t→∞ (for asymptotic analysis). It is not proved that these limits commute. In fast diffusion equations with finite-time singularities, the order of limits can matter.

**(e) The flux ansatz itself.** The form J = 1/q_i − 1/q_j is the "simplest nonlinearity with a pole at q=0" (continuum_qfield.md §I.B, Remark 1). It is not derived from A1-A3. This is honestly acknowledged in the supporting document but presented as a theorem in the main paper.

**Severity: SEVERE**

The derivation is formal, not rigorous. The paper should state clearly:
> "In the formal continuum limit (gradient expansion to leading order), the discrete dynamics yields..."

rather than presenting it as a theorem with a completed proof. The supporting document `continuum_qfield.md` is appropriately caveated; the main manuscript is not.

**Prejudged author rebuttal:** "All derivations of continuum equations from discrete models (hydrodynamic limits, kinetic theory) are formal at this level. Rigorous proofs exist only for linear or special nonlinear cases." True, but the paper should not label a formal derivation as a "Theorem." Call it "Derivation" or "Formal continuum limit."

---

## Attack 4: Static Limit — Existence and Uniqueness

**Claim under review:** Theorem 11 (Static-gravity correspondence) — "In the static limit ∂_t q = 0, the information potential u ≡ 1/q satisfies ∇²u = 0."

**The gap:**

Setting ∂_t q = 0 in the q-field PDE yields ∇²(1/q) = 0. This is mathematically correct as a necessary condition. But:

**(a) Existence of static solutions.** The paper assumes without proof that the time-dependent PDE ∂_t q = D₀∇²(1/q) admits time-independent solutions. For nonlinear PDEs, the existence of stationary solutions is not guaranteed by the steady-state equation alone — boundary conditions and domain geometry matter crucially.

Moreover, `continuum_qfield.md` Theorem 6(c) proves: "No classical stationary solution exists that attains q=0 at an interior point." This means the static equation CANNOT describe the interior of a "mass" (where q≈0). Yet the paper's central physical claim is precisely that the static q-field around a mass satisfies ∇²(1/q)=0. This is only valid **outside** the mass, where q>0. The paper acknowledges this in gravity_theorems.md §11.C3 but the main manuscript's Theorem 11 statement does not carry this restriction.

**(b) Uniqueness.** The Laplace equation ∇²u = 0 with Dirichlet boundary conditions on a bounded domain has a unique solution. But the physical domain is R³ minus the mass interior, with boundary conditions at infinity (u→1) and at the mass surface (unspecified!). The paper never specifies the inner boundary condition. The spherical solution assumes u(r) = 1 + C/r with C determined by Gauss's law, but this selects ONE particular solution among infinitely many harmonic functions that satisfy u(∞)=1 (e.g., u(r) = 1 + Σ C_lm r^{-l-1} Y_lm).

**(c) Well-posedness.** The paper uses the static equation to draw physical conclusions (the 1/r potential, the identification with gravity) without establishing that the static problem is well-posed. What are the correct boundary conditions at the mass surface? At infinity? Is the exterior problem uniquely solvable?

**Severity: SEVERE**

The static limit derivation is correct as far as it goes. The problem is that the paper draws global conclusions (the 1/r potential, the mass-scale table) from a local necessary condition without establishing existence, uniqueness, or proper boundary conditions.

**Prejudged author rebuttal:** "The exterior vacuum solution is uniquely determined by spherical symmetry and the boundary condition at infinity. For non-spherical mass distributions, the multipole expansion is standard." Valid for the exterior solution, but does not address the existence of static solutions in the first place.

---

## Attack 5: Fast Diffusion m=−1 — Singularity Handling

**Claim under review:** Theorem 6 (Fast diffusion classification) — the q-field equation belongs to the fast diffusion class m=−1, supercritical for d≥2.

**The mathematical facts (undisputed):**

- ∂_t q = D₀∇²(q^{-1}) maps to ∂_t u = ∇²(u^m) with m = −1 (setting u = q)
- For the standard fast diffusion equation ∂_t u = ∇²(u^m): m_c(d) = (d−2)/d
- d=2: m_c = 0, m=−1 < m_c → supercritical
- d=3: m_c = 1/3, m=−1 < m_c → supercritical
- Supercritical fast diffusion generically exhibits finite-time extinction (u→0 at some points in finite time)

The classification is correct.

**The gap:**

**(a) The standard theory is for m > 0.** The classification m=−1 is a formal analytic continuation of the fast diffusion equation ∂_t u = ∇²(u^m) to negative m. The standard theorems (existence, regularity, finite-time extinction) are proved for m > 0 (or m ≥ (d−2)/d for some results). Extrapolating these results to m = −1 requires justification that is not provided.

The paper in `continuum_qfield.md` §VI.D acknowledges this:
> "For m = −1, our equation ∂_t q = ∇²(q^{-1}) is a formal analytic continuation to negative m."

But this caveat is absent from the main manuscript.

**(b) The singularity is not handled.** For d≥2, finite-time singularities are expected. The paper:
- Labels finite-time singularity formation as "Conjecture 1" (continuum_qfield.md §III.C) — honest
- Provides a heuristic ODE argument for blow-up — not rigorous
- Does not discuss what happens AFTER the singularity forms
- Nevertheless claims physical conclusions (separation into two domains, stability of q≈0 cores, the gravitational field) that depend on post-singularity behavior

**(c) The physical cutoff is ad hoc.** The paper introduces q_min ∼ (a/L)^d as a "physical cutoff" below which the continuum description breaks down. This is plausible but unquantified — what is L? The coarse-graining length? The system size? The cutoff is not derived from the dynamics; it is imposed by hand.

**(d) Divergent diffusivity → infinite propagation speed.** The paper acknowledges this as "the single most serious mismatch between DGF and gravitational physics" (gravity_theorems.md §12.C1). This is honest. But the main manuscript buries this limitation in §6 ("What is Derived and What is Not") and does not flag it at Theorem 6 where it belongs.

**Severity: SEVERE**

The classification is correct but the physical conclusions drawn from it are not justified by the mathematics. The finite-time singularity is a conjecture, not a theorem, and post-singularity behavior is unexplored. The paper should not claim Theorem 10 (two-domain asymptotics) as established while its central mechanism (singularity formation) remains conjectural.

**Prejudged author rebuttal:** "The physical system has a natural cutoff at the lattice scale, so the mathematical singularity is a continuum artifact. The physical behavior at the cutoff is what matters." True, but then the paper should not use the continuum singularity properties (divergent diffusivity, self-organized criticality) as the mechanism for domain separation. If the continuum description breaks down at q_min, the physics at q < q_min is governed by the discrete dynamics, which has not been solved.

---

## Attack 6: Theorem 10 (Two-Domain Asymptotics) — Theorem or Conjecture?

**Claim under review:** Theorem 10 (Two-domain asymptotics) — "Under the q-field equation (5) with initial condition containing spatial inhomogeneity, the asymptotic state consists of compact q≈0 cores (classical objects) embedded in a q≈1/2 sea (quantum background)."

**The gap:**

This is the most serious finding in this review.

**In the main manuscript (main_prd.tex, line 202):**
The claim is presented as **Theorem 10** with a brief "proof" in the surrounding text:
- "The cores are stable: once a region reaches q≈0, the divergent diffusivity ensures it cannot return to higher q — any incoming information is immediately re-emitted."

**In the supporting document (continuum_qfield.md, §V.B, line 286-296):**
The SAME claim is presented as **Theorem 10** but with the qualification: "*Proof sketch.* ... Full proof deferred to a companion paper."

The "proof sketch" uses:
1. Gradient amplification: "regions where ∇²q < 0 experience ∂_t q > 0" — this is from the linearized equation, not the full nonlinear PDE near q=0.
2. Local ODE approximation: q_min³(t) = q_min³(0) − 3D₀|∇²q|t — this treats |∇²q| as constant near the minimum, which is not justified when q is small and gradients are large.
3. "Detailed asymptotics require singular perturbation theory at the interface" — this is an admission that the proof is incomplete.

**The misrepresentation:**

**The main manuscript presents as a Theorem what the supporting document admits is a proof sketch with a deferred full proof.** This is a FATAL misrepresentation of epistemic status. A statement whose proof is incomplete, and whose key steps rely on unverified approximations (ODE reduction, constant Laplacian), should be labeled a **Conjecture**, not a Theorem.

Furthermore:
- The claim that "cores are stable" depends on the divergent diffusivity D(q)→∞ as q→0, which itself is a continuum artifact (see Attack 5).
- The "entropic preference for q≈1/2" is a genuine theorem (Theorem 9 in continuum_qfield.md), but its role in maintaining the "quantum sea" is a physical interpretation, not a mathematical deduction.
- The "sharp interface" between domains is asserted without solving the interface equation. In Cahn-Hilliard-type equations, interface structure requires matched asymptotics; here it is simply claimed.

**Severity: FATAL**

This is not a difference of opinion about interpretation. It is a difference in epistemic category: a conjecture is being passed off as a theorem in the manuscript that will go to reviewers. The supporting document is honest about the status; the main manuscript is not. **This must be corrected before submission** — change "Theorem 10" to "Conjecture 1 (Two-domain asymptotics)" and clearly state which parts are proved and which are heuristic.

**Prejudged author rebuttal:** "The separation mechanism follows from the mathematical properties established in Theorems 4-9 (anti-diffusion, q→0 singularity, entropic preference at q=1/2, conservation of ∫q). Theorem 10 is a synthesis of these results." This conflates "the ingredients exist" with "the conclusion follows." Having flour, eggs, and sugar does not make a cake — you need to prove the baking process works. The interaction of anti-diffusion, singular diffusivity, and entropic preference is the hard part, and it has not been analyzed.

---

## Attack 7: Spherical Solution — Derivation or Back-Substitution?

**Claim under review:** Theorem 12 (Spherical weak-field solution) — 1/q(r) = 1 + GM/rc².

**The derivation (main_prd.tex, lines 239-241):**

> "In spherical symmetry, the Laplace equation is (1/r²)∂_r(r²∂_r u) = 0. Integrating twice: u(r) = −C₁/r + C₂. Boundary conditions: u(∞) = 1 ⇒ C₂ = 1; the mass M is identified from the Gauss flux ∮∇u·dS = 4πC₁ = κM, giving C₁ = GM/c²."

**What's honest:**
- The integration and boundary condition C₂ = 1 ✓
- The form u = 1 + C₁/r ✓

**What's not honest:**

The step "∮∇u·dS = 4πC₁ = κM, giving C₁ = GM/c²" contains two hidden calibrations:

1. **κ = 4πG/c² is not derived.** The paper defines κ by matching to the Newtonian Poisson equation ∇²Φ = 4πGρ. This is calibration, not derivation. The supporting document `gravity_theorems.md` §11.C1 explicitly says: "κ is not derived. G is a Level 4 (accidental) parameter."

2. **M enters through the Gauss law, which assumes the Poisson equation.** The static vacuum equation is ∇²u = 0. To relate the integration constant C₁ to a mass M, the paper invokes Gauss's law for the SOURCED equation ∇²u = −κρ_m. But this sourced equation is itself an assumption (mass = locked information × conversion factor η). The chain is:
   - ∇²u = −κρ_m ← postulated (Poisson form)
   - ρ_m = η·ρ_I ← postulated (mass-information proportionality)
   - κ = 4πG/c² ← calibrated (not derived)
   - C₁ = κM/4π = GM/c² ← follows from above

The derivation in the main paper makes it appear as if C₁ is determined by the Laplace equation alone with physically motivated boundary conditions, when in fact it requires the Newtonian calibration at three points.

**The paper's own honesty table (§5.4) says:**
- Derived: Laplace/Poisson form, 1/r decay, Gauss's law structure
- Not derived: numerical value of G, the mass-information conversion factor η

But the distinction between "the form 1/r" (derived) and "the coefficient GM/c²" (calibrated) is not clearly maintained in the proof text. The proof says "giving C₁ = GM/c²" which implies G and M and c enter naturally, when in fact they enter through the calibration of κ.

**Severity: SEVERE**

The derivation is mathematically correct once κ is fixed. The problem is presentational: the proof text in the main manuscript blurs the line between derived structure and calibrated constants. The supporting document `gravity_theorems.md` is honest about this; the main manuscript is not. The fix is to rewrite the proof to clearly separate:
1. u(r) = 1 + C₁/r (from Laplace equation + spherical symmetry + boundary condition)
2. C₁ = GM/c² (from calibration of κ to Newtonian gravity)

**Prejudged author rebuttal:** "We clearly state in §5.4 that G is not derived. The proof shows that once κ is fixed by matching to experiment, the 1/r potential follows." This is a valid defense if and only if the proof text is rewritten to make the calibration step explicit. Currently it reads as if C₁ is determined by the Gauss flux integral alone, which is misleading.

---

## Attack 8: Statistical Assumptions — UMP, Ergodicity, and the Continuum Limit

**Claims under review:** Theorems 2 (Entropy Identity), 3 (Kac Recurrence), and S1 (Reflux Bound).

**The gap:**

**(a) Theorem 2 (Entropy Identity) — MATHEMATICALLY CORRECT but physically ambiguous.**

The identity:
```
S[P'] − S[P] = E_{q'}[D[ρ'_{q'}∥μ_{q'}]] − E_q[D[ρ_q∥μ_q]]
```
holds exactly for any bijection f. The proof is "by direct computation" — this is a mathematical identity, not a physical claim requiring additional assumptions. **No gap here.**

However, the physical interpretation ("entropy can only increase when intra-fiber distribution is initially uniform") depends on the initial condition D[ρ_q∥μ_q] = 0. Why should the initial intra-fiber distribution be uniform? This is the standard assumption of equal a priori probability — reasonable for a system in equilibrium, but not derived from A1-A3. The paper acknowledges this implicitly by calling it a "lower bound from the initial condition."

**(b) Theorem 3 (Kac Recurrence) — requires ergodicity.**

The proof: "By Kac's lemma, for any ergodic dynamical system, the expected recurrence time equals the inverse of the stationary measure: ⟨T_rec⟩ = 1/π(s_S) = 2^{N_S}."

Kac's lemma applies to **ergodic, measure-preserving** dynamical systems. The paper assumes:
1. The dynamics f is ergodic (the orbit of almost every state visits all of X)
2. The stationary distribution is uniform over the 2^{N_S} subsystem states

Assumption 1 (ergodicity) is NOT implied by A1-A3. A bijection on a finite set can have multiple cycles (Kac's lemma applies within each cycle separately, giving ⟨T_rec⟩ = cycle length, which may be much less than 2^{N_S}).

Assumption 2 (uniform stationary measure) requires that the bijection f be measure-preserving with respect to the uniform measure — which follows from bijectivity only if f is a permutation sampled uniformly. But the physical dynamics is a specific permutation (determined by physical laws), not a random one.

The wording "under random bijective dynamics" in the theorem statement partially addresses this — but "random bijective dynamics" is not defined. Is it a uniformly random permutation? A random c-local permutation? The expected recurrence time depends on the distribution.

**(c) Theorem S1 (Reflux Bound) — depends on UMP.**

The Uniform Mixing Property (UMP) states: "macrostate transition probabilities are proportional to the number of accessible microstates." This is a maximum-entropy assumption — standard in equilibrium statistical mechanics, but an additional postulate beyond A1-A3.

UMP effectively assumes that the dynamics f thoroughly mixes microstates within each macrostate. This is a strong ergodicity-type assumption. For a specific physical f (e.g., a Hamiltonian flow), UMP may fail — the dynamics may preferentially connect certain microstates, leading to transition probabilities that deviate from the combinatorial ratios.

**(d) Statistical assumptions in the continuum limit.**

The discrete theorems rely on statistical assumptions (ergodicity, UMP). The continuum q-field PDE ∂_t q = D₀∇²(1/q) is deterministic. The connection between them requires a hydrodynamic limit argument: the deterministic PDE emerges from the random discrete dynamics under appropriate scaling.

This hydrodynamic limit is not proved in the paper. The derivation in continuum_qfield.md §II is a formal gradient expansion of a deterministic discrete equation — the randomness has already been coarse-grained away. But the step from "random bijection with UMP" to "deterministic discrete flux J = 1/q_i − 1/q_j" is not justified. The flux ansatz is a modeling choice, not a consequence of the statistical assumptions.

**The chain of unproven steps:**
```
A1+A2+A3 (axioms)
  → f is a bijection on {0,1}^N (Theorem 1) ✓
  → [+ UMP/ergodicity assumptions] → statistical properties (Theorems 2,3,S1)
  → [+ flux ansatz J=1/q_i−1/q_j] → discrete deterministic flux equation
  → [+ gradient expansion, a→0] → continuum PDE ∂_t q = D₀∇²(1/q)
  → [+ static limit] → Laplace equation ∇²(1/q)=0
  → [+ Newtonian calibration] → gravity
```

Each `[+ ...]` is an additional assumption not contained in A1-A3. The paper is transparent about some of these (the flux ansatz is acknowledged as "not derived from the bare DGF axiom" in continuum_qfield.md §I.B), but not about the statistical ones.

**Severity: SEVERE**

The mathematical theorems (1, 2) are correct within their stated assumptions. The problem is that the assumptions multiply as the paper progresses, and the later theorems (10, 11, 12) inherit uncertainties from all the earlier assumptions. The paper should include a "dependency graph" showing which theorems depend on which assumptions beyond A1-A3.

**Prejudged author rebuttal:** "The UMP/ergodicity assumptions are the standard assumptions of statistical mechanics. We are not claiming to derive statistical mechanics from A1-A3; we are using it as a tool." Reasonable, but then the paper should state these as explicit postulates (A4: Uniform Mixing Property, A5: Ergodicity of the physically relevant dynamics) rather than invoking them implicitly.

---

## Summary of Findings

| # | Attack | Severity | Core Issue |
|---|--------|----------|------------|
| 1 | A1→injectivity gap | MODERATE | A1 as stated does not imply dynamic distinguishability; fixable with one sentence |
| 2 | N=2→"any macroscopic quantity" | MODERATE | Counterexample disproves one quantity; universal claim unsubstantiated |
| 3 | Continuum limit derivation | SEVERE | Formal gradient expansion, no error bounds, no convergence proof; labeled as Theorem |
| 4 | Static limit existence/uniqueness | SEVERE | No existence proof; inner boundary condition unspecified; q=0 interior incompatible |
| 5 | Fast diffusion singularity | SEVERE | Singularity conjectured not proved; post-singularity behavior unexplored; conclusions drawn anyway |
| 6 | Theorem 10 status | **FATAL** | Supporting doc admits "proof sketch, full proof deferred"; main ms labels as Theorem |
| 7 | Spherical solution calibration | SEVERE | C₁ = GM/c² requires κ calibration; proof text blurs derivation vs. calibration |
| 8 | Statistical assumptions | SEVERE | UMP/ergodicity not derived from A1-A3; continuum limit of stochastic discrete model not established |

---

## Consistency Check: Main Manuscript vs. Supporting Documents

A notable pattern emerged during this review: **the supporting documents are consistently more honest than the main manuscript.**

| Claim | Main Manuscript (main_prd.tex) | Supporting Document |
|-------|-------------------------------|---------------------|
| Continuum PDE derivation | "Theorem 4" with proof | "Formally derived" (continuum_qfield.md §VI.C: "The derivation is formal") |
| Finite-time singularity | Used as mechanism for separation (Theorem 10) | "Conjecture 1" (continuum_qfield.md §III.C: "rigorous proof is mathematically nontrivial") |
| Two-domain asymptotics | Theorem 10 | "Proof sketch... Full proof deferred" (continuum_qfield.md §V.B) |
| κ = 4πG/c² | Presented as part of the derivation | "κ is not derived" (gravity_theorems.md §11.C1: "Calibrated") |
| Static solutions with q=0 | Not discussed | Theorem 6(c): "No classical stationary solution exists that attains q=0" (continuum_qfield.md §III.B) |
| Infinite propagation speed | Buried in §6 | "The single most serious mismatch" (gravity_theorems.md §12.C1) |

This pattern suggests that the main manuscript has been "upgraded" in certainty during the writing process. The supporting technical documents reflect the actual state of the mathematics; the main manuscript overstates it.

**The single most important fix:** Downgrade Theorem 10 to Conjecture 1, and carry its caveats through all subsequent claims that depend on it (the separation mechanism, the stability of classical cores).

---

## Overall Assessment

The paper contains a genuinely interesting mathematical structure: a discrete information-theoretic model whose continuum limit is a nonlinear diffusion equation structurally related to the Laplace equation. The key results (Theorems 1-3, the continuum PDE form, the static limit ∇²(1/q)=0) are mathematically sound within their stated assumptions.

However, the paper overreaches in two fatal ways:
1. **Theorem 10 is not a theorem.** It is a heuristic synthesis of proved ingredients with an unproved conclusion.
2. **The chain of additional assumptions** (UMP, ergodicity, flux ansatz, gradient expansion validity, commutation of limits) is not tracked transparently.

**Recommendation: Major revision.** All FATAL and SEVERE findings must be addressed before resubmission. The supporting documents provide a template for the appropriate level of honesty.

---

## Appendix: Suggested Fixes

### Fix 1 (Attack 1): Clarify A1
Replace A1 with: "**A1 (Dynamic Distinguishability):** If two states are distinguishable, they remain distinguishable under time evolution. Equivalently, the dynamics f is injective."

### Fix 2 (Attack 2): Narrow the claim
Change "no specific macroscopic quantity need be conserved" to "in particular, the total occupation number is not conserved (Theorem 1e)."

### Fix 3 (Attack 3): Downgrade Theorem status
Label the continuum derivation as "Formal Continuum Limit" rather than "Theorem 4." Add a subsection on "Validity and Limitations of the Gradient Expansion."

### Fix 4 (Attack 4): Add caveat to Theorem 11
Add the restriction: "The static equation ∇²(1/q)=0 is valid in regions where q>0 and the q-field has reached a stationary state. It does not describe the interior of regions where q→0."

### Fix 5 (Attack 5): Separate conjecture from conclusion
State Conjecture 1 (finite-time singularity) explicitly. Do not use its properties to prove Theorem 10.

### Fix 6 (Attack 6): FATAL — relabel Theorem 10
Change "Theorem 10 (Two-domain asymptotics)" to "Conjecture 1 (Two-domain asymptotics)." State the evidence (gradient amplification in linearized regime, singular diffusivity, entropic preference) but acknowledge that the full nonlinear interaction of these mechanisms has not been proved.

### Fix 7 (Attack 7): Separate derivation from calibration
Rewrite the proof of Theorem 12 as:
1. u(r) = 1 + C₁/r (from Laplace equation + spherical symmetry + u(∞)=1)
2. C₁ = GM/c² (by calibrating κ = 4πG/c² to match Newtonian gravity)

### Fix 8 (Attack 8): Add assumption tracker
Add a table or dependency graph: "Assumptions Beyond A1-A3." Track which theorems depend on UMP, ergodicity, the flux ansatz, and the continuum limit validity.

---

*Review completed 2026-06-06. File under: `synthesis/REVIEWER_A_math.md`*
