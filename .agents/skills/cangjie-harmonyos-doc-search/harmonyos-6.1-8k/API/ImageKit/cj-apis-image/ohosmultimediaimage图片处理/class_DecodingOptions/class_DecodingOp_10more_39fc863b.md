## class DecodingOptions

```cangjie
public class DecodingOptions {
    public var index: UInt32
    public var sampleSize: UInt32
    public var rotate: UInt32
    public var editable: Bool
    public var desiredSize: Size
    public var desiredRegion: Region
    public var desiredPixelFormat: PixelMapFormat
    public var fitDensity: Int32
    public var desiredColorSpace: ?ColorSpaceManager
    public var desiredDynamicRange: DecodingDynamicRange
    public init(sampleSize!: UInt32 = 1, rotate!: UInt32 = 0, editable!: Bool = false,
        desiredSize!: Size = Size(0, 0), desiredRegion!: Region = Region(Size(0, 0), 0, 0),
        desiredPixelFormat!: PixelMapFormat = Unknown, index!: UInt32 = 0, fitDensity!: Int32 = 0,
        desiredColorSpace!: ?ColorSpaceManager = None, desiredDynamicRange!: DecodingDynamicRange = Sdr)
}
```

**功能：** 图像解码设置选项。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### var desiredColorSpace

```cangjie
public var desiredColorSpace:?ColorSpaceManager
```

**功能：** 目标色彩空间。

**类型：** ?[ColorSpaceManager](../ArkGraphics2D/cj-apis-color_manager.md#class-colorspacemanager)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### var desiredDynamicRange

```cangjie
public var desiredDynamicRange: DecodingDynamicRange
```

**功能：** 目标动态范围。

如果平台不支持Hdr，设置无效，默认解码为Sdr内容。

**类型：** [DecodingDynamicRange](#enum-decodingdynamicrange)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### var desiredPixelFormat

```cangjie
public var desiredPixelFormat: PixelMapFormat
```

**功能：** 解码的像素格式。仅支持设置：Rgba8888、Bgra8888和Rgb565。有透明通道图片格式不支持设置Rgb565，如PNG、GIF、ICO和WEBP。

**类型：** [PixelMapFormat](#enum-pixelmapformat)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### var desiredRegion

```cangjie
public var desiredRegion: Region
```

**功能：** 解码图像中由Region指定的矩形区域，当原始图像很大而只需要解码图像的一部分时，可以设置该参数，有助于提升性能。

**类型：** [Region](#class-region)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### var desiredSize

```cangjie
public var desiredSize: Size
```

**功能：** 期望输出大小，必须为正整数，若与原尺寸比例不一致，则会进行拉伸/缩放到指定尺寸。

**类型：** [Size](#class-size)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### var editable

```cangjie
public var editable: Bool
```

**功能：** true表示可编辑，false表示不可编辑。当取值为false时，图片不可二次编辑，如writePixels操作将失败。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### var fitDensity

```cangjie
public var fitDensity: Int32
```

**功能：** 图像像素密度，单位为ppi。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### var index

```cangjie
public var index: UInt32
```

**功能：** 解码图片序号。设置值为0，表示第一张图片。当取值为N时，表示第N+1张图片。单帧图片场景中index取值只能为0，动图等多帧图片场景中index的取值范围为：0~（帧数-1）。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### var rotate

```cangjie
public var rotate: UInt32
```

**功能：** 旋转角度。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22