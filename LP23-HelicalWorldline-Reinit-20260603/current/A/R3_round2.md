# LP23-R3 Round2 A路：QNP-Lint 先发查重与有限维 residual 复形 no-go

角色：A博士（学院派）  
日期：2026-06-03  
独立性声明：本轮只读取 `ai/A_AGENT.md`、`synthesis/PI_R3_round1.md`、`current/A/R3_round1_revised.md`、`current/plan/文献库_R3.md` 及 SOP/Phase 文件；未读取 `current/B`、`synthesis/INSPECTOR_B*`，未读取旧 LP23-螺旋世界线目录。

## §-1 先发查重

检索方式：优先 `paper-search-mcp`，使用 Semantic/CrossRef/OpenAlex/Google Scholar 聚合源；本轮补查四组关键词：

1. `"residual cohomology" inverse problems model misspecification residual diagnostics cohomology`
2. `semiparametric nuisance tangent space orthogonal projection residual model checking misspecification`
3. `inverse problems residual method discrepancy principle model checking nuisance parameters`
4. `Bayesian model checking posterior predictive checks residual discrepancy model criticism`

查重判定：

| 方向 | 代表先发 | 对 QNP-Lint 的覆盖 |
|---|---|---|
| cohomological obstruction / quotient / descent | Bredon, *Equivariant obstruction theory*, DOI `10.1007/bfb0082692`; Fujiki, *Kähler Quotient and Equivariant Cohomology*, DOI `10.1201/9781003419983-4`; Alper-Hall-Rydh, *A Luna etale slice theorem for algebraic stacks*, DOI `10.4007/annals.2020.191.3.1` | “取商后非零类/下降失败才有含义”是成熟语言；QNP-Lint 不能声称发明 obstruction/descent。 |
| inverse problems / discrepancy principle | Colton-Piana-Potthast 1997, DOI `10.1088/0266-5611/13/6/005`; Blanchard-Mathe 2012, DOI `10.1088/0266-5611/28/11/115011`; Aravkin-van Leeuwen 2012, DOI `10.1088/0266-5611/28/11/115016` | “残差是否可由噪声、正则化、nuisance 参数吸收”已是逆问题诊断和参数选择的标准问题。 |
| model discrepancy / calibration / history matching | Kennedy-O'Hagan 2001, DOI `10.1111/1467-9868.00294`; Brynjarsdottir-O'Hagan 2014, DOI `10.1088/0266-5611/30/11/114007`; Vernon-Goldstein-Bower 2010, DOI `10.1214/10-ba524` | 模型结构误差、校准参数、观测误差和模型不足的分解已成熟；QNP-Lint 不能把“扩展模板后残差消失”包装为新原则。 |
| semiparametric nuisance tangent / orthogonal projection | *The Nuisance Tangent Space and Its Orthogonal Complement*, DOI `10.1007/0-387-37345-4_8`; Godambe 1991, DOI `10.2307/2336904`; Chernozhukov-Escanciano-Ichimura-Newey-Robins 2022, DOI `10.3982/ecta16294` | 白化后投影到 nuisance tangent 的正交补是既有半参数效率/局部稳健估计核心工具。 |
| Bayesian/model checking | posterior predictive checks、split/holdout predictive checks；Li-Huggins, *Calibrated Model Criticism Using Split Predictive Checks*, DOI `10.1080/01621459.2026.2649585`; NANOGrav posterior predictive checks, DOI `10.1103/PhysRevD.111.042011` | “用复制数据/残差统计量检查模型拟合”已有完整统计语境；QNP-Lint 若只是 residual check，则是换名。 |

先发结论：精确短语 `QNP-Lint` 和“finite-library residual cohomology linter”没有检索到成熟同名框架；但其四个功能部件已经分别由 obstruction/descent、inverse-problem discrepancy、model discrepancy/model checking、semiparametric nuisance projection 覆盖。因此本轮允许保留的最小增量不是新数学或新物理，而是一个有限库相对的、可复核的负判据协议：在每次合法扩张后重建复形、重算残差类、并给出失败边界。

## §0 框架声明

本轮采用的成熟子领域框架为：

**有限维链复形/上同调 + 逆问题 discrepancy principle + 半参数 nuisance tangent 正交投影 + Bayesian/model checking。**

QNP-Lint 输入不是“一个异常 residual”，而是四元组

\[
\mathcal I=(r,\;D_0,\;D_1,\;\Sigma;\;\mathfrak L),
\tag{R2-0}
\]

其中 \(r\in C^1\simeq \mathbb R^m\) 是观测残差向量，\(D_0:C^0\to C^1\) 是允许吸收方向矩阵，\(D_1:C^1\to C^2\) 是一致性约束矩阵，\(\Sigma\succ 0\) 是残差噪声/不确定度协方差，\(\mathfrak L\) 是有限合法扩张库，包含 template、bridge、nuisance、history 的候选列及其合法性规则。

QNP-Lint 的保守定义：

\[
\mathrm{QNP\text{-}Lint}(\mathcal I)=
\begin{cases}
\mathrm{PASS\_OBSTRUCTION}, & [r^{(j)}]_{D_0^{(j)},D_1^{(j)}}\neq 0
\text{ for all legal }j,\\
\mathrm{ABSORBED}, & \exists j \text{ legal s.t. } [r^{(j)}]=0,\\
\mathrm{ILL\_POSED}, & \text{some required complex/metric condition fails.}
\end{cases}
\tag{R2-1}
\]

这里的 `PASS_OBSTRUCTION` 只表示“未被当前有限库吸收”，不是“发现新自由度”。

## §1 有限维 residual 复形的严谨条件

令

\[
C^0\xrightarrow{D_0}C^1\xrightarrow{D_1}C^2
\tag{R2-2}
\]

为有限维 residual 复形。合法判定至少需要四个条件。

**条件 1：复形条件 \(D_1D_0=0\)。**

这保证 \(\operatorname{im}D_0\subseteq \ker D_1\)，允许吸收方向不会破坏一致性约束。失败边界：

- 若 \(D_1D_0\neq 0\)，则 \(C^\bullet\) 不是复形，\(\ker D_1/\operatorname{im}D_0\) 未定义。
- 若某个 template/history 列 \(u\) 满足 \(D_1D_0u\neq0\)，该列不能作为合法吸收方向；若研究者坚持加入，必须同步重定义 \(C^2,D_1\)，不能沿用旧上同调类。
- 若 \(D_1D_0\) 只在数值容差内近似为零，必须声明阈值 \(\tau_c\)，并把结论降级为数值诊断而非代数定理。

**条件 2：候选残差 \(r\in\ker D_1\)。**

只有一致 residual 才能给出类

\[
[r]\in H^1(C^\bullet)=\ker D_1/\operatorname{im}D_0.
\tag{R2-3}
\]

失败边界：

- 若 \(D_1r\neq0\)，残差违反约束；它不是 obstruction class，而是 inconsistency flag。
- 若 \(D_1r\) 只因观测噪声非零，必须用白化量 \(\|W_2D_1r\|\) 与噪声阈值比较；未给 \(\Sigma_2\) 或阈值时不得判定通过。
- 若 \(r\) 的单位混杂而未白化，\(\ker D_1\) 检查会被尺度任意性污染。

**条件 3：扩张后重算，而不是旧类拉回。**

对每个合法扩张 \(j\in\mathfrak L\)，必须构造

\[
C^{0,j}\xrightarrow{D_0^{(j)}}C^{1,j}\xrightarrow{D_1^{(j)}}C^{2,j},\qquad
D_1^{(j)}D_0^{(j)}=0,
\tag{R2-4}
\]

并把残差更新为 \(r^{(j)}\in C^{1,j}\)，然后重算

\[
[r^{(j)}]\in
H^1(C^{\bullet,j})
=\ker D_1^{(j)}/\operatorname{im}D_0^{(j)}.
\tag{R2-5}
\]

失败边界：

- 若只把旧 \([r]\) 口头称为“在扩张后仍非零”，没有给出 \(D_0^{(j)},D_1^{(j)},r^{(j)}\)，则结论无效。
- 若扩张改变了观测空间维度或单位，必须同步给出嵌入/边缘化映射和新协方差；否则不能比较旧 residual 与新 residual。
- 若有限库 \(\mathfrak L\) 未列明合法扩张的生成规则，`PASS_OBSTRUCTION` 只能解释为“未被作者尝试过的扩张吸收”，没有方法论价值。

**条件 4：白化投影。**

令 \(\Sigma\succ0\)，取 \(W=\Sigma^{-1/2}\)。设 \(A=WD_0\)、\(z=Wr\)。白化正交残差为

\[
\epsilon_\perp
=\{I-A(A^\top A)^+A^\top\}z,
\tag{R2-6}
\]

等价地，

\[
\Pi_{\perp\operatorname{im}D_0}^{(W)}r
=W^{-1}\epsilon_\perp.
\tag{R2-7}
\]

判据：若 \(\|\epsilon_\perp\|\le\tau\)，则在当前复形下 residual 可由允许方向吸收；若 \(\|\epsilon_\perp\|>\tau\)，才进入扩张库压力测试。

失败边界：

- \(\Sigma\) 奇异时必须使用可观测子空间上的伪逆并声明被丢弃的零方差/无限方差方向；否则投影未定义。
- \(D_0\) 病态时 \((A^\top A)^+\) 对阈值敏感，必须报告奇异值截断规则。
- \(\tau\) 若由作者事后选择，QNP-Lint 退化为过拟合诊断；必须预注册或由噪声模型给出。

--- INSPECTOR_CHECK ---
[公式] 本步产生 (R2-0)--(R2-7)。所有量为有限维向量/矩阵；\(r\) 继承观测残差单位，\(W=\Sigma^{-1/2}\) 将其转为无量纲白化坐标，\(\epsilon_\perp\) 为无量纲残差。  
[方向] 把 QNP-Lint 限定为有限库相对的 residual 复形压力测试；若不满足 \(D_1D_0=0\)、\(r\in\ker D_1\)、扩张后重算、白化投影，则不得声称 obstruction。  
[数据] 本步使用 paper-search-mcp 查重与 Round1 A 路符号；未使用实验数据。  
[假设] \(C^i\) 有限维，\(\Sigma\) 至少在可观测子空间正定，合法扩张库 \(\mathfrak L\) 可枚举或有明确生成规则。

## §2 可证伪 no-go

**定理 R2-A（QNP-Lint 换名 no-go）。**  
给定有限维输入 \(\mathcal I=(r,D_0,D_1,\Sigma;\mathfrak L)\)。若存在一个合法扩张 \(j\in\mathfrak L\)，使得：

1. \(D_1^{(j)}D_0^{(j)}=0\)；
2. \(r^{(j)}\in\ker D_1^{(j)}\)；
3. 在白化内积下
\[
\epsilon_\perp^{(j)}
=\{I-A_j(A_j^\top A_j)^+A_j^\top\}z_j=0
\quad
\text{or}\quad
\|\epsilon_\perp^{(j)}\|\le\tau_j,
\tag{R2-8}
\]
其中 \(A_j=W_jD_0^{(j)}\)、\(z_j=W_jr^{(j)}\)；
4. 扩张列 \(D_0^{(j)}\) 全部属于预先声明的 gauge/template/bridge/nuisance/history 合法库；

则该 residual 在 QNP-Lint 下不能声称为新方法识别出的新物理自由度或新 obstruction。它至多是既有 nuisance projection、inverse-problem discrepancy/model discrepancy、或 model checking 框架中的可吸收残差。

证明：由 1 和 2，\([r^{(j)}]\) 良定义。由 3，白化后 \(r^{(j)}\) 到 \(\operatorname{im}D_0^{(j)}\) 的距离为零或低于预设噪声阈值，故 \([r^{(j)}]=0\) 或统计上不可区分于零。由 4，吸收方向不是事后非法添加，而是预注册的合法重参数化/模型扩展/nuisance 方向。于是 residual 的消失完全落在既有投影与模型失配诊断语境内；QNP-Lint 若仍称其为新方法，只是给标准吸收检验换名。证毕。

可证伪方式：给出一个具体扩张 \(j\)，列出 \(D_0^{(j)},D_1^{(j)},\Sigma_j,r^{(j)}\)，并计算 (R2-8)。若 (R2-8) 成立，QNP-Lint 的新颖性主张被击穿。

反向限制：若所有已声明合法扩张均有 \(\|\epsilon_\perp^{(j)}\|>\tau_j\)，只能得到“有限库未吸收”。这仍不是充分的新物理证明，因为可能存在未列入库的物理 bridge、真实边界条件、仪器系统误差或更大模型族。

## §3 深挖1：本轮结论的下一层后果

第一层后果：R3a 不能以“residual cohomology”作为新理论名义发表。精确短语未检索到成熟同名领域，但“残差取商成类”和“被 nuisance/model discrepancy 吸收即非新自由度”的功能已经被多领域覆盖。

第二层后果：若要保留论文价值，题名和摘要必须主动降级为 “finite-library pressure test / linter for theory proposals”。贡献点是负结果自动化，而不是正向发现机制。

第三层后果：实验对象也随之改变。QNP-Lint 不应拿一个真实宇宙 residual 宣称新物理；应拿一组历史失败命题或 toy proposal，演示它们如何被 template/history/nuisance 扩张吸收，或如何在有限库内保留非零类。

## §4 深挖2：最可能错误的前提

第一层风险：把 template、bridge、history 全部放入 \(D_0\) 可能过度保守。某些 bridge/history 列不是 nuisance，而是真实协议、介质响应或边界条件；把它们商掉会误杀物理。

第二层风险：合法扩张库 \(\mathfrak L\) 的边界本身可能是主观的。如果作者为杀死 residual 而事后扩张，no-go 成为过拟合；如果作者为保留 residual 而故意缩小库，`PASS_OBSTRUCTION` 成为选择偏差。

第三层风险：白化协方差 \(\Sigma\) 往往来自同一个模型族。若模型错配已经污染 \(\Sigma\)，则投影距离 \(\|\epsilon_\perp\|\) 可能低估或高估 obstruction。此时必须引入 posterior predictive checks 或 holdout/split predictive checks，而不能只依赖线性代数投影。

硬边界：若没有预注册的 \(\mathfrak L\)、没有可复核的 \(\Sigma\)、没有扩张后 \(D_1D_0=0\) 检查，QNP-Lint 不能产生任何可发表判定，只能作为研究笔记。

## §5 本轮判定

QNP-Lint 不是“完全没有活口”，但活口非常窄：

- 不能声称发明 residual cohomology、obstruction class、nuisance tangent projection、model checking 或 inverse-problem discrepancy。
- 可以声称提出一个有限库相对的审稿协议：任何理论提案若 residual 被合法扩张白化投影吸收，则自动降级为模型失配/参数化伪影。
- 必须把输出语义限制为 `ABSORBED / ILL_POSED / FINITE_LIBRARY_PASS`，避免 `NEW_DEGREE_OF_FREEDOM` 这种过强标签。

本轮成果：[给出 QNP-Lint 的有限维 residual 复形条件、白化投影公式、扩张后重算规则，以及可证伪 no-go 定理 R2-A；判定 R3a 只有作为有限库相对负判据协议才不完全是换名。]

新增引用文献：[Colton-Piana-Potthast 1997 DOI `10.1088/0266-5611/13/6/005`; Blanchard-Mathe 2012 DOI `10.1088/0266-5611/28/11/115011`; Aravkin-van Leeuwen 2012 DOI `10.1088/0266-5611/28/11/115016`; Kennedy-O'Hagan 2001 DOI `10.1111/1467-9868.00294`; Brynjarsdottir-O'Hagan 2014 DOI `10.1088/0266-5611/30/11/114007`; Vernon-Goldstein-Bower 2010 DOI `10.1214/10-ba524`; Chernozhukov et al. 2022 DOI `10.3982/ecta16294`; Li-Huggins 2026 DOI `10.1080/01621459.2026.2649585`; NANOGrav posterior predictive checks 2025 DOI `10.1103/PhysRevD.111.042011`; Alper-Hall-Rydh 2020 DOI `10.4007/annals.2020.191.3.1`.]

最弱环节：[合法扩张库 \(\mathfrak L\) 的客观边界。没有预注册库和白化协方差来源，QNP-Lint 极易在“过度吸收”和“故意不吸收”之间摇摆。]

下一步计划：[建议 Round2 后续让独立检查者只审四件事：\(D_1D_0=0\)、\(r\in\ker D_1\)、每个扩张后是否重算 \([r^{(j)}]\)、白化投影的 \(\Sigma,\tau\) 是否预先给定。若 B 路 toy example 能提供矩阵，则 A 路 no-go 可直接套用；若没有矩阵，R3a 应判为叙述性换名。]

需要 PI 投喂的文献方向：[finite-sample model criticism; holdout predictive checks; semiparametric efficiency under misspecification; discrepancy principle with nuisance parameters; quotient-stack descent obstruction in applied gauge theory.]
