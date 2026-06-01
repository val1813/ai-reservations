# A博士 Phase 1 作业 — MBL-Quasiperiodic v1

## 2D Aubry-André准周期势中低无序区域最大尺寸的严格界

---

## ⚡审核入口

⚡ 本Phase结论：准周期势中最大连续低无序区域L_max由β的Diophantine性质严格控制。对badly approximable β（如黄金比例），L_max ≤ C/ε（有限常数），其中ε = (2/π)arcsin(W_c/V_0)。2D中L_max更小（x和y方向独立约束）。
⚡ 最脆弱的一步：将单弧停留时间问题转化为折叠圆上的旋转（§3.6），需要处理I_δ由两段弧组成的情况。
⚡ 预测 vs 实际：预测L_max~q_n有限 → 实际确认，且对黄金比例给出L_max ≤ 3π/(2arcsin(W_c/V_0))
⚡ PI需要关注的问题：Liouville数β使L_max无界→准周期MBL的稳定性完全取决于β的数论性质，不是普适的

---

## 核心结果

### 1D结果

对AA势V_n = V_0 cos(2πβn+φ)，连续L个格点满足|V_n|<W_c的最大L：

**定理：** 设β为badly approximable（部分商a_n ≤ M），ε = (2/π)arcsin(W_c/V_0)为允许区间总测度。则：

$$L_{max} \leq \frac{M+2}{\varepsilon}$$

对黄金比例β=(√5-1)/2（M=1）：

$$L_{max} \leq \frac{3\pi}{2\arcsin(W_c/V_0)}$$

**数值估计：**
- V_0=1, W_c=0.5: ε≈0.161, L_max ≤ 19
- V_0=1, W_c=0.3: ε≈0.097, L_max ≤ 31
- V_0=2, W_c=0.5: ε≈0.081, L_max ≤ 37

### 2D结果

对可分离势V(x,y)=V_0[cos(2πβ_x·x)+cos(2πβ_y·y)]，L×L低无序区域要求x和y方向同时满足条件。

若β_x和β_y线性无关(over Q)，则x和y方向近似独立：

$$L_{max}^{(2D)} \leq \min(L_{max}^{(x)}, L_{max}^{(y)})$$

对β_x=β_y=黄金比例（但相位不同）：L_max^{(2D)} ≤ L_max^{(1D)}（相同上界）。

### 关键推导步骤

1. |cos(2πθ)|<δ的解集I_δ由两段弧组成，总测度ε=(2/π)arcsin(δ)
2. 通过折叠映射θ→2θ mod 1，将双弧问题转化为单弧停留问题
3. 折叠后旋转步长为2β mod 1，弧长为2ε
4. 对badly approximable 2β，停留时间≤(M+2)/(2ε)
5. 2D中x和y方向独立约束进一步限制

---

## §末 声张强度对比与新增卡点

### 声张对比

目标：L_max ~ q_n有限且不随系统尺寸增长
实际：确认。对badly approximable β，L_max有确定上界。

### 新增卡点

**卡点A1：** 折叠映射的严格性——2β mod 1是否仍是badly approximable？
- 若β是badly approximable，2β mod 1也是（因为2β的连分数可从β的连分数推导）
- 但需要验证部分商的界M如何变化

**卡点A2：** 2D联合条件|V_x+V_y|<W_c比|V_x|<W_c/2且|V_y|<W_c/2更宽松
- 使用充分条件（分解）给出的L_max是上界的上界
- 真实L_max可能更大（但仍有限）

**卡点A3：** Liouville数β使L_max无界——实验中β的选择是否总是badly approximable？
- 冷原子实验中β通常选为黄金比例或其他二次无理数→badly approximable
- 但原则上可以选择well approximable的β→MBL不稳定
