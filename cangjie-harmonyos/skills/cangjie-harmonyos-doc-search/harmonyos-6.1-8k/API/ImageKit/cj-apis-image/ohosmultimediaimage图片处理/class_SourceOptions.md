## class SourceOptions

```cangjie
public class SourceOptions {
    public var sourceDensity: Int32
    public var sourcePixelFormat: PixelMapFormat
    public var sourceSize: Size
    public init(sourceDensity: Int32, sourcePixelFormat!: PixelMapFormat = PixelMapFormat.Unknown, sourceSize!: Size = Size(0, 0))
}
```

**功能：** ImageSource的初始化选项。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var sourceDensity

```cangjie
public var sourceDensity: Int32
```

**功能：** 图片资源像素密度，单位为ppi。

在解码参数[DecodingOptions](#class-decodingoptions)未设置desiredSize的前提下，当前参数SourceOptions.sourceDensity与DecodingOptions.fitDensity非零时将对解码输出的pixelmap进行缩放。

缩放后宽计算公式如下(高同理)：(width * fitDensity + (sourceDensity >> 1)) / sourceDensity。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var sourcePixelFormat

```cangjie
public var sourcePixelFormat: PixelMapFormat
```

**功能：** 图片像素格式。

**类型：** [PixelMapFormat](#enum-pixelmapformat)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var sourceSize

```cangjie
public var sourceSize: Size
```

**功能：** 图像像素大小。

**类型：** [Size](#class-size)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### init(Int32, PixelMapFormat, Size)

```cangjie
public init(sourceDensity: Int32, sourcePixelFormat!: PixelMapFormat = PixelMapFormat.Unknown, sourceSize!: Size = Size(0, 0))
```

**功能：** 创建SourceOptions对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sourceDensity|Int32|是|-|图片资源像素密度，单位为ppi。|
|sourcePixelFormat|[PixelMapFormat](#enum-pixelmapformat)|否|PixelMapFormat.Unknown|**命名参数。** 图片像素格式，默认值为PixelMapFormat.Unknown。|
|sourceSize|[Size](#class-size)|否|Size(0, 0)|**命名参数。** 图像像素大小，默认值为空。|