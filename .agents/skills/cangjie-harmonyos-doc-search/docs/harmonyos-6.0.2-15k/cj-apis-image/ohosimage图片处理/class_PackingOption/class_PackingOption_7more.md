## class PackingOption

```cangjie
public class PackingOption {
    public var format: String
    public var quality: UInt8
    public var bufferSize: UInt64
    public var desiredDynamicRange: PackingDynamicRange
    public var needsPackProperties: Bool
    public init(format: String, quality: UInt8, bufferSize!: UInt64 = 25 * 1024 * 1024)
    public init(format: String, quality: UInt8, desiredDynamicRange: PackingDynamicRange, needsPackProperties: Bool,
        bufferSize!: UInt64 = 25 * 1024 * 1024)
}
```

**功能：** 表示图片打包选项。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 12

### var bufferSize

```cangjie
public var bufferSize: UInt64 = 25 * 1024 * 1024
```

**功能：** 接收编码数据的缓冲区大小，单位为Byte。如果不设置大小，默认为25M。如果编码图片超过25M，需要指定大小。bufferSize需大于编码后图片大小。使用[packToFile](#func-packtofileimagesource-intnative-packingoption)不受此参数限制。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**类型：** UInt64

**读写能力：** 可读写

**起始版本：** 12

### var desiredDynamicRange

```cangjie
public var desiredDynamicRange: PackingDynamicRange = SDR
```

**功能：** 目标动态范围。默认值为SDR。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**类型：** [PackingDynamicRange](#enum-packingdynamicrange)

**读写能力：** 可读写

**起始版本：** 19

### var format

```cangjie
public var format: String
```

**功能：** 目标格式。</br>当前只支持"image/jpeg"、"image/webp"、"image/png"和"image/heif"（不同硬件设备支持情况不同）。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var needsPackProperties

```cangjie
public var needsPackProperties: Bool = false
```

**功能：** 是否需要编码图片属性信息，例如EXIF。默认值为false。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var quality

```cangjie
public var quality: UInt8
```

**功能：** JPEG编码中设定输出图片质量的参数，取值范围为0-100。0质量最低，100质量最高，质量越高生成图片所占空间越大。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**类型：** UInt8

**读写能力：** 可读写

**起始版本：** 12

### init(String, UInt8, UInt64)

```cangjie
public init(format: String, quality: UInt8, bufferSize!: UInt64 = 25 * 1024 * 1024)
```

**功能：** 创建PackingOption对象。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|format|String|是|-|目标格式。</br>当前只支持"image/jpeg"、"image/webp"、"image/png"和"image/heif"（不同硬件设备支持情况不同）。 |
|quality|UInt8|是|-|JPEG编码中设定输出图片质量的参数，取值范围为0-100。0质量最低，100质量最高，质量越高生成图片所占空间越大。|
|bufferSize|UInt64|否|25 * 1024 * 1024| **命名参数。** 接收编码数据的缓冲区大小，单位为Byte。如果不设置大小，默认为25M。如果编码图片超过25M，需要指定大小。bufferSize需大于编码后图片大小。使用[packToFile](#func-packtofileimagesource-intnative-packingoption)不受此参数限制。|