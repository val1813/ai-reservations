# NSF-FCS-2R validation review - B

**Role:** B博士, cross-disciplinary structural attack.
**Package reviewed:** coefficient/parity/separability package.
**Independence note:** did not read `current/A` outputs for this round.

## 0. Verdict upfront

**Verdict: REVIEWER_GATE with one mandatory downgrade.**

The package is strong enough to enter REVIEWER gate as a finite-window ledger diagnostic, not as an analytic theorem or asymptotic scaling claim. The valuable object is not `Qhat(L)` and not a universal exponent. It is a parity-resolved response algebra around the equilibrium FDT surface:

`R2 = lambda_T'' - 2 G_T`

with density bias, non-LDB activity skew, and reversible traffic occupying different slots.

## 1. Nonstandard structural map

Borrowed structure: **signal-processing / circuit renormalization**, not geometry first.

Treat the equilibrium FDT identity as a balanced bridge circuit:

`lambda_T'' - 2G_T = 0`.

Perturbations are not forces on the same axis. They are three distinct circuit operations:

1. **Density imbalance as differential-mode injection**

   Centered density bias has an exchange symmetry:

   `delta -> -delta`

   reverses left/right labels but should not change the scalar distance from the FDT bridge. Therefore the first allowed term is even:

   `R2_density(L,alpha,delta) = C_L(alpha) delta^2 + D_L(alpha) delta^4 + ...`

   The observed `C_L(alpha)>0` across `L=4..7`, `alpha=0.5,1.0` means `delta^2` is not just a Taylor convenience; it is the leading symmetry-allowed bridge-unbalance channel in the tested ledger.

2. **nonLDB_site_skew as phase-insensitive activity power**

   I originally would have expected an odd activity current, `A`, if non-LDB skew behaved like a directed forcing. The parity scan kills that simple story. Equal-density `A=+a` and `A=-a` collapse to numerical precision, while `A^2` survives:

   `R2_nonLDB/G_T = b_L(alpha) A^2 + O(A^4)`.

   Structural translation: the measured residual is not seeing the signed activity drive; it is seeing the activity **power** injected by breaking LDB. Like a lock-in amplifier measuring second harmonic power, the sign of the skew is erased by the equal-density protocol.

3. **Mixed additivity as orthogonal channel summation**

   In the tested mixed window, non-LDB skew nearly satisfies:

   `R2(delta,A) ~= R2(delta,0) + R2(0,A) - R2(0,0)`.

   This is the strongest new structural feature. It says the two even channels behave like separable quadratic coordinates:

   `R2/G_T ~= c0 + c_delta delta^2 + c_A2 A^2`

   with the mixed defect small for `nonLDB_site_skew` (`~1e-4` relative). The natural mathematical object is a local graded response ring:

   `R = R0 + <delta^2> + <A^2> + higher ideals`,

   where the cross ideal `<delta A>` is not resolved in the current symmetric window.

4. **reversible traffic renormalization as impedance matching**

   `reversible_side` is not a residual source at equilibrium; it keeps the FDT bridge balanced to numerical floor. But under density bias it changes the curvature coefficient at a few-percent level. In circuit language it does not inject voltage; it changes impedance. In RG language it is not a relevant symmetry-breaking operator; it is a marginal/metric-like renormalization of the NESS response coefficient:

   `C_L(alpha) -> C_L(alpha; A_rev)`,

   while still preserving `R2(delta=0,A_rev) ~= 0`.

This map explains why the package is cleaner than the old exponent story: `delta^2`, `A^2`, mixed additivity, and reversible traffic renormalization are four different algebraic roles, not one noisy scaling curve.

--- INSPECTOR_CHECK ---
[formula] `R2_density = C_L(alpha) delta^2 + D_L(alpha) delta^4`; `R2_nonLDB/G_T ~= b_L(alpha) A^2`; mixed check `Delta_mix = R2(delta,A)-R2(delta,0)-R2(0,A)+R2(0,0)`.
[direction] finite-window parity-resolved response algebra supported; no asymptotic exponent asserted.
[data] PI synthesis files for coefficient extraction, activity parity, separability; CSV paths listed there under `current/plan`.
[assumption] ledger convention `lambda_T''=2G_T` at equilibrium; tested window `L=4..7`, `alpha=0.5,1.0`, small `delta,A`.

## 2. Maximal new attack / new prediction

**Attack:** the observed `A^2` channel may be a protocol-even artifact caused by equal-density centering, not an intrinsic non-LDB law.

If non-LDB skew has a hidden odd component, equal density may project it out. The current parity result proves:

`partial_A (R2/G_T)|_{rho_left=rho_right=0,A=0} ~= 0`.

It does not prove:

`partial_A (R2/G_T)|_{delta != 0,A=0} = 0`.

**New prediction:** at finite density bias, nonLDB skew should generate a symmetry-allowed mixed odd term:

`R2/G_T = c0 + c_delta delta^2 + c_A2 A^2 + c_deltaA delta A + ...`

and `c_deltaA` is the first place where the sign of `A` can reappear. If `c_deltaA` is nonzero and stable under smaller `delta,A`, then the equal-density `A^2` story remains true but incomplete. If `c_deltaA` is also numerical-floor, then the package upgrades from "parity-resolved empirical diagnostic" toward a real separability theorem candidate.

Concrete falsifier:

- run `delta=+0.02,-0.02,+0.04,-0.04`;
- run `A=+0.05,-0.05,+0.10,-0.10`;
- fit the full signed basis `{delta^2, A^2, delta A, delta^2 A^2}`;
- require sign flips of `delta A` under either `delta -> -delta` or `A -> -A`.

## 3. Higher-value subclaim

Yes. The higher-value subclaim is not "finite-volume curvature" alone; it is **parity tomography of FDT-violating response channels**.

One-sentence North Star:

> In open long-jump exclusion, the finite-volume FDT residual defines a parity-tomography ledger that separates density-gradient curvature, non-LDB activity power, and reversible traffic renormalization by their transformation signatures under `delta -> -delta` and `A -> -A`.

Score: **8.7/10**.

Reason: this is more reviewable and more falsifiable than an exponent claim, and it suggests a compact table of perturbation operators. It remains finite-window and computational unless an analytic coefficient theorem is added.

## 4. Mandatory downgrade

Downgrade any statement that says or implies:

- `R2/G_T` is a proven geometric second normal curvature;
- the package establishes asymptotic `L` scaling;
- reversible traffic is a strict separability null;
- nonLDB skew is generally `A^2` without specifying equal-density and the tested protocol.

Correct downgrade wording:

> `R2` is a finite-volume, ledger-defined curvature-like residual coordinate. In the tested window, density bias contributes an even `delta^2` channel, equal-density nonLDB skew contributes an even `A^2` channel, and reversible LDB traffic preserves equilibrium FDT while renormalizing NESS response coefficients.

## 5. Next minimal verifiable proposition

The next proposition should be a signed mixed-parity test:

> At small `delta,A`, the signed mixed coefficient `c_deltaA` in `R2/G_T` is either numerical-floor for nonLDB skew, proving stronger separability to this order, or nonzero with the predicted parity flip, proving that equal-density `A^2` is a projected channel rather than the full non-LDB response.

Minimal fit:

`R2/G_T = c0 + c_delta2 delta^2 + c_A2 A^2 + c_deltaA delta A + c_delta2A2 delta^2 A^2`

Minimum ledger window:

- `L=4..7`;
- `alpha=0.5,1.0`;
- `delta=0,+0.02,-0.02,+0.04,-0.04`;
- `A=0,+0.05,-0.05,+0.10,-0.10`;
- `activity_mode=nonLDB_site_skew,reversible_side`;
- same `eps` and counting-field ledger convention as coefficient extraction.

Decision rule:

- if `nonLDB_site_skew`: `|c_deltaA|` stable and above numerical floor, KEEP diagnostic but weaken separability to "equal-density separability";
- if `|c_deltaA|` floor-scale and `c_A2` stable, promote to REVIEWER-ready separability subclaim;
- if reversible-side mixed defect grows or changes sign under refinement, downgrade reversible traffic to an uncontrolled NESS coefficient renormalizer.

## 6. Final B decision

**Verdict: REVIEWER_GATE.**

The coefficient/parity/separability package is good enough for reviewer gate as a finite-volume diagnostic with explicit finite-window provenance. The required downgrade is semantic and mathematical: no asymptotic law, no proven normal curvature, and no symmetric separability claim for reversible traffic.

The package's best form is:

> parity-resolved finite-volume FDT-residual response algebra: `delta^2` density curvature, equal-density `A^2` non-LDB activity power, additive mixed behavior in the tested nonLDB window, and reversible traffic as NESS curvature renormalization rather than an FDT-violating source.
