## interface LengthProp

```cangjie
public interface LengthProp {
    prop px: Length
    prop vp: Length
    prop fp: Length
    prop percent: Length
    prop lpx: Length
}
```

**功能：** 长度属性标准接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop px

```cangjie
prop px: Length
```

**功能：** 以px为单位的长度属性。

**类型：** [Length](#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop vp

```cangjie
prop vp: Length
```

**功能：** 以vp为单位的长度属性。

**类型：** [Length](#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop fp

```cangjie
prop fp: Length
```

**功能：** 以fp为单位的长度属性。

**类型：** [Length](#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop percent

```cangjie
prop percent: Length
```

**功能：** 以百分比为单位的长度属性。

**类型：** [Length](#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop lpx

```cangjie
prop lpx: Length
```

**功能：** 以lpx为单位的长度属性。

**类型：** [Length](#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### extend Float64 <: LengthProp & Length

```cangjie
extend Float64 <: LengthProp & Length {}
```

**功能：** 扩展Float64为LengthProp和Length的子类。

#### prop px

```cangjie
public prop px: Length
```

**功能：** 以px为单位的长度属性。

**类型：** [Length](#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### prop vp

```cangjie
public prop vp: Length
```

**功能：** 以vp为单位的长度属性。

**类型：** [Length](#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### prop fp

```cangjie
public prop fp: Length
```

**功能：** 以fp为单位的长度属性。

**类型：** [Length](#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### prop percent

```cangjie
public prop percent: Length
```

**功能：** 以百分比为单位的长度属性。

**类型：** [Length](#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### prop lpx

```cangjie
public prop lpx: Length
```

**功能：** 以lpx为单位的长度属性。

**类型：** [Length](#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### prop value

```cangjie
public prop value: Float64
```

**功能：** 长度属性的值。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### prop unitType

```cangjie
public prop unitType: LengthUnit
```

**功能：** 长度属性的单位。

**类型：** [LengthUnit](#enum-lengthunit)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22