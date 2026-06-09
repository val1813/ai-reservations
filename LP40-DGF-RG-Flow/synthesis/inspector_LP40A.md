# INSPECTOR Report: LP40-A Numerical Experiment Verification

**Inspected:** LP40-A Causal Graph RG numerical experiment
**Code:** `experiments/graph_rg/causal_graph_rg.py`
**Results:** `experiments/graph_rg/RESULTS.md`
**Date:** 2026-06-09
**Status:** Independent verification complete; bugs found

---

## Executive Summary

The LP40-A numerical experiment implements a Kadanoff-style blocking RG on random causal graphs and claims three key results: (1) a spectral dimension attractor at ds~2.5-2.8, (2) b1 is IR-relevant, and (3) partial support for d=3 emergence. **One confirmed code bug, one display bug creating a sign error in RESULTS.md, and several methodological issues undermine confidence in all three claims.** The experiment is a reasonable first attempt but its conclusions go significantly beyond what the data supports.

---

## 1. Code Correctness Audit

### 1.1 Blocking transformation -- CORRECT

The `block_coarse_grain` function correctly reduces N from L^d to (L/2)^d at each step. Verified:
- d=3, L=12: N=1728 -> 216 -> 27 -> 8. All correct.
- d=4, L=8: N=4096 -> 256 -> 16. All correct.
- d=2, L=16: N=256 -> 64 -> 16 -> 4. All correct.

q-field averaging (mean of member q-values) is the correct Kadanoff block-spin procedure.

### 1.2 b1 computation -- CORRECT

`compute_betti_numbers` uses the cyclomatic number formula: b1 = E - N + b0 for the undirected skeleton. Verified:
- E count via `(adj + adj.T).sign().nnz // 2` is correct
- b1 = E - N + b0 is mathematically exact for the undirected skeleton
- b1 never exceeds N(N-1)/2 (the maximum for a simple graph)
- Verified at d=3, step 1: E=506, N=216, b0=1 -> b1=291. Confirmed.

### 1.3 Spectral dimension estimator -- FRAGILE BUT FUNCTIONAL

The `spectral_dimension` function fits N(lambda) = lambda^{ds/2} using only the **last 10 points** of the low-energy regime (line 153: `stats.linregress(log_lam[-10:], log_N[-10:])`).

**Stability test across fitting methods (d=3, N=1728):**

| Method | ds | R^2 |
|--------|----|-----|
| Code method (last 10 low-E) | 2.15 | 0.98 |
| All low-E eigenvalues | 2.73 | 0.99 |
| First 20 eigenvalues (deep IR) | 2.79 | 0.96 |
| Middle 50% of low-E | 2.61 | 1.00 |

**Finding:** The ds estimate varies by +/-0.3 depending on fitting range. The code's method (last 10 points) systematically gives the **lowest** ds estimate. While the power-law fit quality is high (R^2 > 0.95), the absolute value is method-dependent.

**Small-N reliability:** For N < 100, the spectral dimension estimate degenerates. Random graphs at N=16 give ds=2.5, at N=27 give ds~2.4-2.7, at N=64 give ds~4.2-5.3. There is no stable ds value for small graphs — the estimator is dominated by noise.

### 1.4 **BUG: Sign display error in analyze_flow (line 327)**

```python
print(f"b1 density scaling: b1/N ~ N^{-gamma:.3f} (R2={r**2:.3f})")
```

The format `{-gamma:.3f}` **negates the actual gamma** for display. Since gamma is negative for all dimensions (see below), the displayed value appears positive. This caused RESULTS.md to report:

| Dimension | Actual gamma (from linregress) | Displayed (as -gamma) | RESULTS.md report |
|-----------|-------------------------------|----------------------|-------------------|
| d=2 | **-0.171** | +0.171 | "+0.17" |
| d=3 | **-0.063** | +0.063 | "+0.06" |
| d=4 | **-0.042** | +0.042 | "+0.04" |

**The signs in RESULTS.md are wrong.** The actual gamma values are negative. This is a display-sign-flip bug that contaminated the written results.

**Impact:** The interpretation at line 328 (`if gamma > 0: IR-irrelevant`) uses the correct gamma and correctly prints "IR-relevant WARNING" for all dimensions. But RESULTS.md, reading the displayed value, reports the wrong sign and mischaracterizes the scaling direction.

### 1.5 Edge generation -- CORRECT but O(N^2)

The graph generation iterates over all node pairs (O(N^2)), which is correct for nearest-neighbor lattice graphs but becomes expensive for N > 10^4. Not a correctness bug, but limits scalability.

### 1.6 Comment error (line 320-321)

Line 320: `# b1 density scaling: b1/N ~ N^{-gamma}`
Line 321: `# If gamma > 0: b1 irrelevant in IR`

Under the convention b1/N ~ N^{-gamma}, gamma > 0 means the exponent -gamma < 0, so b1/N decreases with N. As N decreases (IR coarse-graining), b1/N would increase, making b1 **IR-relevant**. The comment on line 321 is self-contradictory with line 320's convention. The actual check (line 328) uses the correct mathematical relationship where gamma is the slope of log(b1/N) vs log(N), bypassing the comment's error.

---

## 2. Results Validity

### 2.1 ds=4.87 for d=4 initial lattice -- OVERESTIMATE

For a 4D regular lattice, ds should be exactly 4. Edge removal (p_edge=0.7) should reduce or maintain ds, not increase it. The value 4.87 is an overestimate due to:
- The code's specific fitting method (last 10 low-E eigenvalues)
- With the "all low-E" fit: ds=3.87 (closer to but still below 4)
- Finite-size effects at L=8

**This is not a bug but a systematic estimator bias at this size.** The initial ds for d=4 should be ~4, not 4.87.

### 2.2 ds=2.47 for d=3 initial lattice -- UNDERESTIMATE

Expected ds=3.0 for a 3D lattice. Even accounting for 30% edge removal (p_edge=0.7, well above the ~0.25 percolation threshold), ds should be close to 3 at L=12. The measured 2.47 is 18% below expected. Multiple fitting methods give 2.15-2.79, all below 3.0.

**Possible causes:** (a) Finite-size effects at L=12, (b) the specific random seed, (c) edge removal genuinely lowers the spectral dimension at this scale. Regardless, starting 18% below the target dimension undermines the "flow toward d=3" narrative.

### 2.3 "ds attractor at 2.5-2.8" -- NOT ROBUST

**Evidence against the attractor claim:**

1. **d=2 does not join the attractor.** d=2 stays at ds~1.4-1.7 throughout the flow — it never approaches 2.5-2.8. A "universal attractor" should attract all dimensions.

2. **The attractor coincides with small N.** By the time ds "converges" to 2.5-2.8, N <= 256 for d=4 and N <= 27 for d=3. At these sizes, the spectral dimension estimator is unreliable. The apparent convergence could simply reflect that **small dense graphs generically have ds~2-3** regardless of their origin.

3. **No control experiment.** There is no baseline showing what ds values random graphs of the same size would give. Without this control, one cannot distinguish a genuine RG attractor from a trivial small-graph artifact.

4. **d=4 ds drops from 4.87 to 2.29.** This 2.6-unit drop in ONE step is suspicious. The step-1 graph (N=256) is a coarsened block graph that is significantly denser than the original lattice. Its spectral properties are dominated by the coarsening procedure, not by the RG flow of the original theory.

### 2.4 b1/N > 1 -- NOT A BUG, physically concerning

b1/N = 1.35 at d=3 step 1, and 1.99 at d=4 step 1. This is mathematically possible (E < N(N-1)/2 is always satisfied) but physically significant: the coarsened graph has more independent cycles than nodes. This means the coarse-graining procedure creates graph structures that are **topologically denser** than the original lattice.

Whether this is a valid RG feature or an artifact depends on interpretation. In the physical DGF, causal cycles at the Planck scale might be expected to proliferate under coarse-graining. But if b1/N > 1 persists to the IR, the effective theory at large scales would be dominated by dense causal feedback loops — not a smooth continuum.

### 2.5 b1 scaling gamma -- STATISTICALLY MEANINGLESS

| Dimension | gamma | R^2 | p-value | Data points |
|-----------|-------|------|---------|-------------|
| d=2 | -0.171 | 0.294 | 0.46 | 4 |
| d=3 | -0.063 | 0.086 | 0.71 | 4 |
| d=4 | -0.042 | 0.068 | 0.83 | 3 |

**None of these reach p < 0.05.** The R^2 values (7-29%) mean the linear fit explains only a small fraction of the variance. With 3-4 data points, any claim about the sign or magnitude of gamma is statistically unfounded.

A chi-squared test for the null hypothesis gamma=0 (constant b1 density) gives chi^2/dof << 1 for all dimensions, meaning the data is fully consistent with no scaling at all.

### 2.6 q-field invariance -- TAUTOLOGY, not a finding

The q distribution remains at mean~0.5 because:
- Initial q is sampled symmetrically around 0.5
- Blocking uses mean() which preserves the mean by linearity
- The clipping at [0.01, 0.99] is never triggered for means near 0.5

This is a built-in feature of the blocking procedure, not an experimental discovery about RG flow.

---

## 3. Conclusion Audit

### 3.1 Claim: "b1 is IR-relevant" -- **UNCERTAIN** (statistically unsupported)

The actual gamma values are negative (b1/N grows as N shrinks), which would mean b1 is IR-relevant. However:
- R^2 <= 0.29 and p >= 0.46: the trend is not statistically significant
- If the RESULTS.md sign error (+0.06 reported instead of the actual -0.063) were taken at face value, the interpretation would be reversed
- The b1/N > 1 at intermediate steps is a valid observation, but whether this represents IR relevance or a coarsening artifact is unclear
- 3-4 data points cannot constrain a scaling exponent

**Correct statement:** "b1 density does not decrease under coarse-graining; it may increase at intermediate steps, but the trend is not statistically resolved with the current data."

### 3.2 Claim: "ds attractor at 2.5-2.8" -- **OVERSTATED**

The evidence for a universal attractor is weak:
1. d=2 does not flow to 2.5-2.8 (it stays at 1.5-1.7)
2. The "convergence" occurs at N < 256 where ds estimation is unreliable
3. d=4 flows to ~2.5, but this is within the range of random small dense graphs — no evidence of a special attractor value
4. The d=3 ds=2.80 differs from the claimed attractor range center by ~10-20%

**Correct statement:** "The spectral dimension decreases from d=4 and increases from d=2 under coarse-graining, with all dimensions giving ds in the range 1.5-2.8 at accessible scales. Whether this represents a genuine fixed point cannot be determined from 2-3 RG steps on small graphs."

### 3.3 Claim: "partial support for d=3" -- **OVERSTATED**

The claim is based on d=3 ds stabilizing at ~2.8 (close to but below 3.0). However:
- The initial ds=2.47 is already 18% below 3.0 — the "flow" is from 2.47 to 2.80, an increase of only 0.33
- The final ds=2.80 differs from 3.0 by 7%, which is within the systematic uncertainty of the spectral dimension estimator
- The d=4 result (flowing away from 4) is interpreted as "supporting d=3" by process of elimination, but the d=4 flow goes to 2.5, not 3.0
- d=2 does not flow to 3.0

**Correct statement:** "The spectral dimension of d=3 causal graphs under coarse-graining is consistent with both ds=3 (within systematic errors) and ds=2.5-2.8 (the range seen for d=4). The data cannot distinguish between a d=3 fixed point and a generic small-graph attractor."

---

## 4. Honesty of Reporting

### 4.1 Limitations stated -- PARTIALLY ADEQUATE

RESULTS.md acknowledges:
- "当前图生成(超立方格点+p_edge)可能太简单" (graph generation too simple) -- YES
- Need for better graph models, larger graphs, better coarsening -- YES
- "ds并非精确地=3 (差~0.2-0.5)" -- YES, honest about the gap

### 4.2 Limitations MISSING or UNDERSTATED

1. **No mention of sign display bug.** The gamma sign error in RESULTS.md (+0.06 reported, actual -0.06) completely changes the interpretation. The actual data weakly supports IR-relevance (gamma < 0), but RESULTS.md reports the opposite sign.

2. **R^2 values not discussed.** The gamma fits have R^2 = 0.07-0.29, meaning 71-93% of variance is unexplained. These fits should not be used to draw conclusions about scaling exponents, yet RESULTS.md uses them as evidence.

3. **No control experiment.** There is no baseline for what ds values to expect from random graphs of the same size. The "attractor" claim requires demonstrating that the observed ds convergence is different from what you would get by coarse-graining random graphs.

4. **Seed dependence not tested.** Only one seed per dimension (seed=42+d). The ds values for d=2 vary from 1.61 (seed=44) to 1.41 (seed=46) — a 12% difference. Single-seed results cannot establish robust trends.

5. **Small-N ds unreliability not flagged.** The ds=2.61 at d=4 step 2 is computed from N=16 — a graph with only 14 eigenvalues. This should be explicitly noted as unreliable rather than used as evidence for convergence.

6. **Gamma sign convention not explained.** The display format `{-gamma:.3f}` flips the mathematical sign without documentation. A reader comparing RESULTS.md to the code would find contradictory values.

### 4.3 "Partial support" framing -- TOO GENEROUS

The RESULTS.md conclusion section frames findings as "mixed signals" with "good news" and "bad news." The "good news" items are:
- "谱维度确实流向~2.5-2.8的吸引子" — not established (see above)
- "d=4被RG流排斥" — d=4 flows to 2.5, not specifically to 3, so this doesn't support d=3
- "存在某种因果图RG普适类" — not supported by d=2 data

The overall framing overstates the positive evidence while the statistical and methodological weaknesses remain in the fine print.

---

## 5. Verdict Summary

| # | Claim | Verdict | Core Finding |
|---|-------|---------|-------------|
| 1 | ds attractor at 2.5-2.8 | **OVERSTATED** | Not universal (d=2 excluded), occurs at small-N where ds is unreliable, no control experiment, ds estimator is method-dependent with +/-0.3 systematic uncertainty |
| 2 | b1 is IR-relevant (gamma>0, b1/N grows under RG) | **UNCERTAIN** | Actual gamma is negative (sign display bug in RESULTS.md), R^2=0.07-0.29, p=0.46-0.83 — trend is not statistically significant with 3-4 data points |
| 3 | Partial support for d=3 emergence | **OVERSTATED** | d=3 ds goes from 2.47 to 2.80 (both below 3.0 by 7-18%), d=4 flows to 2.5 (not 3.0), d=2 doesn't join. The data is consistent with both d=3 and a generic small-graph attractor. |

---

## 6. Bug Impact Assessment

### Bug 1: Sign display error (line 327)
- **Severity:** Medium. Does not affect computation but contaminates reporting.
- **Impact:** RESULTS.md reports gamma with wrong sign. The actual gamma values are negative, meaning b1/N decreases with N (consistent with b1 density being higher at intermediate coarsening steps).
- **Fix:** Change format to `{gamma:.3f}` (remove the minus sign negation).

### Bug 2: Comment error (line 320-321)
- **Severity:** Low. Does not affect execution.
- **Impact:** The comment's sign convention is inconsistent with the code check.
- **Fix:** Align comment with actual behavior: `# b1/N ~ N^{gamma}; If gamma < 0: b1 IR-relevant`.

### Methodological issues (not bugs, but affect validity):
1. Single seed per dimension -- no error bars, no variance estimate
2. ds estimator uses only last 10 low-E points -- non-standard, biased compared to standard methods
3. No control experiment for small-graph ds baseline
4. 3-4 data points for gamma fit -- statistically insufficient

---

## 7. Recommendations

1. **Fix the sign display bug** (line 327: `{gamma:.3f}` instead of `{-gamma:.3f}`)
2. **Run multiple seeds** (>=10 per dimension) to establish error bars on ds and b1/N
3. **Add a control experiment:** Coarse-grain Erdos-Renyi random graphs of the same sizes and compare ds attractor values
4. **Use consistent ds fitting:** Fit all low-energy eigenvalues (not just last 10) and report R^2
5. **Increase graph sizes:** L0 >= 24 for d=3 to have meaningful spectral dimension at 2+ RG steps
6. **Report p-values** alongside R^2 for all linear fits
7. **Flag all ds values from N < 100** as "low confidence" in the results table
8. **Remove or qualify the "partial support for d=3" claim** until statistical significance is established

---

*INSPECTOR verification complete. The experiment is a reasonable first implementation but its three key claims are either overstated or uncertain. The code has one display bug and several methodological weaknesses that, while individually minor, collectively undermine the reported conclusions. Fix the display bug and re-run with multiple seeds, larger graphs, and a control experiment before drawing physical conclusions.*
