### init(CustomView, ?VoidCallback, ?Bool, ?DialogAlignment, ?Offset, ?Bool, ?UInt32, ?ResourceColor, ?Rectangle, ?AnimateParam, ?AnimateParam, ?Bool, ?ResourceColor, ?Length, ?Bool, ?Callback\<DismissDialogAction,Unit>, ?Length, ?Length, ?Length, ?ResourceColor, ?EdgeStyles, ?ShadowOptions, ?BlurStyle)

```cangjie
public init(
    builder!: CustomView,
    cancel!: ?VoidCallback = None,
    autoCancel!: ?Bool = None,
    alignment!: ?DialogAlignment = None,
    offset!: ?Offset = None,
    customStyle!: ?Bool = None,
    gridCount!: ?UInt32 = None,
    maskColor!: ?ResourceColor = None,
    maskRect!: ?Rectangle = None,
    openAnimation!: ?AnimateParam = None,
    closeAnimation!: ?AnimateParam = None,
    showInSubWindow!: ?Bool = None,
    backgroundColor!: ?ResourceColor = None,
    cornerRadius!: ?Length = None,
    isModal!: ?Bool = None,
    onWillDismiss!: ?Callback<DismissDialogAction, Unit> = None,
    width!: ?Length = None,
    height!: ?Length = None,
    borderWidth!: ?Length = None,
    borderColor!: ?ResourceColor = None,
    borderStyle!: ?EdgeStyles = None,
    shadow!: ?ShadowOptions = None,
    backgroundBlurStyle!: ?BlurStyle = None
)
```

**功能：** 创建一个CustomDialogControllerOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**