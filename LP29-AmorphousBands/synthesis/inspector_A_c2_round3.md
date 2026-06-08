# INSPECTOR Report: A C2 Round 3

Input:
- `D:\Claude\ai-reservations\LP29-AmorphousBands\current\A\C2_round3.json`
- `D:\Claude\ai-reservations\LP29-AmorphousBands\current\A\artifacts\C2_Srivastava_baseline_rows.csv`
- `D:\Claude\ai-reservations\LP29-AmorphousBands\current\A\artifacts\C2_forbidden_controls_rules.csv`

Protocol: `D:\Claude\ai-reservations\ai\INSPECTOR.md`

Mechanical validation: no `validation/` directory exists in this project, so `validate.py` is unavailable. This inspection uses manual Q1-Q6 checks plus programmatic CSV/regex parsing.

## Verdict

INSPECTOR result: pass with warnings.

- Blockers: 0
- Warnings: 2

Round 3 is usable as a baseline/provenance artifact round. It does not establish same-sample material validation and does not claim graph residual power after `OI_norm + controls`.

## Q1. Dimension / Formula Check

Pass.

Claim C2R3-C1 uses:

`OI_norm = sum(N_ab*S_ab)/V`

`N_ab` is a pair count, `S_ab` is dimensionless orbital overlap, and `V` is reported in angstrom^3 in Srivastava Table II. The resulting numerical table quantity is angstrom^-3, consistent with the artifact wording "Number of Pairs * OI per A3 volume". The CSV stores `cell_volume_m3`; the OI values themselves are direct reported Table II values, not recomputed from SI units. This is acceptable because the provenance says `reported_table_and_text`.

Claim C2R3-C2 uses:

`OI_pair_mean - OI_raw_sum/N_pair`

Both sides are dimensionless. The numerical test with `2.5/10 = 0.25` gives zero difference as claimed.

No invalid dimensional argument was found in `exp`, `sin`, `log`, or similar functions because no such functional formula is asserted in Round 3.

## Q2. Direction / Limit Check

Pass.

The fixed-pair and fixed-density directions are correct:

- At fixed pair sum, increasing volume lowers `sum(N_ab*S_ab)/V`.
- At fixed `N_pair`, `OI_pair_mean = OI_raw_sum/N_pair` is the relevant normalization, so raw sums cannot be interpreted as density effects.
- If pair count changes with composition/volume/cutoff, `pair_density` or matched density bins are required before any graph-independent claim.

No reversed ratio or sign error was found.

## Q3. Circularity Check

Pass.

The output does not use the Srivastava effective masses as evidence that graph residual features work. It uses them only as reported baseline rows. The residual protocol remains future-facing and explicitly requires held-out residual improvement after `OI_norm + controls`.

The negative boundaries are explicit:

- "No graph residual power has been verified."
- "No same-sample material validation has been completed."
- "Srivastava Table II rows are baseline/provenance rows, not evidence that graph metrics win."

No same-measurement or same-label validation loop was found.

## Q4 / Q5. Numerical and Source Check

Pass, with one minor hygiene warning.

Srivastava baseline rows are self-consistent against the local PDF `current/A/downloads/1812.11333.pdf`:

- `a-IGZO-1114`: volume `1148.19645 A^3`, Table II sum `0.02966`, effective mass text `0.21 m_e`.
- `a-IGZO-2217`: volume `1152.70734 A^3`, Table II sum `0.02669`, effective mass text `0.22 m_e`.
- `a-ZnON-21`: volume `1081.7498 A^3`, Table II Zn-Zn value `0.06231`, effective mass text `0.16 m_e`.
- `a-ZnON-11`: volume `1506.9619 A^3`, Table II Zn-Zn value `0.06693`, effective mass text `0.17 m_e`.

The CSV has exactly 4 rows and the expected header. Composition JSON strings parse as CSV fields correctly. `decisive_claim_allowed=false` is consistent with blocked provenance.

Warning: `lambda2_resid`, `spectral_radius_resid`, and `attack_resid` are single spaces rather than empty/null cells in all four baseline rows. This is not a scientific blocker, but downstream code that treats non-empty strings as available values could misread these blocked fields. Normalize these cells to empty strings or explicit `NA`.

## Rules CSV Executability

Mostly pass, with one execution warning.

`C2_forbidden_controls_rules.csv` has 18 rows and the expected header:

`target_type,forbidden_namespace,forbidden_columns_pattern,rationale`

All `forbidden_columns_pattern` values compile as regular expressions. The rules cover target leakage, same-measurement algebraic transforms, OI/Wannier leakage, graph metadata leakage, baseline-prediction leakage, and OI fixed-pair/fixed-density safeguards.

Warning: row 18 uses `forbidden_namespace=oi;graph`. This is executable only if downstream code explicitly splits semicolon-delimited namespaces. If the executor does exact namespace matching, the rule can be skipped for both `oi` and `graph`. Safer options: split row 18 into two rows, one for `oi` and one for `graph`, or require a documented namespace-splitting parser.

## Blocked Provenance Check

Pass.

The blocked provenance is honest:

- Jankousky is marked `blocked_provenance`; the approximate `m_eff_over_m0 around 0.2` and `mobility-edge margin around 0.25 eV` are traceable to project plan notes and Round 2, not promoted into same-sample validation.
- Furubayashi is marked `blocked_pending_digitization`; the inspected `A1_Furubayashi2019_digitized_transport_schema.csv` contains only `F2019_TODO` with `target_independence_status=pending_digitization`.
- Missing fields are concrete: structure IDs, same-sample OI, graph metrics, transport/electronic external labels, residuals, and train/test split.

No blocked item is silently used as decisive evidence.

## Same-Sample Boundary

Pass.

No same-sample validation overreach was found. The strongest statements are correctly bounded as:

- reported Srivastava baseline rows,
- executable rules,
- blocked external-label provenance,
- residual protocol not yet met.

The output does not claim that graph metrics survive `OI_norm + controls`, nor that Jankousky/Furubayashi provide complete same-sample residual rows.

## Deepening Check

Pass for task-specific deepening; warning for formal Gate 1.5 shape.

Round 3 deepens C2 from Round 2's protocol/schema scaffold into two concrete artifact layers:

1. Srivastava Table II/Fig. 4 baseline rows with hard blocked fields.
2. Machine-readable forbidden-control rules including fixed-pair/fixed-density OI safeguards.

That is a real deepening of the C2 artifact state.

Warning: `C2_round3.json` does not contain explicit `deepening_1` / `deepening_2` fields or two named layers under each. If the later Gate 1.5 check is applied mechanically to this C2 file, it may fail the format check even though the content-level deepening is adequate.

## Q6. Comprehensive Judgment

Pass with warnings. No blocking defect was found.

The two warnings should be fed forward because they affect implementation robustness, not the scientific boundary:

1. Normalize residual placeholder cells in `C2_Srivastava_baseline_rows.csv`.
2. Make the multi-namespace rule in `C2_forbidden_controls_rules.csv` unambiguous for executors.

--- 投喂下一轮 ---

必须修正（阻断级）:

None.

建议修正（警告级）:

1. `C2_Srivastava_baseline_rows.csv` 中 `lambda2_resid` / `spectral_radius_resid` / `attack_resid` 目前是单空格。改为空值或显式 `NA`，避免 downstream parser 误判为已有 residual。
2. `C2_forbidden_controls_rules.csv` 第 18 行 `forbidden_namespace=oi;graph` 需要拆成两行，或在执行器中明确实现 semicolon namespace splitting。
3. 若后续 Gate 1.5 对 C2 文件做机械检查，补显式 `deepening_1` / `deepening_2` 两层字段；本轮内容级 deepening 合格，但格式未显式呈现。

---
