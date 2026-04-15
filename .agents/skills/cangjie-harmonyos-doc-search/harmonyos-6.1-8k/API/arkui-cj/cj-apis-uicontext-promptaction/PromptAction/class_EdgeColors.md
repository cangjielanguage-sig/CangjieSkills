## class EdgeColors

```cangjie
public class EdgeColors {
    public var top: ResourceColor
    public var right: ResourceColor
    public var bottom: ResourceColor
    public var left: ResourceColor
    public init(
        top!: ResourceColor = Color.Black,
        right!: ResourceColor = Color.Black,
        bottom!: ResourceColor = Color.Black,
        left!: ResourceColor = Color.Black
    )
}
```

**功能：** 提供边框颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var bottom

```cangjie
public var bottom: ResourceColor
```

**功能：** 边框的底部颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var left

```cangjie
public var left: ResourceColor
```

**功能：** 边框的左侧颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var right

```cangjie
public var right: ResourceColor
```

**功能：** 边框的右侧颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var top

```cangjie
public var top: ResourceColor
```

**功能：** 边框的顶部颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(ResourceColor, ResourceColor, ResourceColor, ResourceColor)

```cangjie
public init(
    top!: ResourceColor = Color.Black,
    right!: ResourceColor = Color.Black,
    bottom!: ResourceColor = Color.Black,
    left!: ResourceColor = Color.Black
)
```

**功能：** EdgeColors构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|top|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.Black| **命名参数。** 顶部边框颜色。|
|right|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.Black| **命名参数。** 右侧边框颜色。|
|bottom|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.Black| **命名参数。** 底部边框颜色。|
|left|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.Black| **命名参数。** 左侧边框颜色。|