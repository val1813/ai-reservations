# Phase 1 任务书 — v10-Scrambler

> 类型：A 型核心（解析构造）
> 主攻：北极星正面——Dicke 对称基下显式幺正 U: H_S⊗H_B^{⊗N_q} → ℂ⁴⊗H_dark
> 目标：在 toy 共振+真空+对称耦合 N=2 双模 JC 上构造 U，验证 H_TC|_{bright} 同构 2-qubit Bell scrambler、H_TC|_{dark} ≡ 0

---

## 〇、Phase 价值分类

**[突破]**——产出新结论：N_I^{(S)} = 2ln2 的代数身份（端点差不变量 / Bell 嵌入）。
理由：v10-K0 已闭合 ε 极限的分析层；P1 进入 dim=4 嵌入定理的代数构造层，是北极星的核心命题。

---

## §0 推导目标（一句话，可证伪）

**目标**：在 N=2 全对称 Tavis-Cummings 共振+真空浴+激发 |1⟩_S 初态下，构造显式幺正等价
$$U:\ \mathcal H_S \otimes \mathcal H_B^{\otimes 2}\ \xrightarrow{\sim}\ \mathbb C^4 \otimes \mathcal H_{\rm dark}$$
满足
- (E1) U H_TC U^† = H_{Bell scrambler} ⊗ I_dark + I_4 ⊗ 0
- (E2) [H_TC, P_dark] = 0（dark sector frozen 算符身份）
- (E3) 在 |1⟩_S |0,0⟩_B 初态下，dynamics 完全限制于 4 维 Bell 子空间

**可证伪声张**：
- **R0（强）**：U 存在且唯一（差一个 dark 子空间内幺正），ℂ⁴ 子空间 = span{|0,0⟩, |0,1⟩, |1,0⟩, |1,1⟩}（in 亮模 occupation 表示），H_TC|_{bright} 矩阵元 = 标准 2-qubit Bell scrambler Hamiltonian g_{eff}·(σ_x⊗σ_x + σ_y⊗σ_y)/2
- **R1（弱）**：U 存在但 dim=4 子空间需要额外 finite-T 或非真空浴态修正（即 frozen dark sector 仅在真空浴下严格冻结）
- **R2（否定）**：H_TC 在亮模子空间内含非平凡 dark 耦合项 → Bell scrambler 嵌入失败 → 必须修正北极星

---

## §1 强制撞墙（A 必须先回答）

1. **Dicke 对称基构造**：用 Schwinger-Holstein-Primakoff 把 N=2 双模玻色 (b_1, b_2) 映射到 SU(2) 角动量算符。亮模 b_+ = (b_1+b_2)/√2，暗模 b_− = (b_1−b_2)/√2。亮模耦合到原子，暗模 commutator [H_TC, b_−^† b_−] = 0（暗模算符守恒）。
2. **真空浴+总激发数守恒**：N̂ = σ_+σ_- + b_+^† b_+ + b_-^† b_- 守恒。在 |e⟩_S |0,0⟩_B 初态下 N̂=1，但暗模 b_− 占据数 = 0 严格冻结。dynamics 仅在 N=1 亮模子空间 span{|e,0,0⟩, |g,1,0⟩}（用亮/暗表示）。
3. **dim=4 vs dim=2 张力**：N=1 子空间 dim=2 而非 4。dim=4 来自更广 sector 还是某种张量积重表示？是否需考虑 N=0,1,2 多子空间合并？或 dim=4 应理解为 system-effective Hilbert space d_S·d_{bright} = 2·2 = 4？
4. **Bell scrambler Hamiltonian 形式**：标准 2-qubit Bell scrambler = SWAP 或 iSWAP 类，H = J(σ_x⊗σ_x + σ_y⊗σ_y)/2。需把 H_TC|_{N=1 亮} 写成 ℂ²⊗ℂ² 张量积形式，验证矩阵元同构。

撞墙后 A 必须显式判断：R0 / R1 / R2 哪个被支持？dim=4 的精确 sector 是什么？

---

## §2 假设

- A1（v9-K5）：N_q-mode 全对称 TC 在共振+真空+对称耦合下，亮/暗模 Bogoliubov 分解严格存在
- A2（v10-K0）：ε-Bogoliubov 极限严格 = 2ln2，正则化方案无关——本 Phase 直接用 ε=0 极限值
- A3（XK17 Yoshida-Kitaev）：minimal scrambler 4-qubit 设计的标准形式
- A4（XK18 Tavis-Cummings + Schwinger-Holstein-Primakoff）：玻色↔SU(2) 映射的标准引理
- A5（标准）：U 唯一性差一个 dark 子空间内幺正变换

---

## §3 禁区

不重复建立 v9-K1~K8 / v10-K0 / v8-K1~K10。

**必须**新建立 ≥ 1 项：
1. **U 显式矩阵元**（toy 解析或符号计算）
2. **dim=4 sector 精确刻画**（基矢列表 + 维数对应）
3. **H_TC|_{bright} 与 H_{Bell scrambler} 矩阵元逐项对应**（不是表面类比，是同构）

---

## §4 工作流（强制）

§S 文献检索（≤ 3 条 WebSearch）：
- "Dicke symmetric basis Holstein-Primakoff Tavis-Cummings two-mode"
- "Bell scrambler Hamiltonian 2-qubit iSWAP"
- "minimal scrambler 4-qubit Yoshida Kitaev arXiv:1710.03363"

§0.5 假设清单
§1 撞墙（4 攻击全处理）
§D 推导：
- D.1 双模玻色 → SU(2) 表示（Schwinger 映射 + 亮/暗模分解）
- D.2 总激发数 N̂ 守恒律 + 暗模 b_− 占据数算符守恒
- D.3 dim=4 sector 精确识别（候选：d_S·d_bright = 2·2 = 4）
- D.4 H_TC|_{N≤2 亮} 矩阵元显式写出
- D.5 与 Bell scrambler Hamiltonian g_{eff}(σ_x⊗σ_x + σ_y⊗σ_y)/2 同构验证（或证伪）
- D.6 frozen dark sector 算符身份 [H_TC, P_dark] = 0 验证
§K 卡点
§C 结论

---

## §5 输出路径

A：`current/A/phase-1-output.md`，标题 `## A作业 v10 Phase 1 — Dicke 对称基显式 U + Bell scrambler 嵌入`
B：`current/B/phase-1-output.md`（独立推导，零项目上下文，禁止读 A 与 plan/synthesis）

---

## §6 AHA 引理候选（PI 给 A 的方向提示——非强制）

来自 v10-P0 AHA 4 条 🔥 的精确化驱动矛盾：

**引理候选 L1（来自 AHA #1）**：N_I^{(S)} 仅由对称性保护的亮模 dim 决定 vs 仅由 Hilbert 维度决定。本 Phase 通过 dim=4 sector 显式构造可正面回答此命题。

**引理候选 L2（来自 AHA #2）**：N_I^{(S)} = TV(S^ε) 过程依赖账本，对应 Bell 子空间内单峰 S(u)；推论：若 Bell 嵌入正确，多模 JC 应给加性公式 N_I = 2·∑|S(u_i^max)−S(u_i^min)|。本 Phase **不要求验证多模**（留 v10-P2 副线），仅需在 N=2 上写出加性公式的 N_q=2 特例形式。

**引理候选 L3（来自 AHA #3）**：2ln2 = ln(d_max/d_min) 端点差不变量；Bell 嵌入若成立，d_max=4, d_min=1 自动给 ln 4 = 2ln2。本 Phase 在写出 dim=4 sector 后，应验证此身份（一句话即可）。

**引理候选 L4（来自 AHA #4）**：Bell scrambler 嵌入与 Hayden-Preskill 最小信息镜像同构。本 Phase **不要求 HP 端验证**（留 v10-P2 双轨），仅需在结论中标注"待 HP 端 dim=2 子空间识别"作为 P2 钩子。

⚠️ AHA 引理是方向提示，不是任务目标；A 主攻仍是 §0 的 (E1)+(E2)+(E3) 三项。

---

## §7 BLINDSPOT 钩子

P1 与 BLINDSPOT 同步触发（扫描 v10-K0 推导链 + AHA #2/#3/#4 的潜在盲区）。BLINDSPOT 报告若发现严重盲区，由 PI 在 P1 收尾前判断是否回炉。

---

▶️ 任务书完。
