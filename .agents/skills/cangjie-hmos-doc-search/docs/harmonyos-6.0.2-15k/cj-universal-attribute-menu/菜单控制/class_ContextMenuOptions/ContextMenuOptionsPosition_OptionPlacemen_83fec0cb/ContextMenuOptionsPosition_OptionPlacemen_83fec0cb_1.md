### ContextMenuOptions(Position, Option\<Placement>, Bool, Length, Option\<() -> Unit>, ?ContextMenuAnimationOptions, ?() -> Unit, ?() -> Unit, ?() -> Unit, ?() -> Unit, ResourceColor, BlurStyle, ?TransitionEffect)

```cangjie
public ContextMenuOptions(
    public var offset!: Position = Position(0.0, 0.0),
    public var placement!: Option<Placement> = Option.None,
    public var enableArrow!: Bool = false,
    public var arrowOffset!: Length = 0.vp,
    public var preview!: Option<() -> Unit> = Option.None,
    public var previewAnimationOptions!: ?ContextMenuAnimationOptions = None,
    public var onAppear!: ?() -> Unit = None,
    public var onDisappear!: ?() -> Unit = None,
    public var aboutToAppear!: ?() -> Unit = None,
    public var aboutToDisappear!: ?() -> Unit = None,
    public var backgroundColor!: ResourceColor = Color.TRANSPARENT,
    public var backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK,
    public var transition!: ?TransitionEffect = None
)
```

**功能：** 创建 ContextMenuOptions 对象。

**参数：**