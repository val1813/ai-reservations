# 北极星收尾

## GATE 1.5 深挖检查

**结论：通过。**

grep 输出显示：

- A: round1/round2/round3 均含“深挖1”“深挖2”；round3 的深挖1 包含三层后果，深挖2 包含三层风险。
- B: round1/round2/round3 均含“深挖1”“深挖2”；round3 的深挖1 包含三层结构，深挖2 包含三层推广。

无需补深挖。

## Re-escalation

### 启动声张

“强噪声/热力学极限下，一维带相干自由费米子的全计数输运统计是否真正落入经典 SSEP 大偏差函数，还是存在由相干、长程跳跃、边界或相互作用保留下来的非经典边界项？”

### 被杀死/降级的声张

1. **“所有 noisy free fermion 都 classical SSEP”**：杀死。R1 只覆盖 quasi-local / finite-second-moment effective kernel。
2. **“有限尺寸 quantum correction 是主增量”**：降级。arXiv:2601.16883v1 已推进 QSSEP/QSSIP 的 finite-size correction。
3. **“holonomy 是 leading universality breaker”**：降级。二阶 Zeno population generator 吃掉 Peierls 相位；holonomy 只能作为 full tilted Lindblad residual test。
4. **“alpha=3/2 的 log 标度已证”**：降级。只能作为临界候选/强推断。
5. **“lambda_R'' 与 boundary conductance 同标度已证”**：降级。需要 tilted generator 或 Green-Kubo 验证。

### 更大声张草案

**声张 R：** R1 的 Q-SSEP/SSEP 普适性应由 Zeno-projected jump kernel 的 domain of attraction 分类替代：有限二阶矩 -> ordinary SSEP/MFT；发散二阶矩 -> fractional long-jump exclusion。对一维未归一化 `J(r)~r^-alpha`，边界在 `alpha=3/2`。

## 五个为什么

1. **为什么 R1 的 SSEP 普适性会失效？**  
因为强退相干后得到的有效跳核可能不是短程/有限二阶矩跳核。

2. **为什么有效跳核的二阶矩重要？**  
因为 hydrodynamic generator 的 domain of attraction 由跳分布二阶矩决定：有限二阶矩给 Laplacian，发散二阶矩给 fractional Laplacian。

3. **为什么这会改变 FCS/CGF？**  
因为 CGF 的自然尺度来自穿越系统的边界电导/输运时间；普通扩散给 `L^-1`，fractional Fick law 给 `L^{-(mu-1)}`。

4. **为什么不能只说“量子相干保留/消失”？**  
因为 leading boundary conductance 的失效已经可由 Zeno 后的 classical long-jump exclusion 解释；相干只可能在 finite-size 或 higher-order residual 中重新进入。

5. **为什么这是基础原理层的问题？**  
它把“开放量子系统输运何时经典化”的判据从模型标签（free/noisy）提升到有效生成元的普适类：经典化不等于 SSEP 化，经典化后仍可能落入 fractional nonlocal universality class。

## 优先级队列重算

当前北极星 LP18-NSF-1 三轮完成，结论为 **有边界-强推断**。它的主线已经从选题推进到可写成命题的状态，但未到完整收官；剩余最关键缺口是 `lambda_R''(0)` 的 FCS 层验证。

新候选：

| 编号 | 议题 | 分数 | 理由 | 状态 |
|------|------|------|------|------|
| NSF-FCS-1 | fractional long-jump exclusion 的 reservoir-current FCS：`lambda_R''(0)` 是否继承 boundary conductance 标度 | 8.8 | 直接补齐主线最弱环节，可把强推断升级为准定理/数值判据 | 新最高优先级 |
| NSF-QCORR-1 | fractional conductance scaling 下 QSSEP finite-size quantum corrections 是否从 subleading 被放大 | 8.5 | 连接 R7 新文献与本项目 fractional 主线 | 待评估 |
| NSF-HOL-1 | shortcut holonomy residual `Q(s,theta)` 的 full tilted Lindblad 击毙/保留测试 | 7.4 | 有趣但很可能只是高阶 finite-size correction | 降级副线 |

## 收尾判断

队列存在更高分候选 NSF-FCS-1。按 SOP，应暂停当前北极星的“完整收官”，保存状态并切换到 NSF-FCS-1 作为下一北极星。

