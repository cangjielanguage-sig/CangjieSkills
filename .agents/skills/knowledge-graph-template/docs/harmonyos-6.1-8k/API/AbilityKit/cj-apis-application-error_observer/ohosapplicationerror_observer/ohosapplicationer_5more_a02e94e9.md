# ohos.application.error_observer

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

error_observer模块定义异常监听，可以作为[ErrorManager.on](./cj-apis-app-ability-error_manager.md#static-func-onerrormanagerevent-errorobserver)的入参监听当前应用发生的异常。

## 导入模块

```cangjie
import kit.AbilityKit.*
```

## 权限列表

ohos.permission.DISTRIBUTED_DATASYNC

ohos.permission.PREPARE_APP_TERMINATE

ohos.permission.PRIVACY_WINDOW

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](./cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## class ErrorObject

```cangjie
public class ErrorObject {
    public let name: String
    public let message: String
    public let stack: Option<String>
}
```

**功能：** 包含异常事件名字、消息和错误堆栈信息的对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### let message

```cangjie
public let message: String
```

**功能：** 异常事件的信息。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### let name

```cangjie
public let name: String
```

**功能：** 异常事件的名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### let stack

```cangjie
public let stack: Option<String>
```

**功能：** 异常事件的错误堆栈信息。

**类型：** Option\<String>

**读写能力：** 只读

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22