## class TranslateResult

```cangjie
public class TranslateResult {
    public var x: Float64
    public var y: Float64
    public var z: Float64
    public init(x: Float64, y: Float64, z: Float64)
}
```

**功能：** 平移结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var x

```cangjie
public var x: Float64
```

**功能：** x轴平移距离。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var y

```cangjie
public var y: Float64
```

**功能：** y轴平移距离。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var z

```cangjie
public var z: Float64
```

**功能：** z轴平移距离。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(Float64, Float64, Float64)

```cangjie
public init(x: Float64, y: Float64, z: Float64)
```

**功能：** 构建一个TranslateResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|x轴平移距离。<br>单位: vp。|
|y|Float64|是|-|y轴平移距离。<br>单位: vp。|
|z|Float64|是|-|z轴平移距离。<br>单位: vp。|

## type Matrix4Result

```cangjie
public type Matrix4Result = VArray<Float64, $16>
```

**功能：** 4x4变换矩阵结果类型。

**类型：** VArray<Float64, $16>