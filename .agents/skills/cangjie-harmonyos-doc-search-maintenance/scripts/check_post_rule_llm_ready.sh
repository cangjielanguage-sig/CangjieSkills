#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS="$(cd "${SCRIPT_DIR}/../.." && pwd)"
DOC_SEARCH="${SKILLS}/cangjie-harmonyos-doc-search"
RECORDS="${SCRIPT_DIR}/../records"

INDEX_MANIFEST="${DOC_SEARCH}/index/manifest.json"
AB_AFTER="${RECORDS}/ab-15k-after-rule-llm.json"

echo "== post rule+llm readiness check =="

if pgrep -f "build_index_v3.py --mode rule\+llm" >/dev/null 2>&1; then
  echo "[WARN] rule+llm 构建仍在运行"
else
  echo "[OK] rule+llm 构建进程已结束"
fi

if [[ ! -f "${INDEX_MANIFEST}" ]]; then
  echo "[ERR] manifest 缺失: ${INDEX_MANIFEST}"
  exit 2
fi

python3 - <<'PY' "${INDEX_MANIFEST}"
import json, pathlib, sys
p = pathlib.Path(sys.argv[1])
d = json.loads(p.read_text(encoding="utf-8"))
mode = d.get("generation_mode")
counts = d.get("counts", {})
print(f"[manifest] generation_mode={mode}")
for k in ("llm_enriched_tasks","llm_enriched_apis","llm_enriched_examples","llm_enriched_docs"):
    print(f"[manifest] {k}={counts.get(k)}")
if mode != "rule+llm":
    raise SystemExit(3)
if (counts.get("llm_enriched_tasks", 0) or 0) <= 0 and (counts.get("llm_enriched_apis", 0) or 0) <= 0:
    raise SystemExit(4)
PY

if [[ -f "${AB_AFTER}" ]]; then
  echo "[OK] AB 产物存在: ${AB_AFTER}"
else
  echo "[WARN] AB 产物未生成: ${AB_AFTER}"
fi

echo "== check done =="
