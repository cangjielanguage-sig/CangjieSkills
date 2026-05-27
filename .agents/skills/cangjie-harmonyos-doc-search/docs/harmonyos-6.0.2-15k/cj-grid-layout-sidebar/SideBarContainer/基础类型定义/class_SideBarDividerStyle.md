### class SideBarDividerStyle

```cangjie
public class SideBarDividerStyle {
    public let strokeWidth: Length
    public let color: ?ResourceColor
    public let startMargin: Length
    public let endMargin: Length
    public init(strokeWidth!: Length, color!: ?ResourceColor = Option<ResourceColor>.None,
        startMargin!: Length = 0.vp, endMargin!: Length = 0.vp)
}
```

**功能：** SideBar分割线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

> **说明：**
>
> 针对侧边栏内容区设置[通用属性宽高](../../source_zh_cn/arkui-cj/cj-universal-attribute-size.md)时，宽高都不生效，默认占满SideBarContainer的剩余空间。
> 当showSideBar属性未设置时，依据组件大小进行自动显示：
>
> - 小于minSideBarWidth + minContentWidth：默认不显示侧边栏。
> - 大于等于minSideBarWidth + minContentWidth：默认显示侧边栏。

#### let color

```cangjie
public let color: ?ResourceColor
```

**功能：** 分割线的颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let endMargin

```cangjie
public let endMargin: Length
```

**功能：** 分割线与侧边栏底端的距离。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let startMargin

```cangjie
public let startMargin: Length
```

**功能：** 分割线与侧边栏顶端的距离。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let strokeWidth

```cangjie
public let strokeWidth: Length
```

**功能：** 分割线的线宽。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Length, ?ResourceColor, Length, Length)

```cangjie
public init(strokeWidth!: Length, color!: ?ResourceColor = Option<ResourceColor>.None,
    startMargin!: Length = 0.vp, endMargin!: Length = 0.vp)
```

**功能：** 构造SideBarDividerStyle对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 分割线的线宽。<br>初始值：1.vp。|
|color|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Option\<ResourceColor>.None| **命名参数。** 分割线的颜色。<br>初始值：0x000000。|
|startMargin|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 分割线与侧边栏顶端的距离。|
|endMargin|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 分割线与侧边栏底端的距离。|