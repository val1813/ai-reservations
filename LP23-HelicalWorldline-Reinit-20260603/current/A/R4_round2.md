# LP23-R4 Round2 A博士报告：Proof-Carrying Closure / Witness Checker

日期：2026-06-03  
角色：A博士（学院派，文献驱动）  
独立性声明：本报告未读取 `current/B` 或 B 路 Round2 报告；未读取旧 `LP23-螺旋世界线` 目录。输入只使用 PI 指定的 R4 Round1 综合、A 路 Round1、R4 文献库与 A_AGENT 约束。

## §0 框架声明

本轮采用两个成熟框架作参照：

1. **计算机科学侧：proof-carrying code / type-carrying code / proof-carrying authorization / capability security。**  
   这些框架已经成熟地解决了“一个对象能否携带可机检证明，使宿主只运行 checker 而不重建生产过程”的问题。R4a 若只说“每个补列带证明”，就是换名，不是新命题。

2. **物理与统计侧：EFT operator basis + redundancy quotient；passive/causal response realization；system/causal identifiability。**  
   这些框架已经给出大量局部 witness：operator witness、EOM/IBP redundancy witness、positive-real/Herglotz/passivity witness、SCM/do-calculus identifiability witness、profile-likelihood identifiability witness。R4a 的可能活口只能是：把这些局部 witness 组织成同一个 residual discovery protocol 的跨域合同，且该合同先于 residual、独立于 residual、可复跑。

本轮判定先给出：**R4a 不是 proof-carrying code 的物理改名，除非它只携带形式证明而不携带物理来源 witness；R4a 也不是单一 passivity/EFT/causal checker，除非协议退化到固定单域。真正活口很窄：proof-carrying closure 必须要求每个合法补列携带最小物理 witness tuple，并由 checker 拒绝 residual-shaped oracle column。**

## 1. 先发审查：PCC/type/capability 类比是否只是换名

PCC 的核心已由 Necula 在 POPL 1997 建立：不可信代码携带安全证明，宿主检查证明而非信任代码生成者。Foundational PCC、typed assembly language、proof-carrying authorization 又把 trusted computing base 压到逻辑、类型规则和策略证明上。

代表先发：

- Necula, "Proof-carrying code", POPL 1997, DOI `10.1145/263699.263712`.
- Necula and Lee, "Research on proof-carrying code for untrusted-code security", IEEE S&P 1997, DOI `10.1109/SECPRI.1997.601335`.
- Appel, "Foundational proof-carrying code", LICS 2001, DOI `10.1109/LICS.2001.932501`.
- Morrisett, Walker, Crary, Glew, "From System F to typed assembly language", POPL 1998, DOI `10.1145/268946.268954`; TOPLAS version DOI `10.1145/319301.319345`.
- Appel and Felten, "Proof-carrying authentication", CCS 1999, DOI `10.1145/319709.319718`.
- Bauer, Schneider, Felten, Appel, "Access control on the Web using proof-carrying authorization", DISCEX 2003, DOI `10.1109/DISCEX.2003.1194942`.
- Miller, Tribble, Shapiro, "Concurrency Among Strangers", DOI `10.1007/11580850_12`, as capability-security background.

判定：

- **被覆盖部分。** “补列必须携带可验证 certificate，checker 只验证 certificate”已被 PCC/TAL/PCA 完全覆盖。若 R4a 的 witness 只是一个形式 derivation tree，那么它是 PCC 的应用。
- **未被覆盖部分。** PCC 不定义“哪些物理补列允许生成”。它只要求相对于给定 safety policy 可检查。R4a 的难点是 policy/witness source 的物理自然性：locality、causality、passivity、operator origin、measurement-source、identifiability 是否在看 residual 前已固定。
- **活口条件。** R4a 必须把 PCC 的形式 checker 变为“物理来源 checker”：不是 `proof : Legal(column)` 即可，而是 `witness : Origin(column)` 可独立复核。

--- INSPECTOR_CHECK ---
[公式] `Accept(c)=1 iff Verify_P(c,W_c)=1 and NonOracle_P(c,W_c,r)=1`；`c` 与 `r` 同属观测输出空间 `Y`，SI 单位由 `Y` 的测量通道给定。  
[方向] PCC/type/capability 已覆盖“携证书可机检”的抽象结构；R4a 的新增只能是物理 witness 的来源独立性。  
[数据] 本步使用文献元数据与 DOI 检索，不使用实验数据。  
[假设] 形式证明和物理来源可分离；checker 可访问预注册协议 `P`、候选列 `c`、witness `W_c`，但不能允许 witness 查询 residual 形状。

## 2. 单域 witness 是否已覆盖

### 2.1 Passivity realization / positive-real / Herglotz witnesses

对于线性时不变被动响应，合法响应函数可由 positive-real、Herglotz-Nevanlinna、Kramers-Kronig/causality 与 realization theory 刻画。工程上还有 passive approximation 和 convex constrained fitting。

代表先发：

- Hughes, "A theory of passive linear systems with no assumptions", Automatica 2017, DOI `10.1016/j.automatica.2017.08.017`, arXiv `1611.06140`.
- Ivanenko et al., "Passive Approximation and Optimization Using B-splines", SIAM J. Appl. Math. 2019, DOI `10.1137/17M1161026`.
- Arlinskii, Belyi, Tsekanovskii, "Realization of Herglotz-Nevanlinna Functions by Conservative Systems", DOI `10.1007/978-3-0348-0667-1_50`.
- Cassier and Milton, "Bounds on Herglotz functions and fundamental limits of broadband passive quasi-static cloaking", DOI `10.1063/1.4989990`, arXiv `1610.08592`.
- Haakestad and Skaar, "Causality and Kramers-Kronig relations for waveguides", DOI `10.1364/OPEX.13.009922`.

判定：若 `G_response` 只生成 LTI 被动介质响应，则 witness checker 已成熟：给出 positive-real/Herglotz representation、passivity inequality、realization matrices 或 convex certificate 即可。R4a 在该域无新增。

### 2.2 Local EFT operator generation / redundancy witnesses

EFT 已有 operator basis 枚举、Hilbert series、IBP/EOM/Bianchi/Fierz/Schouten redundancy、field redefinition equivalence、SMEFT/HEFT/LEFT basis 与 RG mixing。

代表先发：

- Henning, Lu, Melia, Murayama, "Hilbert series and operator bases with derivatives in effective field theories", DOI `10.1007/s00220-015-2518-2`.
- Henning, Lu, Melia, Murayama, "Operator bases, S-matrices, and their partition functions", DOI `10.1007/JHEP10(2017)199`.
- Graf, Henning, Lu, Melia, Murayama, "Hilbert series, the Higgs mechanism, and HEFT", DOI `10.1007/JHEP02(2023)064`.
- Barzinji, Trott, Vasudevan, "Equations of motion for the standard model effective field theory", DOI `10.1103/PhysRevD.98.116005`.
- Brivio and Trott, "The standard model as an effective field theory", DOI `10.1016/j.physrep.2018.11.002`.

判定：若 `G_operator` 只生成固定 field content、symmetry、dimension cutoff 下的 local operators，则 witness 是 `(field_content, symmetry_rep, derivative_count, Hilbert-series monomial, redundancy reduction certificate)`。这已是成熟 EFT 技术。R4a 不能宣称发明 operator closure。

### 2.3 System / causal model identifiability certificates

系统识别和因果图模型已有 structural/practical identifiability、profile likelihood、do-calculus、ID algorithm、Markov equivalence 下的识别算法与完备性讨论。

代表先发：

- Godfrey and DiStefano, "Identifiability of Model Parameters", DOI `10.1016/B978-0-08-034929-9.50005-4`.
- Raue et al., "Structural and practical identifiability analysis ... profile likelihood", DOI `10.1093/bioinformatics/btp358`.
- Pearl, *Causality*, DOI `10.1017/CBO9780511803161`.
- Shpitser, "Identification in Graphical Causal Models", DOI `10.1201/9780429463976-16`.
- Bareinboim, Jaber, Ribeiro, Zhang, "Causal Identification Under Markov Equivalence: Calculus, Algorithm, and Completeness", NeurIPS 2022, DOI `10.52202/068431-0266`.

判定：若 `G_causal` 只在固定 SCM/DAG/ADMG、intervention set、latent projection 下判断某个 causal estimand 是否可识别，成熟工具已覆盖。R4a 的活口只能要求：补列的 causal witness 不只是“拟合更好”，而是预注册的 graph operation、intervention source、latent-source bound 与 identifiability certificate。

## 3. 最小 witness checker 对象

设 residual discovery protocol 仍为 Round1 的

```text
P = (X, Y, H, M0, Q, G, E, K, L)
C(P) = mu C . cl_{E,K}(M0 union {g(M) | M in C, g in G, Q[g(M)] = true})
Obs_P(r) = [r] in Y / S_C(P)
```

Round2 的 proof-carrying closure 把“合法补列”从裸列

```text
c in Y_K
```

提升为携证对象

```text
Col = (c, kind, W, provenance, cost)
```

其中 `kind` 至少分为：

```text
operator | response | history | nuisance | measurement | causal | bridge
```

每个合法补列必须携带的最小 witness tuple：

```text
W_c = (
  W_pre,
  W_origin,
  W_locality,
  W_symmetry,
  W_redundancy,
  W_causality,
  W_passivity,
  W_measurement,
  W_identifiability,
  W_cutoff,
  W_nonoracle
)
```

解释如下：

- `W_pre`：预注册证据。说明生成规则、模板族、参数范围、复杂度 cutoff 在看 residual 前已经固定。
- `W_origin`：物理来源证据。operator 来自 local action/UV matching/spurion；response 来自被动实现或介质模型；history 来自独立校准的 memory kernel；nuisance 来自仪器或环境通道；causal 来自 graph/intervention contract。
- `W_locality`：支撑、导数阶、memory depth、light-cone 或显式非局域核类。
- `W_symmetry`：gauge/Lorentz/internal symmetry、守恒律、selection rules。
- `W_redundancy`：EOM/IBP/field redefinition/gauge/protocol reparameterization 下的代表元，证明不是已 quotient 掉的列。
- `W_causality`：支持在因果过去、analyticity、Kramers-Kronig 或 SCM intervention ordering。
- `W_passivity`：能量不产生、positive-real/Herglotz representation、dissipation inequality；若主动介质则必须显式标注外部能源通道。
- `W_measurement`：该补列如何进入观测通道 `Y`，含 SI 单位、校准源、仪器 transfer function 与误差模型。
- `W_identifiability`：新增参数或结构在给定协议下是否可辨识；若不可辨识，必须标为 nuisance quotient 而不能吸收 obstruction。
- `W_cutoff`：dimension/order/rank/bandlimit/smoothness/memory 的有限截断，保证 checker 可枚举或半判定。
- `W_nonoracle`：证明 `c` 的生成不依赖 `r` 的观测后形状；至少要求 hash/time-stamp/pre-registration 或独立数据通道。

最小 checker：

```text
Verify_P(c,W_c) =
  Pre(W_pre,P)
  and Origin(W_origin,P)
  and Locality(W_locality,K)
  and Sym(W_symmetry,Q)
  and RedundancyNormal(W_redundancy,E)
  and Causal(W_causality,Q)
  and PassiveOrPowered(W_passivity,Q)
  and MeasurementMap(W_measurement,Y)
  and IdentifiableOrQuotient(W_identifiability,E,L)
  and CutoffFinite(W_cutoff,K)
  and NonOracle(W_nonoracle,r)
```

合法补列集合改写为

```text
G_W(P,r) = { c | exists W_c : Verify_P(c,W_c)=1 } .
S_W(P,r) = span { c in G_W(P,r) } .
Obs^W_P(r) = [r] in Y / S_W(P,r) .
```

但为了避免 checker 自身偷看 residual，强判据应为

```text
G_W(P) = { c | exists W_c : Verify_P^pre(c,W_c)=1 }
S_W(P) = span G_W(P)
Obs^W_P(r) = [r] in Y / S_W(P)
```

即 `G_W` 不以 `r` 为输入；`r` 只在最后投影到 quotient 时出现。

--- INSPECTOR_CHECK ---
[公式] `W_c=(W_pre,W_origin,W_locality,W_symmetry,W_redundancy,W_causality,W_passivity,W_measurement,W_identifiability,W_cutoff,W_nonoracle)`；`Obs^W_P(r)=[r] in Y/S_W(P)`。`Y` 的单位由 `W_measurement` 指定，`c` 必须与 `r` 同单位。  
[方向] witness checker 的最小对象不是 proof term，而是预注册来源、物理约束、冗余商、观测映射和非 oracle 证明的组合。  
[数据] 文献结构与协议形式化；未使用实验数据。  
[假设] 存在独立的预注册或独立测量通道来验证 `W_pre` 和 `W_nonoracle`；否则 checker 退化为事后证明生成器。

## 4. 防止 residual-shaped oracle column

Round1 no-go 说：若允许 `T_r:x -> r(x)` 作为 template，则 `r in S_C(P)`，所以 `Obs_P(r)=0`。Round2 的 witness checker 必须把这个漏洞变成显式拒绝规则。

最小拒绝条件：

```text
Reject(c,W_c,r)=1
if Dep(c; r | P_pre, D_independent) > 0
and no independent source channel proves c before r.
```

实际可机检近似：

1. **时间顺序检查。** `timestamp(W_pre) < timestamp(r_unblinded)`。
2. **独立数据检查。** 生成 `c` 的校准数据 `D_c` 与发现 residual 的数据 `D_r` 不重叠，或有 blinded split。
3. **复杂度惩罚。** `K(c)` 不随 residual 采样点数线性增长；禁止任意 spline/interpolant 逐点追踪 residual。
4. **低维来源检查。** `dim(theta_c)`、memory depth、operator dimension、rank/bandlimit 由 `K_pre` 固定。
5. **冗余商检查。** 若 `c` 只是在 measurement reparameterization、EOM、field redefinition、history re-binning 中生成，归入 `E` 而不是新补列。
6. **holdout 检查。** `c` 必须预测未参与 residual 发现的通道、频段、边界条件或 intervention，而不只是吸收原 residual。

强形式 no-oracle 条件：

```text
I(c ; r | P_pre, D_c) = 0
```

其中 `I` 是信息依赖的理想条件。实践中用 blind split、pre-registration、independent calibration 和 held-out prediction 近似。

## 5. Round2 no-go：witness checker 仍会失败的条件

**No-go R2-A：形式 proof 不等于物理 witness。**  
若 checker 只验证 `proof : Legal(c)`，而 `Legal` 的规则由研究者事后扩展，则 PCC 成熟框架覆盖 R4a，且无法阻止 residual-shaped column。

**No-go R2-B：单域退化。**  
若所有合法补列都落在固定 EFT basis、固定 passive LTI response、固定 SCM identifiability 或固定 statistical model expansion 中，则 R4a 是这些成熟框架的换名。

**No-go R2-C：witness 可由 residual 生成。**  
若 `W_origin`、`W_measurement` 或 `W_identifiability` 可在看见 `r` 后构造，且无独立校准/holdout，则 `W_nonoracle` 失败，`Obs^W_P(r)` 没有发现意义。

**No-go R2-D：过宽 checker 全吸收。**  
若允许任意 Herglotz measure、任意 local operator 高阶展开、任意 latent variable、任意 history spline 且无复杂度 cutoff，则 `S_W(P)` 在有限采样 `Y_K` 中通常满秩，所有 residual 被吸收。

**No-go R2-E：过窄 checker 误杀物理。**  
若 witness 只接受局域 EFT 或被动 LTI，却排除真实非局域记忆、主动介质、非平衡驱动、开放系统、边界条件变化，则 obstruction 只是 checker 设计偏见。

**No-go R2-F：quotient 不不变量。**  
若 `Obs^W_P(r)` 在 gauge、field redefinition、operator basis choice、measurement calibration、history binning 或 causal graph Markov-equivalent 表示下改变，则它不是物理 obstruction。

**No-go R2-G：不可复跑。**  
若 `S_W(P)` 不能在有限 `K` 下枚举、近似、半判定或用独立脚本复现 rank/projection，则 R4a 只是哲学判据。

--- INSPECTOR_CHECK ---
[公式] 若 `G_W(P)` 在有限 `Y_K` 中生成满秩，则 `S_W(P)=Y_K`，故任意 `r in Y_K` 有 `Obs^W_P(r)=0`。若 `G_W` 依赖 `r`，则存在 `c=r` 使 `Obs^W_P(r)=0`。  
[方向] witness checker 的失败不是局部技术失败，而是来源独立性、复杂度截断、quotient 不变量、可复跑性四者任一失守。  
[数据] 逻辑 no-go；未使用实验数据。  
[假设] `Y_K` 是有限采样/有限带宽/有限通道观测空间；rank 判据在该有限空间中定义。

## 6. 深挖1：本轮结论的下一层后果

本轮把 R4a 从“补列带证明”推进为“补列带物理来源 witness”。下一层后果是：R4 的第一可执行对象不应是模型拟合器，而应是 witness schema validator。

也就是说，任何 toy 或真实协议必须先输出：

```text
(P_pre, WitnessSchema, CandidateColumns, VerifyLog)
```

然后才允许输入 residual `r` 做 projection。若脚本流程是先计算 residual 再生成候选列，即使候选列看起来 local/passive/causal，也已经违反 `W_nonoracle`。

再下一层后果：R4 的可测量量从 residual norm 变为三元组

```text
(rank S_W(P), ||Proj_{S_W(P)^\perp} r||, heldout_error(c))
```

其中 `heldout_error` 是防 oracle 的关键。如果某列只降低训练 residual 而不预测 holdout 通道，则它应进入 nuisance/model-misspecification 诊断，而不是物理补列闭包。

硬边界：在无限维响应函数、任意 measure Herglotz 表示、任意 high-order EFT operator、任意 latent causal graph 情况下，`rank S_W(P)` 不稳定。必须先固定有限 `K`：采样、频带、operator dimension、rank、memory depth、graph size。

## 7. 深挖2：本轮最可能错误的前提

最可能错误的前提是：**跨域 witness schema 可以自然指定。**

局部领域都有自然 witness：

- EFT 的自然性来自 field content、symmetry、dimension cutoff。
- Passive response 的自然性来自 analyticity、positivity、energy inequality。
- Causal identifiability 的自然性来自 graph、intervention、latent projection。
- Measurement nuisance 的自然性来自仪器校准和误差模型。

但 R4a 要把这些放进一个共同 `P`，风险是 schema 变成人工拼盘：哪里需要排除 residual 就收紧哪里，哪里需要吸收 residual 就放宽哪里。这会使 R4a 既不是物理原则，也不是成熟单域方法，而是人为模型选择规则。

再下一层看，真正脆弱点是 `W_origin`。如果某个补列的来源只能说“它满足 local/passive/causal 约束”，但没有独立生成机制、校准通道或 UV/medium/measurement origin，那么它仍可能是 residual-shaped oracle 的平滑版本。R4a 的活口要求来源证据强于约束证据。

硬边界：我本轮没有证明存在一个非人工的跨域 witness schema；只证明了若 schema 存在，它至少必须包含上述 witness tuple，并满足 no-oracle、finite-cutoff、quotient-invariance、heldout-prediction。

## 8. 本轮成果

本轮成果：R4a 的成熟先发风险被压缩清楚。PCC/type/capability 已覆盖“携证明可检查”的抽象结构；passivity/Herglotz、EFT operator basis、因果/系统可辨识已覆盖单域 witness。R4a 的唯一真实活口是：定义跨域 proof-carrying closure，使每个合法补列携带预注册、物理来源、局域/因果/被动、冗余商、测量映射、可辨识性、有限截断和非 oracle witness；否则 R4a 判死或降级为既有框架换名。

## 9. 新增引用文献

- Necula, "Proof-carrying code", POPL 1997, DOI `10.1145/263699.263712`.
- Appel, "Foundational proof-carrying code", LICS 2001, DOI `10.1109/LICS.2001.932501`.
- Morrisett, Walker, Crary, Glew, "From System F to typed assembly language", POPL 1998, DOI `10.1145/268946.268954`.
- Appel and Felten, "Proof-carrying authentication", DOI `10.1145/319709.319718`.
- Bauer, Schneider, Felten, Appel, "Access control on the Web using proof-carrying authorization", DOI `10.1109/DISCEX.2003.1194942`.
- Miller, Tribble, Shapiro, "Concurrency Among Strangers", DOI `10.1007/11580850_12`.
- Hughes, "A theory of passive linear systems with no assumptions", DOI `10.1016/j.automatica.2017.08.017`, arXiv `1611.06140`.
- Ivanenko et al., "Passive Approximation and Optimization Using B-splines", DOI `10.1137/17M1161026`.
- Arlinskii, Belyi, Tsekanovskii, "Realization of Herglotz-Nevanlinna Functions by Conservative Systems", DOI `10.1007/978-3-0348-0667-1_50`.
- Bareinboim, Jaber, Ribeiro, Zhang, "Causal Identification Under Markov Equivalence", DOI `10.52202/068431-0266`.
- Raue et al., "Structural and practical identifiability analysis ... profile likelihood", DOI `10.1093/bioinformatics/btp358`.

## 10. 最弱环节

最弱环节：`W_origin` 与 `W_nonoracle`。只要物理来源 witness 不能独立于 residual 复核，或者 checker 允许观测后生成模板/latent/history/spline，R4a 立即回到 Round1 no-go：所有 residual 都可被合法补列吸收。

## 11. 下一步计划

下一步应要求 Round3 或 PI 侧给出一个最小可复跑 schema：

```text
WitnessSchema.json
columns_pre.json
verify_witness.py
projection_rank.py
holdout_split.json
```

具体测试：在有限 `Y_K` 中，先不输入 residual，只枚举通过 `Verify_P^pre` 的列并计算 `rank S_W(P)`；然后输入 residual 只做 projection；最后用 holdout 通道检验通过 witness 的补列是否有预测力。若 `rank S_W(P)=dim Y_K` 或 holdout 失败，R4a 降级；若 residual 在所有预注册合法列下仍保留稳定非零投影，才进入 Round3。

需要 PI 投喂的文献方向：`certified model expansion`, `prequential model checking`, `passive realization certificate`, `causal identifiability certificate software`, `EFT basis certificate EOM IBP`, `non-oracle residual modeling holdout`.
