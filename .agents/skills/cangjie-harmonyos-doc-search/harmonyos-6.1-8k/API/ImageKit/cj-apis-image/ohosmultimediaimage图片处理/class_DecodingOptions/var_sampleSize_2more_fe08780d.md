### var sampleSize

```cangjie
public var sampleSize: UInt32
```

**功能：** 缩略图采样大小。当前只能取1。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### init(UInt32, UInt32, Bool, Size, Region, PixelMapFormat, UInt32, Int32, ?ColorSpaceManager, DecodingDynamicRange)

```cangjie
public init(sampleSize!: UInt32 = 1, rotate!: UInt32 = 0, editable!: Bool = false,
    desiredSize!: Size = Size(0, 0), desiredRegion!: Region = Region(Size(0, 0), 0, 0),
    desiredPixelFormat!: PixelMapFormat = Unknown, index!: UInt32 = 0, fitDensity!: Int32 = 0,
    desiredColorSpace!: ?ColorSpaceManager = None, desiredDynamicRange!: DecodingDynamicRange = Sdr)
```

**功能：** 创建DecodingOptions对象。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sampleSize|UInt32|否|1|**命名参数。** 缩略图采样大小，默认值为1。当前只能取1。|
|rotate|UInt32|否|0|**命名参数。** 旋转角度。默认值为0。|
|editable|Bool|否|false|**命名参数。** true表示可编辑，false表示不可编辑。默认值为false。当取值为false时，图片不可二次编辑，如writePixels操作将失败。|
|desiredSize|[Size](#class-size)|否|Size(0, 0)|**命名参数。** 期望输出大小，必须为正整数，若与原尺寸比例不一致，则会进行拉伸/缩放到指定尺寸，默认为原始尺寸。|
|desiredRegion|[Region](#class-region)|否|Region(Size(0, 0), 0, 0)|**命名参数。** 解码图像中由Region指定的矩形区域，当原始图像很大而只需要解码图像的一部分时，可以设置该参数，有助于提升性能，默认为原始大小。|
|desiredPixelFormat|[PixelMapFormat](#enum-pixelmapformat)|否|Unknown|**命名参数。** 解码的像素格式。默认值为Unknown。仅支持设置：Rgba8888、Bgra8888和Rgb565。有透明通道图片格式不支持设置Rgb565，如PNG、GIF、ICO和WEBP。|
|index|UInt32|否|0|**命名参数。** 解码图片序号。默认值为0，表示第一张图片。当取值为N时，表示第N+1张图片。单帧图片场景中index取值只能为0，动图等多帧图片场景中index的取值范围为：0~（帧数-1）。|
|fitDensity|Int32|否|0|**命名参数。** 图像像素密度，单位为ppi。默认值为0。|
|desiredColorSpace|?[ColorSpaceManager](../ArkGraphics2D/cj-apis-color_manager.md#class-colorspacemanager)|否|None|**命名参数。** 目标色彩空间。色域默认值为Unknown。|
|desiredDynamicRange|[DecodingDynamicRange](#enum-decodingdynamicrange)|否|Sdr|**命名参数。** 目标动态范围，默认值为Sdr。<br>如果平台不支持Hdr，设置无效，默认解码为Sdr内容。 |