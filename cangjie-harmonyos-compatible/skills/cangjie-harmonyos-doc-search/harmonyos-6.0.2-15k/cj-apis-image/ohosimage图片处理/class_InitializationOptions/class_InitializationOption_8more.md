## class InitializationOptions

```cangjie
public class InitializationOptions {
    public var alphaType: AlphaType
    public var editable: Bool
    public var srcPixelFormat: PixelMapFormat
    public var pixelFormat: PixelMapFormat
    public var scaleMode: ScaleMode
    public var size: Size
    public init(alphaType!: AlphaType = AlphaType.PREMUL, editable!: Bool = false,
        pixelFormat!: PixelMapFormat = PixelMapFormat.BGRA_8888, scaleMode!: ScaleMode = ScaleMode.FIT_TARGET_SIZE,
        size!: Size)
    public init(srcPixelFormat: PixelMapFormat, alphaType!: AlphaType = AlphaType.PREMUL, editable!: Bool = false,
        pixelFormat!: PixelMapFormat = PixelMapFormat.BGRA_8888, scaleMode!: ScaleMode = ScaleMode.FIT_TARGET_SIZE,
        size!: Size)
}
```

**功能：** PixelMap的初始化选项。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### var alphaType

```cangjie
public var alphaType: AlphaType = AlphaType.PREMUL
```

**功能：** 透明度。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**类型：** [AlphaType](#enum-alphatype)

**读写能力：** 可读写

**起始版本：** 12

### var editable

```cangjie
public var editable: Bool = false
```

**功能：** 是否可编辑。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

### var pixelFormat

```cangjie
public var pixelFormat: PixelMapFormat = PixelMapFormat.BGRA_8888
```

**功能：** 像素格式。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**类型：** [PixelMapFormat](#enum-pixelmapformat)

**读写能力：** 可读写

**起始版本：** 12

### var scaleMode

```cangjie
public var scaleMode: ScaleMode = ScaleMode.FIT_TARGET_SIZE
```

**功能：** 缩略值。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**类型：** [ScaleMode](#enum-scalemode)

**读写能力：** 可读写

**起始版本：** 12

### var size

```cangjie
public var size: Size
```

**功能：** 创建图片大小。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**类型：** [Size](#struct-size)

**读写能力：** 可读写

**起始版本：** 12

### var srcPixelFormat

```cangjie
public var srcPixelFormat: PixelMapFormat = PixelMapFormat.BGRA_8888
```

**功能：** 传入的buffer数据的像素格式。默认值为BGRA_8888。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**类型：** [PixelMapFormat](#enum-pixelmapformat)

**读写能力：** 可读写

**起始版本：** 19

### init(AlphaType, Bool, PixelMapFormat, ScaleMode, Size)

```cangjie
public init(alphaType!: AlphaType = AlphaType.PREMUL, editable!: Bool = false,
        pixelFormat!: PixelMapFormat = PixelMapFormat.BGRA_8888, scaleMode!: ScaleMode = ScaleMode.FIT_TARGET_SIZE,
        size!: Size)
```

**功能：** 创建InitializationOptions对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|alphaType|[AlphaType](#enum-alphatype)|否|AlphaType.PREMUL| **命名参数。** 透明度。|
|editable|Bool|否|false| **命名参数。** 是否可编辑。|
|pixelFormat|[PixelMapFormat](#enum-pixelmapformat)|否|PixelMapFormat.BGRA_8888| **命名参数。**  像素格式。|
|scaleMode|[ScaleMode](#enum-scalemode)|否|ScaleMode.FIT_TARGET_SIZE| **命名参数。** 缩略值。|
|size|[Size](#struct-size)|是|-| **命名参数。** 创建图片大小。|