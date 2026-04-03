## enum LastExitReason

```cangjie
public enum LastExitReason {
    | UNKNOWN
    | ABILITY_NOT_RESPONDING
    | NORMAL
    | CPP_CRASH
    | CJ_ERROR
    | APP_FREEZE
    | PERFORMANCE_CONTROL
    | RESOURCE_CONTROL
    | UPGRADE
    | ...
}
```

**功能：** Ability上次退出原因，该类型为枚举，可配合Ability的[onCreate(want, launchParam)](#func-oncreatewant-launchparam)方法根据launchParam.lastExitReason的不同类型执行相应操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### ABILITY_NOT_RESPONDING

```cangjie
ABILITY_NOT_RESPONDING
```

**功能：** ability未响应。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### APP_FREEZE

```cangjie
APP_FREEZE
```

**功能：** 由于watchdog检测出应用Freeze故障，导致应用程序退出。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### CJ_ERROR

```cangjie
CJ_ERROR
```

**功能：** 当应用存在CJ语法错误并未被开发者捕获时，触发CJ_ERROR故障，导致应用程序退出。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### CPP_CRASH

```cangjie
CPP_CRASH
```

**功能：** 本机异常信号，导致应用程序退出。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### NORMAL

```cangjie
NORMAL
```

**功能：** 用户主动关闭，应用程序正常退出。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### PERFORMANCE_CONTROL

```cangjie
PERFORMANCE_CONTROL
```

**功能：** 由于系统性能问题（如设备内存不足），导致应用程序退出。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### RESOURCE_CONTROL

```cangjie
RESOURCE_CONTROL
```

**功能：** 系统资源使用不当，导致应用程序退出。具体错误原因可以通过[LaunchParam.lastExitMessage](#var-lastexitmessage)获取，可能原因如下：

- CPU Highload，CPU高负载。
- CPU_EXT Highload，快速CPU负载检测。
- IO Manage Control，I/O管控。
- App Memory Deterioration，应用内存超限劣化。
- Temperature Control，温度管控。
- Memory Pressure，整机低内存触发按优先级由低到高查杀。

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知原因。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### UPGRADE

```cangjie
UPGRADE
```

**功能：** 应用程序因升级而退出。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19