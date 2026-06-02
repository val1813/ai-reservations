# Phase 1：判决树与可观测量

**日期：** 2026-06-01
**状态：** 完成
**目标：** 把 S1/S2/S3 三路解释转成可执行的实验判决树。

---

## 1. 三路解释的核心差异

### 路径 A：系统性偏差 / 边缘非拓扑修正

本质：
- `kappa_xy` 的异常来自边缘平衡化、热损失、边缘势重构、非对称通道混合。

可观测特征：
- 边缘势改变时，经边缘通道分解后抽取的 `kappa_xy^frac` 和 `kappa_xy^total` 相关变化；
- bulk 物理保持近似不变；
- 无须 bulk puddle / domain-wall 纹理。

### 路径 B：bulk-edge 解耦

本质：
- bulk 仍是 APf，edge 读出因重构/映射/局域 gap 变成 PHPf-like。

可观测特征：
- bulk probe 显示 APf 纹理；
- edge 局域谱、热通道对门电压敏感；
- `kappa_xy^total` 稳定，而 edge 读出可变。

### 路径 C：域壁渗流

本质：
- Pf/APf puddle 形成 domain-wall network；
- Majorana 模在网络上局域化，给出 `K=5/2`。

可观测特征：
- 样品无序强度存在窄窗；
- 中等无序最容易出现 `K=5/2`；
- 强无序进 thermal metal，弱无序回 direct transition；
- bulk 纹理应能看到 puddle / domain wall 痕迹。

---

## 2. 判决树

```text
Start: observe K = 5/2
  |
  +-- Scan side-gate / edge potential
  |     |
  |     +-- kappa_xy^total and kappa_xy^frac co-vary strongly -> Path A
  |     |
  |     +-- bulk unchanged, edge strong response -> Path B
  |
  +-- Scan disorder series
        |
        +-- K=5/2 only near intermediate disorder, weak/strong disorder both lose plateau -> Path C
        |
        +-- K=5/2 stable across disorder series -> Path B or A
```

判决优先级：
1. 无序样品系列
2. 侧门扫描
3. bulk probe

---

## 3. 最小可观测量集合

### 量 1：`kappa_xy^total`
- 判断是否量子化。

### 量 2：`kappa_xy^frac`
- 判断边缘分数通道是否被同步压低。这里的 `kappa_xy^frac` 不是天然独立基本可观测量，必须绑定边缘通道分解、整数通道扣除和热损失校正协议；不能用模型分解量循环验证同一个模型分解。

### 量 3：`kappa_xx`
- 判断是否进入 thermal metal。

### 量 4：门电压斜率 `d kappa_xy / dVg`
- 判断边缘势是否是主驱动。

### 量 5：bulk 纹理指标
- STM / 隧穿 / 局域噪声 / 局域热输运。

---

## 4. 三条排除规则

### 排除 A 的规则

若存在 bulk 纹理，而 edge 变化不能解释样品依赖差异，则系统性偏差不足以独立解释。

### 排除 B 的规则

若 bulk probe 没有 APf 纹理，而 edge 信号显著 PHPf-like，则 bulk-edge 解耦受限。

### 排除 C 的规则

若随无序增强先出现 `K=5/2` 再消失并伴随 `kappa_xx` 升高，则 thermal metal 风险显著，域壁稳定窗很窄。

---

## 5. 第一次排序

| 实验 | 判别力 | 可及性 | 备注 |
|------|------|------|------|
| 无序样品系列 | 高 | 中 | 最能区分窄窗域壁 vs 普适边缘修正 |
| 侧门扫描 | 高 | 中高 | 最便宜的边缘判据 |
| bulk probe | 最高 | 低 | 终局候选；现实可及性最低，不作为近期主导实验 |

---

## 6. Phase 1 结论

**有边界。**

`kappa_xy=5/2` 本身不能判决 S1/S2/S3，必须配套扫描。最强的实验策略不是追求单一读数，而是先用“无序系列 + 门电压”形成近期闭环，再把 bulk probe 作为长周期终局候选。

---

## 7. Phase 2 入口

下一步要做的是把这张判决树压缩为一页的实验路线图，并给出“优先做什么、先排除什么、每一步的失败判据”。
