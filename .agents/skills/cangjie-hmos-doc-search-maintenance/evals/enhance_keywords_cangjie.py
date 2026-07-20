#!/usr/bin/env python3
"""enhance_keywords_cangjie.py — GLM-5.2 语义提取增强 keywords_cangjie.json

原则:
  - 关键词从 query 文本 + intent 提取，不看 acceptable_paths
  - 禁止路径片段 (cj-std, class_, .md 等)
  - 禁止泛化词 (使用, 怎么, API, function, 区别 等)
  - 中英对称: 概念类 query 有中英双语覆盖
  - 噪声门禁: 匹配 >20% 文档的词由 noise_filter.py 后续过滤
"""
import json
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parent
DATASET = EVAL_DIR / "datasets" / "eval_queries_cangjie.jsonl"
OUTPUT = EVAL_DIR / "keywords" / "keywords_cangjie.json"

# === 99 条 GLM-5.2 语义提取的关键词 ===
# 格式: (core_zh, core_en, ctx_zh, ctx_en, syn_zh, syn_en)
KEYWORDS = {
    # === api_lookup (1-16) ===
    1:  (["HashMap"], ["HashMap"], ["键值对"], ["put","store"], [], []),
    2:  (["ArrayList"], ["ArrayList"], ["添加","删除","元素"], ["add","remove","element"], [], []),
    3:  (["String"], ["String","string"], ["字符串"], ["method"], [], []),
    4:  (["Array"], ["Array","array"], ["数组","创建","遍历"], ["create","iterate"], [], []),
    5:  (["File"], ["File","file"], ["读写","文件"], ["read","write"], [], []),
    6:  (["BufferedInputStream"], ["BufferedInputStream"], ["缓冲","输入流","读取"], ["buffer","stream","read"], [], []),
    7:  (["Mutex"], ["Mutex","mutex"], ["互斥锁","加锁","解锁"], ["lock","unlock"], [], []),
    8:  (["DateTime"], ["DateTime"], ["当前时间"], ["time","now"], [], []),
    9:  (["IPAddress"], ["IPAddress"], ["IP地址","解析"], ["IP","address","parse"], [], []),
    10: (["sort"], ["sort"], ["排序"], ["sort","ordering"], [], []),
    11: (["JsonArray"], ["JsonArray"], ["创建","遍历"], ["JSON","array"], [], []),
    12: (["JsonObject"], ["JsonObject"], ["读取","修改","字段"], ["JSON","object","field"], [], []),
    13: (["HttpRequest"], ["HttpRequest"], ["请求头","请求体"], ["HTTP","request","header","body"], [], []),
    14: (["SM4"], ["SM4"], ["加密"], ["encrypt","cipher"], [], []),
    15: (["Logger"], ["Logger"], ["日志","级别"], ["log","level"], [], []),
    16: (["DataModel"], ["DataModel"], ["序列化"], ["serialize"], [], []),

    # === enumeration (17-31) ===
    17: ([], ["collection","data structure"], ["集合","数据结构"], [], [], []),
    18: ([], ["core","type"], ["核心类型"], [], [], []),
    19: ([], ["io","stream"], ["输入输出流"], [], [], []),
    20: ([], ["net","network","socket"], ["网络"], [], [], []),
    21: ([], ["sync","mutex","semaphore"], ["线程同步","同步原语"], [], [], []),
    22: ([], ["time","DateTime","duration"], ["时间","日期"], [], [], []),
    23: ([], ["fs","file"], ["文件系统"], [], [], []),
    24: ([], ["unittest","test","assert"], ["测试","断言"], [], [], []),
    25: ([], ["data type","integer","float","bool"], ["基本数据类型"], [], [], []),
    26: (["函数"], ["function","lambda","closure"], [], [], [], []),
    27: ([], ["generic","constraint","where"], ["泛型","约束"], [], [], []),
    28: ([], ["macro","quote"], ["宏"], [], [], []),
    29: ([], ["concurrency","thread","spawn"], ["并发"], [], [], []),
    30: (["异常"], ["exception","error","try","catch"], [], [], [], []),
    31: ([], ["enum","match","pattern"], ["枚举","模式匹配"], [], [], []),

    # === semantic_fuzzy (32-41) ===
    32: (["字符串"], ["String","string"], [], [], ["字符串类型"], []),
    33: (["类"], ["class"], [], [], ["类定义"], []),
    34: (["接口"], ["interface"], [], [], ["接口实现"], []),
    35: (["泛型"], ["generic","generics"], [], [], ["泛型编程"], []),
    36: (["异常","异常处理"], ["exception","try","catch"], [], [], [], []),
    37: (["并发","多线程"], ["concurrency","thread","spawn"], [], [], [], []),
    38: (["宏"], ["macro"], [], [], ["宏定义"], []),
    39: (["扩展"], ["extension","extend"], [], [], ["扩展机制"], []),
    40: (["反射","动态特性"], ["reflection","annotation","dynamic"], [], [], [], []),
    41: (["互操作"], ["FFI","interop","C"], [], [], ["C互操作"], []),

    # === how_to tools (42-49) ===
    42: (["cjpm"], ["cjpm"], ["依赖包"], ["package","dependency"], [], []),
    43: (["cjdb"], ["cjdb"], ["调试"], ["debug","debugger"], [], []),
    44: (["cjfmt"], ["cjfmt"], ["格式化"], ["format","formatter"], [], []),
    45: (["cjlint"], ["cjlint"], ["代码规范","检查"], ["lint","check"], [], []),
    46: (["cjcov"], ["cjcov"], ["覆盖率"], ["coverage"], [], []),
    47: (["cjprof"], ["cjprof"], ["性能分析"], ["profile","profiler"], [], []),
    48: (["堆栈跟踪","崩溃"], ["stack trace","crash"], [], [], [], []),
    49: (["chir_dis"], ["chir_dis"], ["反序列化"], ["deserialize","CHIR"], [], []),

    # === how_to std (50-57) ===
    50: (["Regex"], ["Regex"], ["正则","匹配","邮箱"], ["regex","pattern","match","email"], [], []),
    51: (["Random"], ["Random"], ["随机数"], ["random"], [], []),
    52: (["sort"], ["sort"], ["数组","排序"], ["sort","ordering"], [], []),
    53: (["Directory"], ["Directory"], ["遍历","目录","文件"], ["directory","traverse","walk"], [], []),
    54: (["Thread"], ["Thread"], ["线程","创建"], ["thread","spawn","create"], [], []),
    55: (["Exception"], ["Exception"], ["异常","捕获"], ["exception","catch","try"], [], []),
    56: (["字符串","整数","转换"], ["parse","convert","string","int"], [], [], [], []),
    57: (["StringBuilder"], ["StringBuilder"], ["拼接","字符串"], ["concat","append"], [], []),

    # === how_to stdx (58-65) ===
    58: (["HttpClient"], ["HttpClient"], ["GET请求","网页"], ["HTTP","GET","client"], [], []),
    59: (["TlsSocket"], ["TlsSocket"], ["证书","私钥","TLS"], ["TLS","certificate","key"], [], []),
    60: (["zlib"], ["zlib"], ["压缩","解压","gzip"], ["gzip","compress","decompress"], [], []),
    61: (["base64"], ["base64"], ["字节数组","编码"], ["encode","decode"], [], []),
    62: (["JsonValue"], ["JsonValue"], ["JSON","解析","字段"], ["JSON","parse"], [], []),
    63: (["Logger"], ["Logger"], ["日志","配置"], ["log","config"], [], []),
    64: (["URL"], ["URL"], ["解析","协议","路径"], ["parse","protocol"], [], []),
    65: (["DataModel"], ["DataModel"], ["序列化","反序列化"], ["serialize","deserialize"], [], []),

    # === workflow (66-71) ===
    66: (["密钥","加密","解密"], ["key","encrypt","decrypt","RSA","SM4"], [], [], [], []),
    67: (["Logger"], ["Logger"], ["日志级别","输出"], ["level","SimpleLogger"], [], []),
    68: (["ServerBuilder","Server"], ["ServerBuilder","Server"], ["路由"], ["HTTP","server","route","handler"], [], []),
    69: (["TlsSocket"], ["TlsSocket"], ["握手","客户端","服务端"], ["TLS","handshake","client","server"], [], []),
    70: (["JsonReader"], ["JsonReader"], ["流式","解析","token"], ["JSON","stream","reader","token"], [], []),
    71: (["压缩","解压"], ["CompressOutputStream","DecompressInputStream","compress","decompress"], [], [], [], []),

    # === comparison (72-83) ===
    72: (["ArrayList","LinkedList"], ["ArrayList","LinkedList"], [], [], [], []),
    73: (["Int","Int64"], ["Int","Int64"], [], [], [], []),
    74: (["Mutex","Semaphore"], ["Mutex","Semaphore"], [], [], [], []),
    75: (["sort","stableSort"], ["sort","stableSort"], [], [], [], []),
    76: (["类","接口"], ["class","interface"], [], [], [], []),
    77: (["结构体","类"], ["struct","class"], [], [], [], []),
    78: (["枚举","模式匹配"], ["enum","match","pattern"], [], [], [], []),
    79: (["let","const"], ["let","const"], [], [], [], []),
    80: (["泛型","子类型"], ["generic","subtype"], [], [], [], []),
    81: (["闭包"], ["closure","lambda"], [], [], [], []),
    82: (["同步","异步"], ["sync","async","concurrent"], [], [], [], []),
    83: (["互操作"], ["FFI","interop"], [], [], [], []),

    # === reverse_lookup (84-87) ===
    84: (["字符串","整数","转换"], ["parse","convert","string","int"], [], [], [], []),
    85: (["StringBuilder"], ["StringBuilder"], ["拼接","字符串"], ["concat","append"], [], []),
    86: (["JsonReader"], ["JsonReader"], ["流式","解析","JSON"], ["stream","parse","JSON"], [], []),
    87: (["base64"], ["base64"], ["编码","解码"], ["encode","decode"], [], []),

    # === composition (88-91) ===
    88: (["File","BufferedInputStream"], ["File","BufferedInputStream"], ["读取","大文件"], ["read"], [], []),
    89: (["Regex","String"], ["Regex","String"], ["验证","邮箱"], ["regex","pattern","email"], [], []),
    90: (["Logger","DataModel"], ["Logger","DataModel"], ["序列化","日志"], ["serialize","log"], [], []),
    91: (["JsonArray","URL"], ["JsonArray","URL"], ["解析","参数"], ["JSON","parse"], [], []),

    # === constrained (92-94) ===
    92: (["ConcurrentHashMap"], ["ConcurrentHashMap"], ["并发","线程安全"], ["concurrent","thread-safe","HashMap"], [], []),
    93: (["TlsSocket"], ["TlsSocket"], ["单向认证","连接"], ["TLS","one-way","connect"], [], []),
    94: (["只读","遍历","集合"], ["read-only","ReadOnlyList","iterate"], [], [], [], []),

    # === cross_ecosystem (95-96) ===
    95: (["HttpClient","NetworkKit"], ["HttpClient","NetworkKit"], ["HTTP请求"], ["HTTP","request"], [], []),
    96: (["文件操作"], ["fs","CoreFileKit","file"], [], [], [], []),

    # === performance_boundary (97-99) ===
    97: (["Array","ArrayList"], ["Array","ArrayList"], ["大量数据"], ["performance","benchmark"], [], []),
    98: (["HashMap","TreeMap"], ["HashMap","TreeMap"], ["查找"], ["lookup","search","performance"], [], []),
    99: (["zlib"], ["zlib"], ["压缩级别"], ["compress","level","performance"], [], []),
}


def main():
    # 读取 query 信息
    with open(DATASET, "r", encoding="utf-8") as f:
        queries = [json.loads(line) for line in f]

    result = {}
    for i, q in enumerate(queries, 1):
        if i not in KEYWORDS:
            print(f"  WARN: Q{i} missing keywords")
            continue
        czh, cen, xzh, xen, szh, sen = KEYWORDS[i]
        # 去重
        czh = list(dict.fromkeys(czh))
        cen = list(dict.fromkeys(cen))
        xzh = list(dict.fromkeys(xzh))
        xen = list(dict.fromkeys(xen))
        szh = list(dict.fromkeys(szh))
        sen = list(dict.fromkeys(sen))
        ken = list(dict.fromkeys(cen + xen + sen))
        kzh = list(dict.fromkeys(czh + xzh + szh))
        result[str(i)] = {
            "query": q["query"],
            "intent": q["intent"],
            "category": q["category"],
            "core": {"zh": czh, "en": cen},
            "context": {"zh": xzh, "en": xen},
            "synonym": {"zh": szh, "en": sen},
            "keywords_en": ken,
            "keywords_zh": kzh,
        }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"生成: {len(result)} 条 keywords")
    print(f"输出: {OUTPUT}")

    # 统计
    total_en = sum(len(v["keywords_en"]) for v in result.values())
    total_zh = sum(len(v["keywords_zh"]) for v in result.values())
    print(f"总关键词: en={total_en}, zh={total_zh}, avg_en={total_en/len(result):.1f}, avg_zh={total_zh/len(result):.1f}")

    empty_en = sum(1 for v in result.values() if not v["keywords_en"])
    empty_zh = sum(1 for v in result.values() if not v["keywords_zh"])
    print(f"空值: en={empty_en}, zh={empty_zh}")


if __name__ == "__main__":
    main()
