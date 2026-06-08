# LP29 优先级队列检查与切换

## 检查

当前 protocol 重算分: `0.45`。  
最高候选: `LP29-C2`, 分数 `1.95`。

阈值: `0.45 × 1.3 = 0.585`。  
判定: `1.95 > 0.585`，满足切换规则。

## 切换结果

触发切换。暂停 LP29-current 的收官流程，保留当前状态文件与所有 synthesis artifacts。

新北极星:

> LP29-C2: LP29 graph metrics 是否只是 Srivastava orbital-overlap metric 的重参数化？  
> A: 加入 orbital-overlap baseline 后，LP29 graph metrics 的 residual predictive power 消失。  
> B: 控制 orbital-overlap、onsite variance、density 与 mobility-edge margin 后，`lambda_2`、spectral radius、high-betweenness damage 仍预测 external residual labels。

## 下一步

下一次 Phase 启动应以 LP29-C2 为当前北极星，先执行 GATE -1 核心矛盾结构验证，并优先补真实或可计算的 orbital-overlap baseline / graph-metric join table。
