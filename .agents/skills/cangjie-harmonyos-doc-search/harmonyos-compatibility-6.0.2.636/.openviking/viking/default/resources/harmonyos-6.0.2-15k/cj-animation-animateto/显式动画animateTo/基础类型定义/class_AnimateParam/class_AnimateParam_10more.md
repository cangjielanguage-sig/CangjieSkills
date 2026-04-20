### class AnimateParam

```cangjie
public class AnimateParam {
    public var duration: Option<Int32>
    public var tempo: Option<Float32>
    public var curve: Option<Curve>
    public var delay: Option<Int32>
    public var iterations: Option<Int32>
    public var playMode: Option<PlayMode>
    public var onFinish: Option<() -> Unit>
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

**功能：** 动画效果参数设置类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var curve

```cangjie
public var curve: Option<Curve>
```

**功能：** 设置动画曲线。

**类型：** [Curve](./cj-common-types.md#enum-curve)

**读写能力：** 可读写

**起始版本：** 12

#### var delay

```cangjie
public var delay: Option<Int32>
```

**功能：** 设置动画延迟播放时间。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

#### var duration

```cangjie
public var duration: Option<Int32>
```

**功能：** 设置动画持续时间。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

#### var expectedFrameRateRange

```cangjie
public var expectedFrameRateRange: Option<ExpectedFrameRateRange>
```

**功能：** 设置动画持续时间。

**类型：** [ExpectedFrameRateRange](#expectedframeraterangeint32-int32-int32)

**读写能力：** 可读写

**起始版本：** 12

#### var finishCallbackType

```cangjie
public var finishCallbackType: Option<FinishCallbackType>
```

**功能：** 设置动画中定义onFinish回调的类型。

**类型：** [FinishCallbackType](./cj-common-types.md#enum-finishcallbacktype)

**读写能力：** 可读写

**起始版本：** 12

#### var iterations

```cangjie
public var iterations: Option<Int32>
```

**功能：** 设置动画播放次数。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

#### var onFinish

```cangjie
public var onFinish: Option<() -> Unit>
```

**功能：** 设置动画播放完成回调。

**类型：** () -> Unit

**读写能力：** 可读写

**起始版本：** 12

#### var playMode

```cangjie
public var playMode: Option<PlayMode>
```

**功能：** 设置动画播放模式。

**类型：** [PlayMode](./cj-common-types.md#enum-playmode)

**读写能力：** 可读写

**起始版本：** 12

#### var tempo

```cangjie
public var tempo: Option<Float32>
```

**功能：** 设置动画播放速度。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 12