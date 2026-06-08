# PI 综合：LP29-C2 Round 1

日期：2026-06-04

## 当前北极星

LP29-C2：graph metrics 是否只是 Srivastava-style orbital-overlap metric 的重参数化。

核心 A vs B：

- A：orbital-overlap baseline 已吸收结构对 transport/effective mass 的主要解释力；LP29 graph metrics 只是换名或弱重参数化。
- B：控制 orbital-overlap、onsite variance、density、mobility-edge margin、batch/finite-size 后，graph spectral residual features 仍能预测外部 Hall/Drude/Wannier/spectral residual labels。

## A/B 独立性

- A 框架：amorphous oxide semiconductor electronic-structure baseline，重点是 orbital-overlap integral 与 same-sample residual schema。
- B 框架：distributed network reliability / graph spectral residual，重点是 lambda_2、spectral radius、high-betweenness targeted damage 的残差预测。
- 两者没有读取对方输出；输出文件分别为：
  - `current/A/C2_round1.json`
  - `current/B/c2_round1.json`

## INSPECTOR

- A：0 blocker，5 warnings。
- B：0 blocker，6 warnings。
- 结论：Round 1 可继续，但只能作为 protocol-stage artifact，不能当作 graph physics 已成立的经验验证。

## PI 判断

C2 没有被击毙，但声称必须缩水：

> 当前可发表/可推进的不是“graph spectra 独立支配非晶氧化物输运”，而是一个可证伪的 same-sample residual protocol：先用 orbital-overlap baseline 与常规控制变量吃掉解释力，再检验 graph spectral features 是否还有外部标签残差预测能力。

这比启动命题更窄，但更干净。若下一轮 residual 被 overlap baseline 全吸收，C2 降级为“graph metrics 是 orbital-overlap geometry 的诊断/可视化”。若 residual 存活，才允许升级为机制候选。

## 必须修正/约束

下一轮 A 必须：

1. 提取 Srivastava overlap normalization / SI，不能再停留在 DOI/摘要级。
2. 明确 `beta_2` 等回归系数单位，避免 eV^2 控制变量的量纲漂移。
3. 将 spectral radius residual 命名为 `spectral_radius_resid`，避免与 orbital decay length `rho_ij` 冲突。
4. 产出至少一行 same-sample table：`O_s`、controls、一个 graph residual feature、一个 external label/residual、provenance。

下一轮 B 必须：

1. 锁定 Laplacian/adjacency normalization。
2. 区分 synthetic benchmark 与材料证据；synthetic `B_positive_label` 只能测管线，不能证明材料机制。
3. 执行一个最小 benchmark：A-null 与 B-positive 两种模式都要跑，输出 seed-level CSV 或等价表。
4. 为 external labels 与 protocol thresholds 加 provenance flags。

## 突破潜力检查

本轮没有把我们直接推近“材料机制突破”；它把问题压缩成一个硬检验。若 residual protocol 成立，影响面是非晶氧化物带状输运判据，可影响 Jankousky 2026 之后的 effective-band 解释框架；若失败，也能明确 LP29 的 graph language 只是 orbital-overlap baseline 的重参数化。

突破潜力：中等，取决于下一轮是否能产出真实 same-sample residual 或可复现实验级 synthetic benchmark。

## AHA 检查

有一个可登记的新洞察，但暂不切换北极星：

> 无序固体中“可传播谱的临界信息”可能不是单一标量 overlap budget，而是 overlap budget 与图谱瓶颈/攻击脆弱性的多投影一致性。

该洞察已经被 C2 覆盖，不单独开新题。

## 下一轮上下文摘要

LP29-C2 Round 1 通过但缩水为 residual protocol。A/B 和 INSPECTOR 均同意：orbital-overlap 是强 baseline，graph metrics 只有在 same-sample residual test 中存活才有独立意义。下一轮不要扩写概念；A 补 Srivastava SI 与同样品表，B 跑 A-null/B-positive synthetic benchmark。任何经验声称都必须带 provenance，并明确 synthetic 结果不是材料证据。
