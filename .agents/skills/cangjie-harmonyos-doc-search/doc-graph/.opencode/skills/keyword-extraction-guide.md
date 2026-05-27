---
name: keyword-extraction-guide
description: Guide for extracting search keywords from user queries for knowledge graph search
trigger: /keyword-guide
---

# Keyword Extraction Guide for Knowledge Graph Search

When extracting keywords from user queries to search a knowledge graph, follow these guidelines:

## Core Keywords (必须命中)

Core keywords are the ESSENTIAL concepts that the target document MUST contain. They are the primary search terms that uniquely identify the document.

**Rules for Core:**
1. MUST be specific API/component names (e.g., `Router`, `animateTo`, `PersistentStorage`)
2. MUST be present in the target document's content or keywords
3. NOT generic platform words (e.g., `HarmonyOS`, `API`, `component`)
4. NOT broad concepts alone (e.g., `navigation`, `storage`, `animation`)
5. 1-2 core keywords per language is optimal

**Examples:**
- Query: "Router.pushUrl的参数" → Core: `Router` (specific API)
- Query: "PersistentStorage怎么配置" → Core: `PersistentStorage`
- Query: "animateTo动画怎么用" → Core: `animateTo`

## Context Keywords (上下文补充)

Context keywords provide additional information about the user's intent, helping refine the search.

**Rules for Context:**
1. Specific aspects the user is asking about (e.g., `pushUrl`, `参数`, `配置`)
2. Problem descriptors (e.g., `超时`, `失败`, `不刷新`)
3. Feature-specific terms (e.g., `生命周期`, `权限`, `回调`)
4. NOT generic verbs (e.g., `使用`, `方法`, `介绍`)

**Examples:**
- Query: "Router.pushUrl的参数" → Context: `pushUrl`, `参数`
- Query: "动画卡顿怎么办" → Context: `卡顿`, `性能`

## Synonym Keywords (语义扩展)

Synonym keywords are alternative terms that might be used in documents or by users from other ecosystems.

**When to include Synonyms:**
1. **Cross-ecosystem queries**: Include the original platform term
   - "Android的RecyclerView在鸿蒙对应什么" → Synonym: `RecyclerView`, `ListView`
   - "React的useState对应什么" → Synonym: `useState`, `hooks`

2. **Comparison queries**: Include alternative names or related concepts
   - "Router和Navigation的区别" → Synonym: `页面跳转`, `路由`, `pushUrl`

3. **Semantic fuzzy queries**: Include common misnomers or related problems
   - "状态不刷新怎么办" → Synonym: `响应式`, `UI更新`, `状态同步`

4. **API aliases**: Include common shorthand or abbreviations
   - "AppStorage怎么用" → Synonym: `应用级状态`, `全局状态`

## Keyword Distribution by Query Type

### api_lookup (API查询)
- **Core**: The specific API name
- **Context**: Method/parameter names, usage aspects
- **Synonym**: Alternative API names, related APIs

### enumeration (列举查询)
- **Core**: The main concept being enumerated
- **Context**: `有哪些`, `属性`, `方法`, `回调`
- **Synonym**: Related concepts, sub-components

### comparison (对比查询)
- **Core**: Both items being compared (e.g., `Router`, `Navigation`)
- **Context**: `区别`, `不同`, `对比`
- **Synonym**: Common alternatives, related concepts

### cross_ecosystem (跨生态映射)
- **Core**: The HarmonyOS equivalent API
- **Context**: The platform being mapped from (e.g., `Android`, `React`)
- **Synonym**: The original platform term (e.g., `RecyclerView`, `useState`)

### semantic_fuzzy (语义模糊)
- **Core**: The main concept or API involved
- **Context**: The problem being encountered (e.g., `不刷新`, `失败`, `卡顿`)
- **Synonym**: Related problems, alternative solutions, common error names

## Examples by Category

### api_lookup
```
Query: "HttpRequest的timeout参数怎么设置"
Core: HttpRequest
Context: timeout, 参数
Synonym: (empty - specific enough)
```

### cross_ecosystem
```
Query: "Android的RecyclerView在鸿蒙对应什么"
Core: List (HarmonyOS equivalent)
Context: 长列表, 列表渲染
Synonym: RecyclerView, ListView, LazyForEach
```

### comparison
```
Query: "Router和Navigation有什么区别"
Core: Router, Navigation
Context: 区别, 页面跳转
Synonym: 路由, pushUrl, replaceUrl
```

### semantic_fuzzy
```
Query: "状态改了界面不更新怎么办"
Core: State, 状态管理
Context: 界面不更新, UI刷新
Synonym: 响应式, 状态同步, 观察者
```

## Anti-patterns to Avoid

1. **Generic words in Core**: `API`, `SDK`, `使用`, `方法` → Move to Context or remove
2. **Missing cross-ecosystem terms**: For "Android's X in HarmonyOS", must include `X` in Synonym
3. **Empty Synonym for comparison**: Comparison queries almost always need synonym expansion
4. **Over-specific Core**: "pushUrl参数timeout值" → Core should be `Router`, not `pushUrl`
5. **Missing problem keywords**: "动画卡顿" should have `卡顿` in Context or Synonym