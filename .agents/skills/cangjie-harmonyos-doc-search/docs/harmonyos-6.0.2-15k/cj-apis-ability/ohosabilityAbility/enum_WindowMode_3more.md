## enum WindowMode

```cangjie
public enum WindowMode {
    | WINDOW_MODE_UNDEFINED
    | WINDOW_MODE_FULLSCREEN
    | WINDOW_MODE_SPLIT_PRIMARY
    | WINDOW_MODE_SPLIT_SECONDARY
    | ...
}
```

**功能：** 启动Ability时的窗口模式，类型为枚举。可配合[startAbility](#func-startabilitywant-startoptions)使用，指定启动Ability的窗口模式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### WINDOW_MODE_FULLSCREEN

```cangjie
WINDOW_MODE_FULLSCREEN
```

**功能：** 全屏模式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### WINDOW_MODE_SPLIT_PRIMARY

```cangjie
WINDOW_MODE_SPLIT_PRIMARY
```

**功能：** 屏幕如果是水平方向表示左分屏，屏幕如果是竖直方向表示上分屏。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### WINDOW_MODE_SPLIT_SECONDARY

```cangjie
WINDOW_MODE_SPLIT_SECONDARY
```

**功能：** 屏幕如果是水平方向表示右分屏，屏幕如果是竖直方向表示下分屏。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### WINDOW_MODE_UNDEFINED

```cangjie
WINDOW_MODE_UNDEFINED
```

**功能：** 未定义窗口模式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

## type Ability

```cangjie
public type Ability = UIAbility
```

**功能：** UIAbility的别名，已废弃。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## type AbilityContext

```cangjie
public type AbilityContext = UIAbilityContext
```

**功能：** UIAbilityContext的别名，已废弃。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core