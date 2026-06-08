# INSPECTOR Report: LP29 B Round 1

输入文件：`D:\Claude\ai-reservations\LP29-AmorphousBands\current\B\round1.json`

角色：INSPECTOR  
检查对象：B 博士 Round 1  
结论：未发现致命阻断级量纲/方向错误；存在若干必须显式标注的警告，尤其是 graph proxy 与 graph Hamiltonian 验证之间的循环论证风险、替代解释排除不足、落地数据仍偏蓝图。

## 0. 机械检查

`D:\Claude\ai-reservations\LP29-AmorphousBands\validation` 不存在，不能运行 `validation/validate.py` 或 `validation/quantum.py`。

本报告降级为手工执行 Q1-Q5，并注明：validate.py 不可用。

## Q1. 量纲校对

### F1: `S_GC - S_c`

- 左边：`S_GC` 为最大连通分量占比，无量纲；`S_c` 为阈值，无量纲。
- 右边：无量纲差值。
- 匹配：通过。
- 注意：`S_GC - S_c` 的自然范围可为 `[-1, 1]`，当前 numerical_test 只给了正例 `[0, 1]`。不是量纲错误，但负侧应在下一轮补一个低于阈值的测试。

### F2: `t0*exp(-(r_ij-r0)/lambda)*exp(-beta*f_OO)`

- 左边：边权/跃迁能量 `t_ij`，单位 eV。
- 右边：`t0` 为 eV；两个指数因子必须无量纲。
- `-(r_ij-r0)/lambda`：若 `r_ij`、`r0`、`lambda` 均为长度，则无量纲，通过。
- `-beta*f_OO`：`f_OO` 是局域缺陷分数，无量纲；因此 `beta` 必须声明为无量纲缺陷惩罚系数。当前变量说明只写了 defect penalty coefficient，未显式写无量纲。
- 判定：量纲可成立，但需要补充 `beta` 无量纲；`alpha_edge`、`alpha_corner` 也应声明为无量纲。

### F3: `mean(min(delta_n,delta_n1)/max(delta_n,delta_n1))`

- `delta_n` 与 `delta_n1` 均为能级差，单位 eV 或同一能量单位。
- 比值无量纲，均值无量纲。
- 匹配：通过。

### 图指标量纲

- `S_GC = N_largest_connected_component / N_In`：无量纲，通过。
- `z_bar = 2E/N_In`：平均度，无量纲，通过。
- `z_eff = mean_i(sum_j(t_ij/t0))`：`t_ij/t0` 无量纲，求和与均值仍无量纲，通过。
- `P(r_In-In)`：若作为归一化概率密度，单位应为 `1/length`；若作为 histogram/bin counts，则依赖 bin 宽。当前未声明归一化约定，警告。
- `medium-range peak areas`：若对概率密度按 `dr` 积分，应无量纲；当前未声明。
- `edge density inside r_cut`：可能是每个 In 的边数、每体积边数或每原子归一化边密度，量纲未定义，警告。
- `f_OO = N(defect motifs)/N_O`：无量纲，通过。
- `R_edge`、`R_corner`：比值无量纲，通过。

## Q2. 符号/方向校对

方向性结论：

- `Lower S_GC or z_eff should lower mu_H, Drude weight, and spectral-ridge coherence`：与 percolation/weighted connectivity 直觉一致。
- `mu_H and D fall nonlinearly when S_GC<S_c or z_eff<z_c`：阈值方向正确。
- `t_ij > t_min thresholded weighted graphs`：阈值方向正确；保留强边、删除弱边。
- 扫描 `t_min` 时需明确：`t_min` 升高会删除更多弱边，`S_GC/z_eff` 应降低或不增；若把 `t_min` 当作“连通性增强”控制量会反向。当前文本没有反用。
- `f_OO -> oo` 导致 `exp(-beta*f_OO) -> 0`：若 `beta > 0`，方向正确。下一轮应显式声明 `beta > 0`。
- level statistics 从 Wigner-Dyson-like 到 Poisson-like 随低连通性/局域化增强：方向合理。

判定：未发现方向反转。需要补充 `beta > 0` 与 `t_min` 扫描方向说明。

## Q3. 循环论证校对

存在警告级循环论证风险。

B 的核心检验提出：

- 从结构生成同一个 weighted graph；
- 用该 graph 的 `S_GC/z_eff/f_OO` 作为解释变量；
- 再在同一个 graph Hamiltonian 上计算 IPR、level statistics、spectral proxy、Drude/Kubo proxy；
- 然后声称这些谱/输运 proxy 与 graph threshold 同步。

如果验证数据完全由同一个 proxy graph Hamiltonian 生成，这只能证明模型内部自洽，不能独立证明真实 a-In2O3 的 band-like transport 由该网络阈值主导。尤其是 P2 的“progressively delete or weaken low-quality defect edges”若同时定义了缺陷边和结果 Hamiltonian，会把输入假设重复输出。

修正建议：

- 至少一条验证链必须独立于 proxy graph 权重：例如 DFT/QSGW/Wannier 提取的 `t_ij`、实验 Hall/Drude 数据、或结构 ensemble 的真实谱函数。
- 对照组必须包含 matched carrier density、matched EF-Ec、matched disorder variance 的非网络解释模型。
- proxy graph Hamiltonian 可以作为蓝图/半成品，但不能作为唯一证据。

判定：警告，不阻断本轮；下一轮必须显式拆开“生成指标”和“验证观测”的来源。

## Q4. 数量级鸿沟

可手工验算的数值：

- F2 substitution: `t0=1.0 eV, r_ij-r0=0.1, lambda=0.5, beta=2.0, f_OO=0.1`，得到 `exp(-0.2)*exp(-0.2) ~= 0.67 eV`，落在 `[0.4, 1.0]`，通过。
- F3 substitution: `min(0.08,0.12)/max(0.08,0.12)=0.667`，落在 `[0,1]`，通过。
- F1 substitution: `0.55-0.45=0.10`，落在 `[0,1]`，通过；但没有低于阈值负例。

未发现 >3 数量级偏差。当前数值仅为 sanity check，不是材料真实参数验证。

## Q5. 代数验算

- F1 为无量纲差值，无代数展开错误。
- F2 两个指数相乘，极限正确：
  - `f_OO -> 0` 时回到距离控制 hopping；
  - `f_OO -> infinity` 且 `beta > 0` 时 hopping 衰减到 0；
  - `r_ij -> r0` 时距离指数为 1；
  - `r_ij` 增大时 hopping 降低。
- F3 adjacent-gap ratio 的形式正确，但变量命名 `delta_n1` 应明确为 `delta_{n+1}`，避免被误读为 `delta_n * 1`。

引用数值来源：

- 具体 DOI 给出 `10.1038/s41567-025-03099-x`，但 B round1 未提供从该文全文抽取的具体数值表。
- 本轮参数 `t0, lambda, beta, f_OO` 是示例 proxy 数值，未标来源。应标为 toy substitution，不得当作材料实测/DFT 数值。

判定：代数通过；数值来源警告。

## Q6. 综合判定

### Q6.3 声张缩水

Round 1 无 B 的上一轮可比对象，因此不能判定相对上一轮缩水。

与 Polaris 问题相比，B 没有明显把命题退化为普通“无序强度影响迁移率”；它提出了中程 In-s connectivity network、O-O/coordination-defect thresholds 与 graph-spectral transition。声张没有明显缩水。

判定：通过；后续轮次需与本轮 C1-C3 对比。

### Q6.4 替代解释

B 回答了 A 式 objection：network metrics 可能只是 renamed disorder strength and can be absorbed into Ec。回答方向是要求 matched-n、matched-EF-Ec 后比较网络阈值。

但替代解释排除仍不足，至少缺以下显式对照：

- O vacancy / carrier-density / compensation 改变，而非 network threshold。
- 普通 Anderson onsite disorder 或 structural disorder variance。
- effective mass、scattering time、polaron/phonon scattering 差异。
- finite-size graph threshold artifact。
- `EF-Ec` 拟合误差或 mobility-edge 定义不稳导致的假优势。

判定：警告。PI/B 下一轮必须把这些替代解释列入模型对照或卡点登记。

### Q6.5 落地计算

B 给出了 1-2 周 metrics 和 next_plan，包括 structure-to-graph script、tight-binding graph Hamiltonian、IPR、`r_bar`、spectral/Drude proxy。这是可执行蓝图。

但还没有具体系统、具体坐标数据、具体 cutoff、具体 `r_cut/t_min/lambda/beta` 标定来源，也没有落地 A/B/C 中的任一具体数值产物。当前属于半成品蓝图，不是已完成落地计算。

判定：警告，不阻断。下一轮需至少落地一个具体数据路径：指定结构来源，给出 cutoff 定义，输出一个表格或最小 toy/真实 ensemble 的数值。

## 重点专项检查

- 图指标量纲：大多通过；`P(r)`、peak area、edge density 的归一化/单位需补。
- edge-weight proxy 的 exp 自变量：可无量纲；必须补充 `lambda` 长度单位、`beta/alpha_edge/alpha_corner` 无量纲、`beta > 0`。
- 网络阈值方向：正确；`t_ij > t_min` 保留强边，`S_GC/z_eff` 下降对应 mobility/Drude/ridge 下降。
- 循环论证：警告。不能只用同一 proxy graph 同时生成解释变量和验证 observables。
- 声张缩水：Round 1 无上一轮可比，未见缩水。
- 替代解释：警告。已有一句 A objection，但未系统排除更简单机制。
- 落地性：警告。计划可行，但当前无具体结构/参数/数值产物。

## INSPECTOR 结论

⚠️ INSPECTOR 警告：B Round 1 可继续，但必须显式标注以下问题。当前没有阻断级量纲错误或方向错误；不得把本轮 proxy 数值当作实证结果。

--- 投喂下一轮 ---

必须修正（阻断级）：

无。

建议修正（警告级）：

1. edge-weight proxy 需声明 `lambda` 为长度，`beta`、`alpha_edge`、`alpha_corner` 为无量纲，且 `beta > 0`；`P(r)`、peak area、edge density 需定义归一化和单位。
2. 补一个低于阈值的 numerical test：例如 `S_GC < S_c` 时 `S_GC-S_c < 0`，并说明对应 transport collapse 方向。
3. 避免循环论证：不要只用同一个 proxy graph Hamiltonian 同时生成网络指标和验证结论；至少引入 DFT/Wannier/实验或独立结构 ensemble 对照。
4. 系统处理替代解释：carrier density/O vacancy、onsite disorder variance、effective mass/scattering time、finite-size artifact、EF-Ec 定义误差。
5. 落地计算需从蓝图推进到具体产物：指定结构数据、cutoff、参数标定来源，并输出至少一个最小表格或 toy/真实 ensemble 数值。

---
