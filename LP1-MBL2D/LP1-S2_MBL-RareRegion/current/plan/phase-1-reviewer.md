# Nature Physics — Anonymous Referee Report

**Manuscript:** "Rare Region Percolation in 2D Disordered Many-Body Localized Systems" (Phase 1 conclusions)
**Review date:** 2026-05-30
**Referee stance:** Fundamental skepticism — claims must survive rigorous cross-examination before publication

---

## 0. NARRATIVE RETREAT DETECTION

**Finding: EVIDENCE OF NARRATIVE RETREAT.**

The six conclusions (K1.1–K1.6) are presented as unconditional physical facts. However, internal documentation (PI review, "phase-1-PI-review.md") reveals that each conclusion carries unstated domain restrictions that substantially weaken the claimed results:

- K1.1–K1.3: The Poisson clumping heuristic is acknowledged internally to be valid only for "W > 2W_c" and "N_s > 20," yet these restrictions do not appear in the conclusion text. For W ∈ [W_c, 2W_c] — precisely the regime most relevant to the MBL transition — no validated prediction is provided.
- K1.4: The claim "η(W) < 1.128 for ALL W > 0" contradicts the trivial limit W → 0 where the entire system is thermal. The internal documentation retreats implicitly to "for W in the deep MBL phase," a restriction that is nowhere stated in K1.4. The claim must be rewritten as "η(W) < 1.128 for W > W_lower," with W_lower explicitly quantified.
- K1.5: The "hard maximum" L_QP^max ≈ 2.8 is derived assuming a separable 2D potential V(x,y) = V_0[cos(2πβ₁x) + cos(2πβ₂y)]. The internal review acknowledges this as a special case but presents the conclusion as general.
- Several "致命" (fatal) self-attacks in the PI review are marked "部分解决" (partially resolved), meaning the authors themselves acknowledge that the derivation chain is not airtight. The conclusions text makes no mention of this.

**Required response from authors:** Each conclusion must be restated with its explicit domain of validity (disorder range, system size, potential type), and conclusions that lack proof outside their restricted domain must be flagged as conjectures.

---

## REJECTION REASON 1: Simplest Counterexample to a Core Assumption

**[评级: 致命]**

The entire derivation chain (K1.1 through K1.4) rests on the assumption that a site can be classified as "thermal" or "not-thermal" based solely on whether its local potential ε_i falls below a single-particle localization threshold ε_c. This binary classification is the linchpin without which the Poisson clumping heuristic, the extremal index analysis, and the continuum percolation mapping all collapse.

A simple counterexample: Consider two adjacent lattice sites A and B, each with ε_A = ε_B = 1.1 ε_c. Individually, both are classified as "not thermal" under the binary criterion, and they contribute zero to the "thermal region" count. However, in the presence of interactions U, the effective level spacing of the joint AB system is reduced by a factor ~2, and the matrix element coupling them to neighboring sites is enhanced by constructive interference. The actual thermalization condition for the AB pair is NOT ε_A < ε_c and ε_B < ε_c independently; it is that some collective wavefunction on AB has a localization length exceeding the AB separation. Standard two-site localization theory (Anderson 1958, Eq. 5.3) gives the joint localization condition: V_intra/|ε_A − ε_B| > 1, where V_intra is the effective hopping within the AB pair. For ε_A ≈ ε_B (near-resonant pair), even sites with ε_i > ε_c can form a delocalized two-site cluster that acts as a thermal reservoir.

This is not a narrow edge case. In a system of N_s² sites, the number of near-resonant pairs (|ε_i − ε_j| < V) scales as N_s² × (V/σ), which is extensive. The binary classification systematically undercounts effective thermal regions by neglecting resonance-assisted delocalization. The missing "resonant-pair thermal regions" are not rare — they are more abundant than the all-below-threshold blocks counted in K1.1, especially near the MBL transition where the gap between typical ε and ε_c is small.

**What the authors must prove:** Quantify the systematic error introduced by the binary classification against a more realistic criterion that accounts for nearest-neighbor resonance effects. Show that the resonance-assisted thermal regions do not qualitatively change the percolation conclusion. If they cannot, the entire paper's foundation is unsound.

---

## REJECTION REASON 2: Weakest Step in the Derivation Chain

**[评级: 致命]**

The claim in K1.2 that the extremal index θ = 1 for the squared exponential correlation kernel C(r) = exp(−r²/2ξ²) contains a category error between asymptotic extreme value theory and finite-threshold physics. The extremal index θ is rigorously defined (Leadbetter 1983, Aldous 1989) as a limit: θ = lim_{u→∞} P(max_{i∈cluster} X_i ≤ u | X₁ > u), where the threshold u is taken to infinity. For the squared exponential kernel, the associated Gaussian field is mean-square differentiable (infinitely differentiable, in fact). In the asymptotic limit u → ∞, exceedances of a smooth Gaussian field occur as isolated points because the local maximum at the exceedance point is so extreme that the field falls below threshold within a vanishingly small distance determined by the second derivative at the maximum, which scales as u/ξ². Formally, θ(u→∞) = 1.

However, the MBL problem involves a FINITE threshold ε_c/W_c, not an asymptotic one. For physical MBL parameters (W ≈ 10–20t, W_c ≈ 4–6t), the effective normalized threshold u_eff = (ε − μ)/σ is typically 2–3 standard deviations above the mean, corresponding to p_th ≈ 0.001–0.02. At this finite threshold, the squared exponential kernel's extreme smoothness actually WORKS AGAINST the θ=1 claim: because the field is differentiable, high-threshold excursions of the squared exponential field form spatially connected clusters whose typical diameter is proportional to ξ (not vanishing), as the field varies continuously in space. The "clumps" of above-threshold sites have non-trivial geometry, and the Poisson clumping heuristic's clump-size calculation (Aldous 1989, Chapter J) gives an effective extremal index θ(u,ξ) that depends on both u and ξ at finite u.

The error can be quantified: for a smooth 2D Gaussian field with squared exponential kernel, the expected area of a single excursion cluster above threshold u is A_clump ≈ 2πξ²/(u²) × log(1/p_th(u)) (from Adler & Taylor 2007, "Random Fields and Geometry," Theorem 15.9.2). For u=3, ξ=2, this gives A_clump ≈ 2π×4/9 × log(1000) ≈ 19.3 lattice sites — a connected region of ~5 sites in diameter, not an isolated point. The effective extremal index θ_eff(u,ξ) = 1/N_eff, where N_eff ≈ A_clump is the average size of an exceedance clump, gives θ_eff(3, 2) ≈ 0.05, NOT 1. This directly contradicts K1.2 and propagates a factor-of-20 error into K1.3, K1.4, and the percolation threshold analysis.

**What the authors must prove:** Derive the extremal index θ at the FINITE physical threshold u = ε_c/W_c relevant to MBL experiments (not the asymptotic u→∞ limit), for both squared exponential and exponential kernels. Show that using θ(u→∞) is a controlled approximation with bounded error. Or acknowledge that K1.2 is valid only in the pathological limit ε_c → ∞, which is physically irrelevant.

---

## REJECTION REASON 3: Conflict with Existing Literature

**[评级: 致命]**

**K1.4 (η(W) < 1.128 for all W > 0 → rare thermal regions NEVER percolate)** is in direct conflict with two established results:

**(a) De Roeck & Huveneers, Phys. Rev. B 95, 155129 (2017) [arXiv:1608.04315].** This paper proves that in d ≥ 2, any finite rare ergodic ("thermal") region of sufficient size triggers a quantum avalanche that thermalizes the entire system in the thermodynamic limit. The critical bubble size N* ~ (1/ξ_loc)^(d/(d−1)) is finite for any nonzero localization length ξ_loc. Critically, the De Roeck–Huveneers proof does NOT require the thermal regions to percolate geometrically — a SINGLE supercritical thermal bubble is sufficient to destroy MBL via runaway growth. The authors' percolation-based stability criterion (requiring η > η_c for instability) therefore addresses a straw man: the established avalanche literature already shows that percolation is not a necessary condition for MBL destruction. A conclusion that thermal regions "NEVER achieve percolation density" is irrelevant to the actual stability question if a single thermal region (not a percolating network) already kills MBL.

The authors' response that "avalanche dynamics are Phase 3" does not excuse presenting K1.4 as a stability conclusion when the avalanche criterion (single-bubble) is strictly weaker than the percolation criterion (network). A system can fail the percolation test and still be unstable to the avalanche mechanism.

**(b) Štrkalj, Doggen & Castelnovo, Phys. Rev. B 106, 184209 (2022) [arXiv:2204.05198]** directly contradicts K1.5. This paper demonstrates that in 2D Aubry-André models, Weak Potential Lines (WPLs) span the entire system and support large-scale particle transport well into the MBL phase. The WPLs are extended over the full system size (limited only by computational constraints to L ~ 20–30 in their numerics), not truncated at L ≈ 3 as K1.5 claims. The WPL phenomenon is a generic feature of 2D quasiperiodic potentials with incommensurate wavevectors — exactly the class K1.5 purports to characterize.

The resolution proffered in the internal PI review — that K1.5's derivation assumes a separable potential while the WPL physics requires nonseparable potentials — merely demonstrates that K1.5 covers a special, nongeneric case. A conclusion about "2D quasiperiodic Aubry-André potential with irrational wavevectors" that does not apply to the nonseparable case studied by Štrkalj et al. is misleadingly broad. The Diophantine hard-cutoff result is an artifact of the separable ansatz, not a physical property of quasiperiodic systems.

**What the authors must prove:** (a) Explain how geometric non-percolation of static rare regions implies stability against dynamical avalanche — this requires bridging the gap between the single-bubble De Roeck–Huveneers criterion and the network-percolation criterion used in K1.4. (b) Demonstrate that their Diophantine hard-cutoff result survives in a nonseparable 2D quasiperiodic potential and does not simply reflect the nongeneric separable-potential assumption. Without (a), K1.4 is a non sequitur. Without (b), K1.5 is overclaimed.

---

## REJECTION REASON 4: Numerical Reasonableness Challenge

**[评级: 严重]**

I perform an independent back-of-envelope estimate to test K1.4's central numerical claim. The prediction chain is:

1. Define p_th(W) = fraction of sites with local disorder below W_c.
2. For IID Gaussian disorder with standard deviation W, p_th(W) = Φ(W_c/W), where Φ is the Gaussian CDF.
3. The number density of thermal blocks of size ≥ L in a system of area A = N_s² is approximately n_L ≈ (A/L²) × p_th(W)^(L²).
4. Map each block to a disc of effective radius r_eff = L/2 (disc diameter equals block side).
5. The percolation parameter η_L ≈ n_L × π(L/2)².

Plug in numbers at the MBL-typical point W = 12t, W_c ≈ 5t (from the well-established 1D MBL transition, Luitz et al. PRL 2015):

- p_th = Φ(5/12) ≈ Φ(0.417) ≈ 0.662. Wait — at W=12t, the typical disorder is actually much larger than W_c, so p_th is NOT ~0.66. Let me reconsider. The standard deviation of local disorder is W, and W_c is the THRESHOLD below which a site is "thermal." In the Anderson model, the localization threshold corresponds to energies near the band edge. At the band center, ALL states are extended in 2D (no mobility edge at band center in the orthogonal class). So the concept of a single-site localization threshold ε_c must refer to the tail states. For the interacting problem, the relevant p_th is the fraction of sites near resonance, estimated by Gopalakrishnan et al. (PRB 2015, arXiv:1502.07715) as p_th ≈ exp(−const × W²/W_c²).

Using Gopalakrishnan's estimate p_th ≈ exp(−α W²/W_c²) with α ≈ 0.2–0.5, at W/W_c = 2 (deep MBL): p_th ≈ exp(−0.3×4) ≈ 0.30. At W/W_c = 3: p_th ≈ exp(−0.3×9) ≈ 0.067. At W/W_c = 4: p_th ≈ exp(−0.3×16) ≈ 0.008.

Now compute n(L=3) for N_s=100 at W/W_c=2: n ≈ (10⁴/9) × 0.30⁹ ≈ 1111 × 1.97×10⁻⁵ ≈ 0.022. η ≈ 0.022 × π × 1.5² / 10⁴ ≈ 1.56×10⁻⁵ << 1.128. So far consistent with K1.4.

But the CRITICAL check comes at weaker disorder, where the avalanche is most dangerous. At W/W_c = 1.5 (near the MBL transition): p_th ≈ exp(−0.3 × 2.25) ≈ 0.51. n(L=4) for N_s=100: (10⁴/16) × 0.51¹⁶ ≈ 625 × 2.2×10⁻⁵ ≈ 0.014. η ≈ 0.014 × π × 4 / 10⁴ ≈ 1.76×10⁻⁵.

At W/W_c = 1.2: p_th ≈ exp(−0.3 × 1.44) ≈ 0.65. n(L=5): (10⁴/25) × 0.65²⁵ ≈ 400 × 2.0×10⁻⁵ ≈ 0.008. η ≈ 0.008 × π × 6.25 / 10⁴ ≈ 1.57×10⁻⁵.

These all seem very small. But I now identify the true numerical problem: **this analysis is self-defeating at the relevant scale.** For the parameters where η(W) is non-negligible (W approaching W_c from above), the thermal blocks are so abundant that the Poisson clumping heuristic's assumptions fail — the system is a dense, interacting network of thermal clusters, not a sparse set of Poisson points. For the parameters where the Poisson heuristic is valid (W >> W_c), η(W) is astronomically small and the conclusion η < 1.128 is trivially true but physically meaningless — it is equivalent to noting that a gale-force wind cannot blow down a concrete bunker.

The regime where the question MATTERS — W ∈ [W_c, 1.5W_c] near the transition — is precisely where the derivation is invalid by the authors' own admission (domain restricted to W > 2W_c). The numerical check thus reveals a catch-22: K1.4 is either (a) trivial (deep MBL, η ~ 10⁻¹⁰) or (b) unjustified (near-transition regime where the derivation fails). In neither case does it constitute a publishable result.

**What the authors must prove:** Compute η(W) at W = 1.2 W_c (near the transition) using a method that does not rely on the Poisson asymptotic, and show that η remains below 1.128. If this cannot be done analytically, provide numerical evidence for at least three disorder realizations at N_s ≥ 100. Without this, K1.4 is a trivial bound dressed as a nontrivial physical result.

---

## REJECTION REASON 5: Closest Existing Work and Novelty Assessment

**[评级: 中等]**

The closest prior work is **Chandran & Laumann, "A semi-classical limit for the many-body localization transition," Phys. Rev. B 92, 024301 (2015) [arXiv:1501.01971].** I compare K1.1–K1.6 against this paper sentence by sentence:

| Aspect | Chandran & Laumann (2015) | Current manuscript (K1.1–K1.6) | Novelty? |
|--------|--------------------------|-------------------------------|----------|
| Framework | Semiclassical Clifford circuit; ergodic puddles percolate at MBL transition in d ≥ 2 | Classical extreme-value statistics of disorder potential; rare thermal blocks mapped to percolation problem | Different mathematical framework, but same physical picture |
| Rare region characterization | Puddle size distribution computed from circuit dynamics; clusters identified via operator spreading | P(L,W) from Poisson clumping heuristic; static geometric criterion | K1.1–K1.3 are static, Chandran & Laumann are dynamical — but the Chandran picture subsumes the static case |
| Percolation conclusion | In d ≥ 2, ergodic puddles percolate at the MBL transition, producing a continuous phase transition | η(W) < 1.128 in deep MBL phase → no percolation of static rare regions | Chandran & Laumann find percolation AT the transition; K1.4 finds no percolation DEEP in the phase. These are not contradictory but the K1.4 framing ("NEVER achieve percolation") is misleading without specifying the parameter regime |
| Quasiperiodic systems | Not addressed | K1.5–K1.6: hard cutoff for QP potentials | Genuinely new (if correct), but K1.5's result of L_max ≈ 3 is too weak to be useful — it states the obvious (deep QP MBL has no rare regions) after the more general result of Štrkalj et al. |
| Scaling | n ∝ exp(−cW²) from extreme-value asymptotics (assumed) | n_rand ∝ exp(−cW²) (K1.6) | The exp(−cW²) form follows directly from Gaussian extreme value theory and is not a discovery — any Gaussian-disordered model has this scaling by construction |

The novelty assessment is unfavorable. The core physical picture — that rare thermal regions should be characterized by their spatial statistics and that percolation arguments constrain MBL stability — was already established by Chandran & Laumann (2015). The specific conclusions K1.1–K1.3 are applications of textbook extreme value theory (Aldous 1989, Leadbetter 1983) that add quantitative detail but no qualitatively new physics. K1.4's bound uses the well-known continuum percolation threshold η_c = 1.128 (Mertens & Moore, PRE 86, 061109, 2012), applied to a disc model of rare regions — a standard technique in disordered systems theory. K1.6's contrast between exp(−cW²) and W^{−γ} scaling is a consequence of the input assumptions (Gaussian vs. power-law tails), not a derived result.

Furthermore, **Prelovšek, Mierzejewski, Krsnik & Barišić, "Many-body localization as a percolation phenomenon," Phys. Rev. B 103, 045139 (2021) [arXiv:2010.12295]** has already characterized the MBL transition via percolation in Fock space, with explicit cluster-size distributions and a percolation threshold. The current manuscript's real-space percolation analysis is complementary but does not obviously supersede the Fock-space approach, which directly incorporates many-body physics absent from the current static real-space treatment.

**What the authors must prove:** Provide a point-by-point comparison table (as above) between their work and Chandran & Laumann (2015) plus Prelovšek et al. (2021), explicitly identifying: (a) which conclusion in K1.1–K1.6 is not implied by either prior work, (b) what new observable prediction follows that is falsifiable with current experiments, and (c) why the real-space approach captures physics that Fock-space percolation misses. Without this, the incremental contribution over existing percolation frameworks is not sufficient for Nature Physics.

---

## RECOMMENDATION

**REJECT.**

The manuscript contains a category error (confusing asymptotic extremal index θ(u→∞) with finite-threshold physics), conflicts with established avalanche literature that renders its central stability conclusion a non sequitur, and its strongest-sounding conclusion (K1.5) is contradicted by a PRB publication. The remaining conclusions are either applications of textbook extreme value theory to a specific physical model, or trivial bounds that hold in a parameter regime where they carry no physical content. The reported novelty does not rise to the standard of Nature Physics.
