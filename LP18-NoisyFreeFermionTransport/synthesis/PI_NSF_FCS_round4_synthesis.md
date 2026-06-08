# PI NSF-FCS-1 Round 4 综合

## 输入

- A: `current/A/NSF_FCS_round4_A.md`
- B: `current/B/NSF_FCS_round4_B.md` 修正版
- INSPECTOR A: `synthesis/inspector_NSF_FCS_A_round4.md`，警告可继续
- INSPECTOR B: `synthesis/inspector_NSF_FCS_B_round4.md` 初检阻断
- INSPECTOR B recheck: `synthesis/inspector_NSF_FCS_B_round4_recheck.md`，通过，带实现警告

## 汇合判断

**类型：原始命题 kill + transport 版本 conditional keep。**

Round 4 解决了一个比原北极星更重要的定义问题：如果 `Q_R(t)` 被定义为单粒子层面的 bare right-reservoir exchange current，那么它是 occupation coboundary。对 `q_R(R,x)=+1`、`q_R(x,R)=-1`，取 `psi(R)=1`、`psi(x)=0`，有

`q_R(i,j)+psi(j)-psi(i)=0`,

因此

`Q_R(t)=psi(X_0)-psi(X_t)`,

有限状态下长期二阶 SCGF 曲率为

`lambda_R''(0)=0`.

这不是 conductance 标度，而是 observable 选错后的 telescoping。A 的 KILL 判断通过 INSPECTOR 校对；B 的初版也正是因为把右库当作闭合可逆节点而被阻断。

B 修正版把台账改成 open two-terminal transport ledger：状态空间 `Omega_L={e,1,...,L}`，reservoir 是 source/sink rates，不作为闭合可逆节点；计数 current 改为左端 throughput / two-terminal transport current；`G_R=dJ_T/dF|_0` 是 two-terminal affinity 对 transport current 的响应。INSPECTOR recheck 确认原 `0/0` 阻断已解除。

## 当前结论

1. **Kill:** “bare right-reservoir exchange current 的 `lambda_R''` 继承 `G_R` 标度”应停止。该 observable 是 coboundary，长期 FCS 二阶曲率为零或无 transport 含义。
2. **Conditional keep:** 只有把 observable 改成 two-terminal transported current，NSF-FCS-1 才有可研究版本：

   `lambda_T''(0) ?~ G_R(L)`.

3. 该 transport 版本仍未证明。A/INSPECTOR 给出的严格状态是：`D_R(L)` 是 capacity Dirichlet energy 的 reservoir-edge 非负部分，方向上有 `D_R <= Cap(R,0)`（至多差固定归一化因子），但 `D_R asymp Cap` 不能由 Dirichlet 原理自动推出，必须保留为未证 lemma。
4. 数值台账的硬门：bare/coboundary observable 必须输出 `INVALID_BARE_EXCHANGE_NOT_TRANSPORT`，不得进入 keep/kill；transport ledger 只有在 `G_R` 与 `lambda_T''` 都稳定后，才能用 `S_T=lambda_T''/G_R` 做科学判断。

## 对北极星的重写

旧版本：

> fractional long-jump exclusion 的 right reservoir-current FCS：`lambda_R''(0)` 是否继承 boundary conductance 标度？

重写后：

> fractional long-jump open transport 中，two-terminal transported current 的 `lambda_T''(0)` 是否与 fractional conductance `G_R(L)` 同标度；等价地，Poisson corrector residual 是否满足可验证的 capacity lower/upper control？

这不是小修正，而是 observable 层面的降级与重命名。继续研究必须使用 transport current；bare exchange 方向关闭。

## 下一步

优先级最高的下一步不是继续 A/B 抽象推导，而是落地一个最小 two-terminal transport ledger：

1. `build_rates -> stationary -> poisson -> tilted -> G_R -> ledger_row -> decide`
2. 强制输出 `observable_kind`；若为 bare exchange/coboundary，直接 `INVALID_BARE_EXCHANGE_NOT_TRANSPORT`
3. 对 two-terminal transport current 输出 `lambda_T''`、`G_R`、`S_T`
4. 若台账 valid 且 `S_T` 跨 tail realization 收敛，transport 版本 keep 到 many-particle / analytic lemma 阶段
5. 若 `S_T` 分叉、幂漂移或对数漂移，kill transport 版本

## 轮次状态

N=4 for NSF-FCS-1。原始 bare-exchange 北极星已被 kill；transport-FCS 改写版 conditional keep。下一步应登记为同一北极星的重写子题，或在队列中将 bare 版本标记关闭、transport 版本保留。
