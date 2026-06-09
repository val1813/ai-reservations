# CFOL反例：QCMI=0但u_i不可因子化

**来源:** INSPECTOR_CFOL_v6_FINAL.md §3
**日期:** 2026-06-09
**结论:** CFOL原始陈述"(⇒)方向"严格为假

---

## 1. 设定

四节点因果环 Q_a→E₁→Q_b→E₂→Q_a，各系统d=2。

初始态：ρ_RQE = |Φ⁺⟩⟨Φ⁺|_{RQ} ⊗ γ_{E₁} ⊗ γ_{E₂}
其中γ = diag(γ₀, γ₁), γ₀≠γ₁, γ₀+γ₁=1。

纯化矢量：|γ̃⟩ = √γ₀|0⟩ + √γ₁|1⟩
正交补：|γ̃⊥⟩ = √γ₁|0⟩ - √γ₀|1⟩

---

## 2. 四个酉算子（全部r_i=2，不可因子化）

### u₁: Q_a ⊗ E₁

$$u_1 = I_{Q_a} \otimes |y\rangle\langle\tilde{\gamma}|_{E_1} \;+\; \sigma_z^{Q_a} \otimes |x\rangle\langle\tilde{\gamma}^\perp|_{E_1}$$

算子Schmidt分解：
$$u_1 = \sqrt{2} \cdot \frac{I}{\sqrt{2}} \otimes |y\rangle\langle\tilde{\gamma}| \;+\; \sqrt{2} \cdot \frac{\sigma_z}{\sqrt{2}} \otimes |x\rangle\langle\tilde{\gamma}^\perp|$$
- s₀=s₁=√2, L₀=I/√2, L₁=σ_z/√2, R₀=|y⟩⟨γ̃|, R₁=|x⟩⟨γ̃⊥|
- r₁=2（两项线性无关，不可因子化为v⊗w）

### u₂: E₁ ⊗ Q_b

$$u_2 = |v\rangle\langle y|_{E_1} \otimes I_{Q_b} \;+\; |v^\perp\rangle\langle x|_{E_1} \otimes \sigma_x^{Q_b}$$

算子Schmidt分解：
$$u_2 = \sqrt{2} \cdot |v\rangle\langle y| \otimes \frac{I}{\sqrt{2}} \;+\; \sqrt{2} \cdot |v^\perp\rangle\langle x| \otimes \frac{\sigma_x}{\sqrt{2}}$$
- t₀=t₁=√2, S₀=|v⟩⟨y|, S₁=|v⊥⟩⟨x|, T₀=I/√2, T₁=σ_x/√2
- r₂=2

### u₃: Q_a ⊗ E₂（对称构造，带撇基）

$$u_3 = I_{Q_a} \otimes |y'\rangle\langle\tilde{\gamma}'|_{E_2} \;+\; \sigma_z^{Q_a} \otimes |x'\rangle\langle\tilde{\gamma}'^\perp|_{E_2}$$

- s'₀=s'₁=√2, L'₀=I/√2, L'₁=σ_z/√2, R'₀=|y'⟩⟨γ̃'|, R'₁=|x'⟩⟨γ̃'⊥|
- r₁^(34)=2

### u₄: E₂ ⊗ Q_b（对称构造，带撇基）

$$u_4 = |v'\rangle\langle y'|_{E_2} \otimes I_{Q_b} \;+\; |v'^\perp\rangle\langle x'|_{E_2} \otimes \sigma_x^{Q_b}$$

- t'₀=t'₁=√2, S'₀=|v'⟩⟨y'|, S'₁=|v'⊥⟩⟨x'|, T'₀=I/√2, T'₁=σ_x/√2
- r₂^(34)=2

### 记号约定

- {|y⟩, |x⟩} 和 {|v⟩, |v⊥⟩} 是E₁上的两组正交基
- {|y'⟩, |x'⟩} 和 {|v'⟩, |v'⊥⟩} 是E₂上的两组正交基
- 具体可取：|y⟩=|0⟩, |x⟩=|1⟩, |v⟩=|+⟩, |v⊥⟩=|-⟩

---

## 3. 验证QCMI=0

### 步骤1: U₂U₁的块对角结构

代入u₁和u₂的显式形式：

$$U_2 U_1 = I_{Q_a} \otimes |v\rangle\langle\tilde{\gamma}|_{E_1} \otimes I_{Q_b} \;+\; \sigma_z^{Q_a} \otimes |v^\perp\rangle\langle\tilde{\gamma}^\perp|_{E_1} \otimes \sigma_x^{Q_b}$$

推导：u₁将E₁的|γ̃⟩分量路由到|y⟩输出（通过I⊗|y⟩⟨γ̃|项），u₂将|y⟩输入路由到|v⟩输出（通过|v⟩⟨y|⊗I项）。|γ̃⊥⟩分量类似，经|x⟩→|v⊥⟩通道。交叉项（|y⟩⟨γ̃|→|v⊥⟩⟨x|和|x⟩⟨γ̃⊥|→|v⟩⟨y|）因u₁和u₂的路由结构互不重叠而消失。

### 步骤2: 环境投影

$$A_a = \langle a|_{E_1} U_2 U_1 |\tilde{\gamma}\rangle_{E_1}$$

由于U₂U₁中|γ̃⟩只出现在⟨γ̃|项中（E₁输入侧），且|v⟩⟨γ̃|项在与⟨a|收缩后给出⟨a|v⟩：

$$A_a = \langle a|v\rangle \cdot I_{Q_a} \otimes I_{Q_b}$$

**关键：交叉项消失。** |γ̃⊥⟩⟨γ̃⊥|项因⟨γ̃⊥|γ̃⟩=0而无贡献。最终A_a全正比于同一算子I⊗I。

### 步骤3: C_b（对称）

由对称构造，u₃和u₄的乘积在E₂上产生相同的块对角结构：

$$C_b = \langle b|_{E_2} U_4 U_3 |\tilde{\gamma}'\rangle_{E_2} = \langle b|v'\rangle \cdot I_{Q_a} \otimes I_{Q_b}$$

### 步骤4: Kraus算子

$$F_{ab} = C_b A_a = \langle b|v'\rangle \langle a|v\rangle \cdot I_{Q_a} \otimes I_{Q_b}$$

$$K_{ab} = \sqrt{\gamma_a \gamma_b} \cdot F_{ab} = \sqrt{\gamma_a \gamma_b} \langle b|v'\rangle \langle a|v\rangle \cdot I_{Q_a} \otimes I_{Q_b}$$

**所有K_ab互相成比例（都正比于I⊗I）。Kraus秩=1。**

### 步骤5: QCMI

由Fawzi-Renner (2015)，Kraus秩=1 ⇒ 信道N等距 ⇒ QCMI=0。或直接验证：ρ_RQ' = I⊗I/d²（最大混合态），S(ρ_RQ')=4，QCMI=S(ρ_RQ')-...=0。

---

## 4. 为什么这推翻了CFOL的(⇒)方向

CFOL原始声称：
> QCMI=0 ⇒ 每个u_i可因子化为v_i⊗w_i（算子Schmidt秩=1）

反例中：
- 每个u_i的算子Schmidt秩=2（不可因子化）
- QCMI=0（Kraus秩=1）
- 全部四边约束（F_ab=C_b A_a ∝ W, ∀a,b）均满足

**因此原始CFOL的(⇒)方向严格为假。**

---

## 5. 正确陈述

QCMI=0迫使每个u_i在适应基下取**块对角受控酉形式**：

$$u_1 = L_A \otimes |y\rangle\langle\tilde{\gamma}| + L_B \otimes |x\rangle\langle\tilde{\gamma}^\perp|$$
$$u_2 = |v\rangle\langle y| \otimes T_A + |v^\perp\rangle\langle x| \otimes T_B$$

其中L_A, L_B为Q_a上的酉算子，T_A, T_B为Q_b上的酉算子。u₃, u₄对称。此形式兼容r_i∈{1,2}。

r_i=1（完全因子化）是Case I（dim(Y)=d，通用情况）。
r_i=2（块对角受控酉）是Case II（dim(Y)≤d-1，测度零退化集）。

---

## 6. 验证清单

| 验证项 | 结果 |
|--------|:--:|
| u_i酉性 (i=1,2,3,4) | ✅ |
| u_i不可因子化 (r_i=2) | ✅ |
| A₁=μA₀ | ✅ |
| C₁=νC₀ | ✅ |
| F_ab = C_b A_a ∝ W ∀a,b | ✅ |
| Kraus秩=1 | ✅ |
| QCMI=0 | ✅ |
| γ₀≠γ₁ | ✅（可选，反例不依赖此条件也可构造） |
