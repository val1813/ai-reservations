# Phase 2：判决路线图与失败判据

**日期：** 2026-06-01
**状态：** 完成
**目标：** 把三路解释压缩成一页实验路线图，并给出每条路径的失败判据。

---

## 1. 一页路线图

### Step 1：无序样品系列

先做多 wafer / 多 setback 样品系列，扫 disorder 强度。

看什么：
- `K` 是否只在中等无序出现；
- `kappa_xx` 是否在强无序下抬升；
- plateau 宽度是否先增后减。

判定：
- 若只在中等无序出现 `K=5/2`，优先支持域壁渗流。
- 若 `K=5/2` 对无序很稳，支持边缘解耦或边缘 tradeoff。

### Step 2：侧门电压扫描

在固定样品上调边缘势。

看什么：
- `d kappa_xy / dVg`
- `kappa_xy^total` 与经边缘通道分解后抽取的 `kappa_xy^frac` 的协同变化
- 边缘热平衡化长度是否随 `Vg` 明显改变

判定：
- 若边缘变化大、bulk 信号稳，支持边缘解耦。
- 若 `kappa_xy^total` 与协议抽取的 `kappa_xy^frac` 锁定，支持纯边缘修正；但该判据必须独立报告抽取协议，避免循环验证。

### Step 3：bulk probe

把 STM、局域隧穿或局域噪声作为长周期终局候选去找 bulk 纹理；它判别力强，但现实可及性最低，不应压过无序系列和侧门扫描。

看什么：
- Pf/APf puddle 纹理；
- domain-wall resonance；
- 局域非均匀热/电信号。

判定：
- 若看到 bulk puddle / domain-wall 纹理，支持域壁渗流；
- 若 bulk 看起来干净，而 edge 有强响应，则更像边缘解耦/边缘修正。

---

## 2. 失败判据

### 失败判据 A：S1 失效

如果 `kappa_xy^frac` 和 `kappa_xy^total` 明显不同步，且边缘势扫描不能解释全部偏差，则纯边缘 tradeoff 不足。

### 失败判据 B：S2 失效

如果 bulk probe 直接看到 Pf/APf puddle，而 edge 只是被动读出，则 `bulk APf + edge PHPf-like` 不是完整解释。

### 失败判据 C：S3 失效

如果 `K=5/2` 没有无序窗口，或者强无序下很快进入 `kappa_xx > 0` 的 thermal metal，则域壁渗流不是稳定主机制。

---

## 3. 推荐执行顺序

1. 无序样品系列
2. 侧门电压扫描
3. bulk probe

原因：
- 样品系列最容易先锁定 S3 是否有窄窗；
- 侧门扫描最便宜地区分 S1 vs S2；
- bulk probe 最慢，只作为终局候选和交叉确认。

---

## 4. 简化判决树

```text
Observe K=5/2
  |
  +-- varies mainly with disorder series?
  |       +-- yes -> domain-wall route favored
  |       +-- no  -> go to side-gate scan
  |
  +-- varies mainly with edge gate?
  |       +-- yes -> edge route favored
  |       +-- no  -> go to bulk probe
  |
  +-- bulk puddle/domain-wall texture seen?
          +-- yes -> domain-wall route
          +-- no  -> systematics/edge route
```

---

## 5. Phase 2 结论

**有边界。**

三条解释都无法靠单一 `kappa_xy` 关闭。真正能做判决的是实验组合，而不是更复杂的单个理论参数。最小闭环已经固定为：

- 无序样品系列
- 侧门电压扫描
- bulk probe（终局候选，不是近期主导实验）

S4 的价值在于把 LP3 的三个理论分支收束到实验可判决对象。
