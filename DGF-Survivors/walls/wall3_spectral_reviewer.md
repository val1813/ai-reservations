# Reviewer Report: "Spectral Graph Theory Breaks Wall #3"

**Journal**: Nature Physics
**Reviewer**: Anonymous (Referee #4 — Spectral Methods Specialist)
**Recommendation**: **Reject** — the tool measures what it was given; it does not derive what it claims
**Date**: 2026-06-12

---

## Summary of Claims

The manuscript asserts that a "spectral dimension detection tool" — which takes an adjacency matrix of the DGF information graph, computes normalized Laplacian eigenvalues, fits the Weyl law log N(λ) = (d/2) log λ + const, and extracts an effective dimension d_eff — demonstrates that DGF information graphs are 3-dimensional. The authors report:

- 3D geometric graphs yield d_eff → 3 (Weyl R² > 0.97)
- 2D graphs yield d_eff → 2 (control verification)
- The spectral convergence theorem of von Luxburg / García Trillos guarantees that the graph Laplacian converges to the continuous Laplace-Beltrami operator
- Therefore, the DGF field equation ∂_τ q = D∇²q − Γ(q) has a rigorous 3D continuous limit

I have examined these claims under the assumption that the numerical computations are correctly executed. Even granting this assumption — and I note several irregularities in the reported N-scaling data that call even the numerics into question — the argument fails at the conceptual level. The spectral tool is a **dimension detector**, not a **derivation engine**. It measures the dimension of a graph it is given; it does not explain why the DGF information graph has that dimension. Wall #3 requires the latter. The manuscript has confused measurement with explanation.

---

## MAJOR OBJECTION 1: The N-Scaling Trend Refutes Convergence to d = 3

### 1.1 Periodic Cubic Lattice: Non-Monotonic Oscillation, Not Convergence

The reported data for periodic cubic lattices:

| N | d_eff | Δ from 3.00 |
|---|-------|-------------|
| 125 | 3.447 | +0.447 |
| 343 | 3.887 | +0.887 |
| 1000 | 3.371 | +0.371 |
| 1728 | 3.192 | +0.192 |
| 3375 | 3.092 | +0.092 |

The authors interpret this as "d_eff → 3." This interpretation is unjustified for three independent reasons.

**First: the trend is non-monotonic.** The sequence 3.447 → 3.887 → 3.371 → 3.192 → 3.092 is not monotonic convergence. At N = 343, d_eff overshoots to 3.887 — a 29% deviation from the claimed asymptotic value — before retreating. A genuine convergence to 3.00 would produce δ_n = |d_eff(N) − 3| that is strictly decreasing for sufficiently large N. Here δ_5 = 0.092 < δ_4 = 0.192 < δ_3 = 0.371, but δ_3 < δ_2 = 0.887 is violated. The non-monotonicity at N = 343 indicates that we are observing **finite-size oscillations**, not asymptotic convergence. Five data points, of which one is an outlier in the wrong direction, do not constitute a convergence trend.

**Second: the functional form of the convergence is unknown.** The authors have not performed a systematic finite-size scaling analysis. What is the functional form of d_eff(N) as N → ∞? Possibilities include:

- Power-law: d_eff(N) = 3 + c·N^(−α), α > 0
- Logarithmic: d_eff(N) = 3 + c/log(N)
- Oscillatory with decaying envelope: d_eff(N) = 3 + A·N^(−β)·sin(ω log N + φ)

Without determining which functional form describes the data, extrapolating N = 3375 → N = ∞ to conclude "d_eff = 3" is curve-fitting with a predetermined conclusion. If the true behavior is d_eff(N) = 3 + A·N^(−β)·sin(ω log N + φ) — which is common in finite-size scaling of spectral quantities on lattices — then N = 3375 could be near a local minimum of the oscillation, and N = 10^6 could just as plausibly give d_eff = 3.3 as d_eff = 3.0.

**Third: the R² values are insufficient to distinguish convergence from oscillation.** The reported Weyl fit R² ranges from 0.949 to 0.973. While "R² > 0.9" sounds impressive, for a log-log linear fit to an integrated eigenvalue counting function on a regular lattice, the expected R² under the null hypothesis of "the data is roughly a power law" is >0.95 by construction. The Weyl law N(λ) ∝ λ^(d/2) is an asymptotic relation; finite-size corrections mean that even a perfect 3D lattice will show R² < 1 at finite N. The authors must demonstrate that their R² values are **better** than those expected from a null model (e.g., random graphs with matched degree distributions) before claiming spectral evidence for d = 3. This has not been done.

**Required but absent**: Fit the N-dependence of d_eff(N) to at least power-law and oscillatory-decay functional forms. Report the extrapolated N → ∞ limit with uncertainty. If the 95% confidence interval for d_eff(∞) includes values below 2.8 or above 3.2, the claim "d_eff → 3" is not statistically supported by the data presented.

### 1.2 Open Boundary Cubic Lattice: The Trend Points Downward

The open boundary data is even more damaging:

| N | d_eff |
|---|-------|
| 343 | 3.340 |
| 1000 | 2.904 |
| 1728 | 2.774 |

The trend is **monotonically decreasing**: 3.340 → 2.904 → 2.774. Each successive data point moves further from 3.00, not closer. The difference between successive values:
- δ(343→1000) = −0.436
- δ(1000→1728) = −0.130

The step size is decreasing, which could indicate convergence to a value **below 2.77**, not to 3.00. If one fits these three points to an exponential decay d_eff(N) = d_∞ + A·exp(−N/N₀), the extrapolated d_∞ would be approximately 2.6–2.7, not 3.0.

The authors dismiss open boundaries as "less physical" because "DGF information graphs are periodic." This is an assertion, not a derivation. DGF axioms say nothing about periodic boundary conditions on the information graph. If the physical universe is finite — which it is — then its information graph must have a boundary of some kind. The open-boundary result (d_eff → ~2.7) is arguably **more** physically relevant than the periodic result for a finite universe. The authors cannot simultaneously claim that periodic boundary conditions are "physical" for DGF while ignoring that the actual universe is not periodic on any scale we can probe.

**The open-boundary data, taken at face value, suggests that the effective spectral dimension of a 3D cubic lattice with open boundaries is below 3.** If the spectral tool cannot correctly recover d = 3 for an open 3D lattice — a graph that is manifestly 3D by construction — then its "measurement" of d = 3 for DGF information graphs proves nothing about their actual dimension.

---

## MAJOR OBJECTION 2: The Spectral Convergence Theorem Does Not Apply to DGF Information Graphs

### 2.1 The von Luxburg / García Trillos Theorem: What It Actually Requires

The authors invoke "the spectral convergence theorem of von Luxburg / García Trillos" as a guarantee that their graph Laplacian converges to the continuous Laplace-Beltrami operator. Let me state precisely what this body of work actually establishes.

The relevant results (von Luxburg et al., JMLR 2008; García Trillos & Slepčev, JMLR 2016; García Trillos et al., FoCM 2020) concern the spectral convergence of **graph Laplacians constructed from random geometric graphs** to the **weighted Laplace-Beltrami operator** on a **Riemannian manifold**. The precise statement is:

> Let M be a compact smooth Riemannian manifold of dimension d. Let X_n = {x_1, ..., x_n} be i.i.d. samples from a probability distribution P on M with density ρ (bounded above and below away from zero). Construct a graph G_n with vertices X_n and edge weights w_ij = η_ε(|x_i − x_j|) for a kernel η_ε with bandwidth ε = ε(n). Then, under appropriate conditions on ε(n) → 0 and nε(n)^d → ∞, the normalized graph Laplacian L_n converges spectrally to the weighted Laplace-Beltrami operator Δ_ρ.

The theorem's premises include — in exhaustive detail — the following requirements:

1. **The graph is undirected.** Edge weights are symmetric: w_ij = w_ji.
2. **The graph is constructed from points sampled i.i.d. from a manifold.** The vertices are random draws from a probability distribution on a smooth manifold M.
3. **Edge weights are constructed from a symmetric kernel.** w_ij = η_ε(|x_i − x_j|) where η_ε is a smooth, symmetric, compactly supported function of Euclidean distance.
4. **The density ρ is bounded away from zero and infinity.** 0 < ρ_min ≤ ρ(x) ≤ ρ_max < ∞ for all x ∈ M.
5. **The manifold M is known a priori.** The theorem proves convergence of the graph Laplacian to the Laplacian **on that manifold**. It does not prove that the graph "has" that manifold structure — the manifold is an input to the construction, not an output of the theorem.

### 2.2 DGF Information Graphs Violate Every Premise

The DGF information graph, as defined by the DGF axioms, has the following properties:

**(a) Directed edges.** The DGF "overflow direction" — information flowing from high-q to low-q nodes under the action of Axiom 3 — creates directed edges. The normalized Laplacian L = I − D^(−1/2) A D^(−1/2) is defined for **undirected** graphs. For directed graphs, the Laplacian is not uniquely defined — there exist multiple generalizations (Chung's directed Laplacian, the magnetic Laplacian, random-walk Laplacian on directed graphs), none of which share the spectral convergence properties of the undirected normalized Laplacian. The authors do not specify which directed Laplacian they use, nor do they prove a spectral convergence theorem for that choice.

**(b) Weighted edges with Cartan parameters.** DGF edge weights involve the Cartan parameter c_e, which is derived from the q-field configuration. These weights are not symmetric kernel evaluations of Euclidean distances between manifold-embedded points — they are dynamical variables that depend on the field configuration. The spectral convergence theorems assume **static** edge weights constructed from a **known** kernel. Dynamic, field-dependent weights have no convergence guarantee.

**(c) Missing connections due to causal shielding.** DGF Axiom 2 (capacity bound) and Axiom 3 (overflow irreversibility) together imply that some node pairs that are "geometrically adjacent" may lack edges because information flow between them is blocked by causal shielding (A = 1 regions). This means the DGF information graph is in general a **subgraph** of the underlying geometric adjacency graph. Spectral properties of subgraphs are not guaranteed to converge to the manifold Laplacian — indeed, removing edges typically reduces the effective spectral dimension (as the open-boundary cubic lattice results already demonstrate).

**(d) No underlying manifold.** The entire point of DGF is that spacetime is **emergent** from the information graph. There is no pre-existing manifold M from which graph vertices are sampled. The von Luxburg / Trillos theorem assumes that vertices are i.i.d. samples from a distribution on a known manifold. Applying the theorem to a graph whose manifold structure is the object to be proved is circular: it assumes the existence of the manifold to prove that the graph Laplacian converges to the operator on that manifold.

### 2.3 The Affirming-the-Consequent Structure

The logical structure of the manuscript's appeal to spectral convergence is:

1. **If** a graph is constructed from points on a 3D manifold, **then** its normalized Laplacian converges to the 3D Laplace-Beltrami operator. (True, under the theorem's premises.)
2. **If** a graph's Laplacian appears to converge to something 3D-like, **then** the graph must be a 3D manifold graph. (Non sequitur — the theorem states an implication, not an equivalence.)
3. The DGF information graph's Laplacian has spectral properties resembling a 3D graph. (Claimed, but see Objection 1.)
4. Therefore, the DGF information graph is a 3D manifold graph. (Does not follow.)

This is the fallacy of affirming the consequent: P → Q, Q, therefore P. The theorem says "random geometric graph on M → spectral convergence to Δ_M." The manuscript uses this as "spectral properties resembling 3D → graph must have 3D manifold structure." The theorem provides no such reverse implication. There exist graphs that are not random geometric graphs on any manifold but whose spectral dimension is 3 (e.g., expander graphs at critical percolation, certain fractal lattices tuned to spectral dimension 3). The spectral tool cannot distinguish between "genuinely 3D" and "effectively 3D for the measured spectral range."

---

## MAJOR OBJECTION 3: The Density Condition Is Self-Defeating

### 3.1 The Condition and Its Violation

The spectral convergence theorems require a density condition: deg(v) ≫ log N for all vertices v. For a 3D cubic lattice with N = 1000 nodes, the degree is deg = 6 (coordination number of the simple cubic lattice), and log(1000) ≈ 6.9. Therefore:

$$6 < 6.9 \implies \text{density condition not satisfied}$$

The cubic lattice **fails** the density condition. But the cubic lattice is manifestly 3D — it has a rigorous continuous limit (the 3D Poisson equation on a cubic grid converges to the continuum Laplacian under standard finite-difference analysis, no spectral graph theory required). The fact that the spectral tool's own validity criterion rejects a graph known to be 3D demonstrates that **the density condition is not a necessary condition for a graph to have a 3D continuous limit.**

### 3.2 The Implication for DGF

If the density condition is too strict — rejecting graphs that are physically 3D — then its satisfaction by a DGF information graph proves nothing about whether that graph has a 3D continuum limit. And if the density condition is **not** necessary, then the spectral convergence theorems (which require it) do not apply to cases where the condition is violated — including, potentially, DGF information graphs with low-degree nodes or causal shielding gaps.

### 3.3 A Specific Concern

The cubic lattice has deg = 6, which is the **maximum** possible coordination number for a simple cubic lattice. DGF information graphs, with causal shielding and capacity bounds, will generally have **lower** average degree than a regular cubic lattice of the same node count. If even deg = 6 fails the density condition at N = 1000, DGF graphs — with missing edges and shielded regions — will fail it more severely. The spectral tool is thus being applied to graphs for which its own theoretical foundation (the convergence theorem) does not hold.

The authors must either:
1. Prove a spectral convergence theorem that does not require the density condition (no such theorem exists in the current literature), or
2. Demonstrate that DGF information graphs satisfy the density condition at all relevant scales (which would require deg ≫ log N, i.e., very high connectivity not expected from local causal graphs), or
3. Concede that the spectral convergence guarantee does not apply.

---

## MAJOR OBJECTION 4: This Does Not Address Wall #3 — It Answers a Different Question

### 4.1 What the Spectral Tool Actually Does

The spectral tool performs the following operation:

> **Input**: An adjacency matrix A (a graph).
> **Output**: An effective dimension d_eff extracted from the eigenvalue spectrum.

This is a **measurement** performed on a **given** graph. It answers the question: "Given this specific graph, what is its effective spectral dimension?"

### 4.2 What Wall #3 Actually Requires

Wall #3 is the problem of deriving macroscopic continuous spacetime from microscopic discrete DGF axioms. Its precise formulation is:

> **Wall #3**: Do the DGF axioms (causal graph, capacity bound, overflow irreversibility, archive accumulation) **necessarily imply** that the coarse-grained information graph converges, in the continuum limit, to a 3+1 dimensional Lorentzian manifold whose metric satisfies Einstein-like field equations?

This is a **derivation** problem. It requires showing that the macroscopic structure is an **output** of the microscopic axioms — that 3D space is not put in by hand but emerges necessarily from the information dynamics.

### 4.3 The Category Error

The spectral tool answers a **measurement** question about a graph that has already been constructed. Wall #3 asks a **derivation** question about what graph structure the DGF axioms necessarily produce.

These are questions in different categories:

| | Spectral Tool | Wall #3 Requirement |
|---|---|---|
| **Question type** | Measurement (descriptive) | Derivation (prescriptive) |
| **What is given** | The graph (adjacency matrix) | The axioms |
| **What is computed** | d_eff of the given graph | Whether any graph satisfying the axioms must have d = 3 |
| **Logical form** | "This graph has d = 3" | "All DGF graphs must have d = 3" |
| **Type of claim** | Existential (∃ graph: d = 3) | Universal (∀ DGF graphs: d = 3) |

The manuscript has provided evidence for an existential claim — "some DGF-like graphs have spectral dimension 3" — and presented it as though it were a universal claim — "DGF axioms imply spectral dimension 3." One example (or even several examples) of 3D DGF graphs does not prove that the axioms **force** 3D. It proves only that 3D graphs are **compatible** with the axioms — a much weaker statement.

### 4.4 The Circularity of the Construction

The authors construct DGF information graphs that are 3D (cubic lattice, FCC, random geometric graph in ℝ³, perturbed cubic in ℝ³), then apply the spectral tool and report d_eff ≈ 3. This is not a discovery — it is a consistency check on the spectral tool. The procedure:

1. Build a graph that is 3D by construction (explicitly embed vertices in ℝ³).
2. Measure its spectral dimension.
3. Find d_eff ≈ 3.
4. Claim this shows DGF information graphs are 3D.

Step 4 is a non sequitur. Step 1 already assumed the conclusion (3D embedding). Steps 2–3 merely verify that the spectral tool works correctly on graphs known to be 3D. The manuscript has demonstrated that a dimension-detection algorithm detects the dimension that was used to construct the graph. This is a validation of the algorithm, not a validation of the DGF axioms.

To actually address Wall #3, the authors would need to:
1. Start from the DGF axioms **without** specifying a spatial embedding.
2. Let the graph structure **emerge** from the axioms and the information dynamics.
3. Apply the spectral tool to the emergent graph.
4. Find d_eff ≈ 3 **as an emergent property**, not as a built-in feature.

The manuscript does none of this. The graphs are constructed with 3D embedding as a premise; the spectral tool reports 3D; the conclusion is "therefore DGF graphs are 3D." The premise was the conclusion.

---

## THE FATAL BLOW: Dimension Detector vs. Derivation Engine

### The Core Confusion

The manuscript's central error is a confusion between two fundamentally different scientific instruments:

**A dimension detector** takes a graph as input and returns its effective dimension. It is a measurement device. It is useful for characterizing graphs whose structure is already known or hypothesized. It cannot tell you **why** the graph has that dimension, nor whether a different graph constructed from the same axioms would have the same dimension.

**A derivation engine** takes axioms as input and returns the necessary structure of the emergent continuum. It is a logical device. It answers questions of the form "do these axioms imply this structure?" It operates at the level of possibility and necessity, not at the level of measurement.

The spectral tool is unambiguously a dimension detector. Wall #3 requires a derivation engine. The manuscript has deployed a detector, measured the dimension of graphs that were constructed to be 3D, and declared the result a derivation. This is a category error so fundamental that it is not remediable by additional data or refined analysis. No amount of R² > 0.99, no number of graph geometries tested, no extension to N = 10^9 will transform a measurement into a derivation.

### What Would Actually Be Required

To address Wall #3 using spectral methods, the authors would need to prove a theorem of the following form:

> **Theorem (required, does not currently exist):** Let G be any directed, weighted graph satisfying the DGF axioms (capacity bound, overflow irreversibility, archive accumulation) with N vertices. Let L_N be the normalized Laplacian of G. Then, as N → ∞ under coarse-graining, the spectrum of L_N converges to the spectrum of the Laplace-Beltrami operator on a compact 3-dimensional Riemannian manifold, and the limiting manifold satisfies ∂_τ q = D∇²q − Γ(q) with the same parameters D, Γ as the discrete dynamics.

No such theorem exists. The von Luxburg / García Trillos theorem is a theorem about undirected random geometric graphs with kernel-based edge weights constructed from a known manifold — it does not even have the same premises as the DGF problem, let alone the same conclusion. The manuscript's invocation of this theorem is an argument by vague association ("both use Laplacians") rather than a rigorous logical deduction.

### The Uneasy Relationship with the Other Wall #3 Attacks

I note that the authors have produced multiple "Wall #3 breakthrough" claims using different methods: RG invariance of archive information (attacked by Referee #3), universality enumeration (attacked by another referee), and now spectral graph theory. A theory that requires three entirely different — and mutually inconsistent — arguments to break the same wall is a theory that has not broken the wall by any of them. If the RG invariance argument were sound, the spectral argument would be unnecessary. The multiplicity of attempted proofs, each attacking a different aspect of the problem while leaving the core untouched, is itself evidence that Wall #3 remains standing.

---

## ADDITIONAL TECHNICAL CONCERNS

### A. Random Geometric Graph: The d_eff Trend Is Inconclusive

The random geometric graph data — N = 300 → 2.574, N = 500 → 2.986, N = 800 → 3.393, N = 1000 → 3.365 — shows values both above and below 3. The sequence: 2.574 → 2.986 → 3.393 → 3.365. As with the periodic cubic data, this is non-monotonic (overshoots to 3.393, then retreats to 3.365). With only four data points, no monotonic trend, and an overshoot, claiming convergence to 3.00 is wishful extrapolation. Four points are insufficient to distinguish convergence from oscillation; the difference between consecutive values (0.412, 0.407, 0.028) is itself not monotonic.

### B. The 2D Control Is Not a Real Control

The 2D control (20² → 2.385, 30² → 2.158, 50² → 2.062) shows d_eff trending toward 2 from above — a genuine convergence pattern (monotonic, decreasing, approaching 2). But this only validates that the spectral tool works on regular lattices whose dimension is known a priori. It does not validate the tool's application to DGF information graphs, which are:
- Directed (not undirected like the 2D test lattice)
- Dynamically weighted (not unweighted like the 2D test lattice)
- Potentially disconnected or causally shielded (not fully connected like the 2D test lattice)

The 2D control demonstrates that the code runs without errors. It does not demonstrate that the tool produces meaningful results on graphs with the structural properties of DGF information graphs.

### C. No Error Analysis on the Weyl Fit

The Weyl law N(λ) ∝ λ^(d/2) is an asymptotic relation valid for λ → ∞. The eigenvalue spectrum of a finite graph contains low-frequency modes (small eigenvalues) that deviate from the Weyl asymptotics. The authors report a single d_eff from a log-log fit but do not specify:

1. The eigenvalue range used for the fit (how many low eigenvalues were excluded?)
2. The sensitivity of d_eff to the fitting range (does d_eff change if the fit window is shifted by 10%?)
3. The uncertainty on d_eff from the linear regression (what is the 1σ confidence interval?)
4. The goodness-of-fit beyond R² (reduced χ², residuals analysis, test for heteroscedasticity)

For a claim of this magnitude — "the spectral dimension of DGF graphs is 3" — the absence of any error analysis on the Weyl fit is unacceptable. If varying the fitting range by ±20% changes d_eff by ±0.3 or more, the central value "3.00" is an artifact of the fitting procedure, not a property of the graph.

### D. Eigenvalue Degeneracy and Spectral Gaps

Regular lattices have highly degenerate eigenvalue spectra due to symmetry. The Weyl law for degenerate spectra requires counting eigenvalues **with multiplicity**, but the functional form N(λ) ∝ λ^(d/2) assumes a continuous spectral density without gaps. Finite lattices have spectral gaps (intervals containing no eigenvalues) that produce steps in N(λ). Fitting a smooth power law through a step function will produce a systematic bias in the extracted exponent. The authors should demonstrate that their eigenvalue counting accounts for degeneracy and spectral gaps, and that the extracted d_eff is stable under different binning or smoothing procedures.

---

## SYNTHESIS AND VERDICT

### The Argument, Laid Bare

The manuscript's logical structure is:

1. Build graphs that are 3D by construction (cubic lattice, FCC, etc.).
2. Apply a spectral dimension detection algorithm to these graphs.
3. The algorithm reports d_eff ≈ 3.
4. Invoke the von Luxburg / García Trillos spectral convergence theorem.
5. Conclude that DGF information graphs have a rigorous 3D continuous limit and that Wall #3 is broken.

**Step 4 is a non sequitur** — the theorem's premises are not satisfied by DGF information graphs (Objection 2).

**Step 5 is a category error** — the spectral tool measures the dimension of a given graph; it does not derive the dimension from the DGF axioms (Objection 4, Fatal Blow).

**Even Step 3 is questionable** — the reported N-scaling trends do not support convergence to d = 3 for open boundary conditions, and the periodic data is consistent with finite-size oscillations (Objection 1).

And the density condition — the very criterion the spectral convergence theorem uses to determine validity — rejects cubic lattices at N = 1000, demonstrating that the theorem's own applicability criterion is not a necessary condition for 3D continuum limits (Objection 3).

### The Deeper Issue

This manuscript is part of a pattern I observe across multiple Wall #3 submissions: the authors construct a computational or mathematical tool designed to recover 3D structure, apply it to graphs that have 3D structure by construction, and then claim the tool has "broken Wall #3." In each case, the tool is a detector, not a derivation — it measures what it was given, not what the axioms imply.

Wall #3 is the problem of **deducing** 3D from the axioms. No amount of numerical detection, no number of R² values, no quantity of spectral fits can substitute for a logical derivation. The manuscript has demonstrated — at best — that if DGF graphs happen to be 3D, a spectral tool can confirm it. But that conditional ("if DGF graphs happen to be 3D") is precisely Wall #3. The conditional has been assumed as a premise and then "discovered" as a conclusion. This is the fallacy of petitio principii — begging the question — in computational form.

### Required for Resubmission

Should the authors wish to pursue a spectral approach to Wall #3, the minimum requirements are:

1. **Derive the graph from the axioms, not from ℝ³.** Start with the DGF axioms and generate the information graph structure through the dynamics alone, without any spatial embedding. Then apply the spectral tool. If d_eff ≠ 3, the axioms do not imply 3D. If d_eff = 3, this is the first actual evidence.

2. **Prove a convergence theorem for DGF graphs.** The von Luxburg / Trillos theorem does not apply. A new theorem — addressing directed edges, dynamic weights, and causal shielding — is required. Without this, the connection between the spectral measurement and any continuous limit is unsubstantiated.

3. **Perform proper finite-size scaling for d_eff(N).** Five data points with a non-monotonic trend do not establish convergence. At minimum: 10+ sizes spanning at least two orders of magnitude in N, with functional-form fitting and extrapolated N → ∞ limits with confidence intervals.

4. **Address the open-boundary failure.** If the spectral tool reports d_eff < 3 for open-boundary 3D lattices, it is not a reliable dimension detector. Either fix the tool to correctly recover d = 3 for open 3D lattices, or explain why DGF information graphs must be periodic.

5. **Provide a logical argument, not a measurement.** Wall #3 is a derivation problem. Measurements characterize what exists; derivations establish what must exist. A spectral measurement, no matter how precise, cannot substitute for a derivation.

### Final Recommendation

**Reject.** The spectral tool is a dimension detector applied to graphs constructed with 3D embedding as a premise. It measures what was put in; it does not derive what must come out. This is not a matter of insufficient data or imprecise measurements — it is a category error at the conceptual foundation of the argument. Wall #3 remains unbroken.

---

*The reviewer is a specialist in spectral graph theory and computational differential geometry with 15 years of experience in Laplacian spectral analysis of complex networks. This review reflects an independent assessment of the manuscript's mathematical and logical content.*

*Confidential note to the editor: This is the fourth Wall #3 submission I have reviewed from this group, each using a different method (RG invariance, universality enumeration, and now spectral graph theory). In each case, the method measures or assumes what it claims to derive. I recommend consolidating these reviews — the pattern across manuscripts is more informative than any individual submission. A synthetic rejection letter addressing the shared logical structure (detector vs. derivation confusion) would be more productive than four separate rebuttals.*

---

*Anonymous Referee #4, Nature Physics*
*Review submitted: 2026-06-12*
