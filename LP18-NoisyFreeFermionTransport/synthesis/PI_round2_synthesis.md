# PI Round 2 综合

## 输入

- A: current/A/round2_A.md
- B: current/B/round2_B.md
- INSPECTOR A: synthesis/inspector_A_round2.md，警告通过
- INSPECTOR B: synthesis/inspector_B_round2_recheck.md，通过

## 汇合判断

**类型：主线/副线分化。**

A 给出严格度更高的主线：在 `gamma sum_j D[n_j]` 规范下，强退相干投影给出

`r_jk = 2 |J_jk|^2 / gamma_phi`。

因此一维 `J(r)~r^-alpha` 投影为 `r(r)~r^-2alpha`。二阶矩有限当且仅当 `alpha>3/2`；`alpha=3/2` 是一维未归一化 bulk power-law hopping 的二阶矩阈值。d维推广为 `alpha>(d+2)/2`。这是目前最可靠、最可发表的增量。

B 的 holonomy 方向保留为副线，但降级为待检假设：二阶 Zeno population generator 只含 `|J_l|^2`，可能吃掉 Peierls 相位；真正 holonomy FCS 项可能需要更高阶闭合路径。B 的可取之处是给出清楚判据：偶性、周期性、`theta=0` 退化，以及扣除 `D_eff` 后高阶 cumulant/FCS 残差。

## 当前核心命题

R1 的 Q-SSEP/SSEP 普适性边界可以精确改写为：

> 强退相干投影后的有效排斥跳核若有有限二阶矩，则 leading large-L transport CGF 仍可能属于普通 SSEP/MFT；若跳核二阶矩发散，则 hydrodynamic generator 进入 fractional long-jump exclusion，普通 SSEP 的 `lambda''(0)~L^-1` 标度不再是正确 leading 标度。

## Round 3 任务

本轮不再扩散到新方向，直接做可判定量。

1. A/B 共同目标但保持独立：围绕 current variance/conductance scaling。
2. A 路：从 classical long-jump exclusion / fractional Fick law 文献给出 `lambda''(0)` 或 boundary conductance 的标度。必须固定 observable 为 reservoir current，不能泛称所有 cut-current。
3. B 路：设计最小数值判据，把 A 的 `alpha` 标度与 B 的 holonomy 残差分离。若无法证明 holonomy 阶数，就给出“如何击毙 B 副线”的实验/数值流程。

## 状态

N=2<3，未触发硬停止。按 SOP 进入 Round 3。

