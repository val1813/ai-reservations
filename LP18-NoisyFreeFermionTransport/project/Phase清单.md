# Phase 执行清单

> 每个Phase开始前读取此文件。每完成一步，把 `[ ]` 改成 `[✅]`。
> 全部勾完才允许进入下一步。

---

## Phase启动

```
[✅] 读 项目/北极星队列.md → 确认当前北极星+优先级分数
[✅] GATE 0: 文献库.md存在？先发检索栏有判定结论？
[✅] GATE 1: 文献库.md反例栏非空？
[✅] 写 当前状态.md（含轮次计数+前置检查）
[✅] 写 研究计划.md（如果不存在的轮次）
[✅] AHA检查: 连续5轮无AHA？→触发AHA访客
```

## AB探索（每轮）

```
[✅] 启动A博士Agent（独立实例，传入当前北极星+已知上下文）
[✅] 启动B博士Agent（独立实例，传入当前北极星+已知上下文）
[✅] ⛔ 确认A框架 ≠ B框架（读两者的§0声明）
[✅] ⛔ 确认B没读A的产出（反之亦然）
[✅] 等两者都完成
```

## 每轮交作业

```
[✅] INSPECTOR — 用Agent工具启动独立INSPECTOR，传入A推导文件
[✅] INSPECTOR — 用Agent工具启动独立INSPECTOR，传入B推导文件
[✅] 读INSPECTOR结果 → 有阻断？→A/B修正→重新提交INSPECTOR
[✅] PI综合推导（读A+B产出→汇合判断→写synthesis/）
[✅] 更新 知识库.md（新增K条目）
[✅] 更新 当前状态.md（轮次+1，更新前置检查框）
[✅] ⛔ 检查停止条件：触发硬停止？or N≥3轮？
      N<3 且未硬停止 → 继续下一轮（回到"AB探索"）
      N≥3 或已硬停止 → 进入"北极星收尾"
```

## 北极星收尾

```
[✅] GATE 1.5: grep A推导文件中"深挖1"和"深挖2"各≥2层？B同？
      通过→继续。不通过→A/B补深挖→INSPECTOR→GATE 1.5再来（最多2次）
[✅] Re-escalation: 声张是否比启动时更窄？→列出被杀死的声张→A/B写更大声张草案
[✅] 矛盾深挖: 用"五个为什么"追溯驱动矛盾→挖到基础原理层
[✅] 更新 项目/北极星队列.md — 优先级矩阵重算
[✅] 检查优先级队列 → 有更高分候选？→触发切换
      是→暂停当前，旧状态保存，启动新北极星
      否→继续收官
```

## 收官

```
[✅] PI最终综合推导（汇合判断：一致/互补/矛盾）
[✅] GATE 3: current/B/存在？B的§0≠A的§0？
[✅] GATE 4: 卡点登记册无开放致命卡点？
[✅] GATE 2: 启动REVIEWER Agent（终审）
[✅] ⛔ REVIEWER验证: 任何"引用虚构"/"先发冲突"→PI用WebSearch独立验证
[✅] GATE 6: shared/知识库汇总.md末尾追加本课题K条目
[✅] GATE 7: knowledge_graph/[课题名]_v[版本号]_[日期].json 存在？
[✅] 更新 项目/北极星队列.md（标记完成+结论类型）
[✅] 可选: 回写 shared/北极星候选池.md（跳过：项目内动态发现不回写 shared 候选池）
[✅] 读取优先级矩阵 → 下一个北极星
```

---

## 禁止事项

```
⛔ 禁止1轮就收官（N<3且未硬停止→必须继续）
⛔ 禁止PI手写INSPECTOR报告（必须启动独立Agent）
⛔ 禁止跳过GATE 1.5的grep验证（必须显示grep输出）
⛔ 禁止PI发明SOP不存在的步骤（如交叉攻击、自我攻击反转）
⛔ 禁止REVIEWER结论直接采信（"引用虚构"指控→PI独立验证）
```
---

## NSF-FCS-2 Round 2 Phase启动（REVIEWER major revision response）

```
[✅] GATE -1: 核心矛盾结构验证；若非 L-1 双真矛盾型，记录不通过原因并转入 REVIEWER 大修验证清单
[✅] 读 项目/北极星队列.md → 确认当前北极星和优先级分数
[✅] 写 NSF-FCS-2_Round2_当前状态.md（含 REVIEWER 五条约束）
[✅] 写 NSF-FCS-2_Round2_研究计划.md
[✅] AHA检查：是否有更高价值议题？
```

## NSF-FCS-2 Round 2 大修验证清单

```
[✅] 直接验证 `R2 ~ delta^2`：多组更小 delta，不先除以 delta^2
[✅] off-center reverse-bias：rho_bar=0.4 和 0.65 的正反向对照
[✅] FDT normalization ledger：明确 lambda_T''、G_T、counting field、time unit 的 convention
[✅] Qhat 大 L / 模型比较：constant+correction、log drift、crossover power
[✅] non-LDB controls：实现/设计 reversible_side 与 nonLDB_site_skew 分离
[✅] 更新知识库和当前状态
[✅] 检查停止条件；若未硬停则进入 Round 2 A/B
```

## NSF-FCS-2 Round 2 A/B re-attack

```
[✅] A博士 Round 2 revised package re-attack：current/A/NSF-FCS-2_round2_A.md
[✅] B博士 Round 2 revised package re-attack：current/B/NSF-FCS-2_round2_B.md
[✅] INSPECTOR 分别校对 A/B Round 2 输出
[✅] PI Round 2 A/B 综合：KEEP / DOWNGRADE / REDIRECT
```

## NSF-FCS-2R coefficient/parity validation

```
[✅] 写 NSF-FCS-2R 当前状态与实验计划
[✅] coefficient extraction：固定 L,alpha 拟合 `R2=C_L delta^2 + D_L delta^4`
[✅] activity parity：`A=+a,-a` 区分 `A` 与 `A^2`
[✅] separability synthesis：判断 density-bias curvature-like coordinate 与 nonLDB skew 是否可分离
[✅] 更新知识库、队列、当前状态
[✅] 检查停止条件；若未硬停则进入下一轮 A/B 或收官门禁
```

## NSF-FCS-2R A/B validation review

```
[✅] A博士 NSF-FCS-2R coefficient/parity/separability review
[✅] B博士 NSF-FCS-2R coefficient/parity/separability review
[✅] INSPECTOR 分别校对 NSF-FCS-2R A/B 输出
[✅] PI 综合：KEEP / DOWNGRADE / REDIRECT / REVIEWER gate
```

## NSF-FCS-2T signed mixed-parity test

```
[✅] 更新当前状态与队列：NSF-FCS-2T parity tomography
[✅] nonLDB signed mixed scan：`delta=0,±0.02,±0.04`, `A=0,±0.05,±0.10`
[✅] reversible signed mixed scan：同窗口，作为 traffic-renormalization control
[✅] signed-basis fit：`delta^2`, `A^2`, `delta A`, `delta^2 A^2`
[✅] PI synthesis：判定 `delta A` 是否存在；是否进入 REVIEWER gate
[✅] 更新知识库/图谱/Phase 状态
```

## NSF-FCS-2T REVIEWER gate

```
[✅] 启动 REVIEWER Agent：审查 finite-window parity-tomography claim
[✅] PI 验证 REVIEWER 负面指控（若有引用虚构/先发冲突/覆盖风险）
[✅] PI final synthesis：accept / major revision / reject / re-escalate
```

## NSF-FCS-2T major-revision response

```
[ ] finite Markov-generator symmetry derivation：解释 `delta`, `A`, `delta A` 为何消失
[ ] ledger convention proof：自洽写出 `lambda_T''=2G_T`
[ ] numerical-floor robustness：eps/window/basis/condition-number checks
[ ] framework positioning：对照 frenetic response / Seifert-Speck / MFT / open-exclusion FCS
[ ] reversible traffic analytic separation or demotion
[ ] 更新知识库/图谱/当前状态
[ ] 检查停止条件；若未硬停则进入 A/B 或 REVIEWER recheck
```
