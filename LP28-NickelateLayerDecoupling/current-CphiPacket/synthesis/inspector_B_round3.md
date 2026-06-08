# INSPECTOR Report: B Round 3

Verdict: PASS with one WARNING.

Input reviewed: `D:\Claude\ai-reservations\LP28-NickelateLayerDecoupling\current-CphiPacket\B\round3.json`

Scope note: reviewed B Round 3 only. Did not read A output and did not perform PI synthesis. No `validation/` directory exists under `current-CphiPacket`, so this is a manual INSPECTOR check.

## Checklist

### 1. kill_table five-state completeness, exclusivity, executability

PASS / WARNING.

Five required statuses are present:

- `NOT_FOUND`
- `NON_DECISION_GRADE`
- `NON_IDENTIFIABLE`
- `PROTOCOL_FAILURE`
- `PACKET_FEASIBLE_NEAR_FUTURE`

Each status has a definition, concrete triggers, allowed claim, and forbidden claim, so the table is executable at the PI synthesis level.

WARNING: mutual exclusivity is mostly adequate but not fully precedence-locked. `NON_IDENTIFIABLE` and `PROTOCOL_FAILURE` can overlap in cases involving shared fitted qz/c-axis/orbital state, red rows, denominator/calibration tuning, or missing blinding locks. PI synthesis should impose a decision order:

1. `NOT_FOUND` if no auditable packet exists.
2. `PROTOCOL_FAILURE` if execution/blinding/locking was violated.
3. `NON_DECISION_GRADE` if a clean packet exists but fails N/batch/lab/validation gates.
4. `NON_IDENTIFIABLE` if clean enough to inspect but information separation fails.
5. `PACKET_FEASIBLE_NEAR_FUTURE` for prospective sealed designs satisfying all concession gates.

This is a WARNING, not a BLOCKER, because B's allowed/forbidden claims are already conservative and executable.

### 2. concession_boundary

PASS.

`concession_boundary` explicitly gives B's mandatory concession conditions for both:

- `PACKET_FEASIBLE_NEAR_FUTURE`
- `PACKET_FEASIBLE_NOW`

It also lists non-concession conditions and limits the concession to packet feasibility/protocol decidability, not truth of `R_oe` or validation of `C_phi`.

### 3. structural_nonidentifiability scope

PASS.

B correctly limits structural non-identifiability to the packet/protocol class where `B_min` depends on the same fitted state that defines `P_oe`. It explicitly avoids upgrading the result into a universal no-go theorem for all future probes or all theoretical objects.

### 4. threshold_interpretation

PASS.

`N=48` target and `>=36` complete blinded rows are written as conservative decision-grade protocol gates. `N=24`, `N=12`, and `24-35` are classified as rehearsal/executable/pilot tiers, not as statistical power theorems. The anti-overclaim text is explicit enough for PI synthesis.

### 5. probe_family_requirements

PASS.

B separates necessary information roles from replaceable instruments:

- Necessary: odd/even susceptibility, material baseline, independent c-axis/path calibration or covariance treatment, leakage/negative controls.
- Replaceable: specific RIXS/neutron implementation, oxygen assay, orbital proxy, negative-control implementation.

The key non-replaceable requirement is preserved: the information roles cannot collapse into one fitted qz/c-axis state.

### 6. near-future sealed campaign route

PASS.

B does not over-kill the near-future sealed campaign route. It includes `PACKET_FEASIBLE_NEAR_FUTURE` as a live state and gives explicit conditions under which B must concede feasibility. The route remains demanding but not impossible.

## Must Pass To PI Synthesis

- B Round 3 is acceptable for synthesis: no BLOCKER found.
- PI should preserve B's scope guard: packet-class identifiability boundary only, not universal no-go.
- PI should preserve B's concession: a sealed near-future packet is feasible if N/batch/lab, firewall, independent-information, and blind-custody gates are all met.
- PI should treat `N=48/36` as a decision-grade protocol gate, not a power theorem or universal sample-size law.
- PI should preserve the probe distinction: instruments are replaceable, independent information roles are not.
- PI should add an explicit kill-table precedence rule to prevent overlap between `PROTOCOL_FAILURE` and `NON_IDENTIFIABLE`.
