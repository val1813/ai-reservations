# INSPECTOR: B C2T-S2 Round 2

Date: 2026-06-04

Input audited:
- `current/B/C2T_S2_round2.json`
- `current/B/artifacts/S2_Os_reproduction_payload_failure_modes.csv`
- `synthesis/inspector_B_C2T_S2_round1.md`

A-output policy: no A output was read.

## Verdict

INSPECTOR result: **PASS with minor implementation warning**.

B Round 2 adequately resolves the main Round 1 warnings. It materializes the prior prose-level certificate idea into a row-level failure-mode table, keeps the conclusion at "current payload not reproduced / blocked under C2T gates", and does not promote reported Srivastava context into material validation or a graph-beats-overlap baseline.

The remaining warning is mechanical rather than conceptual: the CSV is executable enough as a negative-control oracle, but a production executor will still need a fixed enum/branch mapping for conditional statuses such as `BLOCK_IF_REPRODUCTION_CLAIMED_ELSE_NOT_APPLICABLE`, `BLOCK_OR_WARN_BY_MODE`, and `WARN_IF_PARTIAL_BLOCK_IF_REQUIRED_FIELD_ONLY`.

## Round 1 Warning Closure

### 1. Avoid principle irreproducibility claim

Pass.

Round 2 repeatedly confines the result to the current payload:
- JSON `scope_limit`: not material validation and not a claim that Srivastava exact `O_s` is impossible to reproduce in principle.
- Finding F1: "current payload does not reproduce" because executor-grade witnesses are missing.
- Failed jump J4: explicitly rejects converting a blocked reproduction payload into a physical disagreement.
- Claim C3: "current payload not reproduced; this is not evidence that Srivastava exact `O_s` is unreproducible in principle."
- CSV row `current_payload_incomplete_not_principle_failure`: future payload may supply the missing witnesses.

This fixes the main alternative-explanation risk from Round 1: incomplete current witness collection is not treated as evidence that the source result is wrong or unrecoverable.

### 2. Do not use gates as external literature proof

Pass.

Round 2 frames its claims as C2T executor admissibility claims, not external factual claims about the Srivastava paper or public supplementary material. The key claim C1 is explicitly scoped to "under the current C2T witness schema and gate predicates" and assumes the row is claiming `srivastava_reproduction`.

The JSON does list literature search strings under `literature_needed`, but it does not pretend those searches have been completed or use them as proof.

### 3. Instantiate the negative-control table

Pass with minor implementation warning.

The CSV is a concrete failure-mode table with:
- typed blocker name
- blocked gate
- required witness
- reason reported context is insufficient
- executor status

This is materially stronger than Round 1's prose-only design. The rows are actionable for an executor or reviewer because each blocker names the missing witness and the status consequence.

Implementation warning: several executor statuses are conditional rather than final enum values. That is acceptable for an inspector-level failure-mode schema, but the next implementation step should normalize them into deterministic branches keyed by comparison mode and required-field presence.

### 4. Preserve mode separation

Pass.

B Round 2 preserves the distinction among:
- `reported_context_only`
- `srivastava_reproduction`
- exact residual-validation baseline
- material validation

The CSV row `context_value_used_as_residual_baseline` directly blocks promotion of reported `OI_norm` into an exact residual oracle unless all G5 replay witnesses pass. Finding F3 makes the same point in prose.

## Focus Checks

### Failure modes executable?

Mostly yes.

The failure modes are executable as a negative oracle because they map missing witness classes to G5/G6/G7 consequences. They cover the needed blockers: formula/code, normalization, same-structure mapping, source row identity, structure identity, raw overlap sum, pair rule, denominator trace, machine-reviewable evidence, executor trace, mode separation, material-validation suppression, and identity contradictions.

Minor warning: to become a fully deterministic machine payload, the table should specify exact input-field predicates and final status enum values for conditional rows. This does not block Round 2 because the requested artifact is a failure-mode table, not yet the full executor payload.

### "Current not reproduced" maintained?

Pass.

No claim in the audited Round 2 output says Srivastava exact `O_s` is impossible to reproduce in principle. The strongest statement is correctly limited to "current payload does not reproduce" and "reported context is insufficient for exact replay under C2T gates."

### No material validation overclaim?

Pass.

Round 2 explicitly says schema conformance and sub-witnesses are not material validation. It blocks material validation until `row_decision=PASS` and unresolved blockers are cleared. The CSV row `material_validation_claimed_during_reproduction_audit` is correctly marked `BLOCK`.

### No graph-beats-baseline overclaim?

Pass.

No graph-vs-overlap residual superiority claim is made. B says reported Srivastava context may remain literature context but cannot be used as an exact residual-validation baseline until a replayable `O_s` payload passes.

## Inspector Notes

The only unverified dependency is that B Round 2 references schema/gate and PI files not included in this Round 2 read set. I did not open them because the task specified a restricted input list and prohibited A output. This inspection therefore validates internal scope control and executability of the provided B Round 2 artifacts, not the external correctness of every referenced file.

## Final Disposition

`B C2T-S2 Round 2` may proceed.

Carry forward one implementation warning:

1. Before using the CSV as a production executor input, convert conditional executor statuses into fixed enum outcomes or explicit mode-dependent branches.

No blocking fixes required.
