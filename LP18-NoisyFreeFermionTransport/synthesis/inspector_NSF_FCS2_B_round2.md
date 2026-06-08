# INSPECTOR-B Report: NSF-FCS-2 Round 2 B

校对对象：`current\B\NSF-FCS-2_round2_B.md`

边界：未读取 A 输出；仅对 B Round 2 文本及同一 B 侧上一轮文本做声张缩水对比。不做先发文献 REVIEWER 审查。

## Q1. 量纲校对

关键公式：

1. `M_FDT = { ledger models with lambda_T'' - 2 G_T = 0 }`（第 13 行）
   - 左边：模型集合/流形定义，无 SI 单位。
   - 右边约束：`lambda_T''` 与 `G_T` 必须同单位。上一轮 B 明确二者在 ledger 中均为 `1/time`，故 `lambda_T'' - 2G_T` 为 `1/time`。
   - 匹配：通过。

2. `R2 = lambda_T'' - 2 G_T`（第 17 行）
   - 左边：`R2` 单位 `1/time`。
   - 右边：`1/time - 1/time = 1/time`。
   - 匹配：通过。

3. `R2/G_T` 是无量纲曲率响应（第 29 行）
   - 左边：`(1/time)/(1/time) = 1`。
   - 右边：作为无量纲响应/坐标可成立。
   - 匹配：通过。

4. `R2/G_T = K_delta(...) delta^2 + K_A(...) A + K_deltaA(...) delta A + higher orders`（第 33 行）
   - 左边：无量纲。
   - 若 `delta` 与 `A` 均无量纲，则 `K_delta`、`K_A`、`K_deltaA` 均应无量纲。
   - 匹配：形式上通过。
   - 警告：文本没有在 Round 2 B 内重申 `A` 无量纲；上一轮 B 有明示。建议下一轮在公式旁补一句。

5. `R2/G_T = c0 + c_delta delta^2 + c_A A + c_deltaA delta A`（第 109 行）
   - 左边：无量纲。
   - 若 `delta,A` 无量纲，则 `c0,c_delta,c_A,c_deltaA` 均无量纲。
   - 匹配：形式上通过。

超越函数检查：本文件无 `exp()`、`sin()`、`log()`、`sinh()` 公式自变量需要校对。第 41、74 行的 "log drift" 是模型名称/拟合类别，不是显式函数公式。

## Q2. 符号/方向校对

1. Density-bias 路径 `rho_left = rho_bar - delta/2`, `rho_right = rho_bar + delta/2`（第 23 行）
   - `delta -> -delta` 时左右 reservoir 互换。
   - 与第 24、38、61 行的反向 bias/even-in-delta 声称方向一致。
   - 通过。

2. `R2 ~ delta^2` 与 "no detectable odd-in-delta contamination"（第 37-38 行）
   - `delta -> -delta` 时 `delta^2` 不变。
   - 方向与 even-in-bias 声称一致。
   - 通过。

3. `reversible_side`: `delta=0` 无 `A`-linear residual（第 53、113 行）
   - 与上一轮 B 的 equilibrium/FDT sanity control 声称一致：同侧 in/out 同乘不应产生 FDT residual。
   - 通过。

4. `nonLDB_site_skew`: `delta=0` 可出现 `A`-linear residual（第 54、114 行）
   - 方向上可作为非 LDB 法向扰动预测，但与上一轮 B 的局部展开 `R2(delta,A)=c20 delta^2 + c02 A^2 + c11 delta A + ...` 存在阶次变化。
   - 警告：如果 `A -> -A` 的 site-skew protocol 仍有某种反演/左右交换对称，则领先项可能是 `A^2` 而不是 `A`。Round 2 B 没有说明为什么本轮从 `c02 A^2` 改成 `c_A A`。下一轮需显式给出对称性破缺理由，或把拟合式改成同时比较 `A` 与 `A^2`。

5. "K_delta(L) changes substantially under LDB-preserving traffic factor" 是危险结果（第 57 行）
   - 方向正确：若可逆 activity 改变 density-bias curvature，则清洁 NESS 曲率解释被污染。
   - 通过。

## Q3. 循环论证校对

检查对象：

1. 第 35-41 行用 Round 2 结果支持 curvature residual model。
   - 输入假设：FDT residual 可被视为离开 FDT manifold 的 normal coordinate。
   - 检验数据：raw `delta^2`、reverse-bias evenness、FDT normalization、AIC log drift。
   - 风险：这些数据支持 "不是简单归一化/奇次污染 artifact"，但不能单独证明信息几何意义上的 "normal curvature"。
   - 结论：非阻断；需把 "second normal curvature" 改写为 "can be modeled as / operationally measured as curvature-like response"，直到有独立 metric/projection 定义。

2. 第 90-96 行称 redirect subclaim "absorbs all Round 2 fixes naturally"。
   - 这是解释性整合，不是数值验证。
   - 未发现用模型假设生成同一数据再称其验证模型的硬循环。
   - 警告：若下一轮把 "absorbs naturally" 升级为 "证明几何曲率框架"，会形成循环论证。

3. 第 117 行称最小测试区分 curvature residual 与 kinetic artifact。
   - 该测试包含 reversible 与 nonLDB 两类外部扰动，能提供非同源验证。
   - 通过。

## Q4. 数量级鸿沟标记

显式数量级/数值：

1. `rho_bar=0.4,0.5,0.65`（第 24 行）：密度范围合理，无数量级鸿沟。
2. `L=4..8`, `L=4..7`, `L=4..6`（第 71-73 行）：B 正确标记为 small-L empirical evidence；无夸大。
3. `delta = 0, 0.02`; `A = 0, 0.05`; `alpha=0.5,1.0`; `rho_bar=0.5`（第 102-105 行）：均为无量纲小参数/枚举设定；无数量级鸿沟。
4. Score `8.4/10`（第 88 行）：没有计算来源，是主观评分。
   - 警告：若用于矩阵打分或候选排序，必须标注为 B 主观评分，不能当作计算结果。

未发现 `10^N` vs `10^M` 跨越超过 10 个数量级的未标注比较。

## Q5. 代数/数值来源校对

1. 代数展开第 33 行
   - 若 `R2/G_T` 关于小参数 `(delta,A)` 可展开，则常数项默认为 0，`delta` 的奇次项因 reverse-bias evenness 被压制，保留 `delta^2` 合理。
   - 警告：没有写出为什么 `A` 可有线性项而 `delta` 不可有线性项。需要协议对称性说明。

2. 拟合式第 109 行
   - 与第 33 行一致，但作为实验设计只有 `A=0,0.05` 两点，无法区分 `A` 线性项与小窗口二次项。
   - 警告：若目标是判定 `c_A`，至少需要 `A=+0.05,-0.05` 或多幅度；否则 `A`-linear residual 的声称来源不足。

3. AIC/model comparison 声称第 41、74 行
   - 文本称 "AIC comparison says ... log drift, not power law"。
   - B 文件内未给 AIC 表、数值、文件路径或差值。
   - 警告：作为综述性引用可保留；作为证据链节点时需附表或来源路径。

4. `8.4/10` 第 88 行
   - 无计算来源。
   - 警告：仅可作为 B 的 judgment score。

5. 声称 "circularity, reverse-bias, normalization attacks are materially answered"（第 123 行）
   - reverse-bias 与 normalization 在文本中有对应引用；circularity 的材料回答依赖 "direct raw delta^2 before Qhat normalization"。
   - 通过，但建议下一轮指向具体 ledger/表格，避免证据来源悬空。

## Q6. 综合判定

无阻断级量纲错误、方向反转、硬代数错误或数量级鸿沟。

警告级问题：

1. "second normal curvature" 的几何强度高于本文内证据。当前材料支持 "curvature-like residual coordinate"，尚未独立定义 metric/projection 来证明 normal curvature。
2. `nonLDB_site_skew` 的 `A` 领先阶从上一轮的 `A^2` 改为本轮的 `A`，未给出对称性理由。
3. 最小实验只取 `A=0,0.05`，不足以区分线性与二次 `A` 依赖。
4. AIC/log-drift 与 `8.4/10` 的数值来源没有在 B 文件内标明。

## Q6.3 声张缩水检查

与同一 B 侧上一轮相比，本轮明确杀掉/降级 `Qhat ~ L^{1/2}` 和 exponent-centered framing，转为有限体积信息几何曲率/可分离扰动方向。

判定：存在有意识的声张收缩，但它是对 Round 2 修正的吸收，不是未说明的偷换。建议 PI 在北极星矩阵中按 "从 scaling/exponent discovery 降级到 finite-volume curvature/separability subclaim" 重算当前分数；若原分数依赖 asymptotic power law，应下调。

## Q6.4 替代解释检查

B 已显式提出并处理以下替代解释：

1. normalization/circularity artifact（第 41、123 行）
2. kinetic/normalization artifact（第 57、117 行）
3. finite-size/log drift instead of power law（第 41、74、76-78 行）
4. reversible traffic factor as sanity control rather than residual source（第 53、113 行）

判定：替代解释有检查；但 "A-linear nonLDB response" 仍需排除更简单的二次/偶函数 activity response。

## Verdict

Verdict: WARNING

## 投喂下一轮：阻断级修正

无阻断级修正。不得把当前 B 的警告升级前的 "second normal curvature" 当作已证明定理使用。

## 投喂下一轮：警告级修正

1. 将 "R2/G_T is the second normal curvature" 改为 "R2/G_T is an operational curvature-like normal coordinate"，除非下一轮补出独立 metric/projection 定义。
2. 说明 `nonLDB_site_skew` 下为何允许 `A` 线性项；否则拟合式改为同时含 `A` 与 `A^2`，并用 `A=+a,-a` 或多幅度区分奇偶阶。
3. 对第 41、74 行 AIC/log-drift 声称补充来源路径或 AIC 差值；对 `8.4/10` 明确标注为主观评分。
4. 在下一轮总述中显式标注声张缩水：从 asymptotic `Qhat`/power-law scaling 转为 finite-volume curvature/separability subclaim，并相应重算矩阵分数。
