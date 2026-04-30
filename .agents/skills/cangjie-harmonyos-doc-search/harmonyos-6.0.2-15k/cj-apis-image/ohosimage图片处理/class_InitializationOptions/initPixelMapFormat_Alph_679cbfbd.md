### init(PixelMapFormat, AlphaType, Bool, PixelMapFormat, ScaleMode, Size)

```cangjie
public init(srcPixelFormat: PixelMapFormat, alphaType!: AlphaType = AlphaType.PREMUL, editable!: Bool = false,
        pixelFormat!: PixelMapFormat = PixelMapFormat.BGRA_8888, scaleMode!: ScaleMode = ScaleMode.FIT_TARGET_SIZE,
        size!: Size)
```

**功能：** 创建InitializationOptions对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|srcPixelFormat|[PixelMapFormat](#enum-pixelmapformat)|是|-| **命名参数。** 传入的buffer数据的像素格式。|
|alphaType|[AlphaType](#enum-alphatype)|否|AlphaType.PREMUL| **命名参数。** 透明度。|
|editable|Bool|否|false| **命名参数。** 是否可编辑。|
|pixelFormat|[PixelMapFormat](#enum-pixelmapformat)|否|PixelMapFormat.BGRA_8888| **命名参数。**  像素格式。|
|scaleMode|[ScaleMode](#enum-scalemode)|否|ScaleMode.FIT_TARGET_SIZE| **命名参数。** 缩略值。|
|size|[Size](#struct-size)|是|-| **命名参数。** 创建图片大小。|