## class GainmapChannel

```cangjie
public class GainmapChannel {
    public GainmapChannel(
        public var gainmapMax: Float32,
        public var gainmapMin: Float32,
        public var gamma: Float32,
        public var baseOffset: Float32,
        public var alternateOffset: Float32
    )
}
```

**功能：** Gainmap图单个通道的数据内容，参考ISO 21496-1。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### var alternateOffset

```cangjie
public var alternateOffset: Float32
```

**功能：** 提取的可选择图像偏移量，参考ISO 21496-1。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var baseOffset

```cangjie
public var baseOffset: Float32
```

**功能：** 基础图的偏移，参考ISO 21496-1。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var gainmapMax

```cangjie
public var gainmapMax: Float32
```

**功能：** 增强图像的最大值，参考ISO 21496-1。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var gainmapMin

```cangjie
public var gainmapMin: Float32
```

**功能：** 增强图像的最小值，参考ISO 21496-1。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var gamma

```cangjie
public var gamma: Float32
```

**功能：** gamma值，参考ISO 21496-1。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### GainmapChannel(Float32, Float32, Float32, Float32, Float32)

```cangjie
public GainmapChannel(
    public var gainmapMax: Float32,
    public var gainmapMin: Float32,
    public var gamma: Float32,
    public var baseOffset: Float32,
    public var alternateOffset: Float32
)
```

**功能：** 创建GainmapChannel对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|gainmapMax|Float32|是|-|增强图像的最大值，参考ISO 21496-1。|
|gainmapMin|Float32|是|-|增强图像的最小值，参考ISO 21496-1。|
|gamma|Float32|是|-|gamma值，参考ISO 21496-1。|
|baseOffset|Float32|是|-|基础图的偏移，参考ISO 21496-1。|
|alternateOffset|Float32|是|-|提取的可选择图像偏移量，参考ISO 21496-1。|