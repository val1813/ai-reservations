# LP14-S2 Phase 1: B博士独立判断 — U=1.2eV对RuO₂是否物理？

**框架**: 强关联电子理论 + cRPA/第一性原理U值比较  
**方法论角色**: B博士（跨域攻击者），独立于A博士的DFT+U方法论批判  
**目标声张**: "Qian et al. (PRB 2025)脆弱磁性理论需U≥1.2eV→对4d金属RuO₂非物理"

---

## 1. 独立数据检索：4d Ru化合物的Hubbard U全景

### 1.1 系统综述：Ru基4d化合物的有效库仑相互作用

以下表格汇总了经过同行评议的4d Ru化合物Hubbard U值，数据来源涵盖DMFT、cRPA和DFT+U方法。此表是本报告的核心证据基础。

| 材料 | 结构 | 电子性格 | 方法 | U (eV) | J (eV) | U_eff (eV) | 参考文献 |
|------|------|----------|------|--------|--------|------------|----------|
| **Sr₂RuO₄** | 层状钙钛矿 | 关联Fermi液体(Tc=1.5K) | DMFT+cRPA | **2.3-2.4** | 0.3-0.4 | ~2.0 | Standard DMFT(TRIQS/TPRF); Mravlje et al. 2011 |
| **SrRuO₃** | 正交钙钛矿 | Hund's金属(铁磁,Tc~160K) | DMFT | **2.0-2.5** | 0.4-0.5 | ~1.6-2.0 | Dang et al. 2015 (ar5iv:1501.03964) |
| **CaRuO₃** | 倾斜钙钛矿(∠Ru-O-Ru~150°) | Hund's金属(顺磁) | DMFT | **2.0-2.5** | 0.4-0.5 | ~1.6-2.0 | Dang et al. 2015 |
| **α-RuCl₃** | 蜂巢状 | Mott绝缘体(Kitaev QSL) | DFT+U | **1.5-2.5** | — | 1.5-2.5 | Koval et al. 2024 (PCCP) |
| **RuO₂** | 金红石 | 良金属(ρ~μΩ·cm) | DFT+U(Qian) | **1.2**(U*) | ?(未指定) | 1.2? | Qian et al. 2025 (PRB 111,174425) |
| **RuO₂** | 金红石 | 良金属 | DFT+U(Smolyanyuk) | — | — | **~1.06**(临界值) | Smolyanyuk et al. 2024 (PRB 109,134424) |
| **RuO₂** | 金红石 | 良金属 | DFT+U(典型文献值) | **2.0** | ? | ~2.0 | 多篇文献(Nat.Commun. Fig.3等, U=2eV用于SOC计算) |

### 1.2 关键发现：4d Ru化合物的U值范围

从上述数据可以得出以下结论：

1. **4d Ru化合物的Hubbard U值范围是1.0-2.5 eV，而不是0.5-1.0 eV。** A博士声称的"4d金属U典型值0.5-1.0eV"与文献证据不符。

2. **SrRuO₃和CaRuO₃是4d Ru氧化物金属，DMFT优化U=2.0-2.5 eV**。这两个材料是典型的"关联金属"(Hund's金属)，低能物理由Hund耦合主导而非Mott物理。如果它们能接受U~2.0-2.5eV，那么RuO₂在U=1.2eV处是完全合理的。

3. **Sr₂RuO₄是更极端的例子**：这是4d Ru氧化物的"金标准"DMFT系统，其cRPA计算和DMFT拟合一致给出U=2.3-2.4eV，J=0.3-0.4eV。这个材料是超导体，具有清晰的Fermi液体行为，但有效U却是RuO₂的两倍。

4. **α-RuCl₃是Mott绝缘体，其DFT+U优化范围1.5-2.5eV。** Smolyanyuk et al.恰恰使用α-RuCl₃的U值(1-2eV)作为对比来论证RuO₂的U应该更小。但他们忽略了：SrRuO₃和Sr₂RuO₄同为4d Ru金属，同样具有强金属屏蔽，其DMFT U值却是α-RuCl₃的2倍。

### 1.3 带宽度(W)的考量

| 材料 | U (eV) | 4d带宽W (eV) | U/W |
|------|--------|--------------|-----|
| RuO₂ | **1.2** | ~6-8(全4d带) | **~0.15-0.20** |
| SrRuO₃ | 2.0-2.5 | ~2.5(窄带) | 0.8-1.0 |
| CaRuO₃ | 2.0-2.5 | ~2.0(更窄,因GdFeO₃畸变) | 1.0-1.25 |
| Sr₂RuO₄ | 2.3-2.4 | ~2.0(t₂g带) | ~1.2 |
| α-RuCl₃ | 1.5-2.5 | ~1-2(窄带,Mott绝缘体) | ~1.0-2.5 |

**关键洞察**：RuO₂的金红石结构具有宽得多的4d带(~6-8eV vs 钙钛矿的~2.5eV)。因此，U=1.2eV对RuO₂来说对应U/W≈0.15-0.20——这是**弱关联极限**，完全适合一个"良金属"的描述。相比之下，SrRuO₃的U/W≈0.8-1.0处于中等关联区间。

这意味着：即使U值相同，RuO₂的电子关联性也比SrRuO₃弱得多。**U=1.2eV对RuO₂而言不是"太大"，而是"正好较小"**——恰好与其宽带的良金属特性一致。

---

## 2. U=1.2eV对RuO₂是否物理：独立判断

### 2.1 判断结论

**U=1.2eV对RuO₂是物理的。** 理由如下：

1. **其他4d Ru金属氧化物的U值普遍更高**：SrRuO₃(2.0-2.5eV)、Sr₂RuO₄(2.3-2.4eV)的DMFT优化U值均显著高于1.2eV。这些材料同样是4d Ru金属，具有相似的金属屏蔽环境。如果U=2.0-2.5eV对SrRuO₃是物理的，那么U=1.2eV对RuO₂更是物理的。

2. **U/W比分析**：RuO₂的4d带宽W≈6-8eV(U=0时d-band中心在-2.55eV, 带宽覆盖-5eV到EF以上), 因此U/W≈0.15-0.20。这对应弱关联极限。而SrRuO₃的U/W≈0.8-1.0对应中等关联。**U=1.2eV对RuO₂描述的不是"强关联"，而是"弱关联良金属"。**

3. **A博士声称的"4d金属典型U值0.5-1.0eV"无文献支撑。** 经检索，没有发现任何经过同行评议的cRPA或线性响应计算给出RuO₂的U值低于0.5-1.0eV范围。Tesch & Kowalski (PRB 105, 195153, 2022)对元素Ru金属的cLDA计算显示U值随4d带填充增加而增大，Ru(4d⁷)处于中段。更重要的是，Ru在氧化物中的U值总是高于元素金属中的U值(因为氧配位减少了d电子屏蔽)。

4. **Smolyanyuk et al. (PRB 2024)的"U_eff>1eV非物理"论证依赖于有问题的比较**：他们将RuO₂与α-RuCl₃(Mott绝缘体, U_eff~1-2eV)比较，认为RuO₂作为金属应该有更小的U。但同样逻辑应适用于SrRuO₃和Sr₂RuO₄，然而后两者的DMFT U值远高于1eV且被广泛接受。这表明"金属屏蔽必然将U降到极低值"的前提是错误的。

### 2.2 Smolyanyuk vs Qian 临界U值对比

| 参数 | Smolyanyuk et al. (2024) | Qian et al. (2025) | 差异 |
|------|--------------------------|---------------------|------|
| 临界U_eff | ~1.06 eV | ~1.2 eV (U, 未明确是否为U_eff) | ~0.14 eV |
| 方法 | DFT+U (GGA+U) | DFT+U (GGA+U) | 相同 |
| k-point | 12×12×12 | 讨论12³ vs 20³的差异 | 近似 |
| 关键结论 | U_eff>1.06eV非物理 | U接近1.2eV→LP不稳定性 | 相近数值但解读相反 |

**关键观察**：Smolyanyuk和Qian的临界U值仅差0.14eV(约10%)。这个差异可能来自：
- 不同的赝势/PAW设置
- 不同的k点网格(12³ vs 20³)
- 不同的U/J约定(U vs U_eff)
- 不同的收敛标准

如果考虑J=0.4eV(与SrRuO₃ DMFT一致)，则Qian的U=1.2eV对应U_eff=0.8eV——**低于Smolyanyuk的临界值**。这意味着：
- 在U_eff空间，Qian的临界U_eff可能低至0.8eV(若J=0.4eV)
- 这完全在Smolyanyuk认为的"物理"范围内

**结论：Smolyanyuk和Qian的计算结果实际上并不矛盾。** 所谓的"非物理"声张源于U约定不明确和对比较基准的选择性偏差。

---

## 3. A博士论证链评估

### 3.1 论证链结构

```
A博士链:
  P1: U≥1.2eV对4d金属RuO₂非物理
  P2: 若U必须取非物理值才能产生磁性→理论不可信
  P3: 若理论不可信→Qian的"脆弱磁性"解释不成立
  P4: 若脆弱磁性不成立→实验矛盾不可调和
  C: "五探针一致否定"altermagnetism→命题B胜出
```

### 3.2 链条强度评估

**P1 (核心声张): 脆弱性 ⭐(极弱)**

U=1.2eV对RuO₂是物理的。如上所述，4d Ru化合物的U值范围是1.0-2.5eV，RuO₂的宽带宽意味着U/W≈0.15-0.20，属于弱关联极限。P1事实错误。

**P2 (推论): 中等脆弱性 ⭐⭐⭐**

即使U=1.2eV是物理的，DFT+U方法对临界U值的敏感性仍然是一个合理的关切。Qian论文自身报告了k点网格敏感性(12³ vs 20³给出不同的基态)，以及能量差异<0.5meV/atom但磁态截然不同的问题。但这恰恰是Qian论文的核心观点——系统处于LP不稳定性附近，微小扰动即可翻转磁态。这不是方法论缺陷，而是物理结论。

**P3 (推论): 中等偏强 ⭐⭐⭐⭐**

如果Qian的理论不依赖于非物理U值，其核心声张(系统靠近LP不稳定性→磁性脆弱)不仅成立，而且与2024-2025年实验文献高度一致：一部分实验看到磁性，另一部分看不到。这正是"脆弱性"预测的图景。

**P4 (推论): 偏弱 ⭐⭐**

实验矛盾的"可调和性"不依赖于Qian的理论正确与否。即使没有Qian的理论框架，实验矛盾(μSR看不到 vs XMLD看到 vs 输运看到)本身就需要解释。一种可能的替代解释是：磁性是样品依赖的(Ru空位浓度)，这与Smolyanyuk et al.的结论一致。

**C (结论): 中等 ⭐⭐⭐**

"A的五探针一致否定"应受到以下质疑：
- μSR和粉末中子衍射主要探测体材料(bulk)/多畴态
- XMLD(He et al. 2025)、IASSE(Jung et al. 2025)、电操控(Zhang et al. 2025)则探测薄膜/单畴态
- 两种态可能具有根本不同的磁性——这正是"脆弱性"的预测
- "五探针"中有四个是体材料敏感探针(μSR, 中子, NMR, 热容)，仅输运探针(AHE)在薄膜中看到信号

### 3.3 论证链中"最脆弱的一步"

**最脆弱的一步是P1**: U≥1.2eV对RuO₂非物理的声张。

这个声张之所以最脆弱，因为它：
1. **与已知的4d Ru化合物U值范围(1.0-2.5eV)直接矛盾**
2. **忽视了U/W比的物理意义**——RuO₂的宽带宽意味着U=1.2eV实际上是弱关联
3. **依赖于一个有问题的比较基准**(与α-RuCl₃比较，而不是与同为4d Ru金属氧化物的SrRuO₃/Sr₂RuO₄比较)
4. **混淆了U和U_eff**——如果J=0.4eV(标准值)，U=1.2eV→U_eff=0.8eV，这在任何标准下都不是"非物理"的

### 3.4 如果P1被推翻，LP-14结论如何变化

如果P1被推翻(即U=1.2eV是物理的)，则整个论证链崩溃：

1. **Qian的理论拥有物理的输入参数**：U值在4d Ru氧化物的合理范围内
2. **"脆弱磁性"机制复活**：RuO₂确实可能靠近LP不稳定性，其磁性对U、应变、掺杂敏感
3. **实验矛盾的解读逆转**：不是"五探针一致否定altermagnetism"，而是"探针对不同量子态敏感——体材料非磁，薄膜/特殊条件下可调谐交变磁性"
4. **命题B不自动胜出**：交变磁性的存在与否变成一个参数化问题(什么U、什么应变、什么掺杂、什么样品质量下出现)，而非二元的是/否问题
5. **Qian的理论变得具有预测性**：预测了掺杂和应变下磁性的出现阈值，这些阈值可以被实验检验

---

## 4. 苏格拉底追问(≥5个)

### 追问1：关于He et al. (Nat. Commun. 2025) XMLD实验

**问题：** He et al. (Nat. Commun. 2025, 16, 8235)使用Ru M-edge XMLD在RuO₂(101)/Al₂O₃(1-102)薄膜中独立确认了Néel序的存在：角分辨XMLD信号随温度在TN~390K以上消失，XMCD信号为零证明纯补偿AFM序，磁电张量分析将Néel矢量定位于[001]方向~55°倾角。如果这个XMLD实验是独立的、高精度的磁探针，那么A博士声称的"五探针一致否定"是否仍然成立？

**分析：** 
- 不成立。A博士的"五探针"(μSR、中子、NMR、热容、ARPES/AHE)主要在体材料中进行，而XMLD在薄膜中进行。
- 如果薄膜(由于应变、空位、或有限尺寸效应)表现出与体材料不同的磁序，这恰恰是Qian理论预测的"脆弱磁性"——参数敏感性导致磁态在不同样品条件下切换。
- 值得注意的是，He et al.的~55°倾角Néel矢量预测与Qian理论并非完全一致(Qian预测c-axis为易轴)，这为进一步理论-实验比较留下了空间。但Néel序的存在本身与"五探针一致否定"矛盾。
- Keßler et al. (2024) μSR+中子实验报告的磁性上限(1.14×10⁻⁴μB/Ru)和He et al. XMLD观测到的Néel序之间没有直接矛盾——μSR测量的是体材料，由于时间窗口敏感性差异(~10⁻¹¹s)，μSR可能错过缓慢涨落的Néel序。

**结论：** He et al.的XMLD实验直接否定了"五探针一致否定"声张。矛盾不是理论的失败，而是探针对不同样品条件敏感性的自然体现。

### 追问2：关于交变磁性的二元分类

**问题：** 交变磁性是否应该被视为一个二元分类(材料是或不是交变磁体)，还是应该被参数化——即其存在取决于U、应变、掺杂、样品质量、温度、或薄膜厚度？

**分析：**
- 交变磁性不应是二元分类。它是d-wave或g-wave自旋劈裂带结构的一种对称性特征，与磁有序共存。
- 即使RuO₂体材料在某些条件下是非磁性的(如Hiraishi PRL 2024, Keßler npj Spintronics 2024所示)，它仍然可以在以下条件下展现出交变磁性：
  - 特定应变(2%拉伸应变使Qian临界U从1.2降至1.0eV)
  - 特定掺杂(0.4h/uc空穴掺杂使临界U降至0.9eV)
  - 薄膜生长条件(He et al. XMLD薄膜)
  - 特定的Ru空位浓度(Smolyanyuk预计1-5.3%空位即可诱导~0.05μB磁矩)
- 这与Qian论文的核心预测完全一致：系统靠近LP不稳定性，磁性是参数敏感的。
- **类比**：超导性也不是二元分类。纯铜不是超导体，但铜氧化物在特定掺杂和晶格条件下却是高温超导体。将"铜不是超导体"等同于"铜氧化物不是超导体"是逻辑谬误。

**结论：** 交变磁性应该按材料/条件参数化。RuO₂可能在体材料中非磁，但在薄膜/掺杂/应变条件下展现交变磁性。这种参数依赖性本身就是"脆弱磁性"理论的预测。

### 追问3：关于μSR的零信号解读

**问题：** 即使Keßler et al. (npj Spintronics 2024)和Hiraishi et al. (PRL 2024)的μSR实验给出磁矩上限<10⁻⁴μB/Ru，这是否证明了RuO₂完全没有磁性(而非仅仅没有长程磁序)？

**分析：**
- 不完全是。μSR的时间窗口是~10⁻¹¹-10⁻⁵s。自旋涨落快于~10⁻¹¹s时，μSR信号被平均掉。
- 如果RuO₂的Néel序是动态的(Néel矢量在多个易轴间涨落)，或者存在自旋涨落谱的特定分布，μSR可能错过信号。
- Smolyanyuk的理论预测了Ru空位附近形成局域磁矩(~0.05μB)，如果这些磁矩是动态的(在时间平均下为零)，μSR仍可能给出零信号，但XMCD/XMLD可能在不同时间窗口捕捉到信号。
- Keßler et al.使用零场μSR(ZF-μSR)，这对静态磁序敏感，但对慢涨落(<10⁻⁷s)不敏感。如果磁序存在但在μSR时间窗口内涨落，ZF-μSR可能错过。
- **交叉验证需求**：需要更宽时间窗口的μSR测量(如LF-μSR、RF-μSR变温测量)来区分静态序和慢涨落。

**结论：** μSR的零信号不排除动态的、短程的或纳米尺度的磁序。μSR的时间窗口限制使得它对特定类型的磁序不敏感。

### 追问4：关于筛选环境的结构依赖性

**问题：** Smolyanyuk的论证依赖于将RuO₂与α-RuCl₃比较(Mott绝缘体,U_eff~1-2eV)，声称RuO₂作为良金属应该有更小的U。但SrRuO₃同样是一个金属，其DMFT U=2.0-2.5eV。如果金属屏蔽未能将SrRuO₃的U降到<2eV，Smolyanyuk论证中"金属屏蔽必然降低U"的前提是否成立？

**分析：**
- 不成立。RuO₂(带宽~6-8eV)、SrRuO₃(带宽~2.5eV)和Sr₂RuO₄(带宽~2.0eV)虽然都是4d Ru金属，但它们的筛选环境有显著差异。
- 有效库仑屏蔽U = U_bare - U_screening，其中U_screening取决于：
  - 极化率(π极化谱)：与未占据态能量和d-p杂化强度相关
  - 带宽：宽带的材料具有更高的动能，从而增强筛选
  - 晶体场分裂：影响d-轨道分裂和屏蔽通道
- RuO₂的金红石结构具有直通Ru-O-Ru键(180°)，增强了d-p杂化。这意味着更多的高能O-2p→Ru-4d跃迁可用于屏蔽Ru 4d上的库仑相互作用，从而比钙钛矿结构(∠Ru-O-Ru~163°-150°)更有效地降低U。
- **然而**：即使RuO₂的筛选更强，没有证据表明它能将U从2-3eV降至<0.5-1.0eV。SrRuO₃的带宽更窄，但Sr₂RuO₄的带宽也相对窄，且Sr₂RuO₄的cRPA U=2.3eV。RuO₂确实应该有更小的U，但U=1.2eV在合理范围内。

**结论：** 金属筛选会降低U，但不会将U降到零。U=1.2eV处于宽带金红石氧化物U值的合理上边缘，并非非物理。

### 追问5：关于脆弱性是否等同于不可证伪

**问题：** A博士论证的逻辑链条是"U非物理→理论脆弱→不可证伪→命题B胜出"。如果U=1.2eV是物理的，但Qian的理论仍然显示了k点敏感性(12³vs20³给出不同磁态)，这种数值敏感性是否使理论不可证伪？

**分析：**
- 不。数值敏感性是物理的一部分，而非方法论的失败。以下是可证伪的预测：
  - **预测1**：RuO₂体材料在无应变、无掺杂条件下应在基态非磁(或仅有极弱磁矩<0.001μB/Ru)——这与Keßler/Hiraishi μSR一致，已部分验证。
  - **预测2**：2%拉伸应变或0.4h/uc空穴掺杂应在足够好的k点收敛条件下诱导出可测量的AFM序(磁性可调)——可通过应变下的μSR/中子衍射检验。
  - **预测3**：Ru空位浓度>1%应诱导局域磁矩——可通过Ru空位含量不同的样品间比较检验。
  - **预测4**：磁转变温度(TN)应在应变/掺杂下连续可调——可通过应变薄膜的变温XMLD检验。
- 数值敏感性(12³vs20³)不意味着任意性。20³网格是更收敛的结果，它预测了特定应变阈值下的磁转变。这是一个明确的可检验预测。
- **真正的不可证伪理论**是那些"适用于一切数据"的理论(如"外星人干的")。Qian的理论则不同：它明确预测了磁性出现的参数窗口，这些窗口可以被实验测量反驳或验证。

**结论：** 数值敏感性不是不可证伪性。Qian的理论做出了一系列明确的、可检验的预测，这些预测部分(μSR零信号)甚至已被验证。

### 追问6：关于Tian Qian et al. (arXiv:2504.21138)的否定证据

**问题：** 一个不同的研究组(Tiema Qian et al., arXiv:2504.21138, 2025)基于力矩磁力计和量子振荡测量，报告RuO₂高纯单晶是巡游顺磁体，无长程磁序。这是否独立于A博士的"五探针"之外，构成了第六个否定证据？

**分析：**
- 这确实是重要的额外数据点，但它与Zhuang Qian的理论一致而非矛盾。
- 力矩磁力计(扭矩磁力测定)在单晶上进行——这些单晶通常缺乏薄膜中存在的应变和缺陷。
- 量子振荡测量对体材料Fermi面拓扑敏感——如果磁序仅在表面或薄膜中存在，体材料量子振荡自然看不到。
- 关键区别：Tiema Qian et al.测量的是"高纯单晶"，而实验中看到磁序的通常是薄膜或含有空位的样品。
- 这与Zhuang Qian的"参数窗口"预测高度一致：在无应变、无掺杂、高纯单晶中，系统确实处于非磁侧。
- 此论文的标题"Determining the Nature of Magnetism in Altermagnetic Candidate RuO₂"本身暗示了它仍然将RuO₂视为一个"候选者(altermagnetic candidate)"，而非已彻底否定的系统。

**结论：** Tiema Qian的力矩测量提供了另一个"体材料非磁"的证据，但这与Zhuang Qian的预测一致，不能作为否定脆弱磁性理论的证据。

### 追问7：关于A博士的"非物理"论证是否犯了范畴错误

**问题：** 在强关联电子理论中，DFT+U中的U不是一个万能的物理常数(如精细结构常数)，而是一个依赖于子空间选择和屏蔽的模型参数。A博士将U=1.2eV定性为"非物理"——这是否犯了将模型参数与可观测物理量混淆的范畴错误？

**分析：**
- 是的，这是范畴错误。
- DFT+U中的U是模型参数，与以下因素手拉手:
  - 使用了什么交换关联泛函(PBE, PBEsol, SCAN等)
  - 选择了什么投影子空间(原子轨道vs Wannier轨道)
  - 采用了什么双计数校正(fully localized limit vs around mean field)
  - 是否包含自旋轨道耦合(SOC)
  - k点网格和能量截断等计算参数
- 同一个物理系统的"正确"U值在不同方法间可以有显著差异：
  - cRPA U与线性响应U最多差30%(Carta et al., arXiv:2505.03698, 2025)
  - cRPA本身系统性地高估屏蔽，低估U(Han et al. 2018, arXiv:1810.06116)
  - Ce f的系统:cRPA给出U~1-3eV但实际使用的U~6eV
- 因此，说"U=1.2eV对4d金属非物理"相当于说"用FLL双计数校正+PBE泛函+原子轨道投影+12³k点+无SOC对RuO₂的Ru 4d投影U=1.2eV非物理"——这是一个特定计算协议下的陈述，不能外推到"所有方法下U=1.2eV对RuO₂都非物理"。

**结论：** A博士将DFT+U模型参数的数值(在特定计算协议下)等同于某种普适的物理常数，犯了范畴错误。在强关联电子理论中，U是协议依赖的模型参数，其"物理性"取决于能否复现实验观测，而非其绝对数值。

---

## 5. 独立结论

> **U=1.2eV对RuO₂是物理的。** 4d Ru化合物(Sr₂RuO₄、SrRuO₃、CaRuO₃、α-RuCl₃)的Hubbard U值范围是1.0-2.5eV，RuO₂的宽带(6-8eV)意味着U=1.2eV对应U/W≈0.15-0.20(弱关联极限)，远低于典型关联电子系统的中等关联区间(U/W≈0.8-1.2)。A博士声称的"4d金属U典型值0.5-1.0eV"无任何经过同行评议的cRPA、线性响应或DMFT文献支撑。

---

## 6. 数据来源完整引用

1. Dang, H. T., Mravlje, J., Georges, A., & Millis, A. J. (2015). "Electronic correlations, magnetism and Hund's rule coupling in the ruthenium perovskites SrRuO₃ and CaRuO₃." *Phys. Rev. B*, 91, 195149. arXiv:1501.03964. [DMFT U=2.0-2.5eV for SrRuO₃/CaRuO₃]

2. Lee, Y. S., et al. (2001). "Optical investigation of the electronic structures of Y₂Ru₂O₇, CaRuO₃, SrRuO₃, and Bi₂Ru₂O₇." *Phys. Rev. B*, 64, 245107. [Optical U_dd~2-3eV]

3. Koval, A. M., et al. (2024). "Periodic DFT calculations to compute the attributes of a quantum material: honeycomb ruthenium trichloride." *Phys. Chem. Chem. Phys.*, 26, 19369. [DFT+U optimum 1.5-2.5eV for α-RuCl₃]

4. Tesch, R. & Kowalski, P. M. (2022). "Hubbard U parameters for transition metals from first principles." *Phys. Rev. B*, 105, 195153. [Systematic cLDA U for all 3d/4d/5d metals, incl. Ru]

5. Qian, Z., Yang, Y., Liu, S., & Wu, C. (2025). "Fragile unconventional magnetism in RuO₂ by proximity to Landau-Pomeranchuk instability." *Phys. Rev. B*, 111, 174425. [U*=1.2eV critical value]

6. Smolyanyuk, A., Mazin, I. I., Garcia-Gassull, L., & Valenti, R. (2024). "Fragility of the magnetic order in the prototypical altermagnet RuO₂." *Phys. Rev. B*, 109, 134424. [U_eff~1.06eV critical; Ru vacancies enable magnetism at moderate U]

7. He, C., et al. (2025). "Evidence for single variant in altermagnetic RuO₂(101) thin films." *Nat. Commun.*, 16, 8235. [XMLD confirms Néel order in RuO₂ films, TN~390K]

8. Zhang, Y., et al. (2025). "Electrical manipulation of spin splitting torque in altermagnetic RuO₂." *Nat. Commun.*, 16, 5646. [Electrical Néel vector switching via XMLD]

9. Jung, H., et al. (2025). "Reversible Spin Splitting Effect in Altermagnetic RuO₂ Thin Films." *Nano Lett.*, 25, 16985. [IASSE polarity reversal with Néel vector control]

10. Keßler, P., et al. (2024). "Absence of magnetic order in RuO₂: insights from μSR spectroscopy and neutron diffraction." *npj Spintronics*, 2, 50. [Non-magnetic in bulk, prior neutron peak = multiple scattering artifact]

11. Hiraishi, M., et al. (2024). "Nonmagnetic Ground State in RuO₂ Revealed by Muon Spin Rotation." *Phys. Rev. Lett.*, 132, 166702. [No AFM order, upper limit ~1% of claimed]

12. Han, Q., et al. (2018). "Investigation into the inadequacy of cRPA in reproducing screening in strongly correlated systems." arXiv:1810.06116. [cRPA systematically overestimates screening and underestimates U]

13. Carta, M. et al. (2025). "Bridging constrained random-phase approximation and linear response theory for computing Hubbard parameters." arXiv:2505.03698. [cRPA vs LRT U differ by up to 30%]

14. Tian, Q., et al. (2025). "Determining the Nature of Magnetism in Altermagnetic Candidate RuO₂." arXiv:2504.21138. [Torque magnetometry + quantum oscillations: bulk RuO₂ single crystals are itinerant paramagnets]

---

## 附录：进一步实验可检验的预测

基于本分析，以下实验可为LP14-S2提供新的约束：

1. **应变RuO₂薄膜的XMLD**：在受控拉伸应变(0-3%)下测量RuO₂薄膜的XMLD信号强度随应变的变化。Qian理论预测TN在~2%应变下上升，磁矩增强。

2. **Ru空位含量系统扫描**：制备不同Ru空位含量(0-10%)的RuO₂薄膜，定量关联空位浓度与XMLD/AHE信号强度。Smolyanyuk理论预测~0.1 hole/Ru即可诱导~0.05μB磁矩。

3. **薄膜厚度依赖性**：Qian的理论中，薄膜的约化维度效应可能改变磁稳定性。测量不同厚度(5-200nm)RuO₂薄膜的XMLD信号可揭示有限尺寸效应。

4. **直接cRPA计算**：目前缺少对RuO₂的直接cRPA计算。一个明确的可执行任务是使用cRPA(如VASP+DFPT或Wannier90+cRPA)直接计算RuO₂的Ru 4d投影频变U(ω)。这将为Qian的理论提供一个独立的、第一性原理的U基准。

5. **交叉时间窗口实验**：设计μSR+XMLD+XMCD联合实验，在相同样品上同时测量不同时间窗口(μSR:~10⁻¹¹s, XMLD:~10⁻¹⁵s)的磁响应，以区分静态序和动态涨落。
