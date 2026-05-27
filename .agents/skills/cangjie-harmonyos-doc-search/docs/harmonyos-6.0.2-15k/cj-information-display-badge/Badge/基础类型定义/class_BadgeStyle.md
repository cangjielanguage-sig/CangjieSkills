### class BadgeStyle

```cangjie
public class BadgeStyle {
    public var color: UInt32
    public var fontSize: Int64
    public var badgeSize: Int64
    public var badgeColor: UInt32
    public var fontWeight: UInt32
    public var borderColor: UInt32
    public var borderWidth: Float64
    public var borderWidthUnit: Int32
    public init(color!: ResourceColor = Color.WHITE, fontSize!: Int64 = 10, badgeSize!: Int64 = 16,
        badgeColor!: ResourceColor = Color.RED, fontWeight!: FontWeight = FontWeight.Normal, borderColor!: ResourceColor = Color.RED,
        borderWidth!: Length = 1.vp)
}
```

**功能：** 包含Badge组件的样式参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var badgeColor

```cangjie
public var badgeColor: UInt32
```

**功能：** badge的颜色。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var badgeSize

```cangjie
public var badgeSize: Int64
```

**功能：** badge的大小，单位为vp。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var borderColor

```cangjie
public var borderColor: UInt32
```

**功能：** 底板描边颜色。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var borderWidth

```cangjie
public var borderWidth: Float64
```

**功能：** 底板描边粗细。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var borderWidthUnit

```cangjie
public var borderWidthUnit: Int32
```

**功能：** 底板描边粗细的单位。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var color

```cangjie
public var color: UInt32
```

**功能：** 文本颜色。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var fontSize

```cangjie
public var fontSize: Int64
```

**功能：** 文本大小，单位为fp。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var fontWeight

```cangjie
public var fontWeight: UInt32
```

**功能：** 设置文本的字体粗细。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(ResourceColor, Int64, Int64, ResourceColor, FontWeight, ResourceColor, Length)

```cangjie
public init(color!: ResourceColor = Color.WHITE, fontSize!: Int64 = 10, badgeSize!: Int64 = 16,
    badgeColor!: ResourceColor = Color.RED, fontWeight!: FontWeight = FontWeight.Normal, borderColor!: ResourceColor = Color.RED,
    borderWidth!: Length = 1.vp)
```

**功能：** 创建一个BadgeStyle对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.WHITE| **命名参数。** 文本颜色。|
|fontSize|Int64|否|10| **命名参数。** 文本大小。<br>单位：fp。|
|badgeSize|Int64|否|16| **命名参数。** badge的大小。<br>单位：fp。|
|badgeColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.RED| **命名参数。** badge的颜色。|
|fontWeight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 设置文本的字体粗细。|
|borderColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.RED| **命名参数。** 底板描边颜色。|
|borderWidth|[Length](./cj-common-types.md#interface-length)|否|1.vp| **命名参数。** 底板描边粗细。<br>单位：vp。|