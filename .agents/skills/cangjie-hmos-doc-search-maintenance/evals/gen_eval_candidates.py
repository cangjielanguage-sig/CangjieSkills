#!/usr/bin/env python3
"""gen_eval_candidates.py — 扫描 cangjie-docs 自动生成评测 query 候选

自动生成 ~49 条模板候选（api_lookup / enumeration / semantic_fuzzy / how_to）
输出 eval_candidates_auto.jsonl，供 GLM-5.2 润色 + explore agent 补缺。

Usage:
    python gen_eval_candidates.py
    python gen_eval_candidates.py --docs .agents/skills/cangjie-docs --output eval_candidates_auto.jsonl
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# === 路径 ===
SKILLS_DIR = Path(__file__).resolve().parent.parent.parent.parent  # .agents/skills/
DOCS_DIR = SKILLS_DIR / "cangjie-docs"

H1_RE = re.compile(r'^#\s+(.+)', re.MULTILINE)


def read_text(path: Path) -> str:
    full = str(path.resolve())
    if sys.platform == "win32" and len(full) > 240:
        full = "\\\\?\\" + full
    return Path(full).read_text(encoding="utf-8", errors="replace")


def extract_h1(content: str) -> str:
    m = H1_RE.search(content)
    return m.group(1).strip() if m else ""


def make_candidate(query, intent, category, source, capability, paths):
    """构造一条候选 JSONL 记录。"""
    return {
        "query": query,
        "intent": intent,
        "category": category,
        "source": source,
        "capability": capability,
        "acceptable_paths": paths if isinstance(paths, list) else [paths],
        "auto_generated": True,
    }


# === std api_lookup (10 条) ===

STD_API_LOOKUP = [
    ("collection", "class_HashMap.md", "HashMap", "HashMap存键值对"),
    ("collection", "class_ArrayList.md", "ArrayList", "ArrayList用法"),
    ("core", "struct_String.md", "String", "String字符串操作"),
    ("core", "struct_Array.md", "Array", "Array数组用法"),
    ("fs", "class_File.md", "File", "File文件读写"),
    ("io", "class_BufferedInputStream.md", "BufferedInputStream", "缓冲输入流"),
    ("sync", "class_Mutex.md", "Mutex", "Mutex互斥锁"),
    ("time", "struct_DateTime.md", "DateTime", "DateTime日期时间"),
    ("net", "class_IPAddress.md", "IPAddress", "IP地址类"),
    ("sort", "func_sort.md", "sort", "sort排序函数"),
]


def gen_std_api_lookup(docs_dir: Path) -> list:
    results = []
    for module, filename, api_name, intent in STD_API_LOOKUP:
        path = f"cj-std/{module}/{filename}"
        full = docs_dir / path
        if not full.exists():
            # try to find first class_/func_ in module
            mod_dir = docs_dir / "cj-std" / module
            if mod_dir.exists():
                for f in sorted(mod_dir.glob("class_*.md")):
                    filename = f.name
                    api_name = f.stem.replace("class_", "")
                    path = f"cj-std/{module}/{filename}"
                    break
        results.append(make_candidate(
            query=f"{api_name}的参数",
            intent=intent,
            category="api_lookup",
            source="std",
            capability=f"std/{module}",
            paths=[path],
        ))
    return results


# === stdx api_lookup (6 条) ===

STDX_API_LOOKUP = [
    ("json", "class_JsonArray.md", "JsonArray", "JsonArray用法"),
    ("json", "class_JsonObject.md", "JsonObject", "JsonObject用法"),
    ("http", "class_HttpRequest.md", "HttpRequest", "HTTP请求"),
    ("crypto", "class_SM4.md", "SM4", "SM4加密"),
    ("log", "class_Logger.md", "Logger", "日志记录"),
    ("serialization", "class_DataModel.md", "DataModel", "数据序列化"),
]


def gen_stdx_api_lookup(docs_dir: Path) -> list:
    results = []
    for module, filename, api_name, intent in STDX_API_LOOKUP:
        path = f"cj-stdx/{module}/{filename}"
        full = docs_dir / path
        if not full.exists():
            mod_dir = docs_dir / "cj-stdx" / module
            if mod_dir.exists():
                for f in sorted(mod_dir.glob("class_*.md")):
                    filename = f.name
                    api_name = f.stem.replace("class_", "")
                    path = f"cj-stdx/{module}/{filename}"
                    break
        results.append(make_candidate(
            query=f"{api_name}的参数",
            intent=intent,
            category="api_lookup",
            source="stdx",
            capability=f"stdx/{module}",
            paths=[path],
        ))
    return results


# === std enumeration (8 条) ===

STD_ENUMERATION = [
    ("collection", "数据结构", "collection包有哪些数据结构"),
    ("core", "核心类型", "core包有哪些基本类型"),
    ("io", "IO流", "io包有哪些流"),
    ("net", "网络类", "net包有哪些网络类"),
    ("sync", "同步原语", "sync包有哪些同步原语"),
    ("time", "时间类型", "time包有哪些时间类型"),
    ("fs", "文件操作", "fs包有哪些文件操作"),
    ("unittest", "测试断言", "unittest包有哪些测试功能"),
]


def gen_std_enumeration(docs_dir: Path) -> list:
    results = []
    for module, desc, query in STD_ENUMERATION:
        path = f"cj-std/{module}/.overview.md"
        full = docs_dir / path
        if not full.exists():
            continue
        results.append(make_candidate(
            query=query,
            intent=f"{module}枚举",
            category="enumeration",
            source="std",
            capability=f"std/{module}",
            paths=[path],
        ))
    return results


# === kernel enumeration (7 条) ===

KERNEL_ENUMERATION = [
    ("basic_data_type", "基本数据类型", "Cangjie有哪些基本数据类型"),
    ("function", "函数类型", "Cangjie函数有哪些类型"),
    ("generic", "泛型约束", "Cangjie泛型有哪些约束"),
    ("Macro", "宏种类", "Cangjie宏有哪些种类"),
    ("concurrency", "并发机制", "Cangjie并发有哪些机制"),
    ("error_handle", "异常类型", "Cangjie异常有哪些类型"),
    ("enum_and_pattern_match", "枚举与模式匹配", "Cangjie枚举和模式匹配有哪些"),
]


def gen_kernel_enumeration(docs_dir: Path) -> list:
    results = []
    for topic, desc, query in KERNEL_ENUMERATION:
        path = f"cj-kernel/{topic}/.overview.md"
        full = docs_dir / path
        if not full.exists():
            continue
        results.append(make_candidate(
            query=query,
            intent=f"{topic}枚举",
            category="enumeration",
            source="kernel",
            capability=f"kernel/{topic}",
            paths=[path],
        ))
    return results


# === kernel semantic_fuzzy (10 条) ===

KERNEL_SEMANTIC = [
    ("basic_data_type", "strings.md"),
    ("class_and_interface", "class.md"),
    ("class_and_interface", "interface.md"),
    ("generic", "generic_overview.md"),
    ("error_handle", "exception_overview.md"),
    ("concurrency", "concurrency_overview.md"),
    ("Macro", "macro_introduction.md"),
    ("extension", "extend_overview.md"),
    ("reflect_and_annotation", "dynamic_feature.md"),
    ("FFI", "cangjie-c.md"),
]


def gen_kernel_semantic(docs_dir: Path) -> list:
    results = []
    for topic, filename in KERNEL_SEMANTIC:
        path = f"cj-kernel/{topic}/{filename}"
        full = docs_dir / path
        if not full.exists():
            continue
        content = read_text(full)
        h1 = extract_h1(content)
        if not h1:
            h1 = topic
        query = f"什么是{h1}"
        results.append(make_candidate(
            query=query,
            intent=f"{h1}概念",
            category="semantic_fuzzy",
            source="kernel",
            capability=f"kernel/{topic}",
            paths=[path],
        ))
    return results


# === tools how_to (8 条) ===

TOOLS_HOWTO = [
    ("cmd-tools/cjpm_manual.md", "cjpm", "cjpm怎么添加依赖"),
    ("cmd-tools/cjdb_manual.md", "cjdb", "cjdb怎么调试程序"),
    ("cmd-tools/cjfmt_manual.md", "cjfmt", "cjfmt怎么格式化代码"),
    ("cmd-tools/cjlint_manual.md", "cjlint", "cjlint怎么检查代码"),
    ("cmd-tools/cjcov_manual.md", "cjcov", "cjcov怎么测覆盖率"),
    ("cmd-tools/cjprof_manual.md", "cjprof", "cjprof怎么性能分析"),
    ("cmd-tools/cjtrace_recover_manual.md", "cjtrace_recover", "怎么恢复堆栈跟踪"),
    ("cmd-tools/chir_dis_manual.md", "chir_dis", "chir_dis怎么用"),
]


def gen_tools_howto(docs_dir: Path) -> list:
    results = []
    for filename, tool_name, query in TOOLS_HOWTO:
        path = f"cj-tools/{filename}"
        full = docs_dir / path
        if not full.exists():
            continue
        results.append(make_candidate(
            query=query,
            intent=f"{tool_name}使用",
            category="how_to",
            source="tools",
            capability=f"tools/{tool_name}",
            paths=[path],
        ))
    return results


# === 主函数 ===

def main():
    parser = argparse.ArgumentParser(description="生成评测 query 候选")
    parser.add_argument("--docs", default=str(DOCS_DIR), help="cangjie-docs 目录")
    parser.add_argument("--output", default="eval_candidates_auto.jsonl", help="输出 JSONL")
    args = parser.parse_args()

    docs_dir = Path(args.docs).resolve()
    if not docs_dir.exists():
        print(f"ERROR: {docs_dir} 不存在")
        sys.exit(1)

    all_candidates = []

    # 1. std api_lookup
    std_api = gen_std_api_lookup(docs_dir)
    all_candidates.extend(std_api)
    print(f"std api_lookup: {len(std_api)}")

    # 2. stdx api_lookup
    stdx_api = gen_stdx_api_lookup(docs_dir)
    all_candidates.extend(stdx_api)
    print(f"stdx api_lookup: {len(stdx_api)}")

    # 3. std enumeration
    std_enum = gen_std_enumeration(docs_dir)
    all_candidates.extend(std_enum)
    print(f"std enumeration: {len(std_enum)}")

    # 4. kernel enumeration
    kernel_enum = gen_kernel_enumeration(docs_dir)
    all_candidates.extend(kernel_enum)
    print(f"kernel enumeration: {len(kernel_enum)}")

    # 5. kernel semantic_fuzzy
    kernel_sem = gen_kernel_semantic(docs_dir)
    all_candidates.extend(kernel_sem)
    print(f"kernel semantic_fuzzy: {len(kernel_sem)}")

    # 6. tools how_to
    tools_how = gen_tools_howto(docs_dir)
    all_candidates.extend(tools_how)
    print(f"tools how_to: {len(tools_how)}")

    total = len(all_candidates)
    print(f"\n总计: {total} 条候选")

    # 按来源统计
    by_source = {}
    for c in all_candidates:
        by_source[c["source"]] = by_source.get(c["source"], 0) + 1
    for s, n in sorted(by_source.items()):
        print(f"  {s}: {n}")

    # 按类别统计
    by_cat = {}
    for c in all_candidates:
        by_cat[c["category"]] = by_cat.get(c["category"], 0) + 1
    for s, n in sorted(by_cat.items()):
        print(f"  {s}: {n}")

    # 写入 JSONL
    output_path = Path(args.output)
    with open(output_path, "w", encoding="utf-8") as f:
        for c in all_candidates:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"\n输出: {output_path}")

    # 输出 explore agent 补缺清单
    print("\n=== explore agent 需补缺 ===")
    print("std how_to: 8 条 (正则/随机数/排序/文件遍历/线程创建/异常捕获/类型转换/字符串拼接)")
    print("stdx how_to: 8 条 (HTTP GET/TLS配置/gzip压缩/Base64编码/JSON解析/日志配置/URL解析/序列化)")
    print("stdx workflow: 6 条 (加密流程/日志流程/HTTP服务流程/TLS握手/JSON流式解析/压缩解压)")
    print("std comparison: 4 条 (ArrayList vs LinkedList/Int vs Int64/Mutex vs Semaphore/sort vs stableSort)")
    print("kernel comparison: 8 条 (class vs interface/struct vs class/enum vs match/let vs const/generic vs subtype/闭包vs lambda/同步vs异步/FFI vs 互操作)")
    print(f"补缺小计: 34 条 → 总计 {total + 34} 条")


if __name__ == "__main__":
    main()
