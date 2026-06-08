# PI NSF-FCS-2 Round 2 FDT Normalization Ledger

## Purpose

Reviewer attack 1 required the exact normalization behind:

`lambda_T''(0)=2G_T`

## Script Convention

Source: `scripts/nsf_fcs_transport_ledger.py`

1. The Markov generator is a row generator. Off-diagonal entry `mat[src,dst]` stores the jump rate, and diagonal entries are negative escape rates.
2. The tilted generator multiplies each jump rate by `exp(chi * g)`, where:
   - `chi` is a dimensionless counting field;
   - `g` is the dimensionless transported-particle increment for the observed current.
3. `lambda_tilt_second` is computed as:

`[lambda(chi)-2lambda(0)+lambda(-chi)]/chi^2`

Thus `lambda_T''` has units of inverse time in the script's rate units.

4. Reservoir affinity `F` is dimensionless. In `two_terminal_symmetric` mode:

`eta_left=-(1-split)F`, `eta_right=split F`

and rates are modified as:

`in = rho * r * exp(+eta/2)`, `out=(1-rho) * r * exp(-eta/2)`.

5. The transport current `J` is the stationary expectation of the left-terminal `out-in` counting observable. `G_T` is computed as:

`G_T = dJ/dF`

with `F` dimensionless, so `G_T` also has units of inverse time.

## Dimensional Verdict

In this ledger convention:

- `lambda_T''`: inverse time
- `G_T`: inverse time
- `R2=lambda_T''-2G_T`: inverse time
- `S_T=lambda_T''/G_T`: dimensionless
- `Qhat=R2/(delta^2 G_T)`: dimensionless, since density difference `delta` is dimensionless

Therefore `lambda_T''=2G_T` is dimensionally valid in the script units. It should be described as a convention-specific finite-volume FDT identity for the dimensionless entropy-affinity normalization, not as a physical SI conductance equation without beta/charge/time factors.

## Required Wording

Use:

> In the ledger's dimensionless Markov-affinity convention, with counting field `chi` conjugate to particle count and `F` the dimensionless reservoir affinity, equilibrium finite-volume FDT gives `lambda_T''(0)=2G_T`.

Avoid:

> The physical electrical noise equals twice the conductance.

unless charge, temperature, and physical time units are restored.
