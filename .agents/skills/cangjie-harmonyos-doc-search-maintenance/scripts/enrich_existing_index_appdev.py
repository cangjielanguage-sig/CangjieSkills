#!/usr/bin/env python3
"""在现有 V3 索引上增量补充 AppDev 检索语义。"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = MAINTENANCE_DIR.parent
SKILL_DIR = SKILLS_DIR / "cangjie-harmonyos-doc-search"
DOC_CARD_DIR = SKILL_DIR / "doc-card"
BUILDER_DIR = MAINTENANCE_DIR / "builder"
sys.path.insert(0, str(BUILDER_DIR))

from build_index_v3 import normalize_aliases, write_jsonl, write_search_db


DEFAULT_INPUT_DIR = DOC_CARD_DIR / "index"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def appdev_values(row: dict[str, Any]) -> dict[str, list[str]]:
    haystack = " ".join(
        str(value)
        for value in (
            row.get("title"),
            row.get("name"),
            row.get("intent"),
            row.get("summary"),
            " ".join(row.get("aliases", [])),
            " ".join(row.get("semantic_aliases", [])),
            " ".join(row.get("user_queries", [])),
            " ".join(row.get("source_paths", [])),
        )
        if value
    ).lower()
    rules: list[tuple[tuple[str, ...], dict[str, list[str]]]] = [
        (("requestpermissionsfromuser",), {"semantic_aliases": ["运行时申请权限", "动态权限申请", "向用户申请授权"], "user_queries": ["运行时怎么向用户申请权限", "权限申请接口怎么用"], "primary_objects": ["access_token", "ability"]}),
        (("declare-permissions", "module.json5"), {"semantic_aliases": ["声明权限", "module.json5 权限配置", "ohos.permission.INTERNET"], "user_queries": ["网络请求需要配置什么权限", "应用权限要在 module.json5 里怎么声明"], "primary_objects": ["access_token"]}),
        (("uiabilitycontext",), {"semantic_aliases": ["UIAbilityContext", "Ability 上下文", "AbilityContext"], "user_queries": ["UIAbilityContext 能做哪些事情", "UIAbilityContext 怎么获取"], "primary_objects": ["ability"]}),
        (("class_want", "app-ability-want"), {"semantic_aliases": ["Want 对象", "Want 参数", "页面跳转传参"], "user_queries": ["Want 对象怎么传参数", "startAbility 怎么传 Want"], "primary_objects": ["ability"]}),
        (("abilitylifecyclestate",), {"semantic_aliases": ["AbilityLifecycleState", "Ability 生命周期状态", "AbilityDelegator"], "user_queries": ["Ability 生命周期状态怎么测试", "AbilityDelegator 怎么测试生命周期"], "primary_objects": ["ability"]}),
        (("localstorage",), {"semantic_aliases": ["LocalStorage 页面级状态", "UIAbility 共享 LocalStorage"], "user_queries": ["LocalStorage 怎么在 UIAbility 和页面之间共享", "LocalStorage 页面级状态怎么用"], "primary_objects": ["localstorage", "arkui_state", "ability"]}),
        (("preferences",), {"semantic_aliases": ["用户首选项", "保存用户设置", "Preferences.getPreferences", "Preferences.has", "Preferences.put"], "user_queries": ["Preferences 怎么保存用户设置", "Preferences 读取 key 不存在怎么判断", "getPreferences 需要传什么 context 和 options"], "primary_objects": ["preferences"]}),
        (("relational_store", "rdbstore"), {"semantic_aliases": ["RdbStore", "getRdbStore", "executeSql", "querySql", "关系型数据库建表"], "user_queries": ["RelationalStore 怎么创建数据库", "RdbStore 怎么执行建表 SQL", "RdbStore 怎么查询数据"], "primary_objects": ["relational_store"]}),
        (("hascookie",), {"semantic_aliases": ["hasCookie", "WebCookieManager.hasCookie", "检查 Cookie 是否存在"], "user_queries": ["WebView 怎么判断当前有没有 Cookie", "WebCookieManager hasCookie 怎么用"], "primary_objects": ["web"]}),
        (("runjavascript",), {"semantic_aliases": ["runJavaScript", "执行 JavaScript", "WebView JS 返回值"], "user_queries": ["WebView 怎么执行 JavaScript 并拿返回值", "runJavaScript 怎么用"], "primary_objects": ["web"]}),
        (("registerjavascriptproxy",), {"semantic_aliases": ["registerJavaScriptProxy", "JS bridge", "H5 调仓颉"], "user_queries": ["WebView 怎么把仓颉方法暴露给 H5 调用", "registerJavaScriptProxy 怎么注册 JS bridge"], "primary_objects": ["web"]}),
        (("storewebarchive",), {"semantic_aliases": ["storeWebArchive", "保存网页", "网页离线包"], "user_queries": ["WebView 怎么保存网页离线包", "storeWebArchive 怎么用"], "primary_objects": ["web"]}),
        (("darkmode",), {"semantic_aliases": ["darkMode", "WebDarkMode", "Web 深色模式"], "user_queries": ["WebView 深色模式怎么设置", "Web darkMode 属性怎么用"], "primary_objects": ["web"]}),
        (("cj-web-debugging-with-devtools", "setwebdebuggingaccess"), {"semantic_aliases": ["DevTools", "Web 调试", "setWebDebuggingAccess"], "user_queries": ["WebView DevTools 调试怎么打开", "Web 调试开关怎么开启"], "primary_objects": ["web"]}),
        (("cj-web-pdf-preview",), {"semantic_aliases": ["PDF 预览", "WebView PDF"], "user_queries": ["WebView PDF 预览怎么做", "Web 组件怎么预览 PDF"], "primary_objects": ["web"]}),
        (("safe-area",), {"semantic_aliases": ["安全区域", "safe area", "safe-area-insets"], "user_queries": ["WebView 安全区域避让怎么适配", "WebView safe area insets 怎么用"], "primary_objects": ["web"]}),
        (("secure-shield",), {"semantic_aliases": ["secure shield mode", "安全盾牌模式"], "user_queries": ["WebView secure shield mode 是什么", "Web 安全盾牌模式怎么用"], "primary_objects": ["web"]}),
        (("requestinstream",), {"semantic_aliases": ["requestInStream", "HTTP 流式响应", "流式响应"], "user_queries": ["HTTP 请求怎么处理流式响应", "requestInStream 接口怎么用"], "primary_objects": ["http"]}),
        (("证书锁定", "certificate"), {"semantic_aliases": ["证书锁定", "证书校验", "CertificatePinning"], "user_queries": ["HTTP 证书锁定怎么配置", "HTTP 请求证书校验失败怎么排查"], "primary_objects": ["http"]}),
        (("net-connection", "net_connection", "网络连接"), {"semantic_aliases": ["网络连接管理", "网络连接状态", "NetConnection"], "user_queries": ["网络连接状态怎么监听", "怎么监听网络断开和恢复"], "primary_objects": ["network_connection"]}),
        (("websocket",), {"semantic_aliases": ["WebSocket", "upgradeFromClient", "WebSocketFrame", "发送消息"], "user_queries": ["WebSocket 客户端怎么升级连接", "WebSocket 怎么发送消息"], "primary_objects": ["websocket"]}),
        (("rawfile",), {"semantic_aliases": ["rawfile", "resources/rawfile", "资源文件", "ResourceManager", "getRawFd"], "user_queries": ["rawfile 路径无效怎么排查", "如何解码 resources/rawfile 里的图片", "Image 加载 rawfile 图片怎么写"], "primary_objects": ["resource_file"]}),
        (("file_fs", "应用沙箱", "app-file"), {"semantic_aliases": ["应用沙箱文件", "文件读写", "file_fs", "应用文件访问"], "user_queries": ["应用沙箱文件怎么读写", "应用文件访问权限错误怎么排查"], "primary_objects": ["resource_file", "std_fs"]}),
        (("photo_access_helper", "photoaccesshelper", "fetchresult"), {"semantic_aliases": ["PhotoAccessHelper", "FetchResult", "相册图片列表"], "user_queries": ["怎么获取相册里的图片列表", "PhotoAccessHelper 怎么查询图片"], "primary_objects": ["photo_access", "media"]}),
        (("cameramanager",), {"semantic_aliases": ["CameraManager", "相机设备列表", "getSupportedCameras"], "user_queries": ["CameraManager 怎么获取相机设备列表", "相机预览黑屏怎么排查"], "primary_objects": ["camera"]}),
        (("gyroscope", "sensor"), {"semantic_aliases": ["Gyroscope", "传感器订阅", "sensor.off", "陀螺仪"], "user_queries": ["传感器怎么订阅陀螺仪数据", "传感器监听怎么取消"], "primary_objects": ["sensor"]}),
        (("ipc", "rpc", "parcelable"), {"semantic_aliases": ["RPC", "IPCKit", "Parcelable", "远程调用"], "user_queries": ["RPC 通信怎么创建远程调用", "RPC 调用错误码怎么排查"], "primary_objects": ["ipc"]}),
        (("telephony", "callstate"), {"semantic_aliases": ["Telephony", "CallState", "通话状态"], "user_queries": ["Telephony 调用失败错误码怎么排查", "CallState 怎么监听"], "primary_objects": ["telephony"]}),
        (("security_huks", "universalkeystorekit", "huks"), {"semantic_aliases": ["HUKS", "UniversalKeystoreKit", "通用密钥库", "生成密钥", "generateKeyItem", "分段加解密"], "user_queries": ["HUKS 怎么生成密钥", "HUKS 加解密怎么分段处理", "HUKS 密钥不存在怎么排查"], "primary_objects": ["huks", "security"]}),
        (("promptaction", "showtoast", "showactionmenu"), {"semantic_aliases": ["PromptAction", "showToast", "showActionMenu", "Toast 提示", "ActionMenu 菜单"], "user_queries": ["Toast 提示怎么显示", "ActionMenu 菜单怎么弹出"], "primary_objects": ["prompt_action", "arkui_component"]}),
        (("battery_info",), {"semantic_aliases": ["Battery", "battery_info", "电池电量"], "user_queries": ["电池电量等级怎么判断", "battery_info 怎么获取电量"], "primary_objects": ["device_info"]}),
        (("system_date_time",), {"semantic_aliases": ["system_date_time", "系统时间", "时间设置"], "user_queries": ["系统时间怎么获取和设置", "system_date_time API 怎么用"], "primary_objects": ["device_info"]}),
        (("settings",), {"semantic_aliases": ["Settings", "系统设置", "设置读写"], "user_queries": ["Settings 系统设置读写失败怎么排查", "Settings 怎么读取系统设置"], "primary_objects": ["device_info"]}),
        (("displaymanager", "getdefaultdisplay"), {"semantic_aliases": ["Display", "屏幕宽高", "屏幕方向"], "user_queries": ["Display 怎么获取屏幕宽高和方向", "怎么获取屏幕方向"], "primary_objects": ["window_display"]}),
        (("hilog",), {"semantic_aliases": ["HiLog", "日志 domain", "日志 tag"], "user_queries": ["HiLog tag 或 domain 参数错误怎么排查", "HiLog 怎么打印日志"], "primary_objects": ["diagnostics"]}),
    ]
    merged: dict[str, list[str]] = {"semantic_aliases": [], "user_queries": [], "primary_objects": []}
    for hints, values in rules:
        if any(hint in haystack for hint in hints):
            for key, items in values.items():
                merged[key].extend(items)
    return {key: normalize_aliases(values) for key, values in merged.items() if values}


def enrich_rows(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], int]:
    changed = 0
    enriched: list[dict[str, Any]] = []
    for row in rows:
        values = appdev_values(row)
        updated = dict(row)
        for key in ("semantic_aliases", "user_queries", "primary_objects"):
            merged = normalize_aliases([*updated.get(key, []), *values.get(key, [])])
            if merged != updated.get(key, []):
                updated[key] = merged
        if updated != row:
            changed += 1
        enriched.append(updated)
    return enriched, changed


def main() -> None:
    parser = argparse.ArgumentParser(description="在现有索引上补充 AppDev 语义字段")
    parser.add_argument("--input-dir", default=str(DEFAULT_INPUT_DIR))
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    tasks, changed_tasks = enrich_rows(load_jsonl(input_dir / "tasks.jsonl"))
    apis, changed_apis = enrich_rows(load_jsonl(input_dir / "apis.jsonl"))
    examples, changed_examples = enrich_rows(load_jsonl(input_dir / "examples.jsonl"))
    docs, changed_docs = enrich_rows(load_jsonl(input_dir / "docs.jsonl"))

    write_jsonl(output_dir / "tasks.jsonl", tasks)
    write_jsonl(output_dir / "apis.jsonl", apis)
    write_jsonl(output_dir / "examples.jsonl", examples)
    write_jsonl(output_dir / "docs.jsonl", docs)
    for name in ("aliases.json", "manifest.json"):
        shutil.copy2(input_dir / name, output_dir / name)
    write_search_db(output_dir / "search.db", tasks, apis, examples, docs)

    print(json.dumps({
        "output_dir": str(output_dir),
        "changed": {
            "tasks": changed_tasks,
            "apis": changed_apis,
            "examples": changed_examples,
            "docs": changed_docs,
        },
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
