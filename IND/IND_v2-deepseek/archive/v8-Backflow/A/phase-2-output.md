## A作业 Phase 2 — Σ_B^int BKM 二阶解析展开 + B Phase 1 质检报告

> 独立推导。仅使用任务书声明的恒等式 $\Sigma_B^{int}=-\dot D(\rho_B\|\rho_B^{ref})$ 与 BKM 内积定义。无网络搜索。

---

### §0.5 隐含假设清单

1. **BKM 内积归一化**：$(X,Y)_{BKM}:=\int_0^1 d\lambda\,\mathrm{Tr}((\rho_B^{ref})^\lambda X^\dagger(\rho_B^{ref})^{1-\lambda}Y)$，对应 BKM 超算符 $J_\sigma(X):=\int_0^1\sigma^\lambda X\sigma^{1-\lambda}d\lambda$。$D$ 的二阶展开走 $J_\sigma^{-1}=D\log_\sigma$。
2. **弱耦合**：保留至 $g^2$，所有 $g^4$ 修正显式截断。
3. **初态因子化**：$\rho_{SB}(0)=\rho_S(0)\otimes\rho_B^{ref}(\beta)$，$\rho_B^{ref}$ 全秩、与 $H_B$ 对易。
4. **Born/中心化**：保留 $a(s):=\langle\tilde A(s)\rangle_{\rho_S(0)}$ 一般非零（不擅自令 $\langle A_S\rangle=0$）；$B_B$ 已减去 c-数 shift（$\langle B_B\rangle_{\rho_B^{ref}}=0$ 不必要，但 c-数 shift 已被吸收）。
5. **算符对称性**：$A_S, B_B$ 自伴；$\tilde X(s):=e^{iH_0 s}Xe^{-iH_0 s}$；$H_0=H_S+H_B$。
6. **谱条件**：$\rho_B^{ref}$ 全秩，$J_{\rho_B^{ref}}^{-1}$ 在 1-粒子激发空间良定义（避开 Phase 1 K2 退化谱问题）。

---

### §1 强制撞墙

**A1 — t=0+ 自动归零？** 我们的核含 $\theta(t-s)$，$\Sigma_B^{int}(0^+)=g^2\cdot 0=0$。✓ 与初态因子化下 $D(0)=0,\dot D(0^+)=0$ 自洽（$D$ 在 $t=0$ 是平方极小，$\dot D(0^+)=0$）。

**A2 — KMS 二阶自洽？** 推导出的核含 $\partial_t\chi_B''(t-s)$，其中 $\chi_B''$ 是浴 retarded 响应虚部，由 KMS $\chi_B''(\omega)=\tfrac12(1-e^{-\beta\omega})C_B(\omega)$ 给出。Born-级核与 KMS 不引入额外约束（β 显式出现在 BKM 度量中，与 KMS 中的 β 是同一个）。✓

**A3 — Tr conservation？** $\delta\tilde\rho_B^{(1)}=-i\int ds\,a(s)[\tilde B(s),\rho_B^{ref}]$，对易子的迹恒为 0，故 $\mathrm{Tr}\,\delta\tilde\rho_B^{(1)}=0$ 严格成立。同理 $\delta\tilde\rho_B^{(2)}$（双对易子结构）迹也为零。✓

---

### §2 推导

#### §2.1 相互作用图景 + 二阶 Dyson

$H_I=g\,A_S\otimes B_B=:gV$。$U_I(t)=\mathcal T\exp(-ig\int_0^t\tilde V(s)ds)$。

$$\tilde\rho_{SB}(t)=\rho_{SB}(0)-ig\int_0^t ds_1[\tilde V(s_1),\rho_{SB}(0)]-g^2\int_0^t ds_1\int_0^{s_1}ds_2[\tilde V(s_1),[\tilde V(s_2),\rho_{SB}(0)]]+O(g^3)$$

**一阶 Tr_S**（用 $\tilde V=\tilde A\otimes\tilde B$）：
$$\mathrm{Tr}_S[\tilde V(s),\rho_S\otimes\rho_B^{ref}]=\langle\tilde A(s)\rangle_S\,[\tilde B(s),\rho_B^{ref}]=:a(s)\,[\tilde B(s),\rho_B^{ref}]$$

故
$$\boxed{\delta\tilde\rho_B^{(1)}(t)=-ig\int_0^t ds\,a(s)\,[\tilde B(s),\rho_B^{ref}]}$$

**二阶 Tr_S**（保留以备 g⁴ 阶检查；记号 $C_S(s_1,s_2):=\mathrm{Tr}(\rho_S\tilde A(s_1)\tilde A(s_2))$，$C_S^*(s_1,s_2)=C_S(s_2,s_1)$）：

$$\delta\tilde\rho_B^{(2)}(t)=-g^2\!\!\int_0^t\!\!\!\int_0^{s_1}\!\!\Big[C_S(s_1,s_2)\big(\tilde B_1\tilde B_2\rho_B^{ref}-\tilde B_2\rho_B^{ref}\tilde B_1\big)+\mathrm{h.c.}\Big]ds_2 ds_1$$

$\mathrm{Tr}\,\delta\tilde\rho_B^{(2)}=0$（每对花括号内迹为 0）。✓

#### §2.2 D 的 g² 阶 BKM 展开

总偏离 $\Delta(t)=\rho_B(t)-\rho_B^{ref}=g\,\delta\tilde\rho_B^{(1)}/g+g^2\delta\tilde\rho_B^{(2)}/g^2+\cdots$（薛/相互作用图景下 BKM 度量不变，因 $U_B$ 与 $\rho_B^{ref}$ 对易）。

$$D(\rho_B^{ref}+\Delta\|\rho_B^{ref})=\tfrac12\,\mathrm{Tr}[\Delta\cdot J_{\rho_B^{ref}}^{-1}(\Delta)]+O(\Delta^3)$$

代入 $\Delta=g\cdot\tilde\delta^{(1)}+g^2\tilde\delta^{(2)}+\cdots$（$\tilde\delta^{(1)}=\delta\tilde\rho_B^{(1)}/g$）：

$$D=\frac{g^2}{2}\langle\tilde\delta^{(1)},J^{-1}\tilde\delta^{(1)}\rangle_{HS}+O(g^3)=:g^2 D^{(2)}(t)+O(g^3)$$

#### §2.3 J⁻¹ 在对易子上的解析作用

谱分解 $\rho_B^{ref}=\sum_n q_n|n\rangle\langle n|$，$q_n=e^{-\beta E_n}/Z_B$。
$J(X)_{mn}=X_{mn}\cdot\frac{q_m-q_n}{\ln(q_m/q_n)}$，$\,[\tilde B(s),\rho_B^{ref}]_{mn}=\tilde B(s)_{mn}(q_n-q_m)$。

故
$$J^{-1}\big([\tilde B(s),\rho_B^{ref}]\big)_{mn}=\tilde B(s)_{mn}\cdot\ln\frac{q_n}{q_m}=\beta\omega_{mn}\tilde B(s)_{mn}=\beta[H_B,\tilde B(s)]_{mn}$$

即 **$J_{\rho_B^{ref}}^{-1}([\tilde B(s),\rho_B^{ref}])=\beta\,[H_B,\tilde B(s)]=-i\beta\,\partial_s\tilde B(s)$**（Heisenberg）。

#### §2.4 D^(2)(t) 闭式

$$D^{(2)}(t)=\tfrac12\mathrm{Tr}\!\left[\Big(-i\!\int_0^t\!\!ds_1\,a_1[\tilde B_1,\rho_B^{ref}]\Big)\Big(-\beta\!\int_0^t\!\!ds_2\,a_2\,\partial_2\tilde B_2\Big)\right]$$

$$=\tfrac{i\beta}{2}\!\!\int_0^t\!\!\!\int_0^t\!\!a(s_1)a(s_2)\,\mathrm{Tr}\big([\tilde B_1,\rho_B^{ref}]\,\partial_2\tilde B_2\big)\,ds_1 ds_2$$

迹循环：$\mathrm{Tr}([\tilde B_1,\rho^{ref}]X)=\langle[X,\tilde B_1]\rangle_\beta$，故
$$\mathrm{Tr}\big([\tilde B_1,\rho^{ref}]\partial_2\tilde B_2\big)=\partial_{s_2}\langle[\tilde B(s_2),\tilde B(s_1)]\rangle_\beta$$

定义 $\psi_B(\tau):=\langle[\tilde B(\tau),\tilde B(0)]\rangle_\beta=i\phi_B(\tau)$，$\phi_B$ 实、奇，且 $\phi_B(\tau)=2\chi_B''(\tau)$（标准浴 dissipation）。

$$D^{(2)}(t)=-\frac{\beta}{2}\!\!\int_0^t\!\!\!\int_0^t\!\!a(s_1)a(s_2)\,\phi_B'(s_2-s_1)\,ds_1 ds_2$$

（$\phi_B'$ 偶，被积函数 $s_1\!\leftrightarrow\!s_2$ 对称。）

#### §2.5 Σ_B^int 的闭式核

$$\Sigma_B^{int}(t)=-\frac{d}{dt}D=-g^2\frac{dD^{(2)}}{dt}+O(g^4)$$

对 $D^{(2)}$ 求 $t$ 偏导，两个边界项相等（$\phi_B'$ 偶）：

$$\boxed{\;\Sigma_B^{int}(t)=g^2\!\int_0^t\!ds\;K_B^{(A)}(t,s)+O(g^4),\qquad K_B^{(A)}(t,s)=\beta\,a(t)\,a(s)\,\partial_t\big[2\chi_B''(t-s)\big]\,\theta(t-s)\;}$$

或等价：$K_B^{(A)}(t,s)=2\beta\,a(t)a(s)\,\partial_t\chi_B''(t-s)\,\theta(t-s)$。

#### §2.6 KMS 关系

KMS（Kubo-Martin-Schwinger）：$C_B(t-i\beta)=C_B(-t)$，频率域 $C_B(-\omega)=e^{-\beta\omega}C_B(\omega)$。由此：

- **耗散**：$\chi_B''(\omega)=\tfrac12(1-e^{-\beta\omega})C_B(\omega)$；$\chi_B''$ 奇、实。
- **FDT**：$S_B(\omega)=\tfrac12(C_B(\omega)+C_B(-\omega))=\coth(\beta\omega/2)\,\chi_B''(\omega)$。
- **retarded**：$\chi_B^R(t)=2i\theta(t)\chi_B''(t)$。

代入核：
$$K_B^{(A)}(t,s)=\beta\,a(t)a(s)\,\theta(t-s)\!\int\!\!\frac{d\omega}{\pi}(-i\omega)(1-e^{-\beta\omega})C_B(\omega)e^{-i\omega(t-s)}$$

Bose 因子 $1-e^{-\beta\omega}=2e^{-\beta\omega/2}\sinh(\beta\omega/2)$ 显式承载温度，确保高频 $\omega\gg\beta^{-1}$ 时核被 $\sinh(\beta\omega/2)$ 主导，低频时退化为 $\beta\omega C_B(0)$。**核与 retarded susceptibility 通过 KMS 一一对应、显式 β 同步**。

#### §2.7 极限校验

- **$g\to 0$**：核 $\propto g^2$ 一致地退化。
- **$\rho_S(0)$ 与 $H_S$ 对易且 $[\rho_S,A_S]=0$ 但 $a(s)=\langle A\rangle_S$ 时变性消失** → $a(s)=\mathrm{const}$，核仅含 $\partial_t\chi_B''$ 的时间结构。
- **Ohmic bath, $\tau\to 0$**：$\phi_B'(0)=\langle[[H_B,B],B]\rangle_\beta<0$（典型 oscillator 耦合给 $-2\omega$ 类），$D^{(2)}(t)\sim\beta\omega a^2 t^2/2>0$，符合 $D\ge 0$ 凸性。$\Sigma_B^{int}(t)\sim 2\beta g^2 a^2\phi_B'(0)\,t<0$，与"$D$ 从 0 增长 ⇒ $\Sigma_B^{int}\le 0$ 初始"自洽。

---

### §末 新增卡点

**K3（A 新增）**：$J^{-1}$ 在对易子结构上的化简 $J^{-1}([B,\rho^{ref}])=\beta[H_B,B]$ 仅在 $\rho^{ref}$ 是 $H_B$ 的 Gibbs 时严格成立；若改用 §N.3 提议的瞬时不动点 $\sigma_t=\rho_B^{ref}(\beta_t^*)$，$J^{-1}$ 化简引入额外 $\partial_\beta\sigma$ 项，破坏核的 retarded 形式。**与 B-K1 一致，进一步落实在解析层**。

**K4（A 新增）**：本展开未处理 $a(s)$ 的反应（back-action）——在 g² 阶 $\rho_S(t)$ 自身受浴反作用反演（Born-Redfield），$a(s)=\langle\tilde A(s)\rangle_{\rho_S(0)}$ 用零阶 $\rho_S$。修正项为 g⁴，已在 $O(g^4)$ 中。

---

### 本Phase A 结论（一句话）

$\Sigma_B^{int}(t)=2\beta g^2\!\int_0^t\!ds\,a(t)a(s)\,\partial_t\chi_B''(t-s)+O(g^4)$，闭式核 $K_B^{(A)}$ 通过 KMS $\chi_B''(\omega)=\tfrac12(1-e^{-\beta\omega})C_B(\omega)$ 与浴 retarded 响应一一对应、温度参数同步。

---

## A 对 B Phase 1 的质检报告

### 错误#1 [数据/物理]
**位置**：§A1（"N=1 单振子浴 (Jaynes-Cummings) 闭式"）  
**描述**：B 取 $\rho_B(0)=|0\rangle\langle 0|$（vacuum）但用 $\Sigma_B^{int}=dS_B/dt-\beta\,d\langle H_B\rangle/dt$ 中 β 当作有限自由参数，断言"对任何 β>0 成立"。问题：任务公理要求 $\rho_{SB}(0)=\rho_S(0)\otimes\rho_B^{ref}(\beta)$，即 $\rho_B(0)$ 必须是有限-β Gibbs；vacuum 对应 β=∞，与"任何 β>0"自相矛盾。具体：$D(\rho_B(t)\|\rho_B^{ref}(\beta))$ 当 $\rho_B(0)$=vacuum、$\rho_B^{ref}(\beta)$ 为热态时初值非零（$D(0)=\ln Z_B$），$\Sigma_B^{int}=-\dot D$ 在 $t=0$ 起始基础不是任务约定的 $D(0)=0$。即使数值算式有结果，例子并未落在公理给定的初态家族内。  
**严重**：严重（不是致命，因为可以用真实有限-β 浴的 JC 多模数值/绝热极限补救，但当前 A1 文字给出的"反例"不符合公理设定，逻辑上需要明确声明放宽初态条件）。

### 错误#2 [数学/记号]
**位置**：§A3（"普遍约束尝试"，第 63-64 行）  
**描述**：B 写 $\int_0^\infty\Sigma_B^{int}\,dt=[S_B-\beta\langle H_B\rangle]_0^\infty\le\ln d_B-\beta\langle H_B\rangle_{min}$。右边 $\ln d_B-\beta\langle H_B\rangle_{min}$ 是 $S_B-\beta\langle H_B\rangle$ 在某瞬刻的上界（$S_B\le\ln d_B,\,\langle H_B\rangle\ge\langle H_B\rangle_{min}$），不是其增量 $[\cdots]_0^\infty=f(\infty)-f(0)$ 的上界。正确写法应为 $f(\infty)-f(0)\le(\ln d_B-\beta\langle H_B\rangle_{min})-(S_B(0)-\beta\langle H_B\rangle(0))$，或宽松 $|\Delta f|\le\ln d_B+\beta(\langle H_B\rangle_{max}-\langle H_B\rangle_{min})$。B 的写法漏掉初值减项。  
**严重**：轻微（结论"无 a-priori 符号锁定"不变，仅是上界估计的代数不严）。

### 错误#3 [推导细节/未充分论证]
**位置**：§N.2（"考察我们的 $\rho_B(t)$"）  
**描述**：B 论 $\mathcal G_B(t)\rho_B^{ref}\neq 0$ 的"直觉"基于 $\mathrm{Tr}_S[H_I,\rho_S(0)\otimes\rho_B^{ref}]$。但该量正是 §D.1 中 $i\mathcal D_B(t=0)$。在 $\langle A_S\rangle_{\rho_S(0)}=0$（中心化）情形下，此量为零，单点 $t=0$ 的 $\mathcal G_B(0)\rho_B^{ref}=0$ 反而成立。B 未区分"瞬刻不变"vs"全时段不变"，论证粗糙。修正后：$\mathcal G_B(t\!>\!0)\rho_B^{ref}\neq 0$ 一般成立（高阶 g 反作用打破），但需 g² 显式估计而非"直觉"。  
**严重**：轻微（结论方向正确，仅论据不严密；与本 A.Phase 2 §K3 衔接更精细）。

### 总计
- 数学错误：1（#2 上界写法）
- 数据/物理错误：1（#1 初态-β 错配）
- 逻辑错误：1（#3 论证粗糙）
- 致命：0；严重：1；轻微：2

B 推导的核心 (★)(★★) 算符级身份（§D 全部步骤）经逐行复核**全部正确**：D.1 偏迹三项分解、D.2 中 $[\rho_B,\ln\rho_B]=0$ 的正确使用与迹循环、D.3 Heisenberg、D.4 拼合 $\ln\rho_B+\beta H_B=\ln\rho_B-\ln\rho_B^{ref}$（c-数 $\ln Z_B$ 对易子归零）皆无误，与本 A.Phase 2 §2 的 BKM 展开衔接自洽。

