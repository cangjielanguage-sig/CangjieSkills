### init(Position, Option\<Placement>, Bool, Length, Option\<() -> Unit>, ?ContextMenuAnimationOptions, ?() -> Unit, ?() -> Unit, ?() -> Unit, ?() -> Unit, ResourceColor, BlurStyle, ?TransitionEffect, ?String, ?Bool)

```cangjie
public init(
    offset!: Position = Position(0.0, 0.0),
    placement!: Option<Placement> = Option.None,
    enableArrow!: Bool = false,
    arrowOffset!: Length = 0.vp,
    preview!: Option<() -> Unit> = Option.None,
    previewAnimationOptions!: ?ContextMenuAnimationOptions = None,
    onAppear!: ?() -> Unit = None,
    onDisappear!: ?() -> Unit = None,
    aboutToAppear!: ?() -> Unit = None,
    aboutToDisappear!: ?() -> Unit = None,
    backgroundColor!: ResourceColor = Color.TRANSPARENT,
    backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK,
    transition!: ?TransitionEffect = None,
    title!: ?String = None,
    showInSubWindow!: ?Bool = None
)
```

**功能：** 创建 MenuOptions 对象。

**参数：**