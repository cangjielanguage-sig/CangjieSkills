## class AlertDialogParamWithButtons

```cangjie
public class AlertDialogParamWithButtons <: AlertDialogParam {
    public var primaryButton: ?AlertDialogButtonBaseOptions
    public var secondaryButton: ?AlertDialogButtonBaseOptions
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
        primaryButton!: ?AlertDialogButtonBaseOptions,
        secondaryButton!: ?AlertDialogButtonBaseOptions
    )
}
```

**功能：** 定义带有两个确认按钮的警告弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [AlertDialogParam](#class-alertdialogparam)

### var primaryButton

```cangjie
public var primaryButton: ?AlertDialogButtonBaseOptions
```

**功能：** 第一个按钮。

**类型：** ?[AlertDialogButtonBaseOptions](#class-alertdialogbuttonbaseoptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var secondaryButton

```cangjie
public var secondaryButton: ?AlertDialogButtonBaseOptions
```

**功能：** 第二个按钮。

**类型：** ?[AlertDialogButtonBaseOptions](#class-alertdialogbuttonbaseoptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22