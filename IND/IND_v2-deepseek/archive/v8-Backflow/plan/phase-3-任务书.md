# Phase 3 任务书 — v8-Backflow

> 类型：C（物理身份裁决）
> PI 主导执行，不需 A/B 突击推导；可调用 A 子agent做形式核验
> 主任务：综合 v8-K6'/K7/K8/K9 给出"浴熵产生 vs 信息回流记账项"的最终物理身份判定

---

## 〇、北极星距离检查

| 维度 | Phase 2 后 | Phase 3 目标 |
|------|----------|------------|
| 形式判据 | ✅ v8-K1 (★★) | 维持 |
| Σ_B<0 反例 | ✅ v8-K3 (N=1 JC) + v8-K8 (N=2 双模 r(β)) | 维持 |
| Spohn 失效 | ✅ v8-K2 | 维持 |
| Nakagawa structural-domain | ✅ v8-K4 | 维持 |
| BKM 二阶核 | ✅ v8-K7（耦合 sector 分类） | 维持 |
| 重合度 r(β) | ✅ v8-K8（临界 βω₀≈3.69） | 维持 |
| 几何不变量 | ✅ v8-K9（N_I^{(S)}=2ln2 候选） | 普适化（部分） |
| passive+phase-lock 充分条件 | ✅ v8-K6' | 维持 |
| **物理身份裁决** | ❌ **本Phase核心目标** | 给出三选一判定 |

---

## §0 本Phase 推导目标（一句话）

**目标**：基于 v8-K6'/K7/K8/K9 + v8-K1~K5，给出"浴内部熵产生率 Σ_B^{int}"的物理身份精确判定，三个候选解释中选一或给出温度域分割：

- **(A) 浴的 inherent 不可逆熵产生**——Σ_B^{int} 是浴侧独立的不可逆 thermodynamic entropy production，不可化约为信息回流
- **(B) 信息回流记账项**——Σ_B^{int} 实质上是 −d/dt I(S:B) 的某个分量（Esposito 2010 风格），在适当 sector 选择下退化为 Nakagawa N_I 的纯记账量
- **(C) 温度域分割**：低温区（βω₀ ≳ 3.69）走 (B)；高温区（βω₀ ≲ 1.5）走 (A)；中间区是混合

**可证伪声张 J1-J3**：
- J1：在 v8-K8 的 toy 模型中，∫_{T_<} Σ_B^{int} dt = c · N_I^{(neg, S)} 对某常数 c（c=−1 → 完全记账项；c=0 → 完全独立；c∈(−1,0) → 部分记账）
- J2：c 的 β 依赖：c(β→∞) → −1（低温完全记账）；c(β→0) → 0（高温完全独立）
- J3：c 的几何意义：c = N_I^{(neg, B)} / N_I^{(neg, S)} 比值（B sector 与 S sector 的负 backflow 比值）

---

## §1 强制撞墙

PI 必须在裁决前回答：

1. **零阶 sanity check**：在严格 N→∞ + 弱耦合 + 长时间极限下，Σ_B^{int} → 0（v5-K6 已知）。这是 (A) 和 (B) 两个候选都共享的极限。Phase 3 必须给出**有限 N + 强反平衡 + 短时间**域中两候选的可分判据
2. **Esposito 2010 比对**：Esposito 2010 NJP 12, 013013 给出 Σ_total = D(ρ_SB‖ρ_S⊗ρ_B^{eq})。把它对时间求导并 chain-rule 拆解：
   $$\dot Σ_{total} = \dot D(\rho_S\|\rho_S^{eq}) + \dot D(\rho_B\|\rho_B^{eq}) + \dot Σ_{corr}$$
   其中 $\dot Σ_{corr}$ 是 system-bath correlation 部分。**Σ_B^{int} 是不是恰好 = $-\dot D(\rho_B\|\rho_B^{eq})$？** 是的——v8-K1 就是这个！但是，这是不是就证明了候选 (B)？
3. **Nakagawa 等价性**：v8-K4 给出 Σ_B^{int} ≡ İ_B（其中 I_B = −D(ρ_B‖ρ_B^{eq})）。这是不是意味着 Σ_B^{int} **就是定义为** B sector 的 Nakagawa 信息度？如果是，Σ_B^{int}<0 ⟺ I_B 下降 ⟺ 浴远离参考态——这就是字面定义上"信息回流"的反向

**裁决**（由 PI 独立给出）：从 §1 撞墙的回答看，候选 (B) 是 Σ_B^{int} 的**字面定义**——但定义不等于物理。物理判定需要 c 系数（J1）的具体值。

---

## §2 PI 推导步骤（强制）

### §2.1 c 系数计算（toy 模型）

在 v8-K8 setup 下：
- N=2 双模 JC 共振 + |e,0,0⟩ + 对称耦合
- t_max = π/(2Ω)，Ω=g√2

**S sector**（v8-K9）：
$$N_I^{(S)} = \int_0^{t_{max}} [\dot I_S]_+ dt = 2\ln 2$$
$$N_I^{(neg, S)} = \int_0^{t_{max}} [\dot I_S]_- dt = ?$$

由 İ_S = 4Ω sin(2Ωt) ln cot(Ωt)，在 (0, π/(4Ω)) 上 cot(Ωt) > 1 ⟹ ln>0 + sin>0 ⟹ İ_S>0；在 (π/(4Ω), π/(2Ω)) 上 cot<1 ⟹ ln<0 + sin>0 ⟹ İ_S<0。

由对称性 ∫_0^{π/(2Ω)} İ_S dt = I_S(π/(2Ω)) − I_S(0) = 0（两边都是 q=p=1/2 的对称点）。

所以 $N_I^{(neg, S)} = N_I^{(S)} = 2\ln 2$（正负相等）。

**B sector**：
$$N_I^{(B)} = \int [\dot I_B]_+ dt,\quad I_B = -D(\rho_B\|\rho_B^{ref}(\beta))$$
$$\dot I_B = \Sigma_B^{int}(t) = \dot p [\ln(q/p) − \beta\omega_0]$$

**T_<**（Σ_B<0）：(Ωt*, π/4) ∪ (3π/4 reflected) — 在 (0, π/(2Ω)) 内只有一段 (Ωt*, π/4)，长度 = π/4 − Ωt*
**T_>^B**（Σ_B>0）：(0, Ωt*) ∪ (π/4, π/(2Ω))

所以
$$\int_{T_<} \Sigma_B^{int} dt = \int_{Ωt^*/Ω}^{π/(4Ω)} \dot p [\ln(q/p) − \beta\omega_0] dt$$

代换 u=Ωt:
$$= \int_{Ωt^*}^{π/4} \sin(2u)·[2\ln\cot u − \beta\omega_0] du$$

设 v=cos(2u), dv=−2sin(2u)du:
- u=Ωt* ⟺ v=cos(2Ωt*)。由 Ωt*=arccot(e^{βω₀/2}) ⟹ cos(2Ωt*) = (1−e^{βω₀})/(1+e^{βω₀}) = −tanh(βω₀/2)
- u=π/4 ⟺ v=0

$$= -\frac{1}{2}\int_{-\tanh(\beta\omega_0/2)}^{0} [\ln((1+v)/(1-v)) − \beta\omega_0] dv$$

设 w=−v 翻转：
$$= -\frac{1}{2}\int_0^{\tanh(\beta\omega_0/2)} [\ln((1-w)/(1+w)) − \beta\omega_0]·(-dw) = \frac{1}{2}\int_0^{\tanh(\beta\omega_0/2)} [-\ln\frac{1+w}{1-w} − \beta\omega_0] dw$$

$$= -\frac{1}{2}\int_0^{T} [\ln\frac{1+w}{1-w} + \beta\omega_0] dw,\quad T:=\tanh(\beta\omega_0/2)$$

第一项 ∫ ln((1+w)/(1−w)) dw 用 (1+w)ln(1+w) + (1−w)ln(1−w) 的导数 = ln((1+w)/(1−w))，所以 ∫_0^T = (1+T)ln(1+T)+(1−T)ln(1−T)。

第二项 ∫_0^T βω₀ dw = βω₀·T。

合并：
$$\int_{T_<} \Sigma_B^{int} dt = -\frac{1}{2}\left[(1+T)\ln(1+T)+(1-T)\ln(1-T) + \beta\omega_0\cdot T\right]$$

由 T=tanh(βω₀/2)，和 ln((1+T)/(1−T)) = βω₀，所以 (1+T)ln(1+T)+(1−T)ln(1−T) = (1+T)·[ln 2 + ln((1+T)/(1+1)) ... ]——让我用恒等式：
$$2\cosh(x/2)·e^{−|...|}...$$
或直接：1+tanh(x/2) = e^x/(1+...)... 简化：1±T = 2e^{±βω₀/2}/(e^{βω₀/2}+e^{-βω₀/2}) = sech(βω₀/2)·e^{±βω₀/2}

所以 (1+T)ln(1+T)+(1−T)ln(1−T) = sech(βω₀/2)·[e^{βω₀/2}·ln(sech·e^{βω₀/2}) + e^{−βω₀/2}·ln(sech·e^{−βω₀/2})]
= sech·[(e^{βω₀/2}+e^{−βω₀/2})·ln sech + (e^{βω₀/2}·βω₀/2 − e^{−βω₀/2}·βω₀/2)]
= sech·[2cosh(βω₀/2)·ln sech + 2sinh(βω₀/2)·βω₀/2]
= 2 ln sech(βω₀/2) + βω₀·tanh(βω₀/2)
= −2 ln cosh(βω₀/2) + βω₀·T

代回：
$$\int_{T_<} \Sigma_B^{int} dt = -\frac{1}{2}[-2\ln\cosh(\beta\omega_0/2) + \beta\omega_0·T + \beta\omega_0·T]$$
$$= \ln\cosh(\beta\omega_0/2) - \beta\omega_0·\tanh(\beta\omega_0/2)$$

**这个量 < 0**（验证：βω₀=4 时 cosh(2)=3.762, ln=1.325, tanh(2)·4=3.857，差 = 1.325-3.857 = -2.532 ✓）

记 $\Sigma_B^{int,(neg)} := -\int_{T_<} \Sigma_B^{int} dt = \beta\omega_0\tanh(\beta\omega_0/2) - \ln\cosh(\beta\omega_0/2) > 0$（这是浴熵产生在 negative window 上的累积量级）

### §2.2 N_I^{(neg, S)} 计算

由对称性已知 N_I^{(neg, S)} = N_I^{(S)} = 2ln 2 ≈ 1.386 (g 无关)

### §2.3 c 系数

$$c(\beta) := \frac{\Sigma_B^{int,(neg)}}{N_I^{(neg, S)}} = \frac{\beta\omega_0\tanh(\beta\omega_0/2) - \ln\cosh(\beta\omega_0/2)}{2\ln 2}$$

注意符号约定：J1 的 c 是 ∫_{T_<}Σ_B^{int}dt = c·N_I^{(neg, S)}。由 ∫_{T_<}Σ_B^{int}<0 + N_I^{(neg, S)}>0 ⟹ c<0。重写：
$$c(\beta) = -\frac{\beta\omega_0\tanh(\beta\omega_0/2) - \ln\cosh(\beta\omega_0/2)}{2\ln 2} < 0$$

数值表：

| βω₀ | tanh(x/2) | x·tanh(x/2) | ln cosh(x/2) | 浴熵产生累积 (-c·2ln2) | c |
|-----|-----------|-------------|--------------|-----------------------|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0.462 | 0.462 | 0.121 | 0.341 | −0.246 |
| 2 | 0.762 | 1.524 | 0.434 | 1.090 | −0.786 |
| **3.69**(R1) | 0.927 | 3.420 | 0.946 | 2.474 | **−1.785** ⚠️ |
| 4 | 0.964 | 3.857 | 1.325 | 2.532 | −1.826 |
| 6 | 0.995 | 5.970 | 2.882 | 3.088 | −2.227 |
| ∞ | 1 | ∞ | (βω₀/2)−ln 2 | (βω₀/2)+ln 2 | → −∞ |

⚠️ **关键发现**：**c(β) 不停留在 [−1, 0]！** βω₀ ≈ 1.41 时 |c|=0.5；βω₀ ≈ 3 时 |c|≈1.4>1；βω₀=∞ 时 |c|→∞。

**这意味着**：在 toy 模型中，∫_{T_<} Σ_B^{int} dt 比 N_I^{(neg, S)} **大**（绝对值）。

### §2.4 物理身份裁决

**c<−1 的物理意义**：浴熵产生 negative-window 累积量 > 系统侧 N_I^{(neg, S)}。即"浴熵被信息回流'吸收'的量"超过"系统侧获得的信息回流"——存在**额外的浴侧不可逆熵产生**未被信息回流账面化。

**裁决**：
- 候选 (B)（"Σ_B^{int} = 信息回流记账项"）**被证伪**——若 (B) 严格成立，则 c=−1（一对一抵消）。但 toy 数据 c=−1.83 显示**浴侧 negative-window 累积超过 S sector backflow 1.83 倍**
- 候选 (A)（"Σ_B^{int} 是 inherent 浴熵产生"）**部分支持**——存在不能被 N_I^{(S)} 全额吸收的"额外不可逆量"
- 候选 (C)（温度分割）**精化版**：
  - 高温 βω₀→0：c→0，浴熵产生几乎为 0，此时 Σ_B^{int} 的物理意义 trivial（既不是 (A) 也不是 (B)，是 noise）
  - 中温 βω₀∈[1, 3]：c ∈ [−0.25, −1.4]，从"部分记账"过渡到"超额"
  - 低温 βω₀≳3.7：c < −1.8，**浴熵产生显著超过信息回流**——候选 (A) 占优

**最终物理身份**：Σ_B^{int} **既不是纯信息回流记账项，也不是纯 inherent 不可逆熵产生**——它是**两者的复合，且复合系数依赖温度**。

精确陈述（v8-K10）：在 toy 模型中
$$\Sigma_B^{int}(t) \cdot \mathbb{1}_{T_<}(t) = -\dot I_S(t) \cdot \mathbb{1}_{T_<}(t) - \xi(t,\beta)$$
其中 $\xi(t,\beta) ≥ 0$ 是 inherent 浴熵产生密度，且
$$\int_{T_<} \xi(t,\beta) dt = (|c(β)|-1) \cdot 2\ln 2$$

低温下 $\int \xi \to \infty$（按 βω₀ 一阶发散），高温下 $\int \xi \to 0$。

### §2.5 与 Aoki 2021 的连接

Aoki 2021 的 Σ_total<0 包含 Σ_S + Σ_B^{int} + Σ_{corr}（corr 是 S-B 关联部分）。本课题 v8-K10 给出的 ξ(t,β) 是 Aoki 现象在浴侧的**精化分量**——v8-K3 已建立闭式反例，v8-K10 给出"超额不可逆量"的精确闭式。

这是 Aoki 2021 框架未触及的精化层级。

---

## §3 输出

PI 主导执行，不需调用子 agent。所有推导写到本文档。

PI 写作完成后启动收官 GATE：AUDITOR + 恶意审稿人 + AHA 访客 + NAVIGATOR（这些是独立子 agent）。

---

## §4 v8-K10 候选条目（待 PI 独立推导后正式写入知识库）

| 编号 | 内容 | 状态 |
|------|------|------|
| **v8-K10** | **复合身份定理**：Σ_B^{int} 不是纯信息回流记账项也不是纯 inherent 不可逆熵产生；toy 模型中分解为 −İ_S + ξ(t,β)，其中 ξ≥0 是 inherent 浴熵产生密度。c(β) := ∫_{T_<}Σ_B^{int}dt / N_I^{(neg,S)} 的精确闭式 c(β) = −(βω₀·tanh(βω₀/2) − ln cosh(βω₀/2))/(2ln 2)；c(β→0)→0（trivial）；c(β→∞)→−∞（inherent 主导）；临界 c=−1 在 βω₀≈2.27（即 ξ累积=N_I^{(S)}）。物理身份判定：(A) inherent 浴熵产生 + (B) 信息回流记账 的**温度依赖复合**，分隔尺度 T_c≈ω₀/2.27。 | ⚠️L2 候选 |

---

▶️ Phase 3 PI 主导执行。任务书完。
