### init(DecodingDynamicRange, UInt32, UInt32, Bool, Size, Region, PixelMapFormat, UInt32, Int32, ?ColorSpaceManager)

```cangjie
public init(desiredDynamicRange: DecodingDynamicRange, sampleSize!: UInt32 = 1, rotate!: UInt32 = 0,
        editable!: Bool = false, desiredSize!: Size = Size(height: 0, width: 0),
        desiredRegion!: Region = Region(Size(height: 0, width: 0), 0, 0), desiredPixelFormat!: PixelMapFormat = UNKNOWN,
        index!: UInt32 = 0, fitDensity!: Int32 = 0, desiredColorSpace!: ?ColorSpaceManager = None)
```

**功能：** 创建DecodingOptions对象。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|desiredDynamicRange|[DecodingDynamicRange](#enum-decodingdynamicrange)|是|-| **命名参数。** 目标动态范围。<br>通过[CreateIncrementalSource](#func-createincrementalsourcearrayuint8-sourceoptions)创建的imagesource不支持设置此属性，默认解码为SDR内容。<br>如果平台不支持HDR，设置无效，默认解码为SDR内容。 |
|sampleSize|UInt32|否|1| **命名参数。** 缩略图采样大小，当前只能取1。|
|rotate|UInt32|否|0| **命名参数。** 旋转角度。|
|editable|Bool|否|false| **命名参数。** 是否可编辑。当取值为false时，图片不可二次编辑，如crop等操作将失败。|
|desiredSize|[Size](#struct-size)|否|Size(height: 0, width: 0)| **命名参数。** 期望输出大小。|
|desiredRegion|[Region](#struct-region)|否|Region(Size(height: 0, width: 0), 0, 0)| **命名参数。** 解码区域。|
|desiredPixelFormat|[PixelMapFormat](#enum-pixelmapformat)|否|UNKNOWN| **命名参数。** 解码的像素格式。|
|index|UInt32|否|0| **命名参数。** 解码图片序号。|
|fitDensity|Int32|否|0| **命名参数。** 图像像素密度，单位为ppi。|
|desiredColorSpace|[ColorSpaceManager](../ArkGraphics2D/cj-apis-color_manager.md#class-colorspacemanager)|否|None| **命名参数。** 目标色彩空间。|