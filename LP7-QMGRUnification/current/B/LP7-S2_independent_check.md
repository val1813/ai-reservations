# LP7-S2 — B 独立检查

## 0. 独立性声明

我只使用任务书和文献锚点，不读取 A 的 `LP7-S2_phase1.md`。

## 1. 最小模型

考虑两个量子探针 `A,B` 与一个中介 `M`：

`H = H_A + H_B + H_M + H_{AM} + H_{MB}`

如果 `A` 与 `B` 之间没有直接耦合，而纠缠是在演化后出现，那么纠缠必须经由 `M` 传递。

在最朴素的 BMV 读法里，这意味着：

- 若 `M` 是局域经典媒介并满足 local tomography，则它不应能在不留下 classical factorization 痕迹的情况下生成纠缠；
- 若实验确实观察到纠缠，则 `M` 不是这种意义上的完全经典对象。

## 2. Page-like 逻辑类比不适用

BMV 不是 Page-Geilker 型“单次分支 vs ensemble 平均”问题。
它的问题是：

- 纠缠是否真的由单一局域媒介生成；
- 这个媒介是否可被 classical + local tomography 完全描述；
- 以及“非经典”的定义到底停在哪一层。

因此，BMV 只能推出“媒介非经典于某些假设下”，不能自动推出“时空必须量子叠加”。

## 3. 文献边界检查

### 3.1 Marletto & Vedral 2017 / 2025

这组文献给出的主张是：

- 若一个媒介能在局域条件下生成纠缠，则它不能是完全经典的。
- 但这一推论是条件性的，不是无条件总论。

### 3.2 Di Pietra et al. 2024/2025

该文明确把 locality 变成假设边界。
这意味着 BMV 的证明力量取决于你如何定义 locality，而不是只有“看到了纠缠”这一事实。

### 3.3 Vidal et al. 2025

该文给出关键反例：

- 纠缠可以在没有 observable spacetime superpositions 的前提下生成；
- 只要媒介满足非局域可层析耦合，经典基底上没有叠加也不妨碍纠缠。

这直接削弱“BMV = quantum spacetime proof”的读法。

## 4. 对 A 预期结论的攻击

若 A 说“BMV 只边界化 locality + local tomography 下的经典媒介”，我同意。

若 A 进一步说“因此 BMV 只能得到媒介非经典，不能推出量子时空”，我也同意。

我攻击的点不是这个结论本身，而是它的边界是否已经写够：

1. BMV 见证是否真的必须要求 local tomography？
2. non-local-tomographic classical mediator 是否只是语言绕行，还是实质反例？
3. reference-frame 一致性是否会把“非经典”推得比 A 说得更强？

## 5. 逃逸路线表

| 路线 | 是否存活 | 理由 |
|---|---|---|
| 标准经典媒介 | 否 | 在 BMV 假设下难以生成纠缠 |
| classical mediator + non-local tomography | 是 | Vidal et al. 2025 给出明显反例语义 |
| partially quantum mediator | 是 | 非经典不等于标准量子重力 |
| reference-frame loophole | 是 | BMV 的结论强度依赖 frame 处理 |

## 6. B 结论类型

结论类型：**有边界**。

理由：

BMV 类实验确实能排除一类“局域、可完全经典层析、且无法生成纠缠”的媒介模型，但不能直接推出“引力的时空叠加是必要的”。最强结论只能写成“在明确假设下，媒介非经典”；Vidal et al. 2025 还说明，连 observable spacetime superpositions 都不是必要条件。

## 7. 待 PI 仲裁问题

1. `local tomography` 是否应列为 BMV 推论的必要假设。
2. `non-local-tomographic classical mediator` 是否属于真正逃逸，而非换名词。
3. “媒介非经典”与“时空非经典”之间能否无额外假设直接桥接。
4. 参考系一致性是否应上升为 BMV 的单独判据。

