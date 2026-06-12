"""LLM 语义增强模块 — 智能分批、全量读取、结果合并。

本模块负责图谱节点的 LLM 增强核心逻辑：
- EXTRACTION_PROMPT: 向 LLM 发送的提取 prompt（要求输出 JSON）
- read_file_content: 读取文档原文，剥离顶层目录前缀
- build_batch_prompt: 将多个文件内容组装为 LLM prompt
- call_llm: 调用 LLM API（通过线程避免 urllib 超时阻塞主线程）
- merge_llm_results: 将 LLM 返回的语义信息合并到图谱节点中
- create_batches: 按字符数限制将文件列表分为多个批次

合并策略：
- label: 仅当原标签是路径风格（cj-/class_ 等前缀）时才覆盖
- keywords: 原有 + LLM 新增，去重合并
- description/label_zh: 直接覆盖
"""
from __future__ import annotations

import json
import os
import sys
import threading
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional

API_KEY = os.environ.get("DASHSCOPE_API_KEY", "xxx")
API_BASE = os.environ.get("DASHSCOPE_API_BASE", "xxx")
MODEL = "qwen3.6-plus"
MAX_BATCH_CHARS = 40000  # 单批次最大字符数，超出则分批
LLM_TIMEOUT = 600  # 单次 LLM 调用超时（秒）




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
    """读取文档原文，剥离 harmonyos-6.0.2-15k 前缀后拼接路径。
    文件不存在或读取失败时返回空字符串（该文件将被跳过）。"""
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
    """同步调用 LLM API（在子线程中运行）。

    将结果写入 result_holder dict：
    - result: 成功时为 LLM 返回的 JSON 列表
    - error: 失败时为异常字符串
    自动剥离 ```json markdown 包装。
    """
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
    """调用 LLM API 并返回提取结果列表。

    使用线程封装 urllib 调用，避免超时阻塞主线程。
    返回 None 表示调用失败。
    """
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
    """判断原始标签是否为文件路径风格（应被 LLM 结果覆盖）。

    路径风格标签特征：cj-/class_ 等前缀、含 / 或 \\、过长（>30字符）。
    保留原有 API 名称（如 ClientCert、Grid）不被覆盖。
    """
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
    """将 LLM 返回的语义信息合并到图谱节点中。

    合并策略：
    - label: 仅当原标签是路径风格时覆盖（保留 API 名如 ClientCert）
    - label_zh / description: 直接覆盖
    - keywords: 原有 + 新增去重合并（en 关键词大小写不敏感去重）
    - llm_enhanced 标记: 设为 True

    路径匹配容忍前缀差异（source_file 比对使用 endswith）。
    返回成功合并的节点数。
    """
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
    """按字符数限制将文件列表分为多个批次。

    分批策略：
    - 超大文件（内容 > max_chars）单独成批，不截断
    - 常规文件按累加字符数分批，每批不超过 max_chars
    - 空文件（读取失败）直接跳过

    返回 [[(source_file, content)]] 批次列表。
    """
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
