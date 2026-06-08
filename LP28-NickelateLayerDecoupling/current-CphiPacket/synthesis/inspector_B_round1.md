# INSPECTOR Report: B Round 1

Verdict: WARNING

Scope checked: `current-CphiPacket/B/round1.json` only. I did not read A output and do not perform PI synthesis.

Mechanical check:
- JSON parses successfully.
- No validation script was found under the project/current packet paths; no formulas, dimensional claims, or algebraic derivations are present, so Q1/Q4/Q5 are not applicable beyond structural sanity.

## Checklist Findings

1. Universal impossibility risk: PASS

B explicitly states the claim is not a universal theorem and is restricted to current literature assembly plus loosely matched near-term designs that lack a new sealed same-specimen/sister-specimen protocol. The `not_impossible_in_principle: true` and `falsifier_for_B` sections preserve an experimental route. This does not over-upgrade "current literature cannot be stitched" into universal impossibility.

Residual caution: the phrase "near-term matched-specimen designs" should remain tied to "without new sealed protocol"; PI should not quote it as a general impossibility of matched specimens.

2. Non-identifiability specificity: PASS

The non-identifiability argument is concrete enough for Round 1. It names shared latent variables: pressure path, hydrostaticity, oxygen/vacancy state, phase fraction, RP admixture, c-axis coherence, orbital/ligand-hole/self-doping balance, sample damage/strain/disorder, and RIXS matrix-element calibration. It also states the mechanism: P_oe extraction and B_min baselines reuse qz/c-axis/orbital/pressure/structure information, so residual allocation is underdetermined.

This is not merely generic skepticism. It gives a minimum counterfactual requirement: an independent axis changing B_min without changing P_oe calibration, or changing P_oe while holding B_min fixed, under sealed output labels.

3. Contamination paths: PASS

The listed paths cover the main same-origin contamination risks for P_oe/B_min:
- qz/c-axis common cause
- pressure path common cause
- oxygen/vacancy common cause
- phase fraction and RP admixture
- matrix element / resonance / polarization calibration
- sample-quality selection
- lab/instrument/batch aliasing
- output leakage

No major contamination family is missing at this abstraction level. Contact geometry and thermal cycling appear under pressure path / sample quality but could be named explicitly in the next B round if transport rows become central.

4. Falsifier for B: WARNING

B gives a real falsifier: same-crystal or genuinely sister-specimen rows, pre-output P_oe, full B_min, raw calibration, independent B_min extraction, blind residual calls, held-out rows split by batch/lab, permutation controls, and matrix-element/denominator-floor sensitivity.

Weakness: the threshold "at least several independent rows" is too vague for PI synthesis. It is acceptable for Round 1, but PI should require B or the next round to define a decision-grade minimum: how many rows, what axes must vary, and what constitutes batch/lab independence.

5. Small-N/crossfit and matched-specimen issue: PASS

B's warning is reasonable: crossfit is not meaningful if rows are batch/lab/probe-correlated montages rather than independent blinded specimens. The matched-specimen critique correctly focuses on growth batch, oxygenation, pressure path, phase fraction, damage history, and output blinding. This is a valid identification objection, not a blanket rejection of all sister-specimen protocols.

6. Citation / literature-claim risk: WARNING

B relies on broad literature claims but does not expose concrete citations inside the JSON. Claims PI should independently verify before using them as factual support:
- recent La3Ni2O7 work links superconductivity and normal-state behavior to apical oxygen vacancies, oxygen content windows, structural transitions, phase coexistence, and high-pressure measurement reliability;
- La4Ni3O10 or other RP phase admixture is a realistic confounder for the packet under discussion;
- current literature lacks any accessible complete same-sample or properly blinded sister-specimen P_oe + B_min packet;
- raw S_channel_to_chi_unit calibration is usually unavailable in a reusable form.

This is not a blocker for B's design-level conclusion, but it must be marked as PI verification debt.

7. Theory-breakthrough route: PASS

B does not block the real theory/experiment route. It correctly redirects the claim from "literature packet can kill/preserve R_oe now" to "new sealed same-sample or tightly sistered-specimen experiment can make the packet identifiable." This preserves the North Star rather than closing it.

## Must Pass To PI Synthesis

Status: B Round 1 is usable with warnings.

Core conclusion to carry forward:
B has a defensible Round 1 case for `PACKET_NONIDENTIFIABLE_FROM_CURRENT_LITERATURE`, not for universal impossibility.

PI should preserve these B constraints:
- Do not assemble P_oe and B_min from literature montages across different samples/probes as if they were rows.
- Treat qz/c-axis/orbital/pressure/structure/oxygen variables as potentially shared generators of both P_oe and B_min, not automatically independent baselines.
- Crossfit only matters if rows are independent blinded rows split by batch/lab/probe lineage, not repeated measurements or famous sample clusters.
- A valid rescue route is a sealed same-sample or genuinely sister-specimen campaign with raw calibration, pressure/oxygen/phase logs, independent B_min, blinded output labels, negative controls, and sensitivity to matrix-element/denominator-floor choices.

Warnings PI must handle:
- Require citation-level verification for B's broad nickelate literature claims before relying on them.
- Tighten the falsifier threshold beyond "several rows" before using it as a go/no-go experimental criterion.

Blockers: none found.
