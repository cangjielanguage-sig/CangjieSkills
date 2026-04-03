## class AnimatorOptions

```cangjie
public class AnimatorOptions {
    public var duration: Int32
    public var easing: String
    public var delay: Int32
    public var fill: AnimatorFill
    public var direction: AnimatorDirection
    public var iterations: Int32
    public var begin: Float64
    public var end: Float64
    public init(
        duration!: Int32,
        easing!: String,
        delay!: Int32,
        fill!: AnimatorFill,
        direction!: AnimatorDirection,
        iterations!: Int32,
        begin!: Float64,
        end!: Float64
    )
}
```

**功能：** 定义动画选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var duration

```cangjie
public var duration: Int32
```

**功能：** 动画播放的时长，单位毫秒。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var easing

```cangjie
public var easing: String
```

**功能：** 动画插值曲线。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var delay

```cangjie
public var delay: Int32
```

**功能：** 动画延时播放时长，单位毫秒。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var fill

```cangjie
public var fill: AnimatorFill
```

**功能：** 动画执行后是否恢复到初始状态，动画执行后，动画结束时的状态（在最后一个关键帧中定义）将保留。

**类型：** [AnimatorFill](#enum-animatorfill)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var direction

```cangjie
public var direction: AnimatorDirection
```

**功能：** 动画播放模式。

**类型：** [AnimatorDirection](#enum-animatordirection)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var iterations

```cangjie
public var iterations: Int32
```

**功能：** 动画播放次数。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var begin

```cangjie
public var begin: Float64
```

**功能：** 动画插值起点。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var end

```cangjie
public var end: Float64
```

**功能：** 动画插值终点。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(Int32, String, Int32, AnimatorFill, AnimatorDirection, Int32, Float64, Float64)

```cangjie
public init(
    duration!: Int32,
    easing!: String,
    delay!: Int32,
    fill!: AnimatorFill,
    direction!: AnimatorDirection,
    iterations!: Int32,
    begin!: Float64,
    end!: Float64
)
```

**功能：** 创建AnimatorOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|Int32|是|-|**命名参数。** 动画播放的时长，单位毫秒。取值范围：[0, +∞)。|
|easing|String|是|-|**命名参数。** 动画插值曲线。|
|delay|Int32|是|-|**命名参数。** 动画延时播放时长，单位毫秒，设置为0时，表示不延时。设置为负数时动画提前播放，如果提前播放的时长大于动画总时长，动画直接过渡到终点。|
|fill|[AnimatorFill](#enum-animatorfill)|是|-|**命名参数。** 动画执行后是否恢复到初始状态，动画执行后，动画结束时的状态（在最后一个关键帧中定义）将保留。|
|direction|[AnimatorDirection](#enum-animatordirection)|是|-|**命名参数。** 动画播放模式。|
|iterations|Int32|是|-|**命名参数。** 动画播放次数。设置为0时不播放，设置为-1时无限次播放，设置大于0时为播放次数。|
|begin|Float64|是|-|**命名参数。** 动画插值起点。|
|end|Float64|是|-|**命名参数。** 动画插值终点。|