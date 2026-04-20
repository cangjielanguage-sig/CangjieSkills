## class CustomView

```cangjie
public abstract class CustomView <: RemoteView {
}
```

**功能：** UI框架使用的组件基础类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [RemoteView](#class-remoteview)

> **说明：**
>
> 该类型仅供框架内部使用，应用开发者请勿使用，否则可能产生不可预期的行为。

### func getLocalStorage()

```cangjie
public func getLocalStorage(): LocalStorage
```

**功能：** 获取LocalStorage实例。仅供UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[LocalStorage](./cj-state-rendering-appstatemanagement.md#class-localstorage)|持久化存储对象。|

> **说明：**
>
> 该接口仅供框架内部使用，应用开发者请勿调用，否则可能产生不可预期的行为。

### func build()

```cangjie
public func build(): Unit
```

**功能：** 用于定义自定义组件的声明式UI描述，自定义组件必须定义build()函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func aboutToBeDeleted()

```cangjie
public func aboutToBeDeleted(): Unit
```

**功能：** 组件销毁阶段由框架自动触发。仅供UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

> **说明：**
>
> 该接口仅供框架内部使用，应用开发者请勿调用，否则可能产生不可预期的行为。

### func getUIContext()

```cangjie
public func getUIContext(): UIContext
```

**功能：** 获取UIContext对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[UIContext](./cj-apis-uicontext-uicontext.md#class-uicontext)|UI上下文。|

> **说明：**
>
> 该接口仅供框架内部使用，应用开发者请勿调用，否则可能产生不可预期的行为。