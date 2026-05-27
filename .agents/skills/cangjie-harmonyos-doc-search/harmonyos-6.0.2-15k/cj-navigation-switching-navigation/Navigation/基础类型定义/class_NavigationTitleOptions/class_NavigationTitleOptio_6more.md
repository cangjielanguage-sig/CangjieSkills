### class NavigationTitleOptions

```cangjie
public class NavigationTitleOptions {
    public var backgroundColor: ?ResourceColor = None
    public var backgroundBlurStyle: ?BlurStyle = None
    public var barStyle: ?BarStyle = None
    public var paddingStart: ?Length = None
    public var paddingEnd: ?Length = None
    public init(
        backgroundColor!: ?ResourceColor = None,
        backgroundBlurStyle!: ?BlurStyle = None,
        barStyle!: ?BarStyle = None,
        paddingStart!: ?Length = None,
        paddingEnd!: ?Length = None
    )
}
```

**功能：** 表示Navigation标题选项的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: ?BlurStyle = None
```

**功能：** 设置标题栏背景模糊样式，不设置时关闭背景模糊效果。

**类型：** ?[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)

**读写能力：** 可读写

**起始版本：** 20

#### var backgroundColor

```cangjie
public var backgroundColor: ?ResourceColor = None
```

**功能：** 设置标题栏背景颜色，不设置时为系统默认颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**起始版本：** 20

#### var barStyle

```cangjie
public var barStyle: ?BarStyle = None
```

**功能：** 设置标题栏布局方式设置。

**类型：** ?[BarStyle](#enum-barstyle)

**读写能力：** 可读写

**起始版本：** 20

#### var paddingEnd

```cangjie
public var paddingEnd: ?Length = None
```

**功能：** 标题栏结束端内间距。<br/>仅支持以下任一场景:<br/>1. 使用非自定义菜单，即[菜单value](#func-menusarraynavigationmenuitem)为Array&lt;NavigationMenuItem&gt;；<br/>2. 没有右上角菜单，且使用非自定义标题，即标题value类型为ResourceStr或NavigationCommonTitle。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**起始版本：** 20

#### var paddingStart

```cangjie
public var paddingStart: ?Length = None
```

**功能：** 标题栏起始端内间距。<br/>仅支持以下任一场景:<br/>1. 显示返回图标，即[hideBackButton](#func-hidebackbuttonbool)为false；<br/>2. 使用非自定义标题，即标题value类型为ResourceStr或NavigationCommonTitle。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**起始版本：** 20