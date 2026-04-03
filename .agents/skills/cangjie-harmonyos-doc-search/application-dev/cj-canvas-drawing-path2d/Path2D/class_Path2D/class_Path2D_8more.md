## class Path2D

```cangjie
public class Path2D {
    public init()
    public init(d: ?String)
}
```

**功能：** 路径对象，支持通过对象的接口进行路径的描述，并通过Canvas的stroke接口或者fill接口进行绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init()

```cangjie
public init()
```

**功能：** 构造一个空的Path2D对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?String)

```cangjie
public init(d: ?String)
```

**功能：** 使用符合SVG路径描述规范的路径字符串构造一个Path2D对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|d|?String|是|-|符合 SVG 路径描述规范的路径字符串，格式参考Path中SVG路径描述规范说明。|

### func addPath(?Path2D)

```cangjie
public func addPath(path2D: ?Path2D): Unit
```

**功能：** 将另一个路径添加到当前的路径对象中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path2D|?[Path2D](./cj-canvas-drawing-path2d.md#class-path2d)|是|-|需要添加到当前路径的路径对象，路径单位：px。|

### func setTransform(?Float64, ?Float64, ?Float64, ?Float64, ?Float64, ?Float64)

```cangjie
public func setTransform(
    scaleX: ?Float64,
    skewX: ?Float64,
    skewY: ?Float64,
    scaleY: ?Float64,
    translateX: ?Float64,
    translateY: ?Float64
): Unit
```

**功能：** 对路径对象进行缩放、倾斜和平移的操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scaleX|?Float64|是|-|x轴方向上缩放值。|
|skewX|?Float64|是|-|x轴方向上倾斜值。|
|skewY|?Float64|是|-|y轴方向上倾斜值。|
|scaleY|?Float64|是|-|y轴方向上缩放值。|
|translateX|?Float64|是|-|x轴方向上平移值。|
|translateY|?Float64|是|-|y轴方向上平移值。|

### func moveTo(Float64, Float64)

```cangjie
public func moveTo(x: Float64, y: Float64): Unit
```

**功能：** 将路径的当前坐标点移动到目标点，移动过程中不绘制线条。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|目标点X轴坐标。<br>默认单位：vp。|
|y|Float64|是|-|目标点Y轴坐标。<br>默认单位：vp。|

### func lineTo(Float64, Float64)

```cangjie
public func lineTo(x: Float64, y: Float64): Unit
```

**功能：** 从当前点绘制一条直线到目标点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|目标点X轴坐标。<br>默认单位：vp。|
|y|Float64|是|-|目标点Y轴坐标。<br>默认单位：vp。|

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

**功能：** 绘制弧形路径。

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
|counterclockwise|?Bool|否|None| **命名参数。** 是否逆时针绘制圆弧。<br>true:逆时针方向绘制椭圆。<br>false:顺时针方向绘制椭圆。|