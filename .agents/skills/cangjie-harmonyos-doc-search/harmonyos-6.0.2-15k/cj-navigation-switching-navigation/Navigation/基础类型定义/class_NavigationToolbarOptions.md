### class NavigationToolbarOptions

```cangjie
public class NavigationToolbarOptions {
    public var backgroundColor: ?ResourceColor = None
    public var backgroundBlurStyle: ?BlurStyle = None
    public var barStyle: ?BarStyle = None
    public init(
        backgroundColor!: ?ResourceColor = None,
        backgroundBlurStyle!: ?BlurStyle = None,
        barStyle!: ?BarStyle = None
    )
}
```

**功能：** 表示Navigation工具栏选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: ?BlurStyle = None
```

**功能：** 设置工具栏背景模糊样式，不设置时关闭背景模糊效果。

**类型：** ?[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)

**读写能力：** 可读写

**起始版本：** 20

#### var backgroundColor

```cangjie
public var backgroundColor: ?ResourceColor = None
```

**功能：** 设置工具栏背景颜色，不设置时为系统默认颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**起始版本：** 20

#### var barStyle

```cangjie
public var barStyle: ?BarStyle = None
```

**功能：** 设置工具栏布局方式设置。

**类型：** ?[BarStyle](#enum-barstyle)

**读写能力：** 可读写

**起始版本：** 20

#### init(?ResourceColor, ?BlurStyle, ?BarStyle)

```cangjie
public init(
    backgroundColor!: ?ResourceColor = None,
    backgroundBlurStyle!: ?BlurStyle = None,
    barStyle!: ?BarStyle = None
)
```

**功能：** 创建NavigationToolbarOptions。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|backgroundColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|工具栏背景颜色，不设置时为系统默认颜色。|
|backgroundBlurStyle|?[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)|否|None|工具栏背景模糊样式，不设置时关闭背景模糊效果。|
|barStyle|?[BarStyle](#enum-barstyle)|否|None| 工具栏布局模式。|