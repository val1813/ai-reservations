# INSPECTOR_B_R3_round2

对象：`current/B/R3_round2.md`

脚本：`scripts/r3_qnp_lint_toy.py`

复跑命令：

```powershell
python D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r3_qnp_lint_toy.py
```

复跑结果与 B 路文件中记录的关键输出一致：

```text
D0 shape=(9, 5) D1 shape=(1, 9) ||D1@D0||=0
representative_leak      label=REPRESENTATIVE_LEAK    rank= 4 residual_norm=9.408280408e-16 closed_norm=0
template_residual        label=TEMPLATE_RESIDUAL      rank= 5 residual_norm=7.499143576e-16 closed_norm=1.11e-16
nuisance_diagnostic      label=NUISANCE_DIAGNOSTIC    rank= 6 residual_norm=6.184575062e-16 closed_norm=1.11e-16
pass_obstruction         label=PASS_OBSTRUCTION       rank= 7 residual_norm=0.7981011406 closed_norm=6.94e-17
missing_contract         label=UNDECIDED              rank= 4 residual_norm=0.8172550346 closed_norm=6.94e-17
+one_template_col        label=TEMPLATE_RESIDUAL      rank= 6 residual_norm=4.18697711e-16 closed_norm=6.94e-17
+one_nuisance_col        label=NUISANCE_DIAGNOSTIC    rank= 7 residual_norm=4.50012815e-16 closed_norm=6.94e-17
+one_history_col         label=HISTORY_DIAGNOSTIC     rank= 8 residual_norm=3.365900013e-16 closed_norm=6.94e-17
```

## Q1. 量纲校对

关键公式 1：`D1 @ D0 = 0`

- 左边单位：有限矩阵 toy 中 `D0`、`D1` 均按无量纲矩阵处理；`D1 @ D0` 为无量纲矩阵。
- 右边单位：无量纲零矩阵。
- 匹配：✅

关键公式 2：`class_norm(r; A, sigma)=||(I-P_{A/sigma})(r/sigma)||_2`, `A=[D0,T,N,H]`

- 左边单位：白化 residual class norm，`r/sigma` 无量纲，因此范数无量纲。
- 右边单位：`P_{A/sigma}` 是投影算子，无量纲；`r/sigma` 无量纲；二范数无量纲。
- 匹配：✅

关键公式 3：`closed_norm = ||D1 r||_2`

- 左边单位：有限矩阵 toy 中闭合性范数，无量纲。
- 右边单位：`D1` 无量纲，`r` 在本 toy 中无量纲；二范数无量纲。
- 匹配：✅

关键公式 4：`proof(||D1D0||≈0)`, `proof(||D1r||≈0)`, `proof(class_norm(...) > threshold)`

- 左边/右边比较对象均为无量纲范数或无量纲阈值。
- 匹配：✅

超越函数检查：未出现 `exp()`、`sin()`、`log()`、`sinh()` 等超越函数；无自变量量纲问题。✅

Q1 判定：✅ 未发现量纲错误。

## Q2. 符号/方向校对

方向性结论 1：先查 closedness，再查 exact/template/nuisance/history saturation，最后才允许 `PASS_OBSTRUCTION`。

- 极限 1：`||D1r|| > 1e-7`。脚本 `classify()` 先返回 `UNDECIDED`，不会进入 `PASS_OBSTRUCTION`。方向一致。✅
- 极限 2：`||D1r||≈0` 且 `r` 不能被 `D0,T,N,H` 吸收。脚本最终返回 `PASS_OBSTRUCTION`。方向一致。✅

方向性结论 2：`r in im(D0)` 判为 `REPRESENTATIVE_LEAK`。

- 极限 1：`r = D0 x`。复跑中 `representative_leak` 的 residual_norm 为 `9.408280408e-16`，小于阈值，标签为 `REPRESENTATIVE_LEAK`。方向一致。✅
- 极限 2：`r` 不在 `im(D0)`，但被 template 吸收。复跑中 `template_residual` 标签不是 `REPRESENTATIVE_LEAK`，而是 `TEMPLATE_RESIDUAL`。方向一致。✅

方向性结论 3：加一列等于 obstruction 方向的 template/nuisance/history，会使 `PASS_OBSTRUCTION` 退化为对应 diagnostic/residual。

- 极限 1：将 `obstruction_r` 加入 template 列。复跑标签为 `TEMPLATE_RESIDUAL`，norm 降至 `4.18697711e-16`。方向一致。✅
- 极限 2：将 `obstruction_r` 加入 history 列。复跑标签为 `HISTORY_DIAGNOSTIC`，norm 降至 `3.365900013e-16`。方向一致。✅

高危比值/正负号检查：本轮没有分子分母比值方向主张；`D0` incidence 符号与 `D1` 的三角闭合行相乘得到零，复跑 `||D1@D0||=0`。✅

Q2 判定：✅ 未发现符号或方向反转。

## Q3. 循环论证校对

检验操作 1：脚本 base classification。

- 数据生成：本地构造 5 节点、9 边、1 个填充三角面的有限矩阵 toy；`template/nuisance/history/obstruction` 由约束零空间生成。
- 输入假设：有限列空间近似；`sigma` 为已知白化尺度；合法列由 contract 决定。
- 是否循环：classification 确实是在由脚本构造的 toy 数据上恢复预设分层，不能作为真实 LP23 residual 的外部验证。但 B 路文件已声明这是本地有限矩阵 toy、无外部实验数据，并把结论限制为筛选器/合同压力测试。
- 判定：⚠️ toy 内部构造验证，不能外推为真实 residual 证明；当前文本未将其冒充外部验证，因此不构成阻断。

检验操作 2：adversarial expansion。

- 数据生成：将 `obstruction_r` 本身作为新增 template/nuisance/history 列加入。
- 输入假设：若 proposal 允许事后新增刚好等于 obstruction 的合法列，则该方向会被列空间吸收。
- 是否循环：该检验是对“事后补列会吸收 residual”的构造性演示，结论本身依赖补入同一方向；B 路文件明确把它用作合法扩展合同的压力测试，而非独立实验证明。
- 判定：⚠️ 构造性压力测试；需保留“合法扩展合同先验封闭”的限定。非阻断。

Q3 判定：⚠️ 有 toy 构造验证的循环风险标记；文本已显式限定，无阻断。

## Q4. 量级鸿沟标记

量级比较 1：近零 residual norms `~1e-16` vs obstruction norm `~0.798`。

- 指数差约 15-16 个数量级。
- 标记：⚠️ `~1e-16` 是浮点投影残差/数值零，`0.798` 是未吸收 class norm；后续必须将两者解释为“数值零 vs 有限范数”，不能当成连续物理量级比较。

量级比较 2：closed_norm `~6.94e-17` 或 `1.11e-16` vs 阈值 `1e-7`。

- 指数差约 9 个数量级。
- 标记：✅ 未超过 10 个数量级阈值；仍属于数值闭合性通过。

量级比较 3：`0.7981011406` vs adversarial 后 `~3e-16` 至 `~5e-16`。

- 指数差约 15-16 个数量级。
- 标记：⚠️ 同量级比较 1，说明补列后 residual 被投影到数值零；需显式标注为线性代数吸收，不应解释为物理连续衰减。

Q4 判定：⚠️ 存在超过 10 个数量级的数值零/有限范数鸿沟；未见超过 50 个数量级的阻断级鸿沟。

## Q5. 代数验算

### 5a. 逐步展开

矩阵链条件：

- `D0` 为有向边-节点 incidence：每行一个 source `-1`、target `+1`。
- 填充三角面使用边 `(0,1),(1,2),(2,0)`，`D1` 对三条边系数均为 `+1`。
- 对任一节点列，三条边贡献相加为 `(-1 from 0->1 + 1 from 2->0)` 或同类望远镜抵消。
- 因此 `D1 @ D0 = 0`；脚本复跑 `||D1@D0||=0`。✅

白化投影：

- `rw = r/sigma`。
- `aw = columns/sigma[:,None]`。
- SVD 得到列空间正交基 `q = u[:,:rank]`。
- residual 为 `rw - q @ (q.T @ rw)`。
- residual_norm 为其二范数。该实现与 `||(I-P_{A/sigma})(r/sigma)||_2` 一致。✅

分类顺序：

- `contract_complete=False` 直接返回 `UNDECIDED`，复跑 `missing_contract` 标签为 `UNDECIDED`。✅
- `closed_norm > 1e-7` 返回 `UNDECIDED`。本轮构造 residual 均闭合到数值零量级。✅
- 依次测试 `D0`、`D0+template`、`D0+template+nuisance`、`D0+template+nuisance+history` 的白化投影 residual norm。复跑标签与该顺序一致。✅

### 5b. 极限退化

极限 1：`r` 完全在 `im(D0)` 内。

- 公式退化：`P_{D0/sigma}(r/sigma)=r/sigma`，class norm 应为 0。
- 复跑：`representative_leak residual_norm=9.408280408e-16`，数值零。✅

极限 2：`r` 完全在新增 template/nuisance/history 列空间内。

- 公式退化：加入对应列后，class norm 应为 0。
- 复跑：加一列 template/nuisance/history 后 residual_norm 分别为 `4.18697711e-16`、`4.50012815e-16`、`3.365900013e-16`，均为数值零。✅

极限 3：contract 缺失。

- 规则退化：不允许升级为 `PASS_OBSTRUCTION`。
- 复跑：`missing_contract label=UNDECIDED`。✅

### 5c. 数值量级验证

- `||D1@D0||=0`：复跑吻合。✅
- `PASS_OBSTRUCTION residual_norm=0.7981011406`：复跑吻合。✅
- adversarial expansion 三项 residual_norm：复跑均与文件记录吻合。✅
- 近零残差为 `1e-16` 量级，符合双精度 SVD 投影数值残差；未发现 >3 数量级偏差。✅

### 5d. 引用数值来源级别

- 本轮具体数值来自本地脚本复跑，不依赖外部实验数据。
- `sigma` 数组、toy 拓扑、阈值 `TOL=1e-9`、分类阈值 `1e-7` 均在脚本中给出。
- 来源级别：本地脚本全量核实。✅

Q5 判定：✅ 代数验算与脚本输出一致；未发现代数阻断。

## Q6. 综合判定

⚠️ INSPECTOR警告：

1. 本轮验证是本地有限矩阵 toy 的内部构造验证，不能外推为真实 LP23 residual 的外部证明；需保留“toy/筛选器/合同压力测试”限定。
2. `~1e-16` 数值零与 `~0.798` 有限范数之间存在约 15-16 个数量级鸿沟；应显式解释为线性代数投影后的数值零 vs 未吸收有限范数。
3. adversarial expansion 将 `obstruction_r` 本身补入列空间，因此其“立刻死亡”是构造性压力测试；后续使用时必须先定义合法扩展合同。

✅ INSPECTOR通过

无量纲错误、无符号方向反转、无阻断级循环论证、无 >50 数量级鸿沟、无代数验算阻断。
