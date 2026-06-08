# PI Verification Of REVIEWER NSF-FCS-2T

**Date:** 2026-06-03

## Trigger

REVIEWER final recommendation: `major revision`.

Negative claim requiring PI verification:

- no direct duplicate found;
- no citation fabrication found;
- serious standard-framework coverage risk from nonequilibrium response / frenetic activity / MFT / open-exclusion FCS.

## PI Independent Search

Tool: `paper-search-mcp`, primarily CrossRef plus arXiv/OpenAlex/Semantic aggregate where relevant.

### Verified Standard-Framework Coverage

Confirmed relevant literature:

- Baiesi, Maes, Wynants, "Nonequilibrium Linear Response for Markov Dynamics, I: Jump Processes and Overdamped Diffusions", DOI `10.1007/s10955-009-9852-8`.
- Baiesi, Maes, Wynants, "Fluctuations and Response of Nonequilibrium States", DOI `10.1103/physrevlett.103.010602`.
- Baiesi and Maes, "An update on the nonequilibrium linear response", DOI `10.1088/1367-2630/15/1/013004`.
- Seifert and Speck, "Fluctuation-dissipation theorem in nonequilibrium steady states", DOI `10.1209/0295-5075/89/10007`.
- Bertini, De Sole, Gabrielli, Jona-Lasinio, Landim, "Macroscopic fluctuation theory", DOI `10.1103/revmodphys.87.593`.

PI judgment:

REVIEWER's standard-framework coverage risk is real. The NSF-FCS-2T claim must not be framed as a new general FDT violation, new universal nonequilibrium response principle, or replacement for frenetic/MFT response theory.

### Verified Open-Exclusion / FCS Coverage

Confirmed relevant literature:

- Gorissen, Lazarescu, Mallick, Vanderzande, "Exact Current Statistics of the Asymmetric Simple Exclusion Process with Open Boundaries", DOI `10.1103/physrevlett.109.170601`.
- Gorissen and Vanderzande, "Current fluctuations in the weakly asymmetric exclusion process with open boundaries", DOI `10.1103/physreve.86.051114`.
- Ayyer, "Full current statistics for a disordered open exclusion process", DOI `10.1088/1751-8113/49/15/155003`.
- Roche, Derrida, Doucot, "Mesoscopic full counting statistics and exclusion models", DOI `10.1140/epjb/e2005-00087-5`.
- de Queiroz, "Current-activity versus local-current fluctuations in a driven flow with exclusion", DOI `10.1103/physreve.86.041127`.

PI judgment:

The current/activity and open-exclusion FCS background is dense. The novelty bar must be phrased as a specific long-jump finite-volume diagnostic, not as "current cumulants under open boundaries".

### Verified Long-Jump / Reservoir Background

Confirmed relevant literature:

- Bernardin and Jiménez Oviedo, "Fractional Fick's law for the boundary driven exclusion process with long jumps", DOI `10.30757/alea.v14-25`.
- Jiménez Oviedo dissertation entry, "Exclusion process with long jumps in contact with reservoirs", DOI `10.70675/fb0d43d2z62c4z4ccdzb3adzaf2185d0e2c3`.

PI judgment:

Long-jump boundary-driven exclusion with reservoirs is an existing area. The present claim is not first work on long-jump reservoirs. It is at most a finite-volume FCS/response diagnostic inside that setting.

## Direct Duplicate Check

Searches for long-jump exclusion reservoirs plus current fluctuations/FCS did not reveal a direct match to:

`finite-window R2 parity tomography with delta^2, A^2, floor-scale delta A, and reversible traffic renormalization`.

PI agrees with REVIEWER:

- no direct duplicate found under available tools;
- no direct contradiction found;
- standard-framework coverage risk remains serious.

## PI Action

Carry forward the REVIEWER major-revision constraints:

1. Provide finite Markov-generator symmetry derivation for the absence of odd terms in the centered protocol.
2. Fully specify ledger convention for `lambda_T''=2G_T`.
3. Run robustness checks for numerical-floor `delta A`: precision, perturbation windows, alternative fit bases, and preferably independent implementation.
4. Place result explicitly against frenetic response, Seifert-Speck NESS FDT, MFT, and open-exclusion FCS.
5. Analytically separate or demote reversible traffic because it renormalizes NESS coefficients.
