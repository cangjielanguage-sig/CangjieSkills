### func createRadialGradient(Float64, Float64, Float64, Float64, Float64, Float64)

```cangjie
public func createRadialGradient(x0: Float64, y0: Float64, r0: Float64, x1: Float64, y1: Float64, r1: Float64): CanvasGradient
```

**功能：** 创建一个径向渐变色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x0|Float64|是|-|起始圆的x轴坐标。<br>默认单位：vp。|
|y0|Float64|是|-|起始圆的y轴坐标。<br>默认单位：vp。|
|r0|Float64|是|-|起始圆的半径。必须是非负且有限的。<br>默认单位：vp。|
|x1|Float64|是|-|终点圆的x轴坐标。<br>默认单位：vp。|
|y1|Float64|是|-|终点圆的y轴坐标。<br>默认单位：vp。|
|r1|Float64|是|-|终点圆的半径。必须为非负且有限的。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:---|:---|
|[CanvasGradient](cj-canvas-drawing-canvas.md#class-canvasgradient)|渐变对象。使用完毕后需要释放。|

### func createConicGradient(?Float64, ?Float64, ?Float64)

```cangjie
public func createConicGradient(startAngle: ?Float64, x: ?Float64, y: ?Float64): CanvasGradient
```

**功能：** 创建一个圆锥渐变色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|startAngle|?Float64|是|-|开始渐变的角度。角度测量从中心右侧水平开始，顺时针移动。<br>单位：弧度。|
|x|?Float64|是|-|圆锥渐变的中心x轴坐标。<br>默认单位：vp。|
|y|?Float64|是|-|圆锥渐变的中心y轴坐标。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:---|:---|
|[CanvasGradient](cj-canvas-drawing-canvas.md#class-canvasgradient)|新的CanvasGradient对象，用于在canvas上创建渐变效果。|

### func drawImage(ImageBitmap, ?Float64, ?Float64)

```cangjie
public func drawImage(image: ImageBitmap, dx: ?Float64, dy: ?Float64): Unit
```

**功能：** 进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|image|[ImageBitmap](cj-canvas-drawing-imagebitmap.md)|是|-|图片资源。|
|dx|?Float64|是|-|绘制区域左上角在 x 轴的位置。<br>默认单位：vp。|
|dy|?Float64|是|-|绘制区域左上角在 y 轴的位置。<br>默认单位：vp。|

### func drawImage(ImageBitmap, ?Float64, ?Float64, ?Float64, ?Float64)

```cangjie
public func drawImage(image: ImageBitmap, dx: ?Float64, dy: ?Float64, dw: ?Float64, dh: ?Float64): Unit
```

**功能：** 进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|image|[ImageBitmap](cj-canvas-drawing-imagebitmap.md)|是|-|图片资源。|
|dx|?Float64|是|-|绘制区域左上角在 x 轴的位置。<br>默认单位：vp。|
|dy|?Float64|是|-|绘制区域左上角在 y 轴的位置。<br>默认单位：vp。|
|dw|?Float64|是|-|绘制区域的宽度。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。<br>默认单位：vp。|
|dh|?Float64|是|-|绘制区域的高度。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。<br>默认单位：vp。|