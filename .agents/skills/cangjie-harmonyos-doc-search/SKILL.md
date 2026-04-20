---
name: cangjie-harmonyos-doc-search
description: "鸿蒙应用开发文档检索工具，遇到不熟悉的UI组件/系统能力API/框架机制/状态管理时使用"
---

# 仓颉鸿蒙文档检索 Skill

## 目的

遇到不熟悉的鸿蒙 UI 组件、系统能力 API、状态管理或框架机制时，执行 `search.py` 检索相关文档

## 使用方式

```bash
python search.py "Stack组件用法"
python search.py "怎么修改Button的尺寸" --limit N # 限制查询记录数量
```

## 查询技巧

搜索基于语义匹配，查询词写法直接影响召回效果：

- 用**具体名称**而非泛称: `@State装饰器` 优于 `状态管理`，`List列表组件` 优于 `List组件`
- 包含**中文描述 + 英文名称**: `HashMap集合容器`、`JSON序列化编解码`、`Text组件显示文本`
- 无结果时换一种表述重试，避免纯口语化问句

## 结果处理

### 读取对应文档

输出路径是相对路径，源文件位于 `<backend>/.openviking/viking/default/resources/<输出路径>`。其中 `<backend>` 取自 `search.py` 中 `DEFAULT_BACKENDS` 列表里的各项，逐个尝试即可定位到文件。

### JSON 模式 (`--json`)

输出完整 JSON 响应体，包含 `status`、`results` 等字段，可获取更多元信息