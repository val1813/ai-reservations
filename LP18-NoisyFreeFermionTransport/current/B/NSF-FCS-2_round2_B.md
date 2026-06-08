# NSF-FCS-2 Round 2 B Review

**Role:** B博士, wild cross-disciplinary attack.

**Scope boundary:** This review uses the revised Round 2 package supplied by PI: stop check, current status, direct delta test, off-center reverse, FDT normalization, Qhat model comparison, and activity controls. I did not read `current/A` or depend on A.

## 1. Nonstandard Structure Map: Information Geometry + Bayesian Model Comparison

I will not map this as "transport scaling" first. I map it as a statistical manifold problem.

Define the finite-volume FDT surface:

`M_FDT = { ledger models with lambda_T'' - 2 G_T = 0 }`.

The measured object

`R2 = lambda_T'' - 2 G_T`

is then not just a residual. It is the normal coordinate measuring how far a perturbed Markov model leaves the FDT manifold under a chosen perturbation protocol.

The revised package now gives three independent coordinates of this geometry:

- Density-bias NESS path: `rho_left = rho_bar - delta/2`, `rho_right = rho_bar + delta/2`.
- Reversal symmetry test: `delta -> -delta` at `rho_bar=0.4,0.5,0.65`.
- Kinetic-activity path: `reversible_side` versus `nonLDB_site_skew`.

In this map, the central claim is not "Qhat has exponent 1/2." The central claim is:

`R2/G_T` is the second normal curvature of the FDT manifold along the density-bias NESS direction.

Formally, near equilibrium:

`R2/G_T = K_delta(L, alpha, rho_bar) delta^2 + K_A(L, alpha) A + K_deltaA(L, alpha, rho_bar) delta A + higher orders`.

Round 2 has strong evidence for the first coordinate:

- raw `R2 ~ delta^2` before `Qhat` normalization;
- no detectable odd-in-delta contamination under reverse bias;
- finite-volume equilibrium FDT convention is now explicitly normalized.

Bayesian translation: the revised package increases evidence for a "curvature residual" model over a "normalization/circularity artifact" model. But the posterior over asymptotic models for `K_delta(L)` remains broad. The AIC comparison says the best current empirical model is log drift, not power law.

## 2. Biggest New Attack / New Prediction

The largest new attack is orthogonality of perturbation channels.

If density-bias NESS residual and non-LDB kinetic residual are genuinely different normal directions away from `M_FDT`, then a small factorial experiment should separate them:

`delta in {0, small}`, `A in {0, small}`, with both `reversible_side` and `nonLDB_site_skew`.

Prediction under the curvature model:

- `reversible_side`: no `A`-linear residual at `delta=0`, and density-bias curvature remains dominated by `delta^2`.
- `nonLDB_site_skew`: an `A`-linear residual can appear at `delta=0`.
- mixed `delta,A` runs should expose whether the two normal directions add independently or whether there is a nonzero interaction term `K_deltaA delta A`.

The dangerous outcome would be: `K_delta(L)` changes substantially when a formally LDB-preserving traffic factor is added. That would mean the density-bias residual is not a clean NESS curvature, but a fragile kinetic/normalization artifact.

The positive new prediction is sharper than current mainline:

> In long-jump exclusion, the density-bias residual is an even-in-delta FDT-manifold curvature, while true non-LDB skew creates a distinct first-order normal displacement already at equal density.

That is a better structural claim than arguing over the current small-window `Qhat(L)` exponent.

## 3. Weakness Most Likely To Downgrade The Mainline

The mainline's most downgrade-prone weakness is unresolved `L` behavior.

Round 2 killed the overclaim `Qhat ~ L^{1/2}`. That was the right move. But after that kill, the remaining claim is still small-L empirical evidence:

- centered data: `L=4..8`;
- off-center data: mostly `L=4..7`;
- activity controls: `L=4..6`;
- model comparison favors log drift in every tested dataset.

This means the revised mainline is structurally coherent but not yet asymptotic. If later `L` windows show `K_delta(L)` saturating, the broad "NESS residual scaling" story becomes a finite-size curvature observation, not a transport-scaling proposition.

The package should therefore avoid any language that implies universal growth, anomalous scaling, or exponent discovery.

## 4. Better Redirect Subclaim

Yes, there is a more valuable redirect subclaim.

North Star:

> The robust object is not a power-law `Qhat`; it is the finite-volume information-geometric curvature by which density-bias NESS leaves the equilibrium FDT manifold, with even-in-bias symmetry and separable LDB/non-LDB perturbation directions.

Score: **8.4/10**.

This scores higher than the current "NESS FDT residual scaling" mainline because it absorbs all Round 2 fixes naturally:

- direct raw `delta^2` becomes the curvature measurement;
- reverse-bias tests become evenness of the normal coordinate;
- FDT normalization becomes the definition of the base manifold;
- Qhat model comparison becomes model selection over curvature growth;
- activity controls become tangent/normal perturbation separation.

## 5. Next Minimal Verifiable Proposition

Run a minimal `2 x 2 x 2` perturbation ledger:

- `delta = 0, 0.02`;
- `A = 0, 0.05`;
- `activity_mode = reversible_side, nonLDB_site_skew`;
- at `L=4..7`, `alpha=0.5,1.0`, with fixed `rho_bar=0.5`.

Fit:

`R2/G_T = c0 + c_delta delta^2 + c_A A + c_deltaA delta A`.

Pass condition:

- `reversible_side`: `c_A` and `c_deltaA` numerically zero within ledger precision;
- `nonLDB_site_skew`: `c_A` nonzero at `delta=0`;
- density-bias `c_delta` remains stable between `A=0` and reversible-side `A>0`.

This is the smallest test that distinguishes "curvature residual" from "kinetic artifact."

## 6. Verdict

**Verdict: REDIRECT.**

Reason: the revised package is much better structured than Round 1 and should not be downgraded as a failed program. The circularity, reverse-bias, and normalization attacks are materially answered. However, the strongest surviving object is no longer the original `Qhat` scaling mainline. The highest-value version is the redirected information-geometric curvature claim: density-bias NESS produces an even-in-delta normal displacement from the finite-volume FDT manifold, while non-LDB skew is a distinct perturbation direction.

So: keep the data package, keep the residual, abandon exponent-centered framing, and redirect NSF-FCS-2 to the curvature/separability subclaim.
