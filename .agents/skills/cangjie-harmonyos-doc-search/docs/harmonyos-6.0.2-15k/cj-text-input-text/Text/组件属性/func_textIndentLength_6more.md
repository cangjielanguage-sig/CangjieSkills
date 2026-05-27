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
|value|[Length](cj-common-types.md#interface-length)|是|-|首行文本缩进。<br>初始值：0。|

### func textOverflow(TextOverflow)

```cangjie
public func textOverflow(value: TextOverflow): This
```

**功能：** 设置文本超长时的显示方式。

> **说明：**
>
> - 文本截断是按字截断。例如，英文以单词为最小单位进行截断，若需要以字母为单位进行截断，可在字母间添加零宽空格：\u200B。从API version 11开始，建议优先组合wordBreak属性设置为WordBreak.BREAK_ALL方式实现字母为单位进行截断。
> - 当overflow设置为TextOverflow.None、TextOverflow.Clip、TextOverflow.Ellipsis时，需配合maxLines使用，单独设置不生效。设置TextOverflow.None与TextOverflow.Clip效果一样。
> - 当overflow设置为TextOverflow.MARQUEE时：
文本在一行内滚动显示。
设置[maxLines](#func-maxlinesint32)及[copyOption](#func-copyoptioncopyoptions)属性均不生效。
Text组件[clip](./cj-universal-attribute-shapclip.md#func-clipcircleshape)属性默认为true。
[textAlign](#func-textaligntextalign)属性的生效规则：当文本不可滚动时，textAlign属性生效；当文本可滚动时，textAlign属性不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextOverflow](cj-common-types.md#enum-textoverflow)|是|-|文本超长时的显示方式，需配合maxLines使用，单独设置不生效。<br>初始值：TextOverflow.Clip。|

### func textSelectable(TextSelectable)

```cangjie
public func textSelectable(value: TextSelectable): This
```

**功能：** 设置是否支持文本可选择、可获焦以及Touch后能否获取焦点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextSelectable](#enum-textselectable)|是|-|文本是否支持可选择、可获焦。<br>初始值：TextSelectableMode.SELECTABLE_UNFOCUSABLE。|

### func textShadow(ShadowOptions)

```cangjie
public func textShadow(value: ShadowOptions): This
```

**功能：** 设置文字阴影效果。

> **说明：**
>
> 不支持fill字段，不支持智能取色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ShadowOptions](#class-shadowoptions)|是|-|文字阴影效果。|

### func textShadow(Array\<ShadowOptions>)

```cangjie
public func textShadow(value: Array<ShadowOptions>): This
```

**功能：** 设置文字阴影效果。

> **说明：**
>
> 不支持fill字段，不支持智能取色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<[ShadowOptions](#class-shadowoptions)>|是|-|文字阴影效果。|

### func wordBreak(WordBreak)

```cangjie
public func wordBreak(value: WordBreak): This
```

**功能：** 设置断行规则。

> **说明：**
>
> WordBreak.BreakAll与{overflow: TextOverflow.Ellipsis}，[maxLines](#func-maxlinesint32)组合使用可实现英文单词按字母截断，超出部分以省略号显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[WordBreak](cj-common-types.md#enum-wordbreak)|是|-|断行规则。<br>初始值：WordBreak.BreakWord。|