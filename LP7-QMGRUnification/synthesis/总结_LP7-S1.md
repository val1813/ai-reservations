# LP7-S1 收官总结：Page-Geilker 半经典方程失败边界

收官日期：2026-06-01

## 结论类型

有边界。

## 核心结论

Page-Geilker 型论证排除的是 naive expectation-source per-run 半经典源项：

`G_{\mu\nu}=8πG<T_{\mu\nu}>`

不能被解释为“未塌缩/ensemble 量子态的期望应力能量张量直接决定每次实验实际经典度规”。

但它不排除所有 classical/semi-classical gravity。stochastic gravity、classical-channel / measurement-feedback、collapse 后源项、Oppenheim postquantum classical gravity 等路线在 Page-Geilker 层面仍存活。

## 最小模型

二分支宏观质量态：

`|\psi> = (|L> + |R>)/sqrt(2)`

naive expectation-source 给出：

`Φ_sc = (Φ_L + Φ_R)/2`

单次实验分支给出：

`Φ_run = Φ_L` 或 `Φ_R`

差异量：

`ΔΦ_branch = Φ_run - Φ_sc = ±(Φ_L - Φ_R)/2`

Page-Geilker 的打击点就是：实际读数跟随单次分支，而不是平均源项。

## A/B/PI 状态

- A 正规推导：`current/A/LP7-S1_phase1.md`
- B 独立检查：`current/B/LP7-S1_independent_check.md`
- PI 整合：`current/plan/LP7-S1_integration.md`

GATE 结果：

- GATE 1：通过，文献库和反例栏存在。
- GATE 3：通过，B 独立输出存在。
- GATE 4：阶段性通过，B 的主要攻击已由 PI 仲裁。
- GATE 2：未触发正式审稿人收官；本子命题为长命题内部筛选相。

## 入库条目

- K60：Page-Geilker 边界化 naive expectation-source 半经典方程。
- K61：Page-Geilker 不排除所有经典引力，只排除 naive per-run expectation-source interpretation。

## 对 LP7 的影响

LP7 的原始大问题不能写成“半经典引力已被实验击毙，因此必须量子化引力”。正确推进路径是：

> S1 已经把最朴素的 `<T>` 源项排除到边界外；后续若继续推进，应攻击存活路线的联合判据，例如纠缠、噪声、局域性和能量守恒。

## 状态

LP7-S1 已收官。暂停推进，等待新的子命题指令。
