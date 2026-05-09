# Slider

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(?Float64, ?Float64, ?Float64, ?Float64, ?SliderStyle, ?Axis, ?Bool)

```cangjie
public init(
    min!: ?Float64 = None,
    max!: ?Float64 = None,
    step!: ?Float64 = None,
    value!: ?Float64 = None,
    style!: ?SliderStyle = None,
    direction!: ?Axis = None,
    reverse!: ?Bool = None
)
```

**功能：** 创建一个滑动条组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|min|?Float64|否|None| **命名参数。** 设置最小值。<br>初始值：0.0。|
|max|?Float64|否|None| **命名参数。** 设置最大值。<br>初始值：100.0。<br>**说明**：min >= max异常情况，min取初始值0，max取初始值100。<br>value不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。|
|step|?Float64|否|None| **命名参数。** 设置滑动条滑动步长。<br>初始值：1.0。<br>**说明**：当step<=0，或step>=max\-min时，取初始值。|
|value|?Float64|否|None| **命名参数。** 当前进度值。<br>初始值：取min的值。|
|style|?[SliderStyle](./cj-common-types.md#enum-sliderstyle)|否|None| **命名参数。** 设置滑动条的滑块样式。<br>初始值：SliderStyle.OutSet。|
|direction|?[Axis](./cj-common-types.md#enum-axis)|否|None| **命名参数。** 设置滑动条滑动方向为水平或竖直方向。<br>初始值：Axis.Horizontal。|
|reverse|?Bool|否|None| **命名参数。** 设置滑动条取值范围是否反向。<br>初始值：false。<br>**说明**：<br>设置为false时，水平方向滑动条为从左向右滑动，竖直方向滑动条从上向下滑动。<br>设置为true时，水平方向滑动条为从右向左滑动，竖直方向滑动条从下向上滑动。|

## 通用属性/通用事件

通用属性：支持除触摸热区以外的通用属性。

通用事件：全部支持。