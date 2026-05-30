## class AbilityLifecycleCallback

```cangjie
public class AbilityLifecycleCallback {
    public AbilityLifecycleCallback(
        public let onAbilityCreate!: (UIAbility) -> Unit,
        public let onWindowStageCreate!: (UIAbility, WindowStage) -> Unit,
        public let onWindowStageActive!: (UIAbility, WindowStage) -> Unit,
        public let onWindowStageInactive!: (UIAbility, WindowStage) -> Unit,
        public let onWindowStageDestroy!: (UIAbility, WindowStage) -> Unit,
        public let onAbilityDestroy!: (UIAbility) -> Unit,
        public let onAbilityForeground!: (UIAbility) -> Unit,
        public let onAbilityBackground!: (UIAbility) -> Unit,
        public let onAbilityContinue!: (UIAbility) -> Unit,
        public let onAbilityWillCreate!: ?(UIAbility) -> Unit = None,
        public let onWindowStageWillCreate!: ?(UIAbility, WindowStage) -> Unit = None,
        public let onWindowStageWillDestroy!: ?(UIAbility, WindowStage) -> Unit = None,
        public let onAbilityWillForeground!: ?(UIAbility) -> Unit = None,
        public let onAbilityWillDestroy!: ?(UIAbility) -> Unit = None,
        public let onAbilityWillBackground!: ?(UIAbility) -> Unit = None,
        public let onWillNewWant!: ?(UIAbility) -> Unit = None,
        public let onNewWant!: ?(UIAbility) -> Unit = None,
        public let onAbilityWillContinue!: ?(UIAbility) -> Unit = None,
        public let onWindowStageWillRestore!: ?(UIAbility, WindowStage) -> Unit = None,
        public let onWindowStageRestore!: ?(UIAbility, WindowStage) -> Unit = None,
        public let onAbilityWillSaveState!: ?(UIAbility) -> Unit = None,
        public let onAbilitySaveState!: ?(UIAbility) -> Unit = None
    )
}
```

**功能：** AbilityLifecycleCallback类提供应用上下文的生命周期发生变化时触发相应回调的能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

### let onAbilityBackground

```cangjie
public let onAbilityBackground: (UIAbility) -> Unit
```

**功能：** 注册监听应用上下文的生命周期后，在ability的状态从前台转到后台时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onAbilityContinue

```cangjie
public let onAbilityContinue: (UIAbility) -> Unit
```

**功能：** 注册监听应用上下文的生命周期后，在ability迁移时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onAbilityCreate

```cangjie
public let onAbilityCreate: (UIAbility) -> Unit
```

**功能：** 注册监听应用上下文的生命周期后，在ability创建时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onAbilityDestroy

```cangjie
public let onAbilityDestroy: (UIAbility) -> Unit
```

**功能：** 注册监听应用上下文的生命周期后，在ability销毁时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onAbilityForeground

```cangjie
public let onAbilityForeground: (UIAbility) -> Unit
```

**功能：** 注册监听应用上下文的生命周期后，在ability的状态从后台转到前台时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onAbilitySaveState

```cangjie
public let onAbilitySaveState: ?(UIAbility) -> Unit = None
```

**功能：** 注册监听应用上下文的生命周期后，在Ability的onSaveState触发后回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([UIAbility](#class-uiability))->Unit

**读写能力：** 只读

**起始版本：** 19