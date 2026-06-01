## B作业 Phase 1（独立推导）— Σ_B^{internal} 浴侧形式 + Nakagawa 映射

> 独立推导。未读取本项目任何已有作业；仅使用任务书声明的公理与外部公开文献。所有"内部K结论"未被调用。

---

### §S 网络搜索（先于推导）

#### S.1 Nakagawa 信息回流定义（arXiv:2602.09054 v2 + 2601.18822）
- **回流泛函**：$N_I := \int_0^\infty \Theta(\dot I(t))\,\dot I(t)\,dt$（即 $\dot I>0$ 区间的累积）。等价写法 $N_I=\int_{\dot I>0}\dot I\,dt$。
- **信息度量** $I(t)$：作者明示三种典型选择：(a) $S(\rho_R)$；(b) $-D(\rho_R\|\sigma)$ 对参考态 $\sigma$；(c) trace distance / 可区分度。**结构定理**采用 (b)：$I(t):=-D(\rho_R(t)\|\sigma)$，使衰减对应 $I$ 不增。
- **结构定理 1（量子，CP-可除）**：若约化映射 $\Phi(t,0)=\Phi(t,s)\circ\Phi(s,0)$ 满足每段 $\Phi(t,s)$ 是 CPTP（CP-divisible），且 $\sigma$ 是 TCL 生成元 $\mathcal{G}(t)$ 的不动点（$\mathcal{G}(t)\sigma=0$），则 $D(\rho_R(t)\|\sigma)$ 单调不增、$N_I=0$。证明走 data-processing。
- **结构定理 2（Lindblad 检验）**：若 $\mathcal{G}(t)$ 具时变 GKSL 形式且 $\gamma_k(t)\geq 0$ 全部成立，则 CP-divisible，自动 $N_I=0$。
- **关键前提**：$\mathcal{G}(t)\sigma=0$（参考态是约化生成元的不动点）+ CP-divisibility。

来源：[arXiv:2602.09054 v2 — Structural Theory of Information Backflow](https://arxiv.org/html/2602.09054v2/)、[arXiv:2601.18822 — Unifying Entanglement Revivals](https://arxiv.org/abs/2601.18822)。

#### S.2 Spohn 1978 三层前提
- 来源：[Spohn 1978, J. Math. Phys. 19, 1227](https://pubs.aip.org/aip/jmp/article/19/5/1227/460049/Entropy-production-for-quantum-dynamical)。
- 设置：(i) Lindblad CPTP **半群** $\Phi_t=e^{\mathcal{L}t}$；(ii) Gibbs 不变态 $\mathcal{L}[\rho_\beta]=0$；(iii) 由 (i)(ii) + Lindblad 形式 + 数据处理不等式（CPTP 下 $D$ 不增）导出 $\sigma=-dD/dt\ge 0$。

#### S.3 有限维幺正下浴熵产生可负
- [Strasberg-Esposito 2019, PRE 99, 012120](https://arxiv.org/abs/1806.09101v3)：有限维与初始关联场景下 $\sigma(t)<0$ 是 non-Markovian 的指标但非充分。
- [Buscemi-Schindler-Strasberg 2024 (arXiv:2404.15915 v3)](https://arxiv.org/html/2404.15915v3)：strong-coupling 中央自旋数值上 $\Sigma$ 速率振荡至负值。
- [Nishiyama-Hasegawa 2602.01669](https://arxiv.org/html/2602.01669v1)：Unified entropy production，对一般初态 $\Delta\Sigma$ 可负。
- [arXiv:1709.02174 Strasberg](https://ar5iv.labs.arxiv.org/html/1709.02174)：明确"在仅看 system 形式中，没有浴熵贡献，对一类合法过程 σ 不正"。

#### S.4 ELvdB 2010 分解（间接通过引用）
- 形式：$\Sigma=\Delta I(S\!:\!B)+D(\rho_B(t)\|\rho_B(0))$，要求初态乘积 $\rho_{SB}(0)=\rho_S(0)\otimes\rho_B(0)$，$\rho_B(0)=\rho_\beta$。
- 受 [arXiv:1405.6140](https://ar5iv.labs.arxiv.org/html/1405.6140)、[2602.01669](https://arxiv.org/html/2602.01669v1) 第 3-4 节复述确认。

---

### §A 撞墙（攻击点）

#### A1 — N=1 单振子浴 (Jaynes-Cummings) 闭式

设 $H_S=\tfrac{\omega}{2}\sigma_z$，$H_B=\omega a^\dagger a$（截到 $\{|0\rangle,|1\rangle\}$），$H_I=g(\sigma_+ a+\sigma_- a^\dagger)$，$\rho_S(0)=|e\rangle\langle e|$，$\rho_B(0)=|0\rangle\langle 0|$，乘积初态。共振 JC 严格解：
$$|\psi(t)\rangle=\cos(gt)|e,0\rangle-i\sin(gt)|g,1\rangle$$
$$\rho_B(t)=\cos^2(gt)|0\rangle\langle 0|+\sin^2(gt)|1\rangle\langle 1|$$

闭式：
- $S_B(t)=h_2(\sin^2 gt)$，$h_2$ 二元熵；$\dfrac{dS_B}{dt}=g\sin(2gt)\,\ln\cot^2(gt)$，关于 $t=\pi/(4g)$ 反对称（先正后负）。
- $\langle H_B\rangle(t)=\omega\sin^2(gt)$；$\dfrac{d\langle H_B\rangle}{dt}=\omega g\sin(2gt)\ge 0$ 在 $[0,\pi/(2g)]$。

在 $t^*=\pi/(4g)$：$dS_B/dt=0$（熵处于极大），$d\langle H_B\rangle/dt=\omega g$。故
$$\Sigma_B^{int}(t^*)=0-\beta\omega g=-\beta\omega g<0$$
对任何 $\beta>0$ 成立，**显式负值**。在 $(t^*,\pi/(2g))$ 内两项都使 $\Sigma_B^{int}<0$（熵在退还、能量在涨）。

→ **A1 通**：N=1 闭式反例已立。

#### A2 — Spohn 三层在有限维幺正全系统下的失效逐层

- **(i) Lindblad CPTP 半群失效**：$\rho_B(0)\mapsto\rho_B(t)=\mathrm{Tr}_S U(\rho_S(0)\otimes\rho_B(0))U^\dagger$ 是固定 $\rho_S(0)$ 下的 CPTP 映射，但 **不是半群、不是时间齐次、一般不 CP-divisible**（JC 反例证明 trace distance 振荡）。
- **(ii) Gibbs 不变态失效**：偏迹后的演化无固定不动点；$\rho_B^{ref}=e^{-\beta H_B}/Z_B$ 在全局幺正下一般 **不被保持**（除非 $H_I=0$ 或全系统恰是其能本征态）。
- **(iii) 数据处理失效**：$D(\rho_B(t)\|\rho_B^{ref})$ 在偏迹幺正下无单调性。Data-processing 仅在两个变元同时被同一 CPTP 映射作用时给出不增；这里参考态被冻结而 $\rho_B$ 在非半群、非 CP-divisible 映射下演化。

最根本是 (i)：失去半群即失去 (ii)(iii) 的舞台。

#### A3 — 普遍约束尝试

由 $S_B\le\ln d_B$（$d_B=\dim\mathcal H_B$）与全局能量守恒 $\langle H\rangle=\text{const}$（注意：$\langle H_B\rangle$ 自身不守恒），积分：
$$\int_0^\infty\Sigma_B^{int}\,dt=[S_B-\beta\langle H_B\rangle]_0^\infty\le \ln d_B-\beta\,\langle H_B\rangle_{min}$$
（其中 $\langle H_B\rangle_{min}=$ $H_B$ 谱下界）。给出**累积** $\Sigma_B^{int}$ 的上界，**但不约束符号**。

故仅由 $\dim$ 与能量守恒不能锁定 $\Sigma_B^{int}\ge 0$。

---

### §D 核心推导（操作算符级）

设 $H=H_S+H_B+H_I$（每个 $\partial_t=0$），$\dot\rho_{SB}=-i[H,\rho_{SB}]$。$\rho_B=\mathrm{Tr}_S\rho_{SB}$。

#### D.1 $d\rho_B/dt$
$$\dot\rho_B=-i\,\mathrm{Tr}_S[H,\rho_{SB}]$$
分项：
- $\mathrm{Tr}_S[H_S\!\otimes\! I_B,\rho_{SB}]=0$（partial trace 在 S 因子上的迹循环不变性）。
- $\mathrm{Tr}_S[I_S\!\otimes\! H_B,\rho_{SB}]=[H_B,\rho_B]$。
- $\mathrm{Tr}_S[H_I,\rho_{SB}]=:i\mathcal D_B(t)$（一般非零浴算符）。

故
$$\dot\rho_B=-i[H_B,\rho_B]+\mathcal D_B(t),\quad \mathcal D_B(t):=-i\,\mathrm{Tr}_S[H_I,\rho_{SB}]\quad(\dagger)$$

#### D.2 $dS_B/dt$
利用 $\mathrm{Tr}\dot\rho_B=0$ 与 $\frac{d}{dt}\mathrm{Tr}(\rho\ln\rho)=\mathrm{Tr}(\dot\rho\ln\rho)$（标准结果，依据 Klein 函数微分 + $\mathrm{Tr}\dot\rho\cdot 1=0$）：
$$\frac{dS_B}{dt}=-\mathrm{Tr}_B(\dot\rho_B\ln\rho_B)$$

将 $(\dagger)$ 代入。首项：
$$i\,\mathrm{Tr}_B([H_B,\rho_B]\ln\rho_B)\overset{[A,B]C\to A[B,C]}{=}i\,\mathrm{Tr}_B(H_B[\rho_B,\ln\rho_B])=0$$
最后等式由 $[\rho_B,\ln\rho_B]=0$（任何算符与其函数演算对易，依据谱分解）。

故
$$\frac{dS_B}{dt}=-\mathrm{Tr}_B(\mathcal D_B\,\ln\rho_B)=i\,\mathrm{Tr}_{SB}\bigl([H_I,\rho_{SB}](I_S\!\otimes\!\ln\rho_B)\bigr)$$
再用迹循环 $\mathrm{Tr}([A,B]C)=\mathrm{Tr}(A[B,C])$：
$$\boxed{\;\frac{dS_B}{dt}=i\,\mathrm{Tr}_{SB}\Bigl(H_I\,[\rho_{SB}(t),\,I_S\!\otimes\!\ln\rho_B(t)]\Bigr)\;}\quad(\text{D.2})$$

依据：Liouville-von Neumann + partial trace 线性 + 迹循环 + $[\rho,\ln\rho]=0$。

#### D.3 $d\langle H_B\rangle/dt$
Heisenberg：$\dfrac{d\langle H_B\rangle}{dt}=\langle i[H,H_B]\rangle=i\langle[H_I,H_B]\rangle$（$[H_S,H_B]=0$，$[H_B,H_B]=0$）。即
$$\frac{d\langle H_B\rangle}{dt}=i\,\mathrm{Tr}_{SB}([H_I,H_B]\rho_{SB})=i\,\mathrm{Tr}_{SB}\bigl(H_I[I_S\!\otimes\!H_B,\rho_{SB}]\bigr)\quad(\text{D.3})$$

#### D.4 合并：$\Sigma_B^{int}$ 的浴侧+$H_I$ 表达式
组合 (D.2)(D.3)：
$$\Sigma_B^{int}=i\mathrm{Tr}_{SB}\bigl(H_I[\rho_{SB},I_S\!\otimes\!\ln\rho_B]\bigr)+i\beta\,\mathrm{Tr}_{SB}\bigl(H_I[\rho_{SB},I_S\!\otimes\!H_B]\bigr)$$
（注意 $[A,B]=-[B,A]$ 用于 $-\beta\cdot$D.3 项）
$$=i\,\mathrm{Tr}_{SB}\Bigl(H_I\,\bigl[\rho_{SB}(t),\,I_S\!\otimes\!\bigl(\ln\rho_B(t)+\beta H_B\bigr)\bigr]\Bigr)$$

引入 Gibbs 参考 $\rho_B^{ref}:=e^{-\beta H_B}/Z_B$，$\ln\rho_B^{ref}=-\beta H_B-\ln Z_B$，故 $\ln\rho_B+\beta H_B=\ln\rho_B-\ln\rho_B^{ref}-\ln Z_B$；c-数 $\ln Z_B$ 与 $\rho_{SB}$ 对易、对易子 = 0。最终：

$$\boxed{\;\Sigma_B^{int}(t)\;=\;i\,\mathrm{Tr}_{SB}\Bigl(H_I\;\bigl[\rho_{SB}(t),\;I_S\!\otimes\!\bigl(\ln\rho_B(t)-\ln\rho_B^{ref}(\beta)\bigr)\bigr]\Bigr)\;}\quad(\bigstar)$$

**仅含浴侧算符 + $H_I$，无 $H_S$，无 system 算符**（$I_S$ 是平凡因子）。

#### D.5 等价宏观恒等式
直接积分 $S_B,\langle H_B\rangle$：
$$D(\rho_B\|\rho_B^{ref})=-S_B+\beta\langle H_B\rangle+\ln Z_B$$
$$\Rightarrow\;\boxed{\;\Sigma_B^{int}(t)=-\frac{d}{dt}D\bigl(\rho_B(t)\,\|\,\rho_B^{ref}(\beta)\bigr)\;}\quad(\bigstar\bigstar)$$

依据：直接代入定义 + $\frac{d}{dt}\ln Z_B=0$（$\beta$ 固定，$H_B$ 不显式时间依赖）。

#### D.6 极限检查
1. $\rho_B(t)=\rho_B^{ref}$：$\ln\rho_B-\ln\rho_B^{ref}=0$，$(\bigstar)$ 显然零；$(\bigstar\bigstar)$ 在 $\rho_B^{ref}$ 邻域 $D=0$ 极小，$\dot D=0$。✓
2. $H_I=0$：$\rho_{SB}(t)=\rho_S(t)\otimes\rho_B(0)$，$\rho_B$ 仅幺正演化 $e^{-iH_B t}\rho_B(0)e^{iH_B t}$，$S_B$ 守恒、$\langle H_B\rangle$ 守恒，$\Sigma_B^{int}=0$。$(\bigstar)$ 显式 $H_I=0\Rightarrow 0$。✓
3. **Passive 浴**（被动态，$\rho_B(0)$ 与 $H_B$ 同对角且单调），$\rho_B(0)=\rho_B^{ref}$ 是特例：不一定退化；passive 不蕴含 Gibbs，$D\neq 0$ 一般。无平凡退化但 $(\bigstar\bigstar)$ 仍成立。

#### D.7 符号判据
$(\bigstar\bigstar)$ 蕴含：
$$\Sigma_B^{int}(t)\ge 0\;\Longleftrightarrow\;\frac{d}{dt}D(\rho_B(t)\|\rho_B^{ref})\le 0$$
即"浴态向 Gibbs 参考态靠近"。无 a-priori 符号；A1 中 JC 在 $t\in(\pi/(4g),\pi/(2g))$ 上 $\rho_B$ 远离 $\rho_B^{ref}$，故 $\Sigma_B^{int}<0$。

**与外部文献吻合**：[arXiv:2602.01669](https://arxiv.org/html/2602.01669v1) Eq.13 在 $\beta_0=\beta_\tau=\beta$ 下退化为 $\Delta\Sigma=\Delta I(S\!:\!B)+\Delta D(\rho_E\|\gamma_E)$，差分版 $(\bigstar\bigstar)$。我们的速率版 $(\bigstar)$ 是其无穷小算符级实现。

---

### §N Nakagawa 映射尝试

#### N.1 选择
- 约化扇区 $R:=B$（浴自身）。
- 参考态 $\sigma:=\rho_B^{ref}(\beta)=e^{-\beta H_B}/Z_B$。
- 信息度量 $I_B(t):=-D(\rho_B(t)\|\rho_B^{ref})$。

由 $(\bigstar\bigstar)$ 直接得：
$$\dot I_B(t)=-\frac{d}{dt}D(\rho_B(t)\|\rho_B^{ref})=\Sigma_B^{int}(t)$$

→ **逐点恒等成立**。回流泛函 $N_{I_B}=\int_{\Sigma_B^{int}>0}\Sigma_B^{int}\,dt$。

#### N.2 Nakagawa 结构定理是否合法？

结构定理要求约化生成元 $\mathcal G_B(t)$ 满足 $\mathcal G_B(t)\sigma=0$ 且 CP-divisible（→ $N_I=0$）。

考察我们的 $\rho_B(t)=\mathrm{Tr}_S U(t)\rho_{SB}(0)U^\dagger(t)$：
- TCL 生成元 $\mathcal G_B(t)$ 形式上存在（在反演域上），其形式为 $\mathcal G_B(t)\rho_B=-i[H_B,\rho_B]+\mathrm{Tr}_S[(\cdots)]$，但**一般不满足** $\mathcal G_B(t)\rho_B^{ref}=0$。
  - 直觉：$\rho_B^{ref}$ 是 $H_B$ 的不动点但非 $H_I$ 的不动点；偏迹 $\mathrm{Tr}_S[H_I,\rho_S(0)\otimes\rho_B^{ref}]\neq 0$ 一般非零（除非特殊耦合结构如 $H_I$ 的浴侧与 $H_B$ 对易，此时退化）。
- CP-divisibility 一般失败（A1 振荡）。

故 Nakagawa 结构定理的两条充分条件均**不满足**。

**结论**：$\Sigma_B^{int}\equiv\dot I_B$ 的**等同（identity）合法**（仅由 $D$ 的定义与 $(\bigstar\bigstar)$ 推得，无需任何 master-equation 假设）；但该等同**落在 Nakagawa structural theorem 的合法域之外**——结构定理无法保证 $N_I=0$，反过来：$N_I>0$ 不能直接归因于 CP-divisibility 破坏（因为不变性前提就已破坏）。

→ **有条件合法**：作为 backflow 测度合法；作为结构定理推论非法。

#### N.3 修复路径（提议）
若改用**瞬时不动点** $\sigma_t$ 满足 $\mathcal G_B(t)\sigma_t=0$（[arXiv:2602.01669](https://arxiv.org/html/2602.01669v1) 的 $\beta^*_t$ 思路：能量匹配的有效 Gibbs），则可恢复结构定理形式合法性，但 $\sigma$ 时间依赖会改写 $\dot I$ 中产生额外项 $-\partial_\beta D\cdot\dot\beta^*_t$，破坏 $(\bigstar\bigstar)$ 的简洁形式。

---

### §K 卡点

#### K1 — Nakagawa 结构定理的不变性前提与全局幺正不相容

无论选 $\sigma=\rho_B^{ref}(\beta)$ 还是 $\sigma_t=\rho_B^{ref}(\beta^*_t)$，全局有限维幺正下的 reduced bath 生成元一般不以 $\sigma$ 为不动点。要么放弃结构定理（保留 $(\bigstar\bigstar)$ 的精确性），要么引入瞬时参考（破坏简洁性）。当前我无法证明存在第三条路。

#### K2 — $\ln\rho_B(t)$ 在 $\rho_B$ 退化谱处的奇异性

$(\bigstar)$ 形式上要求 $\rho_B(t)$ 全秩。若初态 $\rho_B(0)$ 是纯态（如 A1 vacuum），$\ln\rho_B(0)\to -\infty$ 在零空间。需用 $\rho_B^\epsilon=(1-\epsilon)\rho_B+\epsilon I/d_B$ 正则化，取 $\epsilon\to 0^+$ 极限。$(\bigstar\bigstar)$ 在该极限下良定义（因为 $D(\rho_B\|\rho_B^{ref})$ 在 $\rho_B^{ref}$ 全秩时对所有 $\rho_B$ 良定义且有限），但 $(\bigstar)$ 的算符级形式需谨慎处理。**未完全解决**。

---

### §C 本Phase独立结论（一句话）

$\Sigma_B^{int}(t)=i\,\mathrm{Tr}_{SB}\bigl(H_I[\rho_{SB},I_S\!\otimes\!(\ln\rho_B-\ln\rho_B^{ref})]\bigr)=-\dot D(\rho_B\|\rho_B^{ref})$，符号不定（JC 闭式反例已立），与 Nakagawa $\dot I$ 在选 $R=B,\sigma=\rho_B^{ref}$ 下逐点恒等，但 Nakagawa 结构定理的不变性前提在偏迹幺正下系统失效，故映射"作为定义合法、作为结构推论非法"。

---

### §F 反向预判 A 的可能错误

> 在不读 A 作业前提下，预判正规推导路径中最易疏漏的细节。

#### F1 — 把 $[\rho_B,\ln\rho_B]=0$ 简化误用为"$H_B$ 部分对 $dS_B/dt$ 有贡献"

正规步骤中 $\dot\rho_B=-i[H_B,\rho_B]+\mathcal D_B$ 的 $H_B$ 项在 $\frac{dS_B}{dt}$ 里贡献 $i\mathrm{Tr}([H_B,\rho_B]\ln\rho_B)$；A 若直接用迹循环不慎可能算成 $i\mathrm{Tr}([H_B,\rho_B\ln\rho_B])\neq 0$ 而残留虚假项。正确链是 $\mathrm{Tr}([A,B]C)=\mathrm{Tr}(A[B,C])$ 把 $[H_B,\rho_B]\to[H_B,\cdot]\to H_B[\rho_B,\ln\rho_B]=0$。**易错处：commutator 对哪两个对象、迹循环顺序**。

#### F2 — 误把 $\rho_B^{ref}$ 当作约化生成元的不动点

A 若直接照搬 Spohn 形式宣称 $\Sigma_B^{int}\ge 0$，或调用 Nakagawa 结构定理的 $N_I=0$ 推论而未验证 $\mathcal G_B(t)\rho_B^{ref}=0$，会得到与 JC 反例直接矛盾的结论。**正确边界：$(\bigstar\bigstar)$ 是 identity，不是不等式；是否非负完全由 CPTP 半群 + 不变性两层假设决定，全局幺正下两者皆无**。

#### F3（可选）— partial trace 的 well-definedness 与退化谱

若 A 在推导中 implicit 假设 $\rho_B(t)$ 全秩而未声明正则化或限定初态，对纯态 bath（如 vacuum）会在 $\ln\rho_B$ 处出现 $-\infty$ 项。**$(\bigstar\bigstar)$ 不受此影响、$(\bigstar)$ 的算符级形式受影响**。

---

### 文献附注（独立溯源）
- [Spohn 1978, J. Math. Phys. 19, 1227](https://pubs.aip.org/aip/jmp/article/19/5/1227/460049/Entropy-production-for-quantum-dynamical) — 半群+不变态+数据处理三层框架。
- [Esposito-Lindenberg-Van den Broeck NJP 12, 013013 (2010)](https://iopscience.iop.org/article/10.1088/1367-2630/12/1/013013) — $\sigma=\Delta I(S\!:\!B)+D(\rho_B(t)\|\rho_B^{eq})$（被本推导独立复现差分版）。
- [Strasberg-Esposito 2019, arXiv:1806.09101v3 (PRE 99, 012120)](https://arxiv.org/abs/1806.09101v3) — 非 Markov 场景下 $\sigma<0$ 可能。
- [Nishiyama-Hasegawa 2602.01669 (2026)](https://arxiv.org/html/2602.01669v1) — Unified entropy production 差分版与 $(\bigstar\bigstar)$ 一致。
- [Nakagawa K. arXiv:2602.09054 v2 (2026)](https://arxiv.org/html/2602.09054v2/) — 结构定理 1（CP-divisible+不变性 ⇒ $N_I=0$）。
- [Nakagawa K. arXiv:2601.18822 (2026)](https://arxiv.org/abs/2601.18822) — $N_I=\int_{\dot I>0}\dot I\,dt$ 的统一回流框架。
- [Buscemi-Schindler-Strasberg arXiv:2404.15915v3](https://arxiv.org/html/2404.15915v3) — 有限浴 strong-coupling 数值验证 $\sigma$ 振荡负值。
