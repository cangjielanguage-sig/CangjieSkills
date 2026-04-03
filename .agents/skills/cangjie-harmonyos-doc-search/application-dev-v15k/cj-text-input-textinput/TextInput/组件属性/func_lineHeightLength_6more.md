### func lineHeight(Length)

```cangjie
public func lineHeight(value: Length): This
```

**功能：** 设置文本的文本行高。

> **说明：**
>
> 设置值不大于0时，不限制文本行高，自适应字体大。Length为Int64、Float64类型时，单位为fp。

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
> - 需配合[minFontSize](#func-minfontsizelength)以及[maxLines](#func-maxlinesint32)(组件设置为内联输入风格且编辑态时使用)或布局大小限制使用，单独设置不生效。
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

**功能：** 设置内联输入风格编辑态时文本可显示的最大行数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|内联输入风格编辑态时文本可显示的最大行数。<br>初始值：3。<br>取值范围：(0, +∞)。|

### func minFontSize(Length)

```cangjie
public func minFontSize(value: Length): This
```

**功能：** 设置文本最小显示字号。

> **说明：**
>
> - 需配合[maxFontSize](#func-maxfontsizelength)以及[maxLines](#func-maxlinesint32)(组件设置为内联输入风格且编辑态时使用)或布局大小限制使用，
> - 单独设置不生效。自适应字号生效时，fontSize设置不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|文本最大显示字号。单位：fp。|

### func passwordIcon(String, String)

```cangjie
public func passwordIcon(onIconSrc!: String = "", offIconSrc!: String = ""): This
```

**功能：** 设置当密码输入模式时，输入框末尾的图标。

> **说明：**
>
> - 支持jpg、png、bmp、heic和webp类型的图片格式。
> - 该图标的固定尺寸为24vp，若引用的图标过大或过小，均显示为固定尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onIconSrc|String|否|""| **命名参数。** 密码输入模式时，能够切换密码隐藏的显示状态的图标。默认为系统提供的密码图标。string格式可用于加载网络图片和本地图片。|
|offIconSrc|String|否|""| **命名参数。** 密码输入模式时，能够切换密码显示的隐藏状态的图标。默认为系统提供的密码图标。string格式可用于加载网络图片和本地图片。|