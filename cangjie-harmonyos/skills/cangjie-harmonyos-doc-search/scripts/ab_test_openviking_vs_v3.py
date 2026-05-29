#!/usr/bin/env python3
"""OpenViking 远端检索与 V3 本地索引 AB 评测工具。"""

from __future__ import annotations

import argparse
import json
import random
import socket
import statistics
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
EVALS_DIR = SKILL_DIR / "evals"
DEFAULT_A_HOST = "111.229.30.227"
DEFAULT_A_PORT = 2026
DEFAULT_A_BACKENDS = ("cangjie-1.0.5", "harmonyos-6.1.0.818")
DEFAULT_KEY_REGRESSIONS = (
    "Web 的 loadUrl 方法",
    "loadUrl headers 怎么传",
    "WebView 加载网页",
    "Web 组件加载本地 rawfile",
    "设置 User-Agent 后加载页面",
)
USER_EVAL_KEYS = ("acceptable_paths", "must_contain", "intent")
EVAL_DIMENSION_KEYS = ("category", "card_type", "capability", "query_style", "difficulty")
PATH_PREFIXES = (
    "viking://resources/",
    "resources/",
)
SEGMENT_ALIASES = {
    "application-dev": "harmonyos-6.1-8k",
    "harmonyos-6.1.0.818": "harmonyos-6.1-8k",
    "harmonyos-6.1": "harmonyos-6.1-8k",
    "libs_stdx": "stdx",
}
OVERVIEW_SUFFIXES = ("/.abstract", "/.overview", "/README", "/index")


def utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        fn = getattr(stream, "reconfigure", None)
        if callable(fn):
            fn(encoding="utf-8", errors="replace")


def load_eval_set(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def stratified_sample(rows: list[dict], sample_size: int, seed: int) -> list[dict]:
    if sample_size <= 0 or len(rows) <= sample_size:
        return rows

    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in rows:
        groups[(row.get("card_type", "unknown"), row.get("category", "unknown"))].append(row)

    rng = random.Random(seed)
    for group_rows in groups.values():
        rng.shuffle(group_rows)

    picked: list[dict] = []
    group_keys = sorted(groups)
    while len(picked) < sample_size:
        progressed = False
        for key in group_keys:
            if groups[key]:
                picked.append(groups[key].pop())
                progressed = True
                if len(picked) >= sample_size:
                    break
        if not progressed:
            break
    return picked


def normalize_path(path: str) -> str:
    value = urllib.parse.unquote(str(path or "")).replace("\\", "/").strip()
    for prefix in PATH_PREFIXES:
        if value.startswith(prefix):
            value = value[len(prefix):]
            break
    value = value.split("#", 1)[0].split("?", 1)[0].strip("/")
    if value.endswith(".md"):
        value = value[:-3]
    parts = [SEGMENT_ALIASES.get(part, part) for part in value.split("/") if part]
    return "/".join(parts)


def comparable_paths(path: str) -> set[str]:
    base = normalize_path(path)
    variants = {base}
    for suffix in OVERVIEW_SUFFIXES:
        if base.endswith(suffix):
            variants.add(base[: -len(suffix)])
    return {item.strip("/") for item in variants if item}


def is_match(result: str, expected: str) -> bool:
    result_variants = comparable_paths(result)
    expected_variants = comparable_paths(expected)
    for result_item in result_variants:
        for expected_item in expected_variants:
            if result_item == expected_item:
                return True
            if result_item.startswith(f"{expected_item}/"):
                return True
            if expected_item.startswith(f"{result_item}/"):
                return True
    return False


def hit_rank(results: list[str], expected: list[str]) -> int | None:
    for index, result in enumerate(results, start=1):
        if any(is_match(result, item) for item in expected):
            return index
    return None


def recall_at_k(results: list[str], expected: list[str], k: int) -> float:
    if not expected:
        return 0.0
    top_k = results[:k]
    hits = sum(1 for item in expected if any(is_match(result, item) for result in top_k))
    return hits / len(expected)


def reciprocal_rank(rank: int | None) -> float:
    return 0.0 if rank is None else 1.0 / rank


@dataclass
class SearchOutcome:
    returned: list[dict]
    latency_ms: float
    error: str = ""
    timeout: bool = False


def search_hit(path: str, title: str = "", text: str = "") -> dict:
    return {
        "path": normalize_path(path),
        "title": str(title or ""),
        "text": str(text or ""),
    }


def normalize_hits(rows: list[dict | str]) -> list[dict]:
    hits: list[dict] = []
    for row in rows:
        if isinstance(row, str):
            hits.append(search_hit(row))
        elif isinstance(row, dict):
            hits.append(
                search_hit(
                    row.get("path") or row.get("uri") or row.get("resource") or row.get("source") or row.get("id") or "",
                    row.get("title") or row.get("name") or "",
                    row.get("text") or row.get("summary") or row.get("content") or "",
                )
            )
    return [hit for hit in hits if hit["path"]]


def returned_paths(rows: list[dict]) -> list[str]:
    return [row["path"] for row in rows]


def is_user_eval(rows: list[dict]) -> bool:
    return any(any(key in row for key in USER_EVAL_KEYS) for row in rows)


def timed_search(fn: Callable[[str, int], list[dict | str]], query: str, limit: int) -> SearchOutcome:
    start = time.perf_counter()
    try:
        returned = normalize_hits(fn(query, limit))
        return SearchOutcome(returned=returned, latency_ms=(time.perf_counter() - start) * 1000)
    except (TimeoutError, socket.timeout) as exc:
        return SearchOutcome(
            returned=[],
            latency_ms=(time.perf_counter() - start) * 1000,
            error=f"{type(exc).__name__}: {exc}",
            timeout=True,
        )
    except urllib.error.URLError as exc:
        timed_out = isinstance(getattr(exc, "reason", None), socket.timeout)
        return SearchOutcome(
            returned=[],
            latency_ms=(time.perf_counter() - start) * 1000,
            error=f"{type(exc).__name__}: {exc}",
            timeout=timed_out,
        )
    except Exception as exc:  # noqa: BLE001 - 评测工具需要记录单条失败而非中断全局。
        return SearchOutcome(
            returned=[],
            latency_ms=(time.perf_counter() - start) * 1000,
            error=f"{type(exc).__name__}: {exc}",
        )


def extract_openviking_path(row: dict) -> str:
    for key in ("uri", "path", "resource", "source", "id"):
        value = row.get(key)
        if isinstance(value, str) and value:
            return value
    return ""


def make_openviking_search(host: str, port: int, timeout: int, retries: int, backends: tuple[str, ...]):
    url = f"http://{host}:{port}/api/v1/search"

    def search(query: str, limit: int) -> list[dict]:
        payload = {"query": query, "limit": limit, "backends": list(backends)}
        encoded = json.dumps(payload).encode("utf-8")
        last_error: Exception | None = None
        for attempt in range(retries + 1):
            request = urllib.request.Request(
                url,
                data=encoded,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    data = json.loads(response.read().decode("utf-8"))
                if data.get("status") not in {None, "ok"}:
                    raise RuntimeError(str(data.get("error", "OpenViking 返回非 ok 状态")))
                rows = data.get("results", [])
                if not isinstance(rows, list):
                    raise RuntimeError("OpenViking results 不是列表")
                return [
                    search_hit(
                        extract_openviking_path(row),
                        row.get("title") or row.get("name") or "",
                        row.get("summary") or row.get("content") or row.get("text") or "",
                    )
                    for row in rows
                    if isinstance(row, dict)
                ]
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                if attempt >= retries:
                    raise
                time.sleep(min(0.5 * (attempt + 1), 2.0))
        raise RuntimeError(str(last_error))

    return search


def make_v3_search(index_dir: Path, mode: str, understanding_mode: str):
    sys.path.insert(0, str(SKILL_DIR))
    from search_v3 import collect, load_index

    index = load_index(index_dir)

    def search(query: str, limit: int) -> list[dict]:
        result = collect(index, query, mode, limit, understanding_mode=understanding_mode)
        hits_by_path: dict[str, dict] = {}
        for section in ("tasks", "apis", "examples", "docs"):
            for item in result.get(section, []):
                title = item.get("title", "")
                text = " ".join(str(value) for value in (title, item.get("summary", "")) if value)
                for path in item.get("paths", []):
                    normalized = normalize_path(path)
                    if normalized in hits_by_path:
                        hit = hits_by_path[normalized]
                        hit["title"] = hit["title"] or title
                        hit["text"] = " ".join(dict.fromkeys(part for part in (hit["text"], text) if part))
                    else:
                        hits_by_path[normalized] = search_hit(normalized, title, text)
        hits: list[dict] = []
        for path in result["paths"]:
            normalized = normalize_path(path)
            hits.append(hits_by_path.get(normalized, search_hit(normalized)))
        return hits

    return search


def hit_text(hit: dict) -> str:
    if hit.get("title") or hit.get("text"):
        return " ".join(str(hit.get(key, "")) for key in ("path", "title", "text")).lower()
    return str(hit.get("path", "")).lower()


def must_contain_match(hit: dict, must_contain: list[str]) -> bool:
    haystack = hit_text(hit)
    return all(str(token).lower() in haystack for token in must_contain)


def user_hit_rank(results: list[dict], acceptable: list[str], must_contain: list[str]) -> tuple[int | None, str, str]:
    path_matched = False
    for index, result in enumerate(results, start=1):
        if not any(is_match(result["path"], item) for item in acceptable):
            continue
        path_matched = True
        if must_contain and not must_contain_match(result, must_contain):
            continue
        return index, result["path"], ""
    if path_matched:
        return None, "", "must_contain_not_found"
    return None, "", "path_not_found"


def eval_group(name: str, fn: Callable[[str, int], list[dict | str]], rows: list[dict], limit: int) -> list[dict]:
    details = []
    for row in rows:
        outcome = timed_search(fn, row["query"], limit)
        base = {
            "group": name,
            "query": row["query"],
            "category": row.get("category", "unknown"),
            "card_type": row.get("card_type", "unknown"),
            "capability": row.get("capability", "unknown"),
            "query_style": row.get("query_style", "unknown"),
            "difficulty": row.get("difficulty", "unknown"),
            "source": row.get("source", "unknown"),
            "returned": returned_paths(outcome.returned[:limit]),
            "latency_ms": round(outcome.latency_ms, 2),
            "timeout": outcome.timeout,
            "error": outcome.error,
        }
        acceptable = row.get("acceptable_paths")
        if acceptable is not None:
            must_contain = row.get("must_contain", [])
            rank, matched_path, failed_reason = user_hit_rank(outcome.returned, acceptable, must_contain)
            if outcome.error:
                failed_reason = "search_error"
            details.append(
                {
                    **base,
                    "intent": row.get("intent", ""),
                    "acceptable_paths": acceptable,
                    "must_contain": must_contain,
                    "hit_rank": rank,
                    "matched_path": matched_path,
                    "failed_reason": "" if rank else failed_reason,
                    "success@1": 1.0 if rank and rank <= 1 else 0.0,
                    "success@5": 1.0 if rank and rank <= 5 else 0.0,
                    "success@10": 1.0 if rank and rank <= 10 else 0.0,
                    "mrr": round(reciprocal_rank(rank), 4),
                }
            )
            continue

        expected = row.get("expected_paths", [])
        paths = returned_paths(outcome.returned)
        rank = hit_rank(paths, expected)
        details.append(
            {
                **base,
                "expected": expected,
                "hit_rank": rank,
                "recall@1": round(recall_at_k(paths, expected, 1), 4),
                "recall@5": round(recall_at_k(paths, expected, 5), 4),
                "recall@10": round(recall_at_k(paths, expected, 10), 4),
                "mrr": round(reciprocal_rank(rank), 4),
            }
        )
    return details


def percentile(sorted_values: list[float], ratio: float) -> float:
    if not sorted_values:
        return 0.0
    index = min(len(sorted_values) - 1, int(len(sorted_values) * ratio))
    return sorted_values[index]


def aggregate(rows: list[dict]) -> dict:
    latencies = sorted(row["latency_ms"] for row in rows)
    count = len(rows)
    errors = [row for row in rows if row["error"]]
    timeouts = [row for row in rows if row["timeout"]]
    data = {
        "count": count,
        "mrr": round(statistics.mean(row["mrr"] for row in rows), 4) if rows else 0.0,
        "latency_p50_ms": round(statistics.median(latencies), 2) if latencies else 0.0,
        "latency_p95_ms": round(percentile(latencies, 0.95), 2),
        "error_rate": round(len(errors) / count, 4) if count else 0.0,
        "timeout_rate": round(len(timeouts) / count, 4) if count else 0.0,
    }
    if rows and "success@1" in rows[0]:
        data.update(
            {
                "success@1": round(statistics.mean(row["success@1"] for row in rows), 4),
                "success@5": round(statistics.mean(row["success@5"] for row in rows), 4),
                "success@10": round(statistics.mean(row["success@10"] for row in rows), 4),
            }
        )
    else:
        data.update(
            {
                "recall@1": round(statistics.mean(row["recall@1"] for row in rows), 4) if rows else 0.0,
                "recall@5": round(statistics.mean(row["recall@5"] for row in rows), 4) if rows else 0.0,
                "recall@10": round(statistics.mean(row["recall@10"] for row in rows), 4) if rows else 0.0,
            }
        )
    return data


def build_summary(details_by_group: dict[str, list[dict]]) -> dict:
    summary: dict[str, dict] = {"groups": {}}
    for group, rows in details_by_group.items():
        grouped_by_dimension: dict[str, dict[str, list[dict]]] = {
            key: defaultdict(list) for key in EVAL_DIMENSION_KEYS
        }
        for row in rows:
            for key in EVAL_DIMENSION_KEYS:
                grouped_by_dimension[key][row.get(key, "unknown")].append(row)
        group_summary = {"overall": aggregate(rows)}
        for key, values in grouped_by_dimension.items():
            group_summary[f"by_{key}"] = {
                value_key: aggregate(value_rows)
                for value_key, value_rows in sorted(values.items())
            }
        summary["groups"][group] = group_summary
    return summary


def row_map(rows: list[dict]) -> dict[str, dict]:
    return {row["query"]: row for row in rows}


def compare_rows(left: dict | None, right: dict | None) -> float:
    if not left or not right:
        return 0.0
    metric = "success@5" if "success@5" in right else "recall@5"
    return (right["mrr"] - left["mrr"]) + (right[metric] - left[metric])


def render_table(rows: list[tuple[str, dict | None, dict | None]], left_name: str, right_name: str) -> list[str]:
    lines = [f"| Query | {left_name} Top | {right_name} Top | {left_name} MRR | {right_name} MRR |", "| --- | ---: | ---: | ---: | ---: |"]
    for query, left, right in rows:
        left_rank = left.get("hit_rank") if left else None
        right_rank = right.get("hit_rank") if right else None
        lines.append(
            f"| {query} | {left_rank or '-'} | {right_rank or '-'} | "
            f"{left.get('mrr', 0.0) if left else 0.0} | {right.get('mrr', 0.0) if right else 0.0} |"
        )
    return lines


def build_diff_md(summary: dict, details_by_group: dict[str, list[dict]], key_regressions: tuple[str, ...]) -> str:
    eval_kind = summary.get("eval_kind", "path-recall")
    metric_labels = ("Success@1", "Success@5", "Success@10") if eval_kind == "user-search" else ("Recall@1", "Recall@5", "Recall@10")
    metric_keys = ("success@1", "success@5", "success@10") if eval_kind == "user-search" else ("recall@1", "recall@5", "recall@10")
    lines = [
        "# OpenViking vs V3 AB 测试报告",
        "",
        f"生成时间: {datetime.now(timezone.utc).isoformat()}",
        f"评测类型: {eval_kind}",
        "",
        "## 总览",
        "",
        f"| Group | Count | {metric_labels[0]} | {metric_labels[1]} | {metric_labels[2]} | MRR | P50(ms) | P95(ms) | Error | Timeout |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for group, data in summary["groups"].items():
        overall = data["overall"]
        lines.append(
            f"| {group} | {overall['count']} | {overall[metric_keys[0]]} | {overall[metric_keys[1]]} | "
            f"{overall[metric_keys[2]]} | {overall['mrr']} | {overall['latency_p50_ms']} | "
            f"{overall['latency_p95_ms']} | {overall['error_rate']} | {overall['timeout_rate']} |"
        )

    if "A" in details_by_group and "B" in details_by_group:
        a_rows = row_map(details_by_group["A"])
        b_rows = row_map(details_by_group["B"])
        comparisons = [
            (query, a_rows.get(query), b_rows.get(query), compare_rows(a_rows.get(query), b_rows.get(query)))
            for query in b_rows
        ]
        b_better = sorted((item for item in comparisons if item[3] > 0.2), key=lambda item: item[3], reverse=True)[:20]
        a_better = sorted((item for item in comparisons if item[3] < -0.2), key=lambda item: item[3])[:20]
        both_miss = [
            (query, a_row, b_row)
            for query, a_row, b_row, _score in comparisons
            if a_row and b_row and a_row["mrr"] == 0 and b_row["mrr"] == 0
        ][:20]

        lines.extend(["", "## B 明显优于 A", ""])
        lines.extend(render_table([(q, a, b) for q, a, b, _ in b_better], "A", "B") if b_better else ["无"])
        lines.extend(["", "## A 明显优于 B", ""])
        lines.extend(render_table([(q, a, b) for q, a, b, _ in a_better], "A", "B") if a_better else ["无"])
        lines.extend(["", "## 双方都 Miss", ""])
        lines.extend(render_table(both_miss, "A", "B") if both_miss else ["无"])

    lines.extend(["", "## 关键回归用例", ""])
    for group in details_by_group:
        group_rows = row_map(details_by_group[group])
        selected = [(query, None, group_rows.get(query)) for query in key_regressions if query in group_rows]
        lines.extend([f"### {group}", ""])
        lines.extend(render_table(selected, "-", group) if selected else ["未在本次评测集中出现"])
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_outputs(output_dir: Path, summary: dict, details_by_group: dict[str, list[dict]], diff_md: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    with (output_dir / "details.jsonl").open("w", encoding="utf-8") as handle:
        for group in sorted(details_by_group):
            for row in details_by_group[group]:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    (output_dir / "diff.md").write_text(diff_md, encoding="utf-8")


def parse_backends(value: str) -> tuple[str, ...]:
    return tuple(item.strip() for item in value.split(",") if item.strip())


def build_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="OpenViking 远端检索与 V3 本地索引 AB 评测")
    parser.add_argument("--eval-set", default=str(EVALS_DIR / "search" / "eval_queries.jsonl"))
    parser.add_argument("--sample-size", type=int, default=0, help="按 card_type + category 分层抽样；0 表示全量")
    parser.add_argument("--sample-seed", type=int, default=20260422)
    parser.add_argument("--a-host", default=DEFAULT_A_HOST)
    parser.add_argument("--a-port", type=int, default=DEFAULT_A_PORT)
    parser.add_argument("--a-backends", default=",".join(DEFAULT_A_BACKENDS))
    parser.add_argument("--skip-a", action="store_true", help="只评测本地 V3，不触发 OpenViking 远端请求")
    parser.add_argument("--b-index-dir", default=str(SKILL_DIR / "index"))
    parser.add_argument("--b-mode", choices=("auto", "task", "api", "example", "doc"), default="auto")
    parser.add_argument("--b-understanding-mode", choices=("rule", "host-agent"), default="rule")
    parser.add_argument("--include-c", action="store_true", help="额外评测 C 组 V3 索引")
    parser.add_argument("--c-index-dir", default="")
    parser.add_argument("--c-mode", choices=("auto", "task", "api", "example", "doc"), default="auto")
    parser.add_argument("--c-understanding-mode", choices=("rule", "host-agent"), default="rule")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--output-dir", default=str(SCRIPT_DIR / "ab-results"))
    return parser.parse_args()


def main() -> None:
    utf8_stdio()
    args = build_args()

    eval_set = load_eval_set(Path(args.eval_set))
    eval_set = stratified_sample(eval_set, args.sample_size, args.sample_seed)

    details_by_group: dict[str, list[dict]] = {}
    if not args.skip_a:
        a_fn = make_openviking_search(
            args.a_host,
            args.a_port,
            args.timeout,
            args.retries,
            parse_backends(args.a_backends),
        )
        details_by_group["A"] = eval_group("A", a_fn, eval_set, args.limit)

    b_fn = make_v3_search(Path(args.b_index_dir), args.b_mode, args.b_understanding_mode)
    details_by_group["B"] = eval_group("B", b_fn, eval_set, args.limit)

    if args.include_c:
        c_index_dir = Path(args.c_index_dir) if args.c_index_dir else Path(args.b_index_dir)
        c_fn = make_v3_search(c_index_dir, args.c_mode, args.c_understanding_mode)
        details_by_group["C"] = eval_group("C", c_fn, eval_set, args.limit)

    summary = build_summary(details_by_group)
    summary["eval_kind"] = "user-search" if is_user_eval(eval_set) else "path-recall"
    summary["config"] = {
        "eval_set": str(Path(args.eval_set)),
        "sample_size": args.sample_size,
        "sample_seed": args.sample_seed,
        "limit": args.limit,
        "a": None if args.skip_a else {"host": args.a_host, "port": args.a_port, "backends": parse_backends(args.a_backends)},
        "b": {"index_dir": args.b_index_dir, "mode": args.b_mode, "understanding_mode": args.b_understanding_mode},
        "c": None
        if not args.include_c
        else {
            "index_dir": args.c_index_dir or args.b_index_dir,
            "mode": args.c_mode,
            "understanding_mode": args.c_understanding_mode,
        },
    }
    diff_md = build_diff_md(summary, details_by_group, DEFAULT_KEY_REGRESSIONS)
    write_outputs(Path(args.output_dir), summary, details_by_group, diff_md)

    print(json.dumps(summary["groups"], ensure_ascii=False, indent=2))
    print(f"\n报告已写入: {Path(args.output_dir).resolve()}")


if __name__ == "__main__":
    main()
