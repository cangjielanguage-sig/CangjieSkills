---
name: cangjie-harmonyos-doc-search
description: "这是仓颉鸿蒙应用开发最重要的Skill，提供鸿蒙应用开发框架（基于仓颉语言）的文档检索工具，当你遇到不熟悉的鸿蒙UI组件/系统能力API/框架机制/状态管理/仓颉鸿蒙开发等问题时，请使用此Skill"
---

# 仓颉鸿蒙应用开发文档检索工具（重要）

当你遇到不熟悉的鸿蒙UI组件/系统能力API/框架机制/状态管理/仓颉鸿蒙开发等问题时，请执行本Skill目录下的search.py脚本，查询任何关键词或句子，脚本将返回准确语义关联的文档相对路径，你继续去当前目录下的文档目录中查找对应文档，可以按需全量读取或使用grep等工具部分读取。

## ⚗️ 版本检测

本工作区包含两个版本的文档：**8k** 和 **15k**，对应不同的文档目录和仓颉 SDK。

**执行搜索前，必须先确定版本：**

1. 检查工作区根目录是否存在 `.openvk-version` 文件
2. 如果存在，读取其中的版本号（`8k` 或 `15k`）
3. 如果不存在，自动创建并写入默认值 `8k`（15k 用户需手动修改此文件）
4. 后续所有操作直接读取该文件，不再重复询问

**版本与文档目录的对应关系：**

| 版本 | 返回的文档目录 | 排除的文档目录 |
|------|---------------|---------------|
| 15k  | application-dev-v15k、libs_stdx、std | application-dev |
| 8k   | application-dev、libs_stdx、std | application-dev-v15k |

## search.py 用法

```shell
# 必须指定 --version（或由 .openvk-version 文件自动检测）
python search.py "Stack组件用法" --version 15k
python search.py "怎么修改Button组件的尺寸" --version 8k
python search.py "怎么实现过渡动画" --version 15k --limit 15
```

## 案例

如果当前版本是 15k，查询 Button 组件相关文档：

```shell
python search.py "怎么调整Button的尺寸" --version 15k
# 返回 application-dev-v15k 下的文档路径：
application-dev-v15k/cj-button-picker-button/Button/组件属性/func_buttonStyleButtonStyl_3more.md
application-dev-v15k/cj-common-components-button/按钮Button/按钮Button_3more.md
```

如果当前版本是 8k，同样的查询会返回 application-dev 下的文档路径。

工具返回的路径按关联程度自上而下排序，去当前目录下对应文档目录查阅即可。