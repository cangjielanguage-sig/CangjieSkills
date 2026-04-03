### class DividerStyle

```cangjie
public class DividerStyle {
    public var strokeWidth: ?Length
    public var color: ?ResourceColor
    public var startMargin: ?Length
    public var endMargin: ?Length
    public init(strokeWidth!: ?Length, color!: ?ResourceColor = None, startMargin!: ?Length = None,
        endMargin!: ?Length = None)
}
```

**功能：** SideBar分割线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

> **说明：**
>
> 针对侧边栏内容区设置[通用属性宽高](./cj-universal-attribute-size.md)时，宽高都不生效，默认占满SideBarContainer的剩余空间。
> 当showSideBar属性未设置时，依据组件大小进行自动显示：
>
> - 小于minSideBarWidth + minContentWidth：默认不显示侧边栏。
> - 大于等于minSideBarWidth + minContentWidth：默认显示侧边栏。

#### var strokeWidth

```cangjie
public var strokeWidth: ?Length
```

**功能：** 分割线的线宽。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var color

```cangjie
public var color: ?ResourceColor
```

**功能：** 分割线的颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var startMargin

```cangjie
public var startMargin: ?Length
```

**功能：** 分割线与侧边栏顶端的距离。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var endMargin

```cangjie
public var endMargin: ?Length
```

**功能：** 分割线与侧边栏底端的距离。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Length, ?ResourceColor, ?Length, ?Length)

```cangjie
public init(strokeWidth!: ?Length, color!: ?ResourceColor = None, startMargin!: ?Length = None,
    endMargin!: ?Length = None)
```

**功能：** 构造DividerStyle对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 分割线的线宽。<br>初始值：1.vp。|
|color|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。** 分割线的颜色。<br>初始值：0x08000000。|
|startMargin|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 分割线与侧边栏顶端的距离。<br>初始值：0.vp。|
|endMargin|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 分割线与侧边栏底端的距离。<br>初始值：0.vp。|