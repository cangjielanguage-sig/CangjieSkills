#!/usr/bin/env python3
"""从 eval_queries_full.jsonl 分层抽样生成代表性测评集。

策略：
  - 按 category（5 类）× card_type（4 类）分层
  - 每层均匀抽样，确保覆盖面
  - 同一 card_id 只取一条（避免同卡多 query 的冗余）
  - 输出格式与 eval_queries.jsonl 兼容
"""

import argparse
import json
import random
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
EVALS_DIR = SKILL_DIR / "evals"
DEFAULT_INPUT = EVALS_DIR / "search" / "eval_queries_full.jsonl"
DEFAULT_OUTPUT = EVALS_DIR / "search" / "eval_queries_sampled.jsonl"

CATEGORIES = ["exact", "semi-structured", "natural", "error-driven", "exploration"]
CARD_TYPES = ["api", "task", "example", "doc"]

# 噪声 query 过滤规则
_NOISE_PREFIXES = (".abstract", ".overview")
_NOISE_EXACT = {".abstract", ".overview", "接口", "类", "函数", "枚举", "基础类型定义", "示例代码", "场景示例"}
_NOISE_CONTAINS = ["general 相关文档"]


def _is_noise(query: str) -> bool:
    """判断 query 是否为自动生成的噪声。"""
    q = query.strip()
    # 过短或纯路径名
    if len(q) < 3:
        return True
    # 精确匹配噪声
    if q in _NOISE_EXACT:
        return True
    # 以 .abstract/.overview 开头且紧跟的不是有意义的内容
    for prefix in _NOISE_PREFIXES:
        if q == prefix or q.startswith(prefix + " ") and len(q) < len(prefix) + 5:
            return True
        # .abstract class/doc/example + 英文摘要
        if q.startswith(prefix + " class ") or q.startswith(prefix + " doc ") or q.startswith(prefix + " example "):
            return True
    # "general 相关文档" 模板
    for pattern in _NOISE_CONTAINS:
        if pattern in q:
            return True
    # "X 使用异常 怎么排查" 中 X 是路径组件
    if "使用异常 怎么排查" in q:
        topic = q.split(" 使用异常 怎么排查")[0].strip()
        if topic in _NOISE_EXACT or topic.startswith("."):
            return True
    # 英文摘要混入
    if q.startswith("This directory") or q.startswith("This folder") or q.startswith("A "):
        return True
    return False


def load_queries(path: Path) -> list[dict]:
    queries = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                queries.append(json.loads(line))
    return queries


def stratified_sample(
    queries: list[dict],
    total_target: int,
    seed: int = 42,
) -> list[dict]:
    """按 category × card_type 分层抽样。"""
    rng = random.Random(seed)

    # 按 (category, card_type) 分桶，每桶内按 card_id 去重
    buckets: dict[tuple[str, str], list[dict]] = defaultdict(list)
    seen_cards: dict[tuple[str, str], set[str]] = defaultdict(set)

    for q in queries:
        cat = q.get("category", "unknown")
        ct = q.get("card_type", "unknown")
        cid = q.get("card_id", "")
        key = (cat, ct)
        if cid and cid in seen_cards[key]:
            continue
        if cid:
            seen_cards[key].add(cid)
        buckets[key].append(q)

    # 计算每层配额：按 category 均分
    cat_quota = {cat: total_target // len(CATEGORIES) for cat in CATEGORIES}
    # 余数分配给前几个 category
    remainder = total_target - sum(cat_quota.values())
    for i, cat in enumerate(CATEGORIES):
        if i < remainder:
            cat_quota[cat] += 1

    # 每个 category 内，按 card_type 比例分配
    sampled: list[dict] = []
    for cat in CATEGORIES:
        # 统计该 category 下各 card_type 的数量
        cat_total = sum(len(buckets.get((cat, ct), [])) for ct in CARD_TYPES)
        if cat_total == 0:
            continue

        cat_sampled = []
        remaining = cat_quota[cat]
        for ct in CARD_TYPES:
            pool = buckets.get((cat, ct), [])
            if not pool:
                continue
            # 按比例分配，至少 1 条
            proportion = len(pool) / cat_total
            n = max(1, round(proportion * cat_quota[cat]))
            n = min(n, len(pool), remaining)
            cat_sampled.extend(rng.sample(pool, n))
            remaining -= n

        # 如果还没凑够，从该 category 所有池中补
        if remaining > 0:
            already = {id(q) for q in cat_sampled}
            all_pool = [q for ct in CARD_TYPES for q in buckets.get((cat, ct), []) if id(q) not in already]
            if all_pool:
                cat_sampled.extend(rng.sample(all_pool, min(remaining, len(all_pool))))

        sampled.extend(cat_sampled)

    rng.shuffle(sampled)
    return sampled


def print_stats(sample: list[dict]) -> None:
    print(f"抽样结果: {len(sample)} 条\n")

    # 按 category
    cats = defaultdict(int)
    for q in sample:
        cats[q.get("category", "unknown")] += 1
    print("按 category 分布:")
    for cat in CATEGORIES:
        print(f"  {cat:20s}: {cats.get(cat, 0)}")

    # 按 card_type
    cts = defaultdict(int)
    for q in sample:
        cts[q.get("card_type", "unknown")] += 1
    print("\n按 card_type 分布:")
    for ct in CARD_TYPES:
        print(f"  {ct:20s}: {cts.get(ct, 0)}")

    # 按 source 前缀
    prefixes = defaultdict(int)
    for q in sample:
        for p in q.get("expected_paths", []):
            prefixes[p.split("/")[0]] += 1
    print("\n按 source 前缀 (路径引用次数):")
    for k, v in sorted(prefixes.items(), key=lambda x: -x[1]):
        print(f"  {k:20s}: {v}")

    # unique card_id
    card_ids = {q.get("card_id", "") for q in sample}
    print(f"\nunique card_id: {len(card_ids)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="从全量评测集分层抽样")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="全量评测集路径")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="抽样输出路径")
    parser.add_argument("--size", type=int, default=300, help="目标抽样数量")
    parser.add_argument("--seed", type=int, default=42, help="随机种子")
    parser.add_argument("--dry-run", action="store_true", help="只统计不写文件")
    args = parser.parse_args()

    queries = load_queries(Path(args.input))
    print(f"全量集: {len(queries)} 条")

    # 质量过滤
    clean = [q for q in queries if not _is_noise(q["query"])]
    noise_count = len(queries) - len(clean)
    print(f"过滤噪声: {noise_count} 条 ({noise_count / len(queries) * 100:.1f}%)")
    print(f"有效集: {len(clean)} 条\n")

    sample = stratified_sample(clean, args.size, seed=args.seed)
    print_stats(sample)

    if not args.dry_run:
        with open(args.output, "w", encoding="utf-8") as f:
            for q in sample:
                # 只保留 eval_bench.py 需要的字段
                out = {
                    "query": q["query"],
                    "expected_paths": q["expected_paths"],
                    "category": q.get("category", "unknown"),
                }
                f.write(json.dumps(out, ensure_ascii=False) + "\n")
        print(f"\n已写入: {args.output}")


if __name__ == "__main__":
    main()
