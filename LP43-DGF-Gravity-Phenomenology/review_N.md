# Referee Report N: The α=1 "Additivity Derivation" — Five-Gate Audit

**Referee expertise:** Mathematical physics — graph theory, RG flows, foundations of proper time, axiomatic gravity
**Manuscript under review:** `FINAL_ACCOUNTING.md` — claim that α=1 (dτ = q^α·dt) is "derived" from proper-time additivity on causal graphs
**Date:** 2026-06-10

---

## Summary Verdict: DERIVATION FAILS AT ALL FIVE GATES

The authors' four-step argument (reproduced below) is examined under five independent attacks. Every attack exposes a logically distinct failure mode. No attack is redundant with any other — each isolates a different layer of the argument that is independently fatal.

### The Target Argument (from FINAL_ACCOUNTING.md)

```
1. 因果图上世界线 = 边的序列
2. 固有时间是边贡献的和：dτ_total = Σ dτ_i
3. 每条边贡献只依赖该边的q：dτ_i = f(q_i)·dt_i
4. "尺度不变性"要求τ_a/τ_b不依赖步数N → f(q) ∝ q → α=1
```

---

## ATTACK 1: Step 3 — Locality of Edge Contribution Is Unjustified

### 1.1 The Stated Premise

The authors assert that each edge's proper-time contribution depends **only** on that edge's q-value: dτ_i = f(q_i)·dt_i. This is the linchpin — without it, the entire additivity structure collapses.

### 1.2 Why It Fails

On a causal graph, a worldline is not a sequence of **independent** edges. Each event (node) can have multiple predecessors. Information propagates along multiple paths, and the selection of which path constitutes "the worldline" already involves a global optimization — maximizing q-weighted connectivity. This means:

1. **Path dependence:** The worldline is chosen by a routing criterion (maximize q along the path). The edge contributions to proper time therefore depend not just on the local q_i of that edge, but on the q-values of **adjacent edges** that determined whether this edge was selected as part of the worldline in the first place.

2. **Multi-predecessor interference:** A node with two incoming edges of different q-values receives information from both. The "proper time" accumulated at that node should depend on the interference of these two contributions — not simply on the q of the single edge that was arbitrarily selected as "the worldline."

3. **No unique worldline:** On a causal graph with branching and merging, there is no unique sequence of edges that constitutes "the" worldline between two events. The proper time between A and B is a property of the entire causal diamond connecting them, not of one selected path through it. The authors' reduction to a single sequence of edges is an implicit choice that discards the graph's most important feature — its multi-path connectivity.

### 1.3 Formal Statement of the Gap

Let node v have predecessor set P(v) = {u₁, u₂, ..., u_k} with edge q-values {q_{u₁v}, q_{u₂v}, ..., q_{u_kv}}. The authors assume:

```
dτ(v) = f(q_{u_j v})·dt   for some single predecessor u_j
```

The correct expression on a causal graph would be:

```
dτ(v) = F({q_{u₁v}, q_{u₂v}, ..., q_{u_kv}})·dt
```

where F is a function of the **entire set** of incoming edge weights. The reduction from F to f(q_i) for a single edge is asserted, not derived. It silently assumes that worldlines never branch or merge, which is false on any realistic causal graph.

### 1.4 Verdict

**GATE 1: FAILED.** The premise that each edge contributes independently is unwarranted. The causal graph's multi-path structure — which the authors elsewhere celebrate as the source of emergent geometry — is precisely what prevents each edge's proper-time contribution from depending only on its own q.

---

## ATTACK 2: Step 4 — "Scale Invariance" Only Holds for Uniform q

### 2.1 The Stated Argument

The authors consider two parallel worldlines A and B, each traversing N steps:
- Worldline A: every step has the same q_a
- Worldline B: every step has the same q_b (or "geometric mean" q_b)

They claim the ratio τ_a/τ_b = f(q_a)/f(q_b) must be independent of N (scale invariance), and that this forces f(q) ∝ q.

### 2.2 The Counterexample: Non-Uniform q

Consider a realistic gravitational field where q varies continuously along a worldline. Take:

- Worldline A: traverses N steps with q-values {q₁, q₂, ..., q_N}
- Worldline B: traverses N steps with q-values {q'₁, q'₂, ..., q'_N}

The proper time ratio is:

```
τ_A/τ_B = [Σ f(q_i)] / [Σ f(q'_i)]
```

This ratio **does** depend on N in general, even for linear f(q) = q. Proof:

Take q_i = exp(-GM/r_i c²) along a radial infall trajectory. As N increases (finer discretization), the sum Σ q_i·dt converges to ∫ q(t)·dt, which depends on the path. Two worldlines with different radial trajectories give different accumulated proper times — and the **ratio** of these accumulated proper times depends on the step count N until the continuum limit is reached.

The authors' "scale invariance" argument assumes:
1. Uniform q along each worldline (counterfactual in any curved spacetime)
2. That the proper time ratio between two worldlines should be an **intensive** quantity (independent of the worldline length)

Neither assumption is justified. The proper time ratio between two worldlines **should** depend on their lengths — that's why the twin paradox exists.

### 2.3 Where the Argument Breaks

The authors' step from "τ_a/τ_b must be N-independent" to "f(q) ∝ q" is:

```
τ_a/τ_b = N·f(q_a)·dt / (N·f(q_b)·dt) = f(q_a)/f(q_b)
```

This cancellation of N requires:
1. Every step on worldline A has **identical** q_a
2. Every step on worldline B has **identical** q_b

In any gravitational field where q = exp(-GM/rc²) varies with position, different steps along a worldline have different q values. The sum Σ f(q_i) does **not** factor as N·f(q_avg) for any average q_avg unless f is linear AND q is constant.

But the authors are trying to **prove** f is linear. They cannot assume the conclusion (linearity) to justify the step (factorization of the sum) that they use to prove linearity.

### 2.4 Verdict

**GATE 2: FAILED.** The scale-invariance argument only works for uniform q fields. In realistic gravitational fields with spatially varying q = exp(-GM/rc²), the proper time ratio between worldlines does depend on N (the worldline length), and the factorization step N·f(q)·dt is invalid regardless of f's functional form. The argument proves nothing about f(q) in the physically relevant regime.

---

## ATTACK 3: Linearity Is Not the Unique Solution to "Mergeability"

### 3.1 The Claim

The authors assert that f(q₁)dt₁ + f(q₂)dt₂ must be "mergeable" (可合并的), and that this forces f(q) to be linear. They never define "mergeable" precisely.

### 3.2 Interpretation 1: Standard Addition

If "mergeable" simply means τ_total = τ₁ + τ₂ (standard addition), then **any** function f satisfies this trivially. The identity:

```
f(q₁)dt₁ + f(q₂)dt₂ = f(q₁)dt₁ + f(q₂)dt₂
```

holds for every f. No constraint on the functional form emerges.

### 3.3 Interpretation 2: Effective Edge Replacement

If "mergeable" means: two consecutive edges with parameters (q₁, dt₁) and (q₂, dt₂) can be replaced by one effective edge with parameter q_eff and time interval dt₁+dt₂, such that:

```
f(q_eff)·(dt₁ + dt₂) = f(q₁)·dt₁ + f(q₂)·dt₂
```

Then in the limit dt₁ = dt₂ = dt:

```
2·f(q_eff) = f(q₁) + f(q₂)
```

This requires f to be linear: f(q_eff) = [f(q₁) + f(q₂)]/2 implies q_eff must be such that f(q_eff) equals the arithmetic mean. If f(q) = q, then q_eff = (q₁+q₂)/2 — arithmetic mean.

**But this immediately creates a contradiction with the RG flow.** On the causal graph, q values compose **multiplicatively** under channel concatenation (see review_K.md, Attack 4.2):

```
E_{q₁} ∘ E_{q₂} = E_{q₁q₂}  →  q_eff = q₁·q₂  (NOT (q₁+q₂)/2)
```

If q_eff = q₁·q₂ (multiplicative), then:

```
f(q₁q₂)·2dt = f(q₁)·dt + f(q₂)·dt
```

This forces f to be **logarithmic**: f(q) ∝ ln(q), not linear! Because:

```
ln(q₁q₂) = ln(q₁) + ln(q₂) → f(q₁q₂) = f(q₁) + f(q₂) for f(q) = ln(q)
```

The authors' demand that f(q_eff) = [f(q₁) + f(q₂)]/2 (arithmetic) is incompatible with the RG composition law q_eff = q₁·q₂ (multiplicative) that governs depolarizing channels.

### 3.4 The Deeper Contradiction

If we take the channel composition law seriously (q is multiplicative under concatenation), then:

- **Additive composition in τ**: τ = Σ f(q_i)·dt_i
- **Multiplicative composition of q**: q_eff = ∏ q_i

These two composition laws point to f(q) = ln(q), i.e., α = 0 in the sense that dτ ∝ ln(q)·dt, NOT dτ ∝ q·dt. The authors get α = 1 by ignoring the multiplicative composition of q and imposing an arithmetic composition that has no justification in the physics of depolarizing channels.

### 3.5 The Undefined Term

The word "mergeable" (可合并) does the heavy lifting in the authors' argument, but it is never given an operational definition. It is a term of art that the authors can interpret post-hoc to yield whatever conclusion they need. This is the definitional equivalent of a free parameter.

### 3.6 Verdict

**GATE 3: FAILED.** Depending on how "mergeable" is defined:
- If it means standard addition, any f works — no constraint on α.
- If it means effective edge replacement with arithmetic averaging, f must be linear — but this contradicts the multiplicative composition law for depolarizing channels (q_eff = q₁·q₂), which would force f(q) ∝ ln(q) instead.
- The term "mergeable" is undefined, making the argument unfalsifiable.

---

## ATTACK 4: Asymmetry Between Time and Space — the b=2 Problem

### 4.1 The Asymmetry

The authors claim α=1 (time exponent) is **derived** from additivity on the causal graph, while b=2 (space exponent) is fixed **experimentally** (Cassini γ=1). This asymmetry is suspicious and, upon examination, self-defeating.

### 4.2 Spatial Distances Are Also Edge-Contribution Sums

On the causal graph, a spatial distance between two nodes is also computed as a sum over edge contributions. The graph distance d(i,j) in the q-weighted graph is:

```
d(i,j) = min_path Σ (1/√q_e)  (or some function of edge weights)
```

The spatial metric g_{ij} = q^{-b} δ_{ij} has the same structural origin as g_{00} = -q^{2α}: both come from the q-weighted graph structure. If the "additivity → scale invariance → proportionality" argument works for proper time (giving α=1), the **exact same logic** applied to spatial distances should give b.

### 4.3 The Fork

There are only two possibilities:

**Possibility A: The additivity argument is general.** If it applies to any edge-contribution sum on the causal graph, then it should fix both α and b. Since the authors admit b=2 is experimentally fixed (not derived), the argument must be invalid — otherwise it would have fixed b as well.

**Possibility B: The additivity argument only works for time.** But the causal graph does not distinguish "time edges" from "space edges" at the level of edge-weight contributions. Both are q-weighted. Both contribute additively to their respective geometric quantities (proper time for timelike paths, distance for spacelike paths). If the argument selectively applies to one but not the other, the authors must explain what distinguishes timelike from spacelike additivity on the graph. No such explanation exists in any DGF document.

### 4.4 The Real Source of Asymmetry

The true reason α and b are treated differently is transparent:

- α=1 gives g_{00} = -q² ≈ -(1 - 2GM/rc²), which **happens to match** the Newtonian limit
- b=2 gives g_{ij} = q^{-2}δ_{ij}, which **happens to match** PPN γ=1

Both α and b are calibrated against GR. The "additivity derivation" of α=1 is a post-hoc rationalization of a calibration choice. The fact that it cannot also "derive" b=2 — which has the same structural origin — exposes it as special pleading.

### 4.5 Verdict

**GATE 4: FAILED.** If the additivity argument genuinely derived α=1 from graph structure, it would also derive b=2—since spatial distances are also edge-contribution sums. The fact that b=2 is acknowledged as experimentally fixed while α=1 is claimed as derived reveals the argument as post-hoc calibration, not genuine derivation.

---

## ATTACK 5: Ultimate Test — A Self-Consistent Counterexample for Any α

### 5.1 Construction

Consider the generalized DGF framework with free parameter k (replacing α):

**Postulate:** dτ = q^k · dt

**Field equation (unchanged):** ∇²(ln q) = 4πG_field · ρ/c²

**Solution (unchanged):** q = exp(-G_field M / r c²)

**Metric:** g₀₀ = -q^(2k), g_{ij} = q^{-2} δ_{ij}

**Newtonian limit:** 
- g₀₀ = -q^(2k) ≈ -(1 - 2k·G_field M / r c²)
- Φ = -k·G_field M / r
- Acceleration: a = -∇Φ = -k·G_field M / r²

**Experimental calibration:** The observed Newtonian acceleration is a = -G_obs M / r², with G_obs = 6.67×10^{-11} m³/kg·s².

Therefore: G_obs = k·G_field

### 5.2 Self-Consistency Check

For any k ≠ 0, define G_field = G_obs / k. Then:

1. The field equation uses G_field
2. q = exp(-G_field M / r c²) = exp(-G_obs M / (k r c²))
3. g₀₀ = -q^(2k) = -exp(-2G_obs M / r c²)
4. Newtonian acceleration = -G_obs M / r² ✓

**The theory is mathematically self-consistent for every k > 0.** No internal contradiction emerges for any choice of k. The parameter k is a **gauge freedom** in the relationship between G_field and G_obs.

### 5.3 The Authors' Hidden Assumption

The authors' "derivation" of α=1 implicitly assumes:

```
G_field = G_obs
```

This is the statement that the G appearing in the field equation ∇²(ln q) = 4πGρ/c² is the **same** G that appears in the Newtonian force law F = GMm/r².

But this identity is not a logical necessity — it is the very thing that needs to be proved. Fields can have different coupling constants in different sectors. Brans-Dicke theory has G_field ≠ G_obs (with G_obs/G_field = (2ω+4)/(2ω+3)). Dilaton gravity has different G in string frame vs. Einstein frame. Demanding G_field = G_obs is **equivalent** to demanding α=1 — it is the same statement in different notation.

### 5.4 The Circularity Laid Bare

```
Claim: Additivity on the causal graph → f(q) ∝ q → α=1
Hidden step: This requires time to be the only q-dependent geometric quantity
Hidden step: This requires G_field = G_obs
Truth: G_field = G_obs ⇔ α=1 (they are logically equivalent)
Truth: The "derivation" assumes what it claims to prove
```

### 5.5 Experimental Indistinguishability

For any k, the metric in terms of observables (G_obs) is:

```
ds² = -exp(-2G_obs M / r c²) c² dt² + exp(2G_obs M / (k r c²)) [dr² + r² dΩ²]
```

The g₀₀ component is **independent of k** when expressed in terms of G_obs. Only g_{ij} depends on k. This means:

- Solar system tests of g₀₀ (redshift, time delay) cannot measure k
- Only spatial curvature tests (light deflection, PPN γ) can constrain k (or equivalently, b)
- But b is already separately fixed by Cassini

**k (or α) is not independently measurable from time-related observables.** It is a redundant parameter whose effect is completely absorbed by the definition of G_obs. The claim to have "derived" α=1 is therefore not just logically flawed — it is a claim about an unobservable parameter.

### 5.6 What This Means

The "additivity derivation" of α=1 is a mathematical restatement dressed as a physical argument. It produces α=1 not because the graph forces it, but because the authors' definition of "additivity," "mergeability," and "scale invariance" were crafted — consciously or not — to yield α=1. Any other choice of these undefined terms would yield a different α, as the counterexample demonstrates.

### 5.7 Verdict

**GATE 5: FAILED.** A self-consistent counterexample exists for any k > 0. The parameter α is a gauge freedom relating G_field to G_obs. The "derivation" of α=1 silently assumes G_field = G_obs, which is logically equivalent to α=1. The argument is circular.

---

## SYNTHESIS: The Five Gates

| Gate | Attack | Failure Mode | Independent? |
|:----:|--------|-------------|:-----------:|
| 1 | Locality of dτ_i = f(q_i)·dt_i | Multi-path structure of causal graphs violates edge independence | Yes |
| 2 | Scale invariance τ_a/τ_b indep. of N | Only holds for uniform q; fails for q(x) varying in realistic gravity | Yes |
| 3 | Linearity as unique "mergeable" f(q) | "Mergeable" undefined; multiplicative q composition forces f(q) ∝ ln(q), not f(q) ∝ q | Yes |
| 4 | Asymmetry with spatial b=2 | Same additivity logic should fix b; failure to do so exposes post-hoc reasoning | Yes |
| 5 | Self-consistent counterexample for any k | Free parameter k = α; G_field = G_obs is assumed, not derived; α unobservable | Yes |

These five failures are **logically independent**. Fixing one would not fix any other. Each exposes a different layer of the argument as unsound:

- Gate 1 attacks the premise (step 3 of the argument)
- Gate 2 attacks the inference (step 4 of the argument)
- Gate 3 attacks the undefined term that mediates the inference
- Gate 4 attacks the argument by consistency with the authors' own treatment of the spatial analog
- Gate 5 attacks the argument by explicit counterexample construction

Even if four gates were somehow answered, the fifth would remain fatal.

---

## RECOMMENDATION

**The claim that α=1 is derived from proper-time additivity is not supported by the evidence presented.**

The argument in `FINAL_ACCOUNTING.md` contains five independently fatal logical gaps. The parameter α=1 is a calibration choice — equivalent to demanding that DGF's weak-field limit matches GR's Newtonian limit (G_field = G_obs). This is a legitimate calibration strategy used by all modified gravity theories, but it should not be presented as a derivation.

The honest statement is:

> α=1 is chosen to calibrate DGF to GR in the weak-field/Newtonian limit. This is operationally equivalent to defining G_obs ≡ G_field. The value α=1 is not derived from causal graph structure — it is selected to ensure the correct Newtonian phenomenology. The same is true of b=2, which is selected to ensure PPN γ=1 (Cassini constraint).

DGF's genuine achievements — the exponential form q = exp(-GM/rc²) from ln q RG additivity, the Weyl-geometric structure of the spatial metric, and the 2PN GW predictions — do not depend on whether α=1 is "derived" or "calibrated." The scientific value of DGF is in its falsifiable predictions (2PN phase shift, strong-field deviations), not in contested claims about axiomatic derivations of calibration parameters.

---

*Referee N, PRL — Mathematical Physics Panel*
*Date: 2026-06-10*
*Cross-reference: agent_L_alpha.md (same conclusion via G_field vs. G_obs), review_K.md (quantum channel derivation fails), review_G.md (α=1 is calibration)*
