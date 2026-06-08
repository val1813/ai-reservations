# REVIEWER H — Astrophysicist + Gravitational Wave Experimentalist: The "No Hard Event Horizon" Prediction

**Role:** Astrophysicist specializing in black hole physics, gravitational wave data analysis (LIGO/Virgo), and EHT observations
**Date:** 2026-06-06
**Paper:** LP31 v3, "Information Capacity and the Structure of Physical Law"
**Focus:** Section V.D — "Black holes: no sharp event horizon" and all associated observational claims
**Question:** Is the "no hard event horizon" prediction a real physical prediction, or a decorative claim dressed in the language of astrophysics?

---

## Executive Summary

The v3 paper's headline falsifiable prediction — "black holes lack a sharp event horizon" — is constructed through a sequence of five steps, of which **four are unsupported**. The prediction has no rigorous theoretical foundation, and in the one model where it can be made quantitative (the refractive index model n=1/q), it is already excluded by EHT M87* measurements at approximately 7σ. The prediction is decorative: it reads like a genuine astrophysical claim to an editor scanning for falsifiability, but disintegrates under the scrutiny that an actual astrophysicist would apply.

---

## Attack 1: Parabolic Equations Cannot Describe Gravitational Waves — Ringdown Predictions Are Unfounded

### The claim

The v3 paper states (Section VII, "Experimental Contact"):

> "Gravitational wave ringdown: The quasi-normal mode spectrum of a DGF 'black hole' differs from GR because no sharp boundary condition exists at r_s."

The supporting strong-field analysis (strong_field_black_hole.md, Section 3.1) goes further, estimating that DGF QNM frequencies could differ from GR by a factor of ~3, and that ringdown decay times may be longer due to the absence of an absorbing boundary.

### The problem

The v3 paper itself classifies this as a **FATAL** gap:

> "GAP-SF-1: The parabolic equation cannot describe gravitational waves... ∂_t q = κq∇²(ln q) is a diffusion equation — the propagation speed of initial perturbations is mathematically infinite."

This is not a minor technical gap. It is a **category error**. A diffusion equation describes the spread of a conserved quantity via random walks; a wave equation describes the propagation of oscillatory disturbances at finite speed. These are different mathematical objects with different solution spaces, different boundary conditions, and different observational signatures. You cannot extract a ringdown spectrum — which is defined by the eigenvalues of a wave operator with specific boundary conditions — from a diffusion equation.

### Why the paper's approach is illegitimate

The paper's strategy is:

1. Solve the **static** limit of the parabolic equation: ∇²(ln q) = 0 → q(r) = e^{-GM/rc²}.
2. Note that this static solution has no sharp boundary at r_s.
3. **Extrapolate** from this static property to a claim about **dynamical** ringdown.

This extrapolation is mathematically invalid. The ringdown spectrum depends on:
- The form of the **dynamical** wave operator (hyperbolic, not parabolic)
- The **boundary conditions** at the compact object surface
- The shape of the **effective potential** for wave scattering

None of these can be inferred from the static solution of a different equation class. The static solution tells you the equilibrium q(r) profile. It tells you nothing about how that profile responds to time-dependent perturbations, because the equation governing those perturbations (whatever it is) is not the equation that produced the profile.

### The "telegrapher equation" escape

The supporting material proposes a hyperbolic extension:

> ∂_t²q + γ ∂_t q − c_s² q ∇²(ln q) = 0 (telegrapher-type)

with the note: "the static limit (∂_t² → 0, ∂_t → 0) recovers the solution of Section 1."

This is hand-waving. The telegrapher equation is a specific hyperbolic generalization of the diffusion equation, but:
- There is no derivation of this specific form from DGF principles. Why this form rather than, say, ∂_t²q − c_s²∇²q + V'(q) = 0?
- The parameter c_s (signal propagation speed) is an entirely new free parameter with no DGF-internal determination.
- The damping term γ is another free parameter.
- Even if one accepts this form, the ringdown spectrum depends on c_s, γ, and the boundary conditions — none of which are constrained by the static solution.

The static limit matching is necessary but wildly insufficient. Every hyperbolic equation that contains a Laplacian term has a static limit that reduces to the Laplace equation. The ringdown spectrum is determined by the **hyperbolic part** — the very part that is unspecified.

### Honest pre-judgment of rebuttal

The authors will say: "We already acknowledge this is a fatal gap. The ringdown predictions are presented as qualitative targets."

**Response:** A "qualitative target" that is acknowledged to have no theoretical foundation is not a prediction — it is a wish. The paper's abstract and Section VII present "black holes lack a sharp event horizon" as the framework's **falsifiable prediction**. If the mathematical machinery to connect this claim to any actual observable does not exist, the claim is not falsifiable. It is unfalsifiable in practice and unfounded in theory.

**Verdict:** The ringdown prediction is decorative. It borrows the authority of gravitational wave astronomy without being answerable to gravitational wave data.

---

## Attack 2: No Metric → No Geodesics → No Photon Orbits — The Shadow Prediction Is Ornamental

### The claim

The v3 paper states (Section VII):

> "Event Horizon Telescope: The photon orbit in a q-field background differs from GR at small r. The shadow size is predicted to be smaller than the GR value of ~5.2 GM/c², approaching ~2.7 GM/c² in a refractive-index model."

The supporting material (Section 3.2) develops this into a detailed calculation involving a "refractive index model" n(r) = 1/q(r) = e^{GM/rc²}, a "photon sphere" at r_ph = GM/c², and a shadow radius of approximately 2.718 GM/c².

### The problem: This is not DGF. This is geometric optics grafted onto DGF.

General relativity predicts a specific shadow size because it has:
1. A **metric** g_μν that defines causal structure.
2. **Geodesic equations** that govern photon trajectories: d²x^μ/dλ² + Γ^μ_αβ (dx^α/dλ)(dx^β/dλ) = 0.
3. An **event horizon** that absorbs all photons with impact parameter below the critical value.

DGF has none of these. It has a scalar field q(r) with no geometric interpretation. There are no geodesics. There is no definition of what a "photon orbit" means. There is no equation for how light propagates in a q-field background.

### The refractive index model: Derivation or invention?

The supporting material introduces n(r) = 1/q(r) and states:

> "In DGF, the q-field influences light propagation in the form of a refractive index."

Where does this come from? The paper provides no derivation. There is no Lagrangian coupling between the electromagnetic field and the q-field. There is no effective metric construction. There is no argument from first principles.

Let me enumerate the possible justifications for n = 1/q, and why none work:

1. **Analogy with dielectric media**: In a medium with refractive index n, the optical path length is ∫ n ds. But this analogy requires a background metric to define "ds." DGF has no metric.

2. **Conformal rescaling**: If the effective metric is g_μν^eff = q^{-2} η_μν, then null geodesics satisfy ds_eff = 0 → q^{-1}|dx| = c dt, which gives an effective refractive index n = 1/q. But this assumes a conformal coupling that the paper never derives or justifies. And it immediately creates problems: a conformal metric gives g_00 = q^{-2} and g_rr = q^{-2}, which produces a different PPN γ parameter and different light deflection than the n = 1/q refractive index model used in the ray-tracing calculation.

3. **Fermat's principle analogy**: In a static spacetime with g_00 = -f(r) and g_rr = 1/f(r), the coordinate speed of light is c·f(r), equivalent to a refractive index n = 1/f(r). But DGF has no f(r) — it has no metric at all.

4. **Phenomenological guess**: The simplest way to make light "slow down" near massive objects. But simplicity is not derivation.

### The photon sphere calculation is circular

The supporting material derives the "DGF photon sphere" from:

> d/dr [r n(r)] = 0 → r_ph^DGF = GM/c²

This calculation assumes:
1. That the Bouguer formula r·n(r)·sin θ = b is valid (it assumes spherical symmetry and a refractive index model).
2. That the photon sphere condition d/dr[r n(r)] = 0 is meaningful (it comes from the effective potential in a refractive medium, which itself assumes a background Euclidean geometry that DGF does not provide).

These are assumptions from **geometric optics in flat space with a variable refractive index**. They are not derivable from DGF's fundamental equations (A1-A3, the flux theorem, and the continuum q-field equation). They are imported from an entirely different physical framework and decorated with DGF notation.

### What would be required for a real prediction

To make a genuine EHT shadow prediction, DGF would need at minimum:
1. **An effective metric** derived from the q-field: g_μν[q]. Without this, "photon" and "orbit" are undefined.
2. **A field equation for light** in this effective geometry: a Maxwell-like or eikonal equation.
3. **A definition of the shadow boundary**: the set of directions on the observer's sky for which photons are absorbed/trapped. In GR, this is defined by the event horizon. In DGF, there is no event horizon, so what defines the "shadow"?

None of these exist. The paper substitutes them with an ad hoc refractive index model, performs a calculation in that model, and presents the result as "the DGF prediction."

### Honest pre-judgment of rebuttal

The authors will say: "The refractive index model is a first attempt at phenomenological contact. We acknowledge that the coupling between the q-field and light propagation is an open problem (GAP-SF-3)."

**Response:** An "open problem" is something you don't yet know how to solve. It is not a license to insert an unsupported model, compute a number, and call it a prediction. If the coupling between q and light is unknown, then DGF makes **no prediction** about EHT shadows. Presenting "~2.72 GM/c²" as the DGF shadow size — with no derivation of the optical model that produced it — is not "phenomenological contact." It is dressing an unsupported number in the language of EHT measurements to create the appearance of empirical content.

**Verdict: This is the most fatal attack in this review. The shadow prediction is decorative in the strictest sense: it serves an aesthetic function (making the paper look testable) without any theoretical foundation. A quantity computed in an ad hoc model imported from a different theory does not become a prediction of your theory.**

---

## Attack 3: q(r) = e^{-GM/rc²} → q(r_s) ≈ 0.607 — What Does "No Hard Horizon" Physically Mean?

### The claim

The v3 paper states that q(r) > 0 for all r > 0, the approach to q = 0 is asymptotic as r → 0, and "information is never strictly trapped."

### The physical picture is undefined

Let me trace what DGF says happens to matter falling onto a compact object:

1. An infalling particle approaches r = r_s = 2GM/c². In GR, this is the point of no return. In DGF, q(r_s) ≈ 0.607 — nothing special happens. The particle continues inward.

2. The particle reaches r = GM/c², where q ≈ 0.368. Still nothing special.

3. The particle approaches r → 0. q → 0. The effective diffusivity D(q) = κ/q → ∞. The information flux diverges toward r = 0.

4. At r → 0, q → 0 but never reaches exactly zero. The particle's information is compressed into an arbitrarily small radial region with arbitrarily high information density.

**What is the physical state of matter in this regime?**

DGF provides no answer. The theory describes the q-field — the vacant capacity fraction — but not the state of the matter that occupies that capacity. The paper's foundational ontology is clear: the universe is N cells, each 0 or 1, and q is the fraction of zeros. But what does q → 0 mean for the physical object that fell in?

Three possibilities, none of which are addressed:

**(a) Soft singularity**: As r → 0, the matter density diverges (all cells occupied in vanishing volume), creating a singularity that is "softer" than GR's curvature singularity but still singular in density. This would mean DGF replaces GR's geometric singularity with an information-density singularity — trading one singularity for another.

**(b) Asymptotic compression without singularity**: Matter is compressed to arbitrarily high but finite density as r → 0, with q → 0 asymptotically. No singularity forms, but the matter exists in a state of arbitrarily high information density that is never "trapped" in the GR sense. This raises the question: what prevents indefinite compression? GR has no stable endpoint for collapse without an event horizon — that's the point of the singularity theorems.

**(c) The matter is not "at" r → 0**: In DGF's discrete picture, there is a minimum length scale (cell scale). At r below the cell scale, the continuum description breaks down (acknowledged as GAP-SF-7). The matter's information is distributed across a finite number of cells at r ≈ 0, with q ≈ 0 meaning "almost all occupied." But this means the theory has nothing to say about the interior of a "black hole" at the most fundamental level.

### The "information is never trapped" claim

The paper claims that because q > 0 for all r > 0, "information is never strictly trapped." But what does this mean operationally?

If I drop an encyclopedia into a DGF "black hole," can I ever recover its contents? The S1 reflux bound says the probability of information reflux is P_reflux ≤ exp(-N_S), where N_S is the number of cells in the central region. For a macroscopic object, N_S ~ number of Planck-area cells on the surface ~ (M/m_P)² ~ 10^76 for a solar mass.

P_reflux ≤ exp(-10^76). This is not "never strictly zero" in any physically meaningful sense. The probability is smaller than the probability that every particle in the observable universe quantum-tunnels to Andromeda simultaneously. It is smaller than the inverse of the number of possible quantum states of the observable universe.

**"Not strictly zero" is a mathematical distinction, not a physical one.** In physics, we distinguish possible from impossible by whether something can occur within the age and size of the observable universe. By that criterion, DGF information reflux is impossible — identically as impossible as information escape from a GR black hole.

### The "no hard horizon" slogan

The phrase "no hard event horizon" is rhetorically powerful: it suggests a radical revision of the black hole concept that is simultaneously testable. But when unpacked, it means:
- There is no surface where q = 0 at finite r (true).
- q decays smoothly from q(r_s) ≈ 0.607 to q → 0 as r → 0 (true).
- Information reflux is "non-zero in principle" (true, at the level of e^{-10^76}).
- This constitutes a resolution of the information paradox (claimed by the paper).

The first two are mathematical properties of the solution q(r) = e^{-GM/rc²}. The third is a statement about the S1 bound. The fourth — the claim that this resolves the information paradox — is an interpretive leap that does not follow from the first three.

### Honest pre-judgment of rebuttal

The authors will say: "The 'no hard horizon' claim is about the mathematical structure of the solution, not about observability. The distinction between 'strictly zero' and 'exponentially suppressed' is fundamental to the question of unitarity."

**Response:** This is a debate about what "resolve" means. If DGF claims to resolve the information paradox, it must show that information is recoverable — not just "not strictly destroyed." The S1 bound says recovery probability is exp(-10^76). That is destruction for all practical purposes, and the practical is what the information paradox is about: Hawking's original calculation showed that information appears to be destroyed by any measurement that a finite observer could perform. DGF reproduces this practical impossibility while asserting that it has solved the problem because the impossibility is "only" statistical rather than causal. This is not a resolution — it is relabeling the problem.

**Verdict:** The "no hard event horizon" claim is physically underdetermined. The paper never specifies what happens to matter at small r, what the interior state of a DGF "black hole" is, or how the claimed resolution of the information paradox translates into any operational difference from GR. The slogan is more powerful than its content.

---

## Attack 4: Have Existing LIGO/Virgo Ringdown Measurements Already Excluded DGF?

### The claim

The paper suggests that DGF ringdown differs from GR and that "current LIGO/Virgo ringdown measurements are consistent with GR but have not ruled out soft-boundary alternatives."

### The quantitative situation

The supporting material estimates that DGF QNM frequencies could differ from GR by a factor of ~3 (based on the photon sphere radius shifting from 3GM/c² to GM/c²). The supporting material then acknowledges:

> "A 3× difference is too large — if it existed, LIGO/Virgo would have already ruled it out. This means the possible DGF frequency shift is much smaller than 3× (requiring a more precise effective potential form), or DGF gravitational waves require a completely different wave equation."

This is a remarkable admission: the one quantitative estimate that can be made within the existing framework is **already excluded**. The response is not to abandon the prediction but to assert that the estimate must be wrong, without providing a correct one.

### The experimental reality

LIGO/Virgo has measured ringdown frequencies and damping times for multiple binary black hole mergers. The most precise measurement comes from GW150914:

- **Ringdown frequency**: f_220 ≈ 253 Hz for the (2,2,0) mode
- **Damping time**: τ_220 ≈ 4.0 ms
- **GR prediction**: f_220 = 253 ± 2 Hz, τ_220 = 3.9 ± 0.2 ms (for M_final ≈ 62 M_⊙, a_final ≈ 0.68)

The agreement is at the few-percent level. More recent events with higher SNR (GW190521, GW200129) provide even tighter constraints. The dominant QNM frequency has been confirmed to agree with GR at the ~5-10% level across multiple events spanning a range of masses and spins.

### What would it take for DGF to survive?

For DGF to be consistent with LIGO/Virgo data, its ringdown predictions must agree with GR at the ~10% level or better for the observed mass range. Since DGF currently has no hyperbolic field equation, no ringdown calculation exists to compare. The paper's claim that "current measurements have not ruled out soft-boundary alternatives" is true only in the vacuous sense that no specific soft-boundary prediction exists to be ruled out.

But this cuts both ways: if DGF cannot make a specific ringdown prediction, it cannot claim ringdown as an observational test of the theory. You cannot simultaneously claim (a) our theory differs from GR in ringdown, and (b) current measurements don't rule us out, when you cannot compute what your theory predicts for ringdown.

### Non-linear memory and higher harmonics

Gravitational wave observations also test:
- **Non-linear memory**: the permanent displacement after the wave passes. GR predicts a specific memory amplitude; DGF would need to match this.
- **Higher harmonics**: modes beyond (2,2) have been detected in GW190412 and GW190814. These constrain the multipolar structure of the source.

DGF has nothing to say about any of these because they all require a wave equation.

### Honest pre-judgment of rebuttal

The authors will say: "We are not claiming our current equation makes ringdown predictions. We are identifying ringdown as a future observational target once the hyperbolic extension is developed."

**Response:** Then the paper should not say "current LIGO/Virgo ringdown measurements have not ruled out soft-boundary alternatives." This phrasing implies that there exists a soft-boundary alternative that could have been ruled out but wasn't. There isn't one. The statement is true only because there is nothing to test — not because the test was performed and passed.

**Verdict:** DGF cannot survive contact with LIGO/Virgo data not because it disagrees with the data, but because it cannot engage with the data at all. This is not a successful confrontation with experiment; it is immunity from experiment.

---

## Attack 5: The Information Paradox — "Resolved" by Exp(10^-76)?

### The claim

The v3 paper claims that because q > 0 for all r > 0, "information is never strictly lost → unitarity is automatically preserved." The supporting material (Section 4) develops this into a full discussion of how DGF "resolves" the information paradox.

### The structure of the "resolution"

The DGF resolution of the information paradox has three steps:

1. **GR's problem**: Information that falls into a black hole is causally disconnected from the exterior. Hawking radiation is thermal and carries no information about the infallen state. This violates quantum unitarity.

2. **DGF's answer**: There is no event horizon. q > 0 everywhere. Information is never causally disconnected. The S1 reflux bound gives a non-zero probability for information to return: P_reflux ∝ exp(-N_S).

3. **Conclusion**: Unitarity is preserved because the underlying dynamics f: X → X is a permutation (bijective on a finite set).

### Why this doesn't resolve anything

The information paradox is not a paradox about the **metaphysical possibility** of information recovery. It is a paradox about the **physical mechanism** of information recovery. Hawking's calculation shows that, under the assumptions of semiclassical gravity, the outgoing radiation is exactly thermal. The question is: how does the information get encoded in the radiation?

DGF's answer — "the probability is non-zero" — is not an answer to this question. It is an answer to a different question: "Is information recovery logically impossible?" To which DGF answers "no," based on the finite-state nature of the underlying dynamics.

But this was never the issue. No one claimed information recovery is logically impossible. The claim is that it is incompatible with semiclassical gravity as currently formulated. DGF does not propose an alternative mechanism for Hawking radiation, does not compute the entanglement entropy of the radiation, and does not derive a Page curve. It simply notes that since the fundamental dynamics is a permutation, unitarity is automatic.

**This is not a resolution — it is a refusal to engage with the problem at the level where it exists.**

### The scale of the "non-zero" probability

Let me make the numbers concrete. For a solar-mass black hole:

- Number of Planck-area cells on the horizon: N_S ≈ (M/m_P)² ≈ (2×10^30 / 2.2×10^{-8})² ≈ 10^76
- Reflux probability: P_reflux ≤ exp(-10^76)

The age of the universe is ~10^17 seconds. The number of particles in the observable universe is ~10^80. The number of possible quantum states of the observable universe is ~exp(10^122).

exp(-10^76) is smaller than any of these by an incomprehensible margin. It is "non-zero" in the same sense that the probability of a macroscopic object quantum-tunneling through a wall is non-zero — a statement that is mathematically true and physically meaningless.

### The philosophical dodge

The supporting material acknowledges this tension (Section 4.6):

> "Operationalists: P ~ e^{-10^38} is experimentally indistinguishable from P = 0 → DGF adds no new testable content."
> "Principlists: P > 0 is fundamentally different from P = 0 → DGF preserves quantum mechanical unitarity."

This is presented as a matter of "philosophical stance." It is not. It is a matter of what "resolve" means. If by "resolve" you mean "point out that the underlying mathematics does not strictly forbid information recovery," then DGF resolves the paradox. But so does the observation that GR is probably not the final theory of quantum gravity — a statement that requires no new framework at all.

If by "resolve" you mean "provide a mechanism by which information actually returns to the exterior in time for an observer to recover it," then DGF does nothing, because the probability of reflux is indistinguishable from zero for any macroscopic black hole.

### Comparison with actual resolutions

Contrast DGF's approach with actual attempts to resolve the information paradox:

- **String theory/fuzzball proposal**: Replaces the black hole interior with a specific quantum microstructure from which information can emerge via Hawking radiation. Provides concrete calculations of microstate counting that reproduces the Bekenstein-Hawking entropy.
- **ER=EPR**: Proposes that entanglement is geometrically realized as wormholes, providing a mechanism for information transfer.
- **Island formula/replica wormholes**: Computes the Page curve from Euclidean path integrals, showing explicitly how information emerges from the radiation at the Page time.

All of these make specific, calculable claims about how information escapes. DGF makes none. Its "resolution" consists of noting that the underlying state space is finite and the dynamics is bijective — which is true of the discrete model but has no computational contact with the actual physics of black hole evaporation.

### Honest pre-judgment of rebuttal

The authors will say: "DGF changes the question from 'how does information escape a causal trap' to 'how fast does information diffuse out of a high-density region.' This is a genuine reconceptualization."

**Response:** A reconceptualization that changes the question without answering either the old question or the new one is not progress. If the new question is "how fast does information diffuse out," DGF must compute a diffusion timescale, compare it to the evaporation timescale, and show that information escapes before the black hole evaporates. It does none of this. The S1 bound gives an upper limit, not a rate. Without a rate, there is no way to determine whether information escapes in time — and therefore no way to determine whether unitarity is actually preserved in any operationally meaningful sense.

**Verdict:** The information paradox "resolution" is the weakest claim in the paper. It takes the most profound problem in theoretical physics and "solves" it by declaring that exp(-10^76) ≠ 0. This is not physics — it is a mathematical triviality dressed as a deep insight.

---

## Attack 6: Quantitative Confrontation with EHT M87* — DGF Is Already Excluded

### The measurement

The Event Horizon Telescope measured the shadow of M87*:

- **Shadow angular diameter**: θ_shadow = 42 ± 3 μas (microarcseconds)
- **Mass**: M = 6.5 ± 0.7 × 10^9 M_⊙ (from stellar dynamics, independent of GR)
- **Distance**: D = 16.8 ± 0.8 Mpc

From these, GR predicts a shadow diameter:

θ_GR = 2 × √27 × GM / (c² D)

Plugging in the numbers:

- GM/c² = 6.67×10^{-11} × 6.5×10^9 × 2×10^30 / (9×10^16) ≈ 9.63×10^12 m
- D = 16.8×10^6 × 3.086×10^16 ≈ 5.18×10^23 m
- Angular radius: √27 × 9.63×10^12 / 5.18×10^23 ≈ 5.196 × 1.86×10^{-11} ≈ 9.66×10^{-11} rad
- In μas: 9.66×10^{-11} × 2.063×10^8 ≈ 19.9 μas → diameter ≈ 39.9 μas

GR prediction: ~40 μas. EHT measurement: 42 ± 3 μas. Agreement at < 1σ.

### The DGF prediction (refractive index model)

Using the refractive index model n(r) = 1/q(r) = e^{GM/rc²}:

- Critical impact parameter: b_c = e × GM/c² ≈ 2.718 × 9.63×10^12 ≈ 2.62×10^13 m
- Angular shadow radius: b_c / D = 2.62×10^13 / 5.18×10^23 ≈ 5.05×10^{-11} rad
- In μas: 5.05×10^{-11} × 2.063×10^8 ≈ 10.4 μas
- Shadow diameter: ~20.8 μas

### The discrepancy

| Source | Shadow diameter (μas) |
|--------|----------------------|
| EHT measurement | 42 ± 3 |
| GR prediction | ~40 |
| DGF (refractive index model) | ~21 |

The DGF prediction is 21 μas versus the measured 42 ± 3 μas. This is a **7σ discrepancy**.

Even if we allow generous systematic uncertainties — mass uncertainty (±10%), distance uncertainty (±5%), and theoretical uncertainty in the shadow diameter (±20% for the ad hoc model) — the DGF prediction cannot be stretched beyond ~30 μas. It remains excluded at > 4σ.

### What about Sgr A*?

The EHT also observed Sgr A* (2022). The Sgr A* shadow is consistent with GR at similar precision. While the Sgr A* mass is known more precisely from stellar orbits (GRAVITY collaboration), the shadow measurement has larger relative uncertainties due to the source's variability. Even so, the consistency with GR further constrains any deviation.

### Possible escapes — and why they don't work

**Escape 1: "The refractive index model is wrong."**

This is almost certainly true — the refractive index model is ad hoc. But if it's wrong, you cannot replace it with nothing. You need a different model that:
- Is derived from DGF principles (not imported from geometric optics)
- Predicts a shadow diameter consistent with 42 ± 3 μas
- Does not introduce fine-tuning

No such model exists. The paper's supporting material lists five possible coupling schemes (refractive index, conformal metric, Brans-Dicke, Finsler geometry, no coupling) and notes that they give "completely different observational predictions." If the prediction depends entirely on which ad hoc coupling you choose, then DGF makes no prediction at all — the prediction belongs to the coupling, not to DGF.

**Escape 2: "Rotation enlarges the shadow."**

M87* is rotating. A Kerr black hole's shadow is slightly asymmetric and its size depends on spin and inclination. For prograde orbits at high spin, the shadow can appear slightly larger. But:
- The GR Kerr shadow is at most ~5% different from Schwarzschild in size (the asymmetry is in shape).
- To grow a 21 μas shadow to 42 μas would require a spin-dependent enlargement of factor ~2, which is impossible in any reasonable spacetime geometry.
- Even extremal Kerr (a = 1) has a shadow radius that differs from Schwarzschild by only ~4% for equatorial viewing.

**Escape 3: "The shadow is not b_c — full ray-tracing is needed."**

The supporting material acknowledges this (Section 3.2.3). But full ray-tracing in the refractive index model would give a shadow radius that depends on the detailed bending of light rays, which in turn depends on n(r). For n(r) increasing toward r = 0 (as in DGF), light rays are bent **more** strongly, which generally makes the shadow **smaller**, not larger. It is extremely unlikely that full ray-tracing would increase the shadow diameter from 21 μas to 42 μas — this would require the shadow to be dominated by rays that loop around the center many times and emerge, which (a) are geometrically suppressed and (b) would produce a fuzzy, not sharp, shadow boundary.

**Escape 4: "The EHT measurement doesn't directly measure the shadow — it measures the photon ring, which depends on the accretion flow."**

This is a real systematic. The EHT image shows a ring of emission surrounding a central brightness depression. The ring diameter is not exactly the shadow diameter — it depends on the emission region in the accretion flow. However:
- GRMHD simulations show that for a wide range of accretion models (SANE, MAD, varying R_high), the ring diameter is within ~5% of the shadow diameter.
- To produce a 42 μas ring from a 21 μas shadow would require the emission to peak at ~3× the shadow radius, which is inconsistent with all known accretion physics (the emission peaks near the photon sphere, which in any geometry is comparable to the shadow boundary).

### Honest pre-judgment of rebuttal

The authors will say: "We never claimed the refractive index model is the final word. The shadow prediction is a target for future development, not a claim that DGF has already been tested."

**Response:** Section VII of the v3 paper says: "Current EHT measurements of M87* and Sgr A* constrain but do not exclude such deviations." This is false. The only model in which DGF makes a quantitative shadow prediction is excluded by EHT at 7σ. A theory that "constrains but does not exclude" a deviation must have a specific prediction that falls within the error bars, or at least a parameter range that does. DGF has neither — the one model that produces a number produces the wrong number, and all other models produce no number at all.

**Verdict: In the only model where the shadow prediction is quantitative, DGF is already excluded by EHT M87* at 7σ. The paper's claim that EHT "constrains but does not exclude" DGF is incorrect. EITHER DGF makes no shadow prediction (because the coupling is unknown), OR it makes the refractive-index-model prediction, which is excluded. The paper cannot have it both ways.**

---

## Synthesis: The Decoration Problem

### What "decorative" means in this context

A "decorative prediction" is a statement that:
1. Sounds like a testable empirical claim when read by a non-specialist.
2. Lacks the theoretical machinery required to connect it to actual observables.
3. Would require additional assumptions (not derived from the theory) to make it quantitative.
4. When made quantitative under the simplest assumptions, is already excluded by existing data.
5. Serves primarily to make the paper appear empirically grounded rather than to actually confront data.

The "no hard event horizon" prediction satisfies all five criteria.

### The architecture of the decoration

The paper constructs the appearance of astrophysical contact through a sequence of rhetorical moves:

1. **State the static solution**: q(r) = e^{-GM/rc²} (mathematically rigorous within the framework).
2. **Note a structural difference from GR**: q(r_s) ≈ 0.607 > 0, while GR has g_00(r_s) = 0 (correct observation).
3. **Label this difference as a "prediction"**: "black holes lack a sharp event horizon" (rhetorical elevation of a mathematical property to an empirical claim).
4. **Name observational domains**: "gravitational wave ringdown" and "Event Horizon Telescope" (borrowing the authority of established experiments).
5. **Suggest deviations exist without quantifying them**: "Current measurements... have not ruled out soft-boundary alternatives" (unfalsifiable claim because the alternative is unspecified).
6. **Acknowledge gaps in caveats**: "These signatures require a hyperbolic extension" (protecting against criticism while preserving the appearance of empirical content).

Each step individually is defensible. The combination produces a paper that appears to make contact with astrophysical observations while being immune to astrophysical refutation.

### The asymmetry of evasion

A genuine prediction can be wrong. If DGF made a specific prediction for the ringdown frequency of a 62 M_⊙ black hole, LIGO could test it. If DGF made a specific prediction for the M87* shadow diameter, EHT could test it.

The paper's strategy prevents this. By saying:
- "The current equation doesn't apply to ringdown" → ringdown cannot test DGF.
- "The coupling between q and light is unknown" → EHT cannot test DGF.
- "The numbers are qualitative targets" → no specific number can be wrong.

This creates a structural asymmetry: DGF can claim to differ from GR in these domains without being answerable to the data from these domains. This is not science — it is science-flavored storytelling.

### What an honest paper would say

An honest version of the v3 paper's experimental contact section would read:

> "The framework currently makes no contact with gravitational wave or EHT observations. The field equation is parabolic and cannot describe propagating waves. The coupling between the q-field and electromagnetic radiation is unknown. Until both gaps are closed — which requires a hyperbolic extension of the field equation and a derivation of the q-photon coupling from first principles — the framework's claims about black holes are mathematical properties of the static solution, not empirical predictions. We present these properties as motivation for future theoretical development, not as tests of the framework."

The fact that the paper instead presents these as "observational signatures" and "experimental contact" — with numbers like "~2.72 GM/c²" that appear precise but are derived from an unsupported model — is the decoration.

### What would rescue the prediction?

For the "no hard event horizon" prediction to be genuine, DGF would need:

1. **A hyperbolic field equation** derived from DGF principles (not postulated ad hoc), with:
   - Finite propagation speed (must equal c in the appropriate limit)
   - Well-posed initial value formulation
   - Reduction to the parabolic q-field equation in the static limit

2. **An effective metric** g_μν[q] that couples the q-field to matter and radiation, with:
   - Derivation from DGF's discrete dynamics (not assumed from GR)
   - Correct Newtonian limit
   - Deflection of light consistent with solar system tests (γ_PPN = 1 to 10^{-5})

3. **Specific numerical predictions** for at least one observable:
   - Ringdown QNM frequency for a given mass and spin
   - Shadow diameter for M87* given its independently measured mass and distance
   - Orbital dynamics (ISCO, epicyclic frequencies) testable with X-ray timing

None of these exist. Until they do, "black holes lack a sharp event horizon" is not a prediction. It is a slogan.

---

## Final Verdict

| Attack | Severity | Verdict |
|--------|----------|---------|
| A1: Parabolic equation → no ringdown | FATAL (self-acknowledged) | Ringdown claim has no theoretical foundation. The paper admits this but draws conclusions anyway. |
| A2: No metric → no photon orbits | **FATAL (most devastating)** | The shadow prediction of ~2.72 GM/c² is computed in an ad hoc model with zero derivation from DGF. It is the definition of a decorative prediction. |
| A3: What does q(r_s) ≈ 0.607 mean? | SEVERE | The physical picture of "no hard horizon" is underdetermined. The interior state of a DGF black hole is unspecified. |
| A4: Already excluded by LIGO/Virgo? | SEVERE | The one quantitative estimate (3× frequency shift) is self-admittedly excluded. DGF cannot engage with ringdown data. |
| A5: Information paradox "resolved"? | SEVERE | Replacing "causally impossible" with "probability exp(-10^76)" is not a resolution — it is relabeling. |
| A6: Already excluded by EHT M87* at 7σ? | **FATAL** | In the only quantitative model, DGF is excluded. The paper's claim that EHT "constrains but does not exclude" is false. |

### Bottom line

The "no hard event horizon" prediction is decorative. It is the weakest part of an otherwise internally coherent framework, and it weakens the paper by creating the appearance of empirical contact where none exists. The authors should either:

**(a) Remove the black hole section entirely**, restricting the paper to its genuine contributions (the q-field equation, the universality class, the static Newtonian correspondence), or

**(b) Develop the hyperbolic extension and q-photon coupling to the point where specific, falsifiable predictions can be made**, and then present those predictions honestly, including the fact that the simplest model is already excluded by EHT.

Option (a) is the honest choice given the current state of the theory. A paper that derives the Laplace equation from information principles and shows Newtonian correspondence is already ambitious. It does not need decorative black hole predictions to be interesting.

---

*Reviewer H is an astrophysicist specializing in black hole accretion physics and gravitational wave data analysis. She has been a member of the LIGO Scientific Collaboration since 2015 and the EHT Collaboration since 2017. Her review reflects the standards of observational astrophysics: a prediction that cannot be confronted with data — or that is already excluded by data — is not a prediction.*
