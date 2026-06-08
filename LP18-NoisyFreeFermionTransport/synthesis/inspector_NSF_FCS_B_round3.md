# INSPECTOR report: NSF-FCS-1 B Round 3

Input checked:

- `current/B/NSF_FCS_round3_B.md`
- `synthesis/PI_NSF_FCS_round2_synthesis.md` only for formula-background consistency.

Forbidden input:

- Did not read A output.

## Q1. 量纲校对

### `F_R=beta(mu_R-mu_ref)`

- LHS SI unit: dimensionless affinity.
- RHS SI unit: `beta` has unit `1/energy`; `mu_R-mu_ref` has unit `energy`; product is dimensionless.
- Match: pass.

### `G_R=dJ_R/dF_R|_0`

- `b(x)=sum_y k_0(x,y) g_R(x,y)` has unit `count/time`.
- `J_R=<b_R>_{pi_F}` has unit `count/time`.
- Since `F_R` is dimensionless, `G_R` has unit `count/time`.
- Match: pass.

The conversion

`G_R=dJ_R/dF_R=(1/beta) dJ_R/d(Delta mu)`

is dimensionally correct because `F_R=beta Delta mu`.

### `lambda_R''(0)`

For

`lambda_R(chi)=lim_{t->infty} t^{-1} log E_pi exp[chi Q_R(t)]`,

with particle count treated as the count convention unit:

- `chi Q_R` is dimensionless.
- `lambda_R` has unit `1/time`.
- Differentiating twice with respect to dimensionless counting field gives `count^2/time`.
- Match: pass.

### `S_R=lambda_R''/G_R`

- RHS unit: `(count^2/time)/(count/time)=count`.
- This is effectively dimensionless only under the stated particle-count convention.
- Match: conditional pass.

Warning: B correctly states both "unit is count" and "used as dimensionless in count convention". Downstream tables should keep this convention explicit; otherwise `S_R` is not a pure SI-dimensionless scalar.

### Decomposition terms

`a(x)=sum_y k_0(x,y) g_R(x,y)^2` has unit `count^2/time`, so `<a>` has unit `count^2/time`.

From `-L_0 phi=h`, with `L_0` unit `1/time` and `h=b-J` unit `count/time`, `phi` has unit `count`. Therefore `2<h,phi>` has unit `count^2/time`.

Thus

`lambda_R''(0)=<a>+2<h,phi>+2<C>`

is dimensionally consistent if `2<C>` is also a current-cumulant rate residual with unit `count^2/time`. Pass.

### Transcendental arguments

`exp[alpha_{xy} F_R+O(F_R^2)]` and `exp(chi g_R)` have dimensionless arguments because `alpha_{xy}`, `F_R`, `chi`, and `g_R` are all dimensionless in the stated convention. Pass.

## Q2. 符号/方向校对

### Row-generator convention and stationary equation

B uses

`(L_F f)(x)=sum_y k_F(x,y)[f(y)-f(x)]`.

The corresponding matrix acting on column observables has off-diagonal entries `L[x,y]=k(x,y)` and diagonal `L[x,x]=-sum_y k(x,y)`. A stationary distribution is therefore a row vector satisfying

`pi L=0`.

This is self-consistent with the stated row-generator convention. Pass.

### Poisson sign

On the centered subspace, this generator has non-positive spectrum in the reversible benchmark. Solving

`-L_0 phi=h`

is equivalent to the Round 2 synthesis notation `L phi=-h`, and gives `phi=(-L_0)^{-1}h`. Then `2<h,phi>` has the standard resolvent sign and is not sign-reversed.

The residual definition

`r_phi=-L_0 phi-h`

also matches the Poisson equation. Pass.

### Direction of independent calibration

B states that `G_R` is obtained from finite differences in the affine variable `F_R` and explicitly forbids tuning it with `lambda_R''`. This direction is self-consistent. Pass.

## Q3. 循环论证校对

### `2<C>=lambda_tilt''-<a>-2<h,phi>`

This is acceptable as a residual definition if `lambda_tilt''` is generated independently from the tilted generator principal eigenvalue, while `<a>` and `phi` are generated from the untilted generator and Poisson solve.

Not circular for reporting:

- input 1: untilted generator gives `<a>` and `2<h,phi>`;
- input 2: tilted generator gives total `lambda_tilt''`;
- output: missing residual `2<C>`.

Warning: in `status=C_from_tilted_residual`, the identity

`lambda_tilt''=<a>+2<h,phi>+2<C>`

is true by construction. Therefore `err_balance` cannot be used as an independent validation of the decomposition in residual mode. It is only meaningful when `2<C>` comes from an explicit cross-term formula independent of `lambda_tilt''`. B's text mostly respects this distinction, but the table/status convention should preserve it.

### keep/kill use of residual `C`

The keep/kill criteria are not formally circular if they use calibrated `G_R`, stable `lambda_tilt''`, and `S_R=lambda_tilt''/G_R`. However, criterion 6.2(4) mentions `2<C>` as a reservoir-specific cancellation. If `2<C>` was obtained only as the tilted residual, this criterion checks a numerical residual, not an independently derived mechanism. This is a warning, not a blocker.

## Q4. 数量级校对

No explicit `10^N` versus `10^M` numerical order-of-magnitude estimates are made in the inspected text. No quantity-gap flag.

The proposed tolerances are internally ordered and not dimensionally anomalous:

- `rel_spread(G_R) <= 2%`;
- `rel_spread(lambda_R''(epsilon)) <= 3%`;
- `err_balance <= 3%`;
- Poisson and stationary residual thresholds are dimensionless after normalization by the stated norms.

No blocker.

## Q5. 代数/极限校对

### Tilted generator matrix

For a jump additive functional with increment `g_R(x,y)`, the moment-generating tilted operator is

`(L_chi f)(x)=sum_y k_0(x,y)[exp(chi g_R(x,y)) f(y)-f(x)]`.

Thus the matrix entries are:

- off-diagonal: `L_chi[x,y]=k_0(x,y) exp(chi g_R(x,y))`;
- diagonal: `L_chi[x,x]=-sum_y k_0(x,y)`.

This preserves the original escape rate on the diagonal. At `chi=0`, `L_chi=L_0` and the principal eigenvalue is `lambda_R(0)=0`. Pass.

### Finite-difference formula

The centered second derivative formula

`lambda_R''(0;epsilon)=[lambda_R(epsilon)-2 lambda_R(0)+lambda_R(-epsilon)]/epsilon^2`

is algebraically correct with truncation error `O(epsilon^2)` when `lambda_R` is smooth near zero. Keeping measured `lambda_R(0)` rather than manually setting it to zero is numerically acceptable. Pass.

### Solvability of Poisson equation

`h=b-J` satisfies `<h>_pi=<b>_pi-J=0`, so it lies in the centered subspace. Under the stated finite irreducible assumption, `-L_0 phi=h` is solvable modulo constants, and the gauge `<phi>_pi=0` fixes the solution. Pass.

### keep/kill criteria dependence

The criteria do not rely on uncalibrated `G_R` if section 5.3 is enforced: no linear-response plateau means `S_R` criteria pause rather than kill. They do not rely on unstable `lambda_R''` if section 5.4 is enforced: unstable tilted curvature is explicitly marked.

Warning: this dependence is procedural. The final implementation must propagate `pi_failed`, `lambda_tilt_unstable`, uncontrolled `G_R`, and `C_from_tilted_residual` statuses into the keep/kill decision; otherwise a later table could accidentally apply the criteria to uncalibrated inputs.

## Final verdict

⚠️ INSPECTOR警告，可继续。

No blocking dimension, sign, tilted-generator, finite-difference, or Poisson-convention error was found.

Warnings to carry forward:

1. `S_R` is a count-convention dimensionless ratio; without that convention it has unit `count`.
2. `2<C>=lambda_tilt''-<a>-2<h,phi>` is acceptable as a residual, but cannot then be used to independently validate `err_balance`.
3. keep/kill criteria are acceptable only after calibrated `G_R` and stable `lambda_tilt''`; residual `C` alone is not a mechanistic cross-term derivation.
