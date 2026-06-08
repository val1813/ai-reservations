# Round 1 文献库 — LP26-S1: μSR vs 比热SFD系统比较

**Date:** 2026-06-03
**Agent:** A博士 (学院派)
**框架:** 标准超导体电动力学（London模型 / d-wave BCS / μSR涡旋态理论 / 比热热力学）

---

## §-1 四组文献搜索

### 组1: 核心声张查重 — μSR vs 比热SFD是否已有系统比较？

**结论: 没有发现任何已发表的μSR-λ⁻² vs Cp-λ⁻² 跨家族系统定量比较。这是真实的先发空白 (first-mover gap)。**

证据如下:

1. **Tallon et al. PRL 136, 076002 (2026)** [arXiv:2512.01395] — 这是目前唯一正面挑战μSR范式的工作，但它的比较是定性的:
   - Fig.2(a)将Cp导出的λ₀⁻²与μSR数据叠在同一Uemura图上
   - 仅对(Y,Ca)123和Tl2201做了直接对比，Bi2212无μSR数据可对比
   - La214的Cp-SFD与Uemura μSR数据一致，但与Božović薄膜μSR/互感数据矛盾
   - 未做统计显著性检验，未报告χ²或p值

2. **Tallon/Bernhard/Niedermayer (1997) Supercond. Sci. Technol. 10, A38** — 79篇参考文献的μSR综述，覆盖YBCO/Tl2201/LSCO/Bi2212的σ(T)数据编译，但完全没有与比热SFD做定量比较。

3. **Bernhard/Tallon et al. PRL 86, 1614 (2001)** — 发现n_s在p≈0.19处有异常峰，报道了μSR凝聚密度与比热凝聚能U₀的scaling关系，但这是n_s vs U₀，不是n_s(μSR) vs n_s(Cp)的逐点比较。

4. **Gauzzi et al. PRB 94, 180509 (2016)** — 这是唯一在同一批样品(Cu₀.₇₅Mo₀.₂₅Sr₂YCu₂O₇.₅₄, p≈0.46)上同时做μSR和比热的论文。但它是单个掺杂点的案例研究，未做跨家族的掺杂扫描。

5. **Uemura (2004) JPCM 16, S4515** — 综合性μSR综述，讨论了能标框架但未涉及与比热SFD的系统对比。

**先发空白确认:** 无人对以下核心问题给出定量回答:
- μSR-λ⁻²和Cp-λ⁻²的偏离是否统计显著？
- 偏离方向是否一致（所有家族都是μSR低/Cp高？还是家族依赖的？）
- 系统误差预算是否允许两种探针在同一London模型框架内调和？

---

### 组2: 框架盲区搜索 — 普通物理语言翻译

**翻译:** "用不同方法数超导电子数目，得到的结果对不上——磁探针(μSR)说多了掺杂反而少了超导电子，热力学探针(比热)说没少反而多了"

**搜索结果:**

1. **Dordevic & Homes, PRB 105, 214514 (2022)** — "Superfluid density in overdoped cuprates: Thin films versus bulk samples"
   - 从光谱学角度切入，发现薄膜SFD↓而体材料SFD饱和
   - **关键盲区识别:** 维度效应(2D薄膜 vs 3D体材料)可能是此前争论未充分考虑的变量
   - 在pnictides中也发现了类似的薄膜/体材料差异
   - 这与Tallon的发现部分一致（体材料Cp-SFD不下降），但提供了一个维度解释框架

2. **Mahmood/Božović/Armitage, PRL 122, 027003 (2019)** — "Locating the Missing Superconducting Electrons"
   - 用THz时域光谱+互感测量LSCO薄膜
   - 发现在T→0时有大量未凝聚载流子（Drude峰）
   - SFD线性依赖T，与杂质散射d-wave BCS不一致
   - 提出了量子相位涨落的可能性

3. **物理盲区识别:**
   - μSR测的是涡旋态磁场分布→λ(T,H)，涉及涡旋芯物理
   - 比热测的是热力学态密度→γ(T,H)，通过London模型间接给λ
   - 两种探针对不同的涨落模式敏感: μSR对相位涨落敏感，比热对振幅涨落敏感——如果d-wave节点准粒子贡献有所不同，可能系统性偏离
   - **多晶平均效应:** Tallon的比热数据来自多晶，μSR数据一部分来自单晶/薄膜/多晶——晶粒平均效应未校正
   - **Hao-Clem参数化局限:** 仅对0.02 < H/Hc₂ < 0.3有效，最过掺杂Tl2201样本已到极限

4. **Pickett (2026) arXiv:2601.10578** — 区分了三种不同的"超流密度"概念:
   - London n_s (唯象)
   - 归一化ρ_s ≡ λ²(0)/λ²(T) (探针gap结构)
   - 凝聚密度N_s(T=0) (真实超导电子数)
   - 不同技术可能测的是不同物理量

---

### 组3: 反例/否定性搜索 — 已有文献否定Tallon结论

**结论: 未发现正式发表的"Comment on Tallon PRL 136, 076002"。论文2026年2月发表，至今仅4个月，正式PRL Comments通常需要6-12个月。**

但已发现以下间接反例/潜在矛盾:

1. **Čulo et al., SciPost Phys. 11, 012 (2021) + Nature 595, 661 (2021)** — 两通道模型:
   - 提出Tl2201和LSCO中存在非相干配对通道+相干非配对通道
   - 超流密度来自非相干(奇异金属)载流子
   - 如果Tallon说Cp-SFD对所有载流子都凝聚，这与Čulo的反事实逻辑("n_s增长恰好被相干通道载流子损失补偿")矛盾
   - **关键矛盾:** Tallon的Fig.3(b)显示n_s(0)向(1+p)靠拢，而Čulo的数据需要n_s(0)远小于(1+p)才能成立

2. **Gauzzi et al., PRB 94, 180509 (2016)** — 同时做μSR和比热:
   - 在p≈0.46处: μSR σ(0)≈3.0 μs⁻¹(≈最佳YBCO)，但比热γ_res≈10 mJ K⁻² mol⁻¹(≈正常金属)
   - 暗示两种探针在强过掺杂区给出截然不同的物理图像
   - 如果比热说"所有载流子配对"，为什么γ_res如此之大？

3. **Mahmood/Božović/Armitage, PRL 122, 027003 (2019)** — 直接反例:
   - LSCO薄膜中THz光谱+互感SFD下降→0
   - 有未凝聚Drude峰
   - 与d-wave BCS不一致
   - Tallon的回应(在PRL中): "可能由于薄膜中的Josephson耦合加上gap振幅下降"
   - 但这只是推测，未被独立验证

4. **PRB 106, 184510 (2022)** — "Effect of realistic out-of-plane dopant potentials":
   - 用ab initio计算论证杂质势可以半定量解释过掺杂SFD行为
   - 如果"脏d-wave"可以解释，则Tallon说"不需要新物理"在方向上一致，但具体机制不同

5. **Tl2201作为"例外"的自我矛盾:**
   - Tallon承认Tl2201的Cp-SFD确实下降(与μSR一致)
   - 将Tl2201标记为"唯一例外"回避了一个问题: 为什么最干净的cuprate反而是例外？
   - 如果Tl2201代表本征行为，其他cuprate的"不下降"可能是杂质/无序/晶粒效应

6. **Tallon自我反驳的历史:**
   - Tallon & Loram (1994) J. Superconductivity 7, 151: "μSR and heat capacity studies show pair density falls away to zero on either side of optimum doping"
   - Tallon et al. (2026) PRL: "heat capacity shows no apparent loss of superfluid density"
   - 这代表同一个研究组30年后的180度转向

---

### 组4: 数据可用性评估 — S1所需实验数据是否存在？

**总体评估: 部分可用，但关键缺口显著。**

#### 可用的μSR-SFD数据:
| 系统 | 掺杂范围 | 数据源 | 形式 |
|------|---------|--------|------|
| (Y,Ca)123 | under→over | Bernhard/Tallon PRL 86, 1614 (2001); 多个后续μSR | σ(T→0) vs p 图 |
| Tl2201 | under→over | Niedermayer/Uemura 系列; Tallon/Bernhard SST 1997 | σ(T→0) vs p 图 |
| LSCO | under→over (bulk) | Uemura et al. 系列 | σ(T→0) vs p 图 |
| LSCO | over (film) | Božović 系列 (互感) | λ⁻² vs p 图 |
| Bi2212 | over | 有μSR数据但量少; Tallon PRL Fig.2 未标μSR数据点 | 稀疏 |
| Hg1201 | over | Puzniak et al. PRB 53, 86 (1996) | λ_ab, λ_c 值 |

#### 可用的比热-SFD数据:
| 系统 | 掺杂范围 | 数据源 | 形式 |
|------|---------|--------|------|
| (Y,Ca)123 | under→over (7点) | Tallon PRL 2026 Fig.3(b); Loram/Luo 系列 1994-2001 | n_s(0) vs p 图 (有误差棒) |
| Bi2212 | over | Loram et al. 2001 原始Δγ(H,T); Tallon PRL 2026 重新分析 | λ⁻² vs p 图 |
| La214 | over (bulk, 同批μSR样品) | Panagopoulos μSR + 零场比热; Tallon PRL 2026 | λ⁻² vs p 图 |
| Tl2201 | over (4点) | Tallon PRL 2026 Fig.6 | λ⁻² vs p 图 (有原始数据) |

#### 关键缺口:
1. **Bi2212 μSR数据几乎缺失** — Tallon自己也未在Fig.2中标注Bi2212 μSR数据点
2. **La214的Cp-SFD不是直接从场依赖比热得到的** — Tallon PRL承认"没有直接场依赖比热数据"，而是用了μSR互感数据+零场比热组合，= 不是独立的比热-SFD测定
3. **无数字化表格** — 所有数据仅以图中点的形式存在，无量化的p对应值、误差棒
4. **同一样品批次的μSR+比热数据仅存在于:**
   - (a) Gauzzi et al. (2016) Mo-cuprate 单点
   - (b) La214 — Tallon称用了与Panagopoulos μSR"同一批样品"，但比热是零场的
   - 不存在任何cuprate家族的完整p扫描中同时做μSR和比热的数据
5. **Tallon PRB Part II (PRB 113, 064508) 是否提供误差棒？**
   - 根据arXiv版本分析: 误差在文中以文字给出(如m*/m_e = 4.93 ± 0.19, γ_n = 7.30 ± 0.29)
   - 但Fig.2(a)和Fig.3(b)中λ₀⁻²的逐点误差棒需要从PRB正文中提取
   - 最过掺杂Tl2201的Hao-Clem拟合"已达到参数化极限"——暗示误差可能被低估
   - **需要直接获取PRB全文才能确认**；目前从arXiv v1推断，有部分误差棒但可能不完整

#### 数据可用性评分卡:
| 需求项 | 可用性 | 评分 |
|--------|--------|------|
| μSR-λ⁻²(p) 数据点 | 图中分散存在 | B |
| Cp-λ⁻²(p) 数据点 | Tallon PRL图中存在 | B |
| 逐点误差棒(μSR) | 部分文献有 | C |
| 逐点误差棒(Cp) | Tallon PRL有部分，需PRB确证 | C+ |
| 同一批样品μSR+Cp | 仅Gauzzi 1点 + La214争议 | D |
| 数字化数据表 | 不存在 | F |
| 统计检验 | 无人做过 | F |

---

## 文献对比汇总

### 五种技术测SFD的过掺杂行为:

| 技术 | Y123 | Bi2212 | LSCO | Tl2201 | 探测的物理量 |
|------|------|--------|------|--------|------------|
| μSR | ↓ (Bernhard) | 数据缺失 | bulk: ↔ (Uemura), film: ↓ (Božović) | ↓ (Niedermayer) | 涡旋态场分布→λ |
| 比热 (London) | ↗向(1+p) (Tallon) | ↔/↗ (Tallon) | ↗ (Tallon, 但非独立) | ↓ (Tallon) | ΔF(H)→λ |
| 红外/THz光谱 | — | — | ↓ (Armitage) | — | Drude权重→未凝聚载流子 |
| 微波 | — | — | — | ↓ (Broun) | 表面阻抗→λ |
| 互感 | — | — | ↓ (Božović) | — | 两线圈→λ |

**符号说明:** ↓ = SFD随p↑下降, ↗ = SFD随p↑上升, ↔ = 基本不变

### 核心张力矩阵:

1. **(Y,Ca)123:** μSR↓ vs Cp↗ — **最尖锐矛盾**
2. **LSCO:** 薄膜互感↓ vs bulk μSR↔ vs Cp(间接)↗ — 维度效应混淆
3. **Tl2201:** 全技术一致↓ — 无矛盾
4. **Bi2212:** Cp↔/↗ 但μSR数据缺失 — 无法比较

---

## 关键参考文献目录

### 核心争议论文 (2026):
- J.L. Tallon et al., PRL **136**, 076002 (2026) — Part I: 核心声张
- J.L. Tallon et al., PRB **113**, 064508 (2026) — Part II: 扩展数据
- R. Caruso et al., PRL **136**, 076003 (2026) — 无序→Tc↑

### μSR-SFD 关键文献:
- C. Bernhard, J.L. Tallon et al., PRL **86**, 1614 (2001) — 凝聚密度异常峰
- C. Bernhard, Ch. Niedermayer, J.L. Tallon et al., PRB **52**, 10488 (1995) — μSR方法基础
- J.L. Tallon, C. Bernhard, Ch. Niedermayer, SST **10**, A38 (1997) — μSR综述
- Y.J. Uemura, JPCM **16**, S4515 (2004) — 能标框架综述
- A. Gauzzi et al., PRB **94**, 180509 (2016) — 唯一同一样品μSR+Cp

### 比热-SFD 关键文献:
- J.W. Loram, K.A. Mirza, J.R. Cooper, J.L. Tallon, JPCM **6**, 5049 (1994) — 原始电子比热方法
- J.L. Luo, J.W. Loram, J.R. Cooper, J.L. Tallon, cond-mat/0112065 — Y0.8Ca0.2BCO场依赖比热

### 竞争视角:
- M. Čulo et al., SciPost Phys. **11**, 012 (2021) — 两通道模型
- M. Čulo et al., Nature **595**, 661 (2021) — 非相干输运
- F. Mahmood et al., PRL **122**, 027003 (2019) — 失踪的超导电子(THz)
- S.V. Dordevic & C.C. Homes, PRB **105**, 214514 (2022) — 薄膜vs体材料
- PRB **106**, 184510 (2022) — 掺杂剂电位效应

### 概念澄清:
- W. Pickett, arXiv:2601.10578 (2026) — London n_s vs condensate density区分

---

## 组4补充: 落地计算所需数据缺口

为完成S1的定量比较(μSR-λ⁻² vs Cp-λ⁻²含误差棒)，需要以下目前不可得的数据:

1. **数字化提取:** 需要从已发表图中digitize μSR σ(0)和Cp λ⁻²(0)的逐点值 (可用WebPlotDigitizer)
2. **误差传播:** 需要每点的σ(0)误差(μSR的±值)和λ⁻²(0)误差(Cp拟合不确定性)
3. **p值校准:** 不同文献使用的p标度(Tc标度、晶格参数标度、热电势标度)需要统一
4. **多晶平均校正:** Tallon数据需与单晶μSR数据做同基比较
5. **London模型参数:** m*/m_e值在不同家族和掺杂下不同，影响n_s从λ⁻²的提取

**S1的可行性判定:** 存在足够的图数据做半定量比较(从图中提取数据点+手动估计误差棒)，但精确的逐点统计检验需要原始数据，而原始数据不存在于任何公开数据库中。
