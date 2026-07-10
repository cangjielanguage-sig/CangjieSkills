#!/usr/bin/env python3
"""migrate_harmonyos_eval.py — 迁移 harmonyos 评测集到统一目录

操作:
  1. 读取 graph/evals/datasets/eval_queries_comprehensive_deduped.jsonl (192 条)
  2. 加 source="harmonyos" 字段
  3. 统一 capability 为 "harmonyos/{domain}" 格式
  4. 移除 acceptable_paths_count (冗余)
  5. 输出到 evals/datasets/eval_queries_harmonyos.jsonl
  6. 同步处理 dev/validation 拆分
"""
import json
from pathlib import Path

MAINT_DIR = Path(__file__).resolve().parent.parent  # cangjie-hmos-doc-search-maintenance/
OLD_DATASETS = MAINT_DIR / "graph" / "evals" / "datasets"
NEW_DATASETS = MAINT_DIR / "evals" / "datasets"


def process_file(old_path: Path, new_path: Path):
    """处理单个 JSONL 文件: 加 source + 统一 capability + 移除冗余字段。"""
    count = 0
    with open(old_path, "r", encoding="utf-8") as fin:
        lines = fin.readlines()

    with open(new_path, "w", encoding="utf-8") as fout:
        for line in lines:
            q = json.loads(line)
            # 加 source 字段
            q["source"] = "harmonyos"
            # 统一 capability 格式
            cap = q.get("capability", "")
            if cap and "/" not in cap:
                q["capability"] = f"harmonyos/{cap}"
            # 移除冗余字段
            q.pop("acceptable_paths_count", None)
            fout.write(json.dumps(q, ensure_ascii=False) + "\n")
            count += 1
    return count


def main():
    NEW_DATASETS.mkdir(parents=True, exist_ok=True)

    # 主集
    files = [
        ("eval_queries_comprehensive_deduped.jsonl", "eval_queries_harmonyos.jsonl"),
        ("eval_queries_comprehensive_dev.jsonl", "eval_queries_harmonyos_dev.jsonl"),
        ("eval_queries_comprehensive_validation.jsonl", "eval_queries_harmonyos_validation.jsonl"),
        ("eval_queries_comprehensive.jsonl", "eval_queries_harmonyos_full.jsonl"),
    ]

    for old_name, new_name in files:
        old_path = OLD_DATASETS / old_name
        new_path = NEW_DATASETS / new_name
        if not old_path.exists():
            print(f"  SKIP: {old_name} (not found)")
            continue
        count = process_file(old_path, new_path)
        print(f"  {old_name} -> {new_name}: {count} queries")

    print(f"\n输出目录: {NEW_DATASETS}")


if __name__ == "__main__":
    main()
