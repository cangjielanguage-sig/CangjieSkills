## class PopupOptions

```cangjie
public class PopupOptions {
    public var message: ?String
    public var placement: ?Placement
    public var primaryButton: ?PopupButton
    public var secondaryButton: ?PopupButton
    public var onStateChange: ?(PopupStateChangeParam) -> Unit
    public var arrowOffset: ?Length
    public var showInSubWindow: ?Bool
    public var mask: ?ResourceColor
    public var messageOptions: ?PopupMessageOptions
    public var targetSpace: ?Length
    public var enableArrow: ?Bool
    public var offset: ?Position
    public var popupColor: ?ResourceColor
    public var autoCancel: ?Bool
    public var width: ?Length
    public var arrowPointPosition: Option<ArrowPointPosition>
    public var arrowWidth: ?Length
    public var arrowHeight: ?Length
    public var radius: ?Length
    public var shadow: ?ShadowStyle
    public var backgroundBlurStyle: ?BlurStyle
    public var transition: ?TransitionEffect
    public var onWillDismiss: ?(DismissPopupAction) -> Unit
    public var followTransformOfTarget: ?Bool
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
}
```

**功能：** 弹窗的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var message

```cangjie
public var message: ?String
```

**功能：** 设置弹窗信息内容。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var placement

```cangjie
public var placement: ?Placement
```

**功能：** 设置popup组件相对于目标的显示位置，默认值为Placement.Bottom。如果同时设置了placementOnTop和placement，则以placement的设置生效。

**类型：** ?[Placement](#enum-placement)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var primaryButton

```cangjie
public var primaryButton: ?PopupButton
```

**功能：** 设置第一个按钮。value: 弹窗里主按钮的文本。action: 点击主按钮的回调函数。

**类型：** ?[PopupButton](#class-popupbutton)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var secondaryButton

```cangjie
public var secondaryButton: ?PopupButton
```

**功能：** 设置第二个按钮。 value: 弹窗里辅助按钮的文本。action: 点击辅助按钮的回调函数。

**类型：** ?[PopupButton](#class-popupbutton)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var onStateChange

```cangjie
public var onStateChange: ?(PopupStateChangeParam) -> Unit
```

**功能：** 设置弹窗状态变化事件回调，参数为弹窗当前的显示状态。

**类型：** ?([PopupStateChangeParam](#class-popupstatechangeparam)) -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22