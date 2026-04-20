## class AlertDialogButtonOptions

```cangjie
public class AlertDialogButtonOptions <: AlertDialogButtonBaseOptions {
    public var primary: ?Bool
    public init(
        enabled!: ?Bool = None,
        defaultFocus!: ?Bool = None,
        style!: ?DialogButtonStyle = None,
        value!: ?ResourceStr,
        fontColor!: ?ResourceColor = None,
        backgroundColor!: ?ResourceColor = None,
        action!: ?VoidCallback,
        primary!: ?Bool = None
    )
}
```

**功能：** 定义警告弹窗中的按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [AlertDialogButtonBaseOptions](#class-alertdialogbuttonbaseoptions)

### var primary

```cangjie
public var primary: ?Bool
```

**功能：** 在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。在defaultFocus为true时不生效。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Bool, ?Bool, ?DialogButtonStyle, ?ResourceStr, ?ResourceColor, ?ResourceColor, ?VoidCallback, ?Bool)

```cangjie
public init(
    enabled!: ?Bool = None,
    defaultFocus!: ?Bool = None,
    style!: ?DialogButtonStyle = None,
    value!: ?ResourceStr,
    fontColor!: ?ResourceColor = None,
    backgroundColor!: ?ResourceColor = None,
    action!: ?VoidCallback,
    primary!: ?Bool = None
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
|primary|?Bool|否|None| **命名参数。** 在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。在defaultFocus为true时不生效。初始值: false |