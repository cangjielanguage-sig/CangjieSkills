## class CustomView

```cangjie
public abstract class CustomView <: RemoteView & Observer {
    public let nativeView: View
    public var isReusable: Bool = false
    public init(parent: Option<CustomView>, localStorage: Option<LocalStorage>)
}
```

**功能：** UI框架使用的组件基础类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [RemoteView](#class-remoteview)
- [Observer](#interface-observer)

### var isReusable

```cangjie
public var isReusable: Bool = false
```

**功能：** UI框架使用。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let nativeView

```cangjie
public let nativeView: View
```

**功能：** UI框架使用。

**类型：** [View](#class-view)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 16

### init(Option\<CustomView>, Option\<LocalStorage>)

```cangjie
public init(parent: Option<CustomView>, localStorage: Option<LocalStorage>)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|parent|Option\<[CustomView](#class-customview)>|是|-|父组件。|
|localStorage|Option\<[LocalStorage](./cj-state-rendering-appstatemanagement.md#class-localstorage)>|是|-|持久化存储对象。|

### static func create(CustomView)

```cangjie
public static func create(view: CustomView)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|view|[CustomView](#class-customview)|是|-|-|

### static func createRecycle(CustomView, Bool, String, () -> Unit)

```cangjie
public static func createRecycle(view: CustomView, isRecycling: Bool, name: String, callback: ()->Unit)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|view|[CustomView](#class-customview)|是|-|-|
|isRecycling|Bool|是|-|-|
|name|String|是|-|-|
|callback|()->Unit|是|-|-|

### func aboutToBeDeleted()

```cangjie
public func aboutToBeDeleted(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func aboutToRecycleInternal()

```cangjie
public override func aboutToRecycleInternal(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### func aboutToReuseInternal(ReuseParams)

```cangjie
public override func aboutToReuseInternal(param: ReuseParams): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|param|[ReuseParams](./cj-custom-component-lifecycle.md#class-reuseparams)|是|-|-|

### func addChildById(Int64, CustomView)

```cangjie
public func addChildById(id: Int64, child: CustomView): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|是|-|-|
|child|[CustomView](#class-customview)|是|-|-|

### func addProvideVar(ObservedPropertyAbstract, String)

```cangjie
public func addProvideVar(value: ObservedPropertyAbstract, name: String)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ObservedPropertyAbstract](#class-observedpropertyabstract)|是|-|-|
|name|String|是|-|-|