## class PackingOption

```cangjie
public class PackingOption {
    public var format: String
    public var quality: UInt8
    public var bufferSize: UInt64
    public var desiredDynamicRange: PackingDynamicRange
    public var needsPackProperties: Bool
    public init(format: String, quality: UInt8, bufferSize!: UInt64 = 0,
        desiredDynamicRange!: PackingDynamicRange = Sdr, needsPackProperties!: Bool = false)
}
```

**功能：** 表示图片打包选项。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

### var bufferSize

```cangjie
public var bufferSize: UInt64
```

**功能：** 接收编码数据的缓冲区大小，单位为Byte。如果不设置大小，默认为25M。如果编码图片超过25M，需要指定大小。bufferSize需大于编码后图片大小。使用[packToFile](#func-packtofileimagesource-int32-packingoption)不受此参数限制。

**类型：** UInt64

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

### var desiredDynamicRange

```cangjie
public var desiredDynamicRange: PackingDynamicRange
```

**功能：** 目标动态范围。

**类型：** [PackingDynamicRange](#enum-packingdynamicrange)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

### var format

```cangjie
public var format: String
```

**功能：** 目标格式。

当前只支持"image/jpeg"、"image/webp"、"image/png"和"image/heic(或者image/heif)"、"image/sdr_astc_4x4"、"image/sdr_sut_superfast_4x4"（不同硬件设备支持情况不同）、"image/hdr_astc_4x4"。

> **说明：**
>
> 因为jpeg不支持透明通道，若使用带透明通道的数据编码jpeg格式，透明色将变为黑色。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

### var needsPackProperties

```cangjie
public var needsPackProperties: Bool
```

**功能：** 是否需要编码图片属性信息，例如EXIF。true表示需要，false表示不需要。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

### var quality

```cangjie
public var quality: UInt8
```

**功能：** 编码中设定输出图片质量的参数，该参数仅对JPEG图片和HEIF图片生效。取值范围：[0, 100]。0质量最低，100质量最高，质量越高生成图片所占空间越大。WebP、PNG等图片均为无损编码。

1. sdr_astc_4x4编码中，可以设定输出图片质量的参数，可选参数：92、85。

2. sut编码中，设定输出图片质量可选参数：92。

3. hdr_astc_4x4编码中，可以设定输出图片质量的参数，可选参数：85。

**类型：** UInt8

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22