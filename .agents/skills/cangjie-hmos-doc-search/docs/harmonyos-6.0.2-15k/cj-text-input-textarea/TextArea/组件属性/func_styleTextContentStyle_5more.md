### func style(TextContentStyle)

```cangjie
public func style(value: TextContentStyle): This
```

**功能：** 设置文本框多态样式，内联输入风格只支持TextAreaType.Normal类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextContentStyle](./cj-common-types.md#enum-textcontentstyle)|是|-|文本框多态样式。<br>初始值：TextContentStyle.DEFAULT。|

### func textAlign(TextAlign)

```cangjie
public func textAlign(value: TextAlign): This
```

**功能：** 设置文本在输入框中的水平对齐方式。

> **说明：**
>
> - 支持TextAlign.Start、TextAlign.Center和TextAlign.End。
> - 可通过[align](./cj-universal-attribute-location.md#func-alignalignment)属性控制文本段落在垂直方向上的位置，此组件中不可通过align属性控制文本段落在水平方向上的位置，即align属性中Alignment.TopStart、Alignment.Top、Alignment.TopEnd效果相同，控制内容在顶部，Alignment.Start、Alignment.Center、Alignment.End效果相同，控制内容垂直居中，Alignment.BottomStart、Alignment.Bottom、Alignment.BottomEnd效果相同，控制内容在底部。
> - 当textAlign属性设置为TextAlign.JUSTIFY时，最后一行文本不参与两端对齐，为水平对齐首部效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextAlign](./cj-common-types.md#enum-textalign)|是|-|文本在输入框中的水平对齐方式。仅支持TextAlign.Start、TextAlign.Center和TextAlign.End。<br>初始值：TextAlign.Start。|

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

### func textOverflow(TextOverflow)

```cangjie
public func textOverflow(value: TextOverflow): This
```

**功能：** 设置文本超长时的显示方式。

> **说明：**
>
> - 内联模式，主动配置textoverflow才会生效按maxline截断效果，不配置时，默认不截断。
> - 文本截断是按字截断。例如，英文以单词为最小单位进行截断，若需要以字母为单位进行截断，wordBreak属性可设置为WordBreak.BREAK_ALL。
> - 当overflow设置为TextOverflow.None、TextOverflow.Clip、TextOverflow.Ellipsis时，需配合maxLines使用，单独设置不生效。设置TextOverflow.None与TextOverflow.Clip效果一样。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextOverflow](./cj-common-types.md#enum-textoverflow)|是|-|文本超长时的显示方式。<br>初始值：TextOverflow.Clip。|

> **说明：**
>
> TextArea组件不支持设置TextOverflow.MARQUEE模式,当设置为TextOverflow.MARQUEE模式时 显示为TextOverflow.Clip。

### func wordBreak(WordBreak)

```cangjie
public func wordBreak(value: WordBreak): This
```

**功能：** 设置文本断行规则。该属性对placeholder文本无效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[WordBreak](./cj-common-types.md#enum-wordbreak)|是|-|文本断行规则。<br>初始值：WordBreak.BREAK_WORD。|