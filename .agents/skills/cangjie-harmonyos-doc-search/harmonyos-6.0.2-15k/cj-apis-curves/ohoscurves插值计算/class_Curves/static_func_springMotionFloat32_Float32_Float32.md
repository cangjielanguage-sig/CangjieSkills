### static func springMotion(Float32, Float32, Float32)

```cangjie
public static func springMotion(response!: Float32 = 0.55, damping!: Float32 = 0.825,
    overlapDuration!: Float32 = 0.0): ICurve
```

**功能：** 构造弹性动画曲线对象。如果对同一对象的同一属性进行多个弹性动画，每个动画会替换掉前一个动画，并继承之前的速度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|response|Float32|否|0.55| **命名参数。** 弹簧自然振动周期，决定弹簧复位的速度。<br>单位:秒。<br>取值范围：(0, +∞)。<br>**说明：**<br>设置小于等于0的值时，按默认值0.55处理。|
|damping|Float32|否|0.825| **命名参数。** 阻尼系数。<br>0表示无阻尼，一直处于震荡状态；<br>大于0小于1的值为欠阻尼，运动过程中会超出目标值；<br>等于1为临界阻尼；<br>大于1为过阻尼，运动过程中逐渐趋于目标值。<br>单位:秒。<br>取值范围：(0, +∞)<br>**说明：**<br>设置小于等于0的值时，按默认值0.825处理。|
|overlapDuration|Float32|否|0.0| **命名参数。** 弹性动画衔接时长。发生动画继承时，如果前后两个弹性动画response不一致，response参数会在overlapDuration时间内平滑过渡。<br>单位: 秒。<br>取值范围：(0, +∞)。<br>**说明：**<br>设置小于0的值时，按默认值0处理。<br>弹性动画曲线为物理曲线，[animation](./cj-animation-animation.md)、[animateTo](./cj-animation-animateto.md)、[pageTransition](./cj-animation-pagetransition.md)中的duration参数不生效，动画持续时间取决于springMotion动画曲线参数和之前的速度。时间不能归一，故不能通过该曲线的[interpolate](#func-interpolatefloat32)函数获得插值。|

**返回值：**

|类型|说明|
|:----|:----|
|[ICurve](#class-icurve)|曲线的插值对象。<br>**说明：** 弹性动画曲线为物理曲线，[animation](./cj-animation-animation.md)、[animateTo](./cj-animation-animateto.md)、[pageTransition](./cj-animation-pagetransition.md)中的duration参数不生效，动画持续时间取决于interpolatingSpring动画曲线参数。时间不能归一，故不能通过该曲线的[interpolate](#func-interpolatefloat32)函数获得插值。|

**示例：**

```cangjie
// 创建三个参数均自定义的弹性动画曲线
import kit.UIKit.*

let curve: ICurve = Curves.springMotion(response: 0.5, damping: 0.6, overlapDuration: 0.0)
```