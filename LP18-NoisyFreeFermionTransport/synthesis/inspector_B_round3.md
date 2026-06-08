# INSPECTOR_B_ROUND3

输入文件：`current/B/round3_B.md`

检查范围：INSPECTOR_CHECK 块与关键公式；重点检查 `Q(s,theta)` 单位、Fisher residual 方向、Zeno-effective 不含 `theta` 的方向结论、保留/击毙判据是否循环论证。

## Q1. 量纲校对

1. `lambda(s)=lim_{t->infty} t^-1 log <e^{sQ_t}>`
   - 左边 SI 单位：`time^-1`
   - 右边 SI 单位：`t^-1 * dimensionless = time^-1`
   - 匹配：✅
   - `e^{sQ_t}` 的指数需无量纲：若 `Q_t` 是计数转移量，则 counting field `s` 必须无量纲。INSPECTOR_CHECK 已说明 `s` 无量纲，匹配 ✅

2. `w_{ij}=2|J_{ij}|^2/gamma`
   - 约定：`J_{ij}` 与 `gamma` 都按频率/能量除以 `hbar` 计，即单位 `time^-1`
   - 左边 SI 单位：`time^-1`
   - 右边 SI 单位：`(time^-1)^2 / time^-1 = time^-1`
   - 匹配：✅
   - 若后续把 `J` 写作能量而不是角频率，需要补 `hbar^-2` 或先声明 `hbar=1`。当前文档语境为开放量子系统常用 `hbar=1`，不阻断。

3. `Q(s,theta)=Delta lambda(s,theta) - (partial_D lambda_SSEP)(s;D0) Delta D(theta)`
   - `Delta lambda` 单位：`time^-1`
   - 若 `D` 是格点模型中的有效跳率/扩散参数，单位为 `D_unit`，则 `partial_D lambda_SSEP` 单位为 `time^-1 / D_unit`，乘以 `Delta D` 后为 `time^-1`
   - 左边 SI 单位：`time^-1`
   - 右边 SI 单位：`time^-1 - time^-1 = time^-1`
   - 匹配：✅，但需显式声明 `D_eff` 与 `lambda_SSEP` 中的 `D` 使用同一单位归一化。
   - ⚠️ 标记：文中 `s` 同时作为 counting field 符号，而 INSPECTOR_CHECK 又写单位 `s^-1` 表示每秒，符号可读性有歧义。建议后续把单位写为 `time^-1` 或 `sec^-1`。

4. `C_n=partial_s^n lambda|_0`
   - counting field `s` 无量纲
   - 左边 SI 单位：`time^-1`
   - 右边 SI 单位：`time^-1`
   - 匹配：✅

5. `Q_n(theta)=C_n(theta)-C_n^SSEP[D_eff(theta)]`
   - 左边 SI 单位：`time^-1`
   - 右边 SI 单位：`time^-1 - time^-1 = time^-1`
   - 匹配：✅

6. `Q_n(theta)=B_{n,0}+B_{n,1} cos theta+B_{n,2} cos 2theta+...`
   - `theta` 无量纲，相位函数自变量无量纲
   - `B_{n,m}` 单位：`time^-1`
   - 匹配：✅

7. `|B_{n,1}| ~ |J_l|^mu gamma^{-nu} L^{-kappa}`
   - 左边单位：`time^-1`
   - 右边单位：`time^{-(mu-nu)}`，因为 `L` 无量纲
   - 若候选 `mu=2,nu=1`，右边单位为 `time^-1`，匹配 ✅
   - 若拟合得到其他 `mu,nu`，必须补一个参考频率尺度或写成无量纲化形式，例如 `|B|/J ~ (|J_l|/J)^mu (gamma/J)^(-nu) L^{-kappa}`。当前作为候选二阶不阻断，但后续泛化需标注。

## Q2. 符号/方向校对

1. Zeno-effective generator 不含 `theta`，因此能独立验证 long-jump 主线。
   - 极限 `theta -> theta + delta`：`w_{ij}=2|J_{ij}|^2/gamma` 不变，所有 Zeno-effective population observables 不随 `theta` 变。
   - 极限 `gamma -> infinity` 且保留二阶 Zeno：相位只进入被投影掉的相干 sector，主阶 population kernel 仍无 `theta`。
   - 方向结论：✅ 正确。它支持“主线验证不依赖 holonomy”。
   - ⚠️ 标记：这只能说明二阶 Zeno 主阶无 `theta`，不能单独证明 full tilted Lindblad 的所有高阶 residual 为零。文中多数位置已把 holonomy 降为 high-order residual test，因此不阻断。

2. “full tilted Lindblad 中只有扣除 `D_eff` 后仍非零的偶周期 residual 才能支持 holonomy。”
   - 极限 `Q -> 0`：无独立 residual，holonomy 不可辨识，应击毙。
   - 极限 `Q != 0` 且为稳定 `cos(m theta)`：存在 gauge-invariant 相位依赖，可保留或降级保留。
   - 方向结论：✅ 正确。

3. Fisher residual 投影：
   - 公式：`v_theta^\perp = v_theta - v_D (v_D·v_theta)/(v_D·v_D)`
   - 若 `·` 表示同一 Fisher metric 下的内积，且只有一个 nuisance direction `D_eff`，则这是从 `v_theta` 中扣除 `v_D` 分量，方向正确 ✅
   - 极限 `v_theta = a v_D`：`v_theta^\perp=0`，holonomy 不可辨识，击毙方向正确。
   - 极限 `v_theta·v_D=0`：`v_theta^\perp=v_theta`，residual 完整保留，方向正确。
   - ⚠️ 标记：文中写“Fisher metric 下”但投影公式未显式写 metric 矩阵。若坐标内积不是 Fisher 正交归一坐标，严格写法应为 `v_theta - v_D <v_D,v_theta>_F/<v_D,v_D>_F`，或在多 nuisance 参数时使用 `V_D (V_D^T F V_D)^-1 V_D^T F v_theta`。当前单参数方向正确，不阻断。

4. 保留/降级/击毙方向：
   - `Q` 非零且与主线同阶、可随 loop density 累积 -> 可重新讨论 universality：方向正确。
   - `Q` 非零但高阶小量 -> 降级为 finite-size coherent correction：方向正确。
   - `Q` 扣除 `D_eff` 后消失 -> 击毙 B 副线：方向正确。

## Q3. 循环论证校对

1. `D_eff` 拟合与 `Q_n` 检验：
   - 检验数据来源：同一有限链 tilted Liouvillian 主特征值或 Zeno-effective tilted Markov generator 主特征值。
   - 输入假设：`D_eff` 是 nuisance parameter；用 `C_1`、conductance、`theta=0` 或纯 Zeno 模型拟合。
   - 检验目标：`n>=2` 的 `Q_n` 是否仍有不可吸收 residual。
   - 判定：✅ 不构成循环。因为用于吸收的是 `C_1`/conductance/基线方向，检验对象是扣除后的高阶 cumulants 或正交分量。

2. Zeno-effective 对照：
   - 若仅因 Zeno-effective 二阶公式不含 `theta` 就判定 full Lindblad 的 holonomy 为零，会构成循环/过度外推。
   - 当前文档的击毙条件要求 full tilted Lindblad 与 Zeno-effective 在 `Q_n` 上均为零到数值精度，且误差界受控；这需要 full Lindblad 独立计算。
   - 判定：✅ 不阻断，但需显式标注“Zeno 为零只是 null baseline，击毙必须依赖 full Lindblad 独立 residual 也为零”。

3. 保留判据：
   - 保留条件要求 residual 非零、不可由 `D_eff` 吸收、相位依赖为偶周期、幂律稳定。
   - 这些条件不是从 holonomy 假设直接生成，而是从独立的 theta 扫描、gamma/J_l/L 拟合和 gauge/counting-field 稳定性检验生成。
   - 判定：✅ 未发现循环论证。

4. 击毙判据：
   - “低于数值误差”“误差界小于 long-jump 主线信号的 1%”依赖数值误差估计。
   - 只要误差估计来自独立收敛测试、步长/截断/Liouvillian diagonalization residual，而不是用 `Q=0` 假设反推，判据不循环。
   - ⚠️ 标记：报告执行时必须记录误差界生成方式；否则“低于数值误差”有被循环使用的风险。

## Q4. 量级鸿沟标记

1. 明确数值阈值：
   - `gamma/J = 10,20,40,80`
   - `L=16..64` 或 Zeno-effective `L=32..256`
   - `J_l in {0.02J,0.05J,0.1J,0.2J}`
   - 击毙误差阈值 `1%`
   - 未出现 `10^N` vs `10^M` 且 `|N-M|>10` 的数量级鸿沟。

2. ⚠️ 标记：full tilted Liouvillian 的可达 `L=8..14` 与 Zeno-effective 的 `L=32..256` 存在有限尺寸外推落差，但不是 `>10` 数量级鸿沟。后续不得把小 `L` full Lindblad 的零 residual 直接外推为大 `L` 定理。

## Q5. 代数验算

1. 二阶矩阈值：
   - `r(l)=2|J_l|^2/gamma`
   - 若 `J_l=J0 l^{-alpha}`，则 `r(l)=2J0^2 gamma^-1 l^{-2alpha}`
   - `M_2(L)=sum_{l=1}^L l^2 r(l)=2J0^2 gamma^-1 sum_{l=1}^L l^{2-2alpha}`
   - `alpha>3/2`：指数 `2-2alpha<-1`，级数收敛 ✅
   - `alpha=3/2`：指数 `-1`，`M_2(L) ~ log L` ✅
   - `alpha<3/2`：指数 `>-1`，`M_2(L)` 发散 ✅

2. `Q` 的线性 nuisance 扣除：
   - 一阶展开：`lambda_SSEP(s;D0+Delta D)=lambda_SSEP(s;D0)+(partial_D lambda_SSEP)(s;D0) Delta D + O((Delta D)^2)`
   - 因此 `Delta lambda - (partial_D lambda_SSEP) Delta D` 是扣除 `D` 方向的一阶 residual。
   - 代数方向：✅
   - ⚠️ 标记：若 `Delta D` 不小，需保留高阶项或直接用 `lambda_SSEP(s;D_eff(theta))` 非线性扣除，否则 residual 会混入 nuisance 的二阶曲率。

3. Fisher 投影：
   - 单 nuisance 方向的正交投影为 `Proj_D(v_theta)=v_D <v_D,v_theta>/<v_D,v_D>`。
   - residual `v_theta-Proj_D(v_theta)` 满足 `<v_D,v_theta^\perp>=0`。
   - 代数正确 ✅，条件是内积与 Fisher metric 一致。

4. 闭环高阶 scaling：
   - `|B_{n,1}| ~ J_l^2 J^m gamma^{-(m+1)} L^{-kappa_loop}`
   - 单位：`time^{-(2+m)} time^{m+1}=time^-1`，匹配 ✅
   - 方向：随 `gamma` 增大衰减；若 `m>=2`，衰减比候选二阶 `gamma^-1` 更快，降级方向正确 ✅

5. 数值来源：
   - 当前是实验设计，无实测数值。
   - 扫描参数未给文献或实验来源，属于设计参数，不要求来源。
   - ⚠️ 若后续把 `gamma/J>=40,L>=32` 作为物理可实现阈值而非数值设计阈值，需要来源标注。

## Q6. 综合判定

⚠️ INSPECTOR警告：B Round3 可继续，但需显式标注三点：

1. `Q(s,theta)` 的单位检查通过，前提是 `D_eff` 与 `lambda_SSEP(s;D)` 中的 `D` 使用同一归一化；建议把单位写成 `time^-1`，避免 counting field `s` 与秒 `s` 混淆。
2. Fisher residual 的方向正确，但必须声明点积是 Fisher metric 内积；若后续扩展到多个 nuisance 参数，需改用矩阵投影。
3. Zeno-effective 不含 `theta` 的方向结论正确，但它只是二阶 Zeno null baseline；击毙 holonomy 必须依赖 full tilted Lindblad 的独立 residual 也为零，不能只由 Zeno 二阶无相位推出。

未发现 ❌ 阻断级量纲错误、方向反转或循环论证。结论：✅ 可继续，但上述警告需在后续 PI/数值执行中显式记录。
