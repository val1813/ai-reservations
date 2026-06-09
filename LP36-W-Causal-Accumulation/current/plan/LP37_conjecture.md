# LP37 核心猜想：精确形式

**日期:** 2026-06-08
**状态:** 数值证据已确认，解析证明待完成
**前置:** LP36 Theorem 7, 8 + Buscemi et al. (2025) PRX Quantum 6, 020316

---

## 一、猜想（精确陈述）

### 设定

设G = (V, E)是因果Hasse图的无向化，其团复形为1维单纯复形（Theorem 6保证无三角形）。
b₁(G) = |E| - |V| + b₀(G) 为圈秩（1维Betti数）。

每个节点v ∈ V携带一个d_v维量子系统。初始态：
- R: 参考系统，与系统Q最大纠缠
- Q: 系统节点集合，dim(Q) = Π_{v∈Q} d_v
- E: 环境节点集合，dim(E) = Π_{v∈E} d_v
- ρ_RQE = Φ⁺_RQ ⊗ γ_E，其中γ_E是任意固定环境态

酉演化U作用于Q⊗E，受G约束：U = Π_{(i,j)∈E} U_{ij}，其中每个U_{ij}是作用在节点i和j上的任意两体酉（顺序由因果偏序决定，但无向环的计数不依赖顺序）。

### 猜想（主定理候选）

> **Theorem (QCMI Topological Lower Bound, 待证):**
> 对任意满足上述约束的酉U，任意惰性扩展F：
> $$I(R; E' | Q' F) \geq \eta_0(d, \gamma_E) + \eta(d) \cdot b_1(G)$$
> 其中：
> - η₀(d, γ_E) ≥ 0 是基线QCMI，仅依赖于局部维数d和初始环境态γ_E
> - η(d) > 0 是每个独立因果环的QCMI贡献下界，仅依赖于局部维数d
> - 两者均与系统大小N = |V|无关

### 推论（两条）

**推论1（b₁=0 ⇏ 真正回流）：**
若G是树（b₁(G) = 0），则存在酉U的选择使得N_sq = 0。树状因果结构不能保证真正回流——环境记忆（时序相关性）可能完全被惰性扩展F屏蔽。

**推论2（b₁>0 ⇒ 真正回流下界）：**
若b₁(G) > 0，则对任意酉U和任意惰性扩展F：
$$N_{sq}(\sigma_{RQ'E'}) = \min_F I(R; E' | Q' F) \geq \eta_0 + \eta \cdot b_1(G) > 0$$
即存在不可消除的真正因果回流，其幅度被b₁从下方约束。

**推论3（热力学极限）：**
由LP36 Theorem 7，在3+1维Minkowski散布中Hasse图团复形的b₁随N单调增（不在Chaplin普适类中）。因此：
$$\lim_{N \to \infty} \min_U N_{sq} = \infty$$
大系统中真正非马尔可夫性不可能被消除——因果拓扑强制了一个宏观的量子信息回流。

---

## 二、证明路径（需要的关键引理）

### 引理1：QCMI的边分解（已知？）

QCMI可以沿因果Hasse图的边分解：
$$I(R; E' | Q') = \sum_{(i,j) \in E} \Delta_{ij}$$
其中Δ_{ij} ≥ 0是边(i,j)对QCMI的贡献。

**状态：需要验证。** 量子互信息一般不可加——强次加性是上界而非等式。但条件互信息在特定因果结构下可能有可加性。相关文献：Lieb-Ruskai (1973) 强次加性证明，Petz (1988) 条件互信息的变分刻画。

### 引理2：树饱和性（已知？）

若G是树，则存在酉U的选择使得G中每条边(i,j)的Δ_{ij} → 0。即树状因果图不能强制非零QCMI。

**状态：需要验证。** 数值证据支持（CHAIN和STAR5的QCMI完全一致，叶子边贡献为零）。

### 引理3：环的不可消除性（核心gap）

若G包含至少一个无向环，则沿环的边的Δ_{ij}之和有非零下界：
$$\sum_{(i,j) \in \text{cycle}} \Delta_{ij} \geq \eta(d) > 0$$

等价陈述：无向环上的酉演化强制至少η的QCMI，无论酉如何选择。

**状态：需要证明。** 直觉：环上的酉形成一个"因果反馈回路"——信息从Q流入E再流回Q——这个结构不能被任何选择消除。

### 引理4：同调独立性 ⇒ QCMI可加性（核心gap）

若两个环在团复形中是同调独立的（它们围出的1-链线性无关），则它们对QCMI的贡献是相加的。

**状态：需要证明。** 数值证据强烈支持（两独立副本QCMI = 2×单副本QCMI，机器精度）。证明路径：同调独立 ⇒ 边不相交 ⇒ 作用在不重叠的子系统上 ⇒ QCMI在张量积上可加。

---

## 三、需要搜索的具体问题

1. "topological lower bound quantum conditional mutual information" — QCMI的拓扑下界
2. "monogamy of quantum mutual information graph structure" — 图上量子互信息的单配性
3. "conditional mutual information additivity tensor product" — QCMI张量积可加性  
4. "causal graph constraint quantum channel capacity" — 因果图对量子信道容量的约束
5. "entanglement entropy area law graph topology" — 纠缠熵面积律与图拓扑（类比）

---

## 四、已知的相关定理（需要确认是否可直接引用）

| 定理 | 内容 | 与LP37的关联 |
|------|------|-------------|
| Lieb-Ruskai (1973) | SSA: I(A:C|B) ≥ 0 | QCMI非负性——Buscemi使用的核心工具 |
| Petz (1988, 2003) | QCMI=0 ⇔ 恢复映射存在 | Buscemi的Theorem 1核心引理 |
| Christandl-Winter (2004) | Squashed entanglement可加 | N_sq的张量积可加性 |
| Hayden et al. (2004) | QCMI与恢复映射的定量关系 | Theorem 2的F ≥ 2^{-ε}界 |
| Fawzi-Renner (2015) | 近似恢复映射与QCMI | 推广了Petz的恢复定理 |
| Brandão et al. (2011) | Squashed entanglement的NP-hardness | 间接相关 |

**关键未知：QCMI的图拓扑下界。** 上述定理都独立于图的拓扑结构——它们对任意量子态成立。LP37的创新点是引入因果Hasse图的同调不变量作为QCMI的约束。

---

## 五、如果文献中没有——LP37的定位

**已有**：
- Buscemi (2025): N_sq区分真正/非因果回流
- LP36 Theorem 7, 8: 因果Hasse图的同调性质
- Christandl (2004): QCMI张量积可加性

**缺失**：
- **QCMI的图拓扑下界**：b₁结构性地强制N_sq > 0
- **因果环的不可消除性定理**：环上的酉演化不能将QCMI压缩到零
- **同调独立性与QCMI可加性的联系**

LP37 = Buscemi框架 + LP36同调 + 这篇论文的3个新引理。
