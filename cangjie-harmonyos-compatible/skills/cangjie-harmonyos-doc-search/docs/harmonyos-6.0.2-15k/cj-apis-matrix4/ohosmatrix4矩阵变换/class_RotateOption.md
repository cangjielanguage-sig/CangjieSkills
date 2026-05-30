## class RotateOption

```cangjie
public class RotateOption {
    public let x: Float32
    public let y: Float32
    public let z: Float32
    public let angle: Float32
    public let centerX: Float32
    public let centerY: Float32
    public init(
        x!: Float32 = 0.0,
        y!: Float32 = 0.0,
        z!: Float32 = 0.0,
        angle!: Float32 = 0.0,
        centerX!: Float32 = 0.0,
        centerY!: Float32 = 0.0
    )
}
```

**功能：** 设置旋转参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let x

```cangjie
public let x: Float32
```

**功能：** 表示旋转轴向量x坐标。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let y

```cangjie
public let y: Float32
```

**功能：** 表示旋转轴向量y坐标。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let z

```cangjie
public let z: Float32
```

**功能：** 表示旋转轴向量z坐标。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let angle

```cangjie
public let angle: Float32
```

**功能：** 表示旋转角度。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let centerX

```cangjie
public let centerX: Float32
```

**功能：** 单次矩阵变换中心点相对于组件变换中心点（锚点）的额外x轴偏移值。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let centerY

```cangjie
public let centerY: Float32
```

**功能：** 单次矩阵变换中心点相对于组件变换中心点（锚点）的额外y轴偏移值。

**类型：** Float32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Float32, Float32, Float32, Float32, Float32, Float32)

```cangjie
public init(
    x!: Float32 = 0.0,
    y!: Float32 = 0.0,
    z!: Float32 = 0.0,
    angle!: Float32 = 0.0,
    centerX!: Float32 = 0.0,
    centerY!: Float32 = 0.0
)
```

**功能：** RotateOption构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|否|0.0| **命名参数。** 旋转轴向量x坐标。<br>取值范围 (-∞, +∞)|
|y|Float32|否|0.0| **命名参数。** 旋转轴向量y坐标。<br>取值范围 (-∞, +∞)|
|z|Float32|否|0.0| **命名参数。** 旋转轴向量z坐标。<br>取值范围 (-∞, +∞)|
|angle|Float32|否|0.0| **命名参数。** 旋转角度。|
|centerX|Float32|否|0.0| **命名参数。** 单次矩阵变换中心点相对于组件变换中心点（锚点）的额外x轴偏移值。<br>单位：vp<br>**说明：**<br>为0时表示x方向的矩阵变换中心恰好为组件x方向锚点，取值表示相对组件x方向锚点的额外偏移量。具体实现可参考[示例3（按中心点旋转）](#示例3旋转效果)。|
|centerY|Float32|否|0.0| **命名参数。** 单次矩阵变换中心点相对于组件变换中心点（锚点）的额外y轴偏移值。<br>单位：vp<br>**说明：**<br>为0时表示y方向的矩阵变换中心恰好为组件y方向锚点，取值表示相对组件y方向锚点的额外偏移量。具体实现可参考[示例3（按中心点旋转）](#示例3旋转效果)。|