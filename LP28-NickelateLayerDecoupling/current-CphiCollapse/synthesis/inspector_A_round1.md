# INSPECTOR Report: A Round 1

Target: `LP28-CphiCollapse`, A Round 1 only. B output not inspected.

## Verdict

[WARNING] INSPECTOR warning, not full pass. A Round 1 has dimensionally sane toy formulae and the direction of the proposed discriminator is internally consistent, but the central residual `P_oe` is not yet shown to be actually measurable as an input-side observable in pressurized La3Ni2O7. The result can continue to Round 2 only if A treats `P_oe` as a candidate operational proxy, not as an established invariant.

No fatal algebraic error found. The strongest issue is operational/circularity risk: `chi_odd` and `chi_even` may only be available through theory-constrained fits or superconducting-channel interpretations, which can smuggle in the claimed `C_phi` or downstream output.

## Mechanical Checks

`validation/` was not present under `current-CphiCollapse`; `validate.py` was unavailable. Q1-Q5 were checked manually.

## Q1 Dimensions

- `F1: f_D = W_D / W_c`: dimensionless if `W_D` and `W_c` are extracted from the same optical spectral-weight convention. Pass.
- `F2: P_oe = (chi_odd - chi_even)/(chi_odd + chi_even)`: dimensionless if `chi_odd` and `chi_even` are same-unit susceptibilities. Pass, with missing singular/ill-conditioned case when `chi_odd + chi_even` is small.
- `F3: C_phi_ind = P_oe - (a0 + a1*W_c + ... + a6*Z_dz2)`: dimensionless only if all covariates are explicitly standardized or coefficients carry inverse units. A says "after z-scoring covariates" but the expression still uses raw symbols, including dimensional `W_c` and `gamma`. Warning: rewrite as `z(W_c)`, `z(gamma)`, etc., or define coefficient units.
- `F4: Delta_rank = r_P - r_B`: rank-position difference is dimensionless. Pass, but the rank sign convention needs definition.

Transcendental-argument check: no `exp`, `sin`, `log`, or `sinh` terms present.

## Q2 Direction and Limits

- `F1` limits are correct: `W_D -> 0` gives `f_D -> 0`; `W_D -> W_c` gives `f_D -> 1`, assuming `0 <= W_D <= W_c`.
- `F2` limits are correct for positive susceptibilities: `chi_odd = chi_even` gives `0`; `chi_even -> 0` gives `1`. Missing opposite limit: `chi_odd -> 0` gives `-1`, so the proposed index is signed and must not be treated as a nonnegative readiness score unless the sign convention is justified.
- `F3` collapse limit is directionally correct: if `P_oe` equals the fitted baseline, residual goes to `0`.
- `F4` collapse limit is correct: equal ranks give `0`. However, `r_P=1, r_B=3` gives `-2`; A should define whether negative means "P_oe ranks higher" or only use `abs(Delta_rank)`.

## Q3 Circularity and Output Leakage

Main warning: `P_oe` depends on `chi_odd` and `chi_even`, described as "normal-state interlayer odd-channel phase or spin/orbital transfer susceptibility." This is not yet an operational observable. If these are inferred from pairing-channel theory, gap structure, superconducting resonance, zero resistance, Meissner response, or fits trained on `Tc`, the discriminator leaks output and becomes circular.

A partially avoids leakage by stating that `B_base` must be fitted without `Tc`, zero resistance, Meissner fraction, or gap measurements. That boundary is necessary but not sufficient. Round 2 must specify which raw normal-state measurements produce `chi_odd` and `chi_even`, and which fitting labels are forbidden.

The residualization itself is not circular if `P_oe` is independently measured before output. It is circular if `P_oe` is defined by "the part that survives after baselines" without a pre-existing channel-sensitive measurement.

## Q4 Numerical and Algebra Tests

- `F1`: `0.18 / 0.60 = 0.30`, matches expected `[0.29, 0.31]`.
- `F2`: `(1.4 - 0.8) / (1.4 + 0.8) = 0.6 / 2.2 = 0.2727`, matches expected `[0.27, 0.28]`.
- `F3`: baseline term = `0.02 + 0.015 + 0.030 - 0.020 - 0.006 + 0.004 + 0.056 = 0.099`; residual = `0.28 - 0.099 = 0.181`, matches expected `[0.17, 0.19]`.
- `F4`: `1 - 3 = -2`, matches expected `[-2.1, -1.9]`.

No arithmetic error found in the provided tests.

## Q5 Claim Inflation

Inflated phrase: "The minimal non-collapsing object is the residual odd/even interlayer phase-transfer index." A has not proven minimality or non-collapse; it has proposed a candidate discriminator. Safer wording: "A candidate non-collapsing object is..."

Inflated phrase: "experimentally meaningful because La3Ni2O7 already has..." The cited nuisance evidence makes the test motivated, but not yet lab-ready. The missing same-sample dataset and missing direct `P_oe` extraction path should stay explicit.

The direct prior-art absence claim is appropriately hedged by confidence 0.68 and the assumption that terminology absence is not equivalence absence.

## Q6.5 Landing Strength

Landing category: weak Landing B / half-finished formula plus blueprint.

A does identify a concrete blank: no same-sample normal-state pressurized La3Ni2O7 dataset containing `W_c`, `f_D`, `gamma`, oxygen/strain controls, `Z_dz2`, and odd/even channel susceptibility. It also provides a formula and a next-step blueprint, so this is not a pure missing-landing block.

However, the landing is not yet strong enough to validate the proposed invariant. It is a design sketch, not a measurable residual. Round 2 must move from "Raman/RIXS/neutron/theory-constrained bilayer response could estimate `chi_odd/even`" to a specific extraction protocol with units, temperature/pressure window, and leakage exclusions.

## Is `P_oe` Residual Actually Measurable?

Not yet as written.

The residual `C_phi_ind` is measurable only if all of the following are true:

1. `chi_odd` and `chi_even` can be extracted from normal-state, pre-output data on the same sample or pressure series.
2. The extraction does not use superconducting labels, gap fits, `Tc`, zero resistance, Meissner response, or post-hoc knowledge of which pressure point becomes superconducting.
3. The nuisance covariates are measured on the same specimens or pressure points, not stitched from different papers with uncontrolled sample history.
4. The odd/even decomposition is identifiable with error bars after pressure-cell geometry, disorder, oxygen content, and structural phase uncertainties.

A has shown a plausible theoretical target, not an actual measurement path. `P_oe` is likely measurable only as a proxy from channel-sensitive spectroscopy plus model decomposition; that proxy has to be registered before using it as evidence for independent `C_phi`.

## Summary

No dimensional or arithmetic blocker. Direction/limit checks mostly pass, with missing sign and singular-case conventions for `P_oe`. The report's central claim should be downgraded from established residual invariant to candidate discriminator. The next round must make `P_oe` operational or admit collapse to non-measurability.

--- Feed To Next Round ---

[WARNING] Suggested fixes:

1. Rewrite `F3` with explicit standardized covariates: `z(W_c)`, `z(gamma)`, `z(V_O)`, `z(epsilon_strain)`, `z(Z_dz2)`, or define coefficient units.
2. Define the sign convention for `P_oe`: what does negative `P_oe` mean, and is readiness signed or based on magnitude?
3. Add the missing ill-conditioned limit for `P_oe` when `chi_odd + chi_even` is small.
4. Replace "minimal non-collapsing object" with "candidate non-collapsing discriminator" unless a proof of minimality is supplied.
5. Provide a leakage-free measurement protocol for `chi_odd` and `chi_even`: raw observable, spectroscopy modality, pressure/temperature regime, fitting model, forbidden labels, and error propagation.
6. Specify whether same-sample data exist. If not, Round 2 should label the result as an experimental design rather than a validated residual.
7. Test an annihilation scenario where `P_oe` is fully predicted by oxygen/strain/dephasing covariance; show whether any residual survives with realistic sample counts.

--- 
