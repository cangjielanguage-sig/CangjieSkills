"""LLM 语义增强模块 — 智能分批、全量读取、结果合并。"""
from __future__ import annotations

import json
import sys
import threading
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional

API_KEY = "xxxx"
API_BASE = "xxxxx"
MODEL = "qwen3.6-plus"
MAX_BATCH_CHARS = 40000
LLM_TIMEOUT = 600




def safe_read_text(path: Path) -> str:
    """读取文件内容，自动处理 Windows 长路径问题。"""
    full = str(path.resolve())
    if sys.platform == "win32" and len(full) > 240:
        full = "\\\\?\\" + full
    return Path(full).read_text(encoding="utf-8", errors="replace")

EXTRACTION_PROMPT = """You are a semantic extraction agent for the Cangjie HarmonyOS knowledge graph.
This graph is used by AI coding agents to help developers find documentation when building HarmonyOS apps with Cangjie.

Your task: READ EACH document's FULL content below, then generate HIGH-QUALITY search metadata.
Output a JSON array where each element corresponds to one file.

Output ONLY valid JSON:
[{{
  "source_file": "<exact path from input>",
  "label": "<1-5 English words: core concept label, KEEP original if it is an API/class/component name>",
  "label_zh": "<2-10 Chinese chars: core concept label, KEEP original if it already contains searchable terms>",
  "description_zh": "<15-40 Chinese chars: direct functional statement>",
  "description_en": "<15-40 words: dense English technical terms stack>",
  "keywords_zh": ["5-10 Chinese keywords"],
  "keywords_en": ["5-10 English keywords"]
}}]

=== Field Rules ===

label: 1-5 English words that capture the MOST CORE concept of this doc.
- CRITICAL RULE: If the original label is already an exact API name, class name, or component name (e.g. "ClientCert", "Grid", "NotificationProgress", "AppStorage"), KEEP IT EXACTLY — do NOT replace with a semantic description like "Mutual TLS Configuration" or "Grid Container". Developers search by API names, not by semantic descriptions.
- ONLY overwrite when the original label is a file-path style (e.g. "cj-apis-values_bucket") or a generic/non-searchable string — then replace with the exact API/class name from doc content
- For concept-level docs without a single API name, use a concise English phrase (e.g. "signature verification", "lazy loading")
- GOOD: "ClientCert" (keep original API name), "Grid" (keep original component name), "Router" (keep), "PersistentStorage" (keep), "signature verification" (concept-level)
- BAD: "Mutual TLS Configuration" (replaced searchable ClientCert), "Grid Container" (replaced searchable Grid), "cj-apis-values_bucket" (file path — should overwrite to ValuesBucket)

label_zh: 2-10 Chinese chars that capture the MOST CORE concept of this doc.
- CRITICAL RULE: If the original label_zh already contains the core searchable term (e.g. "ClientCert与进度信息类", "AppStorage应用全局的UI状态存储", "Grid网格容器组件"), KEEP the core term and only trim to 2-10 chars if needed — do NOT replace with a completely different phrase like "双向TLS配置"
- GOOD: "ClientCert" (keep API name), "AppStorage全局状态" (keep core term), "网格容器" (trimmed from Grid网格容器组件), "签名校验"
- BAD: "双向TLS配置" (replaced ClientCert), "组件内状态宏" (replaced State宏组件内状态 core term)

description_zh: 15-40 Chinese chars, DIRECTLY state the core functionality.
- NEVER start with template words: 文档/指南/资源/说明/参考/介绍
- Start with a functional verb or technical noun directly
- GOOD: "签名证书配置字段校验与多模块版本一致性规则"
- BAD: "指南用于介绍签名证书配置字段..." (template opening)

description_en: 15-40 words, dense stack of English technical terms from this doc.
- NOT a translation of description_zh — must include actual API names and technical terms from the doc
- Stack core APIs, method names, key concepts as a dense phrase
- GOOD: "Router pushUrl replaceUrl back inter-page routing parameter passing"
- BAD: "Guide for introducing signature certificate configuration..." (translation of description_zh)

=== Keywords Rules ===

1. READ the ENTIRE document content carefully — keywords MUST reflect what this doc UNIQUELY and CORELY covers
2. Keywords must satisfy BOTH criteria:
   - From USER perspective: What keywords would a developer actually type when searching for this document?
   - From DOC perspective: Keywords must be core content that this document genuinely covers
3. Focus on CORE content: specific API names, method names, key features, important concepts
4. Include the main API/component name (e.g., AppStorage, Router, animateTo) as a keyword
5. Include problem-solving terms (e.g., 卡顿, 不刷新, 内存泄漏) ONLY when the doc specifically addresses these issues
6. NEVER include these generic words in keywords: HarmonyOS, Cangjie, ArkUI, API, SDK, module, component, usage, guide, overview, furthermore, additionally, 使用, 说明, 介绍
7. source_file must match input path EXACTLY
8. Every file must have an output entry
9. Keep keywords count between 5-10 per language

=== Quality Examples ===

label_zh:
- GOOD: "ClientCert" (keep API name), "AppStorage全局状态" (keep core), "签名校验", "列表懒加载", "abilities标签", "PersistentStorage"
- BAD: "双向TLS配置" (replaced searchable ClientCert), "应用安装与更新一致性校验指南", "指南"

label:
- GOOD: "ClientCert" (keep original API name), "Grid" (keep component name), "Router", "ValuesBucket", "PersistentStorage", "signature verification"
- BAD: "Mutual TLS Configuration" (replaced searchable ClientCert), "Grid Container" (replaced searchable Grid), "cj-apis-values_bucket", "guide"

description_zh:
- GOOD: "签名证书配置字段校验与多模块版本一致性规则"
- GOOD: "LazyForEach按需加载数据实现列表懒渲染"
- BAD: "指南用于介绍签名证书配置字段..."

description_en:
- GOOD: "Router pushUrl replaceUrl back inter-page routing parameter passing"
- GOOD: "LazyForEach onLazyLoad data source itemCount render group recycling"
- BAD: "Guide for introducing signature certificate configuration..."

keywords (user search intent + doc core content):
- GOOD: Router doc → "pushUrl", "replaceUrl", "back", "Router"
- GOOD: WebView lifecycle → "onPageBegin", "onPageEnd", "loadUrl", "WebviewController"
- BAD: Generic platform words: "HarmonyOS", "Cangjie", "API"
- BAD: Generic verbs: "使用", "方法", "介绍"

{file_list}
"""


def read_file_content(source_file: str, base_dir: Path) -> str:
    clean_path = source_file
    for prefix in ["harmonyos-6.0.2-15k/", "harmonyos-6.0.2-15k\\"]:
        if clean_path.startswith(prefix):
            clean_path = clean_path[len(prefix):]
            break
    full_path = base_dir / clean_path
    if full_path.exists():
        try:
            return safe_read_text(full_path)
        except Exception:
            pass
    return ""


def build_batch_prompt(files_with_content: list[tuple[str, str]]) -> str:
    parts = []
    for sf, content in files_with_content:
        parts.append(f"---\nFILE: {sf}\nCONTENT:\n{content}\n---")
    file_list = "\n\n".join(parts)
    return EXTRACTION_PROMPT.format(file_list=file_list)


def _call_llm_sync(prompt: str, result_holder: dict) -> None:
    url = f"{API_BASE}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=LLM_TIMEOUT) as response:
            res = json.loads(response.read().decode())
            content = res['choices'][0]['message']['content']
            cleaned = content.strip()
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:]
            if cleaned.startswith("```"):
                cleaned = cleaned[3:]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            result_obj = json.loads(cleaned.strip())
            if isinstance(result_obj, dict) and "files" in result_obj:
                result_holder["result"] = result_obj["files"]
            elif isinstance(result_obj, list):
                result_holder["result"] = result_obj
            else:
                result_holder["result"] = None
    except Exception as e:
        result_holder["error"] = str(e)


def call_llm(prompt: str) -> Optional[list[dict]]:
    result_holder: dict = {"result": None, "error": None}
    worker = threading.Thread(target=_call_llm_sync, args=(prompt, result_holder))
    worker.start()
    worker.join(timeout=LLM_TIMEOUT)
    
    if result_holder.get("error"):
        return None
    
    return result_holder.get("result")


import re

_PATH_LABEL_RE = re.compile(r'^(cj-|harmonyos_|class_|struct_|enum_|interface_|func_|\.overview|\.md)', re.IGNORECASE)


def _is_path_label(label: str) -> bool:
    """Check if original label is a file-path style label that should be overwritten."""
    if not label:
        return True
    if _PATH_LABEL_RE.match(label):
        return True
    if label.startswith(".") or "/" in label or "\\" in label:
        return True
    if len(label) > 30:
        return True
    return False


def merge_llm_results(nodes: dict, llm_results: list[dict]) -> int:
    file_to_node = {}
    for nid, node in nodes.items():
        if hasattr(node, 'source_file') and node.source_file:
            file_to_node[node.source_file] = node
        elif isinstance(node, dict) and node.get("source_file"):
            file_to_node[node["source_file"]] = node

    merged = 0
    for file_data in llm_results:
        source_file = file_data.get("source_file", "")
        node = file_to_node.get(source_file)
        if not node:
            for k, v in file_to_node.items():
                if k.endswith(source_file) or source_file.endswith(k):
                    node = v
                    break
        if not node:
            continue

        if file_data.get("label"):
            original_label = node.get("label", "")
            new_label = file_data["label"]
            if _is_path_label(original_label):
                node["label"] = new_label
        if file_data.get("label_zh"):
            node["label_zh"] = file_data["label_zh"]
        if file_data.get("description_zh"):
            node["description_zh"] = file_data["description_zh"]
        if file_data.get("description_en"):
            node["description_en"] = file_data["description_en"]
        if file_data.get("keywords_zh"):
            existing = set(node.get("keywords_zh", []))
            node["keywords_zh"] = list(dict.fromkeys(
                (node.get("keywords_zh", []) or []) + [k for k in file_data["keywords_zh"] if k not in existing]
            ))
        if file_data.get("keywords_en"):
            existing = set(k.lower() for k in (node.get("keywords_en", []) or []))
            node["keywords_en"] = list(dict.fromkeys(
                (node.get("keywords_en", []) or []) + [k for k in file_data["keywords_en"] if k.lower() not in existing]
            ))
        node["llm_enhanced"] = True
        merged += 1

    return merged


def create_batches(source_files: list[str], base_dir: Path, max_chars: int = MAX_BATCH_CHARS) -> list[list[tuple[str, str]]]:
    batches = []
    current_batch = []
    current_chars = 0
    
    for sf in source_files:
        content = read_file_content(sf, base_dir)
        if not content:
            continue
            
        file_len = len(content)
        
        if file_len > max_chars and not current_batch:
            batches.append([(sf, content)])
            continue
            
        if current_chars + file_len > max_chars and current_batch:
            batches.append(current_batch)
            current_batch = []
            current_chars = 0
            
        current_batch.append((sf, content))
        current_chars += file_len
        
    if current_batch:
        batches.append(current_batch)
        
    return batches
