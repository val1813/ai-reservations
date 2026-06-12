# Confirmed Motivation — Three-Part Structure

## One-Sentence Motivation
Causal topology is an independent control parameter for quantum non-Markovianity that the standard open-systems toolbox misses, and its effect is both exact and experimentally decisive.

## Three-Part Argument

### 1. Problem
The standard theory of open quantum systems accounts for coupling strengths, spectral densities, and temperature — but not the topology of the causal graph connecting system to environment. Two systems with identical Hamiltonian couplings, identical bath spectra, and identical temperatures can differ in whether their interactions form closed causal loops, and standard theory predicts identical behavior for both.

### 2. Status Quo (Why existing approaches fail)
- Perturbative treatments predict QCMI ∝ θ⁴ for aligned-axis configurations, effectively zero at weak coupling
- Previous work on squashed non-Markovianity (Gangwar 2025, Buscemi 2025) established QCMI as a measure but didn't ask the structural question: does the mere presence of a cycle force QCMI > 0?
- The HJPW condition (Hayden et al. 2004) gives an algebraic condition for QCMI = 0 but doesn't translate it to operational, geometric terms
- Numerical studies persistently find more quantum memory than perturbative theory allows — these anomalies are the signature of a deeper structure

### 3. Window (Why now)
- The necessary mathematical machinery exists: Gram matrix factorization for Cartan-aligned graphs, QCMI as a non-Markovianity measure, and the HJPW algebraic structure
- What was missing was asking the right question: "Can a single causal cycle force QCMI > 0 independent of coupling strength?"
- Existing IBM Q hardware (Kingston Heron r2) can test the predictions at S/N > 29
- The CFOL theorem provides an "if and only if" result — exact, not perturbative — which is rare in open quantum dynamics

## Reader 5-Question Test

### Q1. Relevance (first paragraph for non-specialist)
✅ The causal graph structure of quantum interactions matters in a way that standard theory misses — a single closed loop traps quantum information regardless of how weak the coupling is. The effect is geometric, not energetic.

### Q2. Novelty (clear before/after line)
✅ Before: Open quantum systems theory tracks coupling strength, spectra, temperature. Cycles were not considered an independent parameter.
✅ After: We prove cycles force nonzero QCMI iff Cartan angles ∉ (π/2)ℤ — an exact necessary and sufficient condition.

### Q3. Trust (independent verification per claim)
✅ Theorem: mathematical proof + 83,521-point grid scan
✅ Scaling law: numerical Gram matrix diagonalization, R² > 0.998
✅ Experimental tests: three specified protocols on existing IBM Q hardware, with error budgets

### Q4. Reuse (reproducibility)
✅ Circuit specifications in SM
✅ Code: `cat2_task5_precision_small_c.py`, `cfol_scan.py`, `b1_scaling.py`
✅ Analytical derivations with explicit steps

### Q5. Meaning (honest limitations)
✅ "Whether an analogous theorem holds beyond qubits remains open" (Discussion)
✅ π/32 measurement falls below noise floor → explicitly stated as not testable on current hardware
✅ Asymptotic expansion accurate to 8% for θ ≲ π/8 → explicitly quantified
