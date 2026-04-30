## class ScaleOption

```cangjie
public class ScaleOption {
    public let x: Float32
    public let y: Float32
    public let z: Float32
    public let centerX: Float32
    public let centerY: Float32
    public init(
        x!: Float32 = 1.0,
        y!: Float32 = 1.0,
        z!: Float32 = 1.0,
        centerX!: Float32 = 0.0,
        centerY!: Float32 = 0.0
    )
}
```

**功能：** 设置缩放参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let x

```cangjie
public let x: Float32
```

**功能：** 表示x轴的缩放倍数。x>1时以x轴方向放大，0\<x\<1时以x轴方向缩小，x\<0时沿x轴反向并缩放。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let y

```cangjie
public let y: Float32
```

**功能：** 表示y轴的缩放倍数。y>1时以y轴方向放大，0<y<1 时以y轴方向缩小，y<0 时沿y轴反向并缩放。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let z

```cangjie
public let z: Float32
```

**功能：** 表示z轴的缩放倍数。z>1时以z轴方向放大，0\<z\<1时以z轴方向缩小，z\<0时沿z轴反向并缩放。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let centerX

```cangjie
public let centerX: Float32
```

**功能：** 表示变换中心点x轴坐标。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let centerY

```cangjie
public let centerY: Float32
```

**功能：** 表示变换中心点y轴坐标。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Float32, Float32, Float32, Float32, Float32)

```cangjie
public init(
    x!: Float32 = 1.0,
    y!: Float32 = 1.0,
    z!: Float32 = 1.0,
    centerX!: Float32 = 0.0,
    centerY!: Float32 = 0.0
)
```

**功能：** ScaleOption构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|否|1.0| **命名参数。** x轴的缩放倍数。x>1时以x轴方向放大，0\<x\<1时以x轴方向缩小，x\<0时沿x轴反向并缩放。<br>取值范围 (-∞, +∞)|
|y|Float32|否|1.0| **命名参数。** y轴的缩放倍数。y>1时以y轴方向放大，0\<y\<1时以y轴方向缩小，y\<0时沿y轴反向并缩放。<br>取值范围 (-∞, +∞)|
|z|Float32|否|1.0| **命名参数。** z轴的缩放倍数。z>1时以z轴方向放大，0\<z\<1时以z轴方向缩小，z\<0时沿z轴反向并缩放。<br>取值范围 (-∞, +∞)|
|centerX|Float32|否|0.0| **命名参数。** 变换中心点x轴坐标。<br>单位：px<br>取值范围 (-∞, +∞)|
|centerY|Float32|否|0.0| **命名参数。** 变换中心点y轴坐标。<br>单位：px<br>取值范围 (-∞, +∞)|