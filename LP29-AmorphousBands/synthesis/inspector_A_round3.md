# INSPECTOR Report - A Round 3

Input: `D:\Claude\ai-reservations\LP29-AmorphousBands\current\A\round3.json`

Output: `D:\Claude\ai-reservations\LP29-AmorphousBands\synthesis\inspector_A_round3.md`

## 0. Mechanical Check

`validation/` directory does not exist under `D:\Claude\ai-reservations\LP29-AmorphousBands`; `validate.py` and `quantum.py` are unavailable. This report therefore performs manual Q1-Q5 plus Q6.3-Q6.5 checks.

No B Round 3 output was used. The file's scope guard says `read_B_round3=false`, and the allowed inputs are A Round 2, `inspector_A_round2.md`, `PI_round2.md`, and the project knowledge base.

## Q1. Dimensional Check

Pass.

- `mu_D = mu_H/r_H`: same mobility unit as `mu_H`; `r_H` is dimensionless.
- `n_true = r_H*n_H` and `n_m3 = n_H_cm3*1e6*r_H`: density unit is `m^-3`.
- `k_F = (3*pi**2*n_m3)**(1/3)`: unit `m^-1`.
- `tau = mu_H_cm2_Vs*1e-4*m_star/(e*r_H)`: `m^2/(V*s) * kg / C = s`.
- `v_F = hbar*k_F/m_star`: unit `m/s`.
- `l = v_F*tau`: unit `m`.
- `kF_l = k_F*l`: dimensionless.
- `E_F_eV = hbar**2*k_F**2/(2*m_star*e)`: eV numeric conversion.
- `tau_HWHM = hbar/(2*DeltaE_HWHM_J)` and `tau_FWHM = hbar/DeltaE_FWHM_J`: both have unit `s`.

No exponential, trigonometric, logarithmic, or hyperbolic function with dimensional argument appears in the inspected formulas.

## Q2. Direction / Sign Check

Pass. The Round 2 Hall-factor direction blocker is repaired.

Round 3 uses the convention:

```text
mu_H = r_H*mu_D
n_H = n_true/r_H
```

Therefore the executable conversions are:

```text
mu_D = mu_H/r_H
n_true = r_H*n_H
n_m3 = n_H_cm3*1e6*r_H
```

This is the correct repair of the Round 2 wrong executable formula `n_m3 = n_H_cm3*1e6/r_H`.

At fixed reported `mu_H`, `n_H`, and `m*`, the scaling is also directionally correct:

```text
k_F ~ r_H^(1/3)
tau ~ r_H^(-1)
v_F ~ r_H^(1/3)
l ~ r_H^(-2/3)
k_F*l ~ r_H^(-1/3)
E_F ~ r_H^(2/3)
```

The physical direction is consistent: increasing `r_H` increases the inferred true density and `k_F`, but decreases the inferred Drude mobility and `tau`; the net `k_F*l` decreases weakly as `r_H^(-1/3)`.

## Q3. Circular-Argument Check

Pass with warning.

Round 3 explicitly demotes the circular test:

```text
Do not regress mu_H on kF_l when kF_l was computed from the same mu_H.
```

It replaces the A1 targets with non-circular or less-circular observables:

- independently reported `l_reported_nm`, if not recomputed from the same `mu_H`;
- `TCR_or_activation_flag`;
- optical or THz Drude/Drude-Smith `tau`;
- residual class after predeclared matching on `n_true` or `E_F-E_c`.

This removes the main Round 2 circularity risk: using `kF_l(mu_H)` as if it were an independent predictor of the same `mu_H`.

Remaining warning: `kF_l` is still computed from Hall mobility in the A1 sensitivity table, so it can only be a boundary diagnostic or matching covariate unless paired with an independent target. If all available targets are derived from the same Hall mobility, A1 must remain `non-decisive`, as Round 3 states.

## Q4. Order-of-Magnitude Check

Pass.

Manual recomputation of the Round 3 example table used:

```text
n_H = 1e20 cm^-3
mu_H = 10 cm^2/(V*s)
m* = 0.2 m0
n_true = r_H*n_H
mu_D = mu_H/r_H
k_F = (3*pi^2*n_true)^1/3
tau = mu_D*m*/e
l = (hbar*k_F/m*)*tau
E_F = hbar^2*k_F^2/(2*m*)
```

Recomputed values:

| r_H | n_true (cm^-3) | mu_D (cm^2/Vs) | k_F (nm^-1) | tau (fs) | l (nm) | kF_l | E_F (eV) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.5 | 5.0e19 | 20 | 1.140 | 2.274 | 1.500 | 1.710 | 0.247 |
| 1.0 | 1.0e20 | 10 | 1.436 | 1.137 | 0.945 | 1.357 | 0.393 |
| 2.0 | 2.0e20 | 5 | 1.809 | 0.569 | 0.595 | 1.077 | 0.624 |

These match the Round 3 table to the stated precision. The table is internally consistent with the corrected `r_H` direction.

## Q5. Algebra / Numeric-Source Check

Pass with source/execution warnings.

Algebra:

- `n_m3 = n_H_cm3*1e6*r_H` is now consistent with `n_H = n_true/r_H`.
- `tau = mu_H_cm2_Vs*1e-4*m_star/(e*r_H)` is consistent with `mu_D = mu_H/r_H`.
- `kF_l = k_F*(hbar*k_F/m_star)*tau` gives `kF_l ~ r_H^(2/3)*r_H^(-1) = r_H^(-1/3)`.
- `E_F ~ k_F^2 ~ r_H^(2/3)`.

Numeric-source level:

- Furubayashi et al. 2019 is named as the A1 data source with specific targets: Table 1, Fig. 4, Fig. 7/text, and temperature-dependent transport where available.
- Sahoo/Au/Pan 2024 is used as a THz Drude-Smith method precedent, not as a directly extracted A1 table.
- Jankousky et al. is used for spectral/linewidth convention awareness. Round 3 correctly requires the plotted width convention to be recorded before converting linewidth to `tau`.

Warning: the report still does not contain extracted primary numerical data from the cited papers. It is a corrected measurement protocol plus sensitivity table, not yet an executed literature table.

## Q6.3 Claim-Shrinkage Check

Pass.

Round 3 narrows A1 in a scientifically acceptable way:

- A1 is no longer treated as decisive evidence against structure-network explanations.
- Structural proxies are explicitly marked weak compared with direct In-s/O-O/coordination graph metrics.
- A1 can survive weakly, lose weakly, or remain ambiguous depending on independent targets.

This is not improper shrinkage; it is a repair of the prior circularity and proxy-strength warnings.

## Q6.4 Alternative-Explanation Check

Pass with warning.

Round 3 preserves the competing explanation: structure/network variables may explain transport or spectral observables independently of mobility-edge/Ioffe-Regel labels. It also states that A1 cannot decide this strongly because thickness/XRR density/roughness are only proxies.

Warning: Round 3 does not itself execute a residual test against a concrete alternative model. It only specifies the residual-class protocol. This is acceptable for a round whose purpose was formula repair, but the next executable artifact must instantiate the comparison.

## Q6.5 Landing Check

Pass with warning.

The previous Round 2 blocker was a formula-direction defect rather than a missing landing artifact. Round 3 repairs that formula and gives a corrected CSV schema/protocol:

- corrected `r_H` sweep columns;
- non-circular target columns;
- explicit rule that A1 is `non-decisive` if only Hall-derived targets exist;
- linewidth convention column: `FWHM`, `HWHM`, `self_energy_ImSigma`, or `unknown`.

Remaining landing warning: A1 remains weak because it uses structural proxies and still awaits digitized/extracted source values. A2 or a same-sample optical/spectral table remains necessary for a stronger test.

## Focused Checks Requested By PI

### Hall Factor Correction

Correct. The repaired relation is:

```text
mu_H = r_H*mu_D
n_H = n_true/r_H
mu_D = mu_H/r_H
n_true = r_H*n_H
n_m3 = n_H_cm3*1e6*r_H
```

No remaining Hall-factor direction blocker found.

### r_H Scaling And Example Table

Correct. The stated scaling and the example values are numerically consistent:

```text
k_F ~ r_H^(1/3)
tau ~ r_H^(-1)
l ~ r_H^(-2/3)
k_F*l ~ r_H^(-1/3)
E_F ~ r_H^(2/3)
```

The example table values for `r_H = 0.5, 1, 2` match independent recalculation.

### Circularity: kF_l(mu_H) Predicting mu_H

Substantively fixed. Round 3 forbids regressing `mu_H` on `kF_l` computed from the same `mu_H` and redirects A1 to independent `l_reported`, TCR/activation class, optical/THz `tau`, or residual class.

Warning: this fix must be enforced during execution. If a future CSV only contains Hall-derived `kF_l` and Hall-derived targets, it remains diagnostic only and cannot be counted as independent evidence.

### Linewidth HWHM/FWHM Convention

Direction is correct.

Round 3 states:

```text
tau = hbar/(2*DeltaE)
```

is valid when `DeltaE` is HWHM or a self-energy broadening parameter where the full peak width is `2*DeltaE`. If the extracted width is FWHM, the correct conversion is:

```text
tau = hbar/DeltaE_FWHM
```

This direction is correct: substituting a FWHM value into `hbar/(2*DeltaE)` would underestimate `tau` by a factor of 2.

## Integrated Verdict

INSPECTOR does not block A Round 3. The Round 2 Hall-factor density-conversion blocker is fixed, the `r_H` sensitivity table is numerically correct, the main `kF_l(mu_H) -> mu_H` circularity is explicitly removed from the protocol, and the linewidth HWHM/FWHM direction is correct.

Warnings remain about execution strength, not formula validity.

--- Feed To Next Round ---

BLOCKING - must fix:

None.

WARNINGS - should fix:

1. Enforce the non-circular A1 rule during execution: do not count Hall-derived `kF_l` as an independent predictor of the same Hall mobility.
2. A1 remains a weak landing because thickness/XRR density/roughness are structural proxies, not direct In-s/O-O/coordination graph metrics.
3. Extract or digitize actual Furubayashi/Jankousky/optical-THz values before treating the protocol as an executed evidence table.
4. Every linewidth row must record `FWHM`, `HWHM`, `self_energy_ImSigma`, or `unknown`; `unknown` rows cannot support decisive tau classification.
5. If no independent target exists (`l_reported`, TCR/activation, optical/THz `tau`, linewidth/IPR, or residual class), mark A1 `non-decisive`.

---
