# C2T required_join_fields extraction

Source: `knowledge_graph/LP29-AmorphousBands_C2_v1_20260604.json`
Date: 2026-06-04

## Required fields

1. `sample_id`
2. `label_provenance_id`
3. `structure_or_SI_source`
4. `O_s_or_exact_overlap_baseline`
5. `B0_onsite_variance`
6. `B0_carrier_density`
7. `B0_mobility_edge_margin`
8. `B0_finite_size`
9. `B0_batch_or_family`
10. `G1_lambda2_Lsym`
11. `G1_rho_A_budget_norm`
12. `G1_attack_gap_lambda2`
13. `external_Hall_Drude_Wannier_spectral_label`
14. `forbidden_control_audit`

## Gate rule

Rows with any missing provenance-critical field remain `material_validation_allowed=false`.
Synthetic rows may be used only for software sanity checks.

