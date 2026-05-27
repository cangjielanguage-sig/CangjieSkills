## class PluralResource

```cangjie
public class PluralResource {
    public var id: Int64
    public var ty: UInt32
    public var count: Int64
    public var plural: Int64
    public init(id: Int64, ty: UInt32, count: Int64, plural: Int64)
}
```

**功能：** 复数资源，框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var id

```cangjie
public var id: Int64
```

**功能：** 资源的id值。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var ty

```cangjie
public var ty: UInt32
```

**功能：** 资源的类型。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var count

```cangjie
public var count: Int64
```

**功能：** 指定单复数的数量。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var plural

```cangjie
public var plural: Int64
```

**功能：** 复数值。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(Int64, UInt32, String)

```cangjie
public init(id: Int64, ty: UInt32, params: String)
```

**功能：** 创建PluralResource类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|是|-|资源的id值。|
|ty|UInt32|是|-|资源的类型。|
|count|Int64|是|-|指定单复数的数量。|
|plural|Int64|是|-|复数值。|

## class RemoteView

```cangjie
public abstract class RemoteView{
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
public func build(): Unit // abstract
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func purgeVariableDependenciesOnElmtId(Int64)

```cangjie
public open func purgeVariableDependenciesOnElmtId(removedElmtId: Int64): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|removedElmtId|Int64|是|-|待移除元素id。|

### func rerender()

```cangjie
public open func rerender(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12