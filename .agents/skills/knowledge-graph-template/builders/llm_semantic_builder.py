#!/usr/bin/env python3
"""基于LLM语义理解的知识图谱构建框架。

流程：
1. 选择关键文档（Natural 类别相关）
2. LLM 读取文档，分析语义关系
3. 生成语义边（semantically_similar_to, conceptually_related_to, rationale_for）
4. 合并到图谱

LLM语义理解规则：
- semantically_similar_to: 两个概念解决相同问题但无结构链接（confidence 0.6-0.95）
- conceptually_related_to: 概念关联（如组件 ↔ 使用场景）
- rationale_for: 设计意图（如API ↔ 为什么这样设计）
"""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# 关键文档列表（Natural 类别相关）
KEY_DOCS = [
    # List 相关
    ("API/arkui-cj/cj-scroll-swipe-list", ["List", "列表", "列表页面", "滚动列表"]),
    ("Guide/arkui-cj/cj-layout-development-create-list", ["创建列表", "列表页面", "列表组件"]),
    
    # Refresh 相关
    ("API/arkui-cj/cj-scroll-swipe-refresh", ["Refresh", "下拉刷新", "刷新组件"]),
    
    # Navigation 相关
    ("Guide/arkui-cj/cj-navigation-introduction", ["Navigation", "导航", "页面跳转", "路由"]),
    ("API/arkui-cj/cj-apis-uicontext-router", ["Router", "路由", "页面跳转"]),
    
    # Image 相关
    ("API/arkui-cj/cj-image-video-image", ["Image", "图片", "图片加载", "图片显示"]),
    
    # 状态管理
    ("Guide/arkui-cj/state_management/cj-appstorage", ["AppStorage", "状态管理", "全局状态"]),
    
    # HTTP 相关
    ("API/NetworkKit/cj-apis-net-http", ["HttpRequest", "HTTP", "网络请求", "网络连接"]),
    
    # AES 相关
    ("Guide/security/CryptoArchitectureKit/cj-crypto-aes-sym-encrypt-decrypt-cbc", ["AES", "加密", "对称加密"]),
    
    # ArkTS 互操作
    ("Guide/learn-cj/FFI/cangjie-arkts/arkts_import_cangjie", ["ArkTS", "互操作", "仓颉调用ArkTS"]),
]

# 语义边模板
SEMANTIC_EDGE_TEMPLATE = {
    "source": "",
    "target": "",
    "relation": "semantically_similar_to",  # or conceptually_related_to, rationale_for
    "confidence": "INFERRED",
    "confidence_score": 0.0,  # 0.6-0.95
    "source_file": "",
    "rationale": "",  # 为什么认为有关系
}


def generate_llm_prompt(doc_path: str, keywords: list[str]) -> str:
    """生成 LLM 分析提示。
    
    这个提示会被用户提供给 LLM，LLM 返回语义关系JSON。
    """
    return f"""
请分析以下文档并提取语义关系。

文档路径: {doc_path}
关键词: {keywords}

请提取以下类型的语义关系：

1. semantically_similar_to（语义相似）：
   - 两个概念解决相同问题但无结构链接
   - confidence_score: 0.6-0.95（非平凡相似）
   
2. conceptually_related_to（概念关联）：
   - 概念之间的功能关联（如组件 ↔ 使用场景）
   - confidence_score: 0.7-0.9
   
3. rationale_for（设计意图）：
   - API/组件 ↔ 为什么这样设计
   - confidence_score: 0.8-0.95

输出格式（JSON数组）：
[
  {
    "source": "节点ID",
    "target": "节点ID", 
    "relation": "semantically_similar_to",
    "confidence_score": 0.85,
    "rationale": "为什么认为有关系"
  }
]

示例：
- List组件 ↔ 列表页面创建 → semantically_similar_to (0.8) "List是列表页面的核心组件"
- Refresh ↔ 下拉刷新 → conceptually_related_to (0.9) "Refresh是下拉刷新功能的实现"
- Navigation ↔ 页面跳转 → conceptually_related_to (0.85) "Navigation管理页面跳转流程"

请输出JSON：
"""


def save_llm_tasks(tasks: list[dict], output_path: str):
    """保存 LLM 任务列表。"""
    with open(output_path, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(json.dumps(task, ensure_ascii=False) + "\n")


def main():
    # 生成 LLM 任务
    tasks = []
    for doc_path, keywords in KEY_DOCS:
        prompt = generate_llm_prompt(doc_path, keywords)
        tasks.append({
            "doc_path": doc_path,
            "keywords": keywords,
            "prompt": prompt,
        })
    
    # 保存任务列表
    output_path = PROJECT_ROOT / "builders" / "llm_semantic_tasks.jsonl"
    save_llm_tasks(tasks, str(output_path))
    print(f"生成 {len(tasks)} 个LLM语义分析任务")
    print(f"保存到: {output_path}")
    
    # 打印示例任务
    print("\n示例任务:")
    print(tasks[0]["prompt"][:500])


if __name__ == "__main__":
    main()