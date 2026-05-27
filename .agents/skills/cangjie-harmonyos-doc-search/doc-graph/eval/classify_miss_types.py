"""Analyze MISS types - distinguish real misses from more_specific hits."""
import json
from pathlib import Path
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from query import create_session

KEYWORDS_PATH = PROJECT_ROOT / "eval" / "keywords_v7_prompt.json"
JSONL_PATH = PROJECT_ROOT / "eval" / "datasets" / "eval_queries_comprehensive_deduped.jsonl"
GRAPH_PATH = PROJECT_ROOT / "data" / "doc" / "graph.json"
REPORT_PATH = PROJECT_ROOT / "eval" / "miss_type_analysis.md"

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

def analyze_miss_type(top_path, expected_paths, all_top5_paths):
    """Analyze MISS type - is it truly wrong or just more specific?"""
    if not expected_paths:
        return "unknown", "无期望路径"
    
    expected = expected_paths[0]
    expected_base = expected.replace(".overview.md", "").replace(".md", "").rstrip("/")
    
    for p in all_top5_paths:
        p_base = p.replace(".overview.md", "").replace("_2more.md", "").replace("_3more.md", "").rstrip("/")
        if expected_base in p_base or p_base in expected_base:
            if p != expected:
                if ".overview.md" in expected and ".overview.md" not in p:
                    return "more_specific", f"命中了更具体的子文档而非overview"
                else:
                    return "sibling_doc", f"命中了同namespace下的兄弟文档"
    
    top_ns = top_path.split("\\")[0] if "\\" in top_path else top_path.split("/")[0]
    exp_ns = expected.split("\\")[0] if "\\" in expected else expected.split("/")[0]
    
    if top_ns == exp_ns:
        return "same_namespace", "命中了同一namespace但不同文档"
    
    exp_keywords = expected_base.replace("cj-", "").split("-")
    top_lower = top_path.lower()
    matched_kw = [kw for kw in exp_keywords if kw in top_lower and len(kw) > 2]
    
    if len(matched_kw) >= 2:
        return "partial_match", "路径部分匹配但namespace不同"
    
    return "wrong_result", "完全错误的文档"

def main():
    keywords = load_keywords()
    queries = load_queries()
    print(f"Loaded {len(queries)} queries")
    
    session = create_session(graph_dir=str(PROJECT_ROOT / "data" / "doc"))
    session.doc_engine = None
    session.load_doc_graph(str(GRAPH_PATH))
    
    miss_cases = []
    
    for idx, q in enumerate(queries):
        q_id = idx + 1
        kw = keywords.get(str(q_id), {})
        
        keywords_en = kw.get("keywords_en", [])
        keywords_zh = kw.get("keywords_zh", [])
        search_q = " ".join(keywords_en + keywords_zh)
        
        result = session.search(search_q, top_k=5, graph="doc")
        
        status = check_hit_status(result, q.get("acceptable_paths", []))
        
        if status == "MISS":
            top5_paths = [h.source_file for h in result.direct_hits]
            top_path = top5_paths[0] if top5_paths else ""
            expected_paths = q.get("acceptable_paths", [])
            
            miss_type, miss_reason = analyze_miss_type(top_path, expected_paths, top5_paths)
            
            miss_cases.append({
                "id": q_id,
                "query": q.get("query", ""),
                "category": q.get("category", ""),
                "top_path": top_path,
                "expected": expected_paths[0] if expected_paths else "",
                "miss_type": miss_type,
                "miss_reason": miss_reason,
                "top5_paths": top5_paths,
                "top5_scores": [round(h.score, 1) for h in result.direct_hits]
            })
    
    type_counts = {}
    for m in miss_cases:
        t = m["miss_type"]
        type_counts[t] = type_counts.get(t, 0) + 1
    
    print("\n=== MISS类型分析 ===")
    print(f"总MISS数: {len(miss_cases)}")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c} ({c/len(miss_cases)*100:.1f}%)")
    
    lines = ["# MISS类型分析报告", "", "## 1. MISS类型统计", ""]
    lines.append(f"总MISS数: **{len(miss_cases)}** 条")
    lines.append("")
    lines.append("| 类型 | 数量 | 占比 | 说明 |")
    lines.append("|------|-----:|-----:|------|")
    
    type_desc = {
        "more_specific": "命中了更具体的子文档(如_2more.md)，而非overview",
        "sibling_doc": "命中了同namespace下的兄弟文档",
        "same_namespace": "命中了同一namespace但路径不匹配",
        "partial_match": "路径部分关键词匹配但namespace不同",
        "wrong_result": "完全错误的文档",
        "unknown": "无期望路径"
    }
    
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        lines.append(f"| {t} | {c} | {c/len(miss_cases)*100:.1f}% | {type_desc.get(t, '')} |")
    
    lines.append("")
    lines.append("## 2. 各类型详细案例")
    lines.append("")
    
    for miss_type in sorted(type_counts.keys(), key=lambda x: -type_counts[x]):
        cases = [m for m in miss_cases if m["miss_type"] == miss_type]
        lines.append(f"### 2.{list(type_counts.keys()).index(miss_type)+1} {miss_type} ({len(cases)}条)")
        lines.append("")
        
        for m in cases[:10]:
            lines.append(f"**Q{m['id']}** [{m['category']}]: `{m['query']}`")
            lines.append(f"- Top1: `{m['top_path']}` (Score: {m['top5_scores'][0]})")
            lines.append(f"- Expected: `{m['expected']}`")
            lines.append(f"- Reason: {m['miss_reason']}")
            if len(m['top5_paths']) > 1:
                lines.append(f"- Top5: `{m['top5_paths'][1][:50]}` ({m['top5_scores'][1]}), `{m['top5_paths'][2][:50]}` ({m['top5_scores'][2]})")
            lines.append("")
    
    real_miss = type_counts.get("wrong_result", 0) + type_counts.get("partial_match", 0)
    acceptable_miss = type_counts.get("more_specific", 0) + type_counts.get("sibling_doc", 0) + type_counts.get("same_namespace", 0)
    
    lines.append("## 3. 改进策略建议")
    lines.append("")
    lines.append(f"### 当前问题诊断")
    lines.append(f"- **真正MISS**: {real_miss}条 ({real_miss/len(miss_cases)*100:.1f}%) - 完全错误结果")
    lines.append(f"- **可接受MISS**: {acceptable_miss}条 ({acceptable_miss/len(miss_cases)*100:.1f}%) - 命中了相关但非预期的文档")
    lines.append("")
    
    lines.append("### 策略1: 优先返回overview文档")
    lines.append("对于`more_specific`类型，可以在搜索结果中优先展示`.overview.md`文档：")
    lines.append("- 打分时对overview文档额外加分（如+20%）")
    lines.append("- 或在结果排序时，overview优先排在同级分数的前面")
    lines.append("")
    
    lines.append("### 策略2: 扩展acceptable_paths匹配")
    lines.append("当前匹配逻辑是`ap in rp or rp in ap`，可以更宽松：")
    lines.append("- 对于`cj-animation-animateto`类的namespace，匹配所有子文档")
    lines.append("- 期望路径`cj-animation-animateto/.overview.md`应同时接受`cj-animation-animateto/*`")
    lines.append("")
    
    lines.append("### 策略3: 关键词精简优化")
    lines.append("v7关键词已精简至avg2.7词，但仍可进一步优化：")
    lines.append("- **去除过于通用的词**: 如仅含`API`、`component`等无区分度的词")
    lines.append("- **精确匹配加分**: 对label完全匹配的节点大幅加分")
    lines.append("")
    
    report = "\n".join(lines)
    
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"\nReport saved to: {REPORT_PATH}")

if __name__ == "__main__":
    main()