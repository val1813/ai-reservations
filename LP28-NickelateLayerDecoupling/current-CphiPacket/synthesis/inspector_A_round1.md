# INSPECTOR A Round 1

Status: WARNING

Scope: only `current-CphiPacket/A/round1.json` was inspected. This report is for PI synthesis, not PI synthesis itself.

## Verdict

A Round 1 is useful and mostly disciplined: it does not claim an existing leakage-clean nickelate packet, and it correctly frames the strongest route as a new coordinated same-boule / matched-specimen campaign. However, it should not be treated as a pass for executable `R_oe`. The packet remains a near-future protocol, not an existing data object, and the most important unresolved issue is whether `B_min` can be extracted independently of the same qz/c-axis/matrix-element machinery that generates `P_oe`.

## Checks

1. Existing packet vs near-future route: PASS

A explicitly says existing literature supplies components, not the complete packet, and reports no published same-sample or matched-specimen dataset containing calibrated qz/polarization odd/even susceptibility plus full `B_min` before superconducting-output reveal. This is not overclaimed as `PACKET_FEASIBLE_NOW`.

PI synthesis should preserve this wording. Any stronger claim would be unsupported.

2. `P_oe` formula, denominator floor, units: WARNING

Previous north-star formula in the project queue was:

`P_oe = (chi_odd - chi_even)/(chi_odd + chi_even)`

A Round 1 uses:

`P_oe = (chi_odd - chi_even) / max(abs(chi_odd) + abs(chi_even), epsilon_floor)`

This is dimensionally valid only if `chi_odd`, `chi_even`, and `epsilon_floor` are in identical calibrated susceptibility units; the result is dimensionless. The censoring rule for rows with `abs(chi_odd)+abs(chi_even) < epsilon_floor` is also directionally correct.

But this is a definition change, not a harmless implementation detail. The new denominator is positive and L1-like, while the old denominator could approach zero or change sign depending on the channel sum. It stabilizes the observable but makes values not directly comparable to the previous `P_oe` unless the project explicitly renames it, redefines all prior claims, or proves equivalence in the intended positive-susceptibility domain.

Additional warning: A says pressure Raman/structure rows can help with "denominator floor construction." That is dangerous unless it only informs row censoring or pressure-state metadata. The denominator floor itself must come from susceptibility-channel noise, channel-mixing uncertainty, standards, blanks, and calibration residuals in the same units as `abs(chi_odd)+abs(chi_even)`. Structural/Raman quantities have different units and can become circular if they encode the same pressure/phase variables later used in `B_min`.

3. `B_min` independence from `P_oe`: WARNING

A proposes separate teams/locked scripts and anonymized row IDs, which is necessary. It is not sufficient.

Several `B_min` substitutes are plausibly independent of superconducting output but not automatically independent of `P_oe` extraction: lattice geometry, orbital/ligand-hole structure, pressure path, and especially ordinary c-axis coherence can shape the qz-dependent spectral weight, RIXS matrix elements, and odd/even channel decomposition. If these baselines are extracted from the same spectra, same qz model, same pressure-cell correction, or same matrix-element fit used for `P_oe`, the residual can be manufactured by allocation choices.

PI synthesis should require a hard rule: `B_min` may use independently acquired pre-output covariates, but it cannot reuse target-generating qz/polarization/form-factor residuals, RIXS background parameters, odd/even channel-mixing terms, or calibration nuisance parameters from the `P_oe` fit.

4. Same-sample / matched-specimen feasibility: WARNING

The same-sample route is not yet an executable packet. Sequential non-destructive baseline -> pressure Raman/XRD/XAS -> qz-resolved RIXS -> sealed output is experimentally attractive but beamline/sample-environment limited, especially under high pressure.

The matched-specimen route is more realistic, but it is only valid if "same-boule sibling" really preserves oxygen microtexture, phase fraction, damage history, pressure gradient, pressure medium effects, and thermal cycling well enough for row-level inference. Otherwise it becomes a montage of related specimens rather than a same-row packet.

A recognizes this fragility in `U_miss` and failure modes, so this is a warning rather than a blocker. But PI synthesis should state that current literature assembly is montage; only a newly registered row-level campaign could escape that.

5. `missing_fields` classification: WARNING

A's split between engineering gaps and protocol failures is mostly reasonable, but it is too lenient in three places:

- "Published same-row qz-resolved odd/even susceptibility with raw calibration files" is an engineering gap only for planning a future campaign; it is a protocol blocker for any claim that `R_oe` can already be killed or preserved.
- "Beamline-compatible high-pressure RIXS or validated matched-pressure transfer design" is a protocol blocker if pressure is part of the tested row, not merely engineering friction.
- "Matched-sibling oxygen microtexture maps tied to spectroscopy row IDs" becomes a protocol blocker if sibling mismatch is of the same order as the proposed `P_oe` residual.

The `dangerous_if_missing` list is strong and should be carried forward.

6. References / DOI sanity: WARNING

Main resolved references look plausible:

- `10.1038/s41467-024-53863-5`: resolves as "Electronic and magnetic excitations in La3Ni2O7."
- `10.1103/physrevb.109.l180502`: resolves as PRB theory of magnetic excitations in La3Ni2O7.
- `10.1038/s41586-024-07482-1`: resolves as oxygen vacancies / ligand holes in La3Ni2O7.
- `10.1038/s41467-024-52001-5`: resolves as electronic correlations and partial gap.
- `10.1038/s42005-025-02266-z`: resolves as pressure and apical oxygen-vacancy theory.

References needing PI follow-up:

- `10.21203/rs.3.rs-5326664/v1` and `10.21203/rs.3.rs-7347905/v1` are Research Square posted-content records, not peer-reviewed final journal anchors.
- `10.1021/acs.jpcc.5c07252.s001` resolves as an ACS supplementary-information component, not a main article DOI; PI should locate and cite the parent article DOI if using it as evidence.
- `arXiv:2406.04837` and `arXiv:2511.15265` did not resolve through the local arXiv MCP query during this check; PI should verify exact IDs/titles before relying on them.

7. Real progress potential vs wish list: PASS with warning

A is not merely a wish list. It turns the problem into a concrete packet architecture with row schema, output embargo, denominator floor, calibration controls, missingness buckets, and pilot/preferred row counts. That is real protocol progress.

The remaining gap is not "do more experiments" in the vague sense; it is one specific identifiability test: after independent, pre-output `B_min` and `U_miss` are locked, does `P_oe` retain residual variance under a non-circular denominator and raw calibration audit?

## Must Pass To PI Synthesis

1. A should be summarized as `PACKET_FEASIBLE_NEAR_FUTURE`, not `PACKET_FEASIBLE_NOW`.

2. The `P_oe` formula has drifted from the previous north-star formula. The stabilized version may be better, but PI must explicitly standardize the definition before comparing across rounds.

3. The denominator floor is valid only if it is in susceptibility-denominator units and derived from calibration/noise/channel-mixing/blank residuals. Structural/Raman pressure information must not become a hidden denominator tuner.

4. `B_min` is not proven independent of `P_oe`. The major open risk is qz/c-axis/matrix-element leakage from the `P_oe` extraction pipeline into baseline covariates.

5. Current literature is component evidence only. A retrospective montage cannot kill or preserve `R_oe`.

6. Matched-specimen design is feasible only with strong row identity controls: oxygen microtexture, pressure path, phase fraction, beam damage, thermal cycle, and batch replicate.

7. Some A "engineering gaps" become protocol failures the moment the claim moves from future campaign design to actual residual-collapse inference.

8. Citation hygiene needs follow-up for Research Square records, the ACS SI DOI, and the two arXiv IDs.

Final status: WARNING. No hard blocker against using A as a Round 1 route map, but there is a blocker against treating it as evidence that `R_oe` can already be killed or preserved.
