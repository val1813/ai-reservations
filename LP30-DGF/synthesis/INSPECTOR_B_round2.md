# INSPECTOR B Round 2

检查对象：`current/B/round2.json`

## 结论

警告通过。B 的局部展开、量纲和边界系数基本正确，但“fold caustic”表述过强，q 独立性仍未真正解决。

## 关键判定

- `m_star*sin(pi*q/2)` 量纲和极限通过。
- `dm/dq=m_star*pi*cos(pi*q/2)/2` 量纲为 kg，`q=1` 时为 0。
- 局部展开正确：

```text
x=1-q
m_star - m(q) ≈ (pi^2*m_star/8)*x^2
```

- 当前结构更准确应称为 `fold-type critical endpoint`。只有给出观测投影密度或 likelihood Jacobian 奇性后，才可称为 caustic-like boundary。
- `observability_rank_condition` 目前只是抽象条件，未定义矩阵元素、nuisance 参数或 rank 判据。

## 投喂下一轮

阻断级：

1. q 独立性未真正解决。下一轮必须给出具体观测量、校准方式和 nuisance 参数分离方案。
2. “fold caustic”表述过强。改为 “fold-type critical endpoint / caustic-like boundary only if observable projection density is specified”。

警告级：

1. `fold_map`、`fold_derivative`、local normal form 可保留。
2. `boundary_residual` 缺少 `V_DGF(q)` 或 `Gamma(q,Omega,L)` 最小模型。
3. `observability_rank_condition` 需具体化为矩阵元素、参数列表和 rank 判据。
4. “14 microgram near caustic / 22 microgram outside” 必须加入质量校准误差、visibility 误差和环境 null model。
