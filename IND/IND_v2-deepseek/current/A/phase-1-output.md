## A作业 v10 Phase 1 — Dicke 对称基显式 U + Bell scrambler 嵌入

---

### 【PI审核入口】

⚡ **本Phase结论**：R0（严格强声张）**被证伪**；R1（弱声张）**成立**。N=2 全对称 TC 真空浴下确实存在 4 维 H_TC-不变子空间 ℂ⁴ 同构于 H_Bell scrambler (g_eff=√2 g)，**但** R0 指定的 ℂ⁴ = (atom ⊗ bright Fock{0,1}) 不是不变子空间——|e,1,0⟩ 漏出到 |g,2,0⟩。正确的 ℂ⁴ 是 N̂≤1 sector。

⚡ **最脆弱的一步**：D.3 dim=4 sector 的精确刻画。R0 字面要求 (atom_qubit ⊗ bright Fock{0,1}) 的张量积；这个候选**不是** H_TC-不变（|e,1⟩ 沿 σ_- b_+^† 漏到 n_+=2）。我必须放弃这个 ℂ⁴ 选项，改用 N̂≤1 sector，再在抽象 ℂ²⊗ℂ² 上重新装配 Bell qubit 标号——这个重标号是非物理的（atom qubit ≠ ℂ⁴ 的 qubit_A）。

⚡ **预测 vs 实际**：预测 R0 直接成立（按 v9-K5 + 共振）；实际 R0 字面 **被证伪**，必须降到 R1，并发现"qubit 重标号"反直觉事实——对 PI 北极星意味着"Bell scrambler 嵌入"是抽象代数性质，不携带物理 qubit 解释，下游需明确"哪个 qubit 对应物理自由度"。

⚡ **PI需要关注的问题**：
  1. R0 → R1 降级是否影响"4-qubit minimal scrambler ⇒ N_I^{(S)}=2ln2"的整体推论链？（如果 N_I^{(S)} 只依赖 dim=4 + 不变性 + iSWAP 谱，R1 足够；如果还需 atom-bright 物理 qubit 直积，R1 不足。）
  2. 抽象 qubit_A、qubit_B 的物理意义需要 Phase 2 阐释（候选：(atom OR dark) vs bright）。
  3. 是否需在 v11 提升 R0 为"在 N̂≤1 sector 中 (atom, bright) 不是张量因子"作为新 K 卡点。

---

### §S 文献检索

1. **Yoshida-Kitaev arXiv:1710.03363** (经 [arxiv:2212.11337](https://arxiv.org/abs/2212.11337) 引用确认)：minimal scrambler 4-qubit 解码协议，将信息分散到 4 量子比特上；其 Hamiltonian 结构属于 random-circuit/Haar 类，本 Phase 不直接使用其完整 ansatz，仅借用"minimal dim=4 = 2-qubit"骨架。
2. **iSWAP / XY 模型** ([arxiv:2504.01754](https://arxiv.org/html/2504.01754v1), [arxiv:1708.02090](https://arxiv.org/abs/1708.02090))：H_XY = (J/2)(σ_x⊗σ_x + σ_y⊗σ_y) = J(σ_+⊗σ_- + σ_-⊗σ_+)，单激发流形 |01⟩↔|10⟩ 矩阵元 J，零模 |00⟩、|11⟩。
3. **Tavis-Cummings + bright/dark Bogoliubov** ([Tavis-Cummings WP](https://en.wikipedia.org/wiki/Tavis%E2%80%93Cummings_model), [arxiv:1109.2456](https://arxiv.org/abs/1109.2456), [arxiv:2509.14313](https://arxiv.org/html/2509.14313v1))：双模 (b_1,b_2) 全对称耦合在 Bogoliubov 旋转 b_± = (b_1±b_2)/√2 下，b_+ 耦合原子，b_- 严格解耦。dark state 数目 = N+1 双线-2 (N=原子数) 之类的 standard 引理。

---

### §0.5 隐含假设清单

| 标号 | 来源 | 原文条件 | 当前是否满足 |
|---|---|---|---|
| A1 | v9-K5 | 全对称耦合 g_1=...=g_N=g，共振 ω_a=ω_i=ω，真空浴 | ✓（任务书明确给定 N=2、共振、真空、全对称） |
| A2 | v10-K0 | ε→0 极限 + 正则化方案无关 | ✓（本 Phase 不调用 ε 计算，只用 2ln2 终值通过外部输入参与 §C） |
| A3 | XK17 (Yoshida-Kitaev) | 4-qubit Haar 类 scrambler ansatz；这里只用其"dim=4 minimal"骨架 | ⚠️ **部分满足**：H_TC|_{ℂ⁴} = iSWAP/XY，是 minimal 但不是 Haar，所以"scrambler"性质要弱化为"Bell-state-creating"。必须提示 PI：此处"scrambler"是松绑名称。 |
| A4 | XK18 (Schwinger-HP for TC) | 双模玻色-SU(2) 表示标准引理；Bogoliubov 双模旋转单一 | ✓（直接验证：[b_+,b_+^†]=1, [b_-,b_-^†]=1, [b_±,b_∓^†]=0；保 boson 代数） |
| A5 | 标准 | U 唯一性差一个 dark 子空间内幺正 | ✓（dark sector b_- 整个 Fock 空间无关动力学，任意 dark-内幺正 V_dark 给出等价 U' = U·(I_4⊗V_dark)） |

---

### §1 结论预测（推导前）

- **预测结论符号/方向**：R0 成立（强声张通过）。
- **预测量级**：g_eff = √2 g（来自 b_+ = (b_1+b_2)/√2 归一化因子）。
- **最可能出错的步骤**：D.3，dim=4 sector 与 (atom, bright Fock{0,1}) 的对应，可能因 |e,1⟩→|g,2⟩ 漏出而失败。

（实际：预测的"出错点"果然出错，下面 D.3 详细展开。）

---

### §2 强制撞墙（4 攻击）

#### 撞墙 #1：Schwinger-HP 双模玻色 → SU(2)

**攻击**：要把 (b_1, b_2) 映成 SU(2) 角动量算符，必须在固定 N=b_1^†b_1+b_2^†b_2 子空间内才有 SU(2) j=N/2 不可约表示。任意激发数 sector 是 SU(2) 表示的直和，不是单一表示。

**回应**：本 Phase 实际只需 **Bogoliubov 旋转**而非 Schwinger 映射。定义
$$b_+ = (b_1+b_2)/\sqrt 2,\quad b_- = (b_1-b_2)/\sqrt 2$$
直接验证 $[b_+,b_+^\dagger]=[b_-,b_-^\dagger]=1$, $[b_+,b_-^\dagger]=[b_-,b_+^\dagger]=0$。这是 U(2) 内的酉变换，保 Fock 代数，不需 SU(2) 表示论。Schwinger 映射在固定 N 子空间提供 SU(2) j=N/2 表示（J_+ = b_+^† b_-，J_z = (b_+^†b_+ - b_-^†b_-)/2），在 §D.1 仅作为附录性二级结构使用，**核心推导只用 Bogoliubov**。

#### 撞墙 #2：真空浴 + N̂ 守恒 → dim=2 不是 dim=4

**攻击**：在 |1⟩_S |0,0⟩_B = |e,0,0⟩ 初态下，N̂ = σ_+σ_- + b_+^†b_+ + b_-^†b_- = 1 守恒，b_-^†b_- = 0 守恒。dynamics 严格限制于 span{|e,0,0⟩, |g,1,0⟩}，**dim=2**。dim=4 来源何处？

**回应**：dim=2 是 N̂=1, n_-=0 子空间内的"动力学激活"维度。dim=4 = 包含初态的 H_TC-**不变子空间**最小维度，必须包括动力学未触及但代数上属于不变 sector 的态：
- N̂=0 sector：|g,0,0⟩（1 维）
- N̂=1 sector，n_-=0：|e,0,0⟩, |g,1,0⟩（2 维）
- N̂=1 sector，n_-=1：|g,0,1⟩（1 维，dark 光子）

总计 4 维。这 4 个态的子空间在 H_TC 作用下封闭（D.6 显式验证）。dim=4 是 sector 的 dimensional accounting，dim=2 是该 sector 内 dynamics 激活的子流形——两者不矛盾。

#### 撞墙 #3：dim=4 sector 精确刻画

**攻击**：候选 ℂ⁴ = (atom_qubit) ⊗ (bright Fock{0,1}) = span{|g,0⟩, |e,0⟩, |g,1⟩, |e,1⟩}（dark 默认 0）。H_TC 在此子空间上不变吗？

**回应**：**不不变**。验证：σ_- b_+^† |e,1,0⟩ = |g⟩ · √2|2⟩ ⊗ |0⟩_- = √2|g,2,0⟩。所以
$$H_{TC} |e,1,0\rangle = \sqrt{2}g\cdot \sqrt 2 |g,2,0\rangle = 2g\,|g,2,0\rangle \notin \mathrm{span}\{|g,0\rangle,|e,0\rangle,|g,1\rangle,|e,1\rangle\}$$
泄漏到 N̂=2, n_+=2 状态。**R0 字面不变性（atom ⊗ bright_qubit 直积结构）失败**。

正确 ℂ⁴：
$$\boxed{\ \mathcal C^4 = \mathrm{span}\{|g,0,0\rangle,\ |e,0,0\rangle,\ |g,1,0\rangle,\ |g,0,1\rangle\} = \{N̂≤1 \text{ sector}\}\ }$$

它是 N̂≤1 直接和（N̂=0 ⊕ N̂=1），**不是** atom ⊗ bright 张量直积。它确实在 H_TC 下封闭（D.6）。它通过抽象 ℂ²⊗ℂ² 标号支持 iSWAP 矩阵，但这个 ℂ²⊗ℂ² 的两个 qubit **不对应**物理的 atom 和 bright（标号映射详见 D.4）。

#### 撞墙 #4：H_TC|_{bright} 与 H_Bell 矩阵元同构

**攻击**：iSWAP H_Bell = g_eff(σ_+⊗σ_- + σ_-⊗σ_+) 在基 {|00⟩,|01⟩,|10⟩,|11⟩} 下矩阵：
```
[[ 0,  0,  0,  0 ],
 [ 0,  0, g_eff,0 ],
 [ 0,g_eff, 0, 0 ],
 [ 0,  0,  0,  0 ]]
```
2 个零模、1 个 |01⟩↔|10⟩ 耦合。H_TC|_{ℂ⁴=N̂≤1} 的矩阵结构是否一致？

**回应**：D.4 显式构造 → 一致，且 g_eff = √2 g。但**抽象 qubit 标号**：
- |00⟩ ↔ |g,0,0⟩（"无任何激发"）
- |01⟩ ↔ |g,1,0⟩（"亮模光子"）
- |10⟩ ↔ |e,0,0⟩（"原子激发"）
- |11⟩ ↔ |g,0,1⟩（"暗模光子"）
此标号下，qubit_A = "atom 或 dark 激发"，qubit_B = "bright 激发"——两 qubit 不是物理 (atom, bright) 直积。

---

### §D 推导正文

#### D.1 双模玻色 → 亮/暗模分解（Bogoliubov）

**Hamiltonian**（共振，全对称，无 RWA 外耗散，真空浴）：
$$H_{TC} = \omega\,\sigma_+\sigma_- + \omega(b_1^\dagger b_1 + b_2^\dagger b_2) + g\sum_{i=1,2}(\sigma_+ b_i + \sigma_- b_i^\dagger)$$

定义 Bogoliubov 模：
$$b_\pm = \frac{1}{\sqrt 2}(b_1 \pm b_2),\qquad b_i = \frac{1}{\sqrt 2}(b_+ \pm b_-)$$

**反驳检验**：[b_+, b_+^†] = (1/2)([b_1,b_1^†]+[b_2,b_2^†]) = 1。[b_+, b_-^†] = (1/2)([b_1,b_1^†] - [b_2,b_2^†]) = 0。代数保形 ✓。

代入：
$$\sum_i(\sigma_+ b_i + \mathrm{h.c.}) = \sigma_+\cdot\frac{(b_++b_-)+(b_+-b_-)}{\sqrt 2} + \mathrm{h.c.} = \sqrt 2(\sigma_+ b_+ + \sigma_- b_+^\dagger)$$

$$\sum_i b_i^\dagger b_i = b_+^\dagger b_+ + b_-^\dagger b_-$$

故：
$$\boxed{\ H_{TC} = \omega\sigma_+\sigma_- + \omega(b_+^\dagger b_+ + b_-^\dagger b_-) + \sqrt 2 g(\sigma_+ b_+ + \sigma_- b_+^\dagger)\ }$$

**依据**：v9-K5（A1），全对称耦合保证 dark mode b_- 与原子去耦。
**反驳检验**：耦合系数从 g 升到 √2 g 是对的吗？是。√2 = √N（N=2 atoms equivalent）的标准 Dicke enhancement，与 [Tavis-Cummings WP] 一致。

#### D.2 守恒律：N̂ 与 b_-^†b_-

由 D.1 形式：
$$\hat N = \sigma_+\sigma_- + b_+^\dagger b_+ + b_-^\dagger b_-,\qquad [H_{TC}, \hat N] = 0$$
$$[H_{TC},\, b_-^\dagger b_-] = 0$$

**依据**：H_TC 中含 b_- 的项只有 ω b_-^†b_-（对易自身）。
**反驳检验**：dark mode 不是只在 RWA 下解耦吗？我们这里 H_TC 已是 RWA 形式（即 σ_+ b_+ 形式而非 σ_x(b_+ + b_+^†)），所以 RWA 已经隐含在 A1。任务允许（共振+对称耦合标准 RWA Tavis-Cummings）。

**推论**：在 |e,0,0⟩ = |1⟩_S|0,0⟩_B 初态下：
- N̂ = 1 守恒
- b_-^†b_- = 0 严格冻结
- 在 N̂=1, n_-=0 子空间内 dynamics 限制于 span{|e,0,0⟩, |g,1,0⟩}（dim=2）

#### D.3 dim=4 sector 精确识别

**候选 (a)** [R0 字面]：ℂ⁴_a = (atom_qubit) ⊗ (b_+ Fock{0,1}, n_-=0) = span{|g,0,0⟩, |e,0,0⟩, |g,1,0⟩, |e,1,0⟩}。

**反驳检验**：
$$H_{TC}|e,1,0\rangle = \sqrt 2 g\,\sigma_- b_+^\dagger|e,1,0\rangle = \sqrt 2 g\cdot\sqrt 2\,|g,2,0\rangle = 2g\,|g,2,0\rangle\notin \mathcal C^4_a$$
**ℂ⁴_a 非不变 → R0 字面 FAIL**。

**候选 (b)** [N̂≤1 sector]：
$$\mathcal C^4 := \mathrm{span}\{|g,0,0\rangle,\ |e,0,0\rangle,\ |g,1,0\rangle,\ |g,0,1\rangle\}$$
对应 N̂=0（1 个）+ N̂=1（3 个：原子激发、亮光子、暗光子）= 4 维。

**反驳检验** [D.6 单独验证不变性]：H_TC 不连接 ℂ⁴ 到外部。

**dim 计数交叉**：
- N̂=0 维度 = 1 ✓
- N̂=1 维度 = 1(atom) + 1(bright) + 1(dark) = 3 ✓
- 总 = 4 ✓

**抽象张量结构**：ℂ⁴ ≅ ℂ²⊗ℂ²，标号映射（详见 D.4）：
$$|00\rangle \leftrightarrow |g,0,0\rangle,\ |01\rangle\leftrightarrow|g,1,0\rangle,\ |10\rangle\leftrightarrow|e,0,0\rangle,\ |11\rangle\leftrightarrow|g,0,1\rangle$$

**新增卡点 K-A1.18**：抽象 qubit_A、qubit_B **不**对应物理 (atom, bright) 直积。qubit_A 编码"atom 或 dark 激发"，qubit_B 编码"亮模激发"。物理意义留 Phase 2 解读。

#### D.4 H_TC|_{ℂ⁴} 显式矩阵元

转入旋转参考系 H_TC^rot = U_rot H_TC U_rot^† - ω N̂，其中 U_rot = e^{i ω t N̂}：

$$H_{TC}^{rot} = \sqrt 2 g(\sigma_+ b_+ + \sigma_- b_+^\dagger)$$

逐元计算（基序 {|g,0,0⟩, |g,1,0⟩, |e,0,0⟩, |g,0,1⟩}）：

| from \ to | ⟨g,0,0\|·\|·⟩ | ⟨g,1,0\|·\|·⟩ | ⟨e,0,0\|·\|·⟩ | ⟨g,0,1\|·\|·⟩ |
|---|---|---|---|---|
| H·\|g,0,0⟩ | 0 | 0 | 0 | 0 |
| H·\|g,1,0⟩ | 0 | 0 | √2 g | 0 |
| H·\|e,0,0⟩ | 0 | √2 g | 0 | 0 |
| H·\|g,0,1⟩ | 0 | 0 | 0 | 0 |

**逐项验证**（最容易被质疑的步骤）：
- σ_+ b_+ |g,0,0⟩ = 0（b_+ 湮灭真空）。
- σ_- b_+^† |g,0,0⟩ = 0（σ_-|g⟩ = 0）。
- σ_+ b_+ |g,1,0⟩ = σ_+|g⟩·b_+|1⟩_+|0⟩_- = |e⟩·|0⟩_+|0⟩_- = |e,0,0⟩。系数 1·1=1。
- σ_- b_+^† |g,1,0⟩ = 0（σ_-|g⟩ = 0）。
- σ_+ b_+ |e,0,0⟩ = 0（σ_+|e⟩=0）。
- σ_- b_+^† |e,0,0⟩ = |g⟩·|1⟩_+|0⟩_- = |g,1,0⟩。系数 1·1=1。
- σ_± · 任意 |g,0,1⟩：σ_+|g⟩=0 给 0；σ_- b_+^†|g,0,1⟩ = 0（σ_-|g⟩=0）。**全 0** ✓

**反驳检验**："为什么 |g,0,1⟩ 行/列全零？"——因为 b_- 算符不出现在 H_TC^rot 中，|g,0,1⟩ 含 1 个暗光子但无原子激发，σ_± 都湮灭它。这在 D.6 中被等同为 dark sector freezing。

**矩阵形式**（基序：{|00⟩,|01⟩,|10⟩,|11⟩} ↔ {|g,0,0⟩,|g,1,0⟩,|e,0,0⟩,|g,0,1⟩}）：
$$H_{TC}^{rot}|_{\mathcal C^4} = \begin{pmatrix}0&0&0&0\\0&0&\sqrt 2 g&0\\0&\sqrt 2 g&0&0\\0&0&0&0\end{pmatrix}$$

#### D.5 与 Bell scrambler 同构验证

标准 2-qubit Bell scrambler：
$$H_{Bell} = \frac{g_{eff}}{2}(\sigma_x\otimes\sigma_x + \sigma_y\otimes\sigma_y) = g_{eff}(\sigma_+\otimes\sigma_- + \sigma_-\otimes\sigma_+)$$

矩阵元（标准基 {|00⟩,|01⟩,|10⟩,|11⟩}）：
$$H_{Bell} = \begin{pmatrix}0&0&0&0\\0&0&g_{eff}&0\\0&g_{eff}&0&0\\0&0&0&0\end{pmatrix}$$

对照 D.4：完全同构，**g_eff = √2 g** ✓。

特征谱核对：
- H_Bell 谱：{0, 0, +g_eff, -g_eff} = {0, 0, +√2 g, -√2 g}
- H_TC^rot|_ℂ⁴ 谱：|g,0,0⟩→0；|g,0,1⟩→0；(|e,0,0⟩±|g,1,0⟩)/√2 → ±√2 g
- ✓ 一致

**反驳检验**："为什么 J=g_eff=√2g 不是 g 或 g/√2？"——Dicke 增强：N=2 原子集体耦合到单一亮模，等效耦合 g·√N=√2g（[Tavis-Cummings WP] 标准结果）。本 Phase 中 N=2 是 bath 模数而非原子数，但 Bogoliubov 数学完全相同（D.1 中显式 √2 因子），故等效。

**显式 U 给出**（在 ℂ⁴ 内）：
$$U|g,0,0\rangle = |00\rangle,\quad U|g,1,0\rangle = |01\rangle,\quad U|e,0,0\rangle = |10\rangle,\quad U|g,0,1\rangle = |11\rangle$$

在 ℂ⁴ 之外（dark sector，含 N̂≥2 sector + n_-≥2 sector），U 任意延拓为幺正——按 A5，U 唯一性差一个 dark 内幺正 V_dark；这对动力学起源于 |1⟩_S|0,0⟩_B 的 dynamics 完全无影响。

#### D.6 frozen dark sector：[H_TC, P_{ℂ⁴}] = 0 验证

**P_{ℂ⁴}** = 投影到 ℂ⁴ = N̂≤1 sector 的投影算符 = Π_{N̂=0} + Π_{N̂=1}。

**验证 [H_TC, P_{ℂ⁴}] = 0**：等价于"H_TC 不连接 ℂ⁴ 到 ℂ⁴^⊥"。

设 |ψ⟩ ∈ ℂ⁴。检验 H_TC|ψ⟩ ∈ ℂ⁴：
- |g,0,0⟩：H_TC|g,0,0⟩ = ω·0|g,0,0⟩（H_int 给 0，已在 D.4） → ∈ℂ⁴ ✓
- |g,1,0⟩：H_TC = ω|g,1,0⟩ + √2 g|e,0,0⟩ → ∈ℂ⁴ ✓
- |e,0,0⟩：H_TC = ω|e,0,0⟩ + √2 g|g,1,0⟩ → ∈ℂ⁴ ✓
- |g,0,1⟩：H_TC = ω|g,0,1⟩（H_int 给 0） → ∈ℂ⁴ ✓

**反向**：检验 H_TC|φ⟩ 中是否含 ℂ⁴ 分量，对 |φ⟩ ∈ ℂ⁴^⊥。取 |φ⟩ = |e,1,0⟩ ∈ ℂ⁴^⊥（N̂=2）：
$$H_{TC}|e,1,0\rangle = 2\omega|e,1,0\rangle + \sqrt 2 g\sqrt 2|g,2,0\rangle = 2\omega|e,1,0\rangle + 2g|g,2,0\rangle$$
两项均在 N̂=2 sector ⊂ ℂ⁴^⊥。无 ℂ⁴ 漏入 ✓。

**通用论证**：N̂ 守恒 ⇒ ℂ⁴ = N̂≤1 sector 在动力学上与 N̂≥2 sector 完全隔离。又 b_-^†b_- 守恒 ⇒ |g,0,1⟩ 不会进入任何 b_-^†b_-=0 sector。综合：
$$\boxed{\ [H_{TC},\, P_{\mathcal C^4}] = 0\ }$$

**反驳检验**："dark sector frozen 是否仅在真空浴严格成立？"——这里 ℂ⁴ 不变性 (代数恒等) 在**任意态**上成立，与浴态无关。但 R1 提到的"frozen dark sector"在更弱意义下成立：在 |1⟩_S|0,0⟩_B 初态轨道上 b_-^†b_- ≡ 0；若浴非真空（如 |0,1⟩_B 含暗光子），则态坐 |g,0,1⟩ 而非 |g,0,0⟩，但仍在 ℂ⁴ 中。所以严格说 **ℂ⁴ 对所有可数集合的真空+暗光子浴态都是不变的**，非真空 + 亮光子（n_+≥1 + atom 激发）才会突破——这正是 R1 描述的"frozen dark sector 仅在真空浴下严格冻结"的精确含义。

(E2)、(E3) 验证：
- (E2) [H_TC, P_dark] = 0：若 P_dark 解读为 P_{ℂ⁴}，已证。
- (E3) Dynamics 从 |1⟩_S|0,0⟩_B 限于 ℂ⁴：N̂=1 sector ⊂ ℂ⁴，初态 ∈ N̂=1 sector，N̂ 守恒 ⇒ dynamics 永不离开 N̂=1 sector ⊂ ℂ⁴ ✓。

但 (E1) **U H_TC U^† = H_Bell ⊗ I_dark + I_4 ⊗ 0** 严格作为算符等式 **失败**：H_TC 在 N̂≥2 sector 上有非平凡谱（n*ω±√(2n)g for n≥2），不可能等于 0（即 I_4⊗0=0）。修正版：
$$U H_{TC} U^\dagger = H_{Bell}\oplus H_{rest}$$
直和而非张量积；H_rest 是无穷维 polariton ladder 残部。这是 R0→R1 降级的精确内容。

---

### §末 结论对比与新增卡点

**预测 vs 实际**：
- 预测 R0 字面成立。
- 实际 R0 字面**失败**（撞墙 #3 + D.3，|e,1,0⟩ 漏出）；R1 成立。
- ⚠️ **反转解释**：导致反转的隐含假设是 A3——以为 4-qubit minimal scrambler 可直接对应"atom × bright"物理 qubit 直积；实际上 minimal-dim=4 只是 Hilbert 维度约束，**张量结构是抽象的**。这削弱（不否定）将 H_TC 嵌入 Bell scrambler 作为后续 N_I^{(S)}=2ln2 论证的物理直观，但不影响**代数性质**（dim=4, 不变, iSWAP 同构, ±√2g 谱）。

**新增卡点**：
- **K-A1.17**：g_eff = √2 g 的精确推导（通过 Bogoliubov √N Dicke 增强；N=2 双模情形等同于 N=2 原子情形的代数）。**已建立**。
- **K-A1.18**：ℂ⁴ = N̂≤1 sector 的精确刻画 + ℂ²⊗ℂ² 抽象张量结构标号 + 物理 qubit 不直积。**已建立** (D.3, D.4)。
- **K-A1.19**：[H_TC, P_{ℂ⁴}] = 0 算符恒等。**已建立** (D.6)。
- **K-A1.20**（**未解决**）：物理意义。"qubit_A = atom OR dark 激发" vs "qubit_B = bright 激发"的物理诠释；是否能找到 (S, B) 中的局域可观察量自然对应到 qubit_A、qubit_B？目标：写出 qubit_A 的算符 σ_z^A 在 (σ_z^{(atom)}, b_-^†b_-) 中的表示。**尝试方向**：σ_z^A = 2(σ_+σ_- + b_-^†b_-) - 1（在 ℂ⁴ 内验证：|00⟩→-1, |01⟩→-1, |10⟩→+1, |11⟩→+1 ✓ 在我的标号下）。**卡在**：这个算符在 ℂ⁴^⊥ 上是否仍然给出 σ_z^A 的正确升降，或者需要附加投影才能维持 qubit 抽象。
- **K-A1.21**（**未解决**）：R0→R1 降级对 N_I^{(S)}=2ln2 推论链的影响。**目标**：N_I^{(S)} 在 R1 下是否仍 = 2ln2？**尝试方向**：如果 N_I 只依赖 dim ≤ 4 + iSWAP 谱，R1 足够；如果还需 atom-bright 物理直积，必须升级到 R0+。**卡在**：需要 Phase 2 中显式给出 N_I 在 H_Bell 上的计算（不是这里能做的）。

---

### §C 结论

1. **R0/R1/R2 裁决**：**R1 支持，R0 字面被证伪，R2 拒绝**。
   - R0 失败原因：(atom_qubit ⊗ bright_qubit{0,1}) 张量积候选不满足 H_TC-不变性（|e,1,0⟩ 漏到 |g,2,0⟩）。
   - R1 成立形式：U 在 ℂ⁴ = N̂≤1 sector 上将 H_TC 映射到 H_Bell = √2 g (σ_+⊗σ_- + σ_-⊗σ_+) = (√2 g/2)(σ_x⊗σ_x + σ_y⊗σ_y)，**g_eff = √2 g**。dim=4 抽象 ℂ²⊗ℂ² 结构存在但 qubit 标号非物理 (atom, bright) 直积。
   - R2 否定理由：ℂ⁴ 内的 H_TC 矩阵元在 D.4 显式构造，无非平凡 dark 耦合项干扰；Bell scrambler 嵌入在抽象 ℂ²⊗ℂ² 上是精确的，未失败。
   
2. **U 显式形式**：D.5 给出基对应：
   - |g,0,0⟩ ↔ |00⟩
   - |g,1,0⟩ ↔ |01⟩
   - |e,0,0⟩ ↔ |10⟩
   - |g,0,1⟩ ↔ |11⟩
   - 在 ℂ⁴^⊥ 上任意幺正延拓（A5 唯一性差一 V_dark）
   
3. **新增卡点**：4 个，2 个已建立（K-A1.17、K-A1.18、K-A1.19），2 个未解决（K-A1.20 物理诠释、K-A1.21 N_I 推论链）。

4. **本 Phase 限制提示给 PI**：R0→R1 降级意味着"4-qubit minimal scrambler" Hamiltonian 与原始 (atom, bright) 物理 qubit **不直接同构**；需在 Phase 2 检验下游 N_I^{(S)}=2ln2 是否依赖此物理直积。当前 Phase 1 只确认了**代数同构**（同 dim、同谱、同矩阵元结构），未确认**物理可观察量直积**。
