### func fill(?Path2D, ?CanvasFillRule)

```cangjie
public func fill(path: ?Path2D, fillRule!: ?CanvasFillRule = None): Unit
```

**功能：** 根据当前填充样式填充指定路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|?[Path2D](cj-canvas-drawing-path2d.md)|是|-|Path2D剪切路径。|
|fillRule|?[CanvasFillRule](cj-common-types.md#enum-canvasfillrule)|否|None|**命名参数。** 指定要剪切对象的规则。|

### func clip(?CanvasFillRule)

```cangjie
public func clip(fillRule!: ?CanvasFillRule = None): Unit
```

**功能：** 设置当前路径为剪切路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fillRule|?[CanvasFillRule](cj-common-types.md#enum-canvasfillrule)|否|None|**命名参数。** 指定要剪切对象的规则。|

### func clip(?Path2D, ?CanvasFillRule)

```cangjie
public func clip(path: ?Path2D, fillRule!: ?CanvasFillRule = None): Unit
```

**功能：** 根据指定路径进行裁剪。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|?[Path2D](cj-canvas-drawing-path2d.md)|是|-|Path2D剪切路径。|
|fillRule|?[CanvasFillRule](cj-common-types.md#enum-canvasfillrule)|否|None|**命名参数。** 指定要剪切对象的规则。|

### func rotate(Float64)

```cangjie
public func rotate(angle: Float64): Unit
```

**功能：** 针对当前坐标轴进行顺时针旋转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|angle|Float64|是|-|设置顺时针旋转的弧度值，可以通过Float64.PI / 180将角度转换为弧度值。<br>单位：弧度。|

### func scale(Float64, Float64)

```cangjie
public func scale(x: Float64, y: Float64): Unit
```

**功能：** 设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|设置水平方向的缩放值。<br>默认单位：vp。|
|y|Float64|是|-|设置垂直方向的缩放值。<br>默认单位：vp。|

### func transform(Float64, Float64, Float64, Float64, Float64, Float64)

```cangjie
public func transform(
    a: Float64,
    b: Float64,
    c: Float64,
    d: Float64,
    e: Float64,
    f: Float64
): Unit
```

**功能：** transform方法对应一个变换矩阵。在对一个图形进行变化时，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|a|Float64|是|-|指定水平缩放值。|
|b|Float64|是|-|指定水平倾斜值。|
|c|Float64|是|-|指定垂直倾斜值。|
|d|Float64|是|-|指定垂直缩放值。|
|e|Float64|是|-|指定水平移动值。<br>默认单位：vp。|
|f|Float64|是|-|指定垂直移动值。<br>默认单位：vp。|