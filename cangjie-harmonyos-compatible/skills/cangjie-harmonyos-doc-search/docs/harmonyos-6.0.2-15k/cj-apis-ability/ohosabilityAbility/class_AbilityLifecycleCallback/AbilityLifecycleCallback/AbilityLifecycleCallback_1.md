### AbilityLifecycleCallback(...)

```cangjie
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
```

**功能：** AbilityLifecycleCallback类的主构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**