### func selectionMenuHidden(Bool)

```cangjie
public func selectionMenuHidden(value: Bool): This
```

**功能：** 设置是否隐藏系统文本选择菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否不弹出系统文本选择菜单。<br/>设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，隐藏系统文本选择菜单。<br/>设置为false时，显示系统文本选择菜单。<br>初始值：false。|

### func setType(InputType)

```cangjie
public func setType(value: InputType): This
```

**功能：** 设置textInput的类型。InputType设置为Password后，设置placeholderColor不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[InputType](#enum-inputtype)|是|-|textInput 类型。<br>初始值：InputType.Normal。|

> **说明：**
>
> 密码填充服务需要特定的输入框类型。如何使用密码填充服务参考[快速适配](../../../Dev_Guide/security/Password_Auto_Fill_Service/cj-quick-match.md)。

### func showCounter(Bool, Float64, Bool)

```cangjie
public func showCounter(value: Bool, thresholdPercentage!: Float64 = 0.0, highlightBorder!: Bool = true): This
```

**功能：** 设置当通过thresholdPercentage和highlightBorder输入的字符数超过阈值时显示计数器。

> **说明：**
>
> - 参数value为true时，才能设置thresholdPercentage和highlightBorder，文本框开启计数下标功能，需要配合maxlength（设置最大字符限制）一起使用。<br>字符计数器显示的效果是当前输入字符数/最大可输入字符数。
> - 当输入字符数大于最大字符数乘百分比值时，显示字符计数器。如果用户设置计数器时不设置thresholdPercentage和highlightBorder，那么当前输入字符数达到最大字符数时，边框和计数器下标将变为红色。
> - 用户同时设置参数value为true和thresholdPercentage和highlightBorder，当thresholdPercentage数值在有效区间内，且输入字符数超过最大字符数时，边框和计数器下标将变为红色，框体抖动。
> - 内联模式和密码模式下字符计数器不显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否显示计数器。|
|thresholdPercentage|Float64|否|0.0| **命名参数。** thresholdPercentage是可输入字符数占最大字符限制的百分比值。字符计数器显示的样式为当前输入字符数/最大字符数。当输入字符数大于最大字符数乘百分比值时，显示字符计数器。thresholdPercentage值的有效值区间为[1, 100]，数值为小数时，向下取整，如果设置的值超出有效值区间内，不显示字符计数器。thresholdPercentage设置为0.0，显示字符计数器，但此参数不生效。|
|highlightBorder|Bool|否|true| **命名参数。** 如果用户设置计数器时不设置thresholdPercentage和highlightBorder，那么当前输入字符数达到最大字符数时，边框和计数器下标将变为红色。如果用户设置显示字符计数器同时thresholdPercentage参数数值在有效区间内，那么当输入字符数超过最大字符数时，边框和计数器下标将变成红色。如果此参数为true，则显示红色边框。计数器默认显示红色边框。|