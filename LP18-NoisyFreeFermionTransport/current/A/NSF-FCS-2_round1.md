# NSF-FCS-2 Round 1 A侧推导：long-jump open exclusion 的 NESS FDT residual scaling

角色：A博士（学院派）  
北极星：`R2(L)=lambda_T''(L)-2G_T(L)` 在 density-biased NESS 中是否携带 reservoir-tail / fractional conductance 的新标度。

## 0. 文献锚点

1. Baiesi, Maes, Wynants, "Fluctuations and Response of Nonequilibrium States", Phys. Rev. Lett. 103, 010602 (2009), DOI: `10.1103/PhysRevLett.103.010602`.
2. Baiesi, Maes, Wynants, "Nonequilibrium Linear Response for Markov Dynamics, I: Jump Processes and Overdamped Diffusions", J. Stat. Phys. 137, 1094-1116 (2009), DOI: `10.1007/s10955-009-9852-8`.
3. Baiesi, Maes, "An update on the nonequilibrium linear response", New J. Phys. 15, 013004 (2013), DOI: `10.1088/1367-2630/15/1/013004`.
4. Maes, Netocny, Wynants, "On and beyond entropy production: the case of Markov jump processes", arXiv:`0709.4327`.
5. Sano, "The McLennan-Zubarev steady state distribution and fluctuation theorems", Physica A 467, 421-431 (2017), arXiv:`1701.04487`, DOI: `10.1016/j.physa.2017.01.049`.
6. Bernardin, Jimenez Oviedo, "Fractional Fick's law for the boundary driven exclusion process with long jumps", ALEA 14, 473 (2017), arXiv:`1603.01234`, DOI: `10.30757/alea.v14-25`.
7. Bernardin, Cardoso, Goncalves, Scotta, "Hydrodynamic limit for a boundary driven super-diffusive symmetric exclusion", Stoch. Proc. Appl. 165, 43-95 (2023), arXiv:`2007.01621`, DOI: `10.1016/j.spa.2023.08.002`.
8. Jara, "Hydrodynamic limit of particle systems with long jumps", arXiv:`0805.1326`.

说明：本轮未读取 B 侧输出。文献检索以 paper-search-mcp 为主；部分具体方程编号需 PI 后续核对原文 PDF。

## 1. 近 equilibrium 展开：为什么首个非零 bias 项应为 delta^2

设边界密度

`rho_L = rho_bar - delta/2`, `rho_R = rho_bar + delta/2`,

并把 steady generator 写成

`L_delta = L_0 + delta L_1 + delta^2 L_2 + O(delta^3)`,

其中 `L_0` 是同密度 reservoir 下的 detailed-balance generator。若边界驱动满足 local detailed balance，且左右 reservoir 交换 `rho_L <-> rho_R` 与空间反射 `P` 组成一个精确对称，即

`P L_delta P^{-1} = L_{-delta}`,

而被测二阶量 `lambda_T''`、`G_T` 与 `R2` 都是左右端口反射偶量，则

`R2(L,delta)=R2(L,-delta)`.

equilibrium finite-volume FDT 给 `R2(L,0)=0`，于是解析展开若存在，

`R2(L,delta)=c_2(L) delta^2 + c_4(L) delta^4 + O(delta^6)`.

--- INSPECTOR_CHECK ---
[公式] `R2(L,delta)=c_2(L) delta^2 + c_4(L) delta^4 + O(delta^6)`；`R2` 与 `G_T`、`lambda_T''` 同量纲，为单位时间的二阶 transported-particle cumulant rate。若 `delta` 取 density difference，`c_2` 与 `R2` 同量纲。  
[方向] density bias 的线性项不由一般 NESS response 自动消失，而由三件事共同消失：equilibrium FDT、左右反射偶性、`delta=0` 附近解析性。  
[数据] PI bias scan：`L=8` 时三组 alpha 的 `R2` 对 `delta` 斜率分别为 `2.000030`, `2.000000`, `1.999998`；reverse-bias check 显示 `max |Delta R2| = 8.46e-9`。  
[假设] local detailed balance；左右 reservoir 几何对称；observable 是 two-terminal 反射偶量；谱隙/有限体积解析性足够支持 Taylor 展开。无限体积极限下若先取 `L -> infinity` 再取 `delta -> 0`，解析性可能失效。

缺失假设必须明说：如果端口定义不是反射偶量，或者 reservoir coupling 左右不等强，或 counting field 对左右方向有未对称化 convention，则 `R2(delta)=R2(-delta)` 不成立，线性项 `c_1(L) delta` 可以出现。当前 reverse-bias sanity check 基本排除了这一类 convention artifact，但只在 `L=4..8` 和当前 ledger 定义下成立。

## 2. R2 的控制对象：McLennan 一阶项不够，首个残差来自二阶 NESS response 的 frenetic/traffic 混合

McLennan-Zubarev 形式在弱驱动下可写成

`mu_delta(x) = mu_0(x) [1 + delta Phi_1(x) + delta^2 Phi_2(x) + O(delta^3)]`,

其中 `Phi_1` 可理解为从态 `x` 出发的 excess entropy production 的 resolvent。对 Markov jump process，Baiesi-Maes-Wynants 的 nonequilibrium response 将响应分成 time-antisymmetric 的 entropic 项和 time-symmetric 的 frenetic/traffic 项。对 equilibrium reference，二阶 transport cumulant 与 conductance 的 FDT cancellation 吃掉的是 entropic 线性结构；NESS residual 首个非零系数应落在

`c_2(L) = <J_T ; K_T ; Phi_1>_0 + <J_T ; Tau_1>_0 + <A_T ; Phi_2>_0 + boundary counterterms`,

这里 `J_T` 是 time-antisymmetric current sector，`K_T`/`Tau_1` 表示 escape-rate/activity 的一阶或二阶扰动，`A_T` 表示二阶 counting observable 的 equilibrium sector。该式是结构式，不是已核对到原文编号的定理。

--- INSPECTOR_CHECK ---
[公式] `c_2(L) = <J_T ; K_T ; Phi_1>_0 + <J_T ; Tau_1>_0 + <A_T ; Phi_2>_0 + boundary counterterms`；各项量纲合并为单位时间 cumulant rate。  
[方向] `R2` 的 `delta^2` 系数不应只归因于 McLennan density profile；它更可能由 McLennan correction 与 frenetic/traffic 项的混合、或等价的三点 response/capacity 对象控制。  
[数据] 本式只使用 PI ledger 的 `R2 ~ delta^2` 与 `S_T-2 > 0` 事实；未直接拟合 microscopic 三点函数。  
[假设] finite-state Markov jump response 可套用到当前 finite-L exclusion generator；counting observable 的二阶导与 response expansion 可交换；long-jump reservoir tail 未破坏有限 L 的解析性。

更具体地，若 `u_L(i)` 是 equilibrium generator `L_0` 对边界 density bias 源项的 Poisson 解：

`-L_0 u_L = b_L`, 其中 `b_L` 是左/右 reservoir density source 的反射奇组合，

则 McLennan 一阶 correction 是 `Phi_1 ~ u_L`。二阶 residual 的最弱闭合形式可写为

`R2(L,delta) = delta^2 G_T(L) Q_L + O(delta^4)`,

`Q_L := Var_0^{cap}(Phi_1; traffic/counting boundary)`.

这里 `Q_L` 是一个容量型 Green 函数对象：它不是简单的 density profile 幅度，而是 Poisson 解在 reservoir-tail 加权边界层上的二次型。若写成离散 Green 函数，

`Q_L ~ sum_{i,j in Lambda_L} w_i^{bd} G_L(i,j) w_j^{bd} C_{ij}^{traffic}`,

其中 `w_i^{bd}` 是由长跳 reservoir coupling 诱导的边界权重，`G_L=(-L_0)^{-1}` 是 equilibrium resolvent，`C_{ij}^{traffic}` 是 activity/counting sector 的局部或半局部 kernel。

--- INSPECTOR_CHECK ---
[公式] `R2(L,delta)=delta^2 G_T(L) Q_L+O(delta^4)`；`Q_L` 无量纲，若 `G_T` 是单位时间 conductance rate，则 `R2` 仍是单位时间 cumulant rate。  
[方向] 可检验核心：`R2/G_T` 应当约等于 `delta^2 Q_L`，而 `Q_L` 的 L 标度由 equilibrium Green/resolvent 容量和 reservoir-tail 权重决定。  
[数据] PI 表中 `slope log |R2| = slope log G_T + slope log |S_T-2|`；`S_T-2=R2/G_T` 的斜率约 `0.47..0.54`。  
[假设] `Q_L` 与 `delta` 的 leading dependence 可忽略；`G_T` 已吸收主导 fractional conductance；剩余 `Q_L` 是一个较弱、近似 alpha-independent 的 boundary-layer capacity。

## 3. 对当前 alpha 斜率的解释与预测

PI 数据：

| alpha | slope log G_T | slope log \|S_T-2\| | slope log \|R2\| |
|---:|---:|---:|---:|
| 0.5 | 0.540 | 0.469 | 1.009 |
| 1.0 | 0.108 | 0.512 | 0.621 |
| 1.5 | -0.253 | 0.532 | 0.279 |

最弱、但可立即检验的解释是：

`R2(L,delta) ~ delta^2 G_T(L) Q_L`, 且 `Q_L ~ L^{1/2}` 在当前 `L=4..8` window 中近似成立。

于是

`beta_R(alpha) = beta_G(alpha) + beta_Q`, `beta_Q approx 1/2`.

用实测 `beta_G` 加 `1/2` 预测：

- `alpha=0.5`: `0.540 + 0.5 = 1.040`，观测 `1.009`。
- `alpha=1.0`: `0.108 + 0.5 = 0.608`，观测 `0.621`。
- `alpha=1.5`: `-0.253 + 0.5 = 0.247`，观测 `0.279`。

误差在当前小尺寸 window 内是可接受的。更强一点的解析猜测是：fractional conductance 给 `beta_G(alpha)`，而 NESS FDT residual 的额外二次 response 容量 `Q_L` 是一个边界 Green 函数平方根容量，导致近似 universal 的 `L^{1/2}` 增强。

--- INSPECTOR_CHECK ---
[公式] `beta_R(alpha)=beta_G(alpha)+beta_Q`, `beta_Q approx 1/2`；等价于 `R2/G_T ~ delta^2 L^{1/2}`。指数无 SI 单位。  
[方向] 当前三组斜率不要求三种 alpha 有三套机制；它们可由同一机制解释：主 conductance 标度乘以近似 universal 的 NESS capacity correction。  
[数据] PI `L=4..8` ledger：`slope log |S_T-2|` 分别约 `0.469`, `0.512`, `0.532`。  
[假设] `S_T-2` 的 `1/2` 斜率不是小 L 巧合；`G_T` 的实测斜率可作为 fractional conductance 的有限体积代理；`Q_L` 未在更大 L crossover 到 alpha-dependent 指数。

另一个可与文献 fractional Fick law 对接的预测是：

`beta_G(alpha)` 在大 L 应接近 fractional conductance 指数 `g(alpha)`，而

`beta_R(alpha) approx g(alpha)+1/2`.

若采用粗略的 superdiffusive conductance intuition `g(alpha) approx 1-alpha`，则

`beta_R(alpha) approx 3/2-alpha`.

这给出 `alpha=0.5 -> 1.0`，`alpha=1.0 -> 0.5`，`alpha=1.5 -> 0`。它解释了 alpha=0.5 的精确值和 alpha=1.0 的量级，但低估 alpha=1.5 的 `0.279`。因此我把 `3/2-alpha` 只列为 asymptotic 候选，而不是当前结论。alpha=1.5 可能处在 marginal/crossover window：`3/2-alpha=0` 附近的对数修正或 reservoir-tail finite-size correction 会在 `L=4..8` 伪装成小正指数。

可检验判据：

1. 固定 alpha、delta，扩大 L 后若 `slope log(R2/G_T)` 继续稳定在 `1/2`，支持 Green-capacity 解释。
2. 若 `slope log(R2/G_T)` 随 alpha 明显漂移，则 `Q_L` 不是 universal boundary capacity，而是 alpha-dependent fractional resolvent。
3. 若 alpha=1.5 在更大 L 从 `0.279` 下滑到 `0` 或 `log L`，支持 `3/2-alpha` 的 marginal 版本。
4. 若 `R2/G_T/delta^2` 对 density center `rho_bar` 呈 `chi(rho_bar)=rho_bar(1-rho_bar)` 或其倒数的规律，可把 `Q_L` 进一步定位到 equilibrium compressibility 加权 Green 函数。

## 4. 两层深化

### 深化1：本轮结论的下一层后果

若 `R2/G_T ~ delta^2 Q_L`，则直接看 `R2` 不是最干净诊断量；更干净的是

`Qhat_L := R2(L,delta) / [delta^2 G_T(L)]`.

本轮预测 `Qhat_L ~ L^{1/2}`，并且该量应比 `R2` 本身更少受 alpha-dependent conductance 影响。再下一层后果是：`Qhat_L` 应能被 equilibrium/NES near-equilibrium 数据中的三点函数或 resolvent 二次型重建，不需要重新拟合 full counting statistics 的全部 SCGF。

### 深化2：最可能错误的前提

最可能错误的前提不是 `delta^2`，而是 `Q_L ~ L^{1/2}` 的 alpha-independent 假设。long-jump reservoir tail 可能让 boundary source `w_i^{bd}` 与 fractional Green 函数的容量本身 alpha-dependent。若如此，当前 `0.47..0.54` 的 `S_T-2` 斜率只是 `L=4..8` 的伪平台。再下一层的风险是：finite-L exact diagonalization/ledger 的 reservoir truncation `m-tail=2000` 已经把部分 tail capacity 固定住，导致 `Q_L` 的真正 infinite-reservoir 标度被截断窗口污染。这个风险需要通过同时变化 `L` 和 `m-tail` 来排除。

## 5. 本轮成果

本轮成果：推出 `R2` 对 density bias 的首个非零项为 `delta^2` 需要 `local detailed balance + 左右反射偶性 + finite-L 解析性 + equilibrium FDT`；`delta^2` 不是无条件定理。给出最弱结构式 `R2 ~ delta^2 G_T Q_L`，其中 `Q_L` 是由 McLennan correction 与 frenetic/traffic response 混合产生的 Green/resolvent 容量对象。当前斜率最自然解释为 `Q_L ~ L^{1/2}`。

新增引用文献：Baiesi-Maes-Wynants PRL 2009 DOI `10.1103/PhysRevLett.103.010602`；Baiesi-Maes-Wynants JSP 2009 DOI `10.1007/s10955-009-9852-8`；Baiesi-Maes NJP 2013 DOI `10.1088/1367-2630/15/1/013004`；Maes-Netocny-Wynants arXiv:`0709.4327`；Sano arXiv:`1701.04487` DOI `10.1016/j.physa.2017.01.049`；Bernardin-Jimenez Oviedo arXiv:`1603.01234` DOI `10.30757/alea.v14-25`；Bernardin-Cardoso-Goncalves-Scotta arXiv:`2007.01621` DOI `10.1016/j.spa.2023.08.002`；Jara arXiv:`0805.1326`。

最弱环节：`Q_L ~ L^{1/2}` 目前是从 `S_T-2` 的数值斜率反推的 capacity ansatz，不是已从 microscopic Green 函数求和推出的定理。第二弱点是 `3/2-alpha` asymptotic 猜测在 alpha=1.5 处只给 marginal/crossover 解释。

下一步计划：计算或数值估计 `Qhat_L=R2/(delta^2 G_T)`，在 `L=4..10/12` 和多个 `m-tail` 下拟合其斜率；同时从 equilibrium generator 解 Poisson 方程 `-L_0 u=b`，构造候选二次型 `sum w_i G_L(i,j) w_j`，检验其是否与 `Qhat_L` 同标度、同 alpha 趋势。

需要 PI 投喂的文献方向：  
1. "McLennan ensemble Markov jump process second order response traffic frenetic"。  
2. "boundary driven long range exclusion fractional Fick law finite size conductance"。  
3. "fractional Laplacian Green function capacity interval boundary source scaling"。  
4. "nonlinear Green-Kubo formula nonequilibrium steady state second order conductance exclusion process"。
