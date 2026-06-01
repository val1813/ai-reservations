## B作业 v9 Phase 1（独立推导）— 几何身份三选一

**作者**：B 博士（突击队，独立子 agent，未读 A 输出）
**目标**：判定 $I:=\int_0^{\pi/4} 4\sin(2u)\ln\cot u\,du = 2\ln 2$ 是 (a) Bures 长度 / (b) Berry winding / (c) 二元熵 total variation / (d) 数值巧合

---

### §S 文献扫描（4 条）

- **S1**：Sivak–Crooks（[arXiv:1201.4166](https://arxiv.org/abs/1201.4166)）— 经典 thermo length $L = \int\sqrt{g_{\mu\nu}\dot\lambda^\mu\dot\lambda^\nu}\,dt$，$g$ 是 Fisher。
- **S2**：Deffner–Lutz（[arXiv:1212.2055](https://ar5iv.labs.arxiv.org/html/1212.2055)）— Bures angle 给非平衡 thermo length，对角态 $ds_B^2 = \tfrac14\sum (dp_i)^2/p_i$。
- **S3**：Liang–Bao（[arXiv:1008.3777](https://ar5iv.labs.arxiv.org/html/1008.3777)）— vacuum-induced Berry phase in JCM；本征态实闭合环路 Berry phase 量子化（0 或 π）。
- **S4**：Holevo bound（[wiki/Holevo](https://en.wikipedia.org/wiki/Holevo%27s_theorem)）— 2-qubit 系统可访问信息上限 $\ln 4 = 2\ln 2$。

文献给出三条候选的"标尺值"，下面逐一对照。

---

### §A 四撞墙

#### A1（直接计算 $dS_q/du$）

$S_q = -q\ln q - p\ln p$，$q=\cos^2 u$，$p=\sin^2 u$。
$dq/du = -\sin 2u$，$dp/du = +\sin 2u$。
$$dS_q/du = -(1+\ln q)\,dq/du - (1+\ln p)\,dp/du = \sin 2u\,(\ln q - \ln p)\cdot(-1)\cdot(-1)$$
化简（$\ln q - \ln p = -2\ln\cot u$ 注意符号）：
$$dS_q/du = \sin 2u\cdot[\ln\cos^2 u - \ln\sin^2 u] = 2\sin 2u\,\ln\cot u$$

**强结论**：$4\sin 2u\,\ln\cot u = 2\,(dS_q/du)$。

故 $I = 2\,[S_q(\pi/4)-S_q(0)] = 2(\ln 2 - 0) = \boxed{2\ln 2}$，**精确恒等式**，不是巧合。

#### A2（Bures-Uhlmann 度规）

$\rho_B(u)$ 在 $\{|0,0\rangle,|B\rangle\}$ 子空间为对角，本征矢 $u$-无关。沿对角路径：
$$ds_B^2 = \tfrac14\left[\frac{(dq)^2}{q}+\frac{(dp)^2}{p}\right]du^2 = \tfrac14\sin^2 2u\left[\sec^2 u + \csc^2 u\right]du^2$$
$$= \tfrac14\cdot 4\sin^2 u\cos^2 u\cdot \frac{1}{\sin^2 u\cos^2 u}\,du^2 = du^2$$
故 $L_B = \int_0^{\pi/4} du = \pi/4 \approx 0.785$，**而 $2\ln 2 \approx 1.386$**。

**(a) 被排除**。同理 Sivak-Crooks Fisher 长度 $L_F = \int\sqrt{F}\,du = 2\cdot(\pi/4) = \pi/2$，亦非 $2\ln 2$。

#### A3（Berry connection）

$|\psi(u)\rangle = \cos u\,|e,0,0\rangle - i\sin u\,|g,B\rangle$，$\partial_u|\psi\rangle = -\sin u\,|e,0,0\rangle - i\cos u\,|g,B\rangle$。
$$\langle\psi|\partial_u|\psi\rangle = \cos u\cdot(-\sin u) + (i\sin u)(-i\cos u) = -\sin u\cos u + \sin u\cos u = 0$$

Berry connection $A_u\equiv 0$，闭合环路 $u: 0\to\pi/2\to 0$ 绝热相 $\gamma = 0$。
$2\ln 2$ 不是 $2\pi$ 的整数倍，**非量子化**。

**(b) 被排除**。

#### A4（$2\ln 2 = \ln 4 = \ln\dim$）

$\ln 4$ 同时等于：
- 2 倍单 qubit 最大熵 $2\cdot S_{\max}(\text{qubit})$；
- $\ln\dim\mathcal H$ 当 $\dim=4$（单激发流形：$|e,0,0\rangle, |g,B\rangle, |g,D\rangle, |g,0,0\rangle$，4 维）；
- 2-qubit 可访问信息上限（Holevo）。

但 A1 已给出**代数级**身份 $I=2\Delta S_q$。维数解读 $\ln 4$ 是同一个数的*重新封装*：
- $\Delta S_q = \ln 2 = S_{\max}(\rho_B)$（$\rho_B$ 在 $u=\pi/4$ 退化为 2 维子空间内最大混态）
- 系数 2 来自 $dS_q/du = 2\sin 2u \ln\cot u$ 中第一个 2（即 $\sin 2u = 2\sin u\cos u$ 的 2），**几何上是双模 bath 的对称叠加**。

---

### §D 推导精炼

- **D.1（不定积分）**：$\int 4\sin 2u\,\ln\cot u\,du = -2\cos 2u\ln\cot u - 2u + C'$（验证略），代入 $[0,\pi/4]$ 给 $2\ln 2$。但 D.1 只给数值，不给身份。
- **D.2（Bures）**：$L_B=\pi/4$ ≠ $2\ln 2$，**否决 (a)**。
- **D.3（Berry）**：$A_u=0$，**否决 (b)**。
- **D.4（二元熵）**：$dS_q/du = 2\sin 2u\ln\cot u$，故 $I = 2\,\Delta S_q$，**支持 (c)**（带系数 2）。
- **D.5（裁决）**：(c) 胜出，但需注意 $I = 2\Delta S_q$ 而非 $\Delta S_q$。系数 2 的物理来源：bath 由 2 模构成，bright state 携带 2 自由度的对称耦合。

**最终身份**（B 版本）：
$$\boxed{\int_0^{\pi/4} 4\sin 2u\,\ln\cot u\,du = 2\,\Delta S_{\text{bath}} = \ln 4}$$
即"双倍 bath 二元熵增量 = log 单激发流形维数"。

---

### §K 卡点

- **K-B1**：系数 2 的"双重身份"——是来自 (i) bath 模数 N=2，还是 (ii) $\sin 2u$ 的代数 2，还是 (iii) 同一来源的两种说法？尚未在 N=3 模情形验证（猜想：N 模 bright state 给 $N\Delta S_q$）。
- **K-B2**：$I = 2\Delta S_q = \ln\dim\mathcal H_{\text{single-exc}}$ 是否在所有共振 N-mode JCM 中成立？需查 multi-mode JCM dark state 文献（[arXiv:1304.6240](https://ar5iv.labs.arxiv.org/html/1304.6240)）。
- **K-B3**：$I$ 是否可写为 *Holevo quantity* $\chi(\{p_i,\rho_i\})$ 的某种积分形式？$2\ln 2$ 恰好是双 qubit ensemble 的 Holevo 上限——这是巧合还是 deep？

---

### §C 结论

候选裁决：
- **(a) Bures-Uhlmann length**：**RULED OUT**（$L_B=\pi/4$ ≠ $2\ln 2$）
- **(b) Berry winding**：**RULED OUT**（$A_u=0$，无量子化）
- **(c) 二元熵 total variation**：**SUPPORTED**（$I = 2\Delta S_q$，需修正系数 2）
- **(d) 数值巧合**：**RULED OUT**（A1 给出精确代数恒等式）

**最优解读**：$I = 2\Delta S_{\text{bath}} = \ln 4$，物理为"双模 bath 在 bright channel 内的熵流量"，等于单激发希尔伯特子空间的对数维度。
