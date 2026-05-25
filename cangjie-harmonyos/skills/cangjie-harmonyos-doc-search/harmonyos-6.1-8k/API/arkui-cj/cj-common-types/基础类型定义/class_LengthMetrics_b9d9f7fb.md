## class LengthMetrics

```cangjie
public class LengthMetrics <: Length {
    public init(value: Float64, unit!: LengthUnit = LengthUnit.Vp)
}
```

**功能：** 表示长度属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [Length](#interface-length)

### init(Float64, LengthUnit)

```cangjie
public init(value: Float64, unit!: LengthUnit = LengthUnit.Vp)
```

**功能：** 长度属性构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|长度值。|
|unit|[LengthUnit](#enum-lengthunit)|否|LengthUnit.Vp|**命名参数。** 长度单位。|

### prop value

```cangjie
public prop value: Float64
```

**功能：** 长度属性的值。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop unitType

```cangjie
public prop unitType: LengthUnit
```

**功能：** 长度属性的单位。

**类型：** [LengthUnit](#enum-lengthunit)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22