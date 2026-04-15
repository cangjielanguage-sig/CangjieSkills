## class AbilityMonitor

```cangjie
public class AbilityMonitor {
    public var abilityName: String
    public var moduleName: String
    public var onAbilityCreate:?(UIAbility) -> Unit
    public var onAbilityForeground:?(UIAbility) -> Unit
    public var onAbilityBackground:?(UIAbility) -> Unit
    public var onAbilityDestroy:?(UIAbility) -> Unit
    public var onWindowStageCreate:?(UIAbility) -> Unit
    public var onWindowStageRestore:?(UIAbility) -> Unit
    public var onWindowStageDestroy:?(UIAbility) -> Unit
    public init(
        abilityName: String,
        moduleName!: String = "",
        onAbilityCreate!: ?(UIAbility) -> Unit = None,
        onAbilityForeground!: ?(UIAbility) -> Unit = None,
        onAbilityBackground!: ?(UIAbility) -> Unit = None,
        onAbilityDestroy!: ?(UIAbility) -> Unit = None,
        onWindowStageCreate!: ?(UIAbility) -> Unit = None,
        onWindowStageRestore!: ?(UIAbility) -> Unit = None,
        onWindowStageDestroy!: ?(UIAbility) -> Unit = None
    )
}
```

**功能：** [AbilityMonitor](#class-abilitymonitor)模块提供匹配满足指定条件的受监视能力对象的方法的能力，最近匹配的ability对象将保存在[AbilityMonitor](#class-abilitymonitor)中。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var abilityName

```cangjie
public var abilityName: String
```

**功能：** 被监听的UIAbility对象名称。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var moduleName

```cangjie
public var moduleName: String
```

**功能：** 被监听的UIAbility对象所属模块名称。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var onAbilityBackground

```cangjie
public var onAbilityBackground:?(UIAbility) -> Unit
```

**功能：** UIAbility对象状态变成后台时，触发该回调函数。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability))->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var onAbilityCreate

```cangjie
public var onAbilityCreate:?(UIAbility) -> Unit
```

**功能：** UIAbility对象被创建时，触发该回调函数。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability))->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var onAbilityDestroy

```cangjie
public var onAbilityDestroy:?(UIAbility) -> Unit
```

**功能：** UIAbility对象被销毁前，触发该回调函数。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability))->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var onAbilityForeground

```cangjie
public var onAbilityForeground:?(UIAbility) -> Unit
```

**功能：** UIAbility对象状态变成前台时，触发该回调函数。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability))->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var onWindowStageCreate

```cangjie
public var onWindowStageCreate:?(UIAbility) -> Unit
```

**功能：** 当WindowStage实例被创建时，触发该回调函数。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability))->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22