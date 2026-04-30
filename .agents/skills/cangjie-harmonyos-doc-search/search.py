#!/usr/bin/env python3
"""
多源 OpenViking 聚合搜索客户端

用法:
  python client.py "你的问题"
  python client.py "你的问题" --limit 10
"""

import argparse
import json
import sys
import urllib.error
import urllib.request

# ── 默认配置（部署后按需修改）────────────────────────────────
DEFAULT_HOST = "111.229.30.227"
DEFAULT_PORT = 2026
DEFAULT_BACKENDS = ["cangjie-1.0.5", "harmonyos-compatibility-6.0.2.636"]


# ── 工具函数 ─────────────────────────────────────────────────


def _utf8_stdio():
    for stream in (sys.stdout, sys.stderr):
        fn = getattr(stream, "reconfigure", None)
        if callable(fn):
            try:
                fn(encoding="utf-8", errors="replace")
            except Exception:
                pass


def _post_json(url: str, payload: dict, *, timeout: int = 120) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read())


def _short_uri(uri: str) -> str:
    """剥离 URI 中 'resources/' 及之前的前缀，只保留相对路径"""
    tag = "resources/"
    pos = uri.find(tag)
    return uri[pos + len(tag):] if pos != -1 else uri


def _die(msg: str, hint: str = "") -> None:
    print(msg, file=sys.stderr)
    if hint:
        print(hint, file=sys.stderr)
    sys.exit(1)


# ── 主流程 ───────────────────────────────────────────────────


def _build_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="多源 OpenViking 聚合搜索客户端")
    ap.add_argument("query", help="搜索问题")
    ap.add_argument("--host", default=DEFAULT_HOST, help="服务地址")
    ap.add_argument("--port", type=int, default=DEFAULT_PORT, help="服务端口")
    ap.add_argument("--limit", type=int, default=15, help="查询返回的记录数上限")
    ap.add_argument("--target-uri", default="", help="限制检索路径，如 viking://resources/harmonyos-6.1-8k/Guide")
    ap.add_argument("--json", action="store_true", help="输出原始 JSON，获取更多信息")
    ap.add_argument("--timeout", type=int, default=120, help="请求超时阈值(秒)")
    return ap.parse_args()


def _search(args: argparse.Namespace) -> dict:
    url = f"http://{args.host}:{args.port}/api/v1/search"
    payload: dict = {
        "query": args.query,
        "limit": args.limit,
        "backends": DEFAULT_BACKENDS,
    }
    if args.target_uri:
        payload["target_uri"] = args.target_uri

    try:
        return _post_json(url, payload, timeout=args.timeout)
    except urllib.error.HTTPError as e:
        _die(f"HTTP {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        _die(f"连接失败: {e.reason}",
             f"请确认服务已启动: http://{args.host}:{args.port}")
    return {}  # unreachable, for type checker


def main():
    _utf8_stdio()
    args = _build_args()

    data = _search(args)
    if data.get("status") != "ok":
        _die(f"服务端错误: {data.get('error', '未知')}")

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        for r in data.get("results", []):
            print(_short_uri(r.get("uri", "")))


if __name__ == "__main__":
    main()
