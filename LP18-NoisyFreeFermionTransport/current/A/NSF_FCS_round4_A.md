# NSF-FCS-1 Round 4 - A博士

角色：A博士（学院派）。本轮只读取 A 侧历史、PI 综合、Inspector A 与当前状态文件；未读取 `current/B`，未读取 B Round 4 输出。按 PI 收窄任务，本轮不做大范围文献综述，只做单粒子 long-jump reservoir 最小模型的 Poisson/capacity test。

## 0. 最小模型定义

取 bulk sites `1,...,L`，右 reservoir 记为 `R`。右端距离

`d_R(x)=L+1-x`.

未缩放 right-reservoir long-jump contact 取

`r_R(x)=kappa d_R(x)^(-alpha)`,  `kappa>0`,

并允许右库既 source 又 absorbing：

- `R -> x` 速率 `rho_R r_R(x)`，计数增量 `q_R=+1`;
- `x -> R` 速率 `(1-rho_R) r_R(x)` 或在单 walker 对称网络里取同一 conductance `r_R(x)`，计数增量 `q_R=-1`.

为把 Poisson corrector 和 capacity 联系起来，还需要一个远端 Dirichlet sink/source（例如左端 `0` 或左 reservoir）来定义“真正穿过系统”的 conductance。若没有这个远端端点，只含 `R` 与 bulk 的净交换 current 是单粒子占据数的边界项，长期 SCGF 二阶严格为零；这一点是本轮的关键失败点之一。

## 1. 未缩放 activity `A_R(L)`

定义右库总 jump activity 尺度

`A_R(L)=sum_{x=1}^L r_R(x)=kappa sum_{d=1}^L d^(-alpha)`.

于是

- `alpha>1`: `A_R(L)=kappa zeta(alpha) - kappa L^(1-alpha)/(alpha-1) + O(L^(-alpha)) = O(1)`;
- `alpha=1`: `A_R(L)=kappa log L + O(1)`;
- `0<alpha<1`: `A_R(L)=kappa L^(1-alpha)/(1-alpha)+O(1)`.

NSF-FCS-1 先前讨论的未缩放 fractional reservoir 主要落在 `alpha>1`，因此单粒子层面的 reservoir attempts 是 `O(1)`，不是 `O(G_R(L))`。若最终 `lambda_R''` 仍然是 `G_R(L)->0`，它必然来自 Poisson corrector 的强 screening，而不是 activity 本身小。

--- INSPECTOR_CHECK ---
[公式] `A_R(L)=kappa sum_{d=1}^L d^(-alpha)`；`alpha>1` 时 `A_R(L)=kappa zeta(alpha)+O(L^(1-alpha))`，单位为 `s^-1`。  
[方向] 未缩放 reservoir tail 的 microscopic activity 一般不随 `G_R(L)` 变小；这保留 Round 3 的 fast-boundary 型 cancellation 压力。  
[数据] 本轮只使用指定 A/PI/Inspector 文件中的模型设定与手算渐近。  
[假设] `r_R(x)=kappa d_R(x)^(-alpha)` 没有额外乘上 `L` 依赖 prefactor；若有额外缩放，本结论要改判为 slow-boundary 型。

## 2. Poisson corrector 与 harmonic potential

先看只含右库的闭合单粒子链。令 `Q_t` 计数所有 `R <-> bulk` 跳的净数，`q_R(R,x)=+1`，`q_R(x,R)=-1`。取

`psi(R)=1`,  `psi(x)=0`.

则对任意 reservoir edge：

`q_R(i,j)+psi(j)-psi(i)=0`.

所以

`Q_t = psi(X_0)-psi(X_t)`,

是严格 bounded coboundary，长期二阶 SCGF 为

`lambda_R''(0)=lim_{t->infty} t^(-1) Var(Q_t)=0`.

这不是 `G_R(L)`，除非把相应 conductance 也定义为零。因此，“只数右库净交换”的单粒子最小模型直接 KILL `lambda_R''~G_R` 的强命题。

要得到非零 transport conductance，必须把远端吸收/源接入模型。例如加左端 Dirichlet target `0`，bulk 内部为最近邻或 long-jump symmetric walk。令 `u(x)` 是 equilibrium potential：

`u(R)=1`, `u(0)=0`, `L_bulk u=0` in `1,...,L`,

其中 reservoir edges 的 Dirichlet form 包含 `r_R(x)(u(R)-u(x))^2`。对从 `R` 注入到 `x` 的 jump，Poisson/capacity corrector 的 residual 不再是 `1`，而是

`q_R + Delta phi ~= 1-u(x)`

或等价地取相反号约定时为 `u(x)`。它的含义是：粒子从 landing site `x` 出发，先到远端 sink 而非马上被右库重吸收的 harmonic escape probability。

于是 reservoir-edge residual Dirichlet contribution 是

`D_R(L)=sum_{x=1}^L r_R(x) [1-u(x)]^2`

（若用相反 current 约定则写成 `sum_x r_R(x) u(x)^2`，数量级相同但边界值互换）。整体 capacity/conductance 为

`Cap(R,0)=E(u,u)`

且在单粒子 reversible network 中有 Thomson/Dirichlet 原理：

`G_R(L) = Cap(R,0) = inf_{v(R)=1,v(0)=0} E(v,v)`.

因此可证 lemma 的正确形式不是 `A_R(L)~G_R(L)`，而是：

**Lemma candidate.** 对上述单粒子 reversible network，若 `phi` 取为与右库 current 对应的 Poisson corrector，则 reservoir jump residual 满足

`D_R(L)=sum_{x=1}^L r_R(x)(q_R+Delta phi)^2 <= Cap(R,0)=G_R(L)`

或至少 `D_R(L) asymp G_R(L)`，前提是 residual 的符号约定与 equilibrium potential 一致，且 bulk Dirichlet energy 不把同阶贡献藏到非 reservoir edges 上。

这个 lemma 是 Round 4 后续是否 KEEP 的核心；它不是由 `A_R(L)` 自动推出的。

--- INSPECTOR_CHECK ---
[公式] 闭合右库模型：`q_R+Delta psi=0`，故 `lambda_R''(0)=0`。带远端 Dirichlet sink 时：`D_R(L)=sum_x r_R(x)[1-u(x)]^2`，`G_R(L)=Cap(R,0)=inf E(v,v)`，单位均为 `s^-1`。  
[方向] corrector residual 的物理对象是 harmonic escape probability；它和 capacity 同阶需要单独 lemma，而不是由 reservoir activity 推出。  
[数据] 手算单粒子 Markov chain/coboundary 与 reversible network Dirichlet 原理。  
[假设] 网络可逆或至少可用对称 conductance 表示；远端 sink/source 被明确加入。没有远端端点时 `G_R` 没有非零 transport 含义。

## 3. 对 `lambda_R''~G_R` 强命题的判断

本轮判断分两层。

**KILL：原始强命题。** 如果 `lambda_R''` 指右 reservoir 与 bulk 的净交换 current，且单粒子模型只有右 reservoir absorbing/source contact，那么

`lambda_R''(0)=0`

是严格 coboundary 结论。这既不是 `A_R(L)`，也不是先前候选的非零 `G_R(L)`。因此“单粒子右库净交换 FCS 自动继承 `G_R` 标度”的强命题应 KILL。

**CONDITIONAL KEEP：改写后的 transport 命题。** 若 `lambda_R''` 改为右库注入后真正通过到远端 sink 的 transported current，或等价地模型显式包含左端 Dirichlet reservoir，那么可 KEEP 一个弱化命题：

`lambda_transport''(0) asymp D_R(L) asymp Cap(R,0)=G_R(L)`.

但这依赖一个尚未证明的 lemma：Poisson corrector 在 reservoir long-jump edges 上的 residual 等于或同阶于 harmonic escape probability，并且 residual Dirichlet energy 没有被 bulk-edge contribution 改变主阶。若该 lemma 失败，则多粒子 exclusion 中继续声称 `lambda_R''~G_R` 没有基础。

## 4. 深化1：本轮结论的下一层后果

第一层后果：NSF-FCS-1 必须先固定被计数 current 的物理定义。右库净交换 current 在单粒子层面是 occupation coboundary；transport current 才可能有非零 capacity 标度。若 PI 后续沿用 `lambda_R''~G_R`，文件中必须把 `lambda_R''` 改名或定义为 transported/right-to-left current，而不是 bare right reservoir exchange current。

第二层后果：数值台账不能只输出 `lambda_R''` 和 `G_R`。它必须同时输出 `A_R(L)`、`D_R(L)=sum_R c(q+Delta phi)^2`、bulk Dirichlet energy、以及 `Cap(R,0)`。若 `A_R=O(1)` 但 `D_R~G_R`，说明 strong screening 成立；若 `D_R=0`，说明数的是 coboundary；若 `D_R` 与 `Cap` 不同阶，说明 harmonic/capacity lemma 失败。

第三层后果：对 `alpha>1` 的未缩放 tail，`A_R(L)=O(1)` 仍然成立，所以任何非零小量 `G_R(L)` 都必须来自 escape probability 的小量。直观上，深落点 `x` 的 reservoir jump 并不自动贡献一个单位 current；它只贡献“先到远端而非回右库”的概率权重。

## 5. 深化2：最可能出错的前提

第一层风险：本轮把 Poisson corrector residual 识别为 equilibrium potential residual。这在 reversible 单粒子网络中自然成立，但在非平衡 source/sink 或非对称 long-jump kernel 中未必逐字成立；此时需要解真正的非自伴 Poisson 方程，而不能只引用 Dirichlet 原理。

第二层风险：`D_R(L) asymp Cap(R,0)` 可能只给出整体 energy 同阶，而 reservoir-edge 部分 `D_R(L)` 可能不是 capacity 的主导部分。如果 bulk-edge Dirichlet energy 主导，则 reservoir residual 不足以单独代表 `G_R`，Round 3 的 `D_R=O(G_R)` 仍可成立，但 `D_R~G_R` 的强版本会失败。

第三层风险：多粒子 exclusion 的 current 不是单粒子 harmonic measure 的简单叠加。即使单粒子 transport 命题 KEEP，也只能说明强命题没有在最小层面被 kill；要升级到 exclusion FCS，还必须证明 occupation-dependent rates 下的 corrector residual 保持同一 capacity 标度。

硬边界：本轮没有证明 conditional lemma；只完成了单粒子最小模型的二值判断。原始 bare right-reservoir exchange 版本 KILL；加入远端 transport 定义后的 capacity 版本 CONDITIONAL KEEP。

## 本轮输出格式

本轮成果：构造了 bulk `1..L` 加 right reservoir 的单粒子 long-jump 最小模型。未缩放 `r_R(x)=kappa(L+1-x)^(-alpha)` 给出 `A_R(L)=kappa sum_{d=1}^L d^(-alpha)`，特别是 `alpha>1` 时 `A_R(L)=O(1)`。只数右库净交换时，`q_R` 是 occupation coboundary，`lambda_R''(0)=0`，因此 KILL bare `lambda_R''~G_R` 强命题。若显式加入远端 Dirichlet sink/source，则 corrector residual 可解释为 harmonic escape probability，存在 conditional lemma 路线 `D_R(L) asymp Cap(R,0)=G_R(L)`。

新增引用文献：无。本轮按 PI 指令不做大范围文献综述，只使用 Round 3 已建立的 Poisson/carré-du-champ 框架与单粒子 reversible network 手算。

最弱的环节：`D_R(L) asymp Cap(R,0)` 仍是未证 lemma；尤其需要确认 reservoir-edge residual 是否贡献 capacity 主阶，以及非对称 source/sink 下 harmonic potential 是否仍等于 Poisson corrector residual。

下一步计划：让 PI/Inspector 用一个显式矩阵台账同时计算 `A_R`、`lambda_tilt''`、`D_R`、bulk energy、`Cap(R,0)`。若 bare right exchange 的 `lambda_tilt''` 数值非零，应优先检查计数约定或是否隐含加入了左端 sink；若 transport 版本数值显示 `D_R/Cap` 不稳定，则 kill conditional KEEP。

需要 PI 投喂的文献方向：暂不需要新增文献；下一步优先是最小矩阵模型校准与 harmonic/capacity lemma 验算。
