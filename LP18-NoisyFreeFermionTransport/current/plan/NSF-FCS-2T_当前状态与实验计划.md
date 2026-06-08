# NSF-FCS-2T 当前状态与实验计划

**Active subclaim:** parity tomography of finite-volume FDT-residual response channels.

## Working Claim

The ledger residual

`R2=lambda_T''-2G_T`

is used as a finite-window parity tomography observable. The goal is to separate response channels by transformation signatures:

- density bias: `delta -> -delta`
- activity skew: `A -> -A`
- reversible traffic vs non-LDB skew

## Established Before This Stage

- density bias gives `R2=C_L delta^2 + D_L delta^4`, with `C_L>0` for tested `L=4..7`, `alpha=0.5,1.0`;
- equal-density `nonLDB_site_skew` gives an even `A^2` response;
- `reversible_side` preserves equilibrium FDT but renormalizes NESS curvature;
- nonLDB skew was additive with density bias in the one-signed mixed window `delta=+0.04,A=±0.10`.

## Open Ambiguity

Equal-density `A^2` does not rule out a signed mixed term away from equal density:

`delta A`

The decisive test is a signed mixed-parity fit using both `delta=+d,-d` and `A=+a,-a`.

## Plan

Run:

- `L=4..7`
- `alpha=0.5,1.0`
- `rho_bar=0.5`
- `delta=0,+0.02,-0.02,+0.04,-0.04`
- `A=0,+0.05,-0.05,+0.10,-0.10`
- `activity_mode=nonLDB_site_skew,reversible_side`

Fit:

`R2/G_T = c0 + c_delta2 delta^2 + c_A2 A^2 + c_deltaA delta A + c_delta2A2 delta^2 A^2`

Decision:

- `c_deltaA` nonzero: parity tomography keeps but separability weakens to projected equal-density channel.
- `c_deltaA` floor-scale: separability strengthens and reviewer gate becomes plausible.
- reversible control unstable: reversible traffic becomes an uncontrolled NESS coefficient renormalizer.

## Signed Mixed-Parity Result

Completed signed grids:

- `current/plan/nsf_fcs_2T_signed_grid_nonldb_L4_7.csv`
- `current/plan/nsf_fcs_2T_signed_grid_reversible_L4_7.csv`
- `current/plan/nsf_fcs_2T_signed_basis_fit_summary.csv`

Result:

- `nonLDB_site_skew`: `c_deltaA` is numerical-floor (`O(1e-7)` or below), while `c_A2=O(1e-3..1e-2)` and `c_delta2=O(1e-1)`.
- `reversible_side`: equilibrium residual remains floor-scale, but NESS curvature is renormalized through sizable higher mixed terms; it is not a strict separability null.

Current decision:

Proceed to conditional REVIEWER gate as a finite-window ledger diagnostic.

Reviewer-gate claim:

> In the tested finite-volume long-jump open-exclusion ledger, `R2=lambda_T''-2G_T` acts as a parity-tomography diagnostic: centered density bias contributes an even `delta^2` channel, equal-density nonLDB site skew contributes an even `A^2` channel, the signed mixed `delta A` channel is numerical-floor in the tested window, and reversible LDB traffic preserves equilibrium FDT while renormalizing density-biased NESS coefficients.

Mandatory caveats:

- finite-window only;
- dimensionless Markov-affinity ledger convention only;
- not asymptotic scaling;
- not universal FDT anomaly;
- not an analytic theorem.
