# LP29-C2T Re-escalation Draft B

Date: 2026-06-04  
Role: B 博士  
Constraint: did not read A output.

## Killed Claims

Original claim X: existing sources are sufficient to construct provenance-complete same-sample joined rows.  
Killed by: all five current candidates remain `BLOCK`; no row has same-sample crosswalk, graph convention lock, external label independence, forbidden-control audit, and applicable OI/Srivastava reproduction witnesses simultaneously.

Original claim Y: the Round 3 blocker audit is sufficient as the closeout boundary product.  
Killed by: REVIEWER required executable witness payloads, gate predicates, and a deterministic executor before `BLOCK/WARN/PASS` can be reproducible rather than prose-labeled.

Original claim Z: schema/source inventory alone makes `BLOCK/WARN/PASS` reproducible.  
Killed by: schema conformance proves only shape. It does not prove the transition from witness fields to gate status, row decision, or `material_validation_allowed`.

## Larger Claim Now Possible

The larger surviving claim is:

**In amorphous-oxide graph-vs-orbital-overlap validation, the scientific unit is not a joined table row; it is a proof-carrying row whose admissibility must be executable, temporally ordered, and independent of target knowledge before any material-mechanism comparison is meaningful.**

This is larger than the original C2T claim. The original claim asked whether LP29 could assemble provenance-complete external joined rows for this dataset. The re-escalated claim says that for this whole class of materials-informatics comparisons, a row is not eligible for regression until it carries a machine-checkable admissibility proof. The table is demoted from evidence to a container; the witness DAG and executor become the evidence.

## Why the Failure Makes the Larger Claim Plausible

The five `BLOCK` rows are not merely missing data. They reveal a structural category error: a visually complete materials table can still be scientifically inadmissible if row identity, graph protocol, label provenance, forbidden controls, or OI reproduction were assembled after label exposure or through target-aware curation.

Round 4 already points to the stronger object:

- payload schema: row evidence must be represented as machine-readable witness fields;
- gate predicates: `PASS/WARN/BLOCK` must be derived, not declared;
- executor: `material_validation_allowed=true` is reachable only after `row_decision=PASS`;
- actual results: all five current rows remain `BLOCK`, so the infrastructure does not launder failure into validation.

The cross-disciplinary translation is from type systems and proof-carrying code: a material row should not be trusted because it has columns filled in; it should be trusted only when it carries a proof object that the executor can verify. In C2T terms:

```text
schema_conforms(row) != admissible(row)
admissible(row) = executor(witness_payload, gate_predicates)
material_validation_allowed(row) = true only if admissible(row) = PASS
```

## Stronger Form

The next form of C2T should not be just a flat witness payload. It should be a temporal evidence DAG:

- nodes: raw structure source, graph protocol record, label source row, OI formula/code, forbidden-control audit item, row-inclusion decision;
- edges: dependency, derivation, curation, timestamp/order, source authority;
- forbidden paths: target label -> row inclusion, target label -> graph convention, graph proxy -> external label, family/processing screen -> label source selection, manual reconciliation -> same-sample identity;
- pass condition: every required gate has a positive machine-reviewable proof path and no path from target knowledge into any field used to justify admissibility.

Then the first nontrivial prediction is concrete:

**The first future row that appears PASS-like in a normal joined table will probably fail because its evidence DAG exposes post-label curation, protocol locking after target exposure, or material-name/composition identity instead of same-sample identity.**

That is not a boundary-only statement. It is a testable methodological claim about how false validation enters materials ML tables.

## Relationship to the Original Claims

This is at least same-level and likely larger than the original C2T claim:

- original: build provenance-complete same-sample rows;
- re-escalated: define the admissibility calculus that decides whether any future row in this problem class can count as a scientific row at all.

It also absorbs the killed claims:

- if sources are sufficient, the proof-carrying executor will emit `PASS`;
- if sources are insufficient, it emits a minimal blocking dependency path;
- if schema/source inventory is insufficient, the witness DAG supplies the missing transition logic;
- if Round 3 prose audit is insufficient, Round 4 executor contract is the minimal infrastructure layer.

## Guardrails

This draft does not claim material validation, Srivastava reproduction, graph-beats-overlap evidence, or same-sample closure. It also does not upgrade any of the five current candidates. The current empirical state remains:

```text
C2T-AUDIT-0001 BLOCK
C2T-AUDIT-0002 BLOCK
C2T-AUDIT-0003 BLOCK
C2T-AUDIT-0004 BLOCK
C2T-AUDIT-0005 BLOCK
material_validation_allowed=false for all five
```

The re-escalation claim is therefore not "we found a boundary." It is:

**C2T has exposed a stricter precondition for materials-mechanism science: before graph spectra can be compared with orbital-overlap baselines, every candidate row must carry an executable, temporally noncircular admissibility proof.**
