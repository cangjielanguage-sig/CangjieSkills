#### init(EventTarget, Int64, SourceType, Float64, Int64, Int64, SourceTool, Option\<Float32>, Option\<Float32>, Option\<(Array\<String>) -> Bool>, Int64, Bool, Float64, Float64, Float64, Float64, Float64, Float64, Float64, ArrayList\<FingerInfo>, Float64, Float64, Float64)

```cangjie
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
```

**功能：** 构造手势事件类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**