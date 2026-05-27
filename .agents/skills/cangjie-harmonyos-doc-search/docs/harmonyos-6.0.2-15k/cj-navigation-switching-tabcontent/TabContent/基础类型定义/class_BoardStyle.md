### class BoardStyle

```cangjie
public class BoardStyle {
    public let borderRadius: Length
    public BoardStyle(
        borderRadius!: Length = 8.0.vp
    )
}
```

**功能：** 背板风格对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let borderRadius

```cangjie
public let borderRadius: Length
```

**功能：** 背板的圆角半径（不支持百分比设置）。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### BoardStyle(Length)

```cangjie
public BoardStyle(
    borderRadius!: Length = 8.0.vp
)
```

**功能：** 构造一个BoardStyle对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|borderRadius|[Length](cj-common-types.md#interface-length)|否|8.0.vp| **命名参数。** 背板的圆角半径（不支持百分比设置）。<br> 单位：vp <br> 取值范围：[0, +∞)。|