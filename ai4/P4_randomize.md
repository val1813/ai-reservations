# P4: AI Detection Restructuring — Structure Randomizer

> 角色: 统计约束生成器。不写正文,只生成数字。正文由AI按数字写。
> 核心原理: AI检测器做统计假设检验(H0=人写, H1=AI写)。
>   我们的目标: 让文本统计量落在人类分布内。靠随机参数的高方差实现。
> ⛔ 此Phase必须在所有内容修改完成后执行。之后禁止任何内容修改!
> 输入: Phase 2+3审查通过的终稿
> 输出: AI检测率<15%的目标投稿稿

---

## §0 Deep-Humanize 结构诊断 (先行步骤)

### 诊断6个致命对称

扫描全文,检查以下AI特征:

1. **段落长度均匀**: 所有段落都是4-6句? → 重组,制造长短落差
2. **句长均匀**: 所有句子15-25词,标准差<5? → 标记需打破的段落
3. **连接词密度**: 每段都有"However/Moreover/Furthermore"? → 删除30-50%
4. **穷举结构**: "First,... Second,... Finally,..." → 改成不对称表达
5. **安全收尾**: 每段最后一个词都是安全词? → 打破pattern
6. **模板重复**: 连续段落使用相同叙事模板? → 重组

### 结构重组 (不改句子,只改结构)

- 删除roadmap句 ("In this section, we will...")
- 合并或拆分section (打破IMRaD对称性)
- Discussion和Introduction的段落数不对称

→ 输出: paper_output/restructured_draft.tex

---

## §1 参数体系 (14维)

每个段落生成14个参数: [S, T, P, K, W, E, D, C, R, V, F, B, L, H]

### 基础10维

| # | 参数 | 含义 | 取值范围 |
|---|------|------|---------|
| 1 | S | 句子数 | 2-12 (PRL: 2-8) |
| 2 | T | 段落模板 | 1=assertion-first 2=evidence-first 3=narrative 4=compare-judge 5=causal-chain 6=abrupt-end |
| 3 | P | 开头方式 | 1=主语直接(37%) 2=介词/状语(22%) 3=While/However让步(18%) 4=引用他人(12%) 5=It is/被动(11%) |
| 4 | K | 短句数(≤8词) | 0-3 |
| 5 | W | 平均词数/句 | 10-28 (PRL: 10-24) |
| 6 | E | 结尾方式 | 1=直接停(40%) 2=前瞻指针(25%) 3=含义陈述(20%) 4=开放/不确定(15%) |
| 7 | D | 信息密度 | 1=H(高) 2=M(中) 3=L(低) |
| 8 | C | 连接词预算 | 0-2 (0=零连接词) |
| 9 | R | 引用密度 | 0-4 |
| 10 | V | 语气色彩 | 1=客观 2=评价(全文≤4次) 3=承认不确定(全文≥2次) 4=推测(全文1-2次) |

### 补充4维 (针对实测残留AI问题)

| # | 参数 | 含义 | 取值 | 解决的问题 |
|---|------|------|------|-----------|
| 11 | F | 冗余句数 | 0-2 | 密度均匀。F=1表示必须有1句"低效"句 |
| 12 | B | 逻辑断裂 | 0/1 | 连接太完美。B=1表示与上段无过渡直接跳入 |
| 13 | L | 列举限制 | 0-3 | 穷举结构。L=0禁止列举; L≤2最多列举2项 |
| 14 | H | 段内句长标准差 | S/L/H | 句长band窄。S=<5词, L=5-10词, H=>10词 |

### 全文约束

```
F=0的段落 ≤ 60% (人类文本~40%句子是低信息密度的)
B=1至少2次,最多4次 (分布在section间过渡处)
L=0至少占30%段落 (强制用其他方式表达范围)
H=S ≤ 30%, H=H ≥ 20% (确保句长有波动)
```

---

## §2 全局约束 (生成后必须校验)

为全文所有段落一次性生成参数 → 检验 → 不通过则**整体重新生成**(不是修补):

### 方差约束

```
S值标准差 > 2.5 (段落长度必须不均匀)
W值标准差 > 4.0 (句长中心必须波动)
S最大-S最小 ≥ 6 (必须有极短和极长段共存)
W最大-W最小 ≥ 10 (必须有简洁段和复杂段)
```

### 不重复约束

```
相邻T不同: T[i] ≠ T[i+1]
连续H≤2: 不超过2段连续D=H(高密度)
连续3段S差<2禁止: max(S[i:i+3])-min(S[i:i+3]) ≥ 3
连续3段W差<3禁止: max(W[i:i+3])-min(W[i:i+3]) ≥ 4
T值无一值占>35%: 每种T最多占总段落35%
E=3全文≤3次: 含义陈述结尾不超过3段(AI最爱的结尾)
V=1不超过70%: 客观陈述不超过70%段落
```

### AI Pattern自动检测与修正

```
Pattern B风险: T=3且E=3 → E强制改为1或4
Pattern D风险: 连续3段T相同 → 中间段T重新随机
Pattern E风险: 连续3段D=1(全高密度) → 中间段D改为2或3
对称风险: section内所有S值差<2 → 随机选1段S改为min-2或max+3
全文连接词超标: C总和>段落数×0.8 → 随机选30%的C=1段改为C=0
```

### 无周期性检查

```
对每个参数X ∈ {S, T, W, D, V}:
  对周期p ∈ {2,3,4}:
    检查X[i] ≈ X[i+p]对>60%的i成立 → REJECT,重新生成

允许的"伪周期": 只有1个参数呈弱周期(60-70%匹配)且其他参数无周期→PASS
```

---

## §3 Section级预设

### Introduction (3-5段)
```
S: 偏大(5-10为主),允许1段≤3句的过渡
D模式: [H,M,H,L]或[M,H,M,H,L]随机
R: 前60%段落R=2-4(文献重),后40%段落R=0-1
V: V=1为主,最后一段可V=2
禁止: 最后一段不用T=3(不以问句结构结尾)
```

### Theorem/Proof (不参与随机化)
```
固定格式: S=1-2, T=1, P=1, K=0, E=1, D=1, C=0, V=1
仅"评价段"参与随机化
```

### Results/Data (2-4段)
```
S: 中等(3-7为主)
D模式: [H,L,H]或[H,M,H]
K: 每段至少K=1(数据句倾向短)
V: 允许V=3出现1次
```

### Discussion (3-5段)
```
S: 高方差(有2句段也有9句段)
D模式: [M,H,H,L]或[H,M,H,M]
V: 必须包含≥1个V=3和≥1个V=4
C: 允许稍多(每段C≤2)
E: 至少1段E=4(开放结尾)
```

### Conclusion (1-2段)
```
S: 3-5
T: T=6(abrupt)或T=1(assertion)
E: E=1或E=4,禁止E=3
D: H
V: V=1或V=2
禁止: 不得使用T=5(causal)——防止逐条重述
```

---

## §4 词数预算系统

### 目标期刊词数

| 期刊 | 正文词数 | Abstract |
|------|---------|----------|
| PRL | ~3500(含refs)→正文~2000-2500 | ≤120 |
| PRD | 无硬限→建议3000-4000 | ≤150 |
| PRX | 无硬限→建议4000-6000 | ≤150 |
| Nature Physics | ~3000正文 | ≤150 |

### Section词数分配 (理论/计算类)

| Section | 比例 | PRL(~2200) | PRD(~3500) |
|---------|------|-----------|-----------|
| Introduction | 18-22% | ~440 | ~700 |
| Model/Formalism | 10-14% | ~264 | ~420 |
| Results/Data | 15-20% | ~385 | ~612 |
| Mechanism | 12-16% | ~308 | ~490 |
| Discussion | 8-12% | ~220 | ~350 |
| Conclusion | 3-5% | ~88 | ~140 |

### 从预算到段落参数

```
1. 先随机N_para(段落数)
2. 对每段随机S_i,计算W_i_target = W_sec / Σ(S_i)
3. 在W_i_target ±30%范围内随机W_i
4. 计算实际Σ(S_i × W_i)
5. 与W_sec偏差>15% → 调整最长段的S或W
6. 偏差≤15% → 接受

缩放: W_estimated/W_total不在[0.85,1.10]→每段W乘以scale(W_total/W_estimated)
     clamp(W_i_adjusted, 8, 32)
```

---

## §5 执行流程

### 5a. 主文 (完整14维)

```
Step 1: 确定section列表和段落数
Step 2: 为目标期刊计算W_total → 分配各section预算
Step 3: 为所有段落一次性生成14维参数
Step 4: 全局约束校验 → 不通过整体重新生成
Step 5: 输出Blueprint (paper_output/blueprint.md)
Step 6: 按Blueprint逐段重写
  - 每段严格服从14维参数
  - S: ±1句, W: ±3词(弹性)
  - K/F/B/L/C/R/V: 精确
Step 7: 验证 (全局约束re-check + AI pattern终检)
```

### 5b. SM补充材料 (简化8维)

```
适用维度: S, T, K, W, E, D, C, V (去掉R引用/P开头)
不参与: Derivation/Proof sections, Parameter Tables

文字说明段(N=1-3段):
  S: 2-6 (SM段落比正文短)
  T: 禁止T=3(narrative)和T=5(causal),只用T=1/2/4/6
  D: [H,L]或[H,M],不允许连续两段H
  V: 至少1处V=3(承认局限/近似条件)
  E: 禁止E=3(含义陈述)
  F: 至少30%段落F=1
  L: 各subsection穷举不重复正文中已穷举过的

重点检查:
  ① 各subsection引言句是否重复同一模板 → B=1强制跳入
  ② 结尾是否都用"which completes the proof" → E强制E=1(直接停)
  ③ 说明段长度是否不等 → 允许某节只有1句
```

### 5c. Cover Letter (轻量3维)

```
逐句生成3个参数: [W_sentence, V_sentence, Break]

W_sentence: 该句词数
  分布目标: 不均匀,要有≤8词短句和≥30词长句共存
  禁止: 连续3句词数差<5词

V_sentence: 该句语气
  1=客观陈述(默认)
  2=作者判断("We believe...")
  3=承认局限("We recognize that...")
  全文: V=2至少2句, V=3至少1句

Break: 句间逻辑断裂
  0=正常承接
  1=上句和话题突然切换(全文最多1次)

高危pattern及修复:
  Contribution list三条完全等长平行对称 → 一条1句,一条3句,一条2句,长度刻意不等
  "This paper presents X, Y, and Z"穷举 → 只点最核心1个,其余用"among other results"带过
  "We hope this work will..." → 改成具体期待或直接停
  "We are confident that..." → 删掉或改成"The data suggest that..."

不参与的部分: 称呼行、日期、署名、期刊名引用句、利益冲突声明
```

---

## §6 AI Pattern 终检

生成全文后,扫描以下pattern并标记REJECT:

```
1. "Not X; it is Y"结构 → 全文最多1次。第2次→REJECT重写。
2. 分号对仗 "Star does A; Chain does B; Cyclic does C" → 全文最多1次。
3. 相同sentence frame重复 → "X shows... Y shows..." → REJECT。
4. "spanning A, B, C, and D"穷举 → 全文最多1次。
```

### 不确定性表达细分 (V=3子类)

```
V=3的2-3次使用必须来自不同子类:
  3a: 数据层面不确定 "The data suggest X but the sample size is limited..."
  3b: 机制层面不确定 "We cannot explain why the optimum is at 0.02..."
  3c: 范围层面不确定 "Whether this holds beyond N=7 we have not tested."
  3d: 隐式不确定(不说"uncertain") "The connection is formal at best."

⛔ 绝对禁止的hedging措辞 (已被GPTZero学会识别):
  "We should be candid about..."
  "It remains an open question whether..."
  "We leave this for future work."
  "Further investigation is warranted."
```

### 紧急简化版 (时间不够时)

```
只为以下5个高危位置生成参数:
1. Introduction最后一段: [S, T, E]
2. Discussion第一段: [S, T, V]
3. Discussion最后一段: [S, T, V, E]
4. Conclusion: [S, T, E]
5. 最长的那个Results subsection: [S, T, D]

这5个位置贡献了GPTZero检测率的大部分。
```

---

## §7 不参与随机化的内容

```
Theorem/Proof正文 (数学固定格式)
Equation引入句 ("The correction is:" 固定)
Figure/Table caption (另有格式)
itemize/enumerate内容 (列表格式固定)
Abstract (单独处理: L总词数 + N句子数(4-7) + Break在第几句后转折)
```
