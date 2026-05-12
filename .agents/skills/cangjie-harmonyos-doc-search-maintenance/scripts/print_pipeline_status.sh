#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS="$(cd "${SCRIPT_DIR}/../.." && pwd)"
DOC_SEARCH="${SKILLS}/cangjie-harmonyos-doc-search"
RECORDS="${SCRIPT_DIR}/../records"

BUILD_LOG="${BUILD_LOG:-/tmp/build_index_15k_full.err}"
BUILD_MANIFEST_TMP="${BUILD_MANIFEST_TMP:-/tmp/build_index_15k_full_manifest.json}"
AFTER_LOG="${AFTER_LOG:-/tmp/after_rule_llm_build.log}"
INDEX_MANIFEST="${INDEX_MANIFEST:-${DOC_SEARCH}/index/manifest.json}"
AB_OUT="${AB_OUT:-${RECORDS}/ab-15k-after-rule-llm.json}"

echo "=== pipeline status @ $(date -Is) ==="

build_pid="$(pgrep -f "build_index_v3.py --mode rule\\+llm" | head -n 1 || true)"
if [[ -n "${build_pid}" ]]; then
  echo "[build] running pid=${build_pid}"
  ps -o etime=,pcpu=,pmem=,args= -p "${build_pid}" || true
else
  echo "[build] not running"
fi

after_pid="$(pgrep -f "run_after_rule_llm_build.sh" | head -n 1 || true)"
if [[ -n "${after_pid}" ]]; then
  echo "[after] running pid=${after_pid}"
  ps -o etime=,pcpu=,pmem=,args= -p "${after_pid}" || true
else
  echo "[after] not running"
fi

if [[ -f "${BUILD_LOG}" ]]; then
  echo "[build_log] ${BUILD_LOG}"
  tail -n 3 "${BUILD_LOG}" || true
else
  echo "[build_log] missing: ${BUILD_LOG}"
fi

if [[ -f "${AFTER_LOG}" ]]; then
  echo "[after_log] ${AFTER_LOG}"
  tail -n 3 "${AFTER_LOG}" || true
else
  echo "[after_log] missing: ${AFTER_LOG}"
fi

if [[ -f "${BUILD_MANIFEST_TMP}" ]]; then
  echo "[tmp_manifest] bytes=$(wc -c < "${BUILD_MANIFEST_TMP}") path=${BUILD_MANIFEST_TMP}"
else
  echo "[tmp_manifest] missing: ${BUILD_MANIFEST_TMP}"
fi

if [[ -f "${INDEX_MANIFEST}" ]]; then
  echo "[index_manifest] path=${INDEX_MANIFEST}"
  python3 - <<'PY' "${INDEX_MANIFEST}" || true
import json, sys, pathlib
p = pathlib.Path(sys.argv[1])
d = json.loads(p.read_text(encoding="utf-8"))
mode = d.get("generation_mode")
counts = d.get("counts", {})
print(f"  generation_mode={mode}")
for k in ("llm_enriched_tasks", "llm_enriched_apis", "llm_enriched_examples", "llm_enriched_docs"):
    print(f"  {k}={counts.get(k)}")
PY
else
  echo "[index_manifest] missing: ${INDEX_MANIFEST}"
fi

if [[ -f "${AB_OUT}" ]]; then
  echo "[ab_after_rule_llm] exists: ${AB_OUT}"
else
  echo "[ab_after_rule_llm] missing: ${AB_OUT}"
fi

