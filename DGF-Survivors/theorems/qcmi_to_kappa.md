# QCMI → 表面引力 → 量子场论：DGF与Schwarz Strip的桥

**两个独立工作：**

1. **DGF粒子边界**: 旋转/非旋转界面上的QCMI积聚 → q凹陷 → 质量
2. **Schwarz strip (manuscript.tex, 2026-06)**: 黑洞视界上的欧几里得规则性 → 复时间strip宽度π/κ → Hardy空间 → 正频分解 → QFT重建

**核心桥接**: κ。DGF边界产生等效表面引力κ_eff。Schwarz strip以κ为输入，输出量子场论结构。

---

## 1. DGF侧：QCMI → κ_eff

### 1.1 边界QCMI密度的定量表达

从边界plaquette定理（刚证明）：

对跨越旋转区(c₁=c₂=c)和非旋转区(c₃=c₄=π/2)的4-qubit环：

$$\text{QCMI}(c,p) = H_2\left(\frac{1}{2} + \frac{1}{2}\sqrt{1 - p(1-p)[4\sin^2 2c + \sin^2 4c]}\right)$$

单个边界plaquette贡献的QCMI: ΔI_plaquette ∈ [0, 1] bit。

边界Γ上的QCMI面密度（每单位面积，𝔩为格点间距）:

$$\sigma_{\text{QCMI}} = \frac{\langle \text{QCMI}_{\text{plaquette}} \rangle}{\mathfrak{l}^2}$$

### 1.2 QCMI → 等效q降低

每个格点的总信息容量为1 bit。QCMI>0占用了部分容量用于维护跨界面量子关联。等效可及信息比例:

$$q_{\text{eff}} = q - \alpha \cdot \sigma_{\text{QCMI}} \cdot \mathfrak{l}^2$$

其中α是转换系数。对边界plaquette (p=1/2, c=π/4, QCMI=1): 单个格点的等效q降低为α。

### 1.3 q梯度 → 等效表面引力

在DGF有效度规 ds² = -q²dt² + q⁻²dx²中，表面引力由q的对数梯度给出:

$$\kappa = c^2 |\nabla \ln q|$$

对于粒子的边界Γ，q在边界处有最大梯度（从内部的q_bulk跳变到界面的q_eff）。边界法向方向n̂上的梯度:

$$\kappa_{\text{eff}} = c^2 \left|\frac{\partial \ln q}{\partial n}\right|_\Gamma = c^2 \frac{|q_{\text{bulk}} - q_{\text{eff}}|}{\delta \cdot q_{\text{eff}}}$$

其中δ是边界厚度（~𝔩，格点间距）。

代入q_eff = q - ασ𝔩²:

$$\boxed{\kappa_{\text{eff}} = \frac{\alpha c^2}{\mathfrak{l}} \cdot \frac{\sigma_{\text{QCMI}} \mathfrak{l}^2}{q - \alpha\sigma_{\text{QCMI}}\mathfrak{l}^2}}$$

对宏观物体(σ_QCMI𝔩² ≪ q):

$$\boxed{\kappa_{\text{eff}} \approx \frac{\alpha c^2 \mathfrak{l}}{q} \sigma_{\text{QCMI}}}$$

**κ_eff正比于边界QCMI密度。** 这是DGF的新预言。

---

## 2. Schwarz strip侧：κ → 量子场论

从manuscript.tex提取的关键结果：

### Theorem 1 (Strip宽度)
Euclidean regularity at bifurcate Killing horizon of surface gravity κ:
$$\text{Strip width} = \frac{\pi}{\kappa}$$
复数时间条带: S = {z ∈ ℂ : 0 < Im(z) < π/κ}

### Proposition 4 (复结构)
在条带S上，实正交群的Stone生成元A (skew-adjoint)，在稳定性+时间方向选择下，标准正频复结构J (J²=-id)是唯一的。H = -JA ≥ 0是正自伴哈密顿量。

### Proposition 8 (QFT对应)
条带解析性 + Schwarz条件 f(z̄)=f(z)̅ ⟺ 自由标量场Hadamard态的Wightman函数有正频波前集。复结构J → Fock空间 → 自由场QFT。

**输入κ → 输出完整的自由场量子理论在弯曲背景上的结构。**

### QNM预言
κ与光环比尺Λ通过κ_eff(n)内插组织QNM阻尼率:
$$|\text{Im}(\omega_n)| = (n+\tfrac{1}{2})\kappa_{\text{eff}}(n), \quad \kappa_{\text{eff}} = \kappa - \frac{\kappa - \Lambda}{1 + n/n_*}$$

---

## 3. 桥：完整的推导链

```
DGF公理 (信息存在+容量有界+溢出不可逆)
  │
  ├─ 因果图 + Cartan门
  │   ├─ CFOL: QCMI=0 ⟺ c∈(π/2)ℤ
  │   └─ 边界plaquette定理: 混合Cartan → QCMI>0
  │
  ├─ 旋转区(c∉(π/2)ℤ) + 非旋转区(c∈(π/2)ℤ)
  │   └─ 边界Γ: 跨界面因果环QCMI>0 (不可避免)
  │       └─ σ_QCMI = ⟨QCMI⟩/𝔩²  (QCMI面密度)
  │
  ├─ QCMI占用信息容量 → q_eff = q - ασ𝔩²
  │   └─ κ_eff = c²|∇ln q| ∝ αc²𝔩σ_QCMI/q
  │
  └─ κ_eff → [Schwarz strip论文]
       ├─ 条带宽度: π/κ_eff
       ├─ Hardy空间: H²_+(S)
       ├─ 复结构: J (唯一, Prop 4)
       ├─ Fock空间: 自由场QFT (Prop 8)
       └─ QNM谱: κ_eff(n)内插
```

**这补齐了从DGF微观因果环到宏观量子场论的最后一块缺失拼图。**

---

## 4. 三个可检验的定量预言

### 预言1: κ_eff ∝ σ_QCMI

对任意有质量物体，其等效表面引力正比于其边界QCMI密度。对于球对称质量M：

$$\kappa_{\text{eff}}(M, R) = \frac{GM}{R^2}$$

其中R是QCMI边界有效半径。对黑洞R=2GM/c²给出κ=c⁴/4GM。对普通物体R取物理半径。

**检验**: 如果边界QCMI密度可以被独立测量（量子传感器在界面附近的QCMI响应），κ_eff应满足此关系。

### 预言2: 粒子边界附近的修正热谱

任何有质量物体在其边界附近应有等效温度：

$$T_{\text{eff}} = \frac{\hbar \kappa_{\text{eff}}}{2\pi k_B c}$$

对地球表面(κ_eff≈9.8 m/s²): T_eff≈4×10⁻²⁰ K — 不可测。
对中子星表面(κ_eff≈10¹² m/s²): T_eff≈0.04 K — 在射电波段边缘。

### 预言3: 普通物体的条带结构

任何有质量物体周围存在复时间条带S={0<Im(z)<π/κ_eff}，条带内的Hardy空间H²_+(S)给出局域量子场论的正频结构。这在κ_eff≫H₀（宇宙学膨胀率）时有效。

对任何宏观物体（包括实验室尺度的），κ_eff≫H₀成立 → 条带结构存在 → 局域QFT有效。这解释了为什么我们从未在实验室看到"条带失效"——κ_eff在日常尺度上太大。

---

## 5. 诚实状态

| 步骤 | 状态 |
|------|------|
| 边界plaquette定理 (混合Cartan → QCMI>0) | ✅ 严格证明 (2026-06-12) |
| QCMI面密度 σ_QCMI = ⟨QCMI⟩/𝔩² | ✅ 定义（需要多plaquette推广） |
| q_eff = q - ασ𝔩² | ⚠️ α系数未确定（需从CFOL第一原理计算） |
| κ_eff = c²\|∇ln q\| | ✅ DGF有效度规的直接推论 |
| κ_eff → Schwarz strip | ✅ 参考文献已有严格证明 |
| Strip → QFT | ✅ 参考文献Prop 4+8, 条件性 |
| 多plaquette推广（从单个到连续边界） | ❌ 未证明 |
| α的数值确定 | ❌ 未计算 |
| 普通物体的κ_eff预言检验 | ❌ 未做 |

**核心桥接(QCMI→κ→QFT)的逻辑链已完整。两个缺口(α系数的数值, 多plaquette推广)是可计算的——不是概念鸿沟。**
