# LP23-R2 Round3 生死检验 - B 路 adversarial test

## §0 框架声明

本轮采用的跨学科框架是 **纠错码 syndrome quotient + 统计建模 nuisance projection + 数值线性代数 rank-revealing stress test**。Round2 的 `I_bridge` 不是直接物理可观测量，而是 residual 在标准模板列空间商空间里的剩余范数平方。因此生死问题不是“这个 toy residual 有没有数”，而是：只要允许合理扩展的 nuisance/history 模板，那个商空间方向是否仍被迫存在。

## 运行设置

- 脚本：`scripts/r2_syndrome_adversarial.py`
- seed：`2303`
- edge 数：`8`；标准模板矩阵列数：`8`
- Round2 基线：rank `7`，residual_norm `0.0223963644`，I_bridge `0.0005015971`

## 主表：k / rank / residual_norm / I_bridge

| k | tol | template_set | rank | residual_norm | I_bridge |
|---:|---:|---|---:|---:|---:|
| 0 | 1.0e-06 | standard | 7 | 0.0223963644 | 0.0005015971 |
| 0 | 1.0e-08 | standard | 7 | 0.0223963644 | 0.0005015971 |
| 0 | 1.0e-10 | standard | 7 | 0.0223963644 | 0.0005015971 |
| 0 | 1.0e-12 | standard | 7 | 0.0223963644 | 0.0005015971 |
| 0 | 1.0e-14 | standard | 7 | 0.0223963644 | 0.0005015971 |
| 0 | 1.0e-12 | standard+random | 7 | 0.0223963644 | 0.0005015971 |
| 1 | 1.0e-12 | standard+random | 8 | 0 | 0 |
| 2 | 1.0e-12 | standard+random | 8 | 0 | 0 |
| 3 | 1.0e-12 | standard+random | 8 | 0 | 0 |
| 4 | 1.0e-12 | standard+random | 8 | 0 | 0 |
| 5 | 1.0e-12 | standard+random | 8 | 0 | 0 |
| 6 | 1.0e-12 | standard+random | 8 | 0 | 0 |
| 7 | 1.0e-12 | standard+random | 8 | 0 | 0 |
| 8 | 1.0e-12 | standard+random | 8 | 0 | 0 |
| 1 | 1.0e-06 | standard+near_bridge_eps=1e-10 | 7 | 0.0223963644 | 0.0005015971 |
| 1 | 1.0e-08 | standard+near_bridge_eps=1e-10 | 7 | 0.0223963644 | 0.0005015971 |
| 1 | 1.0e-10 | standard+near_bridge_eps=1e-10 | 7 | 0.0223963644 | 0.0005015971 |
| 1 | 1.0e-12 | standard+near_bridge_eps=1e-10 | 8 | 0 | 0 |
| 1 | 1.0e-14 | standard+near_bridge_eps=1e-10 | 8 | 0 | 0 |
| 1 | 1.0e-12 | standard+nonlocal_history | 8 | 0 | 0 |

## 判决

判死。标准模板的 8-edge toy 是 rank 7，剩下的是一维空方向；加入 1 个归一化 random nuisance column 后 rank 变 8，`I_bridge` 在机器精度内塌缩到 0。确定性的 nonlocal/history 对抗列也同样把它吸收；该 history 列含后验 residual 构造成分，只作为 adversarial counterexample，不作为独立预注册物理模板。

## 深挖1：同构结构至少两层

第一层，纠错码语言：`I_bridge = ||(I-P_T)r||^2` 是 syndrome coset 的代表范数。当 `rank(T_standard)=7<8` 时，toy 模型只剩一个 logical/syndrome 方向。任何新模板只要在这个方向上有非零投影，就会把 coset 代表清零。

第二层，统计 nuisance 语言：这等价于把 bridge signal 当成模型残差。如果一个未建模的 nuisance regressor 可以解释该残差，那么残差显著性不是新物理，而是欠拟合。本轮 random nuisance 扫描显示 `k=1` 已经足够把残差吃掉。

## 深挖2：原学科结构至少两层

第一层，几何光学/局域响应：endpoint、spinoptics、local constitutive 被扣除后，Round2 的非零量依赖于“没有更多标准响应模板”的假设。这个假设在 toy 中没有物理封闭性证明，只是列空间没有放满。

第二层，history/nonlocal 响应：真实传播问题允许路径记忆、全局闭路、迟滞或积分核响应。本脚本构造的 deterministic history column 与基线 quotient 方向的 overlap 为 `-0.0636777743`，加入后 rank `8`，I_bridge `0`。该列包含后验 residual 构造，不能当作独立物理模板；它的作用是说明只要允许一个与 quotient 方向非正交的 history/nuisance 列，Round2 的剩余量就不受保护。

--- INSPECTOR_CHECK ---
[公式] `I_bridge=||r-P_T r||_2^2`；本轮基线 `||q||=0.0223963644`，`I=0.0005015971`。加入列空间扩展 `T'=[T,N]` 后重算正交投影。
[方向] rank 从 7 到 8 时 edge space 被填满，故 residual 必须在数值精度内归零；这不是物理发现，而是 toy 维数/模板封闭性失败。
[数据] 使用本地 8-edge toy residual，无外部数据；random nuisance 固定 seed 可复现。
[假设] MGS 使用欧氏内积；death threshold `1e-20`；history 模板只是后验 adversarial 反证示例，不声称独立预注册物理机制。

## rank tolerance 结论

归一化 random/history 列下结论对常见 tolerance 不敏感：新列把秩推到满秩。但 near-bridge 小幅度列显示绝对阈值敏感性：当列尺度 `1e-10` 低于 tolerance 时会被丢弃，高于 tolerance 时又可吸收残差。这要求后续若继续必须先固定列归一化、噪声协方差和物理先验。

## 最小存活条件

若要让 R2 继续活，必须证明：允许的 endpoint/spinoptics/local/nonlocal/history 模板族在 whitened edge space 中，对该 quotient 方向严格正交或被独立实验约束到不可用；否则 toy `I_bridge=0.0005015971` 只是缺列造成的 residual。

## 本轮产出格式

本轮的跨学科跃迁：计算机科学纠错码 syndrome quotient -> 统计模型 nuisance regression -> 几何光学模板完备性反证。
这个结构的数学对象：edge residual 向量空间 `E`、标准模板列空间 `im(T)`、商空间 `E/im(T)`、rank-revealing Gram-Schmidt 投影、nuisance column augmentation。
如果这个同构成立，最奇怪的可检验预测是：只要加入一个与 quotient 方向非正交的额外 history/nonlocal regressor，所谓 bridge invariant 会不连续地从 `0.0005015971` 掉到数值零。
A博士最可能反对的点：random nuisance 太宽泛，history column 不是预先物理指定。我的回应是：这正是生死检验的结论，R2 若要存活，必须先给出模板封闭性和列归一化规则，否则 toy 非零量没有独立物理地位。
本轮失败记录：强版 `I_bridge` 失败；失败原因是 8-edge toy 的标准模板只有 rank 7，剩余一维方向没有被物理保护。
下一步计划：除非 PI 给出预先注册的 nonlocal/history 模板禁区或真实数据 covariance，否则不建议继续把该 toy `I_bridge` 当作 R2 证据。
需要PI投喂的文献方向：weighted nuisance projection, model misspecification tests, optical path memory kernels, nonlocal constitutive electrodynamics, rank-revealing QR/SVD with column normalization。
