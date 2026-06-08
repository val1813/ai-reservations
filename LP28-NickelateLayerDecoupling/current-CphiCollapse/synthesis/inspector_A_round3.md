# INSPECTOR Report: A Round 3

Scope: inspected `current-CphiCollapse/A/round3.json` only. Did not read B outputs. `validation/` directory was not present, so checks were performed manually under INSPECTOR Q1-Q6.

Overall verdict: WARNING

## PASS

1. Formula dimensions and numerical tests are internally consistent.
   - `P_oe = (chi_odd - chi_even)/(chi_odd + chi_even)` is dimensionless if `chi_odd` and `chi_even` are extracted in identical calibrated `chi_unit`.
   - Test: `(1.4 - 0.8)/(1.4 + 0.8) = 0.2727`, matching `[0.27, 0.28]`.
   - `D_floor = max(5*sigma_chi_sum, 10*B_chi, 0.02*median_abs_chi_sum_reference)` has `chi_unit`; test gives `max(0.05, 0.03, 0.04) = 0.05`.
   - `R_oe = P_oe - E_hat[P_oe | B_min]` is dimensionless; test `0.31 - 0.24 = 0.07`.
   - `sigma_R_oe = sigma_P_oe*sqrt(1 - max(0,min(CV_R2,1)))` is dimensionless; test `0.2*sqrt(0.25)=0.1`.

2. Direction and limiting behavior are correct.
   - Equal odd/even channels give `P_oe = 0`.
   - Pure odd channel gives `P_oe -> 1`; pure even channel gives `P_oe -> -1`.
   - If baseline prediction equals `P_oe`, `R_oe -> 0`, which is correctly interpreted as collapse.
   - Negative `CV_R2` is not allowed to inflate the residual claim; it is clipped to zero only for uncertainty propagation.

3. Denominator censoring mostly avoids artificial `P_oe`.
   - Rows below floor are censored, not regularized with epsilon.
   - Censored rows are excluded from survival, collapse, and gray-zone decisions and reported separately as non-identifiable.

4. Temperature leakage control is substantially improved.
   - Fixed grid `[120, 150, 200] K` avoids same-row `Tc + delta`.
   - Same-row `Tc_onset`, zero resistance, Meissner, diamagnetism, gap fits, spin resonance, and output-trained classifiers are explicitly forbidden.
   - Historical phase diagram use is allowed only if frozen before row ranking and not updated from packet superconducting outcomes.

5. `B_min` is not obviously tautological.
   - `P_oe`, `chi_odd - chi_even`, odd/even kernel residuals, superconducting labels, and output-trained latent quality scores are excluded.
   - Included blocks are ordinary input-side baselines: oxygen/asymmetry, strain/lattice, orbital self-doping, disorder/dephasing, pressure path, c-axis coherence, and sample quality.

6. Small-N, gray-zone, and negative `CV_R2` handling are mostly qualified.
   - `N < 12` is design-only unless a prespecified low-dimensional fallback exists.
   - `12 <= N < 20` is not allowed to produce a full claim.
   - `0.65 < CV_R2 < 0.85` is treated as gray-zone unless matched-pair inversion plus independent holdout replication exists.

## WARNING

1. Denominator floor has a mild circularity risk.
   - `median_abs_chi_sum_reference` is defined across "admissible reference rows", but admissibility itself depends on the denominator floor.
   - This does not currently manufacture `P_oe`, because failed rows are censored, but the reference set should be frozen by an external calibration set or computed by a preregistered robust first pass that does not depend on the final floor.

2. `chi_definition` still hides a unit convention.
   - `chi_channel = integral S_channel/max(omega,omega_IR) d_omega` is acceptable only if `S_channel` has been calibrated so the resulting integral has `chi_unit`.
   - Round 3 says this in prose, but the protocol should require the raw-to-`chi_unit` calibration map explicitly before denominator and uncertainty propagation are trusted.

3. Survival thresholds remain candidate-level, not discovery-level.
   - The table correctly forbids "validated universal predictor" claims, but `SURVIVES_AS_CANDIDATE_VARIABLE` could still be over-read.
   - PI synthesis should preserve the weaker wording: survival means only "independent input-side residual candidate in this packet", not evidence that C_phi predicts superconductivity.

4. Collapse criterion is useful but not theorem-level.
   - `CV_R2 >= 0.85`, small residual magnitude, and no matched-pair inversion justify packet-level collapse.
   - They do not prove no possible C_phi definition exists; Round 3 states this correctly, and synthesis must not strengthen it.

5. Pressure as a `B_min` covariate is allowed but needs care in matched-pair design.
   - Including `pressure_GPa` is not tautological, but if the intervention axis is pressure-induced parity transfer, overly tight pressure calipers may make the desired contrast impossible, while loose pressure calipers may let pressure path explain the effect.
   - The caliper and intervention axis must be frozen before looking at `P_oe` ranks.

6. This is still mostly a protocol until the same-sample packet exists.
   - A true contradiction is now defined: matched `B_min` plus stable residual rank inversion preserves `R_oe`; high CV baseline prediction plus no inversion collapses it.
   - However, Round 3 explicitly lacks the same-sample q_z odd/even susceptibility plus full `B_min` packet, so no empirical survival or collapse has been demonstrated.

## BLOCKER

No blocker found in A Round 3 as a protocol document. The formula layer, leakage exclusions, denominator censoring, small-N safeguards, and claim limits are adequate for PI synthesis if warnings are carried forward.

## Must Pass To PI Synthesis

1. A Round 3 passes as a leakage-controlled go/no-go protocol, not as evidence that `R_oe` exists.
2. The core falsifiable contradiction is real enough to preserve: either `B_min` predicts `P_oe` and eliminates matched-pair inversions, or a signed, temperature-stable `R_oe` rank inversion remains after matched baselines.
3. PI must keep all claims packet-level and candidate-level.
4. PI should require a non-circular denominator reference rule before execution.
5. PI should require explicit raw-intensity-to-`chi_unit` calibration before treating `P_oe` uncertainty or censoring as valid.
6. Current status: no same-sample pressure packet, so no survival/collapse call yet.

--- 投喂下一轮 ---

必须修正（阻断级）:
1. None.

建议修正（警告级）:
1. Define `median_abs_chi_sum_reference` from an external/frozen calibration set or a preregistered non-circular robust first pass.
2. Specify the raw `S_channel -> chi_unit` calibration and uncertainty propagation before denominator censoring.
3. Preserve candidate-level language: `R_oe` survives only as an input-side residual candidate in a packet, not as a superconductivity predictor.
4. Freeze pressure-path calipers and intervention axes before inspecting `P_oe` ranks.
5. Do not make any empirical survival/collapse call until a same-sample packet contains q_z-resolved odd/even susceptibility and all `B_min` blocks.
---
