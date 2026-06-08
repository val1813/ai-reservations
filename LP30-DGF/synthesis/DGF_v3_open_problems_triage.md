# DGF v3 Open Problems Triage

Date: 2026-06-05

Source paper: `paper/DGF_Unified_v3.md`

## Executive result

The six open questions do not close as six new positive derivations.  The
defensible optimization is to convert several over-strong claims into explicit
no-go or identifiability results, and to downgrade unsupported mechanisms to
conditional research programs.

## Conclusions checked by subagents

### C1. Metric derivation route

Conclusion: Schrödinger, Lindblad, or path-integral dynamics cannot be used as
DGF first-principles inputs for deriving the complex metric, because they
already presuppose time-evolution or action structure.  The current line
element is therefore an effective complex quadratic representation, not a
completed metric derivation.

INSPECTOR: Passed with warning.  Safe only if phrased as "violates the
founding principle when used as a starting point."

Reviewer: This is necessary but is a downgrade, not a solution.

Paper change: Section 4.3 and Gap 3 rewritten.

### C2. Local screening of `Gdot/G`

Conclusion: The linear point-source solution does not screen cosmological
drift.  For fixed source parameters,

`q(r,t)=q_inf(t)-M l/(4 pi m0 r)` implies `partial_t q(r,t)=dot q_inf(t)`.

INSPECTOR: Passed with scope condition: fixed source, linear equation, far
boundary drift only.

Reviewer: This is the strongest hard result; it kills the old screening
intuition in the linear route.

Paper change: Prediction 4 and Gap 5 rewritten with a no-screening lemma.

### C3. `q_inf` absolute constraints

Conclusion: `G=(pi q_inf/8)c^3 l^2/hbar` fixes only
`q_inf l^2=(8/pi)l_P^2`.  Without an independent measurement or postulate for
`l`, `q_inf` is not identifiable and has no nonzero lower bound.  From
`q_inf<=1` one gets only `l>=sqrt(8/pi)l_P`.

INSPECTOR: Passed.

Reviewer: Necessary correction.  BAO/SN/BBN can constrain relative evolution
of `q_inf l^2`; with constant `l`, they constrain `q_inf(z)/q_inf(0)`, not the
absolute normalization.

Paper change: Section 6.3 rewritten.

### C4. Graph RG fixed point

Conclusion: "Unique stable fixed point is Z^3" is too strong.  Coarse-graining
normally identifies a universality class, not a unique microscopic graph.
The defensible target is a 3D isotropic continuum universality class.

INSPECTOR: Original strong claim fails.

Reviewer: This solves the review risk by downgrading the claim, not by proving
microscopic uniqueness.

Paper change: Gap 6 rewritten.

### C5. Prediction 1

Conclusion: `G_eff(q)=G/sqrt(1+pi^2 q^2)` cannot be interpreted as a
suppression from coherent quantum probes.  At `q=1`, the exact ratio is
`1/sqrt(1+pi^2)=0.303`, an order-unity effect.  Existing cold-atom and
atom-interferometric gravity measurements would already have seen such an
effect if it depended on the probe coherence.

INSPECTOR: Passed with numerical correction from "G/pi" to exact 0.303.

Reviewer: Current Prediction 1 fails under both readings: if `q` is probe
coherence it is experimentally excluded; if `q` is source archival state, the
BEC/atom-interferometer target was misidentified.

Paper change: Prediction 1 rewritten as a conditional source-state test.

External checks used:

- Rosi et al., "Precision measurement of the Newtonian gravitational constant
  using cold atoms", Nature 510, 518-521 (2014), DOI `10.1038/nature13433`.
- Westphal et al., "Measurement of gravitational coupling between
  millimetre-sized masses", Nature 591, 225-228 (2021), DOI
  `10.1038/s41586-021-03250-7`.

### C6. `d=3` via Muller-Masanes

Conclusion: Muller-Masanes cannot directly prove DGF `d=3`.  Short-time
intra-cell reversibility plus long-time irreversible coarse-graining does not
determine the large-scale graph dimension.  Their theorem is compatibility
support only if DGF's effective direction degrees of freedom are independently
shown to satisfy the required axioms.

INSPECTOR: Passed.

Reviewer: This does not solve Gap 1; it prevents an invalid bridge.

Paper change: Relation to Existing Work and Gap 1 rewritten.

External check used:

- Muller and Masanes, "Three-dimensionality of space and the quantum bit: an
  information-theoretic approach", New Journal of Physics 15, 053040 (2013),
  DOI `10.1088/1367-2630/15/5/053040`.

## Remaining real work

1. Derive the complex quadratic representation from information-only axioms.
2. Build an information-graph-to-acceleration bridge without importing GR as
   a starting point.
3. Replace local `Gdot/G` screening intuition with an explicit nonlinear or
   source-locked equation, then solve it.
4. Define a source/test/environment coupling for any source-state gravity
   modification.
5. Prove only a 3D isotropic continuum universality class, not microscopic
   `Z^3` uniqueness.
