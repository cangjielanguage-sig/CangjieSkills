### class DividerStyle

```cangjie
public class DividerStyle {
    public let strokeWidth: Length
    public let color: ResourceColor
    public let startMargin: Length
    public let endMargin: Length
    public init(strokeWidth!: Length, color!: ResourceColor = Color(0X33182431), startMargin!: Length = 0.vp, endMargin!: Length = 0.vp
    )
}
```

**功能：** 分割线样式对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let color

```cangjie
public let color: ResourceColor
```

**功能：** 分割线的颜色。

**类型：** [ResourceColor](cj-common-types.md#interface-resourcecolor)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let endMargin

```cangjie
public let endMargin: Length
```

**功能：** 分割线与侧边栏底端的距离（不支持百分比设置）。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let startMargin

```cangjie
public let startMargin: Length
```

**功能：** 分割线与侧边栏顶端的距离（不支持百分比设置）。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let strokeWidth

```cangjie
public let strokeWidth: Length
```

**功能：** 分割线的线宽（不支持百分比设置）。初始值为0.vp。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Length, ResourceColor, Length, Length)

```cangjie
public init(strokeWidth!: Length, color!: ResourceColor = Color(0X33182431), startMargin!: Length = 0.vp, endMargin!: Length = 0.vp
)
```

**功能：** 构造一个DividerStyle对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|[Length](cj-common-types.md#interface-length)|是|-| **命名参数。** 分割线的线宽（不支持百分比设置）。<br> 初始值：0.0 <br> 单位：vp <br> 取值范围：[0, +∞)。|
|color|[ResourceColor](cj-common-types.md#interface-resourcecolor)|否|Color(0X33182431)| **命名参数。** 分割线的颜色。|
|startMargin|[Length](cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 分割线与侧边栏顶端的距离（不支持百分比设置）。<br> 初始值：0.0 <br> 单位：vp <br> 取值范围：[0, +∞)。|
|endMargin|[Length](cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 分割线与侧边栏底端的距离（不支持百分比设置）。<br>初始值：0.0<br>单位：vp<br>取值范围：[0, +∞)。|