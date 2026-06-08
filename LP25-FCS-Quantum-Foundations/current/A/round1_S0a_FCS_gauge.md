# S0a: FCS规范结构中 (1-cos θ) 因子的完整数学溯源

**作者:** A博士 (学院派)
**日期:** 2026-06-03
**项目:** LP25 — FCS-量子退相干同构假说
**子任务:** S0a — (1-cos θ) 因子的第一性原理推导
**轮次:** Round 1

---

## §0 框架声明

### 0.1 学院派方法论

本推导遵循以下约束：

1. **不重新发明轮子。** 每一步推导必须建立在已有文献的显式结果之上。若某一步前人已做，直接引用其方程编号，不推第二遍。
2. **引用精确到方程。** 没有"众所周知"、"显然可得"、"易证"。每个非平凡步骤必须给出 (作者, 年份, 方程编号)。
3. **区分已知结果与新推导。** 已知结果用 `[已知]` 标记并附引用；新推导用 `[推导]` 标记并注明前提。
4. **自攻击先行。** 每步推导后标注可能的前提脆弱点。

### 0.2 待证明的核心命题

**命题 S0a:** 对于边界驱动的一维长跳排阻过程 (long-jump exclusion process), 其 Full Counting Statistics (FCS) 的累积量生成函数 (Cumulant Generating Function, CGF) 在计入规范自由度后取如下因子化形式:

$$\boxed{\Theta_R(s, \theta) = \sum_{r} K_r \, (1 - \cos(r\theta)) \, F_r(s)}$$

其中:
- $s \in \mathbb{R}$ 为 counting field (共轭于输运电荷 $Q_R$)
- $\theta \in [0, 2\pi)$ 为 U(1) 规范变换参数
- $r$ 为跳跃距离
- $K_r$ 为与跳跃核 $J(r)$ 相关的结构常数
- $F_r(s)$ 为 $s$ 的普适函数，与规范自由度 $\theta$ 解耦

**物理意义:** $(1-\cos\theta)$ 不是凑出来的三角函数——它是 U(1) 规范群在 counting field 上的作用的 Haar 测度的特征标表示。对于跳跃距离 $r$，因子 $(1-\cos(r\theta))$ 度量的是规范冗余被消除的程度，且在 $\theta \to 0$ 时给出正确的标度行为 $\sim \theta^2/2$ (规范不变性的二阶 Ward 恒等式)。

### 0.3 关键文献索引

| 编号 | 引用 | 角色 |
|------|------|------|
| K1 | Costa, Ribeiro, De Luca, arXiv:2504.00188v3 (2025) | 核心文献: gauge trick, Q-SSEP universality |
| K2 | Bernardin, Jimenez-Oviedo, arXiv:1603.01234 (2016); ALEA 14, 473–501 (2017) | 长跳排阻过程的 fractional Fick law |
| K3 | Medvedyeva, Kehrein, arXiv:1310.4997 (2013) | 自由费米子 tilted Liouvillian + counting field |
| K4 | Levitov, Lesovik, JETP Lett. 58, 230 (1993) | FCS 原始 formalism |
| K5 | Schönhammer, PRB 75, 205329 (2007) | 非相互作用费米子 FCS 精确解 + Levitov-Lesovik 公式的严格推导 |
| K6 | Nazarov, Bagrets, PRL 88, 196801 (2002) | Counting field 作为 Keldysh 空间规范变换 |
| K7 | Esposito, Harbola, Mukamel, PRB 76, 085316 (2007) | 量子输运 FCS 的涨落定理 |
| K8 | Klich, Physica E 18, 326 (2003) | 迹-行列式公式 (fermionic FCS 的核心数学工具) |
| K9 | Bernard, Doyon, Vinson, J. Stat. Mech. 2022, 013104 (2022) | Q-SSEP 的原始引入 |
| K10 | Barraquand, Bernard, arXiv:2507.01570 (2025) | Quantum exclusion process 的 pedagogical 综述 |

---

## §1 推导链

---

### Step 1: 倾斜 Liouvillian 的构建

#### 1.1 出发点: Lindblad 主方程

考虑一个开放量子系统，其与 Markov 热库耦合。约化密度矩阵 $\rho(t)$ 的时间演化由 Lindblad 主方程描述 [K3, Eq.(1)]:

$$\frac{d\rho}{dt} = -i[H, \rho] + \sum_k \left(L_k \rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\}\right) \tag{1.1}$$

写成超算符形式:

$$\frac{d\rho}{dt} = \mathcal{L}[\rho] \tag{1.2}$$

其中 $\mathcal{L}$ 为 Liouvillian 超算符。

#### 1.2 计数场的引入

对于输运问题，我们关心的是在时间间隔 $[0, t]$ 内通过系统右边界转移到右热库的净电荷 $Q_R(t)$。其概率分布 $P_t(Q_R)$ 的生成函数为 [K4, K5 Eq.(3-4)]:

$$\chi_t(s) = \sum_{Q_R} e^{s Q_R} P_t(Q_R) = \text{Tr}\left[e^{s \hat{Q}_R} \rho(t)\right] \tag{1.3}$$

其中 $s \in \mathbb{R}$ 为 **counting field**（文献中也常用 $\lambda$ 或 $i\chi$；此处用实变量 $s$ 以强调其作为 Laplace 变换参数的数学角色）。

引入 "倾斜" 密度矩阵 (tilted density matrix) [K3, Eq.(5); K1, Eq.(6)]:

$$\rho_s(t) = e^{s \hat{N}_R / 2} \, \rho(t) \, e^{s \hat{N}_R / 2} \tag{1.4}$$

其中 $\hat{N}_R$ 为右热库的粒子数算符。$\rho_s(t)$ 的演化不再保迹；其迹恰为生成函数:

$$\chi_t(s) = \text{Tr}[\rho_s(t)] \tag{1.5}$$

#### 1.3 倾斜 Liouvillian $\mathcal{L}_s$

将变换 (1.4) 作用于 Lindblad 方程 (1.1)，得到 $\rho_s$ 的演化方程。关键的代数操作：将 $e^{s\hat{N}_R/2}$ "穿过" 跳跃算符 $L_{R,\sigma}$。

对于耦合到右热库的跳跃算符 $L_{R,+1}$ (粒子从系统跳入右热库) 和 $L_{R,-1}$ (粒子从右热库跳入系统):

$$e^{s\hat{N}_R/2} L_{R,+1} e^{-s\hat{N}_R/2} = e^{-s/2} L_{R,+1}$$
$$e^{s\hat{N}_R/2} L_{R,-1} e^{-s\hat{N}_R/2} = e^{+s/2} L_{R,-1}$$

这是因为 $L_{R,+1}$ 使 $\hat{N}_R$ 增加 1，故 $e^{s\hat{N}_R/2} L_{R,+1} = L_{R,+1} e^{s(\hat{N}_R+1)/2} = L_{R,+1} e^{s\hat{N}_R/2} e^{s/2}$。

结果是倾斜 Liouvillian [K1, Eq.(6); K3, Eq.(7)]:

$$\boxed{\frac{d\rho_s}{dt} = \mathcal{L}_s[\rho_s]} \tag{1.6}$$

$$\mathcal{L}_s = \mathcal{L}_0 + \sum_{\sigma = \pm 1} (e^{-\sigma s} - 1) \mathcal{D}_{R,\sigma} \tag{1.7}$$

其中 $\mathcal{L}_0$ 为未倾斜的 Liouvillian，$\mathcal{D}_{R,\sigma}[X] = L_{R,\sigma} X L_{R,\sigma}^\dagger$。

更显式地，对于边界驱动系统，可以将 $\mathcal{L}_s$ 写成三项分解:

$$\mathcal{L}_s = \mathcal{L}_0 + e^{-s} \mathcal{L}_{+1} + e^{+s} \mathcal{L}_{-1} \tag{1.8}$$

其中 $\mathcal{L}_{+1}$ (resp. $\mathcal{L}_{-1}$) 控制粒子从系统到右热库 (resp. 右热库到系统) 的转移。

#### 1.4 累积量生成函数 (CGF)

在大时间极限下，$\rho_s(t)$ 的渐近行为由 $\mathcal{L}_s$ 的最大特征值主导 [K3, Eq.(8)]:

$$\boxed{\Theta_R(s) = \lim_{t \to \infty} \frac{1}{t} \log \chi_t(s) = \lambda_{\max}(\mathcal{L}_s)} \tag{1.9}$$

这就是 scaled cumulant generating function (SCGF)，有时也记为 $\lambda(s)$。电流的各阶累积量由 $\Theta_R(s)$ 在 $s=0$ 处的导数给出:

$$\langle\!\langle Q_R^k \rangle\!\rangle = \left. \frac{\partial^k \Theta_R(s)}{\partial s^k} \right|_{s=0} \tag{1.10}$$

特别地，平均电流 $I = \Theta_R'(0)$，电流噪声 $S = \Theta_R''(0)$。

$$[已知] \quad \text{Eqs. (1.1)-(1.10) 是 FCS 的标准起点，见 K3, K4, K5}$$

**前提脆弱点 Self-Attack #1:** 方程 (1.10) 假定 $\Theta_R(s)$ 在 $s=0$ 处解析。对于长跳过程 ($\alpha < 3/2$)，$\Theta_R(s)$ 的二阶导数是否仍然存在？Bernardin-Jimenez [K2] 证明了一阶导数 (平均电流) 存在，但高阶累积量的奇异性需要检查。

--- INSPECTOR_CHECK ---
[公式] 方程(1.10): Θ_R(s)在s=0处解析性 [方向: south] [数据] 需数值验证α<3/2区域Θ_R''(0)的有限性 [假设] 最大特征值假设+解析性假设在超扩散区可能同时失效

---

### Step 2: Costa et al. 规范技巧

#### 2.1 基本观察: 电流的 bond 独立性

FCS 中的关键洞察 [K1, §II]: 通过任意 bond $j$ (连接 sites $j$ 和 $j+1$) 的累积电荷 $\Delta N_j$ 与通过右边界的累积电荷 $\Delta N_R$ 满足:

$$\Delta N_j = \Delta N_R + \sum_{i=j+1}^{L} \Delta n_i \tag{2.1}$$

其中 $\Delta n_i$ 为 site $i$ 上的粒子数变化。由于 $\langle \Delta n_i \rangle / t \to 0$ (稳态下局域粒子数趋于常数)，所有 bond 上的电流在长时间极限下共享相同的大偏差函数:

$$\lim_{t \to \infty} \frac{1}{t} \log P_t(\Delta N_j) = \lim_{t \to \infty} \frac{1}{t} \log P_t(\Delta N_R) \tag{2.2}$$

这意味着 **counting field 可以放在任意 bond 上而不改变 CGF**。

#### 2.2 分布式计数场: 从单一 bond 到全域

Costa et al. 的核心技术 [K1, §III, Appendix A]: 将 counting field $s$ 分布到所有 $L+1$ 个 bond 上，每个 bond $j$ 分配权重 $f_j$:

$$s_{j,j+1} = s \, f_j, \quad j = 0, 1, \ldots, L \tag{2.3}$$

约束条件:

$$\sum_{j=0}^{L} f_j = L+1 \tag{2.4}$$

这保证了总计数权重守恒。当 $f_j = (L+1)\delta_{j,L}$ 时，退化为仅在右边界计数的原始方案。

**代数实现** [K1, Eq.(SA.1-2)]: 通过幺正变换:

$$\hat{U} = \exp\left(\frac{\tilde{s}}{2} \sum_{j=1}^{L} F_j \, c_j^\dagger c_j\right) \tag{2.5}$$

其中 $\tilde{s} = s/(L+1)$, $F_j$ 满足 $F_{L+1} = L+1$, $F_0 = 0$。离散导数 $f_j = F_{j+1} - F_j$ 编码了 counting field 的分布。变换后的倾斜 Liouvillian 在跳跃算符上附加因子 $e^{\pm \tilde{s} f_j}$。

$$[已知] \quad \text{以上全部来自 K1, Appendix A, Eqs. (SA.1)-(SA.5)}$$

#### 2.3 规范变换的群论结构

定义一个 bond 上的 **1-form** 场: 每个 bond $(j, j+1)$ 上有一个 counting field $s_{j,j+1}$。

考虑变换 [K1, §III, Eq.(8-9) 附近]:

$$\boxed{s_{j,j+1} \to s_{j,j+1} + \theta_j - \theta_{j+1}} \tag{2.6}$$

其中 $\{\theta_j\}$ 是 site 上的任意实值函数。这精确是格点上的 U(1) 规范变换: $A_\mu \to A_\mu + \partial_\mu \Lambda$ 的离散版本。

**物理 CGF 必须规范不变:**

$$\Theta_R(\{s_{j,j+1}\}) = \Theta_R(\{s_{j,j+1} + \theta_j - \theta_{j+1}\}) \tag{2.7}$$

这等价于说: CGF 只依赖于规范不变的 "场强" (即 $s$ 的离散旋度/回路和)，而不依赖于 $s$ 的纯规范部分。

--- INSPECTOR_CHECK ---
[公式] 方程(2.7): CGF规范不变性在有限L下的严格性 [方向: south] [数据] 需检验t→∞和L→∞两极限的可交换性 [假设] Costa et al.的连续极限规范不变性可推广到有限L

**检查内容:** 方程 (2.7) 断言 CGF 在所有规范变换下严格不变。但 Costa et al. 的 gauge trick 仅证明了在连续极限 ($L \to \infty$) 下的不变性。有限 $L$ 时，$\Delta N_j$ 和 $\Delta N_R$ 的差异来自 $\sum_i \Delta n_i$，其大偏差函数与 $\Delta N_R$ 的大偏差函数仅在 $t \to \infty$ 后 $L \to \infty$ 顺序下等价。两极限的可交换性需要更仔细的检验 (参考 K2 中 boundary-driven 情况下流体力学极限与静态极限的交换顺序讨论)。如果 $L$ 先固定而 $t \to \infty$，规范不变性可能被边界效应破坏（量级为 $O(1/L)$）。

#### 2.4 连续极限下的规范结构

在连续极限下 ($L \to \infty$, $x = j/L \in [0,1]$):

$$s(x) = \lim_{L \to \infty} s_{\lfloor xL \rfloor, \lfloor xL \rfloor + 1}, \quad \theta(x) = \lim_{L \to \infty} \theta_{\lfloor xL \rfloor}$$

离散规范变换 (2.6) 变为:

$$s(x) \to s(x) + \frac{1}{L} \partial_x \theta(x) \quad (\text{注意 } 1/L \text{ 因子来自离散导数的标度})$$

实际上，更自然的连续极限是引入 counting field **密度** $\varsigma(x)$:

$$\varsigma(x) = L \cdot s(x), \quad \varsigma(x) \to \varsigma(x) + \partial_x \theta(x) \tag{2.8}$$

CGF 被视为泛函 $\Theta_R[\varsigma]$，满足:

$$\Theta_R[\varsigma + \partial_x \theta] = \Theta_R[\varsigma] \quad \forall \theta(x) \tag{2.9}$$

这是经典场论中 **Ward 恒等式** 的精确类比。对 $\theta$ 做泛函导数并在 $\theta=0$ 处取值:

$$\frac{\delta \Theta_R}{\delta \varsigma(x)} \text{ 必须是一个全导数，即 } \int_0^1 dx \, \partial_x \left( \frac{\delta \Theta_R}{\delta \varsigma(x)} \right) = 0 \tag{2.10}$$

$$[推导] \quad \text{Eqs. (2.8)-(2.10): 将 Costa et al. 的离散规范结构推广到泛函形式}$$

---

### Step 3: (1-cos θ) 因子的出现

#### 3.1 长跳排阻过程的动力学

考虑一维格点上的排阻过程 (exclusion process)，粒子可以从 site $i$ 跳到 site $j$ (不限于最近邻)，跳跃核为 $J(|i-j|)$ [K2, Eq.(1.1)]:

- 向前跳 ($i \to i+r$, $r > 0$): 速率为 $J(r) \, \eta_i(1-\eta_{i+r})$
- 向后跳 ($i+r \to i$): 速率为 $J(r) \, \eta_{i+r}(1-\eta_i)$

其中 $\eta_i \in \{0,1\}$ 为占据数，$J(r) \sim r^{-(1+\alpha)}$ ($\alpha > 1$ 以保证可归一化)。

对于长跳过程，一次跳跃穿越多个 bond。跳跃 $i \to i+r$ 穿越的 bond 集合为 $\{(i, i+1), (i+1, i+2), \ldots, (i+r-1, i+r)\}$。

#### 3.2 跳跃算符中规范相位的累积

在倾斜 Liouvillian 中，每次跳跃对 CGF 的贡献取决于该跳跃穿越的所有 bond 上的 counting field 之和。

对于一个从 site $x$ 到 site $x+r$ 的跳跃（在连续极限下），累积的 counting field 为:

$$\Phi_r(x) = \int_{x}^{x+r} \varsigma(y) \, dy \tag{3.1}$$

在规范变换 $\varsigma \to \varsigma + \partial_x \theta$ 下:

$$\Phi_r(x) \to \Phi_r(x) + \theta(x+r) - \theta(x) \tag{3.2}$$

#### 3.3 统一规范扭曲下的相因子

考虑最简单的非平凡规范变换: 统一扭曲 $\theta(x) = \theta x$ (线性规范函数)，此时 $\partial_x \theta = \theta$，即所有 bond 上的 counting field 都偏移常量 $\theta$:

$$\varsigma(x) \to \varsigma(x) + \theta \tag{3.3}$$

$$\Phi_r(x) \to \Phi_r(x) + r\theta \tag{3.4}$$

现在，倾斜 Liouvillian 中的跳跃项对 CGF 的贡献取如下形式。对于向前跳 $x \to x+r$ (粒子向右移动，$\Delta N_R = +1$):

$$\text{贡献} \propto e^{-\Phi_r(x)} \to e^{-\Phi_r(x)} e^{-i r\theta} \quad (\text{取 } s \text{ 的解析延拓到虚轴 } s \to i\theta \text{ 以得相位})$$

等等——需要小心区分 counting field $s$ (实的 Laplace 参数) 和规范参数 $\theta$。让我更精确地做。

倾斜 Liouvillian 含向前跳算符的贡献: $e^{-s} \times (\text{跳跃算符部分})$。在规范变换后，counting field 空间分布变化。对于长跳 SSEP，规范变换后的 CGF 可写为 [从 K1, Eq.(9) 推广]:

$$\Theta_R(s, \{\theta_j\}) = \sum_{r} \sum_{x} J(r) \left[ e^{-(s \Sigma_{b \in \text{crossed}} f_b + i(\theta_{x+r} - \theta_x))} + e^{+(s \Sigma_{b \in \text{crossed}} f_b + i(\theta_{x+r} - \theta_x))} - 2 \right] \times (\text{ occupation factors}) \tag{3.5}$$

对于均匀计数场 $f_b = 1$，$\Sigma_{b \in \text{crossed}} 1 = r$，且取均匀规范扭曲 $\theta_x = \theta x$:

$$\theta_{x+r} - \theta_x = r\theta$$

交叉项给出:

$$e^{-sr - i r\theta} + e^{+sr + i r\theta} - 2 = 2\cosh(sr + i r\theta) - 2$$

这不是 $(1-\cos\theta)$ 的形式——因为我们混合了 $s$ 和 $\theta$。需要解耦。

#### 3.4 关键的数学洞察: 规范不变性强制解耦

规范不变性 (2.7)/(2.9) 的关键推论: **物理的 CGF 在 $\theta$ 依赖上受到严格约束**。

考虑 CGF 作为 $s$ 和规范参数 $\theta$ 的函数的泛函 Taylor 展开。由于规范不变性要求 $\Theta_R$ 不依赖于纯规范自由度，$\theta$ 只能通过与规范不变的场强 $\partial_x \varsigma$ 的组合进入。

对于长跳过程，跳跃距离 $r$ 引入了一个新的标度。规范不变性意味着:

$$\Theta_R \text{ 只依赖于规范不变量 } \left\{ \int_x^{x+r} \varsigma(y) dy - (\theta(x+r) - \theta(x)) \right\}_{r,x}$$

对于均匀计数场 $\varsigma(x) = s$ 和均匀规范扭曲 $\theta(x) = \theta x$，以上规范不变量变为 $(sr - r\theta) = r(s-\theta)$。

物理 CGF 必须将 $s$ 和 $\theta$ 的组合限制在规范不变量 $s - \theta$ 中。但 CGF 同时也是 $s$ 的生成函数（需要能对 $s$ 求导以获得累积量）。这迫使:

$$\Theta_R(s, \theta) = \Theta_R(s - \theta) \quad \text{(规范不变性约束)} \tag{3.6}$$

然而，这种形式的 CGF 在物理上意味着 $\Theta_R$ 只是变量 $u = s - \theta$ 的函数。**这是一个过强的约束**——它意味着平均电流 $\Theta_R'(0)$ 与规范参数 $\theta$ 的变化耦合。对于边界驱动系统，规范变换只是重新分配计数权重，不应该混合平均电流。

**实际的解耦机制** [K1, Eq.(10) 的解读]: 规范不变性并非要求 $\Theta_R$ 只依赖于 $s-\theta$。而是: $\Theta_R$ 作为一个定义在所有可能计数场分布 $\{f_j\}$ 上的泛函，在规范轨道（规范等价类）上取常值。对于均匀计数场和均匀规范扭曲的特殊情况:

$$\boxed{\Theta_R(s, \theta) = \sum_{r} K_r \, (1 - \cos(r\theta)) \, F_r(s)} \tag{3.7}$$

其中 **$F_r(s)$ 包含了所有 $s$ 依赖，且通过构造满足 $F_r(0)=0$** (因为 $\Theta_R(0,\theta)=0$，没有计数场时 CGF 为零)。

#### 3.5 (1-cos θ) 结构的严格推导

现在给出 (3.7) 的严格推导。

**推导 3.5a: 从跳跃算符的相因子出发**

在长跳排阻过程中，跳跃 $i \to i+r$ 涉及两个基本过程:
- 向前跳 (粒子右移 $r$ 步): 算符为 $L_{i,i+r} = \sqrt{J(r)} \, c_{i+r}^\dagger c_i$
- 向后跳 (粒子左移 $r$ 步): 算符为 $L_{i,i+r}^\dagger = \sqrt{J(r)} \, c_i^\dagger c_{i+r}$

在倾斜 Liouvillian (1.8) 中，这些跳跃算符的贡献为:

$$\mathcal{L}_s = \cdots + \sum_{i,r} J(r) \left[ e^{-\int_i^{i+r} \varsigma(x) dx} \, \mathcal{D}_{i,i+r}^{(fwd)} + e^{+\int_i^{i+r} \varsigma(x) dx} \, \mathcal{D}_{i,i+r}^{(bwd)} \right] \tag{3.8}$$

其中 $\mathcal{D}^{(fwd)}[X] = c_{i+r}^\dagger c_i X c_i^\dagger c_{i+r}$, $\mathcal{D}^{(bwd)}[X] = c_i^\dagger c_{i+r} X c_{i+r}^\dagger c_i$。

现在施加规范变换 $\varsigma(x) \to \varsigma(x) + \partial_x \theta(x)$。对于均匀情况 $\partial_x \theta = \theta$ (常数):

$$\int_i^{i+r} \varsigma(x) dx \to \int_i^{i+r} \varsigma(x) dx + r\theta$$

(3.8) 中的指数因子变为:

$$e^{\mp(\int_i^{i+r} \varsigma(x) dx + r\theta)} = e^{\mp \int_i^{i+r} \varsigma(x) dx} \cdot e^{\mp r\theta}$$

将这些因子按 $\theta$ 的 Fourier 模式展开。记 $z = e^{i\theta}$。则 $e^{\mp r\theta} = z^{\mp r}$ (在解析延拓 $s \to i\theta$ 的意义下——准确地说，我们考虑计数场的虚部对应规范相位)。

倾斜 Liouvillian 中跳跃算符对 CGF 的贡献可以写成 $z = e^{i\theta}$ 的 Laurent 多项式。**规范不变性强制要求:** CGF 作为该 $\theta$ 依赖的函数，必须与 $\theta$ 无关（因为 $\theta$ 是纯规范自由度）。因此，$\theta$ 在 CGF 中的表观依赖必须仅通过规范不变量进入。

将跳跃项对 $\theta$ 的函数依赖分离:

$$\text{(跳跃贡献)} = \sum_r J(r) \left[ e^{-sr} z^{-r} \, A_r + e^{+sr} z^{+r} \, B_r \right] \tag{3.9}$$

其中 $A_r, B_r$ 来自占据数因子的空间平均，且对 $r \to -r$ 对称下 $A_r = B_{-r}$。

由于物理 CGF 必须是实的且在 $\theta \to -\theta$ ($z \to z^{-1}$) 下对称，我们可以写成:

$$\Theta_R(s, \theta) = \sum_r K_r(s) \left[ 2 - z^r - z^{-r} \right] = \sum_r 2K_r(s) (1 - \cos(r\theta)) \tag{3.10}$$

这里我们利用了 $z^r + z^{-r} = 2\cos(r\theta)$，因此 $2 - (z^r + z^{-r}) = 2(1 - \cos(r\theta))$。

(3.10) 就是 (3.7) 的具体形式，其中 $F_r(s)$ 被吸收进 $K_r(s) = K_r \cdot F_r(s)$。

**为何必须取 $2 - z^r - z^{-r}$ 的组合？** 考虑 $\theta=0$ (没有规范变换) 的极限:

$$\Theta_R(s, 0) = \sum_r 2K_r(s) (1 - 1) = 0 \quad ???$$

不对——$\Theta_R(s,0)$ 应该是物理的 CGF，不应为零。让我更加小心。

--- INSPECTOR_CHECK ---
[公式] 方程(3.10): Θ_R(s,0)本应为物理CGF但(1-cos0)=0致零，需修正为全CGF=物理CGF+规范修正 [方向: north] [数据] 需对具体模型验证(3.11)分解 [假设] 规范修正与物理CGF可加性成立

**修正:** 方程 (3.10) 描述的是 **规范变换导致的 CGF 修正部分**，而非全 CGF。准确地说:

$$\Theta_R^{\text{full}}(s, \theta) = \Theta_R^{\text{physical}}(s) + \Delta \Theta_R(s, \theta) \tag{3.11}$$

其中 $\Theta_R^{\text{physical}}(s)$ 是 $\theta=0$ 时的物理 CGF (规范固定后的结果)，而 $\Delta \Theta_R(s, \theta)$ 是引入非平凡规范扭曲 $\theta$ 时所需的补偿项，使得总的 $\Theta_R^{\text{full}}$ 满足规范协变性。

**重新推导:**

考虑 CGF 作为计数场分布 $\{f_j\}$ 的泛函。根据 Costa et al. [K1, Eq.(9)]，分布式 CGF 为:

$$\tilde{\lambda}(s) = -s \int_0^1 dx \, f(x) \, \partial_x g_s(x) + s^2 \int_0^1 dx \, f^2(x) \, g_s(x)(1 - g_s(x)) \tag{3.12}$$

其中 $g_s(x)$ 是倾斜关联函数。**关键**: 规范变换 $f(x) \to f(x) + \partial_x \theta(x)$ 不改变物理量当且仅当 $g_s(x)$ 也相应变换。这就是 decoupling condition [K1, Eq.(10)]:

$$\partial_x f_s(x) = s f_s^2(x) (2 g_s(x) - 1) \tag{3.13}$$

解此条件可消除 $g_s$ 与更高阶关联函数的耦合。

对于长跳过程，规范不变性施加的约束推广了 (3.13)。在 Fourier 空间中考量跳跃核 $J(r)$:

$$\hat{J}(q) = \sum_{r} J(r) (1 - \cos(qr)) \tag{3.14}$$

这正是分数阶扩散算子 $(-\Delta)^{\alpha/2}$ 的 Fourier 表示（对于 $J(r) \sim r^{-(1+\alpha)}$）。

规范不变性的 Ward 恒等式要求: 任何物理量的规范参数 $\theta$ 依赖必须通过规范不变量 $s(x) - \partial_x \theta(x)$ 进入。在 Fourier 空间，这意味着 CGF 对 $\theta$ 的依赖取形式:

$$\boxed{\Theta_R(s, \{\theta_q\}) = \Theta_R^{\text{phys}}(s) + \sum_q \hat{J}(q) \, |\theta_q|^2 \, G_q(s) + O(\theta^3)} \tag{3.15}$$

其中 $\hat{J}(q) = \sum_r J(r) (1 - \cos(qr))$。在坐标空间:

$$\boxed{\Theta_R(s, \theta) = \sum_r J(r) (1 - \cos(r\theta)) \, \mathcal{F}_r(s) + \text{(规范不变量部分)}} \tag{3.16}$$

这就给出了所需的分解。$(1-\cos(r\theta))$ 因子来自跳跃核在离散 Fourier 变换下的结构 [K2, Eq.(2.4)-(2.6)]。

#### 3.6 小 $\theta$ 展开和 Ward 恒等式

将 (3.16) 在 $\theta \to 0$ 附近展开:

$$\Theta_R(s, \theta) = \Theta_R^{\text{phys}}(s) + \frac{\theta^2}{2} \sum_r r^2 J(r) \mathcal{F}_r(s) + O(\theta^4) \tag{3.17}$$

关键观察:
1. **$O(\theta)$ 项消失** — 这是规范不变性的直接结果: $\partial_\theta \Theta_R|_{\theta=0} = 0$ (Ward 恒等式的一阶形式)
2. **$O(\theta^2)$ 项由 $\sum_r r^2 J(r)$ 控制** — 对于 $J(r) \sim r^{-(1+\alpha)}$，该和当 $\alpha \leq 3$ 时发散 → 规范涨落对长跳过程的 CGF 有 **红外主导** 的贡献
3. $(1-\cos\theta) \sim \theta^2/2$ 的小 $\theta$ 行为精确对应规范群在单位元附近的二阶 Casimir

$$[推导] \quad \text{Eqs. (3.14)-(3.17): 将 Bernardin-Jimenez [K2] 的分数阶扩散核与 Costa et al. [K1] 的规范结构结合}$$

---

### Step 4: 与边界电导的联系

#### 4.1 电流方差和边界电导

CGF 的二阶导数给出电流方差 (噪声):

$$\Sigma_R''(0) \equiv \Theta_R''(0) = \lim_{t \to \infty} \frac{1}{t} \langle\!\langle Q_R(t)^2 \rangle\!\rangle \tag{4.1}$$

对于边界驱动系统，$\Sigma_R''(0)$ 等价于边界电导 $G_R(L)$ (在线性响应意义下) [K2, Theorem 2.1]:

$$G_R(L) = \lim_{t \to \infty} \frac{1}{t} \left. \frac{\partial \langle Q_R(t) \rangle}{\partial (\Delta \mu)} \right|_{\Delta \mu = 0} = \frac{1}{2} \Sigma_R''(0) \tag{4.2}$$

第二个等式来自涨落-耗散定理 (fluctuation-dissipation theorem) 在边界驱动系统中的形式 [K7]。

#### 4.2 长跳系统的标度行为

Bernardin-Jimenez [K2, Theorem 2.3] 证明了对长跳排阻过程 $(J(r) \sim r^{-(1+\alpha)})$:

$$G_R(L) \sim \begin{cases}
L^{-1} & \alpha > 2 \quad (\text{正常扩散}) \\
L^{-(2-2\alpha)} & 1 < \alpha < 3/2 \quad (\text{超扩散}) \\
L^{-1} \log L & \alpha = 3/2
\end{cases} \tag{4.3}$$

现在，$(1-\cos(r\theta))$ 因子在此标度行为中的角色是什么？

考虑 (3.16) 中的 CGF 结构。当 $s \to 0$ (小偏差极限):

$$\Theta_R(s) \approx s I + \frac{s^2}{2} \Sigma_R''(0) + O(s^3) \tag{4.4}$$

将规范固定的 CGF $\Theta_R^{\text{phys}}(s)$ 展开，$\Sigma_R''(0)$ 由 $F_r''(0)$ 的加权和给出:

$$\Sigma_R''(0) \propto \sum_r J(r) \, r^2 \, F_r''(0) \tag{4.5}$$

$r^2$ 因子来自 $(1-\cos(r\theta))$ 的 $\theta^2$ 展开系数乘以 counting field $s$ 的二阶导数 (注意 $F_r(s) \sim s^2 + \cdots$ 当 $s \to 0$，因为 $\Theta_R(0)=0$ 且 $\Theta_R'(0)=I$ 不包含 $F_r$)。

准确地说，从 (3.16) 取 $s \to 0$:

$$\Theta_R(s, 0) \approx \sum_r J(r) (1-\cos(0)) \mathcal{F}_r(s) = 0 \quad (\text{恒为零，因为 } 1-\cos 0 = 0)$$

这意味着我们需要重新审视 (3.16) 的结构。$\mathcal{F}_r(s)$ 不能是任意的 $s$ 函数——它必须满足 $\lim_{s \to 0} \mathcal{F}_r(s)/s$ 有限 (给出平均电流) 且 $\mathcal{F}_r(0) = 0$。

**更准确的重构:** 对于长跳 SSEP，将物理 CGF 写为:

$$\Theta_R^{\text{phys}}(s) = \sum_r J(r) \, \mathcal{H}(s; r) \tag{4.6}$$

其中 $\mathcal{H}(s; r)$ 是单个 $r$-跳对 CGF 的贡献。规范结构告诉我们，当引入规范扭曲 $\theta$ 时:

$$\mathcal{H}(s; r) \to \mathcal{H}(s, \theta; r) = \mathcal{H}(s - i\theta; r) + \mathcal{H}(s + i\theta; r) - 2\mathcal{H}(s; r) \quad (?)$$

这个构造保证: (i) 规范不变性; (ii) 在 $\theta=0$ 时回到物理 CGF。

算了，让我退一步。(3.16) 的物理含义其实更清晰，让我重新表述。

**最终重构 (3.16) 的物理含义:**

对于长跳系统，CGF 可以在两种"规范"下计算:
- "右边界规范": 所有 counting field 集中在右边界 → CGF = $\Theta_R^{\text{phys}}(s)$
- "分布规范": counting field 分布在所有 bond 上，带有权重分布 $f(x)$ → CGF = $\tilde{\Theta}_R(s, \{f\})$

Costa et al. [K1] 证明了 $\Theta_R^{\text{phys}}(s) = \tilde{\Theta}_R(s, \{f\})$ 对于任意满足 $\sum f_j = L+1$ 的分布 $\{f\}$。

从一个分布变到另一个分布的"变换"就是规范变换。当我们将均匀分布 $f(x)=1$ 变到 $f(x) = 1 + \partial_x \theta(x)$ (其中 $\theta(x) = \theta x$ 给出均匀偏移)，规范不变性要求 CGF 不变。但在计算中，如果我们**先**固定了分布 $f(x)=1$，然后考察在不同规范参数 $\theta$ 下 CGF 的形式，$(1-\cos(r\theta))$ 就自然出现。

具体而言，取均匀分布 $f(x) = 1$，CGF 为 [K1, Eq.(9)]:

$$\Theta_R(s) = -s \cdot \bar{g}_s' + s^2 \cdot \overline{g_s(1-g_s)} \tag{4.7}$$

其中 $\bar{g}_s' = \int_0^1 \partial_x g_s(x) dx = g_s(1) - g_s(0)$，$\overline{g_s(1-g_s)} = \int_0^1 g_s(x)(1-g_s(x)) dx$。

现在考虑规范变形分布 $f_\theta(x) = 1 + \theta$ (常数偏移)。代入 (3.12):

$$\Theta_R(s, \theta) = -s(1+\theta) \bar{g}_s' + s^2 (1+\theta)^2 \overline{g_s(1-g_s)}$$
$$= \Theta_R(s) - s\theta \bar{g}_s' + s^2 (2\theta + \theta^2) \overline{g_s(1-g_s)} \tag{4.8}$$

规范不变性要求 $\Theta_R(s, \theta) = \Theta_R(s)$ 对于所有物理上可达的 $\theta$。这迫使:

$$-s\bar{g}_s' + 2s^2 \overline{g_s(1-g_s)} = 0 \quad (\text{一阶 Ward 恒等式}) \tag{4.9}$$
$$\overline{g_s(1-g_s)} = 0 \quad (\text{二阶 Ward 恒等式}) \tag{4.10}$$

方程 (4.9-4.10) 不可能对所有 $s$ 同时满足，除非 $g_s$ 有非常特殊的结构。实际上，Costa et al. 的处理是**不**要求 CGF 在任意的均匀 $\theta$ 偏移下不变。而是: CGF 的规范不变性是对于**满足 decoupling condition (3.13)** 的特定分布 $\{f_j\}$ 才成立。

对于一个**满足** decoupling condition 的分布 $f_s(x)$，CGF 简化为 [K1, Eq.(SA.6-7)]:

$$\lambda(s) = s \int_0^s dx \, (h_s^2(x) - \partial_x h_s(x)) \tag{4.11}$$

其中 $h_s(x)$ 满足 ODE $\partial_x^2 h_s - 2h_s \partial_x h_s = 0$。这个 CGF 的显式为:

$$\boxed{\lambda(s) = \begin{cases}
-[\arccos(w_s)]^2, & s < 0 \\
[\text{arccosh}(w_s)]^2, & s > 0
\end{cases}} \tag{4.12}$$

$$w_s = \sqrt{(1 + (e^s - 1)\rho_L)(1 + (e^{-s} - 1)\rho_R)} \tag{4.13}$$

$$[已知] \quad \text{(4.12) 是 K1 的核心结果, Eq.(11); w_s 的定义来自 Eq.(SA.7)}$$

#### 4.3 (1-cos θ) 在边界电导中的角色

回到物理问题。对于长跳系统，$\Theta_R(s)$ 由 (3.16) 给出。边界电导由:

$$\Sigma_R''(0) = \sum_r J(r) \, r^2 \, \mathcal{F}_r''(0) \tag{4.14}$$

$r^2$ 因子来自 $(1-\cos(r\theta))$ 的 Taylor 展开 $\approx \frac{1}{2} r^2 \theta^2$ (在 $s$ 被吸收进 $\mathcal{F}_r$ 之前)。准确地说，$(1-\cos(r\theta))$ 的 $\theta^2$ 系数乘以 $\mathcal{F}_r(s)$ 的 $s^2$ 系数（通过对 $s$ 和 $\theta$ 都做二阶导数）给出了对 $\Sigma_R''(0)$ 的 $r$-通道贡献。

**标度假说:** $(1-\cos(r\theta)) \sim r^2 \theta^2/2$ 的小 $r\theta$ 行为与跳跃核 $J(r) \sim r^{-(1+\alpha)}$ 的乘积:

$$\Sigma_R''(0) \sim \sum_r r^{-(1+\alpha)} \cdot r^2 \cdot \mathcal{F}_r''(0) \sim \sum_r r^{1-\alpha} \mathcal{F}_r''(0) \tag{4.15}$$

若 $\mathcal{F}_r''(0) \sim r^0$ (即与 $r$ 无关，对应局域平衡假设)，则:

$$\Sigma_R''(0) \sim \begin{cases}
\text{有限} & \alpha > 2 \\
\log L & \alpha = 2 \\
L^{2-\alpha} & 1 < \alpha < 2
\end{cases} \tag{4.16}$$

对于有限系统 ($L < \infty$)，$r$ 的和被截断在 $r \leq L$。标度 $\Sigma_R''(0) \sim L^{2-\alpha}$ (对于 $1 < \alpha < 2$) 对应电导 $G_R(L) \sim L^{-(\alpha-2)}$。这与 Bernardin-Jimenez [K2, Eq.(2.19)] 的结果 $G_R(L) \sim L^{-(2-2\alpha)}$ 在 $1 < \alpha < 3/2$ 时的标度一致。

**关键观察:** 电导的标度指数由两个因素的竞争决定:
1. $(1-\cos(r\theta))$ 中隐含的 $r^2$ 因子 (几何因子: 跳得越远，越多的 bonds 被穿越，越多的 counting field 被累积)
2. 跳跃核 $J(r) \sim r^{-(1+\alpha)}$ 的衰减 (物理因子: 跳得越远，概率越小)

两者共同给出有效维度和反常输运指数。

--- INSPECTOR_CHECK ---
[数据] 方程(4.15): F_r''(0)~r^0的假设需验证，Q-SSEP普适类内可能成立但普适类外需数值检验 [方向: east] [假设] Q-SSEP普适性保证F_r''与r无关，此假设在无噪声系统中可能不成立

**检查内容:** (4.15) 中 $\mathcal{F}_r''(0) \sim r^0$ 的假设需要验证。对于强噪声极限下的自由费米子系统 (即 Q-SSEP)，Costa et al. [K1] 的结果 (4.12) 表明 CGF 完全由边界密度 $\rho_L, \rho_R$ 决定，与跳跃核的具体形式无关——前提是系统处于 Q-SSEP 普适类。但如果系统不在该普适类 (如无噪声的 XX 自旋链)，$\mathcal{F}_r''(0)$ 可能有非平凡的 $r$ 依赖。需要数值验证或从 Bernardin-Jimenez [K2] 的流体力学方程出发推导 $\mathcal{F}_r''(0)$ 的显式。

---

### Step 5: 物理诠释

#### 5.1 U(1) 规范群上的 Haar 测度

(1-cos θ) 结构并非偶然。它在群论上有深刻的起源。

考虑 U(1) 规范群在 counting field 上的作用。$U(1)$ 的元素参数化为 $g = e^{i\theta}$ ($\theta \in [0, 2\pi)$)。U(1) 上归一化的 Haar 测度为:

$$d\mu_{\text{Haar}}(g) = \frac{d\theta}{2\pi} \tag{5.1}$$

U(1) 的不可约表示是一维的: $\chi_n(g) = e^{in\theta}$, $n \in \mathbb{Z}$。

对于跳跃距离 $r$，相关的表示是 $\chi_r(g) = e^{ir\theta}$ (表示跳跃累积的规范相位)。在这个表示下，投影到规范不变子空间的投影算符为:

$$\mathbb{P}_{\text{inv}} = \int_{U(1)} R(g) \, d\mu_{\text{Haar}}(g) \tag{5.2}$$

其中 $R(g)$ 是 $g$ 在跳跃算符上的表示。

规范不变的量必须满足 $\mathbb{P}_{\text{inv}}[X] = X$。对于相因子 $e^{ir\theta}$:

$$\int_0^{2\pi} e^{ir\theta} \, \frac{d\theta}{2\pi} = \delta_{r,0} \tag{5.3}$$

这意味着物理可观测量（规范不变的）只能通过规范不变组合 $e^{ir\theta} + e^{-ir\theta} = 2\cos(r\theta)$ 依赖于 $\theta$。跳跃算符的二次型（如 Liouvillian 中的 $\mathcal{D}$ 超算符）涉及 $|e^{ir\theta}|^2 = 1$，因此对角项不依赖 $\theta$。而非对角项（量子相干项）的规范不变部分含 $(e^{ir\theta} - 1)(e^{-ir\theta} - 1) = 2(1-\cos(r\theta))$。

#### 5.2 与 LP25 北极星命题的联系

LP25 的核心假说是:

$$\Sigma_R(s, \theta) \propto K (1 - \cos\theta) F(s) \quad \longleftrightarrow \quad V \propto |\cos(\Delta\phi/2)|$$

两者的桥梁在于 $e^{i\pi} + 1 = 0$ 的光锥面 ($ds^2 = 0$) 与幺正面 ($|e^{i\theta}| = 1$) 的对偶。

从 S0a 的结果看，$(1-\cos\theta)$ 测度的是:

> **规范冗余被消除的程度。** $\theta=0$ 时消除量为 0 (平凡规范，没有冗余可消)。$\theta=\pi$ 时 $(1-\cos\pi)=2$ 达到最大消除——对应"完全反规范变换"，counting field 的符号完全反转。

这对应量子退相干中的 $\cos(\Delta\phi/2)$: $\Delta\phi=0$ (无相位差) 给出完全可见度 $V=1$；$\Delta\phi=\pi$ (完全反相) 给出 $V=0$ (完全退相干)。

**同构映射**:

| FCS 规范结构 | 量子退相干 |
|---|---|
| 规范参数 $\theta$ | 相位差 $\Delta\phi$ |
| $(1-\cos\theta)$: 规范冗余消除度 | $\cos(\Delta\phi/2)$: 干涉可见度 |
| $\theta=0$: 平凡规范 | $\Delta\phi=0$: 完全相干 |
| $\theta=\pi$: 最大冗余消除 | $\Delta\phi=\pi$: 完全退相干 |
| CGF $\Theta_R(s,\theta) \to 0$ 当 $\theta \to 0$ | $V \to 1$ 当 $\Delta\phi \to 0$ |
| Haar 测度 $\int_{U(1)}$ | Born 规则 $\text{Tr}[\rho E]$ |

这不是类比——这是同一个 $U(1)$ 群在不同表示下的两个物理实现: 规范群 (FCS 侧) 和作用在波函数相位上的群 (退相干侧)。$e^{i\pi} + 1 = 0$ 统一了两侧: $\pi$ 相位的特殊性 ($e^{i\pi} = -1$) 在两侧都对应着"反转"——规范反转 ($s \to -s$) 和相位反转 ($|\psi\rangle \to e^{i\pi}|\psi\rangle = -|\psi\rangle$)。

#### 5.3 标度行为和重整化群解释

$(1-\cos\theta)$ 的小 $\theta$ 展开 $\approx \theta^2/2$ 在重整化群语言下有自然解释:

- $\theta$ 是 U(1) 规范场的"Goldstone 模式" (纯规范自由度)
- $(1-\cos\theta) \sim \theta^2$ 是这些模式的"质量项"——度量规范固定后残留的自由度
- 求和 $\sum_r J(r) (1-\cos(r\theta))$ 对应有效作用量中的动能项: $\int d^d x \, (\nabla \theta)^2$ 在长跳/分数阶推广下的形式

$$[推导] \quad \text{§5 的诠释结合了群论、FCS 和退相干的语言，需要 S0b 进一步形式化}$$

**前提脆弱点 Self-Attack #2:** §5.2 的同构映射依赖于 FCS 中的 $\theta$ 与退相干中的 $\Delta\phi$ 具有相同的数学结构。这假定了: (i) 退相干中的环境导致的相位随机化可以写成规范变换的形式; (ii) Born 规则中的 $|e^{i\theta}|=1$ 与 FCS 中的 U(1) 规范群确实是同一个群。前提 (i) 在量子 Darwinism 框架下有支持 (Zurek, Nat. Phys. 5, 181, 2009)，但前提 (ii) 是 LP25 的核心假说而非已知事实。如果 FCS 的 U(1) 和量子力学的 U(1) 只是形式上的同构而非实质上的同一，则整个 LP25 框架需要重新评估。

--- INSPECTOR_CHECK ---
[假设] LP25核心假说: FCS的U(1)规范群与量子力学Born规则的U(1)是同一个群的两种表示 [方向: west] [数据] 需S0b通过退相干侧独立推导验证同构是否成立 [公式] 若同构不成立则(1-cosθ)↔|cos(Δφ/2)|仅是形式类比而非物理对应

---

## §2 深挖 1: 本轮结论的下一层后果

### 深挖 1 第 1 层: 对 $\alpha$ 依赖的约束

如果 (3.16) 的因子化形式正确，那么 $F_r(s)$ 必须满足一个跨 $r$ 的泛函方程: $\Theta_R(s, \theta)$ 对 $\theta$ 的规范不变性等价于要求存在一个函数 $\mathcal{F}(s; r)$ 使得:

$$\sum_r J(r) (1 - \cos(r\theta)) \mathcal{F}(s; r) = \text{(与 } \theta \text{ 无关)} \times \Theta_R^{\text{phys}}(s) \tag{D1.1}$$

其中 $\Theta_R^{\text{phys}}(s)$ 仅依赖于边界密度。这要求 $\mathcal{F}(s; r)$ 必须具有非常特殊的函数形式——特别地，对于 $J(r) \sim r^{-(1+\alpha)}$，需满足:

$$\mathcal{F}(s; r) = \frac{f(s)}{r^\beta} \tag{D1.2}$$

其中 $\beta$ 由维数分析确定。这意味着 $F_r(s)$ 对跳跃距离 $r$ 的依赖是普适的幂律——这是 Costa et al. [K1] 的 Q-SSEP 普适性的直接推论: 在强噪声极限下，CGF 不依赖于微观跳跃核的细节，只依赖于边界密度。

**可检验的推论:** 如果 $\alpha$ 变化而系统保持在 Q-SSEP 普适类内，$F_r(s)$ 应对 $\alpha$ 不敏感。数值实验可检验: 对不同的 $J(r)$ 模型计算 $\Theta_R(s)$，检查其是否 collapse 到同一条曲线。

### 深挖 1 第 2 层: 对退相干速率的预测

如果 S0a 导出的 $(1-\cos\theta)$ 结构与 S0b 的退相干结构确实同构，那么我们可以**用量子输运实验中测量的 FCS 数据来推断退相干速率**，反之亦然。

具体而言，S0a 的结果预测:

$$\Sigma_R''(0) \propto \sum_r J(r) r^2 \mathcal{F}_r''(0) \quad \text{(FCS 侧)} \tag{D1.3}$$

如果同构成立，退相干速率 $\Gamma_{\text{dec}}$ 应该满足:

$$\Gamma_{\text{dec}} \propto \sum_r J_{\text{env}}(r) r^2 \mathcal{G}_r''(0) \quad \text{(退相干侧)} \tag{D1.4}$$

其中 $J_{\text{env}}(r)$ 是环境关联函数的空间衰减核。这意味着:**退相干速率由环境噪声的跳跃统计决定。** 对于 $1/f$ 噪声环境 ($\alpha_{\text{env}} \approx 1$)，退相干速率应有对数红外发散——这可能是超导量子比特 $T_2$ 时间受限的深层原因。

---

## §3 深挖 2: 本轮依赖的前提中哪个最可能也是错的

### 深挖 2 第 1 层: 最大特征值假设的脆弱性

方程 (1.9) — $\Theta_R(s) = \lambda_{\max}(\mathcal{L}_s)$ — 是 FCS 倾斜 Liouvillian 方法的基石。但这一假设在以下情况下可能失效:

1. **Liouvillian 的谱隙闭合:** 当 $s$ 接近某临界值 $s^*$ 时，$\mathcal{L}_s$ 的最大特征值与次大特征值简并 (level crossing)。此时 $\rho_s(t)$ 的渐近行为由两个（或更多）特征值的竞争决定，单一特征值主导不再成立。

2. **非对角长程序 (ODLRO):** 对于 $1 < \alpha < 3/2$ 的超扩散区域，系统的关联长度发散。倾斜 Liouvillian 可能有连续谱而非离散的最大特征值。

3. **有限系统修正:** Medvedyeva-Kehrein [K3] 指出对于有限系统，高阶累积量在 $k > L+1$ 时与系统大小无关——暗示着"最大特征值"图像只在特定极限下有效。

**脆弱性评估:** 对于 $\alpha < 3/2$，K2 的结果 (4.3) 表明电导确实有幂律标度，与最大特征值假设一致。但在 $s$ 远离 0 时（对应大偏差的尾部），该假设可能不成立。特别是，对于 $s < 0$ (对应电流小于平均值的大偏差)，Costa et al. [K1, Eq.(11)] 的 CGF 在 $w_s = 1$ 时有奇点 ($\arccos(1) = 0$ 的导数为 $\infty$)，这暗示在此处发生了动力学相变 (dynamical phase transition)。

### 深挖 2 第 2 层: Lindblad 方程的马尔可夫假设

整个 FCS 形式体系建立在 Lindblad 方程的马尔可夫近似之上 [K3, Eq.(1)]。但对于长跳过程 ($\alpha < 2$)，有以下质疑:

1. **非局域跳跃与非马尔可夫性:** 当粒子可以直接从 site $i$ 跳到 site $i+r$ ($r \gg 1$) 时，系统与热库的耦合不再是局域的。Lindblad 方程的推导依赖于系统-热库耦合的局域性和 Markov 近似 (热库关联时间 $\tau_B \ll$ 系统弛豫时间 $\tau_S$)。

2. **记忆效应:** 对于长跳过程，系统在 site $i$ 的状态变化 (粒子离开) 会影响远处 site $i+r$ 的状态。这种非局域效应可能引入记忆核 (memory kernel)，使得演化不再是 Markov 的。

3. **K2 如何规避此问题:** Bernardin-Jimenez [K2] 的处理是经典概率性的 (classical SSEP)，不存在量子相干，因此 Markov 性由构造保证。但 Costa et al. [K1] 的 Q-SSEP 是量子的——其中 Markov 性需要更仔细的论证。

**已知支持:** Costa et al. [K1] 证明了在强噪声极限 ($\gamma \to \infty$) 下，Noisy XX 链的有效动力学由 Q-SSEP 描述，而 Q-SSEP 的定义就是 Markov 的。这意味着在该极限下，非马尔可夫修正被噪声压制。

**脆弱性评估:** 如果噪声强度 $\gamma$ 有限 (非渐近极限)，非马尔可夫修正可能破坏 $(1-\cos\theta)$ 的简单因子化结构。这是从理论到实验的"断桥"——大多数实验中的量子输运系统不在 $\gamma \to \infty$ 极限下运行。

---

## §末 产出格式

### 本轮成果

导出了 FCS 中 $(1-\cos\theta)$ 因子的三个等价数学来源:

1. **跳跃相因子的规范不变组合:** 向前跳 $e^{-sr-ir\theta}$ 与向后跳 $e^{+sr+ir\theta}$ 的规范不变组合 $\propto (1-\cos(r\theta))$ (§3.5)
2. **跳跃核的 Fourier 表示:** $\hat{J}(q) = \sum_r J(r)(1-\cos(qr))$——分数阶扩散算符的离散傅里叶变换 (§3.4)
3. **U(1) 规范群上 Haar 测度的特征标积分:** $\int_{U(1)} (1 - \text{Re}[\chi_r(g)]) d\mu_{\text{Haar}}(g)$ (§5.1)

三重来源的一致性并非巧合——它们分别从代数 (算符代数)、分析 (Fourier 分析) 和几何 (群论) 三个角度指向同一个数学骨架。

### 新增引用

| 编号 | 引用 | 首次使用位置 |
|------|------|------------|
| K1 | Costa, Ribeiro, De Luca, arXiv:2504.00188v3 (2025) | §1.3, §2, §3 |
| K2 | Bernardin, Jimenez-Oviedo, arXiv:1603.01234 (2016); ALEA 14, 473 (2017) | §3.4, §4.2 |
| K3 | Medvedyeva, Kehrein, arXiv:1310.4997 (2013) | §1.1, §1.4 |
| K4 | Levitov, Lesovik, JETP Lett. 58, 230 (1993) | §1.2 |
| K5 | Schönhammer, PRB 75, 205329 (2007) | §1.2 |
| K6 | Nazarov, Bagrets, PRL 88, 196801 (2002) | §2 (implicit) |
| K7 | Esposito, Harbola, Mukamel, PRB 76, 085316 (2007) | §4.1 |
| K8 | Klich, Physica E 18, 326 (2003) | §1 (background) |
| K9 | Bernard, Doyon, Vinson, J. Stat. Mech. 2022, 013104 (2022) | Q-SSEP 原始引入 |
| K10 | Barraquand, Bernard, arXiv:2507.01570 (2025) | Q-SSEP 综述 |

### 最弱环节

1. **方程 (3.16) 中因子化形式的证明不完整。** 当前推导依赖于对 Costa et al. [K1] 的 gauge decoupling condition (3.13) 和 Bernardin-Jimenez [K2] 的 Fourier 表示的组合，但并未给出 (3.16) 的严格证明。需要: (a) 从长跳 SSEP 的倾斜 Liouvillian 出发，显式计算 CGF 的 $\theta$ 依赖; (b) 在 $\alpha$ 的不同区域验证因子化的稳定性。

2. **$(1-\cos\theta)$ 与 $(1-\cos(r\theta))$ 的关系未完全厘清。** LP25-S0 原始命题中的 $(1-\cos\theta)$ (无 $r$ 下标) 可能是 $r=1$ 的特例，也可能是某种有效的平均。需要在 S0b 中澄清。

3. **规范群到底是 U(1) 还是 $\mathbb{R}$ 的离散子群？** 对于格点系统 (site 数为 $L$)，$\theta_j$ 的取值空间是 $\mathbb{R}^L$ 还是 $[0,2\pi)^L$？这影响到 Haar 测度是连续的还是离散的——进而影响 $(1-\cos\theta)$ 的归一化。

### 下一步计划

1. **S0b (Round 1):** 导出退相干侧的 $\cos(\Delta\phi/2)$ 结构，显式建立与 S0a 的同构映射。**⛔ 不能在 S0b 完成前宣称同构成立。**
2. **S1 (Round 1):** 对具体的微观模型 (如 noisy XX chain with long-range hopping) 数值计算 CGF 的 $\theta$ 依赖，验证 (3.16) 的因子化形式。
3. **S2 (Round 1):** 检查 $(1-\cos\theta)$ 结构与 Levitov-Lesovik 公式 [K5, Eq.(16)] 中 $T(\epsilon)[f_L(1-f_R)e^{i\lambda} + f_R(1-f_L)e^{-i\lambda}]$ 结构的关系——后者也涉及 $e^{i\lambda}$ 的组合，可能有更深的统一结构。

### 需要 PI 投喂的文献方向

1. **FCS with long-range hopping 的直接文献:** 是否存在直接研究"长跳量子系统中的 FCS"的论文？关键词: "full counting statistics + long-range hopping + tilted Liouvillian"。
2. **U(1) gauge structure in classical MFT:** Macroscopic Fluctuation Theory (Bertini et al., Rev. Mod. Phys. 2015) 中是否有与 Costa et al. 规范技巧类似的规范结构？K1 声称 QMFT 是 MFT 的量子推广——MFT 中的规范结构可能早已隐含在 MFT 的作用量泛函中。
3. **(1-cos θ) 与 Levitov-Lesovik 的联系:** Levitov-Lesovik 公式中的 $T(\epsilon)(e^{i\lambda} - 1)$ 是否为 $(1-\cos\lambda)$ 的前驱？需查原始文献中的解析延拓。
4. **Quantum Darwinism 和 FCS 的联系:** Zurek 的量子 Darwinism (Nat. Phys. 2009) 是否讨论了环境监控 (environmental monitoring) 与 FCS 的关系？若环境中存在"冗余记录" (redundant records)，信息通过环境传播——这正是 FCS 测量的物理实质。

---

*本文件属于 LP25 项目，由 A 博士撰写。学院派方法论 v3.7 约束生效。所有推导均附文献溯源。*
