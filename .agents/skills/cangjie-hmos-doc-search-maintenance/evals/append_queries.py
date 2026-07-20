#!/usr/bin/env python3
"""append_queries.py — 追加 16 条新 query 到 eval_queries_cangjie.jsonl (83→99)

补充 5 个缺失类型: reverse_lookup / composition / constrained / cross_ecosystem / performance_boundary
"""
import json
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parent
OUTPUT = EVAL_DIR / "datasets" / "eval_queries_cangjie.jsonl"

NEW_QUERIES = [
    # === reverse_lookup (4) ===
    {"query": "什么API能把字符串转成整数", "intent": "反向查找字符串转数值的API", "category": "reverse_lookup", "source": "std", "capability": "std/convert", "acceptable_paths": ["cj-std/convert/interface_Parsable.md"]},
    {"query": "哪个类能高效拼接大量字符串", "intent": "反向查找高效字符串拼接类", "category": "reverse_lookup", "source": "std", "capability": "std/core", "acceptable_paths": ["cj-std/core/class_StringBuilder.md"]},
    {"query": "哪个类能流式解析大JSON数据", "intent": "反向查找流式JSON解析类", "category": "reverse_lookup", "source": "stdx", "capability": "stdx/json_stream", "acceptable_paths": ["cj-stdx/json_stream/class_JsonReader.md"]},
    {"query": "什么API能做Base64编码解码", "intent": "反向查找Base64编解码API", "category": "reverse_lookup", "source": "stdx", "capability": "stdx/base64", "acceptable_paths": ["cj-stdx/base64/base64.md"]},
    # === composition (4) ===
    {"query": "用File和BufferedInputStream组合读取大文件", "intent": "File+BufferedInputStream组合读大文件", "category": "composition", "source": "std", "capability": "std/fs", "acceptable_paths": ["cj-std/fs/class_File.md", "cj-std/io/class_BufferedInputStream.md"]},
    {"query": "用Regex和String组合验证邮箱格式", "intent": "Regex+String组合验证邮箱", "category": "composition", "source": "std", "capability": "std/regex", "acceptable_paths": ["cj-std/regex/class_Regex.md", "cj-std/core/struct_String.md"]},
    {"query": "用Logger和DataModel组合记录序列化日志", "intent": "Logger+DataModel组合记录序列化", "category": "composition", "source": "stdx", "capability": "stdx/log", "acceptable_paths": ["cj-stdx/log/class_Logger.md", "cj-stdx/serialization/class_DataModel.md"]},
    {"query": "用JsonArray和url组合解析API返回的JSON并提取URL参数", "intent": "JsonArray+url组合解析JSON提取URL", "category": "composition", "source": "stdx", "capability": "stdx/json", "acceptable_paths": ["cj-stdx/json/class_JsonArray.md", "cj-stdx/url/url_parse.md"]},
    # === constrained (3) ===
    {"query": "在多线程并发下怎么安全操作HashMap", "intent": "并发约束下安全操作HashMap", "category": "constrained", "source": "std", "capability": "std/collection_concurrent", "acceptable_paths": ["cj-std/collection_concurrent/class_ConcurrentHashMap.md"]},
    {"query": "在TLS只配单向认证的情况下怎么连接服务端", "intent": "TLS单向认证约束下连接", "category": "constrained", "source": "stdx", "capability": "stdx/tls", "acceptable_paths": ["cj-stdx/tls/client.md"]},
    {"query": "在只读约束下怎么遍历集合不修改内容", "intent": "只读约束下遍历集合", "category": "constrained", "source": "std", "capability": "std/collection", "acceptable_paths": ["cj-std/collection/interface_ReadOnlyList.md"]},
    # === cross_ecosystem (2) ===
    {"query": "发HTTP请求用stdx的http还是harmonyos的NetworkKit", "intent": "跨生态HTTP请求方案选择", "category": "cross_ecosystem", "source": "cross", "capability": "cross/http", "acceptable_paths": ["cj-stdx/http/http_client.md", "cj-network/cj-apis-net-http/ohosnethttp数据请求/class_HttpRequest.md"]},
    {"query": "文件操作用std.fs还是harmonyos的CoreFileKit", "intent": "跨生态文件操作方案选择", "category": "cross_ecosystem", "source": "cross", "capability": "cross/file", "acceptable_paths": ["cj-std/fs/class_File.md", "cj-corefile/cj-apis-file_fs/ohosfile_fs文件系统/class_File.md"]},
    # === performance_boundary (3) ===
    {"query": "Array和ArrayList在大量数据时性能差异", "intent": "Array vs ArrayList性能边界", "category": "performance_boundary", "source": "std", "capability": "std/core", "acceptable_paths": ["cj-std/core/struct_Array.md", "cj-std/collection/class_ArrayList.md"]},
    {"query": "HashMap和TreeMap的查找性能对比", "intent": "HashMap vs TreeMap查找性能", "category": "performance_boundary", "source": "std", "capability": "std/collection", "acceptable_paths": ["cj-std/collection/class_HashMap.md", "cj-std/collection/class_TreeMap.md"]},
    {"query": "zlib不同压缩级别对性能的影响", "intent": "zlib压缩级别性能边界", "category": "performance_boundary", "source": "stdx", "capability": "stdx/zlib", "acceptable_paths": ["cj-stdx/zlib/.overview.md"]},
]


def main():
    # 读取现有
    with open(OUTPUT, "r", encoding="utf-8") as f:
        existing = f.readlines()
    print(f"现有: {len(existing)} 条")

    # 追加新 query
    with open(OUTPUT, "a", encoding="utf-8") as f:
        for q in NEW_QUERIES:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    print(f"追加: {len(NEW_QUERIES)} 条")

    # 验证总数
    with open(OUTPUT, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"总计: {total} 条")

    # 按类型统计
    with open(OUTPUT, "r", encoding="utf-8") as f:
        by_cat = {}
        by_src = {}
        for line in f:
            q = json.loads(line)
            by_cat[q["category"]] = by_cat.get(q["category"], 0) + 1
            by_src[q["source"]] = by_src.get(q["source"], 0) + 1

    print("\n按类型:")
    for c in sorted(by_cat):
        print(f"  {c}: {by_cat[c]}")
    print("\n按来源:")
    for s in sorted(by_src):
        print(f"  {s}: {by_src[s]}")


if __name__ == "__main__":
    main()
