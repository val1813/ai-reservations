# LP-12 Round 2 — S1: 广义对称性序参量构造

**B博士** | 2026-06-02

---

## 1. 从跳跃到数学结构

### Round 1 三跳跃回顾

| 跳跃类比 | 物理直觉 | 数学对应 |
|----------|---------|---------|
| 大森定律 (Omori law) | 余震衰减速率 = 疤痕稳定性 | 能级间距正则度 $\to$ 谱刚度 $R_\Delta$ |
| TGF-$\beta$ 超家族 | 代数破缺梯度 = 连续稳定性谱 | Lanczos系数偏离SU(2)程度 $\to$ Krylov椭圆度 $E_K$ |
| 赋格 (fugue) | 周期扩散速率 = 长久相干性 | revival保真度衰减律 $\to$ 热力学持久度 $\Pi$ |

**中心命题**：QMBS不是二元的（"是/否疤痕"），而是构成一个**稳定性谱系**——从瞬态（$L\to\infty$ 时完全热化）到存活（$L\to\infty$ 时保持完美相干）。需要一个可计算的序参量来刻画这个连续谱。

---

## 2. 文献基础

序参量构造建立于以下关键工作：

### 2.1 Krylov复杂度诊断（Hu, Zhang, Han & You 2025, PRB 111, 165106）

对于疤痕态，Lanczos系数呈现**椭圆模式**，反映隐藏的SU(2)代数：

$$b_n = h\sqrt{n(2S+1-n)}, \quad S = L/2 \quad \text{(XY模型, nematic Néel态)}$$

$$b_n = \frac{1}{2}h\sin\alpha\;\sqrt{n(2L+1-n)} \quad \text{(XXZ模型, spin helix态)}$$

Krylov复杂度在纯SU(2)疤痕中严格周期振荡：

$$C_{\mathcal{K}}(t) = 2S\sin^2(ht) = L\sin^2(ht)$$

对于近似的PXP模型疤痕，Lanczos系数服从**q-变形的SU(2)** (Bhattacharjee, Sur & Nandy 2022, PRB 106, 205150)：

$$b_n \propto \sqrt{[n]_q[2j-n+1]_q}, \quad [x]_q = \frac{q^x-q^{-x}}{q-q^{-1}}$$

热力学极限下 $q < 1$，产生非完美但持久的revival。

### 2.2 相关矩阵零空间维度（Yao & Zhang 2024, arXiv:2410.21812）

对任意本征态 $|\psi\rangle$，构造Hermitian算符基 $\{L_i\}$ 的相关矩阵：

$$M_{ij} = \frac{1}{2}\langle\psi|(L_i L_j + L_j L_i)|\psi\rangle - \langle\psi|L_i|\psi\rangle\langle\psi|L_j|\psi\rangle$$

定义 $N_0 = \dim(\operatorname{Ker}(M))$：
- 热化态：$N_0 = 1$（普适值，对有限尺寸免疫）
- 精确SGA疤痕：$N_0 \gg 1$（如广义AKLT模型中 $N_0^{\min} = 9L+3$）
- 近似疤痕：$N_0 = 1$ 但 $M$ 有大量近零本征值

### 2.3 ODLRO序参量（ETH Zurich, PRR 5, 043208, 2023）

在群不变疤痕中，非对角长程序（ODLRO）关联函数在整个疤痕子空间内取**常数值**且与距离无关：

$$\langle \mathcal{O}_i^\dagger \mathcal{O}_j \rangle = \text{const}, \quad |i-j| \to \infty$$

归一化的ODLRO关联函数之和与子晶格选择无关，提供了0到1之间的有界测度。

### 2.4 Fisher零点（Meng et al. 2025, PRL, arXiv:2501.09478）

QMBS在配分函数 $Z(\beta)$ 的复 $\beta$ 平面上表现为**连续Fisher零点线**，离开虚轴。这为疤痕提供了一种"统计力学"诊断。

### 2.5 稳定性微扰理论（Kolb & Pakrouski 2023, PRX Quantum 4, 040348）

某些费米子疤痕族对微扰**完全不敏感**（如无序），其他的稳定到一阶。提出了两个基于可观测量的稳定性测度。

---

## 3. 序参量定义：疤痕稳定性指数 $\Xi$

### 3.1 设计原则

序参量必须满足：
1. **可计算**：用ED/DMRG/MPS即可，不需要实验设备
2. **正则化**：$\Xi \in [0,1]$
3. **区分性**：热化态 $\to 0$，精确疤痕 $\to 1$，近似疤痕 $\to (0,1)$
4. **标度敏感性**：$L\to\infty$ 极限下：存活 $\to 1$，幂律衰减 $\to 0$（慢），瞬态 $\to 0$（快）

### 3.2 分量定义

对于系统尺寸为 $L$、能谱中央的本征态 $|\psi\rangle$，定义三个分量：

#### 分量一：纠缠异常度 $A_E$

$$A_E(|\psi\rangle) = 1 - \frac{S_{\text{vN}}(L/2)}{S_{\text{Page}}(L/2)}$$

其中 $S_{\text{vN}}(L/2)$ 为半链von Neumann纠缠熵，$S_{\text{Page}}(L/2) = \frac{L}{2}\ln 2 - \frac{1}{2}$ 为无限温度Page值。

- 热化态：$S_{\text{vN}} \approx S_{\text{Page}}$ $\Rightarrow$ $A_E \to 0$
- 精确疤痕：$S_{\text{vN}} = O(\log L)$ $\Rightarrow$ $A_E \to 1$（当 $L \gg 1$）
- 近似疤痕：$S_{\text{vN}} = O(L^\nu)$，$0 < \nu < 1$ $\Rightarrow$ $A_E > 0$

#### 分量二：Krylov椭圆度 $E_K$

从 $|\psi\rangle$ 出发，通过Lanczos算法构造Krylov基 $\{|\mathcal{K}_n\rangle\}$：

$$|\mathcal{K}_0\rangle = |\psi\rangle, \quad b_0 = 0$$
$$\hat{H}|\mathcal{K}_n\rangle = b_n|\mathcal{K}_{n-1}\rangle + a_n|\mathcal{K}_n\rangle + b_{n+1}|\mathcal{K}_{n+1}\rangle$$
$$a_n = \langle\mathcal{K}_n|\hat{H}|\mathcal{K}_n\rangle, \quad b_n = \langle\mathcal{K}_n|\hat{H}|\mathcal{K}_{n-1}\rangle$$

获取Lanczos系数序列 $\{b_n\}_{n=1}^{K}$（$K$ 为截断维数或封闭点）。

定义**椭圆度**为与理想SU(2)轮廓的归一化RMS偏差：

$$E_K = 1 - \min_{h, D} \sqrt{\frac{\sum_{n=1}^{K} \left(b_n - h\sqrt{n(D-n+1)}\right)^2}{\sum_{n=1}^{K} b_n^2}}$$

其中优化在 $h > 0$ 和整数 $D \ge K$ 上进行。

- 精确SU(2)疤痕：存在 $(h, D)$ 使偏差为0 $\Rightarrow$ $E_K = 1$
- q-变形SU(2)近似疤痕：偏差有限 $\Rightarrow$ $0 < E_K < 1$
- 热化态：$b_n$ 单调增长无封闭 $\Rightarrow$ 最优拟合偏差 $\sim O(1)$ $\Rightarrow$ $E_K \approx 0$

**计算细节**：
- Lanczos算法实现时，每步执行Gram-Schmidt正交化防止数值精度丢失
- $K$ 取为 $b_K < \epsilon \cdot \max_n b_n$ 的首个指标（$\epsilon = 10^{-6}$），或截断在 $K_{\max} = 10^4$
- 若在 $K_{\max}$ 内不封闭，标记为"无封闭"，$E_K$ 仍可通过有限截断的最优拟合计算——此时 $E_K$ 将远小于1

#### 分量三：谱刚度 $R_\Delta$

若 $|\psi\rangle$ 属于一个候选疤痕塔 $\{|\psi_n\rangle\}_{n=0}^{N_T-1}$（通过低纠缠熵和相似Krylov轮廓识别），其能级为 $E_n$。定义连续间距比：

$$\delta_n = E_{n+1} - E_n$$
$$r_n = \frac{\min(\delta_n, \delta_{n+1})}{\max(\delta_n, \delta_{n+1})}$$

$$R_\Delta = \frac{\langle r \rangle - r_{\text{Poisson}}}{1 - r_{\text{Poisson}}}$$

其中 $r_{\text{Poisson}} = 2\ln 2 - 1 \approx 0.3863$（Poisson分布的均值）。分母中的1为完美等间距的理论上限 $\langle r \rangle = 1$。

- 完美等间距（SGA塔）：$\langle r \rangle = 1$ $\Rightarrow$ $R_\Delta = 1$
- 混沌热谱（GOE）：$\langle r \rangle \approx 0.536$ $\Rightarrow$ $R_\Delta \approx 0.244$
- 近似疤痕塔：$\langle r \rangle \in (0.536, 1)$ $\Rightarrow$ $R_\Delta \in (0.244, 1)$

**注**：若系统只有一条疤痕塔（如PXP模型），直接用该塔所有态的间距。若无明显塔结构（单态诊断），定义 $R_\Delta = 0$（因为无法建立等间距概念）。

对于**单态诊断**的替代方案（不需先验塔识别），定义自相关谱刚度：

$$\tilde{R}_\Delta = \frac{1}{N_{\text{peak}}} \sum_{k=1}^{N_{\text{peak}}} \frac{|\langle\psi|\hat{H}^k|\psi\rangle|^2}{\langle\psi|\hat{H}^{2k}|\psi\rangle}$$

当 $\hat{H}$ 在 $|\psi\rangle$ 生成的低维Krylov子空间内作用如SU(2)代数时，$\langle\hat{H}^k\rangle$ 呈周期模式，$\tilde{R}_\Delta$ 接近1。

但此版本对有限尺寸效应敏感，3.3小节中默认使用基于塔的 $R_\Delta$。

### 3.3 合成序参量

$$\boxed{\Xi(|\psi\rangle) = \sqrt[3]{A_E \cdot E_K \cdot R_\Delta}}$$

使用几何平均（而非算术平均）的原因：
- 确保 $\Xi = 1$ 当且仅当 $A_E = E_K = R_\Delta = 1$
- 确保 $\Xi = 0$ 当任一分量为0
- 对数尺度上的线性性：$\ln \Xi = \frac{1}{3}(\ln A_E + \ln E_K + \ln R_\Delta)$

### 3.4 完整计算流程

```
输入: 哈密顿量H (L格点), 目标本征态 |ψ⟩
输出: Ξ(|ψ⟩)

Step 1 [纠缠]: 计算 |ψ⟩ 的约化密度矩阵 ρ_{L/2} = Tr_{R}(|ψ⟩⟨ψ|)
              S_vN = -Tr(ρ_{L/2} log ρ_{L/2})
              A_E = 1 - S_vN / S_Page(L/2)

Step 2 [Lanczos]: 初始化 |K_0⟩ = |ψ⟩, b_0 = 0
              for n = 0, 1, ..., K_max:
                  |w⟩ = H|K_n⟩ - b_n|K_{n-1}⟩
                  a_n = ⟨K_n|w⟩
                  |w⟩ = |w⟩ - a_n|K_n⟩
                  b_{n+1} = |||w⟩||
                  if b_{n+1} < ε·max(b): break
                  |K_{n+1}⟩ = |w⟩ / b_{n+1}
              执行Gram-Schmidt重正交化每10步
              拟合 {b_n} 到 h√(n(D-n+1))，最小化RMS偏差
              E_K = 1 - 最小RMS相对偏差

Step 3 [谱]: 识别所有满足 A_E > 阈值 和 E_K > 阈值 的本征态
              若形成塔: 计算能级间距比 ⟨r⟩
              R_Δ = (⟨r⟩ - 0.3863) / (1 - 0.3863)
              若无塔: R_Δ = 0

Step 4 [合成]: Ξ = (A_E · E_K · R_Δ)^{1/3}
```

---

## 4. 热力学极限下的标度行为

序参量的核心价值在于其 $L \to \infty$ 标度行为能区分疤痕稳定性的三个等级。

### 4.1 三类疤痕的标度预测

| 疤痕类型 | $A_E(L)$ | $E_K(L)$ | $R_\Delta(L)$ | $\Xi(L \to \infty)$ |
|----------|---------|---------|-------------|-------------------|
| **存活 (Survival)** | $\to 1$ (对数纠缠) | $\to 1$ | $\to 1$ | **1** |
| **幂律衰减 (Power-law)** | $\to c > 0$ 或 $\sim L^{-\alpha}$ 慢 | $\to c > 0$ | $\to c > 0$ | **$\to 0$** (慢: $L^{-\alpha/3}$) |
| **瞬态 (Transient)** | $\sim e^{-L/\xi}$ 快 | $\sim e^{-L/\xi}$ | $\sim e^{-L/\xi}$ | **$\to 0$** (快: $e^{-L/3\xi}$) |

存活疤痕的判别条件——三个分量在热力学极限下均收敛到1——等价于要求：
1. 纠缠熵完全不遵循体积律（$S \sim \text{const}$ 或 $S \sim \log L$）
2. 动力学由精确的有限维Lie代数生成
3. 疤痕塔的能级严格等间距

### 4.2 有限尺寸标度分析

在实际计算中（有限 $L$），通过以下拟合提取标度律：

$$\Xi(L) = \Xi_\infty + c_1 \cdot e^{-L/\xi} + c_2 \cdot L^{-\eta}$$

- $\Xi_\infty = 1$：存活疤痕
- $\Xi_\infty = 0$ 且主导项为 $c_2 L^{-\eta}$（$\eta > 0$）：幂律衰减疤痕
- $\Xi_\infty = 0$ 且主导项为 $c_1 e^{-L/\xi}$（$\xi > 0$）：瞬态疤痕

### 4.3 与Round 1直觉的形式对应

| Round 1 直觉 | 数学诊断 | 标度判据 |
|-------------|---------|---------|
| 大森 $p > 1$（存活） | $R_\Delta \to 1$ | 间距波动 $\sigma_\Delta / \mu_\Delta \to 0$ |
| 大森 $0 < p < 1$（幂律） | $R_\Delta \to c \in (0,1)$ | 间距波动维持有限比例 |
| 大森 $p \approx 0$（瞬态） | $R_\Delta \to 0$ | 间距分布趋于GOE/WD |
| TGF-$\beta$ 破缺强度 $\varepsilon(L)$ | $1 - E_K \sim \varepsilon(L)$ | 椭圆度偏离的标度指数 |
| 赋格周期扩散 $D_\varphi$ | $\text{Var}(t_{\text{rev},n}) \sim D_\varphi \cdot n$ | revival时间的方差增长 |

---

## 5. 数值实现注意事项

### 5.1 Lanczos算法的数值稳定性

标准Lanczos在有限精度算术下会出现"鬼影"本征值（ghost eigenvalues），源于Krylov向量间的正交性丢失。对策：

1. **全重正交化**：每步对 $|\mathcal{K}_{n+1}\rangle$ 做一次对所有先前 $|\mathcal{K}_j\rangle$ 的Gram-Schmidt
2. **半正交化**：每 $m$ 步（$m \approx 10$）做一次局部重正交化，对最近 $2m$ 个向量
3. **增量正交化**：$|\mathcal{K}_{n+1}\rangle = |\mathcal{K}_{n+1}\rangle - \sum_{j=0}^n \langle\mathcal{K}_j|\mathcal{K}_{n+1}\rangle |\mathcal{K}_j\rangle$，重复直到范数收敛

推荐的实用方案：半正交化 $m=10$ + 每50步一次全重正交化。

### 5.2 有限尺寸效应

- 对于 $L \lesssim 12$ 的自旋链（ED可解），$\Xi$ 的统计波动较大，建议对能谱中央的窗口（如 $|E - E_{\text{mid}}| < 0.1W$，$W$ 为带宽）取平均
- 对于 $L > 12$（DMRG/MPS区域），目标态的选择受限于可达到的本征态数量，建议聚焦于已知候选疤痕态（如Néel态、自旋螺旋态等）

### 5.3 疤痕塔识别算法

```python
def identify_scar_towers(eigenstates, A_E_threshold=0.3, E_K_threshold=0.3):
    """
    输入: 所有本征态及其 A_E, E_K
    输出: 疤痕塔列表
    """
    candidates = [s for s in eigenstates 
                  if s.A_E > A_E_threshold and s.E_K > E_K_threshold]
    
    # 按能量排序
    candidates.sort(key=lambda s: s.E)
    
    # 识别等间距塔
    towers = []
    current_tower = [candidates[0]]
    for i in range(1, len(candidates)):
        if len(current_tower) >= 2:
            expected_E = 2 * current_tower[-1].E - current_tower[-2].E
            if abs(candidates[i].E - expected_E) < 0.1 * abs(expected_E - current_tower[-1].E):
                current_tower.append(candidates[i])
                continue
        # 开始新塔
        if len(current_tower) >= 3:
            towers.append(current_tower)
        current_tower = [candidates[i]]
    
    if len(current_tower) >= 3:
        towers.append(current_tower)
    
    return towers
```

---

## 6. 验证基准：已知模型上的预期值

### 6.1 PXP模型（Rydberg原子链）

$$H_{\text{PXP}} = \sum_j P_{j-1} X_j P_{j+1}$$

- Néel态 $|\mathbb{Z}_2\rangle = |\uparrow\downarrow\uparrow\downarrow\cdots\rangle$：
  - 纠缠：$S \sim \ln L$（对数）$\Rightarrow$ $A_E \to 1$（$L$大时）
  - Lanczos：近似q-变形SU(2)，$E_K \approx 0.7\text{--}0.85$（$L=16\text{--}32$估计）
  - 谱：间距有涨落，$R_\Delta \approx 0.6\text{--}0.8$
  - **预期** $\Xi \approx 0.7\text{--}0.85$（$L=24$），$L\to\infty$ 渐近值待确定

### 6.2 广义AKLT模型（精确SGA疤痕）

$$H = \sum_j \left[\vec{S}_j \cdot \vec{S}_{j+1} + \frac{1}{3}(\vec{S}_j \cdot \vec{S}_{j+1})^2\right] + \text{微扰项}$$

- 疤痕塔态：
  - 纠缠：严格 $S \sim \text{const}$（面积律）$\Rightarrow$ $A_E = 1$（$L$大时）
  - Lanczos：严格SU(2)封闭，$K = L+1$ $\Rightarrow$ $E_K = 1$
  - 谱：严格等间距 $\Rightarrow$ $R_\Delta = 1$
  - **预期** $\Xi = 1$（精确值，任意 $L$）

### 6.3 热化态（非可积模型，如XXZ $\Delta=1.5$ 中能谱）

- 随机中能本征态：
  - 纠缠：体积律 $S \approx S_{\text{Page}}$ $\Rightarrow$ $A_E \approx 0$
  - Lanczos：单调增长无封闭 $\Rightarrow$ $E_K \approx 0$
  - 谱：GOE统计 $\Rightarrow$ $R_\Delta \approx 0$
  - **预期** $\Xi \approx 0$

### 6.4 作为对照：可积模型（XXZ $\Delta=0$，自由费米子）

- 任意中能本征态：
  - 纠缠：对数律（但与疤痕机制无关）$\Rightarrow$ $A_E$ 可能较大
  - Lanczos：可能封闭（可积性）$\Rightarrow$ $E_K$ 可能非零
  - 谱：Poisson统计 $\Rightarrow$ $R_\Delta = 0$
  - **预期** $\Xi$ 可能非零但 $R_\Delta$ 分量暴露可积性而非疤痕性
  - **教训**：$\Xi$ 仅在有先验知识指向非可积哈密顿量时才有意义。对于一般模型，需先用 $r$-统计排除可积性。

---

## 7. 开放问题与下一步

1. **$\Xi$ 的普适性**：三个分量是否完备？是否存在具有高 $\Xi$ 值但并非疤痕的态（假阳性）？可积模型是已知的假阳性来源——需要加一个前置过滤器。

2. **$q$-变形SU(2)的解析处理**：对于近似疤痕，$\{b_n\}$ 偏离理想椭圆的形式可通过 $q$-变形参数量化。$q$ 与 $E_K$ 的关系是：
   $$E_K = 1 - (1-q) \cdot f(L) + O((1-q)^2)$$
   函数 $f(L)$ 的确切形式需要解析推导。

3. **与Fisher零点法的关系**：Fisher零点的连续线特征可能是 $\Xi$ 的独立验证。两种方法是否给出相同的疤痕分类？特别地，是否存在 $\Xi$ 高但Fisher零点结构不典型的态？

4. **动力学版本**：目前 $\Xi$ 是静态（本征态）诊断。是否存在等价的动力学版本——从淬灭动力学直接提取 $\Xi(t)$，使其可被冷原子实验测量？

5. **更高效的Lanczos实现**：对于DMRG/MPS框架，标准的Lanczos算法需要作用于全Hilbert空间的态向量。需要开发MPS兼容的Lanczos变体（如DMRG-Lanczos混合算法），使得 $L=40+$ 的系统可通过MPS计算 $E_K$。

---

## 参考文献

1. Hu, Zhang, Han & You, "Krylov complexity in quantum many-body scars of spin-1 models," *Phys. Rev. B* **111**, 165106 (2025). [arXiv:2503.24073](https://arxiv.org/abs/2503.24073)
2. Bhattacharjee, Sur & Nandy, "Probing quantum scars and weak ergodicity breaking through quantum complexity," *Phys. Rev. B* **106**, 205150 (2022). [arXiv:2208.05503](https://arxiv.org/abs/2208.05503)
3. Yao & Zhang, "Quantum many-body scars through the lens of correlation matrix," (2024). [arXiv:2410.21812](https://arxiv.org/abs/2410.21812)
4. "Majorana scars as group singlets," *Phys. Rev. Research* **5**, 043208 (2023).
5. Meng et al., "Detecting Many-Body Scars from Fisher Zeros," *Phys. Rev. Lett.* (2025). [arXiv:2501.09478](https://arxiv.org/abs/2501.09478)
6. Kolb & Pakrouski, "Stability of the Many-Body Scars in Fermionic Spin-1/2 Models," *PRX Quantum* **4**, 040348 (2023).
7. Pakrouski & Sun, "Certain BCS wavefunctions are quantum many-body scars," (2024). [arXiv:2411.13651](https://arxiv.org/abs/2411.13651)
8. "Group-invariant scars framework," arXiv:2007.00845, arXiv:2106.10300.
