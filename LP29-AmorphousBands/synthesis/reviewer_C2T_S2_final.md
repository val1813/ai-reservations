# LP29-AmorphousBands C2T/S2 final REVIEWER

Date: 2026-06-04

Role: independent final REVIEWER. Scope limited to PI final, N=3 reviewer report, and independent paper-search-mcp checks. The project Phase checklist was not modified.

## 0. Final claim boundary check

PI final currently preserves only the bounded admissibility claim:

> Srivastava 2019 can be used as reported orbital-overlap/effective-mass context, but cannot currently be used as a reproduced exact `O_s` baseline for residual validation.

This is admissible as a bounded closeout, not as a materials-physics discovery. The final text explicitly blocks exact reproduction, material validation, graph-vs-overlap residual regression, graph beats overlap, and an in-principle impossibility/no-go claim. That is the right boundary.

No equation-level dimensional audit is applicable here because the final claim is an evidence/provenance admissibility claim rather than a new quantitative formula.

## 1. Three-round search table

| Round | Purpose | paper-search-mcp queries/tools | Main hits | Judgment |
|---|---|---|---|---|
| 1 | Method-layer duplicate search | `search_papers`: `Srivastava 2019 amorphous semiconductor orbital overlap effective mass OI_norm exact reproduction baseline`; `amorphous materials orbital overlap effective mass pair cutoff overlap sum normalization reproducibility baseline`; `search_crossref`: `10.1063/1.5096042 orbital overlap effective mass amorphous` | Srivastava et al., *Electronic structure and transport in amorphous metal oxide and amorphous metal oxynitride semiconductors*, arXiv:1812.11333 / DOI 10.1063/1.5096042; Karamad et al., OGCNN, arXiv:2008.06415 | Srivastava supports reported orbital-overlap/effective-mass context. No hit supports using reported `OI_norm` as a reproduced exact `O_s` baseline. |
| 2 | Framework blind-spot search | `search_papers`: `reported descriptor exact reproducible baseline missing provenance coordinates cutoff normalization materials informatics`; `materials informatics reproducibility missing structure provenance descriptor benchmark metadata workflow 2024 2025 2026`; `amorphous semiconductor mobility conduction path s orbital overlap effective mass validation reproducibility` | Workflow/provenance/metadata results including Hasan dissertation, Alper et al. LabelFlow, Alberi et al. materials-by-design roadmap | Search supports the need to separate descriptor reporting, metadata, workflow trace, and validation. It does not support material validation from the Srivastava rows. |
| 3 | Negative / criticism search | `search_papers`: `amorphous oxide semiconductor orbital overlap effective mass criticism failure counterexample Srivastava`; `materials informatics reproducibility failure missing provenance structure descriptor criticism counterexample`; `descriptor reproducibility materials science missing metadata benchmark failure exact reproduction disproof counterexample`; `search_arxiv`: `workflow provenance reproducibility analysis data differencing` | Missier et al., *Provenance and data differencing for workflow reproducibility analysis*, arXiv:1406.0905; RSC review records on materials-informatics reproducibility | No direct counterexample/no-go shows exact `O_s` is impossible in principle. The live risk is evidence promotion, not physics impossibility. |

Additional metadata check: `search_arxiv 1812.11333` found Srivastava arXiv metadata and abstract; `search_papers` found DOI 10.1063/1.5096042 metadata. `get_crossref_paper_by_doi` returned empty, but this was not a no-result condition for the overall paper-search-mcp search because other paper-search-mcp tools returned the paper.

Three-round judgment: search passed. No direct prior work was found that already publishes the exact same bounded closeout claim. No source was found that licenses the forbidden stronger claims.

## 2. Five rejection/attack points or remaining risks

1. Evidence-level promotion remains the fatal failure mode if any downstream text says Srivastava exact `O_s` was reproduced. A reported orbital-overlap descriptor is not an executable same-structure baseline without source row/page, structure identity, coordinates/hash, pair cutoff/list, `N_pair`, raw sum, normalization, and executor trace. [fatal]

2. The final claim is acceptable only because it is a block under current evidence. If the text drifts into "exact `O_s` is impossible in principle", it converts a provenance gap into a false no-go theorem. [serious]

3. Material validation is still forbidden. Srivastava can contextualize orbital overlap and effective mass, but cannot validate LP29 graph descriptors or amorphous-band claims without an admitted exact baseline and independent material-level protocol. [serious]

4. Graph-vs-overlap residual regression must remain unrun/unclaimed. A regression against a non-admitted baseline would be circular presentation: the baseline identity is precisely what has not been established. [serious]

5. The proof-carrying contract is a useful closeout artifact, but not a discovery by itself. It should be framed as an admissibility burden for future reproduction, not as evidence that `O_s` outperforms, underperforms, or physically explains transport. [medium]

## 3. Boundary verdict against requested forbidden claims

- exact `O_s` reproduced: not present in PI final; correctly forbidden.
- material validation: not present; correctly forbidden.
- graph-vs-overlap residual regression: not present; correctly forbidden.
- graph beats overlap: not present; correctly forbidden.
- exact impossible in principle: not present; correctly forbidden.

The final synthesis is therefore acceptable only as a bounded reproducibility/admissibility closeout.

## 4. If one fatal error must be chosen

**If one fatal error must be chosen:** treating Srivastava reported `OI_norm` as the same object as a reproduced exact `O_s` baseline without a closed provenance chain over source row, structure identity, pair construction, raw overlap sum, normalization, same-structure mapping, and executor trace.

This is not merely "possibly problematic"; it is the one point I would cite if an editor required a rejection reason.

**Author route out:** submit a targeted provenance package: exact source row/page, structure file and hash, same-structure mapping, pair cutoff, full pair list, `N_pair` provenance, raw overlap sum, normalization formula/code, executable environment, and executor trace. Without that package, keep only `reported_context_only`.

## 5. Tool list

- Round 1: paper-search-mcp `search_papers`, `search_crossref`; no web downgrade.
- Round 2: paper-search-mcp `search_papers`; no web downgrade.
- Round 3: paper-search-mcp `search_papers`, `search_arxiv`; no web downgrade.
- Citation/metadata check: paper-search-mcp `search_arxiv`, `search_papers`, `get_crossref_paper_by_doi`; CrossRef DOI direct lookup returned empty, but arXiv/search_papers returned results, so web search was not used.
- Local files read: `D:\Claude\ai-reservations\AGENTS.md`, `D:\Claude\ai-reservations\ai\CLAUDE.md`, `D:\Claude\ai-reservations\ai\REVIEWER.md`, `synthesis\PI_C2T_S2_final.md`, `synthesis\reviewer_C2T_S2_N3.md`.

## 6. Final recommendation

Recommendation: **accept bounded closeout**.

Reason: PI final now states only the admissible bounded claim: Srivastava 2019 is allowed as reported context, while reproduced exact `O_s` baseline admission is blocked under current evidence. No Round 4 is required unless a future provenance package is submitted for targeted audit.
