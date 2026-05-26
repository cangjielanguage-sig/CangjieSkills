## class AnimateParam

```cangjie
public class AnimateParam {
    public var duration: Option<Int32>
    public var tempo: Option<Float32>
    public var curve: Option<Curve>
    public var delay: Option<Int32>
    public var iterations: Option<Int32>
    public var playMode: Option<PlayMode>
    public var onFinish: Option <() -> Unit>
    public var finishCallbackType: Option<FinishCallbackType>
    public var expectedFrameRateRange: Option<ExpectedFrameRateRange>
    public init(
        duration!: Option<Int32> = 1000,
        tempo!: Option<Float32> = 1.0,
        curve!: Option<Curve> = Curve.EaseInOut,
        delay!: Option<Int32> = 0,
        iterations!: Option<Int32> = 1,
        playMode!: Option<PlayMode> = PlayMode.Normal,
        onFinish!: Option<() -> Unit> = Option.None,
        finishCallbackType!: Option<FinishCallbackType> = FinishCallbackType.REMOVED,
        expectedFrameRateRange!: Option<ExpectedFrameRateRange> = Option.None
    )
}
```

**功能：** 设置动画效果相关参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var curve

```cangjie
public var curve: Option<Curve>
```

**功能：** 动画曲线。

**类型：** Option\<[Curve](#enum-curve)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var delay

```cangjie
public var delay: Option<Int32>
```

**功能：** 动画延迟播放时间，单位为ms(毫秒)，默认不延时播放。

**类型：** Option\<Int32>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var duration

```cangjie
public var duration: Option<Int32>
```

**功能：** 动画持续时间，单位为毫秒。设置小于0的值时按0处理。

**类型：** Option\<Int32>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var expectedFrameRateRange

```cangjie
public var expectedFrameRateRange: Option<ExpectedFrameRateRange>
```

**功能：** 设置动画的期望帧率。

**类型：** Option\<[ExpectedFrameRateRange](./cj-animation-animateto.md#class-expectedframeraterange)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var finishCallbackType

```cangjie
public var finishCallbackType: Option<FinishCallbackType>
```

**功能：** 在动画中定义onFinish回调的类型。

**类型：** Option\<[FinishCallbackType](#enum-finishcallbacktype)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var iterations

```cangjie
public var iterations: Option<Int32>
```

**功能：** 动画播放次数。默认播放一次，设置为-1时表示无限次播放。设置为0时表示无动画效果。

**类型：** Option\<Int32>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var onFinish

```cangjie
public var onFinish: Option <() -> Unit>
```

**功能：** 动画播放完成回调。

**类型：** Option\<()->Unit>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var playMode

```cangjie
public var playMode: Option<PlayMode>
```

**功能：** 动画播放模式，默认播放完成后重头开始播放。

**类型：** Option\<[PlayMode](#enum-playmode)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var tempo

```cangjie
public var tempo: Option<Float32>
```

**功能：** 动画播放速度，值越大动画播放越快，值越小播放越慢，为0时无动画效果。

**类型：** Option\<Float32>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12