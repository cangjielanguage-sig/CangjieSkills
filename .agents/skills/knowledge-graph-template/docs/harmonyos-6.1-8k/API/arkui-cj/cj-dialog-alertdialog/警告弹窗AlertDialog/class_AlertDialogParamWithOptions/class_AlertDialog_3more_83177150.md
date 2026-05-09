## class AlertDialogParamWithOptions

```cangjie
public class AlertDialogParamWithOptions <: AlertDialogParam {
    public var buttons: ?Array<AlertDialogButtonOptions>
    public var buttonDirection: ?DialogButtonDirection
    public init(
        title!: ?ResourceStr = None,
        subtitle!: ?ResourceStr = None,
        message!: ?ResourceStr,
        autoCancel!: ?Bool = None,
        cancel!: ?VoidCallback = None,
        alignment!: ?DialogAlignment = None,
        offset!: ?Offset = None,
        gridCount!: ?UInt32 = None,
        maskRect!: ?Rectangle = None,
        showInSubWindow!: ?Bool = None,
        isModal!: ?Bool = None,
        backgroundColor!: ?ResourceColor = None,
        backgroundBlurStyle!: ?BlurStyle = None,
        onWillDismiss!: ?Callback<DismissDialogAction, Unit> = None,
        cornerRadius!: ?BorderRadiuses = None,
        transition!: ?TransitionEffect = None,
        width!: ?Length = None,
        height!: ?Length = None,
        borderWidth!: ?Length = None,
        borderColor!: ?BorderColor = None,
        borderStyle!: ?EdgeStyles = None,
        shadow!: ?ShadowOptions = None,
        textStyle!: ?WordBreak = None,
        buttons!: ?Array<AlertDialogButtonOptions>,
        buttonDirection!: ?DialogButtonDirection = None
    )
}
```

**功能：** 定义了包含多个按钮的警告弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [AlertDialogParam](#class-alertdialogparam)

### var buttonDirection

```cangjie
public var buttonDirection: ?DialogButtonDirection
```

**功能：** 按钮排布方向默认值为DialogButtonDirection.AUTO，建议3个以上按钮使用Auto模式（两个以上按钮会切换为纵向模式，通常能显示更多按钮），非Auto模式下，3个以上按钮可能会显示不全，超出显示范围的按钮会被截断。

**类型：** ?[DialogButtonDirection](#enum-dialogbuttondirection)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var buttons

```cangjie
public var buttons: ?Array<AlertDialogButtonOptions>
```

**功能：** 弹窗容器中的多个按钮。

**类型：** ?Array\<[AlertDialogButtonOptions](#class-alertdialogbuttonoptions)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22