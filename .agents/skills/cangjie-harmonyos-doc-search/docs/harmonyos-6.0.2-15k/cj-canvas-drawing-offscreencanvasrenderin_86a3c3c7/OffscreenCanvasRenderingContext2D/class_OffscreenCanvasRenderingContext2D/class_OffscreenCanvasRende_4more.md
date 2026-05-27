## class OffscreenCanvasRenderingContext2D

```cangjie
public class OffscreenCanvasRenderingContext2D {
    public init(
        width: Float64,
        height: Float64,
        settings: RenderingContextSettings,
        unit!: LengthMetricsUnit = LengthMetricsUnit.DEFAULT
        )
    public init(
        width: Int64,
        height: Int64,
        settings: RenderingContextSettings,
        unit!: LengthMetricsUnit = LengthMetricsUnit.DEFAULT
        )
}
```

**功能：** OffscreenCanvasRenderingContext2D对象，用于在Canvas组件上进行离屏绘制，绘制对象可以是矩形、文本、图片等。

**起始版本：** 19

### init(Float64, Float64, RenderingContextSettings, LengthMetricsUnit)

```cangjie
public init(
    width: Float64,
    height: Float64,
    settings: RenderingContextSettings,
    unit!: LengthMetricsUnit = LengthMetricsUnit.DEFAULT
    )
```

**功能：** 创造一个OffscreenCanvasRenderingContext2D对象，用于在Canvas组件上进行离屏绘制，绘制对象可以是矩形、文本、图片等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Float64|是|-|离屏画布的宽度。</br>默认单位：vp。|
|height|Float64|是|-|离屏画布的高度。</br>默认单位：vp。|
|settings|[RenderingContextSettings](./cj-canvas-drawing-canvasrenderingcontext2d.md#class-renderingcontextsettings)|是|-|用来配置OffscreenCanvasRenderingContext2D对象的参数。|
|unit|[LengthMetricsUnit](./cj-common-types.md#enum-lengthmetricsunit)|否|LengthMetricsUnit.DEFAULT| **命名参数。** 用来配置OffscreenCanvasRenderingContext2D对象的单位模式。|

### init(Int64, Int64, RenderingContextSettings, LengthMetricsUnit)

```cangjie
public init(
    width: Int64,
    height: Int64,
    settings: RenderingContextSettings,
    unit!: LengthMetricsUnit = LengthMetricsUnit.DEFAULT
    )
```

**功能：** 创造一个OffscreenCanvasRenderingContext2D对象，用于在Canvas组件上进行离屏绘制，绘制对象可以是矩形、文本、图片等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Int64|是|-|离屏画布的宽度。</br>默认单位：vp。|
|height|Int64|是|-|离屏画布的高度。</br>默认单位：vp。|
|settings|[RenderingContextSettings](./cj-canvas-drawing-canvasrenderingcontext2d.md#class-renderingcontextsettings)|是|-|用来配置OffscreenCanvasRenderingContext2D对象的参数。|
|unit|[LengthMetricsUnit](./cj-common-types.md#enum-lengthmetricsunit)|否|LengthMetricsUnit.DEFAULT| **命名参数。** 用来配置OffscreenCanvasRenderingContext2D对象的单位模式。|

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

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|弧线圆心的x坐标值。</br>默认单位：vp。|
|y|Float64|是|-|弧线圆心的y坐标值。</br>默认单位：vp。|
|radius|Float64|是|-|弧线的圆半径。<br>默认单位：vp。|
|startAngle|Float64|是|-|弧线的起始弧度。<br>单位：弧度。|
|endAngle|Float64|是|-|弧线的终止弧度。<br>单位：弧度。|
|anticlockwise|Bool|否|false| **命名参数。** 是否逆时针绘制圆弧。<br>true:逆时针方向绘制椭圆。<br>false:顺时针方向绘制椭圆。|