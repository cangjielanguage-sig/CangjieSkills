## class AlertDialogParam

```cangjie
public open class AlertDialogParam {
    public var message: String = ""
    public var title!: Option<String> = Option.None,
    public var subtitle!: Option<String> = Option.None,
    public var autoCancel!: Option<Bool> = true,
    public var cancel!: Option<() -> Unit> = Option.None,
    public var alignment!: Option<DialogAlignment> = DialogAlignment.Bottom,
    public var offset!: Option<Offset> = Option.None,
    public var gridCount!: Option<UInt32> = 4,
    public var maskRect!: Option<Rectangle> = Rectangle(x: 0, y: 0,
        width: 100.percent, height: 100.percent),
    public var showInSubWindow!: Option<Bool> = false,
    public var isModal!: Option<Bool> = true,
    public var backgroundColor!: Option<Color> = Color.TRANSPARENT,
    public var backgroundBlurStyle!: Option<BlurStyle> = BlurStyle.COMPONENT_ULTRA_THICK,
    public var onWillDismiss!: Option<(DismissDialogAction) -> Unit> = None,
    public var cornerRadius!: Option<BorderRadiuses> = BorderRadiuses(topLeft: 32.vp, topRight: 32.vp,
        bottomLeft: 32.vp, bottomRight: 32.vp),
    public var transition!: Option<TransitionEffect> = Option.None,
    public var width!: Option<Length> = Option<Length>.None,
    public var height!: Option<Length> = Option<Length>.None,
    public var borderWidth!: Option<Length> = 0.vp,
    public var borderColor!: Option<Color> = Color.BLACK,
    public var borderStyle!: Option<EdgeStyle> = EdgeStyle.SOILD,
    public var textStyle!: Option<WordBreak> = WordBreak.Normal

    public init(
        message: String,
        title!: String = "",
        subtitle!: String = "",
        autoCancel!: Bool = true,
        cancel!: () -> Unit = {=>},
        alignment!: DialogAlignment = DialogAlignment.Default,
        offset!: Offset = Offset(0.vp, 0.vp),
        gridCount!: Int32 = 4,
        maskRect!: Rectangle = Rectangle(x: 0, y: 0, width: 100.percent, height: 100.percent),
        showInSubWindow!: Bool = false,
        isModal!: Bool = true,
        backgroundColor!: Color = Color.TRANSPARENT,
        backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
    )
    public init(
        message: String,
        title!: Option<String> = Option.None,
        subtitle!: Option<String> = Option.None,
        autoCancel!: Option<Bool> = true,
        cancel!: Option<() -> Unit> = Option.None,
        alignment!: Option<DialogAlignment> = DialogAlignment.Bottom,
        offset!: Option<Offset> = Option.None,
        gridCount!: Option<UInt32> = 4,
        maskRect!: Option<Rectangle> = Rectangle(x: 0, y: 0, width: 100.percent, height: 100.percent),
        showInSubWindow!: Option<Bool> = false,
        isModal!: Option<Bool> = true,
        backgroundColor!: Option<Color> = Color.TRANSPARENT,
        backgroundBlurStyle!: Option<BlurStyle> = BlurStyle.COMPONENT_ULTRA_THICK,
        onWillDismiss!: Option<(DismissDialogAction) -> Unit>,
        cornerRadius!: Option<BorderRadiuses> = BorderRadiuses(topLeft: 32.vp, topRight: 32.vp, bottomLeft: 32.vp,
            bottomRight: 32.vp),
        transition!: Option<TransitionEffect> = Option.None,
        width!: Option<Length> = Option<Length>.None,
        height!: Option<Length> = Option<Length>.None,
        borderWidth!: Option<Length> = 0.vp,
        borderColor!: Option<Color> = Color.BLACK,
        borderStyle!: Option<EdgeStyle> = EdgeStyle.SOLID,
        textStyle!: Option<WordBreak> = WordBreak.Normal
    )
    public init()
}
```

**功能：** 定义告警弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12