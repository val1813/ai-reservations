# PI审核 Phase 1 — MasslessGravity-Island v1

> PI 主上下文执行，对照 A/B 双博士 Phase 1 独立输出
> 时间：2026-06-01

## ⚠️ 关键文献归属纠正（A/B 独立确认）

**候选池/文献库中的 arXiv 编号与作者对应关系是反的：**

| arXiv | 实际作者 | 实际立场 | 原背景标注 |
|-------|---------|---------|-----------|
| **2506.04311** | Antonini, Chen, Maxfield, **Penington** | **支持岛屿**（"An apologia for islands"） | 原标注为 Geng et al.（命题B） |
| **2602.06543** | **Geng**, Karch, Perez-Pardavila, **Raju**, Randall, Riojas | **反对岛屿**（"Seeing Page Curves with Blinders On"） | 原标注为 Antonini et al.（命题A） |

**修正：命题A（岛屿可推广）= Antonini-Chen-Maxfield-Penington 2506.04311；命题B（规范障碍）= Geng-Karch-PerezPardavila-Raju-Randall-Riojas 2602.06543**

"Tajdini", "Swingle", "Sasieta" 不是这两篇论文任一作者——需从文献库删除。

---

## 一、A/B 审核入口对比

| 维度 | A博士 | B博士 |
|------|-------|-------|
| 文献检索 | 纠正归属+补全 celestial/BMS 交叉文献 | 同确认归属错误+补充 Kapec et al. 1603.07706 |
| C1 结论 | BMS supertranslation 使 ℐ⁺ area 变换 → QES 非自动 BMS-invariant | Attack 1 同结论：Kapec et al. δ_f A_ren = Q_f ≠ 0 |
| 最锐攻击 | — | Attack 1 (supertranslation frame) × Attack 4 (BMS × Type III₁ 交叉强化) |
| 倾向 | 偏命题B（C1 bypass 与 C2 bypass 互斥） | 偏命题B（文献现有结果不支持 C1） |

**A/B 独立收敛：** 双博士在文献归属纠正、C1 非自动 BMS-invariant、命题B 更受现有文献支持 三点上完全一致——未经协调的独立推导给出相同结论。

---

## 二、PI 裁决

### C1（BMS-invariant QES）— 当前判决：命题B占优

基于 Kapec-Raclariu-Strominger (1603.07706) 的严格结果：
- ℐ⁺ renormalized area 在 supertranslation 下变换：δ_f A_ren = Q_f (supertranslation charge) ≠ 0
- QES BMS-invariance 需 Q_f/4G + δ_f S_bulk = 0
- Antonini et al. 的 state-dependent dressing 是已知最可行的 bypass，但 burden of proof 在命题A方

**C1 初步结论：QES 非自动 BMS-invariant。命题A 需要显式构造 state-dependent dressing 使 Q_f + 4G·δ_f S_bulk = 0。**

### 子命题优先级

**A/B 一致：S1a（BMS-invariant QES）> S1c（3D flat gravity）> S1b（flat space replica wormhole）**

S1a 是门控项。如果 S1a 被完全否定（C1 不可满足）→ 命题B 成立 → 课题转向否定性定理方向。

### 知识库增量

**K1.1** ⚠️L1（文献纠正）— 候选池 arXiv 编号作者归属反了。命题A = Antonini-Chen-Maxfield-Penington (2506.04311)；命题B = Geng-Karch-PerezPardavila-Raju-Randall-Riojas (2602.06543)
- math_object: arXiv attribution correction

**K1.2** ⚠️L1（C1 初步结论）— BMS supertranslation 下 ℐ⁺ renormalized area 变换为 δ_f A_ren = Q_f ≠ 0 (Kapec et al. 1603.07706)。QES 非自动 BMS-invariant。
- math_object: BMS supertranslation charge, QES invariance
- 来源: Phase 1 A+B

**K1.3** ⚠️L1（C1-C2 互斥）— C1 的 bypass（state-dependent dressing）与 C2 的 bypass（replica trick factorization）可能存在深层互斥。这是命题B 的最强论证路径。
- math_object: dressing-replica incompatibility

---

## 三、下一步

Phase 1 发现命题B 占优。按 SOP 规则（不叙事退让），Phase 2 应正面攻击 S1a：
- 验证 Antonini et al. state-dependent dressing 是否能抵消 Q_f
- 如果不能 → 建立否定性定理（flat space 中 QES 非 BMS-invariant）

▶️ 下一步：生成 Phase 2 AB 任务书，主攻 S1a（Antonini et al. dressing 是否足以恢复 BMS-invariance），按 SOP 直接执行。
