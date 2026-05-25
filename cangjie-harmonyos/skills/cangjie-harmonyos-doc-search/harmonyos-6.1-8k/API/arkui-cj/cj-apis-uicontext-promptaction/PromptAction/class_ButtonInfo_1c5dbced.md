## class ButtonInfo

```cangjie
public class ButtonInfo {
    public var text: ResourceStr
    public var color: ResourceColor
    public var primary: Bool
    public init(text!: ResourceStr, color!: ResourceColor, primary!: Bool = false)
}
```

**功能：** 提供菜单项按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var color

```cangjie
public var color: ResourceColor
```

**功能：** 按钮文本颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var primary

```cangjie
public var primary: Bool
```

**功能：** 定义按钮是否默认响应Enter/Space键。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var text

```cangjie
public var text: ResourceStr
```

**功能：** 按钮中显示的文本。

**类型：** [ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(ResourceStr, ResourceColor, Bool)

```cangjie
public init(text!: ResourceStr, color!: ResourceColor, primary!: Bool = false)
```

**功能：** 构造菜单中的菜单项按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-| **命名参数。** 按钮文本内容。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-| **命名参数。** 按钮文本颜色。|
|primary|Bool|否|false| **命名参数。** 按钮是否默认响应Enter/Space键。|