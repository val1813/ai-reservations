# PI Synthesis: LP28-S1 Round 2

## Inputs

- A Round 2: `current-S1/A/round2.json`
- B Round 2: `current-S1/B/round2.json`
- INSPECTOR A Round 2: pass with warnings
- INSPECTOR B Round 2: pass with warnings

## Framework Check

A: lab-facing normal-state c-axis optical/Drude measurement stack, fixed at 120 K.

B: zero-leakage SVD observability matrix and blind audit packet, fixed at 80 K.

They remain independent and distinct. The disagreement is useful: Round 3 must decide whether a single preregistration packet can freeze these choices without output leakage.

## Core Synthesis

Round 2 successfully converted S1 from an idea into two executable protocol candidates. Both passed INSPECTOR at the level of units, direction, mock arithmetic, and circularity under stated assumptions.

The surviving claim is still narrow:

`I_phi` is a preregistered input-side encoder, not a validated predictor.

The strongest operational form is:

`I_phi = E_z2 * C_phi / (kB*T + hbar*Gamma_phi + E_floor)`

but all scientific weight has shifted onto the protocol choices:

- which fixed temperature is allowed (`80 K` vs `120 K`)
- whether `C_phi` is a simple normal-state c-axis Drude fraction or a multi-channel SVD observability score
- how arbitrary coefficients are frozen or sensitivity-tested
- whether baseline-collapse tests are specified before output reveal
- whether canonical hashing and auditor recomputation are exact enough to prevent leakage

## What Changed In Round 2

A made the protocol more lab-realistic: same-sample normal-state c-axis optical decomposition, fixed windows, explicit units, divergence control, and mock arithmetic.

B made the audit more rigorous: deposited artifacts, SHA-256 manifest, canonical recomputation, SVD `C_phi`, and pre-output baseline-collapse checks.

The combined route is stronger than either alone: use A's measurement stack but wrap it in B's zero-leakage audit packet.

## Warnings Entering Round 3

- The `C_phi` matrix is executable but may be arbitrary; keep it as an audit score, not a mechanism.
- The A/B temperature conflict must be resolved by an input-side rule, not by output performance.
- Coefficients (`alpha_z2`, `epsilon_W`, `lambda_vac`, `lambda_strain`, `lambda_res`, `E_z2_ref`) are empirical encoder constants unless externally calibrated.
- Need exact baseline metric, uncertainty/tie rule, and collapse threshold.
- Need exact serializer, CSV dialect, null/NaN handling, numeric precision, column order, timestamp authority, and hash rules.
- Need to confirm the chosen temperature is normal-state for all pressure/sample points, or mark `not_computable`.
- Need a c-axis reverse-discordant mock pair; B's mock did not demonstrate D2.

## Breakthrough-Direction Check

Round 2 moved closer to useful technology: it now gives a way to kill circular nickelate screening claims before output comparison. If implemented, this protocol could prevent expensive optimization around `Tc` artifacts, filamentary zero resistance, or generic interlayer-coherence relabeling.

It is not yet a theory breakthrough. The remaining theoretical bottleneck is whether `C_phi` can be non-arbitrary while still input-side.

## AHA Check

No new AHA beyond Round 1. Round 2 stabilized AHA #S1-1 rather than generating a separate one.

## Round 3 Tasking

Round 3 should produce a single go/no-go packet:

1. Freeze one temperature rule by input-side physics.
2. Decide `C_phi`: simple Drude fraction, SVD observability score, or a two-tier rule where SVD is audit-only and Drude fraction is primary.
3. Define exact baseline-collapse metric and threshold.
4. Define canonical serialization/hash/auditor rules.
5. Sensitivity-test arbitrary constants and state what failure would kill S1.
6. Give final go/no-go table for real experiments.

## Stop Condition

No hard stop. N=2<3, so SOP requires Round 3.

