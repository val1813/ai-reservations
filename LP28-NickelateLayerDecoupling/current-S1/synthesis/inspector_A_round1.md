# INSPECTOR Report: LP28-S1 A Round 1

Input inspected:

- `current-S1/A/round1.json`
- `current-S1/plan/研究计划.md`
- `current-S1/plan/本轮已知错误.md`

Scope: A Round 1 only. `current-S1/B` was not inspected.

## Verdict

PASS with warnings. No blocking dimensional, algebraic, limit-direction, or circularity error was found in A Round 1 that would invalidate the round. The output is correctly shrunk to a narrow methodological claim: an input-side preregistration protocol may be novel, while the physical mechanisms are prior-art-heavy.

Primary warnings are protocol strength and operational specificity: A identifies the right leakage risks, but the candidate protocol still lacks fixed numerical windows, coefficient provenance, same-sample feasibility constraints, and a concrete landing calculation.

## Mechanical Validation

No local validation harness was found under `LP28-NickelateLayerDecoupling`:

- `validation/validate.py`: not available
- `validation/quantum.py`: not available
- `validation/schema.md`: not available
- `round1_claims.json`: not available separately from `round1.json`

Manual Q1-Q6 inspection was therefore performed.

## Q1 Dimensions

Main working equation:

`I_phi = E_z2*C_phi/(kB*T + hbar*Gamma_phi + E_floor)`

Status: pass, conditional on declared variable units.

- Numerator has units of energy if `E_z2` is energy and `C_phi` is dimensionless.
- Denominator has units of energy if `T` is temperature, `Gamma_phi` is angular-frequency or rate, and `E_floor` is energy.
- Result is dimensionless.

Warnings:

1. `E_z2_proxy = alpha_z2*Integral(A_z2(omega), (omega, omega1, omega2))` is dimensionally under-specified. If `A_z2` is a normalized spectral function with units `1/energy`, the integral is dimensionless and `alpha_z2` must have units of energy. If `A_z2` is arbitrary experimental intensity, `alpha_z2` must include the full calibration to energy and must not be fitted on superconducting output.
2. `C_phi_allowed_example = W_c_Drude/(W_c_Drude + W_c_incoh + epsilon)` is dimensionless only if `epsilon` has the same units as spectral weight. It should be renamed or defined as `epsilon_W`, not an abstract small number.
3. `E_floor_example` is dimensionally valid only if `lambda_vac` and `lambda_strain` are energy coefficients for their corresponding disorder/strain metrics, and `lambda_res` is dimensionless.

## Q2 Directional Limits

Status: pass.

For nonnegative variables:

- `E_z2` increases -> `I_phi` increases.
- `C_phi` increases -> `I_phi` increases.
- `T`, `Gamma_phi`, or `E_floor` increases -> `I_phi` decreases.
- `C_phi -> 0` gives `I_phi -> 0`.
- `Gamma_phi -> 0` gives finite `E_z2*C_phi/(kB*T + E_floor)` if `T` or `E_floor` is nonzero.
- `E_floor -> large` gives `I_phi -> 0`.

Warnings:

1. The low-temperature, low-disorder, low-dephasing limit can diverge if `T -> 0`, `Gamma_phi -> 0`, and `E_floor -> 0`. A flags this correctly, but the next round must impose a nonzero measurement temperature, nonzero floor, or bounded transform.
2. The protocol must explicitly constrain `E_floor >= 0`, `Gamma_phi >= 0`, `C_phi in [0,1]` or another bounded range. Without these constraints the directional interpretation can fail.

## Q3 Circularity

Status: pass with major warning.

A correctly identifies `C_phi` and `E_floor` as the main circularity bottlenecks and explicitly forbids output-side observables such as Josephson plasma, superfluid density, Meissner screening, zero resistance, critical current, and bulk phase stiffness.

Remaining leakage risks:

1. `C_phi` from normal-state c-axis Drude weight can still leak if the temperature window is chosen after seeing superconducting behavior, if fluctuation conductivity is included, or if decomposition choices are tuned against phase labels.
2. `E_z2` can leak through spectral-window choice, orbital-projection rules, or background subtraction chosen after phase-boundary inspection.
3. `Gamma_phi` can leak if extracted from superconducting fluctuation fits or transition broadening rather than normal-state linewidths.
4. `E_floor` can leak if coefficients are tuned to repair false positives or false negatives.
5. Sample inclusion/exclusion can become an implicit output-side threshold if failed samples are removed after bulk output is known.

No circularity block is issued because A explicitly marks these as fatal risks rather than using them as validated inputs.

## Q4 Algebra, Limits, Numerical Sanity

Status: pass for algebraic form; warning for missing numerical landing.

Algebra:

- The main index is a simple positive ratio and has no detected sign inversion or denominator/numerator swap.
- The proposed `C_phi` ratio is bounded between 0 and 1 if all spectral weights and stabilizer are nonnegative.
- The leakage rule `I_phi_train = f(X_input; theta_fixed)` is schematic, not a physics equation; no algebraic error is present.

Limits:

- The listed limits are consistent with the proposed interpretation.
- The invalid limit `theta_fixed -> fit_to_output` is conceptually correct as a protocol-failure condition.

Numerical sanity:

- A provides no concrete numerical substitution for `E_z2`, `C_phi`, `Gamma_phi`, `E_floor`, or a sample-level `I_phi`.
- Therefore no order-of-magnitude check can be completed.
- This is not a Round 1 block, but it is a required next-round item if the project continues.

## Q5 Claim Shrinkage

Status: pass.

A explicitly shrinks the claim:

- Not novel: interlayer coherence, `dz2`/apical-O/bilayer coupling, c-axis optical weight, density-wave competition, oxygen-vacancy disorder, and pressure/structure tuning.
- Possible novelty: leakage-controlled preregistered input-side protocol.
- Not validated: `I_phi` is called a working/candidate index, not a proven predictor.

This complies with known constraints:

- Does not call `I_phi` validated.
- Does not use correlation with `Tc` as proof.
- Does not claim interlayer coherence or `dz2-pz-dz2` hybridization as novelty.
- Does not use DW disappearance as sufficient evidence for bulk superconductivity.

## Q6 Alternative Explanations

Status: pass with warning.

A names the main alternative explanations and confounders:

- generic interlayer coherence prior art
- density-wave competition
- structural transitions
- oxygen vacancies/disorder
- pressure and apical oxygen control
- sample inhomogeneity and phase purity

Warning: A does not yet give exclusion tests that would distinguish `I_phi` from simpler alternatives such as "normal-state c-axis coherence alone predicts output" or "oxygen/strain disorder alone explains success/failure." Next round should include at least two baseline models:

1. `C_phi`-only or c-axis Drude fraction only.
2. Disorder/structure-only model using `E_floor` inputs.

`I_phi` should survive only if it beats these baselines on a withheld output comparison under the preregistered rule.

## Q6.3 Claim Shrinkage Versus Prior Round

Round 1 has no prior A round for comparison. No shrinkage penalty applied.

## Q6.4 Alternative Explanation Check

Status: warning, not block.

A discusses alternatives in the agent output itself. However, the protocol has not yet forced a PI-level answer to:

- whether simpler explanations can explain the same data without `I_phi`
- why those alternatives are excluded

Feed this warning into the next PI/A prompt.

## Q6.5 Landing Calculation / Protocol Strength

Status: pass as a Round 1 blueprint; warning for weak landing.

A does not merely assert "no prior-art blank." It gives a concrete protocol blueprint: freeze formulas and thresholds, measure structure/spectroscopy/dephasing inputs, timestamp `I_phi`, then reveal bulk outputs only for evaluation.

However, the landing remains under-specified:

- no named same-sample dataset
- no fixed spectral windows
- no exact pressure/temperature grid
- no coefficient source for `alpha_z2`, `lambda_vac`, `lambda_strain`, or `lambda_res`
- no missing-data rule beyond a generic preregistration instruction
- no concrete sample-level calculation
- no explicit blinding procedure for output files

This is acceptable for A Round 1 but must be strengthened in Round 2. If Round 2 still cannot specify at least one calculable route for all four variables without output leakage, S1 should be considered blocked or downgraded.

## Overall Decision

PASS with warnings. A Round 1 can be fed forward.

No blocking errors:

- no fatal dimensional mismatch in the main equation
- no detected directional-limit reversal
- no algebraic sign or ratio error
- no unacknowledged claim inflation
- no output-side observable used as a validated input

Warnings to carry forward:

1. `E_z2_proxy` and `C_phi` examples need exact unit conventions and stabilizer units.
2. The low-temperature/no-floor limit must be bounded by protocol.
3. `C_phi` remains the weakest circularity point.
4. No numerical landing calculation was supplied.
5. Alternative explanations need explicit baseline tests.
6. Protocol must become operational: fixed windows, temperature/pressure grid, coefficient provenance, missing-data rules, and blinding.

--- feed to next round ---

Must correct / blocking-level if unresolved by next round:

1. Define all units and bounds: `E_z2`, `C_phi`, `Gamma_phi`, `E_floor`, `epsilon_W`, and all lambda/alpha coefficients. Keep `E_floor >= 0`, `Gamma_phi >= 0`, and bound `C_phi`.
2. Prevent divergence in the `T -> 0`, `Gamma_phi -> 0`, `E_floor -> 0` limit with a fixed nonzero measurement temperature, fixed floor, or bounded transform.
3. Specify at least one complete, calculable same-sample route for `E_z2`, `C_phi`, `Gamma_phi`, and `E_floor` that does not use `Tc`, zero resistance, shielding, Meissner response, critical current, phase stiffness, Josephson plasma, superfluid density, or condensate spectral weight.

Recommended corrections / warning-level:

1. Provide one sample-level numerical mock calculation or real-data calculation for `I_phi`.
2. Freeze spectral windows, pressure/temperature grid, decomposition method, background subtraction, missing-data rules, and coefficient provenance.
3. Add simpler baseline alternatives: c-axis coherence only, disorder/structure only, and optionally `E_z2` only.
4. Add an explicit output-blinding/timestamping protocol.
5. Treat all mechanism novelty claims as closed; only the leakage-controlled preregistration protocol remains potentially novel.

---
