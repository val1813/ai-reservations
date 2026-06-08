# PI Final Synthesis: LP28-S1

## Final Status

LP28-S1 does not survive as a scientific claim, validated predictor, or mechanism.

It survives only as a bounded preregistered protocol template:

`I_phi` may be computed as a sealed input-side encoder only if a real P0 packet exists, can be independently recomputed, has enough complete rows, passes coefficient-sensitivity checks, and does not collapse to simpler input-side baselines.

## Final Unified Claim

Allowed:

> `I_phi` is a candidate zero-leakage, input-side audit protocol for testing whether a phase-bus readiness index can be computed before bulk superconducting outputs are inspected.

Forbidden:

- `I_phi` predicts superconductivity.
- `C_phi` is a validated phase-bus observable.
- normal-state c-axis Drude fraction is a new mechanism.
- LP28-S1 validates interlayer coherence as the controlling parameter.

## Reviewer Outcome

REVIEWER recommendation:

> Reject as a scientific claim. Major revision only as a preregistered protocol template.

Fatal issue:

`C_phi_primary` remains a normal-state c-axis Drude/interlayer-coherence/sample-quality observable. LP28-S1 has not shown it is independent of prior phase knowledge rather than a relabeled baseline.

## Hard Boundary Conditions

S1 can only be reopened with a real sealed P0 packet satisfying all of:

- at least 6 complete same-sample or predeclared matched-sample rows
- sample/pressure grid timestamped before output reveal
- 120 K normal-state status proven without forbidden outputs
- exact auditor recomputation from sealed artifacts
- coefficient-sensitivity pass before output reveal
- no collapse to `C_phi`-only, total c-axis weight, disorder-only, dephasing-only, or orbital-only baselines
- all suspicious citations manually verified

## Breakthrough Assessment

This is not yet a theory breakthrough. It is a technical discipline improvement: a way to prevent circular nickelate screening claims from masquerading as predictors.

The remaining real breakthrough question is sharper:

Can any real nickelate dataset support a non-arbitrary input-side `C_phi`, or does every operational `C_phi` collapse to prior-art interlayer coherence / sample quality?

## Extracted Next Candidates

1. LP28-S1A: Real sealed P0 feasibility test
   - A: same-sample or predeclared matched-sample input packet exists with >=6 complete rows
   - B: current nickelate data cannot satisfy the sealed-input standard

2. LP28-S1B: `C_phi` baseline-collapse theorem
   - A: any c-axis Drude-fraction `C_phi` collapses to generic interlayer coherence under realistic sample counts
   - B: adding `E_z2`, `Gamma_phi`, and `E_floor` creates a nontrivial input-side rank order

3. LP28-S1C: 120 K normal-state gate validity
   - A: a forbidden-output-free optical gate can certify 120 K normal-state status
   - B: pressure/density-wave/sample-history context makes this certification output-contaminated

## Next Priority Recommendation

Do not continue tuning `I_phi` algebra. The next useful window should attack LP28-S1A or LP28-S1B. The strongest route is LP28-S1A because it can quickly determine whether this protocol has any executable experimental substrate.

