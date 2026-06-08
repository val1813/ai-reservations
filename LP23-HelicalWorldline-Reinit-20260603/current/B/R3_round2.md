# LP23-R3 Round2 - B博士：QNP-Lint 有限矩阵压力测试

日期：2026-06-03

## §0 框架声明

本轮继续使用 B 路的跨学科框架：**编译器静态分析 / proof-carrying code / 纠错码 syndrome-logical 分离**。我没有读取 `current/A`、`synthesis/INSPECTOR_A*`，也没有读取旧 LP23-螺旋世界线目录。

本轮不再只写哲学判断，而是把 QNP-Lint 压成一个本地可跑的有限矩阵 toy：

```text
C0 --D0--> C1 --D1--> C2,    D1 @ D0 = 0
```

解释：

- `D0`：代表元 / endpoint / gauge exact 方向。
- `D1`：闭合性检查，等价于 syndrome consistency check。
- `r`：候选 residual。
- 白化投影：用 `sigma` 定义度量，把 `r/sigma` 投影到 `D0 + template + nuisance + history` 的列空间，剩余范数作为 residual class norm。

脚本位置：

```text
D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r3_qnp_lint_toy.py
```

## 本地运行结果

命令：

```powershell
python D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r3_qnp_lint_toy.py
```

关键输出：

```text
QNP-Lint finite-matrix toy
D0 shape=(9, 5) D1 shape=(1, 9) ||D1@D0||=0

base classification
representative_leak      label=REPRESENTATIVE_LEAK    rank= 4 residual_norm=9.408280408e-16 closed_norm=0
template_residual        label=TEMPLATE_RESIDUAL      rank= 5 residual_norm=7.499143576e-16 closed_norm=1.11e-16
nuisance_diagnostic      label=NUISANCE_DIAGNOSTIC    rank= 6 residual_norm=6.184575062e-16 closed_norm=1.11e-16
pass_obstruction         label=PASS_OBSTRUCTION       rank= 7 residual_norm=0.7981011406 closed_norm=6.94e-17
missing_contract         label=UNDECIDED              rank= 4 residual_norm=0.8172550346 closed_norm=6.94e-17

adversarial expansion on pass_obstruction
base                     label=PASS_OBSTRUCTION       rank= 7 residual_norm=0.7981011406 closed_norm=6.94e-17
+one_template_col        label=TEMPLATE_RESIDUAL      rank= 6 residual_norm=4.18697711e-16 closed_norm=6.94e-17
+one_nuisance_col        label=NUISANCE_DIAGNOSTIC    rank= 7 residual_norm=4.50012815e-16 closed_norm=6.94e-17
+one_history_col         label=HISTORY_DIAGNOSTIC     rank= 8 residual_norm=3.365900013e-16 closed_norm=6.94e-17
```

最低要求覆盖情况：

- `REPRESENTATIVE_LEAK`：`r` 已在 `im(D0)` 内，白化商范数约 `9.4e-16`。
- `TEMPLATE_RESIDUAL`：加入 template 后吸收，白化商范数约 `7.5e-16`。
- `NUISANCE_DIAGNOSTIC`：加入 nuisance 后吸收，白化商范数约 `6.2e-16`。
- `PASS_OBSTRUCTION`：在 `D0 + template + nuisance + history` 下仍有 `0.7981011406` 的白化 residual class norm。
- `UNDECIDED`：choice contract 缺失时不允许升级为物理自由度。

## Adversarial Expansion 判定

最狠的压力测试不是证明 toy 里有 obstruction，而是问：只要允许补一列 template/nuisance/history，它是否立刻死亡？

结果是：会。

`pass_obstruction` 在基准合同下 rank=7、norm=0.7981011406，因此通过 toy 的 obstruction 门槛。但如果把该 quotient 方向本身作为一列合法扩展加入：

- 加一列 template：label 退化为 `TEMPLATE_RESIDUAL`，norm 降到 `4.19e-16`。
- 加一列 nuisance：label 退化为 `NUISANCE_DIAGNOSTIC`，norm 降到 `4.50e-16`。
- 加一列 history：label 退化为 `HISTORY_DIAGNOSTIC`，norm 降到 `3.37e-16`。

B 路结论：QNP-Lint 只有在 choice contract 预先封闭时才有杀伤力；如果 proposal 允许事后把 residual 方向补进 template/nuisance/history，那么所谓 obstruction 只是合同不完整的诊断。

--- INSPECTOR_CHECK ---
[公式] `D1 @ D0 = 0`; `class_norm(r; A, sigma)=||(I-P_{A/sigma})(r/sigma)||_2`, where `A=[D0,T,N,H]`. `r` 的 SI 单位由原 proposal residual 继承；本 toy 使用无量纲有限矩阵。
[方向] 本步把 QNP-Lint 变成可运行的 residual cohomology 筛选器：先查 closedness，再查 exact/template/nuisance/history saturation，最后才允许 `PASS_OBSTRUCTION`。
[数据] 使用本地构造的 5 节点、9 边、1 个填充三角面的有限矩阵 toy；无外部实验数据。
[假设] 允许选择空间可被有限列空间近似；`sigma` 是已知协方差白化尺度；新增 template/nuisance/history 列是否合法由 proposal contract 决定。

## 深挖1：更深层数学结构

第一层同构是：

```text
编译器 representation independence
<-> residual 在 choice quotient 上的类
```

更深一层是 **proof-carrying proposal**：一个理论不能只提交 residual 热图，必须提交能证明 residual 不被合法列空间吸收的 certificate。

本轮 toy 给出 certificate 的最小矩阵版：

```text
certificate(P) =
  D0, D1, sigma,
  T_template, N_nuisance, H_history,
  proof(||D1D0||≈0),
  proof(||D1r||≈0),
  proof(class_norm(r; [D0,T,N,H], sigma) > threshold)
```

这比“看见非零 residual”更强，也更容易杀死伪阳性。

## 深挖2：原学科结构再推一层

纠错码里 syndrome 不是 logical operator。映射回本轮：

- `D1 r != 0`：连 syndrome consistency 都没过，只能 `UNDECIDED/diagnostic`。
- `r in im(D0)`：代表元泄漏，`REPRESENTATIVE_LEAK`。
- `r` 被 template/nuisance/history 吸收：稳定子生成元解释掉了 syndrome。
- 只有 `r` closed 且 quotient class 非零：才像 logical operator。

但 adversarial expansion 暴露了一个硬问题：若 proposal 可以事后增加一列“刚好等于 obstruction”的 history/template，则 logical class 立即变成 stabilizer。也就是说，QNP-Lint 的核心不是矩阵投影本身，而是 **合法扩展合同**。

## 失败记录

第一次手选 nuisance/history 列时失败：nuisance 列落入 `im(D0)`，被判成 `REPRESENTATIVE_LEAK`；同时 history 列提前填满 quotient 空间，使原本想保留的 obstruction 在基准合同下已经被吸收。

修正方式：扩展 toy 到 5 节点 9 边，并用约束零空间自动生成 template/nuisance/history/obstruction 方向，保证它们按预期分层。

这次失败本身支持 B 路判断：人工挑 residual 很容易伪造“新自由度”；必须让脚本报告 rank 和白化 residual norm。

## 下一步

1. 把 toy 的 `template/nuisance/history` 从“任意列”升级为带来源标签的合同列：局部模板、非局部 history kernel、低秩 nuisance tangent。
2. 加入阈值扫描：`sigma` 扰动、rank cutoff 扰动、随机合法列扩展，观察 `PASS_OBSTRUCTION` 是否稳定。
3. 若真实 LP23 residual 数据进入，应先生成 `D0,D1,T,N,H,sigma` certificate，再运行同一分类器；没有 certificate 的 proposal 自动 `UNDECIDED`，不能声称新自由度。

