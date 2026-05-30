import json
from pathlib import Path

v7 = json.loads(Path('eval/keywords_v7_prompt.json').read_text(encoding='utf-8'))

# Check ohos contamination
ohos_count = 0
for k, v in v7.items():
    for field in ['core', 'context', 'synonym']:
        for lang in ['zh', 'en']:
            for kw in v.get(field, {}).get(lang, []):
                if 'ohos' in kw.lower() or '@ohos' in kw.lower() or 'harmonyos' in kw.lower():
                    ohos_count += 1
                    print(f'  ohos contamination: id={k} {field}.{lang}: {kw}')
print(f'Ohos-contaminated keywords: {ohos_count}')

# Check keywords_en/zh present
has_kw_en = sum(1 for v in v7.values() if 'keywords_en' in v and v['keywords_en'])
has_kw_zh = sum(1 for v in v7.values() if 'keywords_zh' in v and v['keywords_zh'])
print(f'Has keywords_en: {has_kw_en}/192, keywords_zh: {has_kw_zh}/192')

# Check cross-framework in synonym
cross_framework = ['OkHttp','URLSession','axios','SharedPreferences','UserDefaults','WKWebView','WebView2','setTimeout','React Router','NavController','Hero','WorkManager','ScheduledExecutor','Timer.singleShot']
v7_cross_syn = 0
for k, v in v7.items():
    for kw in v.get('synonym', {}).get('en', []):
        for cf in cross_framework:
            if cf.lower() in kw.lower():
                v7_cross_syn += 1
                break
print(f'v7 cross-framework in synonym.en: {v7_cross_syn}')

# Aggregate counts
v7_total_core_en = sum(len(v.get('core', {}).get('en', [])) for v in v7.values())
v7_total_ctx_en = sum(len(v.get('context', {}).get('en', [])) for v in v7.values())
v7_total_syn_en = sum(len(v.get('synonym', {}).get('en', [])) for v in v7.values())
v7_total_kw_en = sum(len(v.get('keywords_en', [])) for v in v7.values())
v7_total_kw_zh = sum(len(v.get('keywords_zh', [])) for v in v7.values())

print(f'v7 core.en avg: {v7_total_core_en/192:.1f}')
print(f'v7 context.en avg: {v7_total_ctx_en/192:.1f}')
print(f'v7 synonym.en avg: {v7_total_syn_en/192:.1f}')
print(f'v7 keywords_en avg: {v7_total_kw_en/192:.1f}')
print(f'v7 keywords_zh avg: {v7_total_kw_zh/192:.1f}')

# Empty synonym count
v7_empty_syn_en = sum(1 for v in v7.values() if not v.get('synonym', {}).get('en', []))
v7_empty_syn_zh = sum(1 for v in v7.values() if not v.get('synonym', {}).get('zh', []))
print(f'v7 empty synonym.en: {v7_empty_syn_en}, zh: {v7_empty_syn_zh}')

# Capitalized API names in core
v7_api_core = sum(1 for v in v7.values() for kw in v.get('core', {}).get('en', []) if kw[0].isupper() and len(kw) > 1)
print(f'v7 capitalized API names in core.en: {v7_api_core}')

# Sample entries
for sid in ['1', '3', '5', '50', '100', '145']:
    e = v7[sid]
    print(f'--- id={sid} ---')
    print(f'  query: {e["query"]}')
    print(f'  core.en: {e["core"]["en"]}')
    print(f'  context.en: {e["context"]["en"]}')
    print(f'  synonym.en: {e["synonym"]["en"]}')
    print(f'  keywords_en: {e.get("keywords_en", "MISSING")}')