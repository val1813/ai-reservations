# B 博士任务书 — Phase 2 (MasslessGravity-Island v1)

**课题：** MasslessGravity-Island v1
**Phase：** 2（S1a 反面攻击 — Antonini dressing 的原理性障碍）
**日期：** 2026-06-01
**价值分类：** [防守/核心]

---

## 攻击目标

从跨域角度攻击 Antonini et al. (2506.04311) state-dependent dressing 方案，找出它不能恢复 BMS-invariance 的原理性原因——或者找出它与 C2（replica wormhole）互斥的证据。

---

## 三条攻击链

### 攻击 1：Dressing 与 Replica Structure 的互斥

**跨域工具：** QED Kulish-Faddeev dressing × replica trick

QED 中，软光子 dressing 使 charged particle 的 reduced density matrix 变为 gauge-invariant。但 dressing 也改变了 replica partition function 中的 saddle 结构——因为 dressing 引入了额外的 boundary correlations。

**攻击目标：** 若 Antonini et al. 的 graviton dressing 改变了 ℐ⁺ 上的 boundary correlations，replica manifold 上的 saddle 结构会改变 → C1 bypass 可能与 C2 bypass 互斥（Phase 1 A/B 的共同发现）。

### 攻击 2：Supertranslation Charge 的非零性

**跨域工具：** Ashtekar-Streubel symplectic structure on ℐ⁺

BMS supertranslation charge Q_f 是与 soft graviton theorem 直接关联的物理量（Strominger 2014）。Q_f ≠ 0 不是"规范 artifact 可以被 dressing 消去"——它是 soft graviton 对 entanglement 的物理贡献。

**攻击目标：** 如果 dressing 成功使 Q_f + 4G·δ_f S_bulk = 0，问：dressing 是消去了 Q_f，还是把 Q_f 的贡献转移到了 dressed S_bulk 中？如果是转移，那 C1 名义上满足但物理上等价于"把规范非不变性重命名为 entanglement 贡献"。

### 攻击 3：3D vs 4D 的策略价值重评估

3D gravity 无 propagating graviton → dressing 可能 trivial。但 4D 中有 propagating graviton → BMS charge 有 infinite tower (supertranslation + superrotation + ...)。

**攻击目标：** 即使 Antonini et al. 的方案在 3D 中 work，它在 4D 中面临 propagating graviton 带来的额外障碍——graviton Fock space 使 dressing 的 Hilbert space 结构远更复杂。

---

## 禁止
- 不要重复 Phase 1 的四条攻击
- 不要只做文献评论——每条攻击需要具体数学障碍
- Phase 2 不应该只是"找更多理由反对"，而应该是"找到最可能 kill Antonini dressing 的那一个数学原因"

## 产出格式

```
⚡ 审核入口：
  最致命攻击：[编号 + 原因]
  C1 bypass 是否可独立于 C2 存在：[是/否]
  命题A 存活概率：[%]
  PI 需要裁决的问题
```
