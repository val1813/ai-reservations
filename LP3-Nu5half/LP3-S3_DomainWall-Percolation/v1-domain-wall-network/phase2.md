# Phase 2：域壁网络的参数扫描与判据

**日期：** 2026-06-01
**状态：** 完成
**目标：** 把 Phase 1 的“窄窗条件”整理成可扫描的判据，判断 GaAs ν=5/2 是否更像 `K=5/2` thermal insulator，而不是 direct Pf/APf transition 或 thermal metal。

---

## 1. 三个无量纲扫描轴

定义三个最小扫描轴：

```text
x = E_dis / E_dis^crit
y = xi_dis / d_DW
z = rho_vortex * d_DW^2
```

其中：
- `E_dis^crit ~ 2.9e5 V/m`：稳定 Pf/APf 域壁所需门槛电场；
- `d_DW >= 16 l_B`：域壁穿透长度；
- `xi_dis`：无序相关长度，实验上通常与掺杂 setback 同阶；
- `rho_vortex`：有效 random vortex / pi-flux 面密度。

### 物理含义

- `x` 控制域壁是否能被无序钉扎并长期存在；
- `y` 控制域壁是否足够粗、足够长，能形成 percolating network；
- `z` 控制 Majorana zero mode 是否过密，从而推动 thermal metal。

---

## 2. 经验参数代入

从文献与实验常识取一组保守窗口。注意：这里的 `E_dis` 是作用在 Pf/APf energy bias 上的有效无序分量，不是裸库仑电场；裸电场必须经过 screening、有限厚度、LL projection 和 disorder form factor 后才能代入。

- `l_B ~ 11.5 nm` at `B=5 T`
- `d_DW >= 16 l_B ~ 184 nm`
- `xi_dis ~ 100 nm`
- `sigma_DW ~ (1.7-2.1)e-3 e^2/l_B^2`
- `E_dis^crit ~ 2.9e5 V/m`

因此几何上：

```text
y = xi_dis / d_DW ~ 0.5 - 0.6   (using B=5T and d_DW lower bound)
```

这说明实验样品中的掺杂相关长度与域壁厚度是同阶的，不是强分离尺度。

对 `x`，文献给出的门槛电场与高迁移率 GaAs 的裸局域场是同阶竞争。由于有效分量未算，这里不写成“已严格超过”，只写成：

```text
x_bare = O(1),  x_eff unknown
```

这意味着样品可能停在门槛附近，而不是被一边彻底压死；但是否真正位于窗口，需要自洽 electrostatic/LL-projected 估计。

---

## 3. 三类结果

### Regime A：direct Pf/APf switching

条件：

```text
x << 1 or y >> 1
```

解释：
- 无序电场太弱，或者域壁太厚/太贵；
- Pf/APf 直接一阶样切换；
- 热霍尔值只会落在 `7/2` 或 `3/2`，最多出现窄过渡区。

### Regime B：localised K=5/2 thermal insulator

条件：

```text
x ~ 1
y ~ O(1)
z << 1
eta_intra >> eta_inter
rho_vortex low or paired
```

解释：
- 域壁存在并连成网络；
- 但 Majorana 模被足够强的 intra-island mixing 局域化；
- 结果是 `K=5/2`, `kappa_xx -> 0`。

### Regime C：thermal metal

条件：

```text
x >> 1 or z >> 1 or eta_inter too large
```

解释：
- random vortex / π-flux 过密；
- inter-island hopping 过强；
- Majorana 模形成扩展态；
- `K` 不量子化，`kappa_xx > 0`。

---

## 4. 与文献相图的对应

Wang-Vishwanath-Halperin 给出：
- 弱无序：direct transition；
- 中等无序：thermal metal 主导；
- 限制参数区：`K=5/2` thermal insulator。

Lian-Wang 给出：
- `Lambda < Lambda1`：单一 Pf/APf 转换；
- `Lambda1 < Lambda < Lambda2`：可能出现 `K=5/2`；
- `Lambda > Lambda2`：四次跳变或 thermal metal。

Phase 2 的代理扫描把这两张图压缩成一句话：

```text
GaAs can only realize K=5/2 if it sits near the disorder threshold but below the delocalization threshold.
```

也就是：

```text
x ~ 1
z small enough
```

---

## 5. 判决表

| 区域 | `K` | `kappa_xx` | 对 LP3-S3 的意义 |
|------|-----|-----------|------------------|
| 弱无序 | 7/2 或 3/2 | 0 | 直接 Pf/APf，不支持域壁解释 |
| 窄窗 | 5/2 | 0 | 支持域壁稳定 PH-Pf thermal insulator |
| 强无序 | 非量子化 | >0 | thermal metal，否定 `K=5/2` plateau |

---

## 6. 首轮判定

**L2-4：GaAs 裸参数更像“门槛附近”，不是“强弱无序任取都行”；但有效参数尚未闭合。**

这意味着 S3 的最佳陈述不是“domain wall 模型必然解释实验”，而是：

```text
domain-wall percolation is viable only in a narrow, threshold-near window.
```

从 LP3 全局看：
- S1 给出边缘 tradeoff；
- S2 给出映射稳定但有限边界；
- S3 给出第三路径的窄窗条件。

因此 LP3 最终更可能写成“有边界”的三路分解，而不是单一路径击败一切。

---

## 7. Phase 2 结论

**结论类型：有边界。**

Pf/APf 域壁渗流在理论上能产生 `K=5/2`，但其实验可实现性被压缩到一个窄窗：无序要足以生成并钉扎域壁，又不能大到触发 class-D thermal metal。GaAs ν=5/2 的裸参数看起来并非远离这个窗口，但有效参数未闭合，也没有证据表明它自然、稳健地深落在窗内。

**下一步：** 把这份窄窗结论并入 S1/S2，形成 S3 synthesis；若需要最后闭环，则写判决实验方案 S4。
