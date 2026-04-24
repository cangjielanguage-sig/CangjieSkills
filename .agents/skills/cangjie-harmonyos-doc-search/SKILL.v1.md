---
name: cangjie-harmonyos-doc-search
description: "鸿蒙仓颉应用开发文档检索工具，包括 UI 组件 API、系统能力接口、框架机制、状态管理的语义化查询。适用于开发中遇到不熟悉 API 或组件时的快速文档定位。"
tags: [workflow, platform]
---

# 仓颉鸿蒙文档检索 Skill（V1）

## 目的

遇到不熟悉的鸿蒙 UI 组件、系统能力 API、状态管理或框架机制时，执行 `search.py` 检索文档。

## 使用方式

```bash
python .agents/skills/cangjie-harmonyos-doc-search/search.py "Stack组件用法"
python .agents/skills/cangjie-harmonyos-doc-search/search.py "怎么修改Button的尺寸" --limit 15
```

`--limit` 返回数量（默认 15），`--target-uri` 收敛到指定目录前缀，`--score-threshold` 过滤低相关结果。

## 查询技巧

搜索基于语义匹配，查询词写法直接影响召回效果：

- 用具体名称而非泛称：`@State装饰器` 优于 `状态管理`，`List列表组件` 优于 `List组件`
- 包含中文描述 + 英文名称：`HashMap集合容器`、`JSON序列化编解码`、`Text组件显示文本`
- 无结果时换一种表述重试，避免纯口语化问句

## 结果处理

脚本输出按相关度排序的文档相对路径，在 Skill 目录下读取对应文档即可。

结果覆盖三个来源：`application-dev/`、`libs_stdx/`、`std/`。

无结果时优先换查询词重试；服务超时或 5xx 则稍后重试。
