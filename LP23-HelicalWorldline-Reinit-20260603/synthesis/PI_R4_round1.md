# LP23-R4 Round1 PI 综合

日期：2026-06-03

## 输入

- A 路：`current/A/R4_round1.md`
- B 路：`current/B/R4_round1.md`
- B 路脚本：`scripts/r4_protocol_closure_toy.py`
- INSPECTOR：`synthesis/INSPECTOR_A_R4_round1.md`、`synthesis/INSPECTOR_B_R4_round1.md`

## 独立性与校对

A 路框架：EFT/operator closure、field redefinition/EOM redundancy、RG/operator mixing、system identification、causal/passive response、statistical model expansion。

B 路框架：type system / grammar closure / proof-carrying code，转成有限链复形上的规则生成子空间。

A/B 均声明未读取对方输出和旧 LP23 目录。两个 INSPECTOR 均通过。B 路脚本已由 PI 和 INSPECTOR 复跑，关键输出一致。

## 本轮结论

R4 的各组成模块先发风险高：

- 固定局域 QFT 情形会退化为 EFT operator basis + EOM/IBP/field redefinition 冗余。
- 固定响应函数情形会退化为 causality/passivity/Kramers-Kronig/Herglotz 或 realization/approximation 问题。
- 固定统计/系统辨识情形会退化为 identifiability、nuisance projection、model expansion/model checking。

R4 的唯一活口是跨协议合同：`G,Q,E,K` 同时约束 gauge/template/bridge/nuisance/history/operator/response，且这些规则必须在看 residual 之前给出。

A 路 no-go 明确：若 `G` 允许事后 residual-shaped template/nuisance/history column，则 `r in S_C(P)`，因此 `Obs_P(r)=0`，R4 直接判死。

B 路 toy 给出第一可执行分裂：

```text
constrained_closure label=CONSTRAINED_OBSTRUCTION rank=6 residual_norm=0.8971489604
open_closure        label=OPEN_ABSORBED           rank=7 residual_norm=5.240587849e-16
```

这证明“开放补列吸收”和“受限闭包保留非零类”在有限 toy 中可以分裂，但 B 路也明确受限规则只是人工 toy，不是真实物理定律。

## PI 判定

R4 未硬停止。它没有证明真实 protocol-closure obstruction，但已经形成比 R3a 更明确的可证伪目标：

**从手写 constrained columns 升级为 witness checker。** 每个合法补列必须携带 locality、causality/protocol-order、passivity/response、measurement-source 等 witness；没有 witness 的补列即使能吸收 residual，也应判非法。

若 Round2 不能把 constrained grammar 物理化，R4 将降级为“人工限制下的 toy obstruction”，不能继续作为北极星。

## AHA / 新命题检查

本轮没有比 R4 更大的新北极星。新增的是 R4 内部子任务：

**R4a Proof-carrying closure / witness checker。**

该子任务不单独切换；它是 R4 Round2 的核心验证对象。

## 停止条件

N=1，未硬停止。按 SOP 继续 Round2。

## Round2 指令

1. A 路：查 proof-carrying code/type systems 与物理 witness 的类比是否已有成熟框架；同时查 passivity realization、local EFT generation、causal model identifiability 是否已经提供 witness checker。
2. B 路：把 `r4_protocol_closure_toy.py` 从手写列升级为至少三个自动 witness checker：support-locality、protocol partial order、passive/decaying kernel。输出合法/非法列、rank、residual norm。
3. PI 判据：若 witness checker 仍可事后接纳 residual-shaped column，R4 判死；若 witness checker 只能靠人工规则保留 obstruction，也降级；若 witness 独立且可复跑，则进入 Round3。
