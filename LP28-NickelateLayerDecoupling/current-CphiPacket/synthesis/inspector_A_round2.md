# INSPECTOR Report: A Round 2

Review target: `current-CphiPacket/A/round2.json`

Scope constraint: reviewed A Round 2 only. Did not read B output. This is not PI synthesis.

## Overall Verdict

WARNING

A Round 2 fixes the major Round 1 protocol drift and is now a plausible prospective packet schema. It should not be treated as evidence that a packet exists, that `C_phi` is independent, or that `R_oe` is supported. The remaining risks are not cosmetic: the proposed N/batch thresholds are minimum executability gates, the `B_min`/`P_oe` firewall is still vulnerable around qz/c-axis/matrix-element proxies, and matched-sibling rules still require a stricter pre-output mismatch bound to avoid montage.

## 1. `P_oe` Definition Drift

PASS

A now separates canonical `P_oe` from the L1 diagnostic:

- Canonical: `P_oe = (chi_odd - chi_even) / (chi_odd + chi_even)`.
- Denominator floor is used only for censoring through `epsilon_D`; it does not replace the denominator.
- `P_oe_L1_diagnostic` is explicitly named as diagnostic-only and cannot drive primary residual calls, row choice, thresholds, or post-reveal denominator floors.

Residual warning: `epsilon_D` provenance must be auditable from susceptibility-channel noise/calibration artifacts only. Any future use of structural, Raman, oxygen, pressure-path, residual-collapse, or output behavior to tune `epsilon_D` is a protocol failure.

## 2. `row_schema` Executability

PASS

The row schema is concrete enough to execute prospectively. It specifies row identity, sibling genealogy, frozen grids, raw spectra URIs, calibration files, `chi_odd/chi_even`, channel-mixing covariance, B_min axes, missingness buckets, output custodian, and unlock conditions.

Warning: some B_min entries remain proxy families rather than named instruments/acceptance metrics, especially ordinary c-axis coherence and ligand-hole/orbital proxies. This is acceptable for a design packet, but PI should require a per-facility acquisition ledger before calling it executable in practice.

## 3. Thresholds: N=24 / 18 Valid Rows / 2 Batches

WARNING

The thresholds are reasonable as an executability floor but too low for a strong claim-bearing residual-collapse result.

- `N_total_rows >= 24` and `>=18` valid uncensored `P_oe` rows are acceptable as a minimum serious attempt, not as evidence strength.
- `minimum_growth_batches = 2` is the weakest defensible replication gate; preferred should be treated as operationally `3`, not merely optional, if PI wants a primary claim.
- `valid_rows_per_pressure_landmark = 6` and hard fail below 3 are fragile under censoring, pressure-gradient mismatch, and sibling uncertainty.
- Pilot `N=12` must remain machinery-only. It must not be allowed to produce residual-collapse claims.

PI synthesis should preserve the distinction:

- `N=12`: packet rehearsal only.
- `N=24/18 valid/2 batches`: minimum executable protocol only.
- Strong claim: needs either larger N, 3 batches, or an explicit power/sensitivity analysis showing residual-scale detectability under `U_miss`.

## 4. Probe Order and Output Embargo

PASS

The probe order is leakage-aware:

- pre-registration before measurement,
- B_min and pressure-path covariates before `P_oe`,
- packet lock before output reveal,
- output custodian separated from extractors,
- superconducting labels and output-trained human/model labels embargoed.

Warning: file names, specimen names, lab notes, and known "successful" pressure/sample choices are correctly named as leakage risks, but the implementation needs an audit log requirement. Without timestamped selection logs and blinded IDs, the written embargo is not enough.

## 5. `B_min` / `P_oe` Firewall and qz/c-axis Pollution

WARNING

The firewall is much harder than Round 1 and explicitly bans odd/even residuals, qz/polarization/form-factor nuisance parameters, RIXS backgrounds optimized for odd/even separation, and post-residual covariate selection.

Remaining risk: ordinary c-axis coherence is intrinsically close to the qz physics used to construct `P_oe`. If c-axis proxies come from the same RIXS/neutron session or share matrix-element corrections with odd/even extraction, they can become same-source leakage.

Required PI constraint:

- Primary `B_min` ordinary c-axis covariates should come from independently acquired normal-state optical/transport/structural probes where possible.
- Same-session RIXS-derived non-`P_oe` c-axis proxies must be sensitivity-only unless an audit proves they are extracted from independently defined spectral regions/standards and do not use odd/even fit nuisance terms.
- If `B_min` cannot be reproduced with `P_oe` spectra and fit parameters hidden, the packet is `PACKET_NONIDENTIFIABLE`.

## 6. Same-Sample vs Sister-Specimen Montage Risk

WARNING

A has real anti-montage rules: same-sample preferred/required when nondestructive or pressure path is tested; siblings allowed only for destructive or unavailable same-sample measurements; genealogy, oxygen/phase mapping, pressure ledger, and `U_miss` must be frozen.

However, the hard-fail criterion still references whether sibling uncertainty is comparable to the observed `P_oe` residual scale. That can become post-hoc unless the residual scale or admissible mismatch bound is pre-registered before output reveal and before residual analysis.

Required PI constraint:

- Define a pre-output sibling mismatch tolerance in physical covariate units and in the planned residual-scale units.
- If sibling oxygen microtexture, phase fraction, damage, pressure-path, or c-axis-state uncertainty exceeds that frozen tolerance, exclude the row before output reveal.
- Do not rescue a montage row by inflating `U_miss` after seeing residual behavior.

## 7. Claims: Feasibility vs Overclaim

PASS with WARNING

A mostly avoids overclaiming. It repeatedly states:

- existing data are `PACKET_NOT_FOUND`,
- the design is prospective,
- no measured packet exists,
- no `R_oe` validation follows,
- executable status requires thresholds and audits.

Warning: the label `PACKET_FEASIBLE_NEAR_FUTURE` is acceptable only if PI reads it as "internally coherent prospective protocol." It should not be used as "experimentally feasible at current facilities without facility-specific confirmation." Same-sample high-pressure `P_oe` spectroscopy remains a load-bearing practical assumption.

## Must Pass To PI Synthesis

1. A Round 2 should be accepted with WARNING, not blocked.
2. `P_oe` definition drift is fixed: canonical `P_oe` and `P_oe_L1_diagnostic` are now separated correctly.
3. `row_schema` is executable as a prospective design, but PI must demand facility-specific acquisition ledgers before treating it as operationally executable.
4. N thresholds are minimum gates only. `N=24`, `18` valid rows, and `2` batches are too low for strong claims without power/sensitivity analysis; `N=12` is rehearsal-only.
5. Output embargo and probe order are structurally sound, but require timestamped blinded-ID audit logs to prevent hidden leakage through names, notes, or known successful samples.
6. The `B_min`/`P_oe` firewall remains the decisive risk. qz/c-axis/matrix-element same-source contamination must demote affected covariates to sensitivity-only or make the packet non-identifiable.
7. Same-sample/sibling rules reduce montage risk but need pre-output mismatch tolerances. Post-hoc comparison to observed residual scale is not sufficient.
8. PI should preserve the allowed claim boundary: A supports prospective packet feasibility under hard schema, not measured packet existence and not `R_oe` evidence.

--- Feed To Next Round ---

Must fix or harden:

1. Treat `N=24/18 valid/2 batches` as an executable-protocol floor only; require stronger N/batch/power justification for claim-bearing residual inference.
2. Add explicit pre-output sibling mismatch tolerances; do not rely on post-hoc residual-scale comparison.
3. Demote same-session qz/c-axis/RIXS-derived `B_min` proxies to sensitivity-only unless independently reproducible with `P_oe` spectra and odd/even nuisance terms hidden.

Recommended:

1. Add timestamped blinded-ID audit logs for row selection, file naming, lab notes, and threshold freezes.
2. Convert remaining proxy families into facility-specific acquisition routes and acceptance metrics before calling the packet operationally executable.
