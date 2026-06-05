"""Unified search entry point — 统一搜索入口，编排 card 和 graph 双引擎。

本模块是 cangjie-harmonyos-doc-search Skill 的顶层入口，负责：
1. 调用 doc-card 引擎（search_v3.py）获取卡片搜索结果
2. 调用 doc-graph 引擎（cli.py）获取图谱搜索结果
3. 融合两引擎结果（fuse_results），去重并按引擎优先级排序

引擎优先级：card+graph（双引擎命中）> graph > card
融合策略：graph 直接命中取前3，关联取前2；card 结果补充不重叠的命中；
双引擎重叠时标记为 "card+graph"，优先级最高。

用法：
    python unified_search.py "List 列表" --json --limit 5
    python unified_search.py "List" --engine card --json
    python unified_search.py "卡顿" --engine graph --json
    python unified_search.py "" --engine graph --cmd neighbors List
    python unified_search.py "" --engine graph --cmd path UIAbility WindowStage
    python unified_search.py "" --engine graph --cmd god-nodes 10
"""

import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent
UTF8_ENV = {**os.environ, "PYTHONIOENCODING": "utf-8"}

CARD_DIR = SKILL_DIR / "doc-card"
GRAPH_DIR = SKILL_DIR / "doc-graph"


@dataclass
class Hit:
    """统一搜索命中项 — 跨引擎融合后的最小结果单元。

    engine 字段标识来源："card" / "graph" / "card+graph"（双引擎重叠命中）。
    """
    node_id: str
    label: str
    source_file: str
    score: float
    match_type: str = ""
    related_from: str = ""          # 关联推荐来源节点标签
    relation_type: str = ""         # 关联边类型（如 "see_also"）
    engine: str = ""                # 结果引擎来源：card / graph / card+graph

    def to_dict(self):
        d = {
            "label": self.label,
            "source_file": self.source_file.replace("\\", "/"),
            "engine": self.engine,
        }
        if self.score > 0:
            d["score"] = self.score
        if self.related_from:
            d["related_from"] = self.related_from
        if self.relation_type:
            d["relation_type"] = self.relation_type
        return d


@dataclass
class SearchResult:
    query: str
    engine: str
    direct_hits: list = field(default_factory=list)
    related_hits: list = field(default_factory=list)

    def to_dict(self):
        return {
            "query": self.query,
            "engine": self.engine,
            "direct_hits": [h.to_dict() for h in self.direct_hits],
            "related_hits": [h.to_dict() for h in self.related_hits],
        }

    def to_brief_text(self):
        lines = []
        if self.direct_hits:
            lines.append(f"=== 直接命中 ({len(self.direct_hits)}) ===")
            for h in self.direct_hits:
                score_str = f"[{h.score:.1f}] " if h.score > 0 else "[card] "
                engine_str = f"  [{h.engine}]" if h.engine else ""
                lines.append(f"{score_str}{h.label} | {h.source_file.replace(chr(92), '/')}{engine_str}")
        if self.related_hits:
            lines.append(f"\n=== 关联推荐 ({len(self.related_hits)}) ===")
            for h in self.related_hits:
                from_str = f" (来自 {h.related_from}, {h.relation_type})"
                lines.append(f"[{h.score:.1f}] {h.label} | {h.source_file.replace(chr(92), '/')}{from_str}")
        return "\n".join(lines)


def run_card(query, limit=5):
    """调用 doc-card 引擎（search_v3.py）获取卡片搜索结果。

    通过子进程执行，超时30秒。返回解析后的 JSON dict，失败返回 None。
    """
    script = CARD_DIR / "search_v3.py"
    cmd = [
        sys.executable, str(script),
        query, "--json", "--limit", str(limit),
    ]
    try:
        result = subprocess.run(
            cmd, capture_output=True, cwd=str(CARD_DIR), timeout=30,
            env=UTF8_ENV
        )
        if result.returncode != 0:
            return None
        stdout = result.stdout.decode("utf-8", errors="replace")
        return json.loads(stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        return None


def run_graph(query, limit=5, brief=True):
    """调用 doc-graph 引擎（cli.py）获取图谱搜索结果。

    通过子进程执行，超时30秒。解析 brief 格式输出文本，
    将 "直接命中" 和 "关联推荐" 两个分区分别解析为 Hit 列表。
    返回 {"direct": [...], "related": [...]} dict，失败返回 None。
    """
    script = GRAPH_DIR / "cli.py"
    args = [sys.executable, str(script), "search", query, "--graph", "doc", "-k", str(limit)]
    if brief:
        args.append("-b")
    try:
        result = subprocess.run(
            args, capture_output=True, cwd=str(GRAPH_DIR), timeout=30,
            env=UTF8_ENV
        )
        text = result.stdout.decode("utf-8", errors="replace")
        direct = []
        related = []
        section = None
        for line in text.splitlines():
            stripped = line.strip()
            if "直接命中" in stripped or "direct hit" in stripped.lower():
                section = "direct"
                continue
            if "关联推荐" in stripped or "related" in stripped.lower():
                section = "related"
                continue
            if stripped.startswith("查询") or stripped.startswith("图谱") or stripped.startswith("耗时"):
                continue
            if not stripped or stripped.startswith("==="):
                section = None
                continue
            if section == "direct":
                hit = parse_graph_brief_line(stripped)
                if hit:
                    direct.append(hit)
            elif section == "related":
                hit = parse_graph_related_line(stripped)
                if hit:
                    related.append(hit)
        return {"direct": direct, "related": related}
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None


def run_graph_cmd(cmd_name, *args):
    """调用 doc-graph CLI 的非搜索命令（neighbors/path/god-nodes 等）。

    直接透传子进程输出，不做解析。
    """
    script = GRAPH_DIR / "cli.py"
    full_args = [sys.executable, str(script), cmd_name] + list(args)
    try:
        result = subprocess.run(
            full_args, capture_output=True, cwd=str(GRAPH_DIR), timeout=30,
            env=UTF8_ENV
        )
        return result.stdout.decode("utf-8", errors="replace")
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return f"Error: graph command '{cmd_name}' failed"


def parse_graph_brief_line(line):
    """解析 graph 引擎 brief 格式的单行命中。

    格式示例："[85.0] List | harmonyos-6.0.2-15k/Guide/..."
    返回 Hit 对象，解析失败返回 None。
    """
    try:
        score_end = line.index("]")
        score = float(line[1:score_end])
        rest = line[score_end + 1:].strip()
        if "|" in rest:
            label, source_file = rest.split("|", 1)
            return Hit(
                node_id="", label=label.strip(), source_file=source_file.strip(),
                score=score, engine="graph"
            )
    except (ValueError, IndexError):
        pass
    return None


def parse_graph_related_line(line):
    """解析 graph 引擎 brief 格式的关联推荐行。

    格式示例："[42.5] ScrollView | path/to/doc (来自 List, see_also)"
    括号内的 "来自 X, 关系类型" 被提取到 related_from 和 relation_type。
    """
    from_match = ""
    relation = ""
    source_file_clean = ""
    if "(来自" in line:
        paren_start = line.index("(来自")
        paren_end = line.rindex(")")
        paren_content = line[paren_start + 3:paren_end]
        if "," in paren_content:
            from_match, relation = paren_content.split(",", 1)
            from_match = from_match.strip()
            relation = relation.strip()
        before_paren = line[:paren_start].rstrip()
        hit = parse_graph_brief_line(before_paren)
        if hit:
            hit.related_from = from_match
            hit.relation_type = relation
            return hit
    hit = parse_graph_brief_line(line)
    if hit:
        hit.related_from = from_match
        hit.relation_type = relation
    return hit


TOP_DIR = "harmonyos-6.0.2-15k"  # 文档仓库顶层目录名，用于路径规范化


def _strip_top_dir(path):
    """去掉 TOP_DIR 前缀 — 用于去重比较时忽略顶层目录差异。

    例如 "harmonyos-6.0.2-15k/API/std.List.md" → "API/std.List.md"
    """
    for sep in ("\\", "/"):
        prefix = TOP_DIR + sep
        if path.startswith(prefix):
            return path[len(prefix):]
    return path


def _ensure_top_dir(path):
    """确保路径包含 TOP_DIR 前缀 — 用于最终输出时统一路径格式。

    例如 "API/std.List.md" → "harmonyos-6.0.2-15k/API/std.List.md"
    如果路径已有 TOP_DIR 前缀则不重复添加。
    """
    path = path.replace("\\", "/")
    for sep in ("\\", "/"):
        if path.startswith(TOP_DIR + sep):
            return path
    return TOP_DIR + "/" + path


def extract_card_paths(card_result):
    """从 card 引擎结果中提取所有文件路径和标题映射。

    遍历 tasks/apis/examples/docs 四个分区，收集每个 item 的 paths 和 title。
    同时收集顶层的 paths 字段（可能有未被分区包含的路径）。
    返回 (paths列表, {path→title}映射)。
    """
    paths = []
    titles_by_path = {}
    if not card_result:
        return paths, titles_by_path
    for section in ("tasks", "apis", "examples", "docs"):
        for item in card_result.get(section, []):
            title = item.get("title", "")
            for p in item.get("paths", []):
                norm = normalize_source_file(p)
                paths.append(norm)
                titles_by_path.setdefault(norm, title)
    for p in card_result.get("paths", []):
        norm = normalize_source_file(p)
        if norm not in paths:
            paths.append(norm)
    return paths, titles_by_path


def normalize_source_file(path):
    """规范化源文件路径 — 去掉冗余的中间目录层级。

    当路径中遇到仓库根目录名（如 harmonyos-6.0.2-15k、lang-features、std 等）
    时，重置路径栈，只保留根目录名及其之后的路径段。
    这确保了不同层级来源的路径能统一比较和展示。
    """
    p = Path(path)
    parts = []
    for part in p.parts:
        if part.startswith("harmonyos-6.0.2-15k") or part.startswith("lang-features") or part.startswith("std") or part.startswith("stdx") or part.startswith("tools"):
            parts = [part]
            continue
        parts.append(part)
    return str(Path(*parts)) if parts else str(p)


def fuse_results(query, card_result, graph_result, limit=5):
    """融合 card 和 graph 双引擎搜索结果 — 核心编排逻辑。

    融合策略：
    1. graph 直接命中取前3，关联取前2（graph 结果语义相关性更强）
    2. card 结果补充与 graph 不重叠的命中（前3个），扩展覆盖面
    3. 重叠命中标记为 "card+graph"，优先级最高
    4. 最终按引擎优先级排序：card+graph(0) > graph(1) > card(2)
    5. 直接命中上限6个，关联上限2个
    6. 所有路径统一确保包含 TOP_DIR 前缀
    """
    result = SearchResult(query=query, engine="fusion")

    graph_direct = []
    if graph_result:
        graph_direct = graph_result.get("direct", [])[:3]
    for hit in graph_direct:
        hit.engine = "graph"
    result.direct_hits.extend(graph_direct)

    graph_related = []
    if graph_result:
        graph_related = graph_result.get("related", [])[:2]
    for hit in graph_related:
        hit.engine = "graph"
    result.related_hits.extend(graph_related)

    existing_norms = {_strip_top_dir(h.source_file) for h in result.direct_hits}
    card_paths, titles_by_path = extract_card_paths(card_result)

    for p in card_paths[:3]:
        norm_p = _strip_top_dir(p)
        if norm_p not in existing_norms:
            result.direct_hits.append(Hit(
                node_id="", label=titles_by_path.get(p, p), source_file=p,
                score=0, match_type="v3_card", engine="card"
            ))
            existing_norms.add(norm_p)
        else:
            for h in result.direct_hits:
                if _strip_top_dir(h.source_file) == norm_p and h.engine == "graph":
                    h.engine = "card+graph"
                    h.label = titles_by_path.get(p, h.label)
                    h.source_file = p
                    break

    result.direct_hits.sort(key=sort_hit_key)

    if len(result.direct_hits) > 6:
        result.direct_hits = result.direct_hits[:6]
    if len(result.related_hits) > 2:
        result.related_hits = result.related_hits[:2]

    for h in result.direct_hits:
        h.source_file = _ensure_top_dir(h.source_file)
    for h in result.related_hits:
        h.source_file = _ensure_top_dir(h.source_file)

    return result


def sort_hit_key(hit):
    """排序键 — 引擎优先级为主键，分数为副键（降序）。

    引擎优先级：card+graph(0) > graph(1) > card(2) > 其他(3)
    同引擎内按分数从高到低排列。
    """
    engine_order = {"card+graph": 0, "graph": 1, "card": 2}
    return (engine_order.get(hit.engine, 3), -hit.score)


def utf8_stdio():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")


def main():
    utf8_stdio()
    parser = argparse.ArgumentParser(description="Unified doc search for HarmonyOS Cangjie")
    parser.add_argument("query", nargs="?", default="", help="Search query")
    parser.add_argument("--engine", choices=("fusion", "card", "graph"), default="fusion")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--cmd", choices=("neighbors", "path", "god-nodes", "community", "explain"), default=None)
    parser.add_argument("cmd_args", nargs="*", help="Arguments for --cmd")

    args = parser.parse_args()

    if args.engine == "graph" and args.cmd:
        output = run_graph_cmd(args.cmd, *args.cmd_args)
        print(output)
        return

    if not args.query:
        print("Error: query is required for search (use --cmd for graph traversal)", file=sys.stderr)
        sys.exit(1)

    if args.engine == "card":
        card_result = run_card(args.query, args.limit)
        if card_result:
            card_paths, titles_by_path = extract_card_paths(card_result)
            hits = []
            for p in card_paths[:args.limit]:
                hits.append(Hit(
                    node_id="", label=titles_by_path.get(p, p), source_file=p,
                    score=0, match_type="v3_card", engine="card"
                ))
            result = SearchResult(query=args.query, engine="card", direct_hits=hits)
        else:
            result = SearchResult(query=args.query, engine="card")
        if args.json:
            print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
        else:
            print(result.to_brief_text())
        return

    if args.engine == "graph":
        graph_result = run_graph(args.query, args.limit)
        if graph_result:
            direct = graph_result.get("direct", [])
            related = graph_result.get("related", [])
            for h in direct:
                h.engine = "graph"
            for h in related:
                h.engine = "graph"
            result = SearchResult(
                query=args.query, engine="graph",
                direct_hits=direct[:args.limit],
                related_hits=related[:args.limit]
            )
        else:
            result = SearchResult(query=args.query, engine="graph")
        if args.json:
            print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
        else:
            print(result.to_brief_text())
        return

    card_result = run_card(args.query, args.limit)
    graph_result = run_graph(args.query, args.limit)
    result = fuse_results(args.query, card_result, graph_result, args.limit)

    if args.json:
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(result.to_brief_text())


if __name__ == "__main__":
    main()