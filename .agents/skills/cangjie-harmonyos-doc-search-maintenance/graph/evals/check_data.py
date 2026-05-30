"""Check data sizes for merging."""
import json

queries = []
with open('eval/datasets/eval_queries_comprehensive_deduped.jsonl', encoding='utf-8') as f:
    for line in f:
        queries.append(json.loads(line))

kw5 = json.load(open('eval/keywords_v5_deduped.json', encoding='utf-8'))
print(f'v5 has {len(kw5)} entries')
print(f'Queries have {len(queries)} entries')

sample = kw5['1']
print(f'v5 sample keys: {list(sample.keys())}')
print(f'v5 core keys: {list(sample["core"].keys())}')