# LP23-R3 Round2 A路 INSPECTOR

输入文件：`current/A/R3_round2.md`  
输出日期：2026-06-03  
检查范围：仅做量纲、符号方向、循环论证、量级鸿沟、代数验算和综合判定；不评价发表价值或先发覆盖；未读取 B 路输出。

## Q1. 量纲校对

关键公式检查：

| 公式 | 左边 SI/单位类型 | 右边 SI/单位类型 | 匹配 |
|---|---|---|---|
| (R2-0) \(\mathcal I=(r,D_0,D_1,\Sigma;\mathfrak L)\) | 输入对象元组 | \(r\)：残差单位；\(D_0\)：残差单位/参数单位；\(D_1\)：约束单位/残差单位；\(\Sigma\)：残差单位平方；\(\mathfrak L\)：无 SI 单位的库规则 | ✅ |
| (R2-1) \(\mathrm{QNP\text{-}Lint}(\mathcal I)=...\) | 离散标签 | 条件判定后返回离散标签 | ✅ |
| (R2-2) \(C^0\xrightarrow{D_0}C^1\xrightarrow{D_1}C^2\) | 线性映射链 | \(D_0,D_1\) 分别携带目标空间/源空间单位 | ✅ |
| (R2-3) \([r]\in \ker D_1/\operatorname{im}D_0\) | 商空间元素 | \(r\in C^1\)、\(\operatorname{im}D_0\subset C^1\)，同属残差空间单位 | ✅ |
| (R2-4) \(D_1^{(j)}D_0^{(j)}=0\) | \(C^{0,j}\to C^{2,j}\) 映射 | 零映射，同一映射空间 | ✅ |
| (R2-5) \([r^{(j)}]\in\ker D_1^{(j)}/\operatorname{im}D_0^{(j)}\) | 商空间元素 | \(r^{(j)}\) 与 \(\operatorname{im}D_0^{(j)}\) 同属 \(C^{1,j}\) | ✅ |
| (R2-6) \(\epsilon_\perp=\{I-A(A^\top A)^+A^\top\}z\) | 无量纲白化残差 | \(A=WD_0\)，\(z=Wr\)；括号内为无量纲投影矩阵，乘无量纲 \(z\) | ✅ |
| (R2-7) \(\Pi_{\perp\operatorname{im}D_0}^{(W)}r=W^{-1}\epsilon_\perp\) | 残差单位 | \(W^{-1}\) 恢复残差单位，\(\epsilon_\perp\) 无量纲 | ✅ |
| (R2-8) \(\epsilon_\perp^{(j)}=\{I-A_j(A_j^\top A_j)^+A_j^\top\}z_j=0\) 或 \(\|\epsilon_\perp^{(j)}\|\le\tau_j\) | 无量纲白化残差/范数 | 右侧零与 \(\tau_j\) 应为无量纲阈值 | ✅ |

超越函数检查：全文关键公式未使用 `exp`、`sin`、`log`、`sinh` 等超越函数；无自变量量纲问题。

警告：\(\tau,\tau_j,\tau_c\) 在文本中作为阈值出现；其中 \(\tau,\tau_j\) 应明确为白化空间的无量纲阈值，\(\tau_c\) 应明确为对应矩阵范数中的阈值。当前不构成量纲阻断，但后续数值化时必须标注。

## Q2. 符号/方向校对

方向性结论检查：

| 结论 | 极限/代入检查 | 方向判定 |
|---|---|---|
| \(D_1D_0=0\) 时 \(\operatorname{im}D_0\subseteq\ker D_1\) | 任取 \(v=D_0u\)，则 \(D_1v=D_1D_0u=0\)，故 \(v\in\ker D_1\) | ✅ |
| 若 \(D_1D_0\neq0\)，则 \(\ker D_1/\operatorname{im}D_0\) 未定义为该复形的 \(H^1\) | 因存在 \(u\) 使 \(D_1D_0u\neq0\)，\(\operatorname{im}D_0\not\subseteq\ker D_1\)，不能取该商 | ✅ |
| 若 \(D_1r\neq0\)，则 \(r\) 不是 obstruction class 而是 inconsistency flag | \([r]\in \ker D_1/\operatorname{im}D_0\) 要求 \(r\in\ker D_1\)；代入 \(D_1r\neq0\) 违反定义域 | ✅ |
| \(\|\epsilon_\perp\|\le\tau\) 判为可吸收，\(\|\epsilon_\perp\|>\tau\) 才进入扩张库压力测试 | 极限 \(\epsilon_\perp\to0\)：完全位于允许方向，方向为可吸收；极限 \(\|\epsilon_\perp\|\to\infty\)：不可由当前允许方向解释，方向为压力测试 | ✅ |
| 若所有合法扩张均有 \(\|\epsilon_\perp^{(j)}\|>\tau_j\)，只能得到有限库未吸收 | 对任意合法 \(j\) 都未过阈值，只能排除已列入库吸收；不能推出库外模型不存在 | ✅ |

未发现分子分母放反或负号丢失问题。

## Q3. 循环论证校对

验证/检验类操作：

| 操作 | 输入假设 | 检验数据来源 | 循环性 |
|---|---|---|---|
| 复形条件 \(D_1D_0=0\) 检查 | 给定 \(D_0,D_1\) | 直接矩阵乘法 | ✅ 无循环 |
| \(r\in\ker D_1\) 检查 | 给定 \(r,D_1\) | 直接计算 \(D_1r\) 或白化约束残差 | ✅ 无循环 |
| 扩张后重算 \([r^{(j)}]\) | 给定合法扩张 \(j\) 及 \(D_0^{(j)},D_1^{(j)},r^{(j)}\) | 重新构造后的矩阵和残差 | ✅ 无循环；文本明确禁止旧类口头拉回 |
| 白化投影 \(\epsilon_\perp\) | 给定 \(\Sigma,D_0,r\) 与阈值 \(\tau\) | 线性代数投影计算 | ✅ 无循环，前提是 \(\Sigma,\tau\) 不是事后调参 |
| 定理 R2-A no-go | 假设存在合法扩张且 (R2-8) 成立 | 从假设推出可吸收结论 | ✅ 这是条件定理，不是用生成数据验证同一假设 |

警告：文本已指出若 \(\tau\) 或合法扩张库 \(\mathfrak L\) 事后选择，则会退化为过拟合诊断。该点是方法使用边界，不是当前代数推导的循环论证阻断。

## Q4. 量级鸿沟标记

未发现 \(10^N\) vs \(10^M\) 的量级估算比较。  
未使用实验数值或参数代入。  
结论：✅ 无量级鸿沟可标记。

## Q5. 代数验算

### 5a. 逐步展开

1. 复形推出包含关系：
   \[
   v\in\operatorname{im}D_0\Rightarrow \exists u,\ v=D_0u.
   \]
   \[
   D_1v=D_1D_0u=0.
   \]
   因此 \(v\in\ker D_1\)，即 \(\operatorname{im}D_0\subseteq\ker D_1\)。符号与方向正确。

2. 白化投影：
   \[
   W=\Sigma^{-1/2},\quad A=WD_0,\quad z=Wr.
   \]
   欧氏内积下到 \(\operatorname{im}A\) 的正交投影为
   \[
   P_A=A(A^\top A)^+A^\top.
   \]
   正交残差为
   \[
   \epsilon_\perp=(I-P_A)z
   =\{I-A(A^\top A)^+A^\top\}z.
   \]
   该式与 (R2-6) 一致。若 \(A\) 列满秩，\((A^\top A)^+=(A^\top A)^{-1}\)；若不满秩，使用 Moore-Penrose 伪逆仍给出到 \(\operatorname{im}A\) 的投影。代数正确。

3. 从白化残差回到原残差空间：
   \[
   \Pi_{\perp\operatorname{im}D_0}^{(W)}r=W^{-1}\epsilon_\perp.
   \]
   当 \(\Sigma\succ0\) 时 \(W\) 可逆，该式合法。若只在可观测子空间正定，则应把 \(W^{-1}\) 改写为相应子空间伪逆或限制映射；文本已作为失败边界说明。当前公式在其明示正定前提下成立。

4. R2-A 推理：
   \[
   \epsilon_\perp^{(j)}=0
   \Rightarrow z_j\in\operatorname{im}A_j
   \Rightarrow W_jr^{(j)}=W_jD_0^{(j)}u
   \Rightarrow r^{(j)}=D_0^{(j)}u
   \]
   其中最后一步要求 \(W_j\) 在相关空间可逆。因此 \([r^{(j)}]=0\)。若仅 \(\|\epsilon_\perp^{(j)}\|\le\tau_j\)，只能推出统计上低于阈值，不推出严格代数零类。文本已使用“或统计上不可区分于零”，方向正确。

### 5b. 极限退化

| 公式 | 极限 1 | 极限 2 | 判定 |
|---|---|---|---|
| (R2-6) | \(D_0=0\Rightarrow A=0\)，\(\epsilon_\perp=z\)：无允许吸收方向时残差全保留 | \(r\in\operatorname{im}D_0\Rightarrow z\in\operatorname{im}A\)，\(\epsilon_\perp=0\)：完全吸收 | ✅ |
| (R2-7) | \(\epsilon_\perp=0\Rightarrow\Pi r=0\) | \(W=I\Rightarrow \Pi r=\epsilon_\perp\)，退化为普通欧氏投影残差 | ✅ |
| (R2-8) | \(\tau_j=0\)：只有严格零残差可吸收 | \(\tau_j\to\infty\)：任意白化残差都被阈值接受，判据失去区分力 | ✅，且支持文本中阈值需预注册的警告 |

### 5c. 数值量级验证

没有声称的实验数值、物理参数数值或量级估算；无需代入计算。

### 5d. 引用数值来源级别

文本中的具体数字主要为公式编号、年份和 DOI，不作为推导数值使用。无需要验算的数值来源缺失。

## Q6. 综合判定

✅ INSPECTOR通过。A路 R3 Round2 的核心公式 (R2-0)--(R2-8) 在量纲、符号方向、循环论证、量级鸿沟与代数验算层面未发现阻断错误。

⚠️ INSPECTOR警告：\(\tau,\tau_j,\tau_c\)、\(\Sigma\) 的可逆/子空间伪逆规则、以及合法扩张库 \(\mathfrak L\) 的预先给定性必须在后续数值化或实例化时显式标注。可继续，但不能把事后阈值或事后扩张当作机械检验通过。
