# INSPECTOR Report: LP28-S1 B Round 1

Input inspected:
- `current-S1/B/round1.json`
- `current-S1/plan/研究计划.md`
- `current-S1/plan/本轮已知错误.md`

Scope constraint: inspected B Round 1 only. Did not inspect current-S1/A.

Validation scripts: no local `validation/validate.py`, `validation/quantum.py`, or schema file was found under `LP28-NickelateLayerDecoupling/current-S1` or the project tree. All checks below are manual.

## Verdict

Status: PASS WITH WARNINGS.

No blocking dimensional, directional, algebraic, or circularity error was found in B Round 1, provided the stated assumptions are enforced: `E_z2`, `kBT`, `hbar*Gphi`, and `Efloor` must be energy scales; `C_phi` and F3 singular values must be dimensionless after frozen normalization; all codebook choices must be sealed before bulk superconducting outputs are opened.

Main warning: the output is protocol-strong but landing-weak. It gives a credible non-circular audit criterion, but it does not yet specify the actual transfer-matrix rows, normalization constants, missing-data rules, sample packet, or exact deposited artifacts needed for an auditor to rerun the calculation.

## Q1 Dimensions

F1: `I_phi = Ez2*Cphi/(kBT + hbar*Gphi + Efloor)`
- Required units: `Ez2`, `kBT`, `hbar*Gphi`, and `Efloor` must all be energies; `Cphi` dimensionless.
- Result: dimensionless if and only if `Ez2` is operationalized as an energy scale or a fixed-normalized dimensionless spectral proxy multiplied by an energy scale.
- Warning: B describes `Ez2` as "spectral-weight or energy proxy". A raw spectral weight is not automatically an energy. Round 2 must choose one convention and freeze it.
- Transcendental functions: none.

F2: `Ifrozen - Irecomputed`
- Dimensionless if both labels are dimensionless.
- Pass condition requires exact equality. This is acceptable for labels/hashes/discrete bins, but if labels are floating-point values the protocol must define canonical rounding, serialization, and tolerance.

F3: `C_phi = sigma_min/(sigma_min + sigma_ref)`
- Dimensionless if `sigma_min` and `sigma_ref` have identical units. B states the transfer matrix is fixed-normalized, so this passes as a dimensionless stability score.
- Warning: if the transfer matrix rows mix unlike observables without pre-registered normalization, `sigma_min` is not interpretable.

## Q2 Directional Limits

F1:
- `Gphi -> infinity`: denominator diverges, `I_phi -> 0`; matches claim that dephasing destroys readiness.
- Increasing `Ez2` increases `I_phi`, holding other variables fixed.
- Increasing `Cphi` increases `I_phi`, holding other variables fixed.
- Increasing `kBT`, `Gphi`, or `Efloor` decreases `I_phi`, holding other variables fixed.
- No sign reversal found.

F3:
- `sigma_min -> 0`: `C_phi -> 0`; matches unobservable-channel limit.
- `sigma_min -> infinity`: `C_phi -> 1`; bounded and monotone.
- Increasing `sigma_ref` lowers `C_phi`; this is sensible if `sigma_ref` is a fixed regularizing reference.

## Q3 Circularity

Pass with protocol dependency.

B's core claim is explicitly noninterference: changing sealed bulk output `Y` while holding `X_pre` and `P0` fixed must not change `I_phi`, thresholds, inclusion rules, windows, normalization, or hyperparameters. This directly addresses circularity and is aligned with the plan's hard failure conditions.

Residual circularity risks that must be carried forward:
- `Gamma_phi` can become output-contaminated if inferred from superconducting transition width, phase stiffness, or below-transition behavior.
- `C_phi` can become output-contaminated if it includes Josephson-like bulk phase stiffness or any variable selected because it tracks `Tc`.
- Sample exclusion, frequency windows, and missing-data rules must be frozen before unblinding; otherwise F2 only audits reproducibility, not independence.

## Q4 Numerical Sanity

F1 numerical test:
- Substitutions: `Ez2=20`, `Cphi=0.4`, `kBT=5`, `hbar=1`, `Gphi=10`, `Efloor=5`.
- Calculation: numerator `20*0.4 = 8`; denominator `5 + 1*10 + 5 = 20`; result `0.4`.
- Expected range: `[0.1, 1.0]`.
- Pass.

Order-of-magnitude concern:
- No extreme `10^N` vs `10^M` mismatch appears in B Round 1.
- However, the numeric example is only an internal consistency check. It is not tied to sourced nickelate measurement ranges and must not be treated as validation.

## Q5 Algebra And Limits

F1 algebra is simple ratio form. No coefficient/sign error found.

F2 algebra is a residual. Pass criterion should be `0` or bitwise-identical labels. Warning: floating-point recomputation needs canonicalization.

F3 algebra is a bounded saturation map. The limiting behavior is correct and avoids singular blow-up.

No matrix derivation for the observability transfer matrix is provided, so the algebra of `sigma_min` itself cannot be audited yet. This is a warning, not a blocker for Round 1, because B explicitly makes this the Round 2 task.

## Q6.3 Claim Shrinkage

No previous B round exists for comparison. Against the research plan and known-errors file, B does not overclaim:
- It does not call `I_phi` validated.
- It does not use correlation with `Tc` as proof.
- It explicitly forbids output-side thresholding.
- It does not claim `dz2-pz-dz2` hybridization or interlayer coherence as novelty.

No shrinkage penalty applies in Round 1. The claim is already narrowed to "auditable preregistration candidate / non-circular encoder," not a validated predictor.

## Q6.4 Alternative Explanations

Pass with warning.

B identifies the main simpler alternative: `I_phi` may collapse to a monotone relabeling of `dz2` weight or c-axis coherence already known in the literature. It also states this as a physics-fail condition.

Warning: B does not yet give a decisive exclusion test. Round 2 must include at least one comparison against simpler baselines:
- monotone `S_dz2` only,
- c-axis optical spectral weight only,
- ordinary disorder/scattering proxy only,
- known structural metric only.

The proposed "lower dz2 but higher C_phi/lower Gamma_phi outranks higher dz2" prediction is a useful anti-collapse test, but it needs concrete sample pairs or simulated preregistered rows.

## Q6.5 Landing Calculation / Protocol Strength

Protocol strength: good.
- B gives a clear protocol pass/fail rule: deposit `P0`, raw `X_pre`, missing-data rules, and `I_phi` labels before opening `Tc`, shielding, zero resistance, `Jc`, or bulk phase stiffness.
- The blind-auditor recomputation criterion is strong and directly testable.

Landing strength: weak / half-finished.
- No concrete landing A/B/C packet is provided.
- No specific sample set, frequency windows, normalization constants, threshold values, transfer-matrix rows, or deposited file schema is specified.
- The current numerical example is a toy internal check, not a landing calculation tied to known material measurements.

This is not a blocker because B Round 1 frames the object as an auditable candidate and assigns Round 2 to specify the transfer matrix and preregistration packet. It must become concrete in the next round.

## Final Judgment

PASS WITH WARNINGS.

No blocking error found. Continue to next round, but B Round 2 must convert the protocol into a runnable preregistration object and close the ambiguity in `E_z2`, `C_phi`, and `Gamma_phi`.

--- Feed To Next Round ---

Must fix / blocking-level if still unresolved after next B round:
1. Define `E_z2` units exactly. If it is raw spectral weight, add a frozen normalization or energy conversion; if it is an energy proxy, specify the measurement and energy scale.
2. Define `C_phi` as an explicit transfer matrix: rows, columns, units, row normalization, `sigma_ref`, missing-data handling, and singular-value convention.
3. Keep `Gamma_phi` strictly input-side. It must not use superconducting transition width, phase stiffness, or below-output information.
4. Specify exact anti-leakage artifacts: deposited `P0`, raw input files, label file, hash/timestamp rules, code version, and auditor recomputation tolerance or bitwise equality rule.

Recommended fixes / warning-level:
1. Add baseline-collapse tests against `S_dz2` only, c-axis optical weight only, disorder/scattering only, and structural metric only.
2. Provide a minimal three-sample preregistration packet or worked mock table with concrete variable columns and frozen windows.
3. Treat the F1 numeric example as a toy sanity check only until values are sourced from specific nickelate measurements.
4. State explicitly that F2 verifies recomputation from sealed inputs; it does not by itself prove predictive value.

---
