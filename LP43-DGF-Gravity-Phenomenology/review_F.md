# Referee Report F: The Core Hypothesis dτ = q·dt

**Referee expertise:** Foundations of general relativity, equivalence principle, mathematical physics
**Manuscript under review:** DGF Gravity — Claim that all predictions follow from the single hypothesis dτ = q·dt
**Key files examined:** `DGF_CLOSURE.md`, `DGF_GRAVITY_FINAL.py`, `g00_derivation.md`, `first_principles.py`, `weyl_riemann_wall.md`, `THE_TRUTH.md`, prior reviews A-E

---

## Summary Verdict: REJECT

The authors' entire theoretical edifice rests on a single claimed hypothesis: dτ = q·dt, "proper time of information propagation is proportional to quantum channel openness." The manuscript asserts that all DGF predictions — the metric, PPN parameters, GW phase shifts, cosmological w(z) — follow uniquely from this one postulate. If the hypothesis is correct, DGF is correct; if false, DGF is false.

I demonstrate below that this is not one hypothesis but a package of at least five independent, unevidenced, and in several cases circular choices, each of which could be made differently to produce entirely different predictions. The claim of a "single hypothesis" is a rhetorical device that obscures the theory's true degrees of freedom. Furthermore, I show that the core postulate itself cannot be given an operational definition without presupposing the very metric it is meant to derive. I recommend rejection on grounds of logical circularity, violation of the Einstein Equivalence Principle, and unresolved ambiguity in the foundational postulate.

---

## 1. ATTACK 1: dτ = q·dt Is Not a Derivation — It Is a Post-Hoc Selection from an Infinite Family

### 1.1 What the Causal Graph Actually Gives

The authors' `first_principles.py` (lines 230-262) implements weighted path counting on a (50x51) 1+1D causal graph. The dynamic programming algorithm computes dp, the weighted sum over all causal paths from a source node. In a region of constant q, the result is:

```
dp(t) ~ exp(t ln q) = q^t     [Eq. 1, authors' own code output]
```

This is the only graph-theoretic output. Everything beyond this point is an interpretation that maps the scalar dp(t) to a proper time interval dτ.

### 1.2 The Mapping Ambiguity

From dp ~ q^t, the authors assert:

```
dτ/dt = q     →     dτ = q·dt     →     g_{00} = -q^2
```

But `dp ~ q^t` defines only the scaling of a cumulative weight with time. It does not single out any particular function f(dp, t) as "the" proper time. Consider the general ansatz:

```
dτ/dt = q^α     →     g_{00} = -q^{2α}
```

The exponent α is completely undetermined by the graph computation. Any real α produces a logically consistent mapping from dp to dτ. The three cases the authors themselves identify are:

| α | dτ/dt | g_{00} | Newtonian limit (q = e^{-φ}) | Matches GR? |
|---|-------|--------|------------------------------|-------------|
| 1 | q | -q² | -(1 - 2φ + 2φ² + ...) | Yes (at Newtonian) |
| -1/2 | q^{-1/2} | -q^{-1} | -(1 + φ + ...) | No (wrong sign) |
| 1/2 | q^{1/2} | -q | -(1 - φ + ...) | No (factor 1/2) |

**The only α that reproduces the Newtonian limit is α = 1. The choice α = 1 is not derived from any property of the causal graph — it is selected because it gives the right answer.** This is a textbook example of post-hoc parameter tuning dressed as derivation.

### 1.3 The Authors' Own Code Concedes This

In `first_principles.py`, line 261:

```python
print(f"  The proper time dtau/dt = dp^{1/t} converges to q.")
```

The identification `dτ/dt = dp^{1/t}` is asserted, not derived. The code computes dp, then declares that dp^(1/t) "is" the proper time without argument. But dp^(1/t) is the geometric mean of per-step path weights — one could equally take the arithmetic mean (dp/t → some function of q), the harmonic mean, or any other statistic. The choice of geometric mean is mathematically natural for multiplicative processes, but naturalness is not uniqueness, and uniqueness is what the "single hypothesis" claim requires.

### 1.4 The Newtonian Circularity

The authors' defense — stated in `g00_derivation.md` and `DGF_CLOSURE.md` — is that the choice is physically motivated: "only open quantum channels contribute to proper time." But this physical motivation is itself expressed mathematically as dτ = q·dt. The "physical argument" is the equation itself, restated in words. No independent principle selects α = 1 over any other value.

Worse, the verification that α = 1 is "correct" runs as follows:
1. Assume dτ = q·dt (α = 1)
2. Compute g_{00} = -q²
3. Expand: g_{00} ≈ -(1 - 2GM/rc²), matching Newtonian gravity
4. Conclude: "Therefore dτ = q·dt is correct"

Step 3 verifies that α = 1 matches Newton, but this is precisely the circularity. One could equally:
1. Demand that g_{00} match Newtonian gravity
2. Solve for α: 2αφ = 2φ → α = 1
3. Declare: "Therefore dτ = q·dt"

The Newtonian limit does not test the hypothesis — it **determines** the hypothesis's free parameter. A hypothesis whose sole parameter is fixed by matching the data it claims to predict is not a prediction at all.

### 1.5 The Geometric-Mean vs. Arithmetic-Mean Problem

There is an even deeper ambiguity. The path counting dp is a **sum** over weighted paths:

```
dp(A→B) = Σ_{paths γ} Π_{edges e∈γ} w_e
```

The authors take dp^(1/t) where t is the number of time steps. But t is coordinate time, and the number of steps depends on the discretization scale. If we double the temporal resolution (halve the step size), dp^(1/t) changes because more, smaller-weight edges are traversed. The continuum limit of dp^(1/t) is not well-defined without specifying how q scales with the discretization.

**In short: the mapping dp → dτ requires specifying (a) the exponent α, (b) the statistic (geometric vs. arithmetic mean), and (c) the continuum regularization. Three independent choices, none fixed by the causal graph itself, all packaged as "dτ = q·dt."**

---

## 2. ATTACK 2: The Operational Definition of q Is Circular

### 2.1 What Is q?

The authors define q as "quantum channel openness" — the fraction of quantum channels that remain coherent on a causal edge, with 1 - q representing decohered/classicalized channels.

### 2.2 Measuring q Requires the Metric

To measure q at a spacetime point, one must:

1. **Identify a causal edge.** A "causal edge" connects two causally related events. Identifying such edges requires knowledge of the causal structure — i.e., the light cone, which is determined by the metric g_{μν}. Without the metric, one cannot distinguish timelike, spacelike, and lightlike separations.

2. **Send a probe qubit along that edge.** This requires preparing a quantum state at event A and measuring it at event B, where B is in the causal future of A. The very notion of "causal future" presupposes the metric.

3. **Perform quantum state tomography** to determine how much coherence survived the journey. This requires synchronized measurements, which presupposes a notion of simultaneity, which presupposes the metric's time slicing.

4. **Subtract decoherence from other sources** (environmental coupling, imperfect gates, detector noise). This requires a model of "non-gravitational" decoherence, which presupposes that gravitational and non-gravitational decoherence can be cleanly separated — itself a claim that depends on the theory one is trying to test.

**The operational chain is: metric → causal structure → identify causal edges → send probe qubits → measure q → construct metric.** The metric is both input and output.

### 2.3 The Authors' Implicit Admission

The static solution q = exp(-GM/rc²) is not derived from any microscopic measurement of quantum channel openness. It is derived from the RG flow equation ∂_L ln q = -κρ (or equivalently, the additivity of ln q under coarse-graining), where ρ = Mδ(r) is the mass density. But this derivation uses:
- The Newtonian potential Φ = -GM/r as input
- The identification Φ ↔ ln q

This identification is itself the metric: g_{00} = -q² = -exp(2 ln q) = -exp(2Φ/c²) ≈ -(1 + 2Φ/c²). The "derivation" of q(r) assumes the very gravitational potential that q is supposed to explain. **You cannot derive the metric from q if you need the metric to determine q.**

### 2.4 A Concrete Challenge

The authors should answer this simple question: **Describe an experiment — even a gedankenexperiment — that measures q at a spacetime point without using any pre-existing knowledge of the metric, causal structure, or gravitational potential.** If q cannot be measured independently, the theory is not physics — it is a mathematical reparameterization of GR with no independent empirical content at the foundational level.

---

## 3. ATTACK 3: The Equivalence Principle Is Violated at the Foundational Level

### 3.1 What the Equivalence Principle Requires

The Einstein Equivalence Principle (EEP) has three components:

- **WEP (Weak Equivalence Principle):** Test particles fall along geodesics independent of composition.
- **LLI (Local Lorentz Invariance):** In local freely falling frames, non-gravitational physics is Lorentz invariant.
- **LPI (Local Position Invariance):** The outcome of any local non-gravitational experiment is independent of where and when in the universe it is performed.

LPI is the relevant component here.

### 3.2 DGF's Violation of LPI

In DGF, the parameter q varies with gravitational potential: q = exp(-GM/rc²). Near a massive body, q < 1; far away, q ≈ 1.

The authors' physical interpretation is explicit: q < 1 means fewer quantum channels are open, and decoherence is stronger. This is not merely a geometric effect (like time dilation, where local physics is unchanged but global comparisons differ). It is a claim about **local physics**: the rate of quantum decoherence at a spacetime point depends on q at that point.

Consider two identical quantum optics experiments:
- Experiment A: performed on Earth's surface (q ≈ exp(-GM_⊕/R_⊕c²) ≈ 1 - 7×10^{-10})
- Experiment B: performed in deep space (q ≈ 1)

DGF predicts that Experiment A experiences (very slightly) more decoherence than Experiment B, because q_A < q_B. The outcome of a local non-gravitational experiment depends on the local gravitational potential. This is a direct violation of LPI.

### 3.3 The Authors' Likely Rebuttal and Why It Fails

The authors might argue that the decoherence difference is unmeasurably small (Δq ~ 10^{-9}), so LPI is effectively preserved in the weak-field limit. This argument fails for two reasons:

1. **In-principle violation is sufficient for rejection.** The EEP is a foundational principle of metric gravity. A theory that violates it in principle, even if the violation is small in the solar system, is not a metric theory of gravity in the standard sense. The authors cannot simultaneously claim to "derive GR" (which respects LPI) and violate the principle that GR embodies.

2. **Strong-field regimes.** Near a neutron star (GM/Rc² ~ 0.1-0.2), q = exp(-0.2) ≈ 0.82. The predicted decoherence enhancement is 18%. If local quantum physics near a neutron star differs from local quantum physics in the laboratory by 18%, this is a large effect that should manifest in, e.g., neutron star cooling (via modified Urca processes), pulsar glitches, or magnetar burst statistics.

### 3.4 The Structural Problem

The deeper issue is that DGF conflates two distinct roles of the metric:
- **Role 1 (geometric):** Determining proper time intervals, causal structure, and geodesics — this is what GR's metric does.
- **Role 2 (material):** Determining the local strength of quantum decoherence — this is a property of the matter sector, not geometry.

By tying both to the same function q, DGF entangles geometry and matter in a way that necessarily violates the separation that the equivalence principle enforces. The EEP says: gravity is geometry; local matter physics is independent of geometry. DGF says: gravity is geometry, and geometry determines local matter physics (via q-dependent decoherence). The contradiction is structural, not quantitative.

### 3.5 Experimental Constraint

The best laboratory tests of LPI come from null gravitational redshift experiments (comparing clocks of different composition at different heights) and from tests of the constancy of fundamental constants. The bound on LPI violation, parameterized as a position-dependence of the fine-structure constant or of atomic transition frequencies, is typically |β_LPI| < 10^{-6} (from GPS clock comparisons, Nilsson et al.). If q-dependence modifies local quantum transition rates, the DGF prediction must be compared against these bounds. The authors have not done this.

---

## 4. ATTACK 4: "Information-Prioritized Paths" — No Mathematical Definition Exists

### 4.1 The Claim

The authors state (in `weyl_riemann_wall.md` and `DGF_CLOSURE.md`) that physical particles follow "information-prioritized" paths, which are:
- Not Weyl autoparallel lines (which would follow the full Weyl connection, including the non-metricity vector w_μ)
- Not Jordan-frame geodesics (which follow the Levi-Civita connection of the metric conformally transformed to the Jordan frame)
- Something else: paths that maximize "information propagation"

### 4.2 What Is Missing

A physical trajectory requires an equation of motion. For a test particle in a metric theory, this is the geodesic equation:

```
d²x^μ/dτ² + Γ^μ_{αβ} (dx^α/dτ)(dx^β/dτ) = 0
```

where Γ^μ_{αβ} is some connection. In GR, it's the Levi-Civita connection. In Weyl geometry, two natural connections exist (Levi-Civita and Weyl). The authors reject both but provide no alternative.

An "information-prioritized path" must be defined by one of:
- A variational principle (extremizing some functional of the path)
- A differential equation (specifying the tangent vector's derivative)
- A discrete rule on the causal graph (that has a well-defined continuum limit)

The authors provide none of these. The manuscript contains:
- No Lagrangian or action for the "information-prioritized" path
- No connection coefficients
- No discussion of how path-weight maximization translates to a continuum equation
- No proof that the discrete path-weight rule has a unique continuum limit

### 4.3 Why This Matters

Every observable prediction of a gravity theory depends on how particles move:
- **Perihelion precession:** requires solving the geodesic equation to O(v⁴/c⁴)
- **Light deflection:** requires null geodesics
- **Gravitational waveforms:** require the motion of binary components
- **Shapiro time delay:** requires null geodesics in the time domain

If DGF cannot specify the equation of motion, it makes zero observable predictions. The GW 2PN predictions in `DGF_GRAVITY_FINAL.py` implicitly assume that the binding energy is computed from **circular equatorial geodesics of the Riemannian metric** ds² = -q²dt² + q^{-2}(dr² + r²dΩ²) — i.e., they use standard GR geodesics with a modified metric. But this contradicts the claim that particles follow "information-prioritized" paths rather than geodesics.

**Either the GW calculations are wrong (because they use geodesics, not information-prioritized paths), or the claim of a distinct path concept is vacuous (because geodesics are used in practice). The authors cannot have it both ways.**

### 4.4 The Self-Consistency Demand

I require the authors to provide, at minimum:
1. A mathematical definition of the "information-prioritized path" in continuum language (a differential equation or variational principle).
2. Proof that in the static spherically symmetric case, this equation reduces to the geodesics used in the GW calculations.
3. Alternatively, recompute the GW predictions using the correct equation of motion.

Without (1), the concept is undefined. Without (2) or (3), the existing predictions are unjustified.

---

## 5. ATTACK 5: "One Hypothesis" Is Rhetorical Packaging of Multiple Independent Choices

### 5.1 Deconstructing dτ = q·dt

The authors present their theory as having a single free postulate: dτ = q·dt. All else, they claim, follows uniquely. I count at least seven independent choices embedded in this "single" hypothesis:

**Choice 1: Edge weight combination rule.**
The graph Laplacian uses w_{ij} = (q_i + q_j)/2 (arithmetic mean of endpoint q-values). The path counting uses w_e = (q_u + q_v)/2 for each edge. Why the arithmetic mean? The geometric mean sqrt(q_i q_j) or harmonic mean 2q_i q_j/(q_i + q_j) would give different continuum limits and different metrics. The arithmetic mean is chosen without justification.

**Choice 2: Path sum vs. path maximum.**
The weighted path count dp is defined as a **sum** over all causal paths. But in quantum mechanics, the path integral involves a sum of complex amplitudes, not real weights. In classical mechanics, the particle follows a single extremal path, not a sum. If dp is meant to count "available quantum channels," why sum rather than maximize? A max-path formulation would yield dp ~ max_path(product of weights) ~ q^t (same scaling for homogeneous q) but different behavior in inhomogeneous regions, leading to different geodesic equations.

**Choice 3: The statistic for extracting dτ from dp.**
As discussed in Attack 1, dp^(1/t) (geometric mean) is one of infinitely many statistics one could extract from dp(t). The arithmetic mean dp/t, harmonic mean, median, or mode of the path weight distribution would all give different functions of q.

**Choice 4: The continuum limit prescription.**
The causal graph is discrete. Taking the continuum limit requires specifying how the discretization scale vanishes and how q scales with it. The authors provide no systematic coarse-graining analysis. Different choices of continuum limit (different scalings of q with lattice spacing, different dimensional regularizations) yield different effective metrics.

**Choice 5: Splitting time and space between two different graph structures.**
The time-time component g_{00} comes from causal path counting (structure B). The space-space components g_{ij} come from the graph Laplacian (structure A). These are two different mathematical operations on the same graph. Why does time come from one and space from the other? In `THE_TRUTH.md`, the authors themselves acknowledge that "these two structures are not equivalent to a single Riemannian metric." Yet in `DGF_CLOSURE.md`, they are combined into one. The decision to combine them is an additional assumption: that the physical metric is a hybrid of two incommensurate graph quantities.

**Choice 6: The area radius transformation R = r·q^{-1}.**
The physical metric ds² = -q²dt² + q^{-2}(dr² + r²dΩ²) uses a radial coordinate R = r·q^{-1}. The transformation from "graph coordinate" r to "area radius" R introduces additional q-dependence into g_{ij} (changing q^{-1} to q^{-2}). This transformation is motivated by "physics" (R measures proper circumference/2π), but it is a separate choice. In `weyl_riemann_wall.md`, the authors argue this is "not an additional assumption" because "it follows from the definition of area radius." But the decision to use area radius as the physical coordinate, rather than graph distance, is itself a choice with physical consequences.

**Choice 7: The additivity of ln q.**
The static solution q = exp(-GM/rc²) relies on the claim that ln q is additive under RG blocking. This follows from demanding that q obey a multiplicative group property under coarse-graining. But one could equally demand that some other function of q (e.g., q/(1-q), or 1/q) be additive, yielding different static profiles and different predictions. The choice of ln q as the additive quantity is natural for an exponential parameterization, but naturalness is not uniqueness.

### 5.2 Counting the True Degrees of Freedom

Each of these seven choices could, in principle, be made differently. Different combinations yield different predictions for PPN parameters, GW phase shifts, and cosmological evolution. The claim that "all predictions follow from one hypothesis" is true only in the trivial sense that, once all seven choices are fixed, the resulting equations produce predictions. But the hypothesis dτ = q·dt does not fix the choices — the choices are made independently and justified (when justified at all) by their consequences.

**This is not a one-parameter theory. It is a theory whose parameter space has been hidden by packaging multiple independent decisions under a single slogan.**

### 5.3 Comparison with Established Alternatives

Compare with Brans-Dicke theory: one new parameter ω_BD, clearly identified, with a well-defined limit (ω_BD → ∞) that recovers GR. Or f(R) gravity: one free function f(R), with observables expressed as functionals of this choice. Or Einstein-aether theory: four new parameters c_i, each with a clear operational meaning and independent experimental constraints.

In DGF, the "one hypothesis" packaging obscures the true parameter count. A fair presentation would list each independent choice, its range of alternatives, and the experimental signatures that distinguish them. The manuscript does not do this.

---

## 6. CONNECTION TO PRIOR REVIEWS

### 6.1 Relation to Review E (Ω² Error)

Review E demonstrated that the correct Ω² formula is Ω² = (GM/R³) exp(-3φ)/(1-2φ), not the authors' exp(-φ)/(1-φ), and that this leads to a 92% deviation from GR at 1PN — already ruled out by LIGO.

The present review provides the foundational explanation for Review E's finding: the α ambiguity means the metric itself is not uniquely determined. The "correct" Ω² that Review E derives assumes g_{00} = -q² (α = 1) and g_{φφ} = q^{-2}R², as the authors' metric specifies. But if α were different, a different Ω² would follow. The mathematical error that Review E identifies is actually a symptom of the deeper ambiguity identified here.

### 6.2 Relation to THE_TRUTH.md

The authors' own self-critical document `THE_TRUTH.md` acknowledges that:
- "The graph does not yield a single Riemannian metric"
- "dτ = q·dt is a physical interpretation, not a graph-theoretic derivation"
- "The mapping from graph to a single Riemannian metric does not hold"

The present review systematizes these admissions and demonstrates that they are fatal to the "single hypothesis" claim, not mere caveats.

---

## 7. OVERALL ASSESSMENT AND RECOMMENDATION

### 7.1 Summary of Findings

| Attack | Finding | Severity |
|--------|---------|----------|
| 1: α-ambiguity | dτ = q·dt is one choice from an infinite family; α = 1 is selected to match Newtonian limit (circular) | **FATAL** |
| 2: Operational circularity | q cannot be measured without the metric; the metric requires q | **FATAL** |
| 3: Equivalence principle | DGF ties local quantum decoherence to gravitational potential, violating LPI | **FATAL** |
| 4: Undefined paths | "Information-prioritized path" has no equation of motion; GW calculations use standard geodesics (contradiction) | **FATAL** |
| 5: Packaged choices | At least 7 independent choices are bundled as "one hypothesis" | **FATAL** |

### 7.2 The Core Problem

The DGF program attempts to derive gravity from an information-theoretic causal graph. This is a legitimate and interesting research direction, pursued by Jacobson (1995), Verlinde (2011, 2017), and many others. What distinguishes those works from the present manuscript is that they are explicit about their assumptions and do not claim to have derived GR from a single postulate.

DGF's claim to have condensed all assumptions into dτ = q·dt is simultaneously the theory's most appealing feature (apparent simplicity) and its fatal flaw (hidden complexity). The "single hypothesis" is not a hypothesis — it is a narrative summary of a chain of independent modeling choices.

### 7.3 What Would Be Required

For this manuscript to become publishable, the authors would need to:

1. **Derive α from first principles.** Show, using only the axioms of the causal graph model (without invoking GR or Newtonian gravity), that α = 1 is the unique correct value.

2. **Provide an operational definition of q.** Describe how q can be measured, even in principle, without presupposing the metric.

3. **Confront the equivalence principle.** Either (a) prove that q-dependent decoherence does not violate LPI, or (b) acknowledge the violation and derive experimental constraints.

4. **Define the equation of motion.** Provide the continuum differential equation for "information-prioritized paths" and prove it reduces to the geodesic equation used in the GW calculations, or recompute all predictions using the correct equation.

5. **Itemize assumptions honestly.** List every independent choice made in the derivation (edge weight rule, path statistic, continuum limit, time/space split, coordinate choice, additivity function) and justify each on its own terms.

### 7.4 Final Recommendation

**REJECT.** The manuscript's central claim — that all DGF phenomenology follows from the single hypothesis dτ = q·dt — is unsupported by the evidence provided. The hypothesis is not a single postulate but a collection of independent, unevidenced choices; it cannot be given an operational definition without circularity; it violates the equivalence principle at a foundational level; and the physical consequences that supposedly distinguish DGF from GR depend on a concept ("information-prioritized path") that has no mathematical definition.

The underlying research program — deriving spacetime geometry from quantum information on causal graphs — is scientifically worthwhile. But the claim to have succeeded, and to have done so from a single postulate, is premature and, in its current form, incorrect.

---

*Referee F, PRL Foundations Panel*
*Date: 2026-06-10*
