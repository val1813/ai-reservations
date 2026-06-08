# LP23-R4 Round3 - B博士报告

日期：2026-06-03

## 0. 本轮目标

Round2 的 toy checker 只能说明：如果存在一个准入检查器，residual-shaped oracle column 会被挡在 closure 外。本轮把它改成最小可执行 pipeline：

```text
columns_pre.json / built-in preregistry
  -> verify witness
  -> rank accepted closure
  -> train residual projection
  -> holdout component check
```

新增脚本：

```text
D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_physical_witness_pipeline.py
```

脚本运行时写入并重读：

```text
D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\columns_pre.json
```

关键约束：候选列来自预注册 registry。residual 只在 verify 完成之后进入训练投影和 holdout 评分；脚本没有从 residual 派生候选列。

## 1. 物理化 witness proxy

本轮没有继续使用纯“手写 constrained columns”。我加入了一个最小 positive-real / Herglotz toy proxy：

```text
passive_tail_pr:
  source = passive_realization
  poles = (0.45, 1.6) > 0
  residues = (1.25, 0.35) >= 0
  direct = 0.04 >= 0
  samples H(omega)=direct + sum_j residue_j/(omega + pole_j)
  omega = (1,2,3)
```

checker 检查：

1. pre-registration：列必须在 residual 打开前存在于 registry。
2. source：`oracle` / residual-shaped source 禁止。
3. locality：实际非零 support 必须等于 witness 声明，且图距离直径不超过 witness 阈值。
4. order：依赖边在 protocol rank 上不能来自未来。
5. passive-real proxy：pole 为正、residue/direct 非负，列幅度必须等于 Stieltjes/positive-real toy response samples，且采样值单调衰减。

这比 Round2 的 decaying FIR 更物理化，但仍只是 toy proxy，不是完整 Kramers-Kronig / Herglotz 定理化实现。

## 2. Holdout 设计

训练 residual 投影只使用边：

```text
train_idx = [0,1,2,3,4,5,6,7]
```

held-out component 为：

```text
holdout_idx = [8]
```

合法列不能只吸收训练 residual；拟合训练边后，必须预测 edge 8 的 held-out amplitude。`passive_tail_pr` 的 support 包含 edge 8，但系数由训练边估计，因此 holdout 是独立校验通道，不参与最小二乘拟合。

## 3. 运行结果

命令：

```powershell
python D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_physical_witness_pipeline.py
```

关键输出：

```json
{
  "accepted_columns": [
    "local_loop_stencil",
    "passive_tail_pr"
  ],
  "holdout_error": 0.0014384846096407084,
  "oracle_rejected": true,
  "rank": 6,
  "rejected_columns": [
    {
      "failures": [
        "column was not preregistered before residual was opened",
        "oracle/residual-shaped source is not an allowed physical source",
        "future dependence e0 <- e1"
      ],
      "label": "oracle_source_challenge"
    },
    {
      "failures": [
        "future dependence e0 <- e1"
      ],
      "label": "future_leak_challenge"
    }
  ],
  "train_residual_norm": 0.0013957664881648368,
  "verdict": "R4_TOOL_SURVIVES_TOY_PHYSICAL_PIPELINE"
}
```

强制字段均已输出：

```text
rank = 6
train_residual_norm = 0.0013957664881648368
holdout_error = 0.0014384846096407084
oracle_rejected = true
verdict = R4_TOOL_SURVIVES_TOY_PHYSICAL_PIPELINE
```

`py_compile` 通过。

## 4. 判定

脚本层判定：最小 pipeline 通过。预注册合法列经 verify 后进入 closure，rank 为 6；训练 residual norm 与 holdout error 同时保持在 `~1e-3`；oracle/source challenge 未能进入 closure。

研究层判定：R4 仍应降级为工具命题，不能上升为物理结论。原因是：

1. positive-real / Herglotz 仍是手写 toy proxy，只检查有限个 Stieltjes samples，不是完整解析性、正实性、能量不等式或 Kramers-Kronig 约束。
2. locality 仍是有限图 support 直径，不是真实时空局域算符、coarse-graining 或 EFT operator basis。
3. order/source 仍来自手写 protocol DAG，不是从实际测量协议或系统辨识因果模型中推导。
4. residual 是合成 probe；holdout 证明了 pipeline 结构不会只拟合训练 residual，但没有证明真实光学/响应系统必然生成这些 witness。

所以本轮最强结论是：

```text
R4b 作为可复跑 witness-pipeline 工具命题暂存；
R4 作为“真实物理 obstruction”应降级，除非下一步把 checker 从真实 passive response / EFT locality / measurement DAG 中独立推出。
```

## 5. 本轮跨学科跳跃

本轮的跨学科跳跃：

```text
系统与网络理论 / 被动实现理论
  -> positive-real / Stieltjes response witness
  -> 扩展列必须携带可验证的被动响应实现，而不是只在代数上吸收 residual
```

数学对象：

```text
(g,w) with w = {pre_source, support, protocol_DAG, positive-real realization}
C_W(P)=span(D0, {g_i : Verify_P^pre(g_i,w_i)=PASS})
```

若同构成立，最奇怪的可检验预测是：

```text
同一 residual 在训练投影中可被合法物理列压低，同时在未参与训练的 held-out channel 上仍有预测力；
post-residual/oracle source 即使代数上有利，也因无合法 witness 被拒绝。
```

失败记录：

```text
本轮仍没有把 checker 变成物理定理。它是预注册 pipeline + positive-real toy proxy，而非成熟物理 witness calculus。
```

下一步计划：

```text
把 passive_realization checker 替换为真正的正实函数/耗散实现检验；
把 graph locality 替换为局域 EFT operator generation + redundancy removal；
把 protocol_order 替换为预注册 measurement DAG / causal identifiability。
```

需要 PI 投喂的文献方向：

```text
positive-real lemma; passive realization; Herglotz/Nevanlinna functions;
Kramers-Kronig constrained response fitting;
local EFT operator basis, EOM/IBP redundancies;
causal DAG pre-registration and post-treatment bias in system identification.
```

--- INSPECTOR_CHECK ---
[公式] \(H(\omega)=d+\sum_j a_j/(\omega+p_j)\), \(p_j>0,a_j\ge0,d\ge0\)。\(C_W(P)=\operatorname{span}(D_0,\{g_i:\operatorname{Verify}^{pre}_P(g_i,w_i)=PASS\})\)。训练投影只在 `train_idx=[0..7]` 上做最小二乘，holdout error 为 \(\|(r_{\rm holdout}-\hat r_{\rm holdout})/\sigma_{\rm holdout}\|\)。
[方向] 预注册合法列通过；oracle/source challenge 与 future-leak challenge 被拒绝；rank=6，train_residual_norm=0.0013957664881648368，holdout_error=0.0014384846096407084。
[数据] 本地脚本 `scripts/r4_physical_witness_pipeline.py` 生成的有限矩阵 synthetic probe；无外部实验数据。
[假设] 5 节点 9 边 toy 复形，单边 holdout，positive-real 只用有限 Stieltjes samples 代理；因此 R4 物理结论应降级。
