"""Unified search entry point for cangjie-harmonyos-doc-search.

Orchestrates card (doc-card/search_v3.py) and graph (doc-graph/cli.py)
engines, merges results into a unified SearchResult format.

Usage:
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
    node_id: str
    label: str
    source_file: str
    score: float
    match_type: str = ""
    related_from: str = ""
    relation_type: str = ""
    engine: str = ""

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


TOP_DIR = "harmonyos-6.0.2-15k"


def _strip_top_dir(path):
    for sep in ("\\", "/"):
        prefix = TOP_DIR + sep
        if path.startswith(prefix):
            return path[len(prefix):]
    return path


def _ensure_top_dir(path):
    path = path.replace("\\", "/")
    for sep in ("\\", "/"):
        if path.startswith(TOP_DIR + sep):
            return path
    return TOP_DIR + "/" + path


def extract_card_paths(card_result):
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
    p = Path(path)
    parts = []
    for part in p.parts:
        if part.startswith("harmonyos-6.0.2-15k") or part.startswith("lang-features") or part.startswith("std") or part.startswith("stdx") or part.startswith("tools"):
            parts = [part]
            continue
        parts.append(part)
    return str(Path(*parts)) if parts else str(p)


def fuse_results(query, card_result, graph_result, limit=5):
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