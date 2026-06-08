# PI NSF-FCS-2 Round 2 Qhat Model Comparison

## Purpose

Reviewer attack 4 warned that `Qhat~L^{1/2}` is a small-L ansatz and may be a drift/crossover artifact. This file compares simple fits on available windows.

## Data

`Qhat=R2/(delta^2 G_T)`.

Datasets:

- centered `0.40 -> 0.60`, `L=4..8`
- off-center low `0.30 -> 0.50`, `L=4..7`
- off-center high `0.55 -> 0.75`, `L=4..7`

Models compared by AIC on `Qhat(L)`:

- power: `Qhat=a L^p`
- log drift: `Qhat=a+b log L`
- constant
- constant plus inverse-size correction: `Qhat=q+a/L`

## Result

For every tested dataset and alpha, the log-drift fit has the best AIC. Example centered `0.40 -> 0.60`, `L=4..8`:

| alpha | best model | log AIC | const+1/L AIC | power AIC | const AIC |
|---:|---|---:|---:|---:|---:|
| 0.5 | log | -70.146 | -67.220 | -62.596 | -40.781 |
| 1.0 | log | -63.172 | -55.975 | -53.565 | -31.144 |
| 1.5 | log | -60.497 | -50.279 | -49.240 | -26.338 |

The same ordering appears in both off-center datasets.

## Verdict

Reviewer attack 4 is valid: current data do not justify asymptotic `Qhat~L^{1/2}` language. The observed `0.47..0.56` local slopes should be described as finite-window effective exponents. At this stage, log drift is the best simple empirical fit.

Round 2 should downgrade the claim:

> `Qhat` grows systematically with `L` over accessible sizes and is robust across centered/off-center densities, but the functional form is unresolved.

not:

> `Qhat~L^{1/2}`.
