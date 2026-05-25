## class UIAbilityContext

```cangjie
public open class UIAbilityContext <: Context {}
```

**功能：** 提供允许访问特定UIAbility的资源的能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**父类型：**

- [Context](#class-context)

### prop abilityInfo

```cangjie
public prop abilityInfo: AbilityInfo
```

**功能：** [UIAbility](#class-uiability)的相关信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [AbilityInfo](./cj-apis-bundle_manager.md#class-abilityinfo)

**读写能力：** 只读

**起始版本：** 19

### prop config

```cangjie
public prop config: AbilityConfiguration
```

**功能：** 与[UIAbility](#class-uiability)相关的配置信息，如语言、颜色模式等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [AbilityConfiguration](#class-abilityconfiguration)

**读写能力：** 只读

**起始版本：** 19

### prop currentHapModuleInfo

```cangjie
public prop currentHapModuleInfo: HapModuleInfo
```

**功能：** 当前HAP的信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [HapModuleInfo](./cj-apis-bundle_manager.md#struct-hapmoduleinfo)

**读写能力：** 只读

**起始版本：** 19

### prop windowStage

```cangjie
public prop windowStage: ?WindowStage
```

**功能：** 当前WindowStage对象。仅支持在主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [?WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage)

**读写能力：** 只读

**起始版本：** 19

### prop filesDir

```cangjie
public prop filesDir: String
```

**功能：** 文件目录。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12