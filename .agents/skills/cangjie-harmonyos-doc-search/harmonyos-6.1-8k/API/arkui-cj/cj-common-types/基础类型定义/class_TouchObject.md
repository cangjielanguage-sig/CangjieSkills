## class TouchObject

```cangjie
public class TouchObject {
    public var touchType: TouchType
    public var id: Int32
    public var screenX: Float64
    public var screenY: Float64
    public var x: Float64
    public var y: Float64
    public init(touchType: TouchType, id: Int32, screenX: Float64, screenY: Float64, x: Float64, y: Float64)
}
```

**功能：** 表示当前发生变化的手指信息类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var id

```cangjie
public var id: Int32
```

**功能：** 手指唯一标识符。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var screenX

```cangjie
public var screenX: Float64
```

**功能：** 触摸点相对于设备屏幕左边沿的X坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var screenY

```cangjie
public var screenY: Float64
```

**功能：** 触摸点相对于设备屏幕上边沿的Y坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var touchType

```cangjie
public var touchType: TouchType
```

**功能：** 触摸事件的类型。

**类型：** [TouchType](cj-common-types.md#enum-touchtype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var x

```cangjie
public var x: Float64
```

**功能：** 触摸点相对于被触摸元素左边沿的X坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var y

```cangjie
public var y: Float64
```

**功能：** 触摸点相对于被触摸元素上边沿的Y坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(TouchType, Int32, Float64, Float64, Float64, Float64)

```cangjie
public init(touchType: TouchType, id: Int32, screenX: Float64, screenY: Float64, x: Float64, y: Float64)
```

**功能：** 构造触摸事件类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|touchType|[TouchType](cj-common-types.md#enum-touchtype)|是|-|触摸事件的类型。|
|id|Int32|是|-|手指唯一标识符。|
|screenX|Float64|是|-|触摸点相对于设备屏幕左边沿的X坐标。|
|screenY|Float64|是|-|触摸点相对于设备屏幕上边沿的Y坐标。|
|x|Float64|是|-|触摸点相对于被触摸元素左边沿的X坐标。|
|y|Float64|是|-|触摸点相对于被触摸元素上边沿的Y坐标。|