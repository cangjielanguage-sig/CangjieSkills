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
|value|[LineBreakStrategy](./cj-common-types.md#enum-linebreakstrategy)|是|-|文本的折行规则。<br>初始值：LineBreakStrategy.GREEDY。|

### func lineHeight(Length)

```cangjie
public func lineHeight(value: Length): This
```

**功能：** 设置文本的文本行高。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|文本的文本行高。设置值不大于0时，不限制文本行高，自适应字体大小，Length为Int64、Float64类型时，使用fp单位。|

### func lineSpacing(Length)

```cangjie
public func lineSpacing(value: Length): This
```

**功能：** 设置文本的行间距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|文本的行间距。设置值不大于0时，取初始值0。<br>初始值：0。|

### func maxFontSize(Length)

```cangjie
public func maxFontSize(value: Length): This
```

**功能：** 设置文本最大显示字号。

> **说明：**
>
> - 需配合[minFontSize](#func-minfontsizelength)以及[maxLines](#func-maxlinesint32)或布局大小限制使用，单独设置不生效。
> - 自适应字号生效时，fontSize设置不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|文本最大显示字号。单位：fp。|

### func maxLength(UInt32)

```cangjie
public func maxLength(value: UInt32): This
```

**功能：** 设置文本的最大输入字符数。

> **说明：**
>
> 默认不设置最大输入字符数限制。到达文本最大字符限制，将无法继续输入字符，同时边框变为红色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|UInt32|是|-|文本的最大输入字符数。|

### func maxLines(Int32)

```cangjie
public func maxLines(value: Int32): This
```

**功能：** 设置文本可显示的最大行数。

> **说明：**
>
> 配置textOverflow一起使用时，maxlines为可显示行数，超出截断；未配置textOverflow时，内联模式获焦状态下内容超出maxlines时，文本可滚动显示，内联模式非获焦状态下不生效maxlines，非内联模式按行截断。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|内联输入风格编辑态时文本可显示的最大行数。<br>初始值：3。<br/>非内联模式下，默认值为+∞，不限制最大行数。取值范围：(0, +∞)|