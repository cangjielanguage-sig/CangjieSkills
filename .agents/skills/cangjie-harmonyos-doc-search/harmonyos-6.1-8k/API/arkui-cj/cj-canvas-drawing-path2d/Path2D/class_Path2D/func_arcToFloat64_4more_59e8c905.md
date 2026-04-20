### func arcTo(Float64, Float64, Float64, Float64, Float64)

```cangjie
public func arcTo(
    x1: Float64,
    y1: Float64,
    x2: Float64,
    y2: Float64,
    radius: Float64
): Unit
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

### func quadraticCurveTo(Float64, Float64, Float64, Float64)

```cangjie
public func quadraticCurveTo(
    cpx: Float64,
    cpy: Float64,
    x: Float64,
    y: Float64
): Unit
```

**功能：** 创建二次贝塞尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cpx|Float64|是|-|贝塞尔参数的x坐标值。<br>默认单位：vp。|
|cpy|Float64|是|-|贝塞尔参数的y坐标值。<br>默认单位：vp。|
|x|Float64|是|-|路径结束时的x坐标值。<br>默认单位：vp。|
|y|Float64|是|-|路径结束时的y坐标值。<br>默认单位：vp。|

### func bezierCurveTo(Float64, Float64, Float64, Float64, Float64, Float64)

```cangjie
public func bezierCurveTo(
    cp1x: Float64,
    cp1y: Float64,
    cp2x: Float64,
    cp2y: Float64,
    x: Float64,
    y: Float64
): Unit
```

**功能：** 创建三次贝塞尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cp1x|Float64|是|-|第一个贝塞尔参数的x坐标值。<br>默认单位：vp。|
|cp1y|Float64|是|-|第一个贝塞尔参数的y坐标值。<br>默认单位：vp。|
|cp2x|Float64|是|-|第二个贝塞尔参数的x坐标值。<br>默认单位：vp。|
|cp2y|Float64|是|-|第二个贝塞尔参数的y坐标值。<br>默认单位：vp。|
|x|Float64|是|-|路径结束时的x坐标值。<br>默认单位：vp。|
|y|Float64|是|-|路径结束时的y坐标值。<br>默认单位：vp。|

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
|x|Float64|是|-|椭圆圆心的x轴坐标。<br>默认单位：vp。|
|y|Float64|是|-|椭圆圆心的y轴坐标。<br>默认单位：vp。|
|radiusX|Float64|是|-|椭圆x轴的半径长度。<br>默认单位：vp。|
|radiusY|Float64|是|-|椭圆y轴的半径长度。<br>默认单位：vp。|
|rotation|Float64|是|-|椭圆的旋转角度。<br>单位：弧度。|
|startAngle|Float64|是|-|椭圆绘制的起始点角度。<br>单位：弧度。|
|endAngle|Float64|是|-|椭圆绘制的结束点角度。<br>单位：弧度。|
|counterclockwise|?Bool|否|None| **命名参数。** 是否以逆时针方向绘制椭圆。<br>true:逆时针方向绘制椭圆。<br>false:顺时针方向绘制椭圆。|