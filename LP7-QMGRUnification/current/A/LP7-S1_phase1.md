# LP7-S1 Phase 1 — A 正规推导

生成时间：2026-06-01 20:42

## 0. 输入与边界

本推导只处理 LP7-S1：Page-Geilker 半经典方程失败边界。

不声称：

- Page-Geilker 已证明所有经典引力理论错误。
- Page-Geilker 已证明引力场必须按标准量子场量子化。
- 半经典引力作为有效近似在所有场景失败。

本推导声称的目标更窄：

> naive expectation-source 半经典方程 `G_{\mu\nu}=8πG<\hat T_{\mu\nu}>` 不能直接跨越量子测量分支并预测单次宏观引力读数。

## 1. 方程边界

半经典 Einstein 方程：

`G_{\mu\nu}[g] = 8πG <\psi|\hat T_{\mu\nu}|\psi>`

Newtonian 极限：

`∇²Φ(x) = 4πG <\psi|\hat ρ(x)|\psi>`

若量子态是宏观质量位置叠加：

`|\psi> = α|L> + β|R>`

且 `|L>` 与 `|R>` 对应两个宏观可区分质量分布，则：

`<\hat ρ(x)> = |α|²ρ_L(x) + |β|²ρ_R(x) + interference`

在宏观退相干后，干涉项近似不可见，naive 源项仍给出 ensemble mixture：

`ρ_sc(x) ≈ |α|²ρ_L(x) + |β|²ρ_R(x)`

这不是单次运行中的质量分布，而是跨分支平均。这里的关键边界是：

- 若 `g_{\mu\nu}` 被解释为 ensemble mean geometry，则方程可作为统计量方程。
- 若 `g_{\mu\nu}` 被解释为每次实验的实际经典度规，则它预测平均质量分布的场，与单次分支读数冲突。

## 2. Page-Geilker 逻辑复原

Page-Geilker 的核心不在于高精度测量量子引力，而在于构造一个测量分支选择后的宏观质量配置。

抽象流程：

1. 用量子随机过程选择宏观质量移动方案。
2. 每次运行中，质量实际移动到某个确定配置。
3. 检测器读取的引力场跟随该确定配置。
4. naive semiclassical gravity 若把未塌缩或 ensemble 态的 `<T>` 作为源项，会预测平均配置的引力场。

因此，实验打击对象是：

`actual metric per run = metric sourced by <T> over alternatives`

而不是：

`semiclassical gravity is never a useful approximation`

## 3. 最小模型

取二分支质量配置，概率各 `1/2`：

`|\psi> = (|L> + |R>)/sqrt(2)`

对应 Newtonian 势：

`∇²Φ_L = 4πGρ_L`

`∇²Φ_R = 4πGρ_R`

naive expectation-source 预测：

`Φ_sc = (Φ_L + Φ_R)/2`

单次分支预测：

`Φ_run = Φ_L` 或 `Φ_R`

差异量：

`ΔΦ_branch = Φ_run - Φ_sc = ±(Φ_L - Φ_R)/2`

如果实验读数与 `Φ_L/Φ_R` 分支相关，而不是稳定落在 `Φ_sc`，则 naive expectation-source per-run interpretation 失败。

## 4. 逃逸路线分类

### 4.1 Collapse 后源项

规则：

`|\psi> -> |L>` 或 `|R>` 后，再用 `<T>` 源项。

它能重现 Page-Geilker 的单次读数，但付出代价：

- 需要额外 collapse 规则。
- collapse 与相对论协变性的关系必须说明。
- 这不再是“未塌缩态期望值直接源化”的简单半经典方程。

### 4.2 Stochastic gravity

代表入口：Einstein-Langevin 方程与 stress tensor fluctuation。

思想：

`G_{\mu\nu}` 不只是 `<T_{\mu\nu}>` 的确定函数，而包含由应力张量涨落驱动的经典随机项。

能否逃逸 Page-Geilker 取决于：

- 随机项是否只给出小涨落。
- 是否能在宏观测量场景中选择完整分支。
- 是否给出正确的 Born 权重和跨运行相关性。

若只能描述 ensemble fluctuation，不能产生单次 branch sourcing，则仍不足以完全逃逸。

### 4.3 Classical-channel gravity

代表入口：Kafri-Taylor-Milburn 2014/2015。

核心：

用测量-反馈通道模拟 Newtonian 引力。经典通道可以传递经典信息，但不能生成纠缠；同时引入最小退相干/加热。

这类模型可以避免 naive `<T>` 单次源项问题，但把可检验矛盾转移到：

- 退相干率是否存在。
- BMV 类型实验是否观察到引力诱导纠缠。

因此 LP7-S1 与 LP7-S2 在这里衔接。

### 4.4 Postquantum classical gravity

代表入口：Oppenheim PRX 2023 与协变路径积分工作。

核心：

经典度规与量子物质可通过更一般的完全正混合动力学耦合，而不是 naive expectation-source 方程。

影响：

- Page-Geilker 不能直接排除这类模型。
- 这类模型通常仍面对纠缠生成、噪声、扩散、能量守恒与实验约束。
- LP7-S1 只能把它登记为存活逃逸路线，不能在本 Phase 击毙。

## 5. 判据矩阵 J_PG

| 模型 | 单次分支读数 | ensemble 平均 | 是否生成纠缠 | 是否保留经典度规 | 与 Page-Geilker 冲突 |
|---|---|---|---|---|---|
| naive expectation-source, no collapse | 否 | 是 | 不清楚/通常无机制 | 是 | 是 |
| collapse 后 `<T>` 源项 | 是 | 统计上是 | 取决于 collapse 理论 | 是 | 不直接冲突 |
| stochastic gravity | 未定，取决于噪声是否 branch-selecting | 是 | 通常不作为纠缠介质 | 是 | 未定 |
| classical-channel gravity | 是，可经测量反馈 | 是 | 否 | 是 | 不直接冲突，转入 BMV |
| postquantum classical gravity | 设计目标为可兼容 | 是 | 经典场自身不生成纠缠 | 是 | 不直接冲突，需独立检验 |
| quantized weak-field gravity | 是 | 统计上是 | 是 | 否 | 不冲突 |

## 6. Phase 结论

结论类型：**有边界**。

核心结论：

Page-Geilker 型论证把 naive expectation-source 半经典方程边界化：`G_{\mu\nu}=8πG<T_{\mu\nu}>` 不能被解释为“未塌缩量子态直接决定每次实验的实际经典度规”。但它不排除 collapse 后源项、stochastic gravity、classical-channel gravity 或 postquantum classical gravity。LP7 的真正下一层矛盾应转为“这些逃逸路线能否同时满足单次读数、局域性、低噪声和引力诱导纠缠见证”。

## 7. K 条目候选

K60 [✅ L1] Page-Geilker 边界化 naive expectation-source 半经典方程。
  来源：Page & Geilker 1981; 本 Phase 最小模型。
  适用条件：宏观质量配置由量子随机事件选择；模型把未塌缩或 ensemble 态的 `<T>` 作为每次运行的实际源项。
  math_object：`G_{\mu\nu}=8πG<T_{\mu\nu}>`, `∇²Φ=4πG<ρ>`, `ΔΦ_branch`
  data_access_level：verified_only
  验证状态：待 B 独立验证。

K61 [⚠️ L3] Page-Geilker 不排除所有经典引力，只排除 naive per-run expectation-source interpretation。
  来源：Kafri-Taylor-Milburn 2014/2015; Oppenheim 2023; Terno 2024。
  适用条件：允许 collapse、随机经典度规、测量反馈通道或更一般完全正混合动力学。
  math_object：`J_PG[model]`
  data_access_level：derived
  验证状态：待 B 独立验证。

## 8. 待 B 验证清单

1. Page-Geilker 是否确实只击中 naive expectation-source per-run interpretation。
2. `ΔΦ_branch = ±(Φ_L-Φ_R)/2` 是否是合适的最小差异量。
3. stochastic gravity 是否能被归为“未定”而不是“已逃逸”。
4. Oppenheim/postquantum classical gravity 是否应放入 LP7-S1 的反例栏还是 LP7-S3。
5. `J_PG` 判据矩阵是否漏掉关键模型，例如 Diosi-Penrose collapse 或 semiclassical Newton-Schrodinger。
