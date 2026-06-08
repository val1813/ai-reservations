# INSPECTOR: B C2T-S2 Round 1

Date: 2026-06-04

Input audited:
- `current/B/C2T_S2_round1.json`
- `synthesis/gate_minus1_LP29-C2T-S2.md`
- `current/C2T/artifacts/C2T_witness_payload_schema.json`
- `current/C2T/artifacts/C2T_gate_predicates.csv`

A-output policy: no A output was read. B's own JSON references an `A_witness_requirements` artifact, but that artifact was not opened or used for this inspection.

## Mechanical Check

`validate.py` was not run. The provided object is not a standard numerical `roundN_claims.json` with unit algebra or numeric formulas to validate, and the user restricted the read set to the four listed inputs. The inspection below is therefore a manual INSPECTOR check of claim direction, circularity, scope control, gate predicate consistency, and alternative-explanation risk.

## Verdict

INSPECTOR result: **PASS with warnings**.

B Round 1 is acceptable as a proof-carrying audit-path proposal. It does not provide, and does not claim to provide, a material validation result. It also does not claim that Srivastava exact `O_s` has already been reproduced. However, the round has a nontrivial circularity risk: much of the support for the need for a proof-carrying payload is the existing C2T gate machinery itself. That is valid for enforcing the current gate, but not enough to establish an external factual conclusion that public Srivastava materials are unreplayable in principle.

## Q1 Quantity / Unit Check

No blocking unit error found.

The only displayed equation is schematic:

`O_s = N(S, P, theta_norm)[ sum_{(i,j) in P(S, theta_pair)} omega(i,j; theta_formula) ]`

B treats this as a typed contract, not as a dimensioned physical derivation. The payload fields `pair_cutoff_A`, `pair_density`, `N_pair`, `OI_raw_sum`, and normalization identifiers are correctly presented as required witnesses rather than computed values.

## Q2 Direction / Claim-Scope Check

No direction reversal found.

The direction of B's claim matches GATE -1 Proposition B: reported context is insufficient for a residual-validation baseline unless exact formula/code, raw overlap sum, normalization, pair cutoff, same-structure mapping, and machine-reviewable witness payload are present.

Important scope check: B states:
- `material_validation_claimed=false`
- `scope_limit`: no material validation and no claim that Srivastava `O_s` has been reproduced
- `not_claimed`: includes "Srivastava exact O_s has been reproduced"

This is consistent with the witness schema description that schema conformance is not material validation, and with G7, where material validation is allowed only after PASS and unresolved blockers are cleared.

## Q3 Circular Reasoning Check

Warning, not blocking.

B's strongest support is internal to C2T:
- G5 blocks claimed Srivastava-style OI reproduction when exact formula/code, normalization, or same-structure mapping is missing.
- The schema says manual labels are advisory and row decisions must be recomputed from payload fields.
- B then concludes that reported `OI_norm` remains context-only unless the certificate fields exist.

This is not circular if the claim is read narrowly as: "under the current C2T executor contract, a context-only row cannot be promoted to reproduced `O_s`." That follows directly from the provided predicates.

It becomes circular if read broadly as: "the physics or literature has shown Srivastava exact `O_s` is not reproducible." The gate requirements cannot by themselves prove that external public materials lack enough information; they can only type the current payload as BLOCK/WARN/PASS.

Required PI handling: preserve the narrower wording. Do not let B's Round 1 result become an empirical/material conclusion.

## Q4 Order-of-Magnitude Check

No numerical magnitude claim was made that can be checked. No 10^N comparison or quantitative residual claim appears in the provided B output.

## Q5 Algebra / Limit Check

No algebraic blocker found. The displayed equation is a certificate template, not a derived formula. It correctly separates:
- structure `S`
- pair rule `P(S, theta_pair)`
- overlap weights `omega`
- raw summation
- normalization map `N`

The invariant that changing source row, structure, pair rule, raw sum, or normalization creates a different certificate is consistent with the stated same-structure and replay requirements.

## Q6.3 Claim Shrinkage

No shrinkage against GATE -1 Proposition B.

B does not weaken the proposition into a material claim or a purely discretionary audit burden. It keeps the central standard: residual-validation baseline requires replayable witnesses, while reported context alone remains context.

## Q6.4 Alternative Explanation Risk

Warning.

B acknowledges several failed analogy routes, but the alternative explanation still needs to be kept explicit:

1. Missing proof-carrying fields in the current payload may reflect an incomplete audit artifact, not actual nonexistence in Srivastava public materials.
2. A reported `OI_norm` could be adequate for literature-context comparison while still failing the stricter `srivastava_reproduction` mode.
3. A future executable reconstruction could pass G5 if it supplies formula/code, normalization, same-structure mapping, and machine-reviewable witnesses.

Therefore the correct blocker language is: "not reproduced by this payload / not admissible as exact residual-validation baseline under C2T gates." It should not be phrased as: "Srivastava `O_s` is impossible to reproduce" or "the reported value is physically wrong."

## Q6.5 Landing / Executable Audit Path

Pass with implementation warning.

B gives a concrete landing path:
- negative-control executor table
- null/missing-field certificate instance that deterministically emits BLOCK
- mode-separation rule for `reported_context_only` vs `srivastava_reproduction`
- required fields and blocker paths FP1-FP7

This is an auditable path rather than material validation. However, Round 1 does not yet provide an actual executable payload instance conforming to `C2T_witness_payload_schema.json`; it provides the minimum certificate contract and failure-path design. That is acceptable for B Round 1, but the next round must materialize at least one machine-reviewable payload/table if the project wants an executor-level result.

## Specific Required Checks

### Proof-carrying payload vs material validation

Pass. B correctly frames proof-carrying payload as a reproducibility gate and explicitly excludes material validation. The schema and G7 support this separation.

### Erroneous claim that `O_s` was reproduced

Pass. No erroneous reproduction claim found. B explicitly says it does not claim Srivastava exact `O_s` has been reproduced.

### Circular / alternative-explanation risk

Warning. B's argument is gate-consistent but internally anchored. It must remain an audit-status claim, not an external literature-status claim. The main unresolved alternative explanation is incomplete current witness collection rather than irreproducibility of the source itself.

## Final Disposition

`B C2T-S2 Round 1` may proceed, with warnings carried into the next prompt.

--- Feed To Next Round ---

Must fix (blocking):

None.

Recommended fixes (warning):

1. Avoid broad wording that implies Srivastava exact `O_s` is unreproducible in principle. Use: "not reproduced by the current payload / BLOCK under C2T G5 until witnesses are supplied."
2. Do not use the existing gate predicates as external proof of a literature fact. They prove only executor admissibility under the current C2T contract.
3. Next B round should instantiate the proposed negative-control executor table or JSON payload and show deterministic blocker codes from actual fields, not only describe the certificate contract.
4. Keep `reported_context_only`, `fixed_density`, `fixed_pair`, and `srivastava_reproduction` modes separate; do not let reported `OI_norm` silently become a residual-validation baseline.

---
