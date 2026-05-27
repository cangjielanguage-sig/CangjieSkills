### func fontSize(Length)

```cangjie
public func fontSize(value: Length): This
```

**功能：** 设置字体大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|字体大小。Length为Int64、Float64类型时，使用fp单位。不支持设置百分比字符串。<br>初始值：16.fp。|

### func fontStyle(FontStyle)

```cangjie
public func fontStyle(value: FontStyle): This
```

**功能：** 设置字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FontStyle](./cj-common-types.md#enum-fontstyle)|是|-|字体样式。<br>初始值：FontStyle.Normal。|

### func fontWeight(FontWeight)

```cangjie
public func fontWeight(value: FontWeight): This
```

**功能：** 设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FontWeight](./cj-common-types.md#enum-fontweight)|是|-|文本的字体粗细。<br>初始值：FontWeight.Normal。|

### func heightAdaptivePolicy(TextHeightAdaptivePolicy)

```cangjie
public func heightAdaptivePolicy(value: TextHeightAdaptivePolicy): This
```

**功能：** 设置文本自适应高度的方式。

> **说明：**
>
> - 当设置为TextHeightAdaptivePolicy.MAX_LINES_FIRST时，优先使用[maxLines](#func-maxlinesint32)属性来调整文本高度。如果使用[maxLines](#func-maxlinesint32)属性的布局大小超过了布局约束，则尝试在[minFontSize](#func-minfontsizelength)和[maxFontSize](#func-maxfontsizelength)的范围内缩小字体以显示更多文本。 组件设置为内联输入风格，编辑态与非编辑态存在字体大小不一致情况。
> - 当设置为TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST时，优先使用[minFontSize](#func-minfontsizelength)属性来调整文本高度。如果使用[minFontSize](#func-minfontsizelength)属性可以将文本布局在一行中，则尝试在[minFontSize](#func-minfontsizelength)和[maxFontSize](#func-maxfontsizelength)的范围内增大字体并使用最大可能的字体大小。
> - 当设置为TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST时，优先使用布局约束来调整文本高度。如果布局大小超过布局约束，则尝试在[minFontSize](#func-minfontsizelength)和[maxFontSize](#func-maxfontsizelength)的范围内缩小字体以满足布局约束。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextHeightAdaptivePolicy](./cj-common-types.md#enum-textheightadaptivepolicy)|是|-|文本自适应高度的方式。<br>初始值：TextHeightAdaptivePolicy.MAX_LINES_FIRST。|

### func inputFilter(String, (String) -> Unit)

```cangjie
public func inputFilter(value!: String, error!: (String) -> Unit = {val => }): This
```

**功能：** 设置通过正则表达式设置输入过滤器。

> **说明：**
>
> 匹配表达式的输入允许显示，不匹配的输入将被过滤。仅支持单个字符匹配，不支持字符串匹配。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-| **命名参数。** 正则表达式。|
|error|(String)->Unit|否|{ val => }| **命名参数。** 正则匹配失败时，返回被过滤的内容。|