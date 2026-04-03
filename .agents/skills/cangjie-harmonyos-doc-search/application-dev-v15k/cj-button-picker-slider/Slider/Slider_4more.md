# Slider

滑动条组件，通常用于用快速调节设置值，如音量调节、亮度调节等应用场景。

## 子组件

无

## 创建组件

### init(Float64, Float64, Float64, Float64, SliderStyle, Axis, Bool)

```cangjie
public init(
    min!: Float64 = 0.0,
    max!: Float64 = 100.0,
    step!: Float64 = 1.0,
    value!: Float64 = min,
    style!: SliderStyle = SliderStyle.OutSet,
    direction!: Axis = Axis.Horizontal,
    reverse!: Bool = false
)
```

**功能：** 创建一个滑动条组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|min|Float64|否|0.0| **命名参数。** 设置最小值。|
|max|Float64|否|100.0| **命名参数。** 设置最大值。<br/>初始值：100。<br/>**说明：**<br/>min >= max异常情况，min取初始值0，max取初始值100。<br/>value不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。|
|step|Float64|否|1.0| **命名参数。** 设置滑动条滑动步长。<br/>**说明：**<br/>当step<=0，或step>=max\-min时，取初始值。|
|value|Float64|否|min| **命名参数。** 当前进度值。|
|style|[SliderStyle](#enum-sliderstyle)|否|SliderStyle.OutSet| **命名参数。** 设置滑动条的滑块样式。|
|direction|[Axis](./cj-common-types.md#enum-axis)|否|Axis.Horizontal| **命名参数。** 设置滑动条滑动方向为水平或竖直方向。|
|reverse|Bool|否|false| **命名参数。** 设置滑动条取值范围是否反向。<br/>**说明：**<br/>设置为false时，水平方向滑动条为从左向右滑动，竖直方向滑动条从上向下滑动。<br/>设置为true时，水平方向滑动条为从右向左滑动，竖直方向滑动条从下向上滑动。|

## 通用属性/通用事件

通用属性：支持除触摸热区以外的通用属性。

通用事件：全部支持。