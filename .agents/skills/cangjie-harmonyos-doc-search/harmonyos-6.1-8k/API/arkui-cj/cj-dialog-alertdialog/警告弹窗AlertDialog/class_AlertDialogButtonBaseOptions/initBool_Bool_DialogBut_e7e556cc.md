### init(?Bool, ?Bool, ?DialogButtonStyle, ?ResourceStr, ?ResourceColor, ?ResourceColor, ?VoidCallback)

```cangjie
public init(
    enabled!: ?Bool = None,
    defaultFocus!: ?Bool = None,
    style!: ?DialogButtonStyle = None,
    value!: ?ResourceStr,
    fontColor!: ?ResourceColor = None,
    backgroundColor!: ?ResourceColor = None,
    action!: ?VoidCallback
)
```

**功能：** 定义警告弹窗中的按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|?Bool|否|None| **命名参数。** 点击Button是否响应。初始值: true |
|defaultFocus|?Bool|否|None| **命名参数。** 设置Button是否是默认焦点。初始值: false |
|style|?[DialogButtonStyle](./cj-common-types.md#enum-dialogbuttonstyle)|否|None| **命名参数。** 设置Button的风格样式。初始值: DialogButtonStyle.Default |
|value|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-| **命名参数。** Button的文本内容。 |
|fontColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None| **命名参数。** Button的文本颜色。 |
|backgroundColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None| **命名参数。** Button背景颜色。 |
|action|?[VoidCallback](./cj-common-types.md#type-voidcallback)|是|-| **命名参数。** Button选中时的回调。初始值: {=>} |