# A博士 Phase 3 作业：Subfactor index 是否能绕过 GKRR completeness

**课题：** Hawking-Encoding v1  
**Phase：** 3  
**作者：** A博士  
**日期：** 2026-06-01  
**唯一写入文件：** `current/A/phase3_subfactor_A.md`

---

## ⚡ 审核入口（PI 只读）

| 项目 | 判定 |
|---|---|
| **[𝒜_full : 𝒜_bdy] 估计** | **不确定**；在额外假设 `𝒜_full = B(ℋ_phys)` 且 `𝒜_bdy ⊂ B(ℋ_phys)` 为 proper expected inclusion 失败时，Kosaki-Longo minimal index 倾向 **= ∞**；但该额外假设本身未在 SYK/JT canonical 设置中严格建立。 |
| **最关键论证步骤** | Type III₁ 的 `𝒜_bdy` 与候选 `B(ℋ)` full algebra 属于不同类型，若把二者强行作为同一 Hilbert 空间上的 inclusion，则缺少 normal faithful conditional expectation，minimal index 可为 ∞；但这证明的是所选 algebra package 的 type mismatch，不自动证明 island 算符给出物理真扩张。 |
| **K1.10 升级判定** | **维持 ⚠️L1，不可升级 ✅L2**。Subfactor 路径给出有力条件性论证，但未独立关掉 CP-009/CP-010。 |
| **是否绕过 GKRR completeness** | **部分**。它绕过了 GKRR 的 vacuum projector/P₀ 论证链，但没有绕过对 `𝒜_full`、physical Hilbert space、gauge-invariant island algebra inclusion 的定义依赖。 |

**一句话结论：** Phase 3 A 未能严格证明 `[𝒜_full:𝒜_bdy] > 1`；最强可辩护结论是：若 `𝒜_full` 被定义为同一物理表示上的全有界算符代数，则 canonical Type III₁ boundary algebra 与之不可能 index = 1，且很可能给出 infinite index；但该定义选择本身正是待证物理输入，不能直接把 K1.10 升级到 ✅L2。

---

## §0 声张强度声明

本作业目标不是重证 GKRR completeness，而是检查是否存在一个独立的 subfactor no-go：

> 通过 SYK/JT 中 `𝒜_bdy ⊂ 𝒜_full` 的 Jones/Kosaki-Longo index，证明 `𝒜_bdy` 是 `𝒜_full` 的真子因子，从而得到不依赖 GKRR completeness 的 M.B no-go。

声张强度选择：

- □ 无条件证明 `[𝒜_full:𝒜_bdy] > 1`
- □ 无条件证明 `[𝒜_full:𝒜_bdy] = 1`
- ☑ **条件性判定：若 `𝒜_full = B(ℋ_phys)`，index 非 1，倾向 ∞；但 SYK/JT 中 `𝒜_full` 的正确定义未被严格钉住**

---

## §0.5 隐含假设清单

| # | 假设 | 用途 | 当前状态 |
|---|---|---|---|
| H1 | canonical large-N SYK/JT 的 boundary single-trace von Neumann algebra 是 Type III₁ factor | 定义 `𝒜_bdy` | 强文献支持；沿用 K1.5/K2.1/K2.2 |
| H2 | 加 modular/Schwarzian crossed product 后可得到 Type II∞ algebra | 区分 canonical 与 microcanonical/CPW package | ✅L2 级别结构事实，但依赖 ensemble/weight 选择 |
| H3 | `𝒜_full` 是同一 Hilbert 空间上的 factor，且包含所有 gauge-invariant island/bulk operators | 才能谈 subfactor inclusion | **未严格建立** |
| H4 | `𝒜_full = B(ℋ_phys)` | 用 Type I full algebra 计算 index | **关键额外假设**，不能免费采用 |
| H5 | 存在 normal faithful conditional expectation `E:𝒜_full→𝒜_bdy` 或可证明不存在 | 用 minimal index 定义 | 未建立；若不存在，则 index = ∞ |
| H6 | Donnelly-Wall edge modes 在 JT/SYK 中有具体中心/边缘算符实现 | 用 commutant 证明 proper inclusion | 候选，不是定理 |

---

## §1 精确定义尝试

### 1.1 `𝒜_bdy`

在 canonical large-N SYK/JT 标准 TFD 设置中，最自然的 boundary algebra 是

`𝒜_bdy^can := { single-trace boundary insertions O_i(t), Schwarzian/boundary Hamiltonian H 的可测函数 }''`

其中双撇号表示 von Neumann closure。按 Leutheusser-Liu/CPW 线索，strict large-N canonical 表示中它是 Type III₁ factor。若选择一个 semifinite weight 并与 modular flow 做 crossed product，则得到

`𝒜_bdy^II := 𝒜_bdy^can ⋊_{σ} ℝ`

这是 Type II∞ package。这个转换不是纯代数恒等替换，而是引入 ensemble/weight/clock 的新表述；Phase 2 已裁定它具有 setup dependence。

### 1.2 `𝒜_full`

任务书给出两个可能读法：

1. **强读法：** `𝒜_full = B(ℋ_phys)`，即同一物理 Hilbert 空间上所有 bounded operators。
2. **引力读法：** `𝒜_full` 是所有 diffeomorphism-invariant、gauge-invariant bulk/island observables 生成的 von Neumann algebra。

这两个定义不能无缝等同。若采用强读法，subfactor 问题数学上清楚，但物理上可能把不可观测或不满足引力约束的 bounded operators 也放进 `𝒜_full`。若采用引力读法，物理上更合理，但 `𝒜_full` 的 type、表示、是否等于 `B(ℋ_phys)` 都未给出。

### 1.3 inclusion 映射

可写的 inclusion 是

`ι: 𝒜_bdy → 𝒜_full`

其中 `ι(O_bdy)` 是同一物理 Hilbert 空间上边界算符的作用。问题在于：canonical `𝒜_bdy^can` 是 Type III₁，而 `B(ℋ_phys)` 是 Type I；这是 type-changing inclusion。若改用 CPW crossed product，则 inclusion 变成 Type II∞ 到未知 `𝒜_full`，不再是任务书中最直接的 Type III₁ 问题。

---

## §2 Jones/Kosaki-Longo index 是否 defined

标准 Jones index最初为 Type II₁ subfactor 定义。对 Type III 因子，需要使用 Kosaki-Longo minimal index，即对 normal faithful conditional expectation

`E: M → N`

取 minimal index `Ind(E)`，并定义 `[M:N]` 为所有可用 expectation 的下确界；若不存在合适 expectation，则 index 记为 `∞` 或 inclusion 不具备 finite-index structure。

因此对

`N = 𝒜_bdy^can`，`M = 𝒜_full`

问题是 well-posed 的前提不是“Jones 1983 原始 Type II₁ 公式直接套用”，而是：

1. `N⊂M` 是同一标准形式/同一 Hilbert 表示上的 factor inclusion；
2. `N` 与 `M` 的 modular structure 兼容到足以存在 normal faithful conditional expectation；
3. 若不存在 expectation，finite index 不成立，minimal index 为 ∞。

这给出第一个关键结论：

> Type III₁ 并不阻止谈 index，但阻止直接用 finite-dimensional QEC 或 Type II₁ 直觉；必须先证明 expectation 或证明其不存在。

---

## §3 三条候选路线逐一撞墙

### 3.1 路线 A：`𝒜_bdy^can` Type III₁，`𝒜_full=B(ℋ)` Type I

若接受 `𝒜_full=B(ℋ_phys)`，则 `[B(ℋ):𝒜_bdy^can] = 1` 不可能成立。原因很简单：index 1 的 subfactor inclusion 等价于 `N=M`；但 Type III₁ factor 不同构为 Type I factor `B(ℋ)`。

更强地，finite-index inclusion 通常保留非常强的结构约束。若 `N⊂M` finite index，则二者的类型在可控意义下相容；一个 canonical Type III₁ boundary factor 作为 `B(ℋ)` 的 finite-index proper subfactor 不是自然结构。若 normal faithful conditional expectation `B(ℋ)→𝒜_bdy^can` 不存在，则 minimal index 为 ∞。

**可得结论：**

`𝒜_full=B(ℋ)` 假设下，index 不为 1，强烈倾向 `∞`。

**撞墙点：**

这没有证明 SYK/JT 物理上的 `𝒜_full` 真是 `B(ℋ_phys)`。在引力理论中，全 bounded operator algebra 包含大量未必是 gauge-invariant observable 的对象。把它们统统纳入 `𝒜_full` 会把 M.B 变成“边界代数是否等于所有数学上 bounded operators”，而非“island gauge-invariant operators 是否超出 boundary”。

### 3.2 路线 B：commutant/edge mode

若能构造非平凡算符

`E ∈ (𝒜_bdy)'`，`E ∉ ℂ·1`

则 `𝒜_bdy` 在 `B(ℋ)` 中不可能 irreducible，因此 `𝒜_bdy ≠ B(ℋ)`，可推出 proper inclusion。

Donnelly-Wall edge modes 在 gauge theory 中确实提示：区域代数的边界上会出现 center/edge Hilbert space，导致 naive tensor factorization 失败。对 gravity/JT，可能的对应物包括：

- horizon/entangling surface 的 area 或 dilaton edge datum；
- gravitational dressing 的软模式；
- baby-universe/topology sector 的中心变量；
- island QES 上的 generalized entropy conjugate variable。

**撞墙点：**

这些对象在 JT/SYK canonical algebra 中没有被本作业严格构造成 `𝒜_bdy` 的 commutant 元素。尤其是 dilaton/Schwarzian 边界模式常常已经在 boundary algebra 或其 crossed product 中；把它当成独立 edge mode 会双计数。baby-universe sector 则更像纯引力 path integral 的扩展 Hilbert space，不一定存在于 UV 完备 SYK Hilbert space。

**判定：**

edge-mode 路线是 CP-010 的候选，但不是本 Phase 可关闭的证明。

### 3.3 路线 C：large-N generalized free field irreducibility

large-N single-trace algebra 可近似为 generalized free field (GFF) algebra。若 GFF 的 creation/annihilation operators 在 Fock space 上 irreducibly 作用，则其 von Neumann closure 可能是 `B(ℱ)`，从而 index = 1，而不是 >1。

这一路线反而给 subfactor no-go 带来危险：在普通 free field 的全局 Fock 表示中，全体 creation/annihilation 算符生成的 von Neumann algebra可以是 irreducible 的。若 SYK large-N single-trace algebra在相应 code/Fock space 上也 irreducible，则 commutant 平凡，无法由 GFF 本身推出 proper inclusion。

**撞墙点：**

local algebra、time-band algebra、single-trace algebra、全 fermion algebra 不是同一个对象。SYK finite-N 的全 fermion algebra当然生成全矩阵代数；large-N single-trace canonical algebra则是 Type III₁。把 finite-N irreducibility 直接带到 large-N Type III₁ 表示，会重犯 Phase 2 的 ensemble/limit 顺序问题。

**判定：**

GFF 路线不能证明 `[𝒜_full:𝒜_bdy] > 1`；它同时打开了 `[=1]` 的反向可能。因此不能用于升级 K1.10。

---

## §4 与 QEC subfactor 的连接

Holographic QEC 的 finite-dimensional 说法是：同一 logical operator 可以有多个 physical reconstruction。这个事实本身不等于 algebraic gap。

在 von Neumann algebra 语言中，需要区分三层：

1. **code-subspace logical algebra**：`𝒜_code`，只在低能/半经典 code subspace 上定义；
2. **boundary reconstructable algebra**：`𝒜_bdy|_{code}`，边界在 code subspace 上可实现的 logical algebra；
3. **full physical algebra**：`𝒜_full`，若存在，包含全部 gauge-invariant island/bulk observables。

QEC 可以说明 `𝒜_code` 有多重边界表示，也可以说明某个 erasure channel 的 correctable algebra 与互补 algebra 存在 commutant 关系。但这不直接给出

`[𝒜_full:𝒜_bdy] > 1`

因为 finite-dimensional code 的 index 与 infinite-dimensional Type III/Kosaki-Longo index 不是同一个对象。CP-011 的修正方向应是：用 finite QEC 做动机，不用它替代 index 计算。

---

## §5 必须回答的问题

### Q1. `𝒜_bdy` 和 `𝒜_full` 的精确定义是什么？inclusion 是 type-changing 还是 type-preserving？

**答：** canonical 设置中

`𝒜_bdy = {single-trace boundary operators + H 的可测函数}''`

是 Type III₁ factor。若 `𝒜_full=B(ℋ_phys)`，则 inclusion 是 Type III₁ ⊂ Type I 的 type-changing inclusion。若改用 CPW crossed product，则 `𝒜_bdy` 可变成 Type II∞，但 `𝒜_full` 的 type 仍未确定。当前最合理判定是：canonical subfactor 路径是 type-changing；type-preserving 版本需要另选 algebra package，不能自动继承 canonical 结论。

### Q2. Type III₁ subfactor 的 Jones index 是否 defined？

**答：** defined，但不是原始 Type II₁ Jones index；应使用 Kosaki-Longo minimal index/conditional expectation formulation。若不存在 normal faithful conditional expectation，则 finite index 不存在，minimal index 记为 ∞。所以“Type III₁ 不能谈 index”是错误的；“Type III₁ 可以像 finite QEC 一样直接算 index”也错误。

### Q3. SYK single-trace algebra 在 Fock space 上是否 irreducible？

**答：** 未能在本作业中证明。finite-N SYK 全 fermion algebra irreducible，但 large-N single-trace canonical algebra 是不同极限对象。GFF/Fock 直觉有可能给出 irreducibility，也有可能因 time-band/local algebra 选择而给出 Type III₁ local factor。该问题是 CP-010 的实质卡点之一，不能被当作已知输入。

### Q4. Donnelly-Wall edge modes 在 SYK/JT 中是否有具体对应物？

**答：** 有候选但无严格落地。QES/dilaton edge datum、Schwarzian soft mode、baby-universe center 都像 edge mode；但在 SYK/JT 中它们分别面临“已在 boundary algebra 中”“依赖 crossed product package”“只属于纯引力扩展 Hilbert space”的问题。当前不能用 edge mode 证明 `𝒜_bdy` 的 commutant 非平凡。

### Q5. 如果 `[𝒜_full:𝒜_bdy]=1`，是否意味着 GKRR completeness 在 canonical Type III₁ 中意外成立？

**答：** 不必然。`index=1` 只说明在所选 inclusion package 中 `𝒜_full=𝒜_bdy`。若该 package 把 `𝒜_full` 定义得过窄，例如只定义为 boundary-reconstructable gauge-invariant algebra，那么 index=1 是定义导致的，不等于 GKRR 的 canonical P₀ 论证成立。反过来，若 `𝒜_full=B(ℋ_phys)` 且 index=1，则确实会推出 `𝒜_bdy=B(ℋ_phys)`，这与 Type III₁ canonical 判定张力极大，说明定义/表示/limit 顺序至少有一个出错。

---

## §6 明确判定

### 6.1 index estimate

本作业给出的最强可辩护 estimate 是：

`[𝒜_full:𝒜_bdy] =`

- `∞`，**如果** `𝒜_full=B(ℋ_phys)` 且不存在 normal faithful conditional expectation `B(ℋ_phys)→𝒜_bdy^can`；
- `>1`，**如果** 能构造非平凡 island/edge/baby-universe 算符位于 `𝒜_full` 但不在 `𝒜_bdy`；
- `=1`，**如果** `𝒜_full` 被定义为 boundary-reconstructable gauge-invariant algebra 的 von Neumann closure；
- **不确定**，在不预设 `𝒜_full` 的精确定义时。

因此最终选择：**不确定，条件性倾向 ∞，但不足以关 CP-010。**

### 6.2 M.B no-go 状态

Subfactor 路径没有在本作业中给出独立于 GKRR completeness 的 L2 no-go。原因不是 index 理论本身弱，而是物理输入未闭合：

1. `𝒜_full` 是否等于 `B(ℋ_phys)` 未证；
2. island gauge-invariant algebra 是否严格超出 boundary algebra 未证；
3. edge mode/commutant 元素未在 SYK/JT 中构造；
4. GFF irreducibility 反而可能支持 index=1；
5. CPW Type II∞ crossed product 会改变 algebra package，不能直接回答 canonical Type III₁ 问题。

### 6.3 K1.10 升级/不可升级理由

**不可升级 ✅L2，维持 ⚠️L1。**

理由：

- K1.10 要求的是 SYK/JT 中 M.B no-go 的稳定结论；
- Phase 3 A 只能证明“在 `𝒜_full=B(ℋ)` 这个额外强定义下，index 不为 1，倾向 ∞”；
- 但这个额外强定义没有独立物理证明，且可能把非 gauge-invariant bounded operators 混入 full algebra；
- 因此 subfactor index 尚未真正绕过 GKRR completeness 的 ensemble 依赖；
- 这最多把 CP-010 从“完全开放”推进到“关键定义已定位：`𝒜_full` package 决定答案”。

---

## §末 漏洞/卡点与下一步

### 漏洞 1：`𝒜_full=B(ℋ)` 是最大未证输入

这是整个 subfactor 路径的决定点。若 PI 允许把 full algebra 定义为所有 bounded operators，则 no-go 几乎由类型差异推出；若 PI 要求 full algebra 只含 gauge-invariant physical observables，则还必须构造 island observable 不在 boundary closure 中。

### 漏洞 2：conditional expectation 未被显式证明不存在

我没有给出完整 Takesaki modular invariance 检查。因此 `∞` 仍是条件性结论，不写成 L2。

### 漏洞 3：edge mode 不是 SYK/JT 中的已构造算符

Donnelly-Wall 是强类比，不是当前模型中的 explicit operator construction。

### 漏洞 4：finite-N 与 large-N 极限顺序可能反转结论

finite-N SYK 全代数是矩阵代数，index 直觉可能给 `=1`；large-N canonical algebra 是 Type III₁，index 直觉可能给 `∞`。二者差异来自 limit/closure/ensemble，不是小技术点。

### 建议登记的新知识

**K3.A1** ⚠️L1（subfactor 定义卡点）— canonical SYK/JT 中 `[𝒜_full:𝒜_bdy]` 的值主要由 `𝒜_full` 的定义决定。若 `𝒜_full=B(ℋ_phys)`，Type III₁ boundary algebra 不可能 index=1，且 minimal index 倾向 ∞；但 `𝒜_full=B(ℋ_phys)` 未被物理证明。

**K3.A2** ⚠️L1（QEC 修正）— finite-dimensional QEC 的多重 reconstruction 不足以推出 infinite-dimensional Jones/Kosaki-Longo index >1；必须先给出 von Neumann factor inclusion 与 conditional expectation。

**K3.A3** ⚠️L1（edge mode 候选）— Donnelly-Wall edge mode 可作为证明 commutant 非平凡的候选路线，但 SYK/JT 中尚无明确 operator 对应物。

### 对 CP 的建议

- **CP-010：保持开放。** 已定位核心为 `𝒜_full` 定义与 conditional expectation。
- **CP-011：部分推进。** 已明确 finite QEC 类比不能替代 infinite subfactor index。
- **CP-009：保持开放。** Subfactor 路径尚未独立关闭 canonical Type III₁ 中的 M.B no-go。

---

**A博士签字：** Phase 3 A 独立推导完成。  
**PI 审阅意见栏：**

```text
□ 批准
□ 有条件批准
□ 退回重做
```
