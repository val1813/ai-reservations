# LP23-R3 Round1 A路：Obstruction Class / Quotient Naturality Principle

角色：A博士（学院派）  
日期：2026-06-03  
禁止项：未读取 B 路输出。

## §-1 先发文献检索

检索方式：paper-search-mcp；关键词分四组：

1. `gauge orbit space quotient moduli physical observables gauge invariant obstruction class`
2. `cohomological obstruction class moduli quotient descent equivariant cohomology`
3. `naturality quotient functor invariant physical observable gauge theory natural transformations`
4. `nuisance parameter projection residual model misspecification diagnostic statistical inference`

先发矩阵：

| 风险轴 | 先发框架 | 代表文献 | 对 R3 的覆盖 |
|---|---|---|---|
| gauge/orbit/quotient | 物理量必须降到 gauge orbit/quotient，截面量不是物理量 | Anderson, *Enumeration of the True Observables in Gauge-Invariant Theories*, Phys. Rev. 110, 1197 (1958), DOI: `10.1103/physrev.110.1197`; Orland, *Gauge-invariant coordinates on gauge-theory orbit space*, PRD 70, 045014 (2004), DOI: `10.1103/physrevd.70.045014`; Khavkine, *Local and gauge invariant observables in gravity*, CQG 32, 185019 (2015), DOI: `10.1088/0264-9381/32/18/185019` | “依赖 gauge 截面的 residual 不是新自由度”已被覆盖。 |
| moduli/equivariant quotient | 商空间、同伦商、等变上同调给出在群作用下的自然不变量 | Bredon, *Equivariant obstruction theory*, LNM (1967), DOI: `10.1007/bfb0082692`; Tu, *Homotopy Quotients and Equivariant Cohomology* (2020), DOI: `10.23943/princeton/9780691191751.003.0004`; Fujiki, *Kähler Quotient and Equivariant Cohomology* (2023), DOI: `10.1201/9781003419983-4` | “取商后仍非零的 obstruction class”是成熟语言。 |
| descent/naturality | 对允许变换函子自然的量才可跨表示、截面、背景比较 | Tu, *General Properties of Equivariant Cohomology* (2020), DOI: `10.23943/princeton/9780691191751.003.0009`; Fiorenza-Schreiber-Stasheff, *Cech cocycles for differential characteristic classes*, ATMP 16 (2012), DOI: `10.4310/atmp.2012.v16.n1.a5` | “naturality principle”作为数学要求已覆盖。 |
| anomaly/obstruction in QFT | 非零上同调/异常类作为不能规范化或不能消去的 obstruction | Hsin-Lam-Seiberg, *Comments on one-form global symmetries and their gauging*, SciPost Phys. 6, 039 (2019), DOI: `10.21468/scipostphys.6.3.039`; Benini-Cordova-Hsin, *On 2-group global symmetries and their anomalies*, JHEP 03, 118 (2019), DOI: `10.1007/jhep03(2019)118`; Cordova-Freed-Lam-Seiberg, *Anomalies in the space of coupling constants*, SciPost Phys. 8, 001 (2020), DOI: `10.21468/scipostphys.8.1.001` | “非零 obstruction 可有物理后果”已强覆盖。 |
| nuisance/model misspecification | nuisance 投影、正交化、misspecification 诊断决定 residual 是否只是模型族外误差 | Godambe, *Orthogonality of Estimating Functions and Nuisance Parameters*, Biometrika 78, 143 (1991), DOI: `10.2307/2336904`; Barber-Samworth, *Local continuity of log-concave projection*, Bernoulli 27 (2021), DOI: `10.3150/20-bej1316`; Chernozhukov et al., *Locally Robust Semiparametric Estimation*, Econometrica (2022), DOI: `10.3982/ecta16294` | “被 nuisance/history/template 吸收的 residual 只是诊断量”已覆盖。 |

判定：若 R3 只声称“物理量应 gauge invariant / quotient invariant / obstruction class 非零”，则完全被成熟框架覆盖，死因是同义改写。可保留的最小增量不是新物理自由度原则，而是把 gauge、template、bridge、nuisance、history 五类选择统一为一个可执行的“多商筛选定理/算法”。

## §0 框架声明

本轮采用的成熟子领域框架：

**等变几何 + 商栈/同伦商 + 半参数 nuisance 正交投影。**

对象不是单个残差函数，而是带五类允许选择的资料：

\[
\mathcal D=(X,Y;\mathcal G,\mathcal T,\mathcal B,\mathcal N,\mathcal H),
\tag{A0}
\]

其中 \(\mathcal G\) 是 gauge 群或群胚，\(\mathcal T\) 是 template 扩张族，\(\mathcal B\) 是 bridge/splitting/observer/constitutive map 选择族，\(\mathcal N\) 是 nuisance 方向，\(\mathcal H\) 是 history/memory column 方向。允许选择合成一个群胚或半群胚

\[
\mathfrak A=\langle \mathcal G,\mathcal T,\mathcal B,\mathcal N,\mathcal H\rangle,
\tag{A1}
\]

R3 的目标对象应是 \([\mathfrak A\backslash \mathcal R]\) 上的上同调类，而不是某一截面 \(s\) 下的 residual \(r_s\)。

## 形式化

令 \(\mathcal R\to\mathcal M\) 为 residual bundle，\(\mathcal M\) 是模型/观测协议参数空间。每个截面选择 \(s\) 给出 residual

\[
r_s\in \Gamma(\mathcal M,\mathcal R).
\tag{A2}
\]

允许选择 \(\alpha\in\mathfrak A\) 作用为

\[
r_s\mapsto r_{\alpha s}=\rho(\alpha)r_s+\delta_\alpha q_s,
\tag{A3}
\]

其中 \(\rho(\alpha)\) 是 residual 空间上的表示，\(\delta_\alpha q_s\) 是由 template/bridge/nuisance/history 重新参数化生成的 coboundary 型变化。定义商后 obstruction：

\[
\operatorname{Obs}(r)
  := [r]\in H^k([\mathcal M/\mathfrak A],\mathcal R_{\rho})
  \quad\text{或}\quad
  H^k_{\mathfrak A}(\mathcal M,\mathcal R_{\rho}).
\tag{A4}
\]

则 R3 原则可压缩为：

\[
\operatorname{Obs}(r)\ne 0
\Rightarrow
\text{candidate physical degree of freedom};
\qquad
\operatorname{Obs}(r)=0
\Rightarrow
\text{model-misspecification diagnostic only}.
\tag{A5}
\]

注意：式 (A5) 的反向不成立。非零 obstruction 只是“有资格成为候选自由度”，仍需动力学、耦合、可测量性和反事实预测检验。

--- INSPECTOR_CHECK ---
[公式] 新公式为 (A0)-(A5)。量纲：\(r_s\) 继承观测量残差单位；\(\operatorname{Obs}(r)\) 为带系数上同调类，单位由 \(\mathcal R_\rho\) 系数系统携带，不是新的 SI 基本单位。  
[方向] 将 R3 从哲学原则降为多商空间上的 obstruction/non-obstruction 判别；若只停在 (A5)，先发覆盖严重。  
[数据] 使用 paper-search-mcp 文献检索；本轮未使用实验数据。  
[假设] \(\mathcal G,\mathcal T,\mathcal B,\mathcal N,\mathcal H\) 的合成可建模为群胚/半群胚；template、bridge、history 扩张能写成 residual 复形中的 coboundary 或 nuisance tangent 方向。

## 最小可发表/可验证定理

**定理 A（五重商 residual 筛选定理，最小版）。**  
设 residual 复形

\[
C^0 \xrightarrow{d_0} C^1 \xrightarrow{d_1} C^2
\tag{A6}
\]

描述某一物理提案的观测残差，其中 \(C^0\) 为允许的 gauge/template/bridge/nuisance/history 重参数化，\(C^1\) 为 residual，\(C^2\) 为一致性约束。若：

1. 所有允许选择生成的 residual 改变都落在 \(\operatorname{im}d_0\)；
2. 候选 residual \(r\in C^1\) 满足 \(d_1r=0\)；
3. 对每个扩张模板库 \(\mathcal T'\supseteq\mathcal T\)、桥接族 \(\mathcal B'\supseteq\mathcal B\)、history column 库 \(\mathcal H'\supseteq\mathcal H\)，自然包含诱导
\[
\iota^*:H^1(C^\bullet_{\mathfrak A})\to H^1(C^\bullet_{\mathfrak A'})
\tag{A7}
\]
且 \(\iota^*[r]\ne 0\)；

则 \(r\) 通过 R3 筛选：它不是当前允许选择的截面伪影、模板缺列伪影、bridge 伪影或 nuisance/history 投影残差。若存在某个允许扩张使 \(\iota^*[r]=0\)，则 \(r\) 只能作为模型失配诊断量，不能单独主张为新物理自由度。

证明骨架：

- 条件 1 给出 \(r\sim r+d_0u\)，即所有允许选择只改变上同调代表元。
- 条件 2 保证 \(r\) 是一致 residual，不是违反约束的非法对象。
- 条件 3 是自然性/鲁棒性条件：若加入合法 template、bridge、history 后类变零，则原 residual 是缺列或选择伪影。
- 因此非零且对允许扩张自然非零的 \([r]\in H^1\) 是必要筛选条件；若类为零，则 \(r=d_0u\)，可由允许重参数化吸收。

可验证实现：

1. 明确 \(C^0\)：gauge generator、template columns、bridge basis、nuisance tangent、history columns。
2. 明确 \(C^1\)：观测 residual 向量空间或函数空间。
3. 用线性化版本计算
\[
\Pi_{\perp \operatorname{im}d_0}r.
\tag{A8}
\]
若为零，立即诊断为模型失配/选择伪影。
4. 对 \(\mathcal T,\mathcal B,\mathcal H\) 做单调扩张压力测试；若任何合法扩张吸收 residual，则不得提升为物理自由度。

该定理的发表价值只在“筛选协议/负结果自动化”：它把 LP23 前几轮失败压缩成一个可复用的 no-go filter。它不构成新的 gauge theory、moduli theory、cohomology theory 或统计推断理论。

## 深挖1：本轮结论的下一层后果

第一层后果：LP23-R3 不能以“新物理自由度原则”发表。因为“物理量必须降到商空间”和“非零 obstruction class 才有物理含义”已经是 gauge theory、equivariant cohomology、anomaly theory 的标准结构。

第二层后果：若继续推进，论文形态必须改成“理论构造筛选器”。可验证对象不是光学相位本身，而是一个 residual cohomology pipeline：输入某个提案的 gauge/template/bridge/nuisance/history 库，输出 \([r]\) 是否在所有合法扩张下保持非零。

第三层后果：这会把 LP23 的物理野心降级为方法论工具。成功标准从“发现自由度”变为“提前杀死截面伪影命题”。这与 R2 的失败记录一致：bridge residual 若能被 nuisance/history column 吸收，就不是新自由度。

## 深挖2：最可能错误的前提

第一层风险：把 \(\mathcal T,\mathcal B,\mathcal H\) 与 gauge/nuisance 一起放入同一个 \(\mathfrak A\) 可能过强。Gauge 是冗余对称，template/bridge/history 有时是物理建模选择，不一定都应被商掉。

第二层风险：若某个 bridge 或 history column 对应真实介质响应、探测器协议或边界条件，那么把它当作 nuisance 取商会误杀真实物理。此时筛选定理只能作为“保守必要条件”，不能作为充分否定条件。

第三层风险：自然扩张条件 (A7) 可能不可判定。实际模板库不是完备偏序；“所有合法扩张”可能需要用有限压力测试近似。因此最小可验证版本必须承认它是有限库相对定理，而不是绝对定理。

## 结论

R3 原原则的本体论读法已被成熟框架覆盖：gauge orbit/moduli/equivariant cohomology/anomaly/nuisance projection/model misspecification 全部给出强先发。

未完全覆盖的最小活口是：把五类允许选择统一成 residual 复形，提出“非零且在合法扩张下自然非零”的可执行筛选定理。它的价值是方法论和负结果自动化，不是新物理自由度的发现。

本轮成果：[五重商 residual 筛选定理；R3 本体论版本判死，方法论版本可继续一次压力测试]  
新增引用文献：[Anderson 1958 DOI `10.1103/physrev.110.1197`; Orland 2004 DOI `10.1103/physrevd.70.045014`; Khavkine 2015 DOI `10.1088/0264-9381/32/18/185019`; Bredon 1967 DOI `10.1007/bfb0082692`; Tu 2020 DOI `10.23943/princeton/9780691191751.003.0004`; Fujiki 2023 DOI `10.1201/9781003419983-4`; Hsin-Lam-Seiberg 2019 DOI `10.21468/scipostphys.6.3.039`; Benini-Cordova-Hsin 2019 DOI `10.1007/jhep03(2019)118`; Cordova-Freed-Lam-Seiberg 2020 DOI `10.21468/scipostphys.8.1.001`; Godambe 1991 DOI `10.2307/2336904`; Barber-Samworth 2021 DOI `10.3150/20-bej1316`; Chernozhukov et al. 2022 DOI `10.3982/ecta16294`]  
最弱的环节：[把 template/bridge/history 全部视作可商掉的允许选择，可能误杀真实协议物理]  
下一步计划：[让 INSPECTOR 检查 (A0)-(A8) 的符号、量纲与线性代数方向；若通过，Round2 应做一个有限矩阵 toy example，证明 residual 如何被扩张 template/history 吸收或保持非零]  
需要 PI 投喂的文献方向：[descent obstruction in quotient stacks; residual cohomology in inverse problems; semiparametric orthogonal scores under model misspecification; gauge-invariant relational observables in optics/GR]
