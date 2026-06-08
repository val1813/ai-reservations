# INSPECTOR Report: LP28-S1 A Round 3

Input inspected:

- `current-S1/A/round3.json`
- `current-S1/synthesis/inspector_A_round2.md`

Scope: A Round 3 only. `current-S1/B` was not inspected.

## Verdict

PASS with warnings. No blocking dimensional, directional-limit, algebraic, numerical, circularity, output-leakage, claim-inflation, baseline-collapse-rule, coefficient-sensitivity, or temperature-rule error was found in A Round 3.

A Round 3 is now a preregistered laboratory protocol, not a validation result. It can be fed to PI/Reviewer as a final A-side protocol candidate only if the claim boundary remains: protocol survival/non-survival after withheld-output reveal, with no mechanism, superconductivity prediction, or validation claim from `I_phi` alone.

## Mechanical Validation

No local validation harness was found under `LP28-NickelateLayerDecoupling`.

- `validation/validate.py`: not available
- `validation/quantum.py`: not available
- `validation/schema.md`: not available

Manual inspection was therefore performed.

## Q1 Dimensional Consistency

Status: pass.

Primary equation:

`I_phi = E_z2_meV*C_phi_primary/(kB_meV_per_K*T_K + hbarGamma_phi_meV + E_floor_meV)`

- Numerator: `E_z2_meV*C_phi_primary = meV`.
- Denominator: `kB*T`, `hbarGamma_phi`, and `E_floor` are all `meV`.
- Result: dimensionless.

`C_phi_primary = max(0, min(1, W_c_Drude/(W_c_Drude + W_c_incoh + epsilon_W)))`

- `W_c_Drude`, `W_c_incoh`, and `epsilon_W` are all declared as `ohm^-1 cm^-2`.
- Ratio is dimensionless.
- Clipping preserves dimensional consistency.

`Gamma_phi_ps_inv = Gamma_Drude_cm_minus_1/5.308837` and `hbarGamma_phi_meV = hbar_meV_ps*Gamma_phi_ps_inv`

- Declared conversion is internally consistent: `hbar/5.308837 = 0.123984209 meV per cm^-1`.

`E_floor_meV = max(E_floor_min_meV, lambda_vac*sigma_vac_pct + lambda_strain*sigma_strain_mrad + lambda_res*hbarGamma_res_meV)`

- Dimensionally valid if `sigma_vac_pct` is percentage points, `sigma_strain_mrad` is in mrad, and `lambda_res` is dimensionless.

Warnings:

1. `alpha_z2_meV`, `epsilon_W`, `lambda_vac`, `lambda_strain`, and `lambda_res` remain protocol constants, not physical constants.
2. `epsilon_W = 50 ohm^-1 cm^-2` is dimensionally legal, but real execution needs instrument/noise provenance in the sealed manifest.

## Q2 Direction and Limits

Status: pass.

For nonnegative admissible inputs:

- Increasing `E_z2_meV` increases `I_phi`.
- Increasing `C_phi_primary` increases `I_phi`.
- Increasing `Gamma_phi`, `E_floor`, or fixed-temperature denominator terms decreases `I_phi`.
- `C_phi_primary -> 0` gives `I_phi -> 0`.
- `Gamma_phi -> 0` remains finite because `T=120 K` and `E_floor >= 3 meV`.
- `E_floor -> large` gives `I_phi -> 0`.

Lower denominator bound:

- `kB*T = 0.08617333262*120 = 10.3407999144 meV`
- `denominator_min = 10.3407999144 + 3 = 13.3407999144 meV`

With `E_z2 <= 120 meV` and `C_phi <= 1`, `I_phi <= 8.9949628785`. Divergence is controlled.

## Q3 Algebra and Numerical Test

Status: pass.

Recomputed Round 3 numerical test:

- `C_phi = 0.5806451613`
- `denominator = 10.3407999144 + 9.919 + 3.616 = 23.8757999144 meV`
- `I_phi = 62*0.5806451613/23.8757999144 = 1.5078028853`

This matches the stated expected value `1.5078` and range `[1.50, 1.52]`.

The `Gamma` conversion check also matches:

- `80/5.308837 = 15.069213841 ps^-1`
- `0.6582119569*15.069213841 = 9.918736731 meV`

No coefficient, sign, exponent, or denominator-placement error was detected.

## Q4 Circularity and Output Leakage

Status: pass with warnings.

A Round 3 explicitly forbids the major output-leakage channels from index construction, thresholds, sample inclusion, pressure inclusion, temperature selection, coefficient selection, and baseline selection:

- `Tc`, zero resistance, shielding, Meissner fraction
- critical current, Josephson plasma
- superfluid density, condensate spectral weight, bulk phase stiffness
- transition width and phase-diagram boundary

Anti-leakage improvements over Round 2:

- fixed `120 K` primary temperature
- no temperature substitution
- fixed `C_phi` windows and normal-state gate
- fixed coefficient/sensitivity manifest
- pre-output SHA-256 serialization rules
- auditor recomputation before reveal
- frozen output endpoint and row ledger

Warnings:

1. Pressure-grid and sample-list freezing must be real, not reconstructed from known nickelate dome context.
2. Density-wave disappearance and prior superconducting dome knowledge are correctly excluded from construction, but PI/Reviewer should audit whether they influenced the chosen sample/pressure grid.
3. The protocol depends on separation between input optical files and bulk-output files. Any shared lab notebook field that contains output labels before sealing is leakage.

## Q5 Claim Inflation / Claim Shrinkage

Status: pass.

A Round 3 correctly states:

- no validation claimed
- no mechanism claimed
- no superconductivity prediction claimed
- no claim that `I_phi` is more than a sealed encoder candidate unless it survives frozen post-output checks

No claim inflation was detected. The wording is appropriately weaker than "validated index" and stronger only as a preregistered protocol.

## Q6 Baseline-Collapse Rules

Status: pass.

Round 2 warning is resolved. A now freezes:

- primary endpoint: withheld binary bulk-output label
- primary metric: AUROC with midrank ties
- uncertainty: paired bootstrap, 10000 resamples, seed `280301`
- collapse threshold: fail if any baseline has `AUROC >= AUROC(I_phi)-0.03` or bootstrap interval includes `0`
- tie degeneration: fail if more than 40 percent of computable rows are tied under `I_phi`
- minimum decisive rows: `5`
- small-N rule: `3` or `4` rows can be archived as pilot only, not protocol survival

The baseline list is adequate for the stated weakness:

- `C_phi_primary` only
- `E_z2_meV/120`
- disorder only
- denominator only
- total c-axis spectral weight

No blocker. The rule correctly treats collapse to `C_phi` or total c-axis spectral weight as failure, not a caveat.

Warning: AUROC with very small `N=5` is still fragile even when allowed by rule. This is not a formal contradiction, but the write-up must display exact row labels and bootstrap intervals.

## Q7 Coefficient Sensitivity

Status: pass with warnings.

Round 2 warning is resolved at the protocol level. A defines one-at-a-time and combined stress variants, requires all sensitivity computations before output reveal, and prevents sensitivity results from modifying the primary coefficients.

Pass criteria are explicit:

- every one-at-a-time variant must have Spearman `rho >= 0.80`
- both combined stress variants must have Spearman `rho >= 0.60`
- failure produces `coefficient_fragile`
- `coefficient_fragile` is NO-GO for stable S1 encoder survival

Warnings:

1. With only 3-5 computable rows, Spearman thresholds are coarse and tie-sensitive. The protocol should report exact rank vectors, not only pass/fail.
2. Sensitivity can show rank stability, but not physical calibration of coefficients. This limits claims even if sensitivity passes.

## Q8 Temperature Rule

Status: pass.

Round 3 has a coherent temperature rule:

- primary evaluation is fixed at `120 K`
- `120 K` was selected before output reveal
- no substitution to `80 K`, `150 K`, or other temperatures is allowed
- if `120 K` is output-contaminated or unavailable, the row is `not_computable`
- fewer than 3 computable rows is pre-output NO-GO
- 150 K, 200 K, and 300 K are QC anchors only

No temperature-driven output leakage was detected in the written protocol.

Warning: the normal-state optical gate must be applied before any output reveal. If "independent reason" that a point is superconducting at 120 K comes from bulk output files, that point is contaminated rather than merely `not_computable`.

## Q9 Landing / Baseline-Collapse / Output Rules

Status: pass with warnings.

Landing is now specific enough for a real preregistration attempt:

- required CSV column order
- finite numeric serialization
- missing-value behavior
- hash manifest
- auditor recomputation tolerances
- exact pre-output and post-output NO-GO conditions
- go/no-go table through claim boundary

Warnings:

1. Same-sample or predeclared matched-sample data feasibility remains unproven.
2. The protocol is executable only if raw 120 K c-axis optical spectra, dz2 proxy, dephasing, vacancy, strain, and residual-scattering inputs all exist before output reveal.
3. `C_phi` remains the weakest scientific link because it may be generic interlayer coherence. The protocol handles this by collapse tests, but it does not remove the risk.

## Go / No-Go Table

| Check | Status | Blocker? | Notes |
|---|---:|---:|---|
| Dimensions | PASS | No | `I_phi`, `C_phi`, `Gamma`, and `E_floor` are dimensionally consistent. |
| Direction/limits | PASS | No | Correct monotonicities; denominator bounded. |
| Algebra/numerical test | PASS | No | Recomputed `I_phi = 1.5078028853`. |
| Circularity/output leakage | PASS with warnings | No | Written prohibitions are adequate; execution must enforce file isolation. |
| Claim inflation | PASS | No | Protocol-only claim boundary is explicit. |
| Baseline-collapse rules | PASS | No | Round 2 metric/threshold warning resolved. |
| Coefficient sensitivity | PASS with warnings | No | Rules are frozen; small-N/tie fragility remains. |
| Temperature rule | PASS with warning | No | Fixed 120 K/no substitution rule is coherent. |
| Landing/data feasibility | WARNING | No | No real same-sample dataset identified here. |

## Blockers

None detected in A Round 3 as written.

## Warnings

1. `C_phi_primary` can still reduce to generic normal-state interlayer coherence; collapse against `C_phi` and total c-axis spectral weight must be treated as decisive failure.
2. Coefficients are protocol conventions. Sensitivity testing is necessary but does not physically calibrate them.
3. Small-N AUROC and Spearman decisions are fragile; exact row-level ranks, ties, and bootstrap intervals must be reported.
4. Real execution depends on same-sample or predeclared matched-sample inputs being available before output reveal.
5. Sample/pressure grid selection must be audited for indirect use of known superconducting dome or density-wave context.
6. The normal-state 120 K gate must be based on input-side optical criteria, not bulk output labels.

## Overall Decision

PASS with warnings. A Round 3 is acceptable as a final A-side preregistered protocol candidate. It is not evidence that `I_phi` works; it is an anti-circularity and baseline-collapse-controlled recipe for deciding whether `I_phi` survives a withheld-output test.

--- feed to PI/Reviewer ---

Must correct / blocking-level:

None from INSPECTOR for A Round 3 as written.

Recommended corrections / warning-level:

1. Audit sample and pressure-grid selection for indirect leakage from known superconducting dome, density-wave disappearance, or prior phase-diagram knowledge.
2. Require row-level reporting for AUROC, ties, bootstrap intervals, and every Spearman sensitivity rank vector.
3. Treat `C_phi`-only or total-c-axis-weight survival as the decisive scientific risk: if either baseline collapses the index, abandon or restart S1 rather than retune.
4. Reviewer should verify the cited/data route for real same-sample or predeclared matched-sample 120 K c-axis optical, dz2, dephasing, vacancy, strain, and residual-scattering inputs.
5. Keep final write-up language at preregistered protocol survival/non-survival only; no mechanism, validation, or superconductivity-prediction claim.

---
