# LP29-C2T contradiction deepening

Date: 2026-06-04

## Surface contradiction

Why can C2T define schema, source inventory, blockers, witness payloads, and gate predicates, yet still produce no material-validation row?

## Five whys

1. Why does a filled or fillable joined table not suffice?

Because field presence is not provenance validity. A row can contain material name, label, OI context, and graph placeholders while still lacking same-sample identity and independent provenance.

2. Why is same-sample identity not recoverable from material names or composition?

Because amorphous materials have process, snapshot, batch, density, defect, and measurement-history dependence. The same formula or family can correspond to different structures and transport labels.

3. Why is external label independence a gate rather than a metadata nicety?

Because transport labels, carrier density, effective mass, mobility-edge margin, graph convention, and row inclusion can leak target information if selected after label exposure or derived from the same fit.

4. Why does leakage destroy the validation object rather than merely weaken confidence?

Because the tested claim is residual independence beyond Srivastava/OI and controls. If the row identity or controls are target-derived, the residual comparison becomes circular: the row is no longer an external test.

5. Why must the row carry a proof object?

Because the validity condition is temporal and relational, not scalar. It depends on ordering (protocol before label), independence (label external to graph), same-sample crosswalk, forbidden paths, and baseline reproduction. These cannot be inferred from table values alone; they require witness payloads and gate predicates.

## Deep contradiction

Proposition A: In materials-informatics validation, a table row with values for descriptors, controls, and labels is a valid scientific unit if the columns are present and sourced.

Proposition B: In cross-source amorphous-material validation, a row is valid only if it carries an executable admissibility proof establishing same-sample identity, temporal non-circularity, external label independence, graph-protocol lock, forbidden-control cleanliness, and baseline reproduction status.

These cannot both be sufficient criteria. If A is sufficient, C2T witness gates are overengineering. If B is required, many apparently complete joined rows are not validation objects.

## Basic-principle layer

The root issue is not missing data. It is **object identity under evidence composition**:

> When a scientific claim is tested by composing evidence from multiple sources, the composed object must carry a proof that its identity and independence survived composition.

For LP29-C2T, the scientific object is therefore not a row; it is a proof-carrying row.

## Current unknown

The deepest unknown is whether this proof-carrying-row requirement is merely a conservative engineering standard, or a necessary condition for any credible graph-vs-OI external validation in amorphous materials.
