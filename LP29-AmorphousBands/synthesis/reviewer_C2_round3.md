# REVIEWER C2 Round 3

Date: 2026-06-04

Role: LP29-C2 N=3 forced malicious reviewer.

North star: whether LP29-C2 graph metrics are only a reparameterization of the Srivastava orbital-overlap metric.

## Verdict

Decision: continue internal only.

Not publishable as a physics claim. The present package is a protocol scaffold plus synthetic sanity check. It has not shown one real same-sample material row where graph spectral features survive an orbital-overlap baseline and leakage audit. I do not find a direct prior graph/GNN paper that fully publishes the exact C2 residual protocol, but Srivastava et al. 2019 already covers the core structure-to-transport overlap mechanism strongly enough that C2 must prove residual novelty before any external claim.

## Search Log

All academic searches were run first through paper-search-mcp; no WebSearch was used.

1. Method-layer search: `Srivastava 2019 orbital overlap metric amorphous semiconductors mobility graph metrics`
   - Key hit: Srivastava and Gaur, *Understanding electronic transport in multi-component amorphous semiconductors*, DOI `10.1007/s40012-019-00246-7`.
   - Key hit: Srivastava et al., *Electronic structure and transport in amorphous metal oxide and amorphous metal oxynitride semiconductors*, DOI `10.1063/1.5096042`.
2. Method-layer / recent search: `amorphous semiconductor mobility orbital overlap graph neural network 2023 2024 2025`
   - No direct C2-covering graph residual validation paper found.
3. Framework-blind search: `graph neural network charge carrier mobility amorphous materials orbital overlap`
   - Related but non-decisive hits: Bassler and Kohler 2013 on amorphous organic semiconductor mobility; Jackson et al. 2019 on ML electronic structure at coarse-grained resolutions.
4. Narrow citation verification: `"Understanding electronic transport in multi-component amorphous semiconductors" graph neural network mobility amorphous`
   - Recovered Srivastava/Gaur 2019 review and older amorphous-transport background.
5. Recent blind spot search: `amorphous materials mobility graph neural network review 2024`
   - Related hit: Wang et al. 2026, *A review of topological descriptors for amorphous materials complementing graph neural networks*, DOI `10.1016/j.commt.2026.100053`.
6. Graph-material search: `graph neural network mobility materials review orbital overlap 2024 2025`
   - Related hit: Karamad et al. 2020, *Orbital graph convolutional neural network for material property prediction*, DOI `10.1103/physrevmaterials.4.093801`.

Three-round check result: no exact direct competitor found for the proposed held-out OI-plus-graph residual protocol, but the physical baseline is already heavily occupied by Srivastava 2019.

## Step 0 Hallucination Check

Formula/unit check: no new derivation with executable formula is present in PI round summaries. The concrete baseline columns are unit-tagged in CSV, but graph residual columns in Srivastava rows are empty.

Direction check: the four Srivastava rows show `OI_norm` and `m_eff_over_m0` are strongly anticorrelated in the tiny table (`r ~= -0.971`, n=4). This is consistent with overlap improving transport, but it is not a validation of graph residual power.

Circularity check: failed for any graph-physics claim. The 288 graph rows are synthetic and explicitly marked `material_validation_allowed=false`; they only test whether the software can detect planted graph residuals.

Order-of-magnitude check: no physical magnitude claim survives because external residuals and material graph features are all blocked or empty.

Output: warning, not clean pass. The artifacts prevent overclaiming, but they also prevent the claimed physics from being established.

## Five Rejection Reasons

1. Srivastava 2019 already states the central low-dimensional baseline: orbital-overlap integral can be computed from structural information and directly correlates with effective mass in amorphous metal oxide/oxynitride semiconductors. C2 has not produced same-sample graph features after this baseline, so the current graph language is not yet distinguishable from a reparameterized OI geometry. [fatal]
   - To answer, authors must compute OI and graph metrics on the same real structures, then show held-out residual predictive power after `OI_norm`, pair density, volume/composition, onsite variance, family/batch, and finite-size controls.

2. The current artifacts are protocol/synthetic only. `C2_graph_feature_rows_synthetic_only.csv` has 288 rows, all grouped as `material_validation_allowed=false`, `synthetic_only_not_material_validation=true`, `synthetic_label_flag=true`. `C2_material_graph_rows_blocked.csv` has 5 rows and all are blocked with `graph_feature_ready=false`. [fatal]
   - To answer, authors must unblock at least one auditable real structure-label join with raw atomic coordinates, stable `structure_id`, graph construction provenance, and independent external label provenance.

3. The four-row Srivastava baseline table cannot support any independent C2 conclusion. It contains only a-IGZO and a-ZnON rows from Srivastava Table II/Fig. 4 context, with `decisive_claim_allowed=false`; graph residual columns are empty. Four curated baseline rows can verify citation plumbing, not residual science. [fatal]
   - To answer, authors need enough same-sample rows for family-held-out regression or an explicitly non-statistical paired test with predeclared tolerance bins.

4. The forbidden-control table is useful but not sufficient to prevent leakage. It is a CSV policy list, not an executed audit trace; one rule uses `forbidden_namespace=oi;graph`, which either requires parser support or split rows. The table forbids obvious target leakage but does not prove train-fold residualization, family blocking, sample crosswalk validity, or graph/OI collinearity ablation were actually executed. [serious]
   - To answer, authors must attach machine-generated audit outputs per validation row: allowed/forbidden feature mask, split assignment, leakage checks, residualization fit provenance, and OI-collinearity diagnostics.

5. The blocked material rows are honest but scientifically empty. They prevent self-certification by refusing Jankousky/Furubayashi/Srivastava joins without structures and crosswalks, but that means C2 currently has zero real material graph rows. The blocker is not a minor missing supplement; it is the central experiment. [fatal]
   - To answer, authors must either acquire the raw structure bundle or downgrade C2 permanently to a negative/protocol note: "no evidence yet that graph metrics add beyond orbital overlap."

## Specific Answers To Requested Review Questions

1. Is C2 completely covered by Srivastava 2019 or later graph/GNN mobility literature?
   - Not completely as a residual protocol. However, Srivastava et al. 2019 (`10.1063/1.5096042`) covers the central physical mechanism: structural orbital overlap explains effective mass/transport trends. Later graph/GNN literature found in this search is adjacent, not a direct C2 knockout. The burden remains on C2 to prove non-reparameterization.

2. Are current artifacts only protocol/synthetic, with no real material validation?
   - Yes. The PI summary says this explicitly, and the CSVs confirm it: 288 synthetic graph rows, 5 blocked material rows, no allowed material graph validation row.

3. Are the 4 `C2_Srivastava_baseline_rows.csv` rows enough for any conclusion?
   - No. They are enough to show the baseline schema can store Srivastava-like values. They are not enough for graph residual inference, novelty, or even robust baseline fitting.

4. Are forbidden controls / blocked material rows sufficient against target leakage and self-proof?
   - They are sufficient to stop the current artifacts from making an invalid positive claim. They are not sufficient to establish a valid positive claim because the audit is declarative and the material data remain blocked.

5. Decision?
   - Continue internal only. If framed as a manuscript or external claim, reject. If framed as an internal pre-GATE artifact, allow continuation only toward real same-sample validation.

## Narrative Retreat Check

Detected retreat: the claim moved from "graph spectra independently govern amorphous oxide transport" to "we have an OI baseline plus graph residual protocol scaffold and synthetic planted-residual sanity check." This retreat is scientifically safer, but it also removes the publishable physics claim. It is not a result; it is a work plan with guardrails.

## If I Must Pick One Fatal Error

The fatal error is the missing same-sample real-material join: no row currently contains Srivastava-style `OI_norm`, executable controls, real graph spectral features, and an independent held-out transport/effective-mass/spectral residual label in the same auditable sample.

This is not "possibly a problem"; it is the one reason I would give an editor if forced to reject. The author's way out is concrete: build a real validation table with raw structures and independent labels, run family-held-out residualization against OI/controls, and report whether `G1_lambda2_Lsym`, spectral radius residual, or attack residual adds predictive power beyond Srivastava overlap.

## Final Recommendation

Continue internal only: C2 is a disciplined anti-leakage scaffold, but the current evidence still supports the null hypothesis that graph metrics are only Srivastava orbital-overlap geometry under another parameterization.
