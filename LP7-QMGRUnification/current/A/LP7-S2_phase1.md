# LP7-S2 Phase 1 — A 正规推导

生成时间：2026-06-01 20:42

## 0. 输入与边界

本 Phase 只处理 BMV / gravitationally-induced entanglement witness 的局域性边界。

不声称：

- BMV 实验已实际完成对量子引力的最终证明。
- 任意观察到的探针纠缠都必然来自量子引力。
- 经典媒介下永远不可能出现任何纠缠样外观。

本 Phase 只问：

> 在“局域、无初态隐藏相关、媒介仅通过局域相互作用、并对探针纠缠作标准量子可观测定义”这些假设下，BMV witness 是否要求媒介非经典？

## 1. witness 结构

BMV 的核心信息论句子可写成：

若系统 `M` 仅以局域方式与两个量子探针 `A,B` 相互作用，而

`Ent(A:B)_out > 0`

则 `M` 不能是完全经典的。

更保守地说，它不能是“既局域又完全经典信息通道”的那类媒介。

这不是在说：

- 一定要有可观测时空叠加；
- 一定要有标准意义上的 graviton；
- 一定要用某种单一动力学方程。

它说的是：**纠缠作为输出，能把“完全经典的局域媒介”排除掉。**

## 2. 最小假设表

### 2.1 局域性

若两探针远离，而媒介与每个探针的耦合都是局域的，则纠缠若生成，必须是通过媒介的局域传播而来。

若“局域”被偷偷放松成非局域层析或全局约束，则 witness 的逻辑失效。

### 2.2 初态无隐藏相关

若 A-B 初态已含相关，或媒介与 A/B 共享隐藏资源，则末态纠缠不能直接归因于媒介本身。

### 2.3 媒介的经典性

经典媒介通常意味着：

- 可同时具有确定经典态描述；
- 不携带标准量子相干；
- 不能作为普通量子信道那样传输纠缠。

若一个模型保持“经典基底”但引入非局域层析失效、隐藏量子资源或测量反馈，那么它未必是“完全经典”。

### 2.4 纠缠可测

输出必须是能由标准量子信息指标识别的纠缠，而不是仅仅某种相关函数变化。

## 3. 经典媒介逃逸路线

### 3.1 Classical-channel / measurement-feedback

这类模型把引力解释为测量-反馈通道。

性质：

- 能保留经典度规图像；
- 通常伴随最小退相干或噪声；
- 不能在纯经典意义上作为纠缠通道。

因此它能逃过“naive classical field”表述，但逃不过“纠缠通道”判据。

### 3.2 Non-locally tomographic coupling

2025 的 toy model 直接说明：经典基底的介质如果放松 local tomography，可在局域耦合下表现出纠缠生成。

这意味着：

- “经典基底”不等于“完全经典”；
- BMV witness 的逻辑必须明确假设 local tomography 或其等价条件。

### 3.3 Collapse-based / postquantum hybrid model

若 collapse dynamics 本身携带非局域特征，或者通过隐藏检测器/额外自由度重建纠缠，则这并不是纯 classical mediator。

结论上，它们属于“经典媒介逃逸”还是“其实已引入非经典资源”要靠模型细节裁决。

## 4. 不可同真条件

若以下四项同时成立：

1. A-B 初态无隐藏相关；
2. 媒介只通过局域耦合传播；
3. 媒介满足 local tomography；
4. 末态出现可验证纠缠；

则“媒介完全经典”与“观察到纠缠”不可同真。

这就是 BMV witness 的骨架。

## 5. 判据矩阵 J_BMV

| 模型 | 局域性 | local tomography | 能否生成纠缠 | 是否仍算完全经典媒介 |
|---|---|---|---|---|
| naive classical field, local, no hidden resource | 是 | 是 | 否 | 是 |
| classical-channel / measurement-feedback | 是 | 是 | 通常否 | 是，但带退相干 |
| non-locally tomographic toy mediator | 是/局域耦合 | 否 | 是 | 否 |
| collapse-based model with hidden nonlocality | 未必 | 未必 | 可能是 | 通常否 |
| linearised quantum gravity | 是 | 是 | 是 | 否 |

## 6. Phase 结论

结论类型：**有边界**。

核心结论：

BMV witness 的强处不在于“观测到纠缠就自动证明时空叠加”，而在于：在局域性、初态独立和 local tomography 等条件下，探针纠缠可把“完全经典媒介”排除掉。反过来，2025 的 toy model 说明如果故意放松 local tomography，就可能在“经典基底”下伪装出纠缠生成，因此 witness 的结论必须连同假设一起读。

## 7. K 条目候选

K62 [✅ L1] BMV witness 依赖局域性、初态独立和纠缠可测假设。
  来源：Marletto & Vedral 2017; Bose et al. 2017; Di Pietra et al. 2024。
  适用条件：媒介只通过局域作用与探针耦合，且不预载隐藏 A-B 相关。
  math_object：`Ent(A:B)`, local mediator, locality assumption
  data_access_level：verified_only
  验证状态：待 B 独立验证。

K63 [⚠️ L3] 经典基底不等于完全经典媒介；non-locally tomographic coupling 可生成纠缠样外观。
  来源：Vidal et al. 2025。
  适用条件：放松 local tomography，允许非局域层析失效。
  math_object：local tomography, classical basis, entanglement witness
  data_access_level：derived
  验证状态：待 B 独立验证。

## 8. 待 B 验证清单

1. BMV witness 的最小假设是否应显式包含 local tomography。
2. classical-channel gravity 是否应被列为“仍算完全经典媒介”还是“经典但带噪声的存活路线”。
3. collapse-based 模型是否应在 LP7-S2 中单列或并入 LP7-S3。
4. 2025 toy model 是否足以作为 witness 的反例栏，而不是主结论的推翻。
