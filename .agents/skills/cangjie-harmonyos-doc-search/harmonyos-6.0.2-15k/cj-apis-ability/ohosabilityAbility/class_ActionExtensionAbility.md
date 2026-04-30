## class ActionExtensionAbility

```cangjie
public open class ActionExtensionAbility <: UIExtensionAbility {}
```

**功能：** ActionExtensionAbility是为开发者提供的自定义操作业务模板，继承自[UIExtensionAbility](#class-uiextensionability)。ActionExtensionAbility主要用于查看宿主应用中的内容以及对其进行对应处理。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**父类型：**

- [UIExtensionAbility](#class-uiextensionability)

### func onCreate()

```cangjie
public open func onCreate(): Unit
```

**功能：** ActionExtensionAbility创建时回调，执行初始化业务逻辑操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19