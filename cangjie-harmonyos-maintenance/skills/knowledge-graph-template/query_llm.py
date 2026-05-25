"""LLM增强搜索 - 在搜索流程中集成 Query Enhancement。

使用方式：
    from query_llm import create_llm_session
    
    session = create_llm_session()
    result = session.search("怎么做一个列表页面")  # 自动改写并搜索

流程：
    用户 query → enhance_query() → KG搜索 → 返回结果
    
Agent使用方式：
    当用户问题进入知识图谱搜索流程时，Agent应在对话中：
    1. 理解query语义（识别意图、核心概念）
    2. 改写query为适合KG的格式
    3. 使用改写后的query搜索KG
"""

import json
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(_PROJECT_ROOT))

from query import GraphSession
from builders.query_enhancer import enhance_query, get_llm_prompt_for_query, load_cache, save_cache


class LLMSession:
    """LLM增强搜索会话。
    
    在搜索前自动改写 query，提高命中率。
    
    Agent使用流程：
    1. Agent理解用户query语义
    2. Agent改写query（或使用预定义规则）
    3. KG用改写后的query搜索
    """
    
    def __init__(self, enable_enhancement: bool = True, graph_dir: str = None):
        self._base_session = GraphSession(graph_dir=graph_dir, enable_feedback=False)
        self._enable_enhancement = enable_enhancement
        self._enhancement_log = []
    
    def search(self, query: str, limit: int = 10, force_graph: str = None) -> dict:
        """搜索（自动改写 query）。
        
        如果启用enhancement，会使用预定义改写规则。
        如果query不在预定义规则中，Agent应在对话中自行改写。
        """
        
        # 改写 query
        if self._enable_enhancement:
            enhanced_query = enhance_query(query)
            if enhanced_query != query:
                self._enhancement_log.append({
                    "original": query,
                    "enhanced": enhanced_query,
                    "method": "rule",
                })
        else:
            enhanced_query = query
        
        # 搜索
        result = self._base_session.search(enhanced_query, limit=limit, force_graph=force_graph)
        
        # 添加改写信息到结果
        result.enhanced_query = enhanced_query
        result.original_query = query
        
        return result
    
    def search_raw(self, query: str, limit: int = 10) -> dict:
        """原始搜索（不改写）。"""
        return self._base_session.search(query, limit=limit)
    
    def get_enhancement_log(self) -> list:
        """获取改写日志。"""
        return self._enhancement_log
    
    def clear_enhancement_log(self):
        """清空改写日志。"""
        self._enhancement_log = []


def create_llm_session(enable_enhancement: bool = True, graph_dir: str = None) -> LLMSession:
    """创建LLM增强搜索会话。"""
    return LLMSession(enable_enhancement=enable_enhancement, graph_dir=graph_dir)


def main():
    print("LLM增强搜索测试")
    print("=" * 60)
    
    session = create_llm_session()
    
    test_queries = [
        "List 组件",
        "怎么做一个列表页面",
        "如何实现下拉刷新",
        "HttpRequest 网络请求",
    ]
    
    for q in test_queries:
        result = session.search(q, limit=5)
        print(f"\nQuery: {q}")
        print(f"Enhanced: {result.enhanced_query}")
        print(f"Paths: {len(result.paths)}")
        for i, p in enumerate(result.paths[:3], 1):
            print(f"  {i}. {p}")
    
    print(f"\n改写日志: {len(session.get_enhancement_log())} 条")


if __name__ == "__main__":
    main()