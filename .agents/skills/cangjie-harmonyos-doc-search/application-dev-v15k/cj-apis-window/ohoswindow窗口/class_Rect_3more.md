## class Rect

```cangjie
public class Rect {
    public Rect(
        public var left: Int32,
        public var top: Int32,
        public var width: UInt32,
        public var height: UInt32
    )
}
```

**功能：** 窗口矩形区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### var left

```cangjie
public var left: Int32
```

**功能：** 设置矩形区域的左边界，单位为px。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var top

```cangjie
public var top: Int32
```

**功能：** 设置矩形区域的上边界，单位为px。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var width

```cangjie
public var width: UInt32
```

**功能：** 设置矩形区域的宽度，单位为px。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var height

```cangjie
public var height: UInt32
```

**功能：** 设置矩形区域的高度，单位为px。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### Rect(Int32, Int32, UInt32, UInt32)

```cangjie
public Rect(
    public var left: Int32,
    public var top: Int32,
    public var width: UInt32,
    public var height: UInt32
)
```

**功能：** 构建一个Rect类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|Int32|是|-|矩形区域的左边界，单位为px。|
|top|Int32|是|-|矩形区域的上边界，单位为px。|
|width|UInt32|是|-|矩形区域的宽度，单位为px。|
|height|UInt32|是|-|矩形区域的高度，单位为px。|

## class RectChangeOptions

```cangjie
public class RectChangeOptions {
    public RectChangeOptions(
        public var rect: Rect,
        public var reason: RectChangeReason
    )
}
```

**功能：** 窗口矩形（窗口位置及窗口大小）变化返回的值及变化原因。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### var rect

```cangjie
public var rect: Rect
```

**功能：** 表示窗口矩形变化后的值。

**类型：** [Rect](#class-rect)

**读写能力：** 可读写

**起始版本：** 19

### var reason

```cangjie
public var reason: RectChangeReason
```

**功能：** 表示窗口矩形变化的原因。

**类型：** [RectChangeReason](#enum-rectchangereason)

**读写能力：** 可读写

**起始版本：** 19

### RectChangeOptions(Rect, RectChangeReason)

```cangjie
public RectChangeOptions(
    public var rect: Rect,
    public var reason: RectChangeReason
)
```

**功能：** 构建一个RectChangeOptions类型的对象。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rect|[Rect](#class-rect)|是|-|窗口矩形变化后的值。|
|reason|[RectChangeReason](#enum-rectchangereason)|是|-|窗口矩形变化的原因。|

## class Size

```cangjie
public class Size {
    public Size(
        public var width: UInt32,
        public var height: UInt32
    )
}
```

**功能：** 窗口大小。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### var width

```cangjie
public var width: UInt32
```

**功能：** 设置窗口宽度，单位为px。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var height

```cangjie
public var height: UInt32
```

**功能：** 设置窗口高度，单位为px。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### Size(UInt32, UInt32)

```cangjie
public Size(
    public var width: UInt32,
    public var height: UInt32
)
```

**功能：** 构建一个Size类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|UInt32|是|-|窗口宽度，单位为px。|
|height|UInt32|是|-|窗口高度，单位为px。|