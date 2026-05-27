### func bezierCurveTo(Int64, Int64, Int64, Int64, Int64, Int64)

```cangjie
public func bezierCurveTo(
    cp1x: Int64,
    cp1y: Int64,
    cp2x: Int64,
    cp2y: Int64,
    x: Int64,
    y: Int64
): Unit
```

**功能：** 创建三次贝赛尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cp1x|Int64|是|-|第一个贝塞尔参数的x坐标值。<br>默认单位：vp。|
|cp1y|Int64|是|-|第一个贝塞尔参数的y坐标值。<br>默认单位：vp。|
|cp2x|Int64|是|-|第二个贝塞尔参数的x坐标值。<br>默认单位：vp。|
|cp2y|Int64|是|-|第二个贝塞尔参数的y坐标值。<br>默认单位：vp。|
|x|Int64|是|-|路径结束时的x坐标值。<br>默认单位：vp。|
|y|Int64|是|-|路径结束时的y坐标值。<br>默认单位：vp。|

### func closePath()

```cangjie
public func closePath(): Unit
```

**功能：** 将路径的当前点移回到路径的起点，当前点到起点间画一条直线。如果形状已经闭合或只有一个点，则此功能不执行任何操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func ellipse(Float64, Float64, Float64, Float64, Float64, Float64, Float64, Bool)

```cangjie
public func ellipse(
    x: Float64,
    y: Float64,
    radiusX: Float64,
    radiusY: Float64,
    rotation: Float64,
    startAngle: Float64,
    endAngle: Float64,
    anticlockwise!: Bool = false
): Unit
```

**功能：** 在规定的矩形区域绘制一个椭圆。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|椭圆圆心的x轴坐标。<br>默认单位：vp。|
|y|Float64|是|-|椭圆圆心的y轴坐标。<br>默认单位：vp。|
|radiusX|Float64|是|-|椭圆x轴的半径长度。<br>默认单位：vp。|
|radiusY|Float64|是|-|椭圆y轴的半径长度。<br>默认单位：vp。|
|rotation|Float64|是|-|椭圆的旋转角度。<br>单位：弧度。|
|startAngle|Float64|是|-|椭圆绘制的起始点角度。<br>单位：弧度。|
|endAngle|Float64|是|-|椭圆绘制的结束点角度。<br>单位：弧度。|
|anticlockwise|Bool|否|false| **命名参数。** 是否以逆时针方向绘制椭圆。<br>true:逆时针方向绘制椭圆。<br>false:顺时针方向绘制椭圆。|

### func ellipse(Int64, Int64, Int64, Int64, Int64, Int64, Int64, Bool)

```cangjie
public func ellipse(
    x: Int64,
    y: Int64,
    radiusX: Int64,
    radiusY: Int64,
    rotation: Int64,
    startAngle: Int64,
    endAngle: Int64,
    anticlockwise!: Bool = false
): Unit
```

**功能：** 在规定的矩形区域绘制一个椭圆。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|椭圆圆心的x轴坐标。<br>默认单位：vp。|
|y|Int64|是|-|椭圆圆心的y轴坐标。<br>默认单位：vp。|
|radiusX|Int64|是|-|椭圆x轴的半径长度。<br>默认单位：vp。|
|radiusY|Int64|是|-|椭圆y轴的半径长度。<br>默认单位：vp。|
|rotation|Int64|是|-|椭圆的旋转角度。<br>单位：弧度。|
|startAngle|Int64|是|-|椭圆绘制的起始点角度。<br>单位：弧度。|
|endAngle|Int64|是|-|椭圆绘制的结束点角度。<br>单位：弧度。|
|anticlockwise|Bool|否|false| **命名参数。** 是否以逆时针方向绘制椭圆。<br>true:逆时针方向绘制椭圆。<br>false:顺时针方向绘制椭圆。|

### func lineTo(Float64, Float64)

```cangjie
public func lineTo(x: Float64, y: Float64): Unit
```

**功能：** 从当前点绘制一条直线到目标点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|目标点X轴坐标。<br>默认单位：vp。|
|y|Float64|是|-|目标点Y轴坐标。<br>默认单位：vp。|