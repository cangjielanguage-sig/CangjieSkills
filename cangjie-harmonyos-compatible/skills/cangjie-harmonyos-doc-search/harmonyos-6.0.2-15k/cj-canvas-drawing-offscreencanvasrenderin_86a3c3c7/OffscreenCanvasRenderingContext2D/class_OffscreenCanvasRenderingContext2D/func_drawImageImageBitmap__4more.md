### func drawImage(ImageBitmap, Int64, Int64, Int64, Int64, Int64, Int64, Int64, Int64)

```cangjie
public func drawImage(
    image: ImageBitmap,
    sx: Int64,
    sy: Int64,
    sWidth: Int64,
    sHeight: Int64,
    dx: Int64,
    dy: Int64,
    dWidth: Int64,
    dHeight: Int64
): Unit
```

**功能：** 进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|image|[ImageBitmap](./cj-canvas-drawing-imagebitmap.md#class-imagebitmap)|是|-|图片资源。|
|sx|Int64|是|-| 裁切源图像时距离源图像左上角的x坐标值。<br>image类型为ImageBitmap时，默认单位：vp。|
|sy|Int64|是|-| 裁切源图像时距离源图像左上角的y坐标值。<br>image类型为ImageBitmap时，默认单位：vp。|
|sWidth|Int64 |是|-|裁切源图像时需要裁切的宽度。<br>image类型为ImageBitmap时，默认单位：vp。 |
|sHeight|Int64|是|-|裁切源图像时需要裁切的高度。<br>image类型为ImageBitmap时，默认单位：vp。 |
|dx|Int64|是|-|绘制区域左上角在x轴的位置。<br>默认单位：vp。|
|dy|Int64|是|-|绘制区域左上角在y轴的位置。<br>默认单位：vp。|
|dWidth|Int64 |是|-|绘制区域的宽度。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。<br>默认单位：vp。 |
|dHeight|Int64|是|-|绘制区域的高度。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。<br>默认单位：vp。 |

### func drawImage(PixelMap, Float64, Float64)

```cangjie
public func drawImage(pixelMap: PixelMap, dx: Float64, dy: Float64): Unit
```

**功能：** 进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pixelMap|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap) |是|-|图片资源。|
|dx|Float64|是|-|绘制区域左上角在x轴的位置。<br>默认单位：vp。|
|dy|Float64|是|-|绘制区域左上角在y轴的位置。<br>默认单位：vp。|

### func drawImage(PixelMap, Int64, Int64)

```cangjie
public func drawImage(pixelMap: PixelMap, dx: Int64, dy: Int64): Unit
```

**功能：** 进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pixelMap|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap) |是|-|图片资源。|
|dx|Int64|是|-|绘制区域左上角在x轴的位置。<br>默认单位：vp。|
|dy|Int64|是|-|绘制区域左上角在y轴的位置。<br>默认单位：vp。|

### func drawImage(PixelMap, Float64, Float64, Float64, Float64)

```cangjie
public func drawImage(pixelMap: PixelMap, dx: Float64, dy: Float64, dWidth: Float64, dHeight: Float64): Unit
```

**功能：** 进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pixelMap|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap) |是|-|图片资源。|
|dx|Float64|是|-|绘制区域左上角在x轴的位置。<br>默认单位：vp。|
|dy|Float64|是|-|绘制区域左上角在y轴的位置。<br>默认单位：vp。|
|dWidth |Float64|是|-| 绘制区域的宽度。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。<br>默认单位：vp。|
|dHeight|Float64|是|-| 绘制区域的高度。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。<br>默认单位：vp。|