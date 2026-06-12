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
Step 0: ⛔ 读取 paper_output/author_voice_card.md → 提取注意力分配
    - 标记"最在意"段落 → 这些段落S≥8,不参与全局S缩短
    - 标记"无聊但必要"段落 → 这些段落S≤2,不参与全局S扩展
    - 标记人格化特征使用位置 → 这些位置保留对应参数弹性

Step 1: 确定section列表和段落数
Step 2: 为目标期刊计算W_total → 分配各section预算
    ⛔ Voice Card"最在意"段落不受预算限制 (允许超出平均值3-5倍)
Step 3: 为所有段落一次性生成14维参数
    ⛔ "最在意"段落: S下限=8,不参与全局标准差降低
    ⛔ "无聊但必要"段落: S上限=2,不参与全局标准差提高
    ⛔ 人格化特征位置: K/V/E参数保持弹性
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

### §7a. 公式段落特殊处理 (物理/数学论文)

物理数学论文公式密集。随机化前必须先分类:

**步骤1: 计算每段的公式占比**

对每段执行(用Python或手工):
```python
import re
# 去掉display equations和inline math后统计文本长度
text_only = re.sub(r'\$\$.*?\$\$', '', paragraph, flags=re.DOTALL)  # display eq
text_only = re.sub(r'\$[^$]+\$', '', text_only)  # inline math
text_only = re.sub(r'\\begin\{equation\}.*?\\end\{equation\}', '', text_only, flags=re.DOTALL)
text_only = re.sub(r'\\begin\{align\}.*?\\end\{align\}', '', text_only, flags=re.DOTALL)
formula_ratio = 1 - len(text_only) / len(paragraph)
```

**步骤2: 按公式占比分级处理**

```
Type T (文本主导, formula_ratio < 0.3):
  → 完整14维随机化,正常处理
  S计数: 按text_only的句号/问号/感叹号计数

Type M (混合, 0.3 ≤ formula_ratio < 0.6):
  → 降级为6维: [T, V, E, C, R, B] (去掉S/K/W/D/F/L/H)
  保留叙事结构参数,放弃句长和密度参数
  句长不再约束——公式自然打破均匀性

Type E (公式主导, formula_ratio ≥ 0.6):
  → 最少2维: [T, V]
  只控制段落模板和语气色彩。其余参数不约束。
  这类段落的"人类感"来自公式本身的不规则性。

Theorem/Proof block: 不参与随机化,完全保持原样。
```

**步骤3: 全局约束调整**

公式段落多的论文,全局约束相应放宽:
- S值只统计Type T段落 (公式段落的S本就不受控)
- W值只统计Type T段落
- 方差约束: 如果Type T段落<全文50% → S std>2.0即可 (原2.5),W std>3.0即可 (原4.0)

**步骤4: 执行**

生成Blueprint前先对全文每段分类。Blueprint只包含Type T和M的参数,Type E标注"E级:仅[T,V]"。

---

## §8 去AI化 — ⛔ 双轨制: 禁止清单 + Voice要求

> 旧思路: "禁止AI词汇和句式" → 打地鼠,绕过这个AI换那个
> 新思路: "禁止底线(8a-8j) + Voice要求(8k)" → 正向注入人类特征,不只是被动回避
> 
> 原理: AI检测器做统计假设检验(H0=人写, H1=AI写)。
>   仅仅是"没有AI特征"还不够——因为你可能只是避开了已知模式。
>   真正的防御是"有人类特征"——AI检测器对强人类特征的文本误判率极高。
>   因为检测器在"AI特征缺失"时会倾向于判AI (保守策略),
>   但在"人类特征存在"时会倾向于判人类。
> 
> ⛔ 随机化管结构统计,本节管词汇+风格+人格。
> ⛔ 8a-8j 是底线(不做什么), 8k 是要求(必须做什么)。
> ⛔ 8k Voice要求优先于8a-8j 禁止清单: 
>   如果Voice要求使用某个"像AI"的词但对Voice有贡献 → 保留
>   (例: "I find this surprising." — 如果Voice Card要求第一人称,保留"I")

### 8a. 禁止连接词/过渡词 (用更人类化的方式替代)

| 禁止 | 原因 | 替代 |
|------|------|------|
| Moreover, Furthermore, | AI高频,均匀分布 | 偶尔用Also/Beyond this,更多时候省略直接陈述 |
| Nevertheless, Nonetheless, | AI最爱转折 | However(1段最多1次)或用具体对比句 |
| In conclusion, | AI标准收尾 | 直接陈述结论,不用前缀 |
| Firstly... Secondly... Finally... | AI穷举模板 | 不对称表达: "One factor is... Another... The third..." |
| It is worth noting that | AI标志句 | 删除,直接写内容 |
| It should be emphasized that | 同上 | 删除,直接写内容 |
| plays a crucial/important role | AI空洞强调 | 用具体机制替代:"enables X by providing Y" |
| has garnered significant attention | AI文献综述套话 | 不写"受关注",写具体为什么重要 |
| In this paper, we... / This paper presents... | AI论文开头模板(允许用1次在Abstract) | 正文中最多出现1次,其余省略直接论述 |
| As mentioned above / As discussed earlier | AI自我引用套话 | 直接用"Section X showed that..."或省略 |

### 8b. 禁止hedging措辞 (GPTZero已专门训练识别) + 防御性语言黑名单

```
⛔ AI检测器已学习的hedging:
  "We should be candid about..."
  "It remains an open question whether..."
  "We leave this for future work."
  "Further investigation is warranted."
  "Future studies should..."
  "This warrants further investigation."

⛔ 防御性自我贬低 (同时破坏AI检测和论文说服力):
  "It may be nothing." / "It may be an accident." / "It may be a coincidence."
  "Not a solution. Not even close."
  "We tried to derive it. We couldn't."
  "That does not make it correct."
  "It isn't one."
  "It would be dishonest to claim otherwise."
  "What is missing is not small."
  "We do not see a path from here to there."
  "We have nothing to add here except to mark the gap."
  "Whether [X] is useful is for the reader to judge."
  "We cannot stress that enough."
  "The result is not surprising."
  "What we prove is weaker than what one might want."
  "This is just a consistency check, not a new theorem."

替代: 具体化。不说"有待未来研究",说"当前数据在X条件下不适用,扩展到X需要Y工具"。
自我贬低句 → 直接删除(不需要替代,因为它们对技术内容无贡献)。
```

### 8c. 禁止句式结构 (AI pattern,非词汇)

```
⛔ "Not X; it is Y" 或 "X is not Y; rather, it is Z" → 全文≤1次
⛔ 分号对仗: "Star does A; Chain does B; Cyclic does C" → 全文≤1次
⛔ 穷举: "spanning A, B, C, and D" / "including X, Y, and Z" → 全文≤1次
⛔ 连续2句相同主语-谓语结构: "X shows... Y demonstrates..." → 改写
⛔ 每个段落以However/Thus/Therefore开头 → 不超过全文20%段落
```

### 8d. 连接词密度硬限

```
全文连接词密度: ≤4个/1000词 (AI通常8-15个/1000词)
连接词必须集中在2-3个关键转折处,其余段落零连接词
检查: 全文C值总和 ≤ 段落数×0.8
```

### 8e. 不确定性表达多样性

如果必须使用"不确定"表述,不能重复同一写法:

| 可用 | 例子 |
|------|------|
| 数据层面 | "The data suggest X but the sample size limits..." |
| 机制层面 | "We cannot explain why the optimum is at 0.02..." |
| 范围层面 | "Whether this holds beyond N=7 we have not tested." |
| 隐式(不说uncertain) | "The connection is formal at best." |

全文V=3出现2-3次,必须来自不同子类。连续2次同一子类→重写。

### 8f. Abstract特殊规则

```
禁止: "Here we present..." / "In this work, we demonstrate..."
替代: 直接陈述。 "X is shown to Y." 而不是 "In this paper, we show X does Y."

禁止: contribution list三条完全等长平行
替代: 长度刻意不等(一条1句,一条3句,一条2句)

禁止: 最后一句安全收尾 ("These results open new avenues...")
替代: 具体期待或直接停
```

### 8g. 执行

逐段重写时(Phase 4 §5 Step 6),每段写完后检查上述清单。命中→重写该段。
全文完成后→用Phase清单 Phase 4f做终检。

---

### 8h. AI词汇黑名单 — 整合blader/humanizer 30模式 + UCL语料库研究

> 来源: blader/humanizer (Wikipedia WikiProject AI Cleanup), matsuikentaro1/humanizer_academic,
> UCL TechSocial 2025 ("Marker Word Explosion" — 2023年后87%增长的AI标志词)

#### 8h-1. 意义膨胀词 (Significance Inflation) — 禁止

```
这些词在ChatGPT时代爆炸式增长(UCL 2025: 2023年后+87%)。
⛔ 强标志 (87%增长):
  intricate, meticulous, meticulously, commendable

⛔ 中标志 (18%增长):
  notable, pivotal, invaluable, noteworthy, methodically, strategically

替代: 具体化。不说"pivotal",说"X enables Y by...";不说"notable",直接给数字。
如果论文不是Nature封面级发现 → 禁止用"groundbreaking""landmark""pivotal""paradigm-shifting"
```

#### 8h-2. AI高频词汇 — 禁止

```
⛔ AI最爱动词/名词 (来自blader/humanizer pattern #7):
  "delves into" / "delve into"        → "examines" / "analyzes" / 删除
  "tapestry"                          → 删除(学术论文不用织物比喻)
  "landscape" (非地理意义)            → "field" / "context" / "literature"
  "showcasing" / "showcase"           → "demonstrating" / "showing" / "presenting"
  "underscoring" / "underscores"      → "emphasizing" / "highlighting that"
  "highlighting" (分词分析, pattern #3)→ 改写为主动词: "we find" / "the data show"
  "reflecting" (分词分析)              → "indicating" / 删除
  "garnered" (如"garnered attention")  → 删除(已在8a覆盖)
  "burgeoning"                        → "growing" / "increasing"
  "realm" / "in the realm of"         → "in" / "in the context of"

⛔ AI最爱形容词/副词:
  "nuanced"                           → "subtle" / 删除(不添加元评价)
  "crucial" / "critical"              → 仅在"critical temperature"等固定术语中使用
  "profound"                          → "substantial" / "large" / 具体数字
  "paramount"                         → "central" / "key"
```

#### 8h-3. 系词逃避 (Copula Avoidance) — 禁止

```
AI异常厌恶简单系词"is/are",倾向用更"高级"的替代。这是强检测信号。

⛔ "serves as"   → "is"
⛔ "boasts"      → "has"
⛔ "standing as" → "is"
⛔ "represents" (无表征意义时) → "is"
⛔ "constitutes" → "is" / "forms"

例外: "represents"在数学/物理中有精确含义("矩阵表示")时保留。
```

#### 8h-4. 否定对仗 + 三件套 — 禁止

```
⛔ 否定对仗 (blader pattern #9):
  "Not only X, but also Y"           → "X and Y"
  "Not X; rather, it is Y"           → 已在8c覆盖

⛔ 三件套 (blader pattern #10):
  "X, Y, and Z" 作为三段式列举,且三项结构完全平行 → 改写为不对称
  例: "efficacy, safety, and tolerability" → "efficacy and safety; tolerability data are also reported"
```

#### 8h-5. 模糊归因 — 禁止

```
⛔ "Experts believe..." / "Many researchers argue..." / "It is widely accepted that..."
⛔ "Studies have shown..." (不加引用) / "Observers have cited..."
⛔ "The literature suggests..." (不加具体引用)

替代: 具体引用。 "Ref. [X] showed Y." 不引用就不说。
```

#### 8h-6. 虚假范围 (False Ranges) — 禁止

```
⛔ 非标量极端值之间的"from X to Y":
  "from the Big Bang to dark matter"
  "from quantum mechanics to cosmology"
  "from renal function to cardiac outcomes"

替代: 直接列出。 "in quantum mechanics, general relativity, and cosmology"
```

### 8i. 风格层面规则 — 整合blader/humanizer

#### 8i-1. 破折号零容忍

```
⛔ Em dash (—) / En dash (–) → 零容忍。全文0个。
   AI文本的em dash使用频率显著高于人类学术写作 (blader pattern #14)。
替代: 句号、逗号、冒号、括号。
   "The result—which was unexpected—changed..." → "The result, which was unexpected, changed..."
```

#### 8i-2. 填充短语 — 禁止

```
⛔ "In order to"       → "To"
⛔ "Due to the fact that" → "Because"
⛔ "In the event that"    → "If"
⛔ "With regard to"       → "About" / "Regarding"
⛔ "It is important to note that" → 删除,直接陈述
⛔ "It should be pointed out that" → 删除
```

#### 8i-3. 通用结论 — 禁止

```
⛔ "The future looks bright"
⛔ "These results open new avenues for research"
⛔ "Further studies are needed to fully understand..."
⛔ "This work paves the way for..."

替代: 具体陈述下一个问题是什么,或直接停。
```

#### 8i-4. 同义词轮换 — 禁止

```
AI为"词汇多样性"会轮换同义词,但人类在学术写作中倾向术语一致。

⛔ 同一概念换3+个词:
  "Patients... Participants... Subjects... Individuals..."
  "Method... Approach... Technique... Framework..."

替代: 锁定术语分类账中的规范形式,始终用同一个词。
  (与P1_build.md §4术语分类账一致)
```

### 8j. 学术写作特化规则 — 整合matsuikentaro1/humanizer_academic

> 以下26个模式来自医学/科学论文编辑实际经验,针对学术文本的AI标志词。

#### 8j-1. LLM标志词替换

```
⛔ "linked to" (因果)     → "associated with" (LLM倾向于用linked)
⛔ "Beyond [X]" (段首)    → "In addition to [X]"
⛔ "via"                  → "through" (学术文本中via是AI标志)
⛔ "where" 作为非地点连接词 → 改写:
    "...level, where almost daily use..." → "...level, with almost daily use..."
⛔ "yield" 作为结果动词    → "produced" / "gave" / "resulted in"
    "did not yield stable estimates" → "failed to produce stable estimates"
⛔ 过度缩写表达式           → 展开:
    "fatigue–sleepiness cycle" → "cycle of fatigue and sleepiness"
```

#### 8j-2. AI不足/过度hedging — 学术文本双重陷阱

```
AI学术文本的hedging呈现两端极化:

陷阱A — 不足hedging (AI过于自信):
  ⛔ "may reduce the risk of" → "may help reduce the risk of"
  ⛔ 当引用不足以支撑因果声称时,却用了因果动词 → 降级为关联动词

陷阱B — 过度hedging (AI过于防御):
  ⛔ "may suggest... have the potential to confer..."
  → 保留1-2个hedge词,删除冗余层 (已在8b/8e覆盖)
```

#### 8j-3. 被AI遗忘的经典学术词汇

```
AI系统性回避某些经典学术词汇,偏好"现代"替代。适当使用经典词汇增加人类感:

✅ "proportion"     ← AI偏好 "percentage"
✅ "aim"            ← AI偏好 "goal" / "objective"
✅ "was assessed"   ← AI偏好 "was evaluated" / "was analyzed"
✅ "purpose"        ← AI偏好 "goal" / "aim" / "objective"
✅ "measured"       ← AI偏好 "assessed" / "evaluated" / "quantified"
```

---

### 8k. 学術去AI化终检清单 (Phase 4f扩充)

在原有Phase清单 Phase 4f终检基础上,增加以下grep:

```
[ ] 意义膨胀词: grep "pivotal\|groundbreaking\|landmark\|paradigm-shifting\|intricate\|meticulous"
[ ] AI高频词汇: grep "delve\|tapestry\|landscape\|showcasing\|underscoring\|burgeoning\|realm"
[ ] 系词逃避:   grep "serves as\|boasts\|standing as\|constitutes"
[ ] 模糊归因:   grep "Experts believe\|Many researchers\|widely accepted\|Studies have shown"
[ ] 虚假范围:   grep "from the.*to the.*" (检查非标量配对)
[ ] 破折号:     grep "—\|–" → 必须0匹配
[ ] 填充短语:   grep "In order to\|Due to the fact that\|With regard to\|It is important to note"
[ ] LLM标志词:  grep "linked to\|Beyond\|via\|yield"
[ ] 否定对仗:   grep "Not only.*but also"
[ ] 通用结论:   grep "paves the way\|open new avenues\|future studies are needed"
[ ] 三件套:     检查三项对称列举 (非grep,需阅读扫描)

命中任何 → 重写该段或该句
```

---

### 8l. ⛔ Voice PRESENCE要求 — 正向人类特征注入

> 这是§8最重要的变化。8a-8k是"不做什么"(底线),本节是"必须做什么"(要求)。
> 如果Voice特征缺失,即使通过全部禁止清单,论文仍然会读出AI味。
> 
> 原理: AI检测器在"没有AI特征但没有人类特征"的gray zone文本上,
>   倾向于判AI(保守策略)。你必须给检测器一个"这是人类写的"的积极信号。

#### 8l-1. 每段Voice特征要求

```
每段生成/重写后,必须满足以下至少2项:

[ ] 包含审美判断:
    "This is ugly but it works."
    "I find this decomposition cleaner than the standard approach."
    "The proof of Proposition 4 is the prettiest part of this paper."
    不在Voice Card标注位置的段落可以用技术判断替代审美判断:
    "This convergence rate is suboptimal but sufficient for our purpose."

[ ] 包含具体经验/操作细节 (只有真正做过的人才知道):
    "At N_Sh > 20 the kernel becomes numerically singular in double precision."
    "We had to switch to quad precision for those points."
    "The fit converged only after we removed the n=3 outlier."

[ ] 包含对话句 (对读者说话,帮助理解,非防御):
    "The reader might wonder why we don't simply use X. The reason is..."
    "At this point one could object that... Let me address this directly."

[ ] 包含意外 (AI不会预测到的下一句):
    2词段落: "It doesn't."
    反直觉陈述: "Adding more data made the fit worse."
    诚实承认: "We don't have a good explanation for this."

[ ] 包含不均匀深度:
    极短段: ≤2句
    极长段: ≥8句 (在"最在意"的点上)

⛔ Phase 4逐段重写时,每段写完后检查上述要求。
  如果某段0项满足 → 该段必须重新注入至少1项Voice特征。
  如果连续3段都是"客观陈述"无任何Voice特征 → ⛔ 阻断,重新分配Voice特征。
```

#### 8l-2. Voice特征密度要求

```
全文级别:
  [ ] 审美判断句: ≥ section数 (每个section至少1句)
  [ ] 具体经验/操作细节: ≥ 2处
  [ ] 对话句: ≥ 1处
  [ ] 意外句: ≥ 2处 (极短段算1处意外)
  [ ] 极短段(≤2句): ≥ 2段
  [ ] 极长段(≥8句): ≥ 1段

⛔ 终检时检查(Phase 4f): 如果任一项为0 → 必须注入
  这不是"nice to have"。这是PASS/FAIL标准。
```

#### 8l-3. Voice vs AI禁止 优先级

```
当Voice要求与AI禁止清单冲突时:

  Voice > AI禁止 (原则上)
  例: Voice Card要求第一人称 "I find this surprising" → 即使8a禁止某些第一人称句式,保留
  例: Voice Card要求极短段 "This fails." → 即使8i-2建议禁止短句,保留

  例外: Voice < 防御性语言禁止 (P2_review.md §7)
  例: "We tried to derive it. We couldn't." → 即使可能被误认为Voice,仍需改写
      改写为: "A derivation from first principles remains open."
      (保持坦诚,去掉自我贬低)

  Voice < 技术正确性
  例: 如果Voice Card要求"X holds"但审稿人证明X在条件C下才成立
      → 修改为 "Under C, X holds." (保持断言句式+添加条件)
      不接受降级为 "X may hold under C."
```

#### 8l-4. Phase 4f Voice PRESENCE终检 (与Phase清单同步)

```
[ ] 读取 paper_output/author_voice_card.md → 逐项对比终稿
[ ] 信念梯度 PRESENCE: Level A声称是否仍是断言句式?
[ ] 审美判断 PRESENCE: 每个section是否有≥1句?
[ ] 人格化特征 PRESENCE: Voice Card标注的特征是否在指定位置?
[ ] 注意力分配 PRESENCE: 极短段≥2? 极长段≥1?
[ ] 禁止项 ABSENCE: "这个人不会说"的短语是否未出现?

⛔ 任一项不满足 → ⛔ 阻断,必须修复后再输出终稿
```
