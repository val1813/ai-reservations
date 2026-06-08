# LP29 GATE 1.5 INSPECTOR Report: B Deepening Supplement

Input scope: only `current/B/deepening_supplement_gate15.json`.

Required context read:
- `D:\Claude\ai-reservations\ai\INSPECTOR.md`
- `D:\Claude\ai-reservations\LP29-AmorphousBands\current\B\deepening_supplement_gate15.json`
- `D:\Claude\ai-reservations\LP29-AmorphousBands\synthesis\reviewer_round3.md`

## 0. Mechanical Check

`validation/validate.py` is not available under `D:\Claude\ai-reservations\LP29-AmorphousBands\validation` or `D:\Claude\ai-reservations\validation`. Per INSPECTOR protocol, Q1-Q6 are checked manually.

The object under inspection is a supplement JSON, not a standard `roundN_claims.json`; no schema validation was run.

## 1. Layer-Depth Check

Result: pass.

- `deepening_1` has two explicit layers:
  - `deepening_1_layer_1`: graph spectral projection.
  - `deepening_1_layer_2`: residualization after mobility-edge controls plus targeted attack.
- `deepening_2` has two explicit layers:
  - `deepening_2_layer_1`: same-sample external-label measurement protocol.
  - `deepening_2_layer_2`: negative controls, leave-one-composition-out, and perturbation attack.

Each layer adds distinct content rather than restating the same point: graph-spectral residual testing, targeted perturbation contrast, locked external-label schema, and generalization/negative-control logic.

## 2. Q1 Dimensional Consistency

No blocking dimensional error found.

### `w_ij=t0*exp(-(r_ij-r0)/lambda)*(1+alpha_edge*I_edge+alpha_corner*I_corner)*exp(-beta*f_OO,ij)`

- Left side SI unit: energy, e.g. joule or eV.
- Right side SI unit: `t0` energy times dimensionless factors.
- Match: pass if `r_ij`, `r0`, and `lambda` are lengths, and `lambda != 0`.
- Transcendental arguments:
  - `(r_ij-r0)/lambda` is dimensionless.
  - `beta*f_OO,ij` is dimensionless if `beta` and `f_OO,ij` are dimensionless.
- Protocol caveat: the supplement correctly labels this as a diagnostic graph Hamiltonian, not a physically validated hopping law.

### `L_w=D_w-A_w`

- Left side unit: same as weighted adjacency entries if `D_w` sums `w_ij`; energy if `A_w` stores hoppings.
- Right side unit: energy minus energy.
- Match: pass.
- Protocol caveat: if later reporting normalized `lambda_2`, the normalization must be declared because normalized and unnormalized Laplacian spectra have different units.

### `H_graph=diag(epsilon_i)+A_w`

- Left side unit: energy.
- Right side unit: energy plus energy if `epsilon_i` and `A_w` entries are both energy.
- Match: pass.
- Protocol caveat: `H_graph` is explicitly diagnostic and cannot be used as an external validation label.

### `M_perp=(I-P_controls)M(X)` and `Y_perp=(I-P_controls)Y`

- These are residualization/projection formulas. They require algebraic compatibility in feature space, not a universal physical unit.
- `I-P_controls` is dimensionless as a projection/operator on the chosen design matrix column space.
- `M_perp` has the same units as `M(X)`.
- `Y_perp` has the same units as `Y`.
- Pass, provided the regression/projection is performed after appropriate scaling or with a design matrix whose columns are not treated as directly addable physical quantities outside the statistical model.

### `V_e=b_e*|w_e|/t0`

- `b_e`: dimensionless centrality.
- `|w_e|/t0`: dimensionless energy ratio.
- `V_e`: dimensionless.
- Match: pass.

### `V_target=sum_e betweenness_e*|w_e|/t0`

- Each summand is dimensionless.
- Sum is dimensionless.
- Match: pass.

### `Delta_attack=loss_targeted-loss_random at matched damage budget`

- Left side unit: same as the chosen loss.
- Right side unit: loss minus loss under the same target and same loss definition.
- Match: pass if both losses use the same target, same metric, and matched damage budget.
- Protocol caveat: if the loss is dimensionless predictive loss, no physical unit is required; if it is loss in mobility, Drude weight, or residual label space, units follow the target/loss convention.

## 3. Q2 Direction and Sign Checks

No blocking direction contradiction found, but two warning-level constraints must stay explicit.

### Residual graph-predictive signal after deleting high-leverage motifs

The supplement states:

- Partial residual mobility or Drude weight should increase with `z_eff`, `S_GC`, `lambda_2`, and `rho_A` after controls.
- Partial residual mobility or Drude weight should decrease with high-betweenness O-O damage.
- Targeted high-`V_e` damage should be worse than random damage at matched `f_OO` or deleted-edge count.

This is internally self-consistent. If high graph-leverage or high-vulnerability motifs/edges are deleted or weakened, the residual graph-predictive signal should decline relative to matched random attack, assuming B has real residual content.

Warning: the phrase "delete high graph leverage motifs" can mean either removing beneficial high-conductance connectors or removing damaging O-O motifs. These have opposite expected signs. The supplement mostly uses `high-betweenness O-O damage` as harmful and `high-V_e` attack as damaging important connectors. Future prompts must separate:

- attacking high-value conductive edges: expected residual mobility/Drude/ridge coherence decreases;
- removing harmful O-O damage motifs: expected residual mobility/Drude/ridge coherence may increase.

### Mobility-edge-only baseline and target leakage

The supplement explicitly requires:

- controls fit first;
- graph metrics computed from structure only;
- Hall-derived predictors excluded when predicting the same Hall target;
- external labels not generated by the same graph proxy used to define `M(X)`;
- mobility-edge/Ioffe-Regel controls not tuned post hoc to lose.

This is directionally and statistically self-consistent. The mobility-edge-only baseline is not polluted by the targeted attack unless attack-derived or graph-derived features are allowed into baseline controls. The supplement forbids that leakage in its assumptions and negative controls.

Warning: the actual implementation must enforce separate feature namespaces: baseline controls cannot include `V_e`, `V_target`, attacked-edge masks, graph residuals, or any target-derived Hall quantity when the target is Hall mobility.

## 4. Q3 Circularity Check

No blocking circular validation claim found.

The supplement repeatedly restricts B to a predeclared residual-prediction protocol and says synthetic recovery is diagnostic only. It explicitly states:

- "Synthetic recovery of graph rules is diagnostic-only and cannot validate B."
- `H_graph` is not an external validation label.
- attack inside `H_graph` remains a diagnostic.
- evidence requires external Hall/Drude/Wannier/spectral residuals or matched-control residual labels not generated by the same graph proxy.
- current B Round 3 data status is synthetic toy benchmark only.

This directly addresses Reviewer Round 3's warning that a synthetic generator containing the same graph rule cannot validate material physics.

Warning: any future use of `Y_proxy` generated inside `H_graph`, graph-rule synthetic data, or attacked-graph loss must be labeled "diagnostic/synthetic benchmark only". It cannot be described as physical validation, mechanism discovery, or evidence for real amorphous In2O3 transport.

## 5. Q4-Q5 Order, Algebra, and Source Checks

### Q4 Order-of-magnitude

No concrete numerical estimates are introduced in the supplement. No order-of-magnitude mismatch can be assessed.

### Q5a Algebra

The algebraic definitions are straightforward projections, graph operators, and differences of matched losses. No sign, coefficient, or exponent error is visible at the formula level.

### Q5b Limit behavior

- As `r_ij` increases with `lambda > 0`, `w_ij` decreases: consistent.
- As `f_OO,ij` increases with `beta > 0`, `w_ij` decreases: consistent.
- If `alpha_edge` or `alpha_corner` are positive, the corresponding motif multiplier increases `w_ij`; if negative, it decreases. The supplement does not require a fixed sign, so this is not an error.
- If the graph is more connected under positive weights, `lambda_2`, `rho_A`, `z_eff`, and `S_GC` can plausibly track better graph transport diagnostics, but monotonicity to external mobility is a hypothesis to test, not a derivation.

### Q5c Numerical substitution

No numerical substitution is possible because no parameter values, datasets, or fitted coefficients are supplied.

### Q5d Source/provenance

The supplement correctly marks real data as acquisition targets rather than completed validation:

- Jankousky raw structures/QSGW subset.
- Furubayashi digitized transport table.
- Aliano-style AIMD fallback.
- same-sample external Hall/Drude/Wannier/spectral labels.

Warning: this remains a protocol document until the locked same-sample table and provenance flags exist.

## 6. Q6.3-Q6.5 Integrated Judgment

### Q6.3 Claim shrinkage

There is claim shrinkage relative to a mechanism-level LP29 story, but it is explicit and appropriate after Reviewer Round 3. The supplement sets:

- current claim level: "measurement protocol plus reproducible synthetic benchmark";
- forbidden claim: no new graph mechanism for amorphous band-like transport;
- allowed claim: predeclared residual-prediction protocol.

This is not a blocker; it is a required downgrade. PI should reflect the reduced claim level in the matrix/score if not already done.

### Q6.4 Alternative explanations

The supplement does not prove exclusion of simpler alternatives, but it does predeclare the alternatives and controls:

- mobility-edge/Ioffe-Regel controls;
- onsite disorder;
- oxygen-vacancy proxy;
- finite-size and batch controls;
- Srivastava-style orbital-overlap baseline;
- degree-preserving rewired graphs;
- randomized O-O defect positions;
- leave-one-composition/family-out tests.

Pass at protocol level. Not validated until executed.

### Q6.5 Landing check

The supplement identifies the absence of real same-sample external-label validation and gives landing targets. Because it does not claim the blank is already solved, this is not a landing-missing blocker.

However, the landing is not yet complete. It is a protocol and data-acquisition plan, not a validated result.

## Verdict

Status: warning.

Reason: the supplement passes the requested GATE 1.5 checks as a protocol/synthetic-benchmark document. It has the required two layers for both `deepening_1` and `deepening_2`, no visible dimensional contradiction, no internal direction reversal, and no blocking circular validation claim. The remaining warnings are implementation constraints: keep attack signs separated, prevent target leakage into the mobility-edge baseline, and never promote synthetic graph-rule recovery to physical validation.

--- 投喂下一步 ---

必须修正（阻断级）:
1. None for this supplement, as long as it remains protocol/synthetic benchmark only.

建议修正（警告级）:
1. Separate targeted attack sign conventions: attacking high-value conductive edges should reduce residual mobility/Drude/ridge coherence, while removing harmful O-O damage motifs may increase it.
2. Enforce baseline isolation: mobility-edge/Ioffe-Regel-only controls must not include graph attack masks, graph residuals, `V_e`, `V_target`, or target-derived Hall quantities when predicting Hall targets.
3. Label all `H_graph`, `Y_proxy`, synthetic generator, and graph-rule recovery results as diagnostic/synthetic only.
4. Before any validation claim, produce the locked same-sample table with external Hall/Drude/Wannier/spectral labels, provenance flags, negative controls, and leave-one-family/composition-out tests.
--- 
