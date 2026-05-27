# aa工具

Ability assistant（Ability助手，简称为aa），是用于启动应用和启动测试用例的工具，为开发者提供基本的应用调试和测试能力，例如启动应用组件、强制停止进程、打印应用组件相关信息等。

## 环境要求

在使用本工具前，开发者需要先获取hdc工具，执行hdc shell。

本文中命令介绍均基于交互式命令环境。如果直接执行`hdc shell [aa命令]`，则需要采用""来包裹aa命令，确保命令中的传参能被正确识别。示例如下：

```bash
# 启动命令
hdc shell "aa start -A ohos.want.action.viewData -U 'https://www.example.com'"

# 应用调试/调优命令
hdc shell "aa process -b com.example.myapplication -a EntryAbility -p perf-cmd"
```

## aa工具命令列表

| 命令 | 描述 |
|--------|--------|
| -h/help | 帮助命令。用于查询aa支持的命令信息。|
| start | 启动命令。用于启动一个应用组件，目标组件可以是Stage模型的UIAbility或ServiceExtensionAbility组件，且目标组件相应配置文件中的exported标签不能配置为false。|
| force-stop | 强制停止进程命令。通过bundleName强制停止一个进程。|
| test | 启动测试框架命令。根据所携带的参数启动测试框架。 |
| attach | 进入调试模式命令。通过bundleName使指定应用进入调试模式。|
| detach | 退出调试模式命令。通过bundleName使指定应用退出调试模式。|
| appdebug | 等待调试命令。用于设置、取消设置应用等待调试状态，以及获取处于等待调试状态的应用包名和持久化信息。等待调试状态只对debug类型应用生效。appdebug的设置命令只对单个应用生效，当重复设置时，应用包名与持久化状态会替换成最新设置内容。|
| process | 应用调试/调优命令。对应用进行调试或调优，IDE用该命令集成调试和调优工具。|

## 帮助命令（help）

```bash
# 显示帮助信息
aa help
```