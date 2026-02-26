# Cangjie Skills
## 一、cangjie-dev-harmonyos
本 Skill 赋能 Claude 使用仓颉语言进行 HarmonyOS 应用开发，从需求分析、API/文档检索到本地构建、错误排查、经验沉淀一条龙支持。

三级知识检索流程：
1. L0：先帮你把“业务需求”拆成具体技术点（UI 组件、数据结构、交互等）。
2. L1：用 RAG知识库+混合搜索精准返回项目所需知识点和代码片段。
3. L3：必要时直接查本地 hm-docs 官方文档（UI、语法、stdlib、stdx 全套）。

构建与报错闭环：通过 scripts/build.ps1 触发完整构建流程，拿到详细错误后按“先查 Evolution.md → 再查文档”的优先级指导你修复，并在构建成功后要求把关键问题整理进 Evolution.md。

### 使用方式示例
1. 根据实际主机环境修改API-KEY和build脚本
2. 在项目根配置技能位置：**XXX/MyApplication/.claude/skills/cangjie-dev-harmonyos**，直接在对话里用自然语言提鸿蒙 Cangjie 开发需求，例如：
“用 Cangjie 写一个商品列表页面”

### 注意事项
在首次启动本skill进行开发时，系统会自动构建本地文档树（hm-docs）和向量数据库（chroma-db），预计耗时约 1 分钟。资源加载策略如下：

1. 检测到已解压目录：直接读取并使用

2. 仅检测到本地压缩包：自动执行解压操作

3. 未检测到本地资源：自动触发下载并完成构建


💡 快速跳过构建（可选）

为了节省初始化的等待时间，您可以手动下载以下压缩包，并直接解压至项目的 scripts/ 目录下，即可跳过上述自动构建步骤：

hm-docs压缩包目录：https://my.feishu.cn/file/I3BEbJOyBokdtAxbr18cPUlHnDb

chroma-db压缩包目录：https://my.feishu.cn/file/RqY3bprAKoIm9Lxsfa4czYEwnJd

图示是根据skill赋能的CLAUDE自动化应用开发成果示例。  
![微信图片_20260225115922_232_63.png](https://raw.gitcode.com/user-images/assets/9193544/ad4b63c4-f26d-4fe4-a33e-dfded2054010/微信图片_20260225115922_232_63.png '微信图片_20260225115922_232_63.png')
