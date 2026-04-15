### func drawImage(PixelMap, ?Float64, ?Float64, ?Float64, ?Float64, ?Float64, ?Float64, ?Float64, ?Float64)

```cangjie
public func drawImage(
    image: PixelMap,
    sx: ?Float64,
    sy: ?Float64,
    sw: ?Float64,
    sh: ?Float64,
    dx: ?Float64,
    dy: ?Float64,
    dw: ?Float64,
    dh: ?Float64
): Unit
```

**功能：** 进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|image|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|绘制到画布上的图片对象。|
|sx|?Float64|是|-|裁切源图像时距离源图像左上角的x坐标值。<br>单位：px。|
|sy|?Float64|是|-|裁切源图像时距离源图像左上角的y坐标值。<br>单位：px。|
|sw|?Float64|是|-|裁切源图像时需要裁切的宽度。<br>单位：px。|
|sh|?Float64|是|-|裁切源图像时需要裁切的高度。<br>单位：px。|
|dx|?Float64|是|-|绘制区域左上角在 x 轴的位置。<br>默认单位：vp。|
|dy|?Float64|是|-|绘制区域左上角在 y 轴的位置。<br>默认单位：vp。|
|dw|?Float64|是|-|绘制区域的宽度。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。<br>默认单位：vp。|
|dh|?Float64|是|-|绘制区域的高度。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。<br>默认单位：vp。|

### func getPixelMap(?Float64, ?Float64, ?Float64, ?Float64)

```cangjie
public func getPixelMap(sx: ?Float64, sy: ?Float64, sw: ?Float64, sh: ?Float64): PixelMap
```

**功能：** 以当前canvas指定区域内的像素创建PixelMap。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sx|?Float64|是|-|需要输出的区域的左上角x坐标。<br>默认单位：vp。|
|sy|?Float64|是|-|需要输出的区域的左上角y坐标。<br>默认单位：vp。|
|sw|?Float64|是|-|需要输出的区域的宽度。<br>默认单位：vp。|
|sh|?Float64|是|-|需要输出的区域的高度。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:---|:---|
|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|PixelMap对象。|

### func reset()

```cangjie
public func reset(): Unit
```

**功能：** 将CanvasRenderingContext2D重置为其默认状态，清除后台缓冲区、绘制状态栈、绘制路径和样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func saveLayer()

```cangjie
public func saveLayer(): Unit
```

**功能：** 创建一个图层。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func restoreLayer()

```cangjie
public func restoreLayer(): Unit
```

**功能：** 恢复图像变换和裁剪状态至saveLayer前的状态，并将图层绘制在canvas上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func resetTransform()

```cangjie
public func resetTransform(): Unit
```

**功能：** 使用单位矩阵重新设置当前矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func getTransform()

```cangjie
public func getTransform(): Matrix2D
```

**功能：** 获取当前被应用到上下文的转换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:---|:---|
|Matrix2D|矩阵对象。|

### func transferFromImageBitmap(?ImageBitmap)

```cangjie
public func transferFromImageBitmap(bitmap: ?ImageBitmap): Unit
```

**功能：** 显示给定的ImageBitmap对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bitmap|?[ImageBitmap](cj-canvas-drawing-imagebitmap.md)|是|-|待显示的ImageBitmap对象。|