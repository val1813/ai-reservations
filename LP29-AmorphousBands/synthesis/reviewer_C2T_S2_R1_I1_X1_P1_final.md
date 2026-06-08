# REVIEWER final: LP29-C2T-S2-R1-I1-X1-P1

Date: 2026-06-05

## Verdict

**REJECT / do not close as stated.**

P1 implements a useful fixture-level proof-object shape checker and a converter into X1 predicate payloads. It does **not** yet implement an authenticity precondition that truly constrains terminal validator admission.

The terminal validator still admits a direct forged payload when F01-F22 booleans are all `true` and `comparison.verdict == "match"`, even if `witness.authenticity_status == "BLOCK"` or the authenticity field is absent. Therefore P1 does not close as:

> proof-object authenticity precondition implemented for fixture-level `O_s` admission.

It can only close, if renamed, as:

> fixture-level proof-object metadata checker plus converter for the existing predicate-state validator.

## Files Read

- `synthesis/PI_C2T_S2_R1_I1_X1_P1_final.md`
- `synthesis/authenticity_results_C2T_S2_R1_I1_X1_P1.md`
- `synthesis/gate4_C2T_S2_R1_I1_X1_P1.md`
- `validation/authenticity.py`
- `tests/test_authenticity.py`

## Commands Executed

```powershell
python -m pytest tests/test_authenticity.py
```

Observed: `3 passed`.

```powershell
python -m pytest tests/test_validate.py tests/test_authenticity.py
```

Observed: `8 passed`.

Passing tests do not resolve the fatal issue below because the tests only exercise the converter path, not a direct forged terminal payload.

## Boundary Audit

No overclaim was found in the prose boundary:

- no real source PDFs or rows are authenticated
- no exact Srivastava `O_s` reproduction is claimed
- no material validation is claimed
- no graph-vs-overlap residual regression is claimed
- no graph beats overlap claim is made

The boundary language is mostly disciplined. The failure is implementation semantics, not rhetoric.

## Fatal Findings

1. **Authenticity does not constrain terminal validator admission.**  
   `payload_from_proof_object()` carries `authenticity_status`, but `validate_payload()` does not inspect it. In `validate.py`, `admitted_exact` checks required F01-F22 booleans and `comparison.verdict == "match"`; it does not require `authenticity_status == "PASS"`. I constructed:

   - `target_mode = admitted_exact`
   - all F01-F22 predicates `true`
   - `comparison.verdict = match`
   - `witness.authenticity_status = BLOCK`

   Observed terminal result: `ADMITTED_EXACT`. This is a direct bypass of the claimed precondition. [fatal]

   Authors must prove: terminal exact admission is impossible unless authenticity is present and `PASS`, or the only public admission API accepts proof objects and internally runs authenticity before terminal validation.

2. **Missing authenticity status is also admitted.**  
   I constructed the same all-true admitted-exact payload with no `authenticity_status` field. Observed terminal result: `ADMITTED_EXACT`. That means P1 is optional metadata, not a gate. [fatal]

   Authors must prove: missing authenticity metadata blocks `admitted_exact`, `candidate_exact_replay`, and `diagnosed_mismatch` where these depend on proof-object provenance.

3. **The proof-object checker trusts the comparison verdict instead of validating even fixture-level numeric consistency.**  
   I modified the valid proof object so `source.reported_scalar.scalar = 1.25`, `verification.recomputed_value = 999.0`, and `verification.comparison.verdict = match`. `validate_authenticity()` returned `PASS`, and the converted payload reached `ADMITTED_EXACT`. P1 need not recompute physical `O_s`, but if it calls F21-F22 a replay comparison precondition, it cannot let a self-declared `match` override an internal fixture contradiction. [serious]

   Authors must prove: for fixture-level exact admission, the reported scalar, recomputed value, and predeclared tolerance are checked mechanically, or the claim must be downgraded to metadata presence checking only.

4. **The tests prove only the happy converter path and one missing-locator block.**  
   `test_failed_authenticity_blocks_before_terminal_admission()` creates a bad proof object, runs `payload_from_proof_object()`, and then observes `BLOCK`. That only proves false predicates propagate through the converter. It does not prove terminal validation rejects forged all-true predicate payloads with failed or missing authenticity. [serious]

   Authors must add negative tests for:
   - `authenticity_status=BLOCK` with all F01-F22 true must not admit exact
   - missing `authenticity_status` must not admit exact
   - self-contradictory reported/recomputed values with verdict `match` must not admit exact

## What Works

The metadata checker itself has useful fixture coverage:

- valid full proof object -> `PASS`
- missing source locator -> `BLOCK`, first failed `F02`
- bad structure digest -> `BLOCK`, first failed `F06`
- pair-count mismatch -> `BLOCK`, first failed `F12`
- normalization formula missing required terms -> `BLOCK`, first failed `F14`
- unbound execution trace -> `BLOCK`, first failed `F19`
- missing predeclared tolerance -> `BLOCK`, first failed `F22`

This is a good start, but it is not yet an admission precondition.

## Required Repair

Minimum acceptable repair:

1. Add terminal validation logic that blocks exact-admission modes unless `witness.authenticity_status == "PASS"` or an equivalent signed/structured authenticity result is present.
2. Add negative tests for direct forged payloads that bypass `payload_from_proof_object`.
3. Add fixture-level numeric comparison consistency: `abs(recomputed_value - reported_scalar)` must satisfy the predeclared tolerance for an exact `match`, or exact admission must block / diagnose mismatch.
4. Update synthesis language to distinguish "metadata presence/shape authenticity" from real source authentication and from physical recomputation.

## Final Recommendation

Do **not** close P1 under the requested claim. Close only after authenticity PASS/BLOCK becomes a mandatory condition inside the terminal admission path, not merely a property of the optional converter path.
