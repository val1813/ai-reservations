# INSPECTOR Report: LP28-S1 B Round 2

Input inspected:
- `current-S1/B/round2.json`
- `current-S1/plan/round2_context.md`
- `current-S1/synthesis/inspector_B_round1.md`

Scope constraint: inspected B Round 2 only. Did not inspect `current-S1/A` or any A-round output.

Validation scripts: no local `validation/validate.py`, `validation/quantum.py`, or schema file was found under the project tree. All checks below are manual, with a local float64 recomputation of the mock packet.

## Verdict

Status: PASS WITH WARNINGS.

No blocking dimensional, directional, arithmetic, circularity, or landing-protocol error was found. B Round 2 materially fixes the Round 1 gaps: `E_z2` is now an energy after frozen conversion from normalized spectral weight; `C_phi` has explicit 7x4 rows; row amplitudes are dimensionless; `T_calc_K` is fixed at 80 K; dephasing and missingness rules forbid output leakage; and the mock packet recomputes.

Main warnings:
1. The observability matrix is executable but still partly arbitrary. The row topology and direct/link rows are plausible protocol choices, not derived physics. This must be labeled as a frozen audit design rather than an inferred mechanism.
2. Canonical JSON and decimal emission rules are strong but underspecified enough to cause cross-language hash drift unless the exact serializer and float formatting are frozen.
3. Baseline-collapse handling is good for `S_dz2`, structure/disorder, and `Gamma_phi`, but the mock packet does not demonstrate a c-axis reverse-discordant pair.

## Q1 Dimensions

`I_phi = E_z2_meV * C_phi / (kB_meV_per_K * T_calc_K + hbarGamma_phi_meV + E_floor_meV)`
- Numerator: `meV * dimensionless = meV`.
- Denominator: `meV/K * K + meV + meV = meV`.
- Result: dimensionless. Pass.
- `T_calc_K = 80.0` is fixed and not fitted. Pass.

`E_z2_meV = E_z2_ref_meV * clip(S_dz2_raw / S_dz2_ref, 0, 3)`
- `S_dz2_raw` is a dimensionless normalized spectral weight; `S_dz2_ref` is dimensionless; the ratio is dimensionless.
- Multiplication by `E_z2_ref_meV = 100.0` gives meV.
- The cap is dimensionless before energy conversion and implies `0 <= E_z2_meV <= 300 meV`. Pass.
- Warning: the physical meaning of `E_z2_ref_meV` remains an empirical scale, not a derived orbital splitting. It should be treated as a frozen encoder constant.

`E_floor_meV = 5.0 + 15.0 * D_disorder`
- Correct only if the constants are read as `5.0 meV` and `15.0 meV`; the JSON names and rule imply this. Pass with notation warning: write `5.0 meV + (15.0 meV) D_disorder` in prose/equation form.

`C_phi = sigma_min / (sigma_min + sigma_ref)`
- Rows are dimensionless after normalization, so singular values and `sigma_ref=0.2` are dimensionless.
- Result is dimensionless and bounded `0 <= C_phi < 1`. Pass.

Transcendental functions: none requiring dimensionless arguments.

## Q2 Directional Limits

`I_phi` limits:
- `hbarGamma_phi_meV -> infinity`: denominator diverges, `I_phi -> 0`. Direction matches dephasing penalty.
- `D_disorder` increases: `E_floor_meV` increases, denominator increases, `I_phi` decreases. Direction matches disorder penalty.
- `S_dz2_raw` increases below the cap: `E_z2_meV` increases and `a_dz2` weakly increases; `I_phi` nondecreases, all else fixed. Direction matches availability.
- `S_dz2_raw / S_dz2_ref >= 3`: `E_z2_meV` saturates at 300 meV, while `a_dz2` continues saturating toward 1 through `u/(1+u)`. No divergence.

`C_phi` limits:
- `sigma_min -> 0`: `C_phi -> 0`. Direction matches zero observability.
- `sigma_min -> infinity`: `C_phi -> 1`. Direction and bound pass.
- Any mandatory amplitude exactly zero can drive rank loss in the declared matrix; the JSON also requires missingness flags rather than output-tuned replacement. Pass.

No sign reversal or numerator/denominator inversion found.

## Q3 Circularity / Output Leakage

Pass with protocol dependency.

Strong anti-leakage elements:
- Explicit forbidden outputs include `Tc`, zero resistance, Meissner/shielding, critical current, Josephson plasma, bulk superfluid density, bulk phase stiffness, transition-width fits, and post-output thresholds.
- `Gamma_phi` allowed sources are normal-state input-side spectroscopy/dephasing windows; forbidden sources include transition width, below-transition stiffness, Josephson plasma, and critical-current hysteresis.
- Missing-data alternatives must be sealed in P0 and cannot be selected because they improve output correlation.
- Auditor recomputation disallows output files and A-round outputs.

Residual risks:
- "Normal-state" must be operationally above any superconducting output unblinding, not merely above an assumed transition. If a sample's transition is unknown, the acquisition temperature/window must be sealed before labels.
- Structural bridge score `B_struct` is allowed but its exact formula is deferred to P0. If P0 chooses geometry terms after seeing outputs, leakage returns.
- Baseline-collapse comparisons are pre-output against `I_phi`, which is correct for triviality checks, but any later interpretation against superconductivity must remain separate.

## Q4 Numerical / Mock Recalculation

Recomputed in float64 using the declared equations and 7x4 matrix.

`LP28-MOCK-001`
- `sigma_min = 0.5640122467`, `C_phi = 0.7382240915`, `denominator = 32.8938666096 meV`, `I_phi = 2.8053257627`.
- Matches stated values within about `5e-11`.

`LP28-MOCK-002`
- `sigma_min = 0.3274259361`, `C_phi = 0.6207998388`, `denominator = 63.6438666096 meV`, `I_phi = 1.9508551943`.
- Matches stated values within about `5e-11`.

`LP28-MOCK-003`
- `sigma_min = 0.4706930814`, `C_phi = 0.7018010092`, `denominator = 26.1438666096 meV`, `I_phi = 2.0132858111`.
- Matches stated values within about `5e-11`.

Mock ranking: `001 > 003 > 002` by `I_phi`. This supports the intended anti-collapse example that the highest `S_dz2_raw` row is not highest `I_phi`.

No >3-order numerical mismatch found.

## Q5 Algebra And Matrix Definition

Algebraic checks:
- Row amplitude maps `u/(1+u)` and `Gamma_ref/(Gamma_ref + hbarGamma_phi)` are dimensionless and bounded.
- Link rows with `1/sqrt(2)` preserve dimensionless units and do not introduce scale blow-up.
- SVD convention is explicit: 7x4 real matrix, IEEE-754 float64, singular values descending, fourth value as `sigma_min`.
- `C_phi` saturation formula is monotone and nonsingular.

Warning: the observability matrix is arbitrary in the technical sense. The selected rows encode direct channels plus nearest-neighbor link contrasts, but no derivation shows that these seven rows are uniquely implied by nickelate layer physics or measurement theory. This does not block the protocol because B claims an auditor-recomputable input encoder, not a validated mechanism. It must not be upgraded later to a physical proof without independent justification.

## Q6.3 Claim Shrinkage

No harmful shrinkage detected.

Compared with B Round 1, the claim remains intentionally narrow:
- Round 1: `I_phi` is a non-circular frozen encoder candidate, not validated.
- Round 2: `C_phi` is executable as a frozen dimensionless observability score, still not a superconducting mechanism and not validated here.

This is clarification and implementation, not retreat from a stronger validated claim. No score penalty recommended.

## Q6.4 Alternative Baseline-Collapse Handling

Pass with warnings.

B explicitly includes single-variable baselines:
- `S_dz2_raw / S_dz2_ref`
- `W_caxis_raw / W_caxis_ref`
- `B_struct / (1 + D_disorder)`
- `1 / (1 + hbarGamma_phi_meV / Gamma_ref_meV)`

It also defines collapse as a protocol failure mode if real sealed inputs make `I_phi` rank-identical to a baseline. This is the correct handling: baseline noncollapse is not validation, but collapse is a triviality failure.

Warning: the mock packet demonstrates reverse-discordance for `S_dz2`, structure/disorder, and `Gamma_phi`, but not for c-axis weight. The JSON itself admits D2 is not supplied by the mock. Next round should add one mock or real sealed pair with higher `W_caxis_raw` but lower `I_phi`, or downgrade D2 from demonstrated to required-in-real-data.

## Q6.5 Landing / Protocol Strength

Landing strength: adequate for Round 2 protocol, not yet experimental evidence.

Pass elements:
- Required deposited artifacts are concrete: P0 encoder, raw input CSV, metadata JSON, label CSV, baseline scores, encoder code, manifest.
- Hash and timestamp requirements are present.
- Auditor recomputation inputs and disallowed inputs are clear.
- Numeric tolerance is explicit: absolute error `<= 5e-10` for key float labels.
- Missingness, censored values, and alternatives are specified before unblinding.

Warnings:
- Canonicalization needs one more level of precision. "Decimal numbers emitted with the frozen precision stated in P0" is not enough unless P0 also fixes float-to-decimal mode, treatment of `-0`, `NaN`/null prohibition, CSV dialect, line endings for CSV, column order, and whether numbers are serialized as JSON numbers or strings.
- `timestamp_source` is acceptable, but "repository host or signed lab notebook clock" should specify a single authority for the final deposit to avoid conflicting manifest times.
- The deposited artifact paths under `current-S1/B/deposit/` are protocol paths only; no actual deposit is inspected in this round.

## Final Judgment

PASS WITH WARNINGS.

No blocking correction is required before feeding B Round 2 forward, provided downstream synthesis preserves the non-validation status and does not convert this encoder into a physics mechanism claim.

--- Feed To Next Round ---

Must fix / blocking-level if upgraded to validation or mechanism:
1. Do not treat `C_phi` as physically derived. It is a frozen observability audit matrix unless an independent derivation/ablation justifies the row topology.
2. Do not allow `B_struct`, replacement channels, frequency windows, or missing-data handling to be selected after seeing superconducting outputs.
3. Do not claim hash reproducibility until P0 freezes exact JSON/CSV serializers, numeric formatting, column order, `null` handling, and timestamp authority.

Recommended fixes / warning-level:
1. Add a c-axis reverse-discordant mock or sealed real pair for D2, or mark D2 as required but not demonstrated by the current mock.
2. Rewrite `E_floor_meV = 5.0 + 15.0 * D_disorder` with explicit meV units on both constants.
3. Label `E_z2_ref_meV = 100 meV` as an empirical encoder scale, not a measured orbital energy, unless literature-backed calibration is added.
4. Keep `T_calc_K = 80 K` fixed in all recomputation artifacts; changing it after output inspection would be leakage.

---
