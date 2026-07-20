---
name: cangjie-hmos-doc-search-maintenance
description: "指导 agent 独立完成 cangjie-docs 的 grep vs graph 对比评测。agent 用 PowerShell 命令做 grep 搜索，用 cli.py 做 graph 搜索，逐条对比命中率和耗时，输出 Markdown 报告。包含 10 条采样测试。不依赖 Python 脚本。"
---

# grep vs graph 对比评测 — Agent 独立完成指导

## 目的

指导 agent 独立完成 cangjie-docs 语料的 grep（字面匹配）与 graph（语义图谱）对比评测。agent 直接使用 PowerShell 命令和 cli.py 接口完成搜索，无需编写 Python 脚本。

## 关键路径

| 用途 | 路径 |
|------|------|
| 源文档语料 | `.agents/skills/cangjie-docs/` |
| graph 图谱 | `.agents/skills/cangjie-hmos-doc-search/doc-graph/data/doc/graph_cj.json` |
| graph 搜索 CLI | `.agents/skills/cangjie-hmos-doc-search/doc-graph/cli.py` |
| 评测集（119 条） | `.agents/skills/cangjie-hmos-doc-search-maintenance/evals/datasets/eval_queries_cangjie.jsonl` |
| 关键词映射 | `.agents/skills/cangjie-hmos-doc-search-maintenance/evals/keywords/keywords_cangjie.json` |

## 工作流程

对每条 query 重复以下 4 步：

### Step 1: 读取 query 和关键词

```powershell
# 查看第 N 条 query（以 Q1 为例，将 qs[0] 改为 qs[N-1]）
python -c "import json; qs=[json.loads(l) for l in open(r'.agents/skills/cangjie-hmos-doc-search-maintenance/evals/datasets/eval_queries_cangjie.jsonl',encoding='utf-8')]; q=qs[0]; print('Q1:', q['query']); print('期望:', q['acceptable_paths'])"

# 查看该 query 的搜索关键词（将 kw['1'] 改为 kw['N']）
python -c "import json; kw=json.load(open(r'.agents/skills/cangjie-hmos-doc-search-maintenance/evals/keywords/keywords_cangjie.json',encoding='utf-8')); k=kw['1']; print('keywords_en:', k['keywords_en']); print('keywords_zh:', k['keywords_zh'])"
```

### Step 2: Graph 搜索

```powershell
cd .agents\skills\cangjie-hmos-doc-search\doc-graph

# 将搜索字符串替换为 Step 1 的 keywords_en + keywords_zh（空格拼接，去重）
python cli.py search "HashMap put store 键值对" --graph doc --graph-path "data/doc/graph_cj.json" -b -k 5
```

### Step 3: Grep 搜索

```powershell
cd .agents\skills\cangjie-docs

# 将 @(...) 内的关键词替换为 Step 1 的 keywords_en + keywords_zh（去重）
<#
递归扫描 .agents\skills\cangjie-docs 目录下的所有 Markdown 文件，使用 Step 1 生成并去重后的中英文关键词进行全文匹配，统计每个文件命中的不同关键词数量作为相关性分数，过滤掉未命中任何关键词的文件，再按分数从高到低排序并输出最相关的前 5 个文件；其中 Score 表示命中的关键词种类数，而不是关键词出现的总次数。
#>
$kws=@("HashMap","put","store","键值对"); Get-ChildItem -Recurse -Filter *.md | ForEach-Object { $c=Get-Content $_.FullName -Raw; $s=($kws | Where-Object {$c -match $_}).Count; if($s -gt 0){[PSCustomObject]@{File=$_.FullName.Replace('D:\ZSY\CangjieSkills\.agents\skills\cangjie-docs\','').Replace('\','/');Score=$s}} } | Sort-Object Score -Descending | Select-Object -First 5
```

### Step 4: 对比判定

对每条 query 记录以下信息：

| 记录项 | 说明 |
|------|------|
| 期望路径 | eval_queries_cangjie.jsonl 中的 `acceptable_paths` |
| Graph Top-5 | cli.py 返回的 `source_file` 列表 |
| Grep Top-5 | PowerShell 返回的 File 列表 |
| Graph 状态 | Top-5 中是否包含期望路径 → FULL / MISS |
| Grep 状态 | 同上 |
| Graph 耗时 | cli.py 输出的 `latency_ms`（直接读取） |
| Grep 耗时 | 用 `Measure-Command { ... }` 包裹 grep 命令，读取 `TotalMilliseconds` |
| Graph Token | 由 token-logger 插件自动记录（见下方 Token 统计方法） |
| Grep Token | 同上 |

判定规则：Top-5 中任一路径与期望路径匹配（子串包含或同目录）即为 FULL，否则 MISS。

**耗时测量方法：**
- Graph：cli.py 输出中包含 `latency_ms` 字段，直接读取
- Grep：用 `Measure-Command` 包裹 Step 3 的 PowerShell 命令，示例：
```powershell
Measure-Command { $kws=@("HashMap","put","store","键值对"); Get-ChildItem -Recurse -Filter *.md | ForEach-Object { $c=Get-Content $_.FullName -Raw; $s=($kws | Where-Object {$c -match $_}).Count; if($s -gt 0){[PSCustomObject]@{File=$_.Name;Score=$s}} } | Sort-Object Score -Descending | Select-Object -First 5 } | Select-Object TotalMilliseconds
```

**Token 消耗统计方法（API 级精确统计）：**

使用 opencode 插件 `token-logger.ts` 自动记录每次 LLM API 调用的真实 token 数据，无需手动估算。

- 插件路径：`.opencode/plugins/token-logger.ts`
- 插件配置：`opencode.json` 中 `"plugin": ["./.opencode/plugins/token-logger.ts"]`
- 日志路径：`.agents/skills/cangjie-hmos-doc-search-maintenance/evals/token_log.jsonl`
- 日志格式（每行一个 JSON）：
```json
{"ts":"2026-07-13T03:34:23Z","sessionID":"...","modelID":"GLM-5.2","cost":0,"input":737,"output":115,"reasoning":1031,"cache_read":0,"cache_write":0,"total":1883}
```

工作原理：
1. 插件监听 opencode 的 `message.updated` 事件
2. 每当 LLM API 返回响应时，从 `AssistantMessage.tokens` 字段提取 input/output/reasoning
3. 自动追加到 `token_log.jsonl`

使用方式：
1. 确保 `opencode.json` 中已注册插件（重启 opencode 后生效）
2. 记录评测开始前的日志条数作为 baseline
3. 正常执行 grep vs graph 对比评测（插件自动记录）
4. 评测完成后读取 `token_log.jsonl`，分析 baseline 之后的新条目
5. 去重（同一消息会触发两次 `message.updated`，产生重复条目）后汇总

日志分析命令：
```powershell
# 查看日志总条数
(Get-Content ".agents/skills/cangjie-hmos-doc-search-maintenance/evals/token_log.jsonl").Count

# 查看最近条目
Get-Content ".agents/skills/cangjie-hmos-doc-search-maintenance/evals/token_log.jsonl" -Tail 5

# 汇总 token（去重：按 messageID 去重，跳过 total=0 的空消息）
python -c "
import json
seen = set()
total_input = total_output = total_reasoning = 0
for line in open(r'.agents/skills/cangjie-hmos-doc-search-maintenance/evals/token_log.jsonl', encoding='utf-8'):
    e = json.loads(line)
    if e.get('total', 0) == 0: continue
    mid = e.get('messageID', '')
    if mid in seen: continue
    seen.add(mid)
    total_input += e.get('input', 0)
    total_output += e.get('output', 0)
    total_reasoning += e.get('reasoning', 0)
print(f'去重后: input={total_input}, output={total_output}, reasoning={total_reasoning}, total={total_input+total_output+total_reasoning}')
"
```

## 10 条采样测试

先跑以下 10 条，验证流程后再 resume 扩展到 119 条：

| Q# | 难度 | 类别 | 查询 |
|---:|:---:|------|------|
| 1 | 简单 | api_lookup | HashMap怎么存键值对 |
| 5 | 简单 | api_lookup | File怎么读写文件内容 |
| 17 | 中等 | enumeration | Cangjie标准库有哪些集合数据结构 |
| 50 | 中等 | how_to | 仓颉怎么用正则表达式匹配邮箱地址 |
| 100 | hard | reverse_lookup | 怎么把对象转成JSON字符串 |
| 104 | hard | reverse_lookup | 怎么在多线程间传递消息 |
| 105 | hard | reverse_lookup | 定时执行任务不用sleep循环 |
| 108 | hard | semantic_fuzzy | 变量出了作用域还能访问吗 |
| 113 | hard | cross_ecosystem | Python的json.loads在Cangjie里对应什么 |
| 117 | hard | constrained | 内存有限时怎么处理超大JSON |

## 输出格式

报告保存到 `evals/reports/grep_vs_graph_agent.md`，格式如下：

**总体统计：**

| 指标 | Graph | Grep |
|------|:---:|:---:|
| Recall@5 | ?% | ?% |
| FULL 数 | ? | ? |
| MISS 数 | ? | ? |
| 总耗时 | ?ms | ?ms |
| 平均每条耗时 | ?ms | ?ms |
| 总 Token 消耗 | ? (插件自动记录) | ? (插件自动记录) |
| 平均每条 Token | ? | ? |

**逐条对比：**

### Q1 [api_lookup] HashMap怎么存键值对
- 期望路径: `cj-std/collection/class_HashMap.md`
- 搜索关键词: HashMap, put, store, 键值对

| # | Graph 返回路径 | 分数 | Grep 返回路径 | 命中数 |
|:---:|------|:---:|------|:---:|
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |

| 指标 | Graph | Grep |
|------|:---:|:---:|
| 耗时 | ?ms | ?ms |
| Token | ? | ? |
| 状态 | ✅ FULL | ❌ MISS |

## 注意事项

- Grep 跳过 `.overview.md` 和 `.abstract.md`（以 `.` 开头的文件名）
- Graph 必须用 `--graph-path "data/doc/graph_cj.json"`，否则默认加载 harmonyos 图谱
- 关键词从 `keywords_cangjie.json` 按 query ID（1-119）索引
- Grep 命令中的路径前缀需根据实际工作目录调整
