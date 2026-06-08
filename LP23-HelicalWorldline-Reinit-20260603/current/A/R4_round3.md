# LP23-R4 Round3 A博士报告：Passive/Causal Linear Response Witness Checker

日期：2026-06-03  
角色：A博士（学院派，文献驱动）  
独立性声明：本轮未读取 `current/B` 或 B 路报告；未读取旧 `LP23-螺旋世界线` 目录。输入只使用 `ai/A_AGENT.md`、`synthesis/PI_R4_round2.md`、`current/A/R4_round2.md`、`current/plan/文献库_R4.md`，以及非 B 报告的脚本 `scripts/r4_witness_checker_toy.py` 用于判断 toy checker 的形式边界。

## §0 框架声明

本轮选择的最小物理域是：

**passive / causal linear response of an LTI medium or measurement channel**。

理由是它是 R4 中最小、最干净、最成熟的物理 witness 域：输出空间 \(Y_K\) 可以取有限频点上的响应、阻抗、散射或 susceptibility；合法补列 \(c\) 必须与 residual \(r\) 同属同一观测通道和同一 SI 单位；物理合法性由因果性、被动性、解析性、Kramers-Kronig / Herglotz / positive-real 表示、有限阶实现或凸近似给出。

本轮判定先给出：

**在该最小域内，`W_origin` 可由成熟的 passive realization / Herglotz / positive-real 证书自然给出；`W_nonoracle` 可由预注册、独立校准、blind split / holdout 给出，但这不是新物理证书，而是成熟实验与统计协议。因而 R4 在单域 passive/causal linear response 中应硬停止为新物理命题；若保留，只能降级为“certified passive-response residual linter / witness-validator”工具命题。**

换言之：这里没有保留下一个新的“物理化 witness checker”理论；只有把成熟证书按先后顺序组装进 residual discovery protocol 的工程价值。

## 1. 成熟框架覆盖判据

令有限频点集合为 \(\Omega_K=\{\omega_1,\ldots,\omega_K\}\)，观测输出为

\[
y=(H(i\omega_1),\ldots,H(i\omega_K))\in Y_K .
\tag{R3-1}
\]

候选补列 \(c\in Y_K\) 若声称来自被动线性响应，至少必须给出一个物理来源证书

\[
W_{\rm origin}^{\rm pass}
=({\rm channel},\Omega_K,{\rm units},\mu \ge 0, a,b,{\rm realization\ or\ approximation\ certificate}),
\tag{R3-2}
\]

其中 \(H\) 属于 Herglotz / positive-real 类。标量 Herglotz 形式可写为

\[
H(z)=a+bz+\int_{\mathbb R}
\left({1\over t-z}-{t\over 1+t^2}\right)d\mu(t),
\quad b\ge 0,\quad \mu\ge 0 .
\tag{R3-3}
\]

工程状态空间证书也可用 realization / KYP 型条件表达：存在 \(P=P^\ast\succeq0\)，使得给定 \((A,B,C,D)\) 的 transfer function \(Z(s)=D+C(sI-A)^{-1}B\) 满足 positive-real / dissipativity 条件。有限频采样下，Ivanenko et al. 的 B-spline Herglotz 近似又把正测度密度转成有限维凸优化证书。

因此，在 passive/causal LTI 域中：

- `W_origin` 不是 R4 新造概念；它就是 Herglotz measure、positive-real transfer function、passive realization matrices 或 passive convex approximation certificate。
- `W_causality` 不是新概念；它由上半平面解析性、Kramers-Kronig 关系和支持在因果过去的 impulse response 给出。
- `W_passivity` 不是新概念；它由正实性、正测度、dissipation inequality 或储能函数 \(P\succeq0\) 给出。
- residual 是否可吸收，就是 \(r\) 是否落在预注册 passive-response cone / tangent span / finite approximation space 的白化投影内。

硬停止/降级判据如下：

**硬停止判据 H1：** 若 R4 的合法补列只允许 fixed passive/causal LTI response，则 R4 完全被 passive realization / Herglotz / positive-real / Kramers-Kronig / passive approximation 覆盖；不得宣称新物理 witness checker。

**硬停止判据 H2：** 若补列 \(c\) 的 Herglotz measure、state-space realization、B-spline density 或 kernel 参数是在看到 residual 后拟合出来的，且没有预注册模板、独立校准或 holdout 预测，则 `W_nonoracle` 失败；R4 回到 Round1 的 residual-shaped oracle no-go。

**降级判据 D1：** 若流程能在看到 residual 前固定 passive cone / realization family / bandlimit / model order，并在 residual 后只做投影，则可降级为工具：`PASSIVE_WITNESS_VALIDATOR`。其输出只能是 `ABSORBED / FINITE_LIBRARY_OBSTRUCTION / ILL_POSED`，不能输出 `NEW_PHYSICS`。

**保留判据 S1：** 只有当同一协议同时需要 passive response、EFT operator、measurement nuisance、history kernel、causal identifiability，且任一单域成熟框架无法自然枚举 \(G_W(P)\) 时，R4 才可能保留为跨域工具命题。但本轮选择的最小域没有达到该条件。

--- INSPECTOR_CHECK ---
[公式] (R3-1)--(R3-3)。\(y,c,r\in Y_K\)，单位由测量通道给定，例如 impedance \(Z\) 用 ohm，susceptibility 用相应 SI 响应单位；Herglotz 表示中 \(\mu\) 是非负测度，\(b\ge0\)。  
[方向] passive/causal linear response 的 `W_origin/W_causality/W_passivity` 已有成熟证书；R4 在该单域中应硬停止为新物理命题，最多降级为证书校验工具。  
[数据] 本步使用文献框架与有限频采样形式化；未使用实验数据。  
[假设] 系统是 LTI、被动、因果；观测通道、频段、单位、模型阶数/带宽截断在看到 residual 前已经固定。

## 2. 最小物理 witness schema

在被动/因果线性响应中，最小 schema 不需要 Round2 的全套跨域 tuple，只需要以下 7 项：

```text
W_passive_response(c) = (
  W_pre,
  W_origin,
  W_causality,
  W_passivity,
  W_measurement,
  W_cutoff,
  W_nonoracle
)
```

其中：

- `W_pre`：频段 \(\Omega_K\)、采样网格、模型阶数/带宽、响应类型、单位、允许的 realization family 或 Herglotz approximation family 在 residual 解盲前固定。
- `W_origin`：给出非 residual 来源，例如独立测得的材料参数、已知介质模型、state-space passive realization、Herglotz 正测度或独立校准得到的仪器 transfer function。
- `W_causality`：响应在上半平面解析，或 impulse response 支持在 \(t\ge0\)，或满足 Kramers-Kronig 一致性。
- `W_passivity`：positive-real / Herglotz positivity / dissipation inequality / KYP-LMI / 非负 B-spline measure density。
- `W_measurement`：把该响应映射到 \(Y_K\) 的仪器通道、单位、噪声协方差 \(\Sigma\) 与白化规则。
- `W_cutoff`：有限阶 realization、有限 B-spline knots、有限频带、有限 memory depth 或 rank cap。
- `W_nonoracle`：时间戳、预注册 hash、blind split、独立校准数据 \(D_c\)、holdout 频段/边界条件/通道，要求 \(c\) 生成不依赖 residual 形状。

对应 checker：

\[
\begin{aligned}
{\rm Verify}^{\rm pass}_P(c,W)=&
{\rm Pre}(W_{\rm pre},P)\wedge
{\rm Origin}_{\rm pass}(W_{\rm origin})\wedge\\
&{\rm Causal}(W_{\rm causality})\wedge
{\rm Passive}(W_{\rm passivity})\wedge\\
&{\rm MeasurementMap}(W_{\rm measurement},Y_K)\wedge
{\rm CutoffFinite}(W_{\rm cutoff})\wedge
{\rm NonOracle}(W_{\rm nonoracle}) .
\end{aligned}
\tag{R3-4}
\]

合法列集必须是

\[
G_{\rm pass}(P)=\{c\mid \exists W:\ {\rm Verify}^{\rm pass}_P(c,W)=1\},
\quad
S_{\rm pass}(P)=\operatorname{span}G_{\rm pass}(P),
\tag{R3-5}
\]

而不是 \(G_{\rm pass}(P,r)\)。Residual 只能最后进入

\[
{\rm Obs}^{\rm pass}_P(r)=[r]\in Y_K/S_{\rm pass}(P).
\tag{R3-6}
\]

这个 schema 的关键结论是：**它在单域内没有新增理论。** `Origin_pass`、`Causal`、`Passive`、`CutoffFinite` 都已由成熟响应理论覆盖；`NonOracle` 来自预注册/holdout 的成熟实验协议。R4 的唯一可能新增只是把它们排成“先证书、后 residual 投影”的软件合同。

--- INSPECTOR_CHECK ---
[公式] (R3-4)--(R3-6)。\(S_{\rm pass}(P)\subseteq Y_K\)，\(r\) 和所有 accepted \(c\) 同单位；白化投影可用 \(\Sigma^{-1/2}\) 转为无量纲 residual norm。  
[方向] 最小物理 schema 可写出，但每个物理子证书均有成熟先发；新增只剩协议顺序与工具封装。  
[数据] 文献结构、有限维响应空间与脚本式 checker 抽象；未用真实实验数据。  
[假设] `W_nonoracle` 的时间戳、blind split 或独立校准可信；若这些记录不可审计，schema 立即退化为事后拟合器。

## 3. 是否跨域仍有新增

本轮结论：**在最小 passive/causal linear response 域内，没有跨域新增。**

若 R4 只处理介质响应、仪器响应或线性历史核，它已经是：

```text
passive realization + Herglotz/positive-real certificate
+ finite approximation
+ independent calibration / holdout model check
```

这不是新物理，也不是新数学。

跨域新增的最低门槛必须比本轮 schema 更强：

```text
operator witness
+ passive response witness
+ measurement witness
+ causal identifiability witness
+ history/nuisance witness
+ shared nonoracle protocol
```

并且要满足两个条件：

1. 任一成熟单域框架都无法枚举完整 \(G_W(P)\)。
2. 组合规则不是研究者为了保留/杀死 residual 事后拼装，而是由实验协议或理论边界自然给出。

目前 Round2/Round3 资料尚未给出这样的自然跨域对象。因此 A 路判定为：**R4 物理命题硬停止；可降级为跨域 residual-linter 工具，但该工具仍需真实预注册 schema 与 holdout 验证。**

## 4. B 路若只给 toy checker 的判定

我只检查了非报告脚本 `scripts/r4_witness_checker_toy.py` 的结构。该 toy checker 做了有用但有限的一件事：它要求候选列携带 source、support locality、protocol order、passive/decaying history kernel、preregistration，并拒绝 `SourceKind.ORACLE` 的 residual-shaped column。

若 B 路 Round3 只给类似 toy checker，则判定如下：

```text
verdict = DOWNGRADE_TO_TOY_VALIDATOR
not     = PHYSICAL_WITNESS_CHECKER_SURVIVES
```

原因：

- toy checker 的 `LOCAL_STENCIL` / `HISTORY_KERNEL` / `ORACLE` 是手写枚举类，不是 passive realization、Herglotz measure、EFT operator basis 或真实测量校准来源。
- toy 的 `preregistered=True/False` 是布尔标签，不是可审计的 timestamp、hash、blind split 或独立校准记录。
- toy 的 `passive_decaying_kernel` 只检查非负且单调衰减，不等价于成熟的 causal/passive linear response certificate。
- toy 没有 holdout 频段、独立边界条件或第二通道预测；它只能证明“这个脚本拒绝显式 oracle 列”，不能证明“真实物理协议自然生成了非 oracle witness”。

因此 B 路若只给 toy checker，A 路建议 PI 判为：**R4 降级，不保留为物理化 witness checker；若没有真实预注册 passive certificate 与 holdout，则对物理主张硬停止。**

## 5. 深挖1：本轮结论的下一层后果

第一层后果：R4 的目标函数必须从“让 residual 消失/不消失”改成“先枚举证书闭包，再投影 residual”。对于 passive response，第一步应输出：

```text
PassiveSchema.json
calibration_pre.json
realization_or_herglotz_certificate.json
frequency_grid_pre.json
verify_passive_witness.py
holdout_split.json
```

只有这些对象在 residual 解盲前固定，才允许计算 \(S_{\rm pass}(P)\) 和 \({\rm Obs}^{\rm pass}_P(r)\)。

第二层后果：R4 的发表定位应改变。若保留，应写成“certified residual pressure test for proposed physical extensions”，不是“protocol-closure obstruction as new physics”。输出标签应限制为：

```text
ABSORBED_BY_CERTIFIED_PASSIVE_RESPONSE
FINITE_LIBRARY_OBSTRUCTION
NONORACLE_FAILED
ILL_POSED
```

不得输出 `NEW_DEGREE_OF_FREEDOM` 或 `PHYSICAL_OBSTRUCTION_CONFIRMED`，除非另有独立实验/理论证明。

第三层后果：若使用 passive/Herglotz 证书，checker 必须惩罚无限自由度。任意正测度、任意高阶 realization、任意密 B-spline knots 在有限 \(Y_K\) 中很容易吸收 residual。因此 \(W_cutoff\) 不是技术细节，而是硬边界：model order、bandlimit、knot count、smoothness、noise threshold 必须预注册。

## 6. 深挖2：本轮最可能错误的前提

最弱前提是：**`W_nonoracle` 能被自然地物理化。**

`W_origin` 在 passive response 中确实自然：Herglotz measure、positive-real transfer function、state-space realization 或独立介质模型都可作为物理来源。但是 `W_nonoracle` 并不从 Herglotz 定理自动推出。一个事后拟合出的 Herglotz measure 仍可能是 residual-shaped oracle 的平滑版本。它满足被动性和因果性，不代表它独立于 residual。

下一层风险是：`W_origin` 与 `W_nonoracle` 会被错误合并。正确逻辑必须是：

```text
physical admissibility != non-oracle provenance
```

某列可以是完全 passive/causal 的，却仍然是看过 residual 后构造的；也可以是预注册的，却物理上不 passive。因此 R4 若想活，两个条件都必须独立审计。

再下一层风险是：holdout 也可能被滥用。若 holdout 频段、边界条件或通道是在看到 residual 后挑选的，`W_nonoracle` 仍然失败。真正的 holdout 必须在 `W_pre` 中固定，且预测指标不能由训练 residual 调节。

硬边界：没有可审计预注册、独立校准、blind split 或外部生成机制时，`W_nonoracle` 不成立；此时即使 passive certificate 成立，R4 也只能判为 `NONORACLE_FAILED`。

## 7. 本轮判定

A 路 Round3 判定：

**R4 作为新物理/新数学命题应硬停止。**

**R4 作为工具可降级保留：certified passive/cross-domain witness validator。**

保留条件是：

1. `G_W(P)` 只依赖预注册协议，不依赖 \(r\)。
2. 每个 accepted column 携带成熟物理证书，最小域中就是 passive/Herglotz/positive-real/realization certificate。
3. `W_nonoracle` 由可审计时间戳、hash、blind split、独立校准或 holdout 给出。
4. residual 只在最后用于白化投影和 holdout error 计算。
5. 输出语义降级为有限库压力测试，不能直接宣称新物理。

若 Round3 仍只有 toy checker、手写规则或事后调参，则 R4 对物理主张硬停止；对工具主张也只能算未完成原型。

## 8. 本轮成果

本轮成果：选择 passive/causal linear response 为最小物理域后，`W_origin` 已由 Herglotz / positive-real / passive realization / convex passive approximation 成熟覆盖；`W_nonoracle` 只能由预注册、独立校准、blind split / holdout 成熟协议给出。该域内无新物理 witness checker；R4 应硬停止为物理命题，降级为证书化 residual-linter 工具。

## 9. 新增引用文献

- Hughes, "A theory of passive linear systems with no assumptions", *Automatica* 86, 87-97, 2017, DOI `10.1016/j.automatica.2017.08.017`.
- Ivanenko et al., "Passive Approximation and Optimization Using B-splines", *SIAM Journal on Applied Mathematics*, 2019, DOI `10.1137/17M1161026`.
- Haakestad and Skaar, "Causality and Kramers-Kronig relations for waveguides", *Optics Express* 13, 9922, 2005, DOI `10.1364/OPEX.13.009922`.
- Arlinskii, Belyi, Tsekanovskii, "Realization of Herglotz-Nevanlinna Functions by Conservative Systems", DOI `10.1007/978-3-0348-0667-1_50`.
- Cassier and Milton, "Bounds on Herglotz functions and fundamental limits of broadband passive quasi-static cloaking", DOI `10.1063/1.4989990`, arXiv `1610.08592`.
- Henning, Lu, Melia, Murayama, "Hilbert series and operator bases with derivatives in effective field theories", DOI `10.1007/s00220-015-2518-2`.
- Henning, Lu, Melia, Murayama, "Operator bases, S-matrices, and their partition functions", DOI `10.1007/JHEP10(2017)199`.
- Godfrey and DiStefano, "Identifiability of Model Parameters", DOI `10.1016/B978-0-08-034929-9.50005-4`.

## 10. 最弱环节

最弱环节：`W_nonoracle`。物理合法性证书不能替代来源独立性证书。一个完全 passive/causal 的补列仍可能是看过 residual 后拟合出来的 oracle column。若没有可审计预注册和 holdout，R4 仍被 Round1 no-go 击穿。

## 11. 下一步计划

下一步不建议继续寻找新的物理论证；建议 PI 直接设 gate：

```text
Gate R4-final:
1. 若 B 路只有 toy checker -> R4 降级为 toy validator，物理主张硬停止。
2. 若 B 路给出真实 PassiveSchema/columns_pre/verify/holdout pipeline -> 只保留为工具命题。
3. 若 pipeline 仍从 residual 生成列或调 cutoff -> R4 硬停止。
4. 若 accepted passive columns 有 holdout predictive power 且 residual projection 非零 -> 可写作 certified finite-library obstruction diagnostic，不写新物理。
```

需要 PI 投喂的文献方向：`positive real lemma passive realization certificate`, `Herglotz Nevanlinna realization conservative systems`, `passive approximation convex optimization`, `pre-registration holdout predictive checks residual modeling`, `certified model expansion physical constraints`.
