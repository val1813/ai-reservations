# PI Round 3 综合

## 输入

- A: current/A/round3_A.md
- B: current/B/round3_B.md
- INSPECTOR A: synthesis/inspector_A_round3.md，警告通过
- INSPECTOR B: synthesis/inspector_B_round3.md，警告通过

## 汇合判断

**类型：收敛。**

A 给出主结论：固定 observable 为右 reservoir current / boundary conductance 后，强退相干投影将 `J(r)~r^-alpha` 映射为 classical long-jump exclusion kernel `r(r)=2J0^2/(gamma_phi r^{2alpha})`，对应 `mu=2alpha-1`。因此：

- `1<alpha<3/2`：boundary conductance 标度 `G_R(L)~(2J0^2/gamma_phi) C_< L^{-(2alpha-2)}`，有 fractional Fick law 强文献支撑。
- `alpha>3/2`：有限二阶矩，`G_R(L)~D_eff L^-1`，是普通扩散强推断。
- `alpha=3/2`：`G_R(L)~(2J0^2/gamma_phi) C_c (log L)/L`，是临界截断二阶矩候选/强推断，不得标为已证。
- 对 `lambda_R''(0)`：同标度是 fluctuation/FCS 层面的额外假设；当前是强推断而非已证。

B 给出副线收敛协议：验证主线时关闭 holonomy (`theta=0`) 或直接用 Zeno-effective real-rate generator。holonomy 只通过 full tilted Lindblad 的 residual `Q(s,theta)` 判定；若扣除 `D_eff` 后无独立偶周期残差，则 B 线击毙。B 线不再与主线竞争。

## 本课题的净增量

原候选 LP-18 “耗散下热输运普适类转变”被重写为更精确的边界命题：

> R1 的 noisy free fermion -> Q-SSEP -> classical SSEP 普适性不是由“自由费米 + 噪声”单独保证，而由 Zeno-projected jump kernel 的二阶矩有限性保证。对一维未 Kac 归一化的 `J(r)~r^-alpha`，边界在 `alpha=3/2`。

这个增量比原 LP-18 更干净：它给出可检验标度、明确前提和先发文献边界。

## 结论等级

**有边界-强推断：** 

- 已可作为主张：`1<alpha<3/2` 时普通 SSEP 的 `L^-1` boundary conductance 标度被 fractional long-jump exclusion 的 `L^{-(2alpha-2)}` 替代。
- 不可作为已证：`lambda_R''(0)` 全 FCS 同标度；`alpha=3/2` 临界 `(log L)/L`；holonomy residual 的具体阶数。

## 下一步

进入北极星收尾：

1. GATE 1.5：检查 A/B 深挖。
2. Re-escalation：把启动声张和最终声张对比。
3. 矛盾深挖：五个为什么追到基础原理层。
4. 更新北极星队列优先级，决定是否切换或收官。

