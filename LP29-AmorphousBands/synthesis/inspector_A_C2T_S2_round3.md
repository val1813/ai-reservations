# INSPECTOR: LP29-C2T-S2 A Round 3

Date: 2026-06-04

Input inspected:
- `current/A/C2T_S2_round3.json`
- `current/A/artifacts/S2_Srivastava_reproduction_attempt_contract.csv`
- `synthesis/inspector_A_C2T_S2_round2.md`

B-side output was not read.

## Verdict

INSPECTOR PASS.

A Round 3 correctly converts the Round 2 blocker discipline into a 16-row executor-facing attempt contract. The contract does not incorrectly pass any non-context mode. It preserves the exact `O_s` block, keeps `reported_context_only` as the only passing branch, contains two-layer `deepening_1` and `deepening_2`, and does not advance into material validation.

Mechanical validation note: no `validation/` directory exists under `LP29-AmorphousBands`, so no project validator was run; this report uses manual INSPECTOR checks plus CSV enum/count checks.

## Requested Checks

### 1. 16-row attempt contract and non-context gating

PASS.

Mechanical CSV count:
- Total contract rows: 16.
- `reported_context_only`: 4 rows.
- `fixed_density_attempt`: 4 rows.
- `fixed_pair_attempt`: 4 rows.
- `exact_reproduction_attempt`: 4 rows.

Status enum count:
- `PASS_REPORTED_CONTEXT_ONLY`: 4 rows.
- `BLOCK_FIXED_DENSITY_ATTEMPT`: 4 rows.
- `BLOCK_FIXED_PAIR_ATTEMPT`: 4 rows.
- `BLOCK_EXACT_REPRODUCTION_ATTEMPT`: 4 rows.

No non-context attempt mode is passed. For every sample, `fixed_density_attempt`, `fixed_pair_attempt`, and `exact_reproduction_attempt` have `allowed_use_now=none_beyond_reported_context_only` and an explicit `BLOCK_*` status.

### 2. Exact `O_s` remains blocked

PASS.

Round 3 keeps the exact reproduction boundary explicit:
- JSON verdict is `ATTEMPT_CONTRACT_CREATED__EXACT_REPRODUCTION_STILL_BLOCKED`.
- JSON says exact reproduction is blocked for every sample because the complete Srivastava witness package is missing.
- CSV `exact_reproduction_attempt` rows are all `BLOCK_EXACT_REPRODUCTION_ATTEMPT`.
- Exact rows require official row/page provenance, structure identity, coordinates or file hash, atom count, pair-rule provenance, pair-list hash, `N_pair`, executable Mulliken/STO kernel, `q_i_q_j` weights, `OI_raw_sum`, executable normalization formula id, reproduced `OI_norm` check, and same-structure mapping.
- CSV forbids `do_not_claim_exact_Srivastava_O_s_baseline`.

No row relabels reported `OI_norm` as reproduced exact `O_s`.

### 3. Deepening structure

PASS.

`deepening_1` has exactly two explicit layers:
- `layer_1`: field-level blockers are insufficient for execution because they are global.
- `layer_2`: the row contract makes admissible action row-local and blocks all non-context modes.

`deepening_2` has exactly two explicit layers:
- `layer_1`: the dangerous false upgrade is treating reported `OI_norm` as supplying `OI_raw_sum` or normalized exact `O_s`.
- `layer_2`: the contract blocks that upgrade by requiring independent raw sums, pair provenance, executable normalization, and same-structure mapping.

### 4. No material validation

PASS.

A Round 3 keeps material validation out of scope:
- JSON summary says no material validation, residual validation, or graph-beats-overlap claim is enabled.
- JSON forbidden use says not to run material residual validation and not to claim graph metrics beat the orbital-overlap baseline.
- CSV `reported_context_only` rows forbid residual or graph validation.
- CSV `fixed_pair_attempt` rows forbid material validation.
- CSV exact reproduction rows forbid graph-beats-overlap claims.

No residual fields, graph residuals, material-validation metrics, or decisive LP29 material claims are introduced.

## INSPECTOR Q-Checks

Q1 quantity/unit check: Not applicable. Round 3 introduces an executor contract, not a new dimensional formula.

Q2 sign/direction check: PASS. The direction is conservative: context rows may be displayed; every reproduction or alternative-comparison attempt remains blocked.

Q3 circularity check: PASS. The contract does not validate exact `O_s` from reported `OI_norm`; it explicitly blocks any upgrade without independent witnesses.

Q4 order-of-magnitude check: Not applicable. No new quantitative material estimate is used.

Q5 algebra/numeric provenance check: PASS for this scope. The artifact enumerates witness requirements rather than computing a reproduced overlap.

Q6.3 claim shrinkage: PASS. There is no silent shrinkage; the output explicitly preserves the Round 2 context-only boundary and makes it row/mode executable.

Q6.4 alternative explanation: Warning not required for this audit. The active claim is gating/provenance discipline, not a new physical mechanism.

Q6.5 landing calculation: PASS for this task. A does not assert a no-prior-art blank or material-validation claim; it blocks landing use until witnesses exist.

## Feed To Next Round

--- Feed to next round ---

Blocking fixes:
1. None for A Round 3 under the requested checks.

Warning-level carryovers:
1. Keep only `reported_context_only` as a passing mode.
2. Keep `fixed_density_attempt`, `fixed_pair_attempt`, and `exact_reproduction_attempt` blocked unless their explicit witness packages are attached with provenance ids.
3. Do not relabel reported `OI_norm` as reproduced exact `O_s`.
4. Do not run material/residual/graph validation from this contract.

---
