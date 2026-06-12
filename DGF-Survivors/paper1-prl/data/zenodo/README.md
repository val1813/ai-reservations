# LP38 PRL Submission — Experimental Data & Code

**Paper:** Causal Topology Enforces Quantum Non-Markovianity
**Target:** Physical Review Letters
**Authors:** Zhongchang Huang
**Date:** 2026-06-10

---

## File Inventory

### Experimental Data (IBM Q, ibm_kingston, Heron r2)

| File | Description | Paper Reference |
|:--|:--|:--|
| `cfol_symmetric_results.json` | **Primary result:** Symmetric temporal ring Y-basis CFOL verification. ΔI_Y = 0.645/0.354/0.128 bits at π/4,π/8,π/16. S/N = 129σ/71σ/26σ. | Main text §Experimental |
| `cfol_ZY_results.json` | Y-basis vs Z-basis comparison. Confirms Z-basis blindness (Y/Z = 3-54x). | SM §Z-basis Blindness |
| `cfol_results_d8k1kcj2.json` | First CFOL experiment (20k shots, Z+X basis). | SM §S7 |
| `cfol_final_jobs.json` | Job summary for all IBM Q submissions. | SM Table S5 |
| `cfol_Y_job.json` / `cfol_Z_job.json` | Per-job metadata. | — |

### Experiment Scripts (Qiskit)

| File | Description |
|:--|:--|
| `cfol_symmetric.py` | Symmetric temporal ring submission script (θ₁=θ₂=θ, Y-basis). Primary experiment. |
| `cfol_ibm_experiment.py` | First CFOL experiment script (asymmetric: θ₁=π/2, θ₂=θ, Z+X basis). |
| `protocols_submit.py` / `protocols_retrieve.py` | Ratio test + axis test submission and retrieval. |

### Numerical Experiments & Theory

| File | Description | Paper Reference |
|:--|:--|:--|
| `numerical_experiments.py` | Ring size scaling (N=4,6,8), noise robustness, spatial ring simulation, axis scan. | SM Fig. S2 |
| `numerical_experiments_results.json` | Output data from numerical experiments. | — |
| `ybasis_prediction.py` | Y-basis CFOL signal prediction (local simulation). | SM §Y-basis Prediction |
| `ybasis_prediction.json` | Y-basis prediction values at IBM Q conditions. | — |
| `zbasis_ybasis_full.json` | Z+Y basis full parameter scan (5 Bell fidelities × 5 noise rates × 3 θ values). | SM §Noise Decomposition |
| `theory_ratio_axis_test.py` | Ratio test + axis test theory for 4-node spatial ring. | SM §S5.2, S6 |
| `theory_predictions.json` | Theory prediction values (R=0.48, axis ratio=2.06x). | — |
| `theta_scaling_precision.py` | Small-θ precision scan for scaling law verification (referenced as `cat2_task5_precision_small_c.py` in SM §S4). | SM §S4 |

---

## Reproducibility

```bash
# Install dependencies
pip install qiskit qiskit-ibm-runtime numpy scipy

# Re-run numerical experiments (no IBM Q needed)
python numerical_experiments.py

# Re-run Y-basis prediction
python ybasis_prediction.py

# Re-run theory predictions
python theory_ratio_axis_test.py

# Re-submit to IBM Q (requires valid API token)
python cfol_symmetric.py  # edit TOKEN variable first
```

---

## IBM Q Job Summary

| Job ID | Design | Basis | Shots | Result |
|:--|:--|:--|:--|:--|
| `d8kc05o32u0s73f8ipq0` | Symmetric (θ,θ) | Y | 600k | **CFOL verified (26-129σ)** |
| `d8kborbnn5bs738qlerg` | Asymmetric (π/2,θ) | Y | 600k | Y-basis signal, wrong θ-trend |
| `d8kbp33nn5bs738qlf60` | Asymmetric (π/2,θ) | Z | 600k | Z-basis blindness confirmed |
| `d8k1kcj2d42s73c9kipg` | Asymmetric (π/2,θ) | Z+X | 240k | First CFOL sign check |
| `d8k2e4bnn5bs738q9s70` | Ratio + Axis test | Z | 160k | Null result (ratio test not feasible on temporal ring) |

---

## Notes

- The SM references `cat2_task5_precision_small_c.py` — this is `theta_scaling_precision.py` in this repository (renamed for clarity).
- V3/V4 raw data (`v3_raw.json`, `v4_raw.json`, 3.8MB each) are available on request. These failed experiments are described in SM §S8 with key results in Tables S3-S4.
- All Qiskit circuits use standard gates (RZZ, RXX, H, CX, Sdg). No custom gate definitions.
- Token in submission scripts is placeholder — replace with your own IBM Q API key.

---

*Zenodo archive prepared for PRL submission.*
