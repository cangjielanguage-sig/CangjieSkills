#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
import time
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_ROOT = SKILL_ROOT / "scripts"
DEFAULT_CASES = SKILL_ROOT / "tests" / "cases" / "retrieval.json"

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_ROOT))

from knowledge_core.config import apply_embedding_mode, load_config  # noqa: E402
from knowledge_core.embedding import EmbeddingUnavailable  # noqa: E402
from knowledge_core.search import Searcher  # noqa: E402
from knowledge_core.util import configure_stdio  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate packaged Cangjie HarmonyOS retrieval quality.")
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--index-dir", type=Path, help="Override the packaged index directory.")
    parser.add_argument(
        "--embedding-mode",
        choices=("off", "search", "vector"),
        default="off",
        help="Use deterministic, adaptive, or pure-vector retrieval.",
    )
    parser.add_argument("--embedding-dimensions", type=int, help="Request this embedding dimension for queries.")
    parser.add_argument("--fail-under", type=float, default=1.0, help="Minimum case pass rate in the range 0..1.")
    parser.add_argument(
        "--max-p95-ms",
        type=float,
        help="Fail when measured p95 case latency exceeds this regression limit.",
    )
    parser.add_argument(
        "--require-embeddings",
        action="store_true",
        help="Fail unless a query embedding provider is configured and available.",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON only.")
    return parser.parse_args()


def load_cases(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, list) or not data:
        raise ValueError(f"Evaluation cases must be a non-empty JSON array: {path}")
    return data


def result_text(results: list[dict[str, Any]]) -> str:
    fields: list[str] = []
    for result in results:
        fields.extend(
            str(result.get(key) or "")
            for key in ("ref", "title", "breadcrumb", "snippet")
        )
        for symbol in result.get("symbols") or []:
            fields.extend(str(symbol.get(key) or "") for key in ("name", "signature"))
    return "\n".join(fields).lower()


def first_relevant_rank(results: list[dict[str, Any]], expected: list[str]) -> int | None:
    if not expected:
        return 1 if results else None
    for rank, result in enumerate(results, 1):
        if any(token in result_text([result]) for token in expected):
            return rank
    return None


def evaluate_case(searcher: Searcher, case: dict[str, Any], embedding_mode: str) -> dict[str, Any]:
    started = time.perf_counter()
    search = searcher.vector_search if embedding_mode == "vector" else searcher.search
    kwargs = {
        "top_k": max(1, int(case.get("top_k", 5))),
        "scope": str(case.get("scope", "all")),
    }
    if embedding_mode != "vector":
        kwargs["embedding_mode"] = embedding_mode
    results = search(str(case["query"]), **kwargs)
    haystack = result_text(results)
    expect_any = [str(item).lower() for item in case.get("expect_any", [])]
    expect_all = [str(item).lower() for item in case.get("expect_all", [])]
    expect_empty = bool(case.get("expect_empty", False))
    any_ok = not expect_any or any(token in haystack for token in expect_any)
    all_ok = all(token in haystack for token in expect_all)
    rank = first_relevant_rank(results, expect_any or expect_all)
    max_rank = max(1, int(case.get("max_rank", case.get("top_k", 5))))
    passed = (not results) if expect_empty else bool(results) and any_ok and all_ok and bool(rank and rank <= max_rank)
    return {
        "id": str(case.get("id") or case["query"]),
        "query": str(case["query"]),
        "passed": passed,
        "elapsed_ms": round((time.perf_counter() - started) * 1000, 2),
        "first_relevant_rank": rank,
        "max_rank": max_rank,
        "expected_any": expect_any,
        "expected_all": expect_all,
        "top_refs": [str(item.get("ref") or "") for item in results[:3]],
    }


def main() -> int:
    configure_stdio()
    args = parse_args()
    if not 0.0 <= args.fail_under <= 1.0:
        raise ValueError("fail-under must be between 0 and 1")
    if args.max_p95_ms is not None and args.max_p95_ms <= 0:
        raise ValueError("max-p95-ms must be > 0")
    if args.require_embeddings and args.embedding_mode == "off":
        raise ValueError("require-embeddings requires --embedding-mode search or vector")
    cases = load_cases(args.cases.resolve())
    cfg = apply_embedding_mode(load_config(), "search" if args.embedding_mode == "vector" else args.embedding_mode)
    if args.index_dir:
        cfg.index_dir = str(args.index_dir.resolve())
    if args.embedding_dimensions:
        if args.embedding_dimensions <= 0:
            raise ValueError("embedding dimensions must be > 0")
        cfg.embedding.dimensions = args.embedding_dimensions
    embedding_probe_error = None
    with Searcher(cfg) as searcher:
        embeddings_available = searcher.embedding.available
        if args.require_embeddings:
            if not embeddings_available:
                embedding_probe_error = "provider-not-configured"
            else:
                try:
                    # A configured key is not proof that the provider is usable.
                    # Validate one bounded request so bad credentials, endpoints,
                    # dimensions, and malformed responses cannot pass the gate via
                    # deterministic fallback.
                    searcher.embedding.embed_query("HarmonyOS API retrieval quality gate")
                except EmbeddingUnavailable as exc:
                    embeddings_available = False
                    embedding_probe_error = type(exc).__name__
        results = [evaluate_case(searcher, case, args.embedding_mode) for case in cases]
        embedding_requests = searcher.embedding.request_count
        embedding_input_tokens = searcher.embedding.input_tokens

    passed = sum(1 for item in results if item["passed"])
    score = passed / len(results)
    cases_by_id = {str(case.get("id") or case["query"]): case for case in cases}
    ranked = [item for item in results if not cases_by_id[item["id"]].get("expect_empty")]
    reciprocal_ranks = [1.0 / item["first_relevant_rank"] if item["first_relevant_rank"] else 0.0 for item in ranked]
    ndcg_values = [
        1.0 / math.log2(item["first_relevant_rank"] + 1) if item["first_relevant_rank"] else 0.0
        for item in ranked
    ]
    elapsed = sorted(float(item["elapsed_ms"]) for item in results)
    p95_index = min(len(elapsed) - 1, max(0, math.ceil(len(elapsed) * 0.95) - 1))
    latency_p95_ms = round(elapsed[p95_index], 2)
    score_passed = score >= args.fail_under
    latency_passed = args.max_p95_ms is None or latency_p95_ms <= args.max_p95_ms
    embeddings_passed = not args.require_embeddings or embeddings_available
    if args.embedding_mode == "off":
        effective_profile = "offline-deterministic"
    elif embeddings_available:
        effective_profile = "online-vector" if args.embedding_mode == "vector" else "online-adaptive"
    else:
        effective_profile = "offline-deterministic-fallback"
    report = {
        "mode": args.embedding_mode,
        "effective_profile": effective_profile,
        "index_dir": str(Path(cfg.index_dir).resolve()),
        "embedding_dimensions": cfg.embedding.dimensions,
        "embeddings_available": embeddings_available,
        "embedding_probe_error": embedding_probe_error,
        "embedding_requests": embedding_requests,
        "embedding_input_tokens": embedding_input_tokens,
        "passed": passed,
        "total": len(results),
        "score": round(score, 4),
        "mrr": round(statistics.fmean(reciprocal_ranks), 4) if reciprocal_ranks else 0.0,
        "ndcg": round(statistics.fmean(ndcg_values), 4) if ndcg_values else 0.0,
        "top1_accuracy": round(sum(1 for item in ranked if item["first_relevant_rank"] == 1) / len(ranked), 4) if ranked else 0.0,
        "elapsed_ms": round(sum(float(item["elapsed_ms"]) for item in results), 2),
        "latency_p50_ms": round(statistics.median(elapsed), 2),
        "latency_p95_ms": latency_p95_ms,
        "quality_gate": {
            "fail_under": args.fail_under,
            "score_passed": score_passed,
            "max_p95_ms": args.max_p95_ms,
            "latency_passed": latency_passed,
            "require_embeddings": args.require_embeddings,
            "embeddings_passed": embeddings_passed,
            "passed": score_passed and latency_passed and embeddings_passed,
        },
        "cases": results,
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for item in results:
            marker = "PASS" if item["passed"] else "FAIL"
            print(f"[{marker}] {item['id']} ({item['elapsed_ms']:.2f} ms)")
            if not item["passed"]:
                for ref in item["top_refs"]:
                    print(f"  {ref}")
        print(f"retrieval score: {passed}/{len(results)} ({score:.1%})")
        print(f"profile: {effective_profile}")
        print(
            f"ranking: MRR={report['mrr']:.4f} nDCG={report['ndcg']:.4f} "
            f"top1={report['top1_accuracy']:.1%}"
        )
        print(f"latency: p50={report['latency_p50_ms']:.2f} ms p95={report['latency_p95_ms']:.2f} ms")
        if not embeddings_passed:
            print("quality gate: embedding provider required but unavailable")
        if not latency_passed:
            print(f"quality gate: p95 exceeded {args.max_p95_ms:.2f} ms")
    return 0 if report["quality_gate"]["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
