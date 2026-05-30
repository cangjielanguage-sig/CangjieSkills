### class PopupOptions

```cangjie
public class PopupOptions {
    public var message: String = ""
    public var placementOnTop: Bool = false
    public var primaryButton: Action = Action(value: "", action: {=>})
    public var secondaryButton: Action = Action(value: "", action: {=>})
    public var onStateChange: Option<(StateChangeEvent) -> Unit> = Option.None
    public var messageOptions: PopupMessageOptions = PopupMessageOptions()
    public var arrowOffset: Length = 0.vp
    public var showInSubWindow: Bool = false
    public var mask: Color = Color(0x1000000)
    public var targetSpace: Length = 0.vp
    public var placement: ?Placement = Option.None
    public var offset: Position = Position(0.0, 0.0)
    public var enableArrow: Bool = true
    public var popupColor: Color = Color(0x1000000)
    public var autoCancel: Bool = true
    public var width: Length = 0.vp
    public var arrowPointPosition: Option<ArrowPointPosition> = None
    public var arrowWidth: Length = 16.vp
    public var arrowHeight: Length = 8.vp
    public var radius: Length = 20.vp
    public var shadow: ShadowStyle = ShadowStyle.OUTER_DEFAULT_MD
    public var backgroundBlurStyle: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
    public var transition: Option<TransitionEffect> = Option.None
    public var onWillDismiss: Option<(DismissPopupAction) -> Unit> = None
    public var followTransformOfTarget: Bool = false
    public init(
        message!: String,
        placementOnTop!: Bool = false,
        primaryButton!: Action = Action(value: "", action: { => }),
        secondaryButton!: Action = Action(value: "", action: { => }),
        onStateChange!: Option<(StateChangeEvent) -> Unit> = Option.None
    )
    public init(
        message!: String,
        placementOnTop!: Bool = false,
        primaryButton!: Action = Action(value: "", action: { => }),
        secondaryButton!: Action = Action(value: "", action: { => }),
        onStateChange!: Option<(StateChangeEvent) -> Unit> = Option.None,
        arrowOffset!: Length = 0.vp,
        showInSubWindow!: Bool,
        messageOptions!: PopupMessageOptions = PopupMessageOptions(),
        mask!: Color = Color(0x1000000),
        targetSpace!: Length = 0.vp,
        placement!: ?Placement = Option.None,
        offset!: Position = Position(0.0, 0.0),
        enableArrow!: Bool = true,
        popupColor!: Color = Color(0x1000000),
        autoCancel!: Bool = true,
        width!: Length = 0.vp,
        arrowPointPosition!: ?ArrowPointPosition = None,
        arrowWidth!: Length = 16.vp,
        arrowHeight!: Length = 8.vp,
        radius!: Length = 20.vp,
        shadow!: ShadowStyle = ShadowStyle.OUTER_DEFAULT_MD,
        backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK,
        transition!: ?TransitionEffect = Option.None,
        onWillDismiss!: Option<(DismissPopupAction) -> Unit> = None,
        followTransformOfTarget!: Bool = false
    )
    public init() {}
}
```

**功能：** 弹窗的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12