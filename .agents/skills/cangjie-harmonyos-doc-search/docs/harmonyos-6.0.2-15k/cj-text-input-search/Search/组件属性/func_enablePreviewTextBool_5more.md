### func enablePreviewText(Bool)

```cangjie
public func enablePreviewText(enable: Bool): This
```

**功能：** 设置是否开启输入预上屏。

> **说明：**
>
> 预上屏内容定义为文字暂存态，目前不支持文字拦截功能，因此不触发[onWillInsert](#func-onwillinsertfloat64-string---bool)、[onDidInsert](#func-ondidinsertfloat64-string---unit)、[onWillDelete](#func-onwilldeletefloat64-int32-string---bool)、[onDidDelete](#func-ondiddeletefloat64-int32-string---unit)回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enable|Bool|是|-|是否开启输入预上屏。<br>初始值：true。|

### func enterKeyType(EnterKeyType)

```cangjie
public func enterKeyType(value: EnterKeyType): This
```

**功能：** 设置输入法回车键类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[EnterKeyType](./cj-text-input-textinput.md#enum-enterkeytype)|是|-|输入法回车键类型。<br>初始值：EnterKeyType.Search。|

### func fontColor(ResourceColor)

```cangjie
public func fontColor(color: ResourceColor): This
```

**功能：** 设置输入文本的字体颜色。[文本通用属性](./cj-universal-attribute-textstyle.md)fontSize、fontStyle、fontWeight和fontFamily在[textFont](#func-textfontlength-fontweight-fontstyle-string)属性中设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|输入文本的字体颜色。<br>初始值：0xE5000000。|

### func fontFeature(String)

```cangjie
public func fontFeature(text: String): This
```

**功能：** 设置文字特性效果，比如数字等宽的特性。

> **说明：**
>
> - 格式为：normal | \<feature-tag-value>。
> - \<feature-tag-value>的格式为：\<string> [ \<integer> | on | off ]。
> - \<feature-tag-value>的个数可以有多个，中间用','隔开。
> - 例如，使用等宽数字的输入格式为："ss01" on。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|文字特性效果。|

> **说明：**
>
> - Font Feature当前支持的属性见 [fontFeature属性列表](./cj-text-input-text.md#func-fontfeaturestring)。
> - 设置 Font Feature 属性，Font Feature 是 OpenType 字体的高级排版能力，如支持连字、数字等宽等特性，一般用在自定义字体中，其能力需要字体本身支持。
> - 更多 Font Feature 能力介绍可参考 [https://www.w3.org/TR/css-fonts-3/#font-feature-settings-prop](https://www.w3.org/TR/css-fonts-3/#font-feature-settings-prop) 和 [https://sparanoid.com/lab/opentype-features/](https://sparanoid.com/lab/opentype-features/)

### func inputFilter(String, (String) -> Unit)

```cangjie
public func inputFilter(value!: String, error!: (String)-> Unit = { val => }): This
```

**功能：** 通过正则表达式设置输入过滤器。

> **说明：**
>
> - 匹配表达式的输入允许显示，不匹配的输入将被过滤。仅支持单个字符匹配，不支持字符串匹配。
> - 设置inputFilter且输入的字符不为空字符，会导致设置输入框类型(即type接口)附带的文本过滤效果失效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-| **命名参数。** 正则表达式。|
|error|(String)->Unit|否|{ val => }| **命名参数。** 正则匹配失败时，返回被过滤的内容。|