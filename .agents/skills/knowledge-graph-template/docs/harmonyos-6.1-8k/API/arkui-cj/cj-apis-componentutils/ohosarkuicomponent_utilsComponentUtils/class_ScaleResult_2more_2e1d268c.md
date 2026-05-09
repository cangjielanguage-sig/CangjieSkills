## class ScaleResult

```cangjie
public class ScaleResult {
    public var x: Float64
    public var y: Float64
    public var z: Float64
    public var centerX: Float64
    public var centerY: Float64
    public init(x: Float64, y: Float64, z: Float64, centerX: Float64, centerY: Float64)
}
```

**功能：** 缩放结果。

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

**功能：** x轴缩放因子。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var y

```cangjie
public var y: Float64
```

**功能：** y轴缩放因子。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var z

```cangjie
public var z: Float64
```

**功能：** z轴缩放因子。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(Float64, Float64, Float64, Float64, Float64)

```cangjie
public init(x: Float64, y: Float64, z: Float64, centerX: Float64, centerY: Float64)
```

**功能：** 构建一个ScaleResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|x轴缩放因子。|
|y|Float64|是|-|y轴缩放因子。|
|z|Float64|是|-|z轴缩放因子。|
|centerX|Float64|是|-|中心点的x轴坐标变换。|
|centerY|Float64|是|-|中心点的y轴坐标变换。|

## class Size

```cangjie
public class Size {
    public var width: Float64
    public var height: Float64
    public init(width: Float64, height: Float64)
}
```

**功能：** 定义大小属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var height

```cangjie
public var height: Float64
```

**功能：** 高度属性。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var width

```cangjie
public var width: Float64
```

**功能：** 宽度属性。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(Float64, Float64)

```cangjie
public init(width: Float64, height: Float64)
```

**功能：** 构建一个Size类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Float64|是|-|宽度属性。|
|height|Float64|是|-|高度属性。|