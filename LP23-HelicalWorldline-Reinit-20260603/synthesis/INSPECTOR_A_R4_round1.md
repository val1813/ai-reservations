# INSPECTOR_A_R4_round1

角色：LP23-R4 Round1 A 路 INSPECTOR  
输入文件：`current\A\R4_round1.md`  
输出日期：2026-06-03  
范围：仅做量纲、符号方向、循环论证、量级鸿沟、代数验算和综合判定；不评价发表价值或先发覆盖；未读取 B 路输出。

## Q1. 量纲校对

关键公式逐项检查：

| 公式 | 左边 SI/单位类型 | 右边 SI/单位类型 | 匹配 |
|---|---|---|---|
| `P=(X,Y,H,M0,Q,G,E,K,L)` | protocol 结构对象 | 各结构组件元组；其中 `Y` 携带观测量 SI 单位，其他项为集合/关系/规则/泛函 | ✅ |
| `C(P)=mu C . cl_{E,K}(M0 union {g(M) | M in C, g in G, Q[g(M)]=true})` | 模型类/模型闭包，不是物理量等式 | `M0` 与 `g(M)` 同为模型对象；`cl_{E,K}` 返回经等价关系与截断规则处理后的模型类 | ✅ |
| `\bar C(P)=C(P)/E` | 商模型类 | 模型类按冗余等价关系取商 | ✅ |
| `F_M : Theta_M -> Y` | 预测映射 | 参数空间到观测空间；输出携带 `Y` 的观测 SI 单位 | ✅ |
| `r=y_obs-F_{M0}(\hat theta_0) in Y` | residual，观测单位 | `y_obs` 与 `F_{M0}` 同在 `Y`，相减后仍为 `Y` 单位 | ✅ |
| `S_C(P)=closure span { Im dF_M | M in C(P), allowed finite extensions under K } subset Y` | `Y` 中可吸收方向子空间 | `dF_M` 作用在参数增量后给出 `Y` 中切向输出；线性组合系数应为无量纲 | ✅ |
| `Obs_P(r)=[r] in Y/S_C(P)` | residual 商类 | `r` 与 `S_C(P)` 同属 `Y`，商空间继承 residual 单位类型 | ✅ |
| `F_{M'}(x,theta,alpha)=F_M(x,theta)+alpha T_r(x)` | 观测输出单位 | `F_M` 为观测单位；若 `T_r=r` 为观测单位且 `alpha` 无量纲，则加法合法 | ✅ |
| `r in S_C(P), hence Obs_P(r)=0` | residual 子空间成员关系与商零类 | `r` 与 `S_C(P)` 同单位；商零类判定合法 | ✅ |
| `codim_P=dim(Y_K/S_C(P)_K)` | 无量纲整数/维数 | 有限截断观测空间的商维数 | ✅ |
| `rank([J_M0,J_G])` 与 `projection of r onto null([J_M0,J_G]^T)` | 秩为无量纲整数；投影为 residual 分量 | 若 `J` 列已按 residual 单位或白化空间统一，则矩阵秩/零空间计算合法 | ✅，需后续显式白化/权重约定 |

超越函数自变量检查：关键公式未使用 `exp()`、`sin()`、`log()`、`sinh()` 等超越函数；无自变量量纲问题。

Q1 判定：✅ 未发现量纲阻断错误。警告：后续数值化时需显式说明 `alpha` 为无量纲，并说明 `J`/投影计算是否在白化后的无量纲空间中执行。

## Q2. 符号/方向校对

方向性结论检查：

| 结论 | 极限/代入检查 | 方向判定 |
|---|---|---|
| R4 对象不是 residual 本身，而是 residual 在合法补全闭包商空间中的类 | 若 `r in S_C(P)`，则 `[r]=0`，residual 被吸收；若 `r notin S_C(P)`，则 `[r] != 0`，才有 obstruction 资格 | ✅ |
| `Obs_P(r)=0` 时 residual 不能作为新自由度证据 | 代入商空间定义：零类即属于可吸收子空间 | ✅ |
| `Obs_P(r)!=0` 且对 `E` 中重参数化不变时，才有 protocol-closure obstruction 资格 | 若 gauge/field/protocol reparameterization 可把类变为零，则不是不变量；方向与文本一致 | ✅ |
| No-go A：允许事后 residual-shaped template 时 obstruction 恒为零 | 取 `T_r=r`，`F_{M'}=F_M+alpha T_r`，对 `alpha` 的切向方向含 `r`；取 `alpha=1` 可吸收 residual，故 `r in S_C(P)` | ✅ |
| `codim_P=0` 时任意 residual 都无 obstruction 资格 | `Y_K/S_C(P)_K` 维数为 0 等价于有限截断中无余空间方向 | ✅ |
| `codim_P>0` 时才讨论 residual 在余空间上的投影 | 商空间非零才存在可区分余方向 | ✅ |

未发现分子分母放反、正负号丢失或方向相反问题。

Q2 判定：✅ 符号方向通过。

## Q3. 循环论证校对

验证/检查类操作逐项检查：

| 操作 | 输入假设 | 检查/推导来源 | 循环性 |
|---|---|---|---|
| `C(P)` 闭包定义 | 预先给定 `P=(X,Y,H,M0,Q,G,E,K,L)` | 按生成元、约束、等价关系和截断规则形成最小闭包 | ✅ 无实验数据回灌 |
| `Obs_P(r)=[r] in Y/S_C(P)` | 给定 `r` 与预先构造的 `S_C(P)` | 商空间成员关系 | ✅ 定义性判定，不是用结论生成数据 |
| No-go A | 假设 `G_template` 或 `G_nuisance` 允许事后加入 `T_r=r` | 由线性补列直接推出 `r in S_C(P)` | ✅ 条件 no-go；不是独立验证同一假设 |
| `G_pre,Q_pre,E_pre,K_pre` 必须先于 residual 确定 | 输入为协议预注册条件 | 用于排除事后吸收 | ✅ 该要求正是反循环约束 |
| toy 下一步 `rank([J_M0,J_G])` 与余空间投影 | 输入为预注册生成元矩阵与 residual | 线性代数秩/投影计算 | ✅ 前提是 `J_G` 不由目标 residual 事后构造 |

警告：若后续 toy 中的 `G_pre`、阈值、白化权重或 template 库在观察 residual 后调参，则会退化为循环/过拟合检查；当前文本已把这类情形列为需要排除的病态规则。

Q3 判定：✅ 未发现硬循环论证。

## Q4. 量级鸿沟标记

全文未给出用于推导的 `10^N` vs `10^M` 数量级比较，也未给出实验数值代入或物理参数量级估算。DOI、年份、公式编号不属于数量级估算。

Q4 判定：✅ 无量级鸿沟需要标记。

## Q5. 代数验算

### 5a. 逐步展开

1. 最小闭包定义：
   \[
   C(P)=\mu C.\; cl_{E,K}(M_0\cup\{g(M)\mid M\in C,\ g\in G,\ Q[g(M)]=true\}).
   \]
   该式是递归闭包/最小不动点定义。代数上需要闭包算子对模型类包含关系单调，且 `K` 截断不破坏单调性。文本未显式证明单调性，但在“生成元闭包 + 等价商 + 有限截断保留代表元”的自然读法下可成立。
   判定：⚠️ 形式完备性警告；建议后续写明不动点算子单调，或改写为有限迭代闭包算法。

2. 商空间 obstruction：
   \[
   S_C(P)\subset Y,\qquad Obs_P(r)=[r]\in Y/S_C(P).
   \]
   若 `S_C(P)` 是线性子空间，则商类定义合法：
   \[
   Obs_P(r)=0 \iff r\in S_C(P).
   \]
   文本把 `S_C(P)` 定义为 `closure span`，满足线性子空间要求。代数方向正确。

3. No-go A：
   \[
   F_{M'}(x,\theta,\alpha)=F_M(x,\theta)+\alpha T_r(x).
   \]
   对 `alpha` 求切向：
   \[
   \partial_\alpha F_{M'}=T_r.
   \]
   若 `T_r=r` 且该扩展被 `Q` 判为合法、未被 `K` 排除，则：
   \[
   r\in \operatorname{Im}dF_{M'}\subset S_C(P),
   \]
   因而：
   \[
   Obs_P(r)=[r]=0.
   \]
   代数展开正确。

4. 余维计算：
   \[
   codim_P=\dim(Y_K/S_C(P)_K).
   \]
   若 `codim_P=0`，则 `Y_K=S_C(P)_K`，所有有限截断 residual 均落在可吸收空间中；若 `codim_P>0`，才存在非零余空间方向。代数方向正确。

5. 下一步矩阵 toy：
   \[
   rank([J_{M0},J_G])
   \]
   用于计算可吸收切向空间秩；投影到
   \[
   null([J_{M0},J_G]^T)
   \]
   用于检查 residual 的正交余分量。该线性代数方向正确。若存在噪声协方差或不同单位分量，应使用白化后的 `W[J_M0,J_G]` 与 `Wr`，否则普通欧氏正交投影未必有物理意义。

### 5b. 极限退化

| 公式/结构 | 极限 1 | 极限 2 | 判定 |
|---|---|---|---|
| `Obs_P(r)=[r] in Y/S_C(P)` | `S_C(P)=0` 时，`Obs_P(r)=[r] in Y`，所有非零 residual 保留 | `S_C(P)=Y` 时，`Obs_P(r)=0`，所有 residual 被吸收 | ✅ |
| `F_{M'}=F_M+alpha T_r` | `alpha=0` 回到原模型 `F_M` | `alpha=1,T_r=r` 给出 residual-shaped 吸收方向 | ✅ |
| `codim_P` | `codim_P=0` 无 obstruction 余方向 | `codim_P>0` 可讨论余空间投影 | ✅ |
| `K` 有限截断 | 有限带宽/采样/memory depth 下商维数可计算 | 无限维且无截断时可能不可稳定估计 | ✅，与文本硬边界一致 |

### 5c. 数值量级验证

当前输入未声明需要代入验算的实验数值、物理参数数值或数量级估算。无数值偏差可判定。

### 5d. 引用数值来源级别

文本中的具体数字主要为 DOI、年份、维数标签和轮次编号，不作为推导数值输入。无“无来源数值”影响代数验算。

Q5 判定：✅ 代数验算未发现阻断错误。⚠️ 警告：`mu` 不动点的单调性、`dF_M` 的取点/线性化约定、`closure` 的拓扑或有限截断、以及投影所用白化/内积，需要在后续可计算 toy 中显式写出。

## Q6. 综合判定

✅ INSPECTOR通过。A 路 R4 Round1 的核心机械结构 `C(P)`、`S_C(P)`、`Obs_P(r)`、residual-shaped template no-go、`codim_P` 与后续 rank/nullspace 方向，在量纲、符号方向、循环论证、量级鸿沟和代数验算层面未发现阻断错误。

⚠️ INSPECTOR警告：后续若把这些对象用于实际 toy 或 protocol，必须显式标注 `G,Q,E,K` 的预先给定性，写明不动点/闭包的可计算规则，指定 `dF_M` 的线性化基点与投影内积/白化方案。可继续，但不能把事后 residual-shaped 生成元或事后阈值调参当作机械检验通过。
