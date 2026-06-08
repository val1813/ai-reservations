# PI NSF-FCS-1 Round 5 综合

## 输入

- A: `current/A/NSF_FCS_round5_A.md`
- B: `current/B/NSF_FCS_round5_B.md`
- INSPECTOR A: `synthesis/inspector_NSF_FCS_A_round5.md`，警告通过
- INSPECTOR B: `synthesis/inspector_NSF_FCS_B_round5.md`，警告通过

## 汇合判断

**类型：equilibrium 二阶 DC 分支降级 + 新问题重定向。**

A 给出标准有限状态 Markov jump process 的 fluctuation theorem / FDT 定位：在 local detailed balance、equilibrium、two-terminal entropy affinity 规范下，

`lambda_T''(0)=2G_T`.

INSPECTOR A 校对通过了核心代数：若本项目使用

`lambda(chi,A)=lim t^{-1} log E_A exp[chi Q_T(t)]`

且 GC symmetry 写作

`lambda(chi,A)=lambda(-A-chi,A)`,

则

`lambda_chichi(0,0)=2 lambda_chiA(0,0)`.

由于 `G_T=partial_A J_T|_0=partial_A partial_chi lambda(0,0)`，得到 `lambda_T''=2G_T`。这解释了 single-particle 与 finite-density ledger 中稳定的 `S_T≈2`。

必须保留的符号警告：当前脚本的正向 affinity 是

`A_ledger=F=eta_R-eta_L`,

并配套左端 out-in 为正的 `Q_T`。A 稿中示例 `logit(rho_L)-logit(rho_R)` 与该脚本规范差一个整体号向；后续引用必须使用 `A_ledger`，或同时翻转 current 正方向。

## 当前结论

1. equilibrium、local detailed balance、zero-frequency、two-terminal transported current 的二阶 FCS 问题已经降级：`lambda_T''~G_T` 不是新定理，而是有限体积 FDT corollary。
2. long-jump reservoir 只决定 `G_T(L)` 的标度；在上述规范内，`lambda_T''(L)` 自动继承同一标度并带系数 2。
3. bare exchange 版本仍关闭；transport 版本在 equilibrium 二阶 DC 层面也应收束，不再作为主攻问题。
4. 真正有价值的 NSF-FCS 后续方向是破坏 FDT 前提或离开二阶 DC：
   - NESS：`rho_L != rho_R`
   - non-LDB 或 activity/frenetic forcing
   - finite-frequency noise
   - higher cumulants / nonlinear response
   - random reservoir 与上述破坏条件组合

## 下一步优先级

Round 6 不应继续重复 equilibrium `S_T≈2`。应先做 Tier 0 sanity，再做 Tier 1 非平衡破坏测试：

1. Tier 0：affinity split sanity。扫 `eta_R=aF`、`eta_L=-(1-a)F`，确认只要 total entropy affinity 与 conjugate current 不变，`lambda_T''-2G_T≈0`。
2. Tier 1A：NESS density bias。设 `rho_L != rho_R`，输出 `J0`、`lambda_T''`、`G_T`、`FDT_residual_R2=lambda_T''-2G_T`。
3. Tier 1B：non-LDB / activity forcing。必须报告 `ldb_mismatch_derivative`；activity forcing 要同时作用正反 rate 才是 time-symmetric barrier perturbation。
4. Tier 2：若 Tier 1 仍平凡，再转向 finite-frequency 或 `lambda_4`。

## 轮次状态

N=5 for NSF-FCS-1。equilibrium transport second cumulant 分支收束；新最高价值议题是 **NESS / non-LDB 下的 FDT residual 是否携带 long-jump reservoir 标度**。
