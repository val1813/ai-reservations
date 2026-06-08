# INSPECTOR_B_R4_round2

角色：LP23-R4 Round2 B 路 INSPECTOR  
输入推导文件：`current/B/R4_round2.md`  
复跑脚本：`scripts/r4_witness_checker_toy.py`  
日期：2026-06-03

## 复跑脚本核对

命令：

```powershell
python D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_witness_checker_toy.py
```

关键输出与 B 路报告一致：

```text
D0 shape=(9, 5) D1 shape=(1, 9) ||D1@D0||=0
candidate closedness=4.16e-17
legal_only:WITNESS_OBSTRUCTION               rank= 6 residual_norm=0.8971489604 accepted=['local_loop', 'history_fast'] rejected=[]
with_residual_oracle:WITNESS_OBSTRUCTION     rank= 6 residual_norm=0.8971489604 accepted=['local_loop', 'history_fast'] rejected=['residual_oracle']
algebraic_open_if_oracle_ignored_checks       rank= 7 residual_norm=5.240587849e-16
verdict=TOY_SURVIVES_CHECKER: oracle would absorb algebraically, but fails locality/order/source witnesses before entering closure
```

## Q1. 量纲校对

关键公式：

1. `C_W(P)=span{D_0,g_i: check(g_i,w_i)=PASS}`
   - 左边 SI 单位：无 SI 单位，有限维向量空间/子空间对象。
   - 右边 SI 单位：无 SI 单位，有限矩阵列张成子空间。
   - 匹配：是。

2. `n_W(r)=||(I-Pi_{C_W(P)})r||_{Sigma^{-1}}`
   - 左边 SI 单位：无 SI 单位的 toy norm。
   - 右边 SI 单位：`r` 与 `Sigma` 均为 toy 数组；脚本中 `rw=residual/sigma`，范数无 SI 单位。
   - 匹配：是。

3. `ker D_1 / C_W(P)` 与 `[r]_W in ker D_1 / C_W(P)`
   - 左边 SI 单位：无 SI 单位，线性代数商空间。
   - 右边 SI 单位：无 SI 单位，有限维 toy quotient class。
   - 匹配：是。

4. `D_1 D_0=0`
   - 左边 SI 单位：无 SI 单位，有限矩阵乘积。
   - 右边 SI 单位：无 SI 单位，零矩阵/零范数。
   - 匹配：是；脚本复跑 `||D1@D0||=0`。

超越函数自变量检查：输入推导和脚本中未使用 `exp()`、`sin()`、`log()`、`sinh()` 等超越函数。

结论：未发现量纲阻断。

## Q2. 符号/方向校对

方向性结论 1：residual-shaped oracle column 代数上可吸收 residual。

- 极限/代入检查：脚本将 `oracle.values=residual.copy()` 加入列空间，并在忽略 checker 时计算投影。
- 结果：`algebraic_open_if_oracle_ignored_checks rank=7 residual_norm=5.240587849e-16`，低于 `1e-7` 吸收阈值。
- 方向匹配：是。

方向性结论 2：residual-shaped oracle 因 witness 失败不能进入 checker-filtered closure。

- 复跑输出：`residual_oracle FAIL`。
- 失败项：`nonlocal support diameter=2 max=1`；`future dependence e0 <- e1`；`oracle/residual-shaped source is not an allowed measurement source`。
- closure 结果：`with_residual_oracle` 仍 `rank=6 residual_norm=0.8971489604`，rejected 包含 `residual_oracle`。
- 方向匹配：是。

方向性结论 3：legal columns 通过 witness checker。

- 复跑输出：`local_loop PASS`，`history_fast PASS`。
- closure 结果：accepted 为 `['local_loop', 'history_fast']`。
- 方向匹配：是。

结论：未发现符号方向反转。

## Q3. 循环论证校对

检查对象：脚本生成的 residual 与 checker 对 residual_oracle 的拒绝。

- residual 生成方式：`constraints = vstack([legal_matrix.T, d1])`，然后通过 SVD 取 `unit_null_vector(constraints)`。因此 residual 被构造为与 `D0`、合法列和 `D1` 约束相容的 toy null vector。
- 验证输入假设：固定 5 节点、9 边有限链复形，固定 `D0/D1`，固定合法列，固定 protocol order，固定 locality/order/source/passive checker。
- checker 是否直接重复 residual 构造假设：不是完全重复。residual 构造只用 `legal_matrix.T` 和 `d1`；oracle 失败来自 support-locality、protocol order、source/preregistration 三类规则。
- 但有显式依赖：`residual_oracle_column(residual)` 直接把待检 residual 复制为 oracle column。因此“oracle 代数上可吸收 residual”是构造性恒真，不是独立验证。

判定：存在需要标注的构造性检查，但未构成当前 INSPECTOR 阻断。B 路也明确声称此 toy 只说明“若给 residual-shaped column，则代数可吸收；但 checker 阻止其准入”，没有把代数吸收当作独立经验验证。

## Q4. 量级鸿沟标记

主要数值比较：

1. checker-filtered residual norm：`0.8971489604`
2. 忽略 checker 的 algebraic open residual norm：`5.240587849e-16`

量级差：

- 约 `0.8971489604 / 5.240587849e-16 ~= 1.71e15`
- 即约 15 个数量级。

标记：⚠️ 量级鸿沟。该鸿沟来自“准入规则是否允许 residual_oracle 进入列空间”的离散差异，不应被误读为连续物理效应大小。

其他数值：

- `candidate closedness=4.16e-17`，说明 `D1@residual` 在数值精度下接近零。
- `||D1@D0||=0`，矩阵链条件精确满足。

结论：有量级鸿沟警告，无量级错误阻断。

## Q5. 代数验算

### 5a. 逐步展开

1. `D0` 为 9x5 incidence matrix；每条边一行，source 为 `-1`，target 为 `+1`。
2. `D1` 为 1x9 cycle row，仅前三条边系数为 `+1,+1,+1`。
3. 脚本复跑 `||D1@D0||=0`，链条件成立。
4. 合法列为：
   - `local_loop = e3+e4+e5`
   - `history_fast = 1.0 e6 + 0.45 e7 + 0.20 e8`
5. residual 由 `constraints=[legal_matrix.T; d1]` 的零空间单位向量给出，因此满足：
   - 与 `D0` 列空间正交；
   - 与两个合法列正交；
   - `D1@residual ~= 0`。
6. checker-filtered closure 使用 `hstack(D0, accepted_extra)`，只接纳通过 witness 的列。
7. residual_oracle 若绕过 checker，列值等于 residual，因此投影后 residual norm 降至数值零。

未发现矩阵维度不匹配：

- `D0 shape=(9,5)`
- `D1 shape=(1,9)`
- residual shape 为 9 维。

### 5b. 极限退化

已知极限 1：无 oracle，仅合法列。

- 结果：`rank=6 residual_norm=0.8971489604`
- 与 residual 构造方式一致：residual 被构造为合法闭包外的单位方向；加权范数不必为 1，因为使用 `sigma` whitening。

已知极限 2：oracle 被强行加入且忽略 checker。

- 结果：`rank=7 residual_norm=5.240587849e-16`
- 与 `oracle.values=residual.copy()` 一致；数值残差为 SVD/浮点误差。

已知极限 3：oracle 进入候选但 checker 生效。

- 结果：oracle rejected，closure 与 legal-only 相同，仍 `rank=6 residual_norm=0.8971489604`。
- 与脚本准入逻辑一致。

### 5c. 数值量级验证

复跑值与报告声称值一致：

- 报告声称 `n_W=0.8971489604`；复跑一致。
- 报告声称 `n_open=5.240587849e-16`；复跑一致。
- 报告声称 `candidate closedness=4.16e-17`；复跑一致。

偏差：无。

### 5d. 引用数值来源级别

所有具体数值均来自本地 toy 脚本复跑；无外部实验数据。输入推导已标注“本地脚本、无外部实验数据”。数值来源级别为本地构造 toy，不是实验证据。

结论：代数与脚本输出一致，未发现代数阻断。

## Q6. 综合判定

⚠️ INSPECTOR警告：存在约 15 个数量级的 checker-filtered/open-algebra residual norm 鸿沟；该鸿沟来自 oracle 准入开关，必须显式标注，不能被解释为连续物理量级预测。

⚠️ INSPECTOR警告：`oracle.values=residual.copy()` 使“oracle 代数上吸收 residual”成为构造性结果；可作为 stress test，不可作为独立验证。

✅ INSPECTOR通过。

本轮未发现量纲错误、符号方向反转、阻断性循环论证、阻断性量级错误或代数验算错误。可继续，但后续推导不得把该 toy checker 的准入规则当作已由物理协议独立推出。
