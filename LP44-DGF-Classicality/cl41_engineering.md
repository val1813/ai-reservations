# cl(4,1) 工程落地

**日期:** 2026-06-10
**硬件:** IBM Q Heron (133 qubit, 99.9% 门保真度)
**已有验证:** DGF-Survivors LP38 - Kingston Heron r2, 单环QCMI S/N=617x

---

## 设计

```
Q1 ──[c_tune]── E1 ──[π/2]── Q2
 │                            │
 └────[π/2]──── E2 ──[π/2]────┘

边1: 可调耦合器 (c_tune = 0 ~ π)
边2,3,4: 固定CNOT等价耦合 (c = π/2, Clifford)
```

## 三种冻结点

| c_tune | QCMI测量值 | 时间状态 |
|--------|:---------:|:------:|
| 0 | ~10⁻¹⁰ | 冻结（所有边Clifford） |
| π/2 | ~10⁻¹⁰ | 冻结（所有边Clifford） |
| π/4 | 1.000 bit | 最大流动 |
| π/8 | 0.601 bit | 半流动 |

## 实验参数

- Qubits: 4 (Q1, Q2, E1, E2)
- 总电路: ~256 tomography circuits × 4 c_tune值 × 10000 shots
- 运行时间: ~10分钟 (IBM Q付费账户)
- 测量: 全量子态断层扫描 → 重建ρ_RQ' → 计算QCMI

## 与LP38的区别

LP38: 固定c值，验证CFOL（QCMI=0 ⟺ Clifford）
cl(4,1): 可变c值，演示时间控制（开/关/连续调节）

增量: 不是测量一个点，是扫描整个传递函数QCMI(c_tune)。
