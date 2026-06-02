# A 博士任务书 — LP1-补9 Phase 1

**课题：** LP1-补9 Diophantine分类严格表述
**Phase：** 1（严格写出Theorem 1: Diophantine bound on cluster size）
**价值分类：** [核心] — LP-1论文投稿前必须的数学严格化

---

## 攻击目标

将LP-1论文中目前的口语表述：
> "准周期势 badly approximable β 产生有限最大罕见区域 L_max"

升级为论文级的严格数学定理：

**Theorem 1 (Diophantine bound on cluster size):**
令 β = (β_x, β_y) ∈ ℝ² 为 badly approximable irrationals，即存在 c > 0, M > 0 使 ‖kβ_i‖ ≥ c/|k| for all k ∈ ℤ\{0}, i = x,y。
则对于 2D Aubry-André 势 V(x,y) = V₀[cos(2πβ_x·x+φ_x) + cos(2πβ_y·y+φ_y)]，
罕见低无序区域的最大尺寸满足 L_max ≤ (M+2)/ε + O(1)，
其中 ε 是"低无序"的能量窗口宽度。

---

## 推导任务

### 第1步：精确定义 2D badly approximable irrationals
- 从 Khinchin "Continued Fractions" 写出连分数部分商有界的严格判据
- M = sup_{k} {a_k}（部分商的最大值）
- β = (√5-1)/2 时 M=1（所有 a_k = 1）→ "badly approximable"的最优情形

### 第2步：证明折叠映射引理
- Lemma: 2D 可分离势 V(x,y) 中，(β_x, β_y)各自 badly approximable → 折叠映射 2β mod 1 保持 badly approximable
- 从 Cassels "Geometry of Numbers" 验证此引理的标准证明

### 第3步：证明 L_max bound
- Theorem 1: L_max ≤ (M+2)/ε（或等价的严格版本）
- 步骤：(a) 罕见区域 = {连续的L个格点满足 |V(r_i)-0| < ε} → 等价于 Diophantine 逼近问题
        (b) ‖kβ‖ ≥ c/|k| → 能量接近 0 的格点间距 ≥ f(c,k)
        (c) 积分得到区域内最多包含的连续低能格点数
        (d) 给出 L_max 的严格上界

### 第4步：黄金比例的特殊性
- Corollary: β_i = (√5-1)/2 给出最小的 M=1 → L_max 最小 → "最佳保护"

---

## 产出
论文可直接引用的 Theorem 1 + Lemma + Corollary，含：
- 精确的数学陈述
- 证明骨架（标注引用的标准结果：Cassels第X章，Khinchin定理Y）
- 与LP-1物理部分（Sec 3.6）的接口说明

文件：D:\Claude\ai-reservations\LP1-MBL2D\LP1-补9_Diophantine\current\A\Phase1_A_output.md
