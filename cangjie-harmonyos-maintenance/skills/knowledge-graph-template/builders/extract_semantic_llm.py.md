# builders/extract_semantic_llm.py — LLM 语义提取

基于 graphify 实现的 LLM 语义提取模块，使用大语言模型从文档中提取概念、关系、rationale。

---

## 与简化版对比

| 功能 | 简化版 `extract_semantic.py` | LLM 版 `extract_semantic_llm.py` |
|------|:----------------------------:|:-------------------------------:|
| 标题提取 | ✅ 规则匹配 | ✅ 规则 + LLM |
| 链接提取 | ✅ 规则匹配 | ✅ 规则 + LLM |
| **概念节点** | ❌ | ✅ 提取文档中的关键术语 |
| **rationale 边** | ❌ | ✅ 提取设计原因、决策说明 |
| **跨文档关联** | ❌ | ✅ 相同概念连接不同文档 |
| **INFERRED 边** | ❌ | ✅ 发现隐式依赖 |
| **semantically_similar_to** | ❌ | ✅ 语义相似但无结构关联 |
| **超边（hyperedges）** | ❌ | ✅ 多节点共享概念 |
| 缓存支持 | ❌ | ✅ 避免重复提取 |
| 需要 API key | ❌ | ✅ 需要 OPENAI_API_KEY |
| 成本 | 免费 | Token 成本 |

---

## 使用方法

### CLI 命令

```bash
# 启用 LLM 语义提取（需要 OPENAI_API_KEY）
export OPENAI_API_KEY=sk-...
python cli.py build ./docs --semantic --output graph.json

# 深度模式（更激进的 INFERRED 边）
python cli.py build ./docs --semantic --deep --output graph.json

# 指定 LLM 模型
python cli.py build ./docs --semantic --llm-model gpt-4o --output graph.json
```

### Python API

```python
from pathlib import Path
from builders.extract_semantic_llm import extract_docs_with_llm_sync, LLMConfig

# 配置 LLM
config = LLMConfig(
    api_key="sk-...",           # 或使用环境变量 OPENAI_API_KEY
    api_base="https://api.openai.com/v1",
    model="gpt-4o-mini",        # 推荐：成本低、速度快
    temperature=0.3,            # 低温度：更一致的结果
    max_tokens=4096,
)

# 提取文档
result = extract_docs_with_llm_sync(
    paths=["docs/api.md", "docs/guide.md"],
    root=Path("./docs"),
    config=config,
    deep_mode=False,            # True: 更激进的 INFERRED 边
    chunk_size=22,              # 每个chunk处理22个文件
    max_concurrent=3,           # 最大并发chunk数
    use_cache=True,             # 启用缓存
)

print(f"节点: {len(result['nodes'])}")
print(f"边: {len(result['edges'])}")
print(f"超边: {len(result['hyperedges'])}")
print(f"Token: {result['input_tokens']} 输入, {result['output_tokens']} 输出")
```

---

## 提取内容详解

### 1. 概念节点

LLM 从文档内容中识别关键概念，如：

```
文档: docs/uiability.md

提取节点:
- UIAbility (概念)
- onCreate() (方法)
- WindowStage (关联概念)
- 生命周期 (概念)

边:
- UIAbility --[has_method]--> onCreate()
- UIAbility --[uses]--> WindowStage
- UIAbility --[conceptually_related_to]--> 生命周期
```

### 2. rationale 边

LLM 识别文档中解释设计原因的部分：

```
文档: docs/architecture.md

内容: "采用分层架构是为了方便测试和替换实现"

提取:
- rationale_node: "采用分层架构是为了方便测试和替换实现"
- edge: rationale_node --[rationale_for]--> 分层架构
```

### 3. semantically_similar_to 边

LLM 发现语义相似但无结构关联的节点：

```
文档 1: docs/auth.md (概念: 用户认证)
文档 2: docs/login.md (概念: 登录流程)

提取:
- 用户认证 --[semantically_similar_to]--> 登录流程
  (confidence=0.85, INFERRED)
```

### 4. hyperedges

LLM 识别多节点共享概念：

```
文档: docs/security.md

提取:
- hyperedge: "安全认证流程"
  nodes: [用户认证, Token验证, 权限检查]
  relation: participate_in
```

---

## 分块策略

参考 graphify 实现：

- **chunk_size = 22**：每个 chunk 处理 22 个文件
- **并发控制**：最多 3 个 chunk 同时处理
- **缓存**：每个文件提取后缓存，下次复用

```
2900 个文档文件 → 132 个 chunk
估计时间: ~132 * 45 / 3 = 1980 秒 (~33 分钟)
```

---

## Deep Mode

深度模式启用更激进的推断：

| 特性 | Normal Mode | Deep Mode |
|------|:-----------:|:---------:|
| INFERRED 边 | 仅明确关联 | 包含间接依赖 |
| 不确定性处理 | 省略不确定 | 标记为 AMBIGUOUS |
| 边数量 | ~N | ~2N |
| 准确率 | 高 | 中（需要人工审核） |

---

## 输出格式

```json
{
  "nodes": [
    {
      "id": "uiability_overview",
      "label": "UIAbility 概览",
      "file_type": "document",
      "source_file": "docs/uiability.md",
      "source_location": "H1",
      "source_url": null,
      "author": null,
      "contributor": null
    }
  ],
  "edges": [
    {
      "source": "uiability_overview",
      "target": "windowstage",
      "relation": "conceptually_related_to",
      "confidence": "EXTRACTED",
      "confidence_score": 1.0,
      "source_file": "docs/uiability.md",
      "source_location": "L45",
      "weight": 1.0
    }
  ],
  "hyperedges": [
    {
      "id": "auth_flow",
      "label": "认证流程",
      "nodes": ["login", "token_validate", "permission_check"],
      "relation": "participate_in",
      "confidence": "INFERRED",
      "confidence_score": 0.75,
      "source_file": "docs/security.md"
    }
  ],
  "input_tokens": 15000,
  "output_tokens": 3000
}
```

---

## 成本估算

| 模型 | 输入成本 | 输出成本 | 22 文件/chunk 估算 |
|------|---------|---------|-------------------|
| gpt-4o-mini | $0.15/1M | $0.60/1M | ~$0.05/chunk |
| gpt-4o | $2.50/1M | $10/1M | ~$0.50/chunk |
| gpt-3.5-turbo | $0.50/1M | $1.50/1M | ~$0.10/chunk |

**2900 文档 → 132 chunk → ~$6.6 (gpt-4o-mini)**

---

## 缓存机制

提取结果缓存到 `graphify-out/cache/`：

```
graphify-out/cache/
├── a1b2c3d4e5f6.json    # 文件 1 的提取结果
├── f7e8d9c0b1a2.json    # 文件 2 的提取结果
└── ...
```

- 文件内容变化 → Hash 变化 → 重新提取
- 文件内容不变 → Hash 匹配 → 使用缓存

---

## 错误处理

| 错误类型 | 处理方式 |
|---------|---------|
| 无 API key | 回退到简化版 |
| LLM API 错误 | 回退到简化版 |
| JSON 解析失败 | 警告 + 跳过该 chunk |
| 超时（60s） | 警告 + 跳过该 chunk |
| >50% chunk 失败 | 停止 + 提示重试 |

---

## 使用建议

| 场景 | 推荐方案 |
|------|---------|
| 代码为主（<10% 文档） | 简化版足够 |
| 文档为主（>50% 文档） | LLM 版必需 |
| 需要精确搜索概念 | LLM 版必需 |
| 需要回答设计原因 | LLM 版 + rationale 边 |
| 需要发现隐式关联 | LLM 版 + deep mode |
| 成本敏感 | 简化版 + 手动补关键概念 |

---

## 相关文件

| 文件 | 作用 |
|------|------|
| `extract_semantic.py` | 简化版（无 LLM） |
| `extract_semantic_llm.py` | LLM 版（本文件） |
| `cache.py` | 缓存管理 |
| `cli.py` | CLI 命令入口 |

---

*最后更新: 2026-04-29*