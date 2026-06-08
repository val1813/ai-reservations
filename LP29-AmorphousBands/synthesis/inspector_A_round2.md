# INSPECTOR Report - A Round 2

Input: `D:\Claude\ai-reservations\LP29-AmorphousBands\current\A\round2.json`

Output: `D:\Claude\ai-reservations\LP29-AmorphousBands\synthesis\inspector_A_round2.md`

## 0. Mechanical Check

`validation/` directory does not exist under `D:\Claude\ai-reservations\LP29-AmorphousBands`; `validate.py` and `quantum.py` are unavailable. This report therefore performs manual Q1-Q5 plus Q6.3-Q6.5 checks.

CrossRef/MCP metadata spot-check:

- Furubayashi et al. 2019, DOI `10.1186/s11671-019-2948-4`: exists; title matches; PDF URL is available from Springer metadata.
- Jankousky et al. 2025, DOI `10.1038/s41567-025-03099-x`: exists; title matches; Nature Physics 22, 88-93, published 2025-11-17.
- Sahoo/Au/Pan 2024, DOI `10.3390/coatings14070895`: exists; title matches; abstract confirms THz Drude-Smith extraction of mobility, carrier concentration, scattering time, and negative `c`.

## Q1. Dimensional Check

Passed with one formula-direction defect noted under Q2:

- `k_F = (3*pi**2*n_m3)**(1/3)`: RHS has unit `m^-1`; pass.
- `tau = mu*m_star/e`: `m^2/(V*s) * kg / C = s`; pass.
- `v_F = hbar*k_F/m_star`: `m/s`; pass.
- `l_Drude = v_F*tau`: `m`; pass.
- `kF_l = k_F*l_Drude`: dimensionless; pass.
- `E_F_eV = hbar**2*k_F**2/(2*m_star*e)`: joule divided by coulomb gives eV numeric conversion; pass.
- `tau_linewidth = hbar/(2*DeltaE_J)`: `J*s / J = s`; pass.
- `mu_Drude = e*tau_linewidth/m_star`: `C*s/kg = m^2/(V*s)`; pass.
- `n_opt = epsilon0*m_star*omega_p**2/e**2`: `m^-3`; pass for unscreened angular plasma frequency.
- `sigma_dc = epsilon0*omega_p**2*tau*(1+c)`: `S/m`; pass.
- `IPR = integral(|psi|^4)/(integral(|psi|^2)^2)`: units depend on wavefunction normalization convention. Round 2 labels `IPR_CBM` as `1/volume`, which is acceptable for continuum wavefunctions but should be explicitly normalized if using discrete atomistic grids.

No exp/sin/log/sinh argument issue appears.

## Q2. Direction / Sign Check

Blocking formula-direction error:

- Round 2 correctly states in `hall_factor_and_optical_drude_checks.problem_statement` that `mu_H = r_H*mu_D` and `n_H = n/r_H`.
- Therefore the executable conversion must be `mu_D = mu_H/r_H` and `n_true = r_H*n_H`.
- But A1 `calculation_formulas.unit_conversions` says `n_m3 = n_H_cm3*1e6/r_H`. This is the opposite Hall-factor direction.

Corrected A1 conversion:

```text
mu_m2_Vs = mu_H_cm2_Vs*1e-4/r_H
n_m3 = n_H_cm3*1e6*r_H
```

Consequences:

- With the corrected convention, `k_F ~ r_H^(1/3)`, `tau ~ r_H^-1`, `l ~ r_H^-2/3`, and `k_F*l ~ r_H^-1/3` at fixed reported `mu_H,n_H,m*`.
- Round 2's H1 `impact` sentence gives this corrected scaling, so the file is internally inconsistent rather than globally wrong.
- If the A1 CSV is built from the current `unit_conversions`, all Hall-factor sensitivity columns for `k_F`, `E_F`, `l`, and `k_F*l` will be numerically wrong.

Other direction checks:

- A's falsification direction is correct: if matched `n` or matched `E_F-E_c` leaves graph/O-O/coordination metrics with independent residual predictive power for `mu`, linewidth, or IPR, strong A fails.
- `Drude-Smith c < -0.5` being treated as a warning against clean Drude mean-free-path interpretation is directionally correct because negative `c` suppresses dc conductivity through backscattering.
- `tau_linewidth = hbar/(2*DeltaE)` is acceptable if `DeltaE` is a half-width/self-energy broadening convention; if the extracted plotted linewidth is FWHM, the factor of 2 must be rechecked against the paper's definition. This is a warning, not a blocker.

## Q3. Circular-Argument Check

No direct circular proof is found in the stated A-falsification criteria. Round 2 improves Round 1 by allowing A to lose against graph metrics after matching `n` or `E_F-E_c`.

However, one conceptual circularity risk remains:

- `k_F*l` uses `mu` or linewidth-derived scattering as part of the predictor, while `mu` is also often the target variable. A regression of `mu ~ k_F*l` is partly tautological if `k_F*l` was computed from the same `mu`.
- This is not fatal if the actual test is phrased as either:
  1. graph metrics predict residual `mu` after `E_F-E_c` and independently measured linewidth/optical `tau`; or
  2. graph metrics predict IPR/linewidth at matched `E_F-E_c`, where the target is not algebraically used to construct `k_F*l`.

Required clarification before execution:

- For Hall-transport A1, do not use `mu_H`-derived `k_F*l` alone to predict `mu_H`. Use `k_F*l` mainly as a classification/boundary diagnostic, and test structural proxy residuals against `rho`, metallic/activated flags, reported mean free path, or optical/THz `tau` where available.
- For A2, prefer linewidth/IPR targets over `mu_Drude_calc` if `mu_Drude_calc` is computed directly from the same linewidth predictor.

## Q4. Order-of-Magnitude Check

No large order-of-magnitude error was found in the formulas themselves.

Manual scale checks:

- For `mu_H = 10 cm^2/(V*s)`, `m* = 0.2m0`, `r_H=1`, `tau = mu*m*/e ~= 1.14 fs`, matching Round 1 scale.
- For `DeltaE = 0.25 eV`, `tau = hbar/(2*DeltaE) ~= 1.32 fs`, matching the stated expected range.
- For `n_H = 1e20 cm^-3`, `r_H=1`, `k_F ~= 1.44 nm^-1`; with corrected `n_true = r_H*n_H`, changing `r_H` from 0.5 to 2 changes `k_F` only by factors `0.79` to `1.26`.

Warning:

- A1's `structural_proxy` is a z-score composite of thickness, density, and roughness. This is executable but weak: it is not a direct In-s graph or O-O/coordination measurement, so it cannot decide B failure by itself. Round 2 already says this; keep that limitation explicit.

## Q5. Algebra / Numeric-Source Check

Algebra mostly passes after correcting the Hall density conversion.

Numeric-source level:

- A1 is tied to a named existing experimental source with specific figure/table targets and concrete CSV columns. This is sufficient for a Q6.5 landing artifact, but values are not yet extracted.
- A2 is a concrete computational blueprint with structure-level rows, graph metrics, thresholds, spectral/IPR/mobility columns, model-comparison outputs, and a deliverable filename. It is executable if raw structures and QSGW/SI data are obtainable.
- The Jankousky arXiv ID is cited as `2505.07707`; the local arXiv search did not resolve it in this run, while CrossRef confirms the Nature paper. Treat the arXiv identifier as needing manual verification before using it as a data source.

## Q6.3 Claim-Shrinkage Check

No improper claim expansion was found.

Compared with Round 1, A remains narrowed:

- It no longer claims Hall-derived `k_F*l` is an independent proof.
- It explicitly allows A to lose if structural/network metrics retain residual predictive power.
- It frames the possible synthesis as "mobility edge as projection of structural graph" when graph metrics only act through `DeltaE` or linewidth.

This is acceptable scientific narrowing, not shrinkage that hides the original claim.

## Q6.4 Alternative-Explanation Check

Pass with warning.

Round 2 explicitly names the competing explanation and gives a discriminating test:

- competing explanation: O-O bonds, In coordination, and In-s graph connectivity independently control mobility/localization;
- exclusion/falsification test: match `n` or `E_F-E_c`, then test graph residual power for `mu`, linewidth, or IPR after `k_F*l/E_F-E_c` are included.

Warning:

- The "A win" rule must not count "graph variables predict DeltaE, DeltaE predicts transport" as a strong A win. Round 2 handles this correctly in `ambiguous_condition`; downstream PI should preserve that classification.

## Q6.5 Landing Check

Round 1 A's Q6.5 blocker is substantively repaired.

Why the repair passes:

- A1 gives a named existing dataset, exact extraction targets, sample axis, column schema, formulas, judgment rules, and output path: `current/A/artifacts/A1_Furubayashi2019_digitized_transport.csv`.
- A2 gives a computable same-structure table blueprint, graph definitions, threshold sweeps, target observables, model tests, and output path: `current/A/artifacts/A2_Jankousky_structure_spectral_join.csv`.
- These satisfy Q6.5's "specified existing experimental data / half-finished table / computable blueprint" requirement. Round 2 is no longer merely saying "there is a same-sample blank."

Remaining landing warnings:

- A1 is executable but only a weak landing because its structural variables are proxies from thickness/XRR/roughness, not direct In-s/O-O/coordination connectivity.
- A2 is the stronger landing for the true A-vs-B criterion, but it depends on access to raw structures, SI tables, or digitizable spectral/IPR data. If those are unavailable, A2 must be downgraded from executable table to proposed computation.

## Integrated Verdict

INSPECTOR does not block on the old Round 1 Q6.5 issue: the landing-artifact gap has been fixed.

INSPECTOR blocks on a new executable-formula defect:

1. Hall-factor density conversion is reversed in A1 `unit_conversions`. Replace `n_m3 = n_H_cm3*1e6/r_H` with `n_m3 = n_H_cm3*1e6*r_H`. Without this, A1 Hall-factor sensitivity and any derived `k_F`, `E_F`, `l`, and `k_F*l` columns are wrong.

Warnings:

1. A1 is a concrete landing artifact but weak for B because it uses structural proxies rather than direct In-s/O-O/coordination graph metrics.
2. A2 is concrete and discriminating, but executability depends on obtaining raw structures or digitizable QSGW/SI data.
3. Avoid tautological regression where `mu_H`-derived `k_F*l` is used to predict the same `mu_H`; use independent linewidth/IPR/optical `tau` or residual tests.
4. Confirm the linewidth convention before using `tau = hbar/(2*DeltaE)` on extracted plotted widths.
5. Verify the cited arXiv identifier before treating it as a source path; CrossRef confirms the Nature paper, but local arXiv search did not resolve `2505.07707`.

--- Feed To Next Round ---

BLOCKING - must fix:

1. Correct Hall-factor density conversion in A1: `n_true = r_H*n_H`, so `n_m3 = n_H_cm3*1e6*r_H`. Recompute Hall-factor sensitivity with `k_F ~ r_H^(1/3)` and `k_F*l ~ r_H^(-1/3)`.

WARNINGS - should fix:

1. Mark A1 as a weak experimental landing based on proxies; do not use it alone to claim B failure.
2. For A2, state the actual data-access route for raw structures/QSGW/IPR/linewidth before calling it executable rather than a blueprint.
3. Do not regress `mu_H` on a `k_F*l` value computed from the same `mu_H` as if independent; prefer linewidth/IPR/optical-Drude targets or residual tests.
4. Check linewidth FWHM versus half-width convention before applying `hbar/(2*DeltaE)`.
5. Preserve the non-circular falsification rule: A loses only when graph metrics retain residual predictive power after predeclared matching on `n_true` or `E_F-E_c`; "graph -> DeltaE -> transport" is an ambiguous synthesis, not a strong A win.

---
