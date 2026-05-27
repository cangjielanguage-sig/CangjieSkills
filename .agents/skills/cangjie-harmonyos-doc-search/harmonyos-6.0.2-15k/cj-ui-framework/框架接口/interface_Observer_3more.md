## interface Observer

```cangjie
public interface Observer {
    func onStateUpdate(info: String, dependentElmtIds: ArrayList<Int64>): Unit
    func onStateUpdate(info: String): Unit
    func notifyRead(info: String): Unit
    func id(): Int64
    func aboutToBeDeleted(): Unit
}
```

**功能：** 持久化存储基类。内部接口，框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func aboutToBeDeleted()

```cangjie
func aboutToBeDeleted(): Unit
```

**功能：** 删除持久化存储对象，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func id()

```cangjie
func id(): Int64
```

**功能：** 获取持久化存储对象id。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|持久化存储对象id。|

### func notifyRead(String)

```cangjie
func notifyRead(info: String): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|String|是|-|-|

### func onStateUpdate(String, ArrayList\<Int64>)

```cangjie
func onStateUpdate(info: String, dependentElmtIds: ArrayList<Int64>): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|String|是|-|-|
|dependentElmtIds|ArrayList\<Int64>|是|-|-|

### func onStateUpdate(String)

```cangjie
func onStateUpdate(info: String): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|String|是|-|-|

## class BaseView

```cangjie
public abstract class BaseView {
    public init()
}
```

**功能：** UI框架使用的组件基础类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init()

```cangjie
public init()
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func build()

```cangjie
public open func build(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func rerender()

```cangjie
public open func rerender(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## class CJEntry

```cangjie
public class CJEntry {}
```

**功能：** 用于提供被Native调用的全局函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static func getInstance()

```cangjie
public static func getInstance(): CJEntry
```

**功能：** 创建并返回CJEntry对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[CJEntry](#class-cjentry)|对应的CJEntry对象。|

### func registerEntry(String, () -> Bool)

```cangjie
public func registerEntry(name: String, call: ()->Bool): Unit
```

**功能：** 设置应用开发者注册的应用入口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|注册名称。|
|call|()->Bool|是|-|回调函数。|