## class HdrStaticMetadata

```cangjie
public class HdrStaticMetadata {
    public HdrStaticMetadata(
        public var displayPrimariesX: Array<Float32>,
        public var displayPrimariesY: Array<Float32>,
        public var whitePointX: Float32,
        public var whitePointY: Float32,
        public var maxLuminance: Float32,
        public var minLuminance: Float32,
        public var maxContentLightLevel: Float32,
        public var maxFrameAverageLightLevel: Float32
    )
}
```

**功能：** 静态元数据值，[HdrMetadataKey](#enum-hdrmetadatakey)中HDR_STATIC_METADATA关键字对应的值。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### var displayPrimariesX

```cangjie
public var displayPrimariesX: Array<Float32>
```

**功能：** 归一化后显示设备三基色的X坐标，数组的长度为3，以0.00002为单位，范围[0.0, 1.0]。

**类型：** Array\<Float32>

**读写能力：** 可读写

**起始版本：** 19

### var displayPrimariesY

```cangjie
public var displayPrimariesY: Array<Float32>
```

**功能：** 归一化后显示设备三基色的Y坐标，数组的长度为3，以0.00002为单位，范围[0.0, 1.0]。

**类型：** Array\<Float32>

**读写能力：** 可读写

**起始版本：** 19

### var maxContentLightLevel

```cangjie
public var maxContentLightLevel: Float32
```

**功能：** 显示内容的最大亮度。以1为单位，最大值为65535。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var maxFrameAverageLightLevel

```cangjie
public var maxFrameAverageLightLevel: Float32
```

**功能：** 显示内容的最大平均亮度，以1为单位，最大值为65535。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var maxLuminance

```cangjie
public var maxLuminance: Float32
```

**功能：** 图像主监视器最大亮度。以1为单位，最大值为65535。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var minLuminance

```cangjie
public var minLuminance: Float32
```

**功能：** 图像主监视器最小亮度。以0.0001为单位，最大值6.55535。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var whitePointX

```cangjie
public var whitePointX: Float32
```

**功能：** 归一化后白点值的X坐标，以0.00002为单位，范围[0.0, 1.0]。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var whitePointY

```cangjie
public var whitePointY: Float32
```

**功能：** 归一化后白点值的Y坐标，以0.00002为单位，范围[0.0, 1.0]。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19