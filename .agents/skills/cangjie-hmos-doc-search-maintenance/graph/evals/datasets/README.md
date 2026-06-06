# 知识图谱Skill测评集 V2

## 概述

本测评集基于知识图谱中**实际存在的完整文档路径**设计，并根据查询类型设置不同数量的答案路径。

## 核心设计原则

### 路径数量按类型设置

| 查询类型 | 路径数量 | 设计原因 | 示例 |
|---------|---------|----------|------|
| **精确查找(api_lookup)** | 1条 | 查询意图明确，唯一答案 | "HttpRequest的timeout参数" → 1条具体路径 |
| **枚举查询(enumeration)** | 1条 | 需具体属性/方法列表文档 | "AppStorage有哪些方法" → 1条列表文档 |
| **逆向查询(reverse_lookup)** | 1条 | 定位到唯一组件/方案 | "下拉刷新用什么组件" → 1条Refresh文档 |
| **用法查询(how_to)** | 1条 | 定位到唯一用法文档 | "List怎么用" → 1条用法文档 |
| **约束查询(constrained)** | 1条 | 定位到唯一解决方案 | "后台保持网络连接" → 1条后台任务文档 |
| **模糊查询(semantic_fuzzy)** | 2-3条 | 多种解决方案需覆盖 | "列表卡顿" → 3条优化文档 |
| **对比查询(comparison)** | 2条 | A和B各自核心文档 | "List vs LazyForEach" → 2条文档 |
| **组合查询(composition)** | 概念数条 | 每概念1条核心文档 | "List+Refresh+HTTP" → 3条文档 |
| **跨生态类比(cross_ecosystem)** | 1-2条 | 对应1或多个鸿蒙组件 | "RecyclerView对应" → 2条文档 |
| **流程查询(workflow)** | 2条 | 步骤涉及的多个文档 | "HTTP请求流程" → 2条文档 |
| **性能边界(performance_boundary)** | 2条 | 多优化方案文档 | "大数据列表卡顿" → 2条文档 |

### 路径格式

**使用完整具体路径**，而非前缀匹配：

```
正确格式: cj-scroll-swipe-list\List\List_2more.md
错误格式: cj-scroll-swipe-list (仅前缀)
```

## 测评集统计

| 统计项 | 数量 |
|--------|------|
| 总用例数 | 50 |
| **路径数量分布** | |
| 1条路径 | 35条用例 |
| 2条路径 | 12条用例 |
| 3条路径 | 3条用例 |
| **难度分布** | |
| normal | 26 |
| compound | 17 |
| hard | 7 |
| **查询类型分布** | |
| how_to | 18 |
| api_lookup | 2 |
| enumeration | 5 |
| reverse_lookup | 3 |
| constrained | 3 |
| semantic_fuzzy | 4 |
| comparison | 4 |
| composition | 4 |
| cross_ecosystem | 4 |
| workflow | 3 |
| performance_boundary | 3 |

## 路径验证来源

所有路径通过以下命令验证：

```bash
python cli.py search "关键词" --graph doc -b -k 10
```

### 已验证的完整路径（部分示例）

| 完整路径 | 文档内容 |
|---------|---------|
| `cj-scroll-swipe-list\List\List_2more.md` | List组件核心用法 |
| `cj-state-rendering-lazyforeach\LazyForEach\.overview.md` | LazyForEach懒加载概述 |
| `cj-scroll-swipe-refresh\Refresh\Refresh_4more.md` | Refresh下拉刷新用法 |
| `cj-apis-net-http\ohosnethttp数据请求\.overview.md` | HTTP请求概述 |
| `cj-apis-net-http\ohosnethttp数据请求\class_HttpRequestOptions\.overview.md` | HttpRequest配置参数 |
| `cj-apis-webview\ohoswebviewWebview\.overview.md` | WebView组件概述 |
| `cj-apis-promptaction\ohosprompt_action弹窗\class_PromptAction\.overview.md` | PromptAction弹窗 |
| `cj-apis-bluetooth-ble\ohosbluetoothble蓝牙ble模块\.overview.md` | 蓝牙BLE模块 |
| `cj-crypto-aes-sym-encrypt-decrypt-ecb\cj-crypto-aes-sym-encrypt-decrypt-ecb.md` | AES加密指南 |
| `cj-apis-timer\Timer定时器\Timer定时器_3more.md` | Timer定时器用法 |
| `cj-apis-relational_store\ohosrelational_store关系型数据库\.overview.md` | 关系型数据库概述 |
| `cj-uiability-usage\UIAbility组件基本用法\UIAbility组件基本用法_2more.md` | UIAbility用法 |
| `cj-apis-ability\ohosabilityAbility\class_UIAbility\.overview.md` | UIAbility类定义 |
| `cj-apis-ability\ohosabilityAbility\class_AbilityLifecycleCallback\.overview.md` | Ability生命周期回调 |
| `cj-apis-device_info\ohosdevice_info设备信息\class_DeviceInfo\.overview.md` | DeviceInfo类 |
| `cj-apis-background_task_mgr\ohosbackground_task_mgr后台任务管理\.overview.md` | 后台任务管理 |
| `cj-apis-geo_location_manager\ohosgeo_location_manager位置服务\class_GeoLocationManager\.overview.md` | 定位服务 |
| `cj-apis-file_picker\ohosfile_picker选择器\class_PhotoViewPicker\.overview.md` | 文件选择器 |
| `cj-scroll-swipe-swiper\Swiper\Swiper_4more.md` | Swiper轮播组件 |
| `cj-scroll-swipe-grid\Grid\Grid_4more.md` | Grid网格布局 |
| `cj-apis-router\ohosrouter页面路由\class_Router\.overview.md` | Router路由 |
| `cj-navigation-navigation\cj-navigation-navigation.md` | Navigation导航 |
| `cj-router-to-navigation\Router切换Navigation\Router切换Navigation_2more.md` | Router迁移指南 |
| `cj-application-state-management-overview\cj-application-state-management-overview.md` | 状态管理概述 |
| `cj-properly-use-state-management-to-develope\cj-properly-use-state-management-to-develope.md` | 状态管理指南 |
| `cj-state-rendering-appstatemanagement\应用级变量的状态管理\AppStorage应用全局的UI状态存储\class_AppStorage\.overview.md` | AppStorage类 |
| `cj-apis-image\ohosimage图片处理\class_Image.md` | 图片处理 |
| `cj-animation\cj-animation.md` | 动画概述 |

## 资源消耗预估

每条用例包含资源约束：

```json
{
  "resource_constraints": {
    "expected_latency_ms": 70,
    "expected_token_input": 140,
    "expected_token_output": 70
  }
}
```

### 按难度基线

| 难度 | 平均耗时 | 平均输入Token | 平均输出Token |
|------|---------|--------------|---------------|
| normal | 50ms | 100 | 50 |
| compound | 70ms | 140 | 70 |
| hard | 100ms | 200 | 100 |

## 测评指标

### 主指标

| 指标 | 权重 | 说明 |
|------|------|------|
| Success@1 | 0.30 | Top1命中率 |
| Success@3 | 0.25 | Top3命中率 |
| Success@5 | 0.20 | Top5命中率 |
| MRR | 0.25 | 平均排名倒数 |

### 按类型预期基线

| 类型 | Success@1 | Success@3 | Success@5 |
|------|-----------|-----------|-----------|
| api_lookup | 95% | 98% | 99% |
| enumeration | 90% | 95% | 98% |
| reverse_lookup | 85% | 90% | 95% |
| how_to | 80% | 90% | 95% |
| constrained | 50% | 70% | 85% |
| semantic_fuzzy | 50% | 80% | 90% |
| comparison | 60% | 85% | 95% |
| composition | 40% | 70% | 85% |
| cross_ecosystem | 60% | 80% | 90% |
| workflow | 50% | 75% | 85% |
| performance_boundary | 40% | 70% | 80% |

## 命中判定规则

```
命中判定采用以下规则：
1. 完整路径精确匹配
2. 父目录匹配（返回结果包含acceptable_paths的父目录也算命中）
```

## 与V1版本对比

| 对比项 | V1 (datasets目录) | V2 (datasets_v2目录) |
|-------|-------------------|---------------------|
| 路径格式 | 前缀匹配 | 完整具体路径 |
| 路径数量 | 固定多路径 | 按类型差异化设置 |
| 精确查询 | 2-3条路径 | 1条唯一路径 |
| 模糊查询 | 2条路径 | 2-3条覆盖路径 |
| 组合查询 | 2-4条路径 | 概念数条路径 |
| 资源消耗 | 无预估 | 包含Token/耗时预估 |

---

**创建日期**: 2026-05-18
**版本**: v2.1
**验证状态**: 所有路径已验证存在
**设计原则**: 精确唯一、多解覆盖、双侧对比、概念均分