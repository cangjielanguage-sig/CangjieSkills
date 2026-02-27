# Cangjie Skills
## 一、cangjie-dev-harmonyos
本 Skill 赋能 Claude 使用仓颉语言进行 HarmonyOS 应用开发，从需求分析、API/文档检索到本地构建、错误排查、经验沉淀一条龙支持。

三级知识检索流程：
1. L0：先帮你把“业务需求”拆成具体技术点（UI 组件、数据结构、交互等）。
2. L1（可选-默认关闭）：用 RAG知识库+混合搜索精准返回项目所需知识点和代码片段。
3. L3：必要时直接查本地 hm-docs 官方文档（UI、语法、stdlib、stdx 全套）。

构建与报错闭环：通过 scripts/build.ps1 触发完整构建流程，拿到详细错误后按“先查 Evolution.md → 再查L3文档”的优先级指导你修复，并在构建成功后要求把关键问题整理进 Evolution.md。

### 使用步骤
1. 根据实际主机环境修改.env文件中的API-KEY（可选，用于L1查询，默认关闭）和build.ps1脚本（必选，用于构建鸿蒙项目）。
2. 在项目根配置技能位置：XXX/MyApplication(鸿蒙应用)/**.claude/skills/cangjie-dev-harmonyos**，直接在对话里用自然语言提鸿蒙 Cangjie 开发需求，例如：
“用 Cangjie 写一个商品列表页面的鸿蒙应用”。

### 注意事项（可选）
在首次启动本skill进行开发时，系统会检查是否用户在.env文件中配置API-KEY，如果没有则会跳过L1查询；如果有，则会自动构建向量数据库和关键词数据库以支持L1的混合搜索。

### 示例
图示是根据skill赋能的CLAUDE自动化应用开发成果示例。  
![微信图片_20260225115922_232_63.png](https://raw.gitcode.com/user-images/assets/9193544/ad4b63c4-f26d-4fe4-a33e-dfded2054010/微信图片_20260225115922_232_63.png '微信图片_20260225115922_232_63.png')
