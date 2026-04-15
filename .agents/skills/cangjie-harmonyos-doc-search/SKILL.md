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

脚本输出按相关度排序的文档相对路径，在 Skill 目录下读取对应文档即可（harmonyos-6.1-8k，lang-features，std，stdx，tools）

无结果时优先换查询词重试，服务超时或 5xx 则稍后重试