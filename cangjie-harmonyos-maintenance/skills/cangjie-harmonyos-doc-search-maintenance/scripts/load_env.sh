#!/usr/bin/env bash
set -euo pipefail

API_FILE="${CANGJIE_LLM_API_FILE:-$HOME/.config/cangjie-skills/api.txt}"

if [[ ! -f "$API_FILE" ]]; then
  echo "LLM API 文件不存在: $API_FILE" >&2
  echo "请先把本地 key 文件复制到 ~/.config/cangjie-skills/api.txt，并 chmod 600" >&2
  return 1 2>/dev/null || exit 1
fi

export OPENAI_BASE_URL="${OPENAI_BASE_URL:-https://api.modelarts-maas.com/openai/v1}"
export OPENAI_MODEL="${OPENAI_MODEL:-deepseek-v3.2}"
export LLM_CONCURRENCY="${LLM_CONCURRENCY:-64}"
export LLM_CACHE_DIR="${LLM_CACHE_DIR:-/data/llm-cache-persistent}"
export GRAPHIFY_CACHE_DIR="${GRAPHIFY_CACHE_DIR:-/data/graphify-cache-persistent}"

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  export OPENAI_API_KEY="$(grep -E '^(OPENAI_API_KEY|API_KEY|api_key)=' "$API_FILE" | tail -n 1 | sed -E 's/^[^=]+=//; s/^"//; s/"$//' || true)"
fi

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  export OPENAI_API_KEY="$(grep -E 'sk-|[A-Za-z0-9_-]{24,}' "$API_FILE" | head -n 1 | sed -E 's/.*(sk-[A-Za-z0-9_-]+).*/\1/' || true)"
fi

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  echo "未能从 $API_FILE 读取 OPENAI_API_KEY" >&2
  return 1 2>/dev/null || exit 1
fi
