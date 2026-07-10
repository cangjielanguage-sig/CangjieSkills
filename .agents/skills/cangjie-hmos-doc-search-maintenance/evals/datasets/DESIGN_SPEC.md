# 测评集设计规范

## 一、设计原则

### 1.1 数量要求

| 查询类型 | 数量要求 | 覆盖范围 |
|---------|---------|---------|
| api_lookup | 20条 | cj-apis-* 目录（137个） |
| enumeration | 20条 | 主要API类的属性/方法 |
| reverse_lookup | 20条 | 常见效果→组件映射 |
| how_to | 20条 | 核心组件用法 |
| constrained | 20条 | 条件/版本/平台约束 |
| semantic_fuzzy | 20条 | 性能/状态/路由问题 |
| comparison | 20条 | 常见组件对比 |
| composition | 20条 | 多组件组合场景 |
| cross_ecosystem | 20条 | Android/iOS/React类比 |
| workflow | 20条 | 主要流程步骤 |
| performance_boundary | 20条 | 性能极限问题 |
| **总计** | **220条** | |

### 1.2 文档目录覆盖

| 领域 | 目录数 | 用例覆盖目标 |
|------|--------|-------------|
| cj-scroll-swipe-* | 12 | 每组件至少1条how_to |
| cj-state-* | 6 | 状态管理核心场景 |
| cj-apis-* (top50) | 50 | 主流API各至少1条 |
| cj-animation-* | 9 | 动画相关场景 |
| cj-navigation-* | 4 | 路由导航场景 |
| cj-ability-* | 10+ | Ability生命周期 |
| cj-media-* | 6 | 媒体相关 |
| 其他 | 760+ | 按重要性抽样 |

---

## 二、最优答案判断标准

### 2.1 判断流程

```
Step 1: CLI搜索验证
  命令: python cli.py search "关键词" --graph doc -b -k 10
  目的: 确认路径存在，获取候选路径

Step 2: 内容相关性判断
  检查: 文档description是否直接回答query
  权重: 40%

Step 3: 路径权威性判断
  规则: .overview.md > guide.md > _more.md > 具体类定义
  权重: 30%

Step 4: 覆盖完整性判断
  检查: 组合查询是否覆盖所有概念
  权重: 30%

Step 5: 最终确定acceptable_paths
```

### 2.2 路径权威性排序

| 路径类型 | 权威等级 | 说明 |
|---------|---------|------|
| `.overview.md` | ★★★★★ | 概述文档，最权威 |
| `guide.md` | ★★★★☆ | 指南文档 |
| `_2more.md` / `_3more.md` | ★★★☆☆ | 详细用法 |
| `class_XXX\.overview.md` | ★★☆☆☆ | 类定义概述 |
| `func_XXX.md` | ★☆☆☆☆ | 具体方法 |

### 2.3 示例判断

```json
{
  "query": "List滑动卡顿怎么优化",
  "cli_search_results": [
    "cj-state-rendering-lazyforeach\\LazyForEach\\.overview.md",  // 懒加载核心方案
    "cj-scroll-swipe-list\\List\\List_2more.md",                 // List用法
    "cj-scroll-swipe-list\\List\\基础类型定义\\class_ListScroller\\.overview.md"  // 滚动控制
  ],
  "judgment": {
    "relevance": {
      "LazyForEach": "懒加载是核心优化方案 → 高相关",
      "List": "List用法是基础参考 → 中相关",
      "ListScroller": "滚动控制是技术细节 → 辅助"
    },
    "authority": {
      "LazyForEach.overview.md": "概述文档 → 最高权威",
      "List_2more.md": "详细用法 → 中等权威",
      "class_ListScroller.overview.md": "类定义概述 → 中等权威"
    },
    "coverage": "覆盖了懒加载(ListScroller)两大优化方向 → 完整"
  },
  "acceptable_paths": [
    "cj-state-rendering-lazyforeach\\LazyForEach\\.overview.md",
    "cj-scroll-swipe-list\\List\\List_2more.md",
    "cj-scroll-swipe-list\\List\\基础类型定义\\class_ListScroller\\.overview.md"
  ],
  "acceptable_paths_count": 3,
  "acceptable_paths_reason": "模糊查询需多方案覆盖"
}
```

---

## 三、Baseline设定依据

### 3.1 实测数据来源

| 数据来源 | 文件位置 | 关键数据 |
|---------|---------|---------|
| 当前评测结果 | `data/agent_eval_llm_v3.json` | real_session: 84% recall |
| TEST_GUIDE记录 | `TEST_GUIDE.md` | Agent语义搜索: 76-84% |
| 阶段性报告 | `阶段性报告-15K-Hybrid-Equal-graphify.md` | fusion: 85-100% |

### 3.2 实测Baseline值

| 评测集 | 实测Recall@K | 来源 |
|--------|-------------|------|
| real_session @5 | **84%** | agent_eval_llm_v3.json |
| paraphrase @5 | **85.7%** | TEST_GUIDE.md |
| composition @5 | **80%** | TEST_GUIDE.md |

### 3.3 按类型Baseline估计

| 类型 | Baseline | 依据 |
|------|---------|------|
| **api_lookup** | 95%+ | 现有评测中精确查询命中率最高 |
| **enumeration** | 90%+ | 明确的属性/方法查询 |
| **reverse_lookup** | 85%+ | 效果→组件映射较直接 |
| **how_to** | 80-90% | real_session中占比最高，表现稳定 |
| **constrained** | 70% | 条件约束增加复杂度 |
| **semantic_fuzzy** | 75-85% | 现有评测中模糊查询表现 |
| **comparison** | 80% | 双侧对比需两个都命中 |
| **composition** | 70-80% | TEST_GUIDE实测80%，难度较高 |
| **cross_ecosystem** | 85% | real_session中类比查询表现好 |
| **workflow** | 75% | 流程需多步骤覆盖 |
| **performance_boundary** | 70% | 极限性能问题较复杂 |

### 3.4 Baseline公式

```
类型Baseline = f(实测数据, 查询复杂度)

f(data, complexity) = 
  实测baseline × (1 - complexity_factor)

complexity_factor:
  - 精确查询: 0
  - 单概念推理: 0.1
  - 多概念组合: 0.2
  - 条件约束: 0.15
```

---

## 四、路径数量设置规则

### 4.1 规则表

| 查询类型 | 路径数量 | 规则名称 | 判断依据 |
|---------|---------|---------|---------|
| api_lookup | 1 | **精确唯一** | 查询意图明确→唯一答案 |
| enumeration | 1 | **列表唯一** | 属性列表在单一文档 |
| reverse_lookup | 1 | **映射唯一** | 效果→单一组件 |
| how_to | 1 | **用法唯一** | 用法指南在单一文档 |
| constrained | 1 | **方案唯一** | 条件下的单一解决方案 |
| semantic_fuzzy | 2-3 | **多解覆盖** | 症状描述→多种解决方案 |
| comparison | 2 | **双侧对比** | A和B各自核心文档 |
| composition | N | **概念均分** | N个概念→N条文档 |
| cross_ecosystem | 1-2 | **映射对应** | 可能对应1或多个组件 |
| workflow | 2-3 | **流程串联** | 步骤涉及多文档 |
| performance_boundary | 2-3 | **多方案覆盖** | 性能优化多方案 |

### 4.2 具体路径选择

**精确类(1条)**：选择权威性最高的路径
```
选择规则: .overview.md > guide.md > _more.md
```

**多解类(2-3条)**：选择相关性高的不同方案
```
选择规则: 
  1. 不同优化方案（如懒加载 vs 滚动控制）
  2. 不同概念核心文档（组合查询）
  3. 主文档 + 辅助文档（流程查询）
```

---

## 五、用例设计模板

### 5.1 标准模板

```json
{
  "query": "用户查询文本",
  "intent": "查询意图说明",
  "category": "查询类型",
  "capability": "技术领域",
  "query_style": "表达方式",
  "difficulty": "难度等级",
  
  "expected_keywords": {
    "keywords_en": ["英文关键词"],
    "keywords_zh": ["中文关键词"]
  },
  
  "acceptable_paths": ["完整具体路径"],
  "acceptable_paths_count": 1,
  "acceptable_paths_reason": "路径数量依据",
  "path_judgment": {
    "relevance": "相关性判断",
    "authority": "权威性判断",
    "coverage": "覆盖性判断"
  },
  
  "resource_constraints": {
    "expected_latency_ms": 50,
    "expected_token_input": 100,
    "expected_token_output": 50
  },
  
  "baseline_expected": {
    "success@1": 0.85,
    "success@3": 0.95,
    "baseline_source": "实测数据来源"
  },
  
  "source": "v2-design-规范"
}
```

---

## 六、生成流程

```
1. 领域抽样
   ├─ cj-scroll-swipe-* (12个) → 每组件抽样
   ├─ cj-state-* (6个) → 状态管理抽样
   ├─ cj-apis-* (top50) → 主流API抽样
   └─ 其他按重要性抽样

2. 查询设计
   ├─ 从真实场景提取query
   ├─ 按类型分配query
   └─ 确保难度分布合理

3. 路径验证
   ├─ CLI搜索确认路径存在
   ├─ 人工判断相关性
   └─ 记录判断依据

4. Baseline设定
   ├─ 基于实测数据
   ├─ 考虑复杂度调整
   └─ 记录数据来源
```

---

## 七、验收标准

| 检查项 | 标准 |
|--------|------|
| 类型覆盖 | 每类型≥20条 |
| 领域覆盖 | 覆盖cj-apis-* top50 |
| 路径格式 | 完整具体路径 |
| 路径验证 | CLI搜索确认存在 |
| 判断记录 | 含relevance/authority/coverage说明 |
| Baseline来源 | 标注实测数据来源 |
| 难度分布 | normal/compound/hard合理分布 |

---

**创建日期**: 2026-05-18
**版本**: v2-design-spec
**状态**: 设计规范