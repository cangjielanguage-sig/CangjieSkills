#!/usr/bin/env python3
"""
OpenViking 搜索客户端 - 鸿蒙应用开发文档查询工具

用法:
    python search.py "Stack组件用法" --version 15k
    python search.py "怎么修改Button组件的尺寸" --version 8k
    python search.py "怎么实现过渡动画" --version 15k --limit 15
"""

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error
from typing import List, Optional


def configure_stdio_utf8() -> None:
    """尽量让 Windows/管道环境下的中文路径输出不乱码。

    某些终端/采集器会以 UTF-8 解码 stdout，但 Python 默认按系统代码页编码输出，
    导致包含中文的路径显示为乱码（例如 "\\ufffd" 或 "????"）。
    """

    for stream in (sys.stdout, sys.stderr):
        try:
            reconfigure = getattr(stream, "reconfigure", None)
            if callable(reconfigure):
                reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            # 保守处理：不让工具因为输出编码配置失败而中断
            pass

# 按版本区分的排除规则（路径段精确匹配）
# 15k: 排除 application-dev，保留 application-dev-v15k
# 8k:  排除 application-dev-v15k，保留 application-dev
VERSION_EXCLUDES = {
    "15k": ["application-dev"],
    "8k": ["application-dev-v15k"],
}

# 为了避免先召回后过滤导致结果过少，先多取一批再截断到用户 limit
FETCH_MULTIPLIER = 15
MAX_FETCH_LIMIT = 500
FALLBACK_RESULT_THRESHOLD = 5
QUERY_REWRITE_PATTERNS = [
    "如何使用",
    "怎么使用",
    "如何实现",
    "怎么实现",
    "怎么调",
    "如何",
    "怎么",
    "实现",
    "使用",
]

# 结果混排策略：优先保证不同来源都有结果，再按分数补齐
SOURCE_ORDER = ["application-dev", "application-dev-v15k", "libs_stdx", "std", "other"]
MIN_SOURCE_QUOTA_BY_VERSION = {
    "8k": {
        "application-dev": 5,
        "libs_stdx": 5,
        "std": 5,
    },
    "15k": {
        "application-dev-v15k": 5,
        "libs_stdx": 5,
        "std": 5,
    },
}


def detect_version() -> str:
    """从工作区根目录的 .openvk-version 文件自动检测版本，向上逐级查找，未找到则返回空字符串"""
    current = os.path.dirname(os.path.abspath(__file__))
    while True:
        version_file = os.path.join(current, ".openvk-version")
        try:
            with open(version_file, "r", encoding="utf-8") as f:
                ver = f.read().strip().lower()
                if ver in VERSION_EXCLUDES:
                    return ver
        except FileNotFoundError:
            pass
        parent = os.path.dirname(current)
        if parent == current:
            break
        current = parent
    return ""


def strip_prefix(uri: str, prefix: str = "viking://resources/") -> str:
    """移除 URI 前缀"""
    if uri.startswith(prefix):
        return uri[len(prefix):]
    return uri


def classify_source(path: str) -> str:
    """将文档路径归类到主要来源桶"""
    p = path.lower()
    if p.startswith("application-dev-v15k/"):
        return "application-dev-v15k"
    if p.startswith("application-dev/"):
        return "application-dev"
    if p.startswith("libs_stdx/"):
        return "libs_stdx"
    if p.startswith("std/"):
        return "std"
    return "other"


def parse_score(resource: dict) -> float:
    """读取搜索分数，缺失时返回 0.0"""
    raw = resource.get("score", 0.0)
    try:
        return float(raw)
    except (TypeError, ValueError):
        return 0.0


def rewrite_query(query: str) -> str:
    """移除低信息问句词，作为低结果数时的补搜查询"""
    rewritten = query.strip()
    for pattern in QUERY_REWRITE_PATTERNS:
        rewritten = rewritten.replace(pattern, " ")

    rewritten = re.sub(r"\s+", " ", rewritten).strip()
    rewritten = re.sub(r"^[的了啊呀吗呢吧么嘛]+", "", rewritten)
    rewritten = re.sub(r"[的了啊呀吗呢吧么嘛]+$", "", rewritten).strip()

    if not rewritten or rewritten == query.strip():
        return ""
    return rewritten


def select_mixed_results(candidates: List[dict], limit: int, version: str) -> List[str]:
    """先按来源配额选取，再按分数补齐到 limit"""
    if limit <= 0:
        return []

    quotas = MIN_SOURCE_QUOTA_BY_VERSION.get(version, {})

    buckets = {source: [] for source in SOURCE_ORDER}
    for item in candidates:
        source = item["source"]
        if source not in buckets:
            source = "other"
        buckets[source].append(item)

    selected = []
    selected_indices = set()
    remaining = limit

    # 第一步：按最低配额先取，避免结果被单一来源占满
    for source in SOURCE_ORDER:
        quota = quotas.get(source, 0)
        if quota <= 0 or remaining <= 0:
            continue
        picked = 0
        for item in buckets[source]:
            idx = item["index"]
            if idx in selected_indices:
                continue
            selected.append(item["path"])
            selected_indices.add(idx)
            picked += 1
            remaining -= 1
            if picked >= quota or remaining <= 0:
                break

    if remaining <= 0:
        return selected[:limit]

    # 第二步：其余名额按分数优先补齐；同分时保留原始顺序
    leftovers = [item for item in candidates if item["index"] not in selected_indices]
    leftovers.sort(key=lambda x: (-x["score"], x["index"]))

    for item in leftovers[:remaining]:
        selected.append(item["path"])

    return selected[:limit]


def fetch_candidates(
    query: str,
    url: str,
    headers: dict,
    limit: int,
    target_uri: str,
    score_threshold: Optional[float],
    excludes: List[str],
    strip_uri_prefix: bool,
    index_offset: int = 0,
    pass_rank: int = 0,
) -> List[dict]:
    """向服务端发起一次搜索并转换为候选列表"""
    payload = {
        "query": query,
        "limit": limit,
    }

    if target_uri:
        payload["target_uri"] = target_uri

    if score_threshold is not None:
        payload["score_threshold"] = score_threshold

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))

    if data.get("status") != "ok":
        error_msg = data.get("error", "未知错误")
        raise RuntimeError(error_msg)

    result = data.get("result", {})
    resources = result.get("resources", [])

    candidates = []
    seen_paths = set()
    for idx, resource in enumerate(resources):
        uri = resource.get("uri", "")
        if not uri:
            continue

        if excludes:
            segments = uri.lower().split("/")
            if any(pat.lower() in segments for pat in excludes):
                continue

        if strip_uri_prefix:
            uri = strip_prefix(uri)

        if uri in seen_paths:
            continue
        seen_paths.add(uri)

        candidates.append(
            {
                "index": index_offset + idx,
                "path": uri,
                "score": parse_score(resource),
                "source": classify_source(uri),
                "pass_rank": pass_rank,
            }
        )

    return candidates


def merge_candidates(primary: List[dict], fallback: List[dict]) -> List[dict]:
    """按路径去重合并两轮候选，优先保留首轮结果"""
    merged = []
    seen_paths = set()

    for item in primary + fallback:
        path = item["path"]
        if path in seen_paths:
            continue
        seen_paths.add(path)
        merged.append(item)

    return merged


def search_documents(
    query: str,
    version: str = "15k",
    host: str = "111.229.30.227",
    port: int = 2026,
    limit: int = 15,
    target_uri: str = "",
    score_threshold: Optional[float] = None,
    extra_excludes: Optional[List[str]] = None,
    strip_uri_prefix: bool = True,
) -> List[str]:
    """
    调用 OpenViking API 搜索文档

    Args:
        query: 搜索查询语句
        version: 文档版本（8k 或 15k），决定排除哪个文档目录
        host: 服务主机地址
        port: 服务端口号
        limit: 返回结果数量限制（最终输出数量）
        target_uri: 目标 URI 过滤（可选）
        score_threshold: 相似度阈值
        extra_excludes: 额外排除的路径段关键词
        strip_uri_prefix: 是否移除 viking://resources/ 前缀

    Returns:
        文档路径列表
    """
    url = f"http://{host}:{port}/api/v1/search/find"

    fetch_limit = min(max(limit * FETCH_MULTIPLIER, limit), MAX_FETCH_LIMIT)

    headers = {
        "Content-Type": "application/json",
        "X-API-Key": ",20250329.ljj",
    }

    # 构建排除列表：版本规则 + 用户额外排除
    excludes = list(VERSION_EXCLUDES.get(version, []))
    if extra_excludes:
        for pat in extra_excludes:
            if pat not in excludes:
                excludes.append(pat)

    try:
        primary_candidates = fetch_candidates(
            query=query,
            url=url,
            headers=headers,
            limit=fetch_limit,
            target_uri=target_uri,
            score_threshold=score_threshold,
            excludes=excludes,
            strip_uri_prefix=strip_uri_prefix,
            index_offset=0,
            pass_rank=0,
        )
        selected_paths = select_mixed_results(primary_candidates, limit, version)

        fallback_query = ""
        if len(selected_paths) < FALLBACK_RESULT_THRESHOLD:
            fallback_query = rewrite_query(query)

        if fallback_query:
            fallback_candidates = fetch_candidates(
                query=fallback_query,
                url=url,
                headers=headers,
                limit=fetch_limit,
                target_uri=target_uri,
                score_threshold=score_threshold,
                excludes=excludes,
                strip_uri_prefix=strip_uri_prefix,
                index_offset=len(primary_candidates),
                pass_rank=1,
            )
            merged_candidates = merge_candidates(primary_candidates, fallback_candidates)
            return select_mixed_results(merged_candidates, limit, version)

        return selected_paths

    except urllib.error.HTTPError as e:
        print(f"HTTP 错误: {e.code} - {e.reason}", file=sys.stderr)
        try:
            error_body = e.read().decode("utf-8")
            print(f"错误详情: {error_body}", file=sys.stderr)
        except Exception:
            pass
        return []

    except urllib.error.URLError as e:
        print(f"连接错误: {e.reason}", file=sys.stderr)
        return []

    except json.JSONDecodeError as e:
        print(f"JSON 解析错误: {e}", file=sys.stderr)
        return []

    except RuntimeError as e:
        print(f"错误: {e}", file=sys.stderr)
        return []

    except Exception as e:
        print(f"发生错误: {e}", file=sys.stderr)
        return []


def main():
    parser = argparse.ArgumentParser(
        description="OpenViking 鸿蒙应用开发文档搜索客户端",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s "鸿蒙 Ability 开发" --version 15k
  %(prog)s "ArkTS 布局教程" --version 8k --limit 15
  %(prog)s "鸿蒙开发" --version 15k --exclude drafts
        """,
    )

    parser.add_argument(
        "query",
        help="搜索查询语句（例如：鸿蒙应用开发、Ability、ArkTS等）",
    )

    parser.add_argument(
        "--version",
        choices=["8k", "15k"],
        default=None,
        help="文档版本（8k 或 15k）。未指定时从工作区 .openvk-version 文件自动读取",
    )

    parser.add_argument(
        "--host",
        default="111.229.30.227",
        help="OpenViking 服务主机地址（默认: 111.229.30.227）",
    )

    parser.add_argument(
        "--port",
        type=int,
        default=2026,
        help="OpenViking 服务端口号（默认: 2026）",
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=15,
        help="返回结果数量限制（默认: 15）",
    )

    parser.add_argument(
        "--target-uri",
        default="",
        help="目标 URI 过滤（可选）",
    )

    parser.add_argument(
        "--score-threshold",
        type=float,
        default=None,
        help="相似度阈值，过滤低相关性结果（可选，例如: 0.5）",
    )

    parser.add_argument(
        "--exclude",
        nargs="*",
        default=[],
        help="额外排除的路径段关键词（可选）",
    )

    parser.add_argument(
        "--no-strip-prefix",
        action="store_true",
        help="保留 viking://resources/ 前缀（默认会移除）",
    )

    args = parser.parse_args()

    configure_stdio_utf8()

    # 确定版本：CLI 参数 > .openvk-version 文件 > 报错退出
    version = args.version or detect_version()
    if not version:
        print("错误: 未指定版本。请使用 --version 8k|15k，或在工作区根目录创建 .openvk-version 文件", file=sys.stderr)
        sys.exit(1)

    paths = search_documents(
        query=args.query,
        version=version,
        host=args.host,
        port=args.port,
        limit=args.limit,
        target_uri=args.target_uri,
        score_threshold=args.score_threshold,
        extra_excludes=args.exclude if args.exclude else None,
        strip_uri_prefix=not args.no_strip_prefix,
    )

    if paths:
        for path in paths:
            print(path)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
