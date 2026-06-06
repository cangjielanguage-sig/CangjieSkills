### func letterSpacing(Length)

```cangjie
public func letterSpacing(value: Length): This
```

**功能：** 设置文本字符间距。

> **说明：**
>
> - 设置该值为百分比时，按默认值显示。
> - 设置该值为0时，按默认值显示。
> - 当取值为负值时，文字会发生压缩，负值过小时会将组件内容区大小压缩为0，导致无内容显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|文本字符间距。|

### func lineHeight(Length)

```cangjie
public func lineHeight(value: Length): This
```

**功能：** 设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|文本的文本行高。|

### func maxFontSize(Length)

```cangjie
public func maxFontSize(value: Length): This
```

**功能：** 设置文本最大显示字号。

> **说明：**
>
> 需配合[minFontSize](#func-minfontsizelength)以及布局大小限制使用，单独设置不生效。自适应字号生效时，fontSize设置不生效。

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

**功能：** 设置文本的最大输入字符数。默认不设置最大输入字符数限制。到达文本最大字符限制，将无法继续输入字符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|UInt32|是|-|文本的最大输入字符数。|

### func minFontSize(Length)

```cangjie
public func minFontSize(value: Length): This
```

**功能：** 设置文本最小显示字号。

> **说明：**
>
> 需配合[maxFontSize](#func-maxfontsizelength)以及布局大小限制使用，单独设置不生效。自适应字号生效时，fontSize设置不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|文本最小显示字号。单位：fp。|

### func placeholderColor(ResourceColor)

```cangjie
public func placeholderColor(color: ResourceColor): This
```

**功能：** 设置placeholder文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|目标颜色。<br>初始值：0x99000000。|