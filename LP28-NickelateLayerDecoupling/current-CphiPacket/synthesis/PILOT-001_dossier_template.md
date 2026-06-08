# PILOT-001 Dossier Template

Status: acquisition dossier, not data.

## Facility Route

Primary P_oe route:

- Diamond Light Source I21 RIXS or equivalent odd/even bilayer susceptibility facility.

Archive/custody route:

- facility raw-data archive / ICAT-Topcat or equivalent immutable repository.

## Row Identity

- row_id: `LP28-CphiPacket-PILOT-001`
- material: La3Ni2O7 or explicitly declared bilayer nickelate target
- sample type: same sample preferred; formally sistered adjacent pieces allowed for destructive B_min blocks
- genealogy required: growth lot, anneal, cut order, orientation, storage, transfer log

## Required Raw Archive

- raw RIXS detector frames/spectra
- q/omega/qz/polarization/temperature/pressure metadata
- calibration standards, blanks/darks/backgrounds
- geometry/self-absorption/resolution files
- channel-mixing covariance inputs
- XRD/Raman/pressure marker raw files
- oxygen/valence/orbital raw files for sibling pieces
- normal-state c-axis proxy raw files if used
- extraction code, config, environment lockfile
- SHA256 manifest

## Independent Extraction

P_oe extractor receives only:

- blinded spectra and calibration files
- frozen canonical formula and censoring rule

B_min extractor receives only:

- blinded baseline raw files
- sibling tolerance ledger

Forbidden before packet lock:

- Tc
- zero resistance
- Meissner/diamagnetism
- superconducting gap
- critical current
- superconducting spin resonance
- output-trained labels

## Lock Sequence

Before measurement:

- freeze row ID, grid, denominator floor source, B_min axes, U_miss, sibling tolerances, green/yellow/red firewall

Before output reveal:

- lock P_oe or censor flag
- lock B_min
- lock U_miss
- lock raw archive manifest
- lock firewall classification

After lock:

- output custodian may reveal superconducting labels

## Passing Criterion

`PILOT-001` rescues the current protocol only if it is classified green before output reveal.

Yellow = rehearsal only.

Red = salvage failure.
