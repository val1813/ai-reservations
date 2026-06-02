# LP7-S6 Phase 1 — A 正规推导

生成时间：2026-06-01

## 0. 输入与边界

本推导只处理 LP7-S6：因果集传播子路线对接。

不声称：

- 因果集传播子路线已经给出统一公式。
- v13 的 5 构造判据矩阵已经完成 A/B 验证。
- `J_ij[D,J]` 已经可直接预测 Page-Geilker 或 BMV 实验数值。

本推导只问：

> `J_ij[D,J]` 是否可作为 LP7-S5 的 `J_unify` 候选实现模块。

## 1. 映射对象

v13 主对象：

`J_ij(c) = dist_delta(D^T (K_i - K_j) J, Im M_cross^(5))`

其中：

- `K_i` 是传播子构造；
- `D` 是 detector 配置；
- `J` 是 source 配置；
- `M_cross` 是共同参数空间；
- `J_ij=0` 表示两个构造在给定 detector/source 下不可区分；
- `J_ij≠0` 表示给定观测可以区分两构造。

LP7-S5 需要的对象：

`J_unify = distance(observable predictions, admissible theory manifold)`

所以形式上可以建立映射：

`J_unify^CS[D,J] := J_ij[D,J]`

但这个映射只覆盖传播子 / detector response 层，不覆盖完整引力动力学。

## 2. 对 LP7-S1 的映射

LP7-S1 的核心差异：

`Phi_run` vs `Phi_sc`

可写成 source 选择差异：

- branch source：`J_branch`
- expectation source：`J_avg`

若 detector 读数由 Green function 给出：

`R = D^T K J`

则 Page-Geilker 差异可写为：

`Delta R_PG = D^T K (J_branch - J_avg)`

这说明 causal-set propagator route 可表达 S1 的“源项选择”问题，但不能单独解决测量更新或 collapse 规则。

## 3. 对 LP7-S2 的映射

BMV 的核心是 mediator-induced phase / entanglement witness。

低能极限中可把相位写成传播核积分：

`phi_AB ~ J_A^T K J_B`

若两个候选传播子给出不同的 `phi_AB`，则：

`Delta phi_ij = J_A^T (K_i - K_j) J_B`

这正是 `J_ij[D,J]` 的双源版本。  
因此 S6 可把 BMV 的“媒介非经典性见证”降到 propagation kernel 层做必要条件筛选。

限制：

- 不能从传播子差异直接推出 entanglement；
- 仍需量子态制备、噪声、locality assumptions；
- `K_i` 是否代表 classical/quantum mediator 需要额外字典。

## 4. 对 LP7-S3 的映射

S3 的主结论是 stochastic/diffusion cost。

在 causal-set response 框架里，这可写成：

`K -> K + eta`

其中 `eta` 是随机核或噪声核。  
若噪声可以被 `M_cross` 吸收，则对 detector 不可见；若噪声落在正交补，则：

`J_noise = dist_delta(D^T eta J, Im M_cross)`

因此 S6 能把 S3 的“混合动力学代价”表达为 response kernel 的外分量，但不能从因果集传播子本身推出 Oppenheim trade-off。

## 5. v13 半成品的可用度

v13 B 单边推导给出候选线索：

- `K_B` 类空支撑可能是 5 构造的单一识别器；
- `(path, K)` 可能是唯一强收敛对；
- 含 BDG/BBL 的对可能存在 O(1) 病态。

PI 必须把这些写成“候选线索”，不能写成 LP7-S6 结论，因为 v13 未通过 A/B GATE。

S6 的合法结论只能是：

`J_ij[D,J]` 是 `J_unify` 的可实现模板，但当前仍缺数值闭合与 A/B 验证。

## 6. Phase 结论

结论类型：**有边界**。

因果集传播子路线可以作为 LP7-S5 的一个实现模块：它把 Page-Geilker 的源项选择、BMV 的相位/纠缠见证、S3 的 stochastic noise cost 都写成 detector response kernel 的差异。但它不是统一公式本身；它只提供 `observable-level discriminant`。v13 半成品只允许作为候选实现线索，不能入库为已验证知识。

## 7. K 条目候选

K80 [⚠️ L2] `J_ij[D,J]` 可作为 LP7-S5 `J_unify` 的 causal-set realization template。
  条件：只覆盖传播子 / detector response 层。
  math_object：`dist_delta(D^T(K_i-K_j)J, Im M_cross)`
  验证状态：待 B 独立验证。

K81 [⚠️ L2] Page-Geilker 差异可重写为 `Delta R_PG = D^T K (J_branch-J_avg)`。
  条件：给定传播核 K 与 detector/source 字典。
  math_object：`branch source`, `expectation source`, `detector response`
  验证状态：待 B 独立验证。

K82 [⚠️ L3] BMV 相位差可写为 `Delta phi_ij = J_A^T(K_i-K_j)J_B`，但不能单独推出 entanglement。
  条件：低能核近似、locality、state-preparation assumptions。
  math_object：`BMV phase`, `Green function kernel`
  验证状态：待 B 独立验证。

## 8. 待 B 验证清单

1. `J_unify^CS := J_ij` 是否只是形式重命名，还是有真实映射内容。
2. Page-Geilker 源项差异是否能被 detector kernel 捕捉。
3. BMV phase kernel 是否足以作为 S6 对接点。
4. S3 stochastic/diffusion cost 是否可自然写成 noise kernel 正交分量。
5. v13 半成品是否应完全排除，还是可以作为候选线索。

