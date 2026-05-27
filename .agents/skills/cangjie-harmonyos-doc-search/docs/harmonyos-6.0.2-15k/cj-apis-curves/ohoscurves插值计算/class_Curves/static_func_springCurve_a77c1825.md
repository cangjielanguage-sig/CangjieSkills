### static func springCurve(Float32, Float32, Float32, Float32)

```cangjie
public static func springCurve(velocity: Float32, mass: Float32, stiffness: Float32, damping: Float32): ICurve
```

**功能：** 构造弹簧曲线对象，曲线形状由弹簧参数决定，动画时长受animation、animateTo中的duration参数控制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|velocity|Float32|是|-|初始速度。是由外部因素对弹性动效产生的影响参数，其目的是保证对象从之前的运动状态平滑的过渡到弹性动效。该速度是归一化速度，其值等于动画开始时的实际速度除以动画属性改变值。<br>取值范围：(-∞, +∞)|
|mass|Float32|是|-|质量。弹性系统的受力对象，会对弹性系统产生惯性影响。质量越大，震荡的幅度越大，恢复到平衡位置的速度越慢。<br>取值范围：(0, +∞)。<br>**说明：**<br>设置的值小于等于0时，按1处理。|
|stiffness|Float32|是|-|刚度。是物体抵抗施加的力而形变的程度。在弹性系统中，刚度越大，抵抗变形的能力越强，恢复到平衡位置的速度就越快。<br>取值范围：(0, +∞)。<br>**说明：**<br>设置的值小于等于0时，按1处理。|
|damping|Float32|是|-|阻尼。用于描述系统在受到扰动后震荡及衰减的情形。阻尼越大，弹性运动的震荡次数越少、震荡幅度越小。<br>取值范围：(0, +∞)。<br>**说明：**<br>设置的值小于等于0时，按1处理。|

**返回值：**

|类型|说明|
|:----|:----|
|[ICurve](#class-icurve)|曲线的插值对象。|

**示例:**

```cangjie
// 创建一个弹簧插值曲线
import kit.UIKit.*

let curve: ICurve = Curves.springCurve(10.0, 1.0, 228.0, 30.0)
```