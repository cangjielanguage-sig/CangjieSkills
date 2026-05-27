### var value

```cangjie
public var value: String = ""
```

**功能：** 点击Button是否响应。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Bool, Bool, Option\<DialogButtonStyle>, String, Option\<Color>, Option\<Color>, () -> Unit)

```cangjie
public init(
    enabled!: Bool = true,
    defaultFocus!: Bool = false,
    style!: Option<DialogButtonStyle> = None,
    value!: String = "",
    fontColor!: Option<Color> = None,
    backgroundColor!: Option<Color> = None,
    action!: () -> Unit = {=>}
)
```

**功能：** 定义警告弹窗中的按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| enabled | Bool | 否 | true | **命名参数。**  点击Button是否响应。 |
| defaultFocus | Bool | 否 | false | **命名参数。**  设置Button是否是默认焦点。 |
| style | Option\<[DialogButtonStyle](./cj-common-types.md#enum-dialogbuttonstyle)>  | 否 | None | **命名参数。**  设置Button的风格样式。 |
| value | String | 否 | "" | **命名参数。**  Button的文本内容。 |
| fontColor | Option\<[Color](./cj-common-types.md#class-color)>  | 否 | None | **命名参数。**  Button的文本颜色。 |
| backgroundColor | Option\<[Color](./cj-common-types.md#class-color)>  | 否 | None | **命名参数。**  Button背景颜色。 |
| action | () -> Unit | 否 | { => } | **命名参数。**  Button选中时的回调。 |

#### init(Bool, Bool, Option\<DialogButtonStyle>, String, Option\<Color>, Option\<Color>, () -> Unit, Bool)

```cangjie
public init(
    enabled!: Bool = true,
    defaultFocus!: Bool = false,
    style!: Option<DialogButtonStyle> = None,
    value!: String = "",
    fontColor!: Option<Color> = None,
    backgroundColor!: Option<Color> = None,
    action!: () -> Unit = {=>},
    primary!: Bool
)
```

**功能：** 定义警告弹窗中的按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| enabled | Bool | 否 | true | **命名参数。**  点击Button是否响应。 |
| defaultFocus | Bool | 否 | false | **命名参数。**  设置Button是否是默认焦点。 |
| style | Option\<[DialogButtonStyle](./cj-common-types.md#enum-dialogbuttonstyle)>  | 否 | None | **命名参数。**  设置Button的风格样式。 |
| value | String | 否 | "" | **命名参数。**  Button的文本内容。 |
| fontColor | Option\<[Color](./cj-common-types.md#class-color)>  | 否 | None | **命名参数。**  Button的文本颜色。 |
| backgroundColor | Option\<[Color](./cj-common-types.md#class-color)>  | 否 | None | **命名参数。**  Button背景颜色。 |
| action | () -> Unit | 否 | { => } | **命名参数。**  Button选中时的回调。 |
| primary | Bool | 否 | true | **命名参数。**  在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。在defaultFocus为true时不生效。|