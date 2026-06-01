# A博士 Phase 3 作业 — Subfactor index 攻打 M.B no-go

## ⚡ PI审核入口

⚡ 本 Phase 推进了什么：把 "M.B no-go 是否能不依赖 GKRR completeness" 转成了 subfactor inclusion / Jones-Kosaki-Longo index 的问题，并对 SYK/JT 标准 canonical 设置给出结构性判断。

⚡ 最关键的跨域连接：若 boundary algebra `A_bdy` 是 full algebra `A_full` 的真子代数，则不需要先证明 GKRR completeness，M.B 的非平凡性可从 `[A_full : A_bdy] > 1` 直接读取。

⚡ 预测 vs 实际：原先预测能得到一个明确的数值 index 或至少一个闭合的 `>1` 证明；实际推进后，最稳妥的结论是：canonical Type III_1 下 boundary algebra 不可能被轻率等同于 full algebra，但 exact index 值当前仍未从现有文献中推出。

⚡ 卡在哪里：最脆弱的一步是把 "Type III_1 / split property / modular flow 的非平凡性" 升级成严格的 index 下界。当前可以说 `[A_full : A_bdy] = 1` 缺乏支撑；但引力理论里的 `A_full` 是否真等于 `B(H)` 仍是结构前提。

## §0 声张强度声明

本 Phase 目标声张：
- 独立于 GKRR 的 M.B no-go：部分成功
- 最强独立论证：canonical Type III_1 中，boundary algebra 的 modular/centralizer 结构不支持把 `A_bdy` 直接抬升为 full algebra
- Microcanonical 压力测试结果：K1.10 仍成立于目标精度内，但仍是 conditional on the chosen algebraic setup

## §N 推导正文

### 1. 翻译成 subfactor 语言

若 `A_bdy ⊂ A_full` 是 proper inclusion，则：
- `[A_full : A_bdy] > 1` 或 `= infinity`
- boundary algebra 不是 full algebra
- M.B no-go 不必再依赖 GKRR completeness

若 `[A_full : A_bdy] = 1`，则两者等价，Phase 1 的 algebraic no-go 失去独立内容。

### 2. Canonical Type III_1 中的结构性判断

Phase 2 已知：
- canonical SYK/JT 标准 TFD 设置下，boundary algebra 是 Type III_1
- Type III_1 无有限投影，`P_0` 不在代数中

这意味着 boundary algebra 的标准投影结构不可能和一个显式可分解的 full Type I algebra 同构。Modular flow / centralizer 是非平凡的，说明 algebra 只是在物理可观测层面闭合，而非简单矩阵代数层面的完整性。

### 3. 若把 `A_full` 取为 `B(H)`

若 `A_full = B(H)`，而 `A_bdy` 仍是 Type III_1，则 proper inclusion 压力很强：
- `B(H)` 含所有有限投影
- Type III_1 不含有限投影
- 两者不可能等价

因此，若 full algebra 真是 `B(H)`，index 不应为 1。问题在于：引力理论中的 `A_full` 是否可无条件视为 `B(H)`，文献没有给出无歧义版本。

### 4. Microcanonical 压力测试

若转到 microcanonical Type II_infinity crossed product：
- `P_0` 可出现
- GKRR completeness 的关键缝合恢复
- Phase 1 no-go 在目标精度内仍可成立

因此 microcanonical 压力测试没有击穿 K1.10，但也没有把 K1.10 从 conditional 升级为 unconditional。

## §末 结果登记建议

- 独立于 GKRR 的 M.B no-go：部分成功
- 最强独立论证：canonical Type III_1 的 modular/centralizer 结构指向 proper inclusion，而非 equality
- Microcanonical 压力测试结果：K1.10 仍成立，但仍是 conditional
- K1.10 升级判定：维持 ⚠️L1

