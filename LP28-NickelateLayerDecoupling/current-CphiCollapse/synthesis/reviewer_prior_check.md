# PI Independent Prior-Art Check After REVIEWER

Date: 2026-06-04

Trigger: REVIEWER flagged prior-art / adjacent-explanation risk.

## Search Path

Used paper-search-mcp first:

`La3Ni2O7 qz resolved RIXS odd even bilayer susceptibility pressure superconductivity`

Then WebSearch fallback for the specific REVIEWER claims.

## Result

No complete same-claim prior found for:

`R_oe = P_oe - E_crossfit[P_oe | B_min]`

where `P_oe` is an odd/even bilayer susceptibility residual tested against measured non-tautological `B_min`.

But the adjacent-prior field is dense enough that `LP28-CphiCollapse` must be treated as a bounded protocol, not a theory breakthrough claim.

## Key Adjacent Priors Found

1. RIXS / XAS already studies La3Ni2O7 electronic and magnetic excitations and emphasizes bilayer / dz2-apical-oxygen interlayer coupling.
   - arXiv:2401.12657
   - Nature Communications 2024: `Electronic and magnetic excitations in La3Ni2O7`
   - Risk: `P_oe` may be a reanalysis/protocolization of existing bilayer response information, not a new physical variable.

2. Theory already frames even/odd bilayer spin susceptibility as a useful discriminator.
   - arXiv:2401.16151
   - Risk: odd/even susceptibility language is not novel by itself.

3. Recent neutron / magnetic work on bilayer La3Ni2O7 exists.
   - arXiv:2605.03448
   - Risk: bilayer magnetic framework may already constrain the observable space.

4. Optical / Drude / pressure work exists and can absorb much of the c-axis-coherence interpretation.
   - npj Quantum Materials 2024: `Optical properties and electronic correlations in La3Ni2O7 bilayer nickelates under high pressure`
   - Risk: any `C_phi` correlated with Drude/c-axis coherence is likely not independent.

5. Oxygen vacancies / ligand holes are known high-risk baselines.
   - Nature 2024: Dong et al., `Visualization of oxygen vacancies and self-doped ligand holes in La3Ni2O7-delta`
   - Risk: oxygen stoichiometry and ligand-hole redistribution can swallow apparent residuals unless measured independently.

6. Structural pressure-transition work is highly relevant.
   - arXiv:2511.15265
   - ACS JPCC 2025 `Pressure-Induced Phase Transitions in Bilayer La3Ni2O7`
   - Risk: strain/phase/path effects can mimic odd/even response changes.

## PI Decision

REVIEWER's reduction is accepted:

- Do not claim `LP28-CphiCollapse` is a theoretical breakthrough candidate yet.
- Claim only: a strict bounded residual protocol now exists that can kill or preserve the independent `C_phi` object.
- Novelty, if any, is the residual-collapse framing and leakage-controlled decision architecture, not the component physics.

## Required Boundary For Future Writing

Allowed:

`No complete prior was found for the exact residual-collapse test R_oe | B_min. Existing literature covers the component observables and confounders, so the current contribution is a bounded decision protocol.`

Forbidden:

`P_oe is a newly discovered nickelate variable.`

`R_oe is already evidence for phase-bus readiness.`

`C_phi is independent of c-axis coherence, oxygen, strain, disorder, dz2/self-doping, or sample quality.`
