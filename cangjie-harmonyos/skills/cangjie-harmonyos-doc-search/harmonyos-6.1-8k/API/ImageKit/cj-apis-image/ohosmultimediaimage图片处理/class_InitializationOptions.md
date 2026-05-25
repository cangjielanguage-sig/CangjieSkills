## class InitializationOptions

```cangjie
public class InitializationOptions {
    public var alphaType: AlphaType
    public var editable: Bool
    public var srcPixelFormat: PixelMapFormat
    public var pixelFormat: PixelMapFormat
    public var scaleMode: ScaleMode
    public var size: Size
    public init(size: Size, alphaType!: AlphaType = AlphaType.Premul, editable!: Bool = false, srcPixelFormat!: PixelMapFormat = PixelMapFormat.Bgra8888,
        pixelFormat!: PixelMapFormat = PixelMapFormat.Rgba8888, scaleMode!: ScaleMode = ScaleMode.FitTargetSize)
}
```

**功能：** PixelMap的初始化选项。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var alphaType

```cangjie
public var alphaType: AlphaType
```

**功能：** 透明度。

**类型：** [AlphaType](#enum-alphatype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var editable

```cangjie
public var editable: Bool
```

**功能：** true表示可编辑，false表示不可编辑。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var pixelFormat

```cangjie
public var pixelFormat: PixelMapFormat
```

**功能：** 像素格式。

**类型：** [PixelMapFormat](#enum-pixelmapformat)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var scaleMode

```cangjie
public var scaleMode: ScaleMode
```

**功能：** 缩略值。

**类型：** [ScaleMode](#enum-scalemode)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var size

```cangjie
public var size: Size
```

**功能：** 创建图片大小。

**类型：** [Size](#class-size)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var srcPixelFormat

```cangjie
public var srcPixelFormat: PixelMapFormat
```

**功能：** 传入的buffer数据的像素格式。

**类型：** [PixelMapFormat](#enum-pixelmapformat)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### init(Size, AlphaType, Bool, PixelMapFormat, PixelMapFormat, ScaleMode)

```cangjie
public init(size: Size, alphaType!: AlphaType = AlphaType.Premul, editable!: Bool = false, srcPixelFormat!: PixelMapFormat = PixelMapFormat.Bgra8888,
    pixelFormat!: PixelMapFormat = PixelMapFormat.Rgba8888, scaleMode!: ScaleMode = ScaleMode.FitTargetSize)
```

**功能：** 创建InitializationOptions对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Size](#class-size)|是|-|**命名参数。** 创建图片大小。|
|alphaType|[AlphaType](#enum-alphatype)|否|AlphaType.Premul|**命名参数。** 透明度。默认值为AlphaType.Premul。|
|editable|Bool|否|false|**命名参数。** true表示可编辑，false表示不可编辑。默认值为false。|
|srcPixelFormat|[PixelMapFormat](#enum-pixelmapformat)|否|PixelMapFormat.Bgra8888|**命名参数。** 传入的buffer数据的像素格式。默认值为PixelMapFormat.Bgra8888。|
|pixelFormat|[PixelMapFormat](#enum-pixelmapformat)|否|PixelMapFormat.Rgba8888|**命名参数。**  生成的pixelMap的像素格式。默认值为PixelMapFormat.Rgba8888。|
|scaleMode|[ScaleMode](#enum-scalemode)|否|ScaleMode.FitTargetSize|**命名参数。** 缩略值。默认值为ScaleMode.FitTargetSize。|