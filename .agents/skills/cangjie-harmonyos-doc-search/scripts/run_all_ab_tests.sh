#!/bin/bash
# 批量运行所有评测集的AB测试（排除全量种子库）

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVALS_DIR="$SCRIPT_DIR/../evals"
OUTPUT_DIR="$SCRIPT_DIR/ab-results-all"

mkdir -p "$OUTPUT_DIR"

# 定义所有评测集（排除全量种子库）
EVAL_SETS=(
    "eval_queries.jsonl"
    "eval_queries_user.jsonl"
    "eval_queries_user_appdev.jsonl"
    "eval_queries_user_appdev_batch2.jsonl"
    "eval_queries_user_appdev_batch3.jsonl"
    "eval_queries_user_appdev_next.jsonl"
    "eval_queries_user_appdev_frozen.jsonl"
    "eval_queries_user_appdev_blind.jsonl"
    "eval_queries_user_appdev_blind_20260424.jsonl"
    "eval_queries_app_agent_dev.jsonl"
    "eval_queries_sampled.jsonl"
)

# 汇总文件
SUMMARY_FILE="$OUTPUT_DIR/summary.csv"
echo "eval_set,count,openviking_success@5,v3_success@5,openviking_mrr,v3_mrr,openviking_latency_p50,v3_latency_p50" > "$SUMMARY_FILE"

for eval_set in "${EVAL_SETS[@]}"; do
    eval_path="$EVALS_DIR/$eval_set"
    output_subdir="$OUTPUT_DIR/${eval_set%.jsonl}"

    echo "=========================================="
    echo "测试: $eval_set"
    echo "=========================================="

    if [ ! -f "$eval_path" ]; then
        echo "警告: $eval_path 不存在，跳过"
        continue
    fi

    # 创建输出目录
    mkdir -p "$output_subdir"

    # 运行AB测试
    cd "$SCRIPT_DIR"
    python3 ab_test_openviking_vs_v3.py \
        --eval-set "$eval_path" \
        --output-dir "$output_subdir" \
        2>&1 | tee "$output_subdir/output.log"

    # 提取结果到汇总
    if [ -f "$output_subdir/summary.json" ]; then
        count=$(python3 -c "import json; d=json.load(open('$output_subdir/summary.json')); print(d['groups']['A']['overall']['count'])")
        ov_s5=$(python3 -c "import json; d=json.load(open('$output_subdir/summary.json')); print(d['groups']['A']['overall']['success@5'])")
        v3_s5=$(python3 -c "import json; d=json.load(open('$output_subdir/summary.json')); print(d['groups']['B']['overall']['success@5'])")
        ov_mrr=$(python3 -c "import json; d=json.load(open('$output_subdir/summary.json')); print(d['groups']['A']['overall']['mrr'])")
        v3_mrr=$(python3 -c "import json; d=json.load(open('$output_subdir/summary.json')); print(d['groups']['B']['overall']['mrr'])")
        ov_lat=$(python3 -c "import json; d=json.load(open('$output_subdir/summary.json')); print(d['groups']['A']['overall']['latency_p50_ms'])")
        v3_lat=$(python3 -c "import json; d=json.load(open('$output_subdir/summary.json')); print(d['groups']['B']['overall']['latency_p50_ms'])")
        echo "$eval_set,$count,$ov_s5,$v3_s5,$ov_mrr,$v3_mrr,$ov_lat,$v3_lat" >> "$SUMMARY_FILE"
    fi

    echo ""
done

echo "=========================================="
echo "所有测试完成！"
echo "汇总报告: $SUMMARY_FILE"
echo "详细结果: $OUTPUT_DIR/"
echo "=========================================="
