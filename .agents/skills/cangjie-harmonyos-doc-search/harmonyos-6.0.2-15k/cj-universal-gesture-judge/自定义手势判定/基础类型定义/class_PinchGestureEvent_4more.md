### class PinchGestureEvent

```cangjie
public class PinchGestureEvent <: BaseGestureEvent {
    public let scale: Float64
    public let pinchCenterX: Float64
    public let pinchCenterY: Float64
}
```

**功能：** 捏合手势的基础手势事件信息，可将该对象作为onGestureJudgeBegin的event参数来传递。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [BaseGestureEvent](#class-basegestureevent)

#### let pinchCenterX

```cangjie
public let pinchCenterX: Float64
```

**功能：** 捏合手势中心点相对于当前组件元素原始区域左上角x轴坐标，单位为vp。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let pinchCenterY

```cangjie
public let pinchCenterY: Float64
```

**功能：** 捏合手势中心点相对于当前组件元素原始区域左上角y轴坐标，单位为vp。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let scale

```cangjie
public let scale: Float64
```

**功能：** 缩放比例。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### class RotationGestureEvent

```cangjie
public class RotationGestureEvent <: BaseGestureEvent {
    public let angle: Float64
}
```

**功能：** 旋转手势的基础手势事件信息，可将该对象作为onGestureJudgeBegin的event参数来传递。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [BaseGestureEvent](#class-basegestureevent)

#### let angle

```cangjie
public let angle: Float64
```

**功能：** 表示旋转角度，单位为deg。以起始线条为坐标系，顺时针旋转为0到180度，逆时针旋转为-180到0度。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### class SwipeGestureEvent

```cangjie
public class SwipeGestureEvent <: BaseGestureEvent {
    public let angle: Float64
    public let speed: Float64
}
```

**功能：** swipe手势的基础手势事件信息，可将该对象作为onGestureJudgeBegin的event参数来传递。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [BaseGestureEvent](#class-basegestureevent)

#### let angle

```cangjie
public let angle: Float64
```

**功能：** 表示滑动手势的角度，即两根手指间的线段与水平方向的夹角变化的度数，单位为deg。以起始线条为坐标系，顺时针旋转为0到180度，逆时针旋转为-180到0度。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let speed

```cangjie
public let speed: Float64
```

**功能：** 滑动手势速度，即所有手指相对当前组件元素原始区域滑动的平均速度，单位为vp/s。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### class TapGestureEvent

```cangjie
public class TapGestureEvent <: BaseGestureEvent {}
```

**功能：** 点击手势的基础手势事件信息，可将该对象作为onGestureJudgeBegin的event参数来传递。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**父类型：**

- [BaseGestureEvent](#class-basegestureevent)