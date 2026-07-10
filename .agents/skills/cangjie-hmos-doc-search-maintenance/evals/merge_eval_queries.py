#!/usr/bin/env python3
"""merge_eval_queries.py — 合并自动生成 + explore agent 的评测 query

将 49 条自动生成候选（GLM-5.2 润色后）+ 34 条 explore agent 设计的 query
合并为 eval_queries_cangjie.jsonl（83 条）

Usage:
    python merge_eval_queries.py
"""
import json
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parent
AUTO_PATH = EVAL_DIR / "eval_candidates_auto.jsonl"
OUTPUT_PATH = EVAL_DIR / "eval_queries_cangjie.jsonl"

# === GLM-5.2 润色后的 49 条自动生成 query ===
# 格式: (原query, 润色后query)
POLISHED = {
    # std api_lookup (10)
    "HashMap的参数": "HashMap怎么存键值对",
    "ArrayList的参数": "ArrayList怎么添加和删除元素",
    "String的参数": "String字符串有哪些常用方法",
    "Array的参数": "Array数组怎么创建和遍历",
    "File的参数": "File怎么读写文件内容",
    "BufferedInputStream的参数": "缓冲输入流怎么读取数据",
    "Mutex的参数": "Mutex互斥锁怎么加锁解锁",
    "DateTime的参数": "DateTime怎么获取当前时间",
    "IPAddress的参数": "IPAddress怎么解析IP地址",
    "sort的参数": "sort排序函数怎么用",
    # stdx api_lookup (6)
    "JsonArray的参数": "JsonArray怎么创建和遍历",
    "JsonObject的参数": "JsonObject怎么读取和修改字段",
    "HttpRequest的参数": "HttpRequest怎么设置请求头和请求体",
    "SM4的参数": "SM4加密算法怎么用",
    "Logger的参数": "Logger怎么记录不同级别的日志",
    "DataModel的参数": "DataModel怎么实现数据序列化",
    # std enumeration (8)
    "collection包有哪些数据结构": "Cangjie标准库有哪些集合数据结构",
    "core包有哪些基本类型": "Cangjie的core包提供哪些核心类型",
    "io包有哪些流": "Cangjie的io包有哪些输入输出流",
    "net包有哪些网络类": "Cangjie标准库有哪些网络编程类",
    "sync包有哪些同步原语": "Cangjie有哪些线程同步原语",
    "time包有哪些时间类型": "Cangjie有哪些时间日期类型",
    "fs包有哪些文件操作": "Cangjie的fs包提供哪些文件系统操作",
    "unittest包有哪些测试功能": "Cangjie的unittest包有哪些测试断言方法",
    # kernel enumeration (7)
    "Cangjie有哪些基本数据类型": "仓颉编程语言有哪些基本数据类型",
    "Cangjie函数有哪些类型": "仓颉的函数有哪几种定义方式",
    "Cangjie泛型有哪些约束": "仓颉泛型有哪些约束条件",
    "Cangjie宏有哪些种类": "仓颉宏有哪些种类和用法",
    "Cangjie并发有哪些机制": "仓颉语言有哪些并发编程机制",
    "Cangjie异常有哪些类型": "仓颉有哪些异常处理类型",
    "Cangjie枚举和模式匹配有哪些": "仓颉的枚举和模式匹配怎么配合使用",
    # kernel semantic_fuzzy (10) - H1 extracted, may vary
    "什么是字符串类型": "仓颉的字符串类型怎么用",
    "什么是类": "仓颉怎么定义和使用类",
    "什么是接口": "仓颉的接口有什么用怎么实现",
    "什么是泛型概述": "仓颉泛型编程怎么写",
    "什么是定义异常": "仓颉异常处理机制怎么工作",
    "什么是并发概述": "仓颉多线程并发怎么实现",
    "什么是宏的简介": "仓颉宏怎么定义和使用",
    "什么是扩展概述": "仓颉的扩展机制怎么用",
    "什么是动态特性": "仓颉的反射和动态特性怎么用",
    "什么是仓颉-C 互操作": "仓颉怎么和C语言互操作",
    # tools how_to (8)
    "cjpm怎么添加依赖": "cjpm怎么添加第三方依赖包",
    "cjdb怎么调试程序": "cjdb怎么调试仓颉程序",
    "cjfmt怎么格式化代码": "cjfmt怎么自动格式化仓颉代码",
    "cjlint怎么检查代码": "cjlint怎么检查代码规范问题",
    "cjcov怎么测覆盖率": "cjcov怎么生成代码覆盖率报告",
    "cjprof怎么性能分析": "cjprof怎么分析程序性能瓶颈",
    "怎么恢复堆栈跟踪": "程序崩溃后怎么恢复堆栈跟踪信息",
    "chir_dis怎么用": "chir_dis工具怎么反序列化CHIR",
}

# === 34 条 explore agent 设计的 query ===
EXPLORE_QUERIES = [
    # Agent A: std how_to (8)
    {"query": "仓颉怎么用正则表达式匹配邮箱地址", "intent": "使用正则表达式匹配字符串", "category": "how_to", "source": "std", "capability": "std/regex", "acceptable_paths": ["cj-std/regex/class_Regex.md"]},
    {"query": "仓颉怎么生成一个随机数", "intent": "生成随机数", "category": "how_to", "source": "std", "capability": "std/random", "acceptable_paths": ["cj-std/random/class_Random.md"]},
    {"query": "仓颉怎么对一个数组进行排序", "intent": "对数组元素排序", "category": "how_to", "source": "std", "capability": "std/sort", "acceptable_paths": ["cj-std/sort/func_sort.md"]},
    {"query": "仓颉怎么遍历一个目录下的所有文件", "intent": "遍历目录中的文件", "category": "how_to", "source": "std", "capability": "std/fs", "acceptable_paths": ["cj-std/fs/class_Directory.md"]},
    {"query": "仓颉怎么创建并启动一个新线程", "intent": "创建并启动线程", "category": "how_to", "source": "std", "capability": "std/core", "acceptable_paths": ["cj-std/core/class_Thread.md"]},
    {"query": "仓颉怎么捕获并处理程序抛出的异常", "intent": "捕获和处理异常", "category": "how_to", "source": "std", "capability": "std/core", "acceptable_paths": ["cj-std/core/class_Exception.md"]},
    {"query": "仓颉怎么把字符串转换成整数类型", "intent": "字符串转换为数值类型", "category": "how_to", "source": "std", "capability": "std/convert", "acceptable_paths": ["cj-std/convert/interface_Parsable.md"]},
    {"query": "仓颉怎么高效拼接大量字符串", "intent": "高效拼接字符串", "category": "how_to", "source": "std", "capability": "std/core", "acceptable_paths": ["cj-std/core/class_StringBuilder.md"]},
    # Agent B: stdx how_to (8) + workflow (6) = 14
    {"query": "怎么用仓颉的http客户端发起一个GET请求获取网页内容", "intent": "HTTP GET 请求", "category": "how_to", "source": "stdx", "capability": "stdx/http", "acceptable_paths": ["cj-stdx/http/http_client.md"]},
    {"query": "如何为TLS服务端配置证书和私钥文件", "intent": "TLS 证书配置", "category": "how_to", "source": "stdx", "capability": "stdx/tls", "acceptable_paths": ["cj-stdx/tls/cert_key.md"]},
    {"query": "怎么用zlib对文件做gzip压缩和解压", "intent": "gzip 压缩解压", "category": "how_to", "source": "stdx", "capability": "stdx/zlib", "acceptable_paths": ["cj-stdx/zlib/gzip_compress_decompress.md"]},
    {"query": "怎么把字节数组和Base64字符串互相转换", "intent": "Base64 编码解码", "category": "how_to", "source": "stdx", "capability": "stdx/base64", "acceptable_paths": ["cj-stdx/base64/base64.md"]},
    {"query": "如何把JSON字符串解析成JsonValue对象并读取字段", "intent": "JSON 解析", "category": "how_to", "source": "stdx", "capability": "stdx/json", "acceptable_paths": ["cj-stdx/json/json_value_sample.md"]},
    {"query": "仓颉库里怎么配置和打印日志", "intent": "日志配置", "category": "how_to", "source": "stdx", "capability": "stdx/log", "acceptable_paths": ["cj-stdx/log/log_sample.md"]},
    {"query": "怎么用parse函数解析URL字符串拿到协议路径查询参数等各部分", "intent": "URL 解析", "category": "how_to", "source": "stdx", "capability": "stdx/url", "acceptable_paths": ["cj-stdx/url/url_parse.md"]},
    {"query": "如何给自定义class实现序列化和反序列化", "intent": "序列化", "category": "how_to", "source": "stdx", "capability": "stdx/serialization", "acceptable_paths": ["cj-stdx/serialization/serialize_and_deserialize_class.md"]},
    {"query": "完整的加密解密流程是怎样的：怎么生成RSA密钥对，再用SM4加密数据最后解密还原", "intent": "密钥生成→加密→解密流程", "category": "workflow", "source": "stdx", "capability": "stdx/keys", "acceptable_paths": ["cj-stdx/keys/sample_keys.md", "cj-stdx/crypto/sample_crypto.md"]},
    {"query": "从零开始配置日志的完整步骤：怎么创建Logger、设置日志级别、再通过SimpleLogger输出日志", "intent": "创建Logger→设置级别→输出流程", "category": "workflow", "source": "stdx", "capability": "stdx/log", "acceptable_paths": ["cj-stdx/log/log_sample.md", "cj-stdx/logger/logger_sample.md"]},
    {"query": "搭建HTTP服务的完整流程：怎么用ServerBuilder创建Server、注册路由Handler然后启动服务", "intent": "创建Server→配置路由→启动流程", "category": "workflow", "source": "stdx", "capability": "stdx/http", "acceptable_paths": ["cj-stdx/http/http_server.md", "cj-stdx/http/class_ServerBuilder.md", "cj-stdx/http/class_Server.md"]},
    {"query": "TLS客户端和服务端建立连接握手的全过程怎么写：从配置TlsClientConfig到TlsSocket握手完成", "intent": "TLS 握手流程", "category": "workflow", "source": "stdx", "capability": "stdx/tls", "acceptable_paths": ["cj-stdx/tls/client.md", "cj-stdx/tls/server.md", "cj-stdx/tls/class_TlsSocket.md"]},
    {"query": "怎么用JsonReader流式解析大JSON数据：从创建reader到逐token读取完整流程", "intent": "JSON 流式解析流程", "category": "workflow", "source": "stdx", "capability": "stdx/json_stream", "acceptable_paths": ["cj-stdx/json_stream/sample_json_reader.md", "cj-stdx/json_stream/class_JsonReader.md"]},
    {"query": "用zlib做压缩解压的完整流程：怎么用CompressOutputStream压缩、再用DecompressInputStream解压还原", "intent": "压缩解压流式流程", "category": "workflow", "source": "stdx", "capability": "stdx/zlib", "acceptable_paths": ["cj-stdx/zlib/deflate_compress_decompress.md", "cj-stdx/zlib/class_CompressOutputStream.md", "cj-stdx/zlib/class_DecompressInputStream.md"]},
    # Agent C: std comparison (4) + kernel comparison (8) = 12
    {"query": "ArrayList和LinkedList有什么区别", "intent": "对比两种列表容器的差异", "category": "comparison", "source": "std", "capability": "std/collection", "acceptable_paths": ["cj-std/collection/class_ArrayList.md", "cj-std/collection/class_LinkedList.md"]},
    {"query": "Int和Int64有什么区别", "intent": "对比Int类型别名与Int64内置类型的区别", "category": "comparison", "source": "std", "capability": "std/core", "acceptable_paths": ["cj-std/core/type_Int.md", "cj-std/core/core_package_intrinsics.md"]},
    {"query": "Mutex和Semaphore有什么区别", "intent": "对比互斥锁与信号量的差异", "category": "comparison", "source": "std", "capability": "std/sync", "acceptable_paths": ["cj-std/sync/class_Mutex.md", "cj-std/sync/class_Semaphore.md"]},
    {"query": "sort和stableSort有什么区别", "intent": "对比两种排序函数的差异", "category": "comparison", "source": "std", "capability": "std/sort", "acceptable_paths": ["cj-std/sort/func_sort.md", "cj-std/sort/func_stableSort.md"]},
    {"query": "class和interface有什么区别", "intent": "对比类与接口的区别", "category": "comparison", "source": "kernel", "capability": "kernel/class_and_interface", "acceptable_paths": ["cj-kernel/class_and_interface/class.md", "cj-kernel/class_and_interface/interface.md"]},
    {"query": "struct和class有什么区别", "intent": "对比结构体与类的区别", "category": "comparison", "source": "kernel", "capability": "kernel/struct", "acceptable_paths": ["cj-kernel/struct/define_struct.md", "cj-kernel/class_and_interface/class.md"]},
    {"query": "enum和match有什么区别", "intent": "对比枚举类型与模式匹配的区别", "category": "comparison", "source": "kernel", "capability": "kernel/enum_and_pattern_match", "acceptable_paths": ["cj-kernel/enum_and_pattern_match/enum.md", "cj-kernel/enum_and_pattern_match/match.md"]},
    {"query": "let和const有什么区别", "intent": "对比let与const两种变量修饰符", "category": "comparison", "source": "kernel", "capability": "kernel/basic_programming_concepts", "acceptable_paths": ["cj-kernel/basic_programming_concepts/program_structure.md", "cj-kernel/Appendix/keyword.md"]},
    {"query": "泛型和子类型有什么区别", "intent": "对比泛型与子类型多态", "category": "comparison", "source": "kernel", "capability": "kernel/generic", "acceptable_paths": ["cj-kernel/generic/generic_overview.md", "cj-kernel/generic/generic_subtype.md"]},
    {"query": "闭包和lambda有什么区别", "intent": "对比闭包与lambda表达式", "category": "comparison", "source": "kernel", "capability": "kernel/function", "acceptable_paths": ["cj-kernel/function/closure.md", "cj-kernel/function/lambda.md"]},
    {"query": "同步和异步有什么区别", "intent": "对比同步与异步并发机制", "category": "comparison", "source": "kernel", "capability": "kernel/concurrency", "acceptable_paths": ["cj-kernel/concurrency/sync.md", "cj-kernel/concurrency/use_thread.md"]},
    {"query": "FFI和互操作有什么区别", "intent": "对比FFI与互操作概念", "category": "comparison", "source": "kernel", "capability": "kernel/FFI", "acceptable_paths": ["cj-kernel/FFI/cangjie-c.md", "cj-kernel/FFI/.overview.md"]},
]


def main():
    # 1. 读取自动生成的候选，应用 GLM-5.2 润色
    auto_queries = []
    if AUTO_PATH.exists():
        with open(AUTO_PATH, "r", encoding="utf-8") as f:
            for line in f:
                q = json.loads(line)
                original = q["query"]
                # 尝试精确匹配
                if original in POLISHED:
                    q["query"] = POLISHED[original]
                else:
                    # 模糊匹配: 去空格后匹配
                    found = False
                    for k, v in POLISHED.items():
                        if k.replace(" ", "") == original.replace(" ", ""):
                            q["query"] = v
                            found = True
                            break
                    if not found:
                        print(f"  WARN: 未找到润色: {original}")
                q.pop("auto_generated", None)
                auto_queries.append(q)

    # 2. 合并
    all_queries = auto_queries + EXPLORE_QUERIES

    # 3. 写入 JSONL
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for q in all_queries:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")

    # 4. 统计
    print(f"自动生成（润色后）: {len(auto_queries)}")
    print(f"explore agent: {len(EXPLORE_QUERIES)}")
    print(f"总计: {len(all_queries)}")

    by_source = {}
    for q in all_queries:
        by_source[q["source"]] = by_source.get(q["source"], 0) + 1
    print("\n按来源:")
    for s, n in sorted(by_source.items()):
        print(f"  {s}: {n}")

    by_cat = {}
    for q in all_queries:
        by_cat[q["category"]] = by_cat.get(q["category"], 0) + 1
    print("\n按类别:")
    for s, n in sorted(by_cat.items()):
        print(f"  {s}: {n}")

    print(f"\n输出: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
