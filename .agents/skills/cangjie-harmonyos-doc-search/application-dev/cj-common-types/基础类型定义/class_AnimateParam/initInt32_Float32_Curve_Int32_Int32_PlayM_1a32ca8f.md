### init(?Int32, ?Float32, ?Curve, ?Int32, ?Int32, ?PlayMode, Option\<() -> Unit>, ?FinishCallbackType, Option\<ExpectedFrameRateRange>)

```cangjie
public init(duration!: ?Int32 = None, tempo!: ?Float32 = None, curve!: ?Curve = None, delay!: ?Int32 = None, iterations!: ?Int32 = None, playMode!: ?PlayMode = None, onFinish!: Option<() -> Unit> = Option.None, finishCallbackType!: ?FinishCallbackType = None, expectedFrameRateRange!: Option<ExpectedFrameRateRange> = Option.None)
```

**功能：** 构造一个AnimateParam对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|?Int32|否|None|**命名参数。** 动画持续时间，单位为毫秒。设置小于0的值时按0处理。<br>初始值：1000。<br>**说明：**<br>1. 可以通过在持续时间为0的动画闭包函数中改变属性，以实现停止该属性动画的效果。<br>2. 设置小于0的值时按0处理。|
|tempo|?Float32|否|None|**命名参数。** 动画播放速度，值越大动画播放越快，值越小播放越慢，为0时无动画效果。<br>初始值：1.0。<br>取值范围：[0, +∞)。|
|curve|?[Curve](./cj-common-types.md#enum-curve)|否|None|**命名参数。** 动画曲线。初始值为Curve.EaseInOut。|
|delay|?Int32|否|None|**命名参数。** 动画延迟播放时间，单位为ms(毫秒)。<br>初始值：0。<br>取值范围：(-∞, +∞)。<br>**说明：**<br>delay>=0为延迟播放，delay<0表示提前播放。对于delay<0的情况：当delay的绝对值小于实际动画时长，动画将在开始后第一帧直接运动到delay绝对值的时刻的状态；当delay的绝对值大于等于实际动画时长，动画将在开始后第一帧直接运动到终点状态。其中实际动画时长等于单次动画时长乘以动画播放次数。|
|iterations|?Int32|否|None|**命名参数。** 动画播放次数。设置为-1时表示无限次播放。设置为0时表示无动画效果。<br>初始值：1。<br>取值范围：[-1, +∞)。|
|playMode|?[PlayMode](./cj-common-types.md#enum-playmode)|否|None|**命名参数。** 动画播放模式，默认播放完成后重头开始播放。<br>初始值：PlayMode.Normal。|
|onFinish|Option\<() -> Unit>|否|Option.None|**命名参数。** 动画播放完成回调。|
|finishCallbackType|?[FinishCallbackType](./cj-common-types.md#enum-finishcallbacktype)|否|None|**命名参数。** 在动画中定义onFinish回调的类型。<br>初始值：FinishCallbackType.Removed。|
|expectedFrameRateRange|Option<[ExpectedFrameRateRange](#class-expectedframeraterange)>|否|Option.None|**命名参数。** 设置动画的期望帧率。|