#### PickerDialogButtonStyle(?ButtonType, ?ButtonStyleMode, ?ButtonRole, ?Length, ?ResourceColor, ?FontWeight, ?FontStyle, ?String, ?ResourceColor, ?BorderRadiuses, ?Bool)

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

**功能：** 构造PickerDialogButtonStyle对象，用于设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|?[ButtonType](./cj-button-picker-button.md#enum-buttontype)|否|None| **命名参数。** 按钮显示样式。|
|style|?[ButtonStyleMode](./cj-button-picker-button.md#enum-buttonstylemode)|否|None| **命名参数。** 按钮的样式和重要程度。|
|role|?[ButtonRole](./cj-button-picker-button.md#enum-buttonrole)|否|None| **命名参数。** Button组件的角色。|
|fontSize|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 文本显示字号。|
|fontColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None| **命名参数。** 文本显示颜色。|
|fontWeight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None| **命名参数。** 文本的字体粗细。<br>FontWeight类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。|
|fontStyle|?[FontStyle](./cj-common-types.md#enum-fontstyle)|否|None| **命名参数。** 文本的字体样式。|
|fontFamily|?String|否|None| **命名参数。** 文本字体列表。<br>初始字体'HarmonyOS Sans'，当前支持'HarmonyOS Sans'字体和注册自定义字体。|
|backgroundColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None| **命名参数。** 按钮背景色。|
|borderRadius|?[BorderRadiuses](./cj-common-types.md#class-borderradiuses)|否|None| **命名参数。** 圆角半径。|
|primary|?Bool|否|None| **命名参数。** 在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。|

**异常情形说明：**

|异常情形|对应结果|
|:---|:---|
|起始日期晚于结束日期，选中日期未设置。|起始日期、结束日期和选中日期都为默认值。|
|起始日期晚于结束日期，选中日期早于起始日期默认值。|起始日期、结束日期都为默认值，选中日期为起始日期默认值。|
|起始日期晚于结束日期，选中日期晚于结束日期默认值。|起始日期晚于结束日期，选中日期晚于结束日期默认值。|
|起始日期晚于结束日期，选中日期在起始日期与结束日期默认值范围内。|起始日期晚于结束日期，选中日期在起始日期与结束日期默认值范围内。|
|选中日期早于起始日期。|选中日期早于起始日期。|
|选中日期晚于结束日期。|选中日期晚于结束日期。|
|选中日期晚于结束日期。|选中日期为起始日期。|
|结束日期早于当前系统日期，选中日期未设置。|选中日期为结束日期。|
|日期格式不符合规范，如‘1999-13-32’。|取默认值。|
|起始日期或结束日期早于系统有效范围。|起始日期或结束日期取系统有效范围最早日期。|
|起始日期或结束日期晚于系统有效范围。|起始日期或结束日期取系统有效范围最晚日期。|

系统日期范围：1900-1-31 ~ 2100-12-31。

选中日期会在起始日期与结束日期异常处理完成后再进行异常情形判断处理。