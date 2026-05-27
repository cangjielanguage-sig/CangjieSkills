## struct SourceOptions

```cangjie
public struct SourceOptions {
    public SourceOptions(
        public var sourceDensity!: Int32 = 0,
        public var sourcePixelFormat!: PixelMapFormat = PixelMapFormat.UNKNOWN,
        public var sourceSize!: Size = Size(height: 0, width: 0)
    )
}
```

**功能：** ImageSource的初始化选项。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### var sourceDensity

```cangjie
public var sourceDensity: Int32 = 0
```

**功能：** 图片资源像素密度，单位DPI。

在解码参数[DecodingOptions](#class-decodingoptions)未设置desiredSize的前提下，当前参数SourceOptions.sourceDensity与DecodingOptions.fitDensity非零时将对解码输出的pixelmap进行缩放。

缩放后宽计算公式如下(高同理)：(width * fitDensity + (sourceDensity >> 1)) / sourceDensity。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### var sourcePixelFormat

```cangjie
public var sourcePixelFormat: PixelMapFormat = PixelMapFormat.UNKNOWN
```

**功能：** 图片像素格式，默认值为UNKNOWN。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** [PixelMapFormat](#enum-pixelmapformat)

**读写能力：** 可读写

**起始版本：** 12

### var sourceSize

```cangjie
public var sourceSize: Size = Size(height: 0, width: 0)
```

**功能：** 图像像素大小，默认值为空。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** [Size](#struct-size)

**读写能力：** 可读写

**起始版本：** 12

### SourceOptions(Int32, PixelMapFormat, Size)

```cangjie
public SourceOptions(
    public var sourceDensity!: Int32 = 0,
    public var sourcePixelFormat!: PixelMapFormat = PixelMapFormat.UNKNOWN,
    public var sourceSize!: Size = Size(height: 0, width: 0)
)
```

**功能：** 创建SourceOptions对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sourceDensity|Int32|否|0| **命名参数。** 图片资源像素密度，单位DPI。<br>在解码参数[DecodingOptions](#class-decodingoptions)未设置desiredSize的前提下，当前参数SourceOptions.sourceDensity与DecodingOptions.fitDensity非零时将对解码输出的pixelmap进行缩放。<br>缩放后宽计算公式如下(高同理)：(width * fitDensity + (sourceDensity >> 1))|
|sourcePixelFormat|[PixelMapFormat](#enum-pixelmapformat)|否|PixelMapFormat.UNKNOWN| **命名参数。** 图片像素格式，默认值为UNKNOWN。|
|sourceSize|[Size](#struct-size)|否|Size(height: 0, width: 0)| **命名参数。** 图像像素大小，默认值为空。|