# NSF-FCS-2T Signed Mixed-Parity Test

**Status:** completed.

## Runs

Generated signed grids:

- `current/plan/nsf_fcs_2T_signed_grid_nonldb_L4_7.csv`
- `current/plan/nsf_fcs_2T_signed_grid_reversible_L4_7.csv`
- `current/plan/nsf_fcs_2T_signed_basis_fit_summary.csv`

Window:

- `L=4..7`
- `alpha=0.5,1.0`
- `rho_bar=0.5`
- `delta=0,+0.02,-0.02,+0.04,-0.04`
- `A=0,+0.05,-0.05,+0.10,-0.10`
- `activity_mode=nonLDB_site_skew,reversible_side`

All rows were valid.

## Fit

At fixed `mode,L,alpha`, fit:

`R2/G_T = c0 + c_delta2 delta^2 + c_A2 A^2 + c_deltaA delta A + c_delta2A2 delta^2 A^2`

## nonLDB_site_skew Result

The signed odd mixed channel is not resolved.

Representative coefficients:

| L | alpha | `c_delta2` | `c_A2` | `c_deltaA` | `c_delta2A2` |
|---:|---:|---:|---:|---:|---:|
| 4 | 0.5 | `0.101643` | `0.00384198` | `-6.84e-8` | `-0.00149256` |
| 5 | 0.5 | `0.115478` | `0.00464630` | `1.17e-8` | `-0.00187150` |
| 6 | 0.5 | `0.125916` | `0.00525625` | `-2.40e-8` | `-0.00236867` |
| 7 | 0.5 | `0.134111` | `0.00573578` | `1.25e-7` | `-0.00275617` |
| 4 | 1.0 | `0.238661` | `0.00875994` | `-1.69e-8` | `0.000934955` |
| 5 | 1.0 | `0.273910` | `0.01054750` | `3.57e-9` | `-0.000641406` |
| 6 | 1.0 | `0.301042` | `0.01191550` | `-1.11e-7` | `-0.00239000` |
| 7 | 1.0 | `0.322690` | `0.01300060` | `-2.84e-8` | `-0.00408385` |

`c_deltaA` is `O(1e-7)` or lower, while `c_A2` is `O(1e-3..1e-2)` and `c_delta2` is `O(1e-1)`. In this signed window, the sign-sensitive mixed channel is numerical-floor relative to the even channels.

Interpretation:

The equal-density `A^2` result is not merely a projection artifact in the tested small signed window. The nonLDB channel remains parity-separated from density bias to current precision.

## reversible_side Result

Reversible traffic remains qualitatively different:

- equal-density residual is floor-scale;
- `c_A2` is floor-scale in signed fit;
- `c_delta2A2` is sizable, about `0.0096..0.0525`;
- simple signed basis has larger residuals, about `5.9e-2..1.37e-1` relative.

Interpretation:

`reversible_side` should not be used as a separability null. It preserves equilibrium FDT but renormalizes NESS curvature in a way not captured cleanly by the minimal basis.

## PI Decision

The signed mixed-parity ambiguity is resolved in favor of the parity-tomography claim:

- nonLDB skew: `delta^2`, `A^2`, and tiny `delta A`;
- reversible traffic: equilibrium sanity plus NESS coefficient renormalization;
- no asymptotic `L` law.

This is now strong enough to enter a conditional REVIEWER gate as a finite-window ledger diagnostic, provided the claim is not promoted to theorem or universality.

## Reviewer-Gate Claim

> In the tested finite-volume long-jump open-exclusion ledger, `R2=lambda_T''-2G_T` acts as a parity-tomography diagnostic: centered density bias contributes an even `delta^2` channel, equal-density nonLDB site skew contributes an even `A^2` channel, the signed mixed `delta A` channel is numerical-floor in the tested window, and reversible LDB traffic preserves equilibrium FDT while renormalizing density-biased NESS coefficients.

## Mandatory Caveats

- finite-window only: `L=4..7`, `alpha=0.5,1.0`;
- ledger convention only: dimensionless Markov-affinity convention;
- not an asymptotic scaling claim;
- not a universal FDT anomaly;
- not a proven analytic theorem;
- standard response/MFT/frenetic-response coverage remains a reviewer risk.
