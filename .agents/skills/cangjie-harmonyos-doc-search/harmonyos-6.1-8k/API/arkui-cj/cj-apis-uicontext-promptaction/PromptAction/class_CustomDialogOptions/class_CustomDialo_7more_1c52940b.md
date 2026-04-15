## class CustomDialogOptions

```cangjie
public class CustomDialogOptions <: BaseDialogOptions {
    public var builder: () -> Unit
    public var backgroundColor: ResourceColor
    public var cornerRadius: BorderRadiuses
    public var borderWidth: EdgeWidths
    public var borderColor: EdgeColors
    public var borderStyle: EdgeStyles
    public var width: Length
    public var height: Length
    public var shadow: ?ShadowOptions
    public var backgroundBlurStyle: BlurStyle
    public init(
        builder!: () -> Unit,
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
        hoverModeArea!: HoverModeAreaType = HoverModeAreaType.BottomScreen,
        backgroundColor!: ResourceColor = Color.Transparent,
        cornerRadius!: BorderRadiuses = BorderRadiuses(topLeft: 32.vp, topRight: 32.vp, bottomLeft: 32.vp,
            bottomRight: 32.vp),
        borderWidth!: EdgeWidths = EdgeWidths(top: 0.vp, right: 0.vp, bottom: 0.vp, left: 0.vp),
        borderColor!: EdgeColors = EdgeColors(top: Color.Black, right: Color.Black, bottom: Color.Black, left: Color.Black),
        borderStyle!: EdgeStyles = EdgeStyles(),
        width!: Length = 400.vp,
        height!: Length = 100.vp,
        shadow!: ?ShadowOptions = None,
        backgroundBlurStyle!: BlurStyle = BlurStyle.ComponentUltraThick
    )
}
```

**功能：** 对话框自定义内容选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [BaseDialogOptions](#class-basedialogoptions)

### var backgroundColor

```cangjie
public var backgroundColor: ResourceColor
```

**功能：** 自定义对话框的背景颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var borderColor

```cangjie
public var borderColor: EdgeColors
```

**功能：** 自定义对话框的边框颜色。

**类型：** [EdgeColors](#class-edgecolors)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var cornerRadius

```cangjie
public var cornerRadius: BorderRadiuses
```

**功能：** 自定义对话框的圆角半径。

**类型：** [BorderRadiuses](./cj-common-types.md#class-borderradiuses)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var borderStyle

```cangjie
public var borderStyle: EdgeStyles
```

**功能：** 自定义对话框的边框样式。

**类型：** [EdgeStyles](./cj-common-types.md#class-edgestyles)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var borderWidth

```cangjie
public var borderWidth: EdgeWidths
```

**功能：** 自定义对话框的边框宽度。

**类型：** [EdgeWidths](./cj-common-types.md#class-edgewidths)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var builder

```cangjie
public var builder: () -> Unit
```

**功能：** 允许开发者自定义对话框内容。

**类型：** () -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22