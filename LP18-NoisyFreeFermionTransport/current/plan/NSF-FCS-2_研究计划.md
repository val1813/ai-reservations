# NSF-FCS-2 研究计划

## 北极星

研究 long-jump open exclusion 在 NESS 背景下的 FDT residual:

`R2(L)=lambda_T''(L)-2G_T(L)`

目标是判断 `R2` 是否携带 reservoir-tail / fractional conductance 的新标度，而不是 equilibrium FDT 的自动 corollary。

## Round 1 命题

### A 轨道

任务：建立 near-equilibrium NESS 展开。

需要回答：
- `R2` 对 density bias 的首个非零阶是否必然是 `delta^2`。
- `R2` 的 `L` 指数能否写成 McLennan correction、traffic/frenetic term 或三点响应函数的标度。
- 现有数值斜率 `alpha=0.5 -> 1.009`, `alpha=1.0 -> 0.621`, `alpha=1.5 -> 0.279` 是否有容量/Green 函数解释。

### B 轨道

任务：设计 falsifier/stress test。

需要回答：
- 扩大 `L` 或选择代表性 alpha 后，`R2` 斜率是否稳定。
- 反向 density bias 是否给出相同 `R2`。
- non-LDB/activity forcing 是否产生不同于 thermodynamic NESS residual 的 kinetic residual。
- 是否应转向 `R2/G_T`、`R2/J0^2` 或三阶 cumulant 作为更干净的诊断量。

## 当前最小判据

KEEP:
- `R2` 非零；
- 对 `delta` 二次；
- 对 `L` 的斜率按 alpha 分组稳定；
- 至少一个 analytic response 机制能解释二次幅度和符号。

KILL / downgrade:
- `R2` 被证明只是 finite-size numerical artifact；
- `L` 增大后斜率漂移到无 alpha 分辨率；
- non-LDB/activity forcing 才是唯一稳定 residual，density-bias NESS 不携带 reservoir-tail 标度。
