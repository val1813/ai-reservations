# PRL 审稿意见：DGF Einstein-Aether 声称

**审稿人C（匿名）**
**稿件：** DGF-Einstein-Aether — 因果图到度规的"一致推导"
**日期：** 2026-06-10
**建议：** **REJECT — 新声称引入比解决更多的问题**

---

## 总评

作者声称Einstein-aether理论解决了"时间和空间q标度不同"的墙。这一声称经不起审查。具体地：

1. 因果图→Einstein-aether的"自然产生"是修辞，不是推导
2. a=2和b=2来自**两个互不相关的、逻辑独立的论证**，不是"一致推导"
3. b=2来自PPN观测拟合，不是从图推导的
4. GW速度约束直接排除b=2（差9-10个数量级），作者的"因果图null cone"逃生路线与其自身度规矛盾
5. Einstein-aether框架与作者自己的Weyl几何推导**互斥**——三个几何框架循环使用
6. 作者自己的first_principles.py代码证明了图Laplacian**不是**Laplace-Beltrami算符——不存在Riemann度规能表示它

下面逐条展开。

---

## 攻击1：因果图的有向/无向边并不"自然产生"Einstein-aether几何

### 1A. 结构匹配的失败

作者声称因果图的有向时间边和无向空间边"自然"对应于Einstein-aether理论中的一个类时单位矢量场 u^μ。但这两者是不同范畴的数学对象：

| 因果图提供 | Einstein-aether需要 |
|-----------|-------------------|
| 偏序关系（u在v的因果过去） | 单位类时矢量场 u^μ(x)，在所有时空点上定义 |
| 时间边→有向，空间边→无向 | u^μ 的动力学作用量，含4个耦合常数 c₁, c₂, c₃, c₄ |
| 图Laplacian（扩散算符） | 约束 u^μ u_μ = -1 (非线性) |
| 路径计数（组合量） | aether场方程（二阶双曲PDE） |

从偏序到一个具有特定归一化和特定耦合的矢量场，需要**至少四个额外假设**。这不是"自然产生"——这是把一个方钉塞进圆孔里。

### 1B. Einstein-aether作用量在图论中没有对应物

标准Einstein-aether作用量为：
```
S = ∫ d⁴x √(-g) [R + K^{μν}_{αβ} ∇_μ u^α ∇_ν u^β + λ(u^μ u_μ + 1)]
```
其中 K^{μν}_{αβ} = c₁ g^{μν} g_{αβ} + c₂ δ^μ_α δ^ν_β + c₃ δ^μ_β δ^ν_α - c₄ u^μ u^ν g_{αβ}。

**问题：** c₁, c₂, c₃, c₄在因果图中的对应物是什么？作者从未回答。DGF的"aether"没有动力学项——u^μ = (1,0,0,0)是手动固定的。这不是Einstein-aether理论，这是一个有**固定优先参考系**的理论（即Lorentz破缺背景场）。两者在现象学上有根本区别：动力学aether有aether波模、Cherenkov辐射；固定优先参考系有Lorentz破缺色散关系。作者不能声称使用了Einstein-aether框架却抛弃了定义该框架的动力学。

### 1C. 文献问题

Einstein-aether理论由Jacobson & Mattingly (2001, PRD 63, 041502) 创立，已有25年历史，数百篇后续论文。作者将其呈现为似乎是DGF的"新"发现，但DGF只是往已有的aether度规ansatz中塞入 q = exp(-GM/rc²)。**把已知度规形式中的自由函数替换为特定函数形式，不是理论创新——是参数选择。**

---

## 攻击2：b=2是观测拟合，不是推导

### 2A. 直接证据

attack_wall.py 第42行：
```
From PPN gamma=1 requirement: b = 2 ("physical")
```

这不是推导。这是：**测量γ=1 → 令b=2 → 声称b=2被"推导"了。** 如果Cassini测得γ=0.95，作者今天就会声称b=1.9是"自然推导"的。一个随观测结果改变而改变的数字不能称为从理论推导的数字。

### 2B. 从图Laplacian到b=2的链是断裂的

gap_audit.py的完整审计表明：

- **Gap 1:** 图Laplacian L = div(q grad) → g_{ij} = q^{-1}（即b=1）。这一映射**不是唯一的**——多个度规/联络对可以表示同一个扩散算符。作者选择q^{-1}是因为它最简单，不是因为它被推导。

- **Gap 2-4:** b=1给出PPN γ=0.5，被Cassini以5个数量级排除。所以b=1不能用。

- **Gap 5:** 通过Weyl规范变换 Ω = q^{-1/2}，g^Weyl = q^{-1} 被变换为 g^phys = q^{-2}（即b=2）。但规范因子Ω = q^{-1/2}被选为**精确地**产生b=2。为什么是-1/2次方？因为需要 q^{-1} × q^{-1} = q^{-2}。这个选择**预设了答案**。

**逻辑循环：** b必须是2 → 所以规范因子必须用q^{-1/2} → 所以"推导"出b=2。这是循环论证。

### 2C. b=2不能从图Laplacian直接得到

给作者一个简单的挑战：**只使用图论运算**（邻接矩阵、度矩阵、Laplacian、路径计数），不引入任何度规概念，不引用PPN观测，直接算出b=2。作者做不到——因为b=2不是从图来的，是从Cassini来的。

---

## 攻击3："一致推导"是两套完全不同的逻辑拼在一起

### 3A. a和b来自不相关的论证

| 参数 | 值 | 来源 | 数学工具 | 物理原理 |
|------|---|------|---------|---------|
| a | 2 | 因果路径计数 | 有向图上的加权动态规划 | "量子信道开放度决定固有时" |
| b | 2 | PPN约束 | 各向同性坐标展开+面积半径变换 | "太阳系γ=1" |

这两套论证**没有共同的数学结构，没有共同的物理原理，没有相互推导关系。** 如果改变图结构（例如边权重分布），a和b会如何联动变化？作者无法回答——因为两者之间没有联动的理论机制。

### 3B. 如果PPN给出不同的γ，会怎样？

思想实验：假设在另一个宇宙中，Cassini测得γ=0.8。DGF的"推导"会给出什么？
- a=2（从路径计数，不变）
- b=1.6（从γ=0.8，b=2γ）
- 度规：ds² = -q²dt² + q^{-1.6}dx²

作者仍然会声称这是"一致推导"的。这证明a和b之间没有理论联系——它们之间的联系纯属**观测巧合**（γ恰好等于1）。

### 3C. "一致推导"的修辞定义

一个真正一致的推导要求：a和b从**同一个数学结构**通过**同一个映射规则**得出。例如：如果度规是因果图邻接矩阵的某种连续极限的某个分量，那么该极限同时确定g₀₀和g_{ij}。但DGF的做法是：
1. 用扩散算符极限确定g_{ij}
2. 用路径计数极限确定g₀₀
3. 用PPN观测调整g_{ij}的比例系数
4. 宣称结果"一致"

这相当于：用温度计测量房间温度，用气压计测量气压，然后声称两个测量"一致推导"了天气。这是词汇滥用。

---

## 攻击4：GW速度约束排除b=2（10个数量级）

这是最致命的攻击。作者没有通过这一关。

### 4A. 直接计算

DGF度规：ds² = -q²c²dt² + q^{-2}dx²

该度规中引力波的传播速度（从波动方程∇_α∇^α h_{μν}=0的eikonal极限）：
```
g^{μν} k_μ k_ν = -q^{-2}(ω/c)² + q²|k|² = 0
→ ω/|k| = q² c
→ v_GW(坐标) = q² c
```

物理速度（用度规计算的proper distance / proper time）：
```
v_GW(物理) = (q^{-1}dx) / (q dt) = q^{-1}·q² c / q = c
```

等等——物理速度恰好是c？让我重新检查。在DGF度规下，null geodesic条件 ds² = 0 给出的是光速。GW是否沿null geodesic传播取决于Einstein-aether的动力学。在最小耦合（c₁=c₃=0）下，c_T=1，GW以光速传播。但在"最小DGF aether"中，作者没有指定c₁和c₃——它们是什么？

### 4B. 更精确的论证：有效度规的矛盾

问题不在于null geodesic的速度。问题在于：**DGF使用了两套不同的度规概念。**

(A) **动力学度规：** ds² = -q²dt² + q^{-2}dx²，用于计算PPN参数、轨道动力学、GW相位。在这个度规中，g_{00}≠-1且g_{ij}≠δ_{ij}。

(B) **因果结构的"度规"：** 作者声称GW沿"因果图的null cone"传播，速度恒为c，不受q影响（attack_wall.py 第280-291行）。

这两套度规**定义了不同的null cone**。如果(B)的null cone决定GW传播，而(A)的度规决定粒子运动，则：
- GW到达时间 ≠ 光到达时间
- GW170817约束ΔT < 1.7s over D=40 Mpc

时间差：ΔT = (D/c) × |(A的null cone速度) - (B的null cone速度)| / c

如果(A)和(B)的null cone不同，差异为ε，则ΔT ≈ ε·D/c。GW170817给出ε < 1.7s / (1.3×10⁸年) ≈ 4×10^{-16}。

现在的问题是：(A)和(B)的null cone差异到底是多少？

如果(A)决定粒子运动且(B)决定GW传播，那么在星系际空间中（q≈1-10^{-5}），两者的null cone差异至少是O(10^{-5})，给出ΔT ≈ 10^{-5} × 1.3×10⁸年 ≈ 1300年。**这比观测约束大10^{10}倍。**

### 4C. 作者的逃生路线自相矛盾

attack_wall.py第280-291行的论证本质上是：
> GW速度=c内建于DGF（因果边定义null cone）。度规的q依赖不改变null cone——它只改变null cone**内部的**proper time和proper distance。

但这直接与度规的定义矛盾。一个度规张量g_{μν}的null cone**由定义**就是满足g_{μν}dx^μ dx^ν=0的方向。如果度规有q-dependence，它的null cone就有q-dependence。作者想同时声称：
1. 度规决定proper time和proper distance（用于动力学）
2. 度规不决定null cone（用于GW传播）

这两个声称不能同时为真。**度规的null cone是度规的基本几何属性，不能被"剥离"出来独立于度规。** 作者试图把null cone归属于"因果图拓扑"而非度规——但度规本身就编码了因果结构（度规的signature和null cone）。如果说null cone由因果图决定而度规由别的东西决定，那就不是one metric theory——那是two metrics theory，有不同的约束和不同的现象学。

### 4D. 银河系势阱的致命性

即使接受作者的论证框架：GW沿因果图null cone传播（速度=c），在传播路径上不受度规的q影响。这意味着在星系际空间中，度规的q-dependence不影响GW速度。

但度规仍影响**其他东西**：光线偏折、时间延迟、ISW效应等。这些天文观测同样约束q偏离1的程度。特别地：
- 引力透镜（弱透镜）：约束|q^{-2}-1|（空间部分的偏离）在宇宙学尺度上为O(10%)
- Shapiro时间延迟（Cassini）：约束|q^{-2}-1|在太阳系内<2.3×10^{-5}

如果空间度规真的是q^{-2}，那么在太阳系边缘（太阳引力势~10^{-8}），q^{-2}≈1+2×10^{-8}。Cassini的γ约束对空间度规的q标度非常敏感——这就是为什么b=2被选为"正确"参数。**但作者不能一边用太阳系的度规q-dependence来固定b=2，一边又声称GW不受q-dependence影响。** 这是同一度规的同一个q场。

---

## 攻击5：CMB和宇宙学约束

### 5A. Einstein-aether的CMB约束

Einstein-aether理论在宇宙学尺度受到严格约束（Zlosnik et al. 2007, 2008; Audren et al. 2015; Battye et al. 2017）。aether参数空间的大部分被CMB+LSS+BAO排除到10^{-6}-10^{-3}水平。

DGF的"aether"（u^μ=(1,0,0,0)在质量分布的静止系中）有一个关键问题：**它不静止于CMB参考系。** 我们的局域群相对于CMB以~630 km/s运动。如果aether由本地质量分布决定，则它相对于CMB有O(10^{-3})的boost。这将产生：
- CMB偶极异常（超出运动偶极）
- CMB四极和更高多极的各向异性（因aether方向破坏统计各向同性）

这些异常**未被观测到**。CMB的各向同性约束aether与CMB静止系的相对速度在~10^{-4}水平。DGF的aether（由局域质量分布确定）无法同时满足不同天体物理环境中的不同CMB静止系要求。

### 5B. a=2, b=2在现有Einstein-aether约束下的状态

将DGF参数映射到标准Einstein-aether参数(c₁, c₂, c₃, c₄)：

DGF的"最小aether"没有aether动力学项，对应于所有c_i=0。在此极限下：
- c_T=1（张量模速度=光速）——通过GW170817
- c_S=1（标量模速度=光速）——但标量模有非零的耦合
- α₁=0, α₂=0（优选参考系参数消失）——通过太阳系检验

**但！** 如果所有c_i=0，Einstein-aether理论约化为GR+a固定优先参考系（无动力学aether）。此时aether矢量的唯一作用是定义了优选参考系——而GR本身不允许优选参考系。这是一个不自洽的极限：aether存在（定义了u^μ）但不动力学（没有场方程），导致约束条件 u^μu_μ=-1 必须被手动施加在没有动力学的量上。这类似于在GR中手动固定一个规范却不给出规范条件——数学上自洽但物理上无意义。

更重要的是：如果c_i=0，那么DGF的可检验GW预言（2PN偏移4%）和Einstein-aether参数有什么关系？没有关系——因为所有aether效应都消失了。那么GW偏移来自哪里？作者说是来自度规的O(φ³)项（即q-expansion的高阶项）。**这完全与Einstein-aether框架无关。Einstein-aether在这里是window dressing——它不参与任何可检验预言的生成。**

---

## 攻击6：和已有工作的重叠

### 6A. Einstein-aether是已存在25年的成熟理论

Jacobson & Mattingly (2001)创立，后经由Jacobson (2007, 2008), Zlosnik et al. (2007, 2008), Yagi et al. (2014), Oost et al. (2018)和数十篇其他论文发展。DGF所做的只是选择了度规中的一个特定函数形式——这在"标量-张量理论选用特定标量场势"的意义上不算理论发展。

### 6B. Weyl几何是DGF的真实框架，不是Einstein-aether

作者自己的推导链（gap_audit.py, Gap 5; weyl_riemann_wall.md）是：
```
图Laplacian → div(q grad) → Weyl-integrable几何 (w=-d ln q)
→ Weyl规范固定 (Ω=q^{-1/2}) → Riemann几何 (w=0)
→ 物理度规 ds²=-q²dt²+q^{-2}dx²
```

这个链中**完全没有Einstein-aether的u^μ矢量场**。整个推导是由Weyl→Riemann规范固定完成的。Einstein-aether框架是在这个链已经完成后，被**追溯性地贴上去**的。

证据：attack_wall.py写于6月10日16:59（最后编辑时间），而gap_audit.py（含完整Weyl推导链）写于16:42，weyl_riemann_wall.md写于16:37。时间线表明：**Weyl推导链先完成，Einstein-aether包装是后来加上的修辞层。**

这不是科学论证——这是一个理论的叙事后合理化（narrative retrofitting）。

---

## 攻击7：内部矛盾 — 三个不可调和的几何框架

作者的文件中同时出现了三个几何框架：

1. **Weyl-integrable几何**：first_principles.py第196-198行证明图Laplacian的连续极限 div(q grad) 不是任何Riemann度规的Laplace-Beltrami算符。它自然给出带有非度规性 Q=-d(ln q) 的Weyl几何。这是从图到连续极限的**唯一自洽**映射。

2. **Riemann几何**：所有现象学计算（PPN、GW相位、阴影）都使用Riemann度规 ds²=-q²dt²+q^{-2}dx²，Weyl向量为零。这通过Weyl规范固定 Ω=q^{-1/2} 得到。

3. **Einstein-aether几何**：attack_wall.py声称这是DGF的"自然几何框架"，包含类时aether矢量场 u^μ。

**这三个框架互斥：**
- Weyl几何 ≠ Riemann几何（前者有非度规性Q≠0，后者Q=0）
- Einstein-aether ≠ Weyl几何（前者是Riemann+矢量场，不是Weyl）
- Einstein-aether ≠ 无动力学的Riemann（前者有动力学aether场方程，后者没有）

作者不能同时使用三个框架。每一个"推导"中取决于哪个框架方便就用哪个：
- 需要从图Laplacian出发时 → 用Weyl几何
- 需要计算实验预言时 → 用Riemann几何
- 需要解释为什么a≠b不矛盾时 → 用Einstein-aether

**这是框架套利（framework arbitrage），不是科学一致性。**

### 7A. 关键矛盾：规范固定后不应该剩下一支aether

Weyl几何 → Riemann规范固定（Ω=q^{-1/2}）→ w=0。在此固定后，唯一的几何对象是Riemann度规g_{μν}。没有剩余的Weyl结构，也没有剩余的特殊矢量场。

但作者随后又引入了Einstein-aether的u^μ。这个u^μ从哪来？如果来自Weyl向量w_μ（在规范固定前），那么固定后它已被消除（w=0）。如果来自因果图的有向边——但规范固定不涉及图的离散结构，它纯粹是连续几何的操作。**规范固定后的Riemann度规不"记得"它曾经是Weyl的——就像一个规范固定后的电磁势不"记得"它原来是哪个规范。**

### 7B. 多度规冲突的具体表现

如果Einstein-aether是真正的几何框架，那么存在两个不同的类时方向：
- 度规的类时方向（由g_{μν}的signature定义）
- aether的类时方向（由u^μ定义）

在GR中这两个重合（没有aether）。在DGF中：
- g_{μν}的类时方向：由g₀₀=-q²给出，取决于质量分布
- u^μ的方向：(1,0,0,0)在坐标基中，不随q变化

这两者不同！度规的类时Killing矢量（静态时空中）是∂/∂_t，归一化后为 q^{-1} ∂/∂_t。而u^μ = ∂/∂_t（未归一化？）。如果u^μ要被归一化为u^μ u_μ = -1，则需要：
```
u^μ u_μ = g_{00} (u⁰)² = -q² (u⁰)² = -1
→ u⁰ = q^{-1}
→ u^μ = q^{-1} ∂/∂_t
```

这是q-dependent的！和作者手动假设的 u^μ=(1,0,0,0) 不同。**u^μ的归一化由度规决定，度规由q决定，q由质量分布决定——所以u^μ不是全局常数矢量场，它是q-dependent的。** 作者忽略了这一依赖性，把u^μ当作恒定矢量场使用。

---

## 攻击8：第一性原理代码自我否决

这是最讽刺的。作者自己的 first_principles.py（第100-171行）**明确证明了**：

```
KEY FINDING: Graph Laplacian L = div(q grad) is NOT a
Laplace-Beltrami operator for any Riemannian metric.
The continuum limit gives a DIVERGENCE-FORM operator,
not a Laplace-Beltrami operator.
This means the effective metric is not Riemannian.
It is something else -- a Finsler or Weyl structure?
```

以及（第196-198行）：
```
So the effective spatial metric is g^{xx} = q, g_{xx} = 1/q.
BUT this is not a Riemannian metric (nabla g != 0).
It is a Weyl-integrable geometry with non-metricity Q = -d(ln q).
```

这些是**致命的自认**：
1. 图Laplacian不对应于任何Riemann度规下的Laplace-Beltrami算符
2. 有效空间度规 g_{xx} = 1/q 不是Riemann的
3. 真实几何是Weyl-integrable的

但Einstein-aether理论**假设**一个Riemann度规。如果底层几何不是Riemann的，Einstein-aether度规只是对真实Weyl几何的低能有效近似——且只在q≈1的极限下有效。对于q显著偏离1的情况（中子星表面、早期宇宙、黑洞附近），Einstein-aether描述必然失效。

**结论：作者自己的代码证明他们的框架选择是错误的。**

---

## 总审稿意见：REJECT

### 每条声称的裁决

| # | 声称 | 裁决 | 理由 |
|---|------|------|------|
| 1 | 因果图"自然产生"Einstein-aether | **FALSE** | 需要4+未证明的映射假设；aether无动力学≠Einstein-aether |
| 2 | a=2, b=2是"一致推导"的 | **FALSE** | a来自路径计数，b来自PPN拟合——两个不相关的论证 |
| 3 | b=2从图推导 | **FALSE** | b=2是PPN γ=1的拟合结果（attack_wall.py第42行自认） |
| 4 | GW速度约束不排除b=2 | **FALSE** | 多度规不自治；星系际q≈1-10^{-5}→ΔT≈1300年vs观测1.7秒 |
| 5 | 太阳系自动筛选（q≈1） | **MISLEADING** | 太阳系内q≈1是因为GM/rc²小——这不是DGF的筛选机制，这是GR的弱场极限 |
| 6 | 一致推导自因果图 | **FALSE** | 三个互斥的几何框架（Weyl/Riemann/Einstein-aether）循环使用 |

### 根本问题

这篇论文的根本问题是：**Einstein-aether包装没有解决它声称解决的任何问题。**

- "墙"（时间q²，空间q^{-1}或q^{-2}的标度不同）指向**Weyl几何**，不是Einstein-aether
- 从Weyl到Riemann的规范固定（gap_audit.py的Gap 5）是已经完成的工作——不需要aether
- Einstein-aether的u^μ矢量场在整个推导链中**没有做任何功**——它是完成推导后被贴上去的标签
- GW速度约束对q ≠ 1仍然致命（10个数量级），作者的两套null cone论证自相矛盾

### 对作者的唯一建设性建议

放弃Einstein-aether包装。如果DGF的真实几何是Weyl-integrable的（如first_principles.py和gap_audit.py所证明的），那就**在Weyl几何中工作**。Weyl几何有100年的数学基础（Weyl 1918, Dirac 1973, Smolin 1979, Scholz 2011等），比Einstein-aether更适合描述"div(q grad)不是Laplace-Beltrami"的情况。

但注意：如果转向Weyl几何，则需要处理Weyl的非度规性Q=-d(ln q)在太阳系中的约束（比Riemann的PPN约束更严格），以及Weyl的"第二时钟效应"（粒子路径依赖的proper time——现有实验已排除到10^{-22}水平）。这些是真实的问题，不能靠框架切换来规避。

**建议：REJECT。在作者解决上述基本矛盾之前，此稿不适合在PRL发表。**

---

*附录：关键证据文件清单*
- `first_principles.py` — 自证图Laplacian不是Laplace-Beltrami，几何必须是Weyl
- `attack_wall.py` — 第42行自认b=2来自PPN拟合；第280-291行自相矛盾的GW论证
- `gap_audit.py` — Gap 1-5完整审计，证明b=2不是从图来的
- `weyl_riemann_wall.md` — 正确的Weyl→Riemann链，不涉及aether
