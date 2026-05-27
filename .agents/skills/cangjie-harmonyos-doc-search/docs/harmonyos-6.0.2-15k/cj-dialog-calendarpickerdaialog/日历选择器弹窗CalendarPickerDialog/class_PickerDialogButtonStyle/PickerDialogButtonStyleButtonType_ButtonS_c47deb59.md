### PickerDialogButtonStyle(?ButtonType, ?ButtonStyleMode, ?ButtonRole, ?Length, ?ResourceColor, ?FontWeight, ?FontStyle, ?String, ?ResourceColor, ?BorderRadiuses, ?Bool)

```cangjie
public PickerDialogButtonStyle(
    public let `type`!: ?ButtonType = None,
    public let style!: ?ButtonStyleMode = None,
    public let role!: ?ButtonRole = None,
    public let fontSize!: ?Length = None,
    public let fontColor!: ?ResourceColor = None,
    public let fontWeight!: ?FontWeight = None,
    public let fontStyle!: ?FontStyle = None,
    public let fontFamily!: ?String = None,
    public let backgroundColor!: ?ResourceColor = None,
    public let borderRadius!: ?BorderRadiuses = None,
    public let primary!: ?Bool = None
)
```

**功能：** 设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键等。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|'`type`'|?[ButtonType](./cj-common-types.md#enum-buttontype)|否|None| **命名参数。** 按钮显示样式。|
|style|?[ButtonStyleMode](./cj-common-types.md#enum-buttonstylemode)|否|None| **命名参数。** 按钮的样式和重要程度。|
|role|?[ButtonRole](./cj-common-types.md#enum-buttonrole)|否|None| **命名参数。** Button组件的角色。|
|fontSize|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 文本显示字号。|
|fontColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None| **命名参数。** 文本显示颜色。|
|fontWeight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None| **命名参数。** 文本的字体粗细|
|fontStyle|?[FontStyle](./cj-common-types.md#enum-fontstyle)|否|None| **命名参数。** 文本的字体样式。|
|fontFamily|?String|否|None| **命名参数。** 文本字体家族|
|backgroundColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None| **命名参数。** 按钮背景色。|
|borderRadius|?[BorderRadiuses](./cj-common-types.md#class-borderradiuses)|否|None| **命名参数。** 圆角半径。|
|primary|?Bool|否|None| **命名参数。** 在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。|