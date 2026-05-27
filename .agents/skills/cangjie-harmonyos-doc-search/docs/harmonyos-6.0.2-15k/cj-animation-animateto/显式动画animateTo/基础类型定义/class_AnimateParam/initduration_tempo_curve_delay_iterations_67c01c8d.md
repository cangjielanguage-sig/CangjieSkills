#### init(duration, tempo, curve, delay, iterations, playMode, onFinish, finishCallbackType, expectedFrameRateRange)

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

**功能：** 构造一个AnimateParam类型的对象。

> **说明：**
>
> - PlayMode推荐使用PlayMode.Normal和PlayMode.Alternate，此场景下动画的第一轮是正向播放的。如使用PlayMode.Reverse和PlayMode.AlternateReverse，则动画的第一轮是逆向播放的，在动画刚开始时会跳变到终止状态，然后逆向播放动画。
> - 使用PlayMode.Alternate或PlayMode.AlternateReverse时，开发者应保证动画最终状态和状态变量的取值一致，即应保证动画的最后一轮是正向播放的。使用PlayMode.Alternate时，iterations应为奇数。使用PlayMode.AlternateReverse时，iterations应为偶数。
> - 不推荐使用PlayMode.Reverse，此场景下不仅会导致动画刚开始就跳变到终止状态，还会导致动画最终状态和状态变量的取值不同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|Option\<Int32>|否|1000| **命名参数。** 动画持续时间，单位为毫秒。<br/> 设置小于0的值时按0处理。<br>**说明：** <br>最大动画持续时间为1000毫秒，若超出则固定为1000毫秒。可以通过在持续时间为0的动画闭包函数中改变属性，以实现停止该属性动画的效果。设置小于0的值时按0处理。设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。|
|tempo|Option\<Float32>|否|1.0| **命名参数。** 动画播放速度，值越大动画播放越快，值越小播放越慢，为0时无动画效果。<br>取值范围：[0, +∞)。<br>**说明：**<br/> 当设置小于0的值时按值为1处理。|
|curve|Option\<[Curve](./cj-common-types.md#enum-curve)>|否|Curve.EaseInOut| **命名参数。** 动画曲线。|
|delay|Option\<Int32>|否|0| **命名参数。** 动画延迟播放时间，单位为ms(毫秒)，默认不延时播放。<br/> 取值范围：(-∞, +∞)。<br>**说明：** <br/>delay>=0为延迟播放，delay<0表示提前播放。对于delay<0的情况：当delay的绝对值小于实际动画时长，动画将在开始后第一帧直接运动到delay绝对值的时刻的状态；当delay的绝对值大于等于实际动画时长，动画将在开始后第一帧直接运动到终点状态。其中实际动画时长等于单次动画时长乘以动画播放次数。设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。|
|iterations|Option\<Int32>|否|1| **命名参数。** 动画播放次数。默认播放一次，设置为-1时表示无限次播放。设置为0时表示无动画效果。<br/> 取值范围：(-∞, +∞)。<br/> 该选项不适用于自定义弹窗。|
|playMode|Option\<[PlayMode](./cj-common-types.md#enum-playmode)>|否|PlayMode.Normal| **命名参数。** 动画播放模式，默认播放完成后重头开始播放。<br/> 该选项不适用于自定义弹窗。|
|onFinish|Option\<() -> Unit>|否|Option.None| **命名参数。** 动画播放完成回调。UIAbility从前台切换至后台时会立即结束仍在步进中的有限循环动画，触发播放完成回调。|
|finishCallbackType|Option\<[FinishCallbackType](./cj-common-types.md#enum-finishcallbacktype)> |否|FinishCallbackType.REMOVED| **命名参数。** 在动画中定义onFinish回调的类型。|
|expectedFrameRateRange|Option\<[ExpectedFrameRateRange](#class-expectedframeraterange)>|否|Option.None| **命名参数。** 设置动画的期望帧率。|