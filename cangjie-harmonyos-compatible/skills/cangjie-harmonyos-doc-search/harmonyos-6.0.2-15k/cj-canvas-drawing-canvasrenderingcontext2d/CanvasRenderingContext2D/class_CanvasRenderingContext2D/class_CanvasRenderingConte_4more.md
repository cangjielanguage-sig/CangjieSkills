## class CanvasRenderingContext2D

```cangjie
public class CanvasRenderingContext2D {
    public init(settings: RenderingContextSettings)
    public init(settings: RenderingContextSettings, unit: LengthMetricsUnit)
}
```

**功能：** 表示使用RenderingContext在Canvas组件上进行绘制的类型，绘制对象可以是矩形、文本、图片等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(RenderingContextSettings)

```cangjie
public init(settings: RenderingContextSettings)
```

**功能：** 构造一个CanvasRenderingContext2D类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|settings|[RenderingContextSettings](#class-renderingcontextsettings)|是|-|用来配置CanvasRenderingContext2D对象的参数。|

### init(RenderingContextSettings, LengthMetricsUnit)

```cangjie
public init(settings: RenderingContextSettings, unit: LengthMetricsUnit)
```

**功能：** 构造一个CanvasRenderingContext2D类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|settings|[RenderingContextSettings](#class-renderingcontextsettings)|是|-|用来配置CanvasRenderingContext2D对象的参数。|
|unit|[LengthMetricsUnit](./cj-common-types.md#enum-lengthmetricsunit)|是|-|用来配置CanvasRenderingContext2D对象的单位模式，配置后无法更改。<br>初始值：DEFAULT。|

### func arc(Float64, Float64, Float64, Float64, Float64, Bool)

```cangjie
public func arc(
    x: Float64,
    y: Float64,
    radius: Float64,
    startAngle: Float64,
    endAngle: Float64,
    anticlockwise!: Bool = false
): Unit
```

**功能：** 绘制弧线路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|弧线圆心的x坐标值。<br>默认单位：vp。|
|y|Float64|是|-|弧线圆心的y坐标值。<br>默认单位：vp。|
|radius|Float64|是|-|弧线的圆半径。<br>默认单位：vp。|
|startAngle|Float64|是|-|弧线的起始弧度。<br>单位：弧度。|
|endAngle|Float64|是|-|弧线的终止弧度。<br>单位：弧度。|
|anticlockwise|Bool|否|false| **命名参数。** 是否逆时针绘制圆弧。<br>是否逆时针绘制圆弧。<br>true：逆时针方向绘制椭圆。<br>false：顺时针方向绘制椭圆。|