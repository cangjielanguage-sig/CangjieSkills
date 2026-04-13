#!/usr/bin/env python3
"""鸿蒙应用开发文档检索工具 (OpenViking)"""

import argparse, json, re, sys, time, urllib.request, urllib.error
from typing import Any

# ── 常量 ─────────────────────────────────────────────────────

# 白名单: 只保留这三个目录的结果
ALLOWED_PREFIXES = ("application-dev/", "libs_stdx/", "std/")

# 来源混排配额, 保证每个桶至少占若干条
SOURCE_ORDER = ["application-dev", "libs_stdx", "std", "other"]
SOURCE_QUOTA = {"application-dev": 5, "libs_stdx": 5, "std": 5}

# 网络与召回
FETCH_MULTIPLIER = 15
MAX_FETCH = 500
MAX_RETRIES = 2
TIMEOUT = 45
RETRY_DELAY = 1.0
RETRYABLE_CODES = {502, 503, 504}

# 低信息词, 用于 fallback 重写
_NOISE = ["如何使用", "怎么使用", "如何实现", "怎么实现", "怎么调",
          "如何", "怎么", "实现", "使用"]
_PARTICLE_RE = re.compile(r"^[的了啊呀吗呢吧么嘛]+|[的了啊呀吗呢吧么嘛]+$")

# ── 工具函数 ──────────────────────────────────────────────────


def _utf8_stdio():
    """Windows/管道场景下强制 UTF-8 输出"""
    for s in (sys.stdout, sys.stderr):
        fn = getattr(s, "reconfigure", None)
        if callable(fn):
            try:
                fn(encoding="utf-8", errors="replace")
            except Exception:
                pass


def _strip_viking(uri: str) -> str:
    """去掉 viking://resources/ 前缀"""
    p = "viking://resources/"
    return uri[len(p):] if uri.startswith(p) else uri


def _source_of(path: str) -> str:
    """路径 → 来源桶名"""
    lp = path.lower()
    for prefix in ("application-dev/", "libs_stdx/", "std/"):
        if lp.startswith(prefix):
            return prefix.rstrip("/")
    return "other"


def _score(resource: dict) -> float:
    try:
        return float(resource.get("score", 0))
    except (TypeError, ValueError):
        return 0.0


def _rewrite(query: str) -> str:
    """去掉低信息问句词, 若无实质变化则返回空串"""
    q = query.strip()
    for w in _NOISE:
        q = q.replace(w, " ")
    q = re.sub(r"\s+", " ", q).strip()
    q = _PARTICLE_RE.sub("", q).strip()
    return "" if (not q or q == query.strip()) else q


# ── 网络请求 ──────────────────────────────────────────────────


def _post(url: str, headers: dict, payload: dict) -> dict:
    """POST + 有限重试"""
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(), headers=headers, method="POST",
    )
    last_err: Exception | None = None
    for i in range(MAX_RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code not in RETRYABLE_CODES or i >= MAX_RETRIES:
                raise
        except urllib.error.URLError as e:
            last_err = e
            if i >= MAX_RETRIES:
                raise
        time.sleep(RETRY_DELAY * (i + 1))
    raise last_err or RuntimeError("请求失败")


# ── 召回与混排 ────────────────────────────────────────────────


def _fetch(query: str, url: str, headers: dict, limit: int,
           target_uri: str, threshold: float | None,
           strip_prefix: bool, offset: int = 0) -> list[dict]:
    """单次召回并过滤为候选列表"""
    payload: dict[str, Any] = {"query": query, "limit": limit}
    if target_uri:
        payload["target_uri"] = target_uri
    if threshold is not None:
        payload["score_threshold"] = threshold

    data = _post(url, headers, payload)
    if data.get("status") != "ok":
        raise RuntimeError(data.get("error", "未知错误"))

    seen: set[str] = set()
    out: list[dict] = []
    for i, r in enumerate(data.get("result", {}).get("resources", [])):
        uri = r.get("uri", "")
        if not uri:
            continue
        norm = _strip_viking(uri)
        if not norm.startswith(ALLOWED_PREFIXES):
            continue
        path = norm if strip_prefix else uri
        if path in seen:
            continue
        seen.add(path)
        out.append({"idx": offset + i, "path": path,
                     "score": _score(r), "src": _source_of(norm)})
    return out


def _mix(candidates: list[dict], limit: int) -> list[str]:
    """按来源配额 + 分数混排, 返回路径列表"""
    if not candidates or limit <= 0:
        return []

    buckets: dict[str, list[dict]] = {s: [] for s in SOURCE_ORDER}
    for c in candidates:
        buckets.setdefault(c["src"], buckets["other"]).append(c)

    picked: list[str] = []
    used: set[int] = set()
    remain = limit

    # 按配额先选
    for src in SOURCE_ORDER:
        quota = SOURCE_QUOTA.get(src, 0)
        if quota <= 0 or remain <= 0:
            continue
        n = 0
        for c in buckets.get(src, []):
            if c["idx"] in used:
                continue
            picked.append(c["path"])
            used.add(c["idx"])
            n += 1
            remain -= 1
            if n >= quota or remain <= 0:
                break

    # 按分数补齐
    if remain > 0:
        rest = [c for c in candidates if c["idx"] not in used]
        rest.sort(key=lambda c: (-c["score"], c["idx"]))
        for c in rest[:remain]:
            picked.append(c["path"])

    return picked[:limit]


def _merge(a: list[dict], b: list[dict]) -> list[dict]:
    """去重合并两轮候选, 优先保留首轮"""
    seen: set[str] = set()
    out: list[dict] = []
    for c in a + b:
        if c["path"] not in seen:
            seen.add(c["path"])
            out.append(c)
    return out


# ── 搜索入口 ──────────────────────────────────────────────────


def search(query: str, host: str = "111.229.30.227", port: int = 2026,
           limit: int = 15, target_uri: str = "",
           threshold: float | None = None, strip_prefix: bool = True) -> list[str]:
    url = f"http://{host}:{port}/api/v1/search/find"
    fetch_limit = min(limit * FETCH_MULTIPLIER, MAX_FETCH)
    hdrs = {"Content-Type": "application/json", "X-API-Key": ",20250329.ljj"}
    kw = dict(url=url, headers=hdrs, limit=fetch_limit,
              target_uri=target_uri, threshold=threshold, strip_prefix=strip_prefix)

    try:
        primary = _fetch(query=query, **kw)
        result = _mix(primary, limit)

        if len(result) < 5:
            rq = _rewrite(query)
            if rq:
                fb = _fetch(query=rq, **kw, offset=len(primary))
                result = _mix(_merge(primary, fb), limit)
        return result

    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.reason}", file=sys.stderr)
        return []
    except urllib.error.URLError as e:
        print(f"连接错误: {e.reason}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        return []


# ── CLI ───────────────────────────────────────────────────────


def main():
    ap = argparse.ArgumentParser(description="鸿蒙应用开发文档检索")
    ap.add_argument("query", help="搜索语句")
    ap.add_argument("--host", default="111.229.30.227")
    ap.add_argument("--port", type=int, default=2026)
    ap.add_argument("--limit", type=int, default=15)
    ap.add_argument("--target-uri", default="")
    ap.add_argument("--score-threshold", type=float, default=None)
    ap.add_argument("--no-strip-prefix", action="store_true",
                    help="保留 viking://resources/ 前缀")
    args = ap.parse_args()

    _utf8_stdio()
    paths = search(
        args.query, args.host, args.port, args.limit,
        args.target_uri, args.score_threshold,
        strip_prefix=not args.no_strip_prefix,
    )
    if paths:
        for p in paths:
            print(p)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
