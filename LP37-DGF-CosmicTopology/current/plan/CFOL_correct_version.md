# CFOL正确版本 — 手算推导

## 问题

对4节点因果环 Q_a→E_1→Q_b→E_2→Q_a：
什么时候 QCMI = I(R;E'|Q') = 0？

## 设定

- 边酉：u_i = D(c^{(i)})，Cartan规范固定后
- D(c) = exp(i Σ_k c_k σ_k ⊗ σ_k)，k∈{x,y,z} for d=2
- 环境初态：γ = diag(γ₀, γ₁)，γ₀+γ₁=1
- 初始总态：Φ⁺_{RQ} ⊗ γ_{E1} ⊗ γ_{E2}

## 步骤1：Cartan核心的乘积

**关键事实：** σ_k⊗σ_k 和 σ_l⊗σ_l **不对易** (k≠l)。

证明：在su(2)⊗su(2)中，Cartan子代数由{σ_z⊗I, I⊗σ_z}张成。DGF用的{σ_x⊗σ_x, σ_y⊗σ_y, σ_z⊗σ_z}张成的是另一组基，它们互相不对易：

$$[\sigma_x\otimes\sigma_x, \sigma_y\otimes\sigma_y] = 2i\sigma_z\otimes\sigma_z$$

因此两个一般Cartan核心的乘积有BCH校正：

$$D(a)D(b) = \exp(i a\cdot\vec{\sigma}\otimes\vec{\sigma}) \exp(i b\cdot\vec{\sigma}\otimes\vec{\sigma})$$
$$= \exp(i(a+b)\cdot\vec{\sigma}\otimes\vec{\sigma} - \frac{1}{2}[a\cdot\vec{\sigma}\otimes\vec{\sigma}, b\cdot\vec{\sigma}\otimes\vec{\sigma}] + ...)$$

**当且仅当 a ∥ b（即a和b平行）时**，BCH校正为零，乘积简化为D(a+b)。

若a∦b，乘积产生非Cartan项（包含σ_k⊗σ_l, k≠l的项），导致Q-E纠缠 → QCMI > 0。

## 步骤2：Cartan轴对齐条件

这是CFOL正确的核心条件：

**引理（Cartan对齐）：** 环上四条边的Cartan参数c^{(1)}, c^{(2)}, c^{(3)}, c^{(4)}全部互相平行（即存在单位向量n̂使c^{(i)} = c_i n̂对所有i），是QCMI=0的必要条件。

**证明：** 若存在i,j使c^{(i)} ∦ c^{(j)}，则D(c^{(i)})和D(c^{(j)})不对易。BCH校正产生非Cartan项。这些非Cartan项在Kraus算子K_{ab} = ⟨a|⟨b| U |γ⟩|γ⟩中产生非平凡的Q-E关联——不能被任何局部基变换消除。由HJPW定理，这意味着QCMI>0。□

这是CFOL在Cartan语言中的实质内容：**QCMI>0当且仅当至少两条边的Cartan轴不对齐。**

## 步骤3：Cartan对齐条件下的简化

当所有c^{(i)} ∥ n̂时，所有D(c^{(i)})互相交换，总酉为：

$$U = D(c^{(1)}+c^{(2)}+c^{(3)}+c^{(4)}) = D(C_{\text{tot}})$$

其中C_tot = c^{(1)}+c^{(2)}+c^{(3)}+c^{(4)}沿n̂方向。

环的"有效操作"就是一个大的Cartan旋转：总角度 = |C_tot| = |Σ c_i|。

## 步骤4：QCMI=0的充要条件

在Cartan对齐下，Kraus算子计算简化为：

$$K_{ab} = \langle a|_{E1}\langle b|_{E2} D(C_{\text{tot}}) |\gamma\rangle_{E1}|\gamma\rangle_{E2}$$

展开Cartan核心在n̂轴的本征基中（σ_n̂的本征值为±1），记：
$$D(C_{\text{tot}}) = \cos(|C_{\text{tot}}|) I + i\sin(|C_{\text{tot}}|) \sigma_{\hat{n}}\otimes\sigma_{\hat{n}}$$

Kraus算子在σ_n̂⊗σ_n̂本征基下是对角化的，四个可能的(a,b)组合给出四个独立通道。QCMI=0要求这些通道互成比例。

**最终条件：**
$$\boxed{I(R;E'|Q') = 0 \iff \begin{cases} c^{(1)} \parallel c^{(2)} \parallel c^{(3)} \parallel c^{(4)} & \text{(Cartan轴对齐)} \\ \text{且} \\ \gamma_0=\gamma_1=\frac{1}{2} \;\text{或}\; |C_{\text{tot}}| = n\pi & \text{(有效旋转平凡化)} \end{cases}}$$

## 步骤5：与已有结果的自洽验证

1. **CNOT环**：所有c沿z轴（对齐✓），γ任意。|C_tot| = |π/4+π/4+π/4+π/4| = π → 满足n=1条件 → QCMI=0。✓ 与数值一致。

2. **Haar随机环**：c方向随机 → Cartan轴不对齐 → QCMI>0。✓

3. **对易性定理**（LP36 III）：Cartan对齐 → QCMI相消 = 短量子马尔可夫链的特殊情况。轴失配 → BCH累积 → QCMI>0。✓ 恢复LP36全部17门扫描结果。

4. **γ₀≠γ₁条件**：当|C_tot|≠nπ时，需要γ₀=γ₁=1/2来使两个通道成比例。这恢复了CFOL原始证明中的γ₀≠γ₁作为QCMI>0的充分条件。

## 步骤6：这个版本修正了什么

**旧版本（R1-R3）的错误：**
- [C-GAP-1]：假设Cartan核心总是交换（不总成立）
- R3 §1.7的σ_x符号错误：错误地认为E₂+E₁Ψ=0可以被单扇区满足（实际上需要四扇区同时满足 → ṽ₀=w̃₀=0）

**正确版本：**
- Cartan轴对齐是明确的前提条件（不可以假设）
- 条件自然地退化到HJPW(2004)的短量子马尔可夫链
- γ₀≠γ₁和Cartan轴失配各自独立产生QCMI>0，且效应叠加

## 步骤7：对DGF框架边界的影响

这个正确版本给出了DGF在量子信息层面的精确边界：

**DGF能严格描述的：**
- 因果环上Cartan轴对齐/失配如何创造/消灭量子非马尔可夫性
- QCMI>0的充分条件（Cartan轴失配 OR γ₀≠γ₁）
- 退相干速率的拓扑下界（每个不对齐的环贡献η₀）

**DGF不能严格描述的（需要Cartan对齐假设）：**
- QCMI的精确值（需要完整BCH展开，无限级数）
- 一般多环的b₁可加性（每个环的Cartan轴方向独立 → 有指数多种对齐组合）

**DGF到薛定谔的路线：**
Cartan对齐条件直接连接到了量子达尔文主义：全局Cartan轴 = 指针基方向。当因果环网络上的所有环共享同一个Cartan轴不动点时，该方向就是系统的有效指针基。这不需要从A1+A2推导复数Hilbert空间——而是假设了quantum mechanics的数学框架（Hilbert空间、酉演化），然后问：在这个框架中，经典性是如何被因果拓扑强制产生的。

所以DGF的边界在：**假设量子力学的数学结构，解释经典世界的拓扑起源。** 不是替代薛定谔方程，而是解释为什么薛定谔方程的线性结构会导致某些系统的经典行为。
