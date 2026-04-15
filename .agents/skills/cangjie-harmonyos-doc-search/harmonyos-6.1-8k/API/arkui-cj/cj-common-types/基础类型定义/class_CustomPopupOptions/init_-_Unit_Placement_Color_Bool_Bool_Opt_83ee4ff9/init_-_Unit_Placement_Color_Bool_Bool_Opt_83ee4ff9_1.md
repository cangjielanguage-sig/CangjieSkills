### init(() -> Unit, ?Placement, ?Color, ?Bool, ?Bool, Option\<(PopupStateChangeParam) -> Unit>, ?Bool, ?Color, ?Length, ?Color, ?Length, ?Position, ?Length, ?ArrowPointPosition, ?Length, ?Length, ?Length, ?ShadowStyle, ?BlurStyle, ?Bool, Option\<TransitionEffect>, Option\<(DismissPopupAction) -> Unit>, ?Bool)

```cangjie
public init(
    builder!: () -> Unit,
    placement!: ?Placement = Option.None,
    popupColor!: ?Color = None,
    enableArrow!: ?Bool = None,
    autoCancel!: ?Bool = None,
    onStateChange!: Option<(PopupStateChangeParam) -> Unit> = Option.None,
    showInSubWindow!: ?Bool = None,
    backgroundColor!: ?Color = None,
    arrowOffset!: ?Length = None,
    mask!: ?Color = None,
    targetSpace!: ?Length = None,
    offset!: ?Position = None,
    width!: ?Length = None,
    arrowPointPosition!: ?ArrowPointPosition = None,
    arrowWidth!: ?Length = None,
    arrowHeight!: ?Length = None,
    radius!: ?Length = None,
    shadow!: ?ShadowStyle = None,
    backgroundBlurStyle!: ?BlurStyle = Option.None,
    focusable!: ?Bool = None,
    transition!: Option<TransitionEffect> = Option.None,
    onWillDismiss!: Option<(DismissPopupAction) -> Unit> = None,
    followTransformOfTarget!: ?Bool = None
)
```

**功能：** 构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**