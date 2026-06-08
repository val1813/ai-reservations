# INSPECTOR Report: LP28-S1 A Round 2

Input inspected:

- `current-S1/A/round2.json`
- `current-S1/plan/round2_context.md`
- A-side Round 1 material for claim-shrinkage comparison only

Scope: A Round 2 only. `current-S1/B` was not inspected.

## Verdict

PASS with warnings. No blocking dimensional, directional-limit, algebraic, numerical, or circularity error was found in A Round 2.

A has correctly shrunk the target to a preregistered input-side encoder, not validation and not a new mechanism. The strongest remaining risks are protocol/calibration risks: `C_phi` can still collapse to generic interlayer coherence, baseline comparison rules are not fully numeric, and several coefficients are deliberately frozen but still too arbitrary to support strong claims without external calibration or sensitivity analysis.

## Mechanical Validation

No local validation harness was found under `LP28-NickelateLayerDecoupling`.

- `validation/validate.py`: not available
- `validation/quantum.py`: not available
- `validation/schema.md`: not available

Manual Q1-Q6 inspection was therefore performed.

## Q1 Dimensions

Main equation:

`I_phi = E_z2_meV*C_phi/(kB_meV_per_K*T_K + hbarGamma_phi_meV + E_floor_meV)`

Status: pass.

- `E_z2_meV*C_phi`: meV, because `C_phi` is dimensionless.
- `kB*T`: `(meV/K)*K = meV`.
- `hbarGamma_phi_meV`: meV.
- `E_floor_meV`: meV.
- Result: dimensionless.

`C_phi`:

`C_phi = max(0, min(1, W_c_Drude/(W_c_Drude + W_c_incoh + epsilon_W)))`

Status: pass. `W_c_Drude`, `W_c_incoh`, and `epsilon_W` are all declared as `ohm^-1 cm^-2`, so the ratio is dimensionless. The spectral-weight units are internally consistent for a numerical integral of `sigma1_c` in `ohm^-1 cm^-1` over wavenumber in `cm^-1`.

`Gamma_phi` conversion:

Status: pass. The declared conversion `Gamma_phi_ps_inv = Gamma_Drude_cm_minus_1/5.308837` is consistent with angular-rate conversion: `1 cm^-1 = 0.188365 ps^-1`, and multiplying by `hbar = 0.6582119569 meV ps` gives `0.123984 meV` per `cm^-1`.

`E_floor`:

Status: pass. Each term is in meV if `sigma_vac_pct` is percentage points, `sigma_strain_mrad` is mrad, and `lambda_res` is dimensionless.

Warnings:

1. `alpha_z2_meV = 100` is dimensionally valid but still a convention, not a physically calibrated conversion.
2. `epsilon_W = 50 ohm^-1 cm^-2` is dimensionally valid, but its magnitude needs instrument-noise provenance before real evaluation.

## Q2 Directional Limits

Status: pass.

For nonnegative inputs:

- Increasing `E_z2_meV` increases `I_phi`.
- Increasing `C_phi` increases `I_phi`.
- Increasing `T_K`, `Gamma_phi`, or `E_floor` decreases `I_phi`.
- `C_phi -> 0` gives `I_phi -> 0`.
- `Gamma_phi -> 0` gives finite `E_z2*C_phi/(kB*T + E_floor)` because `T=120 K` and `E_floor >= 3 meV`.
- `E_floor -> large` gives `I_phi -> 0`.

Divergence control passes. With fixed `T=120 K`, `kB*T = 10.3407999144 meV`; with `E_floor >= 3 meV`, the denominator lower bound is `13.3407999144 meV` even at zero dephasing.

## Q3 Circularity / Output Leakage

Status: pass with warnings.

A explicitly forbids the correct output-leakage channels:

- `Tc`
- zero resistance
- shielding / Meissner response
- critical current
- Josephson plasma
- superfluid density
- condensate spectral weight
- bulk phase stiffness
- transition-width fits

The 120 K normal-state optical route for `C_phi` is the least-circular route proposed so far. The strongest anti-leakage provisions are fixed spectral windows, fixed temperature, frozen sample list, frozen missing-data rules, output-separated files, and `not_computable` status rather than post hoc substitution.

Warnings:

1. `C_phi` remains the weakest link. Even if output-clean, a normal-state c-axis Drude fraction may be only generic interlayer coherence.
2. Pressure-point inclusion is allowed but must be frozen before output reveal. If pressure choices track known superconducting domes from outside knowledge, this can become indirect leakage.
3. The optical transfer-matrix decomposition needs a preregistered residual tolerance. The report says "instrument tolerance" but does not give a numeric value.
4. Fixed `T=120 K` avoids divergence and output leakage better than flexible temperature choice, but A must ensure all samples are truly normal-state at that temperature under the selected pressure grid.

## Q4 Algebra and Mock Arithmetic

Status: pass.

Independent recalculation of the three mock rows matches the stated values to rounding precision.

Mock A:

- `C_phi = 900/(900+600+50) = 0.5806451613`
- `Gamma = 80/5.308837 = 15.069214 ps^-1`
- `hbarGamma = 9.919 meV`
- `E_floor = max(3, 2*0.8 + 0.7 + 0.25*0.6582119569*8) = 3.616 meV`
- `denominator = 23.876 meV`
- `I_phi = 1.5078`

Mock B:

- Recomputed `I_phi = 0.1868`
- Recomputed denominator `44.0793 meV`

Mock C:

- Recomputed `I_phi = 0.3669`
- Recomputed denominator `42.2921 meV`

Minor numerical note: the embedded `Gamma_phi_ps_inv` values differ at the fourth to sixth decimal place from direct division by `5.308837`. This is harmless rounding, not an algebraic problem.

## Q5 Claim Shrinkage

Status: pass.

Compared with A Round 1, A Round 2 shrinks correctly:

- From possible methodological novelty to "candidate preregistration stack only; no validation claimed."
- From generic measurability to a concrete frozen measurement grid.
- From broad `C_phi` danger warning to a specific normal-state c-axis optical transfer-matrix/Drude audit.
- From mechanism language to protocol language.

No claim inflation detected. A does not claim validation, prediction success, mechanism novelty, or superconductivity evidence from density-wave disappearance.

## Q6 Alternative Baseline-Collapse Handling

Status: pass with warning.

A includes the right baseline-collapse checks:

- `C_phi` only
- `E_z2` only
- disorder only
- denominator only
- total c-axis spectral weight

This directly addresses the main alternative explanations: generic interlayer coherence, orbital weight alone, sample quality/disorder alone, low scattering alone, and total optical weight without coherent/incoherent distinction.

Warning: the evaluation metric is still only exemplary: "e.g. rank correlation or AUROC." Before output reveal, the protocol must freeze the actual metric, uncertainty rule, tie handling, sample inclusion rule, and collapse threshold. Otherwise baseline selection can become another post hoc degree of freedom.

## Q6.4 Alternative Explanation Check

Status: pass for A Round 2, with PI follow-up required.

A explicitly acknowledges the simpler alternatives and provides a baseline-collapse registry. This satisfies the A-side requirement.

PI still needs to turn this into a frozen evaluation rule before any output reveal. INSPECTOR is not judging whether the alternatives are excluded, only whether the protocol recognizes and handles them.

## Q6.5 Landing / Protocol Strength

Status: pass with warnings.

Landing is much stronger than Round 1:

- fixed sample family and pressure grid
- fixed `T=120 K` index temperature
- fixed spectral windows
- fixed units
- frozen missing-data rules
- explicit output blinding
- three-sample mock arithmetic
- forbidden-output list
- baseline-collapse tests

Warnings:

1. This is still a preregistration packet, not a real data landing. No same-sample La3Ni2O7 dataset with all required inputs is identified.
2. The coefficient choices are too arbitrary for strong claims: `alpha_z2=100`, `epsilon_W=50`, `lambda_vac=2`, `lambda_strain=1`, and `lambda_res=0.25` are protocol constants with relevance provenance, not calibrated physical constants.
3. `C_phi` fit pass/fail depends on "preregistered instrument tolerance," but the actual tolerance is absent.
4. Missing-data sensitivity rules are sensible, but a final protocol must state whether sensitivity tables are evaluated with the same metrics as primary `I_phi` or only reported descriptively.

## Overall Decision

PASS with warnings. A Round 2 can be fed forward.

No blocking errors:

- dimensions are consistent
- `Gamma` unit conversion is correct
- `C_phi` spectral-weight units are consistent
- fixed `T=120 K` and `E_floor >= 3 meV` control divergence
- mock arithmetic reproduces the stated `I_phi` values
- output-leakage sources are explicitly forbidden
- claim is appropriately shrunk
- baseline-collapse alternatives are recognized

Warnings to carry forward:

1. Coefficients remain protocol conventions and are too arbitrary for strong inference without external calibration or preregistered sensitivity analysis.
2. `C_phi` may collapse to generic normal-state interlayer coherence.
3. Baseline evaluation metric, uncertainty tolerance, and collapse threshold must be numerically frozen.
4. Transfer-matrix fit residual tolerance must be specified numerically.
5. Same-sample real-data feasibility remains unproven.

--- feed to next round ---

Must correct / blocking-level if unresolved before output reveal:

1. Freeze the exact baseline metric, uncertainty/tie rule, and collapse threshold for `I_phi` versus `C_phi`-only, `E_z2`-only, disorder-only, denominator-only, and total-c-axis-weight baselines.
2. Specify the numerical transfer-matrix/KK residual tolerance and SNR rule used to accept or reject `C_phi`.
3. Declare whether 120 K is guaranteed normal-state for every pressure/sample point; if not, define a pre-output exclusion or `not_computable` rule.

Recommended corrections / warning-level:

1. Add external or sensitivity-based justification for `alpha_z2`, `epsilon_W`, `lambda_vac`, `lambda_strain`, and `lambda_res`.
2. Add a coefficient-sensitivity table showing whether sample ranking survives reasonable coefficient perturbations.
3. Identify at least one real same-sample or matched-sample data route for all required inputs.
4. Keep the claim at preregistered encoder/protocol level unless withheld-output evaluation beats the frozen baselines.

---
