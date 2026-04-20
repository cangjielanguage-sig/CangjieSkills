### class ScrollResult

```cangjie
public class ScrollResult {
    public var offsetRemain: Float64
    public init(offsetRemain!: Float64)
}
```

**功能：** 表示滚动操作产生的滚动值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var offsetRemain

```cangjie
public var offsetRemain: Float64
```

**功能：** 滚动偏移量剩余值。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(Float64)

```cangjie
public init(offsetRemain!: Float64)
```

**功能：** 构造一个滚动结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offsetRemain|Float64|是|-|滚动偏移量剩余值。|

### class OffsetResult

```cangjie
public class OffsetResult {
    public var xOffset: Float64
    public var yOffset: Float64
    public init(xOffset: Float64, yOffset: Float64)
}
```

**功能：** 表示滚动操作产生的偏移值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var xOffset

```cangjie
public var xOffset: Float64
```

**功能：** 水平滚动偏移。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var yOffset

```cangjie
public var yOffset: Float64
```

**功能：** 垂直滚动偏移。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(Float64, Float64)

```cangjie
public init(xOffset: Float64, yOffset: Float64)
```

**功能：** 构造一个偏移结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|xOffset|Float64|是|-|水平滚动偏移。|
|yOffset|Float64|是|-|垂直滚动偏移。|

### class RectResult

```cangjie
public class RectResult {
    public var x: ?Float64
    public var y: ?Float64
    public var width: ?Float64
    public var height: ?Float64
    public init(
        x: Float64,
        y: Float64,
        width: Float64,
        height: Float64
    )
}
```

**功能：** 表示滚动操作产生的矩形值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var x

```cangjie
public var x: ?Float64
```

**功能：** 矩形值中的x坐标。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var y

```cangjie
public var y: ?Float64
```

**功能：** 矩形值中的y坐标。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var width

```cangjie
public var width: ?Float64
```

**功能：** 矩形值中的宽度。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var height

```cangjie
public var height: ?Float64
```

**功能：** 矩形值中的高度。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(Float64, Float64, Float64, Float64)

```cangjie
public init(
    x: Float64,
    y: Float64,
    width: Float64,
    height: Float64
)
```

**功能：** 构造一个矩形结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|矩形值中的x坐标。|
|y|Float64|是|-|矩形值中的y坐标。|
|width|Float64|是|-|矩形值中的宽度。|
|height|Float64|是|-|矩形值中的高度。|