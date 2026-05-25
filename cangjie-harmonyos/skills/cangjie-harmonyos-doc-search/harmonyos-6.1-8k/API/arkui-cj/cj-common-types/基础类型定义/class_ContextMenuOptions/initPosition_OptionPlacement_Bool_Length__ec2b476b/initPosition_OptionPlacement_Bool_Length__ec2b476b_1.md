### init(?Position, Option\<Placement>, ?Bool, ?Length, Option\<() -> Unit>, ?ContextMenuAnimationOptions, ?() -> Unit, ?() -> Unit, ?() -> Unit, ?() -> Unit, ?ResourceColor, ?BlurStyle, ?TransitionEffect, ?BorderRadiuses, ?Margin)

```cangjie
public init(
    offset!: ?Position = None,
    placement!: Option<Placement> = Option.None,
    enableArrow!: ?Bool = None,
    arrowOffset!: ?Length = None,
    preview!: Option<() -> Unit> = Option.None,
    previewAnimationOptions!: ?ContextMenuAnimationOptions = None,
    onAppear!: ?() -> Unit = None,
    onDisappear!: ?() -> Unit = None,
    aboutToAppear!: ?() -> Unit = None,
    aboutToDisappear!: ?() -> Unit = None,
    backgroundColor!: ?ResourceColor = None,
    backgroundBlurStyle!: ?BlurStyle = Option.None,
    transition!: ?TransitionEffect = None,
    borderRadius!: ?BorderRadiuses = None,
    layoutRegionMargin!: ?Margin = None
)
```

**功能：** 创建ContextMenuOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**