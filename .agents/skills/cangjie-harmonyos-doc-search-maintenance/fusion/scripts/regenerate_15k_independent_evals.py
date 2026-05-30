#!/usr/bin/env python3
"""为 harmonyos-6.0.2-15k 语料重建独立评测集（real_session / composition / paraphrase）。

路径均为相对 doc-search 技能根目录的目录前缀，需能在 docs_manifest 或索引中匹配到 .md 子路径。
"""
from __future__ import annotations

import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = MAINTENANCE_DIR.parent
ROOT = SKILLS_DIR / "cangjie-harmonyos-doc-search"
EVALS = ROOT / "doc-card" / "evals"

# 目录前缀（不含尾部 .md），与 15k 扁平化目录结构一致
P = {
    "list": "harmonyos-6.0.2-15k/cj-scroll-swipe-list",
    "refresh": "harmonyos-6.0.2-15k/cj-scroll-swipe-refresh",
    "lazyforeach": "harmonyos-6.0.2-15k/cj-state-rendering-lazyforeach",
    "grid": "harmonyos-6.0.2-15k/cj-scroll-swipe-grid",
    "http": "harmonyos-6.0.2-15k/cj-apis-net-http",
    "http_req": "harmonyos-6.0.2-15k/cj-http-request",
    "state": "harmonyos-6.0.2-15k/cj-application-state-management-overview",
    "state_comp": "harmonyos-6.0.2-15k/cj-state-rendering-componentstatemanagement",
    "webview": "harmonyos-6.0.2-15k/cj-apis-webview",
    "prompt": "harmonyos-6.0.2-15k/cj-apis-promptaction",
    "toast": "harmonyos-6.0.2-15k/cj-create-toast",
    "router": "harmonyos-6.0.2-15k/cj-apis-router",
    "nav": "harmonyos-6.0.2-15k/cj-navigation-navigation",
    "ability": "harmonyos-6.0.2-15k/cj-apis-ability",
    "ability_overview": "harmonyos-6.0.2-15k/cj-abilitykit-overview",
    "create_list_guide": "harmonyos-6.0.2-15k/cj-layout-development-create-list",
    "first_app": "harmonyos-6.0.2-15k/cj-quick-start-first-cangjie-app",
    "uiability": "harmonyos-6.0.2-15k/cj-apis-ability/ohosabilityAbility/class_UIAbility",
    "camera": "harmonyos-6.0.2-15k/cj-apis-multimedia-camera",
    "upload": "harmonyos-6.0.2-15k/cj-app-file-upload-download",
    "request_agent": "harmonyos-6.0.2-15k/cj-apis-request-agent",
    "bluetooth": "harmonyos-6.0.2-15k/cj-apis-bluetooth-ble",
    "location": "harmonyos-6.0.2-15k/cj-apis-geo_location_manager",
    "relational": "harmonyos-6.0.2-15k/cj-apis-relational_store",
    "picker": "harmonyos-6.0.2-15k/cj-apis-file_picker",
    "timer": "harmonyos-6.0.2-15k/cj-apis-timer",
    "crypto": "harmonyos-6.0.2-15k/cj-apis-crypto",
    "background": "harmonyos-6.0.2-15k/cj-background-task-overview",
    "media": "harmonyos-6.0.2-15k/cj-apis-multimedia_media",
}


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def real_session() -> list[dict]:
    rows = [
        {
            "query": "长列表滑动卡顿怎么优化",
            "intent": "性能：List 滑动",
            "category": "semantic_fuzzy",
            "capability": "performance",
            "query_style": "how_to_optimize",
            "difficulty": "compound",
            "acceptable_paths": [P["list"], P["lazyforeach"], P["create_list_guide"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "为什么 @State 改了 UI 不刷新",
            "intent": "状态管理排查",
            "category": "semantic_fuzzy",
            "capability": "state_management",
            "query_style": "debug_why",
            "difficulty": "compound",
            "acceptable_paths": [P["state"], P["state_comp"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "鸿蒙里类似 Android RecyclerView 的做法",
            "intent": "跨生态类比列表",
            "category": "cross_ecosystem",
            "capability": "arkui_component",
            "query_style": "analogy",
            "difficulty": "normal",
            "acceptable_paths": [P["list"], P["lazyforeach"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "WebView 调原生能力显示 toast",
            "intent": "Web 互操作",
            "category": "composition",
            "capability": "web_interop",
            "query_style": "combination",
            "difficulty": "compound",
            "acceptable_paths": [P["webview"], P["prompt"], P["toast"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "页面切换有白屏",
            "intent": "路由白屏",
            "category": "semantic_fuzzy",
            "capability": "navigation",
            "query_style": "debug_symptom",
            "difficulty": "compound",
            "acceptable_paths": [P["router"], P["nav"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "启动应用的时候怎么预加载数据",
            "intent": "启动与 Ability",
            "category": "how_to",
            "capability": "ability_lifecycle",
            "query_style": "how_to",
            "difficulty": "compound",
            "acceptable_paths": [P["ability_overview"], P["uiability"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "RN 里的 FlatList 对应鸿蒙什么组件",
            "intent": "跨生态类比懒加载列表",
            "category": "cross_ecosystem",
            "capability": "arkui_component",
            "query_style": "analogy",
            "difficulty": "normal",
            "acceptable_paths": [P["list"], P["lazyforeach"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "仓颉怎么发 HTTP 请求",
            "intent": "网络请求",
            "category": "how_to",
            "capability": "network",
            "query_style": "how_to",
            "difficulty": "normal",
            "acceptable_paths": [P["http"], P["http_req"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "第一个鸿蒙仓颉应用从哪里开始",
            "intent": "入门",
            "category": "how_to",
            "capability": "onboarding",
            "query_style": "how_to",
            "difficulty": "normal",
            "acceptable_paths": [P["first_app"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "拍照并上传服务器带进度",
            "intent": "媒体上传",
            "category": "composition",
            "capability": "media_upload",
            "query_style": "combination",
            "difficulty": "hard",
            "acceptable_paths": [P["camera"], P["upload"], P["request_agent"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "蓝牙 BLE 扫描连接基本流程",
            "intent": "蓝牙",
            "category": "how_to",
            "capability": "connectivity",
            "query_style": "how_to",
            "difficulty": "compound",
            "acceptable_paths": [P["bluetooth"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "定位权限与地理位置获取",
            "intent": "定位",
            "category": "how_to",
            "capability": "location",
            "query_style": "how_to",
            "difficulty": "compound",
            "acceptable_paths": [P["location"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "本地关系型数据库入门",
            "intent": "存储",
            "category": "how_to",
            "capability": "storage",
            "query_style": "how_to",
            "difficulty": "normal",
            "acceptable_paths": [P["relational"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "文件选择器选图片",
            "intent": "Picker",
            "category": "how_to",
            "capability": "media",
            "query_style": "how_to",
            "difficulty": "normal",
            "acceptable_paths": [P["picker"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
        {
            "query": "定时任务与延迟回调",
            "intent": "Timer",
            "category": "how_to",
            "capability": "async",
            "query_style": "how_to",
            "difficulty": "normal",
            "acceptable_paths": [P["timer"]],
            "must_contain": [],
            "source": "real-session-15k-20260511",
        },
    ]
    return rows


def composition() -> list[dict]:
    return [
        {
            "query": "做一个带下拉刷新的网络列表页",
            "intent": "List + Refresh + HTTP + State",
            "category": "composition",
            "capability": "app_page",
            "difficulty": "compound",
            "expected_concept_clusters": ["list", "refresh", "http", "state_management"],
            "acceptable_paths": [P["list"], P["refresh"], P["http"], P["state"]],
            "must_contain": [],
            "source": "composition-15k-20260511",
        },
        {
            "query": "做一个带虚拟滚动的大数据量表格",
            "intent": "LazyForEach + List + Grid",
            "category": "composition",
            "capability": "app_page",
            "difficulty": "hard",
            "expected_concept_clusters": ["lazyforeach", "list", "grid"],
            "acceptable_paths": [P["lazyforeach"], P["list"], P["grid"]],
            "must_contain": [],
            "source": "composition-15k-20260511",
        },
        {
            "query": "WebView 里 H5 调起原生 toast",
            "intent": "WebView + Toast",
            "category": "composition",
            "capability": "web_interop",
            "difficulty": "compound",
            "expected_concept_clusters": ["webview", "jsbridge", "toast"],
            "acceptable_paths": [P["webview"], P["prompt"], P["toast"]],
            "must_contain": [],
            "source": "composition-15k-20260511",
        },
        {
            "query": "实现列表加减数量并同步后端",
            "intent": "List + HTTP + State",
            "category": "composition",
            "capability": "app_page",
            "difficulty": "compound",
            "expected_concept_clusters": ["list", "http", "state_management"],
            "acceptable_paths": [P["list"], P["http"], P["state"]],
            "must_contain": [],
            "source": "composition-15k-20260511",
        },
        {
            "query": "后台播放音频与长任务",
            "intent": "Media + Background",
            "category": "composition",
            "capability": "media_background",
            "difficulty": "hard",
            "expected_concept_clusters": ["media", "timer"],
            "acceptable_paths": [P["media"], P["background"]],
            "must_contain": [],
            "source": "composition-15k-20260511",
        },
        {
            "query": "定位与蓝牙同时使用的注意点",
            "intent": "Location + Bluetooth",
            "category": "composition",
            "capability": "iot_app",
            "difficulty": "hard",
            "expected_concept_clusters": ["location", "bluetooth"],
            "acceptable_paths": [P["location"], P["bluetooth"]],
            "must_contain": [],
            "source": "composition-15k-20260511",
        },
        {
            "query": "加密存储与关系型数据库",
            "intent": "Crypto + RDB",
            "category": "composition",
            "capability": "security_storage",
            "difficulty": "hard",
            "expected_concept_clusters": ["cipher", "rdb_store"],
            "acceptable_paths": [P["crypto"], P["relational"]],
            "must_contain": [],
            "source": "composition-15k-20260511",
        },
        {
            "query": "选择相册图片并上传",
            "intent": "Picker + Upload",
            "category": "composition",
            "capability": "media_upload",
            "difficulty": "compound",
            "expected_concept_clusters": ["photo_picker", "request_upload"],
            "acceptable_paths": [P["picker"], P["upload"]],
            "must_contain": [],
            "source": "composition-15k-20260511",
        },
        {
            "query": "路由跳转与页面栈管理",
            "intent": "Router + Navigation",
            "category": "composition",
            "capability": "navigation",
            "difficulty": "compound",
            "acceptable_paths": [P["router"], P["nav"]],
            "must_contain": [],
            "source": "composition-15k-20260511",
        },
        {
            "query": "Ability 生命周期与 UIAbility 入口",
            "intent": "Ability overview",
            "category": "composition",
            "capability": "ability_lifecycle",
            "difficulty": "compound",
            "acceptable_paths": [P["ability_overview"], P["uiability"]],
            "must_contain": [],
            "source": "composition-15k-20260511",
        },
    ]


def paraphrase() -> list[dict]:
    """同 intent 多表述。"""
    intents = [
        (
            "list_refresh",
            [
                ("list_refresh_01", "List 怎么下拉刷新"),
                ("list_refresh_02", "滑动列表拉下来要能刷新"),
                ("list_refresh_03", "鸿蒙版 SwipeRefreshLayout 怎么写"),
                ("list_refresh_04", "列表页顶部下拉重新加载数据"),
                ("list_refresh_05", "带 Refresh 的 List 页面从哪查"),
            ],
            [P["list"], P["refresh"]],
        ),
        (
            "http_request",
            [
                ("http_request_01", "仓颉怎么发 HTTP 请求"),
                ("http_request_02", "网络 GET POST 用哪个包"),
                ("http_request_03", "调用后端 REST 接口示例"),
            ],
            [P["http"], P["http_req"]],
        ),
        (
            "webview_toast",
            [
                ("webview_toast_01", "网页里点击按钮让原生弹 Toast"),
                ("webview_toast_02", "WebView 和 ArkUI 弹窗互通"),
                ("webview_toast_03", "H5 调鸿蒙侧提示"),
            ],
            [P["webview"], P["toast"]],
        ),
        (
            "state_reactive",
            [
                ("state_reactive_01", "状态变了界面不更新"),
                ("state_reactive_02", "@State 不生效排查"),
                ("state_reactive_03", "组件状态管理文档入口"),
            ],
            [P["state"], P["state_comp"]],
        ),
        (
            "lazy_list",
            [
                ("lazy_list_01", "大列表 LazyForEach 从哪看"),
                ("lazy_list_02", "RecyclerView 那种长列表"),
                ("lazy_list_03", "虚拟列表性能相关"),
            ],
            [P["lazyforeach"], P["list"]],
        ),
        (
            "first_app",
            [
                ("first_app_01", "第一个鸿蒙仓颉应用"),
                ("first_app_02", "仓颉 Hello World 工程"),
                ("first_app_03", "快速上手第一个应用"),
            ],
            [P["first_app"]],
        ),
    ]
    rows: list[dict] = []
    for intent_id, variants, paths in intents:
        for variant_id, query in variants:
            rows.append(
                {
                    "intent_id": intent_id,
                    "variant_id": variant_id,
                    "query": query,
                    "category": "paraphrase",
                    "capability": "robustness",
                    "acceptable_paths": paths,
                    "source": "paraphrase-15k-20260511",
                }
            )
    return rows


def minimal_full_eval() -> list[dict]:
    """V3 自举回归用小集合：每条对应 manifest 中存在的 .md 路径（取常见 overview）。"""
    # 从 manifest 抽样：用目录下 .overview.md 若存在
    base = ROOT / "harmonyos-6.0.2-15k"
    samples: list[tuple[str, str]] = []
    for topic_dir in [
        "cj-scroll-swipe-list/List",
        "cj-scroll-swipe-refresh/Refresh",
        "cj-apis-net-http",
        "cj-apis-webview",
        "cj-application-state-management-overview",
        "cj-apis-ability/ohosabilityAbility/class_UIAbility",
        "cj-layout-development-create-list/创建列表List",
        "cj-quick-start-first-cangjie-app",
        "cj-state-rendering-lazyforeach/LazyForEach",
        "cj-http-request",
        "cj-apis-router",
        "cj-navigation-navigation",
        "cj-apis-crypto",
        "cj-apis-relational_store",
        "cj-apis-multimedia-camera",
    ]:
        p = base / topic_dir
        if not p.exists():
            continue
        overview = p / ".overview.md"
        abstract = p / ".abstract.md"
        if overview.is_file():
            rel = overview.relative_to(ROOT).as_posix()
        elif abstract.is_file():
            rel = abstract.relative_to(ROOT).as_posix()
        else:
            # 任意子 md
            mds = sorted(p.rglob("*.md"))
            if not mds:
                continue
            rel = mds[0].relative_to(ROOT).as_posix()
        card_id = rel.replace("/", "-").replace(".md", "")[:120]
        samples.append((rel, card_id))

    rows: list[dict] = []
    for rel, card_id in samples:
        rows.append(
            {
                "query": f"文档路径 {rel} 的核心说明",
                "expected_paths": [rel],
                "category": "exact",
                "card_type": "doc",
                "card_id": f"doc.{card_id}",
            }
        )
    return rows


def main() -> None:
    write_jsonl(EVALS / "eval_queries_real_session.jsonl", real_session())
    write_jsonl(EVALS / "eval_queries_composition.jsonl", composition())
    write_jsonl(EVALS / "eval_queries_paraphrase.jsonl", paraphrase())
    full_rows = minimal_full_eval()
    write_jsonl(EVALS / "eval_queries_full.jsonl", full_rows)
    print(f"wrote real_session={len(real_session())} composition={len(composition())} paraphrase={len(paraphrase())} full={len(full_rows)}")


if __name__ == "__main__":
    main()
