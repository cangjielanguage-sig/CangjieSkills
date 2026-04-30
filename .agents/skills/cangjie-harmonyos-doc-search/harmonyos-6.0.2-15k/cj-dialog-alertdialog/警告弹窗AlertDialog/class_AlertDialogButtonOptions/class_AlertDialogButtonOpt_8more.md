## class AlertDialogButtonOptions

```cangjie
public class AlertDialogButtonOptions {
    public var enabled!: Bool = true,
    public var defaultFocus!: Bool = false,
    public var style!: Option<DialogButtonStyle> = Option.None,
    public var value!: String = "",
    public var fontColor!: Option<Color> = Option.None,
    public var backgroundColor!: Option<Color> = Option.None,
    public var action!: () -> Unit = { => },
    public var primary!: Bool = false

    public init(
        enabled!: Bool = true,
        defaultFocus!: Bool = false,
        style!: Option<DialogButtonStyle> = None,
        value!: String = "",
        fontColor!: Option<Color> = None,
        backgroundColor!: Option<Color> = None,
        action!: () -> Unit = {=>}
    )
    public init(
        enabled!: Bool = true,
        defaultFocus!: Bool = false,
        style!: Option<DialogButtonStyle> = None,
        value!: String = "",
        fontColor!: Option<Color> = None,
        backgroundColor!: Option<Color> = None,
        action!: () -> Unit = {=>},
        primary!: Bool
    )
}
```

**功能：** 定义警告弹窗中的按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var action

```cangjie
public var action: () -> Unit = {=>}
```

**功能：** Button选中时的回调。

**类型：** ()->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var backgroundColor

```cangjie
public var backgroundColor: Option<Color> = Option.None
```

**功能：** Button背景颜色。

**类型：** Option\<[Color](./cj-common-types.md#class-color)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var defaultFocus

```cangjie
public var defaultFocus: Bool = false
```

**功能：** 设置Button是否是默认焦点。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var enabled

```cangjie
public var enabled: Bool = true
```

**功能：** 点击Button是否响应。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var fontColor

```cangjie
public var fontColor: Option<Color> = Option.None
```

**功能：** Button的文本颜色。

**类型：** Option\<[Color](./cj-common-types.md#class-color)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var primary

```cangjie
public var primary: Bool = false
```

**功能：** 在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。在defaultFocus为true时不生效。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var style

```cangjie
public var style: Option<DialogButtonStyle> = Option.None
```

**功能：** 设置Button的风格样式。

**类型：** Option\<[DialogButtonStyle](./cj-common-types.md#enum-dialogbuttonstyle)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12