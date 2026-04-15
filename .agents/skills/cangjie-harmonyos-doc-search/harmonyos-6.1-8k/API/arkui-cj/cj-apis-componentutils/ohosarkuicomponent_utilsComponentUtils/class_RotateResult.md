## class RotateResult

```cangjie
public class RotateResult {
    public var x: Float64
    public var y: Float64
    public var z: Float64
    public var centerX: Float64
    public var centerY: Float64
    public var angle: Float64
    public init(x: Float64, y: Float64, z: Float64, centerX: Float64, centerY: Float64, angle: Float64)
}
```

**功能：** 旋转结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var angle

```cangjie
public var angle: Float64
```

**功能：** 旋转角度。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var centerX

```cangjie
public var centerX: Float64
```

**功能：** 中心点的x轴坐标变换。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var centerY

```cangjie
public var centerY: Float64
```

**功能：** 中心点的y轴坐标变换。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var x

```cangjie
public var x: Float64
```

**功能：** 旋转轴向量x坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var y

```cangjie
public var y: Float64
```

**功能：** 旋转轴向量y坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var z

```cangjie
public var z: Float64
```

**功能：** 旋转轴向量z坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(Float64, Float64, Float64, Float64, Float64, Float64)

```cangjie
public init(x: Float64, y: Float64, z: Float64, centerX: Float64, centerY: Float64, angle: Float64)
```

**功能：** 构建一个RotateResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|旋转轴向量x坐标。|
|y|Float64|是|-|旋转轴向量y坐标。|
|z|Float64|是|-|旋转轴向量z坐标。|
|centerX|Float64|是|-|中心点的x轴坐标变换。|
|centerY|Float64|是|-|中心点的y轴坐标变换。|
|angle|Float64|是|-|旋转角度。|