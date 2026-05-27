## class CustomDialogControllerOptions

```cangjie
public class CustomDialogControllerOptions {
    public var cancel:() -> Unit
    public var autoCancel: Bool
    public var alignment: DialogAlignment
    public var offset: Offset
    public var customStyle: Bool
    public var gridCount: Option<Int32>
    public var maskColor: ResourceColor
    public var maskRect: Rectangle
    public var openAnimation: Option<AnimateParam>
    public var closeAnimation: Option<AnimateParam>
    public var showInSubWindow: Bool
    public var backgroundColor: Option<ResourceColor>
    public var cornerRadius: Length
    public var isModal: Option<Bool>
    public var onWillDismiss: Option <(DismissDialogAction) -> Unit>
    public var borderWidth: Option<Length>
    public var borderColor: Option<ResourceColor>
    public var borderStyle: Option<EdgeStyle>
    public var width: Option<Length>
    public var height: Option<Length>
    public var shadow: Option<ShadowOptions>
    public var backgroundBlurStyle: Option<BlurStyle>
    public init(
        cancel!: () -> Unit = { => },
        autoCancel!: Bool = true,
        alignment!: DialogAlignment = DialogAlignment.Default,
        offset!: Offset = Offset(0.vp, 0.vp),
        customStyle!: Bool = false,
        gridCount!: Option<Int32> = Option.None,
        maskColor!: ResourceColor = Color(0x33000000),
        maskRect!: Rectangle = Rectangle(),
        openAnimation!: Option<AnimateParam> = Option.None,
        closeAnimation!: Option<AnimateParam> = Option.None,
        showInSubWindow!: Bool = false,
        backgroundColor!: Option<ResourceColor> = Option.None,
        cornerRadius!: Length = 24.vp,
        isModal!: Option<Bool> = true,
        onWillDismiss!: Option<(DismissDialogAction) -> Unit> = Option.None,
        borderWidth!: Option<Length> = 0.vp,
        borderColor!: Option<ResourceColor> = Color.BLACK,
        borderStyle!: Option<EdgeStyle> = EdgeStyle.SOILD,
        width!: Option<Length> = Option<Length>.None,
        height!: Option<Length> = Option<Length>.None,
        shadow!: Option<ShadowOptions> = Option<ShadowOptions>.None,
        backgroundBlurStyle!: Option<BlurStyle> = BlurStyle.COMPONENT_ULTRA_THICK
    )
}
```

**功能：** 声明自定义弹窗相关设置的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12