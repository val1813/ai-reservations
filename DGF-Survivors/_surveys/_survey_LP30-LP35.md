# DGF Structured Result Catalog: LP30--LP47

**Survey date:** 2026-06-12

---

## 1. THEOREM STATEMENTS

### 1.1 Strictly Proved

#### T1: CFOL Necessity Theorem
iff (2026-06-09): QCMI=0 iff c_j in (pi/2)Z for all j (p in (0,1)).
83521-point grid scan: zero counterexamples.
Status: PROVED (INSPECTOR final audit PASS).

#### T2: Reflux Bound Theorem
P_reflux <= N_S*q_S/(N_E*q_E). Quantum proof via Holevo bounds (2026-06-09).
59.1% violate per-node monotonicity. Global bound: zero violations.
Status: PROVED.

#### T3: Black Hole Entropy Area Law [LP32-S4]
S <= N_partial-Omega prop. to A. S_DGF/S_BH = 2.68 (a=l_P) or 1.00 (a=1.64 l_P).
Status: PROVED (scaling). Coefficient depends on CONJ-4.

#### T4a: Cencov-Petz Connection [LP33-EPP]
Info metrics are Riemannian under CPTP monotonicity.
Reviewer: genuine non-obvious insight.
Status: PROVED.

#### T5: AG Thermal Activation Falsified [LP35]
N_coop cancels. Arrhenius/AG/RFOT all excluded.
Status: PROVED (within DGF model C[G]).

#### T6a: q_eq Upper Bound Theorem [LP39]
q_eq in [1/e, 1-1/e] for all kappa>0.
Entropy-only. Status: PROVED.

### 1.2 Conjectures
C1: Lorentzian emergence needs extra symmetry breaking (21 lit, zero exceptions)
C2: Physical q_eq approximated by pure entropy bound (E(q) may deviate)
CONJ-4: Causal locking saturation (determines T3 coefficient)
CONJ-5: SFR-q coupling applicability (H10 crack)

### 1.3 Falsified
F1: DGF-N4 mass bound [LP30] - q_inv not physically observable
F2: Attractor theorem [LP30] - all 3 case proofs structurally irreparable
F3: DGF produces time direction [LP33] - eta independent of J coupling
F4: All constructive signature emergence [LP33] - circular definitions
F5: CCQ theorem [LP38] - alpha=4.0 excluded at >200 sigma
N1: Lambda = archival rate [LP39] - Gamma~10^{-122} is calibration, not derivation
N2: Hubble tension [LP39] - q_eq <= 0.632 bound + FP catastrophe, double fatal
N3: q->0 in known objects [LP39] - neutron star f_occ 59 OOM short

## 2. DERIVATION STATUS

Derived: Theta=pi*A, one time direction, q field eq, FP drift, GUP-Lindblad
Calibrated: G=(pi*q_inf/8)*(c^3*l^2/hbar), l>=sqrt(8/pi)*l_P
Not derived: xi(q), SFR-q (Wall #8 H6/H10)

QCMI-specific derivations:
- Single-edge FR coefficient: 2/ln2 ~ 2.885 bit/rad^2 (VERIFIED F_2=1 to 1e-7)
- Ring effective eta_0 = 1/(8*ln2) ~ 0.180 bit/rad^2 (correction factor 1/16)
- QCMI(theta) analytic, R^2=0.999878
- alpha_eff=1.81, asymptotic alpha=2. >200sigma excludes CCQ alpha=4
- CJ bridge: Cartan sum ratio = 5/16
- Non-aligned CFOL forward direction: PROVED (Fawzi-Renner universal bound)

## 3. NUMERICAL RESULTS

CFOL: 83521 pts, 81 zero-QCMI at c_j in (pi/2)Z. Zero counterexamples.
b1 scaling (c=0.5 p=0.5): b1=1:1.408, 2:2.594, 3:3.677, 4:4.712, 5:5.723,
6:6.724, 7:7.719, 8:8.712 bits. Asymptotic delta ~0.99 bits/ring.
p-scan: Linear for ALL p in (0,1). R^2>0.999. p=0.5 max. p<->1-p sym 2.66e-15.
Topology: edge-disjoint alpha=1.0, vertex-sharing alpha=0.88->1.0, edge-sharing alpha~0.78.
Mixed Cartan (b1=5, 52 configs): QCMI=(1.22+/-0.006)*n_nc, R^2=0.9861.
eta_0 gap: max ratio 7.88x at c=0.536 rad. Range 1.1-7.9x.
Small-c: QCMI/c^2 diverges logarithmically. D2 formula ~3.5x low on coefficient.
Wall #7: 59.1% violate per-node monotonicity. X-axis gates: 0% (CFOL).
Global reflux bound: zero violations in all 2337 configs.
QCMI->decay: D_Q0=0.7081 const, D_Qint=0.9148 const, D_global=1-[cos^2(4c)]^{b1}.
Classicality: c=0.5 gives b1_crit=3, QCMI_crit=3.43 bits.
Pointer basis: min 3.022310 at Cartan axis. R^2=0.999878 for sin^2 fit.
sin^2 high-res (19 steps, 0-90 deg): R^2=0.99999997. No azimuthal dependence.
Theta^2 error bounds: pi/256 error=0.043%, pi/8 error=7.849%.

## 4. EXPERIMENTAL RESULTS (IBM Kingston Heron r2)

v3 Z-basis (100k shots): pi/4 S/N~285, pi/8 S/N~617, pi/16 S/N~198
v4 Z+X dual (50k shots): pi/4 S/N~284, pi/8 S/N~194, pi/16 S/N~670
Enhancement over simulation: 15-62x. All S/N > 190.
Error budget: raw 0.038 bits, mitigated 0.0026 bits (H-wrapper).
Differential noise floor: 0.016 bits (rho ~ 0.97).
Differential witness S/N: pi/4 58-sigma, pi/8 20-sigma, pi/16 5.4-sigma, pi/32 1.4-sigma (no)
Binary contrast: 0.435 bits, S/N ~ 29-sigma
Ratio method: R(LP38)=0.48 vs CCQ=0.0625, S/N ~ 52-sigma
CCQ theta^4 excluded at >50-sigma without small-theta measurements.

## 5. GRAVITATIONAL WAVE PREDICTIONS

2PN binding energy: Newton EXACT, 1PN 0.03% dev, 2PN 4.06% dev.
GW170817 BNS: 1.7 rad (not detectable). ET BNS: 38 rad (>100 sigma; Fisher >300 sigma).
LISA EMRI: ~4000 rad. Ringdown delta_f=0.31% (not detectable 3G).
ppE: b=4, beta~0.07. PPN gamma=1.000000, PPN beta=-7e-6.

## 6. COSMOLOGICAL PREDICTIONS

DESI w(z): chi^2_DGF=1.8 vs chi^2_LCDM=17.3 (CPL proj, not full MCMC).
w0~-0.80, wa~-0.51. q0=0.315 (Omega_DE=1-q).
M87 shadow: DGF excluded at -9.05 sigma. DGF~GR at EHT scales (automatic).
Archive-drift cosmology: All honestly negated.

## 7. RG FLOW (Wall #3, ~55% penetrated)

ln q additive under RG => q=exp(-Phi/c^2) DERIVED from first principles.
G_eff=G/q_avg from causal graph conductivity (derived, not assumed).
alpha~1 universal across 1D/2D/3D. Stable under RG flow.
G_eff/G=1.65 at Schwarzschild radius. S_DGF=q*S_BH (q~0.607 at horizon).
BBN constraint: q(t_BBN) > 0.91.
LP40: R^2<0.3, p=0.46-0.83. Archived (statistically insignificant).

## 8. WALL STATUS

Broken (10 as of 2026-06-10):
CFOL, b1>1, pointer basis, T2 monotonicity, QCMI->decay,
high-D interference, decoherence amplifier, mu(c,p) analytic,
Gamma_0=gamma_E, collective Clifford protection.

Remaining:
RG flow (P1 55%), d>2 (P3), EPP No-Go (P3),
H6/H10 cracks (P2), W7 compiler attack (P0),
T1 time flow (P1), T4 two-time (P1).

## 9. KEY CONSTANTS
eta_0 = 1/(8*ln2) ~ 0.180 bit/rad^2
Single-edge FR = 2/ln2 ~ 2.885 bit/rad^2
alpha_eff = 1.81 +/- 0.02 (finite theta, theta~0.005-0.01)
alpha_b1 ~ 1.0 (all p in (0,1))
Cartan sum ratio = 5/16 = 0.3125
m_max ~ 17 micro-g (conditional)
Gram entropy limit ~ 0.965 +/- 0.005 bits/qubit
rho >= 0.80 (best est. 0.96)
Diff noise floor ~ 0.016 bits

## 10. CODE ASSETS (Key)

b1_scaling.py - b1 scaling + Gram matrix
cfol_scan2.py - CFOL 83521-pt grid scan
petz_recovery_v2.py - Petz recovery fidelity (F_2=1 to 1e-7)
wall5_attack.py - Pointer basis S^2 scan
wall7_attack_v2.py - T2 monotonicity (2337 configs)
wall9_attack_v2.py - QCMI->decoherence mapping
dgf_gw_fisher.py - GW Fisher matrix
dgf_cosmology.py - Cosmology G_eff=G/q
dgf_2pn_predictions.py - 2PN binding energy
rg_flow_v2.py - RG flow round 2
cfol_nonaligned_check.py - Non-aligned CFOL
eta0_fundamental.py - eta_0 derivation
gram_spectrum_2d.py - 2D Gram spectrum
high_d_interference.py - High-D interference
cat2_task5_precision_small_c.py - Small-c log div
(50+ scripts total in DGF-Survivors)

---
*End of catalog. Generated 2026-06-12.*
*File: _survey_LP30-LP35.md*
