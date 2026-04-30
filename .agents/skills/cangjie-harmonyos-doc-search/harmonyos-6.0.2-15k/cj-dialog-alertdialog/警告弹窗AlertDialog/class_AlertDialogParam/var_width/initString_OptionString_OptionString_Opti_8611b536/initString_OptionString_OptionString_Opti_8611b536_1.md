#### init(String, Option\<String>, Option\<String>, Option\<Bool>, Option\<() -> Unit>, Option\<DialogAlignment>, Option\<Offset>, Option\<UInt32>, Option\<Rectangle>, Option\<Bool>, Option\<Bool>, Option\<Color>, Option\<BlurStyle>, Option\<(DismissDialogAction) -> Unit>, Option\<BorderRadiuses>, Option\<TransitionEffect>, Option\<Length>, Option\<Length>, Option\<Length>, Option\<Color>, Option\<EdgeStyle>, Option\<WordBreak>)

```cangjie
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
```

**功能：** 定义告警弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**