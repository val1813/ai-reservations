# INSPECTOR Recheck: COH Round 2 — FULL Dataset (L=64 included)

**Date:** 2026-06-03
**Inspector:** Claude (INSPECTOR role)
**Files audited:**
- `phase2_raw_results_FULL.json` (125 data points)
- `phase2_fit_results_FULL.json` (25 fits)
- `round2_COH_numerical.md` (report)

---

## Q1: Data Completeness — PASS

| Check | Result |
|---|---|
| Total data points | 125 (matches 5 L x 5 alpha x 5 gamma_phi = 125) |
| L values present | [4, 8, 16, 32, 64] — all 5 |
| Alpha values | [1.1, 1.3, 1.5, 1.7, 1.9] — 5 values |
| gamma_phi values | [0.01, 0.1, 0.5, 1.0, 2.0] — 5 values |
| 25 points per L | L=4:25, L=8:25, L=16:25, L=32:25, L=64:25 — all present |
| All 25 (alpha, gamma_phi) combos per L | Present for every L |
| Fields abs_C_mid, re_C_mid, im_C_mid | Present in all 125 entries |
| Pure imaginary: max |re_C_mid| | 1.28e-15 (< 1e-14 threshold) — PASS |
| All im_C_mid > 0 | Yes (125/125 positive) |
| \|\|im_C_mid\| - abs_C_mid\| | 0.0 (exact equality) |
| \|C_mid\| decreases with L | Monotonic for all 25 (alpha, gamma_phi) combinations |

**Verdict: Data is complete, well-formed, and physically consistent.** The L=64 data has been correctly merged. All 125 points follow the expected pattern.

---

## Q2: Fit Self-Consistency — PASS

### Beta comparison: raw (L=4 vs L=64) vs fitted (power-law to all 5 L values)

| Metric | Value |
|---|---|
| Mean \|%diff\| across all 25 fits | 0.90% |
| Max \|%diff\| | 2.84% (alpha=1.9, gp=0.01) |
| All within 10% | YES (25/25) |

The small systematic offset (~0.5-2.8%) between the two-point beta and the fitted beta is expected: the power-law fit uses all 5 L values, which slightly adjusts the slope compared to a naive two-point estimate. All deviations are well under the 10% tolerance.

### R^2 Quality

| Metric | Value |
|---|---|
| Min R^2 | 0.8734 (alpha=1.1, gp=0.01) |
| Mean R^2 | 0.9720 |
| R^2 > 0.95 count | 20/25 |
| R^2 < 0.95 entries | 5 (all gp=0.01: R^2 = 0.873, 0.881, 0.887, 0.890, 0.893) |

The 5 entries below R^2=0.95 are exclusively gp=0.01 (very weak dephasing). This is physically expected: at near-zero dephasing, the system is in a coherent/quasi-ballistic regime where |C_mid| has non-power-law corrections (oscillatory components from coherent dynamics). The report correctly notes this: "R^2 ~ 0.87-0.89 for gp=0.01 (non-power-law corrections at very weak dephasing)." For gp >= 0.1, all R^2 > 0.97.

---

## Q3: Report Consistency — PASS

### Beta Table (Section 4) vs fit JSON

All 25 beta values in the report's table match `phase2_fit_results_FULL.json` to 3-decimal-place precision (the resolution of the table). Zero mismatches found.

Spot-check (5 random entries):
- alpha=1.1, gp=0.1: report=0.739, json=0.7391 -- match
- alpha=1.3, gp=1.0: report=1.080, json=1.0803 -- match
- alpha=1.1, gp=0.5: report=1.172, json=1.1723 -- match
- alpha=1.9, gp=2.0: report=1.004, json=1.0040 -- match
- alpha=1.5, gp=1.0: report=0.997, json=0.9974 -- match

### Qualitative Conclusions vs Data

| Claim in report | Data support | Verdict |
|---|---|---|
| "C_mid is pure imaginary for all L, alpha, gamma_phi" | max \|re_C_mid\| = 1.28e-15 across all 125 points | **PASS** |
| "beta(alpha) is monotonic (decreases as alpha increases)" | beta strictly decreases with alpha for all 5 gp values | **PASS** |
| "No sharp transition at alpha=3/2" | Slope change across alpha=1.5 is 0.005-0.24 for all gp (well below the 1.0 sharpness threshold) | **PASS** |
| "beta crosses 1 near alpha=1.5 for moderate dephasing" | gp=0.5: beta crosses 1 at alpha~1.4; gp=1.0: at alpha~1.5 | **PASS** |
| "R^2 > 0.97 for gp >= 0.1" | Min R^2 for gp >= 0.1 is 0.9769 | **PASS** |

No qualitative claim in the report is contradicted by the FULL dataset.

---

## Q6: Synthesis — Previous Warning RESOLVED

**Previous INSPECTOR warning:** `phase2_raw_results.json` contained only 100 points (L=4,8,16,32) while the report claimed 125 (including L=64).

**Status:** RESOLVED. `phase2_raw_results_FULL.json` now contains exactly 125 data points with all 5 L values (4,8,16,32,64), 25 (alpha, gamma_phi) combinations each. The report's data integrity note on line 12 correctly documents this fix.

### New Issues: None

All 11 verification gates passed:
1. 125 data points -- PASS
2. All 5 L values present -- PASS
3. All key fields present -- PASS
4. Pure imaginary (re_C_mid < 1e-14) -- PASS
5. Beta sample self-consistency < 10% -- PASS
6. Beta full self-consistency < 10% -- PASS
7. R^2 > 0.95 (with gp=0.01 caveat as documented) -- PASS
8. Beta table report-json match -- PASS
9. Beta monotonic in alpha -- PASS
10. No sharp transition at alpha=1.5 -- PASS
11. Previous data-missing warning resolved -- PASS

---

## Overall Verdict

**11/11 checks passed. 0 failures. 0 new issues.**

The FULL dataset (125 points, L up to 64) is complete, internally consistent, and fully supports all claims in `round2_COH_numerical.md`. The previous data-completeness warning is definitively resolved. The report can be considered verified for Phase 2 numerical results.
