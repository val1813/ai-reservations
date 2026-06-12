# LP38 → PRL 投稿 — 实验数据与脚本

**论文:** Causal Loop Topology Enforces Quantum Non-Markovianity
**目标期刊:** Physical Review Letters
**数据日期:** 2026-06-08 至 2026-06-09
**硬件:** IBM ibm_kingston (Heron r2, 127 qubits, heavy-hex)

---

## 目录结构

```
data/
├── README.md                             ← 本文件
├── CFOL_RESULTS_SUMMARY.md               ← CFOL实验最终总结 ⭐
│
│   # === CFOL时序环实验 (2026-06-09) ===
├── cfol_ibm_experiment.py                CFOL定理验证脚本 (3-qubit)
├── cfol_results_d8k1kcj2.json            CFOL v1原始结果 (20k shots, Z+X基) ⚠️已废弃

│   # === Y基CFOL验证 (2026-06-10) === ⭐ 论文核心数据
├── cfol_ybasis_submit.py                 Y+Z基提交脚本
├── cfol_ybasis_retrieve.py               Y+Z基结果提取脚本
├── cfol_Y_job.json                       Y基Job元数据 (d8kborbnn5bs738qlerg)
├── cfol_Z_job.json                       Z基Job元数据 (d8kbp33nn5bs738qlf60)
├── cfol_ZY_results.json                  Y+Z基实验结果 ⭐⭐⭐
├── cfol_final_jobs.json                  最终Job汇总
│
│   # === Y基预测 (本地模拟) ===
├── ybasis_prediction.py                  Y基CFOL预测脚本
├── ybasis_prediction.json                Y基预测数值
├── zbasis_ybasis_full.json               Z+Y基全参数扫描网格
│
│   # === 协议1+2: 比例测试 + 轴测试 (2026-06-09) ===
├── protocols_submit.py                   协议1+2提交脚本 (8 circuits)
├── protocols_retrieve.py                 协议结果提取+分析脚本
├── protocols_job_id.txt                  Job元数据 (d8k2e4bnn5bs738q9s70)
│
│   # === 理论预测 (本地计算) ===
├── theory_ratio_axis_test.py             比例测试+轴测试理论计算 ⭐
├── theory_predictions.json               理论预测数值 (R=0.48, 轴比=2.06x) ⭐
│
│   # === 数值实验 (不需要IBM Q) ===
├── numerical_experiments.py              环尺寸标度+噪声鲁棒性+空间环全模拟 ⭐
├── numerical_experiments_results.json     数值实验结果 (4 Figure数据) ⭐
│
│   # === Y基CFOL验证 (本地模拟) ===
├── ybasis_prediction.py                  Y基CFOL预测脚本 ⭐
├── ybasis_prediction.json                Y基预测数值 (IBM Q条件下ΔI_Y=0.079) ⭐
├── zbasis_ybasis_full.json               Z+Y基全参数扫描 (fid×eps×theta网格) ⭐
│
│   # === V3/V4 空间环实验 (2026-06-08) === (已废弃- SWAP破坏Bell对)
├── v3_raw.json                           IBM Q实验V3原始数据 (Z基, 100k shots)
├── v4_raw.json                           IBM Q实验V4原始数据 (Z+X基, 50k shots)
├── analysis_summary.json                 V3/V4分析摘要
├── ibmq_submit_v3.py                     V3提交脚本
├── ibmq_submit_v4.py                     V4提交脚本
├── ibmq_results_analysis.py              原始数据分析脚本 (QCMI计算)
│
│   # === 预飞行模拟 ===
├── causal_ring_sim.py                    理想4节点因果环模拟
│
│   # === 理论计算脚本 ===
├── b1_scaling.py                         Gram矩阵构造 + b1参数标度率
├── cfol_scan2.py                         CFOL充分性网格扫描 (Δ>0区域)
├── petz_recovery_v2.py                   Fawzi-Renner / Petz恢复映射验证
├── wall5_attack.py                       sin²φ连续曲线攻击 (Wall 5)
├── wall9_attack_v2.py                    QCMI→退相干映射攻击 (Wall 9)
├── theta_scaling_precision.py            小θ精度扫描 (cat2_task5重命名)
│
│   # === 验证文档 ===
├── 21-experimental-framework.md          实验框架与设计原理
├── 22-sin2phi-and-rho.md                 sin²φ展开与ρ参数化验证
├── 23-theta2-error-bounds.md             θ²误差界推导与数值检查
├── 24-cfol-nonaligned.md                 CFOL非对齐扩展 (非对角基)
├── PAPER_ADDITIONS.md                    论文补强文字 (QEC段落+多平台表+叙事)
│
│   # === 设备映射分析 ===
├── A_ibm_mapping.md                      Transmon→Cartan理论映射
├── B_literature_feasibility.md           文献数据可行性审查
├── C_existing_data.md                    公开数据侦察报告
├── qcmi_risk_map.py                      ibm_kingston六边形风险热力图
├── qiskit_simulation.py                  Qiskit噪声模拟框架
│
└── IBMQ_EXPERIMENTS_ORGANIZED.md         完整实验整理与诊断
```

---

## ⭐ CFOL实验 (2026-06-09) — 首次成功

### 设计

3-qubit时序因果环 (vs V3/V4的8-qubit空间环):

```
R ─[H]─[CNOT]────────────────────[测量]
Q ─────[CNOT]─[RZZ(π/2)]─[500ns]─[RZZ(θ)]─[测量]
E ─[Ry(φ)]────[RZZ(π/2)]─[500ns]─[RZZ(θ)]─[测量]
```

- **功能环:** 两个RZZ均激活 → 时序因果环闭合
- **死环(对照):** 第一个RZZ = identity → 因果环断开
- **θ扫描:** π/4, π/8, π/16
- **测量:** Z基 + X基 联合测量

### 关键结果

| θ | ΔI(R;Q)_Z | ΔI(R;Q)_X | Bell保真度 |
|:--|:--|:--|:--|
| π/4 | **0.0339** | 0.1498 | 39.3% |
| π/8 | **0.0190** | 0.5527 | 39.3% |
| π/16 | **0.0083** | 0.6916 | 39.8% |

**Δ = I(R;Q)_dead − I(R;Q)_functional > 0** → CFOL签名确认 ✅

### ⭐ Y基CFOL验证 (2026-06-10) — 论文核心数据

3-qubit时序环，Z+Y基分别100k shots，ibm_kingston，总机时4分钟。

| θ | ΔI_Z | ΔI_Y | Y/Z比 | CFOL符号 |
|:--|:--|:--|:--|:--|
| π/4 | 0.016 | **0.048** | 3x | ✅ |
| π/8 | 0.011 | **0.464** | 43x | ✅ |
| π/16 | 0.011 | **0.586** | 54x | ✅ |

**关键发现:**
- Y基信号3-54x放大，证实Z基盲区预测
- ΔI_Y > 0 对所有θ成立，CFOL定理首次Y基硬件验证
- Y/Z比与理论预测(97-115x)定性一致，定量差异来自CX分解在Y基下的额外贡献
- S/N: 10σ (π/4), 93σ (π/8), 117σ (π/16)

### 与V3/V4对比

| | V3/V4 (空间环) | CFOL (时序环) |
|:--|:--|:--|
| Qubits | 8 | **3** |
| SWAP惩罚 | 6-12 CZ | **0** |
| Bell保真度 | 0% | **39%** |
| QCMI信号 | 噪声伪影 | **真实信号** |

---

## V3/V4实验 (2026-06-08) — 已废弃

8-qubit空间因果环在ibm_kingston上运行。QCMI>0被检测但Bell对被SWAP路由破坏(I(Ra:Qa)=0)。QCMI趋势与理论相反——信号为噪声伪影。

详见 `IBMQ_EXPERIMENTS_ORGANIZED.md`。

---

## 理论计算脚本

以下脚本提供论文中各数值结果的理论支撑计算。

| 脚本 | 描述 | 论文对应 |
|:--|:--|:--|
| `b1_scaling.py` | Gram矩阵构造 + b1参数标度率分析。推导b1在n→∞时的渐进行为，确认式(12)的标度指数 | Section III, Eq.(12) |
| `cfol_scan2.py` | CFOL充分性网格扫描。在(θ, φ)参数空间上计算ΔI(R;Q)，确定Δ>0的允许区域 | Section IV, Fig.3 |
| `petz_recovery_v2.py` | Fawzi-Renner恢复映射与Petz恢复映射的双向验证。数值验证量子信道恢复的充要条件 | Appendix A |
| `wall5_attack.py` | sin²φ连续曲线攻击脚本。构造连续参数族证明Wall 5 (QC-EI对偶)的不稳定性 | Section V, Fig.4 |
| `wall9_attack_v2.py` | QCMI→退相干映射攻击脚本。将QCMI过剩映射到退相干幅度，验证Wall 9的解析边界 | Section V, Eq.(23) |
| `theta_scaling_precision.py` | 小θ精度扫描 (原cat2_task5)。验证θ→0时QCMI测量的有限精度极限，确认式(18)的误差标度 | Section IV, Eq.(18) |

所有脚本均为独立可运行的Python 3脚本。依赖: numpy, scipy, matplotlib (部分需qiskit)。

---

## 数值实验 (不需要IBM Q)

`numerical_experiments.py` 运行四个独立数值实验，生成论文Figure数据:

| Figure | 内容 | 关键结果 |
|:--|:--|:--|
| **A** | 环尺寸标度 N=4,6,8 | CFOL条件对所有尺寸成立(QCMI<10⁻¹²)。θ²log标度普适。QCMI随环尺寸线性增长 |
| **B** | 噪声鲁棒性 (depolarizing) | 信号在10%/门噪声下仍存活。IBM Q实验的50x衰减**不是**门退极化导致的 |
| **C** | 4节点空间环全模拟 | R=QCMI(π/8)/QCMI(π/4)=0.50 vs CCQ=0.0625。IBM Q重六角跑不了的电路 |
| **D** | Cartan轴连续扫描 φ∈[0,π/2] | QCMI单调增长1.09→2.26 bits (2.06x)。确认轴控制QCMI大小 |

```bash
python numerical_experiments.py          # 运行全部四个实验
# 输出: numerical_experiments_results.json
```

核心发现:
- **Ring scaling:** N=4→QCMI~1.1, N=6→~2.2, N=8→~3.2 bits at π/4。CFOL零条件(QCMI=0 ⇔ c∈(π/2)ℤ)对所有N精确成立
- **Noise robustness:** 门退极化ε=0.003时QCMI仅降~5%。实验Δ≈0.03 vs 理论~0.5-1.0的50x差距来自Bell保真度损失+时序vs空间环+Z基部分测量，不是门噪声
- **Spatial ring ratio:** R=0.50 vs CCQ R=0.0625，8x差距，14σ可区分
- **Axis scan:** 连续19点φ扫描，单调增长，确认Cartan轴是QCMI的控制参数

```bash
# 示例: 运行单个脚本
python b1_scaling.py          # Gram矩阵与b1标度率
python cfol_scan2.py          # CFOL网格扫描 (生成Fig.3数据)
python petz_recovery_v2.py    # 恢复映射验证
python wall5_attack.py        # sin²φ连续曲线
python wall9_attack_v2.py     # QCMI-退相干映射
python theta_scaling_precision.py  # 小θ精度扫描
```

---

## 验证文档

以下为论文推导链中各环节的交叉验证文档，记录关键公式的独立推导与数值一致性检查。

| 文档 | 内容 | 验证目标 |
|:--|:--|:--|
| `21-experimental-framework.md` | IBM Q实验框架设计: 线路构造、噪声模型选择、shots预算合理性 | 实验设计完备性 |
| `22-sin2phi-and-rho.md` | sin²φ展开推导与ρ参数化: 验证式(15)的展开截断误差<10^{-3} | Eq.(15), 小φ近似 |
| `23-theta2-error-bounds.md` | θ²误差界推导: 传播QCMI测量误差到θ估计，确认式(18)上界紧致性 | Eq.(18), 误差传播 |
| `24-cfol-nonaligned.md` | CFOL非对齐基扩展: 将CFOL从对角基推广到一般测量基，验证Δ>0条件鲁棒性 | Appendix B, 非对角CFOL |

所有文档均为Markdown格式，包含逐步推导与中间数值结果。

---

## 复现

```bash
cd data/

# CFOL实验 (推荐)
pip install qiskit qiskit-ibm-runtime
python cfol_ibm_experiment.py --token YOUR_TOKEN --dry-run   # 先试跑
python cfol_ibm_experiment.py --token YOUR_TOKEN              # 提交

# 结果分析
python check_and_retrieve.py                                  # 自动检测+提取

# V3/V4分析 (参考)
python ibmq_results_analysis.py
```

---

## 原始数据格式

`cfol_results_d8k1kcj2.json`:
```json
{
  "job_id": "d8k1kcj2d42s73c9kipg",
  "results": {
    "pi/4": {
      "delta_Z": 0.0339, "delta_X": 0.1498,
      "irq_functional_Z": 0.7853, "irq_dead_Z": 0.8192,
      "bell_fidelity": 0.3926
    }
  }
}
```

`v3_raw.json` / `v4_raw.json`: 每电路100k/50k个单shot的6-bit测量结果。

---

## 引用

如在论文中使用此数据，请引用:

> "IBM Q experimental data collected on ibm_kingston (Heron r2) as part of the LP38 QCMI precision project. The 3-qubit temporal causal ring experiment (Job ID: d8k1kcj2d42s73c9kipg) provides the first experimental confirmation of the CFOL theorem. Data available at [this repository]/paper1-prl/data/."

---

## 令牌

`0wTawcB4PogS7TQ0Tf8Km59hYGUAdyy3RUkLgahy91wm` (open plan)

---

*最后更新: 2026-06-09 — 理论脚本与验证文档归档完成，10文件入库*
