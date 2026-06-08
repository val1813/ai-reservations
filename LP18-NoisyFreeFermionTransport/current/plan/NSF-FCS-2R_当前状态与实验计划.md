# NSF-FCS-2R 当前状态与实验计划

**Active subclaim:** finite-volume FDT-residual curvature/separability diagnostic.

## Working Claim

In the ledger's dimensionless Markov-affinity convention, equilibrium satisfies `lambda_T''=2G_T`. Under density-biased NESS, the finite-volume residual

`R2=lambda_T''-2G_T`

is treated as an operational curvature-like coordinate away from the equilibrium FDT surface. The next task is not asymptotic `Qhat(L)` scaling, but coefficient extraction and perturbation separability.

## Constraints From Round 2 A/B + INSPECTOR

- Do not claim `Qhat~L^{1/2}`.
- Do not claim an asymptotic power law.
- Do not call `R2/G_T` a proven second normal curvature without a metric/projection definition.
- Treat `reversible_side` as an LDB traffic sanity control.
- Test `nonLDB_site_skew` with both `A=+a` and `A=-a`; otherwise `A`-linear and `A^2` responses cannot be separated.

## Validation Plan

### 1. Coefficient extraction

Run centered density-bias scans:

- `rho_bar=0.5`
- `delta=0.02,0.04,0.06,0.08`
- `L=4..7`
- `alpha=0.5,1.0`
- `activity_mode=none`

Fit raw `R2` at fixed `L,alpha`:

`R2 = C_L(alpha) delta^2 + D_L(alpha) delta^4`

Decision target:

- `C_L(alpha)` nonzero with stable sign.
- Quartic correction does not dominate the fit window.
- Report CSV paths, command parameters, and fit residuals.

### 2. Activity parity

Run equal-density activity scans:

- `rho_left=rho_right=0.5`
- `A=+0.05,-0.05,+0.10,-0.10`
- `activity_mode=reversible_side,nonLDB_site_skew`
- `L=4..7`
- `alpha=0.5,1.0`

Fit:

`R2/G_T = c0 + c_A A + c_A2 A^2`

Decision target:

- `reversible_side`: `c_A` and `c_A2` remain numerical-floor or explicitly bounded as LDB traffic effects.
- `nonLDB_site_skew`: determine whether the leading term is odd (`A`) or even (`A^2`); do not assume.

### 3. Separability

Only after steps 1 and 2, run a minimal mixed scan:

`R2/G_T = c0 + c_delta delta^2 + c_A A + c_A2 A^2 + c_deltaA delta A`

Decision target:

- density-bias coefficient remains stable under `reversible_side`;
- nonLDB skew contributes a distinct activity channel;
- if `c_deltaA` dominates, the separability claim must be weakened.

## Immediate Next Command

Run coefficient extraction first. Activity parity waits until coefficient extraction is recorded.
