# LP23-R4 Round1 A博士报告：Protocol-Closure Obstruction

日期：2026-06-03  
角色：A博士（学院派，文献驱动）  
独立性声明：本报告未读取 `current/B` 或旧 LP23-螺旋世界线目录。

## §-1 先发查重结论

本轮先把 R4 拆成六条成熟文献轴检索。结论很硬：`C(P)` 的组成模块几乎都已有成熟局部版本；R4 若有增量，只能是“给定 residual discovery protocol 后，跨 gauge/template/bridge/nuisance/history 的合法补全合同闭包”，不能声称发明 EFT 闭包、系统辨识、被动响应或统计模型扩张。

| 查重轴 | 已有框架 | 对 R4 的覆盖风险 | 判定 |
|---|---|---|---|
| EFT/operator basis closure | Hilbert series 枚举 operator basis；IBP/EOM/Bianchi/Fierz/Schouten 冗余；SMEFT/HEFT/LEFT operator basis | 若 `P` 是固定局域 QFT、固定对称性和固定维数截断，`C(P)` 直接退化为 operator basis + 冗余商 | 高覆盖 |
| field redefinition/EOM redundancy | EOM 消去、field redefinition ambiguity、equivalence theorem | 若 residual 只是不良场变量或冗余算符方向，R4 被既有 EFT 等价类吸收 | 高覆盖 |
| RG/operator mixing | anomalous dimension matrix 和 operator mixing 给出尺度流下闭合条件 | 若“历史核闭合”只是 Wilsonian/RG closure，R4 被 RG mixing 覆盖 | 高覆盖 |
| system identification identifiability | structural/practical identifiability、nuisance parameters、model structure selection、residual diagnostics | 若 `C(P)` 只是“加参数后 residual 是否可辨识”，R4 是系统辨识旧问题 | 高覆盖 |
| causal/passive response constraints | Kramers-Kronig、positive-real/Herglotz-Nevanlinna、passivity、causal SCM/do-calculus | 若响应侧固定为线性时不变被动介质或固定因果图，合法响应类已有判据 | 高覆盖 |
| statistical natural extension/model expansion | model expansion/contraction、prior information、Bayesian falsifiability、model checking | 若合法扩张由统计模型族和先验给定，R4 是 model expansion 的换名 | 中高覆盖 |

代表性文献锚点：

1. Henning, Lu, Melia, Murayama, “Hilbert series and operator bases with derivatives in effective field theories”, DOI `10.1007/s00220-015-2518-2`.
2. Henning, Lu, Melia, Murayama, “Operator bases, S-matrices, and their partition functions”, DOI `10.1007/JHEP10(2017)199`.
3. Graf, Henning, Lu, Melia, Murayama, “Hilbert series, the Higgs mechanism, and HEFT”, DOI `10.1007/JHEP02(2023)064`.
4. Liao, Ma, “An explicit construction of the dimension-9 operator basis in the standard model effective field theory”, DOI `10.1007/JHEP11(2020)152`.
5. Barzinji, Trott, Vasudevan, “Equations of motion for the standard model effective field theory”, DOI `10.1103/PhysRevD.98.116005`.
6. Jenkins, Manohar, Stoffer, “Low-energy effective field theory below the electroweak scale: anomalous dimensions”, DOI `10.1007/JHEP01(2018)084`.
7. Godfrey, DiStefano, “Identifiability of Model Parameters”, DOI `10.1016/B978-0-08-034929-9.50005-4`.
8. Gustafson, “On Model Expansion, Model Contraction, Identifiability and Prior Information”, DOI `10.1214/088342305000000098`.
9. Spall, Chin, “On system identification with nuisance parameters”, DOI `10.1109/ACC.1994.751793`.
10. Haakestad, Skaar, “Causality and Kramers-Kronig relations for waveguides”, DOI `10.1364/OPEX.13.009922`.
11. Lucarini, “Response Theory for Equilibrium and Non-Equilibrium Statistical Mechanics: Causality and Generalized Kramers-Kronig Relations”, DOI `10.1007/s10955-008-9498-y`.
12. Hughes, “A theory of passive linear systems with no assumptions”, DOI `10.1016/j.automatica.2017.08.017`, arXiv `1611.06140`.
13. Cassier, Milton, “Bounds on Herglotz functions and fundamental limits of broadband passive quasi-static cloaking”, DOI `10.1063/1.4989990`, arXiv `1610.08592`.

## §0 框架声明

本轮采用的成熟子领域框架是：

**物理侧：effective field theory + passive/causal response theory。**  
EFT 负责“局域、对称性、守恒律、EOM/IBP 冗余、RG mixing”的闭包；被动响应理论负责“因果性、能量/响应约束、Kramers-Kronig/positive-real/Herglotz”的闭包。

**统计/协议侧：system identification + model expansion。**  
它负责“参数可辨识、nuisance 投影、测量协议、残差诊断、模型补列”的闭包。

R4 的候选增量不是任一单侧闭包，而是把这些闭包组织成同一个 protocol contract，并问：给定发现流程 `P` 后，所有物理允许的补全是否形成可计算闭包；若闭包内 residual 仍非零，才叫 obstruction。

## §1 R4 最小数学对象：`C(P)`

令一个 residual discovery protocol 的最小合同为

```text
P = (X, Y, H, M0, Q, G, E, K, L)
```

其中：

- `X`：可制备输入/背景/边界条件空间。
- `Y`：观测输出空间，带测量误差模型和单位。
- `H`：history kernel，可包含记忆、迟滞、过去状态、介质制备历史。
- `M0`：基准模型族，含场变量、参数、响应核和测量映射。
- `Q`：物理约束集合，至少包含 causality、locality 或明确的非局域核类、conservation laws、energy/passivity/positivity、measurement protocol constraints。
- `G`：允许补全生成元集合，分为 `G_gauge, G_template, G_bridge, G_nuisance, G_history, G_operator, G_response`。
- `E`：冗余等价关系，含 gauge、field redefinition、EOM/IBP、不可辨识 nuisance、测量重参数化。
- `K`：复杂度/截断规则，如 EFT dimension、memory depth、rank、smoothness、bandlimit、实验前注册模板库。
- `L`：loss/discrepancy functional，用来把 residual 放进同一个观测空间。

定义合法模型补全闭包为最小不动点：

```text
C(P) = mu C . cl_E,K( M0 union { g(M) | M in C, g in G, Q[g(M)] = true } )
```

这里 `cl_E,K` 表示在冗余商 `E` 下取等价类、再按截断/复杂度规则 `K` 保留可计算代表元。若写成商空间：

```text
\bar C(P) = C(P) / E
```

对每个模型 `M in C(P)` 有预测映射

```text
F_M : Theta_M -> Y .
```

给定观测 residual

```text
r = y_obs - F_{M0}(\hat theta_0) in Y ,
```

闭包可吸收方向定义为

```text
S_C(P) = closure span { Im dF_M | M in C(P), allowed finite extensions under K } subset Y .
```

R4 的 obstruction class 是

```text
Obs_P(r) = [r] in Y / S_C(P) .
```

若 `Obs_P(r) != 0`，且非零性对 `E` 中所有 gauge/field/protocol reparameterization 不变，则 residual 才有资格叫 protocol-closure obstruction。若 `Obs_P(r) = 0`，该 residual 被合法补全吸收，不能作为新物理自由度证据。

--- INSPECTOR_CHECK ---
[公式] `C(P)=mu C.cl_{E,K}(M0 union {g(M)|M in C, g in G, Q[g(M)]=true})`；`Obs_P(r)=[r] in Y/S_C(P)`。`Y` 使用观测量 SI 单位；`S_C(P)` 与 `r` 同单位。  
[方向] R4 的对象不是 residual 本身，而是 residual 在合法补全闭包商空间中的类。  
[数据] 本步未用实验数据；只用 protocol 结构和先发文献框架。  
[假设] `G,Q,E,K` 可由协议预先给定，且 `S_C(P)` 可有限截断近似。

## §2 什么条件下被既有框架覆盖

R4 直接降级为既有框架的条件如下。

1. **EFT 覆盖条件。** 若 `P` 的补全只允许局域 operator，且约束仅为固定场内容、对称性、守恒律、导数/质量维数截断，则 `C(P)` 等于 EFT operator basis 闭包；`E` 等于 IBP/EOM/Fierz/Bianchi/field-redefinition 冗余；`K` 等于维数截断。此时 R4 无新增。

2. **RG 覆盖条件。** 若 history kernel 只表示尺度依赖或 integrated-out modes，且合法补全由 counterterms 和 anomalous dimension matrix 闭合，则 `C(P)` 是 RG-invariant operator subspace。此时“历史闭合”不是新概念。

3. **被动响应覆盖条件。** 若 `F_M` 是线性时不变响应，且物理约束为因果性和被动性，则 `G_response` 被 positive-real/Herglotz/Kramers-Kronig 表征；residual 是否可由介质响应吸收，是已有 realization/approximation 问题。

4. **系统辨识覆盖条件。** 若 `G_nuisance` 是参数化扰动，`E` 是不可辨识参数商，`L` 是标准拟合误差，则 `Obs_P` 是 identifiability + model checking 的语言。

5. **因果模型覆盖条件。** 若 `P` 是固定 SCM/DAG、测量协议是 intervention set，合法扩张只是 latent variables、edges 或 do-calculus 可识别操作，则 `C(P)` 被 causal identifiability/causal discovery 覆盖。

6. **统计自然扩张覆盖条件。** 若“合法补全”只由统计模型族、先验、模型扩张/收缩规则给出，物理约束不进入生成元，那么 R4 是 Bayesian/model expansion 的换名。

因此，R4 的第一轮存活条件是：必须存在至少一个 protocol，其中 `G` 同时跨越 EFT/operator、response、measurement、history、nuisance，但任何单一成熟框架都不能枚举完整 `C(P)`；且 `G,Q,E,K` 不是事后按 residual 定制。

## §3 硬 no-go：Residual-template 吸收定理

**No-go A（任意 residual 列生成则 obstruction 恒为零）。**  
给定任意 residual `r in Y`。若闭包生成元 `G` 允许加入一个数据依赖 template

```text
T_r : x -> r(x)
```

或允许加入任意有限秩 nuisance/history column

```text
F_{M'}(x,theta,alpha) = F_M(x,theta) + alpha T_r(x)
```

且 `T_r` 被 `Q` 判为合法、未被 `K` 复杂度惩罚排除、也未要求有独立校准/预注册来源，则取 `alpha=1` 得

```text
r in S_C(P), hence Obs_P(r)=0 .
```

所以闭包内不存在不可吸收 residual。该类 `C(P)` 对新物理发现是空判据。

这给出第一轮判死标准：

- 若 `G_template` 或 `G_nuisance` 允许任何观测后 residual-shaped column，无需独立物理生成机制、独立测量通道或预注册模板库，则 R4 立即判死。
- 若 `Q` 只检查拟合后因果/被动/守恒，而不限制 template 的来源，R4 仍判死；因为可以先把 residual 写入 template，再投影到近似合法类。
- 若 `K` 不给有限复杂度、有限 memory depth 或有限 operator dimension，`C(P)` 不可枚举，R4 退化为哲学口号。

--- INSPECTOR_CHECK ---
[公式] `F_{M'}=F_M+alpha T_r`，若 `T_r=r` 且合法，则 `Obs_P(r)=0`。`F` 和 `r` 同为观测输出单位。  
[方向] R4 必须禁止事后 residual-shaped template；否则所有 obstruction 消失。  
[数据] 逻辑 no-go，无实验数据。  
[假设] 允许生成元可以依赖已观测 residual；这正是要排除的病态规则。

## §4 第一轮判死/存活标准

**判死 1：完全覆盖。**  
若能把 `P` 写成固定 EFT、固定 LTI 被动响应、固定 SCM 或固定统计模型扩张中的任一类，并且该类已有 `G,Q,E,K` 的枚举和 residual 可吸收判据，则 R4 降级为术语迁移。

**判死 2：任意补列。**  
若合法生成元允许观测后新增任意 template/nuisance/history column，则 `Obs_P(r)=0` 对所有 residual 成立，R4 判死。

**判死 3：不可计算闭包。**  
若 `C(P)` 不能给出有限截断、半判定、或可重复近似算法，则 R4 不能作为科学判据。

**判死 4：协议不变量失败。**  
若 `Obs_P(r)` 在 gauge、field redefinition、测量重参数化、history re-binning 下改变，则它是坐标伪影。

**存活门槛。**  
R4 只能在以下组合下进入 Round2：`G` 预注册、`Q` 独立于 residual、`E` 明确商掉冗余、`K` 可计算、且能构造一个 residual 在所有合法有限生成补全下仍非零的 toy 或真实 protocol。

## §5 深挖1：本轮结论的下一层后果

本轮把 R4 从“发现 residual”下移到“发现协议闭包的余核”。下一层后果是：实验或 toy 不能再报告一个数值 residual，而必须报告四件对象：

```text
(r, G_pre, Q_pre, E_pre, K_pre)
```

其中 `G_pre` 和 `Q_pre` 必须在看 residual 之前确定。否则 no-go A 直接把 residual 吸收。

再下一层后果：R4 的可检验量不是拟合误差大小，而是“合法 tangent span 的余维数”：

```text
codim_P = dim(Y_K / S_C(P)_K)
```

在有限观测/有限截断 `K` 下，若 `codim_P=0`，任何 residual 都没有 obstruction 资格；若 `codim_P>0`，才允许讨论 residual 在余空间上的投影。换言之，R4 的第一计算不是拟合，而是 rank/nullspace 计算。

硬边界：对无限维响应核或无限 memory history，`codim_P` 可能不可稳定估计。此时必须先降到有限带宽、有限采样、有限 memory depth，再谈 obstruction。

## §6 深挖2：本轮最可能错的前提

最脆弱前提是：`G,Q,E,K` 可以在不偷看 residual 的情况下被物理原则唯一或至少自然地指定。

如果这个前提错了，R4 会落入两难：

- `G` 太宽：no-go A 生效，所有 residual 被吸收。
- `G` 太窄：真实介质响应、边界条件、测量协议或 history kernel 被排除，R4 误杀物理。

再下一层看，真正困难不是 residual quotient，而是“合法生成元的自然性”。EFT 里自然性来自场内容、对称性和维数截断；被动响应里自然性来自解析性和正性；系统辨识里自然性来自实验设计和可辨识性。R4 若要新增，必须给出跨这些来源的一套 protocol naturality，而不是把它们拼表。

硬边界：我本轮没有证明跨协议 naturality 存在；只给出它必须满足的最小形式和判死条件。

## §7 本轮成果

本轮成果：R4 的最小对象应定义为 `C(P)=mu C.cl_{E,K}(M0 union {g(M)|Q[g(M)]})`，obstruction 是 `Obs_P(r)=[r] in Y/S_C(P)`；若闭包允许事后 residual-shaped template/nuisance/history column，则所有 residual 均可吸收，R4 Round1 直接判死。

## §8 新增引用文献

- Henning et al., “Hilbert series and operator bases with derivatives in effective field theories”, DOI `10.1007/s00220-015-2518-2`.
- Henning et al., “Operator bases, S-matrices, and their partition functions”, DOI `10.1007/JHEP10(2017)199`.
- Graf et al., “Hilbert series, the Higgs mechanism, and HEFT”, DOI `10.1007/JHEP02(2023)064`.
- Liao, Ma, “An explicit construction of the dimension-9 operator basis in the standard model effective field theory”, DOI `10.1007/JHEP11(2020)152`.
- Barzinji, Trott, Vasudevan, “Equations of motion for the standard model effective field theory”, DOI `10.1103/PhysRevD.98.116005`.
- Jenkins, Manohar, Stoffer, “Low-energy effective field theory below the electroweak scale: anomalous dimensions”, DOI `10.1007/JHEP01(2018)084`.
- Godfrey, DiStefano, “Identifiability of Model Parameters”, DOI `10.1016/B978-0-08-034929-9.50005-4`.
- Gustafson, “On Model Expansion, Model Contraction, Identifiability and Prior Information”, DOI `10.1214/088342305000000098`.
- Spall, Chin, “On system identification with nuisance parameters”, DOI `10.1109/ACC.1994.751793`.
- Haakestad, Skaar, “Causality and Kramers-Kronig relations for waveguides”, DOI `10.1364/OPEX.13.009922`.
- Lucarini, “Response Theory for Equilibrium and Non-Equilibrium Statistical Mechanics: Causality and Generalized Kramers-Kronig Relations”, DOI `10.1007/s10955-008-9498-y`.
- Hughes, “A theory of passive linear systems with no assumptions”, DOI `10.1016/j.automatica.2017.08.017`.
- Cassier, Milton, “Bounds on Herglotz functions and fundamental limits of broadband passive quasi-static cloaking”, DOI `10.1063/1.4989990`.

## §9 最弱环节

最弱环节：`G_pre` 的自然指定仍未解决。只要 PI 不能给出独立于 residual 的合法生成元来源，R4 会在“太宽全吸收”和“太窄误杀物理”之间摇摆。

## §10 下一步计划

下一步应做有限矩阵 toy：把 `r3_qnp_lint_toy.py` 的任意补列改为预注册生成元矩阵 `G_pre`，显式计算

```text
rank([J_M0, J_G]) and projection of r onto null([J_M0, J_G]^T)
```

若预注册物理生成元仍能加入 residual 方向，R4 判死；若 residual 在所有合法生成元下保留非零余空间投影，再进入 Round2。

需要 PI 投喂的文献方向：`model class naturality`, `prequential model checking`, `physical model structure identifiability`, `passive system realization constraints`, `EFT basis under field redefinition and measurement protocol`。
