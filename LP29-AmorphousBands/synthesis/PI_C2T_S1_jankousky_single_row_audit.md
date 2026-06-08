# PI: C2T-S1 Jankousky single-row audit

Date: 2026-06-04

## Candidate row

- row_id: `C2T-AUDIT-0101`
- source: local PDF `D:\文献\Nature Physics 2026\Nature Physics 2026.01\s41567-025-03099-x.pdf`
- DOI: `10.1038/s41567-025-03099-x`
- article: Jankousky et al., `Effective bands and band-like electron transport in amorphous solids`

## Local evidence extracted

PDF text extraction artifact:

`current/C2T/artifacts/jankousky_pdf_text_extract.txt`

Useful evidence:
- lines 1-3: Nature Physics article and DOI.
- line 58: published online 17 November 2025.
- lines 606-658: method-level generation of 1,500 random In2O3 structures with 40 atoms per unit cell and structure relaxation details.
- lines 660-669: QSGW subset of 100 structures selected to approximate ensemble averages.
- lines 518-523: online content/data/code availability points to DOI page.

## Executor payload and result

- payload: `current/C2T/artifacts/C2T_jankousky_single_row_payload.jsonl`
- result: `current/C2T/artifacts/C2T_jankousky_single_row_result.csv`

Executor output:

`row_decision=BLOCK`

`material_validation_allowed=false`

## Reason

The paper provides strong method-level and effective-band context, but the locally available PDF does not provide a machine-reviewable same-sample row with:

- stable raw structure coordinates / `structure_id`
- `snapshot_id_or_window`
- label provenance tied to the same graph row
- locked graph convention provenance
- external label independence witness

## Boundary

This is a machine-reproducible blocker witness, not a material-validation row.

## Next unblock action

Attempt to retrieve supplementary/source data linked from the DOI page or author repository. If raw structures or source-data rows are obtained, rerun the same witness payload with updated machine-reviewable evidence.

