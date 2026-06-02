# A 博士任务书 — Phase 3 (MasslessGravity-Island v1)

**课题：** MasslessGravity-Island v1
**Phase：** 3（否定性定理——C1-C2 互斥的严格表述）
**日期：** 2026-06-01
**价值分类：** [突破] — 若能严格证明 C1-C2 互斥，产出新否定性定理

---

## 攻击目标

将 Phase 2 B 博士的 Lemma 1/2（Dressing × Replica 互斥）严格化，写成一个可发表的否定性命题。

**核心论断：**
> 渐近平坦时空中，使 QES BMS-invariant 所需的 gravitational dressing（C1 bypass）必然使 supertranslation charge Q_f 变成代数中心元素；但 replica wormhole saddle 的存在需要 Q_f 在 replica boundary conditions 下有非平凡谱（C2 bypass）。两者不能同时成立。

---

## 推导任务

### 第1步：精确定义 C1 和 C2 的规范表述

- C1: ∃ dressing D 使 QES 位置在 BMS supertranslation 下不变 ⟺ Q_f/4G + δ_f S_bulk^D = 0
- C2: ∃ replica manifold M_n (n copies of flat space, cyclic boundary conditions at I⁺) 使 saddle-point 近似 well-defined

### 第2步：证明 Lemma 1（Dressing → Q_f 中心化）

若 dressing D 使 [O_D, Q_f] = 0 for all dressed observables O_D ∈ A_rad，则 Q_f ∈ center(A_rad)。

证明骨架：若 Q_f 与所有 dressed observables 对易，则 Q_f 是 A_rad 的中心元素。

### 第3步：证明 Lemma 2（互斥引理）

Replica trick 需要：tr(ρ_rad^n) = Z_n/Z_1^n，其中 Z_n 是 n-fold replica manifold 上的路径积分。若 Q_f ∈ center(A_rad) 且 replica boundary conditions 在 I⁺ 上涉及 supertranslation 的 matching，则 Q_f 的中心性 → Z_n 因子化 → replica wormhole saddle 消失。

### 第4步：综合——否定性定理

Theorem (C1-C2 incompatibility): 在渐近平坦时空中，不存在同时满足 C1（BMS-invariant QES）和 C2（replica wormhole saddle well-defined）的 gravitational dressing 方案。

---

## 产出格式
```
⚡ 审核入口：
  定理陈述：[一句话]
  定理等级：[⚠️L1 / ✅L2]
  最脆弱的假设
  PI需要关注的问题
```
