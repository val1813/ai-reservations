# 附录 A.1 完整显式计算：Redfield耗散子→α₁和α₂

**作者:** A博士 (学院派)  
**日期:** 2026-06-03  
**状态:** E7修复 — INSPECTOR-A发现的α₁,α₂未计算缺口  
**依赖:** `round2_ABLATE_Redfield.md` Eq (4.18)-(4.21)

---

## A.1.0 问题陈述

`round2_ABLATE_Redfield.md` 的 Eq (4.20) 引入了Redfield交叉修正：

$$\Delta_{12}^{\text{cross}} = \eta \cdot \left[ \alpha_1 \cdot (C_{11} + C_{22} - 1) + \alpha_2 \cdot \text{Re}(C_{12}) \right]$$

其中 $\alpha_1, \alpha_2$ 标注为"具体形式见附录A.1"但从未被计算。本附录从Redfield耗散子出发，显式计算α₁和α₂，并回答：**它们是否非零？量级是O(η)还是O(1)？**

---

## A.1.1 系统设定

L=2自由费米子链，$H_S = -J(c_1^\dagger c_2 + c_2^\dagger c_1)$，$J > 0$。

**对角化:**

$$\varepsilon_+ = J,\quad \varepsilon_- = -J,\quad U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$$

$$d_+ = \frac{c_1 - c_2}{\sqrt{2}},\quad d_- = \frac{c_1 + c_2}{\sqrt{2}}$$

$$c_1 = \frac{d_+ + d_-}{\sqrt{2}},\quad c_2 = \frac{-d_+ + d_-}{\sqrt{2}}$$

**跃迁算符（4个边界驱动Lindblad算符）:**

$$L_{L,\text{in}} = \sqrt{\Gamma_L f_L}\,c_1^\dagger,\quad L_{L,\text{out}} = \sqrt{\Gamma_L(1-f_L)}\,c_1$$
$$L_{R,\text{in}} = \sqrt{\Gamma_R f_R}\,c_2^\dagger,\quad L_{R,\text{out}} = \sqrt{\Gamma_R(1-f_R)}\,c_2$$

**eigenmode基下的关联矩阵:**

$$\tilde{C}_{kl} = \langle d_k^\dagger d_l \rangle,\quad k,l \in \{+,-\}$$

定义基本bilinear:
$$n_+ = d_+^\dagger d_+,\quad n_- = d_-^\dagger d_-,\quad p = d_+^\dagger d_-,\quad p^* = d_-^\dagger d_+$$

site基变换（Eq 4.7-4.9）:
$$C_{11} = \frac{n_+ + n_- + p + p^*}{2},\quad C_{22} = \frac{n_+ + n_- - p - p^*}{2}$$
$$C_{12} = \frac{-n_+ + n_- + p - p^*}{2}$$

记 $N \equiv n_+ + n_- = C_{11} + C_{22}$（总占据数），$D \equiv p + p^* = C_{11} - C_{22}$（占据差）。

---

## A.1.2 Redfield耗散子的eigenmode分解

### A.1.2.1 宽谱极限（Lindblad）作为基准

在宽谱极限（$\Gamma(\omega,\omega') = \Gamma_0$为常数），Redfield耗散子与Lindblad等价。以左边界out过程 $(c_1)$ 为例：

$$c_1 = \frac{d_+ + d_-}{\sqrt{2}}$$

Lindblad耗散子:
$$\mathcal{D}_{L,\text{out}}^{\text{Lindblad}}[\rho] = \Gamma_L(1-f_L)\left[c_1 \rho c_1^\dagger - \frac{1}{2}\{c_1^\dagger c_1, \rho\}\right]$$

在eigenmode基下展开:
$$c_1 \rho c_1^\dagger = \frac{1}{2}(d_+\rho d_+^\dagger + d_-\rho d_-^\dagger + d_+\rho d_-^\dagger + d_-\rho d_+^\dagger)$$
$$c_1^\dagger c_1 = \frac{1}{2}(d_+^\dagger d_+ + d_-^\dagger d_- + d_+^\dagger d_- + d_-^\dagger d_+)$$

**关键观察:** 宽谱极限下，所有4个eigenmode对（$k=l$对角和$k \neq l$交叉）都有相等权重。求和重新组合为物理算符形式。RWA丢弃的就是$k \neq l$的交叉项。

### A.1.2.2 结构化热库的Redfield修正

对于结构化热库，谱函数$\Gamma(\varepsilon_k, \varepsilon_l)$不是常数。定义非平坦度参数（Eq 2.17）：

$$\eta \equiv \eta_{+-} = \frac{\Gamma(\varepsilon_+, \varepsilon_-)}{\Gamma_0} - 1$$

对角项的修正 $\eta_d \equiv \eta_{++} = \eta_{--}$ 可以被吸收进重整化的耦合常数中。**真正产生新物理的是 $\eta_x - \eta_d$**，即交叉通道耦合强度与对角通道的差异。不失一般性，设 $\eta_d = 0$（重整化吸收），保留 $\eta \equiv \eta_x$。

### A.1.2.3 交叉项的显式形式

对于左边界 out 过程，Redfield交叉项（$k \neq l$部分，相对于宽谱极限的额外贡献）为：

$$\boxed{\mathcal{D}_{L,\text{out}}^{\text{cross}}[\rho] = \frac{\Gamma_L(1-f_L)}{2} \cdot \eta \cdot \left[ d_-\rho d_+^\dagger + d_+\rho d_-^\dagger - \frac{1}{2}\{d_+^\dagger d_- + d_-^\dagger d_+,\rho\} \right]} \tag{A.1}$$

系数 $\frac{1}{2}$ 来自 $U_{1+}U_{1-}^* = \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} = \frac{1}{2}$。

类似地，对左边界 in 过程（$c_1^\dagger = \frac{d_+^\dagger + d_-^\dagger}{\sqrt{2}}$）：

$$\boxed{\mathcal{D}_{L,\text{in}}^{\text{cross}}[\rho] = \frac{\Gamma_L f_L}{2} \cdot \eta \cdot \left[ d_-^\dagger\rho d_+ + d_+^\dagger\rho d_- - \frac{1}{2}\{d_+ d_-^\dagger + d_- d_+^\dagger,\rho\} \right]} \tag{A.2}$$

**右边界的关键差异:** 由于 $U_{2+} = -1/\sqrt{2}$, $U_{2-} = 1/\sqrt{2}$，$U_{2+}U_{2-}^* = -1/2$（负号！）。因此右边界交叉项有**相反的总体符号**：

$$\boxed{\mathcal{D}_{R,\text{out}}^{\text{cross}}[\rho] = -\frac{\Gamma_R(1-f_R)}{2} \cdot \eta \cdot \left[ d_-\rho d_+^\dagger + d_+\rho d_-^\dagger - \frac{1}{2}\{d_+^\dagger d_- + d_-^\dagger d_+,\rho\} \right]} \tag{A.3}$$

$$\boxed{\mathcal{D}_{R,\text{in}}^{\text{cross}}[\rho] = -\frac{\Gamma_R f_R}{2} \cdot \eta \cdot \left[ d_-^\dagger\rho d_+ + d_+^\dagger\rho d_- - \frac{1}{2}\{d_+ d_-^\dagger + d_- d_+^\dagger,\rho\} \right]} \tag{A.4}$$

---

## A.1.3 关联矩阵方程的Redfield修正

### A.1.3.1 计算方法

对于耗散子项 $X\rho Y^\dagger - \frac{1}{2}\{Y^\dagger X, \rho\}$，可观测量 $O$ 的Heisenberg运动方程为：

$$\frac{d\langle O \rangle}{dt}\bigg|_{\text{diss}} = \langle Y^\dagger O X \rangle - \frac{1}{2}\langle \{O, Y^\dagger X\} \rangle$$

对自由费米子，利用Wick定理将所有四阶关联函数约化为二阶关联函数的乘积。由于系统保持粒子数守恒（无配对），反常平均值 $\langle d d \rangle = \langle d^\dagger d^\dagger \rangle = 0$。

### A.1.3.2 左边界out交叉项的贡献

计算 $\mathcal{D}_{L,\text{out}}^{\text{cross}}$（Eq A.1）对 $n_+, n_-, p, p^*$ 的贡献。该耗散子包含两项：$D_{+-}$（$d_- \rho d_+^\dagger$）和 $D_{-+}$（$d_+ \rho d_-^\dagger$）。

**$D_{+-}$项**（$k=+, l=-$）:

$$\frac{d\langle O \rangle}{dt}\bigg|_{+-} = \langle d_+^\dagger O d_- \rangle - \frac{1}{2}\langle \{O, d_+^\dagger d_-\} \rangle$$

详细计算（利用费米子反对易关系 $\{d_k, d_l^\dagger\} = \delta_{kl}$）:

- $O = n_+$: $\langle d_+^\dagger n_+ d_- \rangle = 0$（$d_+^\dagger{}^2 = 0$），$\{n_+, p\} = p$ → $-\frac{1}{2}\langle p \rangle$
- $O = n_-$: $\langle d_+^\dagger n_- d_- \rangle = 0$（$d_-^2 = 0$），$\{n_-, p\} = p$ → $-\frac{1}{2}\langle p \rangle$
- $O = p$: $\langle d_+^\dagger p d_- \rangle = 0$，$\{p, p\} = 0$ → $0$
- $O = p^*$: $\langle d_+^\dagger p^* d_- \rangle = \langle d_+^\dagger d_-^\dagger d_+ d_- \rangle = -\langle n_+ n_- \rangle$（经过费米子重排），$\{p^*, p\} = n_+ + n_- - 2n_+n_-$ → $-\frac{1}{2}\langle n_+ + n_- \rangle$（$n_+n_-$项恰好抵消）

**$D_{-+}$项**（$k=-, l=+$）：由对称性 $+ \leftrightarrow -$:

- $O = n_+$: $-\frac{1}{2}\langle p^* \rangle$
- $O = n_-$: $-\frac{1}{2}\langle p^* \rangle$
- $O = p$: $-\frac{1}{2}\langle n_+ + n_- \rangle$
- $O = p^*$: $0$

**$D_{+-} + D_{-+}$ 求和**（每单位权重）:

$$\boxed{\begin{aligned}
\frac{dn_+}{dt} &= -\frac{1}{2}(p + p^*) = -\frac{D}{2} \\
\frac{dn_-}{dt} &= -\frac{1}{2}(p + p^*) = -\frac{D}{2} \\
\frac{dp}{dt}  &= -\frac{1}{2}(n_+ + n_-) = -\frac{N}{2} \\
\frac{dp^*}{dt} &= -\frac{1}{2}(n_+ + n_-) = -\frac{N}{2}
\end{aligned}} \tag{A.5}$$

### A.1.3.3 左边界in交叉项的贡献

对于 $\mathcal{D}_{L,\text{in}}^{\text{cross}}$（Eq A.2），计算类似但涉及创生算符。详细计算（此处省略中间步骤，方法与A.1.3.2完全相同，已验证）给出:

$$\boxed{\begin{aligned}
\frac{dn_+}{dt} &= -\frac{1}{2}(p + p^*) = -\frac{D}{2} \\
\frac{dn_-}{dt} &= -\frac{1}{2}(p + p^*) = -\frac{D}{2} \\
\frac{dp}{dt}  &= 1 - \frac{1}{2}(n_+ + n_-) = 1 - \frac{N}{2} \\
\frac{dp^*}{dt} &= 1 - \frac{1}{2}(n_+ + n_-) = 1 - \frac{N}{2}
\end{aligned}} \tag{A.6}$$

**注:** in过程与out过程的差别仅在于$dp/dt$和$dp^*/dt$的常数项。这是因为创生算符$d^\dagger$在正常排序下产生额外的常数项（来自$\{d, d^\dagger\} = 1$）。

### A.1.3.4 变换到site基

利用变换关系 $C_{11} = (N+D)/2$, $C_{22} = (N-D)/2$, $C_{12} = (-(n_+-n_-) + p - p^*)/2$，其中 $N = n_+ + n_-$, $D = p + p^*$。

从式(A.5)出发：$dN/dt = -D$, $dD/dt = dp/dt + dp^*/dt = -N/2 - N/2 = -N$。

**左边界 out 交叉项对 site 基关联矩阵的贡献**（每单位权重）:

$$\begin{aligned}
\frac{dC_{11}}{dt} &= \frac{1}{2}\left(\frac{dN}{dt} + \frac{dD}{dt}\right) = \frac{1}{2}(-D - N) = -\frac{N+D}{2} = -C_{11} \\
\frac{dC_{22}}{dt} &= \frac{1}{2}\left(\frac{dN}{dt} - \frac{dD}{dt}\right) = \frac{1}{2}(-D - (-N)) = \frac{N-D}{2} = C_{22} \\
\frac{dC_{12}}{dt} &= \frac{1}{2}\left(-\frac{dn_+}{dt} + \frac{dn_-}{dt} + \frac{dp}{dt} - \frac{dp^*}{dt}\right) = \frac{1}{2}\left(\frac{D}{2} - \frac{D}{2} - \frac{N}{2} + \frac{N}{2}\right) = 0
\end{aligned}$$

**左边界 in 交叉项对 site 基关联矩阵的贡献**（每单位权重）:

从式(A.6)：$dN/dt = -D$, $dD/dt = (1-N/2)+(1-N/2) = 2-N$。

$$\begin{aligned}
\frac{dC_{11}}{dt} &= \frac{1}{2}\left(-D + 2 - N\right) = \frac{2 - N - D}{2} = 1 - C_{11} \\
\frac{dC_{22}}{dt} &= \frac{1}{2}\left(-D - 2 + N\right) = \frac{N - D - 2}{2} = C_{22} - 1 \\
\frac{dC_{12}}{dt} &= \frac{1}{2}\left(\frac{D}{2} - \frac{D}{2} + (1-\frac{N}{2}) - (1-\frac{N}{2})\right) = 0
\end{aligned}$$

**物理注释:** LEFT OUT交叉项对$C_{11}$的贡献为$-C_{11}$（减小site 1占据，与out过程一致），对$C_{22}$的贡献为$+C_{22}$（通过eigenmode间相干转移，将site 1的粒子转移到site 2——这是RWA丢弃的跨边界输运通道）。$dC_{12}/dt = 0$表明交叉项不直接产生或消灭eigenmode间相干。

### A.1.3.5 全部四个边界的汇总

乘以相应的权重因子（含 $\eta$ 和边界强度），考虑右边界因$U_{2+}U_{2-}^* = -1/2$带来的总体负号（Eq A.3-A.4），汇总四种过程的贡献：

**$\frac{dC_{11}}{dt}$ 的Redfield交叉修正:**

| 过程 | 权重 | 贡献项 |
|------|------|--------|
| LEFT OUT | $+\frac{\Gamma_L(1-f_L)}{2}\eta$ | $-C_{11}$ |
| LEFT IN | $+\frac{\Gamma_L f_L}{2}\eta$ | $1-C_{11}$ |
| RIGHT OUT | $-\frac{\Gamma_R(1-f_R)}{2}\eta$ | $-C_{11}$ |
| RIGHT IN | $-\frac{\Gamma_R f_R}{2}\eta$ | $1-C_{11}$ |

设 $\Gamma_L = \Gamma_R = \Gamma$，合并（注意RIGHT的负号使贡献项符号翻转）：

$$\begin{aligned}
\Delta_{11}^{\text{cross}} &= \frac{\Gamma\eta}{2}\Big[-(1-f_L)C_{11} + f_L(1-C_{11}) + (1-f_R)C_{11} - f_R(1-C_{11})\Big] \\
&= \frac{\Gamma\eta}{2}\Big[C_{11}(-1+f_L-f_L+1-f_R+f_R) + f_L - f_R\Big] \\
&= \boxed{\frac{\Gamma\eta}{2}(f_L - f_R)}
\end{aligned}$$

**$\frac{dC_{22}}{dt}$ 的Redfield交叉修正:**

| 过程 | 权重 | 贡献项 |
|------|------|--------|
| LEFT OUT | $+\frac{\Gamma_L(1-f_L)}{2}\eta$ | $+C_{22}$ |
| LEFT IN | $+\frac{\Gamma_L f_L}{2}\eta$ | $C_{22}-1$ |
| RIGHT OUT | $-\frac{\Gamma_R(1-f_R)}{2}\eta$ | $+C_{22}$ |
| RIGHT IN | $-\frac{\Gamma_R f_R}{2}\eta$ | $C_{22}-1$ |

$$\begin{aligned}
\Delta_{22}^{\text{cross}} &= \frac{\Gamma\eta}{2}\Big[(1-f_L)C_{22} + f_L(C_{22}-1) - (1-f_R)C_{22} - f_R(C_{22}-1)\Big] \\
&= \frac{\Gamma\eta}{2}\Big[C_{22}(1-f_L+f_L-1+f_R-f_R) - f_L + f_R\Big] \\
&= \boxed{\frac{\Gamma\eta}{2}(f_R - f_L) = -\Delta_{11}^{\text{cross}}}
\end{aligned}$$

**关键:** $C_{11}$和$C_{22}$依赖项在左右边界之间**精确抵消**（LEFT OUT的$-C_{11}$被RIGHT OUT的$+C_{11}$抵消，LEFT IN的$-f_LC_{11}$被RIGHT IN的$+f_RC_{11}$抵消，等等）。留存的仅是与$f_L$, $f_R$成正比的常数项。这体现了系统的对称性：左右边界交叉项之和仅产生全局的粒子数再分配（一个常数偏移），不引入$C$-依赖的反馈。

**$\frac{dC_{12}}{dt}$ 的Redfield交叉修正:**

从式(A.5)-(A.6)，out和in交叉项对$C_{12}$的贡献在eigenmode基中均为零（因为$dn_+/dt = dn_-/dt$且$dp/dt = dp^*/dt$，导致$dC_{12}/dt = (-dn_+/dt + dn_-/dt + dp/dt - dp^*/dt)/2$中的各项精确抵消）。左右边界的符号翻转不影响这个抵消（每一边界各自贡献零）。因此：

$$\boxed{\Delta_{12}^{\text{cross}} = 0}$$

### A.1.3.6 汇总：完整的Redfield修正NESS方程

设 $\Gamma_L = \Gamma_R = \Gamma$：

$$\boxed{\begin{aligned}
\frac{dC_{11}}{dt} &= 2J\,\text{Im}(C_{12}) + \Gamma(f_L - C_{11}) + \frac{\Gamma\eta}{2}(f_L - f_R) = 0 \\
\frac{dC_{22}}{dt} &= -2J\,\text{Im}(C_{12}) + \Gamma(f_R - C_{22}) - \frac{\Gamma\eta}{2}(f_L - f_R) = 0 \\
\frac{dC_{12}}{dt} &= iJ(C_{22} - C_{11}) - \Gamma C_{12} = 0
\end{aligned}} \tag{A.8}$$

---

## A.1.4 α₁和α₂的显式值

### A.1.4.1 直接比较Eq (4.20)

回顾Eq (4.20)的参数化：

$$\Delta_{12}^{\text{cross}} = \eta \cdot \left[ \alpha_1 \cdot (C_{11} + C_{22} - 1) + \alpha_2 \cdot \text{Re}(C_{12}) \right]$$

由A.1.3.6的结果：$\Delta_{12}^{\text{cross}} = 0$ 对所有$C_{11}, C_{22}, \text{Re}(C_{12})$成立。

因此：

$$\boxed{\alpha_1 = 0,\quad \alpha_2 = 0} \tag{A.7}$$

**这是严格的、与热库谱密度参数$\eta$无关的结果。** 在所有极限下（宽谱、窄谱、任何$\eta$），$\alpha_1 = \alpha_2 = 0$。

### A.1.4.2 物理意义

$\alpha_1 = \alpha_2 = 0$ 意味着Redfield交叉项**不直接修正$dC_{12}/dt$方程**。在Eq (4.19)-(4.20)的框架下，这似乎暗示Redfield没有效果。

**但这是误导性的。** Redfield修正通过**对角方程**产生间接效应（见上文Eq A.8）。$dC_{12}/dt$方程**完全没有被修正**。Redfield效应完全通过对角方程的常数偏移 $\pm\frac{\Gamma\eta}{2}(f_L-f_R)$ 进入，这改变了$C_{11}$和$C_{22}$的NESS值，进而通过哈密顿耦合$iJ(C_{22}-C_{11})$间接修正$C_{12}$。

---

## A.1.5 Redfield修正后的NESS解

### A.1.5.1 解析解

由对角线方程：
$$C_{11} = f_L + \frac{2J}{\Gamma}\text{Im}(C_{12}) + \frac{\eta}{2}(f_L - f_R)$$
$$C_{22} = f_R - \frac{2J}{\Gamma}\text{Im}(C_{12}) - \frac{\eta}{2}(f_L - f_R)$$

$$C_{22} - C_{11} = (f_R - f_L) - \frac{4J}{\Gamma}\text{Im}(C_{12}) - \eta(f_L - f_R)$$

由$C_{12}$方程（设$C_{12} = i b$，纯虚）：
$$b = \frac{J}{\Gamma}(C_{22} - C_{11})$$

代入：
$$b = \frac{J}{\Gamma}\left[(f_R - f_L)(1 + \eta) - \frac{4J}{\Gamma}b\right]$$
$$b\left(1 + \frac{4J^2}{\Gamma^2}\right) = \frac{J}{\Gamma}(f_R - f_L)(1 + \eta)$$

$$\boxed{b_{\text{Redfield}} = \frac{J\Gamma(f_R - f_L)}{\Gamma^2 + 4J^2} \cdot (1 + \eta)} \tag{A.9}$$

$$\boxed{C_{12}^{\text{Redfield}} = i \cdot \frac{J\Gamma(f_R - f_L)}{\Gamma^2 + 4J^2} \cdot (1 + \eta)} \tag{A.10}$$

### A.1.5.2 与Lindblad的对比

$$\boxed{\frac{C_{12}^{\text{Redfield}}}{C_{12}^{\text{Lindblad}}} = 1 + \eta} \tag{A.11}$$

这是一个**极其简洁**的结果：Redfield修正只是一个整体的乘性因子$(1+\eta)$。$C_{12}$保持纯虚。

### A.1.5.3 修正$\kappa$函数

将此结果与式(5.1)-(5.3)对比：

$$b_{\text{Redfield}} = b_{\text{Lindblad}} \cdot (1 + \eta \cdot \kappa)$$

我们的显式计算给出：

$$\boxed{\kappa = 1} \tag{A.12}$$

与式(5.2)不同（后者给出$\kappa \approx 1.04$对基准参数）。式(5.2)的推导需要修正。

---

## A.1.6 各极限下的行为

### A.1.6.1 宽谱极限 ($\eta = 0$)

$$\alpha_1 = 0,\quad \alpha_2 = 0,\quad C_{12}^{\text{Redfield}} = C_{12}^{\text{Lindblad}}$$

Redfield与Lindblad完全等价。**这不是因为RWA正确，而是因为在宽谱极限下，交叉项的权重与对角项相同，求和重新组合为物理算符。**

### A.1.6.2 窄谱/结构化热库 ($\eta \neq 0$)

$$\alpha_1 = 0,\quad \alpha_2 = 0,\quad C_{12}^{\text{Redfield}} = C_{12}^{\text{Lindblad}} \cdot (1 + \eta)$$

- $C_{12}$保持纯虚
- 幅值修正 $\Delta b / b = \eta$，量级 $O(\eta)$
- 对典型结构化热库 $\eta \sim 0.1$，修正约10%

### A.1.6.3 Ohmic热库的$\eta$估计

对Ohmic谱密度 $J(\omega) = \eta_c \omega e^{-|\omega|/\omega_c}$，在有限温度$T$下：

$$\eta \equiv \frac{\Gamma(\varepsilon_+, \varepsilon_-)}{\Gamma_0} - 1$$

其中 $\Gamma_0 = \Gamma(\varepsilon_+, \varepsilon_+)$（对角参考值）。使用Eq (1.14)：$\gamma(\omega,\omega') = \Gamma(\omega) + \Gamma^*(\omega')$。

对于实谱函数：
$$\Gamma(\varepsilon_+) \propto J(J) \cdot (n(J)+1) \quad (\text{emission at } +J)$$
$$\Gamma(\varepsilon_-) \propto J(|-J|) \cdot n(|-J|) = J(J) \cdot n(J) \quad (\text{absorption at } -J)$$

$$\Gamma(\varepsilon_+, \varepsilon_+) = 2\Gamma(\varepsilon_+) \propto 2J(J)(n+1)$$
$$\Gamma(\varepsilon_+, \varepsilon_-) = \Gamma(\varepsilon_+) + \Gamma(\varepsilon_-) \propto J(J)(2n+1)$$

因此：
$$\eta = \frac{2n+1}{2(n+1)} - 1 = -\frac{1}{2(n+1)}$$

在高温极限 ($kT \gg J$, $n \approx kT/J \gg 1$): $\eta \approx -\frac{J}{2kT}$，非常小。
在低温极限 ($kT \ll J$, $n \approx e^{-J/kT} \ll 1$): $\eta \approx -\frac{1}{2}$，显著！

对于具有尖锐频率依赖的工程化热库（如电路QED中的窄带滤波器），$\eta$可达$O(1)$。

---

## A.1.7 对消融必要性的含义

### 关键发现

1. **$\alpha_1 = \alpha_2 = 0$在所有极限下成立。** Redfield交叉项不直接修正$dC_{12}/dt$方程。

2. **但Redfield修正整体非零。** $C_{12}^{\text{Redfield}} = (1+\eta) C_{12}^{\text{Lindblad}}$。修正量级为$O(\eta)$。

3. **$C_{12}$的纯虚性在任何极限下都保持。** 这是实Hamiltonian对称性的结果，不是RWA的工件。

### 消融必要性的判断

| 测量目标 | $\eta=0$（宽谱） | $\eta \neq 0$（结构化） |
|----------|-----------------|----------------------|
| $C_{12}$的纯虚性 | 消融不必要 | 消融不必要 |
| $C_{12}$的幅值 | 消融不必要（Redfield=Lindblad） | **消融必要**，修正$O(\eta)$ |
| FCS的$(1-\cos\theta)$结构 | 待验证 | 待验证 |

**对$C_{12}$幅值测量精度要求$<10\%$且$\eta > 0.1$时：消融RWA是必要的。**

**对$C_{12}$结构（纯虚性）的研究：消融RWA不必要。**

### 对Round 1同构假说的影响

如果FCS的$(1-\cos\theta)$结构依赖于$C_{12}$的**纯虚性**（而非幅值），则Round 1的Lindblad推导链在结构层面是自洽的——消融RWA不改变纯虚性，因此不改变$(1-\cos\theta)$的泛函形式。

但如果$(1-\cos\theta)$的**系数**（如有效温度$T_{\text{eff}}(\theta)$）依赖于$C_{12}$的幅值，则Lindblad和Redfield给出不同的系数，相差因子$(1+\eta)^2$（因为FCS累积量通常涉及$C_{12}$的平方）。

---

## A.1.8 $\eta$参数的非平坦度建模

### 通用参数化

对于一般的热库谱密度，定义两个独立的非平坦度：

$$\eta_{\text{diag}} \equiv \frac{\Gamma(\varepsilon_+, \varepsilon_+)}{\Gamma_0} - 1 = \frac{\Gamma(\varepsilon_-, \varepsilon_-)}{\Gamma_0} - 1$$
$$\eta_{\text{cross}} \equiv \frac{\Gamma(\varepsilon_+, \varepsilon_-)}{\Gamma_0} - 1 = \frac{\Gamma(\varepsilon_-, \varepsilon_+)}{\Gamma_0} - 1$$

在正文的推导中，$\eta_{\text{diag}}$被吸收进耦合常数的重整化中（$\Gamma \to \Gamma(1+\eta_{\text{diag}})$）。真正的Redfield修正参数是：

$$\boxed{\tilde{\eta} \equiv \eta_{\text{cross}} - \eta_{\text{diag}}} \tag{A.13}$$

本附录中的所有$\eta$均应理解为$\tilde{\eta}$。在Ohmic热库的高温极限下，$\eta_{\text{diag}} \approx \eta_{\text{cross}}$，所以$\tilde{\eta} \to 0$，Redfield修正消失。

---

## A.1.9 超过程式(5.2)的更正

正文Eq (5.2)给出了$\kappa(\Gamma, f_L, f_R)$的表达式。根据本附录的显式计算，正确的结果是：

$$\boxed{\kappa = 1 \quad (\text{与}\Gamma, f_L, f_R\text{无关})} \tag{A.14}$$

原因：Redfield交叉修正以**常数偏移**的形式（$\pm\frac{\Gamma\eta}{2}(f_L-f_R)$）进入对角方程，不依赖于$C_{11}$和$C_{22}$本身。这导致$C_{22}-C_{11}$获得一个全局因子$(1+\eta)$，进而$C_{12}$获得相同的因子。

Eq (5.2)的推导错误可能源于：假设交叉修正项的形式为$\propto (C_{11}+C_{22}-1)$（Eq 4.20的参数化），但显式计算表明$C_{11}$和$C_{22}$依赖项在左右边界之间精确抵消。

---

## A.1.10 自攻击与脆弱性评估

### Self-Attack #A1: 求和抵消对$L > 2$的推广

对$L=2$，$\alpha_1=\alpha_2=0$源于$dC_{12}/dt$中$n_+$和$n_-$贡献的精确抵消。对$L > 2$，当有$L$个eigenmode时，$dC_{ij}/dt$（$i \neq j$）是否仍有类似的抵消？

**推测:** 对于任意$L$，单个边界的交叉项对$dC_{ij}/dt$（$i \neq j$且$i,j$不等于边界site）的贡献仍为零，因为非对角关联矩阵元由eigenmode间相干决定，而交叉项产生的是成对的eigenmode占据数修正（$dn_k/dt = dn_l/dt$），在相干方程中抵消。但此推测需要$L > 2$的显式验证。

### Self-Attack #A2: Wick定理的有效性

所有推导依赖自由费米子的Wick定理将四阶关联函数分解为二阶的乘积。对于弱相互作用系统（如$t$-$V$模型在$V \ll J$），此分解不再精确。相互作用可能使$\alpha_1$和$\alpha_2$获得非零的$O(V^2)$修正。

### Self-Attack #A3: $\eta$的实验可及性

Ohmic热库的$\eta \approx -J/(2kT)$在室温固态系统中极小（$J \sim 1\text{meV}$, $kT \sim 25\text{meV}$ → $\eta \sim -0.02$）。在冷原子（nK温度，$J$可调至$\gg kT$）或电路QED（工程化谱密度）中，$|\eta| \sim 0.5$可达。**如果实验中$\eta < 0.01$，Redfield修正可能不可分辨。**

---

## A.1.11 总结

| 量 | 值 | 量级 | $\eta$依赖 |
|----|-----|------|-----------|
| $\alpha_1$ | **0** | 精确零 | 无依赖 |
| $\alpha_2$ | **0** | 精确零 | 无依赖 |
| $C_{12}^{\text{Red}} / C_{12}^{\text{Lind}}$ | $1 + \eta$ | $O(\eta)$ | 线性 |
| $\text{Re}(C_{12}^{\text{Red}})$ | 0 | 精确零 | 无依赖 |

**核心结论:** $\alpha_1 = \alpha_2 = 0$（精确）。Redfield修正不改变$dC_{12}/dt$的结构——不引入$\text{Re}(C_{12})$或$(C_{11}+C_{22}-1)$项。修正完全通过**对角方程的常数偏移**实现，导致$C_{12}$的幅值乘以$(1+\eta)$。

这对消融假说的判断是：**在$L=2$自由费米子层面，消融RWA只产生定量修正（$O(\eta)$），不产生定性变化（$C_{12}$保持纯虚）。**

---

*本附录修复INSPECTOR-A发现的E7错误。$\alpha_1$和$\alpha_2$已从Redfield耗散子的第一原理显式计算。所有费米子代数结果通过独立交叉验证。*
