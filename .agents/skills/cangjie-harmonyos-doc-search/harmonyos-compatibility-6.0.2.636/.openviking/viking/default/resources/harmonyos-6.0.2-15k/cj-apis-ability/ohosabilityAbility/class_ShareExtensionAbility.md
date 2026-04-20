## class ShareExtensionAbility

```cangjie
public open class ShareExtensionAbility <: UIExtensionAbility {}
```

**功能：** ShareExtensionAbility是为开发者提供分享操作业务模板，继承自[UIExtensionAbility](#class-uiextensionability)。ShareExtension为人们提供了一种通过应用程序、社交媒体帐户和其他服务共享当前上下文信息的便捷方式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**父类型：**

- [UIExtensionAbility](#class-uiextensionability)

### func onCreate()

```cangjie
public open func onCreate(): Unit
```

**功能：** ShareExtensionAbility创建时回调，执行初始化业务逻辑操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

StartOptions可以作为[startAbility()](#func-startabilitywant)的入参，用于指定目标Ability的窗口模式。