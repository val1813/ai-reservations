# INSPECTOR_A_R4_round3

输入文件：`current/A/R4_round3.md`

角色：LP23-R4 Round3 A 路 INSPECTOR

范围限制：仅做量纲、符号方向、循环论证、量级鸿沟、代数验算和综合判定。不评价发表价值或先发覆盖；未读取 B 路输出。

## Q1. 量纲校对

### (R3-1)

\[
y=(H(i\omega_1),\ldots,H(i\omega_K))\in Y_K .
\]

- 左边 SI 单位：\(Y_K\) 中每个分量为同一观测通道响应单位，例如 impedance 通道为 \(\Omega\)，susceptibility 通道为对应 SI 响应单位。
- 右边 SI 单位：每个 \(H(i\omega_j)\) 为同一响应函数在频点 \(\omega_j\) 的取值，单位同 \(Y_K\)。
- 匹配：✅，前提是 \(Y_K\) 已按单一观测通道和单一响应单位定义。

### (R3-2)

\[
W_{\rm origin}^{\rm pass}
=({\rm channel},\Omega_K,{\rm units},\mu \ge 0, a,b,{\rm realization\ or\ approximation\ certificate})
\]

- 左边 SI 单位：证书 tuple，不是物理量等式。
- 右边 SI 单位：证书 tuple，包含通道、频点、单位、测度和系数。
- 匹配：✅，作为元数据/证书定义成立。
- 量纲备注：若后续用 \(a,b,\mu\) 进入 \(H(z)\)，则 \(a,b,\mu\) 的单位必须由 \(H\) 的响应单位和 \(z,t\) 的频率单位共同固定。

### (R3-3)

\[
H(z)=a+bz+\int_{\mathbb R}
\left({1\over t-z}-{t\over 1+t^2}\right)d\mu(t),
\quad b\ge 0,\quad \mu\ge 0 .
\]

- 左边 SI 单位：响应单位 \([H]\)，例如 \(\Omega\) 或 susceptibility 的 SI 响应单位。
- 右边 \(a\)：需为 \([H]\)。
- 右边 \(bz\)：若 \(z\) 是物理频率，\([z]={\rm s}^{-1}\)，则 \([b]=[H]\cdot{\rm s}\)。
- 积分核第一项 \(1/(t-z)\)：若 \(t,z\) 是物理频率，单位为 \({\rm s}\)。
- 积分核第二项 \(t/(1+t^2)\)：若 \(t\) 是物理频率，则 \(1+t^2\) 不能相加，量纲不成立；该项只有在 \(t\) 已无量纲化时才成立。
- 匹配：❌，输入文件未声明 \(t,z\) 已无量纲化，也未引入频率尺度 \(\omega_0\) 修正 \(1+t^2\)。

❌ 量纲错误：(R3-3)。若 \(z,t\) 对应 \(i\omega\) 的物理频率变量，左边为响应单位 \([H]\)，右边积分核含 \(1+t^2\) 的无量纲加法错误，积分项单位也未由 \(d\mu(t)\) 明确闭合。建议修正：显式声明 \(\zeta=z/\omega_0,\tau=t/\omega_0\) 为无量纲谱变量并重写 Herglotz 表示；或在公式中保留 \(\omega_0\)，例如把正则化项写成与 \(\tau\) 无量纲变量一致的形式，并声明 \(d\mu\)、\(a\)、\(b\) 的响应单位。

### (R3-4)

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
\]

- 左边 SI 单位：布尔值/谓词值，无量纲。
- 右边 SI 单位：布尔谓词的合取，无量纲。
- 匹配：✅。

### (R3-5)

\[
G_{\rm pass}(P)=\{c\mid \exists W:\ {\rm Verify}^{\rm pass}_P(c,W)=1\},
\quad
S_{\rm pass}(P)=\operatorname{span}G_{\rm pass}(P).
\]

- 左边 \(G_{\rm pass}(P)\)：\(Y_K\) 中合法列集合，元素单位为响应单位 \([Y_K]\)。
- 右边集合定义：\(c\in Y_K\)，单位为 \([Y_K]\)。
- 左边 \(S_{\rm pass}(P)\)：\(Y_K\) 的线性子空间。
- 右边 \(\operatorname{span}G_{\rm pass}(P)\)：同一 \(Y_K\) 内张成空间。
- 匹配：✅，前提是只对同一观测通道、同一单位的列取 span。

### (R3-6)

\[
{\rm Obs}^{\rm pass}_P(r)=[r]\in Y_K/S_{\rm pass}(P).
\]

- 左边 SI 单位：等价类/商空间元素，继承 \(Y_K\) 响应单位；若经 \(\Sigma^{-1/2}\) 白化后可转成无量纲 residual norm。
- 右边 SI 单位：\(Y_K/S_{\rm pass}(P)\) 中的等价类，继承同一响应单位。
- 匹配：✅。

### 超越函数自变量

输入公式中未出现 exp(), sin(), log(), sinh()。✅

## Q2. 符号/方向校对

### 方向结论 1

结论：若补列来自 fixed passive/causal LTI response，则 R4 在该单域内被成熟证书覆盖，应硬停止为新物理命题，最多降级为证书校验工具。

- 极限/边界 1：只允许固定 passive cone / realization family / bandlimit / model order，且这些在 residual 前固定。此时合法集合 \(G_{\rm pass}(P)\) 不依赖 \(r\)，residual 只能最后投影到 \(Y_K/S_{\rm pass}(P)\)。方向支持“降级为工具而非 residual 后造新 witness”。
- 极限/边界 2：允许任意高阶 realization、任意正测度或任意密 B-spline knots。有限 \(Y_K\) 中自由度可吸收 residual，方向支持“必须预注册 cutoff，否则不能给出非 oracle obstruction”。
- 方向判定：✅。

### 方向结论 2

结论：若 Herglotz measure / realization / density / kernel 参数是在看到 residual 后拟合，且无预注册、独立校准或 holdout，则 `W_nonoracle` 失败。

- 极限/边界 1：参数生成完全独立于 residual，且有 timestamp/hash/blind split/holdout。此时 `W_nonoracle` 可成立。
- 极限/边界 2：参数完全由 residual 反推出。此时即使 passive/causal 成立，来源独立性仍失败。
- 方向判定：✅。

### 方向结论 3

结论：`physical admissibility != non-oracle provenance`。

- 极限/边界 1：补列满足 passive/causal 但由 residual 后拟合。物理合法性成立，non-oracle 失败。
- 极限/边界 2：补列预注册但不满足 passive/causal。non-oracle 来源可成立，物理合法性失败。
- 方向判定：✅。

未发现比值分子分母放反或负号方向被吃掉的问题。

## Q3. 循环论证校对

### 检验/验证操作 1：\(G_{\rm pass}(P)\) 的生成

- 检验数据如何生成：由 \({\rm Verify}^{\rm pass}_P(c,W)=1\) 的证书谓词筛选候选列。
- 输入假设：\(W_{\rm pre}\)、通道、单位、cutoff、证书类型和 non-oracle 记录在 residual 前固定。
- 是否由输入假设生成检验数据：若严格按文中要求，\(G_{\rm pass}(P)\) 不依赖 \(r\)，不构成循环。
- 判定：✅。

### 检验/验证操作 2：residual 投影 \({\rm Obs}^{\rm pass}_P(r)\)

- 检验数据如何生成：把 residual 等价类投影到 \(Y_K/S_{\rm pass}(P)\)。
- 输入假设：\(S_{\rm pass}(P)\) 已由 residual 前证书闭包确定。
- 是否由输入假设生成检验数据：若 \(S_{\rm pass}(P)\) 在 residual 前固定，则不是循环；若 \(S_{\rm pass}(P)\) 或 cutoff 由 residual 后调参，则循环。
- 判定：⚠️ 条件性警告。文本已标出该风险，但未给出实际可审计预注册对象。

### 检验/验证操作 3：toy checker 边界判断

- 检验数据如何生成：使用脚本结构抽象判断 toy checker 是否仅拒绝显式 oracle 列。
- 输入假设：toy checker 的 source/preregistered/passive_decaying_kernel 等字段代表形式边界，不代表真实物理证书。
- 是否由输入假设生成检验数据：这是形式边界检查，不是用 toy checker 自证真实 non-oracle provenance。
- 判定：✅，作为边界描述不构成循环。

未发现明确循环论证阻断；存在预注册/holdout 未实际给出时的条件性循环风险。

## Q4. 量级鸿沟标记

输入推导未给出 \(10^N\) vs \(10^M\) 的数值量级比较，也未给出具体参数代入估算。

- \(|N-M|>10\)：未发现。
- \(|N-M|>50\)：未发现。

判定：✅。

## Q5. 代数验算

### 5a. 逐步展开

本轮公式主要是定义、集合构造和谓词合取，没有积分求值、级数展开、矩阵乘法展开或近似展开。

- (R3-1)：有限频采样向量定义，代数成立。
- (R3-2)：证书 tuple 定义，代数无展开项。
- (R3-3)：标准 Herglotz 型表示的形式写法；代数结构本身未展开，但存在 Q1 中的物理量纲归一化缺失。
- (R3-4)：布尔谓词合取，符号结构一致。
- (R3-5)：合法列集合与 span 定义，代数结构一致。
- (R3-6)：商空间等价类定义，代数结构一致。

### 5b. 极限退化

- 空合法列极限：若 \(G_{\rm pass}(P)=\varnothing\)，则 \(S_{\rm pass}(P)=\{0\}\)，\({\rm Obs}^{\rm pass}_P(r)=[r]\in Y_K/\{0\}\cong Y_K\)。退化合理。✅
- 全空间吸收极限：若 \(S_{\rm pass}(P)=Y_K\)，则 \(Y_K/S_{\rm pass}(P)=\{0\}\)，所有 residual 等价类为零。退化合理，并支持文中“无限自由度容易吸收 residual，必须预注册 cutoff”的方向。✅
- residual 为零极限：若 \(r=0\)，则 \([r]=0\) 在商空间中为零类。退化合理。✅
- 非 oracle 失败极限：若 \({\rm NonOracle}(W_{\rm nonoracle})=0\)，则 (R3-4) 合取为 0，候选 \(c\) 不进入 \(G_{\rm pass}(P)\)。退化合理。✅

### 5c. 数值量级验证

输入未声明具体数值或量级估算；无可代入参数。

判定：✅，无数值量级待验算。

### 5d. 引用数值来源级别

输入只列出文献 DOI 和 arXiv 编号，没有使用来自文献的具体数值常数或实验参数。

判定：✅，无具体数值来源待分级。

## Q6. 综合判定

⛔ INSPECTOR阻断：公式 (R3-3) 在接入物理频率变量 \(z=i\omega\)、\(t\in\mathbb R\) 时未声明无量纲化，导致 \(1+t^2\) 的加法和积分项单位不成立。修正后重新提交。

⚠️ INSPECTOR警告：`W_nonoracle`、holdout 和 cutoff 的非循环性依赖可审计预注册对象；输入文本已提出要求，但本轮没有给出实际 timestamp/hash/blind split/holdout 文件。因此相关投影结论只能作为条件性 schema，不得当作已完成的非循环验证。

综合结论：除 (R3-3) 的量纲归一化阻断外，未发现符号方向反转、数量级鸿沟、代数展开错误或明确循环论证阻断。
