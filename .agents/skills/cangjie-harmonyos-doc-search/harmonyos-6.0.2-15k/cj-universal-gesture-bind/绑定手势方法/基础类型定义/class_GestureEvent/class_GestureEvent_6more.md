### class GestureEvent

```cangjie
public class GestureEvent <: BaseEvent {
    public let repeat: Bool
    public let fingerList: ArrayList<FingerInfo>
    public let offsetX: Float64
    public let offsetY: Float64
    public let scale: Float64
    public let pinchCenterX: Float64
    public let pinchCenterY: Float64
    public let angle: Float64
    public let speed: Float64
    public let velocityX: Float64
    public let velocityY: Float64
    public let velocity: Float64
    public init(
        target: EventTarget,
        timestamp: Int64,
        source: SourceType,
        pressure: Float64,
        tiltX: Int64,
        tiltY: Int64,
        sourceTool: SourceTool,
        axisHorizontal: Option<Float32>,
        axisVertical: Option<Float32>,
        getModifierKeyState: Option<(Array<String>) -> Bool>,
        deviveId: Int64,
        repeat: Bool,
        offsetX: Float64,
        offsetY: Float64,
        angle: Float64,
        scale: Float64,
        pinchCenterX: Float64,
        pinchCenterY: Float64,
        speed: Float64,
        fingerList: ArrayList<FingerInfo>,
        velocityX: Float64,
        velocityY: Float64,
        velocity: Float64
    )
}
```

**功能：** 用于描述手势事件的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [BaseEvent](cj-universal-gesture-judge.md#class-baseevent)

#### let angle

```cangjie
public let angle: Float64
```

**功能：** 用于RotationGesture手势触发场景时，表示旋转角度。用于SwipeGesture手势触发场景时，表示滑动手势的角度，即两根手指间的线段与水平方向的夹角变化的度数。

> **说明：**
>
> 角度计算方式：滑动手势被识别到后，连接两根手指之间的线被识别为起始线条，随着手指的滑动，手指之间的线条会发生旋转，根据起始线条两端点和当前线条两端点的坐标，使用反正切函数分别计算其相对于水平方向的夹角，最后arctan2(cy2-cy1,cx2-cx1)-arctan2(y2-y1,x2-x1)为旋转的角度。以起始线条为坐标系，顺时针旋转为0到180度，逆时针旋转为-180到0度。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let fingerList

```cangjie
public let fingerList: ArrayList<FingerInfo>
```

**功能：** 输入源为触屏产生的手势，fingerList中会包含触发事件的所有触点信息；由鼠标发起的手势，fingerList中只会有一条记录；触摸板的事件大类与鼠标一致，所以由触摸板发起的手势，fingerList只会携带一条记录。

> **说明：**
>
> 手指索引编号与位置对应，即fingerList[index]的id为index。先按下且未参与当前手势触发的手指在fingerList中对应位置为空。

**类型：** ArrayList\<[FingerInfo](#class-fingerinfo)>

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let offsetX

```cangjie
public let offsetX: Float64
```

**功能：** 手势事件偏移量X，单位为vp，用于[PanGesture](cj-universal-gesture-pangesture.md)手势触发场景，从左向右滑动offsetX为正，反之为负。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let offsetY

```cangjie
public let offsetY: Float64
```

**功能：** 手势事件偏移量Y，单位为vp，用于[PanGesture](cj-universal-gesture-pangesture.md)手势触发场景，从上向下滑动offsetY为正，反之为负。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let pinchCenterX

```cangjie
public let pinchCenterX: Float64
```

**功能：** 捏合手势中心点的x轴坐标，单位为vp，用于[PinchGesture](./cj-universal-gesture-pinchgesture.md)手势触发场景。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19