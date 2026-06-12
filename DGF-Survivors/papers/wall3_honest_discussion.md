# Wall #3: The Discrete-to-Continuum Limit -- An Honest Discussion

**Target:** PRD long paper, Discussion section
**Word count:** ~1050
**Status:** Draft for integration into main manuscript

---

## VIII. The Discrete-to-Continuum Gap

### A. What We Have and What We Lack

The Decoherence Geometry Framework (DGF) is defined on a discrete causal graph at the Planck scale. Each vertex carries at most O(1) bits of information; each edge encodes a Cartan-parameterized unitary coupling; the local purity field q(x) quantifies the fraction of coherent quantum channels available at a lattice site. The framework yields five rigorous theorems in the discrete setting: the projection angle theorem (T1), time unidirectionality (T2), the Causal-Fold sufficiency condition (T3), the reflux bound (T4), and the black-hole entropy area-law scaling (T5). These results are exact on the graph.

All macroscopic claims of DGF -- Newtonian gravity, post-Newtonian corrections, cosmological effective equations of state, information-horizon thermodynamics -- require something the framework does not yet possess: a rigorously established continuum limit q(x) of the discrete purity field. This is Wall #3, and it is currently unbroken.

The gap is quantitative. The graph is defined at the Planck scale, l ~ 10^{-35} m. Macroscopic phenomena -- atomic physics, fluid dynamics, gravitational lensing, cosmic expansion -- operate at scales separated by a factor of 10^{61} in length, or equivalently 10^{183} in three-dimensional cell count. Establishing that the discrete dynamics flows to a smooth, universal continuum effective theory across this chasm is a renormalization-group problem of extreme severity. Our numerical RG attempts (LP40) on graphs of N ~ 10^3 nodes produced statistically insignificant results; the INSPECTOR audit [R2] identified two fatal flaws in subsequent RG code (manual insertion of exp(-M/r) as an initial condition, and manual calibration of the coupling lambda to match G), confirming that no genuine RG derivation of the continuum limit has been achieved. The present status is honest: the Poisson form of the q-field equation is made plausible by arguments from graph locality and linear b1-scaling, but it is not derived.

### B. What Could Go Wrong

There are at least four ways the continuum limit could fail to produce the smooth, GR-compatible effective theory that DGF's macroscopic phenomenology assumes.

First, a **phase transition** in the causal graph. As the blocking scale increases, the effective connectivity of the graph -- encoded in the first Betti number b1, which counts independent causal cycles -- could undergo a discontinuous jump rather than a smooth flow. If the graph at some intermediate scale transitions between a dense small-world phase (where causal cycles percolate) and a sparse phase (where they are isolated), the effective q-field would develop a non-analyticity that no differential equation could capture. The negative spectral dimensions (d_s = -6.78, -11.99) observed in our RG simulations, while likely a numerical artifact of small graphs, are consistent with the kind of pathology a genuine phase transition would produce.

Second, **emergent symmetry breaking**. The discrete graph has only the symmetries of the lattice. The continuum q-field theory posited in DGF -- a scalar field on a smooth manifold satisfying a Poisson equation -- has full diffeomorphism invariance in the effective metric sector. The emergence of diffeomorphism invariance from a discrete lattice is not a small step; it is the hardest problem in quantum gravity. Causal set theory [Sorkin, 1987] has worked on precisely this problem for four decades without a complete solution. DGF shares the same structural challenge, with the additional complication that the graph carries not just causal order but also information-theoretic degrees of freedom (q, Cartan parameters) whose continuum fate is unknown.

Third, **dimensional reduction or enhancement**. The spectral dimension of the causal graph need not equal the embedding dimension (d=3) at all scales. In causal dynamical triangulations [Ambjorn et al., 2005], the spectral dimension flows from d_s ~ 4 at large scales to d_s ~ 2 at the Planck scale. If DGF's causal graph undergoes a similar dimensional flow, the effective continuum theory would not be a 3+1 dimensional q-field on a smooth manifold, but something more exotic -- a scale-dependent dimension that only asymptotically approaches d=3. Our RG code's unstable spectral dimension measurements prevent us from ruling this out.

Fourth, **non-universality of the IR fixed point**. Even if a continuum limit exists, it may not be unique. Different microscopic graph ensembles (different initial Cartan parameter distributions, different edge-connection rules, different boundary conditions) could flow to different IR effective theories. If this is the case, matching DGF to GR would require fine-tuning the microscopic ensemble, not just extracting universal IR coefficients. The framework would then be a classification of possible low-energy gravities rather than a unique derivation of Einstein gravity.

### C. Scale Gaps in Other Domains of Physics

The 10^{61} gap is severe, but it is not unprecedented. Physics has successfully bridged larger relative gaps in other contexts, and the strategies employed there are instructive for DGF.

**Quantum Chromodynamics (QCD):** The gap between the quark-gluon plasma at ~10^{-16} m and hadronic physics at ~10^{-15} m is only ~10^1 in length, but the coupling runs from asymptotic freedom (alpha_s << 1) to confinement (alpha_s ~ 1), a non-perturbative transition spanning an infinite relative coupling range. QCD bridges this gap with lattice gauge theory: discretize the continuum action on a finite lattice, compute observables via Monte Carlo, and take the continuum limit a -> 0 while tuning the bare coupling to hold physical masses fixed. The strategy works because (a) the microscopic action (QCD Lagrangian) is known exactly, (b) the RG flow is asymptotically free and computable in perturbation theory at high energies, and (c) the lattice formulation preserves the exact gauge symmetry at finite spacing. DGF has none of these advantages: the microscopic action (the graph Hamiltonian governing q-evolution) is not known in closed form, there is no asymptotic freedom to anchor the UV, and the relevant symmetry (diffeomorphism invariance) is not manifest on the lattice.

**Statistical mechanics:** The gap between atomic scales (~10^{-10} m) and macroscopic hydrodynamic scales (~1 m) is ~10^{10} in length. The bridge is the Boltzmann equation and its hydrodynamic limit, established rigorously for large classes of microscopic dynamics via the Chapman-Enskog expansion and, in the modern era, via fluctuation theorems and macroscopic fluctuation theory. The key insight is universality: the hydrodynamic equations (Navier-Stokes, diffusion) depend only on a handful of transport coefficients, not on the microscopic details. If DGF's continuum limit is universal in this sense -- if the effective q-field equation depends only on a few RG-irrelevant microscopic parameters -- then the 10^{61} gap is bridgeable in principle. The challenge is that we do not know the microscopic dynamics of the causal graph well enough to even begin a Chapman-Enskog expansion.

**The cosmological constant problem** itself is a 10^{122} gap between the zero-point energy predicted by quantum field theory and the observed dark energy density. DGF's 10^{61} length-scale gap is numerically smaller but structurally analogous: both involve a microscopic quantity whose naive extrapolation to macroscopic scales fails by a factor that is exponential in the number of degrees of freedom. The difference is that the cosmological constant problem is a known failure mode of an otherwise successful theory (QFT + GR), while DGF's scale gap is a failure to establish the theory itself.

The honest lesson from these comparisons is that scale gaps can be bridged when (i) the microscopic theory is precisely specified, (ii) there is a controlled expansion parameter at one end of the RG flow, and (iii) universality guarantees that the IR physics depends on few parameters. DGF currently satisfies none of these conditions for the causal graph-to-q-field bridge.

### D. Conditional Status of Macroscopic Claims

In light of the above, all macroscopic claims of DGF must carry an explicit conditional prefix. We propose the following tiered qualifier system:

**Tier I -- Graph-Rigorous:** Results that are exact theorems on the discrete causal graph, requiring no continuum limit. These include T1-T5, the CFOL sufficiency condition, the QCMI scaling law (theta^2 ln(1/theta)), the pointer-basis identification (Wall #5), and the global decoherence formula D = 1 - [cos^2(4c)]^{b1}. These results are unconditional and falsifiable on present-day quantum hardware; IBM Q measurements confirm the CFOL prediction at up to 144 sigma.

**Tier II -- Continuum-Conditional:** Results that assume a well-defined continuum limit q(x) exists and that the effective q-field equation takes the Poisson form derived from graph-locality arguments. These include the Newtonian force law (via calibration of the coupling to G), the 2PN bound-energy deviation of 4.06%, the effective dark energy equation of state w_eff(z), and the information-horizon thermodynamic relations. Every Tier II claim should be prefaced with: "If the discrete-to-continuum RG flow of the causal graph converges to a local scalar field theory, then..."

**Tier III -- Heuristic:** Results that depend on additional assumptions beyond the continuum limit -- in particular, the identification of proper time with local purity (d tau/dt = q), the mapping between b1 density and mass density, and any cosmological prediction extending beyond the linear regime. These should be explicitly labeled as "heuristic" or "exploratory" and accompanied by a clear statement of the unverified assumptions.

We emphasize that the Tier II results are not worthless. The fact that a single calibration (matching the q-field coupling to Newton's constant G) yields non-trivial, testable predictions at 2PN order and in cosmology is a non-trivial consistency check. Theories with the wrong structure do not survive this test: an arbitrary scalar-tensor theory calibrated to Newtonian gravity generically fails at the first post-Newtonian correction. That DGF's q-field ansatz survives to 2PN is evidence that the structure -- if the continuum limit exists -- is not arbitrary. But evidence is not proof, and the conditional status must not be obscured.

### E. Path Forward

Bridging Wall #3 requires a computational and conceptual program that we outline here not as accomplished work but as a roadmap:

1. **Graph size:** RG blocking studies require graphs of at least N ~ 10^5 nodes to yield 5-6 statistically meaningful blocking levels. This is feasible with sparse-graph algorithms on a single GPU.

2. **Topology-preserving blocking:** The RG step must preserve causal connectivity across block boundaries, not merely rebuild a new spatial graph. The internal/external b1 decomposition identified in our preliminary analysis is the correct conceptual framework; it needs algorithmic implementation.

3. **Microscopic dynamics:** The graph must evolve under DGF's own rules -- Cartan-parameterized edge unitaries, local decoherence driven by internal b1, entanglement diffusion across block boundaries -- without manual insertion of the exp(-M/r) form. Only if the steady-state q(x) spontaneously approximates this form can the continuum limit be claimed.

4. **Universality checks:** The same RG flow must be run on multiple graph ensembles (different initial topologies, different Cartan distributions, 2D and 3D embeddings) to test whether the IR fixed point is universal.

Until this program is completed, Wall #3 stands. We have chosen to publish the discrete theorems (Tier I) and the continuum-conditional phenomenology (Tier II) together because the former provides the microscopic foundation that makes the latter more than empty parameter-fitting, and the latter provides the empirical motivation that makes the former more than abstract quantum information theory. But we ask the reader to hold the Tier II claims at the appropriate confidence level: not as derived results, but as conditional predictions whose derivation status is explicitly tracked.

---

**Integration note for main.tex:** This section (VIII) should appear after the cosmological results and before the concluding summary. Cross-reference the CFOL theorems from S1 as the unconditional Tier-I anchor. The tiered qualifier system should be applied retroactively to the gravity (Section V), post-Newtonian (Section VI), and cosmological (Section VII) sections of the main manuscript.
