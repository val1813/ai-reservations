# LP10-S2 Phase 2 — 仲裁报告（电流顶点修正对几何超流权重的几何部分是否为零）

> **仲裁者**：独立冷启动凝聚态理论仲裁者，零项目立场，不预设 A/B 任何一方正确。
> **被裁决矛盾**：单点 DMFT（动量无关局域自能 Σ(iω)）计算超流权重 D_s 时，电流顶点修正对**几何部分**（带间/inter-sublattice 相干）是否为零。
> **A 主张**：Khurana 定理 ⇒ 顶点修正零 ⇒ 几何住裸顶点 ∂h(k) ⇒ DMFT 不漏几何 ⇒ 朴素 B2 证否。
> **B 主张**：Khurana 只覆盖单带/纵向(intraband)，几何本质是带间(interband)横向矩阵元 ⇒ 顶点修正 O(1) 非零 ⇒ DMFT 的 D_s^geom 与平均场 BdG 范畴错配。

---

## §0 仲裁结论（先读）

**裁决：三选一中的「(C) 都不全对 —— 部分」，但边界是精确的、可证的，且不是模糊折中。**

核心判据（本仲裁的可证核心，见 §3）：
> 单点 DMFT 中几何（带间）电流顶点修正是否为零，**不**由「单带 vs 多带」或「纵向 vs 横向」决定（B 的二分法过粗），也**不**由「Δ_α 是否均匀」决定（A 的主轴不充分），而是由一个精确的**宇称-轨道判据**决定：
>
> **几何顶点修正 = 0 ⟺ 轨道对角的电流-电流极化 Π^μ_{αα}(iν) 在 k→−k 下为奇 ⟺ 反演(或 C₂)在轨道基下的表示 U_P 为对角（轨道坐落于反演对称 Wyckoff 中心、反演不置换子格）。**
>
> 当 U_P 非对角（子格被反演置换 / 轨道不在反演中心 / 能带带 Wannier 阻碍 obstruction）时，Khurana 的宇称论证**不被强制**，局域顶点修正对几何部分**一般为 O(1) 非零**（平带无 W/U 小参数，B 的量级估计在此正确）。

由此：

| 情形 | 裁决 | 谁对 |
|------|------|------|
| **U_P 对角**（轨道在反演中心，反演不置换子格）+ 轨道对角配对 | 几何顶点修正**被宇称强制为零**，Khurana **可推广到 interband** | **A 对** |
| **U_P 非对角**（子格被反演置换 / 轨道偏离反演中心）或带 Wannier 阻碍(C≠0 拓扑) | 几何顶点修正**一般 O(1) 非零**，DMFT 的 D_s^geom 系统性偏离平均场 BdG | **B 对** |

**对 S2 收官的直接含义**：A 的「Khurana 零顶点修正」支柱在 **C=0 / Wannier 可定域 / 轨道在反演中心** 的模型（纯 Lieb 在角点反演下、轨道对角配对）成立；但在 **C≠0 拓扑平带**（正是 S1 下界 π|C| 非平凡、本课题真正关心的扇区），宇称论证一般**失效**，B 的 O(1) 偏离风险**有实质牙齿**。因此 A 在步4把「Khurana 定理」当作无条件支柱是**越界引用**；精炼 B2「DMFT 用裸度规、漏 O(1) 顶点修正」在拓扑扇区**成立**。

**诚实声明**：本判据的「可证核心」（宇称-轨道分析，§3）是严格的。但其最尖锐推论——「C≠0 拓扑能带必然导致 O(1) 修正」——依赖「DMFT 缺失的顶点修正 ≡ GRPA 的 D_{s,g}^{(1)} 轨道嵌入修正」这一**等同**，该等同在文献中**未被显式证明于单点 DMFT 框架**（GRPA 是平均场上的高斯涨落，非 DMFT）。故该推论**标记为半开放问题**，列入 §6 PI 核实项。这恰好可成为 S2 的合法增量，但不能当成已证结论收官。

---

## §1 文献查证（WebSearch, US-only, 2026-06；真实 arXiv 已核，存疑标「需PI核实」）

| 编号 | 文献 / 出处 | 与裁决的关系 | 核实状态 |
|------|------------|-------------|---------|
| K1 | A. Khurana, *Electrical conductivity in the infinite-dimension Hubbard model*, **PRL 64, 1990 (1990)** | 顶点修正零的原始定理 | ✅真实（PRL 64, 1990，年份与卷期一致；多篇综述引用） |
| K2 | Vučičević, Kokalj, Žitko et al., *Conductivity in the square-lattice Hubbard at high T* (**arXiv:1811.08343**) | 明确写出 Khurana 宇称论证：**全顶点 F 失 k 依赖 + 电流顶点 v_{−k}=−v_k 奇** ⇒ 抵消；并强调**仅单带、纵向、q=0 intraband**，2D 有限维顶点修正不为零 | ✅真实，已读全文确认宇称论证与适用范围 |
| K3 | Freericks/Zlatić 类多层 DMFT，*Vertex corrections on longitudinal transport through multilayers* (**arXiv:1009.5299**) | **直接证据**：多层(等效轨道/层指标)几何下，「momentum 不再是好量子数沿 z，**宇称论证不再成立**，纵向顶点修正非零」；面内仍抵消 | ✅真实，已读全文确认「宇称破坏⇒顶点修正复活」机制 |
| G1 | (multiorbital SC 内禀光电导) *Probing quantum geometry of paired electrons through intrinsic optical conductivity* (**arXiv:2106.00037**, PRB) | 几何贡献来自**非对角速度** V^{mn}_μ=(ε_m−ε_n)⟨m|∂_μ|n⟩ = **非阿贝尔 Berry 联络** = 量子几何张量；确证「几何住 interband 矩阵元」 | ✅真实，Eq.2/3 已核 |
| G2 | (GRPA 孤立带超流权重) *Superfluid weight in the isolated band limit within GRPA* (**arXiv:2308.10780**) | **超平均场**几何修正 D_{s,g}^{(1)}：一般 O(1)，**可经选取「自然/优选轨道位置」置零**；平带极限量子度规关系在 GRPA 下仍成立 | ✅真实（摘要级已核；公式细节需全文，标注） |
| G3 | Huhtinen, Herzog-Arbeitman, Törmä, Peotta, *minimal quantum metric / dependence on band touchings* (**arXiv:2203.11133**) | 几何 D_s 依赖**轨道位置**；物理 D_s 用真实轨道位置的度规，最小度规给下界 ∫g̃≥π|C| | ✅真实 |
| G4 | Herzog-Arbeitman, Peri, Schindler, Huber, Bernevig/Törmä, *Superfluid weight bounds from symmetry & quantum geometry* (**arXiv:2110.14663**) | 对称强制下界；Wannier 阻碍带的几何不可定域 | ✅真实 |
| T1 | Wang & Zhang, *Simplified topological invariants for interacting insulators*, PRX 2 (2012) ＋ 拓扑哈密顿量 h_t=−G⁻¹(0,k) | 关联拓扑荷 = h_t Chern；G-零点处跳变 | ⚠️ arXiv 号需PI核实（PRX 2,031008 = 1201.6431；「topological Hamiltonian」单独文 = 1207.7341，二者别混） |
| T2 | Volovik 动量空间拓扑 N₃=∫tr(G∂G⁻¹)³ | B 的 N₃≠C 轴 | ⚠️ 原始出处需PI核实 |
| P-base | Peotta-Törmä 1506.02815；Liang et al. 1610.01803 | 平均场几何超流权重 D_s^geom∝∫g 原型 | ✅真实 |

**先发判定**：B 的「DMFT 漏 interband 顶点几何」与 GRPA(2308.10780) 的 D_{s,g}^{(1)} 高度同构，**但 G2 是 GRPA（平均场+高斯涨落），非单点 DMFT**；将其搬到 DMFT 是本 S2 的合法增量。Khurana 推广到 interband 的**精确宇称-轨道判据**（§3），文献未见显式整合 → 本仲裁的核心产出。

---

## §2 Kubo 公式与电流顶点结构（裁决的物理基底）

### §2.1 超流权重的 Nambu-Kubo 表达
多轨道吸引 Hubbard，α,β=子格/轨道，Bloch 矩阵 h(k)，最低带为平带。phase-twist 二阶导给出
$$
D_{s,\mu\nu}=\frac{1}{V}\Big[\langle -\hat K_{\mu\nu}\rangle-\Lambda_{\mu\nu}(\mathbf q\!\to\!0,i\nu_m\!=\!0)\Big],
$$
抗磁项 $\hat K_{\mu\nu}=\sum_{\mathbf k}\partial_\mu\partial_\nu h_{\alpha\beta}(\mathbf k)\,c^\dagger_\alpha c_\beta$，顺磁项为流-流关联
$$
\Lambda_{\mu\nu}(\mathbf q,i\nu_m)=\frac1V\int_0^\beta\!d\tau\,e^{i\nu_m\tau}\langle T_\tau j_\mu(\mathbf q,\tau)j_\nu(-\mathbf q,0)\rangle .
$$
**裸**流顶点（Nambu 空间，τ₃ 结构）
$$
\hat j_\mu(\mathbf k)=\partial_\mu h_{\alpha\beta}(\mathbf k)\,\tau_3\ \equiv\ \hat v_\mu(\mathbf k)\,\tau_3,\qquad
\hat v_\mu(\mathbf k)=\partial_\mu \hat h(\mathbf k).
$$

### §2.2 顶点的带基分解：对角(intraband) vs 非对角(interband)
在 h(k) 的本征基（$\mathcal V_{\mathbf k}$ 对角化 h）中速度矩阵
$$
\hat V_\mu(\mathbf k)=\mathcal V_{\mathbf k}^{-1}\,\partial_\mu \hat h(\mathbf k)\,\mathcal V_{\mathbf k},\qquad
V_\mu^{mn}(\mathbf k)=\langle m\mathbf k|\partial_\mu \hat h|n\mathbf k\rangle .
$$
- **对角 m=n**：$V_\mu^{nn}=\partial_\mu\varepsilon_{n}$ = 带群速度（intraband）。**平带 ⇒ V^{FB,FB}_μ=0**。
- **非对角 m≠n**：$V_\mu^{mn}=(\varepsilon_m-\varepsilon_n)\langle m|\partial_\mu|n\rangle$ = **interband 速度** = (能差)×(非阿贝尔 Berry 联络)（G1, arXiv:2106.00037 Eq.3）。量子度规
$$
g_{\mu\nu}(\mathbf k)=\mathrm{Re}\!\!\sum_{n\ne \rm FB}\frac{V_\mu^{\rm FB,n}V_\nu^{n,\rm FB}}{(\varepsilon_{\rm FB}-\varepsilon_n)^2}
=\mathrm{Re}\,\langle\partial_\mu \rm FB|(1-P)|\partial_\nu \rm FB\rangle .
$$
**关键结构事实（A、B 均承认，无争议）**：平带 D_s^geom 完全来自 V^{FB,n≠FB}_μ（off-diagonal velocity），即裸顶点 ∂h(k) 的带间矩阵元。这正是 A「几何住裸顶点」的正确内核，也是 B「几何是带间量」的正确内核。**争议不在裸顶点，而在 Bethe-Salpeter 顶点修正是否改写它。**

### §2.3 重整流顶点的 Bethe-Salpeter 方程
保守(Baym-Kadanoff/Ward 相容)框架下，重整流顶点
$$
\boxed{\;\hat J_\mu(\mathbf k;i\nu)=\hat v_\mu(\mathbf k)\,\tau_3+\frac1N\sum_{\mathbf k'}\Gamma(\mathbf k,\mathbf k';i\nu)\,\big[\hat G(\mathbf k')\hat J_\mu(\mathbf k';i\nu)\hat G(\mathbf k')\big]\;}
$$
顺磁关联 $\Lambda_{\mu\nu}=\frac1N\sum_{\mathbf k}\mathrm{Tr}[\hat v_\mu\tau_3\,\hat G\,\hat J_\nu\,\hat G]$。**顶点修正 = J_μ − v_μτ₃**。在超导态，Γ 含**正常(粒子-空穴)道**与**反常(粒子-粒子/配对)道**；后者携带相位模(Anderson-Bogoliubov/Goldstone)，是规范不变性(Ward 恒等式 $q_\mu\Lambda^{\mu\nu}=0$)所**必须**——这点对下文 §5 很重要。

---

## §3 裁决核心：Khurana 宇称论证对 interband 是否成立（可证部分）

### §3.1 单点 DMFT 的两个定义性事实
1. **自能局域**：$\hat\Sigma_{\alpha\beta}(\mathbf k,i\omega)=\delta_{\alpha\beta}\Sigma_\alpha(i\omega)$（k 无关、**轨道对角**）。
2. **不可约顶点局域**：单点 DMFT 的两粒子不可约顶点 $\Gamma$ **无 k,k′ 依赖**且（对 on-site $U n_{\alpha\uparrow}n_{\alpha\downarrow}$）**轨道对角**：$\Gamma\to\Gamma_\alpha(i\omega,i\omega';i\nu)\,\delta$-在单一轨道 α 上。（d→∞ 标准结果；K1/K2）

### §3.2 顶点修正的轨道-动量结构
把 §2.3 的修正项代入 Λ。因 Γ 局域且轨道对角，k′ 求和与 k 求和经 Γ_α **解耦**，顶点修正写成「极化泡 × 局域顶点 × 极化泡」：
$$
\delta\Lambda_{\mu\nu}\ \propto\ \sum_{\alpha}\ \Pi^{\mu}_{\alpha}(i\nu)\;\Gamma_\alpha(i\nu)\;\Pi^{\nu}_{\alpha}(i\nu),\qquad
\boxed{\;\Pi^{\mu}_{\alpha}(i\nu)\equiv\frac1N\sum_{\mathbf k}\big[\hat G(\mathbf k)\,\hat v_\mu(\mathbf k)\tau_3\,\hat G(\mathbf k)\big]_{\alpha\alpha}\;}
$$
（外 Tr 与一条腿亦取 αα，因 Γ_α 两端均钉在轨道 α。）**裁决归结为一个量：轨道对角的电流极化 $\Pi^{\mu}_{\alpha}$ 是否为零。**

> **这正是 Khurana 论证的真正内容**：单带情形 $\Pi^\mu=\sum_k v_\mu(k)G(k)^2$，$v_\mu=\partial_\mu\varepsilon_k$ 奇、$G$ 偶 ⇒ $\Pi^\mu=0$。B 说「Khurana 只覆盖 intraband」**字面对**（K1/K2 确只证单带纵向），但**机制层面**真正的判据是 $\Pi^\mu_\alpha$ 的宇称，而非「带内/带间」标签。下面把宇称论证**严格推广到多轨道**，给出精确成立/失效边界。

### §3.3 多轨道宇称定理（本仲裁的可证核心）
设系统有反演(或 C₂) 对称 $\mathcal P$，轨道表示 $U_P$：$\hat h(-\mathbf k)=U_P^\dagger \hat h(\mathbf k)U_P$。则
$$
\hat v_\mu(-\mathbf k)=-\,U_P^\dagger \hat v_\mu(\mathbf k)U_P,\qquad
\hat G(-\mathbf k)=U_P^\dagger \hat G(\mathbf k)U_P
$$
（后者要求局域 Σ 守对称，DMFT 自洽自动满足）。于是
$$
\big[\hat G\hat v_\mu\tau_3\hat G\big](-\mathbf k)=-\,U_P^\dagger\big[\hat G\hat v_\mu\tau_3\hat G\big](\mathbf k)\,U_P .
$$
对 k 求和并用 −k↔k 改标：
$$
\Pi^\mu_\alpha=-\frac1N\sum_{\mathbf k}\big[U_P^\dagger\,\hat M_\mu(\mathbf k)\,U_P\big]_{\alpha\alpha},
\qquad \hat M_\mu\equiv \hat G\hat v_\mu\tau_3\hat G .
$$

**情形 A（U_P 对角）**：轨道坐落于反演对称 Wyckoff 中心、反演不置换子格 ⇒ $U_P=\mathrm{diag}(e^{i\phi_\alpha})$ ⇒ $[U_P^\dagger \hat M_\mu U_P]_{\alpha\alpha}=[\hat M_\mu]_{\alpha\alpha}$ ⇒
$$
\boxed{\;\Pi^\mu_\alpha=-\Pi^\mu_\alpha=0\;\Rightarrow\;\delta\Lambda^{\rm geom}_{\mu\nu}=0\;}
$$
**Khurana 抵消推广到 interband 成立 → A 对。** 几何确住裸顶点 ∂h(k)，局域 Σ 只重整 (Z, Δ_eff, ε_α)，不引入新 k 加权抹掉 metric-Chern 不等式。

**情形 B（U_P 非对角）**：反演置换子格 / 轨道偏离反演中心 ⇒
$$
\Pi^\mu_\alpha=-\sum_{\rho\sigma}(U_P^\dagger)_{\alpha\rho}\,\Pi^\mu_{\rho\sigma}\,(U_P)_{\sigma\alpha},\qquad \Pi^\mu_{\rho\sigma}\equiv\tfrac1N\sum_k[\hat M_\mu]_{\rho\sigma},
$$
此式把对角 $\Pi^\mu_{\alpha\alpha}$ 与 **+k 处的非对角 $\Pi^\mu_{\rho\sigma}$** 相联，**不强制 $\Pi^\mu_\alpha=0$**。一般 $\Pi^\mu_\alpha\ne0$ ⇒
$$
\boxed{\;\delta\Lambda^{\rm geom}_{\mu\nu}\sim\sum_\alpha\Pi^\mu_\alpha\,\Gamma_\alpha\,\Pi^\nu_\alpha\ne0\;}
$$
**Khurana 抵消失效 → B 对。** 且因平带无 W/U 小参数，局域顶点 Γ_α~O(U)~O(bandwidth-independent)，修正为 **O(1) 非微扰**（B 的量级估计正确，非 1/d）。

**这正是多层 DMFT(K3, arXiv:1009.5299) 的精确对应**：那里「沿 z 动量非好量子数 ⇒ 宇称论证失效 ⇒ 纵向顶点修正复活；面内平移不变 ⇒ 仍抵消」。本文把「层指标」一般化为「轨道指标」，把「z 方向破缺」一般化为「U_P 非对角」。机制同一，独立交叉验证 ✓。

### §3.4 判据与 A/B 主轴的关系（澄清两位博士各自的偏差）
- **A 的偏差**：把 Khurana 当**无条件**支柱（H5「单点 DMFT 横向顶点修正恒为零」），并以「Δ_α 均匀(Wyckoff 等价)」为主轴。但 §3.3 证明：**Δ_α 均匀 ≠ U_P 对角**。子格可被对称联系（⇒均匀 Δ，A 的 Wyckoff 等价）却仍被反演**置换**（⇒ U_P 非对角 ⇒ 顶点修正复活）。故 A 的「等价 Wyckoff ⇒ 下界存活」推断**有缺口**：等价性管 Δ 均匀，管不住顶点宇称。
- **B 的偏差**：把「interband ⇒ 顶点修正 O(1)」当**普适**。但 §3.3 证明 U_P 对角时 interband 顶点修正**被宇称强制为零**——B 的「范畴错配」并非无条件。B 的二分法（单带/带间）抓错了变量；真正变量是 $\Pi^\mu_\alpha$ 的宇称 = U_P 的轨道对角性。

---

## §4 与 GRPA / 轨道嵌入文献的对接（情形 B 的独立佐证 + 量级）

GRPA(G2, arXiv:2308.10780) 在平均场上加高斯(集体模)涨落，得超流权重
$$
D_s=D_s^{(0)}+D_s^{(1)},\qquad D_s^{(1)}=D_{s,\rm conv}^{(1)}+D_{s,\rm geom}^{(1)},
$$
并发现：**几何涨落修正 $D_{s,\rm geom}^{(1)}$ 一般 O(1)，但可经选取「自然/优选轨道位置」置零**；平带极限下与最小量子度规的关系在 GRPA 下仍成立。

**对接**：单点 DMFT 的 D_s^geom = 「局域 Σ 缀饰传播子 + 裸顶点泡（无顶点修正）」，等价于「在 DMFT 轨道基(= U 局域的物理子格位置)嵌入下的平均场型几何泡」。其**缺失的顶点修正**与 GRPA 的 $D_{s,\rm geom}^{(1)}$ **同属一类**：都是涨落/集体模对几何泡的修正，且都**依赖轨道嵌入**。于是
- DMFT 物理子格位置 = 自然(优选)轨道位置 ⇒ $D_{s,\rm geom}^{(1)}=0$ ⇒ 裸顶点泡即物理几何权重 ⇒ **A 对**（与 §3.3 情形 A 一致：U_P 对角 ⟺ 轨道在对称中心 ⟺ 自然位置）。
- 二者不重合（轨道偏离对称中心 / 带 Wannier 阻碍，C≠0 拓扑无点状 Wannier）⇒ $D_{s,\rm geom}^{(1)}=O(1)\ne0$ ⇒ DMFT 裸顶点泡漏 O(1) ⇒ **B 对**。

**拓扑扇区(C≠0)的特殊危险**：metric-Chern 下界 ∫g̃≥π|C|(G3, arXiv:2203.11133) 的最小度规由轨道位置最小化决定；C≠0 时**无平凡点状 Wannier 基**（拓扑阻碍），物理嵌入一般 ≠ 最小度规嵌入 ⇒ 顶点修正不可被「自然位置」gauge 掉 ⇒ O(1) 修正残存。**这正是 S1 下界 π|C| 唯一非平凡(C≠0)的扇区**——B 的精炼 B2 在此**有牙齿**。

---

## §5 一个 A、B 都忽略的环节：反常(配对)顶点与规范不变性

§3 的宇称论证用于**正常(p-h)道**电流顶点。但超导态 D_s 的**反常(p-p)顶点修正 = 相位模(Anderson-Bogoliubov)**是 Ward 恒等式 $q_\mu\Lambda^{\mu\nu}=0$ 所必须；裸泡本身**不规范不变**。

- 平均场 BdG 的 D_s^geom（自由能对相位扭曲二阶导）**已自动含**平均场级相位模 → 是规范不变的正确量。
- 单点 DMFT 若以**自由能相位扭曲二阶导**(而非朴素裸泡)计算 D_s，则**自动含局域反常顶点**(局域相位模)，规范不变性在局域层面恢复。
- DMFT 真正漏的，仍是**非局域**反常顶点(相位模的 k 色散)——与 §3/§4 同源，归并入「U_P 非对角 / 轨道嵌入」轴。

**修正 A 步4 的一个不严谨处**：A 在步4写「裸顶点 ∂h(k) × 缀饰传播子」并称抗磁项 K=⟨∂²h⟩ 亦裸、无修正。这在**正常道 + U_P 对角**下对；但**忽略了反常顶点的规范不变性要求**。若 A 用裸泡而非自由能二阶导，其 D_s^geom 甚至在情形 A 也可能违反 f-求和/规范不变（高估或低估）。**建议 S2 数值用相位扭曲自由能法，不要用朴素裸泡 Kubo。**

---

## §6 自我攻击 + 网络交叉验证

**自攻 1：§3.3 的 $\hat G(-k)=U_P^\dagger\hat G(k)U_P$ 是否成立？** 需局域 Σ 守反演。DMFT 自洽中各子格杂化函数由对称联系，Σ_α 守点群 ⇒ 成立。但**情形 B（U_P 非对角）下「轨道对角 Σ」本身是否自洽**？若反演置换子格，对称要求 Σ 在子格间有约束，但单点 DMFT 仍令 Σ 轨道对角（位点局域）——这是 DMFT 的**近似**，非精确。→ 不影响裁决（恰恰是 DMFT 漏掉的非局域结构），但说明情形 B 下 DMFT 的轨道对角假设本身就是误差源，**强化 B**。✓

**自攻 2：U_P 对角是否真能与 C≠0 共存？** 若能，则「情形 A(A对) ∧ C≠0(下界非平凡)」可同时满足，A 在非平凡扇区也对。检验：U_P 对角(轨道在反演中心)不排斥 C≠0（如某些含 SOC 的对称模型，Chern 来自 k 空间相位而非轨道置换）。→ **存在 A 在 C≠0 仍对的子扇区**。故不能笼统说「C≠0 ⇒ B 对」；精确陈述是「C≠0 **且** 物理嵌入≠最小度规嵌入(Wannier 阻碍) ⇒ B 对」。**修正 §0 表述**：拓扑性是危险信号但非充分条件，真正充分条件是轨道嵌入失配/U_P 非对角。✓（已在 §0 诚实声明中预留）

**自攻 3：B 的 N₃≠C(Green 零点/Mott) 轴是否被本裁决覆盖？** 否——那是**独立第三轴**（拓扑荷在强关联的去量子化），与顶点修正正交。本仲裁只裁「顶点修正对几何是否零」，不裁 N₃≠C。诚实标注：B 的 N₃ 论点在 Mott 邻近(U>U_c, G 零点)**另行成立**，进一步限制 A，但**不属本矛盾的裁决范围**，移交 S2 拓扑子任务。✓

**自攻 4：会不会 §3.3 情形 B 中各 α 的 $\Pi^\mu_\alpha$ 求和后再抵消？** $\delta\Lambda\sim\sum_\alpha\Pi^\mu_\alpha\Gamma_\alpha\Pi^\nu_\alpha$ 是**平方型**(同一 α 两腿)，即便 $\sum_\alpha\Pi^\mu_\alpha=0$，平方和 $\sum_\alpha(\Pi^\mu_\alpha)^2\Gamma_\alpha$ 一般 ≠0(若 Γ_α 同号，如吸引 U 配对道)。→ 不抵消，O(1) 残存稳健。✓

**网络交叉验证**：
- K3(多层 DMFT, 1009.5299) 独立确认「宇称破坏⇒顶点修正复活」，且明确「面内(对角结构)仍抵消、跨层(非对角)不抵消」——与 §3.3 情形 A/B **机制完全吻合**。这是本裁决最强的独立外部支撑。
- G2(GRPA, 2308.10780) 独立确认「几何超平均场修正 O(1)、可经轨道位置 gauge」——与 §4 对接吻合。
- 未检索到任何文献**显式**做过「单点 DMFT 几何顶点修正的宇称-轨道判据」→ 本判据为新整合，是 S2 合法增量，但也意味**无文献背书该精确判据**，PI 须独立复核 §3.3 代数。

---

## §7 移交 PI 的核实项（不编造，明确标注）

1. **半开放问题**：「单点 DMFT 缺失顶点修正 ≡ GRPA $D_{s,\rm geom}^{(1)}$」的精确等同——本仲裁给了同构论证(§4)，但文献(G2)是 GRPA 非 DMFT，**等同未被显式证明**。S2 若要把「C≠0⇒B对」当结论收官，须补此证明或数值验证（如对 Lieb+flux 算 DMFT 裸泡 D_s^geom vs 真实/GRPA D_s^geom 的 O(1) 差）。
2. **§3.3 宇称代数**：$\hat v_\mu(-k)=-U_P^\dagger\hat v_\mu(k)U_P$ 与 $\Pi^\mu_\alpha=-\Pi^\mu_\alpha$ 的推导请 PI 独立复核（可证核心，应能复核通过）。
3. **模型逐一定 U_P 对角性**：pyrochlore(4 子格 T_d)、纯 Lieb(角点反演)、修饰 Lieb、α-T₃ 各自的反演/C₂ 在子格基下 U_P 是否对角——决定每个模型落 A 还是 B。**初判**：纯 Lieb 角点反演 U_P 对角(边心子格各自对称)→A；修饰 Lieb/α-T₃ 非等价子格→U_P 非对角→B；pyrochlore 需查反演中心是否置换 4 子格(**未定，需 PI 群论核**)。
4. **arXiv 号**：Wang-Zhang(T1: PRX 2,031008=1201.6431 vs topological-Hamiltonian=1207.7341，勿混)、Volovik N₃ 原始出处(T2)、Khurana(K1=PRL 64,1990 已较确定)——请 PI 终核。
5. **§5 规范不变性**：建议 S2 数值采用相位扭曲自由能二阶导法计 D_s，避免朴素裸泡 Kubo 在情形 A 也可能破坏 Ward 恒等式。

---

## §8 一句话裁决（供 S2 收官登记）

> **(C) 部分**：电流顶点修正对几何部分**并非无条件为零(否 A)、亦非无条件 O(1)(否 B)**；其零/非零由**精确宇称-轨道判据**裁定——轨道对角电流极化 $\Pi^\mu_\alpha$ 在 k→−k 下为奇 ⟺ 反演表示 $U_P$ 轨道对角(轨道居反演对称中心)。**U_P 对角 ⇒ Khurana 推广到 interband、修正为零、A 对**；**U_P 非对角或带 Wannier 阻碍(尤其 C≠0 拓扑) ⇒ 修正 O(1)、DMFT 系统性偏离平均场 BdG、精炼 B2 对**。A 误把 Khurana 当无条件支柱(Wyckoff 等价管 Δ 均匀≠管顶点宇称)；B 误把「带间⇒O(1)」当普适(宇称可强制其零)。**S1 下界 π|C| 在 U_P 对角的非拓扑/可定域扇区以重整形式存活；在 C≠0 且嵌入失配的拓扑扇区(下界唯一非平凡处)其「忠实性」非自动，须 §7.1 补证方可收官，否则 S2 只能以「有条件存活 + 拓扑扇区开放」结案。**
