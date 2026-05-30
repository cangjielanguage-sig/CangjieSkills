#!/usr/bin/env python3
"""Generate app-dev expansion and blind eval sets from curated index metadata."""

from __future__ import annotations

import json
import argparse
from datetime import datetime
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = MAINTENANCE_DIR.parent
ROOT = SKILLS_DIR / "cangjie-harmonyos-doc-search"
DOC_CARD_DIR = ROOT / "doc-card"
EVALS_DIR = DOC_CARD_DIR / "evals" / "search"
INDEX = DOC_CARD_DIR / "index"
BATCH3_OUT = EVALS_DIR / "eval_queries_user_appdev_batch3.jsonl"
BLIND_OUT = EVALS_DIR / "eval_queries_user_appdev_blind.jsonl"


CAPABILITY_BY_PREFIX = {
    "ui.": "arkui_component",
    "layout.": "arkui_component",
    "navigation.": "ability",
    "web.": "webview",
    "network.": "network",
    "security.": "security",
    "connectivity.": "bluetooth",
    "interop.": "interop",
    "animation.": "arkui_component",
    "component.": "arkui_component",
    "device.": "device_info",
    "quickstart.": "general",
    "error.": "troubleshooting",
    "std.crypto.": "security",
    "std.net.": "network",
    "std.fs.": "resource_file",
    "data.": "storage",
    "state.": "arkui_state",
}

TASK_PATH_OVERRIDES = {
    "ui.interaction.click": [
        "harmonyos-6.0.2-15k/Guide/arkui-cj/cj-event-overview/cj-event-overview.md",
        "harmonyos-6.0.2-15k/Guide/arkui-cj/cj-common-events-touch-screen-event/触屏事件/.overview.md",
        "harmonyos-6.0.2-15k/API/arkui-cj/cj-universal-event-click/.overview.md",
    ],
    "interop.arkts.basic": [
        "harmonyos-6.0.2-15k/API/arkinterop/cj-apis-ark_interop/.overview.md",
        "harmonyos-6.0.2-15k/API/arkinterop/cj-apis-ark_interop/ohosark_interopArkTS互操作库/.overview.md",
        "harmonyos-6.0.2-15k/Guide/learn-cj/FFI/cangjie-arkts/arkts_import_cangjie/.overview.md",
        "harmonyos-6.0.2-15k/Guide/learn-cj/FFI/cangjie-arkts/cj-using_arkts_module/cj-using_arkts_module.md",
    ],
    "security.aes.basic": [
        "harmonyos-6.0.2-15k/Guide/security/CryptoArchitectureKit/cj-crypto-aes-sym-encrypt-decrypt-cbc/.overview.md",
        "harmonyos-6.0.2-15k/Guide/security/CryptoArchitectureKit/cj-crypto-aes-sym-encrypt-decrypt-ccm/.overview.md",
        "harmonyos-6.0.2-15k/Guide/security/CryptoArchitectureKit/cj-crypto-aes-sym-encrypt-decrypt-gcm/.overview.md",
        "harmonyos-6.0.2-15k/Guide/security/CryptoArchitectureKit/cj-crypto-sym-encrypt-decrypt-spec/对称密钥加解密算法规格/.overview.md",
    ],
    "ui.dialog.alert": [
        "harmonyos-6.0.2-15k/API/arkui-cj/cj-dialog-alertdialog/.overview.md",
        "harmonyos-6.0.2-15k/API/arkui-cj/cj-dialog-alertdialog/警告弹窗AlertDialog/.overview.md",
        "harmonyos-6.0.2-15k/API/arkui-cj/cj-apis-uicontext-promptaction/PromptAction/class_PromptAction.md",
        "harmonyos-6.0.2-15k/API/arkui-cj/cj-apis-uicontext-promptaction/PromptAction/class_ShowDialogOptions/.overview.md",
    ],
}


DOC_SEEDS = [
    {
        "query": "应用里要分享沙箱文件给其他应用怎么做",
        "intent": "查应用文件分享和 FileUri 组合",
        "category": "how_to",
        "capability": "resource_file",
        "acceptable_paths": [
            "harmonyos-6.0.2-15k/Guide/file-management/cj-share-app-file/.overview.md",
            "harmonyos-6.0.2-15k/API/CoreFileKit/cj-apis-file_fileuri",
        ],
    },
    {
        "query": "相册选择视频后怎么拿到资源信息",
        "intent": "查 PhotoAccessHelper 资源访问",
        "category": "how_to",
        "capability": "media",
        "acceptable_paths": [
            "harmonyos-6.0.2-15k/API/MediaLibraryKit/cj-apis-file-photo_access_helper",
            "harmonyos-6.0.2-15k/Guide/media/medialibrary/cj-photoAccessHelper-systemAlbum-guidelines/.overview.md",
        ],
    },
    {
        "query": "HTTP 请求证书校验失败应该看哪块",
        "intent": "查 HTTP 证书锁定和证书校验排查",
        "category": "error-driven",
        "capability": "network",
        "acceptable_paths": [
            "harmonyos-6.0.2-15k/Guide/network/cj-http-request/HTTP数据请求/证书锁定/.overview.md",
            "harmonyos-6.0.2-15k/API/NetworkKit/cj-apis-net-http",
        ],
    },
    {
        "query": "WebView 和 H5 交互要暴露仓颉方法怎么查",
        "intent": "查 WebView registerJavaScriptProxy",
        "category": "how_to",
        "capability": "webview",
        "acceptable_paths": [
            "harmonyos-6.0.2-15k/API/ArkWeb/cj-apis-webview/ohoswebwebviewWebview/class_WebviewController/func_registerJa_2more_454c827e.md",
            "harmonyos-6.0.2-15k/API/ArkWeb/cj-apis-webview/.overview.md",
        ],
    },
]


TASK_VARIANTS = (
    ("how_to", "how_to", "{title} 在 App 里怎么实现"),
    ("error-driven", "debug", "{title} 不生效应该查哪里"),
    ("api_lookup", "exact_api", "{title} 相关 API 从哪看"),
    ("exploration", "explore", "做{title}应该先看哪份文档"),
)

BLIND_VARIANTS = (
    ("how_to", "how_to", "我要做{title}，入口文档是哪块"),
    ("error-driven", "debug", "{title} 开发时出问题怎么定位"),
)

STRICT_BLIND_VARIANTS = (
    ("how_to", "how_to", "鸿蒙仓颉应用开发里，{title} 应该从哪里查起"),
    ("error-driven", "debug", "做{title}时结果不符合预期，优先看哪些文档"),
)


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def capability_for(task_id: str, primary_objects: list[str]) -> str:
    for prefix, capability in CAPABILITY_BY_PREFIX.items():
        if task_id.startswith(prefix):
            return capability
    if primary_objects:
        return str(primary_objects[0]).lower()
    return "general"


def clean_paths(paths: list[str]) -> list[str]:
    picked: list[str] = []
    for path in paths:
        if path not in picked:
            picked.append(path)
        if len(picked) >= 4:
            break
    return picked


def task_records(tasks: list[dict], variants: tuple[tuple[str, str, str], ...], source: str, limit: int) -> list[dict]:
    records: list[dict] = []
    for task in tasks:
        paths = clean_paths(TASK_PATH_OVERRIDES.get(task["task_id"], task.get("source_paths", [])))
        if not paths:
            continue
        title = task["title"]
        capability = capability_for(task["task_id"], task.get("primary_objects", []))
        for category, style, query_template in variants:
            records.append(
                {
                    "query": query_template.format(title=title),
                    "intent": f"查{title}的实现、API 或排查入口",
                    "category": category,
                    "capability": capability,
                    "query_style": style,
                    "difficulty": "compound" if category in {"error-driven", "exploration"} else "normal",
                    "acceptable_paths": paths,
                    "must_contain": [],
                    "source": source,
                }
            )
            if len(records) >= limit:
                return records
    return records


def doc_records(source: str) -> list[dict]:
    records: list[dict] = []
    for seed in DOC_SEEDS:
        row = {
            "query": seed["query"],
            "intent": seed["intent"],
            "category": seed["category"],
            "capability": seed["capability"],
            "query_style": "debug" if seed["category"] == "error-driven" else "how_to",
            "difficulty": "compound",
            "acceptable_paths": seed["acceptable_paths"],
            "must_contain": [],
            "source": source,
        }
        records.append(row)
    return records


def strict_doc_records(source: str) -> list[dict]:
    rows = doc_records(source)
    replacements = (
        "跨应用发送应用沙箱文件时，FileUri 和分享流程看哪里",
        "选择系统相册里的视频后，资源元数据入口在哪",
    )
    for row, query in zip(rows, replacements):
        row["query"] = query
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate app-dev batch3 and blind eval sets")
    parser.add_argument("--batch3-out", default=str(BATCH3_OUT), help="batch3 输出 JSONL")
    parser.add_argument("--blind-out", default=str(BLIND_OUT), help="blind 输出 JSONL")
    parser.add_argument("--strict-blind-out", default="", help="只生成新的严格 blind JSONL，不覆盖旧文件")
    parser.add_argument("--strict-source", default="", help="严格 blind 的 source 标记")
    args = parser.parse_args()

    tasks = load_jsonl(INDEX / "tasks.jsonl")
    if args.strict_blind_out:
        source = args.strict_source or f"strict-blind-{datetime.now().strftime('%Y%m%d')}"
        blind = task_records(tasks, STRICT_BLIND_VARIANTS, source, 78) + strict_doc_records(source)[:2]
        output = Path(args.strict_blind_out)
        write_jsonl(output, blind)
        print(f"wrote {output.name}: {len(blind)}")
        return

    batch3 = task_records(tasks, TASK_VARIANTS, "curated-index-batch3", 156) + doc_records("curated-index-batch3")
    blind = task_records(tasks, BLIND_VARIANTS, "curated-index-blind", 78) + doc_records("curated-index-blind")[:2]
    batch3_out = Path(args.batch3_out)
    blind_out = Path(args.blind_out)
    write_jsonl(batch3_out, batch3)
    write_jsonl(blind_out, blind)
    print(f"wrote {batch3_out.name}: {len(batch3)}")
    print(f"wrote {blind_out.name}: {len(blind)}")


if __name__ == "__main__":
    main()
