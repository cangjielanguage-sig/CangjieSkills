#!/usr/bin/env python3
"""noise_filter.py — 噪声门禁: 扫描 cangjie-docs 语料，过滤匹配率 >20% 的关键词

流程:
  1. 扫描 cangjie-docs/ 全部 .md 文件，统计每个关键词的文档匹配率
  2. 匹配率 > 20% → 标记为噪声，从 keywords_cangjie.json 中删除
  3. 输出噪声报告 + 过滤后的 keywords_cangjie.json
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

EVAL_DIR = Path(__file__).resolve().parent
DOCS_DIR = EVAL_DIR.parent.parent / "cangjie-docs"
KEYWORDS_PATH = EVAL_DIR / "keywords" / "keywords_cangjie.json"
NOISE_THRESHOLD = 0.20  # 20%


def scan_corpus(docs_dir: Path) -> tuple[dict, int]:
    """扫描语料，返回 (词→文档数映射, 总文档数)。"""
    word_doc_count = defaultdict(int)
    total_docs = 0

    for md_file in docs_dir.rglob("*.md"):
        if md_file.name.startswith("."):
            continue
        total_docs += 1
        try:
            content = md_file.read_text(encoding="utf-8", errors="replace").lower()
        except Exception:
            continue
        # 对每个词做子串匹配（lowercase）
        # 为了效率，先收集所有词再统一查
        # 但 99 条 query 的关键词总数不多（~300），直接逐个查
        for word in unique_words:
            if word.lower() in content:
                word_doc_count[word] += 1

    return word_doc_count, total_docs


def main():
    global unique_words

    # 1. 读取 keywords
    with open(KEYWORDS_PATH, "r", encoding="utf-8") as f:
        keywords = json.load(f)

    # 2. 收集所有唯一关键词
    unique_words = set()
    for v in keywords.values():
        unique_words.update(v["keywords_en"])
        unique_words.update(v["keywords_zh"])
    print(f"唯一关键词数: {len(unique_words)}")

    # 3. 扫描语料
    print(f"扫描语料: {DOCS_DIR}")
    word_doc_count, total_docs = scan_corpus(DOCS_DIR)
    print(f"总文档数: {total_docs}")
    print(f"阈值: {NOISE_THRESHOLD*100:.0f}% (匹配 >{int(total_docs*NOISE_THRESHOLD)} 文档的词将被过滤)")
    print()

    # 4. 识别噪声词
    noise_words = []
    for word in sorted(unique_words):
        count = word_doc_count.get(word, 0)
        rate = count / total_docs if total_docs > 0 else 0
        if rate > NOISE_THRESHOLD:
            noise_words.append((word, count, rate))

    print(f"噪声词数: {len(noise_words)}")
    if noise_words:
        print("噪声词清单:")
        for word, count, rate in noise_words:
            print(f"  {word}: {count}/{total_docs} ({rate*100:.1f}%)")
    print()

    # 5. 噪声过滤: 仅过滤 context/synonym，保留 core（core 是用户搜索的主词）
    noise_set = set(w[0] for w in noise_words)
    removed_total = 0
    noise_in_core = []  # 记录 core 中的噪声词（仅报告，不删除）
    for key, v in keywords.items():
        # context 和 synonym: 过滤噪声词
        for section in ("context", "synonym"):
            for lang in ("en", "zh"):
                before = len(v[section][lang])
                v[section][lang] = [w for w in v[section][lang] if w not in noise_set]
                removed_total += before - len(v[section][lang])
        # core: 不过滤，但记录噪声词（报告用）
        for lang in ("en", "zh"):
            for w in v["core"][lang]:
                if w in noise_set:
                    noise_in_core.append((key, w))
        # 重建 keywords_en / keywords_zh = core + context + synonym
        v["keywords_en"] = list(dict.fromkeys(
            v["core"]["en"] + v["context"]["en"] + v["synonym"]["en"]
        ))
        v["keywords_zh"] = list(dict.fromkeys(
            v["core"]["zh"] + v["context"]["zh"] + v["synonym"]["zh"]
        ))

    print(f"删除关键词总数: {removed_total}")

    # 6. 检查过滤后是否有空值
    empty_en = sum(1 for v in keywords.values() if not v["keywords_en"])
    empty_zh = sum(1 for v in keywords.values() if not v["keywords_zh"])
    if empty_en or empty_zh:
        print(f"警告: 过滤后空值 en={empty_en}, zh={empty_zh}")
        for key, v in keywords.items():
            if not v["keywords_en"] or not v["keywords_zh"]:
                print(f"  Q{key}: en={v['keywords_en']}, zh={v['keywords_zh']}")
    else:
        print("过滤后无空值")

    # 7. 写回
    with open(KEYWORDS_PATH, "w", encoding="utf-8") as f:
        json.dump(keywords, f, ensure_ascii=False, indent=2)
    print(f"\n已写回: {KEYWORDS_PATH}")

    # 8. 最终统计
    total_en = sum(len(v["keywords_en"]) for v in keywords.values())
    total_zh = sum(len(v["keywords_zh"]) for v in keywords.values())
    print(f"过滤后: en={total_en} (avg {total_en/len(keywords):.1f}), zh={total_zh} (avg {total_zh/len(keywords):.1f})")


if __name__ == "__main__":
    main()
