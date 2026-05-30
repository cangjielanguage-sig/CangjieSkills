# 15K Post rule+llm AB 对照模板

> 说明：等待 `records/ab-15k-after-rule-llm.json` 生成后，把关键指标填入下表，与 baseline 对比。

## 指标对照（recall@k）

| split | v3 (baseline) | graphify (baseline) | fusion (baseline) | v3 (post) | graphify (post) | fusion (post) | 结论 |
|---|---:|---:|---:|---:|---:|---:|---|
| real_session | 待填 | 待填 | 待填 | 待填 | 待填 | 待填 | 待填 |
| paraphrase | 待填 | 待填 | 待填 | 待填 | 待填 | 待填 | 待填 |
| composition | 待填 | 待填 | 待填 | 待填 | 待填 | 待填 | 待填 |

## 额外门禁

- fusion 是否在三个 split 上都满足 `>= v3` 且 `>= graphify`：待填
- `paraphrase_variance` 是否下降或持平：待填
- `composition_recall_at_concept` 是否提升或持平：待填

## 备注

- baseline 文件：`records/ab-15k-baseline.json`
- post 文件：`records/ab-15k-after-rule-llm.json`
