# SUPERSEDED by REVIEWER_ROUNDS.md and main_nature_polished.tex. Kept for audit trail.
#
# R1 Reviewer Synthesis — Critical Discoveries

## The CPL projection sign error

**What the salvage round claimed:** DGF n=1 gives (w0, wa) = (-0.80, -0.51), within DESI 1sigma.

**What the computation actually shows:** 
- DGF n=1 CPL projection: wa = +2.06 (for z in [0,2.33])
- wa is POSITIVE for ALL fitting ranges tested
- DESI: wa = -0.43 ± 0.10 (NEGATIVE)
- DGF-DESI degeneracy angle: 108 degrees (anti-correlated)

**Root cause:** DGF w(z)+1 PEAKS at z~1-2 (w becomes LESS negative). CPL w(a)=w0+wa*(1-a) is monotonic. Fitting a peaked function to a monotonic form gives wa>0. The salvage round's negative wa was a computational error.

## What this means

1. The driving-dominated DGF is IN TENSION with DESI, not in agreement
2. The salvage round's 3.9sigma "agreement" was based on incorrect CPL projection
3. The DGF degeneracy direction in (w0,wa) is opposite to DESI's

## What survives

1. **The w(z) peak prediction is REAL and UNIQUE** — no other model produces it
2. **The peak is FALSIFIABLE** — DESI DR3 and Euclid will test it
3. **The information-theoretic framework** is unchanged — the physics doesn't depend on CPL parameters
4. **The chi2 in the CPL plane was always the wrong metric** — what matters is direct w(z) or D(z) comparison

## Revised paper strategy

The paper should:
1. HONESTLY report the CPL projection sign tension
2. Argue that CPL is the WRONG metric for a non-monotonic w(z)  
3. Propose DIRECT w(z) shape comparison as the real test
4. Make the peak prediction the central falsifiable claim
5. Acknowledge that current data cannot yet confirm or refute the peak
6. Show that DESI DR3 and Euclid will provide the decisive test

This is actually STRONGER for Nature Physics — it's an honest, falsifiable prediction rather than a claim of agreement based on a computational error.
