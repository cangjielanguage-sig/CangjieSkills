"""Validate keywords_v5_deduped.json for quality issues."""
import json
import sys
from pathlib import Path
from collections import Counter

if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
kw_file = PROJECT_ROOT / "eval" / "keywords_v5_deduped.json"
data = json.loads(kw_file.read_text(encoding="utf-8"))

print(f"Total queries: {len(data)}")
print()

# Analyze core keywords for over-generalization
core_en_all = []
core_zh_all = []
context_en_all = []
context_zh_all = []
synonym_en_all = []
synonym_zh_all = []

issues = []

for qid, entry in data.items():
    query = entry.get("query", "")
    core_en = entry.get("core", {}).get("en", [])
    core_zh = entry.get("core", {}).get("zh", [])
    context_en = entry.get("context", {}).get("en", [])
    context_zh = entry.get("context", {}).get("zh", [])
    synonym_en = entry.get("synonym", {}).get("en", [])
    synonym_zh = entry.get("synonym", {}).get("zh", [])
    
    core_en_all.extend(core_en)
    core_zh_all.extend(core_zh)
    context_en_all.extend(context_en)
    context_zh_all.extend(context_zh)
    synonym_en_all.extend(synonym_en)
    synonym_zh_all.extend(synonym_zh)
    
    # Check for issues
    
    # Issue 1: Generic words in core (should be in synonym or removed)
    generic_words_en = ["API", "SDK", "component", "module", "usage", "method", "function", "class", "interface", "guide", "overview"]
    generic_words_zh = ["API", "方法", "组件", "模块", "功能", "使用", "介绍", "说明", "配置", "设置"]
    
    for w in core_en:
        if w in generic_words_en:
            issues.append({
                "id": qid,
                "type": "generic_in_core_en",
                "word": w,
                "query": query[:50]
            })
    
    for w in core_zh:
        if w in generic_words_zh:
            issues.append({
                "id": qid,
                "type": "generic_in_core_zh",
                "word": w,
                "query": query[:50]
            })
    
    # Issue 2: Cross-ecosystem words in core (should be in synonym)
    cross_ecosystem_words = ["Android", "iOS", "React", "Flutter", "Swift", "Kotlin", "UIViewController", "Activity", "SharedPreferences", "RecyclerView", "Hero"]
    
    for w in core_en:
        if any(ce in w for ce in cross_ecosystem_words):
            issues.append({
                "id": qid,
                "type": "cross_ecosystem_in_core",
                "word": w,
                "query": query[:50]
            })
    
    # Issue 3: Empty core (no core keywords)
    if not core_en and not core_zh:
        issues.append({
            "id": qid,
            "type": "empty_core",
            "query": query[:50]
        })
    
    # Issue 4: Too many core keywords (>3)
    if len(core_en) > 3 or len(core_zh) > 3:
        issues.append({
            "id": qid,
            "type": "too_many_core",
            "core_count": len(core_en) + len(core_zh),
            "query": query[:50]
        })

# Statistics
print("=== Keyword Statistics ===")
print(f"Core EN unique: {len(set(core_en_all))}, total: {len(core_en_all)}")
print(f"Core ZH unique: {len(set(core_zh_all))}, total: {len(core_zh_all)}")
print(f"Context EN unique: {len(set(context_en_all))}, total: {len(context_en_all)}")
print(f"Context ZH unique: {len(set(context_zh_all))}, total: {len(context_zh_all)}")
print(f"Synonym EN unique: {len(set(synonym_en_all))}, total: {len(synonym_en_all)}")
print(f"Synonym ZH unique: {len(set(synonym_zh_all))}, total: {len(synonym_zh_all)}")

print()

# Top core keywords
print("=== Top 20 Core EN Keywords (potential over-generalization) ===")
core_en_counter = Counter(core_en_all)
for w, c in core_en_counter.most_common(20):
    print(f"{w}: {c}")

print()
print("=== Top 20 Core ZH Keywords ===")
core_zh_counter = Counter(core_zh_all)
for w, c in core_zh_counter.most_common(20):
    print(f"{w}: {c}")

print()

# Issue summary
print("=== Issue Summary ===")
issue_types = Counter([i["type"] for i in issues])
for t, c in issue_types.most_common():
    print(f"{t}: {c}")

print()
print("=== Sample Issues ===")
for i in issues[:20]:
    print(f"Q{i['id']} [{i['type']}]: {i['query']}")
    if "word" in i:
        print(f"  Problem word: '{i['word']}'")
    if "core_count" in i:
        print(f"  Core count: {i['core_count']}")
    print()