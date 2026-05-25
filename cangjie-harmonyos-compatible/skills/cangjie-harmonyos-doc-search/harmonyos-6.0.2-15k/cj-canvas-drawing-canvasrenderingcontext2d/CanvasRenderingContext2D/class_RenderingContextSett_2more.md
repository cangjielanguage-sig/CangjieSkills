## class RenderingContextSettings

```cangjie
public class RenderingContextSettings {
    public var antialias: Bool
    public init(antialias!: Bool = false)
}
```

**功能：** 用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var antialias

```cangjie
public var antialias: Bool
```

**功能：** 表明canvas是否开启抗锯齿。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(Bool)

```cangjie
public init(antialias!: Bool = false)
```

**功能：** 用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|antialias|Bool|否|false| **命名参数。** 表明canvas是否开启抗锯齿。初始值：false|

## struct TextMetrics

```cangjie
public struct TextMetrics {
    public var width: Float64 = 0.0
    public var height: Float64 = 0.0
}
```

**功能：** 该对象可以获取指定文本的宽度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var height

```cangjie
public var height: Float64 = 0.0
```

**功能：** 文本方块的高度。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var width

```cangjie
public var width: Float64 = 0.0
```

**功能：** 文本方块的宽度。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12