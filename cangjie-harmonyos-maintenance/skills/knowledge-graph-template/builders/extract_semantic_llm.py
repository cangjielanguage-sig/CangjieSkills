"""语义提取模块（LLM 版）。参考 graphify 实现，使用 LLM 提取概念、关系、rationale。

支持：
- 概念节点提取（文档中的关键术语）
- rationale 边（设计原因、决策说明）
- 跨文档语义关联
- semantically_similar_to 边
- hyperedges（多节点共享概念）
- 缓存机制（避免重复提取）
"""
from __future__ import annotations
import asyncio
import json
import os
import re
import hashlib
from pathlib import Path
from typing import Any, Optional
from dataclasses import dataclass, field


@dataclass
class LLMConfig:
    """LLM 配置。支持 OpenAI-compatible API（包括 GLM-5、阿里云 DashScope 等）。"""
    api_base: str = "https://api.openai.com/v1"
    api_key: Optional[str] = None
    model: str = "gpt-4o-mini"
    temperature: float = 0.3
    max_tokens: int = 8192
    timeout: int = 60
    
    def __post_init__(self):
        if self.api_key is None:
            # 尝试多个环境变量
            self.api_key = (
                os.environ.get("OPENAI_API_KEY") or
                os.environ.get("GLM_API_KEY") or
                os.environ.get("DASHSCOPE_API_KEY") or
                os.environ.get("ZHIPU_API_KEY")
            )


EXTRACTION_PROMPT = """You are a graphify extraction subagent for a HarmonyOS / Cangjie knowledge graph. Read the files listed and extract a knowledge graph fragment.
Output ONLY valid JSON matching the schema below - no explanation, no markdown fences, no preamble.

Files (chunk {chunk_num} of {total_chunks}):
{file_contents}

Domain rules (HarmonyOS / Cangjie):
- Every node MUST have a concrete `source_file` pointing to one of the files above (relative path).
- Node `id` convention: use `<kit_or_module>_<entity>_<disambiguator>` lowercase snake. When the document is part of a known V3 card (see `seed_api_ids` / `seed_task_ids` below), reuse that id verbatim. DO NOT invent parallel ids for the same concept.
- Node `label` should be the human-facing name (e.g. `List`, `@State`, `requestPermissionsFromUser`). Never use generic labels like `cangjie code`, `text code`, `function`, `example`.
- HARD RULE: DO NOT emit any node whose label ends with the word `code` (e.g. `cangjie code`, `text code`, `python code`, `bash code`, `json code`). These are markdown fence language tags, NOT concepts. If a code block references APIs, emit one node per referenced API/component instead.
- HARD RULE: DO NOT emit nodes for generic programming words (keywords, primitive types, language names, file extensions).
- Prefer these file_type values: `task` (how-to-do-X guides), `api` (component / class / struct / interface), `example` (example code sections), `document` (overview / abstract / reference prose), `error_code` (error code tables).

{seed_block}

Edge rules:
- EXTRACTED: relationship explicit in source (`import`, `call`, cross-reference like `see 组件事件.md`, parameter type reference).
- INFERRED: reasonable inference. In this domain, ALWAYS emit these inferred edges when the evidence is there:
  * task -> api (relation `recommends_api`) when a how-to guide mentions a component / API as the primary way to accomplish the task.
  * api -> api (relation `typically_used_with`) when two components commonly appear together in the same example (e.g. `List` + `Refresh`, `WebView` + `registerJavaScriptProxy`).
  * task -> task (relation `follows_from`) for multi-step workflows (e.g. `permission request` -> `camera take photo`).
  * api -> error_code (relation `may_emit`) when an API's error section references a specific error code.
- AMBIGUOUS: uncertain - flag for review, do not omit.

{deep_mode_instruction}

Semantic similarity: if two concepts in this chunk solve the same problem or represent the same idea without any structural link (no import, no call, no citation), add a `semantically_similar_to` edge marked INFERRED with a confidence_score (0.6-0.95).

Hyperedges: if 3 or more nodes clearly participate together in a shared concept, flow, or pattern that is not captured by pairwise edges alone, add a hyperedge. Maximum 3 hyperedges per chunk.

If a file has YAML frontmatter (--- ... ---), copy source_url, captured_at, author, contributor onto every node from that file.

confidence_score is REQUIRED on every edge - never omit it, never use 0.5 as a default:
- EXTRACTED edges: confidence_score = 1.0 always
- INFERRED edges: reason about each edge individually.
  Direct structural evidence (e.g. task.recommended_apis contains this api): 0.8-0.9.
  Reasonable inference (co-occurrence in examples): 0.6-0.7.
  Weak or speculative: 0.4-0.5.
- AMBIGUOUS edges: 0.1-0.3

Output exactly this JSON (no other text):
{output_schema}
"""

OUTPUT_SCHEMA = json.dumps({
    "nodes": [
        {
            "id": "filestem_entityname",
            "label": "Human Readable Name",
            "file_type": "code|document|paper|image",
            "source_file": "relative/path",
            "source_location": None,
            "source_url": None,
            "captured_at": None,
            "author": None,
            "contributor": None,
        }
    ],
    "edges": [
        {
            "source": "node_id",
            "target": "node_id",
            "relation": "calls|implements|references|cites|conceptually_related_to|shares_data_with|semantically_similar_to|rationale_for",
            "confidence": "EXTRACTED|INFERRED|AMBIGUOUS",
            "confidence_score": 1.0,
            "source_file": "relative/path",
            "source_location": None,
            "weight": 1.0,
        }
    ],
    "hyperedges": [
        {
            "id": "snake_case_id",
            "label": "Human Readable Label",
            "nodes": ["node_id1", "node_id2", "node_id3"],
            "relation": "participate_in|implement|form",
            "confidence": "EXTRACTED|INFERRED",
            "confidence_score": 0.75,
            "source_file": "relative/path",
        }
    ],
    "input_tokens": 0,
    "output_tokens": 0,
}, indent=2)


def _make_id(*parts: str) -> str:
    """构建稳定的节点 ID。"""
    combined = "_".join(p.strip("_.") for p in parts if p)
    cleaned = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "_", combined)
    return cleaned.strip("_").lower()


def _build_seed_block(seeds: dict, files: list[Path], root: Path) -> str:
    """根据 chunk 内 files 匹配 V3 种子节点，生成 prompt 片段。

    匹配规则：seed.source_paths 里至少一条是 chunk 内某文件 relative path 的子串（或反向）。
    每组最多取 30 条，避免 prompt 过长。
    """
    if not seeds or not seeds.get("nodes"):
        return ""

    chunk_rel_paths: list[str] = []
    for f in files:
        try:
            rp = str(f.resolve().relative_to(root.resolve())).replace("\\", "/").lower()
            chunk_rel_paths.append(rp)
        except Exception:
            chunk_rel_paths.append(str(f).lower())

    def _match(seed_paths: list[str]) -> bool:
        for sp in seed_paths:
            sp_norm = sp.replace("\\", "/").lower()
            if not sp_norm:
                continue
            for rp in chunk_rel_paths:
                # 严格：一方必须是另一方的真子串，且长度差 > 5 字符防止极短路径假命中
                if len(sp_norm) >= 10 and sp_norm in rp:
                    return True
                if len(rp) >= 10 and rp in sp_norm:
                    return True
        return False

    relevant_apis: list[dict] = []
    relevant_tasks: list[dict] = []

    for node in seeds["nodes"]:
        if not _match(node.get("source_paths", [])):
            continue
        entry = {
            "id": node["id"],
            "label": node["label"],
            "aliases": node.get("aliases", [])[:4],
        }
        if node.get("file_type") == "api":
            entry["module"] = node.get("module", "")
            entry["kind"] = node.get("kind", "")
            relevant_apis.append(entry)
        elif node.get("file_type") == "task":
            relevant_tasks.append(entry)

    if not relevant_apis and not relevant_tasks:
        return ""

    relevant_apis = relevant_apis[:30]
    relevant_tasks = relevant_tasks[:15]

    parts = [
        "Seed nodes (from V3 cards - REUSE these ids verbatim when the document matches):",
    ]
    if relevant_apis:
        parts.append(f"  seed_api_ids ({len(relevant_apis)}):")
        for a in relevant_apis:
            parts.append(f"    - id={a['id']} label={a['label']!r} module={a.get('module','')} aliases={a['aliases']}")
    if relevant_tasks:
        parts.append(f"  seed_task_ids ({len(relevant_tasks)}):")
        for t in relevant_tasks:
            parts.append(f"    - id={t['id']} label={t['label']!r} aliases={t['aliases']}")
    return "\n".join(parts) + "\n"


def _read_file_content(path: Path, root: Path, max_chars: int = 8000) -> str:
    """读取文件内容（截断到 max_chars）。"""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        rel_path = str(path.relative_to(root))
        
        if len(text) > max_chars:
            text = text[:max_chars] + "\n... (truncated)"
        
        return f"=== {rel_path} ===\n{text}\n"
    except OSError:
        return f"=== {path.name} ===\n[ERROR: cannot read file]\n"


async def _call_llm(prompt: str, config: LLMConfig) -> dict:
    """调用 LLM API（带简易重试：超时 / 5xx 最多 2 次重试，指数退避）。"""
    import aiohttp

    headers = {
        "Authorization": f"Bearer {config.api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": config.model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": config.temperature,
        "max_tokens": config.max_tokens,
    }

    last_err: Exception | None = None
    for attempt in range(3):
        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=config.timeout)) as session:
                async with session.post(f"{config.api_base}/chat/completions", headers=headers, json=payload) as resp:
                    if resp.status >= 500:
                        text = await resp.text()
                        raise RuntimeError(f"LLM API {resp.status}: {text[:200]}")
                    if resp.status != 200:
                        text = await resp.text()
                        raise RuntimeError(f"LLM API error {resp.status}: {text[:200]}")

                    data = await resp.json()
                    content = data["choices"][0]["message"]["content"]

                    usage = data.get("usage", {})
                    input_tokens = usage.get("prompt_tokens", 0)
                    output_tokens = usage.get("completion_tokens", 0)

                    return {
                        "content": content,
                        "input_tokens": input_tokens,
                        "output_tokens": output_tokens,
                    }
        except asyncio.TimeoutError as e:
            last_err = RuntimeError(f"LLM API timeout after {config.timeout}s")
            if attempt < 2:
                await asyncio.sleep(2 ** attempt)
                continue
        except Exception as e:
            # 5xx 和其他可重试错误走这里
            last_err = e
            msg = str(e)
            if attempt < 2 and ("5" in msg[:20] or "timeout" in msg.lower() or "reset" in msg.lower()):
                await asyncio.sleep(2 ** attempt)
                continue
            raise RuntimeError(f"LLM API error: {e}")
    raise last_err or RuntimeError("LLM call failed after retries")


def _parse_llm_response(content: str, chunk_num: int) -> dict:
    """解析 LLM 返回的 JSON。"""
    cleaned = content.strip()

    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    if cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    cleaned = cleaned.strip()

    try:
        result = json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"[semantic] Warning: chunk {chunk_num} returned invalid JSON: {e}", file=__import__("sys").stderr)
        raise

    if "nodes" not in result:
        result["nodes"] = []
    if "edges" not in result:
        result["edges"] = []
    if "hyperedges" not in result:
        result["hyperedges"] = []

    return result


async def extract_chunk(
    files: list[Path],
    root: Path,
    chunk_num: int,
    total_chunks: int,
    config: LLMConfig,
    deep_mode: bool = False,
    seeds: Optional[dict] = None,
) -> dict:
    """提取单个 chunk。"""
    file_contents = "\n".join(_read_file_content(f, root) for f in files)

    deep_mode_instruction = ""
    if deep_mode:
        deep_mode_instruction = "DEEP_MODE: be aggressive with INFERRED edges - indirect deps, shared assumptions, latent couplings. Mark uncertain ones AMBIGUOUS instead of omitting."

    seed_block = _build_seed_block(seeds, files, root) if seeds else ""

    prompt = EXTRACTION_PROMPT.format(
        chunk_num=chunk_num,
        total_chunks=total_chunks,
        file_contents=file_contents,
        deep_mode_instruction=deep_mode_instruction,
        seed_block=seed_block,
        output_schema=OUTPUT_SCHEMA,
    )
    
    try:
        last_error: Exception | None = None
        response = None
        for attempt in range(2):
            response = await _call_llm(prompt, config)
            try:
                result = _parse_llm_response(response["content"], chunk_num)
                break
            except json.JSONDecodeError as e:
                last_error = e
                if attempt == 0:
                    retry_config = LLMConfig(
                        api_base=config.api_base,
                        api_key=config.api_key,
                        model=config.model,
                        temperature=0.0,
                        max_tokens=max(config.max_tokens, 8192),
                        timeout=config.timeout,
                    )
                    response = await _call_llm(prompt + "\n\nReturn compact valid JSON only. Do not truncate the response.", retry_config)
                    continue
                raise last_error

        result["input_tokens"] = response["input_tokens"]
        result["output_tokens"] = response["output_tokens"]

        for node in result.get("nodes", []):
            if node.get("id"):
                continue
            label = node.get("label", "unknown")
            source = node.get("source_file", "")
            node["id"] = _make_id(Path(source).stem if source else f"chunk{chunk_num}", label)

        # 硬兜底：过滤 lang-code 噪声节点（prompt 约束的二次保险）
        result["nodes"], dropped_ids = _drop_lang_code_noise(result.get("nodes", []))
        if dropped_ids:
            result["edges"] = [e for e in result.get("edges", []) if e.get("source") not in dropped_ids and e.get("target") not in dropped_ids]

        return result

    except Exception as e:
        print(f"[semantic] Error in chunk {chunk_num}: {e}", file=__import__("sys").stderr)
        return {"nodes": [], "edges": [], "hyperedges": [], "error": str(e)}


_NOISE_LABEL_SUFFIX = (" code", " Code", " fence")
_NOISE_LABEL_EQUALS = frozenset({
    "code", "example", "function", "class", "struct", "interface",
    "import", "return", "variable", "constant",
})


def _drop_lang_code_noise(nodes: list[dict]) -> tuple[list[dict], set[str]]:
    """移除 `cangjie code` / `text code` 这类由 markdown 代码块 lang 标签误抽出的节点。"""
    kept: list[dict] = []
    dropped: set[str] = set()
    for n in nodes:
        label = (n.get("label") or "").strip()
        low = label.lower()
        nid = n.get("id") or ""
        if low.endswith(_NOISE_LABEL_SUFFIX) or low in _NOISE_LABEL_EQUALS or nid.startswith("code_"):
            dropped.add(nid)
            continue
        kept.append(n)
    return kept, dropped


def chunk_files(files: list[Path], chunk_size: int = 22) -> list[list[Path]]:
    """分块策略（22 文件/chunk，参考 graphify）。"""
    chunks = []
    for i in range(0, len(files), chunk_size):
        chunks.append(files[i:i + chunk_size])
    return chunks


async def extract_docs_with_llm(
    paths: list[str],
    root: Path,
    config: Optional[LLMConfig] = None,
    deep_mode: bool = False,
    chunk_size: int = 22,
    max_concurrent: int = 3,
    use_cache: bool = True,
    seeds: Optional[dict] = None,
) -> dict:
    """使用 LLM 批量提取文档。
    
    Args:
        paths: 文件路径列表
        root: 根目录（用于计算相对路径）
        config: LLM 配置（默认使用 OPENAI_API_KEY）
        deep_mode: 深度模式（更激进的 INFERRED 边）
        chunk_size: 每个 chunk 的文件数（默认 22）
        max_concurrent: 最大并发 chunk 数（默认 3）
        use_cache: 是否使用缓存（默认 True）
    
    Returns:
        {"nodes": [...], "edges": [...], "hyperedges": [...], "input_tokens": N, "output_tokens": N}
    """
    if config is None:
        config = LLMConfig()
    
    if not config.api_key:
        print("[semantic] Warning: No API key configured. Set OPENAI_API_KEY or pass config.api_key", file=__import__("sys").stderr)
        return {"nodes": [], "edges": [], "hyperedges": [], "error": "No API key"}
    
    files = [Path(p) for p in paths if Path(p).exists()]
    
    if not files:
        return {"nodes": [], "edges": [], "hyperedges": [], "error": "No files"}
    
    if use_cache:
        from .cache import load_cached, save_cached, llm_cache_namespace
        cache_namespace = llm_cache_namespace(config.model, config.api_base, "semantic-llm-v2")
        cached_results = []
        uncached_files = []

        for f in files:
            cached = load_cached(f, root, namespace=cache_namespace)
            if cached:
                cached_results.append(cached)
            else:
                uncached_files.append(f)
        
        if not uncached_files:
            print(f"[semantic] All {len(files)} files cached, skipping LLM extraction")
            all_nodes = []
            all_edges = []
            all_hyperedges = []
            for r in cached_results:
                all_nodes.extend(r.get("nodes", []))
                all_edges.extend(r.get("edges", []))
                all_hyperedges.extend(r.get("hyperedges", []))
            return {"nodes": all_nodes, "edges": all_edges, "hyperedges": all_hyperedges, "input_tokens": 0, "output_tokens": 0}
        
        print(f"[semantic] Cache: {len(cached_results)} files hit, {len(uncached_files)} files need extraction")
        files = uncached_files
    
    chunks = chunk_files(files, chunk_size)
    print(f"[semantic] Split into {len(chunks)} chunks (~{chunk_size} files each)")
    print(f"[semantic] Estimated time: ~{len(chunks) * 45 // max_concurrent}s")
    
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def process_chunk(chunk: list[Path], idx: int) -> dict:
        async with semaphore:
            print(f"[semantic] Processing chunk {idx + 1}/{len(chunks)} ({len(chunk)} files)")
            result = await extract_chunk(chunk, root, idx + 1, len(chunks), config, deep_mode, seeds=seeds)
            
            if use_cache and "error" not in result:
                for f in chunk:
                    file_result = {
                        "nodes": [n for n in result.get("nodes", []) if n.get("source_file") == str(f.relative_to(root))],
                        "edges": [e for e in result.get("edges", []) if e.get("source_file") == str(f.relative_to(root))],
                        "hyperedges": [h for h in result.get("hyperedges", []) if h.get("source_file") == str(f.relative_to(root))],
                    }
                    save_cached(f, file_result, root, namespace=cache_namespace)
            
            return result
    
    results = await asyncio.gather(*[process_chunk(chunk, i) for i, chunk in enumerate(chunks)])
    
    all_nodes: list[dict] = []
    all_edges: list[dict] = []
    all_hyperedges: list[dict] = []
    total_input_tokens = 0
    total_output_tokens = 0
    failed_chunks = 0
    failures: list[dict] = []

    for index, r in enumerate(results, 1):
        if "error" in r:
            failed_chunks += 1
            failures.append({"chunk": index, "error": r.get("error", "")})
            continue
        all_nodes.extend(r.get("nodes", []))
        all_edges.extend(r.get("edges", []))
        all_hyperedges.extend(r.get("hyperedges", []))
        total_input_tokens += r.get("input_tokens", 0)
        total_output_tokens += r.get("output_tokens", 0)
    
    if use_cache:
        for r in cached_results:
            all_nodes.extend(r.get("nodes", []))
            all_edges.extend(r.get("edges", []))
            all_hyperedges.extend(r.get("hyperedges", []))
    
    seen_ids: set[str] = set()
    deduped_nodes: list[dict] = []
    for n in all_nodes:
        nid = n.get("id")
        if nid and nid not in seen_ids:
            seen_ids.add(nid)
            deduped_nodes.append(n)
    
    print(f"[semantic] Extraction complete: {len(deduped_nodes)} nodes, {len(all_edges)} edges, {len(all_hyperedges)} hyperedges")
    print(f"[semantic] Token usage: {total_input_tokens} input, {total_output_tokens} output")
    
    if failed_chunks > len(chunks) // 2:
        print(f"[semantic] Warning: {failed_chunks}/{len(chunks)} chunks failed")
    if failures:
        failure_path = root / "graphify-out" / "failures.jsonl"
        failure_path.parent.mkdir(parents=True, exist_ok=True)
        with failure_path.open("a", encoding="utf-8") as handle:
            for failure in failures:
                handle.write(json.dumps(failure, ensure_ascii=False) + "\n")

    return {
        "nodes": deduped_nodes,
        "edges": all_edges,
        "hyperedges": all_hyperedges,
        "input_tokens": total_input_tokens,
        "output_tokens": total_output_tokens,
        "failed_chunks": failed_chunks,
        "failure_count": len(failures),
    }


def extract_docs_with_llm_sync(
    paths: list[str],
    root: Path,
    config: Optional[LLMConfig] = None,
    deep_mode: bool = False,
    **kwargs,
) -> dict:
    """同步版本的 LLM 提取（方便 CLI 调用）。"""
    return asyncio.run(extract_docs_with_llm(paths, root, config, deep_mode, **kwargs))


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python -m builders.extract_semantic_llm <dir> [--deep]", file=sys.stderr)
        print("  Requires OPENAI_API_KEY environment variable", file=sys.stderr)
        sys.exit(1)
    
    root = Path(sys.argv[1]).resolve()
    deep_mode = "--deep" in sys.argv
    
    from .detect import detect
    detected = detect(root)
    doc_files = detected.get("files", {}).get("document", [])
    
    print(f"Processing {len(doc_files)} document files...")
    
    config = LLMConfig()
    if not config.api_key:
        print("Error: OPENAI_API_KEY not set", file=sys.stderr)
        sys.exit(1)
    
    result = extract_docs_with_llm_sync(doc_files, root, config, deep_mode=deep_mode)
    
    output_path = root / "graphify-out" / "semantic_extraction.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    
    print(f"Saved to {output_path}")