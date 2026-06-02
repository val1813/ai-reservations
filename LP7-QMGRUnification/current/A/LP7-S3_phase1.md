# LP7-S3 Phase 1 — A 正规推导

生成时间：2026-06-01

## 0. 输入与边界

本推导只处理 LP7-S3：经典-量子混合动力学 no-go 边界。

不声称：

- 所有经典-量子混合理论都不可能。
- 经典引力必然量子化。
- 任何 stochastic hybrid 动力学都必然错误。

本推导声称的目标更窄：

> deterministic / naive hybrid closure 若要同时保持完全正性、局域性、无超光速信号与低噪声可观测输出，通常会触发结构性冲突；一致可行的分支往往要求 stochasticity、diffusion 或额外模型假设。

## 1. 问题拆分

将 hybrid classical-quantum dynamics 分成三类：

1. **确定性闭合型**：经典变量与量子变量通过确定性方程耦合。
2. **随机完全正型**：通过 stochastic trajectory / unravelling 维持 CP 和 TP。
3. **模型受限型**：只在 interactions always on、特定 ensemble、特定耦合结构下成立。

LP7-S3 只问第一类是否能无代价成立。

## 2. 已知冲突模式

### 2.1 非局域信号

Hall-Reginatto 类 hybrid 模型的一类已知问题是：当交互关闭或耦合切换时，可能出现 nonlocal signaling 风险。  
这说明“混合动力学可写”不等于“混合动力学物理上普适”。

最小判据：

`closed deterministic hybrid + interaction switch-off`  
若仍要求同时保留局域性与标准量子边缘统计，则可能出现代数层面的信息回流矛盾。

### 2.2 正性与闭合的张力

要让 classical variable 与 quantum state 同时演化，通常需要：

- CP / TP
- 可定义的 measurement back-action
- classical noise 或 diffusion

若只保留 deterministic drift，则很难同时满足：

`positivity + consistency + no-signaling`

这是 hybrid no-go 的第一层边界。

### 2.3 纠缠生成的分岔

部分文献声称 classical mediator 也可在某些结构下生成纠缠，但这并不自动击败 no-go。  
它只说明“classical”一词有多种实现：

- 可能是 classical bit 级别的介质；
- 可能是 ensemble-level classical field；
- 可能是 stochastic classical geometry；
- 也可能是带额外隐藏变量的 postquantum classical model。

因此，S3 必须把“可生成纠缠”与“介质完全经典”拆开。

### 2.4 2026 直接压缩项

2026 年新文献把 classical gravity 作为纠缠介质的主张进一步压缩：Newton-Cartan 分析下，classical gravity 不能独立产生 entanglement。
这不等于所有 hybrid theory 都失败，但它把 mediator-level claim 直接降级成受限命题：

- 经典引力若仍要保留，不能再声称它本身就是独立纠缠中介；
- 若实验观察到纠缠，必须引入额外非引力结构或更细的中介层；
- 因而 classical mediator 只能写成 model-restricted claim。

## 3. Oppenheim 路线的意义

Oppenheim 类 postquantum classical gravity 并不等于“经典引力失败”。  
它的真正含义是：

1. 经典-量子耦合可以存在；
2. 但必须是 stochastic / completely positive / trace preserving；
3. 同时会出现 decoherence 与 diffusion 的 trade-off；
4. 这个 trade-off 可被实验约束。

因此，混合动力学的正确结论不是“不可存在”，而是：

`deterministic hybrid closure is too strong; stochastic hybrid closure survives with cost`

## 4. 最小模型结论

把所有 hybrid 理论压缩成三个可检验标签：

| 标签 | 结果 |
|---|---|
| deterministic closure | 高风险，易触发非局域信号或正性问题 |
| stochastic CP-TP closure | 存活，但付出 decoherence / diffusion 成本 |
| model-restricted closure | 只在特定耦合结构下成立，不能提升为一般定理 |

## 5. Phase 结论

结论类型：**有边界**。

核心结论：

经典-量子混合动力学的真正 no-go 不是“所有混合都错”，而是“无随机性、无扩散代价、又想保持局域和完全正的 naive hybrid closure”这一类闭合通常不可持续。Hall-Reginatto 型与 Oppenheim 型文献表明，存活的 hybrid 模型必须降级为 stochastic / CP-TP / trade-off 型 proposition；因此 LP7-S3 的结果应写成混合理论的边界分层，而不是全局排除。

## 6. K 条目候选

K70 [✅ L2] deterministic naive hybrid closure 不能同时保住局域性、正性与无超光速信号。
  来源：Hall, Reginatto, Savage 2012；Hall & Reginatto 2021；Bermúdez et al. 2024。
  适用条件：交互开关、经典-量子混合闭合、无额外随机噪声。
  math_object：`no-signaling`, `CP-TP`, `hybrid closure`
  验证状态：待 B 独立验证。

K71 [⚠️ L3] 一致的 hybrid classical-quantum dynamics 需要 stochasticity / diffusion 代价。
  来源：Oppenheim et al. 2020/2023；Oppenheim 2023；Oppenheim & Sajjad 2026。
  适用条件：classical gravity 与 quantum matter 的一致耦合。
  math_object：`decoherence-diffusion trade-off`
  验证状态：待 B 独立验证。

K72 [⚠️ L3] “经典介质可生成纠缠”不能自动推出“所有经典引力都量子化”，只能说明介质定义必须分层。
  来源：Hall & Reginatto 2021；Bermúdez et al. 2024。
  适用条件：纠缠见证、classical mediator、model-dependent assumptions。
  math_object：`entanglement witness`, `classical mediator`
  验证状态：待 B 独立验证。

K73 [⚠️ L3] classical gravity 作为 mediator 不能独立生成 GIE；若观察到纠缠，说明存在额外非引力源或更细中介结构。
  来源：Schneider, Huggett, Linnemann 2026。
  适用条件：Newton-Cartan 分析、gravity-induced entanglement 论证。
  math_object：`GIE`, `Newton-Cartan`, `classical mediator`
  验证状态：待 B 独立验证。

## 7. 待 B 验证清单

1. `deterministic closure` 是否确实应判为高风险，而不是已完全击毁。
2. stochastic CP-TP closure 是否应写成存活 proposition。
3. Hall-Reginatto 与 Oppenheim 是否可放在同一边界图谱里。
4. “经典介质可生成纠缠”是否必须降级为 model-restricted claim。
5. `decoherence / diffusion trade-off` 是否构成 S3 的主结论。
