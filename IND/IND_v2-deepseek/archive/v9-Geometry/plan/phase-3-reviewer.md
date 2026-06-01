## v9 收官 恶意审稿人报告 — Nature Physics 匿名审稿

审稿人立场：根本性怀疑。零项目上下文。仅基于 v9-K1 至 v9-K8 八条声张。

---

### 第一步：查重

**查询路径**：
- OpenAlex: "binary entropy total variation bright mode Bogoliubov universality"（命中3篇均不相关：Braun-Adesso RMP 2018 量子计量、Kilonovae、Plasma Review）。
- OpenAlex: "Crooks thermodynamic length Bures Sivak"（命中 Deffner-Bonança 2020 综述、Acconcia 学位论文等，均无 2 ln 2 普适断言）。
- OpenAlex: "Berry phase Jaynes-Cummings vacuum Rabi"（Calderón-De Zela PRA 2016「Geometric phases and the Rabi Hamiltonian」、Wang-Luo OptComm 2019「Berry phases in generalized Rabi」——这两篇是真正的近邻，下文第3条详细攻击）。
- OpenAlex: "Tavis Cummings single excitation entanglement entropy universal"（命中 Kirton-Keeling Dicke 综述 2018、Sun-Zhao 2021 disordered TC——不涉及 2 ln 2 闭式）。
- OpenAlex: "Bogoliubov bright dark mode Tavis Cummings entropy"（命中 Dambal-Bittner 2026「Thermalization Regimes in a Chaotic Tavis-Cummings Model」——chaos 区域熵热化语境，但未声张 2 ln 2 不变量）。
- Semantic Scholar 多次 429，未能补全。

**判定**：**查重通过，未发现直接竞争者**——没有论文以"N_I^{(S)} = 2 ln 2 普适于任意 N_q"形式发表。但这本身可疑——若结论真有意义，65 年的 Tavis-Cummings 文献 + 50 年的 Holevo 信道容量文献 + 30 年的 Uhlmann 信息几何文献完全没人写下来，作者需要回答"为何无人发现"而非"我发现了"。更可能的解释：**这不是新定理，而是教科书结论的重新包装**（见第5条）。

---

### 五条拒稿理由

**1. 核心假设的最简反例 [致命]**

v9-K5 声张"N_I^{(S)} ≡ 2 ln 2 普适于任意 N_q ≥ 1"建立在"Bogoliubov 变换将 g·Σᵢaᵢ 分解为单一亮模 √N_q·g·B_q + (N_q−1) 暗模"之上。**最简反例**：取 N_q = 2，但让两个原子耦合常数 g₁ ≠ g₂（位置依赖、Stark 移位、制造误差），则正确分解为 g_eff·B = (g₁σ₁⁺+g₂σ₂⁺)/√(g₁²+g₂²)，此时初态 |e,0⟩=|e₁g₂,0⟩ 与亮模并不严格平行——它在亮/暗模空间的投影系数为 g₁/√(g₁²+g₂²) ≠ 1，于是 ρ_B(u) 不再是纯二元谱，N_I^{(S)} ≠ 2 ln 2 而是被一个 g₁/g₂ 依赖因子调制。**这立刻摧毁"与 N_q,g 完全无关"声张**。作者必须证明：(a) v9 模型限定为对称耦合；(b) 一旦松弛对称性，2 ln 2 立即破缺，因此该结果不是"普适"而是"对称点上的精调结果"。**回应这个攻击作者必须证明**：在 g_i 任意分布下重做 Bogoliubov 分解、明确写出 N_I^{(S)} 对耦合非均匀性的展开，并解释为何"普适"一词在文献意义下仍然成立——否则改用"对称特例"避免误导。

**2. 推导链最薄弱一步 [致命]**

最薄弱一步是 v9-K7 的 "T > π/(4g√N_q) → forward+backward 累加保持 2 ln 2"。这里隐含了一个**未声明的逆向时间演化协议**：作者从 forward arc (0→π/4) 切到 backward arc (π/4→π/2) 时，是否物理实施了时间反演？若 H 不变只是 u 越过 π/4，则 ρ_B 自动从 (q,p)=(1/2,1/2) 继续走向 (0,1)——这是同一条 forward 轨迹的延续，**S 并非单调递减再回升而是一次性下降到 0**，total variation 自然变成 2 ln 2，但这就和 v9-K1 端点选择 [0,π/4] 矛盾：原文用 ∫₀^{π/4} 已经只覆盖半个 Rabi 周期，怎么又出现"forward+backward"？这是同一对象被两次计数。v9-K6(i) 的"forward+backward 半段累加 = 2 ln 2"和 v9-K7 的"T>π/4 累加保持 2 ln 2"实际上**指代不同协议但用同一记号**，这是定义混淆。**回应这个攻击作者必须证明**：写出 forward 与 backward 阶段的具体 Hamiltonian/驱动协议（是 H→−H？还是 detuning 翻转？还是单纯延长时间？），并区分"χ 累加"（信息论协议）和"S 路径变差"（动力学）的运算定义；二者在 N_q=2 的"巧合"必须可独立验证。

**3. 与已有文献冲突 [严重]**

v9-K3 声张 "purification |ψ(u)⟩ 的 Berry connection A_u ≡ 0，闭合环路 γ = 0"。这与 **Calderón & De Zela, "Geometric phases and the Rabi Hamiltonian", PRA 93, 033823 (2016)**（arXiv:1601.02926 系列）以及 **Wang-Luo, Opt. Commun. 451, 175 (2019)** 直接冲突——这两篇明确推导 Rabi/JC 模型在循环演化下的非平凡 Berry/Aharonov-Anandan 相位（典型 γ ∝ Ω·T 或与失谐相关的有限值）。作者所选 purification（|e,0⟩,|g,B_q⟩ 实正交基 + 因子 −i）人为吸收了所有 U(1) 规范自由度到全局相位中，所以 A_u = 0 是**规范选择产物，不是物理结论**。在不同 purification（如 |g,B_q⟩→e^{iφ(u)}|g,B_q⟩）下 A_u ≠ 0。"2 ln 2 ≠ 2π·n 故非 winding"这个排除论证因此基于规范固定的 purification，并未排除"在自然 dressed-state purification 下存在 Berry 贡献"的可能。**回应这个攻击作者必须证明**：(a) 在所有 admissible purifications 上做规范不变的 Berry 相位计算（即使用 Uhlmann holonomy 而非裸 |ψ⟩ Berry connection），(b) 直接对比 Calderón-De Zela 公式，明确解释为何他们的非零结果在 v9 setup 退化。

**4. 数值合理性 [中等]**

我做替代估算：对 JC 真空初态，单激发被全局亮模吸收一次的 Holevo 信息量 ≤ ln(dim_bright) = ln 2。一个完整 Rabi 周期 |e,0⟩→|g,1⟩→|e,0⟩ 的"信息往返"naive 估算给 2 ln 2 (出+入)。**这个数字在任何二能级-单激发系统都会出现**——它就是"二态系统跑一个回合"的熵预算上限，与 N_q 无关只是因为亮模子空间永远是 2 维（一个激发 ⊕ 真空）。换言之，2 ln 2 没有 v9-K8 所宣称的"内禀重合"特殊性，它是 **(单激发部门维数=2) × (forward+backward=2)** 的平凡乘积。Crooks-Sivak length L_B = π/4 ≈ 0.785 与 2 ln 2 ≈ 1.386 不相等也是平凡的——L_B 是黎曼弧长（单位弧度），h₂ 是熵（单位 nat），二者量纲不同，作者却把它们直接做数值比较来"裁决三选一"（v9-K4），**这是范畴错误**。π/4 与 ln 2 不应同台。**回应这个攻击作者必须证明**：(a) 两量在共同信息几何度量下的 dimensional homogeneity；(b) 2 ln 2 的"普适性"超出"二维 Hilbert × forward+backward"的平凡组合，给出 N_q-doublet 结构无法解释的剩余信息内容。

**5. 最近似的已有工作 [严重]**

逐句比较：
- **Tavis-Cummings 1968 (PR 170, 379)**：原始论文已写出 N_q-原子集体亮模分解 + Rabi 频率 g√N_q + 单激发部门为 2 维。v9-K5 的 Bogoliubov 普适性定理**是 1968 年的结果，不是新定理**。作者声称"亮/暗模解耦"为 v9 推导基石——这是教科书内容（Garraway, Phil. Trans. R. Soc. A 369, 1137 (2011) 综述第3节就是这个）。
- **Holevo 1973 (Probl. Inf. Transm. 9, 177)**：信道容量 χ_max = ln(dim) 上限；v9-K6(i) 的"亮模 dim=2 ⟹ χ_max = ln 2"是 Holevo bound 的直接代入，零原创。
- **Crooks 2007 (PRL 99, 100602)** 与 **Sivak-Crooks 2012 (PRL 108, 190602)**：thermodynamic length = ∫√{Fisher information} dt。v9-K2 的"L_B = π/4 ≠ 2 ln 2 故排除 Crooks-Sivak 解读"——这是排除一个本来就不该被提的对应（Crooks-Sivak 度量耗散功而非熵变差，作者把"长度"和"熵"放在同一裁决表是**虚假二分**）。
- **2024-2026 量子信息几何**：Campaioli et al. RMP 2024 "Quantum batteries"（命中我们查重列表）综述了 Bures/Fubini-Study geometry 在 JC-like 系统的应用，已系统讨论 |e,0⟩→|g,1⟩ purification 的几何不变量；Dambal-Bittner 2026 chaotic TC 给出熵热化曲线但不主张 2 ln 2 闭式。**v9 与这些工作的差异在哪？只是端点选 π/4 和 [0, π/4] 积分。这不是新物理，是新公式包装。**

**回应这个攻击作者必须证明**：(a) 列出 v9 八条结论中**哪一条不能从 Tavis-Cummings 1968 + Holevo 1973 + 二元熵恒等式三者直接推导**；(b) 给出现有文献中"亮/暗模 + 端点积分 = 2 ln 2"组合从未被显式陈述的具体证据（不仅是"我没找到"），例如询问 Garraway 综述作者或在 Phys. Rev. A 1990-2025 系统检索；(c) 若结论确属已知，立即降级 manuscript 为 pedagogical note 而非 Nature Physics 主稿。

---

### 最终建议

**拒稿（Reject without resubmission）**。

理由一句话：v9-K1 至 v9-K8 八条结论中，K1/K5/K6 是 Tavis-Cummings 1968 + Holevo 1973 + 二元熵恒等式的代数代入，K2/K3/K4 建立在范畴错误（量纲不同的量做数值裁决）和规范选择产物上，K7/K8 涉及未声明的协议混淆——整体上是**一组教科书结论被重命名为"普适定理"**，不构成 Nature Physics 所要求的物理新发现。
