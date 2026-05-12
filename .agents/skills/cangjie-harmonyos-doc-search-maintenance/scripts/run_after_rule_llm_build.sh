#!/usr/bin/env bash
# 在 rule+llm 全量索引构建结束后执行：同步 V3 种子 → 可选校验图谱 → fusion AB → 写摘要。
# 用法：等 build_index_v3.py 不再运行时执行本脚本；或先 watch 进程再跑。
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS="$(cd "${SCRIPT_DIR}/../.." && pwd)"
DOC_SEARCH="${SKILLS}/cangjie-harmonyos-doc-search"
KG="${SKILLS}/knowledge-graph-template"
RECORDS="${SCRIPT_DIR}/../records"
INDEX_DIR="${INDEX_DIR:-${DOC_SEARCH}/index}"
GRAPH_DIR="${GRAPH_DIR:-${KG}/data}"
SEEDS_OUT="${SEEDS_OUT:-${RECORDS}/v3_seeds_15k_post_llm.json}"
AB_OUT="${AB_OUT:-${RECORDS}/ab-15k-after-rule-llm.json}"
# 可选：构建 stderr 日志路径（如 nohup 重定向），轮询时会 tail 末尾几行
BUILD_LOG="${BUILD_LOG:-}"

wait_for_build() {
  local pattern='build_index_v3.py.*--mode rule\+llm'
  local waited=0
  if pgrep -af "$pattern" >/dev/null 2>&1; then
    echo "检测到 rule+llm 构建仍在运行，每 60s 轮询一次（Ctrl+C 可中断仅等待，不影响已跑完的索引）。" >&2
    echo "提示: 构建时设置 CANGJIE_LLM_PROGRESS_FILE=/tmp/xxx.json 可写单行 JSON 进度；本脚本等待时会 cat 该文件。" >&2
    [[ -n "${BUILD_LOG}" ]] && echo "BUILD_LOG=${BUILD_LOG}（将 tail 末尾）" >&2
    while pgrep -af "$pattern" >/dev/null 2>&1; do
      echo "--- $(date -Is) 已等待 ${waited}s | 仍在运行 ---" >&2
      if [[ -n "${BUILD_LOG}" && -f "${BUILD_LOG}" ]]; then
        echo "[BUILD_LOG 末尾]" >&2
        tail -n 5 "${BUILD_LOG}" >&2 || true
      fi
      if [[ -n "${CANGJIE_LLM_PROGRESS_FILE}" && -f "${CANGJIE_LLM_PROGRESS_FILE}" ]]; then
        echo "[CANGJIE_LLM_PROGRESS_FILE]" >&2
        cat "${CANGJIE_LLM_PROGRESS_FILE}" >&2 || true
      fi
      sleep 60
      waited=$((waited + 60))
    done
  fi
  echo "构建进程已结束。" >&2
}

wait_for_build

echo "== sync_v3_to_graph → ${SEEDS_OUT}" >&2
python3 "${SCRIPT_DIR}/sync_v3_to_graph.py" \
  --index-dir "${INDEX_DIR}" \
  --output "${SEEDS_OUT}"

if [[ -f "${GRAPH_DIR}/merged/graph.json" ]]; then
  echo "== sync_v3_to_graph --validate" >&2
  python3 "${SCRIPT_DIR}/sync_v3_to_graph.py" \
    --validate \
    --graph "${GRAPH_DIR}/merged/graph.json" \
    --index-dir "${INDEX_DIR}" || true
fi

echo "== run_ab_eval → ${AB_OUT}" >&2
python3 "${SCRIPT_DIR}/run_ab_eval.py" \
  --eval-dir "${DOC_SEARCH}/evals" \
  --index-dir "${INDEX_DIR}" \
  --graph-dir "${GRAPH_DIR}" \
  --splits real_session,paraphrase,composition \
  --limit 8 \
  --output "${AB_OUT}"

export AB_OUT
python3 -c "
import json, os, pathlib
p = pathlib.Path(os.environ['AB_OUT'])
d = json.loads(p.read_text(encoding='utf-8'))
print('=== fusion AB 摘要 ===')
for name, payload in d.get('splits', {}).items():
    row = {k: round(payload[k]['recall_at_k'], 4) for k in ('v3', 'graphify', 'fusion')}
    print(name, row)
"

echo "完成。manifest: ${INDEX_DIR}/manifest.json ；AB: ${AB_OUT}" >&2
