### init(?String, ?Placement, ?PopupButton, ?PopupButton, Option\<(PopupStateChangeParam) -> Unit>, ?Length, ?Bool, ?Color, ?PopupMessageOptions, ?Length, ?Bool, ?Position, ?Color, ?Bool, ?Length, ?ArrowPointPosition, ?Length, ?Length, ?Length, ?ShadowStyle, ?BlurStyle, ?TransitionEffect, Option\<(DismissPopupAction) -> Unit>, ?Bool)

```cangjie
public init(
    message!: ?String,
    placement!: ?Placement = Option.None,
    primaryButton!: ?PopupButton = None,
    secondaryButton!: ?PopupButton = None,
    onStateChange!: Option<(PopupStateChangeParam) -> Unit> = Option.None,
    arrowOffset!: ?Length = None,
    showInSubWindow!: ?Bool = None,
    mask!: ?Color = None,
    messageOptions!: ?PopupMessageOptions = None,
    targetSpace!: ?Length = None,
    enableArrow!: ?Bool = None,
    offset!: ?Position = None,
    popupColor!: ?Color = None,
    autoCancel!: ?Bool = None,
    width!: ?Length = None,
    arrowPointPosition!: ?ArrowPointPosition = None,
    arrowWidth!: ?Length = None,
    arrowHeight!: ?Length = None,
    radius!: ?Length = None,
    shadow!: ?ShadowStyle = None,
    backgroundBlurStyle!: ?BlurStyle = Option.None,
    transition!: ?TransitionEffect = Option.None,
    onWillDismiss!: Option<(DismissPopupAction) -> Unit> = None,
    followTransformOfTarget!: ?Bool = None
)
```

**功能：** 构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**