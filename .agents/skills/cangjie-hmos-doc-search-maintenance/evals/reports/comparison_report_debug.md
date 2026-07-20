# 三引擎搜索对比评测报告

**测试集**: eval_queries_comprehensive_deduped.jsonl (10 条)
**评测引擎**: card / graph / fusion
**计时范围**: 仅纯搜索（不含 query understanding）

## 1. 总体对比

| 指标 | card | graph | fusion |
|------|------|-------|--------|
| 总查询数 | 10 | 10 | 10 |
| 完全命中 FULL | 8 (80.0%) | 10 (100.0%) | 8 (80.0%) |
| 部分命中 PARTIAL | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| 未命中 MISS | 2 (20.0%) | 0 (0.0%) | 2 (20.0%) |
| Recall@5 (FULL+PARTIAL) | 80.0% | 100.0% | 80.0% |
| Precision@1 (FULL) | 80.0% | 100.0% | 80.0% |
| MRR (平均倒数排名) | 0.143 | 0.650 | 0.600 |
| 平均直接命中数 | 18.8 | 5.0 | 6.0 |
| 平均搜索耗时 | 23.7ms | 0.6ms | 22.3ms |
| P50 耗时 | 19.1ms | 0.4ms | 21.4ms |
| P95 耗时 | 79.5ms | 2.2ms | 55.4ms |

## 2. 各类别 Recall@5 对比

| 类别 | card | graph | fusion |
|------|------|-------|--------|
| api_lookup | 80.0% | 100.0% | 80.0% |

## 3. 搜索耗时分布

| 范围 | card | graph | fusion |
|------|------|-------|--------|
| <10ms | 3 | 10 | 3 |
| 10-100ms | 7 | 0 | 7 |
| 100-500ms | 0 | 0 | 0 |
| 500ms-1s | 0 | 0 | 0 |
| >1s | 0 | 0 | 0 |

## 4. MISS 查询对比

| ID | 类别 | 查询 | card | graph | fusion |
|---:|------|------|------|-------|--------|
| 2 | api_lookup | DeviceInfo获取设备信息的具体API | MISS | FULL | FULL |
| 5 | api_lookup | Router.pushUrl的参数 | FULL | FULL | MISS |
| 7 | api_lookup | Router.replaceUrl的参数 | FULL | FULL | MISS |
| 9 | api_lookup | UIAbilityContext的API有哪些 | MISS | FULL | FULL |

## 5. Fusion 补救命中（fusion=FULL 但 card 或 graph = MISS）

共 2 条：

| ID | 查询 | card | graph |
|---:|------|------|-------|
| 2 | DeviceInfo获取设备信息的具体API | MISS | FULL |
| 9 | UIAbilityContext的API有哪些 | MISS | FULL |