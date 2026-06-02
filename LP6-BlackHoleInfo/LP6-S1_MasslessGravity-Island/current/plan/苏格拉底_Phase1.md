# 苏格拉底自对话 — MasslessGravity-Island v1 Phase 1

> 3 轮视角切换，精化原始北极星
> 2026-06-01

---

## 原始北极星（来自候选池 LP6-S1）

> 无质量引力（Λ=0 渐近平坦时空）中纠缠岛屿是否存在？

**初步驱动矛盾：**
- 命题A（岛屿可推广）：Antonini-Sasieta-Swingle (arXiv:2602.06543, 2026)
- 命题B（规范障碍）：Geng-Karch-Randall-Tajdini-Raju (arXiv:2506.04311, 2025)

---

## 第一轮：微分同胚不变性视角

**问题重述：** 在 AdS/CFT 中，岛屿公式之所以 work，是因为 AdS 边界有固定度规（conformal boundary），微分同胚在边界上 fall off 得足够快。但在渐近平坦时空中，边界是 null infinity (ℐ⁺ ∪ ℐ⁻)，微分同胚的 fall-off 由 BMS 群控制。关键区别：

1. **AdS 中**：度规在边界附近行为是 g_μν ~ 1/z² (dz² + η_ij dx^i dx^j)。边界条件固定了 conformal class → residual diffeos 只是 conformal Killing vectors（有限维）。岛屿区域由 QES 条件定义 → diffeo-invariant because the extremization is over diffeo-invariant quantities (area + entropy)。

2. **Flat space 中**：度规在 null infinity 附近行为是 g_μν ~ (Bondi gauge)。Residual diffeos = BMS 群（无限维！包括 supertranslations）。岛屿的"位置"是否 BMS-invariant？

**核心精确化：**
问题不是"岛屿是否存在"，而是"岛屿能否被 diffeomorphism-invariant 地定义"。

**精确化后的命题：**
- **命题A'**：存在一个 BMS-invariant 的 QES 条件，使得岛屿位置在渐近平坦时空中是规范不变的。
- **命题B'**：BMS supertranslation 使任何有限区域（包括岛屿候选区域）的"位置"依赖于 supertranslation 框架选择 → 岛屿位置是规范 artifact → 岛屿公式在 flat space 中没有物理意义（除非指定某种 supertranslation frame）。

**关键子问题：**
1. QES 条件中 area term 在 null infinity 附近的 supertranslation 变换下是否不变？
2. Entropy term S_bulk 在 flat space 中是否有规范不变的定义？
3. 即使岛屿位置是规范依赖的，Page 曲线（熵的 time evolution）是否仍是规范不变的？

---

## 第二轮：量子信息/操作性视角

**问题重述：** 从 quantum information 角度看，纠缠岛屿是什么？

岛屿 = 辐射密度矩阵的 replica 计算中出现的 new saddle。它告诉你"辐射态 ρ_rad 的 von Neumann 熵由哪些 bulk 自由度贡献"。Operationally：
- 岛屿内的自由度"属于"辐射的 entanglement wedge
- 在 Page time 之后，辐射包含了黑洞内部的某些信息——但这些信息 encoding 在辐射的哪些自由度中？岛屿公式通过"哪些 bulk 区域对辐射熵有贡献"来回答

**Flat space 中 operational 定义的问题：**
- AdS 中有明确的 boundary → bulk dictionary（HKLL, extrapolate dictionary）
- Flat space 中没有这样明确的 dictionary——我们需要理解 QFT on I⁺ 与 bulk 的关系
- Celestial holography 试图建立这样的 dictionary，但远不如 AdS/CFT 成熟

**精确化后的命题（操作性版）：**
- **命题A''**：即使 QES 位置的规范不变性有 subtlety，Page 曲线（辐射 von Neumann 熵作为 time 的函数）是 BMS-invariant 的。Island 贡献的 entanglement entropy 有一个规范不变的 operational 定义（通过 replica trick on I⁺）。
- **命题B''**：Replica trick 在 flat space 中需要处理 IR 发散（soft graviton contributions），这些 IR 问题使 replica partition function 的 saddle-point 分析不 well-defined。没有 well-defined 的 path integral → 没有 island formula。

**关键子问题：**
1. Flat space replica wormhole: 渐近平坦边界条件是否允许 replica wormhole 作为 saddle？
2. Soft graviton 对 replica partition function 的贡献是否破坏了 saddle-point 结构？
3. Infrared 发散是否可以被 celestial conformal block decomposition 处理？

---

## 第三轮：具体模型/设置对比视角

**问题重述：** 不去问"island 在 flat space 中一般是否存在"，而是问"在具体的、计算上可控的 flat space toy model 中，island 是否存在"。

**候选 models：**
1. **JT 引力在 flat space limit**：JT 引力在 Λ → 0 的极限 → flat JT（CGHS/RST model 的近亲）。这个模型中是否有 island？
2. **3D flat space 重力**：3D Einstein gravity with Λ=0 → 由 BMS₃ 代数控制。边界是 2D Carrollian CFT。可以在 Carrollian CFT 中定义 island formula？
3. **4D asymptotically flat black hole + bath**：最近似 Antonini et al. (2026) 的设置。需要理解 replica wormhole 在 4D flat space 中的 saddle 结构。

**精确化后的命题（模型依赖版）：**
- **命题A'''**：在至少一个 well-defined flat space toy model（如 3D flat gravity + Carrollian bath）中，island formula 可以 diffeomorphism-invariant 地定义，并给出正确的 Page 曲线。
- **命题B'''**：在所有已知 flat space toy models 中，要么 replica wormhole saddle 不存在（因 IR 问题），要么 island 位置是规范 artifact（因 BMS supertranslation），没有一个模型同时满足 island formula 的两个必要条件（well-defined QES + Page curve）。

---

## 综合精确化：最终驱动矛盾

综合三轮视角切换，将原始北极星精化为：

> **核心矛盾：** 在渐近平坦时空中，岛屿公式需要同时满足三个条件：
> (C1) QES 位置是规范不变的（BMS-invariant）
> (C2) Replica wormhole saddle 在 flat space path integral 中 well-defined
> (C3) 岛屿贡献使 Page 曲线在 Page time 之后下降
>
> **命题A（三个条件可以被同时满足）**：在至少一个 well-defined setting（如 3D flat gravity）中，存在 BMS-invariant QES + well-defined replica saddle + Page curve。
>
> **命题B（三个条件不能同时满足）**：BMS supertranslations 使 C1 失败（GR 障碍），或 IR soft graviton 使 C2 失败（QFT 障碍），或两者各自的 bypass 互相排斥——C1 的 bypass（固定 supertranslation frame）使 C2 的 bypass（celestial block decomposition）失效。

**为什么不能同时为真：** C1 需要固定 BMS frame（选择特定的 supertranslation Lorentz frame），而 C2 的 celestial approach 在任意 supertranslation frame 中不保持 replica symmetry → C1 和 C2 的 bypass 方案可能互斥。

**为什么这是好北极星：**
- 可分解为三个可独立检验的子问题
- 3D flat gravity 是一个计算上可达的 toy model
- 即使结论是"三个条件不能同时满足"，也是有用的否定性定理
- 正面验证（如果 C1+C2+C3 可同时满足）将直接扩展岛屿公式到 flat space

---

## 候选分解（子命题）

### S1a：BMS-invariant QES
**命题：** 渐近平坦时空中的 QES 条件是否在 BMS supertranslations 下不变？
- 成立 → 存在规范不变的 S_gens 定义
- 证伪 → 岛屿位置根本上是规范 artifact → flat space island 无物理意义

### S1b：Flat space replica wormhole
**命题：** 渐近平坦边界条件是否允许 replica wormhole saddle？
- 成立 → replica trick 在 flat space 中 well-defined
- 证伪 → 不存在 flat space island formula，无论 QES 是否规范不变

### S1c：3D flat gravity 验证
**命题：** 在 3D asymptotically flat gravity（BMS₃/Carrollian CFT 对偶）中，S1a 和 S1b 是否同时成立？
- 同时成立 → island formula 在 flat space 中的第一个具体实现
- 任一失败 → 锁定具体障碍（规范 vs IR vs both）

---

## 下一步

- 完成文献库.md（命题 A 和 B 双侧文献各 ≥3 条）
- 生成 A 博士（正规推导 S1a/S1b/S1c）+ B 博士（反面攻击）任务书
- GATE 1 检查
