### static func responsiveSpringMotion(Float32, Float32, Float32)

```cangjie
public static func responsiveSpringMotion(response!: Float32 = 0.15, dampingFraction!: Float32 = 0.86,
    overlapDuration!: Float32 = 0.25): ICurve
```

**功能：** 构造弹性跟手动画曲线对象，是[springMotion](#static-func-springmotionfloat32-float32-float32)的一种特例，仅默认参数不同，可与[springMotion](#static-func-springmotionfloat32-float32-float32)混合使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|response|Float32|否|0.15| **命名参数。** 解释同springMotion中的response。<br>单位:秒。<br>取值范围：(0, +∞)。<br>**说明：**<br>设置小于等于0的值时，按默认值0.15处理。|
|dampingFraction|Float32|否|0.86| **命名参数。** 解释同springMotion中的dampingFraction。<br>单位:秒。<br>取值范围：(0, +∞)。<br>**说明：**<br>设置小于等于0的值时，按默认值0.86处理。|
|overlapDuration|Float32|否|0.25| **命名参数。** 解释同springMotion中的overlapDuration。<br>单位: 秒。<br>取值范围：(0, +∞)。<br>**说明：**<br>弹性跟手动画曲线为springMotion的一种特例，仅默认值不同。如果使用自定义参数的弹性曲线，推荐使用springMotion构造曲线。如果使用跟手动画，推荐使用默认参数的弹性跟手动画曲线。<br>[animation](./cj-animation-animation.md)、[animateTo](./cj-animation-animateto.md)、[pageTransition](./cj-animation-pagetransition.md)中的duration参数不生效，responsiveSpringMotion动画曲线参数和之前的速度，也不能通过该曲线的[interpolate](#func-interpolatefloat32)函数获得插值。|

**返回值：**

|类型|说明|
|:----|:----|
|[ICurve](#class-icurve)|曲线对象。<br>**说明：**<br>1. 弹性跟手动画曲线为springMotion的一种特例，仅默认值不同。如果使用自定义参数的弹性曲线，推荐使用springMotion构造曲线；如果使用跟手动画，推荐使用默认参数的弹性跟手动画曲线。<br>2. [animation](./cj-animation-animation.md)、[animateTo](./cj-animation-animateto.md)、[pageTransition](./cj-animation-pagetransition.md)中的duration参数不生效，动画持续时间取决于responsiveSpringMotion动画曲线参数和之前的速度，也不能通过该曲线的[interpolate](#func-interpolatefloat32)函数获得插值。|

**示例:**

```cangjie
// 创建一个默认弹性跟手动画曲线
import kit.UIKit.*

let curve: ICurve = Curves.responsiveSpringMotion()
```