## class AbilityMonitor

```cangjie
public class AbilityMonitor {
    public AbilityMonitor(
        public var abilityName: String,
        public var moduleName!: String = "",
        public var onAbilityCreate!: ?(UIAbility) -> Unit = None,
        public var onAbilityForeground!: ?(UIAbility) -> Unit = None,
        public var onAbilityBackground!: ?(UIAbility) -> Unit = None,
        public var onAbilityDestroy!: ?(UIAbility) -> Unit = None,
        public var onWindowStageCreate!: ?(UIAbility) -> Unit = None,
        public var onWindowStageRestore!: ?(UIAbility) -> Unit = None,
        public var onWindowStageDestroy!: ?(UIAbility) -> Unit = None
    )
}
```

**功能：** [AbilityMonitor](#class-abilitymonitor)模块提供匹配满足指定条件的受监视能力对象的方法的能力，最近匹配的ability对象将保存在[AbilityMonitor](#class-abilitymonitor)中。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### var abilityName

```cangjie
public var abilityName: String
```

**功能：** 当前[AbilityMonitor](#class-abilitymonitor)绑定的ability名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var moduleName

```cangjie
public var moduleName: String = ""
```

**功能：** 当前[AbilityMonitor](#class-abilitymonitor)绑定的模块名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var onAbilityBackground

```cangjie
public var onAbilityBackground: ?(UIAbility) -> Unit = None
```

**功能：** ability状态变成后台时的回调函数。不设置该属性则不能收到该生命周期回调。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit

**读写能力：** 可读写

**起始版本：** 19

### var onAbilityCreate

```cangjie
public var onAbilityCreate: ?(UIAbility) -> Unit = None
```

**功能：** ability被启动初始化时的回调函数。不设置该属性则不能收到该生命周期回调。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit

**读写能力：** 可读写

**起始版本：** 19

### var onAbilityDestroy

```cangjie
public var onAbilityDestroy: ?(UIAbility) -> Unit = None
```

**功能：** ability被销毁前的回调函数。不设置该属性则不能收到该生命周期回调。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit

**读写能力：** 可读写

**起始版本：** 19

### var onAbilityForeground

```cangjie
public var onAbilityForeground: ?(UIAbility) -> Unit = None
```

**功能：** ability状态变成前台时的回调函数。不设置该属性则不能收到该生命周期回调。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit

**读写能力：** 可读写

**起始版本：** 19

### var onWindowStageCreate

```cangjie
public var onWindowStageCreate: ?(UIAbility) -> Unit = None
```

**功能：** window stage被创建时的回调函数。不设置该属性则不能收到该生命周期回调。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit

**读写能力：** 可读写

**起始版本：** 19

### var onWindowStageDestroy

```cangjie
public var onWindowStageDestroy: ?(UIAbility) -> Unit = None
```

**功能：** window stage被销毁前的回调函数。不设置该属性则不能收到该生命周期回调。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit

**读写能力：** 可读写

**起始版本：** 19

### var onWindowStageRestore

```cangjie
public var onWindowStageRestore: ?(UIAbility) -> Unit = None
```

**功能：** window stage被重载时的回调函数。不设置该属性则不能收到该生命周期回调。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit

**读写能力：** 可读写

**起始版本：** 19