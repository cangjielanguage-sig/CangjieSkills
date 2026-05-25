# 查询计划规则

## 目标

把用户的产品目标转换成可检索、可实现、可验证的工程查询计划。

核心原则：

- 简单具体问题走 `direct_doc_search`，不做重规划。
- App/页面/功能目标走 `app_goal_planning`，先拆能力再检索。
- 构建和运行问题分别走 `build_diagnosis`、`runtime_diagnosis`，以日志和事实为输入。
- 查询计划只解决“该查什么”，不替代代码实现和构建验证。

## 路由判定

`direct_doc_search`：

- 用户问“XX 怎么用”“XX 参数是什么”“XX 示例在哪”
- 用户给出明确 API、组件、属性、错误码或模块名
- 输出 1-2 条查询即可，优先 `api` 或 `example`

`app_goal_planning`：

- 用户要求“开发一个 App”“做一个页面”“实现一个功能”
- 用户只描述业务目标，没有给出完整组件/API 方案
- 必须输出页面/模块、能力拆解、查询计划和验收点

`build_diagnosis`：

- 用户给出编译错误、构建失败、类型不匹配、模块找不到
- 先读 `build.log` 和 `Evolution.md`，再按错误关键词检索

`runtime_diagnosis`：

- 用户反馈白屏、崩溃、点击无效、权限拒绝、数据不显示
- 先采集截图、控件树和 hilog，再反推查询计划

## 查询计划字段

每条查询计划包含：

```text
query: 传给 search_v3.py 的自然语言查询
mode: auto|task|api|example|doc
purpose: 本次查询要确认的 API、组件、参数、示例、权限或排错依据
capability: arkui_component|navigation|network|storage|permission|ability|media|security|interop|diagnostics|build|runtime
```

## 常见 App 模板

### 聊天 App

能力拆解：

- 消息列表：`List`、`ListItem`、长列表性能、滚动到底部
- 输入发送：`TextInput`、`Button`、状态更新、键盘相关布局
- 会话跳转：会话列表页到聊天详情页，路由或 `Navigation`
- 网络：HTTP 或实时通信方案，header、超时、错误处理
- 本地历史：`RelationalStore`、文件或首选项存储
- 状态管理：`@State`、`AppStorage`、局部状态与全局状态边界

推荐查询：

- `聊天消息列表 List ListItem 滚动到底部`
- `TextInput 输入框 Button 发送按钮 布局 示例`
- `Navigation 路由页面跳转`
- `仓颉 App 发起 HTTP 请求并设置 header`
- `用 RelationalStore 保存列表数据怎么开始`
- `@State 状态管理`

### 待办 App

能力拆解：

- 待办列表：`List`、`ListItem`
- 新增/编辑：`TextInput`、`Button`、弹窗或页面跳转
- 完成/删除：点击事件、状态更新、确认弹窗
- 本地持久化：首选项、文件或 `RelationalStore`

推荐查询：

- `我要做一个待办事项列表页面，List 和点击事件怎么写`
- `用户点击删除按钮前弹出确认 AlertDialog`
- `TextInput 输入框 Button 布局 示例`
- `用 RelationalStore 保存列表数据怎么开始`

### 图片相册 App

能力拆解：

- 图片网格/列表：`Grid`、`List` 或 `Flex`
- 图片显示：`Image`、`objectFit`、占位与裁剪
- 详情页：路由跳转、缩放或预览
- 权限与媒体访问：相册/文件权限、资源加载

推荐查询：

- `我要做一个图片列表，Image 加载和 List 布局怎么组合`
- `头像图片要裁剪适配，Image objectFit 怎么设置`
- `Flex 和 Row Column 哪个适合做自适应卡片布局`
- `相机权限 权限申请`

### 登录/表单页面

能力拆解：

- 表单布局：`Column`、`TextInput`、`Button`
- 输入校验：状态管理、错误提示、禁用按钮
- 网络登录：HTTP 请求、header、超时、错误处理
- 安全存储：token 存储、加密或首选项

推荐查询：

- `我要做一个登录表单，TextInput 和 Button 怎么布局`
- `仓颉 App 发起 HTTP 请求并设置 header`
- `AppStorage 保存全局 UI 状态怎么用`
- `仓颉 App 需要 AES 或 HUKS 加密数据怎么查文档`

## 质量门禁

- 查询计划必须覆盖所有关键能力，不得只保留 UI 查询。
- 每条 query 应是用户态自然语言，不写内部路径或 eval 字段。
- 不确定的 API 名不能直接写进代码，必须先查 `api/example`。
- 查询无关时先换 query，不要把低相关结果硬解释成依据。
