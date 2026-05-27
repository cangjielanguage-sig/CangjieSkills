### ShowDialogOptions(String, String, Array\<ButtonInfo>, DialogAlignment, Offset, Rectangle, Bool, Bool, Color, BlurStyle, Option\<ShadowOptions>, Option\<ShadowStyle>, Bool, HoverModeAreaType)

```cangjie
public ShowDialogOptions(
    public let title!: String = '',
    public let message!: String = '',
    public let buttons!: Array<ButtonInfo> = [ButtonInfo("button", Color(0x31463146))],
    public let alignment!: DialogAlignment = DialogAlignment.Default,
    public let offset!: Offset = Offset(0.vp, 0.vp),
    public let maskRect!: Rectangle = Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent),
    public let showInSubWindow!: Bool = false,
    public let isModal!: Bool = true,
    public let backgroundColor!: Color = Color.TRANSPARENT,
    public let backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK,
    public let shadowOption!: Option<ShadowOptions> = Option.None,
    public let shadowStyle!: Option<ShadowStyle> = Option.None,
    public let enableHoverMode!: Bool = false,
    public let hoverModeArea!: HoverModeAreaType = HoverModeAreaType.BOTTOM_SCREEN
)
```

**功能：** 构造一个ShowDialogOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**