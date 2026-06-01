---
name: doc-card
description: "鸿蒙仓颉应用开发本地检索技能，提供任务卡、API 卡、示例卡、文档卡四层结构化搜索，适用于 UI/API/框架机制/状态管理/构建报错日志知识检索。"
tags: [workflow, platform]
---

# 仓颉鸿蒙文档检索 Skill（V3）

## 定位

负责把鸿蒙仓颉开发问题或构建报错日志线索收敛成四类检索对象：

- 任务卡：回答"我要实现什么功能"
- API 卡：回答"应该用哪个组件或接口"
- 示例卡：回答"代码怎么写"
- 文档卡：回答"原始文档、概览、排错信号在哪里"

本 Skill 仅提供**搜索运行时**，索引构建与评测门禁由 `cangjie-harmonyos-doc-search-maintenance/card/` 负责。

## 使用入口

```bash
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/doc-card/search_v3.py "我想写一个滑动列表"
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/doc-card/search_v3.py "List" --mode api
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/doc-card/search_v3.py "滚动事件示例" --mode example --json
```

日常检索通过顶层 `unified_search.py --engine card` 调用，也可直接调用 `search_v3.py`。

## 用户态在线使用规范

1. 先由当前对话中的 agent 做语义理解，不要求用户提供任何 url/key 或模型配置
2. 功能诉求 → `search_v3.py --mode task` 或默认 `--mode auto`
3. 属性/事件/组件/装饰器/接口 → `search_v3.py --mode api`
4. 代码写法/demo/示例 → `search_v3.py --mode example`
5. 排错问题 → 先看任务卡，再补相关 API 卡
6. 最终回答必须以本地索引命中的文档结果为依据，不直接凭模型记忆回答

## 检索模式

- `auto`：自动判定任务/API/示例
- `task`：优先返回任务卡，并补相关 API、示例
- `api`：优先返回 API 卡，并补相关任务、示例
- `example`：优先返回示例卡，并补相关 API、任务
- `doc`：优先返回文档卡，并补相关任务、API、示例

## V3 使用规范

1. 功能诉求时优先 `--mode task`，或直接用默认 `--mode auto`
2. 明确问组件、属性、事件、装饰器时优先 `--mode api`
3. 准备生成代码前，至少补一次 `--mode example`
4. 命中多个候选时，先读任务卡和示例卡，再下钻 API 明细

## 与 doc-graph 的关系

本 Skill 与 `doc-graph`（知识图谱）**平权并存**，按 query 类型分发。两者共享同一套文档源。日常检索通过顶层 `unified_search.py --engine fusion` 自动融合 card + graph 结果。

| Query 特征 | 首选引擎 | 具体调用 |
|---|---|---|
| 明确 API / 组件 / 装饰器名 | V3 | `search_v3.py "<q>" --mode api --json --limit 5` |
| 属性 / 事件 / 枚举值穷举 | V3 | `search_v3.py "<q>" --mode api` |
| 错误码 / 构建日志关键字 | V3 | `search_v3.py "<q>" --mode auto` |
| 写代码前找示例 | V3 | `search_v3.py "<q>" --mode example` |
| 功能实现类 | V3 默认 + KG 组合 | V3 `--mode task` + KG `search` |
| 跨概念组合 / 语义模糊 / 跨生态类比 | KG | 详见 doc-graph SKILL.md |

### 结果融合规则

当两条引擎同时被调用时：

1. **精确命中优先**：V3 返回的 paths 排在 doc-graph KG 之前
2. **按 source_file / source_paths 去重**：同一文档不重复
3. **doc-graph KG 补充邻域**：V3 没覆盖的相关概念从 KG neighbors 拉进来
4. **矛盾时以 V3 为准**：API 名、签名、参数类型这类事实性信息以 V3 卡片为单一事实源

## 注意事项

- V3 不依赖远端服务
- `index/` 缺失时提示使用维护 Skill 构建索引
- 用户态在线查询优先复用当前 agent 的理解能力，然后再调用本地检索