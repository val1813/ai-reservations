# B 博士任务书 — Phase 5

**课题：** Hawking-Encoding v1
**Phase：** 5（physical commutant / edge-global mode 显式构造）
**日期：** 2026-06-01
**价值分类：** [核心] — 决定 commutant/split 路线是否能关闭 CP-010

---

## 攻击目标

寻找 SYK/JT 中真正的物理算符 `X`，使得

`[X,O]=0` for all `O in A_bdy`

且

`X in A_full \ C*1`。

若成功，`A_bdy` 不可能等于 `A_full`，commutant 路线可独立支持 M.B 非平凡。

若失败，特别是所有候选 edge/global mode 都可归入 boundary charges 或 Tomita mirror，则 commutant 路线不能关闭 CP-010，反而支持宽边界 no-go。

---

## 背景

Phase 4 已判定：

- Tomita mirror algebra 不能自动物理化；
- split property failure 只是 non-factorization 压力；
- 需要显式 physical observable 或 index bridge。

B 线本阶段必须不再停留在 "可能有 edge mode"。要逐一筛掉候选。

---

## 具体推导任务

### 步骤 1：固定 physical Hilbert space

区分：

1. two-sided TFD Hilbert space；
2. one-sided black hole + bath/radiation Hilbert space；
3. gravitationally constrained physical Hilbert space；
4. code subspace。

在每个空间中写出 `A_bdy` 与 `A_full` 的候选定义。

### 步骤 2：候选 `X` 清单

逐一检查：

- ADM/boundary Hamiltonian；
- JT dilaton boundary charge；
- Schwarzian zero mode；
- island QES area operator；
- gravitational Wilson line / dressing endpoint；
- Donnelly-Wall 型 edge mode；
- Tomita mirror operator；
- opposite-side TFD operator；
- microcanonical energy-window projector。

每个候选必须回答：

1. 是否与所有 `A_bdy` 对易？
2. 是否在 `A_full`？
3. 是否非平凡？
4. 是否只是 boundary charge / gauge constraint / state-dependent mirror？

### 步骤 3：JT/SYK 具体判定

在 JT 中，纯引力自由度主要是 boundary Schwarzian/dilaton mode。若候选 global mode 可由 boundary Hamiltonian或 Schwarzian 数据读出，则它不是 `A_bdy` 的物理 commutant。

在 SYK 中，large N single-trace algebra 的 commutant 若只来自另一侧 TFD 或 modular conjugation，则不能证明单侧 radiation/bath 物理代数缺失。

### 步骤 4：split failure 的 bridge

若没有显式 `X`，检查 split failure 是否仍能通过以下桥梁推出 proper inclusion：

- failure of Type I intermediate factor；
- failure of Haag duality；
- nontrivial center / superselection sector；
- inability to define finite-index expectation。

若桥梁也不闭合，则 commutant 路线降级为结构压力。

### 步骤 5：输出判定

必须给出：

- 是否构造出 physical `X`；
- 最接近成功的候选是什么；
- 它为什么失败或成立；
- 对 CP-010 的影响；
- 对 K1.10 的影响。

---

## 禁止

- 不要把另一侧 TFD operator 直接当作单侧物理 commutant。
- 不要把 gauge constraint 的冗余自由度当作新 observable。
- 不要把 QES area operator 当作 commutant，除非证明它与 `A_bdy` 全部对易且不在 `A_bdy`。
- 不要用 "edge mode 通常存在" 代替 JT/SYK 显式检查。

---

## 产出格式

```
⚡ 审核入口（PI 只读）：
  physical commutant X：[构造成功 / 未构造出 / 表示依赖]
  最接近成功候选：[一句话]
  失败/成功原因：[一句话]
  split bridge：[闭合 / 未闭合 / 不适用]
  CP-010 影响：[关闭 / 压缩 / 不变]
  K1.10 升级判定：[可升级 ✅L2 / 维持 ⚠️L1 / 降级]

然后 §1/§2/§N/§末 完整作业。
```

## 关键文献

- Donnelly-Wall edge modes
- Witten, gravity and crossed product
- Penington-Witten 2306.03999
- Leutheusser-Liu Type III_1 / Type II crossed product
- Doplicher-Longo split inclusions
- Almheiri-Dong-Harlow holographic QEC
