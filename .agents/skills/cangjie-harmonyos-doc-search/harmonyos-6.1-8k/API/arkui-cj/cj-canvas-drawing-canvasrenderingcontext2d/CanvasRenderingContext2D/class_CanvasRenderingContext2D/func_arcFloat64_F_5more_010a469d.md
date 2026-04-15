### func arc(Float64, Float64, Float64, Float64, Float64, ?Bool)

```cangjie
public func arc(
    x: Float64,
    y: Float64,
    radius: Float64,
    startAngle: Float64,
    endAngle: Float64,
    counterclockwise!: ?Bool = None
): Unit
```

**功能：** 绘制弧线路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|弧线圆心的x坐标值。<br>默认单位：vp。|
|y|Float64|是|-|弧线圆心的y坐标值。<br>默认单位：vp。|
|radius|Float64|是|-|弧线的圆半径。<br>默认单位：vp。|
|startAngle|Float64|是|-|弧线的起始弧度。<br>单位：弧度。|
|endAngle|Float64|是|-|弧线的终止弧度。<br>单位：弧度。|
|counterclockwise|?Bool|否|None|**命名参数。** 是否逆时针绘制圆弧。<br>true：逆时针方向绘制椭圆。<br>false：顺时针方向绘制椭圆。|

### func arcTo(Float64, Float64, Float64, Float64, Float64)

```cangjie
public func arcTo(x1: Float64, y1: Float64, x2: Float64, y2: Float64, radius: Float64): Unit
```

**功能：** 依据圆弧经过的点和圆弧半径创建圆弧路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x1|Float64|是|-|圆弧经过的第一个点的x坐标值。<br>默认单位：vp。|
|y1|Float64|是|-|圆弧经过的第一个点的y坐标值。<br>默认单位：vp。|
|x2|Float64|是|-|圆弧经过的第二个点的x坐标值。<br>默认单位：vp。|
|y2|Float64|是|-|圆弧经过的第二个点的y坐标值。<br>默认单位：vp。|
|radius|Float64|是|-|圆弧的圆半径值。<br>默认单位：vp。|

### func ellipse(Float64, Float64, Float64, Float64, Float64, Float64, Float64, ?Bool)

```cangjie
public func ellipse(
    x: Float64,
    y: Float64,
    radiusX: Float64,
    radiusY: Float64,
    rotation: Float64,
    startAngle: Float64,
    endAngle: Float64,
    counterclockwise!: ?Bool = None
): Unit
```

**功能：** 在规定的矩形区域绘制一个椭圆。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|椭圆圆心的x轴坐标，单位：vp。|
|y|Float64|是|-|椭圆圆心的y轴坐标，单位：vp。|
|radiusX|Float64|是|-|椭圆x轴的半径长度，单位：vp。|
|radiusY|Float64|是|-|椭圆y轴的半径长度，单位：vp。|
|rotation|Float64|是|-|椭圆的旋转角度，单位为弧度。|
|startAngle|Float64|是|-|椭圆绘制的起始点角度，以弧度表示。|
|endAngle|Float64|是|-|椭圆绘制的结束点角度，以弧度表示。|
|counterclockwise|?Bool|否|None| **命名参数。** 是否以逆时针方向绘制椭圆。</br>true:逆时针方向绘制椭圆。</br>false:顺时针方向绘制椭圆。|

### func rect(Float64, Float64, Float64, Float64)

```cangjie
public func rect(x: Float64, y: Float64, width: Float64, height: Float64): Unit
```

**功能：** 创建矩形路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|指定矩形的左上角x坐标值。<br>默认单位：vp。|
|y|Float64|是|-|指定矩形的左上角y坐标值。<br>默认单位：vp。|
|width|Float64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|height|Float64|是|-|指定矩形的高度。<br>默认单位：vp。|

### func fill(?CanvasFillRule)

```cangjie
public func fill(fillRule!: ?CanvasFillRule = None): Unit
```

**功能：** 根据当前填充样式填充现有路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fillRule|?[CanvasFillRule](cj-common-types.md#enum-canvasfillrule)|否|None|**命名参数。** 指定要剪切对象的规则。|