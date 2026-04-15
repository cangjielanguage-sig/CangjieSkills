### func strokeRect(Float64, Float64, Float64, Float64)

```cangjie
public func strokeRect(x: Float64, y: Float64, w: Float64, h: Float64): Unit
```

**功能：** 描边指定矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|指定矩形左上角点的x坐标。<br>默认单位：vp。|
|y|Float64|是|-|指定矩形左上角点的y坐标。<br>默认单位：vp。|
|w|Float64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|h|Float64|是|-|指定矩形的高度。<br>默认单位：vp。|

### func clearRect(Float64, Float64, Float64, Float64)

```cangjie
public func clearRect(x: Float64, y: Float64, w: Float64, h: Float64): Unit
```

**功能：** 清除矩形区域的绘制内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|指定矩形左上角点的x坐标。<br>默认单位：vp。|
|y|Float64|是|-|指定矩形左上角点的y坐标。<br>默认单位：vp。|
|w|Float64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|h|Float64|是|-|指定矩形的高度。<br>默认单位：vp。|

### func fillText(String, Float64, Float64, Option\<Float64>)

```cangjie
public func fillText(text: String, x: Float64, y: Float64, maxWidth!: Option<Float64> = Option.None): Unit
```

**功能：** 在指定位置填充指定的文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|需要绘制的文本内容。|
|x|Float64|是|-|需要绘制的文本的左下角x坐标。<br>默认单位：vp。|
|y|Float64|是|-|需要绘制的文本的左下角y坐标。<br>默认单位：vp。|
|maxWidth|Option\<Float64>|否|Option.None|**命名参数。** 指定文本允许的最大宽度。<br>默认单位：vp。<br>初始值：不限制宽度。|

### func strokeText(String, Float64, Float64, Option\<Float64>)

```cangjie
public func strokeText(text: String, x: Float64, y: Float64, maxWidth!: Option<Float64> = Option.None): Unit
```

**功能：** 绘制描边类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|需要绘制的文本内容。|
|x|Float64|是|-|需要绘制的文本的左下角x坐标。<br>默认单位：vp。|
|y|Float64|是|-|需要绘制的文本的左下角y坐标。<br>默认单位：vp。|
|maxWidth|Option\<Float64>|否|Option.None|**命名参数。** 需要绘制的文本的最大宽度。<br>默认单位：vp。|

### func measureText(?String)

```cangjie
public func measureText(text: ?String): TextMetrics
```

**功能：** 该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。不同设备上获取的宽度值可能不同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|?String|是|-|需要进行测量的文本。|

**返回值：**

|类型|说明|
|:---|:---|
|[TextMetrics](cj-canvas-drawing-canvas.md#class-textmetrics)|文本测量结果。|

### func stroke()

```cangjie
public func stroke(): Unit
```

**功能：** 进行边框绘制操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func stroke(Path2D)

```cangjie
public func stroke(path: Path2D): Unit
```

**功能：** 进行边框绘制操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|[Path2D](cj-canvas-drawing-path2d.md)|是|-|指定的描边路径对象。|