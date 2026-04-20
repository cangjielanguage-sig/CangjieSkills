## class ImageInfo

```cangjie
public class ImageInfo {
    public var size: Size
    public var density: Int32
    public var stride: Int32
    public var pixelFormat: PixelMapFormat
    public var alphaType: AlphaType
    public var mimeType: String
    public var isHdr: Bool
}
```

**功能：** 表示图片信息。

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

### var density

```cangjie
public var density: Int32
```

**功能：** 像素密度，单位为ppi。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var isHdr

```cangjie
public var isHdr: Bool
```

**功能：** true表示图片为高动态范围（HDR），false表示图片非高动态范围（SDR）。对于[ImageSource](#class-imagesource)，代表源图片是否为HDR；对于[PixelMap](#class-pixelmap)，代表解码后的pixelmap是否为HDR。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var mimeType

```cangjie
public var mimeType: String
```

**功能：** 图片真实格式（MIME type）。

图片解码和图片编码支持格式的范围不同，请避免直接将解码得到的图片真实格式作为图片编码时[PackingOption](#class-packingoption)的format。

可以使用[ImageSource](#class-imagesource)的supportedFormats属性和[ImagePacker](#class-imagepacker)的supportedFormats属性查看解码和编码支持的格式范围。

**类型：** String

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

### var size

```cangjie
public var size: Size
```

**功能：** 图片大小。

**类型：** [Size](#class-size)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var stride

```cangjie
public var stride: Int32
```

**功能：** 跨距，内存中每行像素所占的空间。stride >= region.size.width*4。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22