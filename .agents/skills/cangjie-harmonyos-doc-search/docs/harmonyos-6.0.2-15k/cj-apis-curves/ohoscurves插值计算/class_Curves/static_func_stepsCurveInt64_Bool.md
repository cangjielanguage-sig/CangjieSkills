### static func stepsCurve(Int64, Bool)

```cangjie
public static func stepsCurve(count: Int64, end: Bool): ICurve
```

**功能：** 构造阶梯曲线对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|count|Int64|是|-|阶梯的数量，需要为正整数。<br>取值范围：[1, +∞)。<br>**说明：**<br>设置小于1的值时，按值为1处理。|
|end|Bool|是|-|在每个间隔的起点或是终点发生阶跃变化。<br>-true: 在终点发生阶跃变化。<br>-false：在起点发生阶跃变化。|

**返回值：**

|类型|说明|
|:----|:----|
|[ICurve](#class-icurve)|曲线的插值对象。|

**示例：**

```cangjie
//创建一个阶梯曲线
import kit.UIKit.*

let curve: ICurve = Curves.stepsCurve(10, false)
```