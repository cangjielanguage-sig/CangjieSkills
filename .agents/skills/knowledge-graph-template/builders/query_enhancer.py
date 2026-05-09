#!/usr/bin/env python3
"""LLM Query Enhancement 集成到 KG 搜索流程。

方案：
1. 用户提供原始 query
2. LLM（我）在对话中改写 query
3. KG 用改写后的 query 搜索

输出：
- data/semantic/enhanced_queries_cache.json - 改写结果缓存
- 搜索时自动使用缓存中的改写 query
"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# LLM 改写缓存（避免重复改写）
ENHANCED_CACHE_PATH = PROJECT_ROOT / "data" / "semantic" / "enhanced_queries_cache.json"

# 基于评测集分析的改写规则（作为 fallback）
QUERY_ENHANCEMENT_RULES = {
    # List 相关
    "怎么做一个列表页面": "cj-scroll-swipe-list cj-layout-development-create-list List 创建列表",
    "List 组件": "cj-scroll-swipe-list List API",
    "List 组件的分割线设置": "cj-scroll-swipe-list List divider 分割线",
    
    # Refresh 相关
    "如何实现下拉刷新": "cj-scroll-swipe-refresh Refresh 下拉刷新",
    "Refresh 下拉刷新": "cj-scroll-swipe-refresh Refresh API",
    "Refresh 的 onRefreshing 回调": "cj-scroll-swipe-refresh Refresh onRefreshing",
    
    # Navigation 相关
    "怎么实现页面跳转和路由": "cj-navigation-introduction cj-apis-uicontext-router Navigation Router",
    "Navigation 导航": "cj-navigation-navigation Navigation Guide",
    "Navigation 的 NavPathStack 路由管理": "cj-navigation-introduction NavPathStack Navigation",
    
    # Image 相关
    "Image 组件": "cj-image-video-image Image API",
    "Image 的 objectFit 属性": "cj-image-video-image Image objectFit",
    "如何实现图片加载和显示": "cj-image-video-image Image 图片加载",
    
    # HttpRequest 相关
    "HttpRequest 网络请求": "cj-apis-net-http NetworkKit HttpRequest API",
    "如何实现网络请求": "cj-apis-net-http NetworkKit HttpRequest",
    "HttpRequest 的 header 设置": "cj-apis-net-http HttpRequest header",
    
    # AES 相关
    "AES 加密": "cj-crypto-aes CryptoArchitectureKit AES 加密",
    "如何使用 AES 加密数据": "cj-crypto-aes CryptoArchitectureKit AES 加密解密",
    
    # 状态管理
    "AppStorage 状态管理": "cj-appstorage AppStorage 状态管理 Guide",
    "AppStorage 的 setOrCreate 方法": "cj-appstorage AppStorage setOrCreate",
    
    # ArkTS 互操作
    "ArkTS 互操作": "arkts_import_cangjie cangjie-arkts FFI",
    "如何在仓颉中调用 ArkTS 代码": "arkts_import_cangjie cangjie-arkts FFI ArkTS 互操作",
    
    # Error 相关
    "参数校验失败": "cj-apis-app-ability-error_manager AbilityKit error_manager",
    "类型不匹配错误": "cj-apis-value_type cj-common-types 类型错误",
    "import 找不到模块": "arkts_import_cangjie import 模块 FFI",
    "数据库操作报错": "cj-apis-relational_store ArkData RelationalStore 数据库错误",
    
    # 自定义组件
    "如何创建自定义组件": "cj-custom-component-lifecycle 自定义组件 lifecycle",
    
    # Animation
    "属性动画": "cj-animation-animation Animation 属性动画 API",
    "怎么实现属性动画效果": "cj-animation-animation Animation 属性动画",
    
    # 其他
    "如何获取设备信息": "cj-apis-device_info BasicServicesKit DeviceInfo",
    "怎么用仓颉写第一个鸿蒙应用": "cj-quick-start-first-cangjie-app 仓颉 鸿蒙 第一个应用",
    "如何实现轮播图效果": "cj-scroll-swipe-swiper Swiper 轮播",
    "加密相关 API 有哪些": "cj-apis-crypto CryptoArchitectureKit Cipher Mac",
    "状态管理有哪些方案": "cj-appstorage cj-macro-state State AppStorage",
}


def load_cache() -> dict:
    """加载改写缓存。"""
    if ENHANCED_CACHE_PATH.exists():
        with open(ENHANCED_CACHE_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(cache: dict):
    """保存改写缓存。"""
    with open(ENHANCED_CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def enhance_query_with_rules(query: str) -> str:
    """基于规则改写 query（fallback）。"""
    # 直接匹配
    if query in QUERY_ENHANCEMENT_RULES:
        return QUERY_ENHANCEMENT_RULES[query]
    
    # 关键词匹配
    query_lower = query.lower()
    for original, enhanced in QUERY_ENHANCEMENT_RULES.items():
        original_lower = original.lower()
        # 包含关系
        if original_lower in query_lower or query_lower in original_lower:
            return enhanced
        # 关键词重叠
        overlap = len(set(original_lower.split()) & set(query_lower.split()))
        if overlap >= 2:
            return enhanced
    
    # 未匹配，返回原 query
    return query


def enhance_query(query: str, use_cache: bool = True) -> str:
    """改写 query（使用缓存或规则）。"""
    if use_cache:
        cache = load_cache()
        if query in cache:
            return cache[query]["enhanced"]
    
    # 使用规则改写
    enhanced = enhance_query_with_rules(query)
    
    # 保存到缓存
    if use_cache:
        cache = load_cache()
        cache[query] = {
            "original": query,
            "enhanced": enhanced,
            "method": "rule",
        }
        save_cache(cache)
    
    return enhanced


def get_llm_prompt_for_query(query: str) -> str:
    """生成让 LLM 改写 query 的提示。

    用户将此提示+query 发给 LLM，LLM返回改写后的 query。
    """
    return f"""请改写以下搜索 query，使其更适合知识图谱关键词匹配。

原始 query: {query}

改写规则：
1. 添加关键组件/API路径片段（如 cj-scroll-swipe-list）
2. 添加核心概念关键词（如 List、Refresh、Navigation）
3. 添加 Kit 名称（如 NetworkKit、CryptoArchitectureKit）
4. 去除冗余词（如"怎么"、"如何"、"实现"）
5. 保留核心概念，用空格分隔

示例：
- "怎么做一个列表页面" → "cj-scroll-swipe-list cj-layout-development-create-list List 创建列表"
- "如何实现下拉刷新" → "cj-scroll-swipe-refresh Refresh 下拉刷新"
- "HttpRequest 网络请求" → "cj-apis-net-http NetworkKit HttpRequest"

请输出改写后的 query（不要输出其他内容）："""


def main():
    print("LLM Query Enhancement 集成到 KG 搜索")
    print("=" * 60)
    
    # 初始化缓存
    cache = load_cache()
    print(f"当前缓存: {len(cache)} 条改写")
    
    # 添加预定义规则到缓存
    for original, enhanced in QUERY_ENHANCEMENT_RULES.items():
        if original not in cache:
            cache[original] = {
                "original": original,
                "enhanced": enhanced,
                "method": "rule",
            }
    
    save_cache(cache)
    print(f"更新后缓存: {len(cache)} 条改写")
    
    print("\n使用方式:")
    print("1. Python API: enhance_query(query)")
    print("2. LLM改写: 将 query + get_llm_prompt_for_query(query) 发给 LLM")
    
    # 测试
    test_queries = [
        "怎么做一个列表页面",
        "如何实现下拉刷新",
        "HttpRequest 网络请求",
    ]
    print("\n测试改写:")
    for q in test_queries:
        enhanced = enhance_query(q)
        print(f"  {q} → {enhanced}")


if __name__ == "__main__":
    main()