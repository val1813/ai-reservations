# A 博士任务书 — Phase 1

**课题：** Hawking-Encoding v1
**Phase：** 1（首轮正面构造）
**日期：** 2026-06-01
**价值分类：** [核心] — 直接推进北极星命题的证明

---

## 攻击目标

**证明或构造**：在 SYK/JT + bath 标准设置下，判据 M.B（非平凡性）被满足——即 island reconstruction 给出的 unitary 演化 *不能* 被 boundary algebra 已有的 unitary 精确模拟。

---

## 背景（从苏格拉底继承）

判据 M = (M.A ∧ M.B ∧ M.C)：
- M.A（相容性）：基本被 [A3] 满足，争议小
- **M.B（非平凡性）**：island reconstruction 是否给出 boundary algebra 的 *真正扩张*？这是核心战场
- M.C（微观可验证）：是技术任务，Phase 2+ 处理

[A7] (Antonini-Chen-Maxfield-Penington 2025) 主张：在没有 background isometry 时存在 gauge-invariant compactly supported operators → 这些算符 *不在* boundary algebra 中 → island 提供了新东西。

**你的任务**：把 [A7] 的主张在 SYK/JT 中 *显式实现*，并量化"新东西"的大小。

---

## 具体推导任务

### 步骤 1：建立 M.B 的可操作判据

在 Type II_∞ von Neumann algebra 框架（[A6] CPW 2022）中：
- 设 A_bdy = boundary algebra（boundary 时间 + 单迹算符）
- 设 A_island = A_bdy ∨ {island 内 gauge-invariant compactly supported operators}

**M.B 可操作版本**：A_island ⊋ A_bdy（严格包含），即存在算符 O ∈ A_island 使得 O ∉ A_bdy。

**候选判据**（选一个实施）：
- (a) **Modular flow 判据**：A_island 的 Tomita-Takesaki modular flow σ_t^{island} 与 A_bdy 的 σ_t^{bdy} 不同 → 存在态 ω 使得 S(ω|A_island) ≠ S(ω|A_bdy)
- (b) **相对熵判据**：对某 reference state ω₀ 和 excited state ω₁，S(ω₁||ω₀|A_island) < S(ω₁||ω₀|A_bdy)（island 提供更多信息 → 相对熵下降）
- (c) **算符 norm 判据**：存在 Heisenberg-picture 算符 O(t) 使得 ||O(t) - P_{A_bdy}[O(t)]|| > ε(N) 对所有 N > N₀ 成立（P 是到 A_bdy 的投影）

**建议选 (b)**：相对熵判据最直接连接到"信息量"概念，且 CPW 框架已给出 Rényi 熵的 saddle 计算。

### 步骤 2：在 SYK + JT 双侧 + bath 中计算

模型设置（Almheiri-Engelhardt-Marolf-Maxfield 标准）：
- 双侧 eternal AdS₂ 黑洞（JT gravity）
- 左侧 boundary 耦合到 non-gravitating bath
- Page time 后 island 出现在右侧 interior

计算：
1. 构造 A_bdy：boundary 时间 + SYK 单迹算符 O_i(t) = (1/N) Σ ψ_a₁...ψ_aₖ
2. 构造 A_island：A_bdy ∨ {island 内 bulk field φ(x) 的 gauge-invariant dressing}
3. 选 reference state ω₀ = thermofield double state (TFD)
4. 选 excited state ω₁ = TFD + 一个 infallen qubit（Alice 扔入黑洞的信息）
5. 计算 S(ω₁||ω₀|A_bdy) 和 S(ω₁||ω₀|A_island)
6. 若 S(ω₁||ω₀|A_island) < S(ω₁||ω₀|A_bdy) → M.B 满足

### 步骤 3：量化"非平凡度"

定义 Δ_M.B ≡ S(ω₁||ω₀|A_bdy) - S(ω₁||ω₀|A_island)

- 若 Δ_M.B = O(1)（N-independent）→ 强非平凡
- 若 Δ_M.B = O(1/N)（perturbative）→ 弱非平凡
- 若 Δ_M.B = 0 → M.B 不满足 → 命题 B 赢

**预期**：基于 [A3] 复制虫洞计算，Δ_M.B 应为 O(1)（因为 island 贡献是 leading saddle 切换，不是 1/N 修正）。但这需要显式验证。

---

## 必须回答的问题

1. [A7] 的 "gauge-invariant compactly supported operators" 在 SYK/JT 中的 *显式* 形式是什么？（不能只引用 [A7] 的存在性论证——需要写出来）
2. 这些算符是否真的不在 A_bdy 中？还是可以被 boundary 数据 *精确* 重构（如 [B1] 所主张）？
3. 若 [B1] 的 "boundary algebra completeness" 成立，是否意味着 A_island = A_bdy（即 M.B 自动不满足）？如果是，[A7] 和 [B1] 的矛盾在哪里？

---

## 禁止

- 不要假设 M.B 成立然后推导后果——你的任务是 *证明* M.B 成立或发现它不成立
- 不要用 "in principle" 论证——需要 SYK/JT 中的 *显式* 计算
- 不要混淆 Euclidean 和 Lorentzian——所有 unitary 演化必须在 Lorentzian 签名下定义
- 不要引用 [A7] 的结论作为已知——[A7] 是 2025 年论文，其主张本身需要在 SYK/JT 中验证

---

## 产出格式

```
⚡ 审核入口（PI 只读这里）：
  M.B 判据选择：[a/b/c]
  M.B 在 SYK/JT 中是否满足：[是/否/有边界]
  Δ_M.B 量级：[O(1) / O(1/N) / 0]
  关键技术步骤：[一句话]
  最脆弱假设：[一句话]
  
详细推导：[下方]
```

---

## 文献必读

- [A6] Chandrasekaran-Penington-Witten, arXiv:2209.10454 — Type II_∞ algebra 构造
- [A7] Antonini-Chen-Maxfield-Penington, arXiv:2506.04311 — gauge-invariant compactly supported operators
- [B1] Geng-Karch-Raju et al., arXiv:2602.06543 — boundary algebra completeness 论证
- [A3] Penington-Shenker-Stanford-Yang, arXiv:1911.11977 — 复制虫洞 + island saddle
- Witten, "Gravity and the crossed product", JHEP 10 (2022) 008, arXiv:2112.12828 — Type II₁ algebra in gravity
