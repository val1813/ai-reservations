# PI Synthesis: LP28-CphiPacket Forced Salvage 2

## Inputs

- A Salvage 2: `current-CphiPacket/A/salvage2.json`
- B Salvage 2: `current-CphiPacket/B/salvage2.json`
- PI independent WebSearch verification for Diamond I21 / ICAT-Topcat route

## Core Result

Forced salvage did not produce a green `PILOT-001` row.

It did produce a real contactable acquisition route:

Diamond Light Source I21 RIXS + Diamond raw-data archive / ICAT-Topcat custody path.

This rescues the work only as:

`REAL_CONTACTABLE_DOSSIER_ROUTE`

not as:

`SALVAGE_SUCCESS`

and not as:

`R_oe` evidence.

## Independent Verification

Verified at high level:

- Diamond Light Source I21 is a real RIXS beamline.
- La3Ni2O7 RIXS work has used I21.
- Diamond has data/archive mechanisms that can plausibly anchor immutable raw-data custody.

Not verified:

- Diamond would agree to the exact blinded `PILOT-001` custody workflow.
- raw archive would include all calibration/covariance artifacts required by the packet.
- same-sample or formally sistered La3Ni2O7 pieces are available.
- output labels can be sealed before row lock.

## Final Salvage State

`CONDITIONALLY_KEEP_AS_CONTACTABLE_DOSSIER`

This means:

- keep the dossier as a concrete experimental contact plan;
- do not continue theoretical/protocol elaboration without new external data or facility confirmation;
- do not claim packet feasibility beyond contactable route;
- do not claim the reviewer `REJECT` is fully overturned.

## B Boundary Accepted

B is right:

If no real `PILOT-001` source/row is named, template is not enough.

A named a plausible real source route, so the result is not pure template. But until facility/custody acceptance exists, the row remains absent.

## Next Practical Artifact

Write and use a `PILOT-001 dossier template` for external acquisition:

- facility: Diamond I21 or equivalent RIXS facility;
- sample lineage: same-boule La3Ni2O7 or formally sistered pieces;
- raw archive: immutable URI/checksum manifest;
- extraction separation: independent `P_oe` and `B_min` workspaces;
- lock sequence: canonical `P_oe`, `B_min`, `U_miss`, censoring, firewall before reveal;
- output custodian: superconducting labels sealed until packet lock.

## Close/Continue Decision

The current north star cannot continue with more internal reasoning.

Continue only if the next step is external dossier execution or acquisition planning.

Otherwise close `LP28-CphiPacket` as:

`bounded contactable protocol; green pilot row not yet obtained`.
