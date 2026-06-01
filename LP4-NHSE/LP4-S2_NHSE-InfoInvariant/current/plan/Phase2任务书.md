# Phase 2 任务书

## 目标
数值检验 QLIF 是否通过三重门槛：
1. freeze-rule independence
2. PBC/OBC 分离
3. 固定填充率平台稳定

## 模型
HN-Hubbard:

`H = - sum_j (t_R c_{j+1}^\dagger c_j + t_L c_j^\dagger c_{j+1}) + U sum_j n_j n_{j+1}`

可选 Lindblad:

`L_j = sqrt(G)(c_j + i alpha c_{j+1})`

## 扫描参数
- `L = 4, 6, 8, 10`
- `N = 1...L-1`
- `rho=N/L`
- `U`
- `t_L/t_R`
- PBC/OBC
- hard-delete / dephase-freeze / clamped-source

## 输出
1. `Delta T_N^f(L,rho)`
2. `nu_Q^f(L,rho)=sign(Delta T_N^f)`
3. 平台宽度 `W_f(L)`
4. 平台中心 `rho_f*(L)`

## 成功标准
全部满足才可升级为不变量候选：
- 三种 freeze 标签一致
- PBC/OBC 的差异可解释并在 bulk 标签上消失
- 平台宽度不缩窄
- 平台中心收敛并绑定到 bulk 谱结构

## 失败标准
任一成立即降级为诊断量：
- freeze 标签不一致
- OBC 差异保持 `O(1)`
- 无平台
- 平台宽度缩窄
- 平台中心漂移

## 下一步
实现最小数值脚本或手工构造符号检验表。
