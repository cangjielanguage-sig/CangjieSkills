### let onAbilityWillBackground

```cangjie
public let onAbilityWillBackground: ?(UIAbility) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的[onBackground](#func-onbackground)触发前回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onAbilityWillContinue

```cangjie
public let onAbilityWillContinue: ?(UIAbility) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的onContinue触发前回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onAbilityWillCreate

```cangjie
public let onAbilityWillCreate: ?(UIAbility) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的[onCreate](#func-oncreate)触发前回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onAbilityWillDestroy

```cangjie
public let onAbilityWillDestroy: ?(UIAbility) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的[onDestroy](#func-ondestroy)触发前回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onAbilityWillForeground

```cangjie
public let onAbilityWillForeground: ?(UIAbility) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的[onForeground](#func-onforeground)触发前回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onAbilityWillSaveState

```cangjie
public let onAbilityWillSaveState: ?(UIAbility) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的onSaveState触发前回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onNewWant

```cangjie
public let onNewWant: ?(UIAbility) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的[onNewWant](#func-onnewwantwant-launchparam)触发后回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onWillNewWant

```cangjie
public let onWillNewWant: ?(UIAbility) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的[onNewWant](#func-onnewwantwant-launchparam)触发前回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onWindowStageActive

```cangjie
public let onWindowStageActive: (UIAbility, WindowStage) -> Unit
```

**功能：** 注册监听应用上下文的生命周期后，在windowStage获焦时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit

**读写能力：** 只读

**起始版本：** 19