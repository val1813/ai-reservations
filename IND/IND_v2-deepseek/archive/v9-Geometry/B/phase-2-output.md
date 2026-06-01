## B作业 v9 Phase 2（独立推导）— N_q 普适 + Holevo saturation + 端点依赖

### §S 网络搜索（≤3 条）

S1. Tavis–Cummings / 多模 JC 的 bright/dark 分解是教科书结论：对称耦合下，亮模 $a_B = N_q^{-1/2}\sum_i a_i$ 与原子耦合，正交 dark 模与原子解耦（[Wikipedia: Tavis–Cummings model](https://en.wikipedia.org/wiki/Tavis%E2%80%93Cummings_model)；Cordero et al.，"Algebraic approach to the Tavis–Cummings model with three modes"，2017，[arXiv:1710.10945](https://arxiv.org/abs/1710.10945) — 显式给出 Bogoliubov 法向模诊化 $N_q=3$ 情形）。

S2. Holevo 边界 $\chi \le S(\bar\rho) - \sum_i p_i S(\rho_i)$；对纯态系综饱和条件为 $\bar\rho$ 谱熵 = $\log\dim$，即等概率正交纯态系综（综述见 Wilde《Quantum Information Theory》Ch. 11；近期 [arXiv:2506.06700](https://arxiv.org/html/2506.06700v2)）。

S3. JCM 还原浴态在共振 + 真空初态下产生二元 Fock 混合 $\rho_B = c^2|0\rangle\langle 0| + s^2|1\rangle\langle 1|$；熵 = $h_2(\sin^2 u)$（[arXiv:2202.00330](https://arxiv.org/abs/2202.00330) 综述 §3）。

---

### §A 撞墙（独立推导）

**A1. $N_q=3$ 显式 Rabi 频率与 $\rho_B$ 谱**

定义亮模 $a_B = (a_1+a_2+a_3)/\sqrt{3}$，故 $\sum_i a_i = \sqrt{3}\,a_B$。则
$$H_I = g\sqrt{3}\,(\sigma_+ a_B + \sigma_- a_B^\dagger).$$
两个正交 dark 模 $a_{D_1}, a_{D_2}$ 与 $\sigma_\pm$ 完全解耦。初态 $|e,0,0,0\rangle = |e\rangle|0_B,0_{D_1},0_{D_2}\rangle$。dark 模始终保持真空。

单激发动力学：
$$|\psi(t)\rangle = \cos(g\sqrt{3}\,t)\,|e,0_B\rangle - i\sin(g\sqrt{3}\,t)\,|g,1_B\rangle \;\otimes\; |0_{D_1},0_{D_2}\rangle.$$
真空 Rabi 频率 $\Omega_R = 2g\sqrt{3}$，半周期对应 $u := g\sqrt{3}\,t \in [0,\pi/2]$。

$\rho_B(t) = \cos^2 u\,|0_B\rangle\langle 0_B| + \sin^2 u\,|1_B\rangle\langle 1_B|$ ⊗ |真空⟩⟨真空| (dark)，谱 $\{\cos^2 u, \sin^2 u\}$（dark 部分谱仅含 1，对熵无贡献）。

**A2. Bogoliubov 亮/暗模分解 — $N_I^{(S)}$ 是否随 $N_q$ 缩放？**

对任意 $N_q$，亮模 $a_B = N_q^{-1/2}\sum_i a_i$ 吸收所有耦合：
$$\tilde H_I = g\sqrt{N_q}(\sigma_+ a_B + \sigma_- a_B^\dagger).$$
真空初态在 $\{a_B, a_{D_k}\}$ 基下仍是真空。整动力学 = 单模 JC，有效耦合 $g_{\rm eff}=g\sqrt{N_q}$，**唯一改变的是时间标度** $u = g\sqrt{N_q}\,t$。

故 $\rho_B(u)$ 谱与 $N_q$ 无关；$S(\rho_S) = S(\rho_B) = h_2(\sin^2 u)$；联合纯态 $\Rightarrow$ $S(\rho_{SB}) = 0$；
$$I(S{:}B) = 2 h_2(\sin^2 u).$$
半 Rabi 周期对应 $u \in [0,\pi/2]$，$I$ 由 0 升至 $2\ln 2$（$u=\pi/4$）再回 0。

将 $T_>$ 取 "info 生成相位"（$\dot I > 0$，$u\in[0,\pi/4]$），
$$N_I^{(S)}(N_q) = I(\pi/4) - I(0) = 2\ln 2,\quad \forall N_q.$$
等价地，$I$ 在半周期上的 total variation = $4\ln 2$、半变差 = $2\ln 2$，**两者均与 $N_q$ 无关**。

**A3. Holevo saturating ensemble 显式构造（$N_q=2$）**

目标：$\chi_{\max} = 2\ln 2 = \ln 4$。Holevo 对纯态系综 $\chi = S(\bar\rho)$；要 $S(\bar\rho)=\ln 4$ 需 $\bar\rho = I_4/4$。

显式构造（浴 Fock 基取 4 维子空间）：
$$\Big\{p_k=\tfrac14,\; \rho_k=|\phi_k\rangle\langle\phi_k|\Big\}_{k=1}^{4},\quad |\phi_1\rangle=|0,0\rangle,\;|\phi_2\rangle=|1,0\rangle,\;|\phi_3\rangle=|0,1\rangle,\;|\phi_4\rangle=|1,1\rangle.$$
则 $\bar\rho = \tfrac14 I_4$，$S(\bar\rho) = \ln 4 = 2\ln 2$，每 $S(\rho_k)=0$，$\chi = 2\ln 2$ ✓。

物理诠释：4 个等概率正交纯态在 2 模 Fock 子空间 $\mathrm{span}\{|n_1,n_2\rangle: n_i\in\{0,1\}\}$；这正是 $I(S{:}B)$ 峰值 $2\ln 2$ 所"开锁"的 accessible classical bits（亮 + 暗自由度各贡献 $\ln 2$，合计 $\ln 4$）。

**A4. 端点闭式（任意 $T \in (0,\pi/2)$，$u$ 单位）**

$\dfrac{dI}{du} = 4\sin 2u\,\ln\cot u$。换元 $v=\cos 2u$，
$$I(u_T) = -\int_1^{\cos 2u_T}\!\!\ln\!\tfrac{1+v}{1-v}\,dv = 2h_2(\sin^2 u_T).$$
（中间步：$\int\ln\tfrac{1+v}{1-v}dv = (1+v)\ln(1+v)+(1-v)\ln(1-v)+C$；代回 $1\pm\cos2u = 2\cos^2u, 2\sin^2u$ 化简。）

---

### §D 推导链 D1–D5

- **D1**（亮/暗解耦）：对称耦合 $\Rightarrow$ $H_I$ 仅含 $a_B$；dark 模 commute with $H_I$ 且初始真空 $\Rightarrow$ 全程真空。
- **D2**（时间标度）：$g\to g\sqrt{N_q}$；动力学等价单模 JC，$u = g\sqrt{N_q}\,t$。
- **D3**（浴谱）：$\rho_B(u) = \cos^2u\,|0_B\rangle\langle0_B|+\sin^2u\,|1_B\rangle\langle1_B|$；$S(\rho_B)=h_2(\sin^2u)$。
- **D4**（互信息）：联合纯态 $\Rightarrow$ $I(S{:}B)=2 h_2(\sin^2 u)$；与 $N_q$ 显式无关。
- **D5**（Holevo 饱和）：$\chi=S(\bar\rho)$ 对纯态系综；等概率正交 4 维 $\Rightarrow$ $\chi=\ln 4=2\ln 2$。

---

### §K 卡点

K1. "$T_>$ = first half Rabi period" 字面读为 $u\in[0,\pi/2]$ 时 $\int\dot I\,dt = 0$（trivial）。需读作 $\dot I>0$ 子区间或半变差，方与命题 (a/b/c) 选项匹配。我采用 "rising 半"= $u\in[0,\pi/4]$，给出 $2\ln 2$。

K2. (II) 的 saturating ensemble 不来自 JC 动力学；动力学只到达 2 维子空间（$I=2\ln 2$ 是 mutual information 峰值，但 $\chi = \ln 4$ 需 $\bar\rho$ 占据 4 维 — 这是问题 (II) 的"capacity 解释"，属外部最优化构造，不是 JC 演化态）。命题语义需澄清：(II) 是"独立的 Holevo 上界饱和"还是"JC 浴态的 ensemble decomposition"？我按前者作答。

K3. dark 模数为 $N_q-1$，对熵零贡献，但若问 accessible information 的 "ceiling" 是否为 $\ln(N_q+1)$（含 dark 模标号信息），则需破对称耦合（让 dark 模携标记），此时答案才进入选项 (b)。在严格对称耦合 + 真空初态下，**(b) 不成立**。

---

### §C 结论

(I) **(c) 被支持**：$N_I^{(S)}(N_q) \equiv 2\ln 2$，与 $N_q$ 无关。机制 = bright/dark Bogoliubov 分解将 $N_q$-mode 问题约化为单模 JC，仅时间标度 $g\to g\sqrt{N_q}$ 改变；$h_2$ 形状普适。**二元熵 total variation 普适**成立。

(II) Saturating ensemble（$N_q=2$）：$\{p_k=1/4, |\phi_k\rangle\}_{k=1}^4$，$|\phi_k\rangle\in\{|00\rangle,|10\rangle,|01\rangle,|11\rangle\}$（双模 Fock 单激发以下基）。$\chi = \ln 4 = 2\ln 2$。

(III) $\boxed{N_I^{(S)}(T) = 2 h_2\!\big(\sin^2(g\sqrt{N_q}\,T)\big)}$，$u_T = g\sqrt{N_q}T \in (0,\pi/2)$ 单调上升至 $u_T=\pi/4$ 处达峰 $2\ln 2$。

参考：[Wikipedia TC](https://en.wikipedia.org/wiki/Tavis%E2%80%93Cummings_model)；[arXiv:1710.10945](https://arxiv.org/abs/1710.10945)；[arXiv:2202.00330](https://arxiv.org/abs/2202.00330)；[arXiv:2506.06700](https://arxiv.org/html/2506.06700v2)。
