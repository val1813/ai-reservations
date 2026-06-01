# Phase 2 Minimal Numerical Test

This directory contains a minimal exact-diagonalization style diagnostic for Phase 2.

The script is intentionally small and conservative:
- fixed particle number basis
- HN-Hubbard Hamiltonian
- OBC / PBC
- hard / dephase / clamped freeze
- center-of-mass velocity proxy for directional information flow

It does not claim to compute final QLIF. It tests whether the direction label is stable enough to justify a stricter QLIF implementation.

Run:

```powershell
python .\phase2_minimal_test.py
```

Output:

`phase2_minimal_results.csv`
