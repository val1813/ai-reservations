# PI NSF-FCS-1 Round 2 综合

## 输入

- A: current/A/NSF_FCS_round2_A.md
- B: current/B/NSF_FCS_round2_B.md
- INSPECTOR A: synthesis/inspector_NSF_FCS_A_round2_recheck.md，通过
- INSPECTOR B: synthesis/inspector_NSF_FCS_B_round2.md，通过

## 汇合判断

**类型：校正后收敛。**

Round 2 的最大进展不是证明同标度，而是纠正了一个潜在错误：reservoir jump-current 的二阶 FCS 不能写成单纯正的 `H_-1` 二次型。A 修正后的公式为：

`lambda_R''(0)=<a>_pi + 2<B phi>_pi`

并进一步分解为：

`lambda_R''(0)=<a>_pi + 2<h,phi>_pi + 2<C>_pi`，

其中 `L phi=-h`，`h=b-J`，`B=L'_0`，`C` 是 jump-current martingale 交叉项。`2<h,phi>` 是 corrector 的 `H_-1` 部分，但 `2<C>` 可为负并与 activity/corrector 发生抵消。

B 的算法与此兼容：必须分别输出 activity、Green/corrector、交叉/完整二阶项，而不能只看 `G_R(L)`。

## 当前结论

`lambda_R''(0)~G_R(L)` 仍不能升级为定理。要证明它，需要两个层面的控制：

1. `H_-1` / boundary trace 控制 corrector 部分；
2. martingale 交叉项与 activity 的 cancellation 控制完整 jump-current FCS。

因此 NSF-FCS-1 的主问题被进一步精确化：

> 右 reservoir jump-current variance 的 fractional 标度是否由 activity、Poisson corrector 和 martingale cross term 的精细抵消产生？

## Round 3 指令

A：聚焦完整二阶公式的 cancellation。寻找 nearest-neighbor open SSEP 或 slow-boundary SSEP 中已知 current variance 公式，提取 activity/corrector/cross-term 的抵消机制，看能否迁移到 long-jump/fractional reservoir。

B：给出最小矩阵算法时必须输出完整分解：`<a>`、`2<h,phi>`、`2<C>`、总 `lambda''`、`G_R`、`S_R`。如果算法无法得到 `C`，则必须改为直接 tilted generator 二阶数值微分。

## 轮次状态

N=2 for NSF-FCS-1。未硬停止，继续 Round 3。

