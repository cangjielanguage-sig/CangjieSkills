## class ContextMenuOptions

```cangjie
public open class ContextMenuOptions {
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
}
```

**功能：** 配置弹出菜单的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var aboutToAppear

```cangjie
public var aboutToAppear: ?() -> Unit = None
```

**功能：** 菜单显示动效前的事件回调。

**类型：** ?()->Unit

**读写能力：** 可读写

**起始版本：** 19

### var aboutToDisappear

```cangjie
public var aboutToDisappear: ?() -> Unit = None
```

**功能：** 菜单退出动效前的事件回调。

**类型：** ?()->Unit

**读写能力：** 可读写

**起始版本：** 19

### var arrowOffset

```cangjie
public var arrowOffset: Length = 0.vp
```

**功能：** 箭头在菜单处的偏移。偏移量必须合法且转换为具体数值时大于0才会生效，另外该值生效时不会导致箭头超出菜单四周的安全距离。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**起始版本：** 19

### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
```

**功能：** 弹窗背板模糊材质。

**类型：** [BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)

**读写能力：** 可读写

**起始版本：** 19

### var backgroundColor

```cangjie
public var backgroundColor: ResourceColor = Color.TRANSPARENT,
```

**功能：** 弹窗背板颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**起始版本：** 19

### var enableArrow

```cangjie
public var enableArrow: Bool = false
```

**功能：** 是否显示箭头。如果菜单的大小和位置不足以放置箭头时，不会显示箭头。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var offset

```cangjie
public var offset: Position = Position(0.0, 0.0)
```

**功能：** 菜单弹出位置的偏移量，不会导致菜单显示超出屏幕范围。

**类型：** [Position](./cj-common-types.md#class-position)

**读写能力：** 可读写

**起始版本：** 19

### var onAppear

```cangjie
public var onAppear: ?() -> Unit = None
```

**功能：** 菜单弹出时的事件回调。

**类型：** ?()->Unit

**读写能力：** 可读写

**起始版本：** 19

### var onDisappear

```cangjie
public var onDisappear: ?() -> Unit = None
```

**功能：** 菜单消失时的事件回调。

**类型：** ?()->Unit

**读写能力：** 可读写

**起始版本：** 19

### var placement

```cangjie
public var placement: Option<Placement> = Option.None
```

**功能：** 菜单组件优先显示的位置，当前位置显示不下时，会自动调整位置。

**类型：** Option\<[Placement](./cj-common-types.md#enum-placement)>

**读写能力：** 可读写

**起始版本：** 19

### var preview

```cangjie
public var preview: Option<() -> Unit> = Option.None
```

**功能：** 长按悬浮菜单或使用bindContextMenu显示菜单的预览内容样式，为用户自定义的内容。

**类型：** Option\<() -> Unit>

**读写能力：** 可读写

**起始版本：** 19