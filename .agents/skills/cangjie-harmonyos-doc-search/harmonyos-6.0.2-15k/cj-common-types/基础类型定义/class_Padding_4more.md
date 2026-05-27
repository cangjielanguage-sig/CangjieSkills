## class Padding

```cangjie
public class Padding {
    public let top: Length
    public let right: Length
    public let bottom: Length
    public let left: Length
    public Padding(
        top!: Length = 17.0.vp,
        right!: Length = 8.0.vp,
        bottom!: Length = 18.0.vp,
        left!: Length = 8.0.vp
    )
}
```

**功能：** 内边距类型，用于描述组件不同方向的内边距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let bottom

```cangjie
public let bottom: Length
```

**功能：** 下内边距，组件内元素距组件底部的尺寸。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let left

```cangjie
public let left: Length
```

**功能：** 左内边距，组件内元素距组件左边界的尺寸。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let right

```cangjie
public let right: Length
```

**功能：** 右内边距，组件内元素距组件右边界的尺寸。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let top

```cangjie
public let top: Length
```

**功能：** 上内边距，组件内元素距组件顶部的尺寸。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## class Position

```cangjie
public class Position {
    public Position(
        public var x: Float64,
        public var y: Float64
    )
}
```

**功能：** 位置信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var x

```cangjie
public var x: Float64
```

**功能：** 定义x轴坐标。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

### var y

```cangjie
public var y: Float64
```

**功能：** 定义y轴坐标。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

### Position(Float64, Float64)

```cangjie
public Position(
    public var x: Float64,
    public var y: Float64
)
```

**功能：** 构造一个Position类型的对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|x轴坐标，单位为vp。|
|y|Float64|是|-|y轴坐标，单位为vp。|

## enum AccessibilityHoverType

```cangjie
public enum AccessibilityHoverType {
    | HOVER_ENTER
    | HOVER_MOVE
    | HOVER_EXIT
    | HOVER_CANCEL
}
```

**功能：** 无障碍悬浮类型类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### HOVER_CANCEL

```cangjie
HOVER_CANCEL
```

**功能：** 打断取消当前触发的事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### HOVER_ENTER

```cangjie
HOVER_ENTER
```

**功能：** 手指按下时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### HOVER_EXIT

```cangjie
HOVER_EXIT
```

**功能：** 抬手触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### HOVER_MOVE

```cangjie
HOVER_MOVE
```

**功能：** 触摸移动时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum AdaptiveColor

```cangjie
public enum AdaptiveColor {
    | DEFAULT
    | AVERAGE
}
```

**功能：** 取色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### AVERAGE

```cangjie
AVERAGE
```

**功能：** 使用取色模糊。将取色区域的颜色平均值作为蒙版颜色。

**起始版本：** 12

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 不使用取色模糊。使用默认的颜色作为蒙版颜色。

**起始版本：** 12