## class TranslateOption

```cangjie
public class TranslateOption {
    public let x: Float32
    public let y: Float32
    public let z: Float32
    public init(
        x!: Float32 = 0.0,
        y!: Float32 = 0.0,
        z!: Float32 = 0.0
    )
}
```

**功能：** 设置平移参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let x

```cangjie
public let x: Float32
```

**功能：** 表示x轴的平移距离，单位px。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let y

```cangjie
public let y: Float32
```

**功能：** 表示y轴的平移距离，单位px。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let z

```cangjie
public let z: Float32
```

**功能：** 表示z轴的平移距离，单位px。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Float32, Float32, Float32)

```cangjie
public init(
    x!: Float32 = 0.0,
    y!: Float32 = 0.0,
    z!: Float32 = 0.0
)
```

**功能：** TranslateOption构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|否|0.0| **命名参数。** x轴的平移距离，单位px。<br>取值范围 (-∞, +∞)|
|y|Float32|否|0.0| **命名参数。** y轴的平移距离，单位px。<br>取值范围 (-∞, +∞)|
|z|Float32|否|0.0| **命名参数。** z轴的平移距离，单位px。<br>取值范围 (-∞, +∞)|