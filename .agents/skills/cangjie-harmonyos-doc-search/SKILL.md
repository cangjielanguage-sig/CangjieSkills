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

### 默认模式

- **有结果**: 逐行输出文档相对路径（已去除 `resources/` 前缀），按相关度排序
- **无结果**: 标准输出为空（无任何内容）
- **服务端错误**: stderr 输出 `服务端错误: <错误信息>`，退出码 1
- **HTTP 错误 (4xx/5xx)**: stderr 输出 `HTTP <状态码>: <原因>`，退出码 1
- **连接失败**: stderr 输出 `连接失败: <原因>` 及服务地址提示，退出码 1

### JSON 模式 (`--json`)

输出完整 JSON 响应体，包含 `status`、`results` 等字段，可获取更多元信息

### 读取对应文档

输出路径是相对路径，对应源文件位于 Skill 目录下各 backend 的 `.openviking/viking/default/resources/` 中:
- `cangjie-1.0.5/.openviking/viking/default/resources/<输出路径>`
- `harmonyos-6.1.0.818/.openviking/viking/default/resources/<输出路径>`

例如输出 `lang-features/xxx.md`，对应 `cangjie-1.0.5/.openviking/viking/default/resources/lang-features/xxx.md`

### 无结果或异常时

- 无结果 → 换查询词重试（参考上方查询技巧）
- 连接失败 / HTTP 5xx → 稍后重试