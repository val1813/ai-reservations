# LP18 Round 1 - A博士正方链审查

角色：A博士（学院派）。本轮只重建与审查 Costa/Ribeiro/De Luca arXiv:2504.00188v3 的正方定理链：Noisy XX -> QSSEP -> Gauge trick -> SSEP CGF。

## §-1 先发文献检索

检索工具：优先使用 paper-search-mcp；本轮未使用 web。检索时间：2026-06-03。

### 检索组1：核心论文与版本

查询：`2504.00188`；`"Emergence of universality in transport of noisy free fermions"`。

命中：
- R1: Joao Costa, Pedro Ribeiro, Andrea De Luca, "Emergence of universality in transport of noisy free fermions", arXiv:2504.00188v3, updated 2026-05-29；CrossRef/PRL DOI: 10.1103/v8x8-ft81, published 2026-05-27.

结论：R1 是本轮正方链的主文献，且 v3 已含 Supplement A-K；应以 arXiv v3 方程号为主。

### 检索组2：QSSEP 原型与稳态相干涨落

查询：`QSSEP quantum symmetric simple exclusion process Bernard Jin transport fluctuations`。

命中：
- R2: Denis Bernard, Tony Jin, "Open Quantum Symmetric Simple Exclusion Process", arXiv:1904.01406v3 / PRL 123, 080601 (2019).
- R3: Bernard/Jin 后续连续极限与 QSSEP 文献，包括 CMP 384, 1141-1185 (2021), SciPost/Ann. Henri Poincare 系列。

关键公式定位：
- R2 Eq. (1)-(4): QSSEP Brownian hopping Hamiltonian与边界 Lindblad。
- R2 Eq. (5): 平均密度线性剖面。
- R2 Eq. (6)-(8): coherence loop 的 leading scaling。
- R2 Eq. (9)-(11): loop cumulant 的边界与 contact matching 条件。
- R2 Eq. (13)-(14): `F(A)=lim_{L->infty} L^{-1} log [exp Tr(AG)]` 的大偏差生成函数。
- R2 Eq. (16)-(17): 平均动力学退化为 classical SSEP，且 SSEP 密度 cumulants 可由 QSSEP loop 求和得到。

结论：R1 的 QSSEP 中间层不是新模型凭空假设，而是接在 Bernard/Jin 的 open QSSEP 稳态涨落结构上。

### 检索组3：SSEP/MFT 电流 CGF 基线

查询：`SSEP current cumulant generating function open system Derrida Lebowitz macroscopic fluctuation theory`。

命中：
- R4: Derrida, Lebowitz, Speer, arXiv:cond-mat/0109346v3 / J. Stat. Phys. 107, 599-634 (2002): open SSEP 非平衡稳态大偏差泛函。
- R5: Bodineau, Derrida, PRL 92, 180601 (2004): additivity principle/MFT 电流大偏差。
- R6: Derrida, J. Stat. Mech. 2007/2011 综述与 SSEP exact CGF 公式（R1 引 Ref. [82-85]）。

结论：R1 Eq. (12) 的 `arccosh/arccos` 形式是经典 SSEP/MFT 已知结果的再推导，而不是另一个待证假设。

### 检索组4：R1 后增量与边界检索

查询：`Universal classical and quantum fluctuations large deviations current QSSEP QSSIP`；`long range free fermion hopping dephasing transport fractional diffusion`；`Levy flights exclusion process long jumps hydrodynamic limit fractional Laplacian`。

命中：
- R7: Mathias Albert, Denis Bernard, Tony Jin, Stefano Scopa, Shiyi Wei, "Universal classical and quantum fluctuations in the large deviations of current of noisy quantum systems: The case of QSSEP and QSSIP", arXiv:2601.16883v1.
- R8: Subhajit Sarkar, Bijay Kumar Agarwalla, Devendra Singh Bhakuni, "Impact of dephasing on non-equilibrium steady-state transport in fermionic chains with long-range hopping", arXiv:2310.01323v2 / PRB 109, 165408 (2024).
- R9: Milton Jara, "Hydrodynamic limit of particle systems with long jumps", arXiv:0805.1326v2.
- R10: Cedric Bernardin, Byron Jimenez Oviedo, "Fractional Fick's law for the boundary driven exclusion process with long jumps", arXiv:1603.01234v3 / ALEA 14, 473 (2017), DOI 10.30757/alea.v14-25.

关键定位：
- R7 Introduction/Sec. VII and Eq. (45): 量子电流方差的 subleading correction，`partial_u^2 delta F_qu(u)|_{u=0}=-(n0-nN)^2/(3N)`；Appendix E Eq. (E10) 给独立推导。
- R8 abstract: 长程 hopping `~1/r^alpha` 去相干费米链在 `alpha~O(1)` 出现 superdiffusive regime，估计 `alpha_c approx 1.5`。
- R9 abstract: exclusion/zero-range long jumps 的 hydrodynamic limit 是 fractional heat equation，标度 superdiffusive。
- R10 title/abstract: boundary-driven long-jump exclusion obeys fractional Fick law/fractional hydrostatics。

结论：有限尺寸修正已被 R7 覆盖；长程 hopping 仍是 R1 明确列出的 open question，且有独立长跳排斥/分数扩散文献支撑，是本轮最小增量候选。

## §0 框架声明

采用成熟框架：开放量子系统 + Macroscopic Fluctuation Theory (MFT)。

开放量子系统部分负责从随机 Hamiltonian/Lindblad 增量得到 correlation matrix 的随机闭合方程，并解释 Markovian reservoir、counting field、two-time/tilted Lindblad 的合法性。MFT 部分负责解释 large-L diffusive scaling 下为什么只剩扩散系数/迁移率，以及为什么 classical SSEP CGF 是合适基线。

本轮不重新发明 continuum Q-MFT，只审查 R1 如何在 QSSEP 格点代表中实现：Noisy XX 的强噪声/大尺寸约化给 QSSEP；QSSEP 的 current CGF 通过 gauge trick 退化为 SSEP/MFT 的 Hamilton 方程与已知 CGF。

## 1. 定理链重建

### Step 1: Noisy XX 的开放量子模型

R1 从一维 spinless free fermion chain 出发。确定性 hopping 取
`H0=-sum_{j=1}^{L-1}(c_j^\dagger c_{j+1}+c_{j+1}^\dagger c_j)`，噪声 Hamiltonian 增量为
`dH=H0 dt + sqrt(gamma) sum_j n_j dW_j`。Ito 展开给出 unitary/noise 部分：

`[d rho]_uni = -i[dH,rho] + gamma sum_j D_{n_j}[rho] dt`。

来源：R1 Eq. (1)。

边界 reservoir 由 Lindblad jump operators
`L_(alpha,1)=sqrt(Gamma_{alpha,1}) c_{j_alpha}^\dagger`，
`L_(alpha,-1)=sqrt(Gamma_{alpha,-1}) c_{j_alpha}` 给出。

来源：R1 Eq. (2)-(3)。

审查：这一步完全在标准 Markovian open quantum systems 内。限制条件已经写死：free, quadratic, U(1)-conserving, Markovian boundary reservoirs, local dephasing noise。

### Step 2: strong dephasing / thermodynamic limit -> QSSEP

R1 的物理等价是：固定 `gamma>0` 而 `L->infty` 时，粒子穿越系统累计的去相干次数随 `L` 增长；diffusive timescale `t_Diff~L^2` 支配 `t_deph~1/gamma`。因此大尺寸极限与先取强去相干极限在 leading diffusive sector 等价。

在 `gamma->infty` 并 rescale `t -> gamma t/2` 后，Noisy XX 的剩余动力学为 QSSEP。QSSEP Hamiltonian 增量：

`dH = sum_{j=1}^{L-1}(d xi_j c_{j+1}^\dagger c_j + d xi_j^* c_j^\dagger c_{j+1})`，
`d xi_j d xi_k^* = dt delta_{j,k}`。

对应 Lindblad/Ito unitary 部分：

`[d rho]_uni = -i[dH,rho] + sum_{j=1}^{L-1}(D_{L_j}[rho]+D_{L_j^\dagger}[rho])dt`，`L_j=c_{j+1}^\dagger c_j`。

来源：R1 Eq. (4)。

边界细节：R1 说明 open chain 的强噪声等价见 Supplement Sec. C；映射到少两个 sites 的 QSSEP，且 `tilde Gamma_{alpha,sigma}=Gamma_{alpha,sigma}/(Gamma_{alpha,-1}+Gamma_{alpha,1})`。边界密度在 thermodynamic limit 中只留下
`rho_alpha=Gamma_{alpha,1}/(Gamma_{alpha,1}+Gamma_{alpha,-1})`。

来源：R1 正文 "Local observables and mapping to QSSEP" 段；Supplement Sec. C。

审查：这是正方链中第一个强假设点。R1 用 Supplement J 支撑限次序：对 `gamma^{-1}` 的高阶项产生高阶离散导数，在 diffusive scaling `tau=t/L^2` 下被 `L^{-2}` 或更高阶抑制。关键公式为 R1 Supplement Eq. (SJ.1)-(SJ.9)，尤其 Eq. (SJ.6)-(SJ.9)。

### Step 3: transport observable 与 CGF

R1 定义右 reservoir 转移电荷：

`P_t(Delta N_R)=sum_N delta(N-N0-Delta N_R) P_R(N,t)`。

来源：R1 Eq. (5)。

长时大偏差：

`P_t(Delta N_R) ~ exp[-I(Delta N_R/t)t]`，CGF
`lambda(s)=lim_{t->infty} t^{-1} log Tr[rho_T exp(s Delta N_R(t))]`，
`I(J)=sup_s(sJ-lambda(s))`。

来源：R1 "Transport Observables" 段，紧接 Eq. (5) 后的定义。

引入 pseudo density matrix `rho_{T,s}=exp(s N_R/2) rho_T exp(s N_R/2)` 后，tracing reservoirs 得到 tilted stochastic Lindblad equation：

`d rho_s=[d rho_s]_uni+[d rho_s]_bath+sum_sigma (e^{-sigma s}-1)L_{R,sigma} rho_s L_{R,sigma}^\dagger dt`。

来源：R1 Eq. (6)。

CGF 由 trace growth 得到：

`lambda(s)=lim_{t->infty} t^{-1} log Tr rho_s(t)=lim_{t->infty} d_t log Tr rho_s(t)`。

来源：R1 Eq. (7)。

进一步得到边界表达：

`lambda(s)=sum_sigma Gamma_{R,sigma}(e^{-sigma s}-1)(delta_{sigma,1}-sigma E_infty[(G_s)_{L,L}])`。

来源：R1 Eq. (8)。

但 `G_s` obeys nonlinear SDE，moments hierarchy：

`partial_t G_s^{otimes n}=F^(n)[{G_s^{otimes m}}_{m=n-1}^{n+1}]`。

来源：R1 Eq. (9)。

审查：有限 `L` 的 `lambda(s)` 仍需解无限 hierarchy。R1 的普适性定理不是有限尺寸精确等价，而是 leading large-L CGF 等价。

--- INSPECTOR_CHECK ---
[公式] `lambda(s)=sum_sigma Gamma_{R,sigma}(e^{-sigma s}-1)(delta_{sigma,1}-sigma E_infty[(G_s)_{L,L}])`，SI 单位为 `time^{-1}`；若采用 R1 的 rescaled `tilde lambda=(gamma L/2)lambda`，则无量纲。
[方向] transport CGF 已从 reservoir counting field 降为 tilted correlation matrix 的边界密度问题；有限 L 仍未闭合。
[数据] Costa/Ribeiro/De Luca arXiv:2504.00188v3 Eq. (5)-(9)；Markovian Lindblad counting field 标准构造。
[假设] Markovian reservoirs；long-time self-averaging；Gartner-Ellis 光滑性；quadratic dynamics 保持 gaussianity。

### Step 4: gauge trick 把电流测量点移入 bulk

R1 利用局域守恒：任意 bond `j` 的累计电荷
`Delta N_j = Delta N_R + sum_{i>j} Delta n_i`
与 `Delta N_R` 在 `t->infty` 下有同一 rate function。更一般地，对 normalized weights `f_j`，`sum_j f_j=L+1`，组合电流 `Delta N[f]=(L+1)^{-1}sum_j f_j Delta N_j` 仍有同一大偏差。

来源：R1 Eq. (10) 前正文；严谨证明见 Supplement Sec. D。

在 large-L QSSEP 中，定义 `g_s(x)=lim_{L->infty} E_infty[(G_s)_{xL,xL}]`，并令 `f_j -> f(x)`，可把 rescaled CGF 写成

`tilde lambda(s)=-s int_0^1 dx f^2(x) [partial_x g_s(x)/f(x) - s g_s(x)(1-g_s(x))]`。

来源：R1 Eq. (10)。

选择 gauge `f_s(x)` 满足

`partial_x f_s(x)=s f_s^2(x)(2g_s(x)-1)`，

则高阶 moments 对 `g_s` 的反馈被消去，`g_s` 闭合为可解 ODE。

来源：R1 Eq. (11)；Supplement Eq. (SA.4) 及 Appendix I 的 hierarchy scaling 论证。

审查：这是定理链的核心创新。它不声称 quantum coherences 消失，而是说在该 gauge 与 leading large-L current CGF 中，unknown two-point/higher-loop scaling function 不再进入 `g_s` 的闭合方程。R2 的 loop cumulants 仍存在，R7 也显示它们在 subleading current cumulants 中重新出现。

### Step 5: QSSEP CGF = SSEP CGF

解 gauge-fixed 方程后，R1 得到

`tilde lambda(s)=Theta(w_s-1) [arccosh(w_s)]^2 - Theta(1-w_s)[arccos(w_s)]^2`,

其中

`w_s=sqrt((1+(e^s-1) tilde Gamma_{L,1})(1+(e^{-s}-1) tilde Gamma_{R,1}))`。

来源：R1 Eq. (12)。

在 thermodynamic boundary-density notation 下，`tilde Gamma_{L,1}=rho_L`、`tilde Gamma_{R,1}=rho_R`，即

`w_s=sqrt((1+(e^s-1)rho_L)(1+(e^{-s}-1)rho_R))`。

R1 明确说明 Eq. (12) 与 SSEP 已知结果一致；并且同一 gauge freedom 可直接用于 SSEP，给出对经典结果的新推导。

来源：R1 Eq. (12) 后正文；SSEP 基线见 R1 Refs. [82-85]，与本轮检索 R4-R6 一致。

审查：在正方假设集合内，链条闭合：

`Noisy XX (Eq. 1-3)` -> `QSSEP (Eq. 4 + Supplement C/J)` -> `tilted CGF (Eq. 5-9)` -> `gauge-distributed current (Eq. 10)` -> `gauge condition (Eq. 11)` -> `SSEP CGF (Eq. 12)`。

等价命题应精确表述为：

在一维、spinless、U(1)-conserving、free fermion、unitary noise、quasi-local hopping、Markovian reservoirs、large-L diffusive scaling 下，电荷 transport CGF 的 leading term 与 classical SSEP 相同；quantum coherences 只在系统观测量或 subleading transport corrections 中保留。

## 2. 正方链薄弱点

1. `L->infty` 与 `gamma->infty` 的交换不是严格全阶定理。R1 Supplement J 给强证据：高阶 `gamma^{-1}` 项对应高阶离散导数并在 diffusive scaling 中被压低；但 generic `n` 与 contact/boundary 全证明仍有技术缺口。

2. Eq. (11) 的 gauge closure 依赖 hierarchy scaling 假设。R1 Supplement I 对 `n=2` 做显式检查，并说 generic `n` 结构类似但复杂，留作未来工作。故 “all cumulants” 的严格性比 “low cumulants/leading CGF” 弱。

3. 普适性不覆盖 finite-size quantum corrections。R7 已显示 current variance/skewness 有 `O(1/N)` 量子项，R7 Eq. (45) 和 Appendix E Eq. (E10) 给出方差修正。

4. 普适性明确依赖 quasi-local hopping。R1 在 Eq. (12) 后正文只把结论推广到 `J_{j,k}->0 sufficiently fast with |j-k|` 的 quasi-local quadratic Hamiltonian；long-range hopping 被 R1 结论段列为 natural open question。

## 3. R1 仍未覆盖的最小增量候选

我选择：长程 hopping 的 quasi-locality 失效边界。

不选择有限尺寸修正：R7 已经把 QSSEP/QSSIP current statistics 的 leading finite-size quantum corrections 推进到明确公式，尤其 Eq. (45) 和 Appendix E Eq. (E10)。这仍有价值，但已经不是 R1 未覆盖的最小干净增量。

不选择高维边界：R1 Supplement K 已给出高维 QSSEP 的 gauge trick，核心公式为 Eq. (SK.8)-(SK.20)。其中 Eq. (SK.20) 得到 `tilde lambda_d(s)=C_Lambda tilde lambda_1d(s)`，几何只通过 harmonic conductance `C_Lambda=int_Lambda |grad u|^2` 进入。该方向可审查但不是空白。

不优先选择相互作用：R1 结论列为 open question，R7 也提示相互作用中的 quantum correction 是否保留仍开放；但这需要超出 free/Gaussian closure，第一轮 A 侧可控性较差。

### 最小模型

取 Noisy XX 的 deterministic hopping 改为 power-law：

`H0^{LR}=-sum_{1<=j<k<=L} J_{j,k}(c_j^\dagger c_k+c_k^\dagger c_j)`，
`J_{j,k}=J0/|j-k|^alpha`，仍保留 local dephasing `sqrt(gamma) sum_j n_j dW_j` 与同样 Markovian reservoirs。

在 strong dephasing/quantum Zeno 投影后，二阶虚跃迁应产生 classical long-jump exclusion 有效 rates

`r_{j,k} ~ |J_{j,k}|^2/gamma ~ |j-k|^{-2alpha}/gamma`。

若把 long-jump exclusion 的传统写法 `p(r)~|r|^{-1-mu}` 对齐，则 `mu=2alpha-1`。当 `mu<2`，即 `alpha<3/2`，二阶矩发散，hydrodynamic generator 不再是 Laplacian，而是 fractional Laplacian；这与 R8 的数值临界 `alpha_c approx 1.5` 和 R9/R10 的 long-jump exclusion 分数扩散文献相吻合。

候选命题：

`alpha>3/2`：有效长跳 rates 有有限二阶矩，R1 的 quasi-local/diffusive gauge trick 可能仍给 SSEP CGF，只是扩散常数/电导重整化。

`1<alpha<3/2`：hydrodynamic scaling 变为 superdiffusive/fractional；R1 Eq. (10)-(12) 的 diffusive MFT/SSEP CGF 不再是正确 leading CGF。预期应出现 fractional-SSEP 或 long-jump exclusion 的 current large deviation，而非普通 SSEP。

`alpha<=1`：总 hopping 强度/边界到 bulk 的非局域耦合更奇异；局域守恒下的 bond-current gauge 描述本身可能需要重定义为非局域 jump current network。

最小可计算量：

先只计算二阶 cumulant 的系统尺寸标度。R1 普通 SSEP 预言 `lambda''(0) ~ const/L`；长程候选预言在 `1<alpha<3/2` 区间改为 `lambda''(0) ~ L^{-(2alpha-2)}` 或等价的 fractional conductance 标度（需按具体 reservoir 实现校准）。若数值或解析 Zeno projection 支持该标度，即构成对 R1 普适边界的最小反例型增量。

--- INSPECTOR_CHECK ---
[公式] `r_{j,k} ~ |J_{j,k}|^2/gamma = J0^2/(gamma |j-k|^{2alpha})`，SI 单位为 `time^{-1}`；二阶矩条件 `sum_r r^2 r^{-2alpha}<infty` 等价 `alpha>3/2`。
[方向] 长程 hopping 的最小增量不是改 gauge trick 的细节，而是先改 hydrodynamic universality class：diffusive Laplacian -> fractional generator。
[数据] R1 Eq. (12) 后 quasi-local 条件与结论 open question；R8 arXiv:2310.01323v2/PRB 109, 165408 的 `alpha_c approx 1.5`；R9 arXiv:0805.1326v2；R10 arXiv:1603.01234v3/DOI 10.30757/alea.v14-25。
[假设] Strong dephasing Zeno projection 可推广到 power-law hopping；effective jump rate 按二阶 Schrieffer-Wolff/Golden-rule 标度 `|J|^2/gamma`；reservoir coupling 不引入额外长程边界跳。

## 4. 深挖1：本轮结论的下一层后果

第一层后果：如果 R1 正方链成立，则 leading current LDF 的 “classicality” 并不等于 QSSEP 中 quantum coherence 消失。R2 Eq. (6)-(8) 已显示 off-diagonal coherence loop 的 connected moments 以 `1/L`、`1/L^{N-1}` 标度保留；R1 gauge trick 只是让它们不进入 leading current CGF。

第二层后果：因此真正可发表的边界不是“有没有 quantum coherence”，而是“quantum coherence 何时重新进入可测 transport cumulants”。R7 的结果说明在有限尺寸 `O(1/N)` 层级，coherence-loop `g2(x,y)~N E[G_ij G_ji]` 会进入 current variance/skewness；本项目可沿长程 hopping 检查：当 fractional hydrodynamics 改变 leading scaling 时，coherence-loop 是否从 subleading 被提升为 leading 或同阶。

## 5. 深挖2：本轮依赖前提中最可能出错的一项

第一层风险：最可能出错的前提是 “bond-current gauge freedom 在长程 hopping 下仍等价”。R1 的 gauge 依赖一维局域连续性方程：不同 bond 的累计电荷只差有限系统内蓄积量；但长程 hopping 允许一次 jump 跨过多个 bonds，局域 bond current 与 reservoir current 的关系变成路径/割集依赖。

第二层风险：如果 current 必须定义为跨某个 cut 的所有 long jumps 之和，而不是 nearest-neighbor bond current，则 R1 Eq. (10) 中 `f(x)` 的局域平滑 gauge 可能替换为非局域 kernel `F(x,y)`。这会直接破坏 Eq. (11) 的本地 Riccati 型 gauge condition，导致 SSEP 的 `arccosh/arccos` CGF 不再可从一维 ODE 得到。硬边界：需要先从 microscopic tilted generator 写出 long-jump cut-current 的 continuum fractional action；若该 action 无局域 `f(x)^2 sigma(rho)` 形式，普通 MFT gauge trick 到此停止。

## §末 产出格式

本轮成果：重建了 R1 的正方链 `Noisy XX Eq. (1)-(3) -> QSSEP Eq. (4)+Supplement C/J -> tilted CGF Eq. (5)-(9) -> gauge trick Eq. (10)-(11) -> SSEP CGF Eq. (12)`；结论限定为一维 quasi-local free fermion noisy transport 的 leading large-L current CGF。

新增的引用文献：
- Costa, Ribeiro, De Luca, arXiv:2504.00188v3 / PRL DOI 10.1103/v8x8-ft81。
- Bernard, Jin, arXiv:1904.01406v3 / Phys. Rev. Lett. 123, 080601 (2019)。
- Albert, Bernard, Jin, Scopa, Wei, arXiv:2601.16883v1。
- Sarkar, Agarwalla, Bhakuni, arXiv:2310.01323v2 / Phys. Rev. B 109, 165408 (2024)。
- Jara, arXiv:0805.1326v2。
- Bernardin, Jimenez Oviedo, arXiv:1603.01234v3 / DOI 10.30757/alea.v14-25。

最弱的环节：R1 Supplement I 对 finite-s tilted hierarchy 的 generic `n` closure/scaling 仍未给完整证明；以及 quasi-local hopping 是 gauge trick 保持 diffusive local MFT 形式的关键前提。

下一步计划：Round 2 建议聚焦 long-range hopping。具体推导从 strong-dephasing projection 出发，证明或反驳 `J(r)~r^{-alpha}` 诱导 `r_eff(r)~r^{-2alpha}/gamma`，然后比较 `alpha>3/2` 与 `1<alpha<3/2` 的 current variance 标度是否从 `L^{-1}` 改为 fractional conductance 标度。

需要PI投喂的文献方向：`long-range exclusion current large deviations`, `fractional macroscopic fluctuation theory`, `boundary driven long jump exclusion reservoirs`, `dephasing long-range fermion full counting statistics`, `fractional Laplacian conductance open interval`。
