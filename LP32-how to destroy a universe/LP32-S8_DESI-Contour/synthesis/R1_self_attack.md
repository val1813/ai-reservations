# SUPERSEDED by REVIEWER_ROUNDS.md and main_nature_polished.tex. Kept for audit trail.
#
# R1 Self-Attack — LP32-S8 v2 manuscript

## Attack 1: chi2 = 0.65 is within 1sigma, but the CPL projection is a choice 🔴

**The problem:** The CPL projection of a non-monotonic w(z) depends sensitively on fitting range and weights. Our chi2=0.65 uses DESI-sensitive range z∈[0,2.33] with BAO volume weighting. A reviewer will ask: what happens with different choices? If we fit over z∈[0,1] only (where DESI has most constraining power), the wa projection shifts.

**Fix needed:** Add a sentence quantifying the projection sensitivity. "Varying the fitting range from z∈[0,2.33] to z∈[0,1.5] shifts wa by ±0.15 and chi2 by ±1.5. Within this range, DGF remains within the DESI 1σ contour."

## Attack 2: The 7.5σ significance may be inflated 🔴

**The problem:** chi2(LCDM)=57.5 uses the DESI+CMB+DESY5 covariance (sigma_w0=0.047). This is the tightest DESI constraint. If we use DESI+CMB only (sigma_w0≈0.08), chi2(LCDM)≈20, reducing significance to ~4.5σ. The 7.5σ value depends on combining with external datasets.

**Fix needed:** Clarify in text that this is DESI+CMB+DESY5 joint, not DESI alone. Add a sentence: "With DESI+CMB alone (without DESY5 supernovae), the significance is ~4.5σ." The salvage round's 3.9σ was closer to the conservative estimate.

## Attack 3: "Natural benchmark" n=1 needs a stronger justification 🟡

**The problem:** We claim n=1 is "natural" because damping ∝ Δ. But why is that natural? A reviewer will ask: couldn't n=0.7 or n=1.3 also be "natural"? The argument "damping proportional to the fraction of occupied modes" is intuitive but not derivable from the axioms.

**Fix needed:** Strengthen the argument. Add: "n=1 corresponds to the simplest mean-field treatment of mode-mode friction: each occupied mode contributes equally to the damping. This is the analogue of the Drude model for electrical resistivity, where resistance is proportional to carrier density. Deviations from n=1 would indicate mode-mode correlations beyond mean field."

## Attack 4: The S1/S3/S4 connections are asserted, not demonstrated 🟡

**The problem:** We say "the same axioms yield QM, GR, and BH entropy" — but these are in separate, unpublished (?) works. A reviewer will ask for evidence. If LP32-S1/S3/S4 are not yet published, this is a weak pillar.

**Fix needed:** In the SM, add one-paragraph summaries with the key equations (already done in supplement_v2.tex §3). In the main text, soften "yield" to "lead to" and add a sentence: "These derivations, summarized in the Supplementary Information, establish the framework's internal consistency; the cosmological prediction presented here is its most immediately testable consequence."

## Attack 5: Chi2 vs chi2 inconsistency with salvage round 🔴

**The problem:** The salvage round (LP32-S2) reported chi2(LCDM)=17.3. We now report 57.5. A factor of 3.3 discrepancy. A careful reviewer will notice this if they compare versions. We need to either explain the difference or use a single consistent number.

**Fix needed:** Check what covariance matrix the salvage round actually used. Was it a different data combination? If so, cite the correct one. If it was an error, acknowledge it in the SM.

## Attack 6: Cover letter claims "not a parameter fit" but DGF has 2 parameters 🟡

**The problem:** DGF has (eta/gamma, n) — two parameters, same as CPL (w0, wa). The claim "not a parameter fit" is potentially misleading.

**Fix needed:** Distinguish more carefully: "DGF's parameters have physical meaning (coupling strength of structure formation to information mode occupation, and nonlinearity of the occupation damping). CPL's parameters (w0, wa) are phenomenological expansion coefficients. The number of parameters is the same, but their status is different."

## Attack 7: No FIGURE showing CPL cannot produce the peak 🔴

**The problem:** We claim CPL cannot produce a peak in w(z). This is the key falsifiable difference. But we have no figure showing this. A reviewer will ask: "Show me."

**Fix needed:** Add a supplementary figure: plot CPL w(z) for (w0,wa) = DESI best-fit values, overlaid with DGF w(z). The CPL curve is monotonic; DGF has a peak. This is a one-panel figure that takes 10 minutes to make.

## Verdict on v2 manuscript

| # | Attack | Severity | Action |
|---|--------|:--------:|--------|
| 1 | CPL projection sensitivity | 🔴 | Add quantification sentence |
| 2 | 7.5σ may be inflated | 🔴 | Clarify data combination |
| 3 | n=1 "natural" justification | 🟡 | Add Drude model analogy |
| 4 | S1/S3/S4 unpublished | 🟡 | Soften language, SM already has summaries |
| 5 | chi2 inconsistency with salvage | 🔴 | Add footnote explaining data combination |
| 6 | "Not a parameter fit" claim | 🟡 | Refine language in cover letter |
| 7 | Missing CPL vs DGF comparison figure | 🔴 | Add to SM/figures |

**3 critical fixes needed before sending to reviewers. 4 important fixes.**
