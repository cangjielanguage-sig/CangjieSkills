# MCP server 接入说明

## 启动方式

MCP stdio server 提供 7 个工具给 code agent：

```
query_graph      语义/关键词搜索（跨概念/模糊描述首选）
get_node         节点详情（community/layer/source_file）
get_neighbors    邻居遍历（"这个 API 的典型搭档"）
get_community    社区详情（一个领域里的全部节点）
god_nodes        度中心性 top N（领域核心 API）
graph_stats      图谱规模统计
shortest_path    两节点最短路径（"A 和 B 怎么关联"）
```

## 在 claude-code 注册

编辑 `~/.claude/settings.json`（或项目级 `.claude/settings.local.json`），在 `mcpServers` 下加：

```json
{
  "mcpServers": {
    "cangjie-graphify": {
      "command": "python",
      "args": [
        "<项目根绝对路径>/.agents/skills/knowledge-graph-template/mcp_server.py"
      ]
    }
  }
}
```

重启 claude-code 后 `cangjie-graphify` 的 7 个工具就会出现在工具列表里。

## 手动测试

```bash
cd .agents/skills/knowledge-graph-template
cat > /tmp/test.jsonl <<'EOF'
{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"test","version":"0.1"}}}
{"jsonrpc":"2.0","method":"notifications/initialized"}
{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"graph_stats","arguments":{}}}
EOF
python mcp_server.py < /tmp/test.jsonl
```

## 已知限制

- **merged 图 id 合并不完整**：不少子图节点（如 `list_5more_9f09686f_h1_list`）在 merged 图里查不到，server 已自动回退到子图搜索器。P1 重建图谱后修复。
- **god_nodes 有代码块 lang 标签噪声**（`cangjie code` / `text code` 等），P1 在抽取 prompt 里过滤。
- **shortest_path 不支持跨子图**：两个节点若属于不同子图（harmonyos vs std），server 返回 hint 提示，让 agent 在同一领域内重新查询。
