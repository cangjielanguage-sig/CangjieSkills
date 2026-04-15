## enum OnContinueResult

```cangjie
public enum OnContinueResult {
    | Agree
    | Reject
    | Mismatch
    | ...
}
```

**功能：** Ability迁移结果，该类型为枚举。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### Agree

```cangjie
Agree
```

**功能：** 表示同意。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### Mismatch

```cangjie
Mismatch
```

**功能：** 表示版本不匹配。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### Reject

```cangjie
Reject
```

**功能：** 表示拒绝。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

## enum WindowMode

```cangjie
public enum WindowMode {
    | WindowModeFullscreen
    | WindowModeSplitPrimary
    | WindowModeSplitSecondary
    | ...
}
```

**功能：** 启动UIAbility时窗口的创建模式，类型为枚举。可配合[startAbility](./cj-apis-app-ability-ui_ability.md#func-startabilitywant-startoptions)方法使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### WindowModeFullscreen

```cangjie
WindowModeFullscreen
```

**功能：** 全屏模式。仅在Tablet设备上生效。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### WindowModeSplitPrimary

```cangjie
WindowModeSplitPrimary
```

**功能：** 支持应用内拉起Ability时设置为分屏，左侧分屏。仅在折叠屏和Tablet设备上生效。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### WindowModeSplitSecondary

```cangjie
WindowModeSplitSecondary
```

**功能：** 支持应用内拉起Ability时设置为分屏，右侧分屏。仅在折叠屏和Tablet设备上生效。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22