"""Detailed MISS analysis report."""
import json
import sys
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from query import create_session

KEYWORDS_PATH = PROJECT_ROOT / "eval" / "keywords_v5_deduped.json"
JSONL_PATH = PROJECT_ROOT / "eval" / "datasets" / "eval_queries_comprehensive_deduped.jsonl"
BEFORE_GRAPH = PROJECT_ROOT / "data" / "before_llm" / "graph.json"
AFTER_GRAPH = PROJECT_ROOT / "data" / "doc" / "graph.json"
REPORT_PATH = PROJECT_ROOT / "eval" / "miss_analysis_detailed.md"

def load_keywords():
    with open(KEYWORDS_PATH, encoding="utf-8") as f:
        return json.load(f)

def load_queries():
    queries = []
    with open(JSONL_PATH, encoding="utf-8") as f:
        for line in f:
            queries.append(json.loads(line))
    return queries

def check_hit_status(result, acceptable_paths):
    direct_paths = [h.source_file for h in result.direct_hits]
    related_paths = [h.source_file for h in result.related_hits]
    
    def match(rp, aps):
        return any(rp == ap or ap in rp or rp in ap for ap in aps)
        
    direct_hit = any(match(rp, acceptable_paths) for rp in direct_paths)
    related_hit = any(match(rp, acceptable_paths) for rp in related_paths)
    
    if direct_hit:
        return "FULL"
    elif related_hit:
        return "PARTIAL"
    else:
        return "MISS"

def run_detailed_analysis(graph_path, graph_dir, queries, keywords):
    print(f"Loading graph: {graph_path}")
    session = create_session(graph_dir=str(graph_dir))
    session.doc_engine = None
    session.load_doc_graph(str(graph_path))
    
    miss_cases = []
    
    for idx, q in enumerate(queries):
        q_id = idx + 1
        kw = keywords.get(str(q_id), {})
        
        core_en = kw.get("core", {}).get("en", [])
        core_zh = kw.get("core", {}).get("zh", [])
        context_en = kw.get("context", {}).get("en", [])
        context_zh = kw.get("context", {}).get("zh", [])
        synonym_en = kw.get("synonym", {}).get("en", [])
        synonym_zh = kw.get("synonym", {}).get("zh", [])
        
        search_query = " ".join(core_en + core_zh + context_en + context_zh + synonym_en + synonym_zh)
        
        result = session.search(search_query, top_k=5, graph="doc")
        
        status = check_hit_status(result, q.get("acceptable_paths", []))
        
        if status == "MISS":
            top5_results = []
            for h in result.direct_hits:
                top5_results.append({
                    "label": h.label,
                    "source_file": h.source_file,
                    "score": h.score,
                    "match_type": h.match_type
                })
            
            miss_cases.append({
                "id": q_id,
                "original_query": q.get("query", ""),
                "category": q.get("category", "unknown"),
                "keywords": {
                    "core_en": core_en,
                    "core_zh": core_zh,
                    "context_en": context_en,
                    "context_zh": context_zh,
                    "synonym_en": synonym_en,
                    "synonym_zh": synonym_zh
                },
                "search_query": search_query,
                "top5_results": top5_results,
                "expected_paths": q.get("acceptable_paths", [])
            })
    
    return miss_cases

def generate_report(before_miss, after_miss):
    lines = ["# MISS查询详细分析报告", "", "## 1. 增强前图谱 MISS分析", "", f"共 {len(before_miss)} 条未命中查询：", ""]
    
    for case in before_miss:
        lines.append(f"### Q{case['id']} [{case['category']}]")
        lines.append("")
        lines.append(f"**原始查询**: `{case['original_query']}`")
        lines.append("")
        kw = case['keywords']
        lines.append("**关键词配置**:")
        lines.append(f"- Core(EN): {', '.join(kw['core_en']) if kw['core_en'] else '(空)'}")
        lines.append(f"- Core(ZH): {', '.join(kw['core_zh']) if kw['core_zh'] else '(空)'}")
        lines.append(f"- Context(EN): {', '.join(kw['context_en']) if kw['context_en'] else '(空)'}")
        lines.append(f"- Context(ZH): {', '.join(kw['context_zh']) if kw['context_zh'] else '(空)'}")
        lines.append(f"- Synonym(EN): {', '.join(kw['synonym_en']) if kw['synonym_en'] else '(空)'}")
        lines.append(f"- Synonym(ZH): {', '.join(kw['synonym_zh']) if kw['synonym_zh'] else '(空)'}")
        lines.append("")
        lines.append(f"**实际搜索词**: `{case['search_query']}`")
        lines.append("")
        lines.append("**Top 5 结果**:")
        lines.append("")
        lines.append("| Rank | Label | Source File | Score | Match Type |")
        lines.append("|------|-------|-------------|-------|------------|")
        for i, r in enumerate(case['top5_results'], 1):
            lines.append(f"| {i} | {r['label'][:40]} | `{r['source_file'][:60]}` | {r['score']} | {r['match_type']} |")
        lines.append("")
        lines.append("**期望路径**:")
        for p in case['expected_paths']:
            lines.append(f"- `{p}`")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    lines.append("## 2. 增强后图谱 MISS分析")
    lines.append("")
    lines.append(f"共 {len(after_miss)} 条未命中查询：")
    lines.append("")
    
    for case in after_miss:
        lines.append(f"### Q{case['id']} [{case['category']}]")
        lines.append("")
        lines.append(f"**原始查询**: `{case['original_query']}`")
        lines.append("")
        kw = case['keywords']
        lines.append("**关键词配置**:")
        lines.append(f"- Core(EN): {', '.join(kw['core_en']) if kw['core_en'] else '(空)'}")
        lines.append(f"- Core(ZH): {', '.join(kw['core_zh']) if kw['core_zh'] else '(空)'}")
        lines.append(f"- Context(EN): {', '.join(kw['context_en']) if kw['context_en'] else '(空)'}")
        lines.append(f"- Context(ZH): {', '.join(kw['context_zh']) if kw['context_zh'] else '(空)'}")
        lines.append(f"- Synonym(EN): {', '.join(kw['synonym_en']) if kw['synonym_en'] else '(空)'}")
        lines.append(f"- Synonym(ZH): {', '.join(kw['synonym_zh']) if kw['synonym_zh'] else '(空)'}")
        lines.append("")
        lines.append(f"**实际搜索词**: `{case['search_query']}`")
        lines.append("")
        lines.append("**Top 5 结果**:")
        lines.append("")
        lines.append("| Rank | Label | Source File | Score | Match Type |")
        lines.append("|------|-------|-------------|-------|------------|")
        for i, r in enumerate(case['top5_results'], 1):
            lines.append(f"| {i} | {r['label'][:40]} | `{r['source_file'][:60]}` | {r['score']} | {r['match_type']} |")
        lines.append("")
        lines.append("**期望路径**:")
        for p in case['expected_paths']:
            lines.append(f"- `{p}`")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    # 新增：对比分析
    lines.append("## 3. MISS对比分析")
    lines.append("")
    
    before_ids = {c['id'] for c in before_miss}
    after_ids = {c['id'] for c in after_miss}
    
    new_miss = after_ids - before_ids  # 增强后新增的MISS
    fixed_miss = before_ids - after_ids  # 增强后修复的MISS
    still_miss = before_ids & after_ids  # 仍然MISS
    
    lines.append(f"- 增强前MISS: {len(before_ids)} 条")
    lines.append(f"- 增强后MISS: {len(after_ids)} 条")
    lines.append(f"- 新增MISS: {len(new_miss)} 条 (增强前命中，增强后失败)")
    lines.append(f"- 修复MISS: {len(fixed_miss)} 条 (增强前失败，增强后命中)")
    lines.append(f"- 仍MISS: {len(still_miss)} 条 (前后都失败)")
    lines.append("")
    
    if new_miss:
        lines.append("### 3.1 新增MISS (增强导致)")
        lines.append("")
        for case in after_miss:
            if case['id'] in new_miss:
                lines.append(f"- **Q{case['id']}** [{case['category']}]: `{case['original_query']}`")
                lines.append(f"  - Top1: `{case['top5_results'][0]['source_file'][:50]}` (Score: {case['top5_results'][0]['score']})")
                lines.append(f"  - Expected: `{case['expected_paths'][0] if case['expected_paths'] else 'N/A'}`")
        lines.append("")
    
    if fixed_miss:
        lines.append("### 3.2 修复MISS (增强改善)")
        lines.append("")
        for case in before_miss:
            if case['id'] in fixed_miss:
                lines.append(f"- **Q{case['id']}** [{case['category']}]: `{case['original_query']}`")
        lines.append("")
    
    return "\n".join(lines)

def main():
    keywords = load_keywords()
    queries = load_queries()
    print(f"Loaded {len(queries)} queries")
    
    before_miss = run_detailed_analysis(
        BEFORE_GRAPH, 
        PROJECT_ROOT / "data" / "before_llm", 
        queries, keywords
    )
    
    after_miss = run_detailed_analysis(
        AFTER_GRAPH, 
        PROJECT_ROOT / "data" / "doc", 
        queries, keywords
    )
    
    report = generate_report(before_miss, after_miss)
    
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"Report saved to: {REPORT_PATH}")
    print(f"Before MISS: {len(before_miss)}")
    print(f"After MISS: {len(after_miss)}")

if __name__ == "__main__":
    main()