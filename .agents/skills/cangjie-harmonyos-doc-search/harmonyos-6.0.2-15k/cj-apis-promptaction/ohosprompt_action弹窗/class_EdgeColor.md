## class EdgeColor

```cangjie
public class EdgeColor {
    public var top: Color
    public var right: Color
    public var bottom: Color
    public var left: Color
    public init(top!: Color = Color.BLACK, right!: Color = Color.BLACK, bottom!: Color = Color.BLACK, left!: Color = Color.BLACK)
}
```

**功能：** 边框颜色，用于描述组件边框四条边的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var bottom

```cangjie
public var bottom: Color
```

**功能：** 设置组件下边框颜色。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var left

```cangjie
public var left: Color
```

**功能：** 设置组件左边框颜色。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var right

```cangjie
public var right: Color
```

**功能：** 设置组件右边框颜色。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var top

```cangjie
public var top: Color
```

**功能：** 设置组件上边框颜色。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Color, Color, Color, Color)

```cangjie
public init(top!: Color = Color.BLACK, right!: Color = Color.BLACK, bottom!: Color = Color.BLACK, left!: Color = Color.BLACK)
```

**功能：** 构造EdgeColor对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|top|[Color](./cj-common-types.md#class-color)|否|Color.BLACK| **命名参数。** 组件上边框颜色。|
|right|[Color](./cj-common-types.md#class-color)|否|Color.BLACK| **命名参数。** 组件右边框颜色。|
|bottom|[Color](./cj-common-types.md#class-color)|否|Color.BLACK| **命名参数。** 组件下边框颜色。|
|left|[Color](./cj-common-types.md#class-color)|否|Color.BLACK| **命名参数。** 组件左边框颜色。|