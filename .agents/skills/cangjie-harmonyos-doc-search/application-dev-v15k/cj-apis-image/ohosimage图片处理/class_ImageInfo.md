## class ImageInfo

```cangjie
public class ImageInfo {
    public var size: Size,
    public var density: Int32,
    public var stride: Int32,
    public var pixelFormat: PixelMapFormat,
    public var alphaType: AlphaType,
    public var mimeType: String,
    public var isHdr: Bool
    public init(size: Size, density: Int32)
    public init(size: Size, density: Int32, stride: Int32, pixelFormat: PixelMapFormat, alphaType: AlphaType,
        mimeType: String, isHdr: Bool)
}
```

**功能：** 表示图片信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### var alphaType

```cangjie
public var alphaType: AlphaType
```

**功能：** 透明度。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** [AlphaType](#enum-alphatype)

**读写能力：** 可读写

**起始版本：** 19

### var density

```cangjie
public var density: Int32
```

**功能：** 像素密度，单位为ppi。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### var isHdr

```cangjie
public var isHdr: Bool
```

**功能：** 图片是否为高动态范围（HDR）。对于[ImageSource](#class-imagesource)，代表源图片是否为HDR；对于[PixelMap](#class-pixelmap)，代表解码后的pixelmap是否为HDR。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var mimeType

```cangjie
public var mimeType: String
```

**功能：** 图片真实格式（MIME type）。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var pixelFormat

```cangjie
public var pixelFormat: PixelMapFormat
```

**功能：** 像素格式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** [PixelMapFormat](#enum-pixelmapformat)

**读写能力：** 可读写

**起始版本：** 19

### var size

```cangjie
public var size: Size
```

**功能：** 图片大小。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** [Size](#struct-size)

**读写能力：** 可读写

**起始版本：** 12

### var stride

```cangjie
public var stride: Int32
```

**功能：** 跨距，内存中每行像素所占的空间。stride >= region.size.width*4。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### init(Size, Int32)

```cangjie
public init(size: Size, density: Int32)
```

**功能：** 创建ImageInfo对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Size](#struct-size)|是|-|图片大小。|
|density|Int32|是|-|像素密度，单位为ppi。|

### init(Size, Int32, Int32, PixelMapFormat, AlphaType, String, Bool)

```cangjie
public init(size: Size, density: Int32, stride: Int32, pixelFormat: PixelMapFormat, alphaType: AlphaType,
        mimeType: String, isHdr: Bool)
```

**功能：** 创建ImageInfo对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Size](#struct-size)|是|-|图片大小。|
|density|Int32|是|-|像素密度，单位为ppi。|
|stride|Int32|是|-|跨距，内存中每行像素所占的空间。stride >= region.size.width*4。|
|pixelFormat|[PixelMapFormat](#enum-pixelmapformat)|是|-| 像素格式。|
|alphaType|[AlphaType](#enum-alphatype)|是|-|透明度。|
|mimeType|String|是|-|图片真实格式（MIME type）。|
|isHdr|Bool|是|-|图片是否为高动态范围（HDR）。对于[ImageSource](#class-imagesource)，代表源图片是否为HDR；对于[PixelMap](#class-pixelmap)，代表解码后的pixelmap是否为HDR。|