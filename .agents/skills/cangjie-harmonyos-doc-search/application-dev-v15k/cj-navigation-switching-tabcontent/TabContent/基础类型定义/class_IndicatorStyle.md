### class IndicatorStyle

```cangjie
public class IndicatorStyle {
    public let color: UInt32
    public let height: Length
    public let width: Length
    public let borderRadius: Length
    public let marginTop: Length
    public IndicatorStyle(
        color!: ResourceColor = 0xFF007DFF,
        height!: Length = 2.0.vp,
        width!: Length = 0.0.vp,
        borderRadius!: Length = 0.0.vp,
        marginTop!: Length = 8.0.vp
    )
}
```

**功能：** 下划线风格对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let borderRadius

```cangjie
public let borderRadius: Length
```

**功能：** 下划线的圆角半径（不支持百分比设置）。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let color

```cangjie
public let color: UInt32
```

**功能：** 下划线的颜色和背板颜色。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let height

```cangjie
public let height: Length
```

**功能：** 下划线的高度（不支持百分比设置）。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let marginTop

```cangjie
public let marginTop: Length
```

**功能：** 下划线与文字的间距（不支持百分比设置）。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let width

```cangjie
public let width: Length
```

**功能：** 下划线的宽度（不支持百分比设置）。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### IndicatorStyle(ResourceColor, Length, Length, Length, Length)

```cangjie
public IndicatorStyle(
    color!: ResourceColor = 0xFF007DFF,
    height!: Length = 2.0.vp,
    width!: Length = 0.0.vp,
    borderRadius!: Length = 0.0.vp,
    marginTop!: Length = 8.0.vp
)
```

**功能：** 构造一个IndicatorStyle对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](cj-common-types.md#interface-resourcecolor)|否|0xFF007DFF| **命名参数。** 下划线的颜色和背板颜色。|
|height|[Length](cj-common-types.md#interface-length)|否|2.0.vp| **命名参数。** 下划线的高度（不支持百分比设置）。<br> 单位：vp <br> 取值范围：(0, +∞)。|
|width|[Length](cj-common-types.md#interface-length)|否|0.0.vp| **命名参数。** 下划线的宽度（不支持百分比设置）。<br> 单位：vp <br> 取值范围：(0, +∞)。<br> **说明：** <br> 宽度设置为0时，按页签文本宽度显示。|
|borderRadius|[Length](cj-common-types.md#interface-length)|否|0.0.vp| **命名参数。** 下划线的圆角半径（不支持百分比设置）。<br> 单位：vp <br> 取值范围：(0, +∞)。|
|marginTop|[Length](cj-common-types.md#interface-length)|否|8.0.vp| **命名参数。** 下划线与文字的间距（不支持百分比设置）。<br> 单位：vp <br> 取值范围：(0, +∞)。|