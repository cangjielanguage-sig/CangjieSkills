"""语义提取模块（简化版）。从文档中提取标题、链接、概念等。"""
from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Any


# 代码块里的语言关键字 / 内置类型，不应作为 API 节点。
# 鸿蒙真组件（List / Array / Error 等）不在这里。
_CODE_BLOCK_NOISE = frozenset({
    "True", "False", "None", "Null",
    "String", "Int", "Float", "Bool", "Double", "Boolean",
    "Return", "Break", "Continue", "Class", "Func", "Var", "Let",
    "Import", "From", "Export", "Default", "Public", "Private", "Protected",
    "Try", "Catch", "Finally", "Throw", "New", "This", "Self", "Super",
    "If", "Else", "For", "While", "Switch", "Case",
    "Unit", "Any", "Void", "Object",
})


def _make_id(*parts: str) -> str:
    """构建稳定的节点 ID。"""
    combined = "_".join(p.strip("_.") for p in parts if p)
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", combined)
    return cleaned.strip("_").lower()


def extract_markdown(path: Path, root: Path) -> dict:
    """从 Markdown 文件提取标题和链接（简化版，无需 LLM）。"""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {"nodes": [], "edges": [], "error": f"cannot read {path}"}
    
    rel_path = str(path.relative_to(root))
    stem = path.stem
    nodes: list[dict] = []
    edges: list[dict] = []
    
    file_nid = _make_id(rel_path)
    nodes.append({
        "id": file_nid,
        "label": path.name,
        "file_type": "document",
        "source_file": rel_path,
        "source_location": "L1",
    })
    
    headers = re.findall(r"^#+\s+(.+)$", text, re.MULTILINE)
    for i, h in enumerate(headers):
        level_match = re.match(r"^#+", h)
        if level_match:
            level = len(level_match.group())
        else:
            level = 1
        title = h.lstrip("#").strip()
        h_nid = _make_id(stem, f"h{i+1}", title)
        nodes.append({
            "id": h_nid,
            "label": title,
            "file_type": "document",
            "source_file": rel_path,
            "source_location": f"H{i+1}",
        })
        edges.append({
            "source": file_nid,
            "target": h_nid,
            "relation": "contains",
            "confidence": "EXTRACTED",
            "confidence_score": 1.0,
            "source_file": rel_path,
            "source_location": f"H{i+1}",
            "weight": 1.0,
        })
    
    md_links = re.findall(r"\[([^\]]+)\]\(([^\)]+)\)", text)
    for label, target in md_links:
        if target.startswith(("http://", "https://", "#")):
            continue
        target_nid = _make_id(target)
        if target_nid not in {n["id"] for n in nodes}:
            nodes.append({
                "id": target_nid,
                "label": target.split("/")[-1],
                "file_type": "document",
                "source_file": rel_path,
                "source_location": None,
            })
        edges.append({
            "source": file_nid,
            "target": target_nid,
            "relation": "references",
            "confidence": "EXTRACTED",
            "confidence_score": 1.0,
            "source_file": rel_path,
            "source_location": None,
            "weight": 1.0,
        })
    
    # 从代码块里提取被调用的 API / 组件名，而不是按 lang 建噪声节点
    # 规则：匹配 PascalCase 标识符（List, Refresh, WebView 等鸿蒙组件惯例）或
    # 已知 std.x / stdx.x / @Decorator 形式，挑出前 20 个高频引用作为边
    code_blocks = re.findall(r"```[^\n]*\n(.*?)```", text, re.DOTALL)
    api_counter: dict[str, int] = {}
    for code in code_blocks:
        for m in re.finditer(r"\b([A-Z][A-Za-z0-9]{2,})\b", code):
            name = m.group(1)
            if name in _CODE_BLOCK_NOISE:
                continue
            api_counter[name] = api_counter.get(name, 0) + 1
        for m in re.finditer(r"\b(std|stdx)\.([a-z_][a-z0-9_]*)", code):
            qname = f"{m.group(1)}.{m.group(2)}"
            api_counter[qname] = api_counter.get(qname, 0) + 1
        for m in re.finditer(r"@([A-Z][A-Za-z0-9]+)", code):
            deco = f"@{m.group(1)}"
            api_counter[deco] = api_counter.get(deco, 0) + 1
    # 取前 20 个引用频次最高的作为 INFERRED 边
    for api_name, _ in sorted(api_counter.items(), key=lambda kv: -kv[1])[:20]:
        api_nid = _make_id("api", api_name)
        if api_nid not in {n["id"] for n in nodes}:
            nodes.append({
                "id": api_nid,
                "label": api_name,
                "file_type": "api_reference",
                "source_file": rel_path,
                "source_location": "code_block",
            })
        edges.append({
            "source": file_nid,
            "target": api_nid,
            "relation": "calls_api",
            "confidence": "INFERRED",
            "confidence_score": 0.6,
            "source_file": rel_path,
            "source_location": "code_block",
            "weight": 1.0,
        })
    
    yaml_frontmatter = re.match(r"^---\n(.+?)\n---\n", text, re.DOTALL)
    if yaml_frontmatter:
        fm_text = yaml_frontmatter.group(1)
        title_match = re.search(r"title:\s*[\"']?([^\"'\n]+)[\"']?", fm_text)
        if title_match:
            title = title_match.group(1).strip()
            fm_nid = _make_id(stem, "title", title)
            nodes.append({
                "id": fm_nid,
                "label": title,
                "file_type": "document",
                "source_file": rel_path,
                "source_location": "FM",
            })
            edges.append({
                "source": file_nid,
                "target": fm_nid,
                "relation": "has_title",
                "confidence": "EXTRACTED",
                "confidence_score": 1.0,
                "source_file": rel_path,
                "source_location": "FM",
                "weight": 1.0,
            })
    
    return {"nodes": nodes, "edges": edges}


def extract_docs_simple(paths: list[str], root: Path) -> dict:
    """批量提取文档（简化版）。"""
    all_nodes: list[dict] = []
    all_edges: list[dict] = []
    
    for p in paths:
        path = Path(p)
        if not path.exists():
            continue
        ext = path.suffix.lower()
        if ext in {".md", ".mdx", ".txt", ".rst"}:
            result = extract_markdown(path, root)
            all_nodes.extend(result.get("nodes", []))
            all_edges.extend(result.get("edges", []))
    
    return {"nodes": all_nodes, "edges": all_edges, "input_tokens": 0, "output_tokens": 0}


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m builders.extract_semantic <dir>", file=sys.stderr)
        sys.exit(1)
    
    root = Path(sys.argv[1]).resolve()
    from builders.detect import detect
    detected = detect(root)
    doc_files = detected.get("files", {}).get("document", [])
    
    result = extract_docs_simple(doc_files, root)
    print(json.dumps(result, indent=2, ensure_ascii=False))