# INSPECTOR Report: LP28 A Round 3

Input: `D:\Claude\ai-reservations\LP28-NickelateLayerDecoupling\current\A\round3.json`

Scope: only LP28 A Doctor Round 3. This report follows `D:\Claude\ai-reservations\ai\INSPECTOR.md` and does not perform REVIEWER-style prior-art adjudication.

## Mechanical Check

`validation/` directory was not found under `D:\Claude\ai-reservations\LP28-NickelateLayerDecoupling`, so `validate.py` and `quantum.py` were unavailable.

Q1-Q5 were checked manually.

## Verdict

[WARNING] INSPECTOR warning: A Round 3 passes the main Round 2 circularity correction, but the protocol is still a semi-quantitative working decision rule, not a calibrated mechanism proof.

No blocking dimensional, sign, algebraic, or circularity error was found in the core predictor:

```text
I_phi = E_z2 * C_phi / (k_B*T + hbar*Gamma_phi + E_floor)
```

Primary warnings:

1. `I_phi` is dimensionally consistent only if `E_z2`, `k_B*T`, `hbar*Gamma_phi`, and `E_floor` are all reported in the same energy unit, preferably meV. The file mostly does this, but it must avoid double-counting `hbar` when the linewidth is already reported as an energy `hbar_Gamma_phi`.
2. `W_z2 -> E_z2` remains a calibration convention. `E0 = 10 meV` is explicitly labeled as working calibration, so this is acceptable, but all threshold labels are conditional on that convention.
3. The `I_phi` threshold bands are internally non-overlapping and directionally coherent, but the experimental threshold table leaves some grey zones implicit, especially `0.10 <= Delta W_c/W_c_ref < 0.25`.
4. The go/no-go protocol is no longer circular because `B_bulk` is excluded from `I_phi`; however, the protocol still uses `B_bulk` as a required validation gate, so final `GO_working/GO_strong` is a joint predictor-plus-outcome label rather than a pure prediction.
5. Alternative explanations are operationalized better than Round 2, but the exclusion rule is still comparative and semi-quantitative: "tracks more strongly" needs a specified metric before it can become a hard analysis protocol.
6. Landing calculation is concrete enough to pass Q6.5, but it remains an example substitution, not a material-specific measured landing.

## Q1 Dimensional Check

### F1: `I_phi = E_z2*C_phi/(k_B*T + hbar*Gamma_phi + E_floor)`

- LHS unit: dimensionless index.
- `E_z2`: meV by protocol.
- `C_phi`: dimensionless, product of factors in `[0, 1]`.
- `k_B*T`: `(meV/K) * K = meV`.
- `hbar*Gamma_phi`: meV if `Gamma_phi` is an angular frequency; also acceptable as `hbar_Gamma_phi` if already reported as a linewidth/dephasing energy.
- `E_floor`: meV.
- RHS unit: `meV * 1 / meV = dimensionless`.
- Match: yes, conditional on consistent energy convention.

Warning:

The JSON uses both `hbar*Gamma_phi` and `hbar_Gamma_phi_meV` language. This is not a formula error, but the protocol must state whether the experimental input is a rate `Gamma_phi` or an energy linewidth `hbar_Gamma_phi`. If the latter is supplied, do not multiply by `hbar` again.

No invalid dimensional arguments of `exp`, `sin`, `log`, or `sinh` were present.

### `W_z2`, `E_z2`, and `E_floor` protocol

`W_z2` is dimensionless only after normalization to a stated same-sample high-temperature non-DW reference or a DFT/sum-rule reference. The file correctly warns not to mix raw `sigma_c`, Drude plasma frequency, and integrated spectral weight without a fixed window and normalization.

`E_z2 = E0*W_z2` is dimensionally valid because `E0` carries meV. `E_z2 = hbar*omega_p_c_eff` is also dimensionally valid if the optical scale is reported as angular frequency converted to energy. Both remain calibration choices, not universal definitions.

`E_floor` is dimensionally valid as an additive denominator floor in meV. The required sensitivity sweep over `0.25, 0.5, 1.0 meV` is a necessary guard against using the floor as a tuning parameter.

## Q2 Direction and Limit Check

Direction is internally correct:

- `E_z2 -> 0` gives `I_phi -> 0`, matching no dz2 interlayer bus.
- `C_phi -> 0` gives `I_phi -> 0`, matching no phase-connected domains.
- `Gamma_phi -> large` gives `I_phi -> 0`, matching strong dephasing.
- `T` increase lowers `I_phi`, which is consistent with thermal decoherence under this phenomenological index.
- Larger `E_floor` lowers `I_phi`, correctly making low-energy marginal cases harder to classify as go.

No sign reversal or ratio inversion was found.

## Q3 Circular-Argument Check

Status: pass with residual labeling warning.

Round 2's circular score contained `f_shield` inside the quasi-predictor. Round 3 fixes this by:

- defining `I_phi` using only `W_c/W_z2/E_z2`, `C_phi`, `Gamma_phi`, `T`, and `E_floor`;
- explicitly forbidding shielding fraction, Meissner fraction, zero resistance, `Tc`, vortex signature, and THz superfluid stiffness as predictor inputs;
- moving those bulk observables into `B_bulk` as the outcome.

Therefore, the predictor itself is non-circular.

Residual warning:

The final labels `GO_working` and `GO_strong` require both `I_phi` and `B_bulk`. That is acceptable as a decision protocol, but not as a pure forward predictor. The wording should remain "phase-bus-supported bulk route passes the protocol," not "I_phi alone proves bulk superconductivity."

## Q4 Order-of-Magnitude Check

The explicit landing calculation is arithmetically consistent.

Substitution:

```text
E0 = 10 meV
W_z2 = 0.35
C_phi = 0.80
T = 20 K
k_B = 0.0861733 meV/K
hbar_Gamma_phi = 0.80 meV
E_floor = 0.50 meV
```

Calculation:

```text
E_z2 = E0 * W_z2 = 10 * 0.35 = 3.5 meV
denominator = 0.0861733*20 + 0.80 + 0.50
            = 1.723466 + 0.80 + 0.50
            = 3.023466 meV
I_phi = 3.5*0.80/3.023466
      = 2.8/3.023466
      = 0.926
```

This matches the stated expected range `[0.90, 0.95]` and the interpretation "ambiguous, not go."

The threshold targets are also consistent:

```text
I_phi >= 1 requires W_z2 >= 3.023466/(10*0.80) = 0.378
I_phi >= 2 requires W_z2 >= 2*3.023466/(10*0.80) = 0.756
```

No order-of-magnitude cliff was found.

## Q5 Algebra and Numeric Verification

### F1 algebra

The formula is algebraically direct. It is monotone increasing in `E_z2` and `C_phi`, monotone decreasing in `T`, `Gamma_phi`, and `E_floor`.

The denominator cannot vanish because `E_floor` is positive and `T`, dephasing energies are nonnegative in the intended domain.

Warning:

If `C_kz` or `C_struct` is unavailable, Round 3 correctly says it should be set to unknown rather than silently set to `1`. This must be enforced in later use. Otherwise `C_phi` can become an optimistic hidden prior.

### F2: `Delta_W_c_over_ref`

`Delta_W_c_over_ref = (W_c_tuned - W_c_DW_lowT)/W_c_ref` is dimensionless if all `W_c` terms use the same extraction convention and reference.

The numerical test `Delta_W_c_over_ref = 0.25` is tautological but not wrong. It verifies a threshold value, not a derived physical result.

Source-level warning:

The threshold `0.25` is a working lower bound above expected fit/systematic uncertainty, not a literature-calibrated universal value. Round 3 states this correctly, so this is not blocking.

## Threshold Table Self-Consistency

Status: pass with two warnings.

`I_phi_threshold_table` is internally ordered and non-overlapping:

- `I_phi < 0.3`: no-go
- `0.3 <= I_phi < 1.0`: ambiguous
- `1.0 <= I_phi < 2.0`: go candidate
- `I_phi >= 2.0`: strong go

This is coherent with the landing example `I_phi = 0.926`, which falls in `ambiguous`.

The minimal experimental thresholds are mostly consistent with the decision labels:

- `GO_working` requires `I_phi >= 1.0`, `Delta W_c` lower bound, `B_bulk >= 0.20`, and bounded controls.
- `GO_strong` requires `I_phi >= 2.0`, strong `Delta W_c`, strong `B_bulk`, and all controls pass.
- `NO_GO_phase_bus` covers `B_bulk` without c-axis recovery or no-go `I_phi`.
- `NO_GO_bulk` covers c-axis recovery without bulk validation.

Warnings:

1. `Delta_W_c_lower_bound` defines fail at `<0.10` and go at `>=0.25`, but the interval `0.10-0.25` should be explicitly labeled ambiguous, not left implicit.
2. `Delta_sigma_c` is allowed as a substitute when Drude weight cannot be reliably fitted. The protocol should state how to resolve conflict if `Delta_sigma_c` passes but fitted/integrated `W_c` fails. The current text says `W_c`/`sigma_c` disagreement is ambiguous, which is acceptable, but it should be repeated in the threshold table.

## Go/No-Go Circularity Check

Status: pass.

The go/no-go sequence does not require using the outcome to build the predictor:

1. Baseline extraction quantifies `W_z2/E_z2` and controls.
2. Tuning-axis phase-bus test checks `Delta W_c` and `I_phi`.
3. Bulk outcome validation checks `B_bulk`.
4. Alternative-explanation exclusion checks controls.
5. Decision labels combine predictor, outcome, and controls.

This is a valid decision protocol. It is not a proof of causality unless temporal or tuning-axis ordering and controls are actually measured. Round 3 states that the existing literature does not yet satisfy the combined requirement, so no blocking overclaim is present.

## Q6.3 Claim Shrinkage Check

Status: appropriate shrinkage, no new warning beyond calibration.

Round 2 required A to shrink from a broad "interlayer coherence" criterion to a trilayer-specific recovery-ordering protocol. Round 3 does that:

- name: `Trilayer dz2 phase-bus go/no-go protocol`;
- system: La4Ni3O10/Pr4Ni3O10 trilayer RP nickelates;
- current status: baseline/motivation sufficient, mechanism not verified;
- output claim: proposed testable technology route, not established mechanism.

This is scientifically cleaner than Round 2 and should not be penalized as a flaw. It does mean the North Star remains an experimental protocolization route rather than a completed theoretical breakthrough.

## Q6.4 Alternative Explanation Check

Status: partial pass.

Round 3 explicitly lists the major alternatives and assigns discriminators:

1. carrier density or bandwidth: Hall number tolerance and ab Drude control;
2. structural phase transition: same-axis XRD/Raman plus `W_c` and `B_bulk`;
3. oxygen/disorder: EELS/XAS/annealing or stoichiometry proxy plus linewidth/disorder proxy;
4. scattering anisotropy: separate `plasma_frequency_c**2` from `1/tau_c`;
5. current redistribution or pressure-cell geometry: six-terminal/Corbino-like geometry or optical `sigma_c`;
6. filamentary superconductivity: shielding, Meissner/vortex/THz response.

This is a real improvement over Round 2 and is sufficient for an INSPECTOR pass at the protocol-design stage.

Remaining warning:

The exclusion is still not fully quantitative because "B_bulk tracks X more strongly than I_phi/W_c" lacks a specified statistical or regression criterion. Before final use, define one of:

- same-sample monotonic ordering plus threshold crossing;
- correlation/rank-correlation comparison across tuning points;
- regression or model-selection rule with uncertainty bars;
- pre-registered pass/fail visual decision rule.

Without this, alternative explanations are not actually excluded; they are only assigned plausible controls.

## Q6.5 Landing Calculation Check

Status: pass with warning.

A Round 3 contains a concrete landing calculation:

- system: La4Ni3O10 or Pr4Ni3O10 under same-sample pressure or uniaxial c-axis strain;
- variables: `E0`, `W_z2`, `C_phi`, `T`, `k_B`, `hbar_Gamma_phi`, `E_floor`;
- computed output: `I_phi = 0.926`;
- interpretation: ambiguous, not go;
- target values for go and strong go.

This satisfies the minimum "not empty landing" requirement.

Warning:

The landing remains a worked example, not a measured landing. It does not yet use actual same-sample pressure/strain optical and shielding data. Therefore it supports "protocol ready for experimental test," not "mechanism verified."

## Focused Checks Requested By PI

### `I_phi` quantity and units

Pass. `I_phi` is dimensionless if all denominator terms are in meV and `C_phi` is dimensionless. Required correction for next use: standardize the input name as either `Gamma_phi` in frequency units or `hbar_Gamma_phi` in energy units.

### `E_z2/W_z2/E_floor` protocol

Pass with calibration warning. The protocol correctly separates dimensionless `W_z2`, energy-scale `E_z2`, and additive energy floor `E_floor`. It also requires normalization and sensitivity analysis. The remaining weakness is that `E0 = 10 meV` is a working calibration, not a measured nickelate constant.

### Threshold table self-consistency

Mostly pass. `I_phi` bands and final decision labels are coherent. Add explicit ambiguous labels for intermediate `Delta W_c` and `Delta_sigma_c` cases.

### Go/no-go circularity

Pass. `B_bulk` is not inside `I_phi`. Final labels are joint validation labels, not pure predictor labels.

### Alternative explanation exclusion

Partial pass. The right alternatives and controls are named. The protocol still needs a quantitative rule for "tracks more strongly" before it can truly exclude alternatives.

### Is it still only semi-quantitative?

Yes. Round 3 is still semi-quantitative because all key thresholds are working protocol values pending same-sample calibration. This is acceptable because the file repeatedly states that the route is not yet verified.

## Final INSPECTOR Decision

[WARNING] INSPECTOR warning: continue, but carry the warnings explicitly.

No blocking error was found. A Round 3 successfully fixes the main Round 2 circularity issue and turns the concept into a usable go/no-go draft. It should not be treated as a calibrated mechanism proof until same-sample tuning-axis data fix `E0`, `E_floor`, `W_z2/W_c` extraction, and alternative-explanation statistics.

--- Feed To Next Round ---

[BLOCKING] Must Fix:

None.

[WARNING] Suggested Fixes:

1. Standardize dephasing notation: use either `Gamma_phi` as a rate with `hbar*Gamma_phi`, or `hbar_Gamma_phi` as an energy input, but do not mix them.
2. Add explicit ambiguous ranges for `0.10 <= Delta W_c/W_c_ref < 0.25` and for `Delta_sigma_c` cases that pass while fitted `W_c` fails.
3. Define a quantitative criterion for "B_bulk tracks control variable more strongly than I_phi/W_c" so alternative explanations can be excluded rather than merely listed.
4. Keep every `I_phi` threshold label tied to the declared `W_z2 -> E_z2` calibration and the `E_floor = 0.25/0.5/1.0 meV` sensitivity sweep.
5. Mark the protocol as semi-quantitative and uncalibrated until same-sample pressure/strain/pump/oxygen data measure `W_c` or `sigma_c`, `B_bulk`, Hall number, domain fraction, oxygen stoichiometry, and ab Drude controls on the same tuning axis.

---
