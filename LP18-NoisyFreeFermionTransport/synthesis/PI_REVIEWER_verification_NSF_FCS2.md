# PI Reviewer Verification: NSF-FCS-2

## Reviewer Trigger Check

Reviewer file: `synthesis/REVIEWER_NSF_FCS2_final.md`

Final recommendation: major revision.

The reviewer did not report citation fabrication and did not report an exact prior-art conflict. Therefore the SOP hard trigger for PI independent WebSearch verification is not activated.

## Reviewer Constraints To Carry Forward

1. The FDT anchor `lambda_T''(0)=2G_T` must specify the exact FCS normalization: counting field, time unit, conductance unit, and convention-dependent factor 2.
2. `R2 ~ delta^2` must be established directly on `R2` across multiple smaller `delta` values before `Qhat=R2/(delta^2 G_T)` is used as the primary scaling observable.
3. Reverse-bias checks must be repeated off center, not only at `rho_bar=0.5`.
4. `Qhat ~ L^{1/2}` remains a small-L ansatz. It must be tested against constant-plus-correction, logarithmic drift, and crossover fits.
5. `reversible_side` and `nonLDB_site_skew` activity controls must remain split; reversible activity preserving LDB is only a sanity control.

## PI Action

Proceed to GATE 6/7 because no citation-fabrication or exact prior-art-conflict trigger was raised. Carry all five reviewer constraints into NSF-FCS-2 Round 2.
