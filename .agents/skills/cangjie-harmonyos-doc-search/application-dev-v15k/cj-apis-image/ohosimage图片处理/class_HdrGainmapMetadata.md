## class HdrGainmapMetadata

```cangjie
public class HdrGainmapMetadata {
    public HdrGainmapMetadata(
        public var writerVersion: UInt16,
        public var miniVersion: UInt16,
        public var gainmapChannelCount: UInt8,
        public var useBaseColorFlag: Bool,
        public var baseHeadroom: Float32,
        public var alternateHeadroom: Float32,
        public var channels: Array<GainmapChannel>
    )
}
```

**功能：** Gainmap使用的元数据值，[HdrMetadataKey](#enum-hdrmetadatakey)中HDR_GAINMAP_METADATA关键字对应的值，参考ISO 21496-1。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### var alternateHeadroom

```cangjie
public var alternateHeadroom: Float32
```

**功能：** 提取的可选择图像提亮比，参考ISO 21496-1。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var baseHeadroom

```cangjie
public var baseHeadroom: Float32
```

**功能：** 基础图提亮比，参考ISO 21496-1。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var channels

```cangjie
public var channels: Array<GainmapChannel>
```

**功能：** 各通道的数据，长度为3，参考ISO 21496-1。

**类型：** Array\<[GainmapChannel](#class-gainmapchannel)>

**读写能力：** 可读写

**起始版本：** 19

### var gainmapChannelCount

```cangjie
public var gainmapChannelCount: UInt8
```

**功能：** Gainmap的颜色通道数，值为3时RGB通道的元数据值不同，值为1时各通道元数据值相同，参考ISO 21496-1。

**类型：** UInt8

**读写能力：** 可读写

**起始版本：** 19

### var miniVersion

```cangjie
public var miniVersion: UInt16
```

**功能：** 元数据解析需要理解的最小版本。

**类型：** UInt16

**读写能力：** 可读写

**起始版本：** 19

### var useBaseColorFlag

```cangjie
public var useBaseColorFlag: Bool
```

**功能：** 是否使用基础图的色彩空间，参考ISO 21496-1。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var writerVersion

```cangjie
public var writerVersion: UInt16
```

**功能：** 元数据编写器使用的版本。

**类型：** UInt16

**读写能力：** 可读写

**起始版本：** 19

### HdrGainmapMetadata(UInt16, UInt16, UInt8, Bool, Float32, Float32, Array\<GainmapChannel>)

```cangjie
public HdrGainmapMetadata(
    public var writerVersion: UInt16,
    public var miniVersion: UInt16,
    public var gainmapChannelCount: UInt8,
    public var useBaseColorFlag: Bool,
    public var baseHeadroom: Float32,
    public var alternateHeadroom: Float32,
    public var channels: Array<GainmapChannel>
)
```

**功能：** 创建HdrGainmapMetadata对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|writerVersion|UInt16|是|-|元数据编写器使用的版本。|
|miniVersion|UInt16|是|-|元数据解析需要理解的最小版本。|
|gainmapChannelCount|UInt8|是|-|Gainmap的颜色通道数，值为3时RGB通道的元数据值不同，值为1时各通道元数据值相同，参考ISO 21496-1。|
|useBaseColorFlag|Bool|是|-|是否使用基础图的色彩空间，参考ISO 21496-1。|
|baseHeadroom|Float32|是|-|基础图提亮比，参考ISO 21496-1。|
|alternateHeadroom|Float32|是|-|提取的可选择图像提亮比，参考ISO 21496-1。|
|channels|Array\<[GainmapChannel](#class-gainmapchannel)>|是|-|各通道的数据，长度为3，参考ISO 21496-1。|