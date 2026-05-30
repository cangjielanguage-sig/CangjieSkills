### ActionSheetOptions(...)

```cangjie
public ActionSheetOptions(
    public var title: String,
    public var message: String,
    public var sheets: Array<SheetInfo>,
    public var subtitle!: Option<String> = Option.None,
    public var confirm!: Option<Confirm> = Option.None,
    public var autoCancel!: Option<Bool> = true,
    public var cancel!: Option<() -> Unit> = Option.None,
    public var alignment!: Option<DialogAlignment> = DialogAlignment.Bottom,
    public var offset!: Option<Offset> = Option.None,
    public var maskRect!: Option<Rectangle> = Rectangle(x: 0, y: 0,
        width: 100.percent, height: 100.percent),
    public var showInSubWindow!: Option<Bool> = false,
    public var isModal!: Option<Bool> = true,
    public var backgroundColor!: Option<Color> = Color.TRANSPARENT,
    public var backgroundBlurStyle!: Option<BlurStyle> = BlurStyle.COMPONENT_ULTRA_THICK,
    public var onWillDismiss!: Option<(DismissDialogAction) -> Unit> = None,
    public var cornerRadius!: Option<BorderRadiuses> = BorderRadiuses(topLeft: 32.vp, topRight: 32.vp,
        bottomLeft: 32.vp, bottomRight: 32.vp),
    public var borderWidth!: Option<Length> = 0.vp,
    public var borderColor!: Option<Color> = Color.BLACK,
    public var borderStyle!: Option<EdgeStyle> = EdgeStyle.SOILD,
    public var width!: Option<Length> = Option<Length>.None,
    public var height!: Option<Length> = Option<Length>.None,
    public var transition!: Option<TransitionEffect> = Option.None
) {}
```

**功能：** 构造一个ActionSheetOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**