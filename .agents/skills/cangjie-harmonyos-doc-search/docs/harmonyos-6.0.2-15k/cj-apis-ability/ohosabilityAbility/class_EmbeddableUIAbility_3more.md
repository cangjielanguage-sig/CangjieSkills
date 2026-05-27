## class EmbeddableUIAbility

```cangjie
public class EmbeddableUIAbility <: UIAbility {}
```

**功能：** [EmbeddableUIAbility](#class-embeddableuiability)是为原子化服务提供可以嵌入式启动的Ability，同时具备跳转启动和嵌入式启动两种启动方式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- [UIAbility](#class-uiability)

## class EmbeddableUIAbilityContext

```cangjie
public class EmbeddableUIAbilityContext <: UIAbilityContext {}
```

**功能：** 提供EmbeddableUIAbility的相关配置信息以及操作EmbeddableUIAbility和ServiceExtensionAbility的方法，如启动EmbeddableUIAbility，停止当前EmbeddableUIAbilityContext所属的EmbeddableUIAbility，启动、停止、连接、断开连接ServiceExtensionAbility等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**父类型：**

- [UIAbilityContext](#class-uiabilitycontext)

## class EmbeddedUIExtensionAbility

```cangjie
public open class EmbeddedUIExtensionAbility <: UIExtensionAbility {}
```

**功能：** EmbeddedUIExtensionAbility为开发者提供了跨进程界面嵌入的能力，继承自[UIExtensionAbility](#class-uiextensionability)。目前EmbeddedUIExtensionAbility只能被同应用的UIAbility拉起，并且仅允许在拥有多进程权限的场景下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**父类型：**

- [UIExtensionAbility](#class-uiextensionability)

### func onCreate()

```cangjie
public open func onCreate(): Unit
```

**功能：** EmbeddedUIExtensionAbility创建时回调，执行初始化业务逻辑操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19