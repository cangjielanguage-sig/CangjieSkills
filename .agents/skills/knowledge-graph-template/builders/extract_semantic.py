"""语义提取模块（简化版）。从文档中提取标题、链接、概念等。"""
from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Any


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
    
    code_blocks = re.findall(r"```(\w+)?\n([^`]+)```", text, re.DOTALL)
    for lang, code in code_blocks:
        if lang:
            lang_nid = _make_id(stem, f"code_{lang}")
            nodes.append({
                "id": lang_nid,
                "label": f"{lang} code",
                "file_type": "document",
                "source_file": rel_path,
                "source_location": None,
            })
            edges.append({
                "source": file_nid,
                "target": lang_nid,
                "relation": "contains_code",
                "confidence": "EXTRACTED",
                "confidence_score": 1.0,
                "source_file": rel_path,
                "source_location": None,
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