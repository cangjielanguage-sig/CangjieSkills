### init(Option\<Int32>, Option\<Float32>, Option\<Curve>, Option\<Int32>, Option\<Int32>, Option\<PlayMode>, Option\<() -> Unit>, Option\<FinishCallbackType>, Option\<ExpectedFrameRateRange>)

```cangjie
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
```

**功能：** 构造一个AnimateParam对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
| :--- | :--- | :--- | :--- | :--- |
| duration | Option\<Int32> | 否 | 1000 | **命名参数。**  动画持续时间，单位为毫秒。 <br/> 设置小于0的值时按0处理。 |
| tempo | Option\<Float32> | 否 | 1.0 | **命名参数。**  动画播放速度，值越大动画播放越快，值越小播放越慢，为0时无动画效果。 <br/> 当设置小于0的值时按值为1处理。 |
| curve | Option\<Curve> | 否 | Curve.EaseInOut| **命名参数。**  动画曲线。 <br/> 默认值：Curve.EaseInOut |
| delay | Option\<Int32> | 否 | 0 | **命名参数。**  动画延迟播放时间，单位为ms(毫秒)，默认不延时播放。<br/> 取值范围：(-∞, +∞)  <br/> delay >= 0为延迟播放，delay < 0表示提前播放。 |
| iterations | Option\<Int32> | 否 | 1 | **命名参数。**  动画播放次数。默认播放一次，设置为-1时表示无限次播放。设置为0时表示无动画效果。 <br/> 该选项不适用于自定义弹窗 |
| playMode | Option\<PlayMode> | 否 | PlayMode.Normal | **命名参数。**  动画播放模式，默认播放完成后重头开始播放。 <br/> 该选项不适用于自定义弹窗 |
| onFinish | Option\<() -> Unit> | 否 | - | **命名参数。**  动画播放完成回调。 |
| finishCallbackType | Option\<[FinishCallbackType](#enum-finishcallbacktype)> | 否 | FinishCallbackType.REMOVED | **命名参数。**  在动画中定义onFinish回调的类型。 |
| expectedFrameRateRange | Option\<[ExpectedFrameRateRange](./cj-animation-animateto.md#class-expectedframeraterange)> | 否 | - | **命名参数。**  设置动画的期望帧率。 |