### class CustomPopupOptions

```cangjie
public class CustomPopupOptions {
    public var builder: () -> Unit = {=>}
    public var placement: Placement = Placement.Bottom
    public var maskColor: Color = Color(0x1000000)
    public var backgroundColor: Color = Color(0x1000000)
    public var enableArrow: Bool = true
    public var autoCancel: Bool = true
    public var onStateChange: Option<(StateChangeEvent) -> Unit> = Option.None
    public var popupColor: ?Color = None
    public var arrowOffset: Length = 0.vp
    public var showInSubWindow: Bool = false
    public var mask: ?Color = None
    public var targetSpace: Length = 0.vp
    public var offset: Position = Position(0.0, 0.0)
    public var width: Length = 0.vp
    public var arrowPointPosition: Option<ArrowPointPosition> = None
    public var arrowWidth: Length = 16.vp
    public var arrowHeight: Length = 8.vp
    public var radius: Length = 20.vp
    public var shadow: ShadowStyle = ShadowStyle.OUTER_DEFAULT_MD
    public var backgroundBlurStyle: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
    public var focusable: Bool = false
    public var transition: Option<TransitionEffect> = Option.None
    public var onWillDismiss: Option<(DismissPopupAction) -> Unit> = Noneic var followTransformOfTarget: Bool = false
    public init(
        builder!: () -> Unit,
        placement!: Placement = Placement.Bottom,
        maskColor!: Color = Color(0x1000000),
        popupColor!: Color = Color(0x1000000),
        enableArrow!: Bool = true,
        autoCancel!: Bool = true,
        onStateChange!: Option<(StateChangeEvent) -> Unit> = Option.None
    )
    public init(
        builder!: () -> Unit,
        placement!: Placement = Placement.Bottom,
        maskColor!: Color = Color(0x1000000),
        popupColor!: Color = Color(0x1000000),
        enableArrow!: Bool = true,
        autoCancel!: Bool = true,
        onStateChange!: Option<(StateChangeEvent) -> Unit> = Option.None,
        showInSubWindow!: Bool, // 5.1 start
        backgroundColor!: Color = Color(0x1000000),
        arrowOffset!: Length = 0.vp,
        mask!: ?Color = None,
        targetSpace!: Length = 0.vp,
        offset!: Position = Position(0.0, 0.0),
        width!: Length = 0.vp,
        arrowPointPosition!: ?ArrowPointPosition = None,
        arrowWidth!: Length = 16.vp,
        arrowHeight!: Length = 16.vp,
        radius!: Length = 20.vp,
        shadow!: ShadowStyle = ShadowStyle.OUTER_DEFAULT_MD,
        backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK,
        focusable!: Bool = false,
        transition!: Option<TransitionEffect> = Option.None,
        onWillDismiss! : Option<(DismissPopupAction) -> Unit> = None,
        followTransformOfTarget!: Bool = false
    )
    public init() {}
}
```

**功能：** 弹出弹窗的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12