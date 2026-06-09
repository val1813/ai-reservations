# Confirmed Motivation — LP32-S2

## One-Sentence Motivation
DESI DR2 reveals cosmic structure formation empirically tracks dark energy evolution — we provide the first microscopic theory showing why, using a quantum many-body qubit ensemble driven by gravitational collapse.

## Three-Part Argument

### 1. Problem
DESI DR2 finds ~3σ evidence that dark energy evolves with time and crosses the phantom divide w=-1. This behavior cannot be explained by any single-field dark energy model in standard quantum field theory, nor by ΛCDM. The empirical correlation between cosmic star formation history and w(z) found by Gough (2025) demands a physical explanation, but no microscopic theory exists.

### 2. Current State
Existing approaches fall into four categories, none of which provide a microscopic origin:
- **Quintom/two-field models** (Feng 2005, Chen 2026): Require ad hoc combinations of quintessence and phantom fields
- **Modified gravity** (Linder 2025, Cataneo 2025): Modify GR rather than explaining DE
- **DM-DE interaction** (Khoury 2025, Guedezounme 2026): Phantom behavior is apparent, not intrinsic
- **Dissipative quintessence** (Chanda 2026): Uses classical dissipation; no quantum origin

None address the empirical SFR-DE correlation that Gough identified.

### 3. Why Now
Three developments converge to make this theory possible:
1. **DESI DR2 data** now provides binned w(z) constraints precise enough to test model predictions
2. **Quantum many-body theory** (Curie-Weiss/Lindblad/complex Langevin) is mature and directly applicable
3. **Analog quantum simulation** on 3-5 qubit chips is now feasible, providing a laboratory test of the core mechanism

The combination of new data, mature theory, and testable predictions creates a unique window.

## Reader 5问 (Nature-Skills)

### Q1 — Relevance
**Can a non-specialist understand why this matters from the first paragraph?**
Yes. The opening: "DESI DR2 finds dark energy evolving with time, crossing the phantom divide. No existing theory explains why." This connects a major observational puzzle to a theoretical gap that any physicist can appreciate.

### Q2 — Novelty
**Can the abstract clearly separate prior work from our contribution?**
Yes. Line: "Gough identified an empirical correlation... but no microscopic theory was provided. Here we develop that theory." The prior/our line is explicit: Gough = empirical; we = microscopic theory.

### Q3 — Trust
**Does each core claim have ≥1 independent verification path?**
| Claim | Verification |
|-------|-------------|
| $w(z)$ crosses -1 at $z \sim 0.5-1$ | Compare with DESI binned constraints (data) |
| $a_c^2$ from Curie-Weiss theory | Derive analytically (math); test via analog quantum simulation (experiment) |
| $\mathcal{P}_{\rm coll}$ drives the qubit ensemble | Compute from halo model (numerical); compare SFR vs $\mathcal{P}_{\rm coll}$ variants |
| Landauer principle applies to gravity | Honestly flagged as weakest link; model works phenomenologically without it |

### Q4 — Reuse
**Can a colleague reproduce this work?**
- SM provides full derivation of complex Langevin equation from Lindblad
- SM provides full $\mathcal{P}_{\rm coll}$ computation details
- All parameters and methods specified
- Weak: code is "available upon request" — should consider releasing

### Q5 — Meaning
**Are boundaries and limitations honestly discussed?**
Yes. Explicitly discussed:
- Landauer assumption violations in self-gravitating systems (§4.2)
- $\kappa$-$a_c^2$ degeneracy (§5.3)
- Linear $w+1$ expansion validity range
- $\sim 2\sigma$ significance — not a detection
- Driver systematic uncertainties ($M_{\rm min}$, halo mass function)
- Proposed quantum simulation is proposed, not executed
