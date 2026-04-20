## class Point

```cangjie
public class Point {
    public let x: Float64
    public let y: Float64
    public init(
        x: Float64,
        y: Float64
    )
}
```

**功能：** 设置点坐标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let x

```cangjie
public let x: Float64
```

**功能：** 表示x轴坐标。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let y

```cangjie
public let y: Float64
```

**功能：** 表示y轴坐标。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Float64, Float64)

```cangjie
public init(
    x: Float64,
    y: Float64
)
```

**功能：** Point构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|x轴坐标。<br>取值范围 (-∞, +∞)|
|y|Float64|是|-|y轴坐标。<br>取值范围 (-∞, +∞)|