# INSPECTOR Report: LP28 A Round 2

Input: `D:\Claude\ai-reservations\LP28-NickelateLayerDecoupling\current\A\round2.json`

Scope: only LP28 A Doctor Round 2. This report follows `D:\Claude\ai-reservations\ai\INSPECTOR.md` and does not perform REVIEWER-style prior-art adjudication.

## Mechanical Check

`validation/` directory was not found under `D:\Claude\ai-reservations\LP28-NickelateLayerDecoupling`, so `validate.py` and `quantum.py` were unavailable.

Q1-Q5 were checked manually.

## Verdict

[WARNING] INSPECTOR warning: A Round 2 can continue, but the `Interlayer Phase Quorum Criterion` must be rewritten as an operational decision rule rather than a post-hoc composite score.

No blocking dimensional, sign, algebraic, or numeric error was found in the two explicit formulas:

1. `gamma_rho = rho_c / rho_ab`
2. `Q = (W_c_Drude / W_ab_Drude) * f_shield / (1 + A_DW_static)`

Primary warnings:

1. `Q` is dimensionless, but it mixes a proposed engineering input/proxy (`W_c_Drude/W_ab_Drude`), an outcome variable (`f_shield`), and a competing-order proxy (`A_DW_static`). This makes it usable as a retrospective validation score, not yet as a forward materials-design criterion.
2. There is a circular-argument risk: the criterion defines "phase quorum" using `f_shield`, then uses growth of `f_shield` to validate the existence of the quorum. This is not fatal if `f_shield` is explicitly labelled as the external success metric, but it cannot also be part of the independent predictor.
3. The prior-art boundary forces real claim shrinkage from "interlayer coherence as organizing parameter" to "trilayer DW-induced dz2 layer decoupling and pressure/strain/pump recovery sequence." A Round 2 mostly acknowledges this, but the headline name `Interlayer Phase Quorum Criterion` still sounds broader than the remaining defensible boundary.
4. Alternative explanations are listed well, but most are only "retained" rather than operationally excluded. The next round needs a minimal discriminator table with required measurements and pass/fail outcomes.
5. Engineering landing is improved relative to Round 1, but still semi-operational: it names observables and tuning knobs, yet lacks threshold values, measurement windows, and an explicit go/no-go protocol.

## Q1 Dimensional Check

### F1: `gamma_rho = rho_c / rho_ab`

- LHS unit: dimensionless.
- RHS unit: resistivity/resistivity = dimensionless.
- Match: yes.
- Limit check: `rho_c -> 0` gives `gamma_rho -> 0`, matching the stated "perfect c-axis metallicity reduces anisotropy" limit.

### F2: `Q = (W_c_Drude / W_ab_Drude) * f_shield / (1 + A_DW_static)`

- `W_c_Drude / W_ab_Drude`: dimensionless if both Drude weights use the same spectral-weight convention.
- `f_shield`: dimensionless if normalized to 1.
- `A_DW_static`: dimensionless if normalized to an explicitly stated reference, here ambient low-temperature value.
- RHS unit: dimensionless.
- Match: yes, conditional on normalization conventions being fixed.

Warnings:

- `A_DW_static` can come from diffraction, RIXS, or ultrafast proxies. These are not naturally interchangeable without a calibration map.
- `W_c_Drude/W_ab_Drude` is not automatically a phase-coherence measure; it may include carrier-density, mass-renormalization, and scattering-model choices unless Drude weight and scattering rate are separated.
- No invalid dimensional arguments of `exp`, `sin`, `log`, or `sinh` were present.

## Q2 Direction Check

### Anisotropy direction

Claimed direction: stronger c-axis metallicity or coherence reduces `rho_c/rho_ab`; DW-induced layer decoupling increases it.

Check: `gamma_rho = rho_c/rho_ab` monotonically increases with `rho_c` at fixed `rho_ab`, and decreases if out-of-plane transport improves. Direction is correct.

### Quorum score direction

Claimed direction: `Q` increases when c-axis Drude weight and shielding grow, and decreases when static DW amplitude grows.

Check:

- `W_c_Drude` increase at fixed `W_ab_Drude`, `f_shield`, `A_DW_static` increases `Q`.
- `f_shield -> 0` gives `Q -> 0`.
- `A_DW_static -> 0` gives `Q -> (W_c_Drude/W_ab_Drude)*f_shield`.
- `A_DW_static -> infinity` gives `Q -> 0`.

Direction is internally correct.

Warning: if `W_ab_Drude` changes strongly under pressure, a rise in the ratio can reflect in-plane spectral-weight suppression rather than c-axis recovery. The criterion should require absolute `Delta W_c_Drude > 0` or `Delta sigma_c(omega -> 0) > 0`, not only a ratio.

## Q3 Circular-Argument Check

[WARNING] Circularity risk in `Interlayer Phase Quorum Criterion`.

The submitted rule says the dz2-mediated interlayer phase quorum is retained as an engineerable variable only when:

- `Delta W_c_Drude` or `Delta sigma_c(omega -> 0)` is positive,
- `rho_c/rho_ab` decreases,
- `bulk shielding/Meissner fraction` grows,
- alternative proxies cannot explain the growth alone.

This prose rule is mostly non-circular because it separates c-axis recovery from external superconducting volume validation.

However, the minimal quantitative form

`Q = (W_c_Drude / W_ab_Drude) * f_shield / (1 + A_DW_static)`

does introduce circularity if `Q` is used to predict or prove bulk phase quorum. `f_shield` is the target outcome, not an independent input. The criterion can be used as:

- a retrospective "successful quorum state score"; or
- a plotted joint diagnostic after all measurements are collected.

It cannot yet be used as:

- a forward predictor of shielding fraction; or
- proof that interlayer coherence caused shielding fraction.

Recommended correction: split into two quantities:

1. Predictor: `I_c = Delta W_c_Drude` or `Delta sigma_c(omega -> 0)` with `rho_c/rho_ab` decrease and proxy controls.
2. Outcome: `B = f_shield` plus Meissner/vortex-sensitive response.

Then require temporal or tuning-axis ordering: `I_c` recovers before or at the onset of `B`.

## Q4 Order-of-Magnitude Check

No order-of-magnitude cliff was found in the explicit numerical test.

For F2:

`Q = (0.05 / 1.0) * 0.5 / (1 + 0.2) = 0.020833...`

This falls within the submitted expected range `[0.01, 0.1]`.

Warning: the expected range is broad and not physically calibrated. It verifies arithmetic only; it does not establish a meaningful engineering threshold.

## Q5 Algebra and Numeric Verification

### F1

`gamma_rho = rho_c/rho_ab` is algebraically direct and dimensionless.

The cited values in Round 2, such as room-temperature `gamma ~ 70`, low-temperature `gamma ~ 2600`, and six-terminal values up to `~1.8e4`, are used as evidence anchors rather than as new derivations. No arithmetic inconsistency was detected in the formula itself.

### F2

Step-by-step:

`Q = (W_c/W_ab) * f/(1 + A)`

Substitution:

`Q = (0.05/1.0) * 0.5 / (1 + 0.2)`

`Q = 0.05 * 0.5 / 1.2`

`Q = 0.025 / 1.2 = 0.0208`

Arithmetic matches the expected range.

Source-level warning:

- `W_c_Drude`, `W_ab_Drude`, `f_shield`, and `A_DW_static` are defined, but their normalization and extraction protocols are not yet fixed.
- `A_DW_static` especially needs one primary proxy for the criterion, with cross-proxy conversion treated as secondary.

## Q6.3 Claim Shrinkage Check

[WARNING] Claim shrinkage present but mostly appropriate.

Round 1 A claim:

- Static DW order suppresses dz2-mediated interlayer channel and acts as a suppressor of 3D phase-coherent superconductivity.
- First discriminator: tuning reduces `rho_perp/rho_parallel` and restores coherent c-axis transport before or at superconducting onset.

Round 2 A claim:

- Interlayer coherence as a general organizing parameter is already prior art.
- Bilayer coherent dz2-pz-dz2 hybridization enabling superconductivity is already prior art.
- LP28 should shrink to trilayer La4Ni3O10/Pr4Ni3O10: whether static DW suppresses bulk phase quorum through dz2 layer decoupling, and whether pressure/strain/pump can restore it without destroying pairing fluctuations.

Assessment:

- The shrinkage is scientifically necessary because of the stated prior-art boundary.
- It does reduce the claim level from "mechanism-level suppressor conclusion" to "testable design criterion / causal-ordering hypothesis."
- This is not a blocking flaw, but PI should update the North Star score and claim wording accordingly.

Residual problem:

The criterion name `Interlayer Phase Quorum Criterion` remains broad and could be read as a general RP nickelate framework. Safer name:

`Trilayer DW-Decoupling Recovery Criterion`

or

`Trilayer c-axis Recovery / Bulk Shielding Ordering Criterion`.

## Q6.4 Alternative Explanation Check

Status: partially passed.

A Round 2 explicitly lists major alternatives:

1. Pressure directly changes bandwidth or carrier density.
2. Structural transition directly induces superconductivity.
3. Disorder or oxygen stoichiometry controls both interlayer channel and superconductivity.
4. Scattering anisotropy, not hopping/coherence, explains `rho_c/rho_ab`.
5. Current redistribution creates false anisotropy.
6. Pressure is a common third variable driving DW collapse, interlayer coherence, and superconductivity together.

This is a substantial improvement over Round 1.

Remaining warning:

Most alternatives are "retained" rather than excluded. This is acceptable for Round 2, but the next step must convert each alternative into one pass/fail discriminator. The current rule says proxies "cannot independently explain growth," but does not define what counts as independent explanation failure.

Minimum discriminator set needed:

1. Separate Drude weight from scattering rate: `plasma_frequency_c^2` recovery should dominate, not only `1/tau_c` improvement.
2. Track in-plane carrier proxy: if `Tc` or `f_shield` follows in-plane spectral weight/carrier density while `sigma_c` does not recover, LP28 criterion fails.
3. Track structure: if structural transition occurs without `sigma_c` recovery or shielding growth, structure is not sufficient.
4. Control geometry: use six-terminal/Corbino-like or optical `sigma_c` under pressure to avoid current-redistribution artifacts.
5. Break common pressure variable: use uniaxial strain, epitaxial strain, oxygen compensation, or selective pump as non-equivalent perturbations.

## Q6.5 Landing Calculation Check

Status: pass with warning.

A Round 2 contains landing elements:

- target systems: La4Ni3O10/Pr4Ni3O10 trilayer RP nickelates;
- measurable observables: `rho_c/rho_ab`, `rho_perp/rho_parallel`, c-axis Drude weight, low-frequency `sigma_c`, bulk shielding/Meissner fraction;
- tuning knobs: hydrostatic pressure, uniaxial c-axis strain, epitaxial strain, oxygen stoichiometry compensation, apical-O/dz2-coupled phonon pump;
- falsification condition: shielding grows without c-axis Drude/sigma_c recovery, or c-axis recovery occurs without bulk shielding/vortex/Meissner response.

Warning:

This is an experimental blueprint, not yet a hard engineering criterion. It lacks:

1. a minimum `Delta W_c_Drude` or `Delta sigma_c` threshold;
2. a minimum `f_shield` threshold after demagnetization correction;
3. a pressure/strain/pump window;
4. a decision table for "pass", "fail", and "ambiguous";
5. a rule for what happens if `W_c_Drude` and `rho_c/rho_ab` disagree.

Because Round 2 correctly states that pressure-dependent c-axis Drude or anisotropy data are missing, there is no Q6.5 blocking failure. It should be labelled a proposed landing protocol rather than a completed landing calculation.

## Focused Check: Interlayer Phase Quorum Criterion

### Dimensional status

Pass, conditional.

All components can be dimensionless if normalized consistently.

Required fixes:

- define Drude spectral-weight integration window or plasma-frequency convention;
- define whether `W_ab_Drude` is same-temperature/same-pressure denominator;
- choose one primary `A_DW_static` proxy;
- state normalization reference for `A_DW_static = 1`;
- keep `f_shield` as an outcome metric, not an independent predictor.

### Circularity status

Warning.

The prose criterion is acceptable as a joint validation rule. The scalar `Q` risks circularity because it contains `f_shield`, the same variable used to verify phase quorum.

Recommended rewrite:

- `I_c = Delta W_c_Drude` or `Delta sigma_c(omega -> 0)` as interlayer recovery index.
- `S_DW = A_DW_static` as competing static order index.
- `B = f_shield` as bulk outcome.
- Criterion: `I_c` increases and `S_DW` decreases before or at the rise of `B`, while carrier/structure/disorder proxies fail to explain `B` alone.

### Alternative explanation status

Warning but improved.

A Round 2 names the right alternatives. The missing piece is operational exclusion, not awareness.

### Engineering status

Warning.

The criterion is experimentally actionable enough to guide Round 3, but not yet a landed engineering rule. It needs thresholds and a decision table.

## Final INSPECTOR Decision

[WARNING] INSPECTOR warning: continue, but carry the warnings explicitly.

No mandatory blocking error was found. A Round 2 should not be discarded. The main correction is conceptual hygiene: do not let the `Q` score become a circular proof of the target phenomenon.

--- Feed To Next Round ---

[BLOCKING] Must Fix:

None.

[WARNING] Suggested Fixes:

1. Split `Q` into independent predictor and outcome: keep `f_shield` outside the interlayer-coherence predictor, otherwise the criterion is partly circular.
2. Rename or narrow `Interlayer Phase Quorum Criterion` so it does not overclaim beyond the post-prior-art boundary; prefer a trilayer-specific recovery-ordering criterion.
3. Define normalization and extraction protocols for `W_c_Drude`, `W_ab_Drude`, and `A_DW_static`.
4. Add a pass/fail discriminator table for alternatives: bandwidth/carrier density, structural transition, disorder/oxygen stoichiometry, scattering anisotropy, current redistribution, and common pressure variable.
5. Convert the engineering target into thresholds: minimum `Delta sigma_c` or `Delta W_c_Drude`, minimum corrected `f_shield`, pressure/strain/pump window, and ambiguous-case handling.
6. Mark the current landing as a proposed protocol, not a completed landing calculation, because pressure-dependent c-axis Drude/anisotropy data remain missing.

---
