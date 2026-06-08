# INSPECTOR_B_R4_round1

日期：2026-06-03

检查对象：
- 输入推导文件：`current\B\R4_round1.md`
- 复跑脚本：`scripts\r4_protocol_closure_toy.py`

复跑命令：

```powershell
python D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_protocol_closure_toy.py
```

复跑关键输出核对：

```text
D0 shape=(9, 5) D1 shape=(1, 9) ||D1@D0||=0
local_loop       closedness=0 support=[3, 4, 5]
history_fast     closedness=0 support=[6, 7, 8]
candidate residual closedness=4.16e-17
constrained_closure label=CONSTRAINED_OBSTRUCTION rank=6 closedness=4.16e-17 residual_norm=0.8971489604 column_closedness=0
open_closure        label=OPEN_ABSORBED           rank=7 closedness=4.16e-17 residual_norm=5.240587849e-16 column_closedness=2.78e-17
```

复跑结果与 B 路报告中的关键数字一致。

## Q1. 量纲校对

本轮公式均为有限维 toy 矩阵/向量上的线性代数对象，未引入 SI 物理单位。

1. `D0`
   - 左/右含义：节点 0-cochain 到边 1-cochain 的关联矩阵。
   - SI 单位：无量纲。
   - 匹配：通过。

2. `D1`
   - 左/右含义：边 1-cochain 到一个 cycle 检查量的行向量。
   - SI 单位：无量纲。
   - 匹配：通过。

3. `D1D0=0`
   - 左边 SI 单位：无量纲矩阵乘积。
   - 右边 SI 单位：无量纲零矩阵。
   - 匹配：通过。脚本复跑给出 `||D1@D0||=0`。

4. `C_R(P)=span(D0,G_R)`
   - 左边 SI 单位：无量纲子空间。
   - 右边 SI 单位：由无量纲列向量张成的无量纲子空间。
   - 匹配：通过。

5. `n_R(r)=||(I-Pi_{C_R(P)})r||_{Sigma^{-1}}`
   - 左边 SI 单位：无量纲范数。
   - 右边 SI 单位：`r`、投影矩阵、`sigma` 均按脚本作为无量纲数组处理。
   - 匹配：通过。

6. 超越函数自变量检查
   - 输入推导与脚本中没有 `exp()`、`sin()`、`log()`、`sinh()` 等超越函数。
   - 匹配：通过。

Q1 结论：未发现量纲错误。

## Q2. 符号/方向校对

方向性结论 1：open/oracle closure 吸收 residual。

- 手动代入：open 额外列包含 `residual[:, None]`，因此 `r` 本身属于 `span(D0, constrained_cols, r)`。
- 极限/退化检查：若 open residual-column 系数取 1，其他新增列系数取 0，则可精确重构 `r`；投影残差应退化到数值零。
- 脚本核对：`open_closure residual_norm=5.240587849e-16`，为机器精度零。
- 方向：通过。

方向性结论 2：constrained closure 保留 closed nonzero quotient class。

- 手动代入：constrained closure 只含 `D0`、`local_loop`、`history_fast`。
- `r` 由 `constraints = vstack([constrained_base.T, d1])` 的右零空间生成，因此满足 `D1 r = 0` 且在普通欧氏内积下正交于 constrained columns。
- 脚本用 `Sigma^{-1}` whitened metric 投影，仍给出非零残差 `0.8971489604`。
- 方向：通过。

方向性结论 3：同一 residual 在 constrained/open 两种合同下分裂。

- constrained：非零残差，label 为 `CONSTRAINED_OBSTRUCTION`。
- open：机器零残差，label 为 `OPEN_ABSORBED`。
- 分子/分母反置或正负号吞掉风险：未见比值公式或负号驱动结论；主要方向来自子空间包含关系 `C_constrained subset C_open`。
- 方向：通过。

Q2 结论：未发现符号或方向错误。

## Q3. 循环论证校对

验证/检验数据生成方式：

- `D0`、`D1`、`sigma`、`local_loop`、`history_fast` 均由脚本内固定 toy 设定生成。
- candidate residual 由 `vstack([constrained_base.T, d1])` 的右零空间生成。
- open closure 额外加入 `residual[:, None]`。

输入假设：

- `D1D0=0`。
- constrained grammar 只允许两个人工 toy 列：`local_loop` 与 `history_fast`。
- open/oracle grammar 允许 residual-direction column。
- metric 由固定 `sigma` 给定。

循环性判断：

- 若把脚本输出当作“真实物理 obstruction 存在”的验证，则会构成循环/过度外推，因为 residual 与 grammar 都由 toy 假设生成。
- 但 B 路文本已明确限定：这是 toy pressure-test witness，不是 Maxwell/EFT/真实介质响应/真实测量协议推出的物理定律；结论只声称在有限维 toy 中可以区分“任意补列吸收”和“合法生成闭包吸收”。
- 在该限定结论下，脚本是构造性代数见证，不是把外部验证数据重复为输入假设。

Q3 结论：未发现阻断性循环论证。需保留显式限定：该脚本只能证明 toy 构造内的 closure-dependent splitting，不能作为真实物理 obstruction 的独立验证。

## Q4. 量级鸿沟标记

发现的数量级比较：

1. constrained residual norm vs open residual norm
   - `n_constrained = 0.8971489604 ~ 10^0`
   - `n_open = 5.240587849e-16 ~ 10^-16`
   - 数量级差约 15-16。
   - 标记：⚠️。该鸿沟符合脚本设计：open 将 residual 本身作为列，残差退化到机器精度零；constrained 不允许该列，保留非零残差。

2. closedness vs constrained residual norm
   - `closedness = 4.16e-17 ~ 10^-17`
   - `n_constrained = 0.8971489604 ~ 10^0`
   - 数量级差约 16-17。
   - 标记：⚠️。含义是 residual 在 `D1` 检查下数值闭合，同时不属于 constrained closure。

3. `||D1@D0||=0` vs 非零 residual norm
   - `||D1@D0||` 为精确输出 0，不能作为有限数量级直接比较。
   - 不标为代数错误；这是链复形条件。

Q4 结论：⚠️ 存在超过 10 个数量级的数值鸿沟，但不是阻断错误；必须明确标注其来源为 toy 设计和机器精度投影。

## Q5. 代数验算

### Q5a. 逐步展开

1. `D0` 关联矩阵
   - 每条边 `(source,target)` 对应一行：source 列为 `-1`，target 列为 `+1`。
   - 例如边 `(0,1)` 给出 `[-1,1,0,0,0]`。
   - 代数合法。

2. `D1D0=0`
   - `D1` 只检查边 `e0,e1,e2`，系数均为 `+1`。
   - 三条边为 `(0,1),(1,2),(2,0)`。
   - 三行相加：`[-1,1,0,0,0] + [0,-1,1,0,0] + [1,0,-1,0,0] = [0,0,0,0,0]`。
   - 代数合法；脚本输出 `||D1@D0||=0`。

3. constrained generated columns closedness
   - `local_loop` 支持 `[3,4,5]`，而 `D1` 只作用于 `[0,1,2]`，所以 `D1 local_loop = 0`。
   - `history_fast` 支持 `[6,7,8]`，而 `D1` 只作用于 `[0,1,2]`，所以 `D1 history_fast = 0`。
   - 脚本输出二者 `closedness=0`。

4. residual 构造
   - `constraints = vstack([constrained_base.T, d1])`。
   - `unit_null_vector(constraints)` 返回单位右零空间向量。
   - 因此 `constrained_base.T r = 0` 且 `D1 r = 0`，在普通欧氏内积下 `r` 不在 constrained span 中。
   - 脚本输出 `closedness=4.16e-17`，符合数值 SVD 误差。

5. whitened projection
   - `rw = r/sigma`。
   - `aw = columns/sigma[:,None]`。
   - 对 `aw` 做 SVD，取非零奇异值对应的 `q`，计算 `rw - q(q^T rw)`。
   - 这是 `Sigma^{-1}` 加权范数下的正交投影残差计算。
   - 代数合法。

### Q5b. 极限退化

1. open 极限
   - 当 open 允许列 `r` 时，`r` 属于 closure span。
   - 预期残差为 0；脚本输出 `5.240587849e-16`。
   - 通过。

2. constrained 极限
   - 当只允许 `D0`、`local_loop`、`history_fast` 时，`r` 被构造成 constrained span 的零空间方向。
   - 预期残差非零；脚本输出 `0.8971489604`。
   - 通过。

3. closedness 极限
   - `D1D0=0` 且两个 constrained columns 均为 closed。
   - residual 也由含 `d1` 的约束零空间生成。
   - 预期 `D1 r = 0`；脚本输出 `4.16e-17`。
   - 通过。

### Q5c. 数值量级验证

1. `rank=6` for constrained closure
   - `D0` 为 5 节点连通图 incidence matrix，rank 预期为 `nodes-1=4`。
   - 加两个支持不重叠的 generated columns 后，rank 预期可到 6。
   - 脚本输出 `rank=6`，吻合。

2. `rank=7` for open closure
   - open 在 constrained columns 外再加入 residual direction。
   - residual 被构造成 constrained span 外方向，rank 预期增加 1。
   - 脚本输出 `rank=7`，吻合。

3. residual norm 数值
   - `n_constrained=0.8971489604`，为 O(1)。
   - `n_open=5.240587849e-16`，为机器精度零。
   - 与 B 路声明一致。

### Q5d. 引用数值来源级别

- 所有具体数值均来自本地脚本复跑。
- 无外部实验数据。
- 来源级别：本地 toy 计算，全量可复现；非实验来源。

Q5 结论：未发现代数展开、rank、投影或数值复跑错误。

## Q6. 综合判定

⚠️ INSPECTOR警告：存在约 16 个数量级的 constrained/open 残差鸿沟，以及约 16-17 个数量级的 closedness/residual norm 鸿沟。该鸿沟来自 toy 构造与机器精度投影，必须显式标注；不得被后续推导误用为真实物理量级差。

✅ INSPECTOR通过：在 B 路文本已限定为有限维 toy pressure-test witness 的前提下，量纲、符号方向、循环论证、量级标记、代数验算均未发现阻断错误。可继续，但后续若要推出物理 obstruction，必须另行给出非 toy 的合法生成规则或 witness checker，不能把本脚本当作外部物理验证。
