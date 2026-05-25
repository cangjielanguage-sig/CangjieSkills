#!/usr/bin/env python3
"""查询理解器，支持规则理解结果归一化。"""

from __future__ import annotations

import json
import re
from typing import Any


OBJECT_HINTS = {
    "list": ["list", "列表"],
    "grid": ["grid", "网格"],
    "image": ["image", "图片"],
    "refresh": ["refresh", "刷新"],
    "scroll": ["scroll", "滚动"],
    "lazyforeach": ["lazyforeach"],
    "flex": ["flex", "弹性布局"],
    "row": ["row", "行布局"],
    "column": ["column", "列布局"],
    "stack": ["stack", "层叠布局"],
    "slider": ["slider", "button", "按钮", "滑动条"],
    "dialog": ["dialog", "alertdialog", "弹窗"],
    "navigation": ["navigation", "导航"],
    "router": ["router", "路由"],
    "web": ["web", "webview", "loadurl", "user-agent", "h5", "cookie", "devtools", "pdf"],
    "websocket": ["websocket", "upgradefromclient"],
    "http": ["http", "网络请求", "httprequest", "流式响应", "证书锁定", "证书校验"],
    "network_connection": ["网络连接", "连接状态", "netconnection", "connection"],
    "file_transfer": ["上传下载", "上传", "下载", "upload", "download"],
    "appstorage": ["appstorage", "状态管理"],
    "localstorage": ["localstorage"],
    "arkui_state": ["state", "状态变量"],
    "textinput": ["textinput", "输入框"],
    "textarea": ["textarea", "多行输入"],
    "search": ["search", "搜索框"],
    "checkbox": ["checkbox", "多选"],
    "radio": ["radio", "单选"],
    "toggle": ["toggle", "开关"],
    "rating": ["rating", "评分"],
    "select": ["select", "下拉选择"],
    "progress": ["progress", "进度条"],
    "badge": ["badge", "角标"],
    "sidebarcontainer": ["sidebarcontainer", "侧边栏"],
    "relativecontainer": ["relativecontainer", "相对布局"],
    "gridrow": ["gridrow", "gridcol", "栅格"],
    "patternlock": ["patternlock", "手势密码"],
    "richeditor": ["richeditor", "富文本"],
    "navdestination": ["navdestination"],
    "canvas": ["canvas", "自定义绘制"],
    "tabs": ["tabs", "标签页"],
    "datepicker": ["datepicker", "日期选择"],
    "popup": ["popup", "气泡提示"],
    "swiper": ["swiper", "轮播"],
    "aes": ["aes", "加密"],
    "bluetooth": ["bluetooth", "蓝牙"],
    "ability": ["uiability", "ability", "startability", "startabilityforresult", "want", "abilitycontext", "abilitystage"],
    "preferences": ["preferences", "getpreferences", "用户首选项", "首选项", "用户设置"],
    "access_token": ["requestpermissionsfromuser", "permissionrequestresult", "module.json5", "声明权限", "权限申请", "申请权限", "用户授权", "授权"],
    "location": ["geolocationmanager", "getcurrentlocation", "定位", "经纬度", "位置服务"],
    "sensor": ["sensor", "传感器", "gyroscope", "陀螺仪"],
    "photo_access": ["photoaccesshelper", "相册", "图片列表", "fetchresult"],
    "camera": ["camera", "cameramanager", "相机", "拍照", "预览流", "录像", "相机设备"],
    "distributed_storage": ["分布式 kv", "分布式kv", "distributed_kv_store", "singlekvstore", "kvmanager", "kvstore", "跨设备同步"],
    "notification": ["notification", "通知", "提醒"],
    "common_event": ["commonevent", "公共事件", "系统事件"],
    "background_task": ["backgroundtask", "后台任务", "后台运行", "长时任务"],
    "hilog": ["hilog", "日志", "domain", "tag"],
    "hiappevent": ["hiappevent", "应用事件", "事件上报", "冻屏事件", "崩溃事件", "观察者", "埋点", "上报埋点"],
    "request_agent": ["request-agent", "request agent", "上传下载任务", "下载任务", "请求代理", "formitem", "filespec", "taskinfo", "saveas"],
    "file_picker": ["filepicker", "picker", "选择文件", "保存文件", "文件选择"],
    "pasteboard": ["pasteboard", "clipboard", "剪贴板"],
    "window": ["window", "窗口", "沉浸式", "状态栏", "导航栏"],
    "display": ["display", "屏幕", "折叠屏", "方向"],
    "prompt_action": ["promptaction", "toast", "菜单", "actionmenu", "showtoast", "showactionmenu", "提示"],
    "ipc": ["ipc", "rpc", "parcelable", "跨进程"],
    "telephony": ["telephony", "callstate", "拨打电话", "通话"],
    "graphics": ["color_space", "colorspacemanager", "色彩管理", "arkgraphics2d"],
    "huks": ["huks", "密钥库", "密钥", "generatekeyitem"],
    "arkts_interop": ["arkts", "互操作", "import", "找不到模块"],
    "animation": ["animation", "动画"],
    "std_crypto": ["std.crypto", "cipher"],
    "std_net": ["std.net", "socket"],
    "std_fs": ["std.fs", "文件操作", "文件", "读写文件"],
    "relational_store": ["relationalstore", "rdb", "关系型数据库", "数据库", "rdbstore", "建表", "sql"],
    "validation_error": ["参数校验", "参数异常", "businessexception"],
    "type_error": ["类型不匹配", "valuetype", "contenttype"],
    "window_error": ["窗口操作", "window"],
    "permission_error": ["权限被拒绝", "permission"],
    "memory_error": ["内存不足", "oom", "canvasrenderingcontext2d"],
    "compile_error": ["找不到符号", "builder", "builderparam", "编译错误"],
    "resource_file": ["rawfile", "resources/rawfile", "资源文件", "应用沙箱", "沙箱文件", "应用文件访问", "文件访问", "fileuri"],
    "device_info": ["设备信息", "device_info", "电池", "电量", "系统时间", "settings", "系统设置"],
    "custom_component": ["自定义组件"],
    "click": ["点击事件", "onclick", "点击"],
}

PROPERTY_TOKENS = {
    "objectfit",
    "alignitems",
    "justifycontent",
    "fontsize",
    "fontweight",
    "backgroundcolor",
    "borderradius",
    "placeholdercolor",
    "src",
    "headers",
    "loadurl",
    "user-agent",
    "rawfile",
    "fileuri",
    "value",
    "min",
    "max",
    "step",
    "startability",
    "startabilityforresult",
    "abilitycontext",
    "want",
    "getpreferences",
    "preferences",
    "getrdbstore",
    "rdbstore",
    "relationalstore",
    "executesql",
    "querysql",
    "has",
    "requestpermissionsfromuser",
    "permissionrequestresult",
    "websocket",
    "upgradefromclient",
    "requestinstream",
    "certificatepinning",
    "singlekvstore",
    "kvmanager",
    "commoneventpublishdata",
    "commoneventsubscribeinfo",
    "getcurrentlocation",
    "geolocationmanager",
    "photoaccesshelper",
    "fetchresult",
    "registerjavascriptproxy",
    "runjavascript",
    "hascookie",
    "storewebarchive",
    "setwebdebuggingaccess",
    "darkmode",
    "lazyforeach",
    "pagetransition",
    "localstorage",
    "tabs",
    "select",
    "datepicker",
    "popup",
    "cameramanager",
    "createpreviewoutput",
    "photooutput",
    "startcapture",
    "notificationrequest",
    "publish",
    "requestenable",
    "backgroundtask",
    "hilog",
    "filepicker",
    "pasteboard",
    "getwindowstage",
    "setwindowlayoutfullscreen",
    "getdefaultdisplay",
    "showtoast",
    "showactionmenu",
    "parcelable",
    "callstate",
    "avfiledescriptor",
    "colorspacemanager",
    "generatekeyitem",
    "init_session",
    "updatesession",
    "finishsession",
    "jspromisecapability",
    "grantstatus",
    "textarea",
    "search",
    "checkbox",
    "radio",
    "toggle",
    "rating",
    "select",
    "progress",
    "badge",
    "sidebarcontainer",
    "relativecontainer",
    "gridrow",
    "gridcol",
    "patternlock",
    "richeditor",
    "navdestination",
    "canvas",
    "formitem",
    "filespec",
    "taskinfo",
    "saveas",
    "hiappevent",
    "hitracemeter",
    "watcher",
    "appEventFilter",
    "setuserid",
    "cleardata",
    "datasharepredicates",
    "orderbyasc",
    "eventvaluetype",
    "eventtype",
    "eventcallbacktype",
    "taskinfo",
    "network",
    "progress",
    "ble",
    "hfp",
    "geometrytransition",
    "sharedtransitionoptions",
}

EXPLICIT_API_HINT_WORDS = (
    "属性",
    "事件",
    "api",
    "接口",
    "方法",
    "枚举",
    "参数",
    "返回值",
)

EXPLICIT_API_PHRASES = (
    "组件属性",
    "组件事件",
    "通用属性",
    "通用事件",
)

PROPERTY_QUERY_WORDS = (
    "怎么配",
    "怎么设",
    "怎么设置",
    "如何设置",
    "如何配置",
    "如何使用",
    "怎么用",
    "怎么传",
    "怎么拿",
    "设置",
    "返回",
    "返回结果",
    "取值",
    "含义",
)

TROUBLESHOOTING_WORDS = (
    "错误",
    "失败",
    "异常",
    "denied",
    "找不到符号",
    "超时",
    "报错",
    "排查",
    "路径错",
)

EXPLORATION_WORDS = (
    "有哪些",
    "概览",
    "相关文档",
    "相关 api",
    "相关 api 有哪些",
    "overview",
)

EXAMPLE_WORDS = (
    "示例",
    "示例代码",
    "demo",
    "example",
    "怎么写",
)

QUICKSTART_WORDS = ("快速开始", "第一个")
GENERIC_HOWTO_WORDS = ("如何", "怎么", "怎样", "想", "需要")
GENERIC_ACTION_WORDS = (
    "创建",
    "添加",
    "实现",
    "处理",
    "封装",
    "使用",
    "绑定",
    "存储",
    "读取",
    "保存",
    "查询",
    "申请",
    "声明",
    "跳转",
    "加载",
    "执行",
    "共享",
)


def extract_identifiers(query: str) -> list[str]:
    tokens = re.findall(r"\b[A-Za-z_][A-Za-z0-9_.-]*\b", query)
    return list(dict.fromkeys(token for token in tokens if len(token) >= 2))


def has_property_pattern(query: str) -> bool:
    lowered = query.lower()
    identifiers = extract_identifiers(query)
    if any(word in lowered for word in EXPLICIT_API_HINT_WORDS):
        return True
    if any(phrase in lowered for phrase in EXPLICIT_API_PHRASES):
        return True
    if any(word in lowered for word in PROPERTY_QUERY_WORDS):
        if any(re.search(r"[a-z][A-Z]", token) for token in identifiers):
            return True
        if any(token.lower() in PROPERTY_TOKENS for token in identifiers):
            return True
    if re.search(r"[\u4e00-\u9fff]+\s*的\s*[A-Za-z_][A-Za-z0-9_]*", query):
        return True
    if any(token.lower() in PROPERTY_TOKENS for token in identifiers):
        return True
    return False


def has_generic_howto_pattern(query: str) -> bool:
    lowered = query.lower()
    return any(word in lowered for word in GENERIC_HOWTO_WORDS) and any(
        word in lowered for word in GENERIC_ACTION_WORDS
    )


def has_explicit_api_identifier(query: str) -> bool:
    identifiers = extract_identifiers(query)
    return any(
        re.search(r"[a-z][A-Z]", token) or token.lower() in PROPERTY_TOKENS
        for token in identifiers
    )


def detect_objects(query: str) -> list[str]:
    lowered = query.lower()
    objects = [
        key
        for key, hints in OBJECT_HINTS.items()
        if any(hint in lowered for hint in hints)
    ]
    if any(phrase in lowered for phrase in ("怎么定位", "问题定位", "错误定位", "出问题怎么定位")):
        objects = [item for item in objects if item != "location"]
    identifiers = extract_identifiers(query)
    if any(token.lower() == "objectfit" for token in identifiers):
        objects.append("image")
    if any(token.lower() in {"alignitems", "justifycontent"} for token in identifiers):
        objects.extend(["column", "row", "flex"])
    if any(token.lower() in {"min", "max", "step"} for token in identifiers):
        objects.append("slider")
    if "权限" in lowered:
        objects.append("access_token")
    if any(word in lowered for word in ("保存用户设置", "读取用户设置", "key 不存在", "键不存在")):
        objects.append("preferences")
    if any(word in lowered for word in ("建表", "查询数据", "执行建表", "执行 sql", "执行sql")):
        objects.append("relational_store")
    if any(word in lowered for word in ("分布式 kv", "分布式kv", "singlekvstore", "kvmanager", "kvstore", "跨设备同步")):
        objects = [item for item in objects if item != "relational_store"]
        objects.append("distributed_storage")
    if any(word in lowered for word in ("相机设备", "支持的相机设备")):
        objects = [item for item in objects if item != "device_info"]
        objects.append("camera")
    if any(word in lowered for word in ("应用文件访问", "文件访问权限")):
        objects.append("resource_file")
    if "系统事件" in lowered:
        objects.append("common_event")
    if "hilog" in lowered:
        objects.append("hilog")
    if "生命周期" in lowered and "ability" in lowered:
        objects.append("ability")
    return list(dict.fromkeys(objects or ["general"]))


def detect_intent_type(query: str) -> str:
    lowered = query.lower()
    if any(word in lowered for word in TROUBLESHOOTING_WORDS):
        return "troubleshooting"
    if any(word in lowered for word in EXPLORATION_WORDS):
        return "exploration"
    if any(word in lowered for word in EXAMPLE_WORDS):
        return "example_lookup"
    if has_explicit_api_identifier(query) and any(
        word in lowered
        for word in ("怎么", "如何", "参数", "返回", "用", "设置", "拿", "传", "配置")
    ):
        return "api_lookup"
    if has_generic_howto_pattern(query) and not extract_identifiers(query):
        return "build_feature"
    if has_property_pattern(query):
        return "api_lookup"
    if any(word in lowered for word in QUICKSTART_WORDS):
        return "quickstart"
    return "build_feature"


def detect_stage(intent_type: str) -> str:
    mapping = {
        "troubleshooting": "debug",
        "exploration": "discovery",
        "example_lookup": "example",
        "api_lookup": "reference",
        "quickstart": "quickstart",
        "build_feature": "implementation",
    }
    return mapping[intent_type]


def preferred_result(intent_type: str) -> str:
    mapping = {
        "troubleshooting": "task",
        "exploration": "api",
        "example_lookup": "example",
        "api_lookup": "api",
        "quickstart": "task",
        "build_feature": "task",
    }
    return mapping[intent_type]


def preferred_result_for_query(query: str, intent_type: str) -> str:
    lowered = query.lower()
    component_api_tokens = (
        "textarea",
        "搜索框",
        "checkbox",
        "radio",
        "toggle",
        "rating",
        "select",
        "progress",
        "badge",
        "sidebarcontainer",
        "relativecontainer",
        "gridrow",
        "gridcol",
        "patternlock",
        "richeditor",
        "navdestination",
        "canvas",
        "单选",
        "多选",
        "下拉选择",
        "进度条",
        "角标",
        "侧边栏",
        "相对布局",
        "栅格",
        "手势密码",
        "富文本",
        "request-agent",
        "formitem",
        "filespec",
        "taskinfo",
        "saveas",
        "hiappevent",
        "hitracemeter",
        "setuserid",
        "cleardata",
        "datasharepredicates",
        "eventcallbacktype",
        "ble",
        "hfp",
        "geometrytransition",
        "sharedtransitionoptions",
    )
    if any(token in lowered for token in component_api_tokens):
        return "api"
    if "rawfile" in lowered and any(token in lowered for token in ("web", "webview", "网页")):
        return "doc"
    if "module.json5" in lowered and any(token in lowered for token in ("权限", "permission")):
        return "doc"
    if "rawfile" in lowered and any(token in lowered for token in ("路径无效", "排查", "getrawfd")):
        return "api"
    if "fileuri" in lowered and any(token in lowered for token in ("路径无效", "排查")):
        return "api"
    if "传感器" in lowered and any(token in lowered for token in ("回调", "不触发", "排查")):
        return "api"
    if any(token in lowered for token in ("流式响应", "证书锁定", "证书校验", "网络连接状态", "连接状态怎么监听")):
        return "doc"
    if any(token in lowered for token in ("错误码", "2300055", "1900011", "17100001", "超时")) and any(token in lowered for token in ("http", "rpc", "相机", "camera", "定位", "getcurrentlocation", "上传下载", "web", "webview")):
        return "doc"
    if "telephony" in lowered and "错误码" in lowered:
        return "doc"
    if "hilog" in lowered:
        return "api"
    if "grantstatus" in lowered:
        return "api"
    if any(token in lowered for token in ("电池", "电量", "系统时间", "settings", "系统设置")):
        return "doc"
    if "display" in lowered and any(token in lowered for token in ("屏幕", "宽高", "方向")):
        return "doc"
    if any(token in lowered for token in ("previewoutput", "videooutput")):
        return "doc"
    if "abilitylifecyclestate" in lowered or ("ability" in lowered and "生命周期状态" in lowered):
        return "api"
    if "uiabilitycontext" in lowered and any(token in lowered for token in ("测试", "哪些", "能做", "生命周期")):
        return "doc"
    if "localstorage" in lowered and "uiability" in lowered:
        return "doc"
    if "网络请求" in lowered and "权限" in lowered:
        return "doc"
    if "uiability" in lowered and "生命周期" in lowered:
        return "api"
    if any(token in lowered for token in ("相机设备", "支持的相机设备")):
        return "api"
    if "应用文件访问" in lowered and "权限错误" in lowered:
        return "doc"
    if any(token in lowered for token in ("分布式 kv", "分布式kv", "singlekvstore", "kvmanager", "kvstore", "跨设备同步")):
        return "api"
    if any(token in lowered for token in ("公共事件", "commonevent")):
        return "api" if intent_type == "api_lookup" else "doc"
    if "系统事件" in lowered:
        return "api"
    if any(token in lowered for token in ("上传下载", "上传", "下载")) and any(token in lowered for token in ("任务", "文件", "错误码", "失败", "应用目录")):
        return "doc"
    if any(token in lowered for token in ("tabs", "tabcontent", "标签页")):
        return "doc"
    if any(token in lowered for token in ("popup", "气泡提示")):
        return "doc"
    if any(token in lowered for token in ("state 状态", "状态变化", "lazyforeach", "foreach", "长列表卡顿")):
        return "doc"
    if "state" in lowered and "build" in lowered:
        return "doc"
    if any(token in lowered for token in ("devtools", "pdf", "安全区域", "safe area", "safe-area", "secure shield")) and any(token in lowered for token in ("webview", "web")):
        return "doc"
    if any(token in lowered for token in ("imagesource", "pixelmap")) and any(token in lowered for token in ("解码", "编码", "图片")):
        return "doc"
    if any(token in lowered for token in ("图片编码", "jpeg", "imagepacker")):
        return "doc"
    if any(token in lowered for token in ("相册", "photoaccesshelper", "fetchresult")):
        return "api"
    if any(token in lowered for token in ("应用沙箱", "沙箱文件", "应用文件")):
        return "doc"
    if any(token in lowered for token in ("rpc", "ipc", "parcelable", "远程调用", "跨进程")):
        return "api"
    if "相机" in lowered and any(token in lowered for token in ("黑屏", "预览", "错误码", "失败")):
        return "doc"
    if any(token in lowered for token in ("huks", "密钥库", "生成密钥", "密钥不存在", "加解密")):
        return "doc"
    if "arkts" in lowered and any(token in lowered for token in ("promise", "jsvalue", "互操作", "import")):
        return "api" if intent_type == "api_lookup" else "doc"
    if any(token in lowered for token in ("定位权限", "locationkit", "定位返回", "空位置")):
        return "doc"
    if any(token in lowered for token in ("media 错误码", "无可用资源")):
        return "doc"
    if any(token in lowered for token in ("toast", "actionmenu", "promptaction", "气泡提示", "菜单")):
        return "api" if intent_type == "api_lookup" else "doc"
    if any(token in lowered for token in ("定位", "geolocation", "getcurrentlocation", "传感器", "sensor", "gyroscope", "陀螺仪")):
        return "api" if intent_type in {"api_lookup", "build_feature"} else preferred_result(intent_type)
    if any(token in lowered for token in ("requestpermissionsfromuser", "getpreferences", "rdbstore", "relationalstore", "executesql", "querysql", "hascookie", "runjavascript", "registerjavascriptproxy", "storewebarchive", "darkmode")):
        return "api"
    if "权限" in lowered and any(token in lowered for token in ("申请", "运行时", "授权", "声明")):
        return "doc" if "声明" in lowered else "api"
    if "preferences" in lowered or "用户首选项" in lowered:
        return "api"
    if any(token in lowered for token in ("webview", "web")) and any(token in lowered for token in ("cookie", "javascript", "js", "深色模式", "离线包", "调试", "devtools")):
        return "api"
    return preferred_result(intent_type)


def extract_constraints(query: str) -> list[str]:
    lowered = query.lower()
    hints = {
        "performance": ["性能", "卡顿", "慢", "长列表"],
        "permission": ["权限"],
        "debug": ["报错", "异常", "失败"],
        "ui": ["页面", "组件", "布局"],
    }
    return [name for name, words in hints.items() if any(word in lowered for word in words)]


def search_strategy(preferred: str, intent_type: str) -> dict[str, Any]:
    followups: list[str] = []
    if preferred == "task":
        followups = ["api"]
        if intent_type in {"build_feature", "example_lookup"}:
            followups.append("example")
    elif preferred == "api":
        followups = ["task"]
        if intent_type in {"api_lookup", "example_lookup"}:
            followups.append("example")
    else:
        followups = ["api", "task"]
    return {
        "primary_mode": preferred,
        "followup_modes": followups,
        "should_expand_examples": preferred != "example" and intent_type in {"build_feature", "api_lookup", "example_lookup"},
    }


def normalize_understanding(payload: dict[str, Any], mode: str = "rule") -> dict[str, Any]:
    raw_query = str(payload.get("raw_query") or payload.get("query") or "")
    normalized_query = str(payload.get("normalized_query") or re.sub(r"\s+", " ", raw_query).strip())
    intent_type = str(payload.get("intent_type") or "build_feature")
    preferred = str(payload.get("preferred_result") or preferred_result(intent_type))
    primary_objects = payload.get("primary_objects")
    if not isinstance(primary_objects, list) or not primary_objects:
        primary_objects = ["general"]
    identifiers = payload.get("identifiers")
    if not isinstance(identifiers, list):
        identifiers = []
    constraints = payload.get("constraints")
    if not isinstance(constraints, list):
        constraints = extract_constraints(raw_query)
    stage = str(payload.get("stage") or detect_stage(intent_type))
    strategy = payload.get("search_strategy")
    if not isinstance(strategy, dict):
        strategy = search_strategy(preferred, intent_type)
    return {
        "mode": mode,
        "raw_query": raw_query,
        "normalized_query": normalized_query,
        "intent_type": intent_type,
        "primary_objects": list(dict.fromkeys(str(item) for item in primary_objects if str(item).strip())) or ["general"],
        "identifiers": identifiers,
        "constraints": constraints,
        "stage": stage,
        "preferred_result": preferred,
        "search_strategy": {
            "primary_mode": str(strategy.get("primary_mode") or preferred),
            "followup_modes": [
                str(item) for item in strategy.get("followup_modes", [])
                if str(item) in {"task", "api", "example"}
            ],
            "should_expand_examples": bool(strategy.get("should_expand_examples", False)),
        },
    }


def understand(query: str) -> dict[str, Any]:
    intent_type = detect_intent_type(query)
    identifiers = extract_identifiers(query)
    preferred = preferred_result_for_query(query, intent_type)
    return normalize_understanding(
        {
            "raw_query": query,
            "normalized_query": re.sub(r"\s+", " ", query).strip(),
            "intent_type": intent_type,
            "primary_objects": detect_objects(query),
            "identifiers": identifiers,
            "constraints": extract_constraints(query),
            "stage": detect_stage(intent_type),
            "preferred_result": preferred,
            "search_strategy": search_strategy(preferred, intent_type),
        },
        mode="rule",
    )


def understand_host_agent(query: str, payload: dict[str, Any]) -> dict[str, Any]:
    merged = dict(payload)
    merged.setdefault("raw_query", query)
    merged.setdefault("normalized_query", re.sub(r"\s+", " ", query).strip())
    return normalize_understanding(merged, mode="host-agent")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="规则版查询理解")
    parser.add_argument("query")
    parser.add_argument("--mode", choices=("rule", "host-agent"), default="rule")
    parser.add_argument("--payload", default="", help="host-agent 模式下的 JSON 字符串")
    args = parser.parse_args()
    if args.mode == "host-agent":
        payload = json.loads(args.payload) if args.payload else {}
        result = understand_host_agent(args.query, payload)
    else:
        result = understand(args.query)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
