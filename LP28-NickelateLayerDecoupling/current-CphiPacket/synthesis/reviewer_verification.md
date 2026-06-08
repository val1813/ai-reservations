# Reviewer Verification: LP28-CphiPacket

Date: 2026-06-05

## Trigger

Round 3 REVIEWER returned `REJECT` and requested independent PI verification.

## WebSearch Result

No exact prior found for:

`P_oe + B_min + row firewall + R_oe`

or a row-level identifiability packet with the same residual-collapse framing.

Important adjacent records found:

- Nature 2026: `Uncovering origins of heterogeneous superconductivity in La3Ni2O7`, DOI `10.1038/s41586-025-10095-x`.
- Nature Communications 2024: `Electronic and magnetic excitations in La3Ni2O7`, DOI `10.1038/s41467-024-53863-5`.
- Nature Communications 2024: `Electronic correlations and partial gap in the bilayer nickelate La3Ni2O7`, DOI `10.1038/s41467-024-52001-5`.
- npj Quantum Materials 2024: `Absence of electron-phonon coupling superconductivity in the bilayer phase of La3Ni2O7 under pressure`, DOI `10.1038/s41535-024-00689-5`.
- Nature Communications 2024: `Density-wave-like gap evolution in La3Ni2O7 under high pressure revealed by ultrafast optical spectroscopy`, DOI `10.1038/s41467-024-54518-1`.
- Nature Communications 2024: `Orbital-dependent electron correlation in double-layer nickelate La3Ni2O7`, DOI `10.1038/s41467-024-48701-7`.

## PI Verification Decision

Reviewer rejection is accepted as a valid fatal attack on the current state:

The packet protocol has no real audited pilot row. Without at least one real row passing the firewall, `PACKET_FEASIBLE_NEAR_FUTURE` remains speculative.

This does not kill `R_oe` universally, but it pushes LP28-CphiPacket into forced salvage under SOP.

## Forced Salvage Target

Minimum salvage condition:

one audited pilot row or formally sistered row that can demonstrate:

- immutable raw archive exists;
- `P_oe` and `B_min` extraction can be separated;
- canonical `P_oe` censoring and `U_miss` are frozen;
- output labels are sealed;
- green/yellow/red firewall can be applied before reveal.

If this cannot be specified from real facility/data constraints, CphiPacket must close as rejected protocol packaging.
