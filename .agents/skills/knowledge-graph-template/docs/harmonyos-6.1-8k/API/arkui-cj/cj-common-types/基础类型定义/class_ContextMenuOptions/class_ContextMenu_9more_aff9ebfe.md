## class ContextMenuOptions

```cangjie
public class ContextMenuOptions {
    public var offset: ?Position
    public var placement: Option<Placement>
    public var enableArrow: ?Bool
    public var arrowOffset: ?Length
    public var preview: ?CustomBuilder
    public var previewAnimationOptions: ?ContextMenuAnimationOptions
    public var onAppear: ?() -> Unit
    public var onDisappear: ?() -> Unit
    public var aboutToAppear: ?() -> Unit
    public var aboutToDisappear: ?() -> Unit
    public var backgroundColor: ?ResourceColor
    public var backgroundBlurStyle: ?BlurStyle
    public var transition: ?TransitionEffect
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
}
```

**功能：** 配置弹出菜单的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var offset

```cangjie
public var offset: ?Position
```

**功能：** 菜单弹出位置的偏移量，不会导致菜单显示超出屏幕范围。

**类型：** ?[Position](#class-position)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var placement

```cangjie
public var placement: Option<Placement>
```

**功能：** 菜单组件优先显示的位置，当前位置显示不下时，会自动调整位置。

**类型：** Option<[Placement](#enum-placement)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var enableArrow

```cangjie
public var enableArrow: ?Bool
```

**功能：** 是否显示箭头。如果菜单的大小和位置不足以放置箭头时，不会显示箭头。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var arrowOffset

```cangjie
public var arrowOffset: ?Length
```

**功能：** 箭头在菜单处的偏移。偏移量必须合法且转换为具体数值时大于0才会生效，另外该值生效时不会导致箭头超出菜单四周的安全距离。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var preview

```cangjie
public var preview: ?CustomBuilder
```

**功能：** 长按悬浮菜单或使用bindContextMenu显示菜单的预览内容样式，为用户自定义的内容。

**类型：** ?[CustomBuilder](#type-custombuilder)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var previewAnimationOptions

```cangjie
public var previewAnimationOptions: ?ContextMenuAnimationOptions
```

**功能：** 控制长按预览显示动画开始倍率和结束倍率（相对预览原图比例）。

**类型：** ?[ContextMenuAnimationOptions](#class-contextmenuanimationoptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var onAppear

```cangjie
public var onAppear: ?() -> Unit
```

**功能：** 菜单弹出时的事件回调。

**类型：** ?() -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var onDisappear

```cangjie
public var onDisappear: ?() -> Unit
```

**功能：** 菜单消失时的事件回调。

**类型：** ?() -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22