# Reviewer Report: "Spectral RG Flow Breaks Wall #3 Parts 1 and 2"

**Journal**: Nature Physics
**Reviewer**: Anonymous (Referee #5 -- Renormalization Group and Statistical Physics Specialist)
**Recommendation**: **Reject** -- two orders of magnitude extrapolated to 10^61 is not physics; it is numerology
**Date**: 2026-06-12

---

## Summary of Claims

The manuscript asserts that a "spectral RG analysis" of DGF-type information graphs unifies the solutions to Wall #3 Part 1 (discrete-to-continuum limit) and Part 2 (derivation of d=3 from DGF axioms). The reported findings are:

- D(L) ~ L^{-2.58} (R^2 = 0.972) -- diffusion coefficient decays as a power law
- Gamma(L) ~ L^{-0.12} (R^2 = 0.298) -- archiving rate is "nearly scale-independent"
- d_eff -> 2.5-3 -- effective dimension flows to 3 under RG
- At 10^61 scale ratio (Planck to Hubble), D decays by a factor of 10^{157}
- "d=3 is an RG attractor, not an assumption requiring derivation"

I have examined these claims from the standpoint of a practitioner of numerical RG methods. The manuscript's argument is not merely insufficiently supported -- it is structurally incapable of supporting the conclusions drawn from it. The problem is not that the numerics are imprecise; it is that the chain of inference from the numerics to the conclusions contains four independent fatal gaps, each of which alone would justify rejection.

---

## ATTACK 1: The Data Provenance Problem -- What Was Actually Computed?

### 1.1 The Missing Experimental Section

The manuscript reports spectral RG results -- D(L), Gamma(L), d_eff(L) -- attributed to "a neighboring group's data." A scientific paper that rests its central claim on data whose provenance is not documented is not a scientific paper. The following information, which would occupy Section II of any legitimate numerical RG study, is entirely absent:

**The graph.** What graph was the RG run on? The manuscript mentions "DGF-type graphs" without specifying:
- Number of vertices N. Is N = 10^3, 10^4, 10^6? Without N, the claim that "L spans the full range of the graph" is meaningless.
- Graph construction. Were vertices placed on a cubic lattice? A random geometric graph? Generated from DGF dynamical evolution? Each construction produces different finite-size spectral properties, and the RG flow inherits these differences.
- Boundary conditions. Periodic, open, or something else? The prior spectral analysis (Referee #4's review) demonstrated that open-boundary cubic lattices yield d_eff trending below 3 -- a fact that would fundamentally alter the interpretation of any RG flow toward d=3.

**The coarse-graining scheme.** "Spectral RG" is not a standardized protocol. The manuscript must specify:
- Blocking transformation. What is the coarse-graining operation? Is it real-space block-averaging (Kadanoff blocking)? Eigenvalue truncation (momentum-shell RG)? Diffusion-map based coarse-graining? Each scheme produces different finite-size RG trajectories.
- The scale variable L. What does L denote? Linear block size? Number of RG steps? Diffusion time in the spectral embedding? Without defining L, claiming D(L) ~ L^{-2.58} has no operational meaning -- L^{-2.58} in one scheme could be L^{-1.3} or L^{-5.1} in another.
- Observable definitions. How are D(L) and Gamma(L) extracted at each RG step? Are they computed from the coarse-grained Laplacian spectrum? From random walk statistics on the coarse-grained graph? From fitting the q-field equation to coarse-grained dynamics?

### 1.2 The 10^61 Extrapolation: 59 Orders of Magnitude Beyond the Data

This is the single most egregious claim in the manuscript, and it alone warrants rejection.

The manuscript states that at the 10^61 scale ratio (Planck length l_P to Hubble radius H_0^{-1}), the diffusion coefficient D decays by a factor of 10^{157}. This number is obtained by substituting L = 10^61 into D(L) ~ L^{-2.58}:

$$D(10^{61})/D(1) = (10^{61})^{-2.58} = 10^{-157.38}$$

Let us examine what actual numerical data can support. A realistic spectral RG simulation on a graph of N vertices can probe a scale range of at most:

$$L_{\text{max}}/L_{\text{min}} \sim N^{1/d}$$

For a 3D graph:
- N = 10^3 (cubic 10x10x10): L_max/L_min ~ 10
- N = 10^4: L_max/L_min ~ 21.5
- N = 10^5: L_max/L_min ~ 46.4
- N = 10^6: L_max/L_min ~ 100
- N = 10^9: L_max/L_min ~ 1000

Even with N = 10^9 vertices -- pushing the limits of contemporary sparse matrix computation -- the accessible scale range is **three orders of magnitude** (10^3). The manuscript claims to have measured a power law over two orders of magnitude (L=1 to L=100, consistent with N ~ 10^6) and then **extrapolated this power law over 59 additional orders of magnitude** to reach 10^61.

**This is not a small extrapolation. This is not even an aggressive extrapolation. This is 59 orders of magnitude beyond the data -- a factor of 10^59.**

To put this in perspective: if we had measured the height of a single atom (~10^{-10} m) and extrapolated a linear trend, we would reach the diameter of the observable universe (~10^{27} m) by extrapolating 37 orders of magnitude. The manuscript's extrapolation (59 orders) is to that ratio what the universe-to-atom ratio (37 orders) is to... another factor of 10^22. This is extrapolation without precedent in the history of physics.

### 1.3 What Could Go Wrong in 59 Orders of Magnitude

Between L=100 and L=10^61, any of the following could occur -- and standard RG theory *predicts* that some of them *must* occur:

**(a) Crossover to a different fixed point.** The apparent L^{-2.58} scaling could be a crossover exponent valid only at intermediate scales, with the true infrared fixed point having a different exponent. In disordered systems, crossover between fixed points spanning 2-4 orders of magnitude in L is routine (e.g., the Anderson localization transition, where the critical regime spans ~3 decades in conductance). With only 2 decades of data, we cannot distinguish a true asymptotic exponent from a crossover.

**(b) Finite-size saturation.** Any finite graph has a maximum length scale -- the graph diameter. When L approaches the diameter, D(L) stops decaying and saturates at a finite value (the diffusion constant of the finite graph). The manuscript's own framework predicts this: on a finite graph, the smallest non-zero Laplacian eigenvalue lambda_2 sets the maximum diffusion time, and D(L) cannot decay below the value set by lambda_2. The L^{-2.58} power law **must** break down at some L_max set by the graph size. The manuscript provides no estimate of this L_max and no evidence that L_max > 10^61.

**(c) Emergence of new relevant operators.** Under RG flow, operators that are irrelevant at the Gaussian fixed point can become relevant at strong coupling. The q-field equation at microscopic scales is partial_τ q = D nabla^2 q - Gamma(q). At larger scales, higher-derivative terms (nabla^4 q), non-local terms, or couplings to other emergent fields could become relevant and change the effective dynamics qualitatively. The spectral RG as described measures only D(L) and Gamma(L) -- it is blind to the emergence of new operators.

**(d) The spectral dimension may not be the dimension that matters.** The manuscript equates "spectral dimension ~3" with "the continuum limit is 3D." But spectral dimension is only one of many dimensions that characterize a graph (Hausdorff dimension, walk dimension, resistance dimension, etc.). On fractals, these dimensions differ. On random graphs, they can differ even when the graph is not fractal. The RG flow of d_spec says nothing about whether the other dimensions also flow to 3, or whether the limiting object is a manifold.

Each of (a)-(d) is a known, generic feature of RG flows in complex systems. The manuscript addresses none of them. The claim that a two-decade power law can be extrapolated over 59 decades, through an unknown number of crossovers, fixed points, and emergent operators, to reach a cosmological conclusion -- this is not physics. It is curve-fitting with ambition.

---

## ATTACK 2: Gamma(L) ~ L^{-0.12} With R^2 = 0.298 -- The "Constant" That Isn't

### 2.1 R^2 = 0.298 Means the Fit Explains Nothing

The manuscript reports Gamma(L) ~ L^{-0.12} with R^2 = 0.298 and interprets this as "the archiving rate is nearly scale-independent" and "Gamma is approximately constant." This interpretation is statistically indefensible.

An R^2 of 0.298 means that 70.2% of the variance in Gamma(L) is **not** explained by the power-law fit. The conventional interpretation of R^2 in physical modeling is:

- R^2 > 0.9: Strong evidence for the proposed functional form
- 0.7 < R^2 < 0.9: Moderate evidence; alternative forms not ruled out
- 0.5 < R^2 < 0.7: Weak evidence; data consistent with many functional forms
- R^2 < 0.5: **No statistical evidence for the proposed functional form over the null hypothesis**

R^2 = 0.298 falls squarely in the last category. The data do not support the claim that Gamma(L) follows L^{-0.12}. The exponent -0.12 is not a measurement -- it is a random number produced by fitting noise.

### 2.2 What Gamma(L) Could Actually Be Doing

With R^2 = 0.298, the data are consistent with **all** of the following hypotheses, none of which can be statistically rejected:

**(H1) Gamma(L) is constant.** The null hypothesis. Mean Gamma = constant fits the data essentially as well as a power law (the improvement in R^2 from adding the exponent parameter is negligible).

**(H2) Gamma(L) grows logarithmically.** Gamma(L) = Gamma_0 + c log(L). An equally good fit (R^2 also ~0.3) but with the opposite physical implication: archiving becomes *more* efficient at larger scales.

**(H3) Gamma(L) has a non-monotonic structure.** Gamma(L) could increase up to some L_c and then decrease, reflecting a competition between two physical mechanisms. With R^2 = 0.298 and no reported residuals analysis, non-monotonic behavior cannot be excluded.

**(H4) Gamma(L) undergoes a phase transition.** At some L > 100 (beyond the simulated range), Gamma(L) could jump discontinuously, vanish, or diverge. The data provide zero constraint on this possibility.

**(H5) Gamma(L) oscillates.** Gamma(L) = Gamma_0 + A sin(omega log L). With sparse sampling in L, an oscillatory signal would appear as scatter around a weak trend -- exactly what R^2 = 0.298 describes.

The manuscript selects (H1) -- "Gamma is approximately constant" -- and builds the entire physical interpretation on it: "classical behavior emerges because Gamma dominates while D vanishes." But the data do not select (H1) over (H2)-(H5). This is not inference; it is cherry-picking the interpretation that fits the desired narrative.

### 2.3 The Physical Stakes of Gamma(L)

The claim that Gamma is scale-independent is load-bearing for the manuscript's physical picture. If D decays as L^{-2.58} while Gamma remains constant, then at sufficiently large L, Gamma dominates the q-field dynamics and D becomes negligible. This is the mechanism by which "quantum diffusion is suppressed and classical behavior emerges."

But if Gamma(L) actually grows, decays, oscillates, or undergoes a transition, the entire "classical emergence" narrative collapses. If Gamma(L) also decays (even weakly), then at cosmological scales both D and Gamma might be suppressed, leaving no mechanism for classical behavior. If Gamma(L) grows, then the archiving instability might run away at large scales, producing a qualitatively different macroscopic theory.

The manuscript stakes a cosmological conclusion on a fit with R^2 = 0.298. This is not a minor statistical weakness -- it is a fatal evidentiary gap at the exact point where the argument requires certainty.

---

## ATTACK 3: d_eff -> 2.5-3 Is Oscillation, Not Convergence

### 3.1 The Missing N-Scaling Sequence

The manuscript states that d_eff flows to 2.5-3 under spectral RG but does not provide the N-scaling sequence for the RG-transformed graphs. The prior spectral analysis (Referee #4's review) provided explicit data for cubic lattice d_eff(N):

| N | d_eff | Delta from 3.00 |
|---|-------|-----------------|
| 125 | 3.447 | +0.447 |
| 343 | 3.887 | +0.887 |
| 1000 | 3.371 | +0.371 |
| 1728 | 3.192 | +0.192 |
| 3375 | 3.092 | +0.092 |

This sequence is **non-monotonic**: 3.447 -> 3.887 -> 3.371 -> 3.192 -> 3.092. The value at N=343 overshoots the claimed asymptotic value by 29.6%. A sequence that goes up, then down, from five data points, does not constitute evidence for convergence to any specific value.

The manuscript's spectral RG claim introduces an additional layer: now d_eff is claimed to flow under RG, not just be measured at fixed N. This means the quantity being reported is d_eff(N, L) -- a function of both the graph size N and the RG scale L. To claim "d_eff -> 2.5-3," the authors must demonstrate that the double limit:

$$\lim_{L \to \infty} \lim_{N \to \infty} d_{\text{eff}}(N, L)$$

exists and equals some value in [2.5, 3]. This requires:
1. Taking N -> infinity at fixed L to eliminate finite-size effects
2. Then taking L -> infinity to find the infrared fixed point

The manuscript performs neither limit. It reports d_eff at some finite N and finite L, observes that the value is "between 2.5 and 3," and declares convergence. This is not a scaling analysis -- it is looking at a number and rounding it.

### 3.2 The "2.5-3" Range Is Too Wide to Be Meaningful

The claimed attractor range "d_eff -> 2.5-3" spans a factor of 1.2 in the effective dimension. The difference between d_eff = 2.5 and d_eff = 3.0 is physically enormous:

- d_eff = 2.5: The spectral heat kernel decays as K(t) ~ t^{-1.25}, return probability P_0(t) ~ t^{-1.25}
- d_eff = 3.0: K(t) ~ t^{-1.5}, P_0(t) ~ t^{-1.5}
- The difference in long-time return probability at t = 10^6: factor of 10^{0.25 * 6} = 10^{1.5} ~ 31.6

A factor of 30 in a measurable observable cannot be hand-waved as "approximately 3." If the RG flow truly converges to d=3, the uncertainty should shrink with increasing L and N. If the uncertainty remains large (2.5-3), the RG flow has not converged -- it is still in a crossover regime, and the true fixed point could be anywhere in or outside that interval.

### 3.3 Finite-Size Oscillations in Spectral Dimension

Spectral dimensions extracted from finite graphs are known to exhibit oscillatory finite-size corrections. For a cubic lattice of linear size L, the integrated density of states N(lambda) contains oscillatory terms from the discrete nature of the spectrum:

$$N(\lambda) = \frac{V}{6\pi^2} \lambda^{3/2} + \frac{S}{16\pi} \lambda + \text{(oscillatory terms)}$$

where V = L^3 is the volume and S = 6L^2 is the surface area. The oscillatory terms produce an *apparent* d_eff that oscillates around 3 as a function of the fitting window, with amplitude that decays only as 1/L. For L=15 (N=3375), the oscillation amplitude in d_eff is non-negligible (~0.1-0.3). The non-monotonic behavior in the cubic lattice data (3.447 -> 3.887 -> 3.371) is precisely what one expects from these spectral oscillations -- it is not a signal of "flow toward 3," it is a finite-size artifact.

The manuscript's spectral RG analysis piles an additional layer of coarse-graining on top of graphs that *already* exhibit finite-size spectral oscillations. The RG transformation changes the graph's size and connectivity, which changes the oscillation pattern. The resulting "flow" of d_eff may simply be tracing the finite-size oscillation pattern of a sequence of differently-sized graphs -- not a genuine RG flow toward a fixed point.

### 3.4 The Required Analysis (Not Performed)

To establish that d_eff flows to 3 under spectral RG, the manuscript would need to provide:

1. d_eff(N, L) for at least 5 values of N spanning at least one order of magnitude, and at least 10 values of L spanning the accessible scale range.
2. A finite-size scaling ansatz: d_eff(N, L) = d_infinity + A * N^{-alpha} * f(L/N^{1/d}) + ...
3. Extrapolation to N -> infinity at fixed L/N^{1/d}, demonstrating that the finite-size corrections vanish.
4. The L -> infinity limit of the N -> infinity result, with a confidence interval that does not include values below 2.8 or above 3.2.
5. Demonstration that the result is stable under changes in the coarse-graining scheme, the fitting window for the Weyl law, and the eigenvalue weighting.

None of this is provided. The claim "d_eff -> 2.5-3" is a qualitative impression formed by looking at numbers that happen to fall in the right ballpark.

---

## ATTACK 4: Does the Power Law D(L) ~ L^{-2.58} Persist?

### 4.1 The Finite-Size Saturation Bound

Even granting the reported fit D(L) ~ L^{-2.58} (R^2 = 0.972) over the simulated range, there is a fundamental bound on how far this power law can extend: the graph's finite size.

On any finite graph of diameter d_G, the diffusion coefficient D(L) measured by an RG blocking procedure must saturate when the block size L approaches d_G. At L ~ d_G, each coarse-grained block contains the entire graph, and further coarse-graining does not change the effective dynamics. D(L) cannot decay below the value set by the smallest non-zero Laplacian eigenvalue lambda_2:

$$D_{\text{min}} \sim \lambda_2 \cdot d_G^2$$

For a 3D cubic lattice of N vertices, lambda_2 ~ 1/N^{2/3} and d_G ~ N^{1/3}, giving D_min ~ N^{-1/3}. For N ~ 10^6, D_min ~ 10^{-2} in units of the microscopic D. This means D(L) can decay by at most ~2 orders of magnitude before saturating -- not 157.

To sustain the L^{-2.58} decay over 61 decades in L, the graph would need to be large enough that its diameter exceeds 10^61 microscopic units. That requires N > (10^61)^3 = 10^{183} vertices. No numerical simulation can approach this. The claim that D decays by 10^{157} is not a numerical result -- it is the assumption that the power law continues far beyond the scale where finite-size effects necessarily terminate it.

### 4.2 The Physical Graph vs. The Mathematical Extrapolation

The manuscript's physical picture is that the DGF information graph of the universe contains ~10^{180} vertices (one per Planck volume in the Hubble volume). At this N, the graph's diameter is indeed ~10^60 Planck lengths, and the spectral RG *would* be able to probe L up to 10^60 -- if one could simulate it.

But one cannot simulate it. The simulation -- whatever its actual N -- is smaller than the physical graph by a factor of ~10^{174} in vertex count. The finite-size saturation that limits the simulated power law to ~2 decades of L occurs at L ~ 100 in the simulation but at L ~ 10^60 in the physical graph. The extrapolation from L=100 to L=10^60 assumes that the physics at L=10^60 is the same as the physics at L=100, just with a smaller D.

This assumption is precisely what is at issue. The whole point of RG is that qualitatively new physics can emerge at each scale. The fact that D(L) decays as L^{-2.58} at L=1-100 tells us about the **ultraviolet** RG flow near the lattice scale. It tells us nothing about the **infrared** RG flow at cosmological scales, where qualitatively new fixed points, crossovers, and emergent operators may dominate.

### 4.3 The Spectral Dimension Drift Under RG: A Warning Sign

The manuscript reports that d_eff flows from some UV value toward 2.5-3 under RG. This means the effective dimension *changes* under coarse-graining. But D(L) ~ L^{-2.58} is a power law whose exponent depends on the spectral dimension: for a graph with spectral dimension d_s, the diffusion coefficient on scale L typically scales as:

$$D(L) \sim L^{2 - d_w}$$

where d_w is the walk dimension (d_w = 2 for normal diffusion, >2 for anomalous diffusion). The spectral dimension relates to d_w via d_s = 2 d_f / d_w, where d_f is the fractal dimension.

If d_eff (the spectral dimension) *changes* under RG flow, then the exponent in D(L) should *also* change -- power laws with constant exponents are characteristic of scale-invariant fixed points, not of RG flows between fixed points. A genuine RG flow should produce a running exponent D(L) ~ L^{-gamma(L)} with gamma(L) evolving from its UV value to its IR value. The manuscript's report of a constant exponent -2.58 alongside a flowing d_eff is internally inconsistent: either the system is at a fixed point (constant exponents, constant d_eff) or it is flowing (changing exponents, changing d_eff). It cannot be both.

---

## ATTACK 5: This Is Still Part 1 -- Not Part 2

### 5.1 The Logical Structure of the Two Parts

Wall #3 has two logically distinct sub-problems, which the DGF community refers to as Part 1 and Part 2:

**Part 1 (Discrete-to-Continuum):** Given a DGF information graph that is *already known to be effectively 3-dimensional*, does the discrete q-field dynamics converge to a continuous field equation in the limit of large N?

**Part 2 (Derivation of d=3):** Do the DGF axioms (causal graph, capacity bound, overflow irreversibility, archive accumulation) *imply* that the information graph must be effectively 3-dimensional? That is, is d=3 an *output* of the axioms, not an *input* to the graph construction?

Part 1 is a problem of analysis: given a 3D graph, prove that the continuum limit exists. Part 2 is a problem of derivation: prove that the axioms force the graph to be 3D.

### 5.2 What Spectral RG Actually Shows

A spectral RG analysis takes a graph as input, performs coarse-graining, and measures how spectral quantities flow with scale. The conclusions it can draw are of the form:

> "For *this graph* (the one we simulated), the effective dimension under RG flows to approximately 3."

The italicized qualifier is everything. The spectral RG has nothing to say about graphs it did not simulate. If the simulated graph was constructed to be 3D (cubic lattice, random geometric graph in R^3, etc.), then the spectral RG is measuring the dimension that was baked into the construction. The result "d_eff -> 2.5-3" is not a derivation of d=3 from the axioms -- it is a consistency check confirming that the spectral RG algorithm correctly identifies the dimension of graphs known to be 3D.

The manuscript conflates two fundamentally different statements:

**(A)** "When we run spectral RG on 3D graphs, d_eff flows to ~3." (Consistency check -- true, and unsurprising.)

**(B)** "DGF axioms imply that the information graph is 3D." (Part 2 -- the claim that needs to be proved.)

Statement (A) does not imply (B). To get from (A) to (B), one would need to additionally prove:

> **(C)** "Any graph satisfying the DGF axioms, when evolved under the DGF dynamics from generic initial conditions, produces a graph whose spectral RG flow has d_eff -> 3."

Statement (C) is a claim about *all* DGF graphs, not just the ones the authors chose to simulate. The manuscript provides zero evidence for (C). It simulates graphs that are 3D by construction, measures their dimension, and reports that the measurement returns ~3. This is a validation of the measurement apparatus, not a derivation of the measured quantity.

### 5.3 The RG Attractor Argument Is Circular

The manuscript's key conceptual move is to reframe "d=3" as an "RG attractor" rather than an "axiom-derived necessity." The argument is:

1. Run spectral RG on some DGF-like graphs.
2. Observe d_eff -> 2.5-3.
3. Conclude: d=3 is an RG attractor.
4. Therefore, we don't need to derive d=3 from the axioms -- any graph near d=3 will flow to d=3 under RG.

But step 1 embeds the conclusion. The graphs were *chosen* to be near d=3 (they are 3D lattices or random geometric graphs in R^3). The spectral RG then reports that their effective dimension is near 3. The "attractor" claim is just the observation that if you start near 3, you stay near 3.

What if we started with a graph whose UV dimension is 5? Or 2? Or a graph that is not a manifold at any scale? Would the RG flow carry it to d ~ 3? The manuscript provides no evidence. Without exploring the basin of attraction -- without demonstrating that a wide range of initial graph structures flow to d ~ 3 under the DGF dynamics + spectral RG -- the claim that "d=3 is an attractor" is vacuous. It is the statement that 3 is near 3.

### 5.4 The Part 2 Requirement, Restated

Part 2 demands a proof of the following form:

> **Theorem (Part 2, required):** Let G be an information graph satisfying DGF Axioms 1-4. Let the graph evolve under the DGF dynamical equations. Then, in the limit of large N and under appropriate coarse-graining, the effective spectral dimension of G converges to 3.

Or, more modestly (if one accepts that Part 2 might only yield d=3 with high probability):

> **Theorem (Part 2, statistical version):** Let G be an information graph satisfying DGF Axioms 1-4, with random initial conditions drawn from a specified ensemble. Then, with probability approaching 1 as N -> infinity, the effective spectral dimension under coarse-graining converges to 3.

Neither theorem has been proved. The spectral RG data do not constitute a proof of either theorem. They constitute a measurement of a specific graph's dimension -- a measurement whose outcome was determined by the choice of which graph to measure.

### 5.5 The Bait-and-Switch

The manuscript's title and abstract claim to have broken both Part 1 and Part 2. The body of the manuscript provides evidence for:

- **Part 1 (strengthened):** The spectral convergence theorem (von Luxburg / Garcia Trillos) guarantees that 3D geometric graphs have a well-defined continuum limit. The spectral RG data show that this limit is stable under RG flow -- if you start with a 3D graph, coarse-graining preserves the 3D character. This is a genuine (though modest) contribution: it strengthens the Part 1 result by showing RG stability.

- **Part 2 (unaddressed):** Nothing in the manuscript addresses why the DGF axioms *imply* 3D. The spectral RG flow shows that if the graph is 3D, it stays 3D -- a stability result, not a derivation. The "RG attractor" framing cannot substitute for a derivation because the basin of attraction is unexplored. The entire Part 2 claim rests on a confusion between "3 is a fixed point of the RG flow for 3D graphs" and "the DGF axioms force graphs to be 3D."

The bait: "Spectral RG breaks both Part 1 and Part 2." The switch: Part 1 gets strengthened (RG stability of the known 3D continuum limit), while Part 2 gets nothing -- the "derivation" is a consistency check on graphs that were 3D all along.

---

## THE FATAL BLOW: Synthesis of the Five Attacks

### The Argument, Laid Bare in Its Full Inadequacy

The manuscript's argument reduces to the following chain of inference:

1. **The data:** A spectral RG simulation (provenance undocumented) on an unspecified graph (probably 3D by construction) over ~2 orders of magnitude in L (probably L=1 to L=100).

2. **The power law:** D(L) ~ L^{-2.58} with R^2 = 0.972 over this range. Gamma(L) ~ L^{-0.12} with R^2 = 0.298 over this range. d_eff somewhere between 2.5 and 3.

3. **The extrapolation:** Extend D(L) ~ L^{-2.58} over 59 additional orders of magnitude to L=10^61. Conclude D decays by 10^{157}. Extend Gamma(L) ~ constant (ignoring R^2 = 0.298) over the same range. Conclude Gamma dominates at macroscopic scales.

4. **The physical picture:** "Quantum diffusion is suppressed; classical archiving emerges; gravity is the residue of archiving."

5. **The Wall #3 claims:** "Part 1 is broken because RG flow guarantees the continuum limit. Part 2 is broken because d=3 is an RG attractor, not an assumption."

Each step in this chain is defective:

- **Step 1:** The data provenance is absent. We don't know the graph, the coarse-graining scheme, the definitions of observables, or the range of N and L. Without this, the numbers D(L), Gamma(L), d_eff are free-floating quantities without operational meaning.

- **Step 2:** The Gamma(L) fit has R^2 = 0.298 -- statistically insignificant. The claim "Gamma is constant" is not supported by the data. The d_eff range 2.5-3 is too wide to claim convergence, and no N -> infinity extrapolation has been performed.

- **Step 3:** Extrapolating a two-decade power law over 59 additional decades is scientifically indefensible. Known RG phenomena (crossovers, finite-size saturation, emergent operators) guarantee that the power law *must* break down at some L between 100 and 10^61. The manuscript provides no estimate of where this breakdown occurs and no evidence that it occurs at L > 10^61 specifically.

- **Step 4:** The physical picture depends on Gamma being constant at all scales (R^2 = 0.298), D continuing to decay without saturation (despite finite graph size), and d_eff converging to exactly the right range to produce 3D classical behavior. Each of these dependencies is individually unsupported; their conjunction is fantasy.

- **Step 5:** Even if Steps 1-4 were valid, the argument would only strengthen Part 1 (RG stability of the 3D continuum limit). Part 2 (axioms -> d=3) is untouched -- the spectral RG measures the dimension of a graph that was given to it; it does not derive the dimension from the axioms.

### The Core Conceptual Error: Extrapolation Masquerading as Derivation

The manuscript's deepest error is epistemological. It treats a numerical fit over a limited range as though it were a law of nature valid over all scales. The power law D(L) ~ L^{-2.58} is a **description** of the behavior of one simulation over two decades. It is not a **derivation** of the behavior of the DGF universe over 61 decades. The gap between "this simulation shows D(L) ~ L^{-2.58} for L=1..100" and "D(L) ~ L^{-2.58} for L=1..10^{61}" is not a gap that can be closed by more precise simulations -- it is a gap that can only be closed by an analytic understanding of the RG flow, including all relevant operators, all fixed points, and all crossover scales.

The manuscript provides no such analytic understanding. It provides a curve fit and an act of faith.

### Comparison with Established RG Practice

In condensed matter physics, claiming a new critical exponent based on numerical RG requires:

- At least 3-4 decades of scaling in the relevant variable
- Finite-size scaling analysis with at least 5-10 system sizes
- Extrapolation to the thermodynamic limit with controlled error bars
- Demonstration of scaling collapse (data from different system sizes collapsing onto a single scaling function)
- Consistency check with known exact results (sum rules, hyperscaling relations)
- Stability analysis under changes in the coarse-graining scheme

The manuscript satisfies **zero** of these criteria. It provides 2 decades of scaling (criterion: 3-4), no finite-size scaling (criterion: 5-10 sizes), no thermodynamic limit extrapolation, no scaling collapse, no consistency checks with exact results, and no scheme-stability analysis. By the standards of the RG community, this is not a numerical RG study -- it is a preliminary exploration whose results are too preliminary to support any physical conclusion, let alone one about the dimensionality of spacetime.

### The 10^{157} Number: A Case Study in Spurious Precision

The number 10^{157} appears in the manuscript as the factor by which D decays at cosmological scales. This number is obtained by:

$$D(10^{61})/D(1) = (10^{61})^{-2.58} = 10^{-157.38} \approx 10^{-157}$$

The exponent 157.38 comes from multiplying 61 by 2.58. The factor 2.58 comes from a fit to data spanning 2 decades. The factor 61 comes from the ratio of the Hubble radius to the Planck length.

The number 10^{157} therefore has **zero significant digits**. The exponent 2.58 has an uncertainty -- unquantified, but conservatively at least +/- 0.2 given the fitting range and the absence of systematic error analysis. The factor 61 is a physical input, but the extrapolation over 59 decades beyond the data means the effective uncertainty on the extrapolated exponent is not +/- 0.2 but **unbounded** -- the true large-L behavior could have an entirely different functional form.

To report 10^{157} as a physical prediction, with three significant digits implied by the "157," is spurious precision of the highest order. It is the numerical equivalent of claiming to measure the distance to a galaxy using a ruler calibrated in your backyard.

---

## ADDITIONAL TECHNICAL CONCERNS

### A. The Coarse-Graining Scheme Is Not Specified

"Spectral RG" is a non-standard term. In the RG literature, spectral methods for RG include:

- **Eigenvalue truncation RG:** Diagonalize the Laplacian, discard eigenvectors with eigenvalues above a cutoff, project dynamics onto the remaining subspace. This is essentially momentum-shell RG in the spectral domain.

- **Diffusion map RG:** Use the diffusion distance d_t(x,y) at time t as the coarse-grained distance metric. As t increases, the effective graph coarsens. This is related to the spectral embedding.

- **Real-space blocking with spectral observables:** Perform standard Kadanoff blocking in real space, then use spectral quantities (D, Gamma, d_eff) as observables measured on the blocked graph.

Each scheme has different convergence properties, different systematic errors, and different finite-size artifacts. The manuscript does not specify which scheme was used. Without this, the results cannot be reproduced, and the reported exponents cannot be interpreted -- an exponent measured in one scheme generally differs from the same exponent measured in another.

### B. The Definition of Gamma(L) Under RG

The archiving rate Gamma(q) is defined in the microscopic DGF theory as a local function of the q-field. Under coarse-graining, the effective Gamma(L) is a *different object* from the microscopic Gamma. It is the result of integrating out short-wavelength q-field fluctuations, which can renormalize Gamma in both magnitude and functional form.

The manuscript reports Gamma(L) ~ L^{-0.12} as though this were a measurement of how the microscopic Gamma evolves under RG. But what is actually being measured? Is it:

- The effective archiving rate of the coarse-grained q-field equation, obtained by fitting the coarse-grained dynamics?
- The spectral proxy for Gamma, extracted from the coarse-grained Laplacian spectrum via some assumed relation?
- Something else?

Without specifying the operational definition of Gamma(L), the reported exponent -0.12 has no physical meaning.

### C. The Diffusion Coefficient D(L) in a Non-Translation-Invariant Graph

The diffusion coefficient D is well-defined for translation-invariant systems (where it is proportional to the conductivity via the Einstein relation). On a general graph -- especially a disordered or dynamically generated DGF graph -- the diffusion coefficient is not a single number but a tensorial quantity that can vary in space. The spectral RG presumably measures some spatially averaged D(L). But averaging can hide spatial heterogeneity that is physically crucial: if D is highly inhomogeneous, with some regions having D ~ L^{-2.58} and others having D ~ constant, the average would reflect neither region's actual physics.

The manuscript should demonstrate that the DGF graphs under study are sufficiently homogeneous for a single D(L) to be meaningful. If they are not -- and DGF graphs with causal shielding and capacity bounds seem unlikely to be homogeneous -- then D(L) ~ L^{-2.58} is fitting a homogeneous model to an inhomogeneous system, producing a meaningless average exponent.

### D. No Comparison with Null Models

A spectral RG analysis of a random graph with no particular spatial structure will also produce some D(L), some Gamma(L), and some d_eff(L). The manuscript should compare its DGF results to null models:

- Erdos-Renyi random graphs (no spatial structure)
- Configuration model graphs with matched degree distributions
- Random geometric graphs in d=2, 4, 5 (to test whether the "attractor" is specific to d=3)
- Graphs generated by random matrix ensembles

Without null models, we cannot assess whether the reported scaling behavior is specific to DGF graphs or is a generic feature of any sufficiently connected random graph subjected to spectral RG.

---

## SYNTHESIS AND VERDICT

### The Weight of the Evidence

I have examined the manuscript's claims under the assumption that the numerical computations were performed competently. Even with this charitable assumption, the argument fails at five independent points:

1. **Data provenance:** The graph, coarse-graining scheme, observable definitions, and simulation parameters are undocumented. The reported numbers are untethered from any reproducible procedure.

2. **Statistical insignificance of Gamma(L):** R^2 = 0.298 does not support the claim that Gamma is scale-independent. The central physical mechanism -- "Gamma dominates at large scales" -- rests on a fit that explains 30% of the variance.

3. **No convergence analysis for d_eff:** The claim d_eff -> 2.5-3 is based on visual inspection of a number in the right ballpark. No finite-size scaling, no N -> infinity extrapolation, no confidence intervals. The reported range "2.5-3" is too wide to distinguish a genuine attractor from a slow crossover.

4. **Unjustified extrapolation:** Two decades of L are extrapolated over 59 additional decades to reach cosmological scales. This is not a conservative extrapolation; it is not even an aggressive extrapolation; it is an extrapolation so extreme that it ceases to be science and becomes pure speculation. Finite-size saturation, crossover to new fixed points, and emergence of new relevant operators are all *guaranteed* to occur at some intermediate scale -- the manuscript provides no analysis of where or how.

5. **Category error on Part 2:** The spectral RG measures the dimension of a given graph. It does not derive the dimension from the DGF axioms. The "RG attractor" argument is circular: it assumes graphs near d=3 to conclude that graphs flow to d=3. Part 2 (axioms -> d=3) remains completely unaddressed.

### The Pattern Across Wall #3 Submissions

I note, as Referee #4 did, that this is one of multiple Wall #3 submissions from the same group using different methods (RG invariance of archive information, universality enumeration, spectral dimension detection, and now spectral RG flow). Across these submissions, a consistent pattern emerges:

- A mathematical or computational tool is developed that can detect, measure, or preserve 3D structure.
- The tool is applied to graphs that are 3D by construction.
- The tool reports 3D (or something close to 3D).
- The authors claim the tool has "broken Wall #3."

In each case, the tool is a detector, not a derivation engine. It measures what was given; it does not derive what the axioms imply. The current manuscript adds a new layer -- extrapolation over 59 orders of magnitude -- but the underlying error is the same: confusing a measurement performed on a chosen graph with a derivation from the axioms.

### What Would Actually Be Required

To make a credible claim of breaking Wall #3 Part 2 using spectral RG, the authors would need to provide:

1. **Proof that the DGF axioms constrain the UV dimension.** Without assuming d=3, what does the DGF dynamics imply about the graph's spectral properties at the Planck scale? Are there bounds on the UV spectral dimension from the axioms alone?

2. **Demonstration that the RG flow is universal.** Show that a wide class of graphs -- with varying UV dimensions, varying connectivities, varying boundary conditions -- all flow to the same IR fixed point under the same spectral RG scheme. The basin of attraction must be shown to include the graphs actually generated by DGF dynamics.

3. **Analytic control of the IR fixed point.** A numerical power law with an unquantified uncertainty is not a fixed point. Derive (or at minimum, provide numerical evidence for) the critical exponents of the IR fixed point, with error bars, from finite-size scaling.

4. **Proof that the IR fixed point corresponds to 3D general relativity.** Showing that d_eff ~ 3 does not prove that the effective theory is GR. One must derive the effective action for the q-field at the IR fixed point and show that it reduces to the Einstein-Hilbert action (or equivalent) in the appropriate limit.

None of these requirements are met. The manuscript provides a power-law fit to a few data points from an unspecified simulation, extrapolates it across 59 orders of magnitude, and declares the problem solved. This is not physics. It is curve-fitting with cosmological pretensions.

### Final Recommendation

**Reject.** The manuscript's central claim -- that spectral RG flow has broken both Part 1 and Part 2 of Wall #3 -- is unsupported by the evidence presented. The argument depends on:
- A statistically insignificant fit for Gamma(L) (R^2 = 0.298)
- An extrapolation of 59 orders of magnitude beyond the data
- A convergence claim for d_eff that has not been subjected to finite-size scaling
- A category error that confuses measurement with derivation

These defects are not remediable by additional data within the same framework. The problem is not that the simulation was too small or the fits too noisy -- the problem is that no numerical simulation of this type, regardless of its precision, can address the logical structure of Wall #3 Part 2. Part 2 requires a derivation from axioms; the spectral RG provides measurements of chosen graphs. No number of measurements, no matter how precise, can substitute for a derivation.

The manuscript should be rejected. The authors are encouraged to clearly distinguish between Part 1 (where spectral RG provides genuine, if incremental, insight into the stability of the 3D continuum limit) and Part 2 (which requires a completely different type of argument -- an analytic derivation from the DGF axioms, not a numerical measurement of a graph whose dimension was chosen by hand).

---

*The reviewer is a specialist in renormalization group methods and numerical statistical physics, with 20 years of experience in finite-size scaling analysis of critical phenomena. This review reflects an independent assessment of the manuscript's physical, statistical, and logical content.*

*Confidential note to the editor: This manuscript continues a pattern I have observed across multiple Wall #3 submissions from this group. The common thread is the deployment of a dimension-sensitive tool (spectral analysis, RG flow, universality enumeration) on graphs that are 3D by construction, followed by the claim that the tool has "derived" d=3 from the axioms. Each manuscript dresses this circular logic in different mathematical clothing. I recommend that the editors consider a consolidated response addressing the shared logical structure, rather than engaging each manuscript on its specific technical details -- the technical details change, but the circularity does not.*

---

*Anonymous Referee #5, Nature Physics*
*Review submitted: 2026-06-12*
