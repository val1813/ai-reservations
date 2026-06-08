# INSPECTOR Report: A Round 2

Target: `LP28-CphiCollapse`, A Round 2 only. B output not inspected.

## Verdict

[WARNING] INSPECTOR warning, not blocker. A Round 2 fixes the main Round 1 defects: `P_oe` is now signed, denominator singularity is censored, covariates are standardized through `B_base`, same-sample status is explicitly negative, and covariance annihilation has concrete criteria.

No dimensional, direction, algebraic, or numerical blocker found. The remaining risks are operational rather than algebraic: sample-specific `Tc_onset` must not set the supposedly input-side temperature window, the `N >= 8` minimum is too weak for seven baseline covariates, and the covariance criteria leave a 0.65-0.85 `R2` gray zone that must be predefined before Round 3.

## Mechanical Checks

`validation/` was not present under `current-CphiCollapse`; `validate.py` was unavailable. Q1-Q5 were checked manually.

## Q1 Dimensions

- `F1: P_oe = (chi_odd - chi_even)/(chi_odd + chi_even)`: dimensionless if `chi_odd` and `chi_even` are same-channel, same-window susceptibility integrals. Pass.
- `chi = integral S/omega d_omega`: internally consistent as a static or low-energy integrated response if `S_odd` and `S_even` use identical normalization. The absolute unit is less important than parity-channel equality. Pass with calibration caveat.
- `denominator_floor = max(5*sigma_chi_sum, instrument_background_floor)`: only dimensionally valid if `instrument_background_floor` has been converted from raw intensity/background units into the same units as `chi_odd + chi_even`. Warning.
- `F2: I_qz = A*(chi_even*cos(q_z*d/2)^2 + chi_odd*sin(q_z*d/2)^2) + bg`: pass if `q_z` is inverse length, `d` is length, `A*chi` has intensity units, and `bg` is intensity.
- `F3: C_phi_ind = P_oe - predict(P_oe | B_base)`: dimensionless. Round 1 raw-covariate unit issue is fixed by defining `B_base` as z-scored covariates.
- `F4: sigma_residual = sigma_P_oe*sqrt(1 - R2_baseline)`: dimensionless. Valid only for `0 <= R2_baseline <= 1`; if cross-validated `R2` is negative, the formula must be clipped or not used.
- `F5: f_D = W_D/W_c`: dimensionless if both spectral weights use the same integration convention. Pass.

Transcendental arguments: `cos(q_z*d/2)` and `sin(q_z*d/2)` are dimensionless. No invalid `exp`, `log`, or similar arguments found.

## Q2 Direction and Limits

- `P_oe` limits are correct: equal channels give `0`, pure odd gives `1`, pure even gives `-1`, and vanishing denominator is undefined. Sign convention is now explicit.
- Scale invariance is correct: multiplying both `chi_odd` and `chi_even` by positive `lambda` leaves `P_oe` unchanged.
- Bilayer form factor limits are correct: `q_z*d/2 -> 0` selects the even channel; `q_z*d/2 -> pi/2` selects the odd channel.
- `C_phi_ind` direction is correct: if baselines predict all of `P_oe`, residual goes to `0`.
- `sigma_residual` direction is correct inside the valid `R2` interval: `R2 -> 1` annihilates residual variance; `R2 -> 0` returns the original variance.
- `f_D` limits are correct for `0 <= W_D <= W_c`: no Drude weight gives `0`; all low-energy c-axis weight Drude-like gives `1`.

## Q3 Circularity and Output Leakage

A Round 2 mostly blocks leakage by forbidding superconducting spin resonance, gap fits, `Tc`, zero resistance, Meissner fraction, diamagnetism, and output-trained classifiers.

Remaining leakage warning: the preferred window says `T >= max(Tc_onset + 40 K, 120 K)`. If `Tc_onset` is measured on the same pressure row or revealed before extracting `P_oe`, this is output leakage. Round 3 should replace this with a fixed preregistered normal-state temperature grid, for example 120 K, 150 K, and 200 K, or justify that `Tc_onset` is external historical metadata unavailable at row ranking time.

Residualization is not circular as written because `P_oe` is extracted before conditioning. It becomes circular only if the theory-constrained odd/even fit uses superconducting pairing symmetry, post-hoc pressure labels, or output performance to select the Hamiltonian/model class.

## Q4 Algebra and Numerical Tests

- `F1`: `(1.4 - 0.8)/(1.4 + 0.8) = 0.6/2.2 = 0.2727`, matches `[0.27, 0.28]`.
- `F2`: with `q_z = 1`, `d = pi`, `q_z*d/2 = pi/2`, so `I = 2.0*1.3 + 0.1 = 2.7`, matches `[2.69, 2.71]`.
- `F3`: `0.30 - 0.27 = 0.03`, matches `[0.029, 0.031]`.
- `F4`: `0.20*sqrt(1 - 0.90) = 0.0632`, matches `[0.062, 0.064]`.
- `F5`: `0.18/0.60 = 0.30`, matches `[0.29, 0.31]`.

No arithmetic error found.

## Measurement Feasibility

`chi_odd`, `chi_even`, and `P_oe` are now conceptually measurable, but not yet demonstrated in the required La3Ni2O7 same-sample pressure packet.

RIXS route: plausible near-term proxy, but pressure-cell q_z resolution, self-absorption, polarization leakage, and background coupling must be included in the error model. Ambient-pressure Chen et al. figures cannot validate pressure-series `P_oe`.

Neutron route: formally clean for bilayer parity, but high-pressure La3Ni2O7 sample-volume requirements make this a feasibility bottleneck.

Raman and THz/optical routes: correctly demoted to baselines. They cannot define `P_oe` alone.

Same-sample status: pass as an honest negative result. A states `same_sample_complete_packet_exists: false` and does not claim validation from stitched literature components.

## Covariance Annihilation

The annihilation logic is directionally correct and substantially improved. Baseline collapse criterion `CV_R2 >= 0.85`, small residual mean, and no matched-pair rank inversion is a usable fail condition. Survival criterion requiring residual rank discordance and at least two matched pairs at `|C_phi_ind| >= 2*sigma_residual` is also sensible.

Warnings:

- `N_pressure_rows >= 8` is too weak for `B_base` with seven covariates. With `N <= 8`, ordinary regression is not identifiable or is effectively all leverage. Round 3 should require either `N >= 12-20` for the full block or a preregistered low-dimensional covariate block/shrinkage model.
- The interval `0.65 < CV_R2 < 0.85` is undecided. Round 3 must define it as inconclusive, not survival.
- If cross-validated `R2` is negative, `sigma_residual = sigma_P_oe*sqrt(1 - R2)` can exceed `sigma_P_oe`; that is statistically possible for bad prediction but should be reported as baseline failure, not interpreted as enhanced independent signal.

## Claim Inflation

Claim inflation is mostly fixed. A no longer calls `P_oe` a proven minimal invariant and explicitly treats current literature as proxy/design support.

Remaining phrasing to keep constrained: "leakage-free `P_oe` is definable" is acceptable mathematically, but any future claim that it is "available", "validated", or "pressure-series tested" must be blocked until a same-sample packet exists.

## Q6.3 Claim Shrinkage

No problematic shrinkage from Round 1. The claim appropriately narrows from candidate invariant language to a leakage-free normal-state susceptibility ratio plus experimental design constraints.

## Q6.4 Alternative Explanations

A directly addresses oxygen, strain, dephasing, c-axis coherence, orbital/ligand-hole proxies, and sample quality baselines. Alternative-explanation handling passes, with the caveat that actual exclusion requires same-sample covariance data, not literature stitching.

## Q6.5 Landing

Landing category: Landing B, strong design but not experimental validation.

The blank is concrete: no same-sample La3Ni2O7 packet with q_z-resolved odd/even susceptibility plus optical, oxygen, strain, orbital, and dephasing baselines. A gives formulas, candidate figures, required rows, and annihilation criteria. This is sufficient to proceed to Round 3 thresholding, but not sufficient to claim `C_phi_ind` survives.

--- Feed To Next Round ---

[WARNING] Suggested fixes:

1. Replace the `Tc_onset + 40 K` temperature rule with a fixed preregistered normal-state temperature grid, or explicitly prove `Tc_onset` is not row-output leakage.
2. Convert `instrument_background_floor` into `chi_sum` units before using it in `denominator_floor`.
3. Raise the minimum full-baseline design from `N >= 8` to `N >= 12-20`, or require a preregistered shrinkage/blocked-covariate model for small N.
4. Define `0.65 < cross_validated_R2 < 0.85` as an inconclusive covariance zone, not survival.
5. Specify handling for negative cross-validated `R2` in `sigma_residual`.
6. Keep same-sample status explicit: current literature components are proxy/design inputs only, not validation of `P_oe` or `C_phi_ind`.

---
