# INSPECTOR A Round3

Input checked: `current/A/round3_A.md`

Scope: INSPECTOR_CHECK block and key formulas only. B-side files were not read.

## Q1. Dimensional check

### Formula: `r_{jk}=2|J_{jk}|^2/gamma_phi`

- LHS SI unit: `s^{-1}` transition rate.
- RHS SI unit: `(s^{-1})^2 / s^{-1} = s^{-1}`.
- Match: yes.

### Formula: `r(r)=2J0^2/(gamma_phi |r|^{2alpha})`

- LHS SI unit: `s^{-1}`.
- RHS SI unit: `(s^{-1})^2 / s^{-1}` times dimensionless lattice distance factor = `s^{-1}`.
- Match: yes, provided `r` is measured in lattice spacings.

### Formula: `mu = 2alpha - 1`

- LHS SI unit: dimensionless exponent.
- RHS SI unit: dimensionless.
- Match: yes.

### Formula: `G_R(L) ~ C_alpha (2J0^2/gamma_phi) L^{-(2alpha-2)}`

- LHS SI unit: for `G_R := partial J_R / partial(rho_L-rho_R)`, density difference is dimensionless and reservoir current has unit `s^{-1}`, so `G_R` has unit `s^{-1}`.
- RHS SI unit: `C_alpha` dimensionless; `2J0^2/gamma_phi` has unit `s^{-1}`; `L` is dimensionless in lattice units. Total `s^{-1}`.
- Match: yes.

### Formula: `lambda_R''(0) ~ C_alpha^noise (2J0^2/gamma_phi) L^{-(2alpha-2)}`

- LHS SI unit: `lambda_R(s)=lim_{t->infty} t^{-1} log E exp(s Q_R)`, with `Q_R` dimensionless, so `lambda_R''(0)` is per time, `s^{-1}`.
- RHS SI unit: `s^{-1}`.
- Match: yes.
- Status: dimensional consistency is not evidence of correctness; this formula depends on the extra current-noise/conductance same-scaling hypothesis.

### Transcendental arguments

- `log L`: valid only if `L` is dimensionless. A states `L` is in lattice spacings; acceptable.
- `log E[...]`: expectation is dimensionless; acceptable.

Q1 result: pass.

## Q2. Sign and direction check

### Direction: `1<alpha<3/2`

Claim checked: as `alpha` decreases from `3/2` to `1`, the conductance decay exponent decreases from `1` to `0`.

- Exponent: `2alpha-2`.
- At `alpha=3/2`: `2alpha-2 = 1`.
- At `alpha -> 1+`: `2alpha-2 -> 0+`.
- Therefore `L^{-(2alpha-2)}` decays less strongly as `alpha` decreases, so boundary conductance is enhanced relative to diffusive `L^{-1}`.

Direction is correct.

### Mapping direction: `p(r) ~ |r|^{-(1+mu)}` and `J(r) ~ r^{-alpha}`

Zeno rate gives `r(r) ~ r^{-2alpha}`. Matching `2alpha = 1+mu` gives `mu=2alpha-1`. For `1<alpha<3/2`, `1<mu<2`, consistent with the fractional-Fick regime invoked.

Direction is correct.

Q2 result: pass.

## Q3. Circularity check

The boundary conductance scaling is not generated only from the assumed output; it is obtained by:

1. Zeno projection to a classical long-jump rate kernel.
2. Matching the kernel exponent to `p(r) ~ |r|^{-(1+mu)}`.
3. Importing fractional Fick law scaling for matching boundary-driven long-jump exclusion.

No circularity found for the mean reservoir-current/conductance scaling, subject to the stated reservoir-model matching assumption.

For `lambda_R''(0)`, the same `L` scaling is not independently derived in A Round3. It is explicitly introduced through an Einstein/Green-Kubo or mobility-conductance same-scaling assumption. This is not circular if kept as an assumption, but it would become circular if later used as a verified FCS result.

Q3 result: pass with warning on future use of `lambda_R''(0)`.

## Q4. Order-of-magnitude gap check

No numerical comparison of the form `10^N` vs `10^M` appears in the inspected block or key formulas. No magnitude-gap issue found.

Q4 result: pass.

## Q5. Algebra and limiting checks

### Algebra: fractional exponent substitution

Fractional Fick law input:

`J_R(L) ~ const(mu,reservoirs) (rho_L-rho_R) L^{-(mu-1)}`

Substitution:

`mu = 2alpha - 1`

Then:

`mu - 1 = 2alpha - 2`

Therefore:

`J_R(L)/(rho_L-rho_R) ~ C_alpha (2J0^2/gamma_phi) L^{-(2alpha-2)}`

Algebra is correct.

### Limit: `alpha -> 3/2-`

`2alpha-2 -> 1`, hence `G_R(L) ~ L^{-1}` up to a prefactor that may cross over or become singular near the finite-second-moment boundary. This is directionally consistent with the diffusive side, but does not by itself prove the exact critical `alpha=3/2` log.

### Limit: `alpha -> 1+`

`2alpha-2 -> 0+`, hence conductance tends toward an `L^0` scaling candidate. This is consistent with increasingly long-ranged transport, but the document correctly avoids extending below `alpha<=1`, where the hopping sum/Zeno assumptions become more dangerous.

### Critical formula: `alpha=3/2`, `G_R(L) ~ C_c (2J0^2/gamma_phi) (log L)/L`

The algebraic origin is clear:

`sum_{r<=L} r^2 r(r) ~ sum_{r<=L} r^{-1} ~ log L`

and finite-size Fick substitution gives `D_eff(L)/L ~ (log L)/L`.

However, this is a cutoff/Fick-law heuristic, not a checked theorem for the exact boundary reservoir current and not a checked FCS result. A Round3 mostly marks this correctly as "candidate", "strong inference", or "needs verification". The wording is acceptable if downstream synthesis preserves that status.

Q5 result: pass with warning: the critical log must remain a candidate/strong inference, not a proven conclusion.

## Q6. Integrated verdict

INSPECTOR verdict: pass with warnings.

No blocking dimensional, sign, exponent-substitution, or limit-direction error was found in the inspected formula

`G_R(L) ~ C_alpha (2J0^2/gamma_phi) L^{-(2alpha-2)}`

for `1<alpha<3/2`.

Required warnings to carry forward:

1. `lambda_R''(0)` having the same `L` scaling as boundary conductance is correctly marked in A Round3 as an additional FCS/Green-Kubo-level assumption. It must not be upgraded to an established result without a tilted-generator or current-fluctuation derivation.
2. The `alpha=3/2` `(log L)/L` scaling is plausible from truncated second moment plus Fick scaling, but remains a candidate/strong inference. It is not proven by the cited fractional-Fick statement for `1<mu<2`.
3. The phrase near the opening that treats `lambda_R''(0)` and boundary conductance as "equivalent" is slightly too strong unless read together with the later caveats. Recommended downstream wording: "boundary conductance is established/strongly supported; `lambda_R''(0)` is expected to share the scaling under an additional current-noise/conductance same-scaling hypothesis."

