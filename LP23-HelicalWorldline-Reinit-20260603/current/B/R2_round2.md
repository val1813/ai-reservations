# LP23-R2 Round2 - B route

## §0 框架声明

本轮我采用的跨学科框架是 **计算机科学 / 纠错码的 syndrome quotient**。

借来的结构不是“误差校正”这个表面类比，而是线性码里的商空间判别：

`observed edge residual r` 先扣除一族被认为“标准可吸收”的列空间 `im(T_standard)`，剩下的 syndrome 是

```text
q(r) = (I - P_T) r
I_bridge = ||q(r)||^2
```

物理翻译：endpoint calibration、spinoptics、local constitutive response 都是 code 的 gauge/template subspace；只有落在 quotient `E_edges / im(T_standard)` 里的 residual 才能算 LP23-R2 bridge invariant 的候选。

## 本轮直接落地

已新增脚本：

```text
scripts/r2_syndrome_templates.py
```

该脚本实现了 Round2 要求：

1. 输入 edge residual `r`：支持 `--r 0.1,-0.04,...`，默认内置 8 条边 toy residual。
2. 构造 `D_endpoint`：有向图 incidence/coboundary matrix。
3. 构造 `T_spinoptics`：示例 `O(1/omega)` helicity-curvature 与 helicity-path 两列。
4. 构造 `T_local_constitutive`：示例 material-gradient 与 birefringence 两列。
5. 合并 `T_standard = [D_endpoint | T_spinoptics | T_local_constitutive]`。
6. 用 modified Gram-Schmidt 计算 residual vector `(I - P_T) r` 与 `projection_residual_norm = ||(I - P_T) r||`。当前实现是 toy 级 rank-revealing，不作为病态矩阵下的稳健证明。
7. 输出 `I_bridge = projection_residual_norm^2`。
8. 随机 endpoint calibration invariance check：对 `r -> r + D_endpoint a` 多次随机扰动，检查 quotient residual norm 不变。

默认运行结果摘要：

```text
T_standard shape: (8, 8)
rank(T_standard): 7
projection_residual_norm: 0.0223963644
I_bridge: 0.0005015971
endpoint invariance max |delta norm|: 5.898e-17
```

自定义 residual 验证：

```text
python scripts\r2_syndrome_templates.py --r 0.11,-0.03,0.07,0.02,-0.01,0.05,-0.04,0.03 --invariance-trials 8

projection_residual_norm: 0.0267496766
I_bridge: 0.0007155452
endpoint invariance max |delta norm|: 3.123e-17
```

错误长度输入会直接阻断：

```text
ValueError: edge residual r has length 3, expected 8
```

## 深挖1：同构的更深数学结构

第一层：标准模板投影不是“拟合得好不好”，而是 quotient map。

边空间 `E` 中的 residual `r` 被分解成

```text
r = P_T r + (I - P_T) r
```

其中 `P_T r` 是标准解释可以吸收的成分，`(I - P_T) r` 是 quotient representative。endpoint calibration 是 `D_endpoint` 的像，spinoptics/local constitutive 是另外两组标准模板列。把它们合并后再投影，避免把“endpoint 不能解释”误判为“新物理”，因为它可能被 spinoptics 或 local constitutive 吸收。

第二层：这对应纠错码里的 syndrome degeneracy。

在 stabilizer/code language 中，多个物理 error 可以同 syndrome 等价；这里多个标准物理机制可以同一个 edge pattern 等价。真正有价值的量不是 `r` 本身，而是 coset norm：

```text
dist(r, im(T_standard))^2
```

这就是脚本里的 `I_bridge`。如果 `I_bridge=0`，说明该 residual 在当前标准模板 span 中，不能作为 R2 bridge 的新信号；如果 `I_bridge>0`，才有 quotient-level 活口。

## 深挖2：原学科结构的下一层推广

第一层推广：从硬模板 span 到 nuisance model comparison。

当前脚本把 `T_standard` 当成确定列空间。下一步可以把每类模板视为 nuisance family，比较

```text
im(D_endpoint)
im(D_endpoint, T_spinoptics)
im(D_endpoint, T_spinoptics, T_local)
im(D_endpoint, T_spinoptics, T_local, T_nonlocal)
```

如果 `I_bridge` 只在加入 nonlocal/history template 后消失，LP23-R2 的声称就从“有残差”变成更硬的“残差需要非局域模板才可吸收”。

第二层推广：从欧氏投影到带协方差的 whitening syndrome。

实验 edge residual 不会同方差。更严谨版本应使用噪声协方差 `C`：

```text
I_bridge(C) = r^T C^{-1/2} (I - P_{C^{-1/2}T}) C^{-1/2} r
```

这样 bridge invariant 不会被某条高噪声边虚假放大。当前 toy 先保留欧氏范数，因为 Round2 目标是验证“标准模板投影后是否仍有 quotient residual”。

--- INSPECTOR_CHECK ---
[公式] `T_standard = [D_endpoint | T_spinoptics | T_local_constitutive]`; `projection_residual_norm = ||(I - P_T) r||_2`; `I_bridge = projection_residual_norm^2`。单位：若 `r` 为无量纲 edge phase/time residual，则 `projection_residual_norm` 同 `r`，`I_bridge` 为 `r^2`。若 `r` 带 SI单位，`I_bridge` 带该单位平方。模板列仅定义可吸收子空间；其数值幅度不解释为物理强度，除非另行给出列归一化/单位模型。
[方向] endpoint calibration、spinoptics、local constitutive 三类标准模板被统一扣除；剩余量定义在 edge residual quotient 上。默认 toy 中 `rank(T_standard)=7 < 8`，因此保留一个非标准 residual 方向。
[数据] 本步使用本地 toy graph 和人工 edge features；无外部数据、无文献数值输入。
[假设] 标准模板在本地线性化近似下可由设计矩阵列空间表示；投影使用欧氏内积；endpoint invariance 只检验 `r -> r + D_endpoint a` 的随机有限样本数值稳定性。

## 本轮失败记录

最初 6-edge toy 中 `T_standard` 对 edge space 满秩，导致任何 residual 都被标准模板吸收，`I_bridge=0`。这不是物理结论，而是 toy 设计退化。我已把默认图扩展为 8 条边，使 `rank(T_standard)=7`，保留非平凡 quotient 方向。

## 下一步计划

把当前 toy 的 `edge_features` 替换成 PI 指定的实验/仿真 edge observables，并加入 weighted projection。关键判据应从“endpoint 不可吸收”升级为“endpoint + spinoptics + local constitutive 均不可吸收”。

## 需要 PI 投喂的文献方向

检索关键词建议：

```text
spin Hall effect of light curved spacetime local constitutive tensor optical activity
pre-metric electrodynamics constitutive tensor birefringence
weighted least squares nuisance projection syndrome decoding
```
