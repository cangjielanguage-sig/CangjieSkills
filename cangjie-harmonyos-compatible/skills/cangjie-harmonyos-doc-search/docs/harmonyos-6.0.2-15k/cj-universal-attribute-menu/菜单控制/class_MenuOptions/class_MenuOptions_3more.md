## class MenuOptions

```cangjie
public class MenuOptions <: ContextMenuOptions {
    public var title: ?String
    public var showInSubWindow: ?Bool
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
}
```

**功能：** 配置弹出菜单的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [ContextMenuOptions](#class-contextmenuoptions)

### var showInSubWindow

```cangjie
public var showInSubWindow: ?Bool = None
```

**功能：** 菜单标题。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var title

```cangjie
public var title: ?String = None
```

**功能：** 是否在子窗口显示菜单。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19