# LP7-S5 Phase 1 — A 正规推导

生成时间：2026-06-01

## 0. 引用前提

- [LP7-S1] Page-Geilker 边界化 naive expectation-source 半经典方程
- [LP7-S2] BMV 支持媒介非经典，但不能直接推出量子时空
- [LP7-S3] hybrid classical-quantum dynamics 只能写成分层边界
- [LP7-S4] 黑洞信息悖论压成 `J_BH` 四假设不可同真

本 Phase 不提出统一公式本体，只定义它的准入矩阵。

## 1. 候选统一公式的最小公理

### 1.1 测量与源项公理

若公式涉及经典几何或经典源项，它必须说明：

- 在量子测量单次分支上如何取源；
- 为什么不能简单用 ensemble `<T>` 代替 run-by-run source；
- 何时允许 collapse、stochastic 或 feedback 修正。

这直接继承 LP7-S1。

### 1.2 媒介与纠缠公理

若公式允许引力或任何中介生成纠缠，它必须说明：

- 媒介在什么结构下是非经典的；
- 哪些可观测结构假设被使用；
- 为何这不自动等同于“标准量子时空”。

这直接继承 LP7-S2。

### 1.3 混合动力学公理

若公式包含经典-量子混合，它必须满足至少一项：

- stochastic closure；
- CP-TP / no-signaling 形式；
- 或明确写出 deterministic closure 的代价。

这直接继承 LP7-S3。

### 1.4 熵与信息公理

若公式涉及黑洞或强引力，它必须恢复 Page curve，或者明确修改 `J_BH` 四假设中的哪一项。

这直接继承 LP7-S4。

## 2. 统一判据矩阵 J_unify

| 候选类型 | U1 测量源项 | U2 媒介非经典 | U3 混合动力学 | U4 Page curve | U5 可观测量 | 结论 |
|---|---|---|---|---|---|---|
| naive semiclassical source | 否 | 否 | 否 | 否 | 弱 | 排除 |
| classical mediator + feedback | 部分 | 条件成立 | 部分 | 否 | 中 | 仅实验室侧候选 |
| stochastic gravity / CP-TP hybrid | 部分 | 未定 | 是/边界 | 否 | 中 | 分层候选 |
| island-compatible strong-gravity candidate | 与测量边界相容 | 未必需要 | 未定 | 是 | 中高 | 强引力侧候选 |
| 真正统一候选 | 是 | 是或可等效说明 | 是或可控代价 | 是 | 高 | 仅此类进入 LP7 总候选 |

## 3. 候选分层

### 3.1 仅修补实验室侧

这类候选能处理 Page-Geilker / BMV 一侧，但不处理 Page curve。

结论：不是统一公式，只是局部修补。

### 3.2 仅修补强引力侧

这类候选能恢复 Page curve，但不处理测量源项和媒介非经典边界。

结论：也不是统一公式。

### 3.3 同时覆盖两侧

唯一合格者必须：

1. 不把 ensemble `<T>` 当成 per-run 经典源；
2. 能解释纠缠见证的媒介层级；
3. 对 hybrid dynamics 给出非爆炸性结构；
4. 恢复 Page curve；
5. 给出 detector-response 或等价观测量。

## 4. 结论类型

结论类型：**有边界**。

核心结论：

LP7-S5 不是在寻找新公式本身，而是在定义“什么才配叫统一公式候选”。一个候选若只满足实验室边界或只满足强引力边界，就只能算局部修补。真正的统一候选必须同时跨过 U1-U5 五道门槛。

## 5. K 条目候选

K84 [✅ L2] 候选统一公式必须同时通过 U1-U5 五道门槛，才能进入 LP7 总候选。
  来源：LP7-S1/S2/S3/S4 合成
  适用条件：同时处理测量源项、媒介非经典、混合动力学和 Page curve
  math_object：`J_unify`
  data_access_level：derived
  验证状态：待 B 独立验证

K85 [⚠️ L3] 仅恢复实验室侧或仅恢复强引力侧的公式都不是统一公式，只是局部修补。
  来源：LP7-S1/S2/S3/S4 边界合成
  适用条件：只覆盖边界图谱的一侧
  math_object：`J_unify`
  data_access_level：derived
  验证状态：待 B 独立验证

## 6. 待 B 验证清单

1. U1-U4 是否已经足够刻画统一公式候选的最小要求。
2. `J_unify` 是否应该再加 reference-frame 一致性作为第六维。
3. 局部修补与统一候选之间的边界是否清晰。
4. `J_unify` 是否会因为缺少具体公式而变成空判据。

