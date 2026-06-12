# Referee Report v2 — Nature Physics

**Manuscript:** "Effective Metric from Information Processing Rate: A Derivation Without Ansatz" (Revised)
**Recommendation:** Reject (the five fixes do not resolve the structural problems — they clarify the physical picture but reveal deeper assumptions)
**Confidential to Editor:** Yes
**Benchmark Standard:** Bojowald-Duque, PRD 109, 084006 (2024)

---

## Re-review Scope

In my first report, I identified five independent problems in the claimed derivation chain. The authors have submitted a revised manuscript with targeted fixes for each attack. This second review examines whether the fixes genuinely resolve the problems or merely relocate them.

**Short answer: the fixes clarify the authors' physical picture but do not resolve the structural problems. Two of the five attacks (Attacks 1 and 3) are now *harder*, not easier, to defend — the fixes have revealed deeper assumptions that were previously hidden. Attack 1 in particular now exposes the central question: is τ_eff = τ₀/q unique, and if not, how many free functions does the "derivation" contain?**

---

## RE-EXAMINATION OF ATTACK 1: τ_eff = τ₀/q — The Fix Reveals the Core Problem

### The Authors' Fix

The revised manuscript states:

> "q is operationally defined as the accessible capacity fraction. Axiom 2 stipulates ≤1 bit/τ₀. Available capacity = q × (1 bit/τ₀). Processing 1 bit time = τ₀/q. This is not a choice — it is forced by the definition of q. τ_eff = τ₀/q is unique."

### Analysis

The authors' logic contains three steps:

1. Total capacity: 1 bit/τ₀ (Axiom 2 upper bound, converted to equality)
2. Available capacity: q × (1 bit/τ₀) (definition of q as accessible fraction)
3. Processing time for 1 bit: τ₀/q (converting bandwidth to latency)

**Step 3 is not forced by Steps 1-2.** It requires three unstated modeling assumptions:

**(a) The throughput bound is saturated.** Axiom 2 states "≤O(1) bit/τ₀" — an upper bound, not an exact processing rate. The actual processing rate could be strictly less than the bound for reasons unrelated to q (overhead, inefficiency, graph topology). The authors replace the inequality ≤ with equality =, and then convert this equality into an exact processing time. If the actual processing rate is some fraction α < 1 of the bound, then τ_eff = τ₀/(αq), introducing an additional parameter α.

**(b) Processing work is exactly 1 bit per update.** The conversion "bandwidth → latency" requires specifying the work. The authors assume each lattice update processes exactly 1 bit of information. But in a causal graph, an update might process variable amounts of information depending on the node's connectivity, its q-value, and the information arriving from neighbors. If the work W is variable, τ_eff = W·τ₀/q, introducing functional freedom through W(q, neighbors).

**(c) Bandwidth scales linearly with q.** The step from "available capacity = q × total capacity" to "processing rate = q × maximum rate" assumes that the effect of archiving on processing throughput is a proportional reduction. But information archiving could affect throughput nonlinearly — for instance, if archived information creates interference patterns that reduce effective throughput faster than linearly (τ_eff = τ₀/q^γ with γ > 1), or if the system has compensatory mechanisms that partially mitigate the slowdown (γ < 1).

### The Queueing Theory Counterexample

The authors frame the problem as a bandwidth question. But DGF nodes are information PROCESSORS — they receive, process, and forward information. This is a queueing system. Queueing theory provides a well-studied relationship between utilization and latency that is NOT linear.

Consider an M/M/1 queue — the simplest nontrivial queueing model:
- Service rate μ = 1/τ₀ (maximum processing rate)
- Utilization ρ = 1 - q (fraction of capacity occupied by "archived" traffic)
- Available capacity: q = 1 - ρ
- Mean wait time: W = τ₀/(1 - ρ) = τ₀/q ✓ (matches the authors' form!)
- BUT mean queue length grows as ρ/(1-ρ) = (1-q)/q
- AND the variance of wait time is τ₀²/(1-ρ)² — which diverges as q → 0

However, M/M/1 is ONE queueing model. Different queueing disciplines give different relationships:
- M/D/1 (deterministic service): W = τ₀·(2-ρ)/(2(1-ρ)) = τ₀·(1+q)/(2q)
- Processor sharing: depends on the job size distribution
- Priority queues: high-priority traffic sees W ≈ τ₀, low-priority sees W ≈ τ₀/(q(1-ρ_high))

The point is not that M/M/1 gives the "right" answer — it is that the relationship between q and processing latency depends on the queueing model, and the queueing model is NOT specified by DGF axioms. The authors have implicitly adopted one specific queueing model (deterministic service, FIFO, unit work per update, saturated throughput) without acknowledging that this constitutes a modeling choice.

### The Information-Theoretic Counterexample

Alternatively, frame the node as an information-theoretic channel. Shannon's channel capacity theorem states that information can be transmitted at any rate R < C with arbitrarily low error, where C is the channel capacity. If the node's capacity is C = q/τ₀ (bits per unit time), then:
- At rate R = C, the coding scheme may require arbitrarily long block lengths → arbitrarily long latency
- At rate R = C/2, latency can be made small
- The relationship between R and latency is governed by the channel coding theorem's finite-blocklength corrections, which scale as ~√(V/n)·Q^{-1}(ε) where V is channel dispersion

In other words: Shannon theory does NOT give a unique latency for a given capacity. Latency depends on the coding scheme, the error tolerance, and the block length. The formula τ_eff = τ₀/q is one point in a multidimensional space of (capacity, latency, error, blocklength) tradeoffs.

### The Critical Question: Is τ_eff = τ₀/q UNIQUE?

The authors claim "yes — forced by the operational definition of q."

The correct answer is: **no — the relationship between accessible capacity fraction q and processing latency τ_eff depends on at least these modeling choices, none of which are specified by DGF axioms:**

| Modeling Choice | DGF's Implicit Choice | Alternative | Effect on τ_eff |
|:---|---:|---:|:---|
| Throughput vs bound | Saturated (rate = bound) | Rate could be α×bound, α<1 | Introduces parameter α |
| Work per update | Exactly 1 bit | Variable W(q) | Introduces function W(q) |
| Bandwidth-latency relation | Reciprocal (τ = 1/rate) | Queueing model dependent | Introduces queue discipline |
| Queue discipline | Implicitly FIFO/deterministic | M/M/1, M/D/1, PS, priority | Different τ_eff(q) |
| Coding scheme | Fixed-rate, block=1 | Variable block length | Finite-blocklength corrections |
| Error tolerance | Zero-error (implicit) | ε-error allowed | Blocklength-latency tradeoff |

**Each row is a degree of freedom not constrained by DGF axioms.** The space of admissible τ_eff(q) functions, even under the operational definition of q, is infinite-dimensional.

### Verdict on Attack 1 Fix

**Not resolved. The fix has made the problem MORE visible, not less.** By appealing to the operational definition of q, the authors have exposed the chain of modeling assumptions required to go from "q is the accessible capacity fraction" to "τ_eff = τ₀/q." Each link in that chain is a choice, not a necessity. The claimed uniqueness does not hold.

---

## RE-EXAMINATION OF ATTACK 3: c vs c_eff — The Fix Reveals a Deeper Assumption About the Nature of Space

### The Authors' Fix

The revised manuscript states:

> "Signal propagation = flight between nodes (vacuum c) + processing at node (τ₀/q). Flight time 𝔩/c = τ₀ is negligible compared to τ₀/q when q < 1. Spatial stretching is the spatial projection of processing delay. c is the vacuum speed — it describes propagation between nodes, where there is no q (q is a property of nodes, not of space)."

### Analysis

This fix clarifies the authors' physical picture. It also reveals a deep assumption that was previously hidden: **the existence of a background space in which the information graph is embedded.**

**What is "space" in DGF?** The DGF framework defines a graph G = (V, E) where:
- V is the set of information-processing nodes
- E is the set of causal edges connecting nodes

There are two possible ontologies for this graph:

**Ontology A (Embedded Graph):** The graph is embedded in a pre-existing 3D space. Edges have geometric lengths 𝔩. The speed of light c is a property of this embedding space. Signals "fly" through space along edges at speed c, and nodes are localized objects sitting at vertices that process signals when they arrive.

**Ontology B (Constitutive Graph):** The graph IS space. There is no "background space" — spatial relations are defined by graph connectivity. An edge is not a geometric line through space; it is the primitive spatial relation. "Distance" is defined by signal traversal time along graph paths. c is not a speed through pre-existing space — it is the conversion factor between graph distance and time.

**The authors' fix assumes Ontology A.** The distinction between "flight through vacuum between nodes" and "processing within nodes" requires:
1. A space that exists between nodes (the "vacuum")
2. A speed c that characterizes propagation through this space
3. Nodes that are spatially localized objects within this space

But what is the "vacuum" between nodes made of? If DGF's fundamental ontology is the information graph, then "between nodes" literally means "along edges." An edge IS the spatial relation. There is no "space between nodes" that is not already captured by the edge.

Under Ontology B, the situation is:
- Signal propagation IS edge traversal
- Edge traversal time = τ₀ (by definition: τ₀ = 𝔩/c where 𝔩 is the graph spacing)
- There is no separate "processing time" that adds to traversal time because the edge traversal IS the fundamental process

The total signal propagation time from node u to node v is simply the number of edges traversed times τ₀. There is no additional "processing delay" because what the authors call "processing" (the receiving node handling the incoming signal) is part of what it means for a signal to traverse from u to v in a causal graph. You cannot cleanly separate "flight" from "processing" — the edge traversal time already accounts for whatever happens at the receiving end.

### What the Fix Actually Asserts

The authors' "flight + processing" model is equivalent to a two-component latency:
- Edge traversal: 𝔩/c = τ₀ (this is the "vacuum flight" time)
- Node processing: τ₀/q (this is the "information processing" time)
- Total: τ₀(1 + 1/q)

In the q ≪ 1 limit, the processing term dominates, and dR ≈ c × τ₀/q = 𝔩/q.

But notice what happened: the authors introduced a NEW piece of physics — the "flight through vacuum" that happens BETWEEN nodes, in a space that is not the graph itself. This "vacuum" is not derived from DGF axioms — it is assumed. And this assumption is load-bearing: without "vacuum flight time" being negligible compared to processing time, the total propagation time would include an additive τ₀ that would modify the effective metric.

### Verdict on Attack 3 Fix

**Not resolved.** The fix clarifies the physical picture but introduces a new assumption: that the information graph is embedded in a background vacuum space through which signals propagate at speed c. This assumption is not derived from DGF axioms and contradicts the natural ontology where the graph constitutes space. The "flight vs. processing" distinction is a modeling choice, not a derivational necessity.

---

## RE-EXAMINATION OF ATTACK 2: q → 1 Limit

### The Authors' Response

> "q = 1 → full capacity → τ_eff = τ₀ → no time dilation → dτ = dt. Minkowski recovered. Derivation is self-consistent at q → 1."

### Analysis

The authors correctly note that their derivation is SELF-CONSISTENT at q → 1. But this was never the problem. The problem, as stated in my first report, is that **every candidate function f(q) with f(1) = 1 gives the same q → 1 limit.** The vacuum cannot discriminate among candidate functions. Self-consistency at q → 1 is necessary but not sufficient — it provides zero constraint on the functional form of τ_eff(q) away from q = 1.

The authors' response does not address this point. They have re-stated that their chosen function gives the correct vacuum limit, which I already acknowledged in the first report.

### Verdict on Attack 2 Fix

**Not resolved.** The response confuses self-consistency (which was never disputed) with uniqueness (which was the point of the attack). All admissible f(q) with f(1) = 1 are self-consistent at q → 1. The q → 1 limit provides zero constraint on which f(q) is correct.

---

## RE-EXAMINATION OF ATTACK 4: Local Minkowski Presupposition

### The Authors' Response

> "(τ, R) are physical measurement coordinates. τ is defined by lattice update count. R is defined by signal crossing time × c. Physical observers use physical instruments — (τ, R) are operationally defined, not geometrically presupposed."

### Analysis

This defense shifts the philosophical framing but does not change the mathematical content. Whether you call it a "geometrical presupposition" or an "operational definition," the fact remains:

1. The DGF derivation takes the Minkowski line element in (τ, R) coordinates as the starting point.
2. It then performs a coordinate transformation to (t, r) coordinates.
3. The transformed metric is the DGF effective metric.

This is: Minkowski(τ, R) + coordinate_transform → DGF_metric.

The issue is not whether (τ, R) are "operationally defined" — it is that the step "in physical coordinates, spacetime is Minkowski" contains all the physics of Lorentzian signature, local Lorentz invariance, and pseudo-Riemannian geometry. These properties are not derived from DGF axioms; they are asserted as properties of the (τ, R) coordinate system.

To see this clearly: why is the line element in (τ, R) coordinates exactly Minkowski? Why not:
- de Sitter: ds² = -c²dτ² + e^{2Hτ}(dR² + R²dΩ²) ?
- Anti-de Sitter: ds² = -cosh²(R/L)c²dτ² + dR² + L²sinh²(R/L)dΩ² ?
- A Finsler metric with a preferred frame?

The authors' operational definitions of τ (lattice updates) and R (signal crossing time) define a coordinate system. They do NOT determine the metric in that coordinate system. The metric is additional structure — it specifies how coordinate intervals relate to physical distances. Asserting that the metric in (τ, R) coordinates is Minkowski is equivalent to asserting local Lorentz invariance and a specific signature — neither of which follows from the operational definitions of τ and R alone.

### The Bojowald-Duque Contrast (Revisited)

In Bojowald-Duque, the metric (including its signature) is COMPUTED from the constraint algebra. The structure function q^{ab} appears in the [H, H] bracket, and this same q^{ab} determines the spacetime metric. The Lorentzian signature is encoded in the sign of the [H, H] bracket relative to the [D, D] bracket. None of this is assumed — the algebra either closes (yielding a specific metric) or it does not.

In DGF, by contrast:
- The signature (-, +, +, +) is assumed (by writing the Minkowski line element)
- Local Lorentz invariance is assumed (by asserting the metric is Minkowski locally)
- The pseudo-Riemannian nature of spacetime is assumed (by writing a line element at all)

These are the very properties that a "derivation of the effective metric" should PRODUCE, not assume.

### Verdict on Attack 4 Fix

**Not resolved.** The reframing as "operational definitions" does not change the mathematical fact that the metric structure (signature, local Lorentz invariance, pseudo-Riemannian geometry) is asserted, not derived. The coordinate transformation Minkowski(τ,R) → DGF(t,r) is algebra, not physics.

---

## RE-EXAMINATION OF ATTACK 5: R(r) Undetermined

### The Authors' Response

> "R(r) = ∫₀ʳ dr'/q(r'). q(r) is determined by DGF field equation + source terms. For static spherical symmetry, q(r) = exp(-GM/rc²) → R(r) fully determined. Metric is closed."

### Analysis

The authors have stated a PROGRAM, not a result. The response asserts that q(r) is determined by the DGF field equation, but:

1. **What IS the DGF field equation for q(r)?** The effective metric "derivation" does not produce it. The field equation is a separate construction that has not been presented in this manuscript.

2. **Is the field equation derived from the same first principles?** If the field equation itself contains unevidenced functional choices (analogous to the τ_eff(q) choice in the metric derivation), then the metric is doubly underdetermined — once by the free function in the metric derivation, and again by the free functions in the field equation.

3. **The example q(r) = exp(-GM/rc²) is illustrative, not derived.** The manuscript presents this as the form that q(r) takes for a static spherical source, but the derivation of this form from DGF axioms and the field equation is not provided. Is this the unique spherically symmetric static solution, or is it one of a family parameterized by additional free functions?

4. **The non-locality remains.** g_{θθ} at radius r depends on ∫₀ʳ dr'/q(r') — the entire interior profile of q. This means the angular part of the metric is non-local in the q-field, a feature absent in GR (where g_{θθ} = r² locally) and absent in Bojowald-Duque (where all metric components are determined by local structure functions).

### Verdict on Attack 5 Fix

**Not resolved.** The response defers the problem to a field equation that is not part of the present manuscript and whose derivation status is unknown. The metric remains a template parameterized by the undetermined function q(r).

---

## THE CENTRAL QUESTION: How Many Free Functions?

The authors' claim that their metric is "derived, not assumed" rests on the assertion that every step in the derivation is forced by DGF axioms with no freedom. My first report demonstrated that the function τ_eff(q) is chosen from an infinite family. The revision attempts to close this freedom by appealing to the operational definition of q.

**The core question, sharpened by this re-review, is: how many free functions does the DGF "derivation" actually contain, and how does this compare to the Bojowald-Duque benchmark?**

### The DGF Freedom Inventory

| Degree of Freedom | Location | Dimensionality | Constrained by |
|:---|---|---:|:---|
| τ_eff(q) | Processing time function | ∞-dimensional (any monotone f with f(1)=1) | NOT constrained by DGF axioms; chosen to reproduce GR at 1PN |
| α (throughput saturation) | Axiom 2: ≤ vs = | 1 parameter | NOT constrained |
| W(q) | Work per update | ∞-dimensional functional | NOT constrained |
| c_fundamental vs c_effective | Distance calibration | Binary choice | NOT constrained; vacuum c chosen without justification |
| Metric signature | Local inertial frame | 3-way (Lorentzian, Euclidean, degenerate) | NOT derived; Lorentzian assumed |
| Local Lorentz invariance | Local inertial frame | Yes/No | NOT derived; assumed via Minkowski form |
| Spatial dimensions | Local inertial frame | Integer (3 assumed) | NOT derived from DGF axioms |
| Field equation for q(r) | Determines R(r) = ∫dr/q | ∞-dimensional PDE | NOT derived in this manuscript |
| Solution for q(r) | Determines angular metric components | ∞-dimensional (depends on BCs and source) | Deferred to unsolved field equation |

**Total: Infinite-dimensional functional freedom (at least the space of monotone functions on [0,1] with f(1)=1), plus multiple binary/parametric choices, plus an undetermined field equation.**

### The Bojowald-Duque Comparison

| Property | Bojowald-Duque (PRD 109, 084006) | DGF (this manuscript) |
|:---|:---|:---|
| Origin of metric functions | Computed from constraint brackets | Chosen from admissible family |
| Constraint on metric functions | Algebraic closure (PDE system) | None (any monotone f(q) allowed) |
| Parameterized freedom | ~2-3 modification functions | ∞-dimensional τ_eff(q) + field equation + discrete choices |
| Signature determination | Output of constraint algebra | Assumed (Minkowski local frame) |
| Field equation status | Derived from constraints (Einstein equations) | Not derived; deferred to future work |
| Internal consistency test | Anomaly freedom of constraint algebra | None analogous |

**The structural asymmetry is not merely quantitative — it is qualitative.** Bojowald-Duque's freedom is finite-dimensional and constrained by algebraic consistency conditions (the constraint algebra must close, which imposes PDEs). DGF's freedom is infinite-dimensional and constrained by nothing internal to the framework — the only constraint is external (matching GR at 1PN, which picks out τ_eff = τ₀/q from the infinite family).

### The Teleological Diagnosis

The authors' derivation selects τ_eff = τ₀/q because it is the unique function in the infinite-dimensional space that reproduces the Newtonian limit g_rr ≈ 1 + 2GM/rc² at 1PN. But this is not a derivation from DGF axioms — it is a selection from the space of DGF-consistent functions based on an external requirement (matching GR). The logic is:

1. DGF allows any τ_eff = τ₀/f(q) with f monotone and f(1) = 1
2. Among these, only f(q) = q gives g_rr = 1/q² ≈ 1 + 2GM/rc² at 1PN
3. Therefore τ_eff = τ₀/q

Step 2 reveals the true logical structure: the function is chosen to match GR. This is legitimate — in fact, it is exactly what effective field theory does: write down all terms allowed by symmetry, then fix coefficients by matching to the known low-energy theory. But EFT theorists call this "matching," not "derivation." The authors call it "derivation," and that is the problem.

---

## NET ASSESSMENT: FIX STATUS

| Attack | Original Verdict | Author Response | v2 Verdict | Reason |
|:---|---:|:---|:---:|:---|
| Attack 1 (τ_eff form) | Not derived — unevidenced choice | q's definition forces 1/q | **NOT RESOLVED** | Hidden modeling assumptions (throughput saturation, unit work, linear bandwidth-latency) remain unacknowledged. Infinite-dimensional freedom persists. |
| Attack 2 (q→1 limit) | Zero constraint on f(q) | Self-consistent at q=1 | **NOT RESOLVED** | Confuses self-consistency (acknowledged in v1) with uniqueness (the actual problem) |
| Attack 3 (c vs c_eff) | Unargued choice | Flight (vacuum c) + processing (τ₀/q) | **NOT RESOLVED** | Introduces new assumption: background vacuum space. Graph-as-constitutive-of-space ontology would not support this distinction. |
| Attack 4 (Minkowski presupposition) | Conclusion dressed as premise | (τ,R) are operational definitions | **NOT RESOLVED** | Operational definitions define coordinates, not the metric in those coordinates. Signature and Lorentz invariance are assumed, not derived. |
| Attack 5 (R(r) undetermined) | Template with unknown function | Deferred to field equation | **NOT RESOLVED** | Field equation not presented. Derivation status of field equation unknown. Non-locality remains. |

**Zero of five attacks are resolved.**

---

## FINAL ASSESSMENT

The revision has clarified the authors' physical picture. We now understand better what they are trying to do. But clarification is not resolution. The structural problems identified in the first review survive the revision intact, and two of them (Attacks 1 and 3) are now deeper than before — the fixes have exposed assumptions (background vacuum space, implicit queueing model, linear bandwidth-latency conversion) that the original formulation kept hidden.

**The central claim — "this is a derivation, not an ansatz" — remains unsupported.** The function τ_eff(q) = τ₀/q is one point in an infinite-dimensional space of DGF-consistent functions, selected by the external requirement of matching GR at 1PN. The metric is not derived from DGF axioms; it is matched to GR using the free function τ_eff(q) as the matching parameter. This is a parameterized framework with an external matching condition — a legitimate theoretical structure, but not a derivation.

**The Bojowald-Duque benchmark remains unmet.** Bojowald-Duque earns the word "derivation" because the constraint algebra forces the metric's form through internal consistency. DGF has no analogous consistency condition. Its free function is constrained by matching to GR (external), not by closure of an algebraic structure (internal). Publishing this as a "derivation" would equate external matching with internal algebraic closure, which this reviewer considers a category error.

---

## RECOMMENDATION

**Reject.** The five fixes do not resolve the five attacks. The manuscript should be reconsidered only if the authors provide:

1. **A uniqueness proof for τ_eff(q) = τ₀/q from DGF axioms alone**, without appealing to matching with GR. Specifically, a proof that the modeling choices (throughput saturation = 1, work per update = 1 bit, linear bandwidth-latency relation) are forced by DGF axioms — not merely consistent with them.
2. **A derivation of local Lorentz invariance and the Lorentzian signature from the causal graph structure**, without presupposing a Minkowski local frame.
3. **A clear statement of the theory's free functions and their dimensionalities**, analogous to how Bojowald-Duque explicitly parameterizes their quantization ambiguities.

Absent these, the word "derivation" should be replaced with "motivated ansatz" or "EFT matching" throughout the manuscript. The paper would still be publishable — parameterized frameworks with GR matching are legitimate contributions — but the claim of having derived the metric without ansatz is not supported by the evidence.

---

**Confidential note to Editor:** The revision has the character of a rearguard action rather than a substantive fix. The authors have clarified their position without strengthening it. The central problem — that τ_eff(q) is one choice among infinitely many equally DGF-consistent functions — has not been addressed. The appeal to the "operational definition of q" is a new argument, but it dissolves under examination of the modeling assumptions hidden in the bandwidth-to-latency conversion. I maintain my recommendation to reject.

I note, as I did in v1, that the DGF framework may contain interesting physics. But the specific claim under review — that the effective metric is rigorously derived without ansatz — is false. The authors would be better served by acknowledging the free function, parameterizing it explicitly, constraining it through multiple independent observational channels (not just 1PN matching), and presenting the work as an EFT-style framework. That would be a publishable paper. The current manuscript, claiming a derivation where only a matching exists, is not.

---
