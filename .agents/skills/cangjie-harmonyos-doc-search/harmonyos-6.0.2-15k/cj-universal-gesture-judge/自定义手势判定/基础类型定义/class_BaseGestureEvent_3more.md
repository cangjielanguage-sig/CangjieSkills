### class BaseGestureEvent

```cangjie
public open class BaseGestureEvent <: BaseEvent {
    public let fingerList: ArrayList<FingerInfo>
}
```

**功能：** 基础手势事件信息的基类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [BaseEvent](#class-baseevent)

#### let fingerList

```cangjie
public let fingerList: ArrayList<FingerInfo>
```

**功能：** 触发事件的所有手指信息。

**类型：** ArrayList\<[FingerInfo](./cj-universal-gesture-bind.md#class-fingerinfo)>

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### class LongPressGestureEvent

```cangjie
public class LongPressGestureEvent <: BaseGestureEvent {
    public let repeat: Bool
}
```

**功能：** 长按手势的基础手势事件信息，可将该对象作为onGestureJudgeBegin的event参数来传递。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [BaseGestureEvent](#class-basegestureevent)

#### let repeat

```cangjie
public let repeat: Bool
```

**功能：** 是否为重复触发事件。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### class PanGestureEvent

```cangjie
public class PanGestureEvent <: BaseGestureEvent {
    public let offsetX: Float64
    public let offsetY: Float64
    public let velocityX: Float64
    public let velocityY: Float64
    public let velocity: Float64
}
```

**功能：** 滑动手势的基础手势事件信息，可将该对象作为onGestureJudgeBegin的event参数来传递。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [BaseGestureEvent](#class-basegestureevent)

#### let offsetX

```cangjie
public let offsetX: Float64
```

**功能：** 手势事件偏移量X，单位为vp，从左向右滑动offsetX为正，反之为负。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let offsetY

```cangjie
public let offsetY: Float64
```

**功能：** 手势事件偏移量Y，单位为vp，从上向下滑动offsetY为正，反之为负。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let velocity

```cangjie
public let velocity: Float64
```

**功能：** 获取当前手势的主方向速度。为xy轴方向速度的平方和的算术平方根。单位为vp/s。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let velocityX

```cangjie
public let velocityX: Float64
```

**功能：** 获取当前手势的x轴方向速度。坐标轴原点为屏幕左上角，分正负方向速度，从左往右为正，反之为负。单位为vp/s。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let velocityY

```cangjie
public let velocityY: Float64
```

**功能：** 获取当前手势的y轴方向速度。坐标轴原点为屏幕左上角，分正负方向速度，从上往下为正，反之为负。单位为vp/s。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19