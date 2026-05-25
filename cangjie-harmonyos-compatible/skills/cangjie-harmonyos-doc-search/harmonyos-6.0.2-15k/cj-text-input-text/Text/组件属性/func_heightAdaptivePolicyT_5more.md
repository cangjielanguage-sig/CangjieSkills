### func heightAdaptivePolicy(TextHeightAdaptivePolicy)

```cangjie
public func heightAdaptivePolicy(value: TextHeightAdaptivePolicy): This
```

**功能：** 设置文本自适应高度的方式。

> **说明：**
>
> - 当设置为TextHeightAdaptivePolicy.MAX_LINES_FIRST时，优先使用[maxLines](#func-maxlinesint32)属性来调整文本高度。如果使用maxLines属性的布局大小超过了布局约束，则尝试在[minFontSize](#func-minfontsizelength)和[maxFontSize](#func-maxfontsizelength)的范围内缩小字体以显示更多文本。
> - 当设置为TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST时，优先使用minFontSize属性来调整文本高度。如果使用minFontSize属性可以将文本布局在一行中，则尝试在minFontSize和maxFontSize的范围内增大字体并使用最大可能的字体大小。
> - 当设置为TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST时，优先使用布局约束来调整文本高度。如果布局大小超过布局约束，则尝试在minFontSize和maxFontSize的范围内缩小字体以满足布局约束。如果将字体大小缩小到minFontSize后，布局大小仍然超过布局约束，则删除超过布局约束的行。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextHeightAdaptivePolicy](cj-common-types.md#enum-textheightadaptivepolicy)|是|-|文本自适应高度的方式。<br>初始值：TextHeightAdaptivePolicy.MAX_LINES_FIRST。|

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
|value|[Length](cj-common-types.md#interface-length)|是|-|文本字符间距。单位：fp。|

### func lineBreakStrategy(LineBreakStrategy)

```cangjie
public func lineBreakStrategy(value: LineBreakStrategy): This
```

**功能：** 设置折行规则。

> **说明：**
>
> 该属性在[wordBreak](#func-wordbreakwordbreak)不等于BreakAll的时候生效，不支持连词符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[LineBreakStrategy](cj-common-types.md#enum-linebreakstrategy)|是|-|文本的折行规则。<br>初始值：LineBreakStrategy.GREEDY。|

### func lineHeight(Length)

```cangjie
public func lineHeight(value: Length): This
```

**功能：** 根据Length设置文本的文本行高。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|文本的文本行高，设置值不大于 0 时，不限制文本行高，自适应字体大小。|

### func lineSpacing(Length)

```cangjie
public func lineSpacing(value: Length): This
```

**功能：** 设置文本的行间距，设置值不大于0时，取默认值0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|文本的行间距。<br>初始值：0。|