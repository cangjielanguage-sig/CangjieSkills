#### let pinchCenterY

```cangjie
public let pinchCenterY: Float64
```

**功能：** 捏合手势中心点的y轴坐标，单位为vp，用于[PinchGesture](./cj-universal-gesture-pinchgesture.md)手势触发场景。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let repeat

```cangjie
public let repeat: Bool
```

**功能：** 是否为重复触发事件，用于[LongPressGesture](./cj-universal-gesture-longpressgesture.md)手势触发场景。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let scale

```cangjie
public let scale: Float64
```

**功能：** 缩放比例，用于[PinchGesture](./cj-universal-gesture-pinchgesture.md)手势触发场景。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let speed

```cangjie
public let speed: Float64
```

**功能：** 滑动手势速度，即所有手指相对当前组件元素原始区域滑动的平均速度，单位为vp/秒，用于[SwipeGesture](./cj-universal-gesture-swipegesture.md)手势触发场景。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let velocity

```cangjie
public let velocity: Float64
```

**功能：** 用于[PanGesture](./cj-universal-gesture-pangesture.md#pangesture)手势中，获取当前手势的主方向速度。为xy轴方向速度的平方和的算术平方根。单位为vp/s。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let velocityX

```cangjie
public let velocityX: Float64
```

**功能：** 用于[PanGesture](./cj-universal-gesture-pangesture.md#pangesture)手势中，获取当前手势的x轴方向速度。坐标轴原点为屏幕左上角，分正负方向速度，从左往右为正，反之为负。单位为vp/s。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let velocityY

```cangjie
public let velocityY: Float64
```

**功能：** 用于[PanGesture](./cj-universal-gesture-pangesture.md#pangesture)手势中，获取当前手势的y轴方向速度。坐标轴原点为屏幕左上角，分正负方向速度，从上往下为正，反之为负。单位为vp/s。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19