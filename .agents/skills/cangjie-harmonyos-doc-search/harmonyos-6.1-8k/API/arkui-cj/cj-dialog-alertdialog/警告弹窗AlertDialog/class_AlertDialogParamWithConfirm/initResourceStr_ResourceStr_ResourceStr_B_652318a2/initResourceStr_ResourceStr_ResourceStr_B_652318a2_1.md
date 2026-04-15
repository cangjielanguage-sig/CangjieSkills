### init(?ResourceStr, ?ResourceStr, ?ResourceStr, ?Bool, ?VoidCallback, ?DialogAlignment, ?Offset, ?UInt32, ?Rectangle, ?Bool, ?Bool, ?ResourceColor, ?BlurStyle, ?Callback\<DismissDialogAction, Unit>, ?BorderRadiuses, ?TransitionEffect, ?Length, ?Length, ?Length, ?BorderColor, ?EdgeStyles, ?ShadowOptions, ?WordBreak, ?AlertDialogButtonBaseOptions)

```cangjie
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
    confirm!: ?AlertDialogButtonBaseOptions = None
)
```

**功能：** 定义带有确认按钮的警告弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**