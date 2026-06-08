# INSPECTOR 校对：NSF-FCS-2 A Round 1

结论：WARNING

A 报告可继续进入后续比较/综合，但必须显式保留以下弱点：`R2 ~ delta^2 G_T Q_L` 是结构性闭合/标度 ansatz，`Q_L ~ L^{1/2}` 是由 `S_T-2=R2/G_T` 的 `L=4..8` 小尺寸斜率反推的 capacity ansatz，`3/2-alpha` 只是 asymptotic 候选解释，不是当前报告已经推出或数值确认的结论。

## Q1. 量纲校对

PASS/WARNING。

1. `R2(L,delta)=c_2(L) delta^2 + c_4(L) delta^4 + O(delta^6)`：若 `delta` 为密度差，则无量纲；`R2` 与 `lambda_T''`、`G_T` 同为单位时间的二阶 transported-particle cumulant rate。因此 `c_2,c_4` 与 `R2` 同量纲，量纲匹配。
2. `R2(L,delta)=delta^2 G_T(L) Q_L+O(delta^4)`：若 `G_T` 定义为单位时间 conductance/cumulant-rate 量，`delta` 与 `Q_L` 无量纲，则右边为单位时间 cumulant rate，量纲匹配。这里的关键前提是 `Q_L` 被定义为无量纲容量型比值；A 已在 INSPECTOR_CHECK 中明确标注。
3. `Q_L ~ sum w_i^{bd} G_L(i,j) w_j^{bd} C_{ij}^{traffic}`：A 没有给出 `w_i^{bd}`、`G_L=(-L_0)^{-1}`、`C_{ij}^{traffic}` 的逐项单位归一化。因此该式只能作为结构示意，不能作为已完成量纲严格推导。A 已称其为 Green/resolvent 容量对象，但后续若要用它计算 `Q_L`，必须固定时间尺度和 kernel 归一化。
4. `beta_R=beta_G+beta_Q`、`beta_Q approx 1/2`、`beta_R approx 3/2-alpha` 均为指数关系，无 SI 单位问题。

未发现 `exp/sin/log/sinh` 等超越函数自变量量纲错误；报告中涉及 `log |R2|`、`slope log` 时应理解为对固定单位/同类数据的 log-log 斜率，未构成阻断。

## Q2. 符号/方向校对

PASS/WARNING。

1. `R2(delta)=R2(-delta)` 的方向结论依赖四个条件：local detailed balance、左右 reservoir 几何对称、observable 为左右反射偶量、finite-L 解析性。A 明确说明若端口定义、coupling 或 counting-field convention 破坏该偶性，则线性项可以出现。因此没有把偶性误写成无条件结论。
2. `R2/G_T approx delta^2 Q_L` 的方向可检验，且 A 使用 `S_T-2=R2/G_T` 的正斜率 `0.47..0.54` 支持 `Q_L` 随 L 增长。若 `G_T` 为正 conductance rate，则方向一致。
3. `beta_R=beta_G+beta_Q` 与表中数值一致：`0.540+0.5=1.040` 对 `1.009`，`0.108+0.5=0.608` 对 `0.621`，`-0.253+0.5=0.247` 对 `0.279`。未发现分子分母倒置或符号反向。
4. `3/2-alpha` 对 `alpha=1.5` 预测约 `0`，低于观测 `0.279`。A 已把它降级为 asymptotic 候选，并用 marginal/crossover 解释；这是 WARNING，不是 PASS 级结论。

## Q3. 循环论证校对

WARNING。

存在一个需要保留的循环/半循环风险：

1. `R2 ~ delta^2`：A 的主要论证来自对称性、equilibrium FDT 与解析性；PI bias scan 只作为 sanity check。这里不是明显循环论证。
2. `R2 ~ delta^2 G_T Q_L`：A 先定义/提出 `Q_L` 为使 `R2/G_T ~ delta^2 Q_L` 成立的容量对象，再用 `S_T-2=R2/G_T` 的斜率来支持 `Q_L ~ L^{1/2}`。若没有独立的 microscopic Green/resolvent 二次型计算，这一步本质上是解释性重参数化加 ansatz，而不是独立验证。
3. `Q_L ~ L^{1/2}`：目前由 `S_T-2` 的斜率 `0.469,0.512,0.532` 反推，且窗口只有 `L=4..8`。A 在“最弱环节”中明确承认它是 capacity ansatz，不是定理；标注充分，但后续不得把它当作已证明输入。

## Q4. 数量级鸿沟标记

WARNING。

1. `Q_L` 斜率用 `1/2` 近似解释三组数据，偏差分别约 `0.031,0.013,0.032`，在指数拟合层面很小。
2. `3/2-alpha` 的数量级在 `alpha=1.5` 处有明显张力：预测 `0` 或对数型 marginal，而有限窗口观测为 `0.279`。这不是多于 1 个数量级的数值鸿沟，但它是核心机制判断上的有限尺寸/交叉风险。
3. `m-tail=2000` 可能污染 reservoir-tail capacity 标度；A 已指出需要同时变化 `L` 与 `m-tail` 排除。该风险必须在 synthesis 中保留。

未发现 `10^N` vs `10^M` 且 `|N-M|>10` 的显式数量级冲突。

## Q5. 代数/极限退化/数值来源

WARNING。

### 5a. 代数展开

1. 偶性推出 `R2=c_2 delta^2+c_4 delta^4+...` 代数正确，前提是 finite-L 解析性成立。
2. `slope log |R2| = slope log G_T + slope log |S_T-2|` 在 `S_T-2=R2/G_T` 定义下代数恒等；表中三组数值相加吻合。
3. `beta_R=beta_G+beta_Q` 是上述恒等式在幂律 ansatz 下的直接结果；没有发现代数错误。
4. `g(alpha) approx 1-alpha` 推出 `beta_R approx g(alpha)+1/2 approx 3/2-alpha` 代数正确，但物理输入 `g(alpha) approx 1-alpha` 在 A 中标为粗略 intuition，不能升级为定理。

### 5b. 极限退化

1. `delta -> 0`：有限 L、反射偶性和 equilibrium FDT 下，`R2 -> 0` 且首个非零偶次项为 `delta^2`，退化合理。
2. 破坏左右反射或 counting convention：A 明确允许 `c_1 delta` 出现，退化合理。
3. `L -> infinity` 与 `delta -> 0` 交换：A 已提醒若先取无穷体积极限，解析性可能失效。该警告必要。
4. `alpha=1.5`：`3/2-alpha=0` 退化为 marginal/log 或 crossover 场景；A 的解释是候选，不是验证完成。

### 5c. 数值量级

1. 三组 `beta_G+1/2` 与 `beta_R` 的差异小于约 `0.04`，当前小窗口内可作为一致性迹象。
2. 但所有斜率来自 PI ledger 的 `L=4..8`，不是大 L 渐近拟合；数值支持级别应标为“小尺寸 ledger 经验支持”。

### 5d. 引用数值来源级别

WARNING。

1. 文献锚点提供 DOI/arXiv，但 A 明确说部分具体方程编号需 PI 后续核对原文 PDF；因此文献级支持是“方向/框架引用”，不是逐公式全文核实。
2. 具体数值如 `R2` 的 delta 斜率、reverse-bias check、`slope log G_T`、`slope log |S_T-2|` 均来自 PI ledger/bias scan。A 没有在本报告中给出 ledger 文件路径、参数表或可复算脚本引用；来源级别应标为“项目内部数值，待复算/定位原始文件”。
3. `m-tail=2000` 是关键数值设定，但未给出完整来源路径和复现实验矩阵；后续综合中必须保留这一 provenance 弱点。

## Q6. 综合判定

WARNING。

未发现必须 BLOCK 的量纲错误、方向反转、代数恒等式错误或明显数量级灾难。A 对三个重点弱点的标注基本清楚：

1. `R2 ~ delta^2 G_T Q_L`：已称为“最弱闭合形式/结构式”，可作为 ansatz/可检验结构继续推进，但不能当作 microscopic theorem。
2. `Q_L ~ L^{1/2}`：A 已明确说是从 `S_T-2` 数值斜率反推的 capacity ansatz，不是 Green 函数求和推出的定理。
3. `3/2-alpha`：A 已明确降级为 asymptotic 候选；在 `alpha=1.5` 处只能给 marginal/crossover 解释。

必须显式保留的弱点：

1. 补充 `Qhat_L=R2/(delta^2 G_T)` 的原始 ledger 路径、参数、误差和复算脚本，否则数值来源仍是内部摘要级。
2. 用独立 equilibrium Poisson/Green 二次型计算检验 `Q_L`，否则 `Q_L ~ L^{1/2}` 仍是对 `R2/G_T` 的重命名式解释。
3. 扩展 `L` 与 `m-tail` 双参数扫描，排除 reservoir-tail truncation 对 capacity 斜率的污染。
4. 对 `3/2-alpha` 只允许写成候选渐近图像；尤其不得用当前 `alpha=1.5, L=4..8` 数据声称其已被验证。
