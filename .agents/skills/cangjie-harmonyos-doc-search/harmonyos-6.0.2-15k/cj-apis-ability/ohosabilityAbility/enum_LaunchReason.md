## enum LaunchReason

```cangjie
public enum LaunchReason {
    | UNKNOWN
    | START_ABILITY
    | CALL
    | CONTINUATION
    | APP_RECOVERY
    | SHARE
    | AUTO_STARTUP
    | INSIGHT_INTENT
    | PREPARE_CONTINUATION
    | ...
}
```

**功能：** Ability初次启动原因，该类型为枚举，可配合Ability的[onCreate(want, launchParam)](#func-oncreatewant-launchparam)方法根据launchParam.launchReason的不同类型执行相应操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### APP_RECOVERY

```cangjie
APP_RECOVERY
```

**功能：** 设置应用恢复后，应用故障时自动恢复启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### AUTO_STARTUP

```cangjie
AUTO_STARTUP
```

**功能：** 通过设置开机自启动来启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### CALL

```cangjie
CALL
```

**功能：** 通过startAbilityByCall接口启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### CONTINUATION

```cangjie
CONTINUATION
```

**功能：** 跨端迁移启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### INSIGHT_INTENT

```cangjie
INSIGHT_INTENT
```

**功能：** 通过洞察意图来启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### PREPARE_CONTINUATION

```cangjie
PREPARE_CONTINUATION
```

**功能：** 跨端迁移提前启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### SHARE

```cangjie
SHARE
```

**功能：** 通过原子化服务分享启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### START_ABILITY

```cangjie
START_ABILITY
```

**功能：** 通过[startAbility](#func-startabilitywant)接口启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知原因。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12