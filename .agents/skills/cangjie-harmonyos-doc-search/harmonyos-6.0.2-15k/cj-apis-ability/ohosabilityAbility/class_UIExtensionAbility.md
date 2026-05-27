## class UIExtensionAbility

```cangjie
public open class UIExtensionAbility <: ExtensionAbility {}
```

**功能：** UIExtensionAbility是特定场景下带界面扩展能力的基类，继承自[ExtensionAbility](#class-extensionability)，新增带界面扩展能力相关的属性和方法。不支持开发者直接继承该基类。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**父类型：**

- [ExtensionAbility](#class-extensionability)

### prop context

```cangjie
public prop context: UIExtensionContext
```

**功能：** 获取UIExtensionAbility的上下文。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [UIExtensionContext](#class-uiextensioncontext)

**读写能力：** 只读

**起始版本：** 19

### func onBackground()

```cangjie
public open func onBackground(): Unit
```

**功能：** UIExtensionAbility生命周期回调，当UIExtensionAbility从前台转到后台时触发。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

### func onCreate(LaunchParam)

```cangjie
public open func onCreate(launchParam: LaunchParam): Unit
```

**功能：** UIExtensionAbility创建时回调，执行初始化业务逻辑操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|launchParam|[LaunchParam](#class-launchparam)|是|-|创建UIExtensionAbility、上次异常退出的原因信息。|

### func onDestroy()

```cangjie
public open func onDestroy(): Unit
```

**功能：** UIExtensionAbility生命周期回调，在销毁时回调，执行资源清理等操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func onForeground()

```cangjie
public open func onForeground(): Unit
```

**功能：** UIExtensionAbility生命周期回调，当UIExtensionAbility从后台转到前台时触发。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func onSessionCreate(Want, UIExtensionContentSession)

```cangjie
public open func onSessionCreate(want: Want, session: UIExtensionContentSession): Unit
```

**功能：** 当UIExtensionAbility界面内容对象创建后调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](#class-want)|是|-|当前UIExtensionAbility的Want类型信息，包括ability名称、bundle名称等。|
|session|[UIExtensionContentSession](#class-uiextensioncontentsession)|是|-|UIExtensionAbility界面内容相关信息。|

### func onSessionDestroy(UIExtensionContentSession)

```cangjie
public open func onSessionDestroy(session: UIExtensionContentSession): Unit
```

**功能：** 当UIExtensionAbility界面内容对象销毁后调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|session|[UIExtensionContentSession](#class-uiextensioncontentsession)|是|-|UIExtensionAbility界面内容相关信息。|