## enum LaunchReason

```cangjie
public enum LaunchReason {
    | Unknown
    | StartAbility
    | Call
    | Continuation
    | AppRecovery
    | ...
}
```

**功能：** Ability启动原因，该类型为枚举，可配合UIAbility的[onCreate(want, launchParam)](./cj-apis-app-ability-ui_ability.md#func-oncreatewant-launchparam)方法根据launchParam.launchReason的不同类型执行相应操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### AppRecovery

```cangjie
AppRecovery
```

**功能：** 设置应用恢复后，应用故障时自动恢复启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### Call

```cangjie
Call
```

**功能：** 调用启动。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### Continuation

```cangjie
Continuation
```

**功能：** 跨端迁移启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### StartAbility

```cangjie
StartAbility
```

**功能：** 通过[startAbility](./cj-apis-app-ability-ui_ability.md#func-startabilitywant-startoptions)接口启动Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### Unknown

```cangjie
Unknown
```

**功能：** 未知原因。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22