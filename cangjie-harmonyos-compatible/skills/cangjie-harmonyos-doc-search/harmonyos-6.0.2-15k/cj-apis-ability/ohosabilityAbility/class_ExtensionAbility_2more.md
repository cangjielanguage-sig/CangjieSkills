## class ExtensionAbility

```cangjie
abstract sealed class ExtensionAbility <: BaseAbility {}
```

**功能：** ExtensionAbility是特定场景扩展能力的基类，继承自[BaseAbility](#class-baseability)，未新增属性和方法。不支持开发者直接继承该基类。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**父类型：**

- [BaseAbility](#class-baseability)

## class ExtensionContext

```cangjie
public open class ExtensionContext <: Context {}
```

**功能：** 提供访问特定Extension的资源的能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- [Context](#class-context)

### prop config

```cangjie
public prop config: AbilityConfiguration
```

**功能：** 所属Module的配置信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [AbilityConfiguration](#class-abilityconfiguration)

**读写能力：** 只读

**起始版本：** 19

### prop currentHapModuleInfo

```cangjie
public prop currentHapModuleInfo: HapModuleInfo
```

**功能：** 所属Hap包的信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [HapModuleInfo](./cj-apis-bundle_manager.md#struct-hapmoduleinfo)

**读写能力：** 只读

**起始版本：** 19

### prop extensionAbilityInfo

```cangjie
public prop extensionAbilityInfo: ExtensionAbilityInfo
```

**功能：** 所属Extension的信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [ExtensionAbilityInfo](cj-apis-bundle_manager.md#class-extensionabilityinfo)

**读写能力：** 只读

**起始版本：** 19