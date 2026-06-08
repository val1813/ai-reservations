# LP29-AmorphousBands Reviewer Round 3

Role: Nature Physics malicious reviewer  
Input scope: only the supplied core conclusion list; no full derivation read.

## Step 0: hallucination check

### Q0.1 Dimensional consistency

1. `mu_D = mu_H / r_H`
   - `mu_D`, `mu_H`: SI unit `m^2 V^-1 s^-1`.
   - `r_H`: dimensionless Hall factor.
   - Result: dimensionally consistent.

2. `n_true = r_H * n_H`; `n_m3 = n_H_cm3 * 1e6 * r_H`
   - `n_H_cm3`: `cm^-3`; multiplying by `1e6` gives `m^-3`.
   - `r_H`: dimensionless.
   - Result: dimensionally consistent.
   - Caveat: sign and convention of `r_H` must be explicit because transport literature often defines Hall factor as `r_H = mu_H / mu_D`, but some data reductions hide this in `n_H` rather than `mu_H`.

3. `kF propto r_H^(1/3), tau propto r_H^-1, l propto r_H^(-2/3), kF*l propto r_H^(-1/3)`
   - If `n_true = r_H n_H`, then `kF propto n_true^(1/3) propto r_H^(1/3)`: consistent.
   - If `mu_D = e tau / m* = mu_H / r_H`, then `tau propto r_H^-1`: consistent, assuming fixed `m*`.
   - If `l = vF tau` and `vF propto kF`, then `l propto r_H^(1/3) r_H^-1 = r_H^(-2/3)`: consistent.
   - Then `kF l propto r_H^(1/3) r_H^(-2/3) = r_H^(-1/3)`: consistent.
   - Caveat: fixed `m*`, parabolic band, degeneracy convention, and same `n_H` baseline are hidden assumptions.

4. `t_ij = t0 * exp(-(r_ij-r0)/lambda) * (1 + alpha_edge I_edge + alpha_corner I_corner) * exp(-beta f_OO)`
   - `t_ij`, `t0`: energy.
   - `(r_ij-r0)/lambda`: dimensionless only if `lambda` is length.
   - `alpha_edge`, `alpha_corner`, `beta`, `f_OO`, indicators: dimensionless.
   - Result: dimensionally consistent if `lambda > 0` and the multiplicative bracket stays nonnegative.

### Q0.2 Direction checks

1. Hall-factor scaling:
   - Increase `r_H`: `n_true` and `kF` increase; `tau`, `l`, and `kF*l` decrease under the stated convention.
   - Direction is internally consistent, but counterintuitive enough that a manuscript must state whether it is holding `mu_H` and `n_H` fixed.

2. B-line hopping model:
   - Larger `r_ij` reduces `t_ij` if `lambda > 0`.
   - Larger `f_OO` reduces `t_ij` if `beta > 0`.
   - Positive `alpha_edge/corner` increase hopping through those motifs; negative values can reverse this.
   - The claimed direction "mobility/Drude/ridge coherence decreases as `z_eff/S_GC` decreases" is not derivable from the formula alone unless `z_eff/S_GC` is explicitly tied to a monotone aggregate of the positive hoppings.

### Q0.3 Circularity check

- A1 warning is correct: using `kF*l(mu_H)` to predict the same `mu_H` is circular because `tau` is derived from `mu_H`.
- Allowed tests using independent `l_reported`, TCR/activation, optical `tau`, or residual class reduce but do not eliminate circularity unless sample matching and preprocessing are locked before regression.
- B currently has only a reproducible synthetic toy benchmark. That is circular for physics validation if the toy generator encodes the same graph rule being "discovered".

### Q0.4 Order-of-magnitude check

- No concrete numerical estimates are supplied except unit conversion `cm^-3 -> m^-3` via `1e6`, which is correct.
- No >10-order mismatch can be assessed from the supplied list.

Verdict: no mechanical dimensional error found. Main hallucination risks are hidden convention dependence in `r_H`, circular use of Hall-derived quantities, and treating synthetic toy recovery as physical validation.

## Three-round priority search

Search rule followed: paper-search-mcp first in all academic searches. WebSearch was not used because MCP returned nonempty relevant results.

### Round 1: method-level duplication

Queries used:
- paper-search-mcp arXiv/Semantic/CrossRef/Google Scholar: `amorphous oxide mobility edge Ioffe-Regel Hall factor Drude Wannier spectral observables graph metrics`

Relevant hits:
- Graham, Adkins, Behar, Rosenbaum, "Experimental study of the Ioffe-Regel criterion for amorphous indium oxide films", Journal of Physics: Condensed Matter, 1998, DOI `10.1088/0953-8984/10/4/010`.
- Lee, Cobb, Dodabalapur, "Band transport and mobility edge in amorphous solution-processed zinc tin oxide thin-film transistors", Applied Physics Letters, 2010, DOI `10.1063/1.3517502`.

Finding: mobility edge and Ioffe-Regel diagnostics in amorphous oxide transport are not new. No exact same-sample residual-comparison protocol was found in this round.

### Round 2: framework-blind search

Queries used:
- paper-search-mcp arXiv/Semantic/CrossRef/Google Scholar: `same sample comparison Hall Drude optical mobility amorphous oxide transport local structure connectivity`
- paper-search-mcp all selected sources: `amorphous oxide semiconductor local structure graph connectivity mobility In s orbital overlap`

Relevant hits:
- Kamiya, Nomura, Hosono, "Origins of High Mobility and Low Operation Voltage of Amorphous Oxide TFTs: Electronic Structure, Electron Transport, Defects and Doping", Journal of Display Technology, 2009, DOI `10.1109/JDT.2009.2021582` and related 2009 version DOI `10.1109/JDT.2009.2034559`.
- Nomura et al., "Local coordination structure and electronic structure of the large electron mobility amorphous oxide semiconductor In-Ga-Zn-O: Experiment and ab initio calculations", Physical Review B, 2007, DOI `10.1103/PhysRevB.75.035212`.
- Srivastava et al., "Electronic structure and transport in amorphous metal oxide and amorphous metal oxy-nitride semiconductors", Journal of Applied Physics, 2019 / arXiv `1812.11333`.
- Narushima et al., "Electronic structure and transport properties in the transparent amorphous oxide semiconductor", Physical Review B, 2002, DOI `10.1103/PhysRevB.66.035203`.

Finding: the In-s orbital overlap, local coordination, amorphous oxide high mobility, and structure-transport framing are heavily preexisting. LP29's only possible novelty is not "graph metrics matter", but whether its exact graph metrics beat mobility-edge/Ioffe-Regel under strict same-sample residual tests.

### Round 3: negative/criticism/counterexample search

Queries used:
- paper-search-mcp arXiv/Semantic/CrossRef/Google Scholar: `amorphous oxide band transport mobility edge failure criticism counterexample Hall factor disorder`
- paper-search-mcp all selected sources: `Jankousky amorphous oxide QSGW structures In s conduction band mobility graph`

Relevant hits:
- Nenashev, Gebhard, Meerholz, Baranovskii, "Percolation Description of Charge Transport in Amorphous Oxide Semiconductors: Band Conduction Dominated by Disorder", in *Amorphous Oxide Semiconductors*, 2022, DOI `10.1002/9781119715641.ch6`.
- Pashmakov, Claflin, Fritzsche, "Transport near the mobility edge, the sign of the hall effect, photoreduction and oxidation of amorphous InOx", Journal of Non-Crystalline Solids, 1993, DOI `10.1016/0022-3093(93)90584-k`.
- Fishchuk et al., "Interplay between hopping and band transport in high-mobility disordered semiconductors at large carrier concentrations: The case of the amorphous oxide InGaZnO", Physical Review B, 2016, DOI `10.1103/PhysRevB.93.195204`.
- Jankousky et al., "Effective bands and band-like electron transport in amorphous solids", Nature Physics, 2026, DOI/page indicated by MCP as `s41567-025-03099-x`.

Finding: no fully identical protocol found. However, there are direct prior frameworks explaining band-like transport, mobility-edge language, Hall/drift comparison, disorder-dominated band conduction, and In-s conduction. LP29 must be sold as a measurement-comparison protocol, not as a new mechanism.

Search tool log:
- Round 1: paper-search-mcp arXiv, Semantic Scholar, CrossRef, Google Scholar. No WebSearch fallback.
- Round 2: paper-search-mcp arXiv, Semantic Scholar, CrossRef, Google Scholar, OpenAlex via unified search. No WebSearch fallback.
- Round 3: paper-search-mcp arXiv, Semantic Scholar, CrossRef, Google Scholar, OpenAlex via unified search. No WebSearch fallback.

## Five strongest rejection reasons

0. Narrative retreat warning: the claim has already shrunk from a mechanism for amorphous band-like transport to a measurement protocol comparing residual predictive power. That is a real retreat, not a Nature Physics-level mechanism unless the protocol yields an externally validated surprise.

1. Same-sample residual protocol has no real dataset yet. The current state admits no digitized A1 CSV, no Jankousky raw-structure/QSGW join table, and no external labels. Without these, the central claim is not evidence; it is an analysis plan. To answer, authors must supply locked CSVs, sample IDs, observables, preprocessing, and blind residual tests. [fatal]

2. A1 can easily become algebraic self-prediction. `kF*l` inherits `mu_H` through `tau` unless it uses independent `l`, optical `tau`, TCR/activation, or externally labeled classes. The proposal states this caveat, but has not executed the noncircular version. Authors must prove every A-line predictor is independent of the target observable. [fatal]

3. B-line graph-metric direction is underdetermined by the stated hopping formula. The formula says distance, O-O penalty, and motif multipliers affect `t_ij`; it does not by itself prove that lower `z_eff/S_GC` lowers mobility/Drude/ridge coherence. Authors must define `z_eff/S_GC`, show monotonic relation to the Hamiltonian spectrum, and test against controls. [serious]

4. Prior art consumes most scientific novelty. Mobility edge in amorphous oxides, Ioffe-Regel tests, band-like amorphous oxide transport, In-s orbital overlap, and local coordination explanations are all already present in the literature. Authors must explicitly distinguish LP29 from Graham 1998, Lee 2010, Nomura 2007, Kamiya/Nomura/Hosono 2009, Srivastava 2019, Fishchuk 2016, and Jankousky 2026. [fatal]

5. Synthetic toy benchmark is not validation. If the synthetic generator contains the same graph rule, recovering graph superiority only verifies code plumbing. Authors must provide seed-level CSV/scripts/edge lists for reproducibility, then show transfer to independent Hall/Drude/Wannier/spectral observables not used in model construction. [serious]

## Citation and priority issues requiring PI verification

- Verify the exact bibliographic status and content of Jankousky et al., "Effective bands and band-like electron transport in amorphous solids", Nature Physics, 2026 / DOI-like article id `s41567-025-03099-x`, especially whether it already contains raw structures, QSGW mobility calculations, or conclusions that subsume LP29.
- Check whether "same-sample comparison of Hall, drift/Drude, optical tau, mobility edge, and local-structure descriptors" exists in supplementary datasets or review chapters, not just title/abstract.
- Verify Hall factor conventions in each experimental source before using `mu_D = mu_H/r_H` and `n_true = r_H n_H`; one convention flip reverses the correction.
- Verify whether Srivastava 2019's orbital-overlap metric is mathematically equivalent to LP29's In-s graph metrics under a change of notation.
- Verify whether Nenashev et al. 2022 percolation/disorder framework already predicts residual structure metrics beyond mobility edge.

## Must-add work before next round

Yes. The next round must add real implementation, not more prose:

1. A1 digitized same-sample CSV with target observables and predictor provenance flags.
2. Jankousky raw structures/QSGW join table or a documented reason it cannot be obtained.
3. B-line seed-level synthetic CSV, script, and edge list.
4. One external-label application where the target was not used to define the graph metric.
5. Locked ablation: Hall/Ioffe-Regel only vs graph metrics only vs combined model, with matched `n`/`E_F-Ec`, linewidth convention, onsite variance, and finite-size controls.

## If forced to pick one fatal error

If I must identify one fatal flaw: LP29 currently has no noncircular, same-sample, independently labeled dataset demonstrating that In-s graph metrics have residual predictive power beyond mobility-edge/Ioffe-Regel controls.

This is not "maybe a problem"; it is the single rejection reason I would give an editor if forced to choose one.

Author escape route: produce the locked same-sample table and run the predeclared residual comparison against independent Hall/Drude/Wannier/spectral observables, with all Hall-factor and linewidth conventions fixed before looking at outcomes.

## Recommendation

Reject in current form. It may continue as an internal protocol-development project, but it is not yet a publishable physics result. The next round must add real executed data products and external validation.
