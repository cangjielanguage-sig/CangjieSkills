### func drawImage(ImageBitmap, ?Float64, ?Float64, ?Float64, ?Float64, ?Float64, ?Float64, ?Float64, ?Float64)

```cangjie
public func drawImage(
    image: ImageBitmap,
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
|image|[ImageBitmap](cj-canvas-drawing-imagebitmap.md)|是|-|图片资源。|
|sx|?Float64|是|-|裁切源图像时距离源图像左上角的x坐标值。<br>单位：px。|
|sy|?Float64|是|-|裁切源图像时距离源图像左上角的y坐标值。<br>单位：px。|
|sw|?Float64|是|-|裁切源图像时需要裁切的宽度。<br>单位：px。|
|sh|?Float64|是|-|裁切源图像时需要裁切的高度。<br>单位：px。|
|dx|?Float64|是|-|绘制区域左上角在 x 轴的位置。<br>默认单位：vp。|
|dy|?Float64|是|-|绘制区域左上角在 y 轴的位置。<br>默认单位：vp。|
|dw|?Float64|是|-|绘制区域的宽度。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。<br>默认单位：vp。|
|dh|?Float64|是|-|绘制区域的高度。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。<br>默认单位：vp。|

### func drawImage(PixelMap, ?Float64, ?Float64)

```cangjie
public func drawImage(image: PixelMap, dx: ?Float64, dy: ?Float64): Unit
```

**功能：** 进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|image|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|绘制到画布上的图片对象。|
|dx|?Float64|是|-|绘制区域左上角在 x 轴的位置。<br>默认单位：vp。|
|dy|?Float64|是|-|绘制区域左上角在 y 轴的位置。<br>默认单位：vp。|

### func drawImage(PixelMap, ?Float64, ?Float64, ?Float64, ?Float64)

```cangjie
public func drawImage(image: PixelMap, dx: ?Float64, dy: ?Float64, dw: ?Float64, dh: ?Float64): Unit
```

**功能：** 进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|image|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|绘制到画布上的图片对象。|
|dx|?Float64|是|-|绘制区域左上角在 x 轴的位置。<br>默认单位：vp。|
|dy|?Float64|是|-|绘制区域左上角在 y 轴的位置。<br>默认单位：vp。|
|dw|?Float64|是|-|绘制区域的宽度。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。<br>默认单位：vp。|
|dh|?Float64|是|-|绘制区域的高度。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。<br>默认单位：vp。|