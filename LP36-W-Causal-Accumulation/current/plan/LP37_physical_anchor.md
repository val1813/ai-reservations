# LP37 物理锚点：b₁为何出现在两处

**核心问题**: 为什么Kitaev的toric code和DGF的因果环都用d^{b₁}来度量信息保护？是巧合还是有更深机制？

---

## 一、两处b₁的精确对照

### Toric Code (Kitaev 2003)

- **系统**: 2D格点上的Z₂格点规范理论。量子比特在边上，稳定子在各面和顶点。
- **拓扑**: 空间流形Σ的Betti数b₁(Σ)。环面b₁=2，球面b₁=0。
- **基态简并度**: GSD = d^{b₁}（d=2对应Z₂）。4个基态扇区对应两个不可缩环上的Wilson loop取值的组合。
- **保护机制**: 局域算符不能改变同调类。基态之间的隧穿需要非局域环算符，其长度~系统尺寸L。能隙保护随L指数增长。
- **数学结构**: 基态空间 ≅ H₁(Σ, Z₂)（一维同调群）。基态是平坦联络的等价类。

### 因果环 (LP36+LP37)

- **系统**: 因果Hasse图上的量子过程。系统Q和环境E节点由光锥边连接。
- **拓扑**: 因果图G的Betti数b₁(G)。4节点环b₁=1，树b₁=0。
- **QCMI下界**: N_sq ≥ η·b₁(G)。每个独立环贡献至少η的非马尔可夫回流。
- **保护机制**: 环上的酉演化形成闭合因果回路。回路上的信息不能完全被Q'屏蔽——惰性扩展F最多屏蔽树上的相关，环的闭合路径强制残留。
- **数学结构**: 环因子化阻碍 ⇔ H₁(G) ≠ 0。QCMI=0当且仅当环退化（所有u_i可因子化）。

---

## 二、同一数学，不同物理

| 维度 | Toric Code | 因果环 |
|------|-----------|--------|
| 流形 | 空间格点Σ | 因果Hasse图G |
| b₁的含义 | 空间不可缩环数 | 因果不可约化环数 |
| 保护对象 | 基态简并度 | 量子非马尔可夫性 |
| 保护机制 | 局域算符不能改变同调类 | 惰性扩展F不能屏蔽环相关 |
| 扰动 | 局域磁场的任意子对产生 | 酉参数的可因子化变形 |
| 数学核心 | H₁(Σ) ≅ 基态空间 | H₁(G) ≠ 0 ⇒ N_sq > 0 |
| 容量公式 | log GSD = b₁·log d | N_sq ≥ b₁·η(d) |

两者的共同数学结构：

$$\dim(\text{protected space}) = d^{b_1}$$

- Toric code: protected space = 基态空间，dim = 2^{b₁}（对Z₂）
- 因果环: protected space = 不可消除的回流通道，容量 ≥ b₁·η

**这不是巧合**。两个场景中，b₁都计数了"局域操作不可达"的拓扑扇区数。在toric code中，不可达是因为同调障碍。在因果环中，不可达是因为环因子化阻碍。

---

## 三、推广猜想：拓扑保护的信息容量普适公式

> **猜想（信息容量的同调约束）**:
> 设物理系统的相互作用由因果图G描述。设W为G的拓扑保护信息容量（即局域操作不能消除的信息量）。则对任意有界容量的因果系统：
> $$\log \dim(W) \geq b_1(G) \cdot \log d$$
> 其中d是局域希尔伯特空间维数。
>
> toric code和DGF因果环是此公式在两个极限下的特例：
> - **空间极限**（toric code）: G是静态空间格点，b₁是空间拓扑
> - **时空极限**（DGF）: G是动态因果图，b₁是因果拓扑
> - **一般情况**: G可以是混合时空因果结构，b₁同时包含空间和因果环

**可检验预言**: 在空间拓扑和因果拓扑共存（如Kitaev模型嵌入动态因果结构）的系统中，信息容量应同时依赖空间b₁和因果b₁。

---

## 四、与已知物理的连接点

### 4.1 拓扑量子场论 (TQFT)

Witten (1989): 3D Chern-Simons理论的Hilbert空间维数由共形块(conformal blocks)给出，其维数由Riemann面Σ的Betti数决定：
$$\dim \mathcal{H}_\Sigma = \sum_{i} (S_{0i})^{2-2g}$$
其中g是Σ的亏格(genus)，b₁ = 2g。此公式与Verlinde公式直接相关。

DGF的因果图可以视为一种"时序TQFT"——在时空因果结构上定义的拓扑不变量，其"基态空间"是非马尔可夫回流的可能模式空间。

### 4.2 全息对偶 (AdS/CFT)

Ryu-Takayanagi公式: 边界区域的纠缠熵 = 体积极小面的面积/4G_N。体几何由边界纠缠结构决定。

因果环的QCMI可以视为"时间方向上的纠缠熵"——R和E'之间的QCMI度量了R的信息有多少"落入"环境。环拓扑决定了这个量的最小非零值。

连接点: 如果全息对偶成立，体时空的b₁应该约束边界态的QCMI。这提供了一个从引力侧检验因果环猜想的路径。

### 4.3 量子纠错码

Calderbank-Shor-Steane (CSS)码: 逻辑量子比特数 = b₁(Tanner图)。同调量子码（如toric code）是此类特例。

DGF因果环暗示: **任何量子过程本身就是一个量子码——码字是被Q'恢复的信息，错误是泄漏到E'的信息，b₁(G)是码的逻辑量子比特数的下界。**

---

## 五、对于PRL的叙事锚点

论文应以此开头:

> Kitaev's toric code taught us that topology protects quantum information: the ground state degeneracy on a manifold Σ is d^{b₁(Σ)}, and local perturbations cannot mix different homology sectors. Here we show that a different kind of topology — the topology of causal structure — protects a different kind of quantum information: quantum non-Markovianity. On a causal graph G, the minimum squashed non-Markovianity is bounded below by η·b₁(G). The same Betti number that counts non-contractible loops in space counts irremovable backflow channels in time. This is not a coincidence — both arise from the homological obstruction to factorizing a global structure into local pieces. In the toric code, the obstruction prevents factorizing the ground state into product states. In our case, it prevents factorizing the cycle unitary into product gates.
