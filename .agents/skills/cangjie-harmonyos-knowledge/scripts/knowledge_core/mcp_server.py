from __future__ import annotations

import json
import sys
from typing import Any

from .config import AppConfig
from .search import Searcher


class MCPServer:
    def __init__(self, cfg: AppConfig) -> None:
        self.searcher = Searcher(cfg)

    def serve(self) -> None:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                request = json.loads(line)
                response = self.handle(request)
            except Exception as exc:
                response = {"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(exc)}}
            if response is None:
                continue
            sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
            sys.stdout.flush()

    def handle(self, request: dict[str, Any]) -> dict[str, Any] | None:
        method = request.get("method")
        req_id = request.get("id")
        params = request.get("params") or {}
        if method == "initialize":
            return self.reply(req_id, {"protocolVersion": "2024-11-05", "capabilities": {"tools": {}}, "serverInfo": {"name": "cangjie-harmonyos-knowledge", "version": "0.1.0"}})
        if method == "notifications/initialized":
            return None
        if method == "tools/list":
            return self.reply(req_id, {"tools": tool_specs()})
        if method == "tools/call":
            name = params.get("name")
            args = params.get("arguments") or {}
            result = self.call_tool(name, args)
            return self.reply(req_id, {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=2)}]})
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Unknown method: {method}"}}

    def call_tool(self, name: str, args: dict[str, Any]) -> Any:
        if name == "search_docs":
            return self.searcher.search(
                str(args.get("query") or ""),
                top_k=int(args.get("top_k") or 8),
                scope=str(args.get("scope") or "all"),
                embedding_mode=args.get("embedding_mode"),
                version=args.get("version"),
            )
        if name == "lookup_symbol":
            return self.searcher.lookup_symbol(
                str(args.get("name") or ""),
                include_members=bool(args.get("include_members", False)),
                include_examples=bool(args.get("include_examples", False)),
                version=args.get("version"),
            )
        if name == "read_doc":
            return self.searcher.read_doc(
                str(args.get("ref") or ""),
                mode=str(args.get("mode") or "section"),
                max_chars=int(args.get("max_chars") or 12000),
                version=args.get("version"),
            )
        if name == "find_examples":
            return self.searcher.find_examples(str(args.get("query_or_symbol") or ""), top_k=int(args.get("top_k") or 5), version=args.get("version"))
        if name == "related_docs":
            return self.searcher.related_docs(str(args.get("ref") or ""), top_k=int(args.get("top_k") or 8), version=args.get("version"))
        if name == "status":
            return self.searcher.status()
        raise ValueError(f"Unknown tool: {name}")

    @staticmethod
    def reply(req_id: Any, result: Any) -> dict[str, Any]:
        return {"jsonrpc": "2.0", "id": req_id, "result": result}


def tool_specs() -> list[dict[str, Any]]:
    return [
        {
            "name": "search_docs",
            "description": "Search Cangjie HarmonyOS docs with deterministic and optional embedding retrieval.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "top_k": {"type": "integer", "default": 8},
                    "scope": {"type": "string", "enum": ["all", "api", "guide", "examples"], "default": "all"},
                    "embedding_mode": {"type": "string", "enum": ["off", "search", "all"]},
                    "version": {"type": "string", "description": "SDK/docs version, or 'all' for all versions"},
                },
                "required": ["query"],
            },
        },
        {
            "name": "lookup_symbol",
            "description": "Look up an API symbol and signature. Members/examples are opt-in to keep responses bounded.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "include_members": {"type": "boolean", "default": False},
                    "include_examples": {"type": "boolean", "default": False},
                    "version": {"type": "string"},
                },
                "required": ["name"],
            },
        },
        {
            "name": "read_doc",
            "description": "Read a section or full document by ref path#anchor.",
            "inputSchema": {"type": "object", "properties": {"ref": {"type": "string"}, "mode": {"type": "string"}, "version": {"type": "string"}}, "required": ["ref"]},
        },
        {
            "name": "find_examples",
            "description": "Find Cangjie code examples.",
            "inputSchema": {"type": "object", "properties": {"query_or_symbol": {"type": "string"}, "version": {"type": "string"}}, "required": ["query_or_symbol"]},
        },
        {
            "name": "related_docs",
            "description": "Find related docs by Markdown links and local graph.",
            "inputSchema": {"type": "object", "properties": {"ref": {"type": "string"}, "version": {"type": "string"}}, "required": ["ref"]},
        },
        {"name": "status", "description": "Show index and embedding status.", "inputSchema": {"type": "object", "properties": {}}},
    ]


def run_mcp(cfg: AppConfig) -> None:
    MCPServer(cfg).serve()
