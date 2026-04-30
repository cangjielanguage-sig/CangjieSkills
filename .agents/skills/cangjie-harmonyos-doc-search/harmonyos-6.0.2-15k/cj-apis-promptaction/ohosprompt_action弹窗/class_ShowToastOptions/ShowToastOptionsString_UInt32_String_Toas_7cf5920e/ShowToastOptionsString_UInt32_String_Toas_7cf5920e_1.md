### ShowToastOptions(String, UInt32, String, ToastShowMode, Alignment, Offset, Color, Color, BlurStyle, Option\<ShadowOptions>, Option\<ShadowStyle>, Bool, HoverModeAreaType)

```cangjie
public ShowToastOptions(
    public let message!: String = 'ShowToast',
    public let duration!: UInt32 = 1500,
    public let bottom!: String = '80vp',
    public let showMode!: ToastShowMode = ToastShowMode.Default,
    public let alignment!: Alignment = Alignment.Bottom,
    public let offset!: Offset = Offset(0.vp, 0.vp),
    public let backgroundColor!: Color = Color.TRANSPARENT,
    public let textColor!: Color = Color.BLACK,
    public let backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK,
    public let shadowOption!: Option<ShadowOptions> = Option.None,
    public let shadowStyle!: Option<ShadowStyle> = Option.None,
    public let enableHoverMode!: Bool = false,
    public let hoverModeArea!: HoverModeAreaType = HoverModeAreaType.BOTTOM_SCREEN
)
```

**功能：** 生成ShowToastOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**