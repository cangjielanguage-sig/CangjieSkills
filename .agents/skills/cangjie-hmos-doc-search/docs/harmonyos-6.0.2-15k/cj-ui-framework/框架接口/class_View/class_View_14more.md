## class View

```cangjie
public open class View <: ViewBase {}
```

**功能：** UI框架使用的基础类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [ViewBase](#class-viewbase)

### static func create(View)

```cangjie
public static func create(view: View): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|view|[View](#class-view)|是|-|-|

### static func create(Int64)

```cangjie
public static func create(remoteId: Int64): View
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|remoteId|Int64|是|-|-|

**返回值：**

|类型|说明|
|:----|:----|
|[View](#class-view)|-|

### static func createRecycle(View, Bool, String, () -> Unit)

```cangjie
public static func createRecycle(componentCall: View, isRecycling: Bool, reuseId: String, callback: ()->Unit)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|componentCall|[View](#class-view)|是|-|-|
|isRecycling|Bool|是|-|-|
|reuseId|String|是|-|-|
|callback|()->Unit|是|-|-|

### func deletedElmtIdsHaveBeenPurged(ArrayList\<Int64>)

```cangjie
public func deletedElmtIdsHaveBeenPurged(elmtIds: ArrayList<Int64>): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|elmtIds|ArrayList\<Int64>|是|-|-|

### func destroy()

```cangjie
public func destroy(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func finishUpdateFunc(Int64)

```cangjie
public func finishUpdateFunc(elmtId: Int64): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|elmtId|Int64|是|-|-|

### func getDeletedElemtIds()

```cangjie
public func getDeletedElemtIds(): ArrayList<Int64>
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|ArrayList\<Int64>|-|

### func isFirstRender()

```cangjie
public func isFirstRender():Bool
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|-|

### func isStatic()

```cangjie
public func isStatic(): Bool
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|-|

### func markNeedUpdate()

```cangjie
public func markNeedUpdate(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func markStatic()

```cangjie
public func markStatic(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func needsUpdate()

```cangjie
public func needsUpdate(): Bool
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|-|

### func resetRecycleCustomNode()

```cangjie
public func resetRecycleCustomNode()
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19