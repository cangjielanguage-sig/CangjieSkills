## class AlertDialogButtonBaseOptions

```cangjie
public open class AlertDialogButtonBaseOptions {
    public var enabled: ?Bool
    public var defaultFocus: ?Bool
    public var style: ?DialogButtonStyle
    public var value: ?ResourceStr
    public var fontColor: ?ResourceColor
    public var backgroundColor: ?ResourceColor
    public var action: ?VoidCallback
    public init(
        enabled!: ?Bool = None,
        defaultFocus!: ?Bool = None,
        style!: ?DialogButtonStyle = None,
        value!: ?ResourceStr,
        fontColor!: ?ResourceColor = None,
        backgroundColor!: ?ResourceColor = None,
        action!: ?VoidCallback
    )
}
```

**功能：** 定义警告弹窗中的按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var action

```cangjie
public var action: ?VoidCallback
```

**功能：** Button选中时的回调。

**类型：** ?[VoidCallback](./cj-common-types.md#type-voidcallback)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var backgroundColor

```cangjie
public var backgroundColor: ?ResourceColor
```

**功能：** Button背景颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var defaultFocus

```cangjie
public var defaultFocus: ?Bool
```

**功能：** 设置Button是否是默认焦点。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var enabled

```cangjie
public var enabled: ?Bool
```

**功能：** 点击Button是否响应。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var fontColor

```cangjie
public var fontColor: ?ResourceColor
```

**功能：** Button的文本颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var style

```cangjie
public var style: ?DialogButtonStyle
```

**功能：** 设置Button的风格样式。

**类型：** ?[DialogButtonStyle](./cj-common-types.md#enum-dialogbuttonstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var value

```cangjie
public var value: ?ResourceStr
```

**功能：** Button的文本内容。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22