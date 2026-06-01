## A作业 v9 Phase 1 — Bures-Uhlmann度规 vs sin(2u)·ln cot u 比对 + 三选一裁决

---

### §S 文献检索（≤4 条 WebSearch）

- XK10 Sivak-Crooks 2012 "Thermodynamic metrics and optimal paths" arXiv:1201.4166 — friction tensor → Riemann 度规；线性响应下 ds² = g_{ij} dλ^i dλ^j。
- XK9 Crooks 2007 "Measuring thermodynamic length" arXiv:0706.0559 — 在微观系统上 thermodynamic length 必须用 Fisher information 定义，ds = √F dλ。
- XK14 Uhlmann 1976 + Slater "Mixed State Holonomies" — diag(p_i) 沿单参数路径，**若特征向量与 u 无关，则 Uhlmann holonomy 平凡**（对角度规退化为经典 Fisher）。
- Wiki Bures metric — 对易/对角态：ds²_B = ¼ Σ (dp_i)²/p_i（经典极限）。

结论：四参考均支持"对角态 ⇒ Bures = ¼·Fisher × du²"以及"u-独立特征向量 ⇒ Uhlmann holonomy 平凡"。

---

### §0.5 隐含假设清单（来源 + 条件 + 满足性）

| 引用 | 来源 | 条件 | 是否满足 |
|---|---|---|---|
| ρ(u) = q\|0,0⟩⟨0,0\| + p\|B⟩⟨B\|, q=cos²u, p=sin²u | v8-K9（A1） | N=2 双模 JC 共振+真空+对称耦合，u=Ωt, Ω=g√2 | 假设满足（任务书指定） |
| Bures 距离 d_B = √(2−2√F)，对角态退化 | XK14, Wiki Bures | ρ,σ 在同一固定基下对角 | 满足：本子空间内特征向量 \|0,0⟩,\|B⟩ 与 u 无关 |
| ds²_B = ¼·[(dq)²/q+(dp)²/p] | A3（任务书） | 同上 | 满足 |
| F_classical(u) = Σ (∂_u p_i)²/p_i | A4（任务书） | 同上 | 满足 |
| Berry connection 用 \|ψ(u)⟩=√q\|e,0,0⟩−i√p\|g,B⟩ | A5（任务书） | 选定一个纯态展开（purification） | 满足；i 因子取规范 |
| Holevo χ ≤ ln d, d=2 | A6 | 二维有效子空间 | 满足 |
| c(β) v8-K10 | 不直接进入本 phase | — | 暂不调用 |

**禁区**：v8-K1~K10/v5-K6/v3-K10/v4-K3/v6-K1/v7-K1 仅作为既定结果调用，不重新推导。

---

### §1 强制撞墙（4 攻击全处理）

**攻击 1：被积式形状 + indefinite integral 闭式**

f(u) = sin(2u)·ln cot u, u∈(0, π/4)：u→0⁺ 时 ln cot u→+∞ 但 sin(2u)→0；u→π/4 时 ln cot u→0，sin(2u)→1，f(π/4)=0。f>0 全程。

构造 indefinite integral：注意 q=cos²u, p=sin²u ⇒
- dq/du = −sin(2u), dp/du = +sin(2u)
- d(−q ln q − p ln p)/du = −(ln q+1)·dq/du − (ln p+1)·dp/du
  = sin(2u)·[(ln q+1) − (ln p+1)] = sin(2u)·ln(q/p) = sin(2u)·ln(cos²u/sin²u)
  = **2·sin(2u)·ln cot u**

故 **∫ sin(2u)·ln cot u du = ½·S_q(u) + C = −½(cos²u·ln cos²u + sin²u·ln sin²u) + C**。✓ 闭式存在。

**攻击 2：Bures 度规先验估算（对角态）**

ρ(u) 在固定基 {\|0,0⟩,\|B⟩} 内对角，特征向量与 u 无关 ⇒ Bures 度规退化为经典 Fisher / 4：
- ds²_B = ¼·[(dq)²/q + (dp)²/p] = ¼·(dp/du)²·du²·[1/p+1/q]
- (dp/du)² = sin²(2u);  1/p+1/q = 1/sin²u + 1/cos²u = 1/(sin²u cos²u) = 4/sin²(2u)
- ds²_B = ¼·sin²(2u)·(4/sin²(2u))·du² = **du²**

⇒ **ds_B/du ≡ 1**（常数线元）。

**攻击 3：Fisher 度规对比**

F(u) = (dp/du)²/p + (dq/du)²/q = sin²(2u)·[1/p+1/q] = sin²(2u)·4/sin²(2u) = **4**

⇒ Fisher 沿轨迹是常数 4；Bures 线元是常数 1。两者形状均**与 sin(2u)·ln cot u 形状不匹配**（被积式在 u→0 端 log-发散却被 sin(2u) 压回零，且峰值在 u≈0.4 附近）。**形状证明：sin(2u)·ln cot u 不是 Bures/Fisher 的线元密度。**

**攻击 4：二元熵导数识别**

由攻击 1 已直接验证：

> **dS_q/du = 2·sin(2u)·ln cot u  ⇔  4·sin(2u)·ln cot u = 2·dS_q/du**

且
- 4·∫₀^{π/4} sin(2u)·ln cot u du = 2·[S_q(π/4)−S_q(0)] = 2·[ln 2 − 0] = **2 ln 2** ✓
- 在 (0, π/2) 全段：q: 1→1/2→0，S_q: 0→ln 2→0；total variation TV = ∫₀^{π/2}|dS_q/du|du = (ln 2−0)+(ln 2−0) = **2 ln 2** ✓

---

### §D 推导

**§D.1 indefinite integral**：见攻击 1，∫ sin(2u)·ln cot u du = ½·S_q(u) + C。

**§D.2 Bures-Uhlmann 度规**：见攻击 2，ds²_B = du²。在 (0, π/2) 上 Bures 长度 = π/2 ≈ 1.5708。

**§D.3 Fisher 度规**：F(u) = 4，∫₀^{π/2} √F du = 2·(π/2) = π；half-trajectory 上 √F·u = π/2。

**§D.4 Berry connection**

|ψ(u)⟩ = √q·|e,0,0⟩ − i√p·|g,B⟩，∂_u√q = −sin u，∂_u√p = +cos u。

⟨ψ|∂_u|ψ⟩ = √q·(−sin u) + (i√p)·(−i cos u) = −cos u sin u + sin u cos u = **0**

⇒ A_u = i·⟨ψ|∂_u|ψ⟩ = 0，**Berry phase ≡ 0** 沿任何 u 路径。

对应 Uhlmann holonomy：ρ(u) 的特征向量与 u 无关 ⇒ Uhlmann parallel transport 在每个特征子空间内退化为 U(1)，但由于 d|n(u)⟩/du = 0，Uhlmann connection ≡ 0 ⇒ holonomy = 𝟙（trivial）。**与 2π·n 的 winding 无关**。

**§D.5 二元熵 total variation 识别 ✓**

由攻击 4：
- 4·sin(2u)·ln cot u = 2·dS_q/du  ✓
- 4·∫₀^{π/4} sin(2u)·ln cot u du = 2·ΔS_q = **2 ln 2**  ✓
- (0, π/2) 全段 TV = 2 ln 2  ✓

**身份识别成立**：北极星 N_I^{(S)} = 2 ln 2 = **2 × ΔS_q（二元熵 monotonic 区间增量）= 二元熵在 (0, π/2) 上的 total variation**。

**§D.6 三选一裁决**

| 候选 | 判定 | 依据 |
|---|---|---|
| (a) R1: Crooks-Sivak thermodynamic length | **排除** | ds_B = du（常数），sin(2u)·ln cot u 非 Bures/Fisher 线元；2 ln 2 ≠ π/2 ≠ π |
| (b) R2: Berry-Uhlmann winding | **排除** | A_u = 0（Berry）+ 特征向量 u-独立 ⇒ Uhlmann holonomy 平凡；2 ln 2 ≠ 2π·n |
| (c) R3: Holevo / 二元熵 dimension counting | **支持** | 4·f(u) = 2·dS_q/du，总积分 = 2·ΔS_q = 2 ln 2；与 χ ≤ ln d=ln 2（d=2）量级一致 |
| (d) R4: 数值巧合 | 不需要 | R3 已正面命中 |

**裁决结论**：v8-K9 几何身份的本质是 **二元熵 total variation**，不是几何长度也不是拓扑 winding。Holevo bound 给出量级解释（forward+backward 各 ln 2，合计 2 ln 2），但要确立精确等式需在 Phase 2 引入 ensemble 与 averaged-state 的 Holevo χ 显式构造。

---

### §K 卡点（新增）

**K-A.v9.1**：Holevo 候选 R3 的"严格相等"需补：构造 ρ(u) 对应的纯态系综 {(p_i, |ψ_i⟩)} 使 χ(ensemble) 在 monotonic 半段恰好等于 ΔS_q = ln 2，且 forward+backward = 2 ln 2。当前仅证明 R3 量纲与量级正确（χ ≤ ln 2 = ΔS_q），未证 saturation。

**K-A.v9.2**：dS_q/du 的"total variation 与 (0, π/2) 区间端点"耦合：北极星出现 |2 ln 2| 是因为 q 在 (0, π/2) 上恰好 1→1/2→0（symmetric V-shape）。若 Ωt 终点不是 π/2 而是其他值，N_I^{(S)} 会偏离 2 ln 2 ⇒ **几何身份强烈依赖共振+对称耦合的特殊端点**，这与 v8-K10 c(β) 的非对称 deformation 相关。

**K-A.v9.3**（保留）：Bures 度规 ds_B = du 暗示存在另一个守恒量 = π/2（在 (0, π/2) 半段）—— 这与 N_I^{(S)} = 2 ln 2 是**两个独立**的几何不变量。需要 Phase 2 区分二者。

---

### §C 结论

1. **被积式 sin(2u)·ln cot u 是二元熵 S_q(u) = −q ln q − p ln p 关于 u 的导数 / 2**：精确身份 dS_q/du = 2·sin(2u)·ln cot u。
2. **N_I^{(S)} = 2 ln 2 = 二元熵在 (0, π/2) 上的 total variation = 2·ΔS_q**（forward + backward 半段各贡献 ln 2）。
3. **R1 (Bures length) 排除**：Bures 度规退化为 ds = du（常数），与 sin(2u)·ln cot u 形状不符。
4. **R2 (Berry/Uhlmann winding) 排除**：Berry connection A_u = 0；Uhlmann holonomy 因特征向量 u-独立而平凡。
5. **R3 (Holevo / 二元熵 dimension counting) 支持**：身份成立、量级匹配 χ ≤ ln d=ln 2；saturation 需 Phase 2 显式构造 ensemble。
6. **R4 (数值巧合) 不需要**。

至少排除一个候选的硬性要求：**R1 与 R2 双双正面排除**，R3 正面支持。可证伪声张全部正面回答。

---

### §末 对未来 B 的预判攻击点

1. **B-attack-1（端点依赖性）**：B 应攻击"为何北极星恰好对应 (0, π/2) 而不是任意 (0, T)"。我的回答预演：在 v8-K9 共振+对称耦合下，u=π/2 是 |B⟩ 完全占据→完全退激发的半周期端点，q(π/2)=0；任何其他 T 给出的 TV 不是 2 ln 2。这说明几何身份是**特殊端点的二元熵跳变**，而非沿轨迹的几何不变量。B 若试图证明"几何长度"将失败。

2. **B-attack-2（Holevo saturation 显式构造）**：B 应攻击"R3 仅量级正确，未证严格相等"。我的预演反驳：构造系综 {(½, |g,B⟩), (½, |e,0,0⟩)}，平均态 ρ̄ = ½·(|g,B⟩⟨g,B|+|e,0,0⟩⟨e,0,0|) 在 u=π/4 处，χ = S(ρ̄) − ⟨S(ψ_i)⟩ = ln 2 − 0 = ln 2。若 ρ(u) 沿轨迹可视作 u-参数化的 Holevo-saturating ensemble 的混合极限，则 forward+backward 累计正好 2 ln 2。B 若主张 R3 不成立需推翻该构造。
