# PI NSF-FCS-2 Round 1 Synthesis

## Inputs

- A: `current/A/NSF-FCS-2_round1.md`
- B: `current/B/NSF-FCS-2_round1.md`
- Inspector A: `synthesis/inspector_NSF_FCS2_A_round1.md`
- Inspector B: `synthesis/inspector_NSF_FCS2_B_round1.md`
- Inspector B recheck: `synthesis/inspector_NSF_FCS2_B_round1_recheck.md`
- PI numeric check: `Qhat=R2/(delta^2 G_T)` from the three centered-bias NESS ledgers.

## Inspector Status

- A: `WARNING`, not blocked. The claims `R2 ~ delta^2 G_T Q_L`, `Q_L ~ L^{1/2}`, and `3/2-alpha` must remain explicitly marked as ansatz / candidate explanation.
- B: initially `BLOCKED` on units and activity/LDB design; revised and rechecked as `PASS`.

## A-Side Result

A establishes the first clean theoretical filter:

`R2(L,delta)=c2(L) delta^2 + c4(L) delta^4 + ...`

This is not unconditional. It requires:

- finite `L` analyticity near `delta=0`;
- equilibrium FDT at `delta=0`;
- left-right reflection symmetry;
- the two-terminal observable being reflection-even at second cumulant level;
- local detailed balance for the equilibrium reference.

This matches the reverse-bias sanity check: `rho_left/rho_right=0.6/0.4` agrees with `0.4/0.6` to `~1e-8`.

A's useful ansatz is:

`R2(L,delta) ~= delta^2 G_T(L) Q_L(alpha)`

where `Q_L` is a McLennan/frenetic/traffic Green-resolvent correction. This is a candidate mechanism, not a theorem.

## PI Qhat Check

Define:

`Qhat=R2/(delta^2 G_T)=(S_T-2)/delta^2`

Measured slopes:

| rho_left -> rho_right | alpha=0.5 | alpha=1.0 | alpha=1.5 |
|---|---:|---:|---:|
| 0.45 -> 0.55 | 0.469129 | 0.512462 | 0.532147 |
| 0.40 -> 0.60 | 0.469479 | 0.514271 | 0.536279 |
| 0.35 -> 0.65 | 0.470088 | 0.517327 | 0.543307 |

This is stronger than fitting raw `R2`: the normalized residual is almost bias-independent and has a stable `~L^{1/2}` growth window. The next numerical target should be `Qhat`, not raw `R2`.

## B-Side Result

B turns the next round into falsifiers rather than more confirmation:

1. Extend `L` and fit sliding-window slopes for `Qhat`, not only `R2`.
2. Run off-center density pairs to test whether `delta^2` was protected by particle-hole symmetry around `rho_bar=0.5`.
3. Track `J0`, `R2/G_T`, `tau_J=R2/J0^2` with units of time, and `Q_JG=R2*G_T/J0^2` as a dimensionless current-normalized diagnostic.
4. Add two activity controls:
   - `reversible_side`: sanity control, should keep `R2≈0` at `delta=0`.
   - `nonLDB_site_skew`: true kinetic forcing, site-dependent forward/backward reservoir ratio that cannot be absorbed into a single reservoir chemical potential.

The key B correction after INSPECTOR is that pure same-side activity is not kinetic evidence if it preserves LDB; it is an equilibrium sanity check.

## PI Decision

NSF-FCS-2 survives Round 1 with a sharper form:

> Study the normalized NESS residual `Qhat(L,alpha)=R2/(delta^2 G_T)`. Current evidence suggests a robust near-`L^{1/2}` growth window across `alpha=0.5,1.0,1.5`, but this is an ansatz-level observation until larger-L and off-center density falsifiers pass.

## Round 2 Instructions

- A Round 2: derive or falsify `Qhat ~ L^{1/2}` from an equilibrium Poisson/Green object. The target is a concrete quadratic form, not a verbal McLennan explanation.
- B Round 2: implement or specify the smallest script changes for `Qhat`, off-center density ledgers, and `nonLDB_site_skew`. If implementation is too large, produce exact CLI/API design and expected CSV columns.

Hard constraints:

- Do not claim `3/2-alpha` as a theorem.
- Do not use `R2/J0^2` as dimensionless.
- Treat reversible activity as FDT sanity control, not kinetic residual evidence.

## Off-Center Density Falsifier

Additional ledgers:

- `current/plan/nsf_fcs_tier1_ness_offcenter_0p30_0p50_L4_7.csv`
- `current/plan/nsf_fcs_tier1_ness_offcenter_0p55_0p75_L4_7.csv`

Both have 12 rows and all rows are `ROW_VALID`.

For fair comparison use `L=4..7`, `delta=0.2`, and:

`Qhat=R2/(delta^2 G_T)`

| density pair | alpha=0.5 slope | alpha=1.0 slope | alpha=1.5 slope |
|---|---:|---:|---:|
| centered `0.40 -> 0.60` | 0.496859 | 0.542479 | 0.564290 |
| off-center `0.30 -> 0.50` | 0.496877 | 0.542582 | 0.564527 |
| off-center `0.55 -> 0.75` | 0.496907 | 0.542727 | 0.564847 |

The amplitude increases with `rho_bar`, but the `L` exponent is unchanged at this resolution. This falsifies the simplest worry that the observed `Qhat ~ L^{1/2}` window is merely a particle-hole-centered artifact at `rho_bar=0.5`.

Updated PI decision: keep NSF-FCS-2 and promote `Qhat` to the primary numeric observable for Round 2.
