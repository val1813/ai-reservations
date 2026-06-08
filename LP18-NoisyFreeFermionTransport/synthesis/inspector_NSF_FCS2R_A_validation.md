# INSPECTOR-A Report: NSF-FCS-2R validation A

**Object:** `current\A\NSF-FCS-2R_validation_A.md`  
**Inspector:** NSF-FCS-2R validation INSPECTOR-A  
**Date:** 2026-06-03  
**Constraint:** did not read `current\B` for this round.

## Q1. 量纲校对

A 文件没有新增有量纲物理公式；其核心公式均在 ledger 的 dimensionless Markov-affinity convention 内陈述。

关键公式逐项：

1. `R2 = lambda_T'' - 2G_T`
   - 左边 SI/ledger 单位：dimensionless residual in ledger convention.
   - 右边：`lambda_T''` dimensionless response curvature; `G_T` dimensionless conductance-like ledger coefficient; `2G_T` dimensionless.
   - 匹配：通过。

2. `R2 = C_L(alpha) delta^2 + D_L(alpha) delta^4`
   - 左边：dimensionless residual.
   - 右边：`delta` is density contrast and dimensionless; therefore `C_L,D_L` dimensionless in the ledger convention.
   - 匹配：通过。

3. `R2(delta,A)=C_L delta^2 + E_L A^2 + H_L delta^2 A^2 + O(delta^4,A^4)`
   - 左边：dimensionless residual.
   - 右边：`delta` and `A` are dimensionless perturbation coordinates in the ledger scans; coefficients are dimensionless.
   - 匹配：通过。

4. `R2/G_T`, `Qhat~L^{1/2}`
   - `R2/G_T` is dimensionless/dimensionless.
   - `L` is a site count; `L^{1/2}` dimensionless as finite-size index scaling.
   - A uses both only as downgrade targets, not as asserted formulae.
   - 匹配：通过。

Transcendental arguments: A 文件中未使用 `exp`, `sin`, `log`, `sinh` 等函数。

## Q2. 符号/方向校对

1. `C_L(alpha)>0` in all tested cells:
   - Source check: `nsf_fcs_2R_coeff_fit_summary.csv` gives `C_L` from `0.0700926580` to `0.1375468422`, all positive for `L=4..7`, `alpha=0.5,1.0`.
   - Direction: correct.

2. Density bias leading term is `delta^2`:
   - Limit check: `delta -> 0` gives `R2 -> 0` with positive quadratic leading coefficient; sign is even under `delta -> -delta` as phrased.
   - Direction: correct within tested centered-density convention.

3. Equal-density `nonLDB_site_skew` is even in `A`:
   - Source check: fitted `c_A2` is `0.00384197..0.0130007`, while `c_A` is only about `1e-10..6e-9`; `A=+a` vs `A=-a` differences are about `1e-9` or below.
   - Limit check: `A -> 0` gives residual returning to baseline; sign flip leaves leading term unchanged.
   - Direction: correct.

4. `reversible_side` is equilibrium floor but not strict NESS separability null:
   - Source check: equal-density parity summary has floor-scale coefficients; mixed separability summary has reversible interaction up to about `3.23e-5`, relative to mixed about `5.88e-2`.
   - Direction: correct.

No direction reversal found.

## Q3. 循环论证校对

A 文件 is a validation/reframing note and does not present a new numerical validation generated from its own assumptions. Its numerical statements trace to independent ledger CSV/synthesis artifacts:

- coefficient extraction: `current/plan/nsf_fcs_2R_coeff_fit_summary.csv`;
- activity parity: `current/plan/nsf_fcs_2R_activity_parity_fit_summary.csv`;
- mixed separability: `current/plan/nsf_fcs_2R_mixed_separability_summary.csv`.

The main risk is not circular proof, but that the proposed next theorem in lines 78-80 says odd terms vanish by "tested" symmetries. A correctly promoted theorem still needs an analytic generator-symmetry derivation, which A itself lists in lines 84-85. Therefore this is not a blocking circularity, but must remain a next-step requirement.

## Q4. 数量级鸿沟标记

Checked explicit orders in A and sources:

- `C_L` values are `~7e-2..1.4e-1`.
- nonLDB `c_A2` values are `~4e-3..1.3e-2`.
- nonLDB odd terms are `~1e-9`, about 6-7 orders below the even term.
- reversible equal-density residual floor terms are `~1e-7..1e-9`.
- mixed nonLDB additive residual is `~1e-8`, relative `~1e-4`.
- mixed reversible interaction is `~3e-5`, relative `~6e-2`.

No >10-order unexplained magnitude jump inside A's active claims. The large odd/even separation is explicitly interpreted as parity/numerical-floor behavior and is acceptable.

## Q5. 代数/数值来源校对

### Q5a. 代数展开

`R2 = C_L delta^2 + D_L delta^4` is a fit ansatz, not an analytic expansion proven in A. A correctly treats it as finite-volume coefficient extraction and asks for analytic derivation before theorem promotion.

`R2(delta,A)=C_L delta^2 + E_L A^2 + H_L delta^2 A^2 + O(delta^4,A^4)` is proposed as a next proposition. This is plausible from parity, but not yet derived. A marks it as "next" and asks to derive absence of `delta`, `A`, and `delta A`; no blocking algebra error.

### Q5b. 极限退化

- `delta -> 0`, `A=0`: `R2 -> 0` in the finite-fit ansatz, consistent with equilibrium floor.
- `A -> 0`, equal density: nonLDB contribution returns to baseline/floor.
- `A -> -A`: proposed even response unchanged; source parity scan supports this.
- `L` large/asymptotic: A explicitly refuses to infer asymptotic scaling from `L=4..7`.

### Q5c. 数值量级验证

Spot checks:

- `C_L>0` all cells: verified from CSV.
- nonLDB even response at `A=0.10`: with `c_A2~0.004..0.013`, contribution scale `c_A2 A^2 ~ 4e-5..1.3e-4`, matching mixed/source magnitudes.
- reversible mixed relative effect: max interaction `3.2267e-5` over mixed `5.4855e-4` gives `5.88e-2`, matching synthesis.
- nonLDB mixed relative effect: max interaction `6.7503e-8` over mixed `6.4621e-4` gives `1.04e-4`, matching synthesis.

Numerical claims are within stated order and provenance.

### Q5d. 来源级别

A gives DOI-level literature references for standard framework, but those references are being used for coverage-risk framing. Per user instruction, I did not perform先发 REVIEWER审查.

For ledger numbers, A gives qualitative statements and points through Scope Read to synthesis files, but it does not cite the actual CSV paths next to each numerical claim. This is not blocking because A is a validation note, but next-round theorem/proposition text should include script, CSV, parameter window, and fit source when promoting numerical values.

## Q6. 综合判定

No blocking量纲、方向、循环论证、数量级、代数或数值来源错误 found in A's active claims.

Warnings:

1. A is not formatted as an INSPECTOR report; it is a standard-framework validation/reframing note. This is acceptable as the object under inspection, but PI should not treat A itself as satisfying Q1-Q6.
2. Lines 78-80 should remain a proposed next proposition, not a theorem, until the finite generator symmetry derivation is actually supplied.
3. Numerical provenance is adequate through synthesis references but should be inlined when claims are promoted.

## Q6.3 声张缩水检查

A explicitly shrinks the claim:

- from asymptotic `Qhat~L^{1/2}` / exponent language to finite-volume coefficient/parity ledger claim;
- from proven `R2/G_T` normal curvature to curvature-like diagnostic unless metric/projection is defined;
- from symmetric separability to asymmetric separability with reversible-side NESS renormalization;
- from generic FDT violation discovery to ledger-conventional finite-volume residual response.

This shrinkage is real and properly marked. It should be carried forward as a deliberate downgrade, not silently re-expanded.

## Q6.4 替代解释检查

A explicitly raises the simpler alternative explanation in line 51: observed `C_L`, `A^2`, and additivity may follow from symmetry plus local detailed-balance bookkeeping rather than a new transport mechanism. A also proposes a symmetry-derived coefficient theorem as the next minimal step.

Status: pass for validation-stage framing. Next round must answer this alternative by deriving the symmetry constraints and identifying what, if anything, exceeds standard bookkeeping.

## Q6.5 落地计算检查

No "blank without landing" found. A's finite-window statements are grounded in already generated ledger files for `L=4..7`, `alpha=0.5,1.0`, density windows `delta=0.02..0.08`, activity windows `A=±0.05,±0.10`, and mixed `delta=0.04,A=±0.10`.

The only under-landed item is the proposed expanded mixed fit over more `delta,A` values, which A correctly labels as minimum next work rather than completed evidence.

## Verdict

Verdict: PASS

--- 投喂下一轮 ---
必须修正（阻断级）:
1. 无。

建议修正（警告级）:
1. 保持 A 的降级边界：不得把有限窗口 coefficient/parity diagnostic 重新写成 asymptotic scaling、universal FDT anomaly 或 proven geometric curvature。
2. 若采用 `R2(delta,A)=C_L delta^2 + E_L A^2 + H_L delta^2 A^2 + O(delta^4,A^4)`，必须先给出 finite Markov generator symmetry derivation，特别是说明 `delta`、`A`、`delta A` 项为何消失。
3. 推广任何数值结论时，在正文内标注 CSV path、script/command family、参数窗口、fit ansatz 和 residual，而不只引用 synthesis 摘要。
4. 显式处理替代解释：这些奇偶性与 additivity 是否只是 left/right symmetry、`A -> -A` symmetry 与 LDB bookkeeping 的结果；若不是，说明新增内容在哪里。
---
