# PI Synthesis: LP28-S1 Round 1

## Inputs

- A Round 1: `current-S1/A/round1.json`
- B Round 1: `current-S1/B/round1.json`
- INSPECTOR A Round 1: pass with warnings
- INSPECTOR B Round 1: pass with warnings
- AHA visitor: yes, registered in `synthesis/aha记录.md`

## A/B Independence And Framework Check

A framework: input-output separation in layered-superconductor spectroscopy.

B framework: information leakage plus network observability.

They are distinct. Both agents reported not reading the other side's output.

## Core Synthesis

Round 1 moved S1 forward, but narrowed the claim sharply. `I_phi` is not a mechanism and not a validated predictor. It can only survive as a frozen input-side encoder:

`I_phi = f_P0(X_pre)`

where `P0` fixes formulas, units, windows, thresholds, missing-data rules, and coefficient provenance before any bulk superconducting output is opened.

The shared fatal bottleneck is `C_phi`. If `C_phi` is defined with Josephson plasma, superfluid density, Meissner screening, zero resistance, critical current, bulk phase stiffness, or transition-width fits, then it is output leakage and S1 fails. The best surviving version is:

`C_phi = input-side observability/connectivity score`

computed from pre-output variables such as normal-state c-axis optical response, `dz2` spectral proxy, structural/apical-O metrics, and normal-state dephasing.

## AHA

AHA #S1-1: `C_phi` is not primarily a material descriptor; it is the audit variable for whether the phase-bus index leaks bulk superconducting output.

Why it matters: this changes the next task from "find a better predictor formula" to "build a blind recomputation protocol." That is closer to actual technology progress because it can kill false routes before expensive pressure/film optimization.

## INSPECTOR Warnings To Feed Round 2

- Define exact units and allowed ranges for `E_z2`, `C_phi`, `Gamma_phi`, `E_floor`, stabilizers, and coefficients.
- Prevent the divergence at `T -> 0`, `Gamma_phi -> 0`, `E_floor -> 0`.
- Freeze spectral windows, pressure/temperature grid, normalizations, coefficient provenance, missing-data rules, and output blinding.
- Provide a concrete three-sample preregistration packet with hashes/timestamps and auditor recomputation tolerance.
- Run baseline-collapse checks against `S_dz2` only, c-axis optical weight only, disorder/structure only, and dephasing/scattering only.

## Breakthrough-Direction Check

This is closer to a real breakthrough than LP28's original mechanism framing, but only as an experimental protocol. If true, it changes how nickelate searches are run: instead of chasing `Tc`/zero resistance after pressure or strain sweeps, labs would first perform an input-side leak-free audit of phase-bus readiness. It can open one concrete direction: blind, same-sample screening of recoverable interlayer phase-bus readiness before bulk-output testing.

This does not yet change many literature conclusions. It changes the decision procedure for future experiments.

## Round 2 Tasking

Round 2 should not broaden. It should produce one executable protocol:

1. A: specify a lab-feasible measurement stack for `E_z2`, `Gamma_phi`, `E_floor`, and the least-circular `C_phi`, with literature/data provenance and exact units.
2. B: specify the `C_phi` transfer matrix: rows, units, normalization, `sigma_ref`, missing-data rules, and auditor recomputation workflow.
3. Both: include a three-sample mock calculation and baseline-collapse tests.

## Stop Condition

No hard stop. N=1<3, so SOP requires Round 2.

