# cangjie-harmonyos-doc-search-maintenance

鸿蒙仓颉文档搜索的构建、评测和维护 Skill — 负责索引重建、图谱构建、LLM 增强、评测集管理和发布门禁。

## 目录结构

```
cangjie-harmonyos-doc-search-maintenance/
├── SKILL.md                  # 维护 Skill 入口定义和三分区结构说明
├── card/                     # 卡片索引构建与评测
│   ├── builder/              # V3 索引构建器
│   ├── evals/                # 评测数据集
│   ├── records/              # 评测结果和历史记录
│   ├── references/           # 参考文档
│   └── scripts/              # 维护和评测脚本
├── graph/                    # 知识图谱构建与评测
│   ├── builder/              # 图谱构建器（doc/code/llm）
│   ├── evals/                # 图谱评测数据和脚本
│   ├── records/              # 评测结果
│   ├── references/           # 参考文档
│   └── scripts/              # 构建和评测脚本
└── fusion/                   # 融合发布门禁（card + graph AB 评测）
│   ├── evals/                # 融合评测数据集（全部 9 个评测集）
│   ├── records/              # 评测结果基线
│   ├── references/           # 参考文档
│   └── scripts/              # 发布门禁和评测脚本
```

## 三分区架构

维护 Skill 按照"对应于谁的评测，就放在谁的目录下面"原则分为三个独立分区：

| 分区 | 职责 | 核心脚本 |
|------|------|----------|
| **card** | V3 索引构建 + 卡片评测 + 卡片回归门禁 | `run_maintenance.py`, `run_ab_eval.py`, `run_v3_regression_gate.py` |
| **graph** | 图谱构建 + 图谱评测 + 三引擎对比 | `run_graph_release_eval.py`, `build_cli.py` |
| **fusion** | 发布总门禁 + 融合 AB 评测 + 评测集管理 | `run_maintenance.py`, `run_release_eval.py`, `run_ab_eval.py` |

### 跨分区依赖

- `fusion/scripts/run_maintenance.py` 调用 `card/scripts/sync_v3_to_graph.py`（card→graph 种子同步）
- `fusion/scripts/run_ab_eval.py` 和 `card/scripts/run_ab_eval.py` 共享相同的 AB 评测逻辑，但 eval-dir 默认值不同
- `graph/evals/run_eval.py` 使用 doc-search 运行时的 card 和 graph 搜索代码

## 维护流程

### 标准维护流程（card）

```bash
# 1. 全量重建 + 评测 + 归档
python card/scripts/run_maintenance.py --mode rule+llm --publish-dir /tmp/publish

# 2. 仅规则模式重建（快速验证）
python card/scripts/run_maintenance.py --mode rule --publish-dir /tmp/publish

# 3. 仅 AB 评测（不重建）
python card/scripts/run_ab_eval.py --eval-dir fusion/evals --output ab_result.json
```

### 标准维护流程（fusion）

```bash
# 1. 全量维护（V3重建 + 图重建 + AB评测 + 种子同步）
python fusion/scripts/run_maintenance.py --mode rule+llm --publish-dir /tmp/publish

# 2. 发布门禁
python fusion/scripts/run_release_eval.py --output-dir /tmp/release-eval
```

### 图谱构建

```bash
# 构建 doc 图谱
python graph/scripts/build_doc_graph.py

# 构建代码图图谱
python graph/scripts/build_code_graph.py

# 验证图数据
python graph/scripts/validate_graph_data.py

# 三引擎对比评测
python graph/scripts/run_graph_release_eval.py --output report.md
```

## 发布门禁规则

| 评测集 | 门禁指标 | 通过阈值 |
|--------|----------|----------|
| eval_queries_user.jsonl (75) | success@5 | >= 0.98 |
| eval_queries_app_agent_dev.jsonl (32) | success@5 | >= 0.98 |
| eval_queries_user_appdev*.jsonl | success@5 | >= 0.95 |
| eval_queries_user_appdev_blind_20260424.jsonl | success@5 | >= 0.80 |
| AB 评测（fusion vs v3 vs graphify） | fusion >= v3 且 fusion >= graphify | 每个 split |

发布状态判定：
- **pass** — 所有门禁通过
- **gray_release** — 门禁通过但 blind 评测 success@5 < 0.95
- **blocked** — 任一门禁失败

## 子模块详细说明

- [card/README.md](card/README.md) — 卡片索引构建与评测
- [graph/README.md](graph/README.md) — 知识图谱构建与评测
- [fusion/README.md](fusion/README.md) — 融合发布门禁

## 与搜索 Skill 的关系

本 Skill 与 `cangjie-harmonyos-doc-search`（搜索运行时）配合使用：

- 本 Skill 负责构建索引和图谱数据 → 搜索 Skill 使用这些数据执行搜索
- 本 Skill 负责评测搜索质量 → 搜索 Skill 提供搜索能力供评测调用
- 本 Skill 负责发布门禁 → 决定搜索 Skill 的索引/图谱是否可以上线