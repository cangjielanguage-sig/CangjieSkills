### init(?ResourceStr, ?ResourceStr, ?ResourceStr, ?ActionSheetButtonOptions, ?VoidCallback, ?Array\<SheetInfo>, ?Bool, ?DialogAlignment, ?ActionSheetOffset, ?Rectangle, ?Bool, ?Bool, ?ResourceColor, ?BlurStyle, ?Callback\<DismissDialogAction, Unit>, ?TransitionEffect, ?BorderRadiuses, ?Length, ?Length, ?Length, ?ResourceColor, ?EdgeStyles, ?ShadowOptions)

```cangjie
public init(
    title!: ?ResourceStr,
    subtitle!: ?ResourceStr = None,
    message!: ?ResourceStr,
    confirm!: ?ActionSheetButtonOptions = None,
    cancel!: ?VoidCallback = None,
    sheets!: ?Array<SheetInfo>,
    autoCancel!: ?Bool = None,
    alignment!: ?DialogAlignment = None,
    offset!: ?ActionSheetOffset = None,
    maskRect!: ?Rectangle = None,
    showInSubWindow!: ?Bool = None,
    isModal!: ?Bool = None,
    backgroundColor!: ?ResourceColor = None,
    backgroundBlurStyle!: ?BlurStyle = None,
    onWillDismiss!: ?Callback<DismissDialogAction, Unit> = None,
    transition!: ?TransitionEffect = None,
    cornerRadius!: ?BorderRadiuses = None,
    width!: ?Length = None,
    height!: ?Length = None,
    borderWidth!: ?Length = None,
    borderColor!: ?ResourceColor = None,
    borderStyle!: ?EdgeStyles = None,
    shadow!: ?ShadowOptions = None
)
```

**功能：** ActionSheetOptions类的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**