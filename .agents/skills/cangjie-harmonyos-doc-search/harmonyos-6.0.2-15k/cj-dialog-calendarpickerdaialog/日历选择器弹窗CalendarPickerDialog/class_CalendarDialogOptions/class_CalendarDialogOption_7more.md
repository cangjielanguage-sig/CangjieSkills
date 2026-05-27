## class CalendarDialogOptions

```cangjie
public class CalendarDialogOptions <: CalendarOptions {
    public let onAccept:?(DateTime) -> Unit
    public let onCancel:?() -> Unit
    public let onChange:?(DateTime) -> Unit
    public let backgroundColor: ResourceColor
    public let backgroundBlurStyle: BlurStyle
    public let acceptButtonStyle:?PickerDialogButtonStyle
    public let cancelButtonStyle:?PickerDialogButtonStyle
    public let onDidAppear:?() -> Unit
    public let onDidDisappear:?() -> Unit
    public let onWillAppear:?() -> Unit
    public let onWillDisappear:?() -> Unit
    public let shadow:?ShadowOptions
    public init(
        hintRadius!: Length = 16,
        selected!: DateTime = DateTime.now(),
        onAccept!: ?(DateTime) -> Unit = None,
        onCancel!: ?() -> Unit = None,
        onChange!: ?(DateTime) -> Unit = None,
        backgroundColor!: ResourceColor = Color.TRANSPARENT,
        backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK,
        acceptButtonStyle!: ?PickerDialogButtonStyle = None,
        cancelButtonStyle!: ?PickerDialogButtonStyle = None,
        onDidAppear!: ?() -> Unit = None,
        onDidDisappear!: ?() -> Unit = None,
        onWillAppear!: ?() -> Unit = None,
        onWillDisappear!: ?() -> Unit = None,
        shadow!: ?ShadowOptions = None
    )
}
```

**功能：** 继承自[CalendarOptions](./cj-button-picker-calendarpicker.md#class-calendaroptions)。配置日历选择器弹窗的相关参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [CalendarOptions](./cj-button-picker-calendarpicker.md#class-calendaroptions)

### let acceptButtonStyle

```cangjie
public let acceptButtonStyle:?PickerDialogButtonStyle
```

**功能：** 设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。

**类型：** ?[PickerDialogButtonStyle](./cj-dialog-calendarpickerdaialog.md#class-pickerdialogbuttonstyle)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let backgroundBlurStyle

```cangjie
public let backgroundBlurStyle: BlurStyle
```

**功能：** 弹窗背板模糊材质。

**类型：** [BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let backgroundColor

```cangjie
public let backgroundColor: ResourceColor
```

**功能：** 弹窗背板颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let cancelButtonStyle

```cangjie
public let cancelButtonStyle:?PickerDialogButtonStyle
```

**功能：** 设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。

**类型：** ?[PickerDialogButtonStyle](./cj-dialog-calendarpickerdaialog.md#class-pickerdialogbuttonstyle)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let onAccept

```cangjie
public let onAccept:?(DateTime) -> Unit
```

**功能：** 点击弹窗中的“确定”按钮时触发该回调。DateTime表示选中的日期值。

**类型：** ?(DateTime)->Unit

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let onCancel

```cangjie
public let onCancel:?() -> Unit
```

**功能：** 点击弹窗中的“取消”按钮时触发该回调。

**类型：** ?()->Unit

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19