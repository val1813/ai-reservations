# REVIEWER: LP29-C2T Round 3 Forced Review

Role: Nature Physics anonymous hostile reviewer  
Input scope: only the supplied core conclusion list plus `current/C2T/artifacts/C2T_row_level_audit_record_round3.csv`; no A/B derivation text read.  
Verdict: **reject as a North-Star closing boundary product; require Round 4 executor/witness payload schema before closure.**

## Step 0: AI Hallucination Check

No dimensional formula, numerical scaling claim, or physical directionality claim was supplied. The check therefore reduces to provenance-loop and claim-scope inspection.

- Circular-validation risk: present. The artifact blocks all rows, so it does not validate material claims; any wording that treats it as validation is circular over the audit design itself.
- Quantity-gap risk: not applicable from the supplied input.
- Directionality risk: not applicable from the supplied input.
- Claim-scope risk: severe. A blocker table is being asked to carry the rhetorical role of a closure artifact, but it has no executable witness layer.

## Three-Round Prior-Art Search

### Round 1: Method-Layer Search

Query used with paper-search-mcp: `materials machine learning provenance audit framework joined dataset row-level provenance schema`  
Sources: arXiv, Semantic Scholar, CrossRef, OpenAlex. No Web downgrade.

Relevant hits:

- Zinn and Ludaescher, **"Abstract Provenance Graphs: Anticipating and Exploiting Schema-Level Data Provenance"**, 2010, DOI `10.1007/978-3-642-17819-1_23`.
- Kerzel, Samuel, and Koenig-Ries, **"Towards Tracking Provenance from Machine Learning Notebooks"**, 2021, DOI `10.5220/0010681400003064`.
- Padovani, Anantharaj, and Fiore, **"Yprov4ml: Effortless Provenance Tracking for Machine Learning Systems"**, 2025, DOI `10.2139/ssrn.5226904`.
- Pushkarna, Zaldivar, and Kjartansson, **"Data Cards: Purposeful and Transparent Dataset Documentation for Responsible AI"**, 2022, DOI `10.1145/3531146.3533231`.

Finding: no exact LP29-C2T physical/material conclusion was found, but the general idea of provenance-aware ML/data documentation is already occupied.

### Round 2: Framework-Blind Search

Query used with paper-search-mcp: `dataset documentation provenance machine learning materials science FAIR data audit reproducibility`  
Sources: arXiv, Semantic Scholar, CrossRef, OpenAlex. No Web downgrade.

Relevant hits:

- Samuel, Loeffler, and Koenig-Ries, **"Machine Learning Pipelines: Provenance, Reproducibility and FAIR Data Principles"**, 2021, DOI `10.1007/978-3-030-80960-7_17`.
- Schindler et al., **"Data Documentation Beyond Provenance: Metadata, Research Data Management, FAIR Principles"**, 2024, DOI `10.1007/978-3-031-58468-8_14`.
- Hutchinson et al., **"Towards Accountability for Machine Learning Datasets: Practices from Software Engineering and Infrastructure"**, 2021, DOI `10.1145/3442188.3445918`.

Finding: the plain-language version of C2T, namely "document dataset provenance, blockers, and auditability before ML claims", is not novel. C2T must therefore be defended only as a materials-specific executable gate, not as a general audit framework.

### Round 3: Negative/Conflict Search

Query used with paper-search-mcp: `materials informatics machine learning dataset bias reproducibility benchmark leakage provenance audit`  
Follow-up query: `"Reproducibility in materials informatics" "A general-purpose machine learning framework for predicting properties of inorganic materials"`  
Sources: arXiv, Semantic Scholar, CrossRef, OpenAlex. No Web downgrade.

Relevant hit:

- Persaud, Ward, and Hattrick-Simpers, **"Reproducibility in materials informatics: lessons from 'A general-purpose machine learning framework for predicting properties of inorganic materials'"**, 2024, DOI `10.1039/d3dd00199g`.

Finding: materials informatics already has a recent reproducibility failure literature line. C2T is not protected by being in materials ML; the field already recognizes reproducibility and trust failures as first-class issues.

Three-round conclusion: **no direct duplicate of the exact C2T joined-table blocker contract was found, but the broader provenance/ML-materials-audit space is heavily prior-arted.**

## Narrative-Retreat Warning

The claim has retreated from "material mechanism discovery / graph beats orbital-overlap baseline" to "external joined-table audit contract with all rows BLOCK." That is not scientific progress; it is a failed validation attempt converted into a process artifact. If the authors present this as closure, they are laundering a negative gate as an achievement.

This retreat does not invalidate the blocker table as a negative record. It invalidates treating the blocker table as a North-Star closing product.

## Five Rejection Reasons

1. **No executable witness payload exists.**  
   The CSV records `witness_payload_status`, but provides no witness object, hash, URI, parser, validator, or failed-field evidence. [fatal]  
   Authors must provide machine-readable JSONL/CSV witness rows with deterministic validation rules.

2. **The PASS transition is undefined.**  
   A row can be BLOCK today, but the artifact does not define what exact payload changes convert it to PASS. [fatal]  
   Authors must specify gate predicates for same-sample crosswalk, OI comparison, graph convention, and label independence.

3. **Prior-art pressure reduces novelty to implementation detail.**  
   Data Cards, ML pipeline provenance, dataset accountability, and materials-informatics reproducibility already cover the broad framework. [serious]  
   Authors must isolate the materials-specific delta: exact row-level witnesses for OI/Srivastava/B gates.

4. **The negative audit is not a closure boundary.**  
   Five BLOCK rows prove only that material validation is forbidden; they do not establish a completed external table. [serious]  
   Authors must run an executor on at least one candidate row or explicitly close C2T as a failed branch.

5. **The rhetoric still invites overclaiming.**  
   Terms like "audit contract" and "blocker audit" can be misread as validation infrastructure already working. [medium]  
   Authors must state that no material validation, baseline comparison, reproduction, or same-sample closure is achieved.

## Specific Answer to the Boundary Question

The Round 3 blocker audit is **not sufficient** as the N=3 artifact for entering North-Star closing, unless the project is closing C2T as a negative/failure branch. It is sufficient only for one narrower statement:

> C2T currently has a minimal blocker audit that forbids material-validation claims for all five candidate sources.

It is not sufficient for:

- provenance-complete external joined table,
- material validation,
- Srivastava reproduction,
- graph-vs-OI/orbital-overlap comparison,
- same-sample closure,
- or a closure-grade audit framework.

The mandatory Round 4 should generate an executor/witness payload schema, not another prose audit. Minimum required artifacts:

- `C2T_witness_payload_schema.json`
- `C2T_witness_payload_examples.jsonl`
- `C2T_gate_predicates.csv`
- `C2T_executor_expected_results.csv`
- one deterministic command or script contract that maps witness payloads to `BLOCK/WARN/PASS`

## If I Must Pick One Fatal Error

**If I must pick one fatal error:** the report has a blocker-status CSV but no executable witness payload schema, so `BLOCK/WARN/PASS` is a reviewer-readable label rather than a reproducible audit decision.

This is not "possibly a problem"; this is the single rejection reason I would give the editor if forced to name one.

**Author's exit route:** define machine-readable witness payloads and deterministic gate predicates, then show that at least one row can be independently evaluated from raw witness inputs to the same `row_decision`.

## Recommendation

**Reject as North-Star closure / require major revision as C2T infrastructure.**  
Reason: Round 3 establishes a negative blocker record, not an executable provenance-complete audit product.

## Search Tool Usage Log

- Round 1: paper-search-mcp `search_papers`; sources `arxiv,semantic,crossref,openalex`; no Web downgrade.
- Round 2: paper-search-mcp `search_papers`; sources `arxiv,semantic,crossref,openalex`; no Web downgrade.
- Round 3: paper-search-mcp `search_papers`; sources `arxiv,semantic,crossref,openalex`; no Web downgrade.
- Follow-up within Round 3: paper-search-mcp exact-title search for the RSC materials-informatics reproducibility paper; no Web downgrade.
