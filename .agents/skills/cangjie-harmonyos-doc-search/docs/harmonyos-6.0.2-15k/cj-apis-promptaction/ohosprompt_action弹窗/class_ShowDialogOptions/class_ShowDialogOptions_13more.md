## class ShowDialogOptions

```cangjie
public open class ShowDialogOptions {
    public ShowDialogOptions(
        public let title!: String = '',
        public let message!: String = '',
        public let buttons!: Array<ButtonInfo> = [ButtonInfo("button", Color(0x31463146))],
        public let alignment!: DialogAlignment = DialogAlignment.Default,
        public let offset!: Offset = Offset(0.vp, 0.vp),
        public let maskRect!: Rectangle = Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent),
        public let showInSubWindow!: Bool = false,
        public let isModal!: Bool = true,
        public let backgroundColor!: Color = Color.TRANSPARENT,
        public let backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK,
        public let shadowOption!: Option<ShadowOptions> = Option.None,
        public let shadowStyle!: Option<ShadowStyle> = Option.None,
        public let enableHoverMode!: Bool = false,
        public let hoverModeArea!: HoverModeAreaType = HoverModeAreaType.BOTTOM_SCREEN
    )
}
```

**功能：** 对话框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let title

```cangjie
public let title: String = ""
```

**功能：** 表示标题文本。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let message

```cangjie
public let message: String = ""
```

**功能：** 表示内容文本。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let buttons

```cangjie
public let buttons: Array<ButtonInfo> = [ButtonInfo("button", Color(0x31463146))]
```

**功能：** 表示对话框中按钮的数组。

**类型：** Array\<[ButtonInfo](#class-buttoninfo)>

**读写能力：** 只读

**起始版本：** 19

### let alignment

```cangjie
public let alignment: DialogAlignment = DialogAlignment.Default
```

**功能：** 表示弹窗在竖直方向上的对齐方式。

**类型：** [DialogAlignment](./cj-common-types.md#enum-dialogalignment)

**读写能力：** 只读

**起始版本：** 19

### let offset

```cangjie
public let offset: Offset = Offset(0.vp, 0.vp)
```

**功能：** 表示弹窗相对alignment所在位置的偏移量。

**类型：** [Offset](./cj-common-types.md#class-offset)

**读写能力：** 只读

**起始版本：** 19

### let maskRect

```cangjie
public let maskRect: Rectangle = Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent)
```

**功能：** 表示弹窗遮蔽层区域。

**类型：** [Rectangle](./cj-common-types.md#class-rectangle)

**读写能力：** 只读

**起始版本：** 19

### let showInSubWindow

```cangjie
public let showInSubWindow: Bool = false
```

**功能：** 表示弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isModal

```cangjie
public let isModal: Bool = true
```

**功能：** 表示弹窗是否为模态窗口。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let backgroundColor

```cangjie
public let backgroundColor: Color = Color.TRANSPARENT
```

**功能：** 表示弹窗背板颜色。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 只读

**起始版本：** 19

### let backgroundBlurStyle

```cangjie
public let backgroundBlurStyle: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
```

**功能：** 表示弹窗背板模糊材质。

**类型：** [BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)

**读写能力：** 只读

**起始版本：** 19

### let shadowOption

```cangjie
public let shadowOption: Option<ShadowOptions> = Option.None
```

**功能：** 表示弹窗背板阴影。

**类型：** Option\<[ShadowOptions](./cj-text-input-text.md#class-shadowoptions)>

**读写能力：** 只读

**起始版本：** 19

### let shadowStyle

```cangjie
public let shadowStyle: Option<ShadowStyle> = Option.None
```

**功能：** 表示弹窗背板阴影。

**类型：** Option\<[ShadowStyle](#enum-shadowstyle)>

**读写能力：** 只读

**起始版本：** 19