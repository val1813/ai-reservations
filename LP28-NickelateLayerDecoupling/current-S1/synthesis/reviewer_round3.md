# REVIEWER Report: LP28-S1 Round 3

Role: independent malicious reviewer after 3 A/B rounds.

Input read:

- `D:\Claude\ai-reservations\ai\REVIEWER.md`
- `current-S1\synthesis\pi_round3_synthesis.md`
- `current-S1\A\round3.json`
- `current-S1\B\round3.json`
- `current-S1\synthesis\inspector_A_round3.md`
- `current-S1\synthesis\inspector_B_round3.md`

Core conclusion list attacked:

1. LP28-S1 survives only as a preregistered protocol candidate, not a validated predictor or mechanism.
2. Unified primary encoder: `I_phi = E_z2_meV*C_phi_primary/(kB*120K + hbarGamma_phi + E_floor)`, all input-side.
3. Primary `C_phi` is normal-state c-axis Drude fraction at 120 K; SVD observability is audit-only.
4. GO requires sealed input packet, exact auditor recomputation, `>=6` complete rows, coefficient-sensitivity pass, and noncollapse against simpler baselines.
5. Any output leakage, post-output retuning, baseline collapse, or arbitrary sensitivity failure kills S1.

## Q0 Hallucination Check

### Q0.1 Dimensional check

Primary equation:

`I_phi = E_z2_meV*C_phi_primary/(kB_meV_per_K*120 + hbarGamma_phi_meV + E_floor_meV)`

- Left side: declared dimensionless.
- Numerator: `E_z2_meV` is meV, `C_phi_primary` is dimensionless, so numerator is meV.
- Denominator: `kB_meV_per_K*120 K`, `hbarGamma_phi_meV`, and `E_floor_meV` are meV.
- Result: dimensionless.

Primary Drude fraction:

`C_phi_primary = max(0, min(1, W_c_Drude/(W_c_Drude + W_c_incoh + epsilon_W)))`

- `W_c_Drude`, `W_c_incoh`, and `epsilon_W` are all declared as `ohm^-1 cm^-2`.
- Ratio is dimensionless; clipping is dimensionless.

No mechanical dimensional hallucination found in the merged A-side formula.

### Q0.2 Direction check

For admissible nonnegative inputs:

- `E_z2_meV` increases `I_phi`.
- `C_phi_primary` increases `I_phi`.
- `hbarGamma_phi_meV` decreases `I_phi`.
- `E_floor_meV` decreases `I_phi`.
- `W_c_Drude -> 0` gives `C_phi_primary -> 0` and `I_phi -> 0`.
- `W_c_incoh -> infinity` gives `C_phi_primary -> 0`.
- `hbarGamma_phi_meV -> infinity` gives `I_phi -> 0`.

No numerator/denominator reversal was detected. The direction is algebraically self-consistent.

### Q0.3 Circularity check

The written protocol forbids `Tc`, zero resistance, shielding, Meissner fraction, critical current, Josephson plasma, superfluid density, condensate spectral weight, transition width, and phase-diagram labels from entering construction. That is necessary but not sufficient. The live circularity risk is indirect: 120 K normal-state status, sample/pressure-grid selection, and matched-sample provenance can encode known superconducting dome or density-wave context before the packet is sealed.

Verdict: no formula-level circularity, but protocol-level leakage risk remains fatal unless the real P0 packet proves independent sample/pressure selection and pre-output provenance.

### Q0.4 Order-of-magnitude check

Denominator lower bound:

- `kB*120 K = 0.08617333262*120 = 10.3407999144 meV`.
- With `E_floor >= 3 meV`, denominator minimum is `13.3407999144 meV`.
- With `E_z2 <= 120 meV` and `C_phi <= 1`, `I_phi <= 8.995`.

No extreme magnitude gulf in the formula itself. The magnitude problem is statistical and experimental: `>=6` rows is far too small to establish noncollapse robustly in a high-pressure nickelate system with heterogeneous sample quality, oxygen stoichiometry, pressure gradients, and output controversy.

### Q0.5 Q0 verdict

Hallucination check: PASS for dimensions, algebraic direction, and gross formula magnitude. FAIL as a scientific survival claim unless the protocol is treated as a purely preregistered execution recipe with no validation, no mechanism, and no predictor language.

## Three-Round Prior-Art / Challenge Search

All academic searches were performed with `paper-search-mcp` first. Web search was not used because paper-search-mcp returned nonempty results for the relevant searches.

### Round 1: method-level overlap

Queries:

- `La3Ni2O7 c-axis optical conductivity Drude fraction pressure superconductivity normal state 120 K`
- `layered nickelate interlayer coherence c-axis Drude optical conductivity superconductivity predictor`
- `La3Ni2O7 high pressure superconductivity normal state optical spectroscopy density wave 120 K`

Findings:

- Wang, Wen, Wu, Yao, Xiang, `Normal and superconducting properties of La3Ni2O7`, arXiv:2406.04837, reviews the field and explicitly emphasizes sample quality, oxygen deficiencies, and measurement reliability as unresolved problems.
- Meng et al., `Density-wave-like gap evolution in La3Ni2O7 under high pressure revealed by ultrafast optical spectroscopy`, Nature Communications 2024, DOI `10.1038/s41467-024-54518-1`, reports pressure-dependent density-wave gap evolution and a new density-wave order around 130 K above 29.4 GPa. This directly threatens the claim that a fixed 120 K optical gate is generically clean normal-state input.
- Won and Maki, `The c-axis optical conductivity and the superconducting fluctuation`, Physica C 2000, DOI `10.1016/S0921-4534(00)00721-8`, and older layered-cuprate optical-conductivity work show that c-axis optical response and interlayer coherence are long-standing superconductivity-adjacent observables, not a novel LP28-specific construct.

No exact duplicate of the sealed LP28-S1 protocol was found.

### Round 2: framework blind-spot search

Queries:

- `superconducting Tc prediction materials optical conductivity interlayer coherence no-go failure limit nickelate 2024 2025 2026`
- `blind prediction superconductivity nickelates input features baseline collapse small sample protocol preregistration`
- `La3Ni2O7 oxygen deficiency sample quality superconductivity pressure Meissner controversy 2024 2025 2026`

Findings:

- Lu et al., `Impact of pressure and apical oxygen vacancies on superconductivity in La3Ni2O7`, Communications Physics 2025, DOI `10.1038/s42005-025-02266-z`, argues oxygen vacancies suppress pairing strength and superfluid density. This makes the proposed `E_floor` not a nuisance term but a dominant uncontrolled sample-quality axis.
- Jiao et al., `Enhanced conductivity in Sr doped La3Ni2O7-delta with high-pressure oxygen annealing`, Physica C 2024, DOI `10.1016/j.physc.2024.1354504`, reinforces that oxygen processing changes conductivity itself, hence the Drude fraction can be a sample-preparation proxy.
- Talantsev, `Solving mystery with the Meissner state in La3Ni2O7-delta`, 2024, DOI `10.62539/2949-5644-2024-0-3-65-76`, frames the Meissner-state issue as experimentally difficult. This matters because LP28-S1 evaluates against bulk-output labels whose own reliability is contested.

Blind-spot verdict: the protocol underweights the difficulty of making input variables and output labels mutually clean in the same high-pressure nickelate sample.

### Round 3: denial / counterexample search

Queries:

- `10.1103/PhysRevB.109.205156 La3Ni2O7 optical spectroscopy`
- `La4Ni3O10 optical spectroscopy c-axis Drude Liu 2025 arXiv 2512.03806`
- `La3Ni2O7 pressure c-axis transport interlayer coupling dz2 orbital superconductivity criticism counterexample`

Findings:

- Ouyang, Gao, Lu, `Absence of electron-phonon coupling superconductivity in the bilayer phase of La3Ni2O7 under pressure`, npj Quantum Materials 2024, DOI `10.1038/s41535-024-00689-5`, is not a direct contradiction of LP28-S1, but it undercuts any drift toward a mechanism claim by showing that a plausible conventional mechanism is absent.
- The cited `Liu et al. 2025 La4Ni3O10 optical spectroscopy / arXiv:2512.03806` from A Round 3 did not resolve through paper-search-mcp in the targeted query. Under REVIEWER rules I do not declare it fabricated, but it is citation-suspect and requires PI verification before any write-up.
- Recent theory and experiments continue to point to multiple competing explanations: pressure-induced structural change, density-wave evolution, oxygen stoichiometry, strange-metal behavior, interlayer coupling, and orbital-selective correlations. LP28-S1 has no way to distinguish these without becoming a baseline-collapse exercise.

Three-round duplicate verdict: no direct prior duplicate found; direct competition is not the problem. The problem is that the protocol may be a formal wrapper around prior-art interlayer-coherence/sample-quality observables.

## Rejection Reasons

1. The 120 K normal-state premise is not stable in the target material. Meng et al. report high-pressure density-wave behavior with a new transition near 130 K above 29.4 GPa. A fixed 120 K spectrum can sit inside a pressure-induced ordered regime, so the optical gate is not guaranteed to be clean input. Authors must prove, for each row, that 120 K is pre-output normal-state by optical criteria alone. [fatal]

2. `C_phi_primary` is almost certainly generic c-axis interlayer coherence. The Drude fraction is readable, but that readability is exactly why it collapses to prior-art c-axis optical conductivity. The protocol admits this by making `C_phi`-only and total-c-axis-weight baselines fatal, which means the central variable is not a new mechanism but a baseline waiting to fail. Authors must show noncollapse on sealed rows, not argue physical plausibility. [fatal]

3. Same-sample sealed inputs are experimentally unrealistic at the required specificity. The protocol needs 120 K c-axis optical spectra, dz2 proxy, dephasing, oxygen vacancy, strain, residual scattering, pressure grid, and output labels with independent timestamps. The nickelate literature emphasizes oxygen deficiency, sample heterogeneity, and measurement difficulty under pressure. Authors must produce a real P0 packet; a written recipe is not survival. [fatal]

4. The statistical gate is underpowered even after the Inspector-B fix to `>=6` rows. With six rows, AUROC, Spearman, Kendall tau-b, tie rules, bootstrap intervals, and baseline-collapse calls are quantized and fragile. One mislabeled output, one pressure-gradient artifact, or one oxygen-defect outlier can flip survival. Authors must justify a power model or downgrade all post-output conclusions to pilot failure/success only. [serious]

5. The coefficient-sensitivity grid audits arbitrariness but does not remove it. Constants such as `alpha_z2`, `epsilon_W`, `E_floor_intercept_meV`, `E_floor_disorder_slope_meV`, and collapse thresholds are conventions, not calibrated physics. Rank stability under a handpicked grid only shows internal robustness to the chosen grid. Authors must either externally calibrate constants before P0 or state that a sensitivity pass is procedural, not scientific. [serious]

## Citation / Prior-Art Risk Items

- `Sui et al. 2024`, DOI `10.1103/PhysRevB.109.205156`, was cited in A Round 3 but did not clearly resolve in my targeted paper-search-mcp query. PI should verify title, content, and whether the citation actually supports the 120 K c-axis optical premise.
- `Liu et al. 2025 La4Ni3O10 optical spectroscopy`, cited as `arXiv:2512.03806`, did not resolve through paper-search-mcp. This is citation-suspect pending manual verification.
- The protocol should not cite cuprate c-axis optical conductivity or Josephson-plasma literature as support for a nickelate input predictor unless it explicitly labels those citations as analogy/background only.

## Narrative Retreat Check

Retreat detected but scientifically acceptable only if made explicit.

Earlier LP28-S1 language appears to have sought an index/predictor/mechanism. Round 3 now says "preregistered protocol candidate only" and "not validated predictor or mechanism." That is a major claim retreat. I will not punish it as evasive if the final title, abstract, and conclusions preserve the retreat. Any later phrase such as "predicts superconductivity", "validates phase-bus readiness", or "mechanism of layer decoupling" would be post-review claim inflation.

## Final Fatal-Error Item

**If I must pick one fatal error:** the primary variable `C_phi_primary` is a normal-state c-axis Drude fraction measured at a fixed 120 K, but the same literature field already treats c-axis optical coherence, density-wave evolution, oxygen stoichiometry, and pressure-induced structural state as entangled superconductivity-adjacent observables; therefore LP28-S1 has not shown an input-side variable that is independent of prior phase knowledge rather than a relabeled interlayer-coherence/sample-quality baseline.

This is not "possibly a problem"; it is the rejection reason I would give an editor if forced to name one fatal defect.

**Author's exit route:** deposit a real sealed P0 packet with at least six complete same-sample or predeclared matched-sample rows; timestamp sample/pressure selection before any superconducting outputs; prove 120 K normal-state status from forbidden-output-free optical fits; verify all suspicious citations; and demonstrate exact auditor recomputation plus noncollapse against `C_phi`-only, total-c-axis-weight, disorder-only, dephasing-only, and orbital-only baselines. Without that packet, S1 is only an unexecuted preregistration template.

## Recommendation

Reject as a scientific claim. Major revision only as a preregistered protocol template with no predictor, mechanism, or validation language.

One-sentence basis: the algebra is internally consistent, but the proposed primary input is not yet separable from prior-art c-axis coherence, sample quality, and high-pressure nickelate phase knowledge.

## Search Tool Usage Log

All academic searches used `paper-search-mcp` first. Web fallback was not used.

1. Method-level overlap:
   - `paper-search-mcp.search_papers`: `La3Ni2O7 c-axis optical conductivity Drude fraction pressure superconductivity normal state 120 K`
   - `paper-search-mcp.search_papers`: `layered nickelate interlayer coherence c-axis Drude optical conductivity superconductivity predictor`
   - `paper-search-mcp.search_papers`: `La3Ni2O7 high pressure superconductivity normal state optical spectroscopy density wave 120 K`
2. Framework blind-spot search:
   - `paper-search-mcp.search_papers`: `superconducting Tc prediction materials optical conductivity interlayer coherence no-go failure limit nickelate 2024 2025 2026`
   - `paper-search-mcp.search_papers`: `blind prediction superconductivity nickelates input features baseline collapse small sample protocol preregistration`
   - `paper-search-mcp.search_papers`: `La3Ni2O7 oxygen deficiency sample quality superconductivity pressure Meissner controversy 2024 2025 2026`
3. Denial / counterexample search:
   - `paper-search-mcp.search_papers`: `10.1103/PhysRevB.109.205156 La3Ni2O7 optical spectroscopy`
   - `paper-search-mcp.search_papers`: `La4Ni3O10 optical spectroscopy c-axis Drude Liu 2025 arXiv 2512.03806`
   - `paper-search-mcp.search_papers`: `La3Ni2O7 pressure c-axis transport interlayer coupling dz2 orbital superconductivity criticism counterexample`
