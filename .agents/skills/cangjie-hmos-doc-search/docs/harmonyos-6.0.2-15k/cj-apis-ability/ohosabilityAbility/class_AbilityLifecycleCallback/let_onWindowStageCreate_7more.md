### let onWindowStageCreate

```cangjie
public let onWindowStageCreate: (UIAbility, WindowStage) -> Unit
```

**功能：** 注册监听应用上下文的生命周期后，在windowStage创建时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onWindowStageDestroy

```cangjie
public let onWindowStageDestroy: (UIAbility, WindowStage) -> Unit
```

**功能：** 注册监听应用上下文的生命周期后，在windowStage销毁时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onWindowStageInactive

```cangjie
public let onWindowStageInactive: (UIAbility, WindowStage) -> Unit
```

**功能：** 注册监听应用上下文的生命周期后，在windowStage失焦时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onWindowStageRestore

```cangjie
public let onWindowStageRestore: ?(UIAbility, WindowStage) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的onWindowStageRestore触发后回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onWindowStageWillCreate

```cangjie
public let onWindowStageWillCreate: ?(UIAbility, WindowStage) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的[onWindowStageCreate](#func-onwindowstagecreatewindowstage)触发前回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onWindowStageWillDestroy

```cangjie
public let onWindowStageWillDestroy: ?(UIAbility, WindowStage) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的[onWindowStageDestroy](#func-onwindowstagedestroy)触发前回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onWindowStageWillRestore

```cangjie
public let onWindowStageWillRestore: ?(UIAbility, WindowStage) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的onWindowStageRestore触发前回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit

**读写能力：** 只读

**起始版本：** 19