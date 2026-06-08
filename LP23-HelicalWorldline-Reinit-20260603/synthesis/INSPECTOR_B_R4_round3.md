# INSPECTOR_B_R4_round3

日期：2026-06-03

角色：LP23-R4 Round3 B 路 INSPECTOR

范围：仅检查量纲、符号方向、循环论证、量级鸿沟、代数验算和综合判定；未读取 A 路输出；不评价发表价值或先发覆盖。

输入：

- `current/B/R4_round3.md`
- `scripts/r4_physical_witness_pipeline.py`

复跑命令：

```powershell
python -m py_compile D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_physical_witness_pipeline.py
python D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_physical_witness_pipeline.py
```

复跑关键输出与 B 路报告一致：

```json
{
  "accepted_columns": [
    "local_loop_stencil",
    "passive_tail_pr"
  ],
  "holdout_error": 0.0014384846096407084,
  "oracle_rejected": true,
  "rank": 6,
  "train_residual_norm": 0.0013957664881648368,
  "verdict": "R4_TOOL_SURVIVES_TOY_PHYSICAL_PIPELINE"
}
```

## Q1. 量纲校对

1. `H(omega)=d+sum_j a_j/(omega+p_j)`

- 左边 SI 单位：未声明；脚本中为无量纲 toy response。
- 右边 SI 单位：脚本中 `omega,p_j,a_j,d` 均为 float toy 参数；按脚本实现整体无量纲。
- 若按物理频率解释：`omega` 与 `p_j` 必须同为频率量纲，`a_j` 必须为 `[H]*[frequency]`，`d` 必须为 `[H]`；报告未把该式提升为带 SI 单位的物理公式。
- 匹配：✅ 在脚本 toy 无量纲约定下匹配；物理量纲解释未充分声明，只能作为 toy proxy。

2. `C_W(P)=span(D0,{g_i: Verify_P^pre(g_i,w_i)=PASS})`

- 左边单位：边空间/列空间中的向量子空间。
- 右边单位：`D0` 的列与 accepted `g_i` 均为边向量；脚本中均为长度 9 的实向量。
- 匹配：✅

3. 训练投影只在 `train_idx=[0..7]` 上做最小二乘

- 左边单位：加权列矩阵和加权 residual 的线性最小二乘。
- 右边单位：`columns[train]/sigma` 与 `residual[train]/sigma` 均为归一化后的同型量。
- 匹配：✅

4. `holdout_error=||(r_holdout-rhat_holdout)/sigma_holdout||`

- 左边单位：归一化范数，无量纲。
- 右边单位：`r` 与 `rhat` 同单位，除以 `sigma` 后无量纲。
- 匹配：✅

超越函数自变量：脚本与推导中未使用 `exp()`, `sin()`, `log()`, `sinh()`。✅

Q1 结论：未发现量纲阻断。

## Q2. 符号/方向校对

1. positive-real / Stieltjes samples

- 公式：`H(omega)=d+sum_j a_j/(omega+p_j)`，`p_j>0,a_j>=0,d>=0`。
- 极限 `omega` 增大：每项 `a_j/(omega+p_j)` 单调减小，`H(omega)` 单调趋向 `d`。
- 脚本检查：`np.diff(observed)>TOL` 则拒绝，即要求 samples 非增。
- 方向匹配：✅

2. oracle/source challenge 被拒绝

- `oracle_source_challenge.preregistered=False` -> 触发未预注册失败。
- `source=ORACLE` -> 触发 residual-shaped source 失败。
- `dependencies` 含 `e0 <- e1`，且 `protocol_rank[1]>protocol_rank[0]` -> future dependence 失败。
- 与复跑输出一致：✅

3. future-leak challenge 被拒绝

- `dependencies=((0,(1,)),(1,(1,)))`；`e0 <- e1` 为未来依赖。
- 与复跑输出一致：✅

4. accepted columns 方向

- `local_loop_stencil`：预注册、local source、support 与非零位置一致、diameter<=2、依赖不来自未来。
- `passive_tail_pr`：预注册、passive realization、support 与非零位置一致、diameter<=2、依赖不来自未来，且 poles positive、residues/direct nonnegative、samples 匹配且非增。
- 与复跑输出一致：✅

Q2 结论：未发现符号方向阻断。

## Q3. 循环论证校对

检查对象：`holdout_error` 被用来支持“合法物理列在 held-out channel 仍有预测力 / pipeline survives”。

数据生成方式：

- `synthetic_residual(d0,specs)` 显式构造
  `residual = gauge + 0.55*local_loop_stencil + 1.35*passive_tail_pr + deterministic_probe_noise`。
- 其中 `local_loop_stencil` 与 `passive_tail_pr` 正是 verify 后进入 closure 的 accepted columns。
- held-out edge 8 位于 `passive_tail_pr` 的 support 内；训练边 6、7 也含同一列的 Stieltjes samples。

本步骤输入假设：

- residual 由 gauge + accepted witness columns + 小 deterministic noise 合成。
- holdout 使用同一个 `passive_tail_pr` 列在 edge 8 的预注册值进行预测。

循环性判断：

- 对“脚本流程是否按 verify -> fit -> holdout 的顺序执行”，该测试不是循环；脚本顺序确实如此。
- 对“holdout 证明合法列具有独立预测力”或“物理 witness 有效性”，该测试存在循环论证：检验数据由被检验通过的同一 witness 列合成，holdout 只是在未参与拟合的坐标上恢复输入生成模型。

❌ 循环论证：`holdout_error≈1.4e-3` 的小值不能作为独立物理 witness 证据；它只验证了 synthetic residual 按同一 accepted-column 模型生成时，最小二乘能恢复该模型。修正建议：若要保留 holdout 结论，需把判定降为“脚本自洽/流程 smoke test”；若要主张独立预测力，需使用不由 accepted columns 生成的 residual 或独立生成机制。

Q3 结论：发现阻断。

## Q4. 量级鸿沟标记

复跑数值：

- `train_residual_norm = 0.0013957664881648368 ≈ 1.4e-3`
- `holdout_error = 0.0014384846096407084 ≈ 1.4e-3`
- 阈值：脚本 verdict 使用 `5e-3`

比较：

- `train_residual_norm` 与 `holdout_error` 同为 `10^-3` 量级。
- 二者与 `5e-3` 阈值同量级，无 `|N-M|>10` 的量级鸿沟。
- 未发现 `10^N` vs `10^M` 且 `|N-M|>10` 的比较。

Q4 结论：未发现量级鸿沟阻断。

## Q5. 代数验算

### 5a. 逐步展开

1. incidence matrix

- 每条有向边 `(source,target)` 对应一行：source 位置 `-1`，target 位置 `+1`。
- 9 条边、5 节点，`D0` 为 `9x5`。
- 代数实现与定义一致。✅

2. passive samples

- 参数：`poles=(0.45,1.6)`, `residues=(1.25,0.35)`, `direct=0.04`, `frequencies=(1,2,3)`。
- `H(1)=0.04+1.25/1.45+0.35/2.6≈1.0366976127`
- `H(2)=0.04+1.25/2.45+0.35/3.6≈0.6474886621`
- `H(3)=0.04+1.25/3.45+0.35/4.6≈0.4783684310`
- 非增方向成立。✅

3. closure rank

- `D0` 在连通 5 节点图上 rank 为 `5-1=4`。
- accepted columns 两列加入后，复跑 SVD 给 `rank=6`。
- 与报告一致。✅

4. train/holdout least squares

- 加权训练矩阵：`columns[0..7,:]/sigma[0..7]`。
- 加权训练 residual：`residual[0..7]/sigma[0..7]`。
- 系数由 `np.linalg.lstsq` 得出；holdout 仅在系数拟合后计算。
- 代数流程与报告描述一致。✅

### 5b. 极限退化

1. `omega -> infinity`

- `H(omega)->d=0.04`，正且有限。
- 与 positive-real toy proxy 的非增尾部方向一致。✅

2. `a_j -> 0`

- 对应 pole-residue 项消失，`H(omega)->d`。
- 脚本中若 residues 非负且 samples 匹配，退化合法。✅

3. `p_j -> 0+`

- `a_j/(omega+p_j)` 对 `omega>0` 有限，且随 `omega` 非增。
- 脚本要求 `p_j>TOL`，避免零/负 pole。✅

### 5c. 数值量级验算

- 报告声称的 `rank=6`、`train_residual_norm=0.0013957664881648368`、`holdout_error=0.0014384846096407084`、`oracle_rejected=true` 与复跑完全一致。✅
- 偏差：0 个数量级。

### 5d. 引用数值来源级别

- 具体数值来自本地脚本生成的 finite synthetic probe。
- 报告已声明“无外部实验数据”和“toy proxy”。
- 来源级别：脚本生成，不是外部实验或全文物理数据。
- ⚠️ 验算仅支持脚本自洽，不支持外部物理结论。

Q5 结论：代数与脚本复跑一致；但数值来源为 synthetic probe。

## Q6. 综合判定

⛔ INSPECTOR阻断：Q3 循环论证。`holdout_error` 的小值来自 synthetic residual，而该 residual 显式由 verify 后 accepted 的同一列 `local_loop_stencil` 与 `passive_tail_pr` 合成；因此它不能作为独立物理 witness 或独立预测力证据。修正后需重新提交。

允许保留的非阻断结论：

- 脚本可编译并可复跑。
- 关键 JSON 输出与 B 路报告一致。
- verify -> rank -> train projection -> holdout scoring 的执行顺序在脚本层成立。
- 量纲、符号方向、量级和代数验算未发现额外阻断。

最终判定：

```text
⛔ INSPECTOR阻断：循环论证。修正后重新提交。
```
--- INSPECTOR_CHECK_REVISED ---

[循环论证修正] B 路修正版已承认原 `holdout_error` 不是独立预测力证据。脚本中的 synthetic residual 由 `gauge + 0.55*local_loop_stencil + 1.35*passive_tail_pr + deterministic_probe_noise` 合成，而 `local_loop_stencil` 与 `passive_tail_pr` 正是 verify 后进入 closure 的 accepted columns。

[修正路径] 当前项目没有提供不由 accepted columns 合成的独立 holdout residual/component，因此未构造非循环 holdout test。修正版采用硬降级路径：`verdict = R4_TOOL_NOT_VALIDATED_BY_HOLDOUT`。

[脚本复核] `scripts/r4_physical_witness_pipeline.py` 现在输出 `holdout_independent=false`、`holdout_evidence_status=not_independent_synthetic_smoke_test_only`、`blocked_claims=[...]`，并保留 `holdout_error=0.0014384846096407084` 仅作为 synthetic smoke-test 诊断值。

[结论] 阻断已被处理：修正后不再把合成 holdout 当作独立证据；不再声称 holdout_error 验证 physical witness checker 或 accepted columns 的独立预测力。
