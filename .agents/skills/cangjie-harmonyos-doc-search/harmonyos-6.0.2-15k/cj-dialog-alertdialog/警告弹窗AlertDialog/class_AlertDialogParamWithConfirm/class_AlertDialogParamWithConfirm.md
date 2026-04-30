## class AlertDialogParamWithConfirm

```cangjie
public class AlertDialogParamWithConfirm <: AlertDialogParam {
    public var confirm: AlertDialogButtonOptions = AlertDialogButtonOptions()

    public init(
        message: String,
        title!: String = "",
        subtitle!: String = "",
        autoCancel!: Bool = true,
        cancel!: () -> Unit = {=>},
        alignment!: DialogAlignment = DialogAlignment.Default,
        offset!: Offset = Offset(0.vp, 0.vp),
        gridCount!: Int32 = 4,
        maskRect!: Rectangle = Rectangle(),
        showInSubWindow!: Bool = false,
        isModal!: Bool = true,
        backgroundColor!: Color = Color.TRANSPARENT,
        backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK,
        confirm!: AlertDialogButtonOptions = AlertDialogButtonOptions()
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
        onWillDismiss!: Option<(DismissDialogAction) -> Unit>, // 5.1 start
        cornerRadius!: Option<BorderRadiuses> = BorderRadiuses(topLeft: 32.vp, topRight: 32.vp, bottomLeft: 32.vp,
            bottomRight: 32.vp),
        transition!: Option<TransitionEffect> = Option.None,
        width!: Option<Length> = Option<Length>.None,
        height!: Option<Length> = Option<Length>.None,
        borderWidth!: Option<Length> = 0.vp,
        borderColor!: Option<Color> = Color.BLACK,
        borderStyle!: Option<EdgeStyle> = EdgeStyle.SOLID,
        textStyle!: Option<WordBreak> = WordBreak.Normal,
        confirm!: AlertDialogButtonOptions = AlertDialogButtonOptions()
    )
    public init()
}
```

**功能：** 定义带有确认按钮的警告弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [AlertDialogParam](cj-dialog-alertdialog.md#class-alertdialogparam)