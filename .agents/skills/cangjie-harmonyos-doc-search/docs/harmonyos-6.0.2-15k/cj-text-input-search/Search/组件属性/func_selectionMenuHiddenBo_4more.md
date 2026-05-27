### func selectionMenuHidden(Bool)

```cangjie
public func selectionMenuHidden(value: Bool): This
```

**功能：** 设置是否不弹出系统文本选择菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否不弹出系统文本选择菜单。<br/>设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，不弹出系统文本选择菜单。<br/>设置为false时，弹出系统文本选择菜单。<br>初始值：false。|

### func textAlign(TextAlign)

```cangjie
public func textAlign(value: TextAlign): This
```

**功能：** 设置文本在搜索框中的对齐方式。目前支持的对齐方式有：[Start](./cj-common-types.md#enum-textalign)、[Center](./cj-common-types.md#enum-textalign)、[End](./cj-common-types.md#enum-textalign)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextAlign](./cj-common-types.md#enum-textalign)|是|-|文本在搜索框中的对齐方式。<br>初始值：TextAlign.Start。|

### func textFont(Length, FontWeight, FontStyle, String)

```cangjie
public func textFont(
    size!: Length = DEFAULT_SIZE.fp,
    weight!: FontWeight = FontWeight.W400,
    style!: FontStyle = FontStyle.Normal,
    family!: String = ""
): This
```

**功能：** 设置搜索框内输入文本样式，包括字体大小，字体粗细，字体族，字体风格。目前仅支持默认字体族。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|DEFAULT_SIZE.fp| **命名参数。** 文本尺寸。Length为Int64、Float64类型时，使用fp单位。支持设置百分比字符串。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.W400| **命名参数。** 输入字体的目标粗细。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 输入字体的目标样式。|
|family|String|否|""| **命名参数。** 输入字体的样式族。|

### func textIndent(Length)

```cangjie
public func textIndent(value: Length): This
```

**功能：** 设置首行文本缩进。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|首行文本缩进。<br>初始值：0。|