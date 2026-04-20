### class RichEditorTextStyle

```cangjie
public class RichEditorTextStyle {
    public var fontColor: ?ResourceColor
    public var fontSize: ?Length
    public var fontStyle: ?FontStyle
    public var fontWeight: ?FontWeight
    public var fontFamily: ?ResourceStr
    public var decoration: ?TextDecorationOptions
    public init(
        fontColor!: ?ResourceColor = None,
        fontSize!: ?Length = None,
        fontStyle!: ?FontStyle = None,
        fontWeight!: ?FontWeight = None,
        fontFamily!: ?ResourceStr = None,
        decoration!: ?TextDecorationOptions = None
    )
}
```

**功能：** 定义span文本样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fontColor

```cangjie
public var fontColor: ?ResourceColor
```

**功能：** 字体颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fontSize

```cangjie
public var fontSize: ?Length
```

**功能：** 字体大小。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fontStyle

```cangjie
public var fontStyle: ?FontStyle
```

**功能：** 字体样式。

**类型：** ?[FontStyle](./cj-common-types.md#enum-fontstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fontWeight

```cangjie
public var fontWeight: ?FontWeight
```

**功能：** 字体粗细。

**类型：** ?[FontWeight](./cj-common-types.md#enum-fontweight)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fontFamily

```cangjie
public var fontFamily: ?ResourceStr
```

**功能：** 字体族。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var decoration

```cangjie
public var decoration: ?TextDecorationOptions
```

**功能：** 字体装饰。

**类型：** ?[TextDecorationOptions](#class-textdecorationoptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?ResourceColor, ?Length, ?FontStyle, ?FontWeight, ?ResourceStr, ?TextDecorationOptions)

```cangjie
public init(
    fontColor!: ?ResourceColor = None,
    fontSize!: ?Length = None,
    fontStyle!: ?FontStyle = None,
    fontWeight!: ?FontWeight = None,
    fontFamily!: ?ResourceStr = None,
    decoration!: ?TextDecorationOptions = None
)
```

**功能：** RichEditorTextStyle构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fontColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。** 字体颜色。初始值：Color.Black。|
|fontSize|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 字体大小。初始值：16.vp。|
|fontStyle|?[FontStyle](./cj-common-types.md#enum-fontstyle)|否|None|**命名参数。** 字体样式。初始值：FontStyle.Normal。|
|fontWeight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None|**命名参数。** 字体粗细。初始值：FontWeight.Normal。|
|fontFamily|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 字体族。初始值：DEFAULT_FONT。|
|decoration|?[TextDecorationOptions](#class-textdecorationoptions)|否|None|**命名参数。** 字体装饰。初始值：TextDecorationOptions(decorationType: TextDecorationType.None, color: Color.Black)。|