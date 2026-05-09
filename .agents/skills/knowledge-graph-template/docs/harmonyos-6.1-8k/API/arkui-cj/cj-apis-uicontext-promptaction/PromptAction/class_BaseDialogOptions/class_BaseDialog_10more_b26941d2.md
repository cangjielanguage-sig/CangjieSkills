## class BaseDialogOptions

```cangjie
public open class BaseDialogOptions {
    public var maskRect: Rectangle
    public var alignment: DialogAlignment
    public var offset: Offset
    public var isModal: Bool
    public var showInSubWindow: Bool
    public var autoCancel: Bool
    public var maskColor: ResourceColor
    public var transition: TransitionEffect
    public var onDidAppear: () -> Unit
    public var onDidDisappear: () -> Unit
    public var onWillAppear: () -> Unit
    public var onWillDisappear: () -> Unit
    public var keyboardAvoidMode: KeyboardAvoidMode
    public var enableHoverMode: Bool
    public var hoverModeArea: HoverModeAreaType
    public init(
        maskRect!: Rectangle = Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent),
        alignment!: DialogAlignment = DialogAlignment.Default,
        offset!: Offset = Offset(0.vp, 0.vp),
        isModal!: Bool = true,
        showInSubWindow!: Bool = false,
        autoCancel!: Bool = true,
        maskColor!: ResourceColor = Color(0x33000000),
        transition!: TransitionEffect = TransitionEffect.OPACITY,
        onDidAppear!: () -> Unit = {=>},
        onDidDisappear!: () -> Unit = {=>},
        onWillAppear!: () -> Unit = {=>},
        onWillDisappear!: () -> Unit = {=>},
        keyboardAvoidMode!: KeyboardAvoidMode = KeyboardAvoidMode.Default,
        enableHoverMode!: Bool = false,
        hoverModeArea!: HoverModeAreaType = HoverModeAreaType.BottomScreen
    )
}
```

**功能：** 对话框基础选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var alignment

```cangjie
public var alignment: DialogAlignment
```

**功能：** 对话框在屏幕上的对齐方式。

**类型：** [DialogAlignment](./cj-common-types.md#enum-dialogalignment)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var autoCancel

```cangjie
public var autoCancel: Bool
```

**功能：** 是否允许用户点击遮罩层退出。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var enableHoverMode

```cangjie
public var enableHoverMode: Bool
```

**功能：** 是否响应悬停模式。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var hoverModeArea

```cangjie
public var hoverModeArea: HoverModeAreaType
```

**功能：** 悬停模式下对话框的显示区域。

**类型：** [HoverModeAreaType](#enum-hovermodeareatype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var isModal

```cangjie
public var isModal: Bool
```

**功能：** 是否为模态对话框。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var keyboardAvoidMode

```cangjie
public var keyboardAvoidMode: KeyboardAvoidMode
```

**功能：** 自定义对话框的键盘避免模式。

**类型：** [KeyboardAvoidMode](#enum-keyboardavoidmode)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var maskColor

```cangjie
public var maskColor: ResourceColor
```

**功能：** 自定义对话框遮罩颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var maskRect

```cangjie
public var maskRect: Rectangle
```

**功能：** 对话框遮罩区域。大小不能超过主窗口。

**类型：** [Rectangle](./cj-common-types.md#class-rectangle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var offset

```cangjie
public var offset: Offset
```

**功能：** 对话框偏移量。

**类型：** [Offset](./cj-common-types.md#class-offset)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22