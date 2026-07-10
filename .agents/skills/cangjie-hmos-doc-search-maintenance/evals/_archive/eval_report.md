# 知识图谱搜索评测报告

**图谱**: `data/doc/graph.json`
**搜索方法**: OR+累加
**测试集**: eval_queries_comprehensive_deduped.jsonl (192 条)

## 1. 总体指标

| 指标 | 值 |
|------|-----|
| 总查询数 | 192 |
| 完全命中 (FULL) | 178 (92.7%) |
| 部分命中 (PARTIAL) | 8 (4.2%) |
| 未命中 (MISS) | 6 (3.1%) |
| 综合 Recall@5 | 96.9% |
| 平均延迟 | 2.4ms |

## 2. 各类别表现

| 类别 | 总数 | FULL | PARTIAL | MISS | R@5 |
|------|-----:|----:|--------:|-----:|----:|
| api_lookup | 20 | 17 | 2 | 1 | 95.0% |
| comparison | 15 | 14 | 0 | 1 | 93.3% |
| composition | 15 | 14 | 0 | 1 | 93.3% |
| constrained | 20 | 18 | 2 | 0 | 100.0% |
| cross_ecosystem | 15 | 14 | 1 | 0 | 100.0% |
| enumeration | 20 | 20 | 0 | 0 | 100.0% |
| how_to | 22 | 19 | 1 | 2 | 90.9% |
| performance_boundary | 16 | 16 | 0 | 0 | 100.0% |
| reverse_lookup | 16 | 15 | 0 | 1 | 93.8% |
| semantic_fuzzy | 16 | 14 | 2 | 0 | 100.0% |
| workflow | 17 | 17 | 0 | 0 | 100.0% |

## 4. 未命中查询 (MISS)

共 6 条：

| ID | 类别 | 查询 | Top1 结果 |
|---:|------|------|-----------|
| 14 | api_lookup | Duration的构造方法 | `cj-image-video-imageanimator\ImageAnimator\基础类型定义.` |
| 44 | reverse_lookup | 要发送通知用什么API | `cj-notification-overview\cj-notification-overview.` |
| 76 | comparison | AES和RSA加密有什么区别 | `cj-huks-encryption-decryption-overview\cj-huks-enc` |
| 101 | composition | 做一个带通知的下载任务 | `cj-information-display-progress\Progress\.overview` |
| 185 | how_to | 动画效果怎么实现 | `cj-attribute-animation-apis\实现属性动画\.overview.md` |
| 187 | how_to | 通知怎么发 | `cj-notification-overview\cj-notification-overview.` |