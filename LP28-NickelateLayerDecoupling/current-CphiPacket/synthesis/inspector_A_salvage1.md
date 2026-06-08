# INSPECTOR Report: A Salvage 1

Reviewed file: `current-CphiPacket/A/salvage1.json`

Scope: independent inspection of A only. B output was not read. No PI synthesis performed.

## Overall Verdict

**PASS with WARNING.**

A Salvage 1 can recover the prior REVIEWER REJECT only as **bounded technical progress**, not as a full scientific rescue. It converts the objection from "protocol packaging with no executable row" into a concrete one-row pilot route with explicit audit, custody, archive, lock, reveal, and failure conditions.

The REJECT is not overturned by this document alone. It becomes reviewer-facing progress only if `PILOT-001` is actually executed, or if an already existing dossier can satisfy the stated green firewall conditions with real raw archive, custody log, hashes, and pre-reveal lock.

## Findings

### 1. `PILOT-001` Route

**PASS.**

`PILOT-001` is specified as a real executable route rather than a broad protocol restatement. It names the material class, same-sample carrier, sibling pieces, measurement types, pressure-path ledger, odd/even spectroscopy source, facility requirements, and minimum next artifact. The route is still conditional on facility cooperation, but it is operationally defined enough to attempt.

Residual warning: the route does not yet identify an actual booked facility, actual specimen, actual archive URI, or actual row data. That is acceptable for salvage route definition, but not enough for a completed row claim.

### 2. Same-Sample vs Sibling Split

**PASS.**

The same-sample core is concrete: `PILOT-001-A` carries the P_oe spectroscopy, pressure path, structural/quality checks, damage ledger, and optional independent c-axis proxy.

The sibling role is also concrete: `PILOT-001-B` handles destructive or dose-heavy oxygen, valence, ligand-hole, and orbital proxies; `PILOT-001-C` optionally supplies an independent c-axis baseline. The sibling pieces are constrained by same boule, cut sequence, anneal/storage history, and frozen mismatch tolerances.

This directly addresses the reviewer concern that same-sample and sibling evidence were previously blurred.

### 3. Raw Archive / Custody / Lock / Reveal

**PASS.**

The archive requirements are strong enough to answer a protocol-packaging attack at the route level. The file requires raw detector frames or spectra, calibrations, standards, pressure markers, sibling raw files, extraction code, environment lockfiles, checksum manifest, immutable URI or handle, and auditor access before output reveal.

Custody is also explicit: separate sample custodian, P_oe extractor, B_min extractor, firewall auditor, and output custodian. The lock sequence freezes row identity, grids, formula, denominator floor, sibling tolerances, B_min variables, U_miss, firewall rules, and output embargo before reveal.

Important limitation: these are requirements, not evidence that such custody already exists.

### 4. Firewall Test Green Pass

**PASS.**

The firewall test has a clear green pass condition. The row passes only if `PILOT-001` is green before output reveal. Yellow is explicitly rehearsal only and does not rescue the reviewer reject.

The green conditions are meaningful: complete same-sample P_oe archive, valid canonical P_oe or frozen censoring, independently regenerable B_min, sibling tolerance pass, complete pressure/damage ledger, frozen U_miss, and attested absence of superconducting output leakage before lock.

### 5. Failure Without a Real Row

**PASS.**

The file explicitly admits failure if the conditions cannot be met for even `PILOT-001`. It states that without a real archive and custody package, the packet remains rejected protocol packaging and should not be described as packet-feasible.

This is the strongest part of the salvage: it does not hide the absence of a real passing row.

### 6. Claims About R_oe or C_phi

**PASS.**

The claim boundary is appropriately restrained. The file says it does not claim that R_oe exists, that C_phi is independent, or that current literature contains a passing row. The forbidden claims repeat those constraints.

No overclaim of R_oe or C_phi was found.

## Blocking Issues

**None at the route-definition level.**

No BLOCKER was found that prevents A Salvage 1 from being treated as a bounded salvage route.

## Remaining Warning

**WARNING: route-only status.**

A Salvage 1 remains a route specification, not an audited pilot row. A reviewer can still maintain the original REJECT against the scientific packet unless the next artifact is produced: archive accession or immutable URI, SHA256 manifest, custody ledger, locked P_oe extraction, locked B_min extraction, frozen U_miss/censoring table, green firewall classification, packet-lock hash, and output-custodian attestation.

## Final Inspector Judgment

**PASS with WARNING: A Salvage 1 is sufficient to reframe REVIEWER REJECT as bounded technical progress.**

It does not prove the packet, does not establish R_oe, and does not establish C_phi independence. It does establish a concrete, falsifiable, auditable `PILOT-001` route whose failure conditions are explicit.
