#!/usr/bin/env python3
"""V3 本地结构化检索入口。"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from query_understanding import understand, understand_host_agent


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INDEX_DIR = SCRIPT_DIR / "index"
MODE_TYPES = {
    "task": ("task",),
    "api": ("api",),
    "example": ("example",),
    "doc": ("doc",),
    "auto": ("task", "api", "example", "doc"),
}
TYPE_ID_KEY = {"task": "task_id", "api": "api_id", "example": "example_id", "doc": "doc_id"}
GENERIC_ALIAS_KEYS = {
    ".abstract",
    ".overview",
    "API_列表",
    "class",
    "get",
    "on",
    "put",
    "store",
    "基础类型定义",
    "示例代码",
    "组件事件",
    "组件属性",
    "通用属性通用事件",
    "类",
    "函数",
    "接口",
    "枚举",
}
CONTEXTUAL_IDENTIFIER_TOKENS = {
    "value",
    "min",
    "max",
    "step",
    "duration",
    "delay",
    "curve",
    "headers",
    "src",
    "type",
    "key",
    "id",
}
HIGH_VALUE_IDENTIFIERS = {
    "darkmode",
    "executesql",
    "getpreferences",
    "getrdbstore",
    "hascookie",
    "hilog",
    "jspromisecapability",
    "17100001",
    "querysql",
    "rawfile",
    "registerjavascriptproxy",
    "requestinstream",
    "requestpermissionsfromuser",
    "runjavascript",
    "setwebdebuggingaccess",
    "showactionmenu",
    "showtoast",
    "storewebarchive",
    "upgradefromclient",
    "generatekeyitem",
    "abilitylifecyclestate",
    "actionmenuoptions",
    "fetchresult",
    "fileuri",
    "imagepacker",
    "popup",
    "tabs",
    "singlekvstore",
    "kvmanager",
    "commoneventpublishdata",
    "commoneventsubscribeinfo",
    "grantstatus",
    "state",
}
DOMAIN_QUERY_EXPANSIONS = {
    "access_token": "AccessToken declare permissions requestPermissionsFromUser module.json5 权限声明 向用户申请授权",
    "ability": "UIAbility UIAbilityContext Want startAbility startAbilityForResult AbilityLifecycleState",
    "arkui_state": "State LocalStorage LazyForEach ForEach AppStorage 状态管理",
    "camera": "CameraKit CameraManager PreviewOutput PhotoOutput VideoOutput getSupportedCameras 相机管理 相机设备列表",
    "common_event": "CommonEvent CommonEventManager CommonEventPublishData CommonEventSubscribeInfo 公共事件 发布 订阅",
    "device_info": "device_info battery_info system_date_time settings 设备信息",
    "distributed_storage": "ArkData distributed_kv_store SingleKVStore KVManager KVOptions DistributedKVStore 分布式键值数据库 分布式KV 跨设备同步",
    "file_transfer": "request 上传下载 app-file-upload-download 下载网络资源文件 应用文件上传下载 upload download",
    "ipc": "IPCKit RPC Parcelable rpc通信",
    "location": "LocationKit GeoLocationManager getCurrentLocation geo_location_manager 位置服务",
    "media": "MediaKit ImageKit PhotoAccessHelper ImageSource ImagePacker PixelMap AVFileDescriptor 媒体错误码 无可用资源",
    "huks": "UniversalKeystoreKit HUKS generateKeyItem initSession updateSession finishSession 密钥库 生成密钥 加解密",
    "http": "NetworkKit HttpRequest request requestInStream CertificatePinning 证书锁定 HTTP数据请求",
    "hilog": "PerformanceAnalysisKit HiLog Hilog 日志 tag domain",
    "hiappevent": "PerformanceAnalysisKit HiAppEvent hiappevent HiTraceMeter 事件上报 观察者 冻屏事件 崩溃事件 Watcher TriggerCondition AppEventFilter",
    "arkts_interop": "arkinterop ArkTSInterop JSValue JSPromise JSPromiseCapability requireArkModule arkts_import_cangjie 仓颉 ArkTS 互操作 import Promise",
    "network_connection": "NetworkKit net_connection NetConnection connection 网络连接管理 网络连接状态",
    "preferences": "ArkData Preferences getPreferences PreferencesOptions has get put flush 用户首选项 用户设置",
    "photo_access": "MediaLibraryKit PhotoAccessHelper FetchResult Album 相册 图片列表",
    "prompt_action": "PromptAction showToast showActionMenu Toast ActionMenu ActionMenuOptions 气泡提示 菜单",
    "request_agent": "BasicServicesKit request-agent 上传下载任务 下载任务 请求代理 FormItem FileSpec Config Task TaskInfo EventCallbackType State Faults Network saveas headers getTask Progress pause stop on",
    "resource_file": "CoreFileKit ResourceManager rawfile getRawFd file_fs file_fileuri FileUri cj-errorcode-filemanagement cj-app-file-access 沙箱目录 应用文件访问 文件管理错误码",
    "relational_store": "ArkData RelationalStore RdbStore getRdbStore StoreConfig executeSql querySql ResultSet 关系型数据库 建表 查询",
    "storage": "ArkData DataSharePredicates data_share_predicates equalTo orderByAsc 列表筛选 排序 谓词",
    "sensor": "SensorServiceKit sensor on once off SensorId Gyroscope Accelerometer ohossensor 传感器 回调 订阅",
    "telephony": "TelephonyKit CallState telephony-call 拨打电话",
    "web": "ArkWeb WebviewController WebCookieManager hasCookie loadUrl runJavaScript registerJavaScriptProxy storeWebArchive darkMode DevTools",
    "websocket": "stdx.net.http WebSocket upgradeFromClient WebSocketFrame write read WebSocket 客户端",
    "webview": "ArkWeb WebviewController WebCookieManager runJavaScript registerJavaScriptProxy",
    "window_display": "WindowStage Window Display displaymanager windowmanager 窗口 屏幕",
}
ACTION_QUERY_EXPANSIONS = (
    (("request-agent",), "request-agent BasicServicesKit 上传下载任务 Config Task TaskInfo State EventCallbackType Faults Network"),
    (("request-agent", "headers"), "request-agent Config headers var_headers"),
    (("saveas",), "request-agent Config saveas 保存路径"),
    (("formitem",), "request-agent FormItem 上传表单字段"),
    (("filespec",), "request-agent FileSpec 上传文件配置"),
    (("taskinfo", "priority"), "request-agent TaskInfo priority"),
    (("faults",), "request-agent Faults 错误枚举"),
    (("下载任务", "进度"), "request-agent Task on EventCallbackType Progress 任务进度"),
    (("下载任务", "暂停"), "request-agent Task pause State 任务控制"),
    (("下载任务", "停止"), "request-agent Task stop State 任务控制"),
    (("任务状态", "枚举"), "request-agent State enum_State 任务状态枚举"),
    (("上传下载", "回调事件"), "request-agent EventCallbackType Task on 上传下载事件类型"),
    (("任务信息", "优先级"), "request-agent TaskInfo priority 任务信息优先级"),
    (("请求代理", "网络类型"), "request-agent Network Config 网络限制"),
    (("datasharepredicates",), "ArkData DataSharePredicates equalTo orderByAsc 数据共享谓词"),
    (("筛选", "排序"), "DataSharePredicates equalTo orderByAsc 列表筛选 排序"),
    (("hiappevent",), "HiAppEvent 事件上报 Watcher AppEventFilter EventType EventValueType"),
    (("hiappevent", "用户标识"), "HiAppEvent setUserId 用户标识"),
    (("清空", "事件数据"), "HiAppEvent clearData 清空本地事件数据"),
    (("观察者名称非法",), "HiAppEvent 11102001 非法的观察者名称 错误码"),
    (("崩溃", "冻屏"), "HiAppEvent watcher crash events freeze events"),
    (("hitracemeter",), "HiTraceMeter 性能打点"),
    (("冻屏事件",), "HiAppEvent watcher freeze events 订阅应用冻屏事件"),
    (("崩溃事件",), "HiAppEvent watcher crash events 订阅崩溃事件"),
    (("观察者",), "HiAppEvent Watcher addWatcher TriggerCondition"),
    (("共享元素转场",), "geometryTransition shared element transition 共享元素转场"),
    (("geometrytransition",), "geometryTransition shared element transition 共享元素转场"),
    (("视频播放", "事件"), "Video 视频播放 事件调用"),
    (("视频组件", "事件回调"), "Video 视频播放 事件调用"),
    (("蓝牙", "ble"), "Bluetooth BLE cj-apis-bluetooth-ble BLE开发"),
    (("video", "说明"), "Video 视频播放 其他说明 事件调用"),
    (("蓝牙", "hfp"), "Bluetooth HFP HandsFreeAudioGatewayProfile on off ProfileCallbackType"),
    (("动画衔接",), "cj-animation-smoothing 动画衔接 平滑动画"),
    (("textarea",), "TextArea cj-text-input-textarea 多行输入 组件属性 组件事件"),
    (("编辑列表",), "创建列表List 编辑列表 List swipe delete sort"),
    (("控制滚动位置",), "滚动组件通用API 控制滚动位置 Scroll List Scroller"),
    (("提示与确认弹窗",), "AlertDialog 警告弹窗 PromptAction showDialog 确认弹窗"),
    (("组件点击事件",), "ArkUI 交互事件 点击事件 onClick 触屏事件"),
    (("自定义组件",), "custom component lifecycle 自定义组件 生命周期"),
    (("第一个鸿蒙仓颉应用",), "quick start first cangjie app 第一个鸿蒙仓颉应用"),
    (("设备信息获取",), "device_info 设备信息 BasicServicesKit"),
    (("仓颉与 arkts 互操作",), "arkinterop ArkTSInterop arkts_import_cangjie 仓颉 ArkTS 互操作"),
    (("aes 对称加解密",), "AES 对称密钥 CBC CCM GCM CryptoArchitectureKit"),
    (("search", "搜索框"), "Search cj-text-input-search 搜索框 组件属性 组件事件"),
    (("checkbox",), "Checkbox CheckboxGroup cj-button-picker-checkbox 多选"),
    (("radio",), "Radio cj-button-picker-radio 单选框"),
    (("toggle",), "Toggle cj-button-picker-toggle 开关"),
    (("rating",), "Rating cj-button-picker-rating 评分"),
    (("select",), "Select cj-button-picker-select 下拉选择"),
    (("progress",), "Progress cj-information-display-progress 进度条"),
    (("badge",), "Badge cj-information-display-badge 角标"),
    (("sidebarcontainer",), "SideBarContainer cj-grid-layout-sidebar 侧边栏"),
    (("relativecontainer",), "RelativeContainer cj-row-column-stack-relativecontainer 相对布局"),
    (("gridrow", "gridcol"), "GridRow GridCol cj-grid-layout-gridrow cj-grid-layout-gridcol 栅格布局"),
    (("patternlock",), "PatternLock cj-information-display-patternlock 手势密码"),
    (("richeditor",), "RichEditor cj-text-input-richeditor 富文本"),
    (("navdestination",), "NavDestination cj-navigation-switching-navdestination 页面生命周期"),
    (("canvas",), "Canvas cj-canvas-drawing-canvas 自定义绘制"),
    (("提示", "toast"), "PromptAction showToast Toast cj-apis-uicontext-promptaction"),
    (("设置数据项",), "settings cj-apis-settings ohossettings 设置数据项"),
    (("前后台",), "UIAbility Foreground Background cj-uiability-lifecycle app-file-upload-download"),
    (("cookie", "有没有", "判断"), "WebCookieManager hasCookie static func hasCookie Cookie 存在性检查"),
    (("cookie", "是否"), "WebCookieManager hasCookie static func hasCookie Cookie 存在性检查"),
    (("javascript", "返回值"), "WebviewController runJavaScript AsyncCallback String 执行JavaScript"),
    (("js", "返回值"), "WebviewController runJavaScript AsyncCallback String 执行JavaScript"),
    (("暴露", "h5"), "WebviewController registerJavaScriptProxy JavaScriptProxyCallback JS bridge"),
    (("仓颉方法", "h5"), "WebviewController registerJavaScriptProxy JavaScriptProxyCallback JS bridge"),
    (("离线包",), "WebviewController storeWebArchive 保存网页 网页存档"),
    (("深色模式",), "Web darkMode WebDarkMode forceDarkAccess 设置深色模式"),
    (("rawfile",), "加载本地页面 rawfile resources rawfile loadUrl 本地HTML Web组件加载页面"),
    (("rawfile", "路径无效"), "ResourceManager getRawFd rawfile resources rawfile 路径无效"),
    (("fileuri",), "CoreFileKit file_fileuri FileUri 文件URI 路径无效"),
    (("传感器", "回调"), "SensorServiceKit sensor on once off 回调 订阅 传感器开发指导"),
    (("传感器", "不触发"), "SensorServiceKit sensor on once off 回调 不触发 传感器开发指导"),
    (("陀螺仪",), "Gyroscope GyroscopeResponse SensorServiceKit sensor 传感器 订阅"),
    (("devtools",), "setWebDebuggingAccess DevTools Web调试 调试前端页面"),
    (("调试", "webview"), "setWebDebuggingAccess DevTools Web调试 调试前端页面"),
    (("pdf", "webview"), "WebView PDF 预览 cj-web-pdf-preview"),
    (("安全区域", "webview"), "WebView safe area safe-area-insets 安全区域避让"),
    (("secure shield",), "WebView secure shield mode 安全盾牌模式"),
    (("运行时", "权限"), "AtManager requestPermissionsFromUser PermissionRequestResult UIAbilityContext 向用户申请授权"),
    (("申请", "权限"), "AtManager requestPermissionsFromUser PermissionRequestResult UIAbilityContext 向用户申请授权"),
    (("grantstatus",), "GrantStatus requestPermissionsFromUser AtManager PermissionRequestResult"),
    (("网络请求", "权限"), "ohos.permission.INTERNET module.json5 declare permissions HTTP数据请求"),
    (("上传下载",), "app-file-upload-download 应用文件上传下载 上传 下载 request"),
    (("下载", "应用目录"), "下载网络资源文件至应用文件目录 app-file-upload-download"),
    (("上传下载", "错误码"), "app-file-upload-download cj-errorcode-net-http 上传下载任务失败 错误码"),
    (("2300055",), "cj-errorcode-net-http 2300055 发送网络数据失败 HTTP错误码"),
    (("17100001",), "cj-errorcode-webview Webview错误码 17100001 WebviewController 未关联 Web 组件"),
    (("流式响应",), "HttpRequest requestInStream HTTP数据请求 requestInStream接口开发步骤"),
    (("证书锁定",), "HTTP 证书锁定 CertificatePinning certificate pinning 证书校验"),
    (("证书校验",), "HTTP 证书锁定 CertificatePinning certificate pinning 证书校验失败"),
    (("网络连接",), "NetworkKit net_connection 网络连接管理 连接状态 监听"),
    (("websocket", "升级"), "WebSocket upgradeFromClient stdx.net.http WebSocket客户端"),
    (("websocket", "发送"), "WebSocket write WebSocketFrame stdx.net.http 发送消息"),
    (("保存用户设置",), "Preferences getPreferences put flush 用户首选项 保存用户设置"),
    (("读取", "key"), "Preferences has get key 键存在性检查 用户首选项"),
    (("key 不存在",), "Preferences has get key 键存在性检查 用户首选项"),
    (("建表",), "RdbStore executeSql func_executeSqlString_ArrayRelationalStor_2056707e getRdbStore StoreConfig 创建数据库 执行SQL"),
    (("查询数据",), "RdbStore querySql func_querySqlString_ArrayRelationalStoreValueType query ResultSet SQL查询 数据库查询"),
    (("创建数据库",), "RelationalStore getRdbStore func_getRdbStoreUIAbilityContext_StoreConfig RdbStore StoreConfig 创建数据库"),
    (("生命周期", "测试"), "AbilityLifecycleState AbilityDelegator TestKit UIAbility 生命周期状态"),
    (("生命周期状态",), "AbilityLifecycleState AbilityDelegator TestKit UIAbility 生命周期状态"),
    (("uiabilitycontext",), "UIAbilityContext UIAbilityContext 能力 上下文 startAbility terminateSelf"),
    (("imagesource", "解码"), "ImageSource PixelMap 图片解码 cj-image-decoding createPixelMap"),
    (("pixelmap", "解码"), "ImageSource PixelMap 图片解码 cj-image-decoding createPixelMap"),
    (("应用沙箱",), "CoreFileKit file_fs 应用沙箱文件 文件读写"),
    (("filesdir",), "应用沙箱目录 filesDir cj-app-sandbox-directory file_fs 应用文件目录"),
    (("沙箱文件",), "CoreFileKit file_fs 应用沙箱文件 文件读写"),
    (("rpc",), "IPCKit RPC Parcelable rpc通信 远程调用"),
    (("rpc", "错误码"), "IPCKit RPC错误码 cj-errorcode-rpc BusinessError IPC 调用失败"),
    (("1900011",), "cj-errorcode-rpc 1900011 内存分配失败 RPC错误码"),
    (("相机", "黑屏"), "CameraKit 预览黑屏 cj-errorcode-multimedia-camera cj-camera-preparation PreviewOutput"),
    (("相机", "错误码"), "CameraKit 错误码 cj-errorcode-multimedia-camera 相机预览"),
    (("相机设备",), "CameraManager getSupportedCameras camera device management 相机设备列表"),
    (("支持的相机设备",), "CameraManager getSupportedCameras camera device management 相机设备列表"),
    (("previewoutput",), "PreviewOutput createPreviewOutput CameraManager 相机预览输出"),
    (("videooutput",), "VideoOutput start createVideoOutput CameraManager 录像输出"),
    (("huks",), "UniversalKeystoreKit HUKS generateKeyItem 生成密钥 密钥库"),
    (("密钥不存在",), "HUKS hasKeyItem check-key delete-key 密钥是否存在"),
    (("分段", "huks"), "HUKS initSession updateSession finishSession 加解密 分段处理"),
    (("promise",), "JSPromiseCapability JSPromise Promise ArkTS 互操作"),
    (("import", "找不到模块"), "arkts_import_cangjie requireArkModule ArkTS import 仓颉模块 路径"),
    (("调用", "arkts"), "arkts_import_cangjie ArkTS 侧使用互操作代码 仓颉调用ArkTS"),
    (("互操作",), "arkts_import_cangjie cj-apis-ark_interop ArkTSInterop JSValue"),
    (("hilog",), "PerformanceAnalysisKit Hilog HiLog tag domain 日志打印"),
    (("生成密钥",), "HUKS generateKeyItem UniversalKeystoreKit 生成密钥"),
    (("toast",), "PromptAction showToast Toast 提示"),
    (("actionmenu",), "PromptAction showActionMenu ActionMenu 菜单"),
    (("actionmenu", "菜单"), "PromptAction ActionMenuOptions showActionMenu ActionMenu 菜单弹出"),
    (("公共事件", "发布"), "CommonEventPublishData CommonEventManager 公共事件 发布"),
    (("公共事件", "订阅"), "CommonEventSubscribeInfo CommonEventManager 公共事件 订阅"),
    (("后台", "系统事件"), "CommonEventManager CommonEventSubscribeInfo 公共事件 订阅 后台 系统事件"),
    (("commonevent",), "CommonEventManager CommonEventPublishData CommonEventSubscribeInfo 公共事件"),
    (("分布式 kv",), "distributed_kv_store SingleKVStore KVManager KVOptions 分布式键值数据库"),
    (("分布式kv",), "distributed_kv_store SingleKVStore KVManager KVOptions 分布式键值数据库"),
    (("singlekvstore",), "SingleKVStore distributed_kv_store put get 分布式键值数据库"),
    (("kvmanager",), "KVManager distributed_kv_store KVOptions 分布式键值数据库"),
    (("跨设备同步",), "distributed_kv_store SingleKVStore KVManager 分布式键值数据库 跨设备同步"),
    (("tabs",), "Tabs TabContent cj-navigation-switching-tabs 标签页 选项卡"),
    (("标签页",), "Tabs TabContent cj-navigation-switching-tabs 标签页 选项卡"),
    (("popup",), "Popup bindPopup 气泡提示 cj-popup-and-menu-components-popup"),
    (("气泡提示",), "Popup bindPopup 气泡提示 cj-popup-and-menu-components-popup"),
    (("lazyforeach",), "LazyForEach 数据懒加载 rendering_control lazyforeach 组件创建规则"),
    (("状态变化",), "State 状态变化 State宏 观察变化 常见问题 cj-macro-state"),
    (("build", "state"), "State宏 不允许在build里改状态变量 常见问题"),
    (("长列表", "卡顿"), "List LazyForEach 长列表 性能优化 数据懒加载"),
    (("相册", "图片列表"), "PhotoAccessHelper FetchResult Album 相册管理 图片列表"),
    (("修改头像", "相册"), "PhotoAccessHelper FetchResult ImageSource ImagePacker Preferences 头像 相册 选择 保存"),
    (("定位", "权限"), "LocationKit 定位权限 cj-location-permission-guidelines getCurrentLocation"),
    (("定位", "没有权限"), "LocationKit 定位权限 cj-location-guidelines getCurrentLocation 位置服务"),
    (("定位打卡",), "LocationKit GeoLocationManager PhotoAccessHelper app-file-upload-download 定位 上传 图片"),
    (("定位", "空位置"), "LocationKit 定位失败 空位置 cj-location-guidelines cj-location-permission-guidelines"),
    (("media", "错误码"), "MediaKit Media错误码 cj-errorcode-multimedia-media 无可用资源"),
    (("无可用资源",), "MediaKit Media错误码 5411007 无可用资源"),
    (("jpeg",), "ImagePacker 图片编码 JPEG cj-image-encoding"),
)


def utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        fn = getattr(stream, "reconfigure", None)
        if callable(fn):
            fn(encoding="utf-8", errors="replace")


def load_jsonl(path: Path, id_key: str) -> dict[str, dict]:
    rows: dict[str, dict] = {}
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            rows[item[id_key]] = item
    return rows


def load_index(index_dir: Path) -> dict:
    required = [
        index_dir / "manifest.json",
        index_dir / "tasks.jsonl",
        index_dir / "apis.jsonl",
        index_dir / "examples.jsonl",
        index_dir / "docs.jsonl",
        index_dir / "aliases.json",
        index_dir / "search.db",
    ]
    missing = [str(path.name) for path in required if not path.exists()]
    if missing:
        build_script = Path(__file__).resolve().parent / "build_index_v3.py"
        raise FileNotFoundError(
            f"V3 索引不完整，缺少: {', '.join(missing)}。"
            f" 请先执行 `python {build_script}`。"
        )
    return {
        "manifest": json.loads((index_dir / "manifest.json").read_text(encoding="utf-8")),
        "tasks": load_jsonl(index_dir / "tasks.jsonl", "task_id"),
        "apis": load_jsonl(index_dir / "apis.jsonl", "api_id"),
        "examples": load_jsonl(index_dir / "examples.jsonl", "example_id"),
        "docs": load_jsonl(index_dir / "docs.jsonl", "doc_id"),
        "aliases": json.loads((index_dir / "aliases.json").read_text(encoding="utf-8")),
        "db": index_dir / "search.db",
    }


def normalize_query(query: str, aliases: dict[str, list[str]]) -> str:
    expanded = [query.strip()]
    lowered = query.lower()
    for key, values in aliases.items():
        key_lower = key.lower()
        if key in GENERIC_ALIAS_KEYS:
            continue
        if key_lower.isascii() and len(key_lower) <= 3:
            key_matched = bool(re.search(rf"(?<![a-z0-9_]){re.escape(key_lower)}(?![a-z0-9_])", lowered))
        else:
            key_matched = key_lower in lowered
        if key_matched:
            expanded.extend(values)
            continue
        for value in values:
            if value in GENERIC_ALIAS_KEYS:
                continue
            value_lower = value.lower()
            if value_lower.isascii() and len(value_lower) <= 3:
                value_matched = bool(re.search(rf"(?<![a-z0-9_]){re.escape(value_lower)}(?![a-z0-9_])", lowered))
            else:
                value_matched = value_lower in lowered
            if value_matched:
                expanded.extend(values)
                break
    return " ".join(dict.fromkeys(item for item in expanded if item))


def expand_query_for_understanding(query: str, aliases: dict[str, list[str]], understanding: dict) -> str:
    expanded = [normalize_query(query, aliases)]
    lowered = query.lower()
    for key in understanding.get("primary_objects", []):
        value = DOMAIN_QUERY_EXPANSIONS.get(str(key))
        if value:
            expanded.append(value)
    for required_tokens, value in ACTION_QUERY_EXPANSIONS:
        if all(token in lowered for token in required_tokens):
            expanded.append(value)
    return " ".join(dict.fromkeys(item for item in expanded if item))


def tokenize_query(query: str) -> str:
    import re

    tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_.-]*|[\u3400-\u4dbf\u4e00-\u9fff]+|[0-9]+", query)
    parts: list[str] = []
    for token in tokens:
        for char in token:
            if "\u3400" <= char <= "\u9fff":
                parts.append(char)
        if token.isascii():
            parts.append(token)
    parts = list(dict.fromkeys(part for part in parts if part.strip()))
    return " OR ".join(f'"{part}"' for part in parts)


def score_bonus(query: str, metadata: dict) -> float:
    q = query.lower()
    bonus = 0.0
    for alias in metadata.get("aliases", []):
        alias_lower = alias.lower()
        if alias_lower == q:
            bonus += 6.0
        elif alias_lower in q or q in alias_lower:
            bonus += 3.0
    if metadata.get("title", "").lower() in q:
        bonus += 2.0
    return bonus


def normalize_object(value: object) -> str:
    return str(value).lower().replace("_", "").replace("-", "").strip()


def has_object_overlap(query_objects: set[str], metadata_objects: set[str]) -> bool:
    for query_object in query_objects:
        if query_object == "general":
            continue
        for metadata_object in metadata_objects:
            if query_object == metadata_object or query_object in metadata_object or metadata_object in query_object:
                return True
    return False


def action_identifiers(query: str) -> set[str]:
    lowered = query.lower()
    identifiers: set[str] = set()
    phrase_map = (
        (("cookie", "有没有", "判断", "是否"), "hascookie"),
        (("javascript", "返回值", "js"), "runjavascript"),
        (("暴露", "h5", "仓颉方法"), "registerjavascriptproxy"),
        (("离线包",), "storewebarchive"),
        (("深色模式",), "darkmode"),
        (("devtools", "web调试", "webview 调试"), "setwebdebuggingaccess"),
        (("rawfile",), "rawfile"),
        (("fileuri",), "fileuri"),
        (("传感器", "回调"), "sensor"),
        (("17100001",), "17100001"),
        (("运行时", "申请权限", "用户申请权限", "用户授权"), "requestpermissionsfromuser"),
        (("保存用户设置", "用户设置"), "getpreferences"),
        (("key 不存在", "键不存在"), "has"),
        (("建表",), "executesql"),
        (("查询数据",), "querysql"),
        (("创建数据库",), "getrdbstore"),
        (("生命周期", "测试"), "abilitylifecyclestate"),
        (("生命周期状态",), "abilitylifecyclestate"),
        (("流式响应",), "requestinstream"),
        (("升级连接",), "upgradefromclient"),
        (("toast", "提示"), "showtoast"),
        (("actionmenu", "菜单"), "showactionmenu"),
        (("actionmenu",), "actionmenuoptions"),
        (("singlekvstore", "kvstore"), "singlekvstore"),
        (("kvmanager",), "kvmanager"),
        (("公共事件", "发布"), "commoneventpublishdata"),
        (("公共事件", "订阅"), "commoneventsubscribeinfo"),
        (("grantstatus",), "grantstatus"),
        (("promise",), "jspromisecapability"),
        (("hilog",), "hilog"),
        (("build", "state"), "state"),
        (("相册", "图片列表"), "fetchresult"),
        (("图片编码", "jpeg"), "imagepacker"),
        (("生成密钥", "huks"), "generatekeyitem"),
    )
    for phrases, identifier in phrase_map:
        if any(phrase in lowered for phrase in phrases):
            identifiers.add(identifier)
    return identifiers


def source_path_text(metadata: dict) -> str:
    return " ".join(str(path).lower() for path in metadata.get("source_paths", []))


PATH_QUERY_TOKENS = (
    (("request-agent",), ("cj-apis-request-agent", "ohosrequest上传下载", "class_task", "class_config", "enum_state")),
    (("request-agent", "headers"), ("var_headers", "class_config")),
    (("saveas",), ("var_saveas", "class_config")),
    (("formitem",), ("class_formitem",)),
    (("filespec",), ("class_filespec",)),
    (("taskinfo", "priority"), ("class_taskinfo", "priority")),
    (("faults",), ("enum_faults",)),
    (("下载任务", "进度"), ("func_oneventcallb", "class_progress")),
    (("下载任务", "暂停"), ("func_pause", "class_task")),
    (("下载任务", "停止"), ("func_stop", "class_task")),
    (("任务状态", "枚举"), ("enum_state",)),
    (("回调事件", "事件类型"), ("enum_eventcallbacktype", "func_oneventcallb")),
    (("请求代理", "网络类型"), ("enum_network", "class_config")),
    (("datasharepredicates", "筛选", "排序"), ("data_share_predicates", "class_datasharepredicates", "equalto", "orderbyasc")),
    (("hiappevent", "事件上报", "应用事件"), ("cj-apis-hiappevent", "hi_app_event", "class_hiappevent", "eventvaluetype", "eventtype")),
    (("用户标识", "setuserid"), ("static_func_setus", "class_hiappevent")),
    (("清空", "cleardata"), ("static_func_clear", "class_hiappevent")),
    (("观察者名称非法", "11102001"), ("cj-errorcode-hiappevent", "11102001")),
    (("观察者", "watcher"), ("class_watcher", "triggercondition", "appeventfilter")),
    (("冻屏事件",), ("freeze-events", "订阅应用冻屏事件")),
    (("崩溃事件",), ("crash-events", "订阅崩溃事件")),
    (("hitracemeter",), ("hi_tracemeter", "class_hitracemeter")),
    (("共享元素转场", "geometrytransition"), ("cj-shared-element-transition", "geometrytransition", "sharedtransition")),
    (("视频播放", "video"), ("cj-common-components-video-player", "视频播放video", "事件调用", "其他说明")),
    (("视频组件", "事件回调"), ("cj-common-components-video-player", "事件调用")),
    (("ble",), ("cj-apis-bluetooth-ble",)),
    (("蓝牙", "hfp"), ("cj-apis-bluetooth-hfp", "handsfreeaudiogatewayprofile")),
    (("动画衔接", "顺滑"), ("cj-animation-smoothing", "动画衔接")),
    (("textarea", "多行输入"), ("cj-text-input-textarea", "textarea")),
    (("编辑列表",), ("编辑列表", "cj-layout-development-create-list")),
    (("控制滚动位置",), ("滚动组件通用api", "控制滚动位置")),
    (("提示与确认弹窗",), ("cj-dialog-alertdialog", "promptaction")),
    (("组件点击事件",), ("cj-event-overview", "touch-screen-event", "universal-event-click")),
    (("自定义组件",), ("cj-custom-component-lifecycle",)),
    (("第一个鸿蒙仓颉应用",), ("cj-quick-start-first-cangjie-app",)),
    (("设备信息获取",), ("cj-apis-device_info",)),
    (("仓颉与 arkts 互操作",), ("cj-apis-ark_interop", "arkts_import_cangjie")),
    (("aes 对称加解密",), ("cj-crypto-aes-sym-encrypt-decrypt", "cj-crypto-sym-encrypt-decrypt-spec")),
    (("search", "搜索框"), ("cj-text-input-search", "/search/")),
    (("checkbox", "多选"), ("cj-button-picker-checkbox", "checkbox")),
    (("radio", "单选"), ("cj-button-picker-radio", "radio-button", "/radio")),
    (("toggle", "开关"), ("cj-button-picker-toggle", "toggle")),
    (("rating", "评分"), ("cj-button-picker-rating", "rating")),
    (("select", "下拉选择"), ("cj-button-picker-select", "/select/")),
    (("progress", "进度"), ("cj-information-display-progress", "progress")),
    (("badge", "角标"), ("cj-information-display-badge", "badge")),
    (("sidebarcontainer", "侧边栏"), ("cj-grid-layout-sidebar", "sidebarcontainer")),
    (("relativecontainer", "相对布局"), ("cj-row-column-stack-relativecontainer", "relativecontainer")),
    (("gridrow", "gridcol", "栅格"), ("cj-grid-layout-gridrow", "cj-grid-layout-gridcol", "gridrow", "gridcol")),
    (("patternlock", "手势密码"), ("cj-information-display-patternlock", "patternlock")),
    (("richeditor", "富文本"), ("cj-text-input-richeditor", "richeditor")),
    (("navdestination",), ("cj-navigation-switching-navdestination", "navdestination")),
    (("canvas", "自定义绘制"), ("cj-canvas-drawing-canvas/", "/canvas/")),
    (("promptaction", "toast", "本地提示"), ("cj-apis-uicontext-promptaction", "promptaction")),
    (("settings", "设置数据项"), ("cj-apis-settings", "ohossettings")),
    (("photooutput", "拍照输出"), ("class_photooutput", "createphotooutput")),
    (("条件渲染",), ("cj-rendering-control-ifelse",)),
    (("图片压缩", "图片编码"), ("cj-image-encoding", "imagepacker", "app-file-upload-download")),
    (("camera", "相机", "预览黑屏"), ("cj-camera-preparation", "cj-errorcode-multimedia-camera", "cj-apis-multimedia-camera")),
    (("定位", "location"), ("geo_location_manager", "cj-location-guidelines")),
    (("公共事件", "commonevent"), ("common_event_manager", "common_event_subscribe_info", "cj-appstorage")),
    (("权限拒绝", "授权"), ("cj-request-user-authorization", "cj-apis-settings")),
    (("token",), ("preferences", "security_huks", "huks")),
    (("前后台", "foreground", "background"), ("cj-uiability-lifecycle", "app-file-upload-download")),
)


def path_query_score(query: str, path: str) -> int:
    lowered = query.lower()
    normalized_path = path.lower()
    score = 0
    for query_tokens, path_tokens in PATH_QUERY_TOKENS:
        if any(token in lowered for token in query_tokens) and any(token in normalized_path for token in path_tokens):
            score += 100
    for token in re.findall(r"[A-Za-z_][A-Za-z0-9_.-]*", query):
        token_lower = token.lower()
        if len(token_lower) >= 4 and token_lower in normalized_path:
            score += 20
    if "组件属性" in normalized_path or "组件事件" in normalized_path:
        score += 5
    if any(alias in normalized_path for alias in ("/.overview", "/.abstract")):
        score += 2
    return score


def ordered_paths_for_query(paths: list[str], query: str) -> list[str]:
    return sorted(paths, key=lambda path: path_query_score(query, path), reverse=True)


DIRECT_PATHS = (
    (("request-agent",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/.overview.md",)),
    (("request-agent headers",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_Config/var_headers_12more_569af778.md",)),
    (("saveas",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_Config/var_saveas_4more_81a0a222.md",)),
    (("formitem",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_FormItem_2more_88e81b66.md",)),
    (("filespec",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_FileSpec.md",)),
    (("taskinfo", "priority"), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_TaskInfo/.overview.md",)),
    (("faults",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/enum_Faults_2more_08d0fb1f.md",)),
    (("下载任务进度",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_Task/func_onEventCallb_2more_7f18e261.md", "harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_Progress_f8608967.md")),
    (("下载任务暂停",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_Task/func_pause_3more_83cdc281.md", "harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_Task/.overview.md")),
    (("下载任务停止",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_Task/func_stop_a2a70321.md", "harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_Task/.overview.md")),
    (("任务状态枚举",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/enum_State.md",)),
    (("回调事件类型",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/enum_EventCallbackType.md", "harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_Task/.overview.md")),
    (("任务信息优先级",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_TaskInfo/let_priority_9more_2ec57424.md", "harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_TaskInfo/.overview.md")),
    (("请求代理网络类型",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/enum_Network.md", "harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-request-agent/ohosrequest上传下载/class_Config/.overview.md")),
    (("datasharepredicates",), ("harmonyos-6.1-8k/API/ArkData/cj-apis-data_share_predicates/.overview.md",)),
    (("筛选", "排序"), ("harmonyos-6.1-8k/API/ArkData/cj-apis-data_share_predicates/ohosdatadata_share_predicates数据共享谓词/class_DataSharePredicates/.overview.md",)),
    (("hiappevent", "事件上报"), ("harmonyos-6.1-8k/API/PerformanceAnalysisKit/cj-apis-hiappevent/.overview.md", "harmonyos-6.1-8k/Guide/dfx/cj-hiappevent-event-reporting/.overview.md")),
    (("用户标识",), ("harmonyos-6.1-8k/API/PerformanceAnalysisKit/cj-apis-hiappevent/ohoshiviewdfxhi_app_event应用事件打点/class_HiAppEvent/static_func_setUs_2more_d59e3176.md", "harmonyos-6.1-8k/API/PerformanceAnalysisKit/cj-apis-hiappevent/ohoshiviewdfxhi_app_event应用事件打点/class_HiAppEvent/.overview.md")),
    (("清空本地事件数据", "清空事件数据"), ("harmonyos-6.1-8k/API/PerformanceAnalysisKit/cj-apis-hiappevent/ohoshiviewdfxhi_app_event应用事件打点/class_HiAppEvent/static_func_clear_3more_c06532ad.md", "harmonyos-6.1-8k/API/PerformanceAnalysisKit/cj-apis-hiappevent/ohoshiviewdfxhi_app_event应用事件打点/class_HiAppEvent/.overview.md")),
    (("观察者",), ("harmonyos-6.1-8k/API/PerformanceAnalysisKit/cj-apis-hiappevent/ohoshiviewdfxhi_app_event应用事件打点/class_Watcher/.overview.md",)),
    (("观察者名称非法",), ("harmonyos-6.1-8k/API/PerformanceAnalysisKit/cj-errorcode-hiappevent/应用事件打点错误码/11102001_非法的观察者名称_7more_87fae833.md", "harmonyos-6.1-8k/API/PerformanceAnalysisKit/cj-errorcode-hiappevent/应用事件打点错误码/.overview.md")),
    (("冻屏事件",), ("harmonyos-6.1-8k/Guide/dfx/cj-hiappevent-watcher-freeze-events-cangjie/订阅应用冻屏事件/.overview.md",)),
    (("崩溃事件",), ("harmonyos-6.1-8k/Guide/dfx/cj-hiappevent-watcher-crash-events-cangjie/订阅崩溃事件/.overview.md",)),
    (("崩溃和冻屏",), ("harmonyos-6.1-8k/Guide/dfx/cj-hiappevent-watcher-crash-events-cangjie/.overview.md", "harmonyos-6.1-8k/Guide/dfx/cj-hiappevent-watcher-freeze-events-cangjie/.overview.md")),
    (("hitracemeter",), ("harmonyos-6.1-8k/API/PerformanceAnalysisKit/cj-apis-hi_tracemeter/.overview.md",)),
    (("共享元素转场", "geometrytransition"), ("harmonyos-6.1-8k/Guide/arkui-cj/cj-shared-element-transition/.overview.md",)),
    (("视频播放", "video"), ("harmonyos-6.1-8k/Guide/arkui-cj/cj-common-components-video-player/视频播放Video/.overview.md",)),
    (("视频组件事件", "视频播放页退出"), ("harmonyos-6.1-8k/Guide/arkui-cj/cj-common-components-video-player/视频播放Video/事件调用_2more_f25bfbd8.md", "harmonyos-6.1-8k/Guide/arkui-cj/cj-common-components-video-player/视频播放Video/.overview.md")),
    (("蓝牙 ble",), ("harmonyos-6.1-8k/API/ConnectivityKit/cj-apis-bluetooth-ble/.overview.md", "harmonyos-6.1-8k/API/ConnectivityKit/cj-apis-bluetooth-ble/ohosbluetoothble蓝牙ble模块/.overview.md")),
    (("蓝牙 hfp",), ("harmonyos-6.1-8k/API/ConnectivityKit/cj-apis-bluetooth-hfp/ohosbluetoothhfp蓝牙hfp模块/class_HandsFreeAudioGatewayProfile/.overview.md",)),
    (("hfp 状态回调",), ("harmonyos-6.1-8k/API/ConnectivityKit/cj-apis-bluetooth-hfp/ohosbluetoothhfp蓝牙hfp模块/class_HandsFreeAudioGatewayProfile/func_onProfileCallbackT_afa11f1f.md",)),
    (("hfp 监听取消",), ("harmonyos-6.1-8k/API/ConnectivityKit/cj-apis-bluetooth-hfp/ohosbluetoothhfp蓝牙hfp模块/class_HandsFreeAudioGatewayProfile/func_offProfileCa_2more_0abcf780.md",)),
    (("动画衔接",), ("harmonyos-6.1-8k/Guide/arkui-cj/cj-animation-smoothing/.overview.md", "harmonyos-6.1-8k/Guide/arkui-cj/cj-animation-smoothing/动画衔接/.overview.md")),
    (("textarea", "多行输入"), ("harmonyos-6.1-8k/API/arkui-cj/cj-text-input-textarea/TextArea/.overview.md",)),
    (("编辑列表",), ("harmonyos-6.1-8k/Guide/arkui-cj/cj-layout-development-create-list/创建列表List/编辑列表_2more_47baa191.md",)),
    (("控制滚动位置",), ("harmonyos-6.1-8k/API/arkui-cj/cj-scroll-swipe-common/滚动组件通用API/.overview.md", "harmonyos-6.1-8k/Guide/arkui-cj/cj-layout-development-create-list/创建列表List/控制滚动位置_2more_e6a56bcb.md")),
    (("提示与确认弹窗",), ("harmonyos-6.1-8k/API/arkui-cj/cj-dialog-alertdialog/.overview.md", "harmonyos-6.1-8k/API/arkui-cj/cj-dialog-alertdialog/警告弹窗AlertDialog/.overview.md")),
    (("组件点击事件",), ("harmonyos-6.1-8k/Guide/arkui-cj/cj-event-overview/cj-event-overview.md", "harmonyos-6.1-8k/Guide/arkui-cj/cj-common-events-touch-screen-event/触屏事件/.overview.md")),
    (("自定义组件",), ("harmonyos-6.1-8k/API/arkui-cj/cj-custom-component-lifecycle/.overview.md",)),
    (("第一个鸿蒙仓颉应用",), ("harmonyos-6.1-8k/Guide/cj-start/start/quick-start/cj-quick-start-first-cangjie-app/.overview.md",)),
    (("设备信息获取",), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-device_info/.overview.md",)),
    (("仓颉与 arkts 互操作",), ("harmonyos-6.1-8k/API/arkinterop/cj-apis-ark_interop/.overview.md", "harmonyos-6.1-8k/Guide/learn-cj/FFI/cangjie-arkts/arkts_import_cangjie/.overview.md")),
    (("aes 对称加解密",), ("harmonyos-6.1-8k/Guide/security/CryptoArchitectureKit/cj-crypto-aes-sym-encrypt-decrypt-cbc/.overview.md", "harmonyos-6.1-8k/Guide/security/CryptoArchitectureKit/cj-crypto-aes-sym-encrypt-decrypt-ccm/.overview.md", "harmonyos-6.1-8k/Guide/security/CryptoArchitectureKit/cj-crypto-aes-sym-encrypt-decrypt-gcm/.overview.md")),
    (("search", "搜索框"), ("harmonyos-6.1-8k/API/arkui-cj/cj-text-input-search/Search/组件属性.md",)),
    (("radio", "单选"), ("harmonyos-6.1-8k/API/arkui-cj/cj-button-picker-radio/.overview.md",)),
    (("toggle", "开关"), ("harmonyos-6.1-8k/API/arkui-cj/cj-button-picker-toggle/Toggle/.overview.md",)),
    (("patternlock", "手势密码"), ("harmonyos-6.1-8k/API/arkui-cj/cj-information-display-patternlock/PatternLock/组件事件_3more_ba8a0175.md",)),
    (("richeditor", "富文本"), ("harmonyos-6.1-8k/API/arkui-cj/cj-text-input-richeditor/RichEditor/组件事件/.overview.md",)),
    (("navdestination",), ("harmonyos-6.1-8k/API/arkui-cj/cj-navigation-switching-navdestination/NavDestination/组件事件_3more_9fedce6b.md",)),
    (("canvas", "自定义绘制"), ("harmonyos-6.1-8k/API/arkui-cj/cj-canvas-drawing-canvas/Canvas/.overview.md",)),
    (("前后台", "foreground", "background"), ("harmonyos-6.1-8k/Guide/application-models/cj-uiability-lifecycle/UIAbility组件生命周期/生命周期状态说明/Foreground和Background状态.md",)),
    (("token", "本地保存"), ("harmonyos-6.1-8k/API/ArkData/cj-apis-preferences", "harmonyos-6.1-8k/API/arkui-cj/cj-apis-uicontext-router")),
    (("token", "加密"), ("harmonyos-6.1-8k/API/UniversalKeystoreKit/cj-apis-security_huks", "harmonyos-6.1-8k/API/ArkData/cj-apis-preferences")),
    (("http", "header"), ("harmonyos-6.1-8k/API/NetworkKit/cj-apis-net-http/ohosnethttp数据请求/class_HttpRequestOptions/.overview.md", "harmonyos-6.1-8k/API/NetworkKit/cj-apis-net-http")),
    (("条件渲染",), ("harmonyos-6.1-8k/Guide/arkui-cj/rendering_control/cj-rendering-control-ifelse",)),
    (("图片压缩", "图片编码"), ("harmonyos-6.1-8k/Guide/media/image/cj-image-encoding", "harmonyos-6.1-8k/Guide/basic-services/request/cj-app-file-upload-download")),
    (("相机权限", "相机需要声明", "声明哪些权限"), ("harmonyos-6.1-8k/Guide/security/AccessToken/cj-declare-permissions", "harmonyos-6.1-8k/API/CameraKit/cj-apis-multimedia-camera")),
    (("camera", "相机", "预览黑屏"), ("harmonyos-6.1-8k/Guide/media/camera/cj-camera-preparation", "harmonyos-6.1-8k/API/CameraKit/cj-errorcode-multimedia-camera")),
    (("photooutput", "拍照输出"), ("harmonyos-6.1-8k/API/CameraKit/cj-apis-multimedia-camera/ohosmultimediacamera相机管理/class_PhotoOutput/.overview.md",)),
    (("连续定位", "定位轨迹"), ("harmonyos-6.1-8k/API/LocationKit/cj-apis-geo_location_manager", "harmonyos-6.1-8k/Guide/location/cj-location-guidelines")),
    (("公共事件", "刷新状态"), ("harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-common_event_manager", "harmonyos-6.1-8k/Guide/arkui-cj/state_management/cj-appstorage")),
    (("权限拒绝", "引导设置"), ("harmonyos-6.1-8k/Guide/security/AccessToken/cj-request-user-authorization", "harmonyos-6.1-8k/API/BasicServicesKit/cj-apis-settings")),
)


def direct_paths_for_query(query: str) -> list[str]:
    lowered = query.lower()
    paths: list[str] = []
    for query_tokens, target_paths in DIRECT_PATHS:
        if any(token in lowered for token in query_tokens):
            for path in target_paths:
                if path not in paths:
                    paths.append(path)
    return paths


def path_intent_bonus(query: str, metadata: dict, card_type: str) -> float:
    lowered = query.lower()
    paths = source_path_text(metadata)
    bonus = 0.0
    component_path_boosts = (
        (("textarea", "多行输入"), ("cj-text-input-textarea",), 180.0),
        (("search", "搜索框"), ("cj-text-input-search",), 180.0),
        (("checkbox", "多选"), ("cj-button-picker-checkbox",), 180.0),
        (("radio", "单选"), ("cj-button-picker-radio", "cj-common-components-radio-button"), 180.0),
        (("toggle", "开关"), ("cj-button-picker-toggle",), 180.0),
        (("rating", "评分"), ("cj-button-picker-rating",), 180.0),
        (("select", "下拉选择"), ("cj-button-picker-select",), 160.0),
        (("progress", "进度"), ("cj-information-display-progress",), 160.0),
        (("badge", "角标"), ("cj-information-display-badge",), 160.0),
        (("sidebarcontainer", "侧边栏"), ("cj-grid-layout-sidebar",), 160.0),
        (("relativecontainer", "相对布局"), ("cj-row-column-stack-relativecontainer",), 160.0),
        (("gridrow", "gridcol", "栅格"), ("cj-grid-layout-gridrow", "cj-grid-layout-gridcol"), 160.0),
        (("patternlock", "手势密码"), ("cj-information-display-patternlock",), 160.0),
        (("richeditor", "富文本"), ("cj-text-input-richeditor",), 160.0),
        (("navdestination",), ("cj-navigation-switching-navdestination",), 160.0),
        (("canvas", "自定义绘制"), ("cj-canvas-drawing-canvas",), 140.0),
        (("rect",), ("cj-graphic-drawing-rect",), 140.0),
        (("设置数据项", "settings"), ("cj-apis-settings",), 120.0),
        (("foreground", "background", "前后台"), ("cj-uiability-lifecycle",), 120.0),
    )
    for query_tokens, path_tokens, value in component_path_boosts:
        if any(token in lowered for token in query_tokens) and any(token in paths for token in path_tokens):
            bonus += value
    if ("navigation" in lowered or "导航" in lowered) and "cj-navigation-navigation" in paths:
        bonus += 18.0
    if ("跳转" in lowered or "带参数" in lowered) and (
        "cj-apis-uicontext-router" in paths or "cj-navigation-switching-navdestination" in paths
    ):
        bonus += 22.0
    if "textinput" in lowered and "cj-text-input-textinput" in paths:
        bonus += 18.0
    if "rawfile" in lowered and any(token in lowered for token in ("web", "webview", "网页")) and (
        "cj-web-page-loading-with-web-components" in paths
        or "loadurl" in paths
        or "cj-web-web" in paths
    ):
        bonus += 180.0
    if "rawfile" in lowered and not any(token in lowered for token in ("web", "webview", "网页")) and (
        "resource_manager" in paths or "getrawfd" in paths or "raw_file_descriptor" in paths
    ):
        bonus += 120.0
    if "fileuri" in lowered and ("file_fileuri" in paths or "class_fileuri" in paths):
        bonus += 120.0
    if "传感器" in lowered and (
        "cj-apis-sensor" in paths or "cj-sensor-guidelines" in paths or "sensorservicekit" in paths
    ):
        bonus += 120.0
    if ("陀螺仪" in lowered or "gyroscope" in lowered) and (
        "gyroscope" in paths or "class_gyroscopere" in paths
    ):
        bonus += 180.0
    if "localstorage" in lowered and "uiability" in lowered and "cj-localstorage" in paths:
        bonus += 45.0
    if ("scroll" in lowered or "滚动" in lowered) and "cj-scroll-swipe-scroll" in paths:
        bonus += 22.0
    if ("arkts" in lowered or "互操作" in lowered or "import" in lowered) and "arkts_import_cangjie" in paths:
        bonus += 55.0
    if "import" in lowered and "requirearkmo" in paths:
        bonus += 90.0
    if "promise" in lowered and "jspromisecapability" in paths:
        bonus += 90.0
    if "previewoutput" in lowered and (
        "class_previewoutput" in paths or "createpreviewoutput" in paths or "func_createprevie" in paths
    ):
        bonus += 90.0
    if "videooutput" in lowered and (
        "class_videooutput" in paths or "func_start" in paths or "createvideo" in paths
    ):
        bonus += 90.0
    if "17100001" in lowered and "cj-errorcode-webview" in paths:
        bonus += 55.0
    if ("popup" in lowered or "气泡提示" in lowered) and "cj-popup-and-menu-components-popup" in paths:
        bonus += 55.0
    if ("相机错误码" in lowered or ("相机" in lowered and "错误码" in lowered)) and "cj-errorcode-multimedia-camera" in paths:
        bonus += 55.0
    if ("相机设备" in lowered or "支持的相机设备" in lowered or "设备列表" in lowered) and (
        "class_cameramanager" in paths or "cj-camera-device-management" in paths or "cj-camera-preparation" in paths
    ):
        bonus += 80.0
    if "黑屏" in lowered and ("cj-errorcode-multimedia-camera" in paths or "cj-camera-preparation" in paths):
        bonus += 120.0
    if "telephony" in lowered and "cj-errorcode-telephony" in paths:
        bonus += 60.0
    if "uiability" in lowered and "class_uiability" in paths:
        bonus += 80.0
    if ("横竖屏" in lowered or "屏幕方向" in lowered) and (
        "displaymanager" in paths or "cj-apis-window" in paths
    ):
        bonus += 45.0
    if "hilog" in lowered and "cj-apis-hilog" in paths:
        bonus += 60.0
    if ("promptaction" in lowered or "toast" in lowered or "本地提示" in lowered) and "cj-apis-uicontext-promptaction" in paths:
        bonus += 120.0
    if ("photoutput" in lowered or "photooutput" in lowered or "拍照输出" in lowered) and (
        "class_photooutput" in paths or "createphotooutput" in paths
    ):
        bonus += 140.0
    if ("图片压缩" in lowered or "图片编码" in lowered) and (
        "cj-image-encoding" in paths or "imagepacker" in paths or "app-file-upload-download" in paths
    ):
        bonus += 90.0
    if "video" in lowered and ("cj-image-video-video" in paths or "cj-errorcode-multimedia-media" in paths):
        bonus += 110.0
    if "条件渲染" in lowered and ("cj-rendering-control-ifelse" in paths or "cj-scroll-swipe-list" in paths):
        bonus += 110.0
    if "权限拒绝" in lowered and (
        "cj-request-user-authorization" in paths or "cj-apis-settings" in paths or "cj-app-permission" in paths
    ):
        bonus += 120.0
    if "token" in lowered and ("preferences" in paths or "security_huks" in paths or "huks" in paths):
        bonus += 80.0
    if "后台" in lowered and "系统事件" in lowered and "common_event" in paths:
        bonus += 50.0
    if "grantstatus" in lowered and "enum_grantstatus" in paths:
        bonus += 70.0
    if "requestinstream" in lowered or ("流式下载" in lowered and "文件保存" in lowered):
        if "requestinstream" in paths or "app-file-upload-download" in paths:
            bonus += 35.0
    if "state" in lowered and "build" in lowered and "cj-macro-state" in paths:
        bonus += 90.0
    if "定位打卡" in lowered and (
        "geo_location_manager" in paths or "photo_access_helper" in paths or "app-file-upload-download" in paths
    ):
        bonus += 38.0
    if "定位" in lowered and "没有权限" in lowered and (
        "cj-location-guidelines" in paths or "geo_location_manager" in paths
    ):
        bonus += 45.0
    if "密钥不存在" in lowered and ("cj-huks-check-key" in paths or "func_haskeyitem" in paths):
        bonus += 55.0
    if "分段" in lowered and "huks" in lowered and (
        "cj-huks-encryption-decryption" in paths or "cj-crypto-encrypt-decrypt-by-segment" in paths
    ):
        bonus += 45.0
    if "应用文件访问权限错误" in lowered and (
        "cj-errorcode-filemanagement" in paths or "cj-app-file-access" in paths
    ):
        bonus += 90.0
    if "filesdir" in lowered and (
        "cj-app-sandbox-directory" in paths or "cj-apis-file_fs" in paths or "cj-app-file-access" in paths
    ):
        bonus += 90.0
    return bonus


def rerank_score(understanding: dict, item: dict, card_type: str) -> float:
    metadata = item["metadata"]
    score = item["score"]
    primary_objects = {normalize_object(value) for value in metadata.get("primary_objects", [])}
    query_objects = {normalize_object(value) for value in understanding["primary_objects"]}
    overlap = primary_objects.intersection(query_objects)
    has_overlap = bool(overlap) or has_object_overlap(query_objects, primary_objects)
    identifiers = {str(value).lower() for value in understanding.get("identifiers", [])}
    identifiers.update(action_identifiers(understanding["normalized_query"]))
    if identifiers:
        searchable_values = [
            metadata.get("title", ""),
            metadata.get("name", ""),
            *metadata.get("aliases", []),
            *metadata.get("semantic_aliases", []),
            *metadata.get("user_queries", []),
            *metadata.get("source_paths", []),
            *[Path(path).stem for path in metadata.get("source_paths", [])],
        ]
        searchable = {str(value).lower().replace("\\", "") for value in searchable_values if value}
        for identifier in identifiers:
            if (
                identifier in CONTEXTUAL_IDENTIFIER_TOKENS
                and query_objects != {"general"}
                and not has_overlap
            ):
                continue
            if identifier in searchable:
                score += 40.0 if identifier in HIGH_VALUE_IDENTIFIERS else 25.0
            elif identifier in {"headers", "loadurl", "rawfile", "user-agent"} and any(identifier in value for value in searchable):
                score += 25.0
            elif any(identifier in value for value in searchable):
                score += 20.0 if identifier in HIGH_VALUE_IDENTIFIERS else 10.0
    if understanding["preferred_result"] == card_type:
        score += 8.0
    intent_types = metadata.get("intent_types", [])
    if understanding["intent_type"] in intent_types:
        score += 10.0
    stages = metadata.get("stages", [])
    if understanding["stage"] in stages:
        score += 4.0
    score += 8.0 * len(overlap)
    if has_overlap and not overlap:
        score += 6.0
    if "stdfs" in overlap and query_objects <= {"stdfs", "general"}:
        score += 20.0
    if query_objects != {"general"} and not has_overlap:
        score -= 30.0 if understanding["intent_type"] == "api_lookup" else 6.0
    problem_signals = metadata.get("problem_signals", [])
    lowered_query = understanding["normalized_query"].lower()
    if any(signal.lower() in lowered_query for signal in problem_signals):
        score += 5.0
    score += path_intent_bonus(lowered_query, metadata, card_type)
    score += float(metadata.get("priority", 0.0))
    return round(score, 3)


def search_cards(db_path: Path, query: str, card_types: tuple[str, ...], limit: int) -> list[dict]:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    fts_query = tokenize_query(query)
    if not fts_query:
        conn.close()
        return []
    placeholders = ",".join("?" for _ in card_types)
    sql = f"""
        SELECT c.card_type, c.card_id, c.title, c.metadata_json,
               bm25(cards_fts, 10.0, 8.0, 5.0, 2.0) AS rank
        FROM cards_fts f
        JOIN cards c ON c.rowid = f.rowid
        WHERE cards_fts MATCH ?
          AND c.card_type IN ({placeholders})
        ORDER BY rank
        LIMIT ?
    """
    try:
        rows = conn.execute(sql, (fts_query, *card_types, limit * 20)).fetchall()
    finally:
        conn.close()
    results: list[dict] = []
    for row in rows:
        metadata = json.loads(row["metadata_json"])
        results.append(
            {
                "card_type": row["card_type"],
                "card_id": row["card_id"],
                "score": round((-float(row["rank"])) + score_bonus(query, metadata), 3),
                "metadata": metadata,
            }
        )
    results.sort(key=lambda item: item["score"], reverse=True)
    return results[: limit * 20]


def expand_related(base_rows: list[dict], all_rows: dict[str, dict], relation_key: str, limit: int) -> list[dict]:
    picked: list[dict] = []
    seen: set[str] = set()
    for row in base_rows:
        for related_id in row["metadata"].get(relation_key, []):
            if related_id in seen or related_id not in all_rows:
                continue
            seen.add(related_id)
            picked.append({"score": row["score"], **all_rows[related_id]})
            if len(picked) >= limit:
                return picked
    return picked


def format_item(item: dict, id_key: str) -> dict:
    title = item.get("title") or item.get("name") or item[id_key]
    return {
        id_key: item[id_key],
        "title": title,
        "score": item.get("score"),
        "summary": item.get("summary") or item.get("intent") or item.get("scenario"),
        "paths": item.get("source_paths", []),
        "source": item.get("source"),
        "doc_kind": item.get("doc_kind"),
    }


def hits_to_grouped(hits: list[dict], section: str, id_key: str, limit: int) -> list[dict]:
    seen: set[str] = set()
    rows: list[dict] = []
    for hit in hits:
        row_id = hit["metadata"][id_key]
        if row_id in seen:
            continue
        seen.add(row_id)
        rows.append(format_item({**hit["metadata"], "score": hit["score"]}, id_key))
        if len(rows) >= limit:
            break
    return rows


def load_understanding(query: str, understanding_mode: str, understanding_payload: dict | None) -> dict:
    if understanding_mode == "host-agent":
        return understand_host_agent(query, understanding_payload or {})
    return understand(query)


def collect(
    index: dict,
    query: str,
    mode: str,
    limit: int,
    understanding_mode: str = "rule",
    understanding_payload: dict | None = None,
) -> dict:
    understanding = load_understanding(query, understanding_mode, understanding_payload)
    effective_mode = understanding["preferred_result"] if mode == "auto" else mode
    normalized = expand_query_for_understanding(query, index["aliases"], understanding)
    mixed_hits: dict[str, list[dict]] = {}
    for card_type in ("task", "api", "example", "doc"):
        base_hits = search_cards(index["db"], normalized, MODE_TYPES[card_type], limit)
        reranked = [
            {**hit, "score": rerank_score(understanding, hit, card_type)}
            for hit in base_hits
        ]
        reranked.sort(key=lambda item: item["score"], reverse=True)
        mixed_hits[card_type] = reranked

    grouped = {"tasks": [], "apis": [], "examples": [], "docs": []}
    if effective_mode == "task":
        task_hits = mixed_hits["task"]
        grouped["tasks"] = hits_to_grouped(task_hits, "tasks", "task_id", limit)
        grouped["apis"] = [format_item(item, "api_id") for item in expand_related(task_hits, index["apis"], "recommended_apis", limit)]
        grouped["examples"] = [format_item(item, "example_id") for item in expand_related(task_hits, index["examples"], "example_ids", limit)]
        api_fallback = hits_to_grouped(mixed_hits["api"], "apis", "api_id", limit)
        if len(grouped["apis"]) < limit:
            seen = {row["api_id"] for row in grouped["apis"]}
            grouped["apis"].extend([row for row in api_fallback if row["api_id"] not in seen][: limit - len(grouped["apis"])])
        grouped["docs"] = hits_to_grouped(mixed_hits["doc"], "docs", "doc_id", limit)
    elif effective_mode == "api":
        api_hits = mixed_hits["api"]
        grouped["apis"] = hits_to_grouped(api_hits, "apis", "api_id", limit)
        grouped["examples"] = [format_item(item, "example_id") for item in expand_related(api_hits, index["examples"], "example_ids", limit)]
        related_tasks = []
        for hit in api_hits:
            api_id = hit["metadata"]["api_id"]
            for task in index["tasks"].values():
                if api_id in task.get("recommended_apis", []) or api_id in task.get("optional_apis", []):
                    related_tasks.append({"score": hit["score"], **task})
        uniq_tasks: dict[str, dict] = {}
        for item in related_tasks:
            uniq_tasks.setdefault(item["task_id"], item)
        grouped["tasks"] = [format_item(item, "task_id") for item in list(uniq_tasks.values())[:limit]]
        task_fallback = hits_to_grouped(mixed_hits["task"], "tasks", "task_id", limit)
        if len(grouped["tasks"]) < limit:
            seen = {row["task_id"] for row in grouped["tasks"]}
            grouped["tasks"].extend([row for row in task_fallback if row["task_id"] not in seen][: limit - len(grouped["tasks"])])
        grouped["docs"] = hits_to_grouped(mixed_hits["doc"], "docs", "doc_id", limit)
    elif effective_mode == "doc":
        grouped["docs"] = hits_to_grouped(mixed_hits["doc"], "docs", "doc_id", limit)
        grouped["tasks"] = hits_to_grouped(mixed_hits["task"], "tasks", "task_id", limit)
        grouped["apis"] = hits_to_grouped(mixed_hits["api"], "apis", "api_id", limit)
        grouped["examples"] = hits_to_grouped(mixed_hits["example"], "examples", "example_id", limit)
    else:
        example_hits = mixed_hits["example"]
        grouped["examples"] = hits_to_grouped(example_hits, "examples", "example_id", limit)
        grouped["apis"] = [format_item(item, "api_id") for item in expand_related(example_hits, index["apis"], "related_apis", limit)]
        grouped["tasks"] = [format_item(item, "task_id") for item in expand_related(example_hits, index["tasks"], "related_tasks", limit)]
        task_fallback = hits_to_grouped(mixed_hits["task"], "tasks", "task_id", limit)
        api_fallback = hits_to_grouped(mixed_hits["api"], "apis", "api_id", limit)
        if len(grouped["tasks"]) < limit:
            seen = {row["task_id"] for row in grouped["tasks"]}
            grouped["tasks"].extend([row for row in task_fallback if row["task_id"] not in seen][: limit - len(grouped["tasks"])])
        if len(grouped["apis"]) < limit:
            seen = {row["api_id"] for row in grouped["apis"]}
            grouped["apis"].extend([row for row in api_fallback if row["api_id"] not in seen][: limit - len(grouped["apis"])])
        grouped["docs"] = hits_to_grouped(mixed_hits["doc"], "docs", "doc_id", limit)

    path_order = {
        "task": ("tasks", "apis", "examples", "docs"),
        "api": ("apis", "tasks", "examples", "docs"),
        "example": ("examples", "apis", "tasks", "docs"),
        "doc": ("docs", "tasks", "apis", "examples"),
    }[effective_mode]
    paths: list[str] = direct_paths_for_query(query)
    for key in path_order:
        for item in grouped[key]:
            for path in ordered_paths_for_query(item.get("paths", []), query):
                if path not in paths:
                    paths.append(path)
    return {
        "query": query,
        "mode": effective_mode,
        "understanding": understanding,
        "tasks": grouped["tasks"][:limit],
        "apis": grouped["apis"][:limit],
        "examples": grouped["examples"][:limit],
        "docs": grouped["docs"][:limit],
        "paths": paths[: limit * 4],
    }


def print_text(result: dict) -> None:
    print(f"query: {result['query']}")
    print(f"mode: {result['mode']}")
    for section in ("tasks", "apis", "examples", "docs"):
        items = result[section]
        if not items:
            continue
        print(f"\n[{section}]")
        for item in items:
            summary = item.get("summary") or ""
            print(f"- {item['title']} (score={item['score']})")
            if summary:
                print(f"  {summary}")
            for path in item.get("paths", [])[:3]:
                print(f"  path: {path}")
    if result["paths"]:
        print("\n[paths]")
        for path in result["paths"]:
            print(f"- {path}")


def top_titles_by_path(result: dict) -> dict[str, str]:
    titles: dict[str, str] = {}
    for section in ("tasks", "apis", "examples", "docs"):
        for item in result.get(section, []):
            title = str(item.get("title", ""))
            for path in item.get("paths", []):
                titles.setdefault(str(path), title)
    return titles


def write_search_event(
    index: dict,
    index_dir: Path,
    query: str,
    mode: str,
    limit: int,
    understanding_mode: str,
    result: dict | None,
    latency_ms: float,
    error: str = "",
) -> None:
    log_path = os.environ.get("DOC_SEARCH_LOG_PATH", "").strip()
    if not log_path:
        return

    paths = [str(path) for path in (result or {}).get("paths", [])[:limit]]
    titles_by_path = top_titles_by_path(result or {})
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "query": query,
        "mode": mode,
        "understanding_mode": understanding_mode,
        "index_dir": str(index_dir),
        "index_manifest_generated_at": index.get("manifest", {}).get("generated_at", ""),
        "limit": limit,
        "latency_ms": round(latency_ms, 2),
        "top_paths": paths,
        "top_titles": [titles_by_path.get(path, "") for path in paths],
        "result_count": len(paths),
        "error": error,
    }

    path = Path(log_path)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n")
    except OSError as exc:
        print(f"写入搜索日志失败: {exc}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(description="V3 本地结构化文档检索")
    parser.add_argument("query", help="搜索语句")
    parser.add_argument("--mode", choices=("auto", "task", "api", "example", "doc"), default="auto")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--json", action="store_true", help="输出结构化 JSON")
    parser.add_argument("--index-dir", default=str(DEFAULT_INDEX_DIR))
    parser.add_argument("--understanding-mode", choices=("rule", "host-agent"), default="rule")
    parser.add_argument("--understanding-json", default="", help="host-agent 模式下传入的理解结果 JSON")
    args = parser.parse_args()

    utf8_stdio()
    try:
        index = load_index(Path(args.index_dir))
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)

    payload = json.loads(args.understanding_json) if args.understanding_json else None
    started = time.perf_counter()
    try:
        result = collect(
            index,
            args.query,
            args.mode,
            args.limit,
            understanding_mode=args.understanding_mode,
            understanding_payload=payload,
        )
    except Exception as exc:  # noqa: BLE001 - CLI 需要记录失败后继续按原行为退出。
        write_search_event(
            index,
            Path(args.index_dir),
            args.query,
            args.mode,
            args.limit,
            args.understanding_mode,
            None,
            (time.perf_counter() - started) * 1000,
            f"{type(exc).__name__}: {exc}",
        )
        raise
    write_search_event(
        index,
        Path(args.index_dir),
        args.query,
        args.mode,
        args.limit,
        args.understanding_mode,
        result,
        (time.perf_counter() - started) * 1000,
    )
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_text(result)


if __name__ == "__main__":
    main()
