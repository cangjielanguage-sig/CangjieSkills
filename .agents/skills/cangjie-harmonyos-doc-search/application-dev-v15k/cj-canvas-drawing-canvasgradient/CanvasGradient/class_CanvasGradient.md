## class CanvasGradient

```cangjie
public class CanvasGradient <: RemoteData {
    public init(contextId: Int64, x0: Float64, y0: Float64, x1: Float64, y1: Float64)
    public init(contextId: Int64, x0: Float64, y0: Float64, r0: Float64, x1: Float64, y1: Float64, r1: Float64)
}
```

**功能：** 渐变对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

> **说明：**
>
> - 该对象使用 [CanvasRenderingContext2D](./cj-canvas-drawing-canvasrenderingcontext2d.md#canvasrenderingcontext2d) 和 [OffscreenCanvasRenderingContext2D](./cj-canvas-drawing-offscreencanvasrenderingcontext2d.md#offscreencanvasrenderingcontext2d) 中的 [createlineargradient](./cj-canvas-drawing-offscreencanvasrenderingcontext2d.md#func-createlineargradientfloat64-float64-float64-float64) 或 [createRadialGradient](./cj-canvas-drawing-offscreencanvasrenderingcontext2d.md#func-createradialgradientfloat64-float64-float64-float64-float64-float64) 创建；
> - 该对象使用完毕后，需要调用 release() 方法进行释放，详见示例。

### init(Int64, Float64, Float64, Float64, Float64)

```cangjie
public init(contextId: Int64, x0: Float64, y0: Float64, x1: Float64, y1: Float64)
```

**功能：** 创建线性渐变对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|contextId|Int64|是|-|组件所在的context的描述符。|
|x0|Float64|是|-|渐变起点的x坐标。|
|y0|Float64|是|-|渐变起点的y坐标。|
|x1|Float64|是|-|渐变终点的x坐标。|
|y1|Float64|是|-|渐变终点的y坐标。|

### init(Int64, Float64, Float64, Float64, Float64, Float64, Float64)

```cangjie
public init(contextId: Int64, x0: Float64, y0: Float64, r0: Float64, x1: Float64, y1: Float64, r1: Float64)
```

**功能：** 创建径向/圆形渐变对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|contextId|Int64|是|-|组件所在的context的描述符。|
|x0|Float64|是|-|渐变圆1的圆心x坐标。|
|y0|Float64|是|-|渐变圆1的圆心y坐标。|
|r0|Float64|是|-|渐变圆1的半径。|
|x1|Float64|是|-|渐变圆2的圆心x坐标。|
|y1|Float64|是|-|渐变圆2的圆心y坐标。|
|r1|Float64|是|-|渐变圆2的半径。|

### func addColorStop(Float64, ResourceColor)

```cangjie
public func addColorStop(offset: Float64, color: ResourceColor): Unit
```

**功能：** 设置渐变断点值，包括偏移和颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Float64|是|-|设置渐变点距离起点的位置占总体长度的比例，范围为0到1。设置offset<0或offset>1无渐变效果。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|设置渐变的颜色。颜色格式参考[ResourceColor](./cj-common-types.md#interface-resourcecolor)中string类型说明。未按格式设置颜色无渐变效果。|

### func addColorStop(Int64, ResourceColor)

```cangjie
public func addColorStop(offset: Int64, color: ResourceColor): Unit
```

**功能：** 设置渐变断点值，包括偏移和颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int64|是|-|设置渐变点距离起点的位置占总体长度的比例，范围为0到1。设置offset<0或offset>1无渐变效果。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|设置渐变的颜色。颜色格式参考[ResourceColor](./cj-common-types.md#interface-resourcecolor)中string类型说明。未按格式设置颜色无渐变效果。|