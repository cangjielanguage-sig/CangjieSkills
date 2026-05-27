### func heightAdaptivePolicy(TextHeightAdaptivePolicy)

```cangjie
public func heightAdaptivePolicy(value: TextHeightAdaptivePolicy): This
```

**功能：** 组件设置为内联输入风格时，设置文本自适应高度的方式。

> **说明：**
>
> - 当设置为TextHeightAdaptivePolicy.MAX_LINES_FIRST时，优先使用[maxLines](#func-maxlinesint32)属性来调整文本高度。如果使用maxLines属性的布局大小超过了布局约束，则尝试在[minFontSize](#func-minfontsizelength)和[maxFontSize](#func-maxfontsizelength)的范围内缩小字体以显示更多文本。
> - 当设置为TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST时，优先使用[minFontSize](#func-minfontsizelength)属性来调整文本高度。如果使用[minFontSize](#func-minfontsizelength)属性可以将文本布局在一行中，则尝试在[minFontSize](#func-minfontsizelength)和[maxFontSize](#func-maxfontsizelength)的范围内增大字体并使用最大可能的字体大小。
> - 当设置为TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST时，与TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST效果一样。组件设置为非内联输入风格时，设置文本自适应高度(TextHeightAdaptivePolicy)的三种方式效果一样，即在[minFontSize](#func-minfontsizelength)和[maxFontSize](#func-maxfontsizelength)的范围内缩小字体以显示更多文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextHeightAdaptivePolicy](./cj-common-types.md#enum-textheightadaptivepolicy)|是|-|文本自适应高度的方式。<br>初始值：TextHeightAdaptivePolicy.MAX_LINES_FIRST。|

### func inputFilter(String, (String) -> Unit)

```cangjie
public func inputFilter(value!: String, error!: (String)-> Unit = { val => }): This
```

**功能：** 通过正则表达式设置输入过滤器。

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

### func letterSpacing(Length)

```cangjie
public func letterSpacing(value: Length): This
```

**功能：** 设置文本字符间距。

> **说明：**
>
> - 设置该值为百分比时，按默认值显示。设置该值为0时，按默认值显示。
> - 当取值为负值时，文字会发生压缩，负值过小时会将组件内容区大小压缩为0，导致无内容显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|文本字符间距。单位：fp。|

### func lineBreakStrategy(LineBreakStrategy)

```cangjie
public func lineBreakStrategy(strategy: LineBreakStrategy): This
```

**功能：** 设置折行规则。该属性在[wordBreak](#func-wordbreakwordbreak)不等于breakAll的时候生效，不支持连词符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strategy|[LineBreakStrategy](./cj-common-types.md#enum-linebreakstrategy)|是|-|文本的折行规则。仅设置内联模式时该属性生效。<br>初始值：LineBreakStrategy.GREEDY。|