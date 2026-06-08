# INSPECTOR Report: A Round 3

Review target: `current-CphiPacket/A/round3.json`

Constraint followed: reviewed A Round 3 only; no B output was read; no PI synthesis was performed here.

## Overall Status

PASS with WARNING.

A Round 3 is acceptable as a prospective protocol specification for `PACKET_FEASIBLE_NEAR_FUTURE`, provided PI synthesis preserves the conditional language. I found no BLOCKER-level defect. The main residual risks are calibration specificity and the distinction between protocol gates and empirically justified statistical thresholds.

## Required Checks

### 1. Green / Yellow / Red Row Firewall

PASS.

The firewall is operationally executable: green rows require valid canonical `P_oe`, denominator-floor censoring, independent/reconstructable `B_min`, full core axes, same-sample or pre-toleranced sibling identity, raw archives, timestamped blinded logs, and pre-output row selection. Red conditions include denominator replacement, epsilon_D leakage, B_min dependence on P_oe nuisance terms, missing pressure ledger, missing raw archive, and output leakage.

WARNING: a few boundaries still require protocol handbook expansion before live execution:

- Yellow row logic mixes row-level defects with packet-level weakness, e.g. "batch/lab replication below decision-grade." This is usable for sensitivity classification, but PI should not let it blur row firewall status with packet tier status.
- "Audit-proven independent" and "reproducible with P_oe spectra hidden" are auditable concepts, but the actual audit procedure should be locked in the live protocol.

### 2. Sibling Tolerances

PASS with WARNING.

Sibling tolerances are explicitly pre-output and contain an anti-rescue rule: no sibling row can be rescued by post-hoc comparison to observed residuals. The thresholds cover oxygen/microtexture, phase fraction, pressure path, beam damage, ordinary c-axis state, and sample quality. Green, yellow, and red limits are separated, and same-sample override is required where core sibling matching cannot be measured.

WARNING: the tolerances are reasonable as provisional protocol gates, not as facility-calibrated constants. Several limits depend on "pooled pre-output standard deviation" or instrument repeatability; those quantities must be computed before output reveal and frozen with hashes. PI synthesis should preserve the warning that these gates need facility repeatability tightening before acquisition.

No post-hoc residual rescue path is present.

### 3. Facility Acceptance

PASS with WARNING.

Facility acceptance is more than a wish list. It includes auditable capabilities and metrics: denominator-to-floor ratios, sign stability under frozen channel-mixing uncertainty, calibration drift limit, missing-grid fraction, raw archive completeness, regeneration of B_min with P_oe and outputs hidden, U_miss freeze, packet-lock hash, timestamp order, and design-level leakage failure conditions.

WARNING: a few acceptance metrics are still qualitative or procedure-dependent:

- "P_oe sign is stable under frozen channel-mixing uncertainty" needs an implementation definition.
- "B_min table can be regenerated" needs a reproducibility threshold or hash-based acceptance record.
- Facility status labels are credible, but they remain conditional until actual beamline/probe/pressure/blinding ledgers are confirmed.

### 4. Tiered Thresholds

PASS.

The N=12, N=24, and N=48 thresholds are written as protocol gates with allowed-claim boundaries, not as statistical theorems. A explicitly states that rehearsal allows no residual-collapse or R_oe claim; minimum executable establishes prospective executability only; decision-grade supports only a later residual protocol and still does not assert R_oe.

WARNING: leave-one-batch-out and leave-one-lab-out are required at decision-grade but the validation statistic is not specified in this A file. PI synthesis should treat this as a downstream pre-registration requirement, not as a completed statistical guarantee.

### 5. Decision Table Completeness

PASS.

The decision table includes all required labels:

- `NOT_FOUND`
- `NON_DECISION_GRADE`
- `NON_IDENTIFIABLE`
- `PROTOCOL_FAILURE`
- `PACKET_FEASIBLE_NEAR_FUTURE`

The triggers and allowed statements are mostly aligned with the firewall and tier thresholds.

### 6. Overclaim Check: R_oe / Packet Existence

PASS.

A Round 3 does not overclaim that `R_oe` exists. It repeatedly states that the protocol is prospective and that the packet alone cannot establish `R_oe`. It also distinguishes prospective feasibility from current measured status: `PACKET_FEASIBLE_NEAR_FUTURE as a prospective protocol only; current measured packet status remains NOT_FOUND`.

No overclaim that a measured packet already exists was found.

## Conclusions That Must Be Passed To PI Synthesis

PASS: A Round 3 can be used as the A-side prospective protocol proposal for `PACKET_FEASIBLE_NEAR_FUTURE`.

PASS: The green/yellow/red row firewall is executable enough for synthesis, with green-only primary packet discipline and red design-level failure conditions.

PASS: Sibling tolerances are pre-output and explicitly block post-hoc residual rescue.

PASS: Facility acceptance contains auditable metrics rather than only desired capabilities.

PASS: N=12 / N=24 / N=48 are framed as protocol gates and claim tiers, not statistical proof.

PASS: The required five-way decision table is present.

PASS: A does not claim `R_oe` exists and does not claim that a measured packet already exists.

WARNING: PI synthesis should preserve the conditional nature of the verdict. The correct synthesized use is: prospective feasible protocol, current measured packet still `NOT_FOUND` unless row-level schema, archive, blinding, and firewall conditions are actually satisfied.

WARNING: PI synthesis should require live-protocol expansion for audit mechanics, facility repeatability constants, and decision-grade validation statistics before treating this as acquisition-ready.

## BLOCKER

None found.
