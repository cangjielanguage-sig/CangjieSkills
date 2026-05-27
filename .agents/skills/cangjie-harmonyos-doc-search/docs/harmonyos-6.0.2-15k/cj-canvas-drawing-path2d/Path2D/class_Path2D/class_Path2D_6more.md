## class Path2D

```cangjie
public open class Path2D {
    public init(unit!: LengthMetricsUnit = LengthMetricsUnit.DEFAULT)
    public init(path: String, unit!: LengthMetricsUnit = LengthMetricsUnit.DEFAULT)
}
```

**功能：** 路径对象，支持通过对象的接口进行路径的描述，并通过Canvas的stroke接口或者fill接口进行绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(LengthMetricsUnit)

```cangjie
public init(unit: LengthMetricsUnit) 
```

**功能：** 构造一个空的Path2D对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|unit|[LengthMetricsUnit](./cj-common-types.md#enum-lengthmetricsunit)|是|-| **命名参数。** 用来配置Path2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](./cj-canvas-drawing-canvasrenderingcontext2d.md#class-canvasrenderingcontext2d)。|

### init(String, LengthMetricsUnit)

```cangjie
public init(path: String, unit: LengthMetricsUnit)
```

**功能：** 使用符合SVG路径描述规范的路径字符串构造一个Path2D对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|符合 SVG 路径描述规范的路径字符串，格式参考Path中SVG路径描述规范说明。|
|unit|[LengthMetricsUnit](./cj-common-types.md#enum-lengthmetricsunit)|是|-| **命名参数。** 用来配置Path2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](./cj-canvas-drawing-canvasrenderingcontext2d.md#class-canvasrenderingcontext2d)。|

### func addPath(Path2D)

```cangjie
public func addPath(path2D: Path2D): Unit
```

**功能：** 将另一个路径添加到当前的路径对象中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path2D|[Path2D](#class-path2d)|是|-|需要添加到当前路径的路径对象，路径单位：px。|

### func addPath(Path2D, Matrix2D)

```cangjie
public func addPath(path2D: Path2D, transform: Matrix2D): Unit
```

**功能：** 将另一个路径添加到当前的路径对象中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path2D|[Path2D](#class-path2d)|是|-|需要添加到当前路径的路径对象，路径单位：px。|
|transform|[Matrix2D](./cj-canvas-drawing-matrix2d.md#class-matrix2d)|是|-|新增路径的变换矩阵对象。|

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
|anticlockwise|Bool|否|false| **命名参数。** 是否逆时针绘制圆弧。<br>true:逆时针方向绘制椭圆。<br>false:顺时针方向绘制椭圆。|