# Referee Report — PRL Manuscript: "Second Scaling Exponent for Off-Diagonal Coherence in Power-Law Hopping Nonequilibrium Steady States"

**Reviewer:** Theoretical Physicist (Quantum Many-Body Theory / Statistical Physics)
**Recommendation:** Reject with encouragement to resubmit to a specialized journal (Phys. Rev. B or Phys. Rev. E) after addressing the fundamental concerns below.

---

## Overview

This manuscript studies the boundary-driven free-fermion chain with power-law hopping and bulk dephasing, proposes a "second independent scaling exponent" beta(alpha) for the spatial decay of off-diagonal coherence, fits it to a 1/alpha functional form, claims a "speed-coherence trade-off" anti-correlation with the transport exponent mu(alpha), and performs a universality test by varying boundary parameters. The numerical work is competent at the level of solving Lyapunov equations for systems up to L=64. However, the conceptual framework, the claimed novelty, and the strength of the conclusions all fall substantially short of the PRL standard. I detail my concerns below.

---

## 1. The Claimed "Independence" of beta from mu Is Not Established

This is the most serious conceptual flaw in the paper.

### 1.1 Both exponents are controlled by the same Liouvillian

The authors define mu from the diagonal sector (occupation numbers, governing current) and beta from the off-diagonal sector (coherence decay). They then claim these are "independent scaling dimensions." But the entire NESS is determined by a single Liouvillian L. The Lyapunov equation:

$$-i[h, C] + \{\Gamma, C\} + \gamma_\phi (C - \text{diag}(C)) = S$$

couples the diagonal and off-diagonal sectors through the commutator -i[h, C]. The off-diagonal sector is not independently driven — the source term S is purely diagonal. The off-diagonal elements of C are generated *entirely* through the commutator with the Hamiltonian, which transmits the diagonal occupation gradient into off-diagonal coherences.

The authors' own analysis script (`analyze_lyapunov_structure.py`) confirms this: it verifies the first-order relation

$$O_{ij} \approx -\frac{h_{ij}}{\gamma_\phi}(D_j - D_i)$$

numerically. This means the off-diagonal coherence |C_{ij}| is, to leading order, proportional to h_{ij} times the occupation *difference* between sites i and j. The spatial decay of |C_{ij}| is therefore largely determined by (a) the power-law decay of h_{ij} ~ |i-j|^{-alpha}, and (b) the spatial decay of the occupation gradient, which is itself controlled by the same transport physics that produces mu.

### 1.2 The "nonzero Jacobian" argument is mathematically vacuous

The authors argue that "the Jacobian d(beta,mu)/d(alpha,gamma_phi) is nonzero, formally establishing beta and mu as independent scaling dimensions." This is a trivial statement. Any two functions that are not identically equal will have a nonzero Jacobian generically. Consider f(x) = x^2 and g(x) = x^3. Their Jacobian with respect to x is nonzero — are they "independent"? In any meaningful physical sense, no: both are functions of the single variable x. The relevant question is whether beta and mu are functions of the *same underlying parameters* with no additional degrees of freedom, and the answer is yes: both are determined by (alpha, gamma_phi), and both are properties of the same C-matrix solving the same Lyapunov equation.

### 1.3 The burden of proof for "independence" is not met

To claim independence, the authors would need to:
- Identify a physical control parameter that changes beta while leaving mu strictly invariant (not just "approximately" — the statement dmu/d(gamma_phi) ~ 0 from the literature is an approximation, not a theorem).
- OR identify an observable that directly probes the off-diagonal sector without contamination from the diagonal transport physics.
- OR demonstrate that beta can be computed from first principles without reference to the diagonal occupation profile.

The authors have done none of these. Instead, they have observed that two different projections of the same NESS produce different numerical values when functions are fit to their scaling with L. That is expected; it is not evidence of independence.

---

## 2. The "Universality Class" Claim Is Grossly Overstated

### 2.1 One model, one dimension, zero interactions

The term "universality class" in PRL implies invariance of critical exponents across microscopically distinct systems. The authors test exactly one model (free fermions with quadratic Hamiltonian). They vary no microscopic details except boundary coupling strength Gamma (a factor of 4) and driving bias Delta-f (a factor of 5). These are *boundary conditions*, not model parameters. A genuine universality test would vary:
- The lattice structure (square, triangular, honeycomb, random graph)
- The spatial dimension (d=2, d=3)
- The nature of the hopping (e.g., add disorder, use different J(r) functional forms beyond pure power-law)
- Whether interactions are present (the authors explicitly relegate this to "future work")

The authors' own "firewall 2" results (for the XXZ chain with Delta != 0) are buried in the supplementary data and explicitly acknowledged to break the pure-imaginary structure — but this is never discussed in the manuscript body. The reader is left with the false impression that the claimed universality class has survived an interaction test.

### 2.2 The firewall test measures measurement robustness, not universality

Varying Gamma at fixed gamma_phi is equivalent to changing the ratio of boundary to bulk dephasing rates. The authors find beta varies by 6.84% — which they classify as "weak dependence." But this variation is *monotonic* with Gamma (beta decreases smoothly from 0.9525 to 0.8782 as Gamma increases from 0.5 to 2.0). This is not random scatter around a universal value; it is a systematic trend. For a true universal exponent, one expects convergence to a constant value in the scaling limit, not 7% systematic drift across a modest factor-of-4 scan. The authors attribute this drift to "Gamma renormalizing the effective dephasing" — but this is precisely an admission that beta is not independent of the boundary coupling scale.

### 2.3 Small system sizes undermine the scaling analysis

All power-law fits use five system sizes: L = 4, 8, 16, 32, 64. The smallest systems (L = 4, 8) are dominated by boundary effects and are far from any scaling regime. Fitting a power law to 5 points, of which 2-3 are in the boundary-dominated regime, can produce spurious R^2 values. With only three points in any plausible "scaling regime" (L >= 16), the determination of beta is underdetermined. The authors should at minimum:
- Demonstrate that the fitted beta is stable under exclusion of L=4 and L=8
- Show that L=128 (achievable with sparse solvers for free fermions) confirms the scaling
- Report and propagate systematic uncertainties from the choice of fitting range, not just statistical uncertainties from the log-log linear regression

---

## 3. The "Generalization" of the Bhat-Znidaric Theorem Is Trivial

The authors state: "We generalize Bhat and Znidaric's pure imaginary off-diagonal theorem from nearest-neighbor to power-law hopping." Let me be precise about what this generalization consists of.

Bhat and Znidaric (PRB 111, 174306, 2025) proved that for a nearest-neighbor XX chain with on-site dephasing and boundary driving, Re(C_{i!=j}) = 0. Their proof relies on three conditions:
1. The hopping matrix h_{ij} is real and symmetric.
2. The jump operators are linear in fermion operators.
3. The dephasing acts on-site.

Power-law hopping satisfies condition (1) trivially: h_{ij} = J_0 |i-j|^{-alpha} is manifestly real and symmetric. Conditions (2) and (3) are unchanged. The proof goes through *verbatim* — not a single line of the argument needs modification. The Lyapunov equation separates into decoupled real and imaginary sectors regardless of whether h_{ij} = delta_{|i-j|,1} or h_{ij} = |i-j|^{-alpha}.

This is not a "generalization" — it is the *same theorem* applied to a different instance of the same class of hopping matrices. It is an observation that belongs in a remark, not a claimed theoretical contribution in a PRL.

The authors' numerical verification that |Re(C_{i!=j})| < 10^{-15} is a useful sanity check but does not constitute a result.

---

## 4. The "Speed-Coherence Trade-off" Is a Mathematical Tautology

### 4.1 The anti-correlation follows from monotonicity in alpha alone

The authors define the "speed-coherence trade-off" as d(beta)/d(mu) < 0. Let us compute this derivative using the chain rule:

$$\frac{d\beta}{d\mu} = \frac{d\beta/d\alpha}{d\mu/d\alpha}$$

For alpha < 3/2, mu(alpha) = 2*alpha - 2 (from Dhawan et al.), so d(mu)/d(alpha) = 2 > 0.

From the authors' own Table 1, beta decreases monotonically with alpha at every fixed gamma_phi >= 0.1:
- gamma_phi = 0.5: beta goes from 1.172 (alpha=1.1) to 0.872 (alpha=1.9), so d(beta)/d(alpha) < 0.
- gamma_phi = 0.1: beta goes from 0.739 (alpha=1.1) to 0.602 (alpha=1.9), same sign.
- gamma_phi = 1.0, 2.0: same.

Therefore d(beta)/d(mu) = (negative)/(positive) < 0 is automatic. It is not a discovery — it is a logical consequence of two independently monotonic dependences on alpha with opposite signs.

### 4.2 The "trade-off" is a spurious correlation from alpha parameterization

To see why this is not a physical trade-off, consider an analogy. Define f(x) = x and g(x) = 1/x. Then df/dg = -x^2 < 0 for all x > 0. Would we claim there is a "speed-coherence trade-off" between f and g? No — these are simply two different functions of the same parameter x. Their anti-correlation carries no physical content beyond the fact that one is increasing and the other is decreasing with x.

The authors' situation is structurally identical. Beta and mu are both functions of alpha. The "trade-off" is entirely encoded in the signs of their individual derivatives with respect to alpha. It does not represent a constraint between physically independent quantities — it represents two different projections of the same underlying parameter dependence.

### 4.3 What would constitute a genuine trade-off

A genuine speed-coherence trade-off would require holding alpha fixed (same hopping range) and varying some *other* parameter (e.g., the dephasing rate gamma_phi, or the boundary driving strength) while observing that systems with intrinsically faster transport exhibit intrinsically faster coherence decay. The authors never perform this test. For fixed alpha and varying gamma_phi, the transport exponent mu is approximately constant (dmu/d(gamma_phi) ~ 0), so there is no "trade-off" to observe — mu doesn't move while beta does.

### 4.4 The "four physical constants" check is a red herring

The authors verify that "beta + mu != const, beta*mu != const, beta^2 + mu^2 != const, and beta - |mu-1| != 0." This is a bizarre list of quantities to check. These are ad-hoc algebraic combinations with no physical motivation. The fact that beta*mu is not constant does not demonstrate that beta and mu are independent — it merely demonstrates that they are not reciprocals. The authors could check 100 such combinations; the failure of each one proves nothing about independence.

---

## 5. The Functional Form beta = a/alpha + b Is Underexplained

### 5.1 The "derivation" is not presented

The manuscript states that "The 1/alpha functional form is derived from a scaling analysis of the fractional diffusion equation that governs the steady-state density profile." This derivation appears nowhere in the manuscript or its supplementary material. The reader is given a hand-waving sketch: "the nonlocal dispersion relation epsilon(k) ~ |k|^{2*alpha-1} ... combined with the nonlocal Robin boundary conditions ... produces a boundary layer whose width scales with alpha. The competition between nonlocal transport and boundary-induced dephasing yields the 1/alpha form."

This is not a derivation. It is a plausibility argument. A derivation would:
- Start from the exact Lyapunov equation for C_{ij}
- Derive the closed equation for the diagonal occupation D_i (the authors' own analysis shows this involves [h, O]_{ii}, which is a second-order coupling back to the off-diagonal sector)
- Extract the scaling of |C_mid| from this equation in the large-L limit
- Produce a(alpha,gamma_phi) and b(alpha,gamma_phi) from first principles

The authors have done none of this. What they have is a fit: beta = a/alpha + b with two free parameters per gamma_phi. Five data points per gamma_phi (5 alpha values) are fit with two parameters — the excellent R^2 is unremarkable. A two-parameter fit to five points will always have high R^2 unless the data are pathological.

### 5.2 Alternative functional forms are not tested

The authors fit beta(alpha) = a/alpha + b but do not test alternatives. For example:
- beta = a/alpha^2 + b (diffusive-inspired form)
- beta = a*exp(-alpha) + b (exponential, as might arise from localization physics)
- beta = a/(alpha - alpha_c)^nu + b (critical form with an adjustable alpha_c)

Without comparing against alternatives, the 1/alpha form is merely an empirical fit, not a theoretically established result. The authors claim "RMSE = 0.015 and R^2 > 0.999" as evidence for the 1/alpha form, but with only 5 data points and 2 free parameters, many functional forms would achieve comparable or better fits.

---

## 6. Comparison with PRL-Standard References Reveals the Gap

The authors cite two recent PRB papers (Dhawan et al. PRB 2024, Costa et al. arXiv 2025) as context. These papers set the standard for what constitutes a significant contribution in this subfield:

- **Dhawan et al. (PRB 110, L081403, 2024):** This is a Letter (not a full article) — and it provides an *analytic derivation* of mu(alpha) = 2*alpha - 2 from the non-equilibrium Green's function formalism, with a non-perturbative treatment of the power-law hopping. The transport exponent is derived, not fit.

- **Costa et al. (arXiv:2504.00188, 2025):** Develops a gauge-trick methodology that reveals the mathematical structure of FCS for noisy fermion systems. The contribution is methodological — a new way to compute things — not just a new number.

In contrast, the present manuscript:
- Does not derive beta analytically; it fits it numerically
- Does not introduce a new method; it uses standard Lyapunov equation solvers
- Does not prove a new theorem; the pure-imaginary property is a trivial extension of Bhat-Znidaric
- Does not validate across multiple models; only free fermions are studied

The contribution reduces to: "We computed |C_mid| for 25 (alpha, gamma_phi) pairs, fit power laws in L, and found beta decreases with alpha." This is a numerical observation, not a theoretical advance. It belongs in PRB as a regular article with a more cautious interpretation.

---

## 7. Additional Technical Concerns

### 7.1 The midchain coherence proxy is arbitrary

The authors define |C_mid| = |C_{L/2-1, L/2}|, the coherence between the two central sites. Why this specific pair? The off-diagonal coherence spans all i != j, with a structure that depends on both the separation r = |i-j| and the position relative to the boundaries. Reducing this entire structure to a single matrix element is a drastic simplification. Do other off-diagonal elements (e.g., C_{1,L}, C_{L/4, 3L/4}) show the same beta? If not, beta is not a property of the NESS but of the particular element chosen. The authors should demonstrate that all off-diagonal elements at a given separation r decay with the same exponent — a property that is not obvious given the inhomogeneous density profile.

### 7.2 The gamma_phi = 0.01 data are too noisy for the claims made

The authors acknowledge that beta fits at gamma_phi = 0.01 have R^2 ~ 0.87-0.89 and ~20% uncertainty. Yet these data points are included in Figure 2 (beta vs mu) and in the argument for the anti-correlation (where they are noted as "statistically consistent with zero within 1sigma, but slope remains negative"). If the slope is consistent with zero, the data do not support the anti-correlation claim for this regime. The inclusion of these noisy points to buttress a trend is misleading.

### 7.3 Pre-registered criteria are not explained

The authors refer to "pre-registered criteria (universal: <5%; weak dependence: 5-10%; non-universal: >10%)" for the firewall test. These criteria are arbitrary. Why 5% and 10%? Are these thresholds grounded in any statistical principle, or are they post-hoc choices designed to place the observed 6.84% in the "weak dependence" rather than "non-universal" category? Pre-registration is a safeguard against p-hacking, but the thresholds themselves must be justified.

---

## Summary and Recommendation

The paper presents a competent numerical study of coherence decay in a boundary-driven free-fermion chain, but the claims substantially outstrip what has been demonstrated:

1. **"Independent" exponent:** Not established. Beta is coupled to mu through the same Liouvillian and the same Lyapunov equation. The off-diagonal coherence is sourced by the diagonal occupation gradient through the commutator with the Hamiltonian.

2. **"Universality class":** Not established. One model (free fermions), one dimension, zero interactions, no variation of lattice geometry or hopping functional form. The firewall test varies boundary conditions, not model universality class.

3. **"Speed-coherence trade-off":** A mathematical tautology. Both beta and mu are monotonic functions of alpha with opposite signs; their anti-correlation follows from the chain rule alone. No independent physical constraint is demonstrated.

4. **"Generalization" of Bhat-Znidaric:** Trivial. The proof structure is unchanged when h_{ij} = |i-j|^{-alpha} replaces h_{ij} = delta_{|i-j|,1}.

5. **Functional form beta = a/alpha + b:** An empirical fit to 5 data points per gamma_phi with 2 free parameters. The claimed "derivation" from fractional diffusion is not presented.

The numerical data are sound, and the observation that |C_mid| ~ L^{-beta} with beta decreasing in alpha is a genuine empirical finding. But it is a single finding on a single model, and the theoretical interpretation overreaches substantially. **I recommend rejection from PRL**, with the suggestion that a revised manuscript, stripped of the unwarranted "universality class" and "independent exponent" language and reframed as a numerical study of coherence scaling in power-law hopping chains, could be suitable for Physical Review B.

---

## Specific Required Revisions (if the authors wish to resubmit to PRL)

1. Either derive beta analytically from the Lyapunov equation (not just fit it), or retract the claim that the functional form is "derived."

2. Provide a rigorous definition of "independence" for two scaling exponents and prove that beta and mu satisfy it, or retract the claim.

3. Test at least one distinct model class (e.g., interacting XXZ, disordered chain, two-dimensional square lattice) before invoking "universality class."

4. Compute d(beta)/d(alpha) and d(mu)/d(alpha) explicitly and demonstrate that d(beta)/d(mu) < 0 encodes physics beyond the signs of these individual derivatives.

5. Extend calculations to L >= 128 (entirely feasible for free fermions using sparse solvers) and demonstrate stability of beta fitting under exclusion of boundary-dominated small-L data.

6. Present the fractional diffusion derivation in full, or honestly label the 1/alpha form as an empirical observation.
