# INSPECTOR Report - A Round 1

Input: `D:\Claude\ai-reservations\LP29-AmorphousBands\current\A\round1.json`

Output: `D:\Claude\ai-reservations\LP29-AmorphousBands\synthesis\inspector_A_round1.md`

## 0. Mechanical Check

`validation/` directory does not exist under `D:\Claude\ai-reservations\LP29-AmorphousBands`; `validate.py` and `quantum.py` are unavailable. This report therefore performs manual Q1-Q5 checks.

## Q1. Dimensional Check

Checked formulas:

- F1 `tau = mu*m_star/e`: `(m^2 V^-1 s^-1)*(kg)/C = s`, since `1 V = kg m^2 s^-3 A^-1` and `C = A s`. Pass.
- F2 `k_F = (3*pi^2*n)^(1/3)`: `(m^-3)^(1/3) = m^-1`. Pass.
- F3 `v_F = hbar*k_F/m_star`: `(kg m^2 s^-1)*(m^-1)/kg = m s^-1`. Pass.
- F4 `l = v_F*tau`: `(m s^-1)*s = m`. Pass.
- F5 `k_F*l`: `m^-1*m = 1`. Pass.
- F6 `E_F = hbar^2*k_F^2/(2*m_star)`: `kg m^2 s^-2 = J`; division by `e` gives eV. Pass.

No exp/sin/log/sinh dimensionless-argument issue appears in this file.

## Q2. Direction / Sign Check

Ioffe-Regel direction is correct:

- `k_F*l ~ 1` is the boundary scale.
- Larger `k_F*l` moves to the more metallic / extended-state side.
- Smaller or sub-unity `k_F*l` moves toward localization / mobility-edge boundary risk.

A's classification is directionally consistent: `k_F*l = 1.36` is near boundary, `2.7-5.4` is above boundary, and `>10` is well metallic. The DeltaE cross-check also correctly makes the lowest-mobility case slightly below/at boundary (`k*l = 0.864`).

No reversed ratio or sign error found.

## Q3. Circular-Argument Check

No direct circular proof is found in the arithmetic: the table computes `tau/k_F/v_F/l/k_F*l` from stated inputs rather than assuming the output.

Warning: the interpretation partly risks circularity at the conceptual level. Hall mobility is used as Drude mobility, and nominal carrier density is used as a free-electron density; these assumptions already encode a band/Drude picture. Therefore the resulting `k_F*l` is a consistency check for A, not an independent proof that mobility-edge/Drude physics is the correct microscopic explanation.

## Q4. Order-of-Magnitude Check

Manual recomputation using:

- `m* = 0.2 m0`
- `mu = 10, 20, 40 cm^2/Vs = 0.001, 0.002, 0.004 m^2/Vs`
- `n = 1e20, 3e20, 1e21 cm^-3 = 1e26, 3e26, 1e27 m^-3`

Results match A's table within rounding:

| n (cm^-3) | mu (cm2/Vs) | tau (fs) | kF (nm^-1) | vF (1e6 m/s) | l (nm) | kF*l | EF (eV) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1e20 | 10 | 1.137 | 1.436 | 0.831 | 0.945 | 1.357 | 0.393 |
| 1e20 | 20 | 2.274 | 1.436 | 0.831 | 1.890 | 2.714 | 0.393 |
| 1e20 | 40 | 4.549 | 1.436 | 0.831 | 3.781 | 5.429 | 0.393 |
| 3e20 | 10 | 1.137 | 2.071 | 1.199 | 1.363 | 2.823 | 0.817 |
| 3e20 | 20 | 2.274 | 2.071 | 1.199 | 2.726 | 5.646 | 0.817 |
| 3e20 | 40 | 4.549 | 2.071 | 1.199 | 5.453 | 11.292 | 0.817 |
| 1e21 | 10 | 1.137 | 3.094 | 1.791 | 2.036 | 6.300 | 1.823 |
| 1e21 | 20 | 2.274 | 3.094 | 1.791 | 4.073 | 12.599 | 1.823 |
| 1e21 | 40 | 4.549 | 3.094 | 1.791 | 8.145 | 25.198 | 1.823 |

DeltaE = 0.25 eV cross-check also matches:

- `k = 1.146 nm^-1`
- `v = 0.663e6 m/s`
- `mu = 10/20/40 cm2/Vs` gives `l = 0.754/1.508/3.016 nm`
- `k*l = 0.864/1.728/3.455`

No >1 order-of-magnitude numerical error found.

## Q5. Algebra / Numeric-Source Check

Algebra is standard Drude + free-electron/parabolic-band algebra and degrades correctly in known limits:

- `mu -> 0` gives `tau -> 0`, `l -> 0`, `k_F*l -> 0`.
- increasing `mu` linearly increases `tau`, `l`, and `k_F*l`.
- increasing `n` increases `k_F ~ n^(1/3)`, `v_F ~ n^(1/3)`, `E_F ~ n^(2/3)`, and `k_F*l ~ n^(2/3)` at fixed `mu,m*`.

Numeric-source warnings:

- `m*=0.2m0` is attributed to project/Jankousky record, but not independently re-extracted here.
- `mu=10-40 cm2/Vs`, `n=1e20-1e21 cm^-3`, and `DeltaE=0.25 eV` are parameter-window inputs; this is acceptable for a Round 1 estimate but should remain marked as assumption-level.
- `reported_l=1-3 nm` is listed but not used as an independent calibration against the Drude-derived `l`; next round should compare measured/claimed mean-free-path extraction methods against the table.

## Q6.3 Claim-Shrinkage Check

Round 1 has no previous A round for strict shrinkage comparison.

Within the file, A explicitly weakens the strong proposition: it says the numeric check supports "A weak version" but not "A strong version", and that local structure/connectivity cannot be excluded near the boundary. This is a scientific narrowing rather than an internal arithmetic error.

Warning for PI matrix scoring: the claim should be scored as a weakened A, not as the original strong A proposition.

## Q6.4 Alternative-Explanation Check

Warning: alternative explanations are acknowledged but not explicitly eliminated.

The file names structural connectivity, O-O/coordination defects, multiband/nonparabolic effects, Hall factor deviations, and effective-mass variation as risks. However, it does not provide a concrete exclusion test showing why these simpler or competing explanations fail on the same observables. Therefore A's result should be treated as a Drude/mobility-edge plausibility check, not as a discriminating proof against B.

Required next-round handling:

- explicitly test Hall factor / optical Drude mobility vs Hall mobility;
- compare density-derived `k_F*l` against independently reported mean free path;
- state whether structural connectivity can explain the same mobility trend without invoking a separate mobility-edge criterion.

## Q6.5 Landing Check

BLOCKER: A identifies a blind spot / unsolved comparison but does not provide a concrete landing A/B/C product for that gap.

The file states that no literature fully resolves LP29's A/B criterion and that a key blind spot is the lack of a same-sample comparison between `k_F*l` boundary and an In-s connectivity graph / structural-threshold dataset. But the output does not give a concrete landing artifact such as:

- a specific existing dataset and exact columns to extract;
- a half-finished table with named samples and values;
- a blueprint with computable graph metric, threshold definition, and target systems;
- a specified experimental dataset where A/B can be tested.

Per Q6.5, this is not merely a warning: the round cannot be used as a complete "no-prior-blank" landing. Next A round must explicitly supply at least one landing item.

## Integrated Verdict

INSPECTOR blocks on landing completeness, not on arithmetic.

Blocking issue:

1. Landing missing: A claims a literature/criterion blind spot around same-sample `k_F*l` vs In-s/structural connectivity threshold, but does not provide a concrete landing A/B/C artifact. The next round must add at least one concrete dataset/table/blueprint.

Warnings:

1. Hall mobility = Drude mobility is a high-leverage assumption. If Hall factor differs strongly from 1, or if multiband/nonparabolic effects are important, `tau`, `l`, and `k_F*l` shift systematically.
2. The free-electron density-derived `k_F` assumes a single isotropic parabolic 3D band. This is a consistency estimate, not an independent microscopic proof.
3. Alternative explanations are acknowledged but not excluded; structural connectivity and defect-threshold explanations remain live.
4. A's strong proposition shrinks to a weaker claim: mobility-edge/Ioffe-Regel is a necessary first diagnostic, but not sufficient to rule out local-structure criteria near the boundary.

--- Feed To Next Round ---

BLOCKING - must fix:

1. Add landing artifact for the stated blind spot: give a concrete same-sample dataset/table/blueprint that connects `k_F*l` or mobility-edge diagnostics to In-s connectivity / O-O / coordination-defect structural metrics. At least one computable landing item is required.

WARNINGS - should fix:

1. Do not treat Hall mobility as automatically equal to Drude mobility. State Hall factor assumptions and, where possible, compare to optical/Drude mobility.
2. Keep `k_F*l` as a plausibility/consistency check unless independent evidence supports single-band parabolic transport.
3. Explicitly test whether structural connectivity or defect-threshold explanations can reproduce the same mobility trends without the A framework.
4. Preserve the narrowed claim: A Round 1 supports only a weak A, not the original strong proposition that structure is merely subordinate.

---
