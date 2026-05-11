#!/usr/bin/env python3
"""LLM语义增强知识图谱构建框架。

输出结构：
- 原版图谱：data/merged/graph_layered.json（不变）
- LLM增强图谱：data/merged/graph_layered_llm.json（新）
- 语义边文件：data/semantic/semantic_edges.json（单独保存）
"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

KEY_DOCS = [
    "API/arkui-cj/cj-scroll-swipe-list/.abstract.md",
    "Guide/arkui-cj/cj-layout-development-create-list/.abstract.md",
    "API/arkui-cj/cj-scroll-swipe-refresh/.abstract.md",
    "Guide/arkui-cj/cj-navigation-introduction/.abstract.md",
    "API/arkui-cj/cj-apis-uicontext-router/.abstract.md",
]


def main():
    semantic_dir = PROJECT_ROOT / "data" / "semantic"
    semantic_dir.mkdir(parents=True, exist_ok=True)
    
    print("LLM语义增强知识图谱框架")
    print("=" * 50)
    print("\n工作流程:")
    print("1. 读取关键文档")
    print("2. LLM（我）分析文档，提取语义关系")
    print("3. 保存语义边到 semantic_edges.json")
    print("4. 合并到图谱生成 graph_layered_llm.json")
    print("\n关键文档列表:")
    for doc in KEY_DOCS:
        print(f"  - {doc}")
    
    print("\n下一步: 请让我开始读取第一个文档进行分析")


if __name__ == "__main__":
    main()