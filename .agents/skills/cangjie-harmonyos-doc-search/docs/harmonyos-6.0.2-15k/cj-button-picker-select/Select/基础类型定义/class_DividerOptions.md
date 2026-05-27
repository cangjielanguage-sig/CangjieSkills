### class DividerOptions

```cangjie
public class DividerOptions {
    public let strokeWidth: Length
    public let startMargin: Length
    public let endMargin: Length
    public let color: ResourceColor
    public init(strokeWidth!: Length, startMargin!: Length, endMargin!: Length, color!: ResourceColor)
}
```

**功能：** 设置分割线组件参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let color

```cangjie
public let color: ResourceColor
```

**功能：** 分割线的颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let endMargin

```cangjie
public let endMargin: Length
```

**功能：** 分割线与TextPicker侧边结束端的距离（默认单位vp），也可指定单位为px，不支持百分比设置。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let startMargin

```cangjie
public let startMargin: Length
```

**功能：** 分割线与TextPicker侧边起始端的距离（默认单位vp），也可指定单位为px，不支持百分比设置。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let strokeWidth

```cangjie
public let strokeWidth: Length
```

**功能：** 分割线的线宽（默认单位vp），也可指定单位为px，不支持百分比设置。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Length, Length, Length, ResourceColor)

```cangjie
public init(strokeWidth!: Length, startMargin!: Length, endMargin!: Length, color!: ResourceColor)
```

**功能：** 构造DividerOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 分割线的线宽（默认单位vp），也可指定单位为px，不支持百分比设置。取值范围：strokeWidth小于0取初始值，最大不得超过列高的一半。<br>初始值：2.0.px。|
|startMargin|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 分割线与TextPicker侧边起始端的距离（默认单位vp），也可指定单位为px，不支持百分比设置。取值范围：startMargin小于0无效，最大不得超过TextPicker列宽。<br>初始值：0。|
|endMargin|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 分割线与TextPicker侧边结束端的距离（默认单位vp），也可指定单位为px，不支持百分比设置。取值范围：startMargin小于0无效，最大不得超过TextPicker列宽。<br>初始值：0。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-| **命名参数。** 分割线的颜色。<br>初始值：0x33000000。|

**读写能力：** 可读写

**起始版本：** 19

#### init(Length, Length)

```cangjie
public init(dx: Length, dy: Length)
```

**功能：** 构造MenuOffset对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dx|[Length](./cj-common-types.md#interface-length)|是|-|水平方向偏移量。|
|dy|[Length](./cj-common-types.md#interface-length)|是|-|竖直方向偏移量。|