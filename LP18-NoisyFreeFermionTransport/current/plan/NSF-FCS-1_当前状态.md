# NSF-FCS-1 当前状态

**状态：** AB Round 2 完成，INSPECTOR 通过。

**来源：** north_star_closure.md 优先级重算，分数 8.8。

**前置材料：**
- A round3: boundary conductance 标度已收敛。
- Inspector A round3: `lambda_R''(0)` 同标度为额外假设，需验证。
- B round3: holonomy 副线已降级，不应干扰主线。

## Round 1 结果

- A：写出右 reservoir-current tilted generator；`lambda_R''(0)` 进入 Poisson/Green-Kubo 形式。
- B：独立给出 activity + Green 相关项分解，并提出 `S_R(L)=lambda_R''(0)/G_R(L)` 作为诊断。
- INSPECTOR：B 初稿公式类型错误已修正；A/B 均通过。

**下一步：** Round 2。A 攻 resolvent / H_-1 norm / nonlocal Dirichlet form 标度；B 设计低密度/单粒子 Poisson 方程数值判据。

## Round 2 结果

- A：发现并修正关键符号问题；jump-current FCS 二阶项不是纯正 `H_-1`，完整公式含 martingale cross term。
- B：给出最小矩阵算法，但后续必须输出完整二阶分解或直接 tilted generator 二阶数值。
- INSPECTOR：A 初稿阻断，修正后通过；B 通过。

**下一步：** Round 3。A 查 nearest-neighbor/slow-boundary SSEP 的 current variance cancellation 机制；B 改算法以输出 `<a>`、corrector、cross term 或直接二阶 tilted eigenvalue。
## Round 3 结果

- A：用 fast open SSEP / slow-boundary SSEP 的 current FCS 对照，确认完整二阶公式可写成 `lambda_R''=<sum c(q_R+Delta phi)^2>`；对未缩放 long-jump reservoir，若 `A_R(L)=O(1)` 而 `G_R(L)->0`，则必须证明 fast-boundary 型强 cancellation。
- B：把验证方案压成台账：输出 `<a>`、`2<h,phi>`、`2<C>`、`lambda_R''`、`G_R`、`S_R`；当显式 `C` 不稳定时，以 tilted generator 主特征值二阶差分作为总量。
- INSPECTOR：A 通过，条件警告为 reservoir tail 若含额外 `L` 缩放则改判 slow-boundary 型；B 警告可继续，`C_from_tilted_residual` 只能作 residual 报告，不能作独立 balance 验证。

**当前精确命题：** `lambda_R''~G_R` 等价地应先检验 `D_R(L)=<sum_R c(q_R+Delta phi)^2>_pi=O(G_R(L))`。

**下一步：** Round 4 定向推进。A 做单粒子 long-jump reservoir 的 Poisson/capacity test；B 给出最小矩阵台账算法或脚本规范，用已校准 `G_R` 与稳定 `lambda_tilt''` 给出 keep/kill。
## Round 4 结果

- A：单粒子最小模型显示 bare right-reservoir exchange current 是 occupation coboundary，长期二阶曲率 `lambda_R''(0)=0`；因此原始 bare-exchange 强命题应 kill。若加入远端 Dirichlet sink/source，transport 版本只能 conditional keep，依赖未证 `D_R~Cap` lemma。
- B：初版闭合可逆 reservoir-node 台账被 INSPECTOR 阻断；修正版改为 open two-terminal transport ledger，并通过 recheck。bare exchange/coboundary observable 被硬门控为 `INVALID_BARE_EXCHANGE_NOT_TRANSPORT`。
- INSPECTOR：A 警告可继续，强调 `D_R<=Cap` 可用但 `D_R~Cap` 未证；B 修正版通过，带实现警告。

**当前判定：** NSF-FCS-1 的 bare reservoir-exchange 版本关闭；two-terminal transport-FCS 版本 conditional keep。

**下一步：** 落地最小 two-terminal transport ledger，计算 `lambda_T''`、`G_R`、`S_T=lambda_T''/G_R`；若 valid ledger 显示 `S_T` 分叉/漂移，则 kill transport 版本，否则进入 many-particle 或 analytic capacity lemma 阶段。
## Transport ledger 落地结果

- 已新增 `scripts/nsf_fcs_transport_ledger.py`，实现 channel-resolved open two-terminal single-particle ledger。
- 正式输出：`current/plan/nsf_fcs_transport_ledger.csv`，15 行全部 valid。
- bare sanity check：`current/plan/nsf_fcs_transport_ledger_bare_check.csv`，bare exchange 被硬门控为 `INVALID_BARE_EXCHANGE_NOT_TRANSPORT`，`S_R=NA`。
- 数值结论：`alpha=0.5,1.0,1.5` 下，`lambda_T''` 与 `G_R` 的 log-slope 一致，`S_T=lambda_T''/G_R≈2` 且无漂移。

**当前判定：** transport-FCS 改写版通过 single-particle minimal falsifier，暂时 KEEP 到下一阶段；bare exchange 版本仍关闭。

**下一步：** 选择 analytic `D_R~Cap` lemma 或 finite-density exclusion ledger。若继续 numerical，优先扩展到多粒子 exclusion sector；若继续 analytic，优先证明 reservoir-edge residual 是否与 total capacity 同阶。
## Finite-density exclusion ledger 结果

- 已扩展 `scripts/nsf_fcs_transport_ledger.py`：新增 `--sector exclusion`，状态空间为 occupation bitmask，包含 exclusion bulk jumps 与 channel-resolved source/sink reservoirs。
- 正式输出：`current/plan/nsf_fcs_exclusion_ledger.csv`，`L=4,5,6,7,8`、`alpha=0.5,1.0,1.5` 共 15 行全部 valid。
- 数值结论：finite-density exclusion 中 `lambda_T''` 与 `G_R` 的 log-slope 完全一致，`S_T=lambda_T''/G_R≈2` 且无漂移。

**当前判定：** transport-FCS 改写版通过 finite-density minimal falsifier，KEEP 强度上升。当前最有价值的新问题是：`lambda_T''(0)=2G_R` 是否是 equilibrium two-terminal symmetric gauge 下的有限体积 FDT/Einstein 恒等式。

**下一步：** 进入 analytic FDT 证明/反证。若恒等式成立，应把 NSF-FCS-1 的二阶问题降级为 FDT corollary，并转向非平衡、非对称 reservoir 或高阶 cumulants。
## Round 5 结果

- A：定位并推导 equilibrium two-terminal transport current 的有限体积 FDT/Einstein-Helfand 恒等式 `lambda_T''(0)=2G_T`。
- B：给出破坏 FDT 前提的方向：NESS density bias、non-LDB、activity/frenetic forcing、finite-frequency noise、高阶 cumulants；指出 pure affinity split 与 equilibrium random reservoir 不应单独破坏二阶 FDT。
- INSPECTOR：A/B 均警告通过。A 的关键警告是 affinity 方向必须固定为脚本规范 `A_ledger=F=eta_R-eta_L`；B 的关键警告是 finite-frequency resolvent 需投影/伪逆，activity forcing 需同时作用正反 rate。

**当前判定：** equilibrium transport second cumulant 分支收束为 FDT corollary；不再作为主攻问题。

**下一步：** 推进 Tier 0/Tier 1 扩展。先做 affinity split sanity，再做 NESS (`rho_L != rho_R`) 与 non-LDB/activity forcing ledger，观察 `FDT_residual_R2=lambda_T''-2G_T` 是否出现稳定标度。
## Tier 1 NESS 推进结果

- Tier 0 affinity split sanity 已通过：`a=0,0.25,0.5,0.75,1` 均保持 `S_T≈2`。
- Tier 1A NESS ledger 已完成：`rho_left=0.4`、`rho_right=0.6`，`L=4..7`、`alpha=0.5,1.0,1.5` 共 12 行全部 valid。
- NESS 下 `S_T` 明确偏离 2，`R2=lambda_T''-2G_T` 非零并有稳定标度。

**当前判定：** equilibrium NSF-FCS-1 已收束；更高价值问题已转为 `NSF-FCS-2: NESS FDT residual scaling`。

**下一步：** 扩大 NESS 扫描并加入 non-LDB/activity forcing；若 residual 斜率稳定，将 `NSF-FCS-2` 正式切为当前北极星。
## 2026-06-03 NSF-FCS-2 正式切换

- 最新 NESS bias scan 已完成：`rho_left/rho_right=0.45/0.55,0.40/0.60,0.35/0.65`，`L=4..8`，`alpha=0.5,1.0,1.5`，45 行全部 `ROW_VALID`。
- `R2=lambda_T''-2G_T` 在所有测试中稳定非零。
- 固定 `L=8` 时，`R2` 对 `delta=|rho_R-rho_L|` 的斜率约等于 2，说明 near-equilibrium 首个非零残差为二阶偏置效应。
- 按 alpha 分组的 `R2` 尺度斜率稳定：`alpha=0.5 -> ~1.009`，`alpha=1.0 -> ~0.621`，`alpha=1.5 -> ~0.279`。

**判定：** NSF-FCS-1 的 equilibrium second-cumulant 主线正式收束为 FDT corollary；当前主攻问题切换为 `NSF-FCS-2: long-jump open exclusion 的 NESS FDT residual scaling`。

**新状态文件：** `current/plan/NSF-FCS-2_当前状态.md`

**新综合文件：** `synthesis/PI_NSF_FCS_ness_bias_scan_result.md`
