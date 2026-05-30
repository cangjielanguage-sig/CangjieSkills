## class RectResult

```cangjie
public class RectResult {
    public var x: Float64
    public var y: Float64
    public var width: Float64
    public var height: Float64
    public init(
        x: Float64,
        y: Float64,
        width: Float64,
        height: Float64
    )
}
```

**功能：** 位置和尺寸类型，用于描述组建的位置和高度。通过scroller.getItemRect获取。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var height

```cangjie
public var height: Float64
```

**功能：** 内容高度大小。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var width

```cangjie
public var width: Float64
```

**功能：** 内容宽度大小。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var x

```cangjie
public var x: Float64
```

**功能：** 水平方向横坐标。

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var y

```cangjie
public var y: Float64
```

**功能：** 竖直方向纵坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Float64, Float64, Float64, Float64)

```cangjie
public init(
    x: Float64,
    y: Float64,
    width: Float64,
    height: Float64
)
```

**功能：** 构造一个RectResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|水平方向横坐标。|
|y|Float64|是|-|竖直方向纵坐标。|
|width|Float64|是|-|内容宽度大小。|
|height|Float64|是|-|内容高度大小。|