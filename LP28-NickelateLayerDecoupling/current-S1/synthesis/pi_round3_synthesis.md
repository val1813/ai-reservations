# PI Synthesis: LP28-S1 Round 3

## Inputs

- A Round 3: `current-S1/A/round3.json`
- B Round 3: `current-S1/B/round3.json`
- INSPECTOR A Round 3: pass with warnings
- INSPECTOR B Round 3: pass with blockers to fix before P0/GO

## Core Verdict Before Reviewer

S1 is not validated, but it survived the three-round exploration as a bounded preregistration protocol candidate.

The strongest unified protocol is:

1. Use A's lab-facing primary index: fixed 120 K, input-side normal-state optical gate, Drude-fraction `C_phi_primary`.
2. Use B's adversarial audit wrapper: canonical serialization, SHA-256 manifest, auditor recomputation, baseline-collapse kill rules, and anti-arbitrariness sensitivity grid.
3. Treat B's SVD observability matrix as audit-only, not the primary `C_phi`.

## Fixes Required By INSPECTOR B

The following are now binding in the unified protocol:

- Auditor allowed inputs include the hashed comparison artifacts `I_phi_labels.csv` and `baseline_scores.csv` for byte-for-byte comparison only. They may not include bulk superconducting outputs.
- `n_complete < 6` is not `GO_PROTOCOL_ONLY`. It is `NO_GO_UNDERPOWERED` for S1 survival. The packet may be archived as a pilot but cannot claim protocol survival.
- Add required artifact `sensitivity_grid_results.csv`.
- `E_floor` constants must be named explicitly: `E_floor_intercept_meV`, `E_floor_disorder_slope_meV`.
- `T_prior_upper_K`, if used in any acquisition-temperature guard, must have a provenance field and cannot come from same-sample output.

## Unified Protocol

Primary encoder:

`I_phi = E_z2_meV*C_phi_primary/(kB_meV_per_K*120 + hbarGamma_phi_meV + E_floor_meV)`

Primary `C_phi`:

`C_phi_primary = max(0, min(1, W_c_Drude/(W_c_Drude + W_c_incoh + epsilon_W)))`

Forbidden in construction:

`Tc`, zero resistance, shielding, Meissner fraction, critical current, Josephson plasma, superfluid density, condensate spectral weight, bulk phase stiffness, transition width, and phase-diagram labels.

Go/no-go hard rules:

- GO requires at least 6 complete preregistered rows.
- GO requires exact auditor recomputation from sealed input artifacts.
- GO requires coefficient sensitivity to pass before output reveal.
- GO requires post-output noncollapse against frozen baselines.
- Any post-output retuning, row exclusion, threshold change, or endpoint drift is NO-GO.

## Breakthrough-Direction Check

This is a technical-progress protocol, not a theory mechanism. Its value is that it can kill circular nickelate screening claims before they consume experimental effort. The actual theoretical bottleneck remains unresolved: whether a non-arbitrary, input-side `C_phi` exists in real samples rather than merely in an auditable encoder.

If this protocol works, it changes the experimental workflow more than the explanatory theory: run blind input-side phase-bus readiness audits before interpreting `Tc`, zero resistance, or shielding.

## AHA Check

No new AHA beyond Round 1. Round 3 hardened AHA #S1-1 into a final protocol constraint.

## Reviewer Feed

Reviewer should attack:

- whether same-sample or predeclared matched-sample inputs are realistically obtainable
- whether 120 K can be guaranteed normal-state without output leakage
- whether Drude-fraction `C_phi` collapses to prior-art interlayer coherence
- whether coefficient/sensitivity rules are strong enough or still arbitrary
- whether the protocol is too underpowered for real nickelate sample counts

## Stop Condition

N=3 reached. Enter mandatory REVIEWER.

