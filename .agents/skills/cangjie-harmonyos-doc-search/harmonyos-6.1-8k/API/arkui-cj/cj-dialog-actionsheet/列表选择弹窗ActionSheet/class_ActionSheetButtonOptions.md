## class ActionSheetButtonOptions

```cangjie
public class ActionSheetButtonOptions {
    public var enabled: ?Bool
    public var defaultFocus: ?Bool
    public var style: ?DialogButtonStyle
    public var value: ?ResourceStr
    public var action: ?VoidCallback
    public init(
        enabled!: ?Bool = None,
        defaultFocus!: ?Bool = None,
        style!: ?DialogButtonStyle = None,
        value!: ?ResourceStr,
        action!: ?VoidCallback
    )
}
```

**功能：** 弹窗中按钮的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var action

```cangjie
public var action: ?VoidCallback
```

**功能：** Button选中时的回调。

**类型：** ?[VoidCallback](./cj-common-types.md#type-voidcallback)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var defaultFocus

```cangjie
public var defaultFocus: ?Bool
```

**功能：** 设置Button是否是默认焦点。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var enabled

```cangjie
public var enabled: ?Bool
```

**功能：** 点击Button是否响应。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var style

```cangjie
public var style: ?DialogButtonStyle
```

**功能：** 设置Button的风格样式。

**类型：** ?[DialogButtonStyle](./cj-common-types.md#enum-dialogbuttonstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var value

```cangjie
public var value: ?ResourceStr
```

**功能：** Button文本内容。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Bool, ?Bool, ?DialogButtonStyle, ?ResourceStr, ?VoidCallback)

```cangjie
public init(
    enabled!: ?Bool = None,
    defaultFocus!: ?Bool = None,
    style!: ?DialogButtonStyle = None,
    value!: ?ResourceStr,
    action!: ?VoidCallback
)
```

**功能：** ActionSheetButtonOptions类的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|?Bool|否|None|**命名参数。** 点击Button是否响应，true表示Button可以响应，false表示Button不可以响应。|
|defaultFocus|?Bool|否|None|**命名参数。** 设置Button是否是默认焦点，true表示Button是默认焦点，false表示Button不是默认焦点。|
|style|?[DialogButtonStyle](./cj-common-types.md#enum-dialogbuttonstyle)|否|None|**命名参数。** 设置Button的风格样式。 |
|value|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|**命名参数。** Button文本内容。|
|action|?[VoidCallback](./cj-common-types.md#type-voidcallback)|是|-|**命名参数。** Button选中时的回调。|