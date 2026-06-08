# INSPECTOR Report: LP28-S1 B Round 3

Input inspected:
- `current-S1/B/round3.json`
- `current-S1/synthesis/inspector_B_round2.md`

Scope constraint: inspected B Round 3 only. Did not inspect `current-S1/A` or any A-round output.

Validation scripts: no local `validation/validate.py`, `validation/quantum.py`, or schema file was found under the project tree. All checks below are manual protocol/algebra checks.

## Verdict

Status: PASS WITH BLOCKERS TO FIX BEFORE P0/GO, otherwise strong protocol.

B Round 3 fixes most Round 2 warnings: canonical JSON/CSV rules are now concrete, JSON numeric values are string-only, negative zero/NaN/infinity are forbidden, timestamp authority is single-source, manifest construction is specified, auditor recomputation has tolerances, and baseline-collapse plus anti-arbitrariness kill rules are explicit.

No dimensional, sign, output-leakage, or physics-claim inflation blocker was found. The remaining blockers are protocol executability gaps: the auditor must be allowed to read deposited labels/scores for byte-for-byte comparison, and the GO rule must not allow an underpowered sample set to pass as noncollapse.

## Blockers

1. Auditor recomputation input list is internally incomplete.
   - `auditor_recomputation_protocol.allowed_inputs` lists only `P0_encoder.json`, `X_pre_raw.csv`, `X_pre_metadata.json`, `encoder_code.py`, and `manifest.sha256.json`.
   - The recomputation steps require comparing emitted `I_phi_labels.csv` and `baseline_scores.csv` to deposited labels byte-for-byte, but those deposited comparison artifacts are not in the allowed readable set.
   - Fix: split `allowed_compute_inputs` from `allowed_comparison_artifacts`, or add `deposit/I_phi_labels.csv` and `deposit/baseline_scores.csv` as readable comparison-only artifacts. They must be hashed before unblinding and must not be used to compute labels.

2. Baseline-collapse GO rule has an underpowered-sample escape.
   - The metric says if `n_complete < 6`, testing is underpowered and S1 cannot claim noncollapse.
   - The GO conditions only require `baseline-collapse fatal_rule is false`; with `n_complete < 6`, a packet could avoid fatal collapse and still reach `GO_PROTOCOL_ONLY`.
   - Fix: add `n_complete >= 6` as a required GO condition for any nontrivial-encoder claim, or define a separate verdict such as `NO_GO_BASELINE_UNDERPOWERED` / `AUDIT_INCOMPLETE_NONCOLLAPSE`.

## Warnings

1. Anti-arbitrariness constants are not fully named in the frozen constants block.
   - The sensitivity grid tests `E_floor_intercept_meV` and `E_floor_slope_meV`, but the frozen constants list only encodes them inside `E_floor_rule`.
   - Fix: add explicit constants `E_floor_intercept_meV = "5.0"` and `E_floor_slope_meV = "15.0"` so the grid is machine-addressable.

2. `C_phi` monotonic direction is not proven.
   - Dimensions and bounds pass, but the 7x4 SVD matrix includes contrast rows. It is not algebraically guaranteed in the artifact that every individual channel increase monotonically increases `sigma_min`.
   - This is acceptable because B frames `C_phi` as a frozen audit observability score, not a physical mechanism. Do not later claim monotonic physical causality without a separate proof or exhaustive sealed sensitivity check.

3. Manifest self-hash rule is usable but needs auditor wording precision.
   - The field `manifest_sha256_excluding_self_hash` should be verified by zeroing that field to 64 zeros and hashing the canonical bytes. It is not the SHA-256 of the final manifest bytes.
   - Fix: state this explicitly in auditor steps to avoid false hash mismatch reports.

4. `T_prior_upper_K` provenance remains a leakage-sensitive metadata field.
   - The rule is input-side if the value comes from pre-existing literature or pre-output instrument planning.
   - Fix: require a metadata citation or lab-notebook timestamp for each `T_prior_upper_K`; post-output same-sample transition knowledge must mark the sample `input_contaminated`.

5. Sensitivity-grid output obligations are not fully enumerated.
   - The protocol defines thresholds but does not name the required deposited artifact for all variant ranks and collapse outcomes.
   - Fix: add a canonical `sensitivity_grid_results.csv` or JSON artifact with primary rank, variant id, Kendall tau-b, pair-reversal fraction, collapse verdict, and variant inclusion status.

## Q1 Dimensions

`I_phi = E_z2_meV * C_phi / (kB_meV_per_K * T_calc_K + hbarGamma_phi_meV + E_floor_meV)`
- Numerator: `meV * dimensionless = meV`.
- Denominator: `meV/K * K + meV + meV = meV`.
- Result: dimensionless. Pass.

`E_z2_meV = E_z2_ref_meV * min(max(S_dz2_raw / S_dz2_ref, 0.0), 3.0)`
- Ratio is dimensionless; multiplication by `E_z2_ref_meV` gives meV. Pass.

`E_floor_meV = 5.0 meV + (15.0 meV) * D_disorder`
- Pass after Round 3's explicit unit annotation.

`C_phi = sigma_min / (sigma_min + sigma_ref)`
- Matrix rows and singular values are dimensionless; `sigma_ref` is dimensionless; result is dimensionless and bounded. Pass.

Transcendental functions: only `sqrt(2)` appears and is dimensionless. Pass.

## Q2 Direction And Limits

Pass with monotonicity warning above.

- `hbarGamma_phi_meV -> infinity`: denominator diverges and `a_phi_clean -> 0`; `I_phi` tends toward zero or rank-loss suppression. Direction matches dephasing penalty.
- `D_disorder` increases: `E_floor_meV` increases, so `I_phi` decreases for fixed `E_z2` and `C_phi`.
- `sigma_min -> 0`: `C_phi -> 0`; `sigma_min -> infinity`: `C_phi -> 1`.
- `S_dz2_raw / S_dz2_ref >= 3`: `E_z2_meV` saturates at `300 meV`; no divergence.

No numerator/denominator reversal or sign loss found.

## Q3 Circularity / Output Leakage

Pass.

Round 3 explicitly forbids `Tc`, resistance-transition features, Meissner/shielding, critical current, Josephson plasma, bulk superfluid density, bulk phase stiffness, phase diagrams, and post-output human threshold choices from defining or tuning `I_phi`.

The primary protocol also prevents leakage by freezing canonical artifacts before output unblinding, disallowing current-S1/A paths for B auditing, keeping `C_phi` as an audit score, and killing S1 if any forbidden output changes constants, windows, inclusion rules, missing-data handling, row topology, or encoder replacement.

Residual leakage risk is operational rather than algebraic: `T_acq_K`, `T_prior_upper_K`, and `B_struct` must be sealed with provenance before same-sample output labels are opened.

## Q4 Algebra / Numerical Definitions

Pass with warnings.

Algebraic definitions are executable:
- Row amplitudes are dimensionless.
- SVD shape and precision are fixed: 7x4 real matrix, IEEE-754 binary64, LAPACK-compatible SVD, descending singular values, fourth value as `sigma_min`.
- Label formatting is fixed to 10 digits after the decimal point with round-half-to-even.
- Ties and tolerances are explicit.

No concrete sample packet is included in Round 3, so no numerical label recomputation was possible in this inspection.

## Q5 Canonicalization / Hash Rules

Pass with warning.

Canonical JSON and CSV rules are now strong enough for cross-language reproduction if implemented literally:
- UTF-8 without BOM.
- LF line endings and final LF.
- sorted JSON object keys.
- no JSON number tokens in hashed JSON.
- decimal strings only; no scientific notation, NaN, infinity, or negative zero.
- deterministic CSV header, row order, missing literal, quoting, and decimal formatting.

The only remaining precision issue is manifest self-hash wording, listed as a warning.

## Q6 Baseline Collapse

Protocol concept passes; GO logic has blocker #2.

The baseline set covers dz2-only, c-axis-only, structure/disorder-only, dephasing-only, and product-without-SVD comparators. The fatal rules are appropriately adversarial:
- exact rank identity is always fatal.
- near collapse is fatal unless P0 already names auditor-verifiable discordant pairs.
- noncollapse is not treated as validation.

The underpowered case must be converted into a formal no-go/incomplete condition before PI can issue `GO_PROTOCOL_ONLY`.

## Q7 Anti-Arbitrariness

Pass with warnings.

The frozen grid covers multiplicative constants, `T_calc_K`, and row-topology variants; variants are run before output unblinding; no variant may become primary because it improves output agreement. Fatal thresholds for rank fragility, noncollapse fragility, and temperature fragility are explicit.

Warnings:
- machine-readable names for the two floor constants are missing from the constants block.
- deposit format for the full grid results should be specified.

## Q8 Claim Inflation / Alternative Explanation

Pass.

B Round 3 correctly restricts S1 to a frozen input-side encoder protocol. It does not claim that `I_phi` predicts superconductivity, explains nickelate pairing, validates interlayer coherence, or proves a physical mechanism. It also permits simpler Drude-like channels only as baselines, not as post-output replacements.

## Q9 Go / No-Go Kill Rules

Pass after blocker fixes.

The kill rules are strong and correctly include output leakage, missing or mismatched artifacts, recomputation failure, normal-state contamination, baseline collapse, arbitrary sensitivity behavior, mechanism overclaiming, output-only survival, and replacing the primary encoder because a baseline performs better against outputs.

The PI should not issue `GO_PROTOCOL_ONLY` until the two blockers are patched in the protocol text.

--- Feed To PI / Reviewer ---

Must fix / blocking-level:
1. Split auditor inputs into compute-only inputs and comparison artifacts, or explicitly allow reading hashed `I_phi_labels.csv` and `baseline_scores.csv` for byte-for-byte comparison.
2. Add an underpowered-baseline verdict or GO condition: `n_complete >= 6` is required for any nontrivial-encoder/noncollapse claim.

Recommended fixes / warning-level:
1. Add explicit frozen constants `E_floor_intercept_meV` and `E_floor_slope_meV`.
2. Add a canonical sensitivity-grid results artifact and required columns.
3. State manifest self-hash verification as "zero self-hash field, canonicalize, hash, then compare to field."
4. Require timestamped/cited provenance for every `T_prior_upper_K`.
5. Keep `C_phi` labeled as an audit observability score; do not upgrade it to a physical mechanism or monotonic causal quantity without separate proof.

Concise verdict: B Round 3 is a strong final zero-leakage protocol draft but is NO-GO for final P0 until the auditor-readable comparison artifacts and underpowered-baseline GO rule are fixed.
