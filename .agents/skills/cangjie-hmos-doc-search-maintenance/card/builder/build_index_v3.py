#!/usr/bin/env python3
"""V3 本地结构化索引构建脚本，支持 rule / rule+llm 两种模式。"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock
from typing import Any


BUILDER_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = BUILDER_DIR.parent
SKILLS_DIR = MAINTENANCE_DIR.parent.parent
DOC_SEARCH_DIR = SKILLS_DIR / "cangjie-hmos-doc-search"
DOC_CARD_DIR = DOC_SEARCH_DIR / "doc-card"
DOCS_DIR = DOC_SEARCH_DIR / "docs"
EVALS_DIR = DOC_CARD_DIR / "evals"
DEFAULT_INDEX_DIR = DOC_CARD_DIR / "index"
DOC_SOURCES = ("harmonyos-6.0.2-15k", "lang-features", "std", "stdx", "tools")
EXAMPLE_HINTS = ("示例", "example", "demo")
NOISE_HEADINGS = {"目录", "概述", "overview", "quick navigation"}
PROMPT_VERSION = "v1"
LLM_RETRYABLE_CODES = {429, 500, 502, 503, 504}
MAX_EVIDENCE_DOCS = int(os.environ.get("LLM_MAX_EVIDENCE_DOCS", "4"))
MAX_EVIDENCE_CHARS = int(os.environ.get("LLM_MAX_EVIDENCE_CHARS", "1800"))
DEFAULT_LLM_BATCH_SIZE = 6
DEFAULT_LLM_CONCURRENCY = int(os.environ.get("LLM_CONCURRENCY", "1"))
DEFAULT_LLM_CARD_TYPES = ("task", "api", "example", "doc")
EVAL_QUERY_CATEGORIES = ("exact", "natural", "semi-structured", "error-driven", "exploration")

HIGH_VALUE_API_MAP = {
    "image": {
        "api_id": "arkui.image",
        "name": "Image",
        "aliases": ["图片", "图片组件", "图像", "Image 组件"],
        "path_keywords": [
            "cj-image-video-image",
            "cj-image-video-image/Image",
            "cj-graphics-display/显示图片Image",
        ],
        "summary": "用于显示本地、网络或资源图片的基础图像组件。",
        "related_apis": [],
    },
    "list": {
        "api_id": "arkui.list",
        "name": "List",
        "aliases": ["滑动列表", "列表", "List 组件"],
        "path_keywords": [
            "cj-layout-development-create-list/创建列表List",
            "cj-scroll-swipe-list/List/",
            "cj-scroll-swipe-list/List/.overview.md",
        ],
        "summary": "展示连续、多行同类数据的可滚动容器组件。",
        "related_apis": ["arkui.list_item", "arkui.list_item_group", "arkui.lazyforeach", "arkui.scroll", "arkui.refresh"],
    },
    "list_item": {
        "api_id": "arkui.list_item",
        "name": "ListItem",
        "aliases": ["列表项", "List 列表项"],
        "path_keywords": ["cj-scroll-swipe-listitem/ListItem", "响应列表项侧滑", "创建列表List/布局与约束"],
        "summary": "List 的子组件，用于承载单个列表项视图。",
        "related_apis": ["arkui.list", "arkui.list_item_group"],
    },
    "list_item_group": {
        "api_id": "arkui.list_item_group",
        "name": "ListItemGroup",
        "aliases": ["分组列表", "列表分组", "List 分组"],
        "path_keywords": ["cj-scroll-swipe-listgroup/ListItemGroup", "支持分组列表"],
        "summary": "List 的分组容器，用于构建带组头或分段结构的列表。",
        "related_apis": ["arkui.list", "arkui.list_item"],
    },
    "grid": {
        "api_id": "arkui.grid",
        "name": "Grid",
        "aliases": ["网格", "网格布局", "Grid 组件"],
        "path_keywords": [
            "cj-scroll-swipe-grid",
            "cj-scroll-swipe-grid/Grid",
        ],
        "summary": "用于按网格方式展示内容的可滚动布局容器，支持分行分列与模板配置。",
        "related_apis": ["arkui.grid_item", "arkui.scroll", "arkui.lazyforeach"],
    },
    "grid_item": {
        "api_id": "arkui.grid_item",
        "name": "GridItem",
        "aliases": ["网格项", "Grid 子项", "GridItem 组件"],
        "path_keywords": [
            "cj-scroll-swipe-griditem",
            "cj-scroll-swipe-griditem/GridItem",
        ],
        "summary": "Grid 的子组件，用于定义单个网格单元的位置和内容。",
        "related_apis": ["arkui.grid"],
    },
    "scroll": {
        "api_id": "arkui.scroll",
        "name": "Scroll",
        "aliases": ["滚动容器", "滚动组件", "Scroll 组件"],
        "path_keywords": ["cj-scroll-swipe-scroll/Scroll/", "滚动组件通用API"],
        "summary": "提供通用滚动能力的容器组件，可用于自定义滚动布局和嵌套滚动。",
        "related_apis": ["arkui.list", "arkui.refresh"],
    },
    "refresh": {
        "api_id": "arkui.refresh",
        "name": "Refresh",
        "aliases": ["下拉刷新", "刷新组件", "Refresh 组件"],
        "path_keywords": ["cj-scroll-swipe-refresh/Refresh", "enum_RefreshStatus"],
        "summary": "为列表或滚动容器提供下拉刷新交互能力。",
        "related_apis": ["arkui.list", "arkui.scroll"],
    },
    "lazyforeach": {
        "api_id": "arkui.lazyforeach",
        "name": "LazyForEach",
        "aliases": ["懒加载列表", "长列表", "LazyForEach 懒加载"],
        "path_keywords": ["cj-rendering-control-lazyforeach/LazyForEach数据懒加载"],
        "summary": "用于长列表场景的懒加载循环渲染能力。",
        "related_apis": ["arkui.list", "arkui.foreach"],
    },
    "foreach": {
        "api_id": "arkui.foreach",
        "name": "ForEach",
        "aliases": ["循环渲染", "ForEach 渲染"],
        "path_keywords": ["cj-rendering-control-foreach", "循环渲染"],
        "summary": "用于列表和布局中的常规循环渲染能力。",
        "related_apis": ["arkui.list", "arkui.lazyforeach"],
    },
    "flex": {
        "api_id": "arkui.flex",
        "name": "Flex",
        "aliases": ["弹性布局", "Flex 布局", "Flex 组件"],
        "path_keywords": [
            "cj-layout-development-flex-layout",
            "cj-row-column-stack-flex/Flex",
            "cj-universal-attribute-flexlayout",
        ],
        "summary": "提供可伸缩和多行排列能力的弹性布局容器，适合响应式和比例分配场景。",
        "related_apis": ["arkui.row", "arkui.column"],
    },
    "stack": {
        "api_id": "arkui.stack",
        "name": "Stack",
        "aliases": ["层叠布局", "Stack 布局", "堆叠布局"],
        "path_keywords": [
            "cj-layout-development-stack-layout",
            "层叠布局Stack",
        ],
        "summary": "用于将多个子元素按层叠方式放置在同一空间中的布局容器。",
        "related_apis": [],
    },
    "row": {
        "api_id": "arkui.row",
        "name": "Row",
        "aliases": ["行布局", "Row 布局", "水平布局"],
        "path_keywords": [
            "cj-layout-development-linear",
            "线性布局RowColumn",
            "Row容器内子元素在水平方向上的排列",
        ],
        "summary": "沿水平方向排列子元素的线性布局容器。",
        "related_apis": ["arkui.column", "arkui.flex"],
    },
    "column": {
        "api_id": "arkui.column",
        "name": "Column",
        "aliases": ["列布局", "Column 布局", "垂直布局"],
        "path_keywords": [
            "cj-layout-development-linear",
            "线性布局RowColumn",
            "Column容器内子元素在垂直方向上的排列",
        ],
        "summary": "沿垂直方向排列子元素的线性布局容器。",
        "related_apis": ["arkui.row", "arkui.flex"],
    },
    "slider": {
        "api_id": "arkui.slider",
        "name": "Slider",
        "aliases": ["滑动条", "进度滑块", "Slider 组件"],
        "path_keywords": [
            "cj-button-picker-slider",
            "cj-button-picker-slider/Slider",
        ],
        "summary": "用于在指定范围内拖动选择数值的滑动条组件。",
        "related_apis": [],
    },
    "alert_dialog": {
        "api_id": "arkui.alert_dialog",
        "name": "AlertDialog",
        "aliases": ["警告弹窗", "提示弹窗", "AlertDialog 弹窗"],
        "path_keywords": [
            "cj-dialog-alertdialog",
            "警告弹窗AlertDialog",
        ],
        "summary": "用于展示确认、提示或危险操作确认的警告弹窗能力。",
        "related_apis": ["arkui.ui_context"],
        "module": "kit.ArkUI",
        "kind": "dialog",
    },
    "navigation": {
        "api_id": "arkui.navigation",
        "name": "Navigation",
        "aliases": ["组件导航", "导航容器", "Navigation 导航"],
        "path_keywords": [
            "cj-navigation-navigation",
            "cj-navigation-switching-navigation",
            "cj-navigation-switching-navigation/Navigation",
        ],
        "summary": "用于构建分栏、堆栈和页面切换式导航结构的组件导航容器。",
        "related_apis": ["arkui.nav_path_stack", "arkui.router"],
    },
    "router": {
        "api_id": "arkui.router",
        "name": "Router",
        "aliases": ["路由", "页面路由", "Router 路由"],
        "path_keywords": [
            "cj-apis-uicontext-router",
            "cj-apis-uicontext-router/Router",
            "cj-navigation-introduction",
        ],
        "summary": "用于执行页面跳转、返回和路由参数管理的路由能力。",
        "related_apis": ["arkui.navigation"],
        "module": "kit.ArkUI",
        "kind": "service",
    },
    "web": {
        "api_id": "arkui.web",
        "name": "Web",
        "aliases": ["Web 组件", "网页组件", "Webview 组件"],
        "path_keywords": [
            "cj-web-web",
            "cj-web-web/Web",
            "cj-apis-webview",
            "ohoswebwebviewWebview",
        ],
        "summary": "用于在页面中嵌入网页内容，并结合 Webview 控制能力加载和交互。",
        "related_apis": ["arkweb.webview_controller"],
        "module": "kit.ArkUI",
        "kind": "component",
    },
    "http_request": {
        "api_id": "ohos.net.http.HttpRequest",
        "name": "HttpRequest",
        "aliases": ["网络请求", "HTTP 请求", "HttpRequest 网络请求"],
        "path_keywords": [
            "cj-apis-net-http",
            "ohosnethttp数据请求",
            "cj-http-request/HTTP数据请求",
        ],
        "summary": "用于发起 HTTP 数据请求并配置 header、method、body 等请求参数。",
        "related_apis": [],
        "module": "ohos.net.http",
        "kind": "service",
    },
    "app_storage": {
        "api_id": "arkui.app_storage",
        "name": "AppStorage",
        "aliases": ["应用状态存储", "全局状态存储", "AppStorage 状态管理"],
        "path_keywords": [
            "cj-appstorage",
            "AppStorage应用全局的UI状态存储",
            "cj-application-state-management-overview",
        ],
        "summary": "应用级全局 UI 状态存储，用于跨组件共享和同步状态数据。",
        "related_apis": [],
        "module": "kit.ArkUI",
        "kind": "state",
    },
    "text_input": {
        "api_id": "arkui.text_input",
        "name": "TextInput",
        "aliases": ["输入框", "文本输入", "TextInput 输入框"],
        "path_keywords": [
            "cj-common-components-text-input",
            "cj-text-input-textinput",
            "cj-text-input-textinput/TextInput",
        ],
        "summary": "用于单行文本输入的基础组件，支持 placeholder、样式和事件配置。",
        "related_apis": [],
    },
    "swiper": {
        "api_id": "arkui.swiper",
        "name": "Swiper",
        "aliases": ["轮播", "轮播图", "Swiper 组件"],
        "path_keywords": [
            "cj-scroll-swipe-swiper",
            "cj-scroll-swipe-swiper/Swiper",
        ],
        "summary": "用于分页滑动、轮播展示和导航点切换的容器组件。",
        "related_apis": [],
    },
    "aes": {
        "api_id": "ohos.security.crypto.aes",
        "name": "AES",
        "aliases": ["AES 加密", "AES 对称加密", "对称加密"],
        "path_keywords": [
            "cj-crypto-aes-sym-encrypt-decrypt-cbc",
            "cj-crypto-aes-sym-encrypt-decrypt-ccm",
            "cj-crypto-aes-sym-encrypt-decrypt-gcm",
            "cj-crypto-aes-sym-encrypt-decrypt-ecb",
        ],
        "summary": "提供 AES 对称加解密相关能力，覆盖 CBC、CCM、GCM、ECB 等模式。",
        "related_apis": [],
        "module": "ohos.security.crypto",
        "kind": "service",
    },
    "bluetooth": {
        "api_id": "ohos.bluetooth",
        "name": "Bluetooth",
        "aliases": ["蓝牙", "Bluetooth", "蓝牙开发"],
        "path_keywords": [
            "cj-apis-bluetooth-a2dp",
            "cj-apis-bluetooth-base_profile",
            "cj-apis-bluetooth-ble",
            "cj-apis-bluetooth-hfp",
        ],
        "summary": "提供 HarmonyOS 蓝牙连接、BLE、A2DP 和 HFP 等能力的 API 入口。",
        "related_apis": [],
        "module": "ohos.bluetooth",
        "kind": "service",
    },
    "arkts_interop": {
        "api_id": "interop.arkts",
        "name": "ArkTSInterop",
        "aliases": ["ArkTS 互操作", "仓颉与 ArkTS 互操作", "ArkTS 调仓颉"],
        "path_keywords": [
            "arkts_import_cangjie",
            "ArkTS_侧使用互操作代码",
            "cj-apis-ark_interop",
        ],
        "summary": "用于仓颉与 ArkTS 之间模块导入、调用和互操作集成的能力入口。",
        "related_apis": [],
        "module": "ohos.ark_interop",
        "kind": "interop",
    },
    "animation": {
        "api_id": "arkui.animation",
        "name": "Animation",
        "aliases": ["属性动画", "动画", "Animation"],
        "path_keywords": [
            "cj-animation-animation",
            "属性动画animation",
            "cj-animation",
        ],
        "summary": "提供属性动画的配置与执行能力，用于实现时长、曲线和效果控制。",
        "related_apis": [],
    },
    "crypto_framework": {
        "api_id": "ohos.security.crypto.framework",
        "name": "CryptoFramework",
        "aliases": ["加密框架", "加密相关 API", "crypto framework"],
        "path_keywords": [
            "cj-apis-crypto",
            "ohossecuritycrypto_framework加解密算法库框架",
        ],
        "summary": "HarmonyOS 加解密算法库框架的 API 总入口，覆盖 Cipher 等通用加密能力。",
        "related_apis": ["ohos.security.crypto.aes"],
        "module": "ohos.security.crypto",
        "kind": "service",
    },
    "std_crypto": {
        "api_id": "std.crypto.cipher",
        "name": "std.crypto",
        "aliases": ["std.crypto", "std.crypto 加密", "crypto.cipher"],
        "path_keywords": [
            "std/cipher_package_overview",
            "std/cipher_package_interfaces",
            "std/std_module_overview",
        ],
        "summary": "仓颉标准库中的对称加解密接口与能力概览。",
        "related_apis": [],
        "module": "std.crypto",
        "kind": "package",
    },
    "std_net": {
        "api_id": "std.net",
        "name": "std.net",
        "aliases": ["std.net", "std.net 网络", "net 包"],
        "path_keywords": [
            "std/net_package_overview",
            "std/net_package_classes",
            "std/net_package_interfaces",
            "std/net_package_enums",
        ],
        "summary": "仓颉标准库中的网络通信能力，覆盖 IP、Socket 和常见网络接口。",
        "related_apis": [],
        "module": "std.net",
        "kind": "package",
    },
    "std_fs": {
        "api_id": "std.fs",
        "name": "std.fs",
        "aliases": ["std.fs", "std.fs 文件操作", "fs 包"],
        "path_keywords": [
            "std/fs_package_overview",
            "std/fs_package_classes",
            "std/fs_package_enums",
            "std/fs_package_funcs",
        ],
        "summary": "仓颉标准库中的文件系统能力，覆盖路径、文件、目录和文件元数据操作。",
        "related_apis": [],
        "module": "std.fs",
        "kind": "package",
    },
    "relational_store": {
        "api_id": "ohos.data.relational_store",
        "name": "RelationalStore",
        "aliases": ["关系型数据库", "RelationalStore 数据库", "RDB 数据库"],
        "path_keywords": [
            "cj-apis-relational_store",
            "ohosdatarelational_store关系型数据库",
            "cj-data-persistence-by-rdb-store",
        ],
        "summary": "用于关系型数据库创建、查询和持久化管理的 HarmonyOS 数据库能力。",
        "related_apis": [],
        "module": "ohos.data.relational_store",
        "kind": "service",
    },
    "error_manager": {
        "api_id": "ohos.app.ability.error_manager",
        "name": "ErrorManager",
        "aliases": ["错误管理", "参数校验错误", "error_manager"],
        "path_keywords": [
            "cj-apis-app-ability-error_manager",
            "ohosappabilityerror_manager错误管理模块",
        ],
        "summary": "HarmonyOS 错误管理模块，覆盖应用能力相关的错误处理与错误码。",
        "related_apis": ["ohos.application.error_observer", "ohos.business_exception"],
        "module": "ohos.app.ability",
        "kind": "service",
    },
    "error_observer": {
        "api_id": "ohos.application.error_observer",
        "name": "ErrorObserver",
        "aliases": ["错误观察", "应用错误观察", "error_observer"],
        "path_keywords": [
            "cj-apis-application-error_observer",
            "ohosapplicationerror_observer",
        ],
        "summary": "应用错误观察模块，用于监听和处理应用运行时错误。",
        "related_apis": ["ohos.app.ability.error_manager"],
        "module": "ohos.application",
        "kind": "service",
    },
    "business_exception": {
        "api_id": "ohos.business_exception",
        "name": "BusinessException",
        "aliases": ["业务异常", "BusinessException", "参数异常"],
        "path_keywords": [
            "cj-api-business_exception",
            "business_exception",
        ],
        "summary": "业务异常类型定义，用于承载 API 调用过程中的错误码与错误信息。",
        "related_apis": ["ohos.app.ability.error_manager"],
        "module": "ohos",
        "kind": "exception",
    },
    "value_type": {
        "api_id": "ohos.value_type",
        "name": "ValueType",
        "aliases": ["值类型", "类型不匹配", "value_type"],
        "path_keywords": [
            "cj-apis-value_type",
            "value_type",
            "enum_ContentType",
        ],
        "summary": "值类型与基础内容类型定义，常用于定位类型不匹配与入参类型问题。",
        "related_apis": ["ohos.app.ability.error_manager"],
        "module": "ohos",
        "kind": "type",
    },
    "window": {
        "api_id": "ohos.window",
        "name": "Window",
        "aliases": ["窗口", "窗口操作", "window"],
        "path_keywords": [
            "cj-apis-window",
            "ohoswindow窗口",
        ],
        "summary": "HarmonyOS 窗口管理能力，用于窗口创建、控制与错误定位。",
        "related_apis": [],
        "module": "ohos.window",
        "kind": "service",
    },
    "permission": {
        "api_id": "ohos.permission",
        "name": "Permission",
        "aliases": ["权限", "权限被拒绝", "permission"],
        "path_keywords": [
            "cj-app-permission-group-list",
            "cj-app-permission-mgmt-overview",
        ],
        "summary": "权限分组与权限管理总览，用于定位权限声明、申请和拒绝原因。",
        "related_apis": [],
        "module": "ohos.permission",
        "kind": "service",
    },
    "canvas_context_2d": {
        "api_id": "arkui.canvas_rendering_context_2d",
        "name": "CanvasRenderingContext2D",
        "aliases": ["Canvas 2D", "内存不足错误", "CanvasRenderingContext2D"],
        "path_keywords": [
            "cj-canvas-drawing-canvasrenderingcontext2d",
            "CanvasRenderingContext2D",
        ],
        "summary": "Canvas 2D 绘制上下文能力，常见于图形绘制与大对象内存占用场景。",
        "related_apis": [],
        "module": "kit.ArkUI",
        "kind": "component",
    },
    "builder_macro": {
        "api_id": "arkui.builder_macro",
        "name": "BuilderMacro",
        "aliases": ["Builder 宏", "编译错误找不到符号", "BuilderParam"],
        "path_keywords": [
            "cj-macro-builder",
            "cj-macro-builderparam",
            "Builder宏自定义构建函数",
            "BuilderParam宏引用Builder函数",
        ],
        "summary": "Builder 与 BuilderParam 宏能力，用于处理自定义构建函数与相关编译问题。",
        "related_apis": [],
        "module": "kit.ArkUI",
        "kind": "macro",
    },
}

HIGH_VALUE_TASKS = [
    {
        "task_id": "ui.image.display",
        "title": "图片加载与显示",
        "aliases": ["图片显示", "图片加载", "Image 组件"],
        "intent": "在页面中展示本地、网络或资源图片，并控制填充效果与显示方式。",
        "when_to_use": ["需要加载并展示图片资源", "需要配置 objectFit、填充或占位效果"],
        "recommended_apis": ["arkui.image"],
        "optional_apis": [],
        "path_keywords": ["cj-image-video-image", "显示图片Image"],
        "example_keywords": ["示例1加载基本类型图片", "示例3为图像设置填充效果", "示例4切换显示不同类型图片"],
        "tags": ["image", "ui", "arkui"],
    },
    {
        "task_id": "ui.list.basic",
        "title": "基础滑动列表",
        "aliases": ["滑动列表", "可滚动列表", "List 列表"],
        "intent": "展示一组可滚动浏览的同类数据项。",
        "when_to_use": ["展示连续多行数据", "需要列表滚动能力", "准备扩展分组、编辑、刷新能力"],
        "recommended_apis": ["arkui.list", "arkui.list_item", "arkui.foreach"],
        "optional_apis": ["arkui.lazyforeach", "arkui.refresh", "arkui.scroll"],
        "path_keywords": [
            "cj-layout-development-create-list/创建列表List",
            "cj-scroll-swipe-list/List/",
        ],
        "example_keywords": [
            "cj-scroll-swipe-list/List/示例代码/示例1_添加滚动事件",
            "cj-scroll-swipe-list/List/示例代码/示例2_",
            "cj-scroll-swipe-list/List/示例代码/示例3_设置编辑模式",
        ],
        "tags": ["list", "scroll", "ui", "arkui"],
    },
    {
        "task_id": "ui.list.grouped",
        "title": "分组列表",
        "aliases": ["分组列表", "带分组的列表", "List 分组"],
        "intent": "将列表项按分组展示，并支持组头或分段结构。",
        "when_to_use": ["联系人分组", "分类展示列表数据"],
        "recommended_apis": ["arkui.list", "arkui.list_item_group", "arkui.list_item"],
        "optional_apis": ["arkui.lazyforeach"],
        "path_keywords": ["支持分组列表", "ListItemGroup"],
        "example_keywords": ["cj-scroll-swipe-listgroup/ListItemGroup/示例代码.md", "支持分组列表"],
        "tags": ["list", "group", "ui", "arkui"],
    },
    {
        "task_id": "ui.grid.basic",
        "title": "网格布局展示",
        "aliases": ["Grid 布局", "网格布局", "Grid 组件"],
        "intent": "按网格模板展示多列内容，并支持滚动、模板和位置控制。",
        "when_to_use": ["宫格内容展示", "需要 columnsTemplate 或 rowsTemplate 配置"],
        "recommended_apis": ["arkui.grid", "arkui.grid_item"],
        "optional_apis": ["arkui.scroll", "arkui.lazyforeach"],
        "path_keywords": ["cj-scroll-swipe-grid", "cj-scroll-swipe-griditem"],
        "example_keywords": ["cj-scroll-swipe-grid/Grid/示例代码.md", "cj-scroll-swipe-griditem/GridItem/示例代码.md"],
        "tags": ["grid", "layout", "ui", "arkui"],
    },
    {
        "task_id": "ui.list.edit",
        "title": "编辑列表",
        "aliases": ["编辑列表", "列表编辑模式", "可编辑列表"],
        "intent": "在列表中支持排序、删除或状态编辑。",
        "when_to_use": ["列表项需要批量操作", "拖拽排序或删除"],
        "recommended_apis": ["arkui.list", "arkui.list_item"],
        "optional_apis": ["arkui.lazyforeach"],
        "path_keywords": ["编辑列表"],
        "example_keywords": ["编辑列表_2more", "示例3_设置编辑模式"],
        "tags": ["list", "edit", "ui", "arkui"],
    },
    {
        "task_id": "ui.list.scroll-position",
        "title": "控制滚动位置",
        "aliases": ["控制滚动位置", "列表定位", "滚动到指定位置"],
        "intent": "在列表或滚动容器中主动控制滚动位置。",
        "when_to_use": ["跳转到指定项", "恢复上次浏览位置"],
        "recommended_apis": ["arkui.list", "arkui.scroll"],
        "optional_apis": ["arkui.scroller"],
        "path_keywords": ["控制滚动位置", "滚动组件通用API"],
        "example_keywords": ["控制滚动位置_2more", "示例代码1设置scroller控制器", "示例1_添加滚动事件"],
        "tags": ["list", "scroll", "position", "ui"],
    },
    {
        "task_id": "layout.linear.basic",
        "title": "线性布局 Row/Column",
        "aliases": ["Row 布局", "Column 布局", "线性布局"],
        "intent": "使用 Row 或 Column 按单轴方向组织页面内容。",
        "when_to_use": ["子元素需要水平或垂直线性排列", "需要配置 alignItems 或主轴排列方式"],
        "recommended_apis": ["arkui.row", "arkui.column"],
        "optional_apis": ["arkui.flex"],
        "path_keywords": ["cj-layout-development-linear", "线性布局RowColumn"],
        "example_keywords": ["Row容器内子元素在水平方向上的排列", "Column容器内子元素在垂直方向上的排列"],
        "tags": ["layout", "row", "column", "ui"],
    },
    {
        "task_id": "layout.stack.basic",
        "title": "层叠布局 Stack",
        "aliases": ["Stack 布局", "层叠布局", "堆叠布局"],
        "intent": "使用 Stack 将多个组件按层叠方式组合在同一区域展示。",
        "when_to_use": ["需要组件叠放展示", "需要前后景覆盖或角标类布局"],
        "recommended_apis": ["arkui.stack"],
        "optional_apis": [],
        "path_keywords": ["cj-layout-development-stack-layout", "层叠布局Stack"],
        "example_keywords": ["层叠布局Stack"],
        "tags": ["layout", "stack", "ui"],
    },
    {
        "task_id": "layout.flex.basic",
        "title": "弹性布局 Flex",
        "aliases": ["Flex 布局", "弹性布局", "Flex 组件"],
        "intent": "使用 Flex 管理子元素的主轴、交叉轴和伸缩排列。",
        "when_to_use": ["需要自适应伸缩布局", "需要 justifyContent 或 alignItems 等弹性布局能力"],
        "recommended_apis": ["arkui.flex"],
        "optional_apis": ["arkui.row", "arkui.column"],
        "path_keywords": ["cj-layout-development-flex-layout", "cj-row-column-stack-flex/Flex"],
        "example_keywords": ["示例1子组件排列方向", "示例3子组件在主轴上的对齐格式", "示例4子组件在交叉轴上的对齐方式"],
        "tags": ["layout", "flex", "ui"],
    },
    {
        "task_id": "ui.slider.basic",
        "title": "滑动条数值选择",
        "aliases": ["Slider 滑动条", "滑动条", "Slider 组件"],
        "intent": "通过拖动滑块在指定数值范围内进行选择。",
        "when_to_use": ["需要选择连续数值", "需要配置 min、max 或样式"],
        "recommended_apis": ["arkui.slider"],
        "optional_apis": [],
        "path_keywords": ["cj-button-picker-slider", "cj-button-picker-slider/Slider"],
        "example_keywords": ["示例1滑动条基础样式"],
        "tags": ["slider", "input", "ui"],
    },
    {
        "task_id": "ui.refresh.basic",
        "title": "下拉刷新",
        "aliases": ["下拉刷新", "列表刷新", "Refresh"],
        "intent": "为滚动列表增加下拉刷新交互。",
        "when_to_use": ["内容需要主动刷新", "社交流、消息流、内容流更新"],
        "recommended_apis": ["arkui.refresh", "arkui.list"],
        "optional_apis": ["arkui.scroll"],
        "path_keywords": ["cj-scroll-swipe-refresh/Refresh"],
        "example_keywords": ["cj-scroll-swipe-refresh/Refresh/示例代码.md"],
        "tags": ["refresh", "list", "ui"],
    },
    {
        "task_id": "ui.list.lazy-load",
        "title": "LazyForEach 长列表",
        "aliases": ["懒加载列表", "长列表", "LazyForEach"],
        "intent": "在大数据量场景中使用懒加载循环渲染降低开销。",
        "when_to_use": ["大数据量列表", "滚动性能敏感"],
        "recommended_apis": ["arkui.lazyforeach", "arkui.list"],
        "optional_apis": ["arkui.foreach"],
        "path_keywords": ["cj-rendering-control-lazyforeach/LazyForEach数据懒加载"],
        "example_keywords": ["cj-rendering-control-lazyforeach/LazyForEach数据懒加载"],
        "tags": ["lazyforeach", "list", "performance"],
    },
    {
        "task_id": "ui.dialog.alert",
        "title": "提示与确认弹窗",
        "aliases": ["AlertDialog 弹窗", "提示框", "警告弹窗"],
        "intent": "在页面中弹出提示、确认或危险操作确认对话框。",
        "when_to_use": ["需要用户确认操作", "需要展示重要提示或风险信息"],
        "recommended_apis": ["arkui.alert_dialog"],
        "optional_apis": [],
        "path_keywords": ["cj-dialog-alertdialog", "警告弹窗AlertDialog"],
        "example_keywords": ["示例1弹出多个按钮的弹窗", "示例2可在主窗外弹出的弹窗"],
        "tags": ["dialog", "alert", "ui"],
    },
    {
        "task_id": "navigation.page.basic",
        "title": "页面导航与路由栈",
        "aliases": ["Navigation 导航", "页面导航", "NavPathStack 路由管理"],
        "intent": "使用 Navigation 和 NavPathStack 管理页面切换、堆栈和导航结构。",
        "when_to_use": ["需要页面级导航容器", "需要管理导航栈和路由跳转"],
        "recommended_apis": ["arkui.navigation"],
        "optional_apis": [],
        "path_keywords": ["cj-navigation-navigation", "cj-navigation-switching-navigation", "NavPathStack"],
        "example_keywords": ["cj-navigation-switching-navigation/Navigation/示例代码.md"],
        "tags": ["navigation", "router", "ui"],
    },
    {
        "task_id": "navigation.router.basic",
        "title": "页面跳转与 Router",
        "aliases": ["Router 路由", "页面跳转", "路由管理"],
        "intent": "使用 Router 执行页面跳转、返回和参数传递。",
        "when_to_use": ["需要简单页面跳转", "需要使用 pushUrl、replaceUrl 或 back"],
        "recommended_apis": ["arkui.router"],
        "optional_apis": ["arkui.navigation"],
        "path_keywords": ["cj-apis-uicontext-router", "Router", "cj-navigation-introduction"],
        "example_keywords": ["cj-apis-uicontext-router/Router"],
        "tags": ["navigation", "router", "ui"],
    },
    {
        "task_id": "web.embed.basic",
        "title": "嵌入网页与 Webview 控制",
        "aliases": ["Web 组件", "Webview", "网页嵌入"],
        "intent": "在应用页面中嵌入网页内容，并控制页面加载、权限和交互。",
        "when_to_use": ["需要显示网页内容", "需要 loadUrl 或 Webview 控制能力"],
        "recommended_apis": ["arkui.web"],
        "optional_apis": [],
        "path_keywords": ["cj-web-web", "cj-apis-webview", "ohoswebwebviewWebview"],
        "example_keywords": ["cj-web-web/Web/示例代码.md"],
        "tags": ["web", "webview", "ui"],
    },
    {
        "task_id": "network.http.basic",
        "title": "HTTP 网络请求",
        "aliases": ["HttpRequest 网络请求", "HTTP 请求", "网络请求"],
        "intent": "发起 HTTP 请求并配置请求头、方法和返回结果处理。",
        "when_to_use": ["需要访问服务端接口", "需要设置 header 或请求参数"],
        "recommended_apis": ["ohos.net.http.HttpRequest"],
        "optional_apis": [],
        "path_keywords": ["cj-apis-net-http", "ohosnethttp数据请求", "cj-http-request/HTTP数据请求"],
        "example_keywords": ["HTTP数据请求"],
        "tags": ["network", "http", "request"],
    },
    {
        "task_id": "security.aes.basic",
        "title": "AES 对称加解密",
        "aliases": ["AES 加密", "AES 对称密钥加密", "对称加密"],
        "intent": "使用 AES 对数据进行加密和解密，并根据场景选择具体模式。",
        "when_to_use": ["需要对称加密数据", "需要使用 CBC、CCM、GCM 或 ECB 模式"],
        "recommended_apis": ["ohos.security.crypto.aes"],
        "optional_apis": ["std.crypto.cipher"],
        "path_keywords": ["cj-crypto-aes-sym-encrypt-decrypt", "使用AES对称密钥"],
        "example_keywords": ["使用AES对称密钥CBC模式加解密", "使用AES对称密钥CCM模式加解密", "使用AES对称密钥GCM模式加解密"],
        "tags": ["crypto", "aes", "security"],
    },
    {
        "task_id": "connectivity.bluetooth.basic",
        "title": "蓝牙开发",
        "aliases": ["蓝牙 Bluetooth", "蓝牙开发", "Bluetooth"],
        "intent": "使用 HarmonyOS 蓝牙能力处理连接、BLE 和音频协议场景。",
        "when_to_use": ["需要蓝牙连接与通信", "需要 BLE、A2DP 或 HFP 能力"],
        "recommended_apis": ["ohos.bluetooth"],
        "optional_apis": [],
        "path_keywords": ["cj-apis-bluetooth-a2dp", "cj-apis-bluetooth-base_profile", "cj-apis-bluetooth-ble", "cj-apis-bluetooth-hfp"],
        "example_keywords": ["ohosbluetootha2dp蓝牙a2dp模块", "ohosbluetoothbase_profile蓝牙baseProfile模块"],
        "tags": ["bluetooth", "connectivity"],
    },
    {
        "task_id": "interop.arkts.basic",
        "title": "仓颉与 ArkTS 互操作",
        "aliases": ["ArkTS 互操作", "仓颉和 ArkTS 互操作", "调用 ArkTS 代码"],
        "intent": "在仓颉与 ArkTS 之间完成模块导入、调用和互操作桥接。",
        "when_to_use": ["需要在 ArkTS 中调用仓颉代码", "需要仓颉接入 ArkTS 能力"],
        "recommended_apis": ["interop.arkts"],
        "optional_apis": [],
        "path_keywords": ["arkts_import_cangjie", "ArkTS_侧使用互操作代码", "cj-apis-ark_interop"],
        "example_keywords": ["方式一使用_import_语法加载仓颉模块"],
        "tags": ["interop", "arkts"],
    },
    {
        "task_id": "ui.interaction.click",
        "title": "组件点击事件",
        "aliases": ["点击事件", "组件点击", "添加点击事件"],
        "intent": "给组件绑定点击交互并响应用户触发动作。",
        "when_to_use": ["需要处理组件点击事件", "需要为基础组件增加 onClick 交互"],
        "recommended_apis": ["arkui.slider"],
        "optional_apis": ["arkui.text_input", "arkui.image"],
        "path_keywords": ["cj-button-picker-slider", "点击", "组件事件"],
        "example_keywords": ["示例1滑动条基础样式"],
        "tags": ["event", "click", "ui"],
    },
    {
        "task_id": "animation.property.basic",
        "title": "属性动画效果",
        "aliases": ["属性动画", "Animation 动画", "动画效果"],
        "intent": "为组件配置属性动画的时长、曲线和触发效果。",
        "when_to_use": ["需要视觉过渡效果", "需要控制 animation duration 等动画属性"],
        "recommended_apis": ["arkui.animation"],
        "optional_apis": [],
        "path_keywords": ["cj-animation-animation", "属性动画animation"],
        "example_keywords": ["属性动画animation"],
        "tags": ["animation", "ui"],
    },
    {
        "task_id": "component.custom.basic",
        "title": "自定义组件",
        "aliases": ["自定义组件", "创建自定义组件", "组件封装"],
        "intent": "定义并组织自定义组件，用于复用页面结构与交互逻辑。",
        "when_to_use": ["需要封装复用 UI 片段", "需要定义组件生命周期或访问限制"],
        "recommended_apis": [],
        "optional_apis": [],
        "path_keywords": ["cj-custom-component-lifecycle", "cj-custom-components-access-restrictions"],
        "example_keywords": ["自定义组件"],
        "tags": ["component", "custom", "ui"],
    },
    {
        "task_id": "device.info.basic",
        "title": "设备信息获取",
        "aliases": ["设备信息", "获取设备信息", "device_info"],
        "intent": "读取设备基础信息与运行环境相关元数据。",
        "when_to_use": ["需要获取设备型号或系统信息", "需要基于设备信息做分支逻辑"],
        "recommended_apis": [],
        "optional_apis": [],
        "path_keywords": ["cj-apis-device_info", "ohosdevice_info设备信息"],
        "example_keywords": ["设备信息"],
        "tags": ["device", "info"],
    },
    {
        "task_id": "quickstart.first-app",
        "title": "第一个鸿蒙仓颉应用",
        "aliases": ["第一个鸿蒙应用", "仓颉快速开始", "快速开始"],
        "intent": "从模板与工程初始化开始，完成第一个仓颉 HarmonyOS 应用。",
        "when_to_use": ["刚开始搭建仓颉鸿蒙应用", "需要第一个可运行工程示例"],
        "recommended_apis": [],
        "optional_apis": [],
        "path_keywords": ["cj-quick-start-first-cangjie-app", "cj-quick-start-first-cangjie-hybrid-app"],
        "example_keywords": ["first-cangjie-app"],
        "tags": ["quickstart", "app"],
    },
    {
        "task_id": "error.validation",
        "title": "参数校验与业务异常",
        "aliases": ["参数校验失败", "业务异常", "参数异常"],
        "intent": "定位参数校验失败、业务异常和应用错误观察相关文档。",
        "when_to_use": ["出现参数校验失败", "需要查看业务异常或错误观察机制"],
        "recommended_apis": ["ohos.app.ability.error_manager", "ohos.application.error_observer", "ohos.business_exception"],
        "optional_apis": [],
        "path_keywords": ["cj-apis-app-ability-error_manager", "cj-apis-application-error_observer", "cj-api-business_exception"],
        "example_keywords": ["error_manager", "error_observer", "business_exception"],
        "tags": ["error", "validation"],
    },
    {
        "task_id": "error.type-mismatch",
        "title": "类型不匹配错误定位",
        "aliases": ["类型不匹配错误", "值类型错误", "类型错误"],
        "intent": "定位值类型、内容类型和类型不匹配相关错误文档。",
        "when_to_use": ["出现类型不匹配错误", "需要查看值类型定义和内容类型枚举"],
        "recommended_apis": ["ohos.value_type", "ohos.app.ability.error_manager"],
        "optional_apis": [],
        "path_keywords": ["cj-common-types", "enum_ContentType", "cj-apis-value_type", "cj-apis-app-ability-error_manager"],
        "example_keywords": ["enum_ContentType", "value_type"],
        "tags": ["error", "type"],
    },
    {
        "task_id": "error.window-operation",
        "title": "窗口操作错误定位",
        "aliases": ["窗口操作错误", "窗口错误", "window 错误"],
        "intent": "定位窗口创建、控制和窗口能力相关错误。",
        "when_to_use": ["出现窗口操作错误", "需要查看窗口 API 和错误原因"],
        "recommended_apis": ["ohos.window"],
        "optional_apis": [],
        "path_keywords": ["cj-apis-window", "ohoswindow窗口"],
        "example_keywords": ["window"],
        "tags": ["error", "window"],
    },
    {
        "task_id": "error.permission-denied",
        "title": "权限拒绝错误定位",
        "aliases": ["权限被拒绝", "权限错误", "permission denied"],
        "intent": "定位权限声明、分组和权限管理相关错误。",
        "when_to_use": ["出现权限被拒绝", "需要查看权限申请和权限组说明"],
        "recommended_apis": ["ohos.permission"],
        "optional_apis": [],
        "path_keywords": ["cj-app-permission-group-list", "cj-app-permission-mgmt-overview"],
        "example_keywords": ["permission"],
        "tags": ["error", "permission"],
    },
    {
        "task_id": "error.out-of-memory",
        "title": "内存不足与 Canvas 绘制错误",
        "aliases": ["内存不足错误", "OOM", "Canvas 内存错误"],
        "intent": "定位 Canvas 2D 绘制和大对象处理中的内存不足问题。",
        "when_to_use": ["出现内存不足错误", "需要排查 Canvas 绘制相关内存问题"],
        "recommended_apis": ["arkui.canvas_rendering_context_2d"],
        "optional_apis": [],
        "path_keywords": ["cj-canvas-drawing-canvasrenderingcontext2d", "CanvasRenderingContext2D"],
        "example_keywords": ["CanvasRenderingContext2D"],
        "tags": ["error", "memory", "canvas"],
    },
    {
        "task_id": "error.compile-symbol",
        "title": "编译期符号找不到",
        "aliases": ["编译错误找不到符号", "找不到符号", "Builder 编译错误"],
        "intent": "定位 Builder、BuilderParam 和宏引用相关编译错误。",
        "when_to_use": ["出现编译错误找不到符号", "需要排查 Builder 宏引用问题"],
        "recommended_apis": ["arkui.builder_macro"],
        "optional_apis": [],
        "path_keywords": ["cj-macro-builder", "cj-macro-builderparam", "Builder宏自定义构建函数", "BuilderParam宏引用Builder函数"],
        "example_keywords": ["Builder", "BuilderParam"],
        "tags": ["error", "compile", "builder"],
    },
    {
        "task_id": "std.crypto.basic",
        "title": "std.crypto 加密能力",
        "aliases": ["std.crypto 加密", "std.crypto", "crypto.cipher"],
        "intent": "使用仓颉标准库中的对称加解密接口完成基础加密能力接入。",
        "when_to_use": ["需要标准库级加密接口", "不依赖 HarmonyOS 平台专有 API"],
        "recommended_apis": ["std.crypto.cipher"],
        "optional_apis": ["ohos.security.crypto.aes"],
        "path_keywords": ["std/cipher_package_overview", "std/cipher_package_interfaces"],
        "example_keywords": ["cipher_package_overview"],
        "tags": ["crypto", "std"],
        "domain": "std",
    },
    {
        "task_id": "std.net.basic",
        "title": "std.net 网络通信",
        "aliases": ["std.net 网络", "std.net", "net 包"],
        "intent": "使用仓颉标准库的网络通信接口处理 IP、Socket 和基础网络能力。",
        "when_to_use": ["需要标准库网络接口", "需要 Socket、IP 地址或网络类能力"],
        "recommended_apis": ["std.net"],
        "optional_apis": [],
        "path_keywords": ["std/net_package_overview", "std/net_package_classes", "std/net_package_interfaces"],
        "example_keywords": ["net_package_overview"],
        "tags": ["net", "std"],
        "domain": "std",
    },
    {
        "task_id": "std.fs.basic",
        "title": "std.fs 文件操作",
        "aliases": ["std.fs 文件操作", "std.fs", "fs 包"],
        "intent": "使用仓颉标准库完成文件、目录、路径和元数据操作。",
        "when_to_use": ["需要读写文件", "需要路径和目录操作"],
        "recommended_apis": ["std.fs"],
        "optional_apis": [],
        "path_keywords": ["std/fs_package_overview", "std/fs_package_classes", "std/fs_package_funcs"],
        "example_keywords": ["fs_package_overview"],
        "tags": ["fs", "std"],
        "domain": "std",
    },
    {
        "task_id": "data.relational-store.basic",
        "title": "关系型数据库 RelationalStore",
        "aliases": ["RelationalStore 数据库", "关系型数据库", "RDB 数据库"],
        "intent": "使用 RelationalStore 进行关系型数据存储、查询和持久化。",
        "when_to_use": ["需要关系型数据库持久化", "需要 RdbStore、ResultSet 或 Predicates 能力"],
        "recommended_apis": ["ohos.data.relational_store"],
        "optional_apis": [],
        "path_keywords": ["cj-apis-relational_store", "ohosdatarelational_store关系型数据库", "cj-data-persistence-by-rdb-store"],
        "example_keywords": ["通过关系型数据库实现数据持久化"],
        "tags": ["database", "rdb", "storage"],
    },
    {
        "task_id": "state.appstorage.basic",
        "title": "全局状态存储 AppStorage",
        "aliases": ["AppStorage 状态管理", "全局状态存储", "应用状态共享"],
        "intent": "使用 AppStorage 在应用级别共享和同步 UI 状态。",
        "when_to_use": ["多个组件需要共享状态", "需要应用级全局 UI 状态存储"],
        "recommended_apis": ["arkui.app_storage"],
        "optional_apis": [],
        "path_keywords": ["cj-appstorage", "AppStorage应用全局的UI状态存储"],
        "example_keywords": ["使用场景", "从应用逻辑使用AppStorage和LocalSto"],
        "tags": ["state", "storage", "appstorage"],
    },
    {
        "task_id": "ui.textinput.basic",
        "title": "文本输入框",
        "aliases": ["TextInput 输入框", "输入框", "文本输入"],
        "intent": "构建单行文本输入框并配置 placeholder、样式和输入事件。",
        "when_to_use": ["表单输入", "搜索框或基础文本录入"],
        "recommended_apis": ["arkui.text_input"],
        "optional_apis": [],
        "path_keywords": ["cj-common-components-text-input", "cj-text-input-textinput"],
        "example_keywords": ["TextInput"],
        "tags": ["textinput", "input", "ui"],
    },
    {
        "task_id": "ui.swiper.basic",
        "title": "轮播与分页切换",
        "aliases": ["Swiper 轮播", "轮播图", "分页滑动"],
        "intent": "使用 Swiper 实现分页切换、轮播展示和导航点交互。",
        "when_to_use": ["需要轮播图效果", "需要分页切换或指示器"],
        "recommended_apis": ["arkui.swiper"],
        "optional_apis": [],
        "path_keywords": ["cj-scroll-swipe-swiper", "cj-scroll-swipe-swiper/Swiper"],
        "example_keywords": ["示例代码1设置导航点交互及翻页动效", "示例代码2设置数字指示器"],
        "tags": ["swiper", "carousel", "ui"],
    },
    {
        "task_id": "ui.scroll.nested",
        "title": "嵌套滚动",
        "aliases": ["嵌套滚动", "父子滚动协同", "Nested Scroll"],
        "intent": "协调父子滚动容器之间的滚动传递和拦截行为。",
        "when_to_use": ["页面存在多层滚动容器", "需要控制父子滚动优先级"],
        "recommended_apis": ["arkui.scroll", "arkui.list"],
        "optional_apis": ["arkui.refresh"],
        "path_keywords": ["嵌套滚动", "nestedScroll", "cj-web-nested-scrolling", "cj-scroll-swipe-scroll/Scroll/示例代码"],
        "example_keywords": [
            "示例代码2嵌套滚动实现方式一",
            "示例代码3嵌套滚动实现方式二",
            "示例代码4嵌套滚动父组件向子组件传递滚动",
            "Web组件嵌套滚动",
        ],
        "tags": ["scroll", "nested", "ui"],
    },
]

try:
    from high_value_tasks_ext import HIGH_VALUE_TASKS_EXT
    HIGH_VALUE_TASKS.extend(HIGH_VALUE_TASKS_EXT)
except ImportError:
    pass


@dataclass
class DocRecord:
    path: str
    source: str
    title: str
    content: str
    summary: str


@dataclass
class LLMConfig:
    base_url: str
    api_key: str
    model: str
    timeout: float
    max_retries: int
    temperature: float


@dataclass
class LLMErrorInfo:
    kind: str
    message: str
    retryable: bool
    stop_provider: bool = False
    status_code: int | None = None


def classify_llm_exception(exc: Exception) -> LLMErrorInfo:
    if isinstance(exc, urllib.error.HTTPError):
        code = exc.code
        message = f"HTTP {code}: {exc.reason}"
        if code == 402:
            return LLMErrorInfo("quota_or_billing", message, retryable=False, stop_provider=True, status_code=code)
        if code in {401, 403}:
            return LLMErrorInfo("auth_or_permission", message, retryable=False, stop_provider=True, status_code=code)
        if code == 429:
            return LLMErrorInfo("rate_limit", message, retryable=True, status_code=code)
        if code in LLM_RETRYABLE_CODES:
            return LLMErrorInfo("server_error", message, retryable=True, status_code=code)
        return LLMErrorInfo("http_error", message, retryable=False, status_code=code)
    if isinstance(exc, urllib.error.URLError):
        return LLMErrorInfo("network_error", str(exc.reason), retryable=True)
    if isinstance(exc, TimeoutError):
        return LLMErrorInfo("network_error", str(exc), retryable=True)
    if isinstance(exc, json.JSONDecodeError):
        return LLMErrorInfo("response_error", str(exc), retryable=False)
    if isinstance(exc, KeyError):
        return LLMErrorInfo("response_error", str(exc), retryable=False)
    if isinstance(exc, RuntimeError):
        return LLMErrorInfo("response_error", str(exc), retryable=False)
    return LLMErrorInfo("unknown_error", str(exc), retryable=False)


class OpenAICompatClient:
    def __init__(self, config: LLMConfig):
        self.config = config
        self.last_usage: dict[str, int] = {}

    @staticmethod
    def parse_json_content(content: str) -> dict[str, Any]:
        text = content.strip()
        fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.DOTALL | re.IGNORECASE)
        if fenced:
            text = fenced.group(1).strip()
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            decoder = json.JSONDecoder()
            start = text.find("{")
            while start != -1:
                try:
                    parsed, _ = decoder.raw_decode(text[start:])
                    if isinstance(parsed, dict):
                        return parsed
                except json.JSONDecodeError:
                    start = text.find("{", start + 1)
                    continue
                break
            raise

    def generate_json(self, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        payload = {
            "model": self.config.model,
            "temperature": self.config.temperature,
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }
        url = self.config.base_url.rstrip("/") + "/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.config.api_key}",
        }
        data = json.dumps(payload).encode("utf-8")

        last_error: Exception | None = None
        for attempt in range(self.config.max_retries + 1):
            req = urllib.request.Request(url, data=data, headers=headers, method="POST")
            try:
                with urllib.request.urlopen(req, timeout=self.config.timeout) as response:
                    body = json.loads(response.read().decode("utf-8"))
                content = body["choices"][0]["message"]["content"]
                if not isinstance(content, str):
                    raise RuntimeError("LLM 响应 content 不是字符串")
                usage = body.get("usage")
                self.last_usage = usage if isinstance(usage, dict) else {}
                return self.parse_json_content(content)
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError, RuntimeError) as exc:
                last_error = exc
                error_info = classify_llm_exception(exc)
                if not error_info.retryable or attempt >= self.config.max_retries:
                    raise
            time.sleep(1.0 * (attempt + 1))

        raise RuntimeError(f"LLM 请求失败: {last_error}")


def llm_config_from_env() -> LLMConfig:
    base_url = os.environ.get("OPENAI_BASE_URL", "").strip()
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    model = os.environ.get("OPENAI_MODEL", "").strip()
    missing = [
        name for name, value in (
            ("OPENAI_BASE_URL", base_url),
            ("OPENAI_API_KEY", api_key),
            ("OPENAI_MODEL", model),
        ) if not value
    ]
    if missing:
        raise RuntimeError(
            "rule+llm 模式缺少必要环境变量: "
            + ", ".join(missing)
            + "。请配置 OpenAI 兼容 API 后重试。"
        )
    return LLMConfig(
        base_url=base_url,
        api_key=api_key,
        model=model,
        timeout=float(os.environ.get("OPENAI_TIMEOUT", "60")),
        max_retries=int(os.environ.get("OPENAI_MAX_RETRIES", "2")),
        temperature=float(os.environ.get("OPENAI_TEMPERATURE", "0.2")),
    )


def parse_card_types(raw: str) -> tuple[str, ...]:
    allowed = {"task", "api", "example", "doc"}
    parts = tuple(item.strip() for item in raw.split(",") if item.strip())
    if not parts:
        raise ValueError("llm-card-types 不能为空")
    invalid = [item for item in parts if item not in allowed]
    if invalid:
        raise ValueError(f"llm-card-types 包含非法值: {', '.join(invalid)}")
    return parts


def read_text(path: Path) -> str:
    for encoding in ("utf-8", "gb18030"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="ignore")


def first_heading(content: str) -> str:
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return ""


def summarize(content: str) -> str:
    lines: list[str] = []
    for raw in content.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#") or line.startswith("```") or line.startswith("|") or line.startswith(">"):
            continue
        if line.lower() in NOISE_HEADINGS:
            continue
        lines.append(line)
        if len(" ".join(lines)) >= 180:
            break
    text = re.sub(r"\s+", " ", " ".join(lines)).strip()
    return text[:220]


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "card"


def unique_id(base: str, used: set[str]) -> str:
    candidate = base
    index = 2
    while candidate in used:
        candidate = f"{base}-{index}"
        index += 1
    used.add(candidate)
    return candidate


def detect_tags(*values: str) -> list[str]:
    haystack = " ".join(values).lower()
    tags: list[str] = []
    mapping = {
        "list": ["list", "列表"],
        "scroll": ["scroll", "滚动"],
        "refresh": ["refresh", "刷新"],
        "lazyforeach": ["lazyforeach"],
        "foreach": ["foreach"],
        "group": ["group", "分组"],
        "edit": ["编辑"],
        "nested": ["嵌套滚动", "nested"],
        "example": ["示例", "demo", "example"],
        "arkui": ["arkui"],
        "image": ["image", "图片", "图像"],
        "grid": ["grid", "网格"],
        "layout": ["布局", "layout"],
        "row": ["row", "行布局"],
        "column": ["column", "列布局"],
        "flex": ["flex", "弹性布局"],
        "slider": ["slider", "滑动条"],
        "dialog": ["dialog", "弹窗"],
        "alert": ["alertdialog", "alert", "警告弹窗"],
        "navigation": ["navigation", "导航", "navpathstack"],
        "router": ["router", "路由"],
        "web": ["web", "webview", "网页"],
        "network": ["http", "网络请求"],
        "storage": ["appstorage", "状态存储"],
        "textinput": ["textinput", "输入框"],
        "swiper": ["swiper", "轮播"],
        "stack": ["stack", "层叠布局"],
        "crypto": ["crypto", "aes", "加密"],
        "bluetooth": ["bluetooth", "蓝牙"],
        "interop": ["interop", "arkts 互操作", "arkts", "import", "模块导入"],
        "animation": ["animation", "动画"],
        "std": ["std.", "标准库"],
        "fs": ["fs", "文件操作", "文件"],
        "net": ["std.net", "socket", "网络通信"],
        "database": ["relationalstore", "关系型数据库", "rdb", "数据库"],
        "event": ["事件", "onclick", "点击"],
        "click": ["点击", "tap"],
        "component": ["组件", "component"],
        "custom": ["自定义", "custom"],
        "device": ["设备", "device"],
        "quickstart": ["快速开始", "第一个应用"],
        "app": ["应用", "app"],
        "error": ["错误", "异常", "failed", "denied"],
        "validation": ["参数校验", "businessexception", "参数异常"],
        "type": ["类型不匹配", "valuetype", "contenttype"],
        "window": ["窗口", "window"],
        "permission": ["权限", "permission"],
        "memory": ["内存不足", "memory", "oom"],
        "canvas": ["canvasrenderingcontext2d", "canvas"],
        "compile": ["编译错误", "找不到符号", "compile"],
        "builder": ["builder", "builderparam"],
    }
    for tag, hints in mapping.items():
        if any(h.lower() in haystack for h in hints):
            tags.append(tag)
    return tags


def normalize_aliases(values: list[str]) -> list[str]:
    seen: set[str] = set()
    aliases: list[str] = []
    for value in values:
        value = re.sub(r"\s+", " ", value).strip()
        if not value:
            continue
        key = value.lower()
        if key in seen:
            continue
        seen.add(key)
        aliases.append(value)
    return aliases


def infer_intent_types(row: dict[str, Any], card_type: str) -> list[str]:
    haystack = " ".join(
        str(value)
        for value in (
            row.get("title"),
            row.get("name"),
            row.get("intent"),
            row.get("summary"),
            " ".join(row.get("aliases", [])),
            " ".join(row.get("tags", [])),
        )
        if value
    ).lower()
    intents: list[str] = []
    if any(word in haystack for word in ("错误", "异常", "permission", "window", "builder", "memory", "参数校验")):
        intents.append("troubleshooting")
    if any(word in haystack for word in ("如何", "实现", "创建", "布局", "列表", "页面", "轮播", "动画", "组件", "导航", "状态")):
        intents.append("build_feature")
    if any(word in haystack for word in ("api", "属性", "事件", "模块", "接口", "框架", "包", "type", "macro")):
        intents.append("api_lookup")
    if any(word in haystack for word in ("示例", "demo", "example")) or card_type == "example":
        intents.append("example_lookup")
    if any(word in haystack for word in ("有哪些", "概览", "overview", "标准库", "蓝牙开发", "加密能力", "探索")):
        intents.append("exploration")
    if any(word in haystack for word in ("快速开始", "第一个", "quickstart")):
        intents.append("quickstart")
    if not intents:
        intents.append("build_feature" if card_type == "task" else "api_lookup")
    return intents


def infer_primary_objects(row: dict[str, Any]) -> list[str]:
    values = " ".join(
        str(value)
        for value in (
            row.get("title"),
            row.get("name"),
            row.get("intent"),
            row.get("summary"),
            " ".join(row.get("aliases", [])),
            " ".join(row.get("tags", [])),
            " ".join(row.get("source_paths", [])),
        )
        if value
    ).lower()
    mapping = {
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
        "slider": ["slider", "滑动条"],
        "dialog": ["alertdialog", "弹窗"],
        "navigation": ["navigation", "navpathstack"],
        "router": ["router", "路由"],
        "web": ["webview", "web", "arkweb", "webcookie", "webviewcontroller"],
        "websocket": ["websocket", "upgradefromclient", "websocketframe"],
        "http": ["httprequest", "http", "requestinstream", "证书锁定", "证书校验"],
        "network_connection": ["netconnection", "网络连接"],
        "appstorage": ["appstorage"],
        "localstorage": ["localstorage"],
        "textinput": ["textinput", "输入框"],
        "swiper": ["swiper", "轮播"],
        "aes": ["aes"],
        "bluetooth": ["bluetooth", "蓝牙"],
        "arkts_interop": ["arkts", "互操作", "import", "模块导入"],
        "animation": ["animation", "动画"],
        "std_crypto": ["std.crypto", "cipher"],
        "std_net": ["std.net", "socket"],
        "std_fs": ["std.fs", "file", "文件"],
        "ability": ["uiability", "abilitycontext", "want", "abilitylifecyclestate", "abilitydelegator"],
        "access_token": ["requestpermissionsfromuser", "atmanager", "权限申请", "用户授权"],
        "preferences": ["preferences", "用户首选项", "用户设置"],
        "relational_store": ["relationalstore", "rdb", "关系型数据库", "数据库", "rdbstore"],
        "resource_file": ["rawfile", "resource_manager", "resourcemanager", "应用沙箱", "file_fs"],
        "photo_access": ["photoaccesshelper", "fetchresult", "相册"],
        "camera": ["cameramanager", "camerakit", "相机"],
        "sensor": ["sensor", "gyroscope", "accelerometer", "传感器"],
        "ipc": ["ipc", "rpc", "parcelable"],
        "telephony": ["telephony", "callstate"],
        "huks": ["huks", "security_huks", "universalkeystorekit", "密钥库", "generatekeyitem"],
        "prompt_action": ["promptaction", "showtoast", "showactionmenu", "toast", "actionmenu"],
        "device_info": ["device_info", "设备信息", "battery_info", "system_date_time", "settings"],
        "window_display": ["display", "windowstage", "displaymanager", "windowmanager"],
        "validation_error": ["参数校验", "businessexception", "error_manager"],
        "type_error": ["类型不匹配", "valuetype", "contenttype"],
        "window_error": ["窗口", "ohoswindow"],
        "permission_error": ["权限", "permission"],
        "memory_error": ["内存不足", "canvasrenderingcontext2d", "oom"],
        "compile_error": ["builder", "builderparam", "找不到符号", "编译错误"],
        "custom_component": ["自定义组件", "custom component"],
    }
    objects = [key for key, hints in mapping.items() if any(hint in values for hint in hints)]
    return objects or ["general"]


def infer_problem_signals(row: dict[str, Any]) -> list[str]:
    aliases = [alias for alias in row.get("aliases", []) if any(token in alias.lower() for token in ("错误", "失败", "异常", "denied", "oom"))]
    tags = [tag for tag in row.get("tags", []) if tag in {"error", "validation", "permission", "memory", "compile"}]
    values = aliases + tags
    return normalize_aliases(values)


def infer_stages(row: dict[str, Any], card_type: str) -> list[str]:
    haystack = " ".join(
        str(value)
        for value in (
            row.get("title"),
            row.get("name"),
            row.get("intent"),
            row.get("summary"),
            " ".join(row.get("aliases", [])),
        )
        if value
    ).lower()
    stages: list[str] = []
    if any(word in haystack for word in ("错误", "异常", "失败", "找不到符号", "denied")):
        stages.append("debug")
    if any(word in haystack for word in ("概览", "有哪些", "overview", "标准库", "框架")):
        stages.append("discovery")
    if any(word in haystack for word in ("属性", "事件", "api", "模块", "接口", "包")):
        stages.append("reference")
    if card_type == "example":
        stages.append("example")
    if card_type == "task" and not stages:
        stages.append("implementation")
    return stages or ["reference"]


def appdev_semantic_values(row: dict[str, Any]) -> dict[str, list[str]]:
    haystack = " ".join(
        str(value)
        for value in (
            row.get("title"),
            row.get("name"),
            row.get("intent"),
            row.get("summary"),
            " ".join(row.get("aliases", [])),
            " ".join(row.get("source_paths", [])),
        )
        if value
    ).lower()
    rules: list[tuple[tuple[str, ...], dict[str, list[str]]]] = [
        (
            ("requestpermissionsfromuser", "atmanager"),
            {
                "semantic_aliases": ["运行时申请权限", "向用户申请授权", "动态权限申请", "权限弹窗", "PermissionRequestResult"],
                "user_queries": ["运行时怎么向用户申请权限", "权限申请接口怎么用", "用户拒绝授权后怎么处理"],
                "primary_objects": ["access_token", "ability"],
            },
        ),
        (
            ("declare-permissions", "module.json5"),
            {
                "semantic_aliases": ["声明权限", "module.json5 权限配置", "ohos.permission.INTERNET", "权限声明"],
                "user_queries": ["网络请求需要配置什么权限", "应用权限要在 module.json5 里怎么声明", "相机需要声明哪些权限"],
                "primary_objects": ["access_token"],
            },
        ),
        (
            ("uiabilitycontext",),
            {
                "semantic_aliases": ["UIAbilityContext", "Ability 上下文", "获取 UIAbility 上下文", "AbilityContext"],
                "user_queries": ["UIAbilityContext 能做哪些事情", "UIAbilityContext 怎么获取", "用 UIAbilityContext 启动页面"],
                "primary_objects": ["ability"],
            },
        ),
        (
            ("class_want", "app-ability-want"),
            {
                "semantic_aliases": ["Want 对象", "Want 参数", "页面跳转传参", "Ability 启动参数"],
                "user_queries": ["Want 对象怎么传参数", "startAbility 怎么传 Want", "页面跳转参数怎么放到 Want 里"],
                "primary_objects": ["ability"],
            },
        ),
        (
            ("abilitylifecyclestate", "abilitydelegator"),
            {
                "semantic_aliases": ["AbilityLifecycleState", "Ability 生命周期状态", "AbilityDelegator", "UIAbility 测试"],
                "user_queries": ["Ability 生命周期状态怎么测试", "AbilityDelegator 怎么获取生命周期状态", "UIAbility 测试生命周期"],
                "primary_objects": ["ability"],
            },
        ),
        (
            ("localstorage",),
            {
                "semantic_aliases": ["LocalStorage 页面级状态", "UIAbility 共享 LocalStorage", "页面状态共享"],
                "user_queries": ["LocalStorage 怎么在 UIAbility 和页面之间共享", "LocalStorage 页面级状态怎么用", "UIAbility 传 LocalStorage 给页面"],
                "primary_objects": ["localstorage", "arkui_state", "ability"],
            },
        ),
        (
            ("preferences",),
            {
                "semantic_aliases": ["用户首选项", "保存用户设置", "Preferences.getPreferences", "Preferences.has", "Preferences.put"],
                "user_queries": ["Preferences 怎么保存用户设置", "Preferences 读取 key 不存在怎么判断", "getPreferences 需要传什么 context 和 options"],
                "primary_objects": ["preferences"],
            },
        ),
        (
            ("relational_store", "rdbstore"),
            {
                "semantic_aliases": ["RdbStore", "getRdbStore", "executeSql", "querySql", "关系型数据库建表", "SQL 查询"],
                "user_queries": ["RelationalStore 怎么创建数据库", "RdbStore 怎么执行建表 SQL", "RdbStore 怎么查询数据"],
                "primary_objects": ["relational_store"],
            },
        ),
        (
            ("webcookie", "hascookie"),
            {
                "semantic_aliases": ["hasCookie", "WebCookieManager.hasCookie", "检查 Cookie 是否存在", "WebView Cookie"],
                "user_queries": ["WebView 怎么判断当前有没有 Cookie", "WebCookieManager hasCookie 怎么用", "WebView Cookie 是否存在怎么判断"],
                "primary_objects": ["web"],
            },
        ),
        (
            ("runjavascript",),
            {
                "semantic_aliases": ["runJavaScript", "执行 JavaScript", "WebView JS 返回值", "AsyncCallback String"],
                "user_queries": ["WebView 怎么执行 JavaScript 并拿返回值", "runJavaScript 怎么用", "WebviewController 执行 JS"],
                "primary_objects": ["web"],
            },
        ),
        (
            ("registerjavascriptproxy",),
            {
                "semantic_aliases": ["registerJavaScriptProxy", "JS bridge", "H5 调仓颉", "JavaScriptProxyCallback"],
                "user_queries": ["WebView 怎么把仓颉方法暴露给 H5 调用", "registerJavaScriptProxy 怎么注册 JS bridge", "H5 怎么调用仓颉方法"],
                "primary_objects": ["web"],
            },
        ),
        (
            ("storewebarchive",),
            {
                "semantic_aliases": ["storeWebArchive", "保存网页", "网页离线包", "WebView 离线存档"],
                "user_queries": ["WebView 怎么保存网页离线包", "storeWebArchive 怎么用", "WebView 保存当前页面"],
                "primary_objects": ["web"],
            },
        ),
        (
            ("darkmode", "webdarkmode"),
            {
                "semantic_aliases": ["darkMode", "WebDarkMode", "Web 深色模式", "forceDarkAccess"],
                "user_queries": ["WebView 深色模式怎么设置", "Web darkMode 属性怎么用", "Web 组件怎么适配深色模式"],
                "primary_objects": ["web"],
            },
        ),
        (
            ("cj-web-debugging-with-devtools", "setwebdebuggingaccess"),
            {
                "semantic_aliases": ["DevTools", "Web 调试", "setWebDebuggingAccess", "调试前端页面"],
                "user_queries": ["WebView DevTools 调试怎么打开", "DevTools 无法发现网页怎么办", "Web 调试开关怎么开启"],
                "primary_objects": ["web"],
            },
        ),
        (
            ("cj-web-pdf-preview",),
            {
                "semantic_aliases": ["PDF 预览", "WebView PDF", "PDF 文档预览"],
                "user_queries": ["WebView PDF 预览怎么做", "Web 组件怎么预览 PDF", "PDF 文档预览能力"],
                "primary_objects": ["web"],
            },
        ),
        (
            ("safe-area", "safe_area"),
            {
                "semantic_aliases": ["安全区域", "safe area", "safe-area-insets", "网页安全区域避让"],
                "user_queries": ["WebView 安全区域避让怎么适配", "网页安全区域怎么计算", "WebView safe area insets 怎么用"],
                "primary_objects": ["web"],
            },
        ),
        (
            ("secure-shield", "secure shield"),
            {
                "semantic_aliases": ["secure shield mode", "安全盾牌模式", "Web 安全盾牌"],
                "user_queries": ["WebView secure shield mode 是什么", "Web 安全盾牌模式怎么用", "secure shield mode 文档"],
                "primary_objects": ["web"],
            },
        ),
        (
            ("requestinstream",),
            {
                "semantic_aliases": ["requestInStream", "HTTP 流式响应", "流式响应", "HTTP 数据请求流"],
                "user_queries": ["HTTP 请求怎么处理流式响应", "requestInStream 接口怎么用", "HTTP 流式响应怎么读取"],
                "primary_objects": ["http"],
            },
        ),
        (
            ("证书锁定", "certificate"),
            {
                "semantic_aliases": ["证书锁定", "证书校验", "CertificatePinning", "HTTP 证书锁定"],
                "user_queries": ["HTTP 证书锁定怎么配置", "HTTP 请求证书校验失败怎么排查", "证书锁定配置在哪里"],
                "primary_objects": ["http"],
            },
        ),
        (
            ("net-connection", "net_connection", "网络连接"),
            {
                "semantic_aliases": ["网络连接管理", "网络连接状态", "NetConnection", "连接状态监听"],
                "user_queries": ["网络连接状态怎么监听", "网络连接管理 API 怎么用", "怎么监听网络断开和恢复"],
                "primary_objects": ["network_connection"],
            },
        ),
        (
            ("websocket",),
            {
                "semantic_aliases": ["WebSocket", "upgradeFromClient", "WebSocketFrame", "发送消息"],
                "user_queries": ["WebSocket 客户端怎么升级连接", "WebSocket 怎么发送消息", "WebSocketFrame 怎么写入"],
                "primary_objects": ["websocket"],
            },
        ),
        (
            ("rawfile",),
            {
                "semantic_aliases": ["rawfile", "resources/rawfile", "资源文件", "ResourceManager", "getRawFd"],
                "user_queries": ["rawfile 路径无效怎么排查", "如何解码 resources/rawfile 里的图片", "Image 加载 rawfile 图片怎么写"],
                "primary_objects": ["resource_file"],
            },
        ),
        (
            ("file_fs", "应用沙箱", "app-file"),
            {
                "semantic_aliases": ["应用沙箱文件", "文件读写", "file_fs", "应用文件访问", "沙箱目录"],
                "user_queries": ["应用沙箱文件怎么读写", "应用文件访问权限错误怎么排查", "文件路径怎么获取"],
                "primary_objects": ["resource_file", "std_fs"],
            },
        ),
        (
            ("photo_access_helper", "photoaccesshelper", "fetchresult"),
            {
                "semantic_aliases": ["PhotoAccessHelper", "FetchResult", "相册图片列表", "Album"],
                "user_queries": ["怎么获取相册里的图片列表", "PhotoAccessHelper 怎么查询图片", "FetchResult 怎么遍历"],
                "primary_objects": ["photo_access", "media"],
            },
        ),
        (
            ("cameramanager",),
            {
                "semantic_aliases": ["CameraManager", "相机设备列表", "getSupportedCameras", "相机预览"],
                "user_queries": ["CameraManager 怎么获取相机设备列表", "相机预览黑屏怎么排查", "CameraKit 预览怎么创建"],
                "primary_objects": ["camera"],
            },
        ),
        (
            ("gyroscope", "sensor"),
            {
                "semantic_aliases": ["Gyroscope", "传感器订阅", "sensor.on", "sensor.off", "陀螺仪"],
                "user_queries": ["传感器怎么订阅陀螺仪数据", "传感器监听怎么取消", "Gyroscope 数据怎么获取"],
                "primary_objects": ["sensor"],
            },
        ),
        (
            ("ipc", "rpc", "parcelable"),
            {
                "semantic_aliases": ["RPC", "IPCKit", "Parcelable", "远程调用", "跨进程通信"],
                "user_queries": ["RPC 通信怎么创建远程调用", "RPC 调用错误码怎么排查", "Parcelable 怎么传输对象"],
                "primary_objects": ["ipc"],
            },
        ),
        (
            ("telephony", "callstate"),
            {
                "semantic_aliases": ["Telephony", "CallState", "通话状态", "拨打电话"],
                "user_queries": ["Telephony 调用失败错误码怎么排查", "CallState 怎么监听", "拨打电话 API 怎么用"],
                "primary_objects": ["telephony"],
            },
        ),
        (
            ("security_huks", "universalkeystorekit", "huks"),
            {
                "semantic_aliases": ["HUKS", "UniversalKeystoreKit", "通用密钥库", "生成密钥", "generateKeyItem", "分段加解密"],
                "user_queries": ["HUKS 怎么生成密钥", "HUKS 加解密怎么分段处理", "HUKS 密钥不存在怎么排查"],
                "primary_objects": ["huks", "security"],
            },
        ),
        (
            ("promptaction", "showtoast", "showactionmenu"),
            {
                "semantic_aliases": ["PromptAction", "showToast", "showActionMenu", "Toast 提示", "ActionMenu 菜单"],
                "user_queries": ["Toast 提示怎么显示", "ActionMenu 菜单怎么弹出"],
                "primary_objects": ["prompt_action", "arkui_component"],
            },
        ),
        (
            ("battery_info",),
            {
                "semantic_aliases": ["Battery", "battery_info", "电池电量", "电量等级"],
                "user_queries": ["电池电量等级怎么判断", "battery_info 怎么获取电量", "怎么判断设备电池状态"],
                "primary_objects": ["device_info"],
            },
        ),
        (
            ("system_date_time",),
            {
                "semantic_aliases": ["system_date_time", "系统时间", "时间设置", "获取系统时间"],
                "user_queries": ["系统时间怎么获取和设置", "system_date_time API 怎么用", "怎么设置系统时间"],
                "primary_objects": ["device_info"],
            },
        ),
        (
            ("settings",),
            {
                "semantic_aliases": ["Settings", "系统设置", "设置读写", "settings 错误码"],
                "user_queries": ["Settings 系统设置读写失败怎么排查", "Settings 怎么读取系统设置", "系统设置写入失败怎么办"],
                "primary_objects": ["device_info"],
            },
        ),
        (
            ("displaymanager", "getdefaultdisplay", "display"),
            {
                "semantic_aliases": ["Display", "屏幕宽高", "屏幕方向", "getDefaultDisplay"],
                "user_queries": ["Display 怎么获取屏幕宽高和方向", "怎么获取屏幕方向", "折叠屏显示信息怎么获取"],
                "primary_objects": ["window_display"],
            },
        ),
        (
            ("hilog",),
            {
                "semantic_aliases": ["HiLog", "日志 domain", "日志 tag", "打印日志"],
                "user_queries": ["HiLog tag 或 domain 参数错误怎么排查", "HiLog 怎么打印日志", "日志 domain 参数怎么填"],
                "primary_objects": ["diagnostics"],
            },
        ),
    ]
    merged: dict[str, list[str]] = {
        "semantic_aliases": [],
        "user_queries": [],
        "primary_objects": [],
    }
    for hints, values in rules:
        if any(hint in haystack for hint in hints):
            for key, items in values.items():
                merged[key].extend(items)
    return {key: normalize_aliases(values) for key, values in merged.items() if values}


def seed_user_queries(row: dict[str, Any], card_type: str) -> list[str]:
    title = str(row.get("title") or row.get("name") or "").strip()
    summary = str(row.get("summary") or row.get("intent") or row.get("scenario") or "").strip()
    aliases = [str(alias).strip() for alias in row.get("aliases", []) if str(alias).strip()]
    head = aliases[0] if aliases else title
    queries = [title, head]
    if card_type == "task":
        queries.extend([f"如何{title}", f"怎么{head}", summary])
    elif card_type == "api":
        queries.extend([f"{head} API", f"{head} 怎么用", f"{head} 方法"])
    elif card_type == "example":
        queries.extend([f"{head} 示例", f"怎么参考{head}", summary])
    else:
        queries.extend([f"{head} 文档", f"{head} 怎么用", summary])
    return [query for query in queries if query]


def enrich_card_metadata(row: dict[str, Any], card_type: str) -> dict[str, Any]:
    updated = dict(row)
    identity_text = str(updated.get("title") or updated.get("name") or "")
    aliases = updated.get("aliases", [])
    appdev_values = appdev_semantic_values(updated)
    if "semantic_aliases" not in updated:
        updated["semantic_aliases"] = normalize_aliases([identity_text, *aliases])
    updated["semantic_aliases"] = normalize_aliases(
        [*updated.get("semantic_aliases", []), *appdev_values.get("semantic_aliases", [])]
    )
    if "user_queries" not in updated:
        updated["user_queries"] = normalize_aliases(seed_user_queries(updated, card_type))
    updated["user_queries"] = normalize_aliases(
        [*updated.get("user_queries", []), *appdev_values.get("user_queries", [])]
    )
    if "when_to_use" not in updated:
        updated["when_to_use"] = []
    if "when_not_to_use" not in updated:
        updated["when_not_to_use"] = []
    updated["intent_types"] = infer_intent_types(updated, card_type)
    updated["primary_objects"] = normalize_aliases(
        [*infer_primary_objects(updated), *appdev_values.get("primary_objects", [])]
    )
    updated["problem_signals"] = infer_problem_signals(updated)
    updated["stages"] = infer_stages(updated, card_type)
    updated["priority"] = round(float(updated.get("confidence", 0.7)), 2)
    return updated


def discover_docs(root: Path) -> list[DocRecord]:
    records: list[DocRecord] = []
    for source in DOC_SOURCES:
        source_root = root / source
        if not source_root.exists():
            continue
        for file_path in source_root.rglob("*.md"):
            if file_path.name == "SKILL.md":
                continue
            rel = file_path.relative_to(root).as_posix()
            content = read_text(file_path).strip()
            if not content:
                continue
            title = first_heading(content) or file_path.stem
            records.append(
                DocRecord(
                    path=rel,
                    source=source,
                    title=title,
                    content=content,
                    summary=summarize(content),
                )
            )
    return records


def filter_docs(records: list[DocRecord], keywords: list[str]) -> list[DocRecord]:
    lowered = [keyword.lower() for keyword in keywords]
    return [
        record for record in records
        if any(keyword in f"{record.path} {record.title}".lower() for keyword in lowered)
    ]


def prefer_primary_doc(records: list[DocRecord]) -> list[DocRecord]:
    def score(record: DocRecord) -> tuple[int, int, int]:
        path = record.path
        return (
            0 if path.endswith("/.overview.md") else 1,
            0 if "/示例代码/" not in path and "示例代码.md" not in path else 1,
            len(path),
        )

    return sorted(records, key=score)


def find_examples(records: list[DocRecord]) -> list[dict]:
    examples: list[dict] = []
    used_ids: set[str] = set()
    for record in records:
        haystack = f"{record.path} {record.title}".lower()
        if not any(hint in haystack for hint in EXAMPLE_HINTS):
            continue
        example_id = unique_id(f"example.{slugify(record.path)}", used_ids)
        related_apis: list[str] = []
        for config in HIGH_VALUE_API_MAP.values():
            if any(keyword.lower() in haystack for keyword in config["path_keywords"]):
                related_apis.append(config["api_id"])
        examples.append(
            enrich_card_metadata(
                {
                "example_id": example_id,
                "title": record.title,
                "scenario": record.summary or "示例代码场景。",
                "related_tasks": [],
                "related_apis": sorted(set(related_apis)),
                "source_paths": [record.path],
                "tags": sorted(set(detect_tags(record.path, record.title, record.summary))),
                "generation_mode": "rule",
                "confidence": 0.72,
                "needs_review": False,
                },
                "example",
            )
        )
    return examples


def api_kind_from_path(path: str) -> str | None:
    lowered = path.lower()
    if "/func_" in lowered:
        return "function"
    if "/class_" in lowered:
        return "class"
    if "/interface_" in lowered:
        return "interface"
    if "/enum_" in lowered:
        return "enum"
    if "组件属性" in path:
        return "property"
    if "组件事件" in path:
        return "event"
    if "基础类型定义" in path:
        return "type"
    return None


def api_name_from_record(record: DocRecord, kind: str) -> str:
    stem = Path(record.path).stem
    if kind == "function":
        normalized_title = record.title.replace("\\", "")
        title_match = re.search(r"\bfunc\s+([A-Za-z_][A-Za-z0-9_]*)", normalized_title)
        if title_match:
            return title_match.group(1)
    mapping = {
        "class": "class_",
        "interface": "interface_",
        "enum": "enum_",
        "function": "func_",
    }
    prefix = mapping.get(kind)
    if prefix and prefix in stem:
        suffix = stem.split(prefix, 1)[1]
        if kind == "function":
            suffix = re.split(r"_[0-9a-f]{6,}$", suffix, maxsplit=1)[0]
            suffix = suffix.split("_", 1)[0] if "_" in suffix else suffix
        suffix = suffix.strip("_")
        if suffix:
            return suffix
    title = record.title.strip()
    title = re.sub(r"^(class|interface|enum|func)\s+", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\s+", " ", title).strip()
    return title or stem


def api_module_from_path(path: str) -> str:
    parts = path.split("/")
    for segment in reversed(parts[:-1]):
        if segment.startswith(("ohos", "std", "kit.", "arkui", "arkweb")):
            return segment
    if parts and parts[0] == "std":
        return "std"
    if parts and parts[0] == "stdx":
        return "stdx"
    return "application"


def api_aliases(record: DocRecord, name: str) -> list[str]:
    parent = Path(record.path).parent.name
    stem = Path(record.path).stem
    raw = [name, record.title, parent, stem]
    if record.title.startswith("func "):
        normalized_title = record.title.replace("\\", "")
        title_match = re.search(r"\bfunc\s+([A-Za-z_][A-Za-z0-9_]*)", normalized_title)
        if title_match:
            raw.append(title_match.group(1))
    return normalize_aliases([item for item in raw if item and item != ".overview"])


def related_examples_for_record(record: DocRecord, examples: list[dict]) -> list[str]:
    group = "/".join(record.path.split("/")[:2])
    name_lower = api_name_from_record(record, api_kind_from_path(record.path) or "").lower()
    related: list[str] = []
    for example in examples:
        joined = " ".join(example.get("source_paths", []) + [example.get("title", "")]).lower()
        if group and group in joined:
            related.append(example["example_id"])
            continue
        if name_lower and name_lower in joined:
            related.append(example["example_id"])
    return sorted(dict.fromkeys(related))[:6]


def discover_api_cards(records: list[DocRecord], examples: list[dict]) -> list[dict]:
    cards: list[dict] = []
    used_ids: set[str] = set()
    for record in records:
        kind = api_kind_from_path(record.path)
        if not kind:
            continue
        name = api_name_from_record(record, kind)
        api_id = unique_id(f"api.{slugify(record.path[:-3])}", used_ids)
        summary = record.summary or record.title
        cards.append(
            enrich_card_metadata(
                {
                    "api_id": api_id,
                    "name": name,
                    "kind": kind,
                    "module": api_module_from_path(record.path),
                    "source": record.source,
                    "doc_kind": "reference",
                    "summary": summary,
                    "aliases": api_aliases(record, name),
                    "when_to_use": [summary] if summary else [],
                    "when_not_to_use": [],
                    "related_apis": [],
                    "example_ids": related_examples_for_record(record, examples),
                    "source_paths": [record.path],
                    "tags": sorted(set(detect_tags(record.path, record.title, record.summary, name))),
                    "generation_mode": "rule",
                    "confidence": 0.68,
                    "needs_review": False,
                    "llm_candidate": False,
                },
                "api",
            )
        )
    return cards


def merge_api_cards(curated: list[dict], discovered: list[dict]) -> list[dict]:
    merged: list[dict] = []
    path_to_index: dict[str, int] = {}
    identity_to_index: dict[tuple[str, str, str], int] = {}

    def identity(row: dict) -> tuple[str, str, str]:
        return (
            str(row.get("module", "")),
            str(row.get("kind", "")),
            str(row.get("name", "")).lower(),
        )

    def merge_into(target: dict, source: dict) -> None:
        target["source_paths"] = sorted(
            dict.fromkeys([*target.get("source_paths", []), *source.get("source_paths", [])])
        )
        target["aliases"] = normalize_aliases([*target.get("aliases", []), *source.get("aliases", [])])
        target["tags"] = sorted(set([*target.get("tags", []), *source.get("tags", [])]))
        target["example_ids"] = sorted(
            dict.fromkeys([*target.get("example_ids", []), *source.get("example_ids", [])])
        )[:6]
        if not target.get("summary") and source.get("summary"):
            target["summary"] = source["summary"]
        target["priority"] = round(float(target.get("confidence", 0.7)), 2)

    def register(row: dict, index: int) -> None:
        for path in row.get("source_paths", []):
            path_to_index[path] = index
        key = identity(row)
        if all(key):
            identity_to_index[key] = index

    for row in curated:
        merged.append(row)
        register(row, len(merged) - 1)

    for row in discovered:
        paths = set(row.get("source_paths", []))
        path_hit = next((path_to_index[path] for path in paths if path in path_to_index), None)
        key = identity(row)
        identity_hit = identity_to_index.get(key) if all(key) else None
        target_index = path_hit if path_hit is not None else identity_hit
        if target_index is not None:
            merge_into(merged[target_index], row)
            register(merged[target_index], target_index)
            continue
        merged.append(row)
        register(row, len(merged) - 1)
    return merged


def build_api_cards(records: list[DocRecord], examples: list[dict]) -> list[dict]:
    curated_cards: list[dict] = []
    for config in HIGH_VALUE_API_MAP.values():
        matched = prefer_primary_doc(filter_docs(records, config["path_keywords"]))
        source_paths = sorted({record.path for record in matched[:8]})
        summary = config["summary"]
        if matched and matched[0].summary:
            summary = matched[0].summary
        example_ids = sorted({
            example["example_id"]
            for example in examples
            if any(api_id == config["api_id"] for api_id in example["related_apis"])
        })[:6]
        curated_cards.append(
            enrich_card_metadata(
                {
                "api_id": config["api_id"],
                "name": config["name"],
                "kind": config.get("kind", "component"),
                "module": config.get("module", "kit.ArkUI"),
                "summary": summary,
                "aliases": normalize_aliases([config["name"], *config["aliases"]]),
                "when_to_use": [summary],
                "when_not_to_use": [],
                "related_apis": config["related_apis"],
                "example_ids": example_ids,
                "source_paths": source_paths,
                "tags": sorted(set(detect_tags(config["name"], summary, " ".join(config["aliases"])))),
                "generation_mode": "rule",
                "confidence": 0.83,
                "needs_review": False,
                "llm_candidate": True,
                },
                "api",
            )
        )
    discovered_cards = discover_api_cards(records, examples)
    return merge_api_cards(curated_cards, discovered_cards)


def build_task_cards(records: list[DocRecord], examples: list[dict]) -> list[dict]:
    cards: list[dict] = []
    for config in HIGH_VALUE_TASKS:
        matched = prefer_primary_doc(filter_docs(records, config["path_keywords"]))
        example_ids = sorted({
            example["example_id"]
            for example in examples
            if any(
                keyword.lower() in " ".join(example["source_paths"]).lower()
                or keyword.lower() in example["title"].lower()
                for keyword in config["example_keywords"]
            )
        })[:6]
        cards.append(
            enrich_card_metadata(
                {
                "task_id": config["task_id"],
                "title": config["title"],
                "aliases": normalize_aliases([config["title"], *config["aliases"]]),
                "domain": config.get("domain", "ui"),
                "intent": config["intent"],
                "when_to_use": config["when_to_use"],
                "recommended_apis": config["recommended_apis"],
                "optional_apis": config["optional_apis"],
                "example_ids": example_ids,
                "source_paths": sorted({record.path for record in matched[:8]}),
                "tags": config["tags"],
                "generation_mode": "rule",
                "confidence": 0.8,
                "needs_review": False,
                },
                "task",
            )
        )
    return cards


def infer_doc_kind(path: str) -> str:
    lowered = path.lower()
    if lowered.endswith("/.overview.md") or lowered.endswith(".overview.md"):
        return "overview"
    if lowered.endswith("/.abstract.md") or lowered.endswith(".abstract.md"):
        return "abstract"
    if "示例代码" in path or "example" in lowered or "demo" in lowered:
        return "example"
    if "/class_" in lowered or "/interface_" in lowered or "/enum_" in lowered or "/func_" in lowered:
        return "reference"
    return "article"


def build_doc_cards(records: list[DocRecord]) -> list[dict]:
    cards: list[dict] = []
    used_ids: set[str] = set()
    for record in records:
        stem = record.path[:-3] if record.path.endswith(".md") else record.path
        doc_id = unique_id(f"doc.{slugify(stem)}", used_ids)
        aliases = normalize_aliases(
            [
                record.title,
                Path(record.path).stem,
                Path(record.path).parent.name,
            ]
        )
        cards.append(
            enrich_card_metadata(
                {
                    "doc_id": doc_id,
                    "title": record.title,
                    "summary": record.summary or record.title,
                    "source": record.source,
                    "doc_kind": infer_doc_kind(record.path),
                    "aliases": aliases,
                    "source_paths": [record.path],
                    "tags": sorted(set(detect_tags(record.path, record.title, record.summary))),
                    "generation_mode": "rule",
                    "confidence": 0.55,
                    "needs_review": False,
                },
                "doc",
            )
        )
    return cards


def attach_example_relations(tasks: list[dict], examples: list[dict]) -> None:
    task_map = {task["task_id"]: task for task in tasks}
    for example in examples:
        related_tasks: list[str] = []
        joined = f"{example['title']} {' '.join(example['source_paths'])}".lower()
        for task in tasks:
            if any(alias.lower() in joined for alias in task["aliases"]):
                related_tasks.append(task["task_id"])
        example["related_tasks"] = sorted(set(related_tasks))
        for task_id in example["related_tasks"]:
            task = task_map[task_id]
            if example["example_id"] not in task["example_ids"]:
                task["example_ids"].append(example["example_id"])
                task["example_ids"].sort()


def build_aliases(tasks: list[dict], apis: list[dict]) -> dict[str, list[str]]:
    aliases: dict[str, list[str]] = {}
    for task in tasks:
        aliases[task["title"]] = task["aliases"]
    for api in apis:
        aliases[api["name"]] = api["aliases"]
    aliases.update(
        {
            "滑动列表": ["List", "列表", "可滚动列表"],
            "下拉刷新": ["Refresh", "刷新组件"],
            "懒加载列表": ["LazyForEach", "懒加载", "长列表"],
            "图片": ["Image", "图片组件", "图像"],
            "网格布局": ["Grid", "GridItem", "网格"],
            "线性布局": ["Row", "Column", "Row 布局", "Column 布局"],
            "弹性布局": ["Flex", "Flex 布局"],
            "滑动条": ["Slider", "滑块"],
            "提示弹窗": ["AlertDialog", "警告弹窗"],
            "导航": ["Navigation", "NavPathStack", "路由管理"],
            "路由": ["Router", "页面跳转"],
            "网页": ["Web", "Webview", "网页组件"],
            "网络请求": ["HttpRequest", "HTTP 请求"],
            "状态管理": ["AppStorage", "全局状态存储"],
            "输入框": ["TextInput", "文本输入"],
            "轮播": ["Swiper", "轮播图"],
            "层叠布局": ["Stack", "堆叠布局"],
            "加密": ["AES", "std.crypto", "对称加密"],
            "加密框架": ["CryptoFramework", "加密相关 API", "Cipher"],
            "蓝牙": ["Bluetooth", "BLE", "A2DP"],
            "互操作": ["ArkTSInterop", "ArkTS 互操作", "ArkTS"],
            "动画": ["Animation", "属性动画"],
            "文件操作": ["std.fs", "fs 包"],
            "标准库网络": ["std.net", "net 包"],
            "数据库": ["RelationalStore", "关系型数据库", "RDB"],
            "点击事件": ["onClick", "点击", "组件事件"],
            "自定义组件": ["自定义组件", "组件封装"],
            "设备信息": ["device_info", "设备信息"],
            "快速开始": ["第一个鸿蒙应用", "仓颉快速开始"],
            "错误处理": ["ErrorManager", "ErrorObserver", "BusinessException"],
            "类型错误": ["ValueType", "ContentType"],
            "窗口错误": ["Window", "窗口操作"],
            "权限错误": ["Permission", "权限被拒绝"],
            "内存错误": ["CanvasRenderingContext2D", "OOM"],
            "编译错误": ["BuilderMacro", "Builder", "BuilderParam"],
        }
    )
    return aliases


def spaced_cjk(text: str) -> str:
    return re.sub(r"([\u3400-\u4dbf\u4e00-\u9fff])", r" \1 ", text)


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_search_db(path: Path, tasks: list[dict], apis: list[dict], examples: list[dict], docs: list[dict]) -> None:
    if path.exists():
        path.unlink()
    conn = sqlite3.connect(path)
    conn.executescript(
        """
        CREATE TABLE cards (
            card_type TEXT NOT NULL,
            card_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            aliases TEXT NOT NULL,
            summary TEXT NOT NULL,
            content TEXT NOT NULL,
            paths_json TEXT NOT NULL,
            metadata_json TEXT NOT NULL
        );
        CREATE VIRTUAL TABLE cards_fts USING fts5(
            title, aliases, summary, content, content=''
        );
        """
    )
    for card_type, rows, card_id_key in (
        ("task", tasks, "task_id"),
        ("api", apis, "api_id"),
        ("example", examples, "example_id"),
        ("doc", docs, "doc_id"),
    ):
        for row in rows:
            card_id = row[card_id_key]
            title = row.get("title") or row.get("name") or card_id
            aliases = row.get("aliases", [])
            summary = row.get("summary") or row.get("intent") or row.get("scenario") or ""
            content_parts = [title, summary, " ".join(aliases)]
            for key in (
                "user_queries", "semantic_aliases", "when_to_use", "when_not_to_use",
                "intent_types", "primary_objects", "problem_signals",
                "recommended_apis", "optional_apis", "related_apis", "related_tasks", "tags",
            ):
                value = row.get(key)
                if isinstance(value, list):
                    content_parts.append(" ".join(str(item) for item in value))
            for key in ("source", "doc_kind"):
                value = row.get(key)
                if isinstance(value, str) and value:
                    content_parts.append(value)
            content_parts.append(" ".join(row.get("source_paths", [])))
            content = " ".join(part for part in content_parts if part)
            conn.execute(
                """
                INSERT INTO cards (card_type, card_id, title, aliases, summary, content, paths_json, metadata_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    card_type,
                    card_id,
                    title,
                    json.dumps(aliases, ensure_ascii=False),
                    summary,
                    spaced_cjk(content),
                    json.dumps(row.get("source_paths", []), ensure_ascii=False),
                    json.dumps(row, ensure_ascii=False),
                ),
            )
            conn.execute(
                """
                INSERT INTO cards_fts (rowid, title, aliases, summary, content)
                VALUES (last_insert_rowid(), ?, ?, ?, ?)
                """,
                (
                    spaced_cjk(title),
                    spaced_cjk(" ".join(aliases)),
                    spaced_cjk(summary),
                    spaced_cjk(content),
                ),
            )
    conn.commit()
    conn.close()


def evidence_for_paths(records_by_path: dict[str, DocRecord], source_paths: list[str]) -> list[dict[str, str]]:
    evidence: list[dict[str, str]] = []
    for path in source_paths[:MAX_EVIDENCE_DOCS]:
        record = records_by_path.get(path)
        if not record:
            continue
        excerpt = select_evidence_excerpt(record.content, MAX_EVIDENCE_CHARS)
        evidence.append(
            {
                "path": record.path,
                "title": record.title,
                "summary": record.summary,
                "excerpt": excerpt,
            }
        )
    return evidence


def select_evidence_excerpt(content: str, max_chars: int) -> str:
    preferred: list[str] = []
    fallback: list[str] = []
    in_table = False
    in_code = False
    for raw in content.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("```"):
            in_code = not in_code
            continue
        lowered = line.lower()
        important = (
            line.startswith("#")
            or line.startswith("public ")
            or line.startswith("|")
            or "功能：" in line
            or "参数" in line
            or "返回" in line
            or "异常" in line
            or "示例" in line
            or "loadurl" in lowered
            or "user-agent" in lowered
            or "rawfile" in lowered
        )
        if line.startswith("|"):
            in_table = True
        elif in_table and not line.startswith("|"):
            in_table = False
        if important or in_table or (in_code and len(" ".join(preferred)) < max_chars // 2):
            preferred.append(line)
        else:
            fallback.append(line)
        if len(" ".join(preferred)) >= max_chars:
            break
    text = " ".join(preferred or fallback)
    return re.sub(r"\s+", " ", text).strip()[:max_chars]


def compact_card(card: dict[str, Any], allowed_keys: list[str]) -> dict[str, Any]:
    return {key: card.get(key) for key in allowed_keys if key in card}


def merge_list(old: list[str], new: Any) -> list[str]:
    if not isinstance(new, list):
        return old
    return normalize_aliases([str(item) for item in new if str(item).strip()])


def clamp_confidence(value: Any, default: float) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return max(0.0, min(1.0, number))


def filter_existing(ids: list[str], valid_ids: set[str]) -> list[str]:
    return [item for item in ids if item in valid_ids]


def cache_file_for(cache_dir: Path, card_type: str, row_id: str, fingerprint: str) -> Path:
    digest = hashlib.sha256(f"{row_id}\0{fingerprint}".encode("utf-8")).hexdigest()[:24]
    safe_id = re.sub(r"[^A-Za-z0-9_.-]+", "_", row_id)[:120]
    return cache_dir / card_type / f"{safe_id}.{digest}.json"


def prompt_fingerprint(
    config: LLMConfig,
    card_type: str,
    skeleton: dict[str, Any],
    evidence: dict[str, Any],
) -> str:
    payload = {
        "prompt_version": PROMPT_VERSION,
        "model": config.model,
        "card_type": card_type,
        "max_evidence_docs": MAX_EVIDENCE_DOCS,
        "max_evidence_chars": MAX_EVIDENCE_CHARS,
        "skeleton": skeleton,
        "evidence": evidence,
    }
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_llm_cache(path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    payload = data.get("payload")
    return payload if isinstance(payload, dict) else None


def write_llm_cache(path: Path, payload: dict[str, Any], usage: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(
            {
                "prompt_version": PROMPT_VERSION,
                "payload": payload,
                "usage": usage,
                "cached_at": datetime.now(timezone.utc).isoformat(),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    tmp.replace(path)


def merge_semantic_fields(updated: dict[str, Any], payload: dict[str, Any]) -> None:
    for key in ("user_queries", "semantic_aliases", "intent_types", "primary_objects"):
        merged = merge_list(updated.get(key, []), payload.get(key))
        if merged:
            updated[key] = merged
    when_not = merge_list(updated.get("when_not_to_use", []), payload.get("when_not_to_use"))
    if when_not or payload.get("when_not_to_use") == []:
        updated["when_not_to_use"] = when_not


def llm_prompts(card_type: str, skeletons: list[dict[str, Any]], evidences: list[dict[str, Any]]) -> tuple[str, str]:
    system_prompt = (
        "你是仓颉 HarmonyOS 文档卡片构建助手。"
        "你只能基于给定证据摘取与归纳，不能臆造不存在的 API、场景或约束。"
        "输出必须是 JSON 对象，不要输出解释文本。"
    )
    schema_by_type = {
        "task": {
            "summary": "string",
            "intent": "string",
            "aliases": ["string"],
            "user_queries": ["string"],
            "semantic_aliases": ["string"],
            "intent_types": ["string"],
            "primary_objects": ["string"],
            "when_to_use": ["string"],
            "when_not_to_use": ["string"],
            "recommended_apis": ["string"],
            "optional_apis": ["string"],
            "tags": ["string"],
            "confidence": 0.0,
            "needs_review": False,
        },
        "api": {
            "summary": "string",
            "aliases": ["string"],
            "user_queries": ["string"],
            "semantic_aliases": ["string"],
            "intent_types": ["string"],
            "primary_objects": ["string"],
            "when_to_use": ["string"],
            "when_not_to_use": ["string"],
            "related_apis": ["string"],
            "tags": ["string"],
            "confidence": 0.0,
            "needs_review": False,
        },
        "example": {
            "summary": "string",
            "scenario": "string",
            "user_queries": ["string"],
            "semantic_aliases": ["string"],
            "intent_types": ["string"],
            "primary_objects": ["string"],
            "when_to_use": ["string"],
            "when_not_to_use": ["string"],
            "related_apis": ["string"],
            "related_tasks": ["string"],
            "tags": ["string"],
            "confidence": 0.0,
            "needs_review": False,
        },
        "doc": {
            "summary": "string",
            "aliases": ["string"],
            "user_queries": ["string"],
            "semantic_aliases": ["string"],
            "intent_types": ["string"],
            "primary_objects": ["string"],
            "when_to_use": ["string"],
            "when_not_to_use": ["string"],
            "tags": ["string"],
            "confidence": 0.0,
            "needs_review": False,
        },
    }
    user_prompt = json.dumps(
        {
            "prompt_version": PROMPT_VERSION,
            "card_type": card_type,
            "task": "基于 skeleton 和 evidence 批量补全高语义字段，不要修改 id、source_paths、name/title。",
            "requirements": [
                "只能使用 evidence 中能支持的信息",
                "数组字段仅保留有把握的项",
                "如果证据不足，返回空数组或简短保守描述，并把 needs_review 设为 true",
                "不要返回 schema 之外的字段",
                "user_queries 至少给出 3 条，覆盖精确名称、自然语言、排错或探索式问法",
                "semantic_aliases 用于召回同义词、缩写、中英文混合叫法，不要替代原始 aliases",
                "输出格式必须是 {\"items\": [{\"card_id\": \"...\", ...fields}]}",
                "items 中每个对象必须带 card_id，且 card_id 必须来自给定 skeletons",
            ],
            "schema": schema_by_type[card_type],
            "skeletons": skeletons,
            "evidences": evidences,
        },
        ensure_ascii=False,
        indent=2,
    )
    return system_prompt, user_prompt


def enrich_task_card(card: dict[str, Any], payload: dict[str, Any], valid_api_ids: set[str]) -> dict[str, Any]:
    updated = dict(card)
    if isinstance(payload.get("summary"), str) and payload["summary"].strip():
        updated["intent"] = payload["summary"].strip()
    if isinstance(payload.get("intent"), str) and payload["intent"].strip():
        updated["intent"] = payload["intent"].strip()
    aliases = merge_list(card["aliases"], payload.get("aliases"))
    if aliases:
        updated["aliases"] = aliases
    when_to_use = merge_list(card["when_to_use"], payload.get("when_to_use"))
    if when_to_use:
        updated["when_to_use"] = when_to_use
    merge_semantic_fields(updated, payload)
    recommended = filter_existing(merge_list(card["recommended_apis"], payload.get("recommended_apis")), valid_api_ids)
    optional = filter_existing(merge_list(card["optional_apis"], payload.get("optional_apis")), valid_api_ids)
    if recommended:
        updated["recommended_apis"] = recommended
    if optional or payload.get("optional_apis") == []:
        updated["optional_apis"] = optional
    tags = merge_list(card["tags"], payload.get("tags"))
    if tags:
        updated["tags"] = tags
    updated["confidence"] = clamp_confidence(payload.get("confidence"), card["confidence"])
    updated["needs_review"] = bool(payload.get("needs_review", card["needs_review"]))
    updated["generation_mode"] = "rule+llm"
    return updated


def enrich_api_card(card: dict[str, Any], payload: dict[str, Any], valid_api_ids: set[str]) -> dict[str, Any]:
    updated = dict(card)
    if isinstance(payload.get("summary"), str) and payload["summary"].strip():
        updated["summary"] = payload["summary"].strip()
    aliases = merge_list(card["aliases"], payload.get("aliases"))
    if aliases:
        updated["aliases"] = aliases
    when_to_use = merge_list(card["when_to_use"], payload.get("when_to_use"))
    if when_to_use:
        updated["when_to_use"] = when_to_use
    merge_semantic_fields(updated, payload)
    related = filter_existing(merge_list(card["related_apis"], payload.get("related_apis")), valid_api_ids)
    if related:
        updated["related_apis"] = related
    tags = merge_list(card["tags"], payload.get("tags"))
    if tags:
        updated["tags"] = tags
    updated["confidence"] = clamp_confidence(payload.get("confidence"), card["confidence"])
    updated["needs_review"] = bool(payload.get("needs_review", card["needs_review"]))
    updated["generation_mode"] = "rule+llm"
    return updated


def enrich_example_card(
    card: dict[str, Any],
    payload: dict[str, Any],
    valid_api_ids: set[str],
    valid_task_ids: set[str],
) -> dict[str, Any]:
    updated = dict(card)
    if isinstance(payload.get("summary"), str) and payload["summary"].strip():
        updated["scenario"] = payload["summary"].strip()
    if isinstance(payload.get("scenario"), str) and payload["scenario"].strip():
        updated["scenario"] = payload["scenario"].strip()
    related_apis = filter_existing(merge_list(card["related_apis"], payload.get("related_apis")), valid_api_ids)
    related_tasks = filter_existing(merge_list(card["related_tasks"], payload.get("related_tasks")), valid_task_ids)
    updated["related_apis"] = related_apis
    updated["related_tasks"] = related_tasks
    when_to_use = merge_list(card.get("when_to_use", []), payload.get("when_to_use"))
    if when_to_use:
        updated["when_to_use"] = when_to_use
    merge_semantic_fields(updated, payload)
    tags = merge_list(card["tags"], payload.get("tags"))
    if tags:
        updated["tags"] = tags
    updated["confidence"] = clamp_confidence(payload.get("confidence"), card["confidence"])
    updated["needs_review"] = bool(payload.get("needs_review", card["needs_review"]))
    updated["generation_mode"] = "rule+llm"
    return updated


def enrich_doc_card(card: dict[str, Any], payload: dict[str, Any]) -> dict[str, Any]:
    updated = dict(card)
    if isinstance(payload.get("summary"), str) and payload["summary"].strip():
        updated["summary"] = payload["summary"].strip()
    aliases = merge_list(card["aliases"], payload.get("aliases"))
    if aliases:
        updated["aliases"] = aliases
    when_to_use = merge_list(card.get("when_to_use", []), payload.get("when_to_use"))
    if when_to_use:
        updated["when_to_use"] = when_to_use
    merge_semantic_fields(updated, payload)
    tags = merge_list(card["tags"], payload.get("tags"))
    if tags:
        updated["tags"] = tags
    updated["confidence"] = clamp_confidence(payload.get("confidence"), card["confidence"])
    updated["needs_review"] = bool(payload.get("needs_review", card["needs_review"]))
    updated["generation_mode"] = "rule+llm"
    return updated


def select_llm_payload_for_card(items: Any, row_id: str, *, single_card_request: bool = False) -> dict[str, Any] | None:
    if not isinstance(items, list):
        return None
    for item in items:
        if isinstance(item, dict) and item.get("card_id") == row_id:
            return item
    if not single_card_request:
        return None
    dict_items = [item for item in items if isinstance(item, dict)]
    if len(dict_items) != 1:
        return None
    return dict_items[0]


def high_value_example_ids(tasks: list[dict], apis: list[dict]) -> set[str]:
    ids: set[str] = set()
    for task in tasks:
        ids.update(task.get("example_ids", []))
    for api in apis:
        ids.update(api.get("example_ids", []))
    return ids


def _rule_llm_progress_msg(
    card_type: str,
    done_in_type: int,
    total_in_type: int,
    stats: dict[str, Any],
    phase_start: float,
    *,
    phase_idx: int,
    phase_count: int,
    overall_done: int,
    overall_total: int,
    provider_healthy: bool,
    last_error: str | None = None,
) -> str:
    """单行 rule+llm 进度：阶段序号、当前类型完成/总量、全任务 overall、成功/失败/跳过、ETA、provider 状态。"""
    elapsed = time.monotonic() - phase_start
    remain = max(0, total_in_type - done_in_type)
    pct = (100.0 * done_in_type / total_in_type) if total_in_type else 100.0
    eta = "eta~?"
    if done_in_type > 0 and remain > 0 and elapsed > 0.5:
        rate = done_in_type / elapsed
        if rate > 0:
            eta_sec = remain / rate
            if eta_sec >= 3600:
                eta = f"eta~{eta_sec / 3600:.1f}h"
            elif eta_sec >= 120:
                eta = f"eta~{eta_sec / 60:.0f}m"
            else:
                eta = f"eta~{eta_sec:.0f}s"
    orem = max(0, overall_total - overall_done)
    opct = (100.0 * overall_done / overall_total) if overall_total else 100.0
    msg = (
        f"[rule+llm] p{phase_idx}/{phase_count} {card_type} {done_in_type}/{total_in_type} "
        f"remain={remain} {pct:.1f}% | overall={overall_done}/{overall_total} oremain={orem} {opct:.1f}% | "
        f"ok={stats['succeeded']} fail={stats['failed']} skip={stats['skipped']} cache={stats['cache_hits']} | "
        f"phase_elap={elapsed:.0f}s {eta}"
    )
    provider_status = str(stats.get("provider_status") or "healthy")
    provider_last_error = str(stats.get("provider_last_error") or "")
    if provider_status == "degraded":
        if "403" in provider_last_error:
            msg += f" | provider_degraded(last_403={provider_last_error[:120]})"
        elif provider_last_error:
            msg += f" | provider_degraded(last_error={provider_last_error[:120]})"
        else:
            msg += " | provider_degraded"
    elif not provider_healthy or provider_status != "healthy":
        msg += f" | provider={provider_status}"
        pr = stats.get("provider_stop_reason") or provider_last_error
        if pr:
            msg += f" stop={str(pr)[:160]}"
    if last_error:
        msg += f" | last_err={last_error[:200]}"
    return msg


def _llm_stderr_ts() -> str:
    """rule+llm 进度行前缀时间戳（UTC，便于对齐日志与 API 侧监控）。"""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def enrich_cards_with_llm(
    tasks: list[dict],
    apis: list[dict],
    examples: list[dict],
    docs: list[dict],
    records_by_path: dict[str, DocRecord],
    batch_size: int,
    llm_card_types: tuple[str, ...],
    llm_concurrency: int,
    llm_cache_dir: Path | None,
) -> tuple[list[dict], list[dict], list[dict], list[dict], dict[str, Any]]:
    try:
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(line_buffering=True)
    except Exception:
        pass
    config = llm_config_from_env()
    client = OpenAICompatClient(config)
    client_lock = Lock()
    valid_api_ids = {card["api_id"] for card in apis}
    valid_task_ids = {card["task_id"] for card in tasks}

    stats = {
        "requested": 0,
        "succeeded": 0,
        "failed": 0,
        "skipped": 0,
        "skipped_due_to_provider_unhealthy": 0,
        "batch_fallbacks": 0,
        "cache_hits": 0,
        "cache_writes": 0,
        "failures": [],
        "failure_summary_by_type": {},
        "by_card_type": {
            card_type: {
                "requested": 0,
                "succeeded": 0,
                "failed": 0,
                "skipped": 0,
                "review": 0,
            }
            for card_type in TYPE_ID_KEY
        },
        "usage": {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
        },
        "provider_status": "healthy",
        "provider_stop_reason": "",
        "provider_last_error": "",
        "enabled_card_types": list(llm_card_types),
        "concurrency": llm_concurrency,
        "cache_dir": str(llm_cache_dir) if llm_cache_dir else "",
        "max_evidence_docs": MAX_EVIDENCE_DOCS,
        "max_evidence_chars": MAX_EVIDENCE_CHARS,
    }

    provider_healthy = True

    def register_failure(card_type: str, row_id: str, exc: Exception, batch_exc: Exception | None = None) -> None:
        nonlocal provider_healthy
        info = classify_llm_exception(exc)
        stats["failed"] += 1
        stats["by_card_type"][card_type]["failed"] += 1
        stats["failure_summary_by_type"][info.kind] = stats["failure_summary_by_type"].get(info.kind, 0) + 1
        record = {
            "card_type": card_type,
            "card_id": row_id,
            "error": info.message,
            "error_type": info.kind,
        }
        if info.status_code is not None:
            record["status_code"] = info.status_code
        if batch_exc is not None:
            record["batch_error"] = str(batch_exc)
        stats["failures"].append(record)
        if info.stop_provider:
            stats["provider_last_error"] = info.message
            if llm_concurrency > 1:
                # 并发模式下其余 worker 可能仍在成功返回：仅标记 degraded，避免误导为全局停机。
                if stats["provider_status"] == "healthy":
                    stats["provider_status"] = "degraded"
            else:
                provider_healthy = False
                stats["provider_status"] = "stopped"
                if not stats["provider_stop_reason"]:
                    stats["provider_stop_reason"] = info.message

    def register_success(card_type: str, row: dict[str, Any]) -> None:
        stats["succeeded"] += 1
        stats["by_card_type"][card_type]["succeeded"] += 1
        if row.get("needs_review"):
            stats["by_card_type"][card_type]["review"] += 1

    def register_skip(card_type: str, row: dict[str, Any]) -> None:
        stats["skipped"] += 1
        stats["by_card_type"][card_type]["skipped"] += 1
        if row.get("needs_review"):
            stats["by_card_type"][card_type]["review"] += 1

    def register_usage() -> None:
        usage = client.last_usage
        for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
            value = usage.get(key)
            if isinstance(value, int):
                stats["usage"][key] += value

    def add_usage(usage: dict[str, Any]) -> None:
        for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
            value = usage.get(key)
            if isinstance(value, int):
                stats["usage"][key] += value

    def apply_payload(card_type: str, row: dict[str, Any], item_payload: dict[str, Any]) -> dict[str, Any]:
        row_id = row[TYPE_ID_KEY[card_type]]
        if card_type == "task":
            return enrich_task_card(row, item_payload, valid_api_ids)
        if card_type == "api":
            return enrich_api_card(row, item_payload, valid_api_ids)
        if card_type == "example":
            return enrich_example_card(row, item_payload, valid_api_ids, valid_task_ids)
        return enrich_doc_card(row, item_payload)

    _llm_phase_specs = [
        (ct, len(rs))
        for ct, rs in (("task", tasks), ("api", apis), ("example", examples), ("doc", docs))
        if ct in llm_card_types
    ]
    _llm_total_units = sum(n for _, n in _llm_phase_specs)
    _llm_phase_count = len(_llm_phase_specs)
    _llm_phase_cursor = {"i": 0}
    print(
        f"[{_llm_stderr_ts()}] [rule+llm] schedule phases={_llm_phase_count} "
        f"detail={' '.join(f'{c}:{n}' for c, n in _llm_phase_specs)} total_units={_llm_total_units} "
        f"concurrency={llm_concurrency} batch_size={batch_size}",
        file=sys.stderr,
        flush=True,
    )

    def process_rows(card_type: str, rows: list[dict], allowed_keys: list[str]) -> list[dict]:
        if card_type not in llm_card_types:
            return rows
        _llm_phase_cursor["i"] += 1
        phase_idx = _llm_phase_cursor["i"]
        phase_start = time.monotonic()
        enriched_map: dict[str, dict] = {}
        target_rows = rows
        print(
            f"[{_llm_stderr_ts()}] [rule+llm] p{phase_idx}/{_llm_phase_count} start {card_type}: in_type_total={len(target_rows)}",
            file=sys.stderr,
            flush=True,
        )

        def _emit_llm_progress(done_in_type: int, total_in_type: int) -> None:
            overall_done = stats["succeeded"] + stats["failed"] + stats["skipped"]
            last_e: str | None = None
            if stats["failed"] and (stats["failed"] <= 3 or stats["failed"] % 10 == 0):
                fails = stats.get("failures") or []
                if fails:
                    last_e = str(fails[-1].get("error") or "")
            print(
                f"[{_llm_stderr_ts()}] "
                + _rule_llm_progress_msg(
                    card_type,
                    done_in_type,
                    total_in_type,
                    stats,
                    phase_start,
                    phase_idx=phase_idx,
                    phase_count=_llm_phase_count,
                    overall_done=overall_done,
                    overall_total=_llm_total_units,
                    provider_healthy=provider_healthy,
                    last_error=last_e,
                ),
                file=sys.stderr,
                flush=True,
            )
            pf = (os.environ.get("CANGJIE_LLM_PROGRESS_FILE") or "").strip()
            if pf:
                snap = {
                    "ts": time.time(),
                    "wall_iso": _llm_stderr_ts(),
                    "phase_idx": phase_idx,
                    "phase_count": _llm_phase_count,
                    "card_type": card_type,
                    "done_in_type": done_in_type,
                    "total_in_type": total_in_type,
                    "overall_done": overall_done,
                    "overall_total": _llm_total_units,
                    "ok": stats["succeeded"],
                    "fail": stats["failed"],
                    "skip": stats["skipped"],
                    "cache_hits": stats["cache_hits"],
                    "provider_status": stats.get("provider_status"),
                    "provider_stop_reason": stats.get("provider_stop_reason") or "",
                    "provider_last_error": stats.get("provider_last_error") or "",
                    "last_error": last_e or "",
                }
                try:
                    Path(pf).write_text(json.dumps(snap, ensure_ascii=False) + "\n", encoding="utf-8")
                except OSError:
                    pass

        if llm_concurrency > 1:
            processed = 0

            def process_single(row: dict[str, Any]) -> dict[str, Any]:
                row_id = row[TYPE_ID_KEY[card_type]]
                evidence = evidence_for_paths(records_by_path, row.get("source_paths", []))
                if not evidence:
                    failed = dict(row)
                    failed["needs_review"] = True
                    return {"status": "skipped", "row_id": row_id, "row": failed}

                skeleton = compact_card(row, allowed_keys)
                skeleton["card_id"] = row_id
                evidence_payload = {"card_id": row_id, "docs": evidence}
                fingerprint = prompt_fingerprint(config, card_type, skeleton, evidence_payload)
                cache_path = cache_file_for(llm_cache_dir, card_type, row_id, fingerprint) if llm_cache_dir else None
                if cache_path:
                    cached = read_llm_cache(cache_path)
                    if cached is not None:
                        return {"status": "cached", "row_id": row_id, "payload": cached, "row": row}

                local_client = OpenAICompatClient(config)
                system_prompt, user_prompt = llm_prompts(card_type, [skeleton], [evidence_payload])
                payload = local_client.generate_json(system_prompt, user_prompt)
                items = payload.get("items")
                if not isinstance(items, list):
                    raise RuntimeError("LLM 返回缺少 items 数组")
                item_payload = select_llm_payload_for_card(items, row_id, single_card_request=True)
                if not item_payload:
                    raise RuntimeError("LLM 响应缺少对应 card_id")
                if cache_path:
                    write_llm_cache(cache_path, item_payload, local_client.last_usage)
                return {
                    "status": "success",
                    "row_id": row_id,
                    "payload": item_payload,
                    "row": row,
                    "usage": local_client.last_usage,
                    "cache_written": bool(cache_path),
                }

            with concurrent.futures.ThreadPoolExecutor(max_workers=llm_concurrency) as executor:
                future_to_row = {executor.submit(process_single, row): row for row in target_rows}
                for future in concurrent.futures.as_completed(future_to_row):
                    row = future_to_row[future]
                    row_id = row[TYPE_ID_KEY[card_type]]
                    processed += 1
                    try:
                        result = future.result()
                    except Exception as exc:  # noqa: BLE001
                        failed = dict(row)
                        failed["needs_review"] = True
                        enriched_map[row_id] = failed
                        register_failure(card_type, row_id, exc)
                    else:
                        status = result["status"]
                        if status == "skipped":
                            enriched_map[row_id] = result["row"]
                            register_skip(card_type, result["row"])
                        elif status == "cached":
                            enriched = apply_payload(card_type, result["row"], result["payload"])
                            enriched_map[row_id] = enriched
                            register_success(card_type, enriched)
                            stats["cache_hits"] += 1
                        else:
                            enriched = apply_payload(card_type, result["row"], result["payload"])
                            enriched_map[row_id] = enriched
                            register_success(card_type, enriched)
                            add_usage(result.get("usage", {}))
                            if result.get("cache_written"):
                                stats["cache_writes"] += 1
                    stats["requested"] = stats["succeeded"] + stats["failed"]
                    stats["by_card_type"][card_type]["requested"] = (
                        stats["by_card_type"][card_type]["succeeded"]
                        + stats["by_card_type"][card_type]["failed"]
                    )
                    _emit_llm_progress(processed, len(target_rows))
            return [enriched_map.get(row[TYPE_ID_KEY[card_type]], row) for row in rows]

        for offset in range(0, len(target_rows), batch_size):
            batch = target_rows[offset:offset + batch_size]
            if not provider_healthy:
                for row in batch:
                    row_id = row[TYPE_ID_KEY[card_type]]
                    fallback = dict(row)
                    fallback["needs_review"] = True
                    enriched_map[row_id] = fallback
                    register_skip(card_type, fallback)
                    stats["skipped_due_to_provider_unhealthy"] += 1
                batch_end = min(offset + len(batch), len(target_rows))
                _emit_llm_progress(batch_end, len(target_rows))
                continue
            batch_rows: list[dict] = []
            skeletons: list[dict[str, Any]] = []
            evidences: list[dict[str, Any]] = []
            for row in batch:
                evidence = evidence_for_paths(records_by_path, row.get("source_paths", []))
                if not evidence:
                    failed = dict(row)
                    failed["needs_review"] = True
                    enriched_map[row[TYPE_ID_KEY[card_type]]] = failed
                    register_skip(card_type, failed)
                    continue
                batch_rows.append(row)
                skeleton = compact_card(row, allowed_keys)
                skeleton["card_id"] = row[TYPE_ID_KEY[card_type]]
                skeletons.append(skeleton)
                evidences.append(
                    {
                        "card_id": row[TYPE_ID_KEY[card_type]],
                        "docs": evidence,
                    }
                )

            if not batch_rows:
                batch_end = min(offset + len(batch), len(target_rows))
                _emit_llm_progress(batch_end, len(target_rows))
                continue

            stats["requested"] += len(batch_rows)
            stats["by_card_type"][card_type]["requested"] += len(batch_rows)
            system_prompt, user_prompt = llm_prompts(card_type, skeletons, evidences)
            try:
                payload = client.generate_json(system_prompt, user_prompt)
                register_usage()
                items = payload.get("items")
                if not isinstance(items, list):
                    raise RuntimeError("LLM 返回缺少 items 数组")
                payload_by_id = {
                    item.get("card_id"): item
                    for item in items
                    if isinstance(item, dict) and isinstance(item.get("card_id"), str)
                }
                for row in batch_rows:
                    row_id = row[TYPE_ID_KEY[card_type]]
                    item_payload = payload_by_id.get(row_id)
                    if not item_payload:
                        failed = dict(row)
                        failed["needs_review"] = True
                        enriched_map[row_id] = failed
                        register_failure(card_type, row_id, RuntimeError("LLM 响应缺少对应 card_id"))
                        continue
                    enriched = apply_payload(card_type, row, item_payload)
                    enriched_map[row_id] = enriched
                    register_success(card_type, enriched)
            except Exception as exc:  # noqa: BLE001
                stats["batch_fallbacks"] += 1
                for row in batch_rows:
                    if not provider_healthy:
                        row_id = row[TYPE_ID_KEY[card_type]]
                        failed = dict(row)
                        failed["needs_review"] = True
                        enriched_map[row_id] = failed
                        register_skip(card_type, failed)
                        stats["skipped_due_to_provider_unhealthy"] += 1
                        continue
                    row_id = row[TYPE_ID_KEY[card_type]]
                    evidence = evidence_for_paths(records_by_path, row.get("source_paths", []))
                    skeleton = compact_card(row, allowed_keys)
                    skeleton["card_id"] = row_id
                    system_prompt, user_prompt = llm_prompts(
                        card_type,
                        [skeleton],
                        [{"card_id": row_id, "docs": evidence}],
                    )
                    try:
                        payload = client.generate_json(system_prompt, user_prompt)
                        register_usage()
                        items = payload.get("items")
                        if not isinstance(items, list):
                            raise RuntimeError("LLM 返回缺少 items 数组")
                        item_payload = select_llm_payload_for_card(items, row_id, single_card_request=True)
                        if not item_payload:
                            raise RuntimeError("LLM 响应缺少对应 card_id")
                        enriched = apply_payload(card_type, row, item_payload)
                        enriched_map[row_id] = enriched
                        register_success(card_type, enriched)
                    except Exception as single_exc:  # noqa: BLE001
                        failed = dict(row)
                        failed["needs_review"] = True
                        enriched_map[row_id] = failed
                        register_failure(card_type, row_id, single_exc, batch_exc=exc)
            batch_end = min(offset + len(batch), len(target_rows))
            _emit_llm_progress(batch_end, len(target_rows))
        return [enriched_map.get(row[TYPE_ID_KEY[card_type]], row) for row in rows]

    task_allowed = [
        "task_id", "title", "aliases", "intent", "when_to_use",
        "when_not_to_use", "recommended_apis", "optional_apis", "tags",
        "user_queries", "semantic_aliases", "intent_types", "primary_objects",
    ]
    api_allowed = [
        "api_id", "name", "summary", "aliases", "when_to_use",
        "when_not_to_use", "related_apis", "tags",
        "kind", "module", "user_queries", "semantic_aliases", "intent_types", "primary_objects",
    ]
    example_allowed = [
        "example_id", "title", "scenario", "when_to_use", "when_not_to_use",
        "related_apis", "related_tasks", "tags",
        "user_queries", "semantic_aliases", "intent_types", "primary_objects",
    ]
    doc_allowed = [
        "doc_id", "title", "summary", "aliases", "source", "doc_kind",
        "when_to_use", "when_not_to_use", "tags",
        "user_queries", "semantic_aliases", "intent_types", "primary_objects",
    ]

    enriched_tasks = process_rows("task", tasks, task_allowed)
    enriched_apis = process_rows("api", apis, api_allowed)
    enriched_examples = process_rows("example", examples, example_allowed)
    enriched_docs = process_rows("doc", docs, doc_allowed)

    task_by_id = {row["task_id"]: row for row in enriched_tasks}
    example_by_id = {row["example_id"]: row for row in enriched_examples}
    for task in enriched_tasks:
        task["recommended_apis"] = filter_existing(task.get("recommended_apis", []), valid_api_ids)
        task["optional_apis"] = filter_existing(task.get("optional_apis", []), valid_api_ids)
        task["example_ids"] = filter_existing(task.get("example_ids", []), set(example_by_id))
    for example in enriched_examples:
        example["related_apis"] = filter_existing(example.get("related_apis", []), valid_api_ids)
        example["related_tasks"] = filter_existing(example.get("related_tasks", []), set(task_by_id))
    for task in enriched_tasks:
        for example_id in task.get("example_ids", []):
            example = example_by_id.get(example_id)
            if not example:
                continue
            if task["task_id"] not in example["related_tasks"]:
                example["related_tasks"].append(task["task_id"])
                example["related_tasks"].sort()

    stats["model"] = config.model
    stats["base_url"] = config.base_url
    stats["prompt_version"] = PROMPT_VERSION
    stats["example_candidate_count"] = len(examples)
    if stats["provider_status"] == "healthy" and stats["failed"] > 0:
        stats["provider_status"] = "degraded"
    return enriched_tasks, enriched_apis, enriched_examples, enriched_docs, stats


TYPE_ID_KEY = {"task": "task_id", "api": "api_id", "example": "example_id", "doc": "doc_id"}


def eval_query_rows_for_card(card_type: str, row: dict[str, Any]) -> list[dict[str, Any]]:
    title = str(row.get("title") or row.get("name") or "").strip()
    if not title:
        title = str(row.get(TYPE_ID_KEY[card_type], "")).strip()
    aliases = [str(alias).strip() for alias in row.get("aliases", []) if str(alias).strip()]
    semantic_aliases = [str(alias).strip() for alias in row.get("semantic_aliases", []) if str(alias).strip()]
    paths = [str(path) for path in row.get("source_paths", []) if str(path).strip()]
    if not title or not paths:
        return []

    head = aliases[0] if aliases else title
    semantic = next((alias for alias in semantic_aliases if alias.lower() != head.lower()), head)
    summary = str(row.get("summary") or row.get("intent") or row.get("scenario") or title).strip()
    api_name = str(row.get("name") or title).strip()
    problem = next((str(item) for item in row.get("problem_signals", []) if str(item).strip()), "")
    object_name = next((str(item) for item in row.get("primary_objects", []) if str(item).strip()), head)

    templates = {
        "exact": head,
        "natural": f"如何使用{head}" if card_type != "doc" else f"怎么理解{head}",
        "semi-structured": f"{api_name} {row.get('kind', card_type)} {summary[:40]}",
        "error-driven": f"{head} {problem or '使用异常'} 怎么排查",
        "exploration": f"{object_name} 相关文档有哪些",
    }
    rows: list[dict[str, Any]] = []
    for category in EVAL_QUERY_CATEGORIES:
        query = templates[category]
        if category == "natural" and semantic and semantic != head:
            query = f"{query} {semantic}"
        rows.append(
            {
                "query": re.sub(r"\s+", " ", query).strip(),
                "expected_paths": paths,
                "category": category,
                "card_type": card_type,
                "card_id": row.get(TYPE_ID_KEY[card_type]),
            }
        )
    return rows


def regression_eval_rows() -> list[dict[str, Any]]:
    load_url_path = (
        "harmonyos-6.0.2-15k/API/ArkWeb/cj-apis-webview/ohoswebwebviewWebview/"
        "class_WebviewController/func_loadUrlTT_ArrayWebHeader_where_T_ResourceStr.md"
    )
    web_paths = [
        load_url_path,
        "harmonyos-6.0.2-15k/API/ArkWeb/cj-apis-webview/ohoswebwebviewWebview",
        "harmonyos-6.0.2-15k/API/arkui-cj/cj-web-web/Web/示例代码_c46e8890.md",
    ]
    return [
        {
            "query": "Web 的 loadUrl 方法",
            "expected_paths": [load_url_path],
            "category": "semi-structured",
            "card_type": "regression",
            "card_id": "regression.web.load_url",
        },
        {
            "query": "loadUrl headers 怎么传",
            "expected_paths": [load_url_path],
            "category": "natural",
            "card_type": "regression",
            "card_id": "regression.web.load_url_headers",
        },
        {
            "query": "WebView 加载网页",
            "expected_paths": web_paths,
            "category": "natural",
            "card_type": "regression",
            "card_id": "regression.web.load_page",
        },
        {
            "query": "Web 组件加载本地 rawfile",
            "expected_paths": [
                "harmonyos-6.0.2-15k/Guide/web/cj-web-page-loading-with-web-components/使用Web组件加载页面/加载本地页面/加载本地页面_1.md",
                "harmonyos-6.0.2-15k/API/arkui-cj/cj-web-web/Web/示例代码_c46e8890.md",
            ],
            "category": "natural",
            "card_type": "regression",
            "card_id": "regression.web.rawfile",
        },
        {
            "query": "设置 User-Agent 后加载页面",
            "expected_paths": [
                "harmonyos-6.0.2-15k/API/ArkWeb/cj-apis-webview/ohoswebwebviewWebview/"
                "class_WebviewController/func_setCustomUserAgentString.md",
                load_url_path,
            ],
            "category": "semi-structured",
            "card_type": "regression",
            "card_id": "regression.web.user_agent_load",
        },
    ]


def write_full_eval_queries(path: Path, tasks: list[dict], apis: list[dict], examples: list[dict], docs: list[dict]) -> int:
    rows: list[dict[str, Any]] = []
    for card_type, cards in (("task", tasks), ("api", apis), ("example", examples), ("doc", docs)):
        for row in cards:
            rows.extend(eval_query_rows_for_card(card_type, row))
    rows.extend(regression_eval_rows())

    seen: set[tuple[str, str]] = set()
    deduped: list[dict[str, Any]] = []
    for row in rows:
        key = (row["query"].lower(), ",".join(row["expected_paths"]))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)

    with path.open("w", encoding="utf-8") as handle:
        for row in deduped:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    return len(deduped)


def assert_default_llm_publishable(
    index_dir: Path,
    llm_card_types: tuple[str, ...],
    tasks: list[dict],
    apis: list[dict],
    examples: list[dict],
    docs: list[dict],
    llm_stats: dict[str, Any] | None,
    max_llm_publish_failures: int = 0,
) -> None:
    if index_dir.resolve() != DEFAULT_INDEX_DIR.resolve() or llm_stats is None:
        return
    expected = {
        "task": len(tasks),
        "api": len(apis),
        "example": len(examples),
        "doc": len(docs),
    }
    failed_total = int(llm_stats.get("failed") or 0)
    if failed_total > max(0, max_llm_publish_failures):
        raise RuntimeError(
            "rule+llm 默认索引发布门禁失败（LLM 失败条数超过阈值），未写入 index/: "
            f"failed={failed_total} max_allowed={max_llm_publish_failures}"
        )
    if 0 < failed_total <= max_llm_publish_failures:
        print(
            f"[rule+llm] WARN: 允许带失败发布 index/（failed={failed_total} <= max={max_llm_publish_failures}），"
            "请后续排查 failures 列表并重跑或补缓存。",
            file=sys.stderr,
            flush=True,
        )
    # 每条卡片应落在 succeeded / skipped / failed 之一；仅用 succeeded 会把「无证据 skip」误判为未完成。
    incomplete: list[str] = []
    for card_type in llm_card_types:
        by = llm_stats["by_card_type"][card_type]
        accounted = int(by["succeeded"]) + int(by["skipped"]) + int(by["failed"])
        exp = expected[card_type]
        if accounted != exp:
            incomplete.append(
                f"{card_type}: accounted={accounted}/{exp} "
                f"(ok={by['succeeded']} skip={by['skipped']} fail={by['failed']})"
            )
    if incomplete:
        raise RuntimeError(
            "rule+llm 默认索引发布门禁失败（各类型处理条数与卡片总数不一致），未写入 index/: " + "; ".join(incomplete)
        )


def build(
    index_dir: Path,
    mode: str = "rule",
    batch_size: int = DEFAULT_LLM_BATCH_SIZE,
    llm_card_types: tuple[str, ...] = DEFAULT_LLM_CARD_TYPES,
    llm_concurrency: int = DEFAULT_LLM_CONCURRENCY,
    llm_cache_dir: Path | None = None,
    max_llm_publish_failures: int = 0,
    docs_dir: Path | None = None,
) -> dict[str, Any]:
    docs_root = docs_dir or DOCS_DIR
    docs = discover_docs(docs_root)
    records_by_path = {record.path: record for record in docs}
    examples = find_examples(docs)
    apis = build_api_cards(docs, examples)
    tasks = build_task_cards(docs, examples)
    doc_cards = build_doc_cards(docs)
    attach_example_relations(tasks, examples)
    aliases = build_aliases(tasks, apis)

    llm_stats: dict[str, Any] | None = None
    if mode == "rule+llm":
        tasks, apis, examples, doc_cards, llm_stats = enrich_cards_with_llm(
            tasks,
            apis,
            examples,
            doc_cards,
            records_by_path,
            batch_size,
            llm_card_types,
            llm_concurrency,
            llm_cache_dir,
        )
        aliases = build_aliases(tasks, apis)
        assert_default_llm_publishable(
            index_dir,
            llm_card_types,
            tasks,
            apis,
            examples,
            doc_cards,
            llm_stats,
            max_llm_publish_failures=max_llm_publish_failures,
        )

    index_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(index_dir / "tasks.jsonl", tasks)
    write_jsonl(index_dir / "apis.jsonl", apis)
    write_jsonl(index_dir / "examples.jsonl", examples)
    write_jsonl(index_dir / "docs.jsonl", doc_cards)
    EVALS_DIR.mkdir(parents=True, exist_ok=True)
    full_eval_count = write_full_eval_queries(EVALS_DIR / "eval_queries_full.jsonl", tasks, apis, examples, doc_cards)
    (index_dir / "aliases.json").write_text(
        json.dumps(aliases, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_search_db(index_dir / "search.db", tasks, apis, examples, doc_cards)

    manifest: dict[str, Any] = {
        "version": "v3",
        "generation_mode": mode,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "prompt_version": PROMPT_VERSION,
        "sources": list(DOC_SOURCES),
        "counts": {
            "tasks": len(tasks),
            "apis": len(apis),
            "examples": len(examples),
            "docs": len(doc_cards),
            "llm_enriched_tasks": sum(1 for row in tasks if row.get("generation_mode") == "rule+llm"),
            "llm_enriched_apis": sum(1 for row in apis if row.get("generation_mode") == "rule+llm"),
            "llm_enriched_examples": sum(1 for row in examples if row.get("generation_mode") == "rule+llm"),
            "llm_enriched_docs": sum(1 for row in doc_cards if row.get("generation_mode") == "rule+llm"),
        },
        "eval": {
            "full_eval_queries": "evals/eval_queries_full.jsonl",
            "full_eval_query_count": full_eval_count,
        },
        "entrypoints": {
            "search": "doc-card/search_v3.py",
            "build": "../cangjie-hmos-doc-search-maintenance/card/builder/build_index_v3.py",
        },
    }
    if llm_stats is not None:
        manifest["llm"] = llm_stats
    (index_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="构建 V3 本地结构化索引")
    parser.add_argument("--index-dir", default=str(DEFAULT_INDEX_DIR), help="索引输出目录")
    parser.add_argument("--docs-dir", default="", help="文档语料根目录（默认使用 DOCS_DIR）")
    parser.add_argument("--mode", choices=("rule", "rule+llm"), default="rule", help="构建模式")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_LLM_BATCH_SIZE, help="rule+llm 模式下的批次大小")
    parser.add_argument(
        "--llm-concurrency",
        type=int,
        default=DEFAULT_LLM_CONCURRENCY,
        help="rule+llm 模式下的单卡并发数；大于 1 时忽略批量请求，改用并发单卡请求",
    )
    parser.add_argument(
        "--llm-cache-dir",
        default="",
        help="rule+llm 缓存目录；按卡片缓存 LLM 结果，支持中断后恢复",
    )
    parser.add_argument(
        "--llm-card-types",
        default=",".join(DEFAULT_LLM_CARD_TYPES),
        help="rule+llm 模式下要补全的卡片类型，逗号分隔：task,api,example,doc",
    )
    parser.add_argument(
        "--max-llm-publish-failures",
        type=int,
        default=0,
        help="仅当 --index-dir 为默认 index/ 时生效：rule+llm 写盘前允许的最大 LLM 失败条数（默认 0=不允许失败）。",
    )
    args = parser.parse_args()
    llm_card_types = parse_card_types(args.llm_card_types)
    docs_dir_arg = Path(args.docs_dir) if args.docs_dir else None
    manifest = build(
        Path(args.index_dir),
        mode=args.mode,
        batch_size=args.batch_size,
        llm_card_types=llm_card_types,
        llm_concurrency=max(1, args.llm_concurrency),
        llm_cache_dir=Path(args.llm_cache_dir) if args.llm_cache_dir else None,
        max_llm_publish_failures=max(0, args.max_llm_publish_failures),
        docs_dir=docs_dir_arg,
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(f"build_index_v3 失败: {exc}", file=sys.stderr)
        sys.exit(1)
