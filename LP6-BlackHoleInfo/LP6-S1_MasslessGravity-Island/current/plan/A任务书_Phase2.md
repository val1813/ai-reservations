# A 博士任务书 — Phase 2 (MasslessGravity-Island v1)

**课题：** MasslessGravity-Island v1
**Phase：** 2（S1a 正面检验 — Antonini et al. state-dependent dressing 是否恢复 BMS-invariance）
**日期：** 2026-06-01
**价值分类：** [核心] — S1a 是门控项

---

## 攻击目标

检验 Antonini-Chen-Maxfield-Penington (arXiv:2506.04311, "An apologia for islands") 中提出的 state-dependent dressing 方案能否使 QES 在 BMS supertranslation 下不变。

**已知障碍（Phase 1）：**
- Kapec-Raclariu-Strominger (1603.07706): ℐ⁺ renormalized area 在 supertranslation 下变换 δ_f A_ren = Q_f ≠ 0
- QES BMS-invariance 需要 Q_f/4G + δ_f S_bulk = 0
- 一般态中不成立 → 需要特殊的 dressing 或 subalgebra 选择

---

## 推导任务

### 第1步：精确写出 Antonini et al. 的 dressing 方案

读取 2506.04311 中关于 subalgebra/dressing 的关键段落，精确写出：
1. 他们选择的 gravitational dressing 是什么形式？
2. 这个 dressing 作用于哪些自由度（soft graviton? boundary graviton?）？
3. dressing 如何改变 QES 的定位？

### 第2步：计算 dressed QES 的 supertranslation 变换

对于 Antonini et al. 的 dressing 方案，计算：
1. δ_f (dressed A_ren) = ? 是否仍等于 Q_f？
2. δ_f (dressed S_bulk) = ? 
3. 是否有参数窗口使 Q_f + 4G·δ_f S_bulk = 0？

### 第3步：判断

- 若能证明存在 dressing 使条件满足 → C1 可满足 → 命题A 存活
- 若证明不存在或 dressing 与 replica trick（C2）冲突 → C1 不可满足 → 命题B 占优

---

## 禁止
- 不要绕过 Kapec et al. 的严格结果——必须正面处理 Q_f ≠ 0
- 不要声称"显然" Q_f 可被抵消
- 文献引用必须基于确切 arXiv/DOI，不可凭记忆

## 产出格式

```
⚡ 审核入口：
  Dressing方案：[形式]
  δ_f (dressed QES) = [结果]
  C1 是否可满足：[是/否/不确定]
  最脆弱的步骤
  PI需要关注的问题
```
