### static func stepsCurve(Int32, Bool)

```cangjie
public static func stepsCurve(count: Int32, end: Bool): ICurve
```

**功能：** 创建阶梯曲线对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|count|Int32|是|-|阶梯的数量，需要为正整数。<br>取值范围：[1, +∞)。<br>**说明：**<br>设置小于1的值时，按值为1处理。|
|end|Bool|是|-|在每个间隔的起点或是终点发生阶跃变化。<br>-true: 在终点发生阶跃变化。<br>-false：在起点发生阶跃变化。|

**返回值：**

|类型|说明|
|:----|:----|
|[ICurve](#class-icurve)|返回曲线的插值对象。|