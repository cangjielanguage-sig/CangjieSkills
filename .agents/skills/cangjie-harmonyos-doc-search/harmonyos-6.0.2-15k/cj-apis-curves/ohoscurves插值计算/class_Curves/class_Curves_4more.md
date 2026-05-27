## class Curves

```cangjie
public class Curves {}
```

**功能：** 动画插值曲线类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static func cubicBezierCurve(Float32, Float32, Float32, Float32)

```cangjie
public static func cubicBezierCurve(x1: Float32, y1: Float32, x2: Float32, y2: Float32): ICurve
```

**功能：** 构造三阶贝塞尔曲线对象，曲线的值必须处于0-1之间。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x1|Float32|是|-|确定贝塞尔曲线第一点横坐标。<br>取值范围：[0，1]<br>**说明：**<br>设置的值小于0时，按0处理；设置的值大于1时，按1处理。|
|y1|Float32|是|-|确定贝塞尔曲线第一点纵坐标。<br>取值范围：(-∞, +∞)。|
|x2|Float32|是|-|确定贝塞尔曲线第二点横坐标。<br>取值范围：[0，1]。<br>**说明：**<br>设置的值小于0时，按0处理；设置的值大于1时，按1处理。|
|y2|Float32|是|-|确定贝塞尔曲线第二点纵坐标。<br>取值范围：(-∞, +∞)。|

**返回值：**

|类型|说明|
|:----|:----|
|[ICurve](#class-icurve)|曲线的插值对象。|

**示例：**

```cangjie
// 创建一个三阶贝塞尔曲线
import kit.UIKit.*

let curve: ICurve = Curves.cubicBezierCurve(0.5, 10.0, 0.5, 10.0)
```

### static func customCurve((Float32) -> Float32)

```cangjie
public static func customCurve(interpolate: (Float32) -> Float32): ICurve
```

**功能：** 构造自定义曲线对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|interpolate|(Float32) -> Float32|是|-|用户自定义的插值回调函数。<br>动画开始时的插值输入x值。<br>取值范围：[0,1]。<br>返回值为曲线的y值。<br>取值范围：[0,1]。<br>**说明：**<br>fraction等于0时，返回值为0对应动画起点，返回不为0，动画在起点处有跳变效果。fraction等于1时，返回值为1对应动画终点，返回值不为1将导致动画的终值不是状态变量的值，出现大于或者小于状态变量值，再跳变到状态变量值的效果。|

**返回值：**

|类型|说明|
|:----|:----|
|[ICurve](#class-icurve)|曲线的插值对象。|

**示例：**

```cangjie
// 创建一个用户自定义插值曲线
import kit.UIKit.*

let curve: ICurve = Curves.customCurve({interpolate => interpolate * 0.5})
```

### static func initCurve(Curve)

```cangjie
public static func initCurve(curve!: Curve = Curve.Linear): ICurve
```

**功能：** 插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|curve|[Curve](../arkui-cj/cj-common-types.md#enum-curve)|否|Curve.Linear| **命名参数。** 曲线类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[ICurve](#class-icurve)|曲线的插值对象。|

**示例：**

```cangjie
// 创建一个默认先慢后快插值曲线
import kit.UIKit.*

let curve: ICurve = Curves.initCurve(curve: Curve.EaseIn)
```