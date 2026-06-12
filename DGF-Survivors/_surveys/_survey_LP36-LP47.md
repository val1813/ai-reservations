# DGF Comprehensive Survey: LP36 -- LP47

**Generated:** 2026-06-12
**Scope:** All DGF work across LP36-LP40, LP47

---

## PART I: LP47 -- Causal Ring Information Localization

### 1.1 First-Principles Results (r1, r2, r3, fix)

**System:** n=5 qubit cluster ring, CZ gates. Partition I (A): A={0}, C={k}, B=[n]\{0,k}. Partition II (B): A={0}, B={k}, C={k+1 mod n}

**Clifford Point:** n>=5 QCMI=1 bit (Partition II); n=4 anomalous QCMI=2 bits; Partition I QCMI=0

**No-Go Theorem:** Rz/Rx/T gates give Delta_QCMI=0 identically (theorem, proven by unitary invariance)

**Hmix Results (Partition I):** Non-zero Delta_QCMI with M4 scaling: theta^2*ln(1/theta) + theta^2 + theta^2*ln^2(1/theta). Delta_AICc~21.7. Coefficients: alpha~-0.104, beta~-0.168, gamma~+0.022 (n=5,6,7)

**Protection Horizon (Partition I):** n=5: none; n=6: 2-3/6; n=7: 3-5/7; n=8: 4-7/7. Mechanism: graph automorphism cancellation

**Magic Correlation Length FALSIFIED (Partition I):** k=1 (dist 1 odd): NONZERO; k=2 (dist 2 even): ZERO; k=3 (dist 3 odd): NONZERO. Not length-1, but bipartite parity effect. Under Partition II, length=1 is CONFIRMED.

**QCMI-SRE Correlation:** Pearson r=0.9977. Delta_QCMI approx 0.015 x SRE_4

**Independent Audit (W1/W2) CRITICAL:** Dr A Hmix results FALSIFIED. Found QCMI=0 identically (analytical identity: reduces to mutual info). Dr A alpha~0.244 off by 14 orders of magnitude. Suggests Dr A computed wrong quantity.

**Partition Resolution:** Dual-track both partitions. Agreement only 43-88%. Universal protection: NONE for n=6,7,8

**CONFIRMED:** Clifford point QCMI; No-go theorem; Protection horizon n>=6; ln^2 significance; QCMI-SRE correlation
**FALSIFIED:** Magic correlation length=1 (Partition I); Global T-gate claim; Dr A Hmix results (factor 10^14 off); Cycle space necessity

---

## PART II: LP38 -- QCMI Precision / Alpha Origin

### 2.1 CCQ Theorem Falsification
- CCQ predicted alpha=4.0; measured alpha~1.81 (>20 sigma)
- Alignment axis: QCMI/sum|c|^2 -> INFINITY (not ->0)

### 2.2 Eta_0 Final
- eta_0=1/(8ln2)~0.180 asymptotically optimal (cannot be exactly achieved)
- Evidence: Zhou Gang 2026 Thm 5.3 + CCQ experiment

### 2.3 IBM Q Hardware
| Experiment | S/N | Status |
|:-----------|:---:|:-------|
| Binary contrast | 29 sigma | Robust |
| Mixed-axis pi/4 | 58 sigma | Robust |
| Mixed-axis pi/8 | 20 sigma | Robust |
| Mixed-axis pi/16 | 5.4 sigma | Marginal |
| Ratio method | 52 sigma | Robust |
- All S/N depend on rho~0.97 (unmeasured)
- pi/32: S/N=1.4, NOT feasible
- Excluding alpha=4.0 at >50 sigma via ratio method

### 2.4 Withdrawn Claims
- f_CJ=0.54-0.72 -> Cartan ratio constant 0.3125
- QCMI saturates at b_1>3 -> contaminated scan
- pi/32 measurable -> S/N=1.4
- g(G)>0.5 -> g in [0.33,0.80]

---

## PART III: LP37 -- DGF Cosmic Topology

### 3.1 CFOL Theorem
- QCMI=0 iff Cartan alignment + (Theta=n*pi or gamma=1/2)
- F1-F4 corrections: sigma_k x sigma_k commute (Abelian)
- PASS+WARNING: correct for d=2 SU(2); [C-GAP-1] compactness unverified

### 3.2 HJPW-CFOL: Forward PROVEN; Reverse FAILED
- R3 section 1.7 fatal sign error (sigma_x eigenvalues)
- Five-way equivalence claim FALSE

### 3.3 w(z) vs DESI DR2
- DGF w_a>0; DESI w_a<0 (~4.2 sigma, ~2 sigma after corrections)
- w_b1(z) = 1/3 - 2q_EA(z)/3 is ANSATZ, not derived
- Position: in tension, awaiting DESI DR3

---

## PART IV: LP36 -- W-Causal Accumulation

**CCQ Theorem Falsification** was the decisive moment that shaped ALL subsequent DGF work.

**Eta_0 Tightness Final:** 1/(8ln2)~0.180 is asymptotically optimal. Wall 1 closed (impossible to improve). Walls 2-3 refined.

---

## PART V: LP39 -- DGF Physical Interface

**Core Contradiction:** q_inf=1/2 (Dr A, DGF v3 self-consistent) vs q_inf~1 (Dr B, needed for cosmology)

**Killed Claims (5):** Hubble explanation; rho_vac formula; Landauer analogy; void q->1; dG/dt/G~10^{-10}/yr

**Survivor:** b_1 -> S_BH area law (strongest cosmological connection)
**New Direction:** Asymmetric entropy functional (kappa != 1)
**FP Sign Problem:** Need +3H(1-<q>) source term for expansion cells

---

## PART VI: LP40 -- DGF RG Flow

**LP40-A Numerical:** ds attractor~2.5-2.8 OVERSTATED. b_1 IR-relevant UNCERTAIN. Sign bug fixed (gamma<0 now, favorable but p>0.46). No statistically significant conclusion.

**LP40-B Theoretical:** Log nonlinearity core obstacle. Graph coarse-graining correct start. Scale chasm cannot close perturbatively.

**Honest Closeout:** Code framework reusable. Single-seed results UNRELIABLE. Needs 10+ seeds, N>=100000.

---

## PART VII: Cross-LP Synthesis

**Confirmed Constants:** eta_0~0.180 (STRICT); alpha~1.81->2 (NUMERICAL); CFOL d=2 (THEOREM*); b_1 scaling~0.80 (VERIFIED*); Protection horizon (NUMERICAL)

**Validated Predictions:** Binary contrast (29 sigma); Mixed-axis (20-58 sigma); Ratio method (52 sigma)

**Walls:** W1 IMPOSSIBLE, W2 PARTIAL, W3 IMPOSSIBLE, W4 SOLVED, W5 SOLVED, W7 PARTIAL, W9 SOLVED

**Great Partition Controversy:** Dr A and Dr B computed DIFFERENT QCMI throughout R1-R3. OLD convention gave mutual info for k=1 -> illusion of correlation length=1. Resolution: dual-track partitions.

**Independent Audit Crisis:** Dr A Hmix results falsified (factor 10^14). Partition I results NOT independently verified. URGENT: full verification before publication.

**Cosmology Status:** q_inf=1/2 self-consistent but Hubble UNEXPLAINABLE. Asymmetric entropy only path. DESI DR2 conflict real (~2 sigma). RG barely started. b_1->S_BH strongest survivor. Recommend focus on core theory, defer cosmology.

---

*End of survey. Covers all DGF work LP36-LP47 as of 2026-06-12.*