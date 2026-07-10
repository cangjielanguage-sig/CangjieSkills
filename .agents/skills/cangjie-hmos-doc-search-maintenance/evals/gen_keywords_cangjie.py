#!/usr/bin/env python3
"""gen_keywords_cangjie.py — 为 99 条 cangjie query 生成 keywords_cangjie.json

格式与 keywords_harmonyos.json 完全兼容:
  - 数字字符串键 "1"-"99" 对应 JSONL 行号
  - 每条含 core/context/synonym (zh+en) + keywords_en + keywords_zh

关键词提取规则:
  - api_lookup:     core = API 名 (从路径文件名提取)
  - enumeration:    core = 模块名 (从路径目录名提取)
  - how_to:         core = API 名, context = 操作动词
  - semantic_fuzzy: core = 概念名, synonym = 英文等价词
  - comparison:     core = 两个 API 名
  - workflow:       core = 主 API, context = 其他 API
  - reverse_lookup: core = 功能描述, synonym = 英文等价
  - composition:    core = 两个 API 名
  - constrained:    core = API 名, context = 约束条件
  - cross_ecosystem: core = 两个生态名
  - performance_boundary: core = 两个 API 名, context = 性能
"""
import json
import re
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parent
DATASET = EVAL_DIR / "datasets" / "eval_queries_cangjie.jsonl"
OUTPUT = EVAL_DIR / "keywords" / "keywords_cangjie.json"

# === 内核概念中英映射 ===
KERNEL_CONCEPT_MAP = {
    "字符串": {"en": ["String", "string"], "zh_syn": ["字符串类型"]},
    "类": {"en": ["class"], "zh_syn": []},
    "接口": {"en": ["interface"], "zh_syn": []},
    "泛型": {"en": ["generic", "generics"], "zh_syn": ["泛型编程"]},
    "异常": {"en": ["exception", "exception handling"], "zh_syn": ["异常处理"]},
    "并发": {"en": ["concurrency", "concurrent"], "zh_syn": ["多线程", "线程"]},
    "宏": {"en": ["macro", "macros"], "zh_syn": ["宏定义"]},
    "扩展": {"en": ["extension", "extend"], "zh_syn": ["扩展机制"]},
    "动态特性": {"en": ["reflection", "dynamic"], "zh_syn": ["反射", "注解"]},
    "互操作": {"en": ["FFI", "interop", "interoperability"], "zh_syn": ["C互操作"]},
}

# === 模块中英映射 (用于 enumeration) ===
MODULE_MAP = {
    "collection": {"en": ["collection", "collections"], "zh": ["集合", "数据结构"]},
    "core": {"en": ["core"], "zh": ["核心类型", "基本类型"]},
    "io": {"en": ["io", "stream"], "zh": ["输入输出", "流"]},
    "net": {"en": ["net", "network"], "zh": ["网络"]},
    "sync": {"en": ["sync", "synchronization"], "zh": ["同步", "线程同步"]},
    "time": {"en": ["time", "DateTime"], "zh": ["时间", "日期"]},
    "fs": {"en": ["fs", "file", "filesystem"], "zh": ["文件系统", "文件操作"]},
    "unittest": {"en": ["unittest", "test", "assertion"], "zh": ["单元测试", "测试断言"]},
    "function": {"en": ["function"], "zh": ["函数"]},
    "generic": {"en": ["generic", "generics"], "zh": ["泛型"]},
    "Macro": {"en": ["macro", "macros"], "zh": ["宏"]},
    "concurrency": {"en": ["concurrency", "concurrent"], "zh": ["并发"]},
    "error_handle": {"en": ["exception", "error"], "zh": ["异常", "错误处理"]},
    "enum_and_pattern_match": {"en": ["enum", "match", "pattern"], "zh": ["枚举", "模式匹配"]},
    "basic_data_type": {"en": ["data type", "basic type"], "zh": ["基本数据类型"]},
}

# === 工具名映射 ===
TOOL_MAP = {
    "cjpm": {"en": ["cjpm", "package manager"], "zh": ["包管理", "依赖"]},
    "cjdb": {"en": ["cjdb", "debugger"], "zh": ["调试"]},
    "cjfmt": {"en": ["cjfmt", "formatter"], "zh": ["格式化"]},
    "cjlint": {"en": ["cjlint", "linter"], "zh": ["代码检查", "lint"]},
    "cjcov": {"en": ["cjcov", "coverage"], "zh": ["覆盖率"]},
    "cjprof": {"en": ["cjprof", "profiler"], "zh": ["性能分析", "profiling"]},
    "cjtrace_recover": {"en": ["cjtrace_recover", "stack trace"], "zh": ["堆栈跟踪", "栈恢复"]},
    "chir_dis": {"en": ["chir_dis", "deserializer"], "zh": ["反序列化", "CHIR"]},
}


def extract_api_name(path: str) -> str:
    """从路径提取 API 名: class_HashMap.md → HashMap, func_sort.md → sort
    对非 API 文件 (sample_*, overview, 手册等) 返回模块名或工具名作为 fallback。"""
    fname = Path(path).name
    for prefix in ("class_", "func_", "enum_", "interface_", "struct_", "type_", "let_", "const_"):
        if fname.startswith(prefix):
            return fname[len(prefix):].replace(".md", "").split("_2more")[0]
    # 工具手册: cjpm_manual.md → cjpm
    if fname.endswith("_manual.md"):
        return fname.replace("_manual.md", "")
    # 非 API 文件 → 用模块名 (路径第二段)
    parts = path.split("/")
    if len(parts) >= 2:
        return parts[1]  # 如 cj-stdx/keys/sample_keys.md → keys
    return fname.replace(".md", "")


def extract_module(path: str) -> str:
    """从路径提取模块名: cj-std/collection/class_HashMap.md → collection"""
    parts = path.split("/")
    if len(parts) >= 2:
        return parts[1]
    return ""


def gen_keywords(query: dict, idx: int) -> dict:
    """为单条 query 生成 keywords 结构。"""
    cat = query["category"]
    src = query["source"]
    paths = query["acceptable_paths"]
    q_text = query["query"]
    intent = query["intent"]

    core_zh = []
    core_en = []
    ctx_zh = []
    ctx_en = []
    syn_zh = []
    syn_en = []

    if cat == "api_lookup":
        # core = API 名
        api = extract_api_name(paths[0])
        core_zh = [api]
        core_en = [api]
        # context = 从 query 提取操作词
        if "参数" in q_text or "怎么" in q_text:
            ctx_zh = []
            ctx_en = []

    elif cat == "enumeration":
        # core = 模块名 + 中文描述
        mod = extract_module(paths[0])
        if mod in MODULE_MAP:
            core_en = MODULE_MAP[mod]["en"]
            ctx_zh = MODULE_MAP[mod]["zh"]
        else:
            core_en = [mod]
            core_zh = [mod]

    elif cat == "how_to":
        # core = API 名
        if src == "tools":
            matched = False
            for tool, mapping in TOOL_MAP.items():
                if tool in q_text.lower():
                    core_en = mapping["en"]
                    syn_zh = mapping["zh"]
                    matched = True
                    break
            if not matched:
                # Fallback: 从路径提取工具名
                api = extract_api_name(paths[0])
                if api:
                    core_zh = [api]
                    core_en = [api]
        else:
            api = extract_api_name(paths[0])
            if api:
                core_zh = [api]
                core_en = [api]
        # context = 操作 (从 intent 提取)
        if intent:
            ctx_zh = [intent]

    elif cat == "semantic_fuzzy":
        # core = 概念名, synonym = 英文等价
        for concept, mapping in KERNEL_CONCEPT_MAP.items():
            if concept in q_text:
                core_zh = [concept]
                core_en = mapping["en"]
                syn_zh = mapping.get("zh_syn", [])
                break
        else:
            # 从路径文件名提取
            api = extract_api_name(paths[0])
            core_zh = [api]
            core_en = [api]

    elif cat == "comparison":
        # core = 两个 API 名
        apis = [extract_api_name(p) for p in paths]
        core_zh = apis
        core_en = apis
        ctx_en = ["comparison", "difference"]
        ctx_zh = ["区别", "对比"]

    elif cat == "workflow":
        # core = 主 API, context = 其他 API
        apis = [extract_api_name(p) for p in paths if not p.endswith(".overview.md")]
        if apis:
            core_zh = [apis[0]]
            core_en = [apis[0]]
            ctx_zh = apis[1:]
            ctx_en = apis[1:]
        ctx_en.append("workflow")

    elif cat == "reverse_lookup":
        # core = 功能描述, synonym = 英文
        if "JSON" in q_text or "json" in q_text.lower():
            core_zh = ["JSON解析"]
            core_en = ["JSON", "parse"]
        elif "Base64" in q_text:
            core_zh = ["Base64编码"]
            core_en = ["Base64", "encode"]
        elif "字符串" in q_text and "整数" in q_text:
            core_zh = ["字符串转整数"]
            core_en = ["parse", "convert"]
        elif "拼接" in q_text:
            core_zh = ["字符串拼接"]
            core_en = ["StringBuilder", "concat"]
        else:
            api = extract_api_name(paths[0])
            core_zh = [api]
            core_en = [api]
        syn_zh = ["反向查找", "哪个API"]

    elif cat == "composition":
        # core = 两个 API 名
        apis = [extract_api_name(p) for p in paths]
        core_zh = apis
        core_en = apis
        ctx_en = ["composition", "combine"]
        ctx_zh = ["组合"]

    elif cat == "constrained":
        # core = API 名, context = 约束
        api = extract_api_name(paths[0])
        core_zh = [api]
        core_en = [api]
        if "线程" in q_text and "并发" in q_text:
            ctx_zh = ["并发", "线程安全"]
            ctx_en = ["concurrent", "thread-safe"]
        elif "TLS" in q_text:
            ctx_zh = ["TLS", "单向认证"]
            ctx_en = ["TLS", "one-way"]
        elif "只读" in q_text:
            ctx_zh = ["只读", "不可变"]
            ctx_en = ["read-only", "immutable"]

    elif cat == "cross_ecosystem":
        # core = 两个生态名
        if "http" in q_text.lower() or "HTTP" in q_text:
            core_zh = ["HttpClient", "NetworkKit"]
            core_en = ["HttpClient", "NetworkKit", "HTTP"]
        elif "文件" in q_text or "file" in q_text.lower():
            core_zh = ["std.fs", "CoreFileKit"]
            core_en = ["fs", "CoreFileKit", "file"]
        ctx_zh = ["跨生态", "方案选择"]
        ctx_en = ["cross-ecosystem", "comparison"]

    elif cat == "performance_boundary":
        # core = 两个 API 名, context = 性能
        apis = [extract_api_name(p) for p in paths if not p.endswith(".overview.md")]
        if apis:
            core_zh = apis
            core_en = apis
        ctx_zh = ["性能", "性能差异"]
        ctx_en = ["performance", "benchmark"]

    # 去重
    core_zh = list(dict.fromkeys(core_zh))
    core_en = list(dict.fromkeys(core_en))
    ctx_zh = list(dict.fromkeys(ctx_zh))
    ctx_en = list(dict.fromkeys(ctx_en))
    syn_zh = list(dict.fromkeys(syn_zh))
    syn_en = list(dict.fromkeys(syn_en))

    keywords_en = list(dict.fromkeys(core_en + ctx_en + syn_en))
    keywords_zh = list(dict.fromkeys(core_zh + ctx_zh + syn_zh))

    return {
        "query": q_text,
        "intent": intent,
        "category": cat,
        "core": {"zh": core_zh, "en": core_en},
        "context": {"zh": ctx_zh, "en": ctx_en},
        "synonym": {"zh": syn_zh, "en": syn_en},
        "keywords_en": keywords_en,
        "keywords_zh": keywords_zh,
    }


def main():
    with open(DATASET, "r", encoding="utf-8") as f:
        queries = [json.loads(line) for line in f]

    result = {}
    for i, q in enumerate(queries, 1):
        result[str(i)] = gen_keywords(q, i)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"生成: {len(result)} 条 keywords")
    print(f"输出: {OUTPUT}")

    # 按类型统计 keyword 数
    by_cat = {}
    for v in result.values():
        cat = v["category"]
        total_kw = len(v["keywords_en"]) + len(v["keywords_zh"])
        by_cat[cat] = by_cat.get(cat, 0) + total_kw
    print("\n关键词总数 by category:")
    for c in sorted(by_cat):
        print(f"  {c}: {by_cat[c]}")


if __name__ == "__main__":
    main()
