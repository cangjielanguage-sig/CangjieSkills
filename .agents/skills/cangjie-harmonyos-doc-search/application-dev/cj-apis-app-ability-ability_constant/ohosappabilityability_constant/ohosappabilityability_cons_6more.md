# ohos.app.ability.ability_constant

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

ability_constant模块提供Ability相关的枚举，包括应用启动原因LaunchReason、上次退出原因LastExitReason、迁移结果OnContinueResult等。

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

## class LaunchParam

```cangjie
public class LaunchParam {
    public var launchReason: LaunchReason
    public var lastExitReason: LastExitReason
}
```

**功能：** 启动参数，主要包括Ability启动原因以及上次退出原因。Ability启动时由系统自动传入，开发者无需修改。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var lastExitReason

```cangjie
public var lastExitReason: LastExitReason
```

**功能：** 枚举类型，表示Ability上次退出原因。

**类型：** [LastExitReason](#enum-lastexitreason)

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var launchReason

```cangjie
public var launchReason: LaunchReason
```

**功能：** 枚举类型，表示Ability启动原因（如故障恢复拉起、意图调用拉起、原子化服务分享拉起等），详见[LaunchReason](#enum-launchreason)。

**类型：** [LaunchReason](#enum-launchreason)

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

## enum LastExitReason

```cangjie
public enum LastExitReason {
    | Unknown
    | Normal
    | CppCrash
    | AppFreeze
    | ...
}
```

**功能：** Ability上次退出原因，该类型为枚举，可配合UIAbility的[onCreate(want, launchParam)](./cj-apis-app-ability-ui_ability.md#func-oncreatewant-launchparam)方法根据launchParam.lastExitReason的不同类型执行相应操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### AppFreeze

```cangjie
AppFreeze
```

**功能：** 应用冻屏导致的应用程序退出。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### CppCrash

```cangjie
CppCrash
```

**功能：** 进程崩溃导致的应用程序退出。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### Normal

```cangjie
Normal
```

**功能：** 用户主动关闭，应用程序正常退出。

> **说明：**
>
> 当开发者直接调用内核kill命令等非Ability Kit提供的能力强制退出应用进程时，也会返回Normal。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### Unknown

```cangjie
Unknown
```

**功能：** 未知原因。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22