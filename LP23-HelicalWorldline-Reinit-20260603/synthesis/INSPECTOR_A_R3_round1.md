# INSPECTOR_A_R3_round1

角色：LP23-R3 Round1 A 路 INSPECTOR  
输入：`current\A\R3_round1.md`  
范围：仅做量纲、符号方向、循环论证、量级鸿沟、代数验算和综合判定；不评价发表价值或先发覆盖；未读取 B 路输出。

## Q1. 量纲校对

关键公式逐项检查：

- (A0) `\mathcal D=(X,Y;\mathcal G,\mathcal T,\mathcal B,\mathcal N,\mathcal H)`
  - 左边 SI 单位：资料/结构对象，无单一 SI 单位。
  - 右边 SI 单位：`X,Y` 携带观测变量单位；五类选择族为结构对象。
  - 匹配：✅。该式是对象定义，不是物理量等式。

- (A1) `\mathfrak A=\langle \mathcal G,\mathcal T,\mathcal B,\mathcal N,\mathcal H\rangle`
  - 左边 SI 单位：群胚/半群胚结构，无 SI 基本单位。
  - 右边 SI 单位：生成元族的代数闭包结构，无 SI 基本单位。
  - 匹配：✅。

- (A2) `r_s\in \Gamma(\mathcal M,\mathcal R)`
  - 左边 SI 单位：观测 residual 单位。
  - 右边 SI 单位：以 residual bundle 为值的截面，继承 `\mathcal R` 纤维单位。
  - 匹配：✅。

- (A3) `r_s\mapsto r_{\alpha s}=\rho(\alpha)r_s+\delta_\alpha q_s`
  - 左边 SI 单位：residual 单位。
  - 右边 SI 单位：`\rho(\alpha)r_s` 为 residual 单位；若 `\delta_\alpha q_s` 被定义为 residual 复形中的 coboundary，则同为 residual 单位。
  - 匹配：✅，但依赖文中假设“template/bridge/nuisance/history 重新参数化生成 coboundary 型 residual 变化”。

- (A4) `\operatorname{Obs}(r):=[r]\in H^k([\mathcal M/\mathfrak A],\mathcal R_\rho)` 或 `H^k_{\mathfrak A}(\mathcal M,\mathcal R_\rho)`
  - 左边 SI 单位：带系数上同调类；不是新 SI 基本单位。
  - 右边 SI 单位：由系数系统 `\mathcal R_\rho` 携带 residual 单位。
  - 匹配：✅。

- (A5) `\operatorname{Obs}(r)\ne0 => candidate physical degree of freedom; \operatorname{Obs}(r)=0 => diagnostic only`
  - 左边 SI 单位：上同调类的零/非零判别。
  - 右边 SI 单位：分类结论，无 SI 单位。
  - 匹配：✅。这是判别规则，不是量纲等式。

- (A6) `C^0 \xrightarrow{d_0} C^1 \xrightarrow{d_1} C^2`
  - `C^0`：允许重参数化方向，单位取决于参数坐标。
  - `C^1`：residual 空间，单位为 residual 单位。
  - `C^2`：一致性约束空间，单位由约束定义决定。
  - `d_0` 必须携带“residual / 参数”型单位；`d_1` 必须携带“约束 / residual”型单位。
  - 匹配：✅，作为线性映射链可量纲自洽。

- (A7) `\iota^*:H^1(C^\bullet_{\mathfrak A})\to H^1(C^\bullet_{\mathfrak A'})`
  - 左边 SI 单位：`H^1` residual 类。
  - 右边 SI 单位：`H^1` residual 类。
  - 匹配：✅，若映射存在且保持系数系统单位。

- (A8) `\Pi_{\perp \operatorname{im}d_0}r`
  - 左边 SI 单位：residual 单位。
  - 右边 SI 单位：正交投影后的 residual 分量。
  - 匹配：✅。

超越函数自变量检查：全文关键公式未使用 `exp()`、`sin()`、`log()`、`sinh()` 等超越函数。✅

Q1 判定：✅ 量纲未发现阻断错误。

## Q2. 符号/方向校对

- (A3) 方向：允许选择 `\alpha` 作用后，residual 变为表示作用项加 coboundary 项。极限检查：若 `\alpha=e` 且 `\delta_e q_s=0`，则 `r_{\alpha s}=r_s`，方向正确。✅

- (A5) 方向：`Obs(r)=0` 时 residual 为可吸收/可平凡化对象，判为 diagnostic；`Obs(r)\ne0` 时仅给出 candidate 资格。该方向与后文“反向不成立”一致。✅

- 定理 A 条件 1-2 到结论方向：若允许选择只改变 `\operatorname{im}d_0` 中的代表元，且 `r\in\ker d_1`，则 `[r]\in \ker d_1/\operatorname{im}d_0` 是可定义的候选类。方向正确，但需 Q5 中复形条件支撑。⚠️

- (A7) 扩张方向：文中设 `\mathcal T'\supseteq\mathcal T`、`\mathcal B'\supseteq\mathcal B`、`\mathcal H'\supseteq\mathcal H`，即允许方向增加。若 `C^0` 因新增可吸收列而变大，则 `\operatorname{im}d_0` 通常变大，`H^1=\ker d_1/\operatorname{im}d_0` 通常应由较小允许族下的类映到“进一步取商后”的类，或通过压力测试重新计算其像是否为零。文中写作 `\iota^*:H^1(C^\bullet_{\mathfrak A})\to H^1(C^\bullet_{\mathfrak A'})` 可以表达此方向，但使用星号 `\iota^*` 通常表示反变拉回，符号方向有歧义。
  - 结论：⚠️ 符号方向警告。建议改名为 `\iota_*`、`j_{\mathfrak A\to\mathfrak A'}` 或明确说明这是“扩张后再取商的自然投影/诱导映射”，不是通常意义的反变 pullback。

Q2 判定：⚠️ 有符号方向歧义，但未单独构成阻断。

## Q3. 循环论证校对

- 文献检索段：未作为代数验证数据使用，不构成循环论证检查对象。

- (A4)-(A5)：先定义 obstruction 类，再以零/非零作筛选规则。这是定义性判别，不是用输出证明输入；未发现循环。✅

- 定理 A 条件 3：把“对每个允许扩张仍非零”作为通过条件，再推出“不是当前允许选择及扩张下的吸收伪影”。该结论基本是条件 3 的直接展开，属于筛选准则定义，不是独立证明。若文本把它称为可执行判据，可以接受；若声称由更弱条件推出，则会循环。
  - 当前判定：⚠️ 证明增量较小，条件 3 与结论高度同义，但未发现“验证数据由待证假设生成”的硬循环。

- (A8) 投影验证：输入为给定 `d_0` 与 `r`，输出为正交残差。若 `d_0` 的列空间由同一假设任意扩张到包含 `r`，则会变成平凡吸收；但文中限定“合法扩张压力测试”，因此是边界条件问题，不是形式循环。

Q3 判定：⚠️ 有“条件即结论”的弱证明风险；未发现硬循环阻断。

## Q4. 量级鸿沟标记

全文未给出 `10^N` vs `10^M` 的数量级比较，也未给出实验数值估算。DOI、年份、公式编号不属于量级估算。

Q4 判定：✅ 无需标记量级鸿沟。

## Q5. 代数验算

### 5a. 逐步展开

- (A6) 声称为 residual 复形：
  \[
  C^0 \xrightarrow{d_0} C^1 \xrightarrow{d_1} C^2.
  \]
  要定义 `H^1(C^\bullet_{\mathfrak A})`，必须满足
  \[
  d_1\circ d_0=0,
  \]
  从而 `\operatorname{im}d_0\subseteq\ker d_1`，并有
  \[
  H^1=\ker d_1/\operatorname{im}d_0.
  \]
  输入文件只说 `C^2` 为一致性约束、条件 1 为允许选择改变落在 `\operatorname{im}d_0`、条件 2 为 `d_1r=0`，但没有明示或证明 `d_1d_0=0`。

  ❌ 代数错误/缺口：`H^1(C^\bullet_{\mathfrak A})` 和 `[r]` 的定义依赖 `d_1\circ d_0=0`。若该条件不成立，则允许重参数化可能改变一致性约束，`[r]` 不一定是良定义的上同调类。建议修正：在定理 A 假设中加入并验证 `d_1d_0=0`，或把结构降级为“两步线性筛选”而不称为上同调复形。

- (A8) `\Pi_{\perp \operatorname{im}d_0}r`：
  正交投影需要给定 `C^1` 上的内积/度量/权重矩阵。输入文件未说明投影所用内积。若 residual 各分量单位不同，还需要先白化或指定带单位的权重。

  ⚠️ 代数警告：投影算子未完全定义。建议补充 `C^1` 的内积或噪声协方差权重，并说明投影前的单位归一化。

- (A7) 扩张诱导映射：
  新增 template/bridge/history 列通常改变 `C^0`、`d_0`，也可能改变 `C^1` 或 `d_1`。若复形本身改变，`H^1(C^\bullet_{\mathfrak A})\to H^1(C^\bullet_{\mathfrak A'})` 的诱导映射存在需要链映射条件：
  \[
  f^1 d_0 = d'_0 f^0,\qquad f^2 d_1 = d'_1 f^1.
  \]
  输入文件未给出这些链映射条件。

  ❌ 代数错误/缺口：自然扩张映射未被定义到足以保证 `\iota^*[r]` 良定义。建议补充扩张 `\mathfrak A\to\mathfrak A'` 对 `C^0,C^1,C^2` 的链映射，或把条件 3 改写为“在每个扩张后的复形中重新计算 `[r]_{\mathfrak A'}` 是否为零”。

### 5b. 极限退化

- 自由极限：若允许族为空或 `d_0=0`，则 `H^1=\ker d_1`，(A8) 退化为保留全部满足一致性的 residual。✅

- 全吸收极限：若 `r\in\operatorname{im}d_0`，则 `[r]=0` 且 `\Pi_{\perp\operatorname{im}d_0}r=0`，结论退化为 diagnostic only。✅

- 不一致极限：若 `d_1r\ne0`，条件 2 失败，`r` 不进入 `H^1` 候选类。✅

- 扩张极限：若新增合法列使 `r\in\operatorname{im}d'_0`，则扩张后类应为零。该方向与文字结论一致，但依赖上面的链映射/重算定义。⚠️

### 5c. 数值量级验证

本轮未声称具体数值或数量级估算。✅

### 5d. 引用数值来源级别

本轮没有用于代数验算的具体数值。文献 DOI 和年份不是数值输入。✅

Q5 判定：❌ 存在代数阻断：

1. 未给出 `d_1\circ d_0=0`，导致 `H^1` 与 `[r]` 的上同调类定义不充分。
2. 扩张诱导映射 (A7) 缺少链映射/重算定义，导致 `\iota^*[r]` 是否良定义无法验算。

## Q6. 综合判定

⛔ INSPECTOR阻断：定理 A 的核心对象 `H^1(C^\bullet_{\mathfrak A})`、`[r]` 与扩张下的 `\iota^*[r]` 依赖未写出的复形条件和链映射条件。当前文本没有明示/证明 `d_1\circ d_0=0`，也没有定义扩张 `\mathfrak A\to\mathfrak A'` 如何诱导良定义的上同调映射。因此后续结论不得建立在 (A6)-(A7) 的当前形式之上。

修正后重新提交建议：

1. 在定理 A 假设中加入 `d_1d_0=0`，并解释每类 gauge/template/bridge/nuisance/history 重参数化为何不破坏一致性约束。
2. 对每个扩张 `\mathfrak A\to\mathfrak A'`，明确给出链映射条件，或取消 `\iota^*` 表述，改为“在扩张后的复形中重新计算 `[r]_{\mathfrak A'}`”。
3. 为 (A8) 指定 `C^1` 上的内积/权重矩阵；若 residual 分量单位不同，先说明白化或单位归一化方案。
