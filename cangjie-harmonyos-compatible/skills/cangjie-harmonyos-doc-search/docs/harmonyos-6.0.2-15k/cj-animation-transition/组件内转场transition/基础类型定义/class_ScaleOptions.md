### class ScaleOptions

```cangjie
public class ScaleOptions {
    public var x: Float32
    public var y: Float32
    public var z: Float32
    public var centerX: Length
    public var centerY: Length
    public init(
        x!: Float32 = 0.0,
        y!: Float32 = 0.0,
        z!: Float32 = 0.0,
        centerX!: Length = 50.percent,
        centerY!: Length = 50.percent
    )
}
```

**功能：** 设置缩放参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var x

```cangjie
public var x: Float32
```

**功能：** 表示x轴的缩放倍数。x>1时以x轴方向放大，0\<x\<1时以x轴方向缩小，x\<0时沿x轴反向并缩放。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var y

```cangjie
public var y: Float32
```

**功能：** 表示y轴的缩放倍数。y>1时以y轴方向放大，0\<y\<1时以y轴方向缩小，y\<0时沿y轴反向并缩放。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var z

```cangjie
public var z: Float32
```

**功能：** 表示z轴的缩放倍数。z>1时以z轴方向放大，0\<z\<1时以z轴方向缩小，z\<0时沿z轴反向并缩放。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var centerX

```cangjie
public var centerX: Length
```

**功能：** 表示变换中心点x轴坐标。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var centerY

```cangjie
public var centerY: Length
```

**功能：** 表示变换中心点y轴坐标。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Float32, Float32, Float32, Length, Length)

```cangjie
public init(
    x!: Float32 = 0.0,
    y!: Float32 = 0.0,
    z!: Float32 = 0.0,
    centerX!: Length = 50.percent,
    centerY!: Length = 50.percent
)
```

**功能：** ScaleOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|否|0.0| **命名参数。** x轴的缩放倍数。x>1时以x轴方向放大，0<x<1时以x轴方向缩小，x<0时沿x轴反向并缩放。|
|y|Float32|否|0.0| **命名参数。** y轴的缩放倍数。y>1时以y轴方向放大，0<y<1时以y轴方向缩小，y<0时沿y轴反向并缩放。|
|z|Float32|否|0.0| **命名参数。** z轴的缩放倍数。z>1时以z轴方向放大，0<z<1时以z轴方向缩小，z<0时沿z轴反向并缩放。|
|centerX|[Length](./cj-common-types.md#interface-length)|否|50.percent| **命名参数。** 变换中心点x轴坐标。表示组件变换中心点（即锚点）的x方向坐标。|
|centerY|[Length](./cj-common-types.md#interface-length)|否|50.percent| **命名参数。** 变换中心点y轴坐标。表示组件变换中心点（即锚点）的y方向坐标。|