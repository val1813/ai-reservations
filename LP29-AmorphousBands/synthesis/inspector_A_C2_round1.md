# INSPECTOR Report: A C2 Round 1

Input: `D:\Claude\ai-reservations\LP29-AmorphousBands\current\A\C2_round1.json`

Scope: only derivation/protocol consistency for A's LP29-C2 Round 1. This report does not judge topic value.

## Mechanical Check

- `validation/validate.py`: not found under `D:\Claude\ai-reservations\LP29-AmorphousBands`; Q1-Q5 were checked manually.
- `quantum.py`: not applicable / not found.

## Verdict

INSPECTOR result: pass with warnings.

- Blockers: 0
- Warnings: 5

No fatal dimensional, sign, algebraic-limit, or order-of-magnitude error was found in the formulas as written. The main risks are claim strength and landing depth: A correctly marks the result as protocol-level, but the output still lacks exact Srivastava normalization, same-sample rows, and quantitative exclusion of alternative explanations.

## Q1 Dimensional Check

### F1 `exp(-d_ij/rho_ij)`

- `d_ij`: length.
- `rho_ij`: length.
- `d_ij/rho_ij`: dimensionless.
- `exp()` argument: dimensionless.
- Result: dimensionless.
- Status: pass.

Numerical spot check: with `d_ij=3.0`, `rho_ij=1.0`, `exp(-3)=0.0498`, matching the stated expected range `[0.04, 0.06]`.

### F2 `Sum(q_i*q_j*exp(-d_ij/rho_ij), (i,j))/N_pair`

- `exp(-d_ij/rho_ij)`: dimensionless.
- `N_pair`: count, dimensionless.
- If `q_i`, `q_j` are dimensionless conduction-orbital weights, `O_s` is dimensionless.
- Status: pass, conditional on `q_i/q_j` being declared dimensionless in the next numerical implementation.

### F3 `beta_0 + beta_1*log(1/(O_s + eps)) + beta_2*V_s`

- Intended LHS: `log(m_eff/m0)`, dimensionless.
- `O_s` and `eps`: dimensionless.
- `log(1/(O_s+eps))`: dimensionless.
- `V_s`: eV^2, so `beta_2` must carry eV^-2.
- Status: warning.

Warning 1: coefficient units are incomplete. `beta_2` must be explicitly specified as eV^-2, and any later regression table must store coefficient units. This is not a formula-killing error because regression coefficients can absorb units, but the current JSON only labels variables, not coefficient dimensions.

### F4 `R2(G_k ~ O_s + V_s + n_s + DeltaE_s + size_s)`

- `R2`: dimensionless.
- Regressors have mixed physical units, but regression coefficients absorb them.
- Status: pass.

### F5 `r_y_s - (alpha_0 + alpha_1*lambda2_resid_s + alpha_2*rho_resid_s + alpha_3*damage_resid_s)`

- Output has same units as residual label `y` if `alpha` coefficients are fitted in those units.
- `lambda2_resid`, spectral-radius residual, and damage residual are admissible if computed on dimensionless or consistently weighted graphs.
- Status: pass with notation caution.

Warning 2: `rho_resid_s` is used for spectral-radius residual while `rho_ij` is already used for orbital decay length. This is a notation collision risk in later algebra/code. Rename spectral radius to `lambda_max_resid_s` or `spectral_radius_resid_s`.

## Q2 Direction / Sign Check

- F1: as `d_ij -> infinity`, overlap tends to 0; as `d_ij -> 0`, overlap tends to 1. Direction is correct.
- F2: normalization by `N_pair` prevents trivial growth with pair count; direction is correct for average overlap.
- F3: if `beta_1 > 0`, increasing `O_s` decreases `log(1/(O_s+eps))`, hence decreases predicted log effective mass. This matches the stated "larger overlap -> lower effective mass" direction.
- F4: `R2 -> 1` implies graph metric variance is absorbed by controls; direction is correct.
- F5: `alpha_1, alpha_2, alpha_3 -> 0` implies no independent graph signal; direction is correct.

No direction reversal found.

## Q3 Circular-Argument Check

No hard circularity found. A explicitly requires graph metrics to predict external residual labels after the overlap baseline and controls, and it states that external labels must not be used to construct graph features.

Warning 3: the absorption map is still conceptual. Claims such as weighted degree, cation distance, and coordination being absorbed are plausible because they are monotone summaries of the same pair-overlap structure, but they are not yet verified on same-sample data. Keep them labeled as protocol constraints or hypotheses, not numerical results.

## Q4 Order-of-Magnitude Check

Only one concrete numerical substitution is present:

- `exp(-3.0/1.0)=4.98e-2`, consistent with the stated range.

No 10+ order-of-magnitude mismatch found.

## Q5 Algebra / Limits / Numerical Sources

### Algebra and Limits

- Exponential overlap limits are correct.
- Pair-sum normalization has the intended finite-size behavior.
- Effective-mass baseline has correct monotonicity under the declared `beta_1 > 0`.
- Residual test algebra is acceptable as a model specification, though the JSON's F5 expression is the residual error, not the prediction equation itself. This is not fatal because the description clarifies that graph features are added to the overlap-controlled residual.

### Numerical Sources

Warning 4: numerical-source depth is insufficient for reproduction. A states that the exact Srivastava normalization/full SI was not downloaded and that the result is not yet a numerical defeat or survival of graph metrics. This is a correct limitation, but it must remain binding: no later derivation should treat this round as having reproduced the orbital-overlap metric.

Source-level classification:

- Srivastava 2019: DOI-level / metadata-plus-abstract baseline, full constants missing.
- Jankousky 2026: DOI-level external label candidate, structures/SI not obtained.
- Furubayashi 2019: PDF reportedly downloaded, but no extracted numeric table is used in this JSON.

## Q6.3 Claim Shrinkage

No same-subtopic prior C2 A round was found for comparison; this is C2 Round 1. Therefore no formal shrinkage penalty is triggered.

Relative to the C2 Polaris statement, A narrows the claim into a baseline-first protocol and explicitly says there is no numerical defeat/survival claim yet. Because this is Round 1 and the output is explicit about protocol-level status, this is not counted as shrinkage.

## Q6.4 Alternative Explanation

A does address simpler alternatives:

- conventional amorphous semiconductor mobility physics;
- defect/trap/band-tail variables;
- overlap, density, onsite variance, and mobility-edge controls absorbing graph signals.

Status: pass with warning.

Warning 5: alternatives are identified but not quantitatively excluded. This is acceptable for a protocol-level Round 1, but the next round must not claim independent graph survival unless a same-sample residual test beats these alternatives with held-out validation or a declared equivalent.

## Q6.5 Landing Calculation

Landing status: weak but present.

A provides a half-product blueprint:

- residual formula: `r_y_s = y_s - f_y(O_s,V_s,n_s,DeltaE_s,batch_s,size_s)`;
- acceptance condition: graph residual features must improve cross-validated prediction with stable signed coefficients;
- required data/code list: full Srivastava SI, Jankousky structures/labels, Furubayashi transport rows, NetworkX/scipy pipeline, residual-model script.

This avoids the Q6.5 blocking case because the blank is paired with a concrete half-product plan. However, it is not a concrete numeric landing calculation. It should be marked as half-product only until at least one real same-sample row or reproducible synthetic benchmark table is computed.

## Blocking Issues

None.

## Warnings

1. Coefficient units incomplete in F3: `beta_2` must be eV^-2 if `V_s` is eV^2.
2. Notation collision: `rho_resid_s` for spectral radius conflicts with `rho_ij` decay length.
3. Absorption map is conceptual, not yet same-sample numerical evidence.
4. Srivastava normalization/SI and same-sample numerical constants are missing; reproduction not established.
5. Alternative explanations are named but not quantitatively excluded; landing remains half-product.

## Feed To Next Round

--- 投喂下一轮 ---

必须修正（阻断级）:

None.

建议修正（警告级）:

1. Specify regression coefficient units, especially `beta_2` as eV^-2 for `V_s` in eV^2.
2. Rename spectral-radius residual from `rho_resid_s` to avoid collision with orbital decay length `rho_ij`.
3. Keep graph-metric absorption claims labeled as protocol/hypothesis until same-sample residual tests are run.
4. Extract exact Srivastava overlap normalization/full SI before any numerical reproduction claim.
5. Turn the Q6.5 half-product blueprint into at least one concrete row: `O_s`, controls, one graph residual feature, one external label/residual, and a reproducible calculation path.

---
