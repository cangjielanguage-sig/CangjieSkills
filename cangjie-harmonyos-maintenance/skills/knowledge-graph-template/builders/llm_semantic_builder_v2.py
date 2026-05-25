#!/usr/bin/env python3
"""LLM语义增强知识图谱构建框架。

输出结构：
- 原版图谱：data/merged/graph_layered.json（不变）
- LLM增强图谱：data/merged/graph_layered_llm.json（新）
- 语义边文件：data/semantic_edges.json（单独保存）
- 评测对比：scripts/compare_kg_versions.py

这样可以对比：
- KG原版（关键词匹配）
- KG+LLM语义边（语义理解）
"""

import json
import sys
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# 关键文档列表（Natural 类别相关）
KEY_DOCS = [
    # List 相关
    "API/arkui-cj/cj-scroll-swipe-list/.abstract.md",
    "Guide/arkui-cj/cj-layout-development-create-list/.abstract.md",
    
    # Refresh 相关
    "API/arkui-cj/cj-scroll-swipe-refresh/.abstract.md",
    
    # Navigation 相关  
    "Guide/arkui-cj/cj-navigation-introduction/.abstract.md",
    "API/arkui-cj/cj-apis-uicontext-router/.abstract.md",
    
    # Image 相关
    "API/arkui-cj/cj-image-video-image/.abstract.md",
    
    # 状态管理
    "Guide/arkui-cj/state_management/cj-appstorage/.abstract.md",
    
    # HTTP 相关
    "API/NetworkKit/cj-apis-net-http/.abstract.md",
    
    # AES 相关
    "Guide/security/CryptoArchitectureKit/cj-crypto-aes-sym-encrypt-decrypt-cbc/.abstract.md",
    
    # ArkTS 互操作
    "Guide/learn-cj/FFI/cangjie-arkts/arkts_import_cangjie/.abstract.md",
    
    # Error 相关
    "API/AbilityKit/cj-apis-app-ability-error_manager/.abstract.md",
    
    # Database 相关
    "API/ArkData/cj-apis-relational_store/.abstract.md",
]


def generate_llm_analysis_prompt(doc_content: str, doc_path: str) -> str:
    """生成LLM分析提示。
    
    用户将此提示+文档内容提供给LLM（如我），LLM返回语义关系JSON。
    """
    content_preview = doc_content[:2000] if len(doc_content) > 2000 else doc_content
    
    prompt = f"""## 任务：分析文档，提取语义关系，构建知识图谱语义边

文档路径: {doc_path}
文档内容: {content_preview}...

请分析文档，提取以下语义关系：

1. semantically_similar_to（语义相似）：两个概念解决相同问题但无结构链接
   - confidence_score: 0.6-0.95

2. conceptually_related_to（概念关联）：概念之间的功能关联
   - confidence_score: 0.7-0.9

3. rationale_for（设计意图）：API/组件与为什么这样设计/使用场景
   - confidence_score: 0.8-0.95

输出JSON数组格式，每条关系包含：
- source_label: 源概念名称
- source_path: 源文档路径片段
- target_label: 目标概念名称
- target_path: 目标文档路径片段
- relation: 关系类型
- confidence_score: 置信度
- rationale: 关系理由

示例输出：
[
  {"source_label": "List组件", "target_label": "列表页面", "relation": "semantically_similar_to", "confidence_score": 0.85, "rationale": "List是列表页面的核心组件"},
  {"source_label": "Refresh", "target_label": "下拉刷新", "relation": "conceptually_related_to", "confidence_score": 0.9, "rationale": "Refresh实现下拉刷新功能"}
]

重要规则：
1. 只提取非平凡关系（不是简单的路径匹配）
2. 关系必须有意义
3. 最多输出5-10条关系

请输出JSON数组：
"""
    return prompt


def merge_semantic_edges(original_graph_path: str, semantic_edges_path: str, output_path: str):
    """合并语义边到原图谱，生成LLM增强版。"""
    
    # 加载原图谱
    with open(original_graph_path, encoding="utf-8") as f:
        graph = json.load(f)
    
    # 加载语义边
    with open(semantic_edges_path, encoding="utf-8") as f:
        semantic_edges = json.load(f)
    
    # 合并边
    original_links = graph.get("links", [])
    
    # 转换语义边为图谱边格式
    for edge in semantic_edges:
        link = {
            "source": edge.get("source_id", ""),
            "target": edge.get("target_id", ""),
            "relation": edge.get("relation", "semantically_similar_to"),
            "confidence": "INFERRED",
            "confidence_score": edge.get("confidence_score", 0.8),
            "rationale": edge.get("rationale", ""),
            "source_file": edge.get("source_path", ""),
        }
        original_links.append(link)
    
    # 更新图谱
    graph["links"] = original_links
    graph["graph"]["semantic_edges_added"] = len(semantic_edges)
    graph["graph"]["llm_enhanced_at"] = datetime.now().isoformat()
    
    # 保存增强版
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)
    
    print(f"合并完成:")
    print(f"  原版边数: {len(original_links) - len(semantic_edges)}")
    print(f"  语义边数: {len(semantic_edges)}")
    print(f"  增强版边数: {len(original_links)}")
    print(f"  保存到: {output_path}")


def main():
    # 创建输出目录
    semantic_dir = PROJECT_ROOT / "data" / "semantic"
    semantic_dir.mkdir(parents=True, exist_ok=True)
    
    # 输出路径
    tasks_path = semantic_dir / "llm_analysis_tasks.json"
    semantic_edges_path = semantic_dir / "semantic_edges.json"
    enhanced_graph_path = PROJECT_ROOT / "data" / "merged" / "graph_layered_llm.json"
    
    # 生成任务文件
    tasks = []
    for doc_path in KEY_DOCS:
        full_path = PROJECT_ROOT / "docs" / "harmonyos-6.1-8k" / doc_path
        if full_path.exists():
            content = full_path.read_text(encoding="utf-8")
            tasks.append({
                "doc_path": doc_path,
                "full_path": str(full_path),
                "prompt": generate_llm_analysis_prompt(content, doc_path),
            })
    
    with open(tasks_path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
    
    print(f"生成 {len(tasks)} 个LLM语义分析任务")
    print(f"任务文件: {tasks_path}")
    print(f"\n下一步:")
    print(f"  1. 用户将任务prompt提供给LLM（我）")
    print(f"  2. LLM返回语义关系JSON")
    print(f"  3. 保存到 {semantic_edges_path}")
    print(f"  4. 运行 merge_semantic_edges() 生成增强图谱")


if __name__ == "__main__":
    main()