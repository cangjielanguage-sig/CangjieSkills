### class NavigationTitleOptions

```cangjie
public class NavigationTitleOptions {
    public var backgroundColor: ?ResourceColor
    public var backgroundBlurStyle: ?BlurStyle
    public var barStyle: ?BarStyle
    public var paddingStart: ?Length
    public var paddingEnd: ?Length
    public init(backgroundColor!: ?ResourceColor = None, backgroundBlurStyle!: ?BlurStyle = None,
        barStyle!: ?BarStyle = None, paddingStart!: ?Length = None, paddingEnd!: ?Length = None
    )
}
```

**功能：** Navigation标题栏的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: ?BlurStyle
```

**功能：** 标题栏的背景模糊样式。如果未设置此参数，则禁用背景模糊效果。

**类型：** ?[BlurStyle](./cj-common-types.md#enum-blurstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var backgroundColor

```cangjie
public var backgroundColor: ?ResourceColor
```

**功能：** 标题栏的背景颜色。如果未设置此参数，则使用默认颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var barStyle

```cangjie
public var barStyle: ?BarStyle
```

**功能：** 标题栏的布局样式。

**类型：** ?[BarStyle](#enum-barstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var paddingEnd

```cangjie
public var paddingEnd: ?Length
```

**功能：** 设置标题栏结束边距。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var paddingStart

```cangjie
public var paddingStart: ?Length
```

**功能：** 设置标题栏起始边距。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?ResourceColor, ?BlurStyle, ?BarStyle, ?Length, ?Length)

```cangjie
public init(backgroundColor!: ?ResourceColor = None, backgroundBlurStyle!: ?BlurStyle = None,
    barStyle!: ?BarStyle = None, paddingStart!: ?Length = None, paddingEnd!: ?Length = None)
```

**功能：** NavigationTitleOptions的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|backgroundColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|标题栏背景颜色。|
|backgroundBlurStyle|?[BlurStyle](./cj-common-types.md#enum-blurstyle)|否|None|标题栏背景模糊样式。|
|barStyle|?[BarStyle](#enum-barstyle)|否|None|标题栏布局样式。初始值：BarStyle.Standard。|
|paddingStart|?[Length](./cj-common-types.md#interface-length)|否|None|标题栏起始边距。|
|paddingEnd|?[Length](./cj-common-types.md#interface-length)|否|None|标题栏结束边距。|