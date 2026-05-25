## class DecodingOptions

```cangjie
public class DecodingOptions {
    public let sampleSize: UInt32
    public let rotate: UInt32
    public let editable: Bool
    public let desiredSize: Size
    public let desiredRegion: Region
    public let desiredPixelFormat: PixelMapFormat
    public let index: UInt32
    public let fitDensity: Int32
    public let desiredColorSpace: ?ColorSpaceManager
    public let desiredDynamicRange: DecodingDynamicRange
    public init(sampleSize!: UInt32 = 1, rotate!: UInt32 = 0, editable!: Bool = false,
            desiredSize!: Size = Size(height: 0, width: 0), desiredRegion!: Region = Region(Size(height: 0, width: 0), 0, 0),
            desiredPixelFormat!: PixelMapFormat = UNKNOWN, index!: UInt32 = 0, fitDensity!: Int32 = 0,
            desiredColorSpace!: ?ColorSpaceManager = None)
    public init(desiredDynamicRange: DecodingDynamicRange, sampleSize!: UInt32 = 1, rotate!: UInt32 = 0,
            editable!: Bool = false, desiredSize!: Size = Size(height: 0, width: 0),
            desiredRegion!: Region = Region(Size(height: 0, width: 0), 0, 0), desiredPixelFormat!: PixelMapFormat = UNKNOWN,
            index!: UInt32 = 0, fitDensity!: Int32 = 0, desiredColorSpace!: ?ColorSpaceManager = None)
}
```

**功能：** 图像解码设置选项。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

### let desiredColorSpace

```cangjie
public let desiredColorSpace: ?ColorSpaceManager = None
```

**功能：** 目标色彩空间。

**类型：** ?[ColorSpaceManager](../ArkGraphics2D/cj-apis-color_manager.md#class-colorspacemanager)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

### let desiredDynamicRange

```cangjie
public let desiredDynamicRange: DecodingDynamicRange = SDR
```

**功能：** 目标动态范围，默认值为SDR。

通过[CreateIncrementalSource](#func-createincrementalsourcearrayuint8-sourceoptions)创建的imagesource不支持设置此属性，默认解码为SDR内容。

如果平台不支持HDR，设置无效，默认解码为SDR内容。

**类型：** [DecodingDynamicRange](#enum-decodingdynamicrange)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 19

### let desiredPixelFormat

```cangjie
public let desiredPixelFormat: PixelMapFormat = UNKNOWN
```

**功能：** 解码的像素格式。

**类型：** [PixelMapFormat](#enum-pixelmapformat)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

### let desiredRegion

```cangjie
public let desiredRegion: Region = Region(Size(height: 0, width: 0), 0, 0)
```

**功能：** 解码区域。

**类型：** [Region](#struct-region)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

### let desiredSize

```cangjie
public let desiredSize: Size = Size(height: 0, width: 0)
```

**功能：** 期望输出大小。

**类型：** [Size](#struct-size)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

### let editable

```cangjie
public let editable: Bool = false
```

**功能：** 是否可编辑。当取值为false时，图片不可二次编辑，如crop等操作将失败。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

### let fitDensity

```cangjie
public let fitDensity: Int32 = 0
```

**功能：** 图像像素密度，单位为ppi。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

### let index

```cangjie
public let index: UInt32 = 0
```

**功能：** 解码图片序号。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12