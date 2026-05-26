## class CustomDialogOptions

```cangjie
public class CustomDialogOptions <: BaseDialogOptions {
    public let builder:() -> Unit = {=>}
    public let backgroundColor: UInt32 = Color.TRANSPARENT.toUInt32()
    public let cornerRadius: BorderRadiuses= BorderRadiuses(topLeft: 32.vp, topRight: 32.vp, bottomLeft: 32.vp, bottomRight: 32.vp)
    public let borderWidth: EdgeWidths = EdgeWidths()
    public let borderColor: EdgeColor = EdgeColor()
    public let borderStyle: Option<BorderStyle> = None
    public let borderEdgeStyle: Option<EdgeStyles> = None
    public let width: Length = 400.vp
    public let height: Length = 100.vp
    public let shadowOption: Option<ShadowOptions> = None
    public let shadowStyle: Option<ShadowStyle> = None
    public let backgroundBlurStyle: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
    public init(
        maskRect!: Rectangle = Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent),
        alignment!: DialogAlignment = DialogAlignment.Default,
        offset!: Offset = Offset(0.vp, 0.vp),
        isModal!: Bool = true,
        showInSubWindow!: Bool = false,
        builder!: ()-> Unit
    )
    public init(
        maskRect!: Rectangle = Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent),
        alignment!: DialogAlignment = DialogAlignment.Default,
        offset!: Offset = Offset(0.vp, 0.vp),
        isModal!: Bool = true,
        showInSubWindow!: Bool = false,
        builder!: ()-> Unit,
        autoCancel!: Bool, // 5.1 start
        maskColor!: Color = Color(0x33000000),
        transition!: TransitionEffect = TransitionEffect.OPACITY,
        onDidAppear!: () -> Unit = { => },
        onDidDisappear!: () -> Unit = { => },
        onWillAppear!: () -> Unit = { => },
        onWillDisappear!: () -> Unit = { => },
        keyboardAvoidMode!: KeyboardAvoidMode = KeyboardAvoidMode.DEFAULT,
        enableHoverMode!: Bool = false,
        hoverModeArea!: HoverModeAreaType = HoverModeAreaType.BOTTOM_SCREEN,
        backgroundColor!: Color = Color.TRANSPARENT,
        cornerRadius!: BorderRadiuses = BorderRadiuses(topLeft: 32.vp, topRight: 32.vp, bottomLeft: 32.vp, bottomRight: 32.vp),
        borderWidth!: EdgeWidths = EdgeWidths(top: 0.vp, right: 0.vp, bottom: 0.vp, left: 0.vp),
        borderColor!: EdgeColor = EdgeColor(top: Color.BLACK, right: Color.BLACK, bottom: Color.BLACK, left: Color.BLACK),
        borderStyle!: Option<BorderStyle> = Option.None,
        borderEdgeStyle!: Option<EdgeStyles> = Option.None,
        width!: Length = 400.vp,
        height!: Length = 100.vp,
        shadowOption!: Option<ShadowOptions> = Option.None,
        shadowStyle!: Option<ShadowStyle> = Option.None,
        backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
    )
    public init()
}
```

**功能：** 自定义弹窗的内容，继承自BaseDialogOptions。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [BaseDialogOptions](#class-basedialogoptions)