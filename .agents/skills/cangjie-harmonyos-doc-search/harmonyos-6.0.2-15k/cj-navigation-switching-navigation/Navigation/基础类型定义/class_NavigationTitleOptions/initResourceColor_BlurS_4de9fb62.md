#### init(?ResourceColor, ?BlurStyle, ?BarStyle, ?Length, ?Length)

```cangjie
public init(
    backgroundColor!: ?ResourceColor = None,
    backgroundBlurStyle!: ?BlurStyle = None,
    barStyle!: ?BarStyle = None,
    paddingStart!: ?Length = None,
    paddingEnd!: ?Length = None
)
```

**功能：** 创建NavigationTitleOptions。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| backgroundColor |?[ResourceColor](./cj-common-types.md#interface-resourcecolor)| 否  | None | 标题栏背景颜色，不设置时为系统默认颜色。|
| backgroundBlurStyle |?[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)| 否  | None | 标题栏背景模糊样式，不设置时关闭背景模糊效果。|
| barStyle |?[BarStyle](#enum-barstyle)| 否  | None | 标题栏布局方式设置。<br/>初始值：BarStyle.Standard。|
| paddingStart |?[Length](./cj-common-types.md#interface-length)| 否  | None | 标题栏起始端内间距。<br/>仅支持以下任一场景:<br/>1. 显示返回图标，即[hideBackButton](#func-hidebackbuttonbool)为false；<br/>2. 使用非自定义标题，即标题value类型为ResourceStr或NavigationCommonTitle。|
| paddingEnd |?[Length](./cj-common-types.md#interface-length)| 否  | None | 标题栏结束端内间距。<br/>仅支持以下任一场景:<br/>1. 使用非自定义菜单，即[菜单value](#func-menusarraynavigationmenuitem)为Array\<NavigationMenuItem>；<br/>2. 没有右上角菜单，且使用非自定义标题，即标题value类型为ResourceStr或NavigationCommonTitle。|