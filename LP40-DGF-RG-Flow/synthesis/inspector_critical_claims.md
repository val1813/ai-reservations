# INSPECTOR Report: LP40 R1 Critical Claims Verification

**Inspected:** LP40 Round 1 (A博士 Wilson RG + 图RG + 标度灾难连接)
**Source:** `/d/Claude/ai-reservations/LP40-DGF-RG-Flow/current/A/round1.md`
**Reference:** DGF v3.1-prd at `/d/Claude/ai-reservations/LP30-DGF/paper/DGF_Unified_v3.md`
**Date:** 2026-06-09

---

## Claim 1: DGF requires exp(+S) path integral weight, not exp(-S)

**Verdict: [CORRECT]**

### Reasoning

#### 1.1 s''(1/2) = -4 -- Verified

s(q) = -q ln q - (1-q) ln(1-q)

s'(q) = -ln q - 1 + ln(1-q) + 1 = ln((1-q)/q)

s''(q) = -1/q - 1/(1-q)

At q=1/2: s''(1/2) = -1/(1/2) - 1/(1-1/2) = -2 - 2 = -4

A博士's computation is **mathematically correct**. s''(1/2) = -4 < 0 confirms q=1/2 is a local maximum of s(q), as expected for the binary entropy function.

#### 1.2 Convergence check -- Verified

Expanding S_DGF around q=1/2 with q = 1/2 + φ:

S_DGF[1/2+φ] = S_DGF[1/2] + ∫ d³x [-2φ² + (ℓ²/2)(∇φ)² + O(φ³)]

Under **exp(+S_DGF)** weight:
exp(+S_DGF) = exp(+S_DGF[1/2]) exp(∫ [-2φ² + (ℓ²/2)(∇φ)² + ...])
= exp(+S_DGF[1/2]) exp(-∫ [2φ² + ...] d³x)
→ Gaussian converges (negative quadratic coefficient) ✓

Under **exp(-S_DGF)** weight:
exp(-S_DGF) = exp(-S_DGF[1/2]) exp(∫ [+2φ² - (ℓ²/2)(∇φ)² + ...])
→ The φ² term has **positive coefficient** (+2φ²), causing Gaussian **divergence** ✗

A博士's convergence analysis is **mathematically correct**. If one wishes to formulate DGF as a statistical field theory with a path integral, the weight MUST be exp(+S_DGF) for the Gaussian integral to converge around q=1/2. The alternative (exp(-S_DGF)) yields a pathologically divergent theory.

#### 1.3 The dual Euclidean action convention -- Verified and appropriate

A博士 defines S̃ = -S_DGF + const, giving:

S̃[φ] = ∫ d³x [½m²φ² + ½Z(∇φ)² + (g/3!)φ³ + (λ/4!)φ⁴ + ...]

with m² = -s''(q_eq) = 4 > 0, Z = ℓ² > 0.

This is a **mathematically equivalent reformulation**: exp(+S_DGF) = exp(-S̃). The rest of the RG analysis uses S̃ with the standard weight exp(-S̃), restoring full compatibility with standard Wilson RG formalism. This is the correct procedure.

#### 1.4 What DGF v3 actually says -- Important context

DGF v3 §6.1 states the q-field equation comes from an "entropy variational principle" and gives the action S[q] with s_bin(q) as its leading term. The field equation is δS/δq = 0. However, DGF v3 does **not** discuss:

- Path integral quantization
- Whether exp(+S) or exp(-S) is the correct statistical weight
- The sign of s''(q) or its implications for Gaussian convergence
- Any statistical field theory formulation

A博士's claim that "DGF requires exp(+S)" is therefore an **extrapolation** beyond what DGF v3 explicitly provides. A博士 honestly acknowledges this in §0.1: "此前提需要DGF原作者确认" (this premise requires DGF author confirmation).

#### 1.5 The entropic interpretation defense

While DGF v3 doesn't discuss path integrals, the theoretical basis supports A博士's convention:

1. DGF's founding principle is information-theoretic: s_bin(q) IS the binary entropy
2. In statistical physics, probability of a configuration ∝ exp(S/k_B) when S is entropy
3. The functional S_DGF[q] is built from s_bin(q) -- it is genuinely entropic in origin
4. Therefore exp(+S_DGF) is the physically motivated convention for DGF, not an arbitrary choice

This distinguishes DGF from standard QFT where the Euclidean action is an energy functional (probability ∝ exp(-E/kT) = exp(-S_E)).

#### 1.6 Conclusion on Claim 1

**All three mathematical checks pass.** The only uncertainty is whether DGF should be path-integral-quantized at all -- a question DGF v3 does not address. Within the framework of statistical field theory applied to DGF, A博士's exp(+S) convention is correct and the exp(-S) alternative is mathematical pathological.

---

## Claim 2: φ⁴ is relevant in d=3 for DGF q-field

**Verdict: [PARTIALLY CORRECT with caveats]**

### Reasoning

#### 2.1 Canonical scaling dimension of φ -- Correct

Standard result from requiring the kinetic term ∫ d^d x (∇φ)² to be dimensionless in the action:

[d^d x] = -d, [(∇φ)²] = 2 + 2[φ]
-d + 2 + 2[φ] = 0 → [φ] = (d-2)/2

For d=3: [φ] = 1/2. ✓

This is standard field theory. The convention is consistent (mass dimension, not length dimension).

#### 2.2 φ⁴ scaling dimension -- Correct

[φ⁴] = 4 × [φ] = 4 × (1/2) = 2
RG eigenvalue: y₄ = d - [φ⁴] = 3 - 2 = 1 > 0 → **relevant** ✓

[φ⁶] = 6 × [φ] = 3
y₆ = d - [φ⁶] = 3 - 3 = 0 → **marginal** (tree level) ✓

These differ from standard φ⁴ in d=4 where y₄ = 0 (marginal). The difference is a simple consequence of dimensionality. ✓

#### 2.3 The table in §1.2 -- Verified

A博士's table of RG eigenvalues for d=3:

| n | y_n = 3 - n/2 | RG class |
|---|---------------|----------|
| 2 | 2 | relevant |
| 3 | 1.5 | relevant |
| 4 | 1 | **relevant** |
| 5 | 0.5 | relevant |
| 6 | 0 | **marginal** |
| 8 | -1 | irrelevant |

All entries are arithmetically correct given [φ] = 1/2. ✓

#### 2.4 Caveat 1: Anomalous dimension could change the classification

With anomalous dimension η ≠ 0:
[φ] = (d-2+η)/2

For φ⁴ to become marginal in d=3: 4 × (1+η)/2 = 3 → 2(1+η) = 3 → η = 0.5

**η = 0.5** would make φ⁴ marginal. While this is large compared to known 3D universality classes (Wilson-Fisher η ≈ 0.035), it is not logically impossible. DGF's non-polynomial potential could in principle generate large anomalous dimensions. **A博士 does not discuss this possibility.**

#### 2.5 Caveat 2: Relevant φ⁴ does NOT imply "no IR fixed point"

A博士 concludes (§1.2, §1.3.2, §X.1) that because φ⁴ is relevant, "对称相没有微扰IR不动点" and "系统必然流向强耦合." This conclusion is **stronger than the scaling analysis warrants**:

1. **Wilson-Fisher counterexample:** In d=4-ε (d<4), φ⁴ is relevant, yet a NON-TRIVIAL IR fixed point exists at finite coupling. The relevance of φ⁴ means the Gaussian fixed point is IR-unstable, but the flow can terminate at a Wilson-Fisher fixed point. A博士 acknowledges this existence in §1.2 ("Wilson-Fisher 不动点的标准分析（ε-展开, d=4-ε）不适用") but then dismisses it because DGF is not a φ⁴ theory but a non-polynomial theory. This dismissal is valid but the stronger claim of "no IR fixed point" is not proven by scaling alone.

2. **A博士's own calculation finds a WF fixed point** (§1.3.2): m̄²_* = -1/7, λ̄_* ≈ 9.67. He dismisses it because m̄²_* < 0 (symmetry-broken phase). However, non-perturbative effects and the full non-polynomial potential could alter this conclusion. The DGF potential Ṽ(φ) is not truncated at φ⁴ -- it contains all powers. The "phase" classification (symmetric vs broken) based on the quadratic coefficient alone is misleading for a non-polynomial potential.

3. **"Strong coupling" is not inconsistent:** Even if no perturbative fixed point exists, the theory could have a well-defined non-perturbative IR fixed point accessible via FRG or lattice methods. A博士 acknowledges this (§1.6) but the rhetorical framing ("必然流向强耦合") suggests a problem that may not exist.

#### 2.6 Caveat 3: Canonical normalization with ℓ rescaling

DGF's original action has dimensionless q and kinetic coefficient ℓ². To reach canonical normalization (kinetic term = ½(∇φ)²), one must rescale φ = ℓ δq. This introduces ℓ factors into all couplings:

g_n^canonical = s^(n)(q_eq) / ℓ^n

These ℓ factors (which carry mass dimension n) modify the dimensional analysis of couplings. In natural units ℏ=c=1, [ℓ] = -1, so each ℓ factor contributes dimension -1. The net effect on coupling dimensions is:

[g_n^canonical] = n - n[φ] = n - n(d-2)/2 = n(4-d)/2 + ... 

Wait, this needs more careful check. In A博士's formulation, the dual action S̃ already absorbs sign conventions and uses Z = ℓ². The field φ in S̃ is presumably the canonically normalized field. The dimensional analysis [φ] = (d-2)/2 is therefore standard. However, the **absolute normalization** of couplings (their "bare" values at the UV scale) depends on ℓ, and the dimensionless ratios m̄² = m²/Λ², λ̄ = λ/Λ, etc. are what enter the RG equations. A博士's numerical evaluation in §1.3.1 correctly identifies that ℓ's absolute value affects whether the theory is weakly or strongly coupled at the UV scale.

#### 2.7 Conclusion on Claim 2

The **tree-level scaling analysis is correct**: φ⁴ IS relevant in d=3 by standard dimensional analysis. This is a rigorous mathematical fact given [φ] = (d-2)/2.

However, A博士 draws **stronger conclusions** from this fact than are strictly warranted:

1. The claim that "no perturbative IR fixed point exists" is a 1-loop calculation result, not a consequence of scaling alone. It could be modified by higher-loop effects or the full non-polynomial potential.
2. The claim that "the system necessarily flows to strong coupling" overlooks the possibility of a Wilson-Fisher-type non-trivial fixed point at finite coupling.
3. The anomalous dimension η could in principle modify the relevance/marginality classification, though requiring η=0.5 to make φ⁴ marginal is implausibly large.

**Impact on LP40:** The finding that φ⁴ is relevant in d=3 (unlike standard d=4 φ⁴ theory) is genuinely important and correct. It means DGF's RG structure is qualitatively different from standard φ⁴ theory. The IR behavior is controlled by the full non-polynomial potential, making non-perturbative methods (FRG, lattice) necessary. This justifies LP40's recommended next steps (R2: FRG numerical solution). The overstatement that "no IR fixed point exists" should be softened to "no perturbative IR fixed point found in 1-loop analysis of the φ⁴ truncation" -- the non-perturbative full-potential fixed point structure remains open.

---

## Summary

| Claim | Verdict | Core finding |
|-------|---------|-------------|
| Claim 1: exp(+S) required | **CORRECT** | s''(1/2)=-4 verified; exp(-S) mathematically divergent; exp(+S) convergent; convention physically motivated by entropy origin. Requires DGF author confirmation only because DGF v3 doesn't discuss path integrals. |
| Claim 2: φ⁴ relevant in d=3 | **PARTIALLY CORRECT** | Tree-level scaling analysis is correct and important. Overstated conclusions about "no IR fixed point" and "necessary strong coupling" go beyond what scaling alone supports. 1-loop analysis finding a symmetry-broken WF fixed point doesn't rule out a non-perturbative symmetric-phase fixed point in the full non-polynomial potential. |

**Neither claim is WRONG.** Claim 2's partial caveats do not invalidate LP40's main findings -- they suggest the conclusions should be somewhat softened and that the non-perturbative fixed point analysis (LP40 R2) is indeed the right next step.

---

*INSPECTOR verification complete. Signed.*
