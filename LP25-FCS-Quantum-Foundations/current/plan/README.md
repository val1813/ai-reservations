# LP25-FCS Quantum Foundations — Data & Code Repository

**Paper:** "Second Scaling Exponent for Off-Diagonal Coherence in Power-Law Hopping Nonequilibrium Steady States"
**Target:** Physical Review D (Letter)
**Date:** 2026-06-05

---

## Repository Structure

```
plan/
├── main.tex                          # Main manuscript (LaTeX)
├── supplemental.tex                  # Supplemental Material (LaTeX)
├── references.bib                    # Bibliography
├── cover_letter.md                   # Cover letter
├── PRL_manuscript_v2.md             # Manuscript source (markdown)
├── PRL_supplementary.md             # SM source (markdown)
│
├── figures/
│   ├── generate_figures.py          # Figure generation script
│   ├── Fig1_beta_alpha.pdf          # Figure 1: β(α) main plot
│   ├── Fig1_beta_alpha.png
│   ├── Fig2_beta_mu.pdf             # Figure 2: β-μ anti-correlation
│   ├── Fig2_beta_mu.png
│   ├── Fig3_firewall_universality.pdf # Figure 3: Universality test
│   └── Fig3_firewall_universality.png
│
├── phase2_L64_compute.py            # COH baseline solver (dense, L≤64)
├── phase2_L_large.py                # COH extended solver (L up to 256)
├── fss_compute.py                   # FSS sparse GMRES solver (L=128,256)
├── firewall_AHA1.py                 # Universality scan solver
├── defense_all_attacks.py           # Cross-validation + Lyapunov checks
├── model_selection.py               # AICc model selection + κ computation
├── finite_size_stability.py         # Leave-one-out stability analysis
├── verify_claims.py                 # Claim verification script
├── verify_kappa.py                  # κ factor verification
├── verify_referee_attacks.py        # Reviewer attack verification
│
├── phase2_raw_results_FULL.json     # Raw |C_mid| data (125 COH points)
├── phase2_fit_results_FULL.json     # β fits with std_err (125 points)
├── phase2_raw_results_FULL.csv      # Same data in CSV
├── phase2_fit_results_FULL.csv      # Same fits in CSV
├── firewall_AHA1_results.json       # Universality test data (60 points)
├── firewall_AHA1_results.csv        
├── firewall_AHA1_beta_values.csv    
├── model_selection_results.json     # AICc/κ/anti-correlation results
├── finite_size_stability_results.json # Stability check results
├── fss_gamma0.1_L128_combined.json  # FSS L=128, γ_φ=0.1
├── fss_gamma0.5_L128.json           # FSS L=128, γ_φ=0.5
├── fss_gamma1.0_L128.json           # FSS L=128, γ_φ=1.0
├── fss_gamma2.0_L128.json           # FSS L=128, γ_φ=2.0
├── fss_gamma0.5_L256.json           # FSS L=256 anchors, γ_φ=0.5
└── fss_gamma0.5_L256_raw.json       # Raw L=256 solver outputs
```

## Data-to-Claim Correspondence

| Manuscript Claim | Data Source | Script |
|:----------------|:------------|:-------|
| Table 1 (β for 25 α,γ_φ) | `phase2_fit_results_FULL.json` | `phase2_L64_compute.py` |
| Table 2 (L=256 FSS flow) | `fss_gamma0.5_L256.json` | `fss_compute.py` |
| Table 3 (Universality test) | `firewall_AHA1_results.json` | `firewall_AHA1.py` |
| Table S1 (AICc model selection) | `model_selection_results.json` | `model_selection.py` |
| Table S3 (κ correction factor) | `model_selection_results.json` | `model_selection.py` |
| Table S4 (Full β table with raw errors) | `phase2_fit_results_FULL.json` | `phase2_L64_compute.py` |
| Table S5 (dβ/dμ slopes) | `model_selection_results.json` | `model_selection.py` |
| Table S6 (Finite-size stability) | `finite_size_stability_results.json` | `finite_size_stability.py` |
| Table S7 (L=256 anchors) | `fss_gamma0.5_L256.json` | `fss_compute.py` |
| Pure imaginary verification | All .json files (max Re < 1e-15) | `defense_all_attacks.py` |
| Fig 1 (β(α) plot) | `phase2_fit_results_FULL.json` | `figures/generate_figures.py` |
| Fig 2 (β-μ plot) | `phase2_fit_results_FULL.json` | `figures/generate_figures.py` |
| Fig 3 (universality panel) | `firewall_AHA1_results.json` | `figures/generate_figures.py` |

## Reproducibility

All numerical results can be reproduced by running the computation scripts in order:

```bash
# 1. Baseline COH scan (L=4-64, dense solver)
python phase2_L64_compute.py

# 2. Extended COH scan (L up to 256, dense + sparse)
python phase2_L_large.py

# 3. FSS sparse GMRES (L=128,256 for each γ_φ)
python fss_compute.py

# 4. Universality scan
python firewall_AHA1.py

# 5. Analysis scripts
python model_selection.py
python finite_size_stability.py
python verify_claims.py

# 6. Figures
cd figures && python generate_figures.py
```

**Note:** L=256 GMRES solves require ~15-25 minutes per (α, γ_φ) point on a standard CPU. The L=256 data in `fss_gamma0.5_L256.json` were computed on a local machine (details in `fss_gamma0.5_L256_raw.json` timing fields).

## Solver Parameters

| Parameter | Value |
|:----------|:------|
| L≤64 solver | Dense LU (`numpy.linalg.solve`) |
| L=128,256 solver | Sparse GMRES, diagonal preconditioning |
| GMRES rtol | 10⁻¹⁰ |
| Model parameters | J₀=0.3, Γ_L=Γ_R=1.0, f_L=0.65, f_R=0.35 |
| Scan ranges | α∈[1.1,1.9] (5 values), γ_φ∈[0.01,2.0] (5 values), L∈[4,8,16,32,64] baseline |

## Known Limitations

1. L=256 data only for γ_φ=0.5 (5 anchor points)
2. γ_φ=0.01 L=128 computation incomplete (ballistic limit is computationally stiff)
3. No independent cross-validation of L=256 GMRES (single solver/preconditioner)
4. μ(α,γ_φ) not independently computed (relies on Dhawan et al. for μ)
5. Generate_figures.py needs updating for L=128/256 flow/plateau visualization
6. Local exponents (β_64→128, β_128→256) are 2-point estimates without formal error bars
