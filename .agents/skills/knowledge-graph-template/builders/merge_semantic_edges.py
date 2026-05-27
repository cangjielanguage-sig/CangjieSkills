#!/usr/bin/env python3
"""合并语义边到图谱，生成LLM增强版。

输入：
- 原版图谱：data/merged/graph_layered.json
- 语义边：data/semantic/semantic_edges.json

输出：
- LLM增强图谱：data/merged/graph_layered_llm.json
"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_graph(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_semantic_edges(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_node_id(label: str, path: str) -> str:
    """根据label和path构建节点ID（与graphify规则一致）。"""
    # 清理label：lowercase，只保留[a-z0-9_]
    import re
    clean_label = re.sub(r"[^a-z0-9]", "_", label.lower()).strip("_")
    # 从path提取stem
    stem = Path(path).stem.replace("-", "_").lower()
    return f"{stem}_{clean_label}"


def merge_semantic_edges():
    # 加载原图谱
    original_graph = load_graph(str(PROJECT_ROOT / "data" / "merged" / "graph_layered.json"))
    semantic_data = load_semantic_edges(str(PROJECT_ROOT / "data" / "semantic" / "semantic_edges.json"))
    
    print(f"原版图谱: {len(original_graph['nodes'])} nodes, {len(original_graph['links'])} links")
    print(f"语义边: {len(semantic_data['edges'])} edges")
    
    # 构建节点索引（用于查找节点ID）
    node_index = {}
    for node in original_graph["nodes"]:
        node_index[node["label"].lower()] = node["id"]
        node_index[node.get("norm_label", "").lower()] = node["id"]
        # 添加路径关键词索引
        source_file = node.get("source_file", "").lower()
        if source_file:
            node_index[source_file] = node["id"]
    
    # 转换语义边为图谱边格式
    new_links = []
    for edge in semantic_data["edges"]:
        source_label = edge["source_label"].lower()
        target_label = edge["target_label"].lower()
        
        # 查找节点ID（从索引或构建）
        source_id = node_index.get(source_label) or build_node_id(source_label, edge["source_path"])
        target_id = node_index.get(target_label) or build_node_id(target_label, edge["target_path"])
        
        link = {
            "source": source_id,
            "target": target_id,
            "relation": edge["relation"],
            "confidence": "INFERRED",
            "confidence_score": edge["confidence_score"],
            "rationale": edge["rationale"],
            "source_file": edge["source_path"],
            "weight": edge["confidence_score"],
        }
        new_links.append(link)
    
    # 合并边
    original_links = original_graph.get("links", [])
    merged_links = original_links + new_links
    
    # 更新图谱元数据
    original_graph["links"] = merged_links
    original_graph["graph"]["semantic_edges_added"] = len(new_links)
    original_graph["graph"]["llm_enhanced"] = True
    original_graph["graph"]["original_links"] = len(original_links)
    
    # 保存增强版
    output_path = PROJECT_ROOT / "data" / "merged" / "graph_layered_llm.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(original_graph, f, ensure_ascii=False, indent=2)
    
    print(f"\n合并完成:")
    print(f"  原版边数: {len(original_links)}")
    print(f"  语义边数: {len(new_links)}")
    print(f"  增强版边数: {len(merged_links)}")
    print(f"  保存到: {output_path}")
    
    # 输出新增边详情
    print("\n新增语义边示例:")
    for i, link in enumerate(new_links[:5]):
        print(f"  {i+1}. {link['relation']}: {link['rationale'][:50]}...")


if __name__ == "__main__":
    merge_semantic_edges()