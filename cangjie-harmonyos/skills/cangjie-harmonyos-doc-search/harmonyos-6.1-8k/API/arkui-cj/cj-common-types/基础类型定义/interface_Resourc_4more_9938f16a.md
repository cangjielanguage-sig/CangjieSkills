## interface ResourceColor

```cangjie
public interface ResourceColor {
    func toUInt32(): UInt32
}
```

**功能：** Color、UInt32、Int64、AppResource 均实现了 ResourceColor 接口类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### extend Int64 <: ResourceColor

```cangjie
extend Int64 <: ResourceColor {
    public func toUInt32(): UInt32
}
```

**功能：** 扩展Int64为ResourceColor子类型。

#### func toUInt32()

```cangjie
public func toUInt32(): UInt32
```

**功能：** 转为UInt32颜色取值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|ResourceColor的UInt32值。|

### extend UInt32 <: ResourceColor

```cangjie
extend UInt32 <: ResourceColor {
    public func toUInt32(): UInt32
}
```

**功能：** 扩展UInt32为ResourceColor子类型。

#### func toUInt32()

```cangjie
public func toUInt32(): UInt32
```

**功能：** 转为UInt32颜色取值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|ResourceColor的UInt32值。|

### func toUInt32()

```cangjie
func toUInt32(): UInt32
```

**功能：** 转为UInt32颜色取值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|ResourceColor的UInt32值。|

## interface ResourceStr

```cangjie
public interface ResourceStr {}
```

**功能：** 字符串类型，用于描述字符串入参可以使用的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### extend String <: ResourceStr

```cangjie
extend String <: ResourceStr {}
```

**功能：** 扩展String为ResourceStr子类。

## interface TextContentControllerBase

```cangjie
public interface TextContentControllerBase {}
```

**功能：** 文本内容控制器基础接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

## class Bindable\<T>

```cangjie
public class Bindable<T> {
    public let value: T
    public let onChange: (T) -> Unit
    public init(value: T, onChange: (T) -> Unit)
}
```

**功能：** 定义可绑定属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(T, (T) -> Unit)

```cangjie
public init(value: T, onChange: (T) -> Unit)
```

**功能：** Bindable构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|T|是|-|可绑定属性的值。|
|onChange|(T) -> Unit|是|-|可绑定属性的回调函数，当属性改变时将调用该回调函数。|

### let value

```cangjie
public let value: T
```

**功能：** 定义可绑定属性的值。

**类型：** T

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### let onChange

```cangjie
public let onChange: (T) -> Unit
```

**功能：** 可绑定属性的回调函数，当属性改变时将调用该回调函数。

**类型：** (T) -> Unit

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22