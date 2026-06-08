# INSPECTOR-A 校对报告：NSF-FCS-2 Round 2 A

校对对象：`current\A\NSF-FCS-2_round2_A.md`

约束执行：已读取 `D:\Claude\ai-reservations\ai\INSPECTOR.md`。本报告只做 INSPECTOR Q1-Q6 校对；不做先发文献 REVIEWER 审查；未读取 B 输出。

## Q1. 量纲校对

判定：PASS。

A 稿保留的核心公式和归一化为：

1. `lambda_T''(0)=2G_T`
   - 左边：`lambda(chi)` 是 tilted generator 主特征值，单位为 inverse time；`chi` 为 dimensionless counting field，因此 `lambda_T''` 仍为 inverse time。
   - 右边：`G_T=dJ/dF`，`J` 为 particle-current rate，`F` 为 dimensionless reservoir affinity，因此 `G_T` 为 inverse time。
   - 匹配：是。

2. `R2=lambda_T''-2G_T`
   - `lambda_T''`、`G_T` 均为 inverse time。
   - `R2` 为 inverse time。
   - 匹配：是。

3. `Qhat=R2/(delta^2 G_T)`
   - `delta` 为 density difference，无量纲。
   - `R2/G_T` 无量纲，因此 `Qhat` 无量纲。
   - 匹配：是。

4. `R2(L,delta,alpha)=C_L(alpha) delta^2 + O(delta^4)`
   - `delta` 无量纲，因此 `C_L(alpha)` 与 `R2` 同为 inverse time。
   - 匹配：是。

未发现 `exp()`、`log()`、`sin()`、`sinh()` 等超越函数自变量量纲错误。A 稿的 `log drift`、AIC、local slopes 均是对同类无量纲或固定单位序列做模型比较，不构成量纲阻断。

## Q2. 符号/方向校对

判定：PASS。

1. A 稿声称 equilibrium finite-volume FDT 给出 `lambda_T''(0)=2G_T`，且 density-biased NESS 中 `R2` 非零。极限检查：`delta -> 0` 时，PI normalization ledger 给出 equilibrium FDT；因此 `R2 -> 0`。方向一致。

2. A 稿声称 raw `R2` 在 `delta` 上呈二次标度。PI delta test 中 `L=4..7`、`alpha=0.5,1.0,1.5` 的 raw exponent 全部约为 `2.000`，未发现把 `Qhat` 归一化结果倒推为 raw 结论的方向错误。

3. A 稿声称 off-center reverse-bias checks 无可检测 odd contamination。PI off-center reverse check 给出 `max abs Delta S_T` 为 `4.10e-8`、`2.96e-8`，`max abs Delta R2` 为 `6.03e-9`、`8.01e-9`。方向结论与数据一致。

4. A 稿把 `reversible_side` 降级为 LDB sanity check，把 `nonLDB_site_skew` 分离为非 LDB perturbation。PI activity controls 显示 reversible equilibrium 仍满足 FDT 到约 `1e-7`，non-LDB equal-density residual 达约 `4.95e-5`。方向未反。

未发现分子/分母倒置、正负号吃掉、或反偏置结论方向相反的问题。

## Q3. 循环论证校对

判定：PASS/WARNING。

PASS 部分：

1. `raw R2 ~ delta^2` 是在除以 `delta^2 G_T` 形成 `Qhat` 前直接拟合得到；这实质回答了上一轮对 circular normalization 的主要攻击。

2. 反偏置检查使用 forward/off-center 与 reverse/off-center ledger 比较，不是从偶性假设直接生成同一结论。

WARNING 部分：

1. A 稿关于 `Qhat` 增长的表述仍依赖 PI 已整理的模型比较摘要，而非本稿内逐行复算。A 已把 `Qhat~L^{1/2}` 撤回，并写成 finite-window growth / log drift favored，因此不构成阻断；但下一轮不得把 `Qhat` 增长当成已独立推导的 asymptotic law。

2. A 稿提出的下一步 proposition `R2=C_L(alpha)delta^2+O(delta^4)` 是合理的修正目标，但当前 Round 2 A 并未给出 `C_L(alpha)` 的独立系数表、误差模型或 quartic fit；这仍是待验证命题。

## Q4. 数量级鸿沟标记

判定：PASS/WARNING。

未发现 `10^N` vs `10^M` 且指数差超过 10 的显式数量级鸿沟。

需要保留的数量级警告：

1. `L=4..8` 和 `L=4..7` 是极小 finite-volume windows。A 稿已明确说不能推出 asymptotic scaling；这是正确降级。

2. `Qhat` 的 finite-window local slopes `0.47..0.56` 与 log-drift AIC favored 之间存在模型未定性。A 稿已建议删除 hard power-law language，因此没有阻断，但必须继续标注为 finite-window empirical growth。

3. activity controls 中 equilibrium numerical floor 约 `1e-7`，non-LDB equal-density residual 约 `5e-5`，相差约 2-3 个数量级；这支持“非 LDB perturbation distinct”表述，但仍是有限精度数值现象，不是解析分离定理。

## Q5. 代数/极限退化/数值来源

判定：WARNING。

### 5a. 代数来源

1. `R2=lambda_T''-2G_T`、`S_T=lambda_T''/G_T`、`Qhat=R2/(delta^2 G_T)` 的代数关系自洽。

2. 从 `Qhat=R2/(delta^2 G_T)` 可得 `R2=delta^2 G_T Qhat`；A 稿没有再把此恒等式误写成独立 microscopic proof。

3. `R2=C_L delta^2+O(delta^4)` 与反偏置偶性、finite-L 解析性兼容。A 稿把它作为 next minimal proposition，而不是声称已完成全密度/全 L 证明，处理正确。

### 5b. 极限退化

1. `delta -> 0`：`R2 -> 0`，退化到 equilibrium FDT，正确。

2. `L -> infinity`：A 稿没有声称可由当前 finite-window 数据推出极限；正确。

3. 非 LDB perturbation at equal density：activity controls 显示 equal-density residual 不再受 equilibrium FDT sanity 控制，A 稿将其与 density-bias NESS 主线分离，正确。

### 5c. 数值量级验算

1. raw `R2` delta exponent：PI 表中所有值为 `1.999968..2.000108`，与 A 稿“quadratically in density bias”一致。

2. off-center reverse：`Delta R2` 在 `1e-8` 量级，支持“no detectable odd-bias contamination at current precision”。

3. Qhat 模型比较：PI 摘要称所有测试 dataset/alpha 中 log drift AIC 最优；A 稿因此撤回 `Qhat~L^{1/2}`，数值方向一致。

### 5d. 数值来源级别

WARNING：A 稿本身是 review/standard-framework synthesis，不是可复算 ledger notebook。具体数值主要来自 PI Round 2 摘要文件和内部 CSV ledger，而 A 稿没有逐项列出参数、脚本 commit、误差传播或复算命令。作为 INSPECTOR 结果，这不阻断 A 稿进入下一轮，但下一轮若要把这些数值升级为 proof/numerics 主张，必须补齐可复算 provenance。

## Q6. 综合判定

判定：WARNING。

未发现阻断级的量纲错误、方向错误、循环论证、数量级灾难或明显代数错误。A 稿相对 Round 1 有实质性声张降级：从 `Qhat~L^{1/2}` / asymptotic scaling story 降级为 finite-volume residual program，并明确要求删除 hard scaling language。这是合理收缩，不是偷偷缩水。

### Q6.3 声张缩水检查

存在声张收缩，但它是对上一轮 INSPECTOR WARNING 的必要修正：

1. Round 1：`Q_L ~ L^{1/2}` 被作为自然解释/预测。
2. Round 2 A：`Qhat` grows over finite windows，log drift favored，asymptotic law unresolved。

这是显著降级，但 A 稿公开承认并给出下一步更窄 proposition；建议 PI 在北极星矩阵中按“声张保真度下降但风险降低”重新计分，而不是把它视为已完成 asymptotic claim。

### Q6.4 替代解释检查

WARNING：A 稿指出主要替代解释是 known MFT / fluctuating-hydrodynamic finite-size projection 或 near-equilibrium second-order response correction，而不是新 long-jump universality class。它承认该替代解释尚未排除。因此当前只能保留为“standard-framework 内的 sharp diagnostic/residual program”，不能写成概念新机制已被建立。

## Verdict

Verdict: WARNING

## 投喂下一轮：阻断级修正

无当前阻断级修正。不得在下一轮把 `Qhat~L^{1/2}`、`square-root growth` 或 `3/2-alpha` 写成已证明/已验证的 asymptotic law；若这样写，将构成阻断。

## 投喂下一轮：警告级修正

1. 补齐 `R2=C_L(alpha)delta^2+O(delta^4)` 的 coefficient extraction：固定 `L,alpha` 做更小 `delta` 与 quartic correction fit，报告 `C_L`、误差和 residual。
2. 给出数值 provenance：CSV 路径、脚本入口、参数、精度设置、拟合窗口和复算命令。
3. 对 `Qhat(L)` 只使用 finite-window / model-underdetermined language；保留 log drift favored over power-law 的警告。
4. 显式登记替代解释风险：MFT/fluctuating hydrodynamics 或标准 near-equilibrium second-order response 可能解释同一 residual，不应声称新 universality class。
